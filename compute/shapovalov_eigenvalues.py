#!/usr/bin/env python3
r"""Compute Virasoro Shapovalov/Gram matrix eigenvalues by level.

This script builds the level-N Gram matrix on the Verma module basis
  L_{-\lambda_1} ... L_{-\lambda_k} |h>
indexed by partitions lambda of N with lambda_1 >= ... >= lambda_k >= 1.

It reports the smallest eigenvalue lambda_min(G_N) and the ratio
lambda_min(G_N) / p(N), where p(N) is the partition number.

The matrix elements are computed directly from the Virasoro commutator
  [L_m, L_n] = (m-n) L_{m+n} + (c/12) (m^3-m) delta_{m+n,0}
and the highest-weight conditions
  L_n |h> = 0  (n > 0),   L_0 |h> = h |h>.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
from typing import Iterable

import numpy as np


def parse_rational(text: str) -> Fraction:
    """Parse integers, fractions, or decimal strings into a Fraction."""
    return Fraction(text)


def partitions_of(n: int, max_part: int | None = None) -> list[tuple[int, ...]]:
    """Partitions of n in weakly decreasing order."""
    if n < 0:
        raise ValueError("partition level must be non-negative")
    if max_part is None or max_part > n:
        max_part = n
    if n == 0:
        return [()]
    parts: list[tuple[int, ...]] = []
    for first in range(max_part, 0, -1):
        for tail in partitions_of(n - first, first):
            parts.append((first,) + tail)
    return parts


def partition_number(n: int) -> int:
    """Euler partition number p(n)."""
    if n < 0:
        return 0
    counts = [0] * (n + 1)
    counts[0] = 1
    for k in range(1, n + 1):
        for m in range(k, n + 1):
            counts[m] += counts[m - k]
    return counts[n]


def make_expectation_evaluator(h: Fraction, c: Fraction):
    """Return a memoized highest-weight expectation evaluator."""

    @lru_cache(maxsize=None)
    def expectation(modes: tuple[int, ...]) -> Fraction:
        # We evaluate <h| L_{m_1} ... L_{m_r} |h>.
        if not modes:
            return Fraction(1, 1)
        if modes[0] < 0:
            return Fraction(0, 1)
        if modes[-1] > 0:
            return Fraction(0, 1)
        if modes[0] == 0:
            return h * expectation(modes[1:])
        if modes[-1] == 0:
            return h * expectation(modes[:-1])

        for i in range(len(modes) - 1):
            m = modes[i]
            n = modes[i + 1]
            if m > 0 and n <= 0:
                prefix = modes[:i]
                suffix = modes[i + 2 :]
                total = expectation(prefix + (n, m) + suffix)
                total += (m - n) * expectation(prefix + (m + n,) + suffix)
                if m + n == 0:
                    total += Fraction(m**3 - m, 12) * c * expectation(prefix + suffix)
                return total

        raise RuntimeError(f"unable to reduce mode string {modes}")

    return expectation


def gram_matrix(level: int, h: Fraction, c: Fraction) -> tuple[list[tuple[int, ...]], list[list[Fraction]]]:
    """Construct the level-N Virasoro Gram matrix."""
    basis = partitions_of(level)
    expectation = make_expectation_evaluator(h, c)
    matrix: list[list[Fraction]] = []
    for left in basis:
        row: list[Fraction] = []
        bra_modes = tuple(reversed(left))
        for right in basis:
            ket_modes = tuple(-part for part in right)
            row.append(expectation(bra_modes + ket_modes))
        matrix.append(row)
    return basis, matrix


def matrix_to_numpy(matrix: Iterable[Iterable[Fraction]]) -> np.ndarray:
    """Convert a rational Gram matrix to a float array for eigensolvers."""
    return np.array([[float(entry) for entry in row] for row in matrix], dtype=float)


def format_partition(partition: tuple[int, ...]) -> str:
    return "[" + ",".join(str(part) for part in partition) + "]"


def verify_reference_values() -> None:
    """Check the N=1 and N=2 sample values used in the manuscript task."""
    c = Fraction(25, 1)
    h = Fraction(2, 1)

    basis_1, gram_1 = gram_matrix(1, h, c)
    assert basis_1 == [(1,)]
    assert gram_1 == [[Fraction(4, 1)]]

    basis_2, gram_2 = gram_matrix(2, h, c)
    assert basis_2 == [(2,), (1, 1)]
    expected_2 = [
        [Fraction(41, 2), Fraction(12, 1)],
        [Fraction(12, 1), Fraction(40, 1)],
    ]
    assert gram_2 == expected_2

    eigenvalues_2 = np.linalg.eigvalsh(matrix_to_numpy(gram_2))
    assert abs(eigenvalues_2[0] - 14.78835390393377) < 1e-12


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--c", default="25", help="central charge c")
    parser.add_argument("--h", default="2", help="highest weight h")
    parser.add_argument("--max-level", type=int, default=8, help="largest level N to compute")
    parser.add_argument(
        "--show-level",
        type=int,
        action="append",
        default=[],
        help="print the exact Gram matrix and eigenvalues at this level",
    )
    args = parser.parse_args()

    c = parse_rational(args.c)
    h = parse_rational(args.h)

    if c == Fraction(25, 1) and h == Fraction(2, 1) and args.max_level >= 2:
        verify_reference_values()
        print("Reference checks passed for N=1 and N=2 at c=25, h=2.")
        print()

    print(f"Virasoro Gram spectrum at c={c}, h={h}")
    print("Basis convention: partitions in weakly decreasing order.")
    print()
    print(f"{'N':>2} {'p(N)':>5} {'lambda_min(G_N)':>18} {'lambda_max(G_N)':>18} {'lambda_min/p(N)':>18}")

    stored_results: dict[int, tuple[list[tuple[int, ...]], list[list[Fraction]], np.ndarray]] = {}

    for level in range(1, args.max_level + 1):
        basis, matrix = gram_matrix(level, h, c)
        eigenvalues = np.linalg.eigvalsh(matrix_to_numpy(matrix))
        stored_results[level] = (basis, matrix, eigenvalues)
        part_count = partition_number(level)
        lambda_min = eigenvalues[0]
        lambda_max = eigenvalues[-1]
        ratio = lambda_min / part_count
        print(f"{level:>2} {part_count:>5} {lambda_min:>18.12f} {lambda_max:>18.12f} {ratio:>18.12f}")

    for level in args.show_level:
        if level not in stored_results:
            continue
        basis, matrix, eigenvalues = stored_results[level]
        print()
        print(f"Level {level} basis:")
        print(", ".join(format_partition(partition) for partition in basis))
        print(f"Level {level} exact Gram matrix:")
        for row in matrix:
            print("  " + "  ".join(str(entry) for entry in row))
        print(f"Level {level} eigenvalues:")
        print("  " + ", ".join(f"{value:.12f}" for value in eigenvalues))


if __name__ == "__main__":
    main()
