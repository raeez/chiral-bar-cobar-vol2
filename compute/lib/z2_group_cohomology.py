"""Exact normalized sign cochains for ``H^3(BZ/2; U(1))``.

This module checks only the finite group-cohomology normalization used
by the finite-orbifold BV obstruction.  It does not compute the local
BV anomaly of a lattice orbifold.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import prod
from typing import Iterable, Mapping

IDENTITY = 0
SIGMA = 1
Z2_ELEMENTS = (IDENTITY, SIGMA)


def z2_mul(a: int, b: int) -> int:
    """Multiplication in ``Z/2`` encoded additively."""
    if a not in Z2_ELEMENTS or b not in Z2_ELEMENTS:
        raise ValueError("Z/2 elements are encoded as 0 and 1")
    return (a + b) % 2


def all_tuples(length: int) -> tuple[tuple[int, ...], ...]:
    """All ``length``-tuples in ``(Z/2)^length``."""
    if length < 0:
        raise ValueError("tuple length must be non-negative")
    return tuple(product(Z2_ELEMENTS, repeat=length))


def is_degenerate(args: Iterable[int]) -> bool:
    """A normalized cochain is forced to be ``1`` on degenerate tuples."""
    values = tuple(args)
    if any(value not in Z2_ELEMENTS for value in values):
        raise ValueError("Z/2 elements are encoded as 0 and 1")
    return any(value == IDENTITY for value in values)


@dataclass(frozen=True)
class NormalizedSignCochain:
    """A normalized multiplicative cochain with values in ``{+1,-1}``."""

    degree: int
    values: Mapping[tuple[int, ...], int]

    def __post_init__(self) -> None:
        if self.degree < 1:
            raise ValueError("degree must be at least 1")
        normalized: dict[tuple[int, ...], int] = {}
        for key, value in self.values.items():
            if len(key) != self.degree:
                raise ValueError(f"key {key!r} has wrong degree")
            if is_degenerate(key):
                raise ValueError("normalized cochains omit degenerate keys")
            if value not in (-1, 1):
                raise ValueError("sign cochain values must be +1 or -1")
            normalized[tuple(key)] = value
        object.__setattr__(self, "values", normalized)

    def __call__(self, *args: int) -> int:
        if len(args) != self.degree:
            raise ValueError(f"expected {self.degree} inputs, got {len(args)}")
        if is_degenerate(args):
            return 1
        return self.values.get(tuple(args), 1)


def _inverse_sign(value: int) -> int:
    if value not in (-1, 1):
        raise ValueError("sign must be +1 or -1")
    return value


def multiplicative_coboundary_value(
    cochain: NormalizedSignCochain, args: tuple[int, ...]
) -> int:
    """Evaluate the standard multiplicative group-cohomology coboundary.

    For a normalized ``n``-cochain ``f`` with trivial group action,

    ``df(g_1,...,g_{n+1}) =
       f(g_2,...,g_{n+1})
       prod_i f(...,g_i g_{i+1},...)^{(-1)^i}
       f(g_1,...,g_n)^{(-1)^{n+1}}``.

    Values are signs, so inversion leaves the sign unchanged.
    """
    n = cochain.degree
    if len(args) != n + 1:
        raise ValueError(f"expected {n + 1} inputs, got {len(args)}")
    if any(arg not in Z2_ELEMENTS for arg in args):
        raise ValueError("Z/2 elements are encoded as 0 and 1")

    terms = [cochain(*args[1:])]
    for i in range(n):
        merged = args[:i] + (z2_mul(args[i], args[i + 1]),) + args[i + 2 :]
        term = cochain(*merged)
        terms.append(_inverse_sign(term) if (i + 1) % 2 else term)

    last = cochain(*args[:-1])
    terms.append(last if (n + 1) % 2 == 0 else _inverse_sign(last))
    return prod(terms)


def coboundary(cochain: NormalizedSignCochain) -> NormalizedSignCochain:
    """Return the normalized coboundary cochain."""
    next_degree = cochain.degree + 1
    values = {
        args: multiplicative_coboundary_value(cochain, args)
        for args in all_tuples(next_degree)
        if not is_degenerate(args)
    }
    return NormalizedSignCochain(next_degree, values)


def is_cocycle(cochain: NormalizedSignCochain) -> bool:
    """Whether the normalized coboundary is identically ``1``."""
    return all(
        multiplicative_coboundary_value(cochain, args) == 1
        for args in all_tuples(cochain.degree + 1)
    )


def normalized_z2_3_cocycle(triple_sign: int) -> NormalizedSignCochain:
    """The normalized ``3``-cochain determined by ``alpha(s,s,s)``."""
    if triple_sign not in (-1, 1):
        raise ValueError("triple_sign must be +1 or -1")
    return NormalizedSignCochain(3, {(SIGMA, SIGMA, SIGMA): triple_sign})


def h3_bz2_u1_class_from_triple_sign(triple_sign: int) -> int:
    """Return ``0`` for the trivial class and ``1`` for the generator."""
    if triple_sign == 1:
        return 0
    if triple_sign == -1:
        return 1
    raise ValueError("triple_sign must be +1 or -1")


def normalized_h3_bz2_u1_classes() -> dict[int, int]:
    """The two normalized sign representatives of ``H^3(BZ/2; U(1))``."""
    return {
        sign: h3_bz2_u1_class_from_triple_sign(sign)
        for sign in (1, -1)
    }
