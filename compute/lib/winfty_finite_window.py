"""Finite-window diagnostics for the Winfty endpoint.

The Winfty endpoint is a limit statement.  A finite spin cutoff can
check a finite Dunn rung; it contributes to the chain-level Einfty
endpoint only after the Yamada weight-window threshold and
inverse-system compatibility hypotheses are supplied.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations_with_replacement


@dataclass(frozen=True)
class WindowDiagnostic:
    """Finite-window status for a Winfty truncation."""

    spin_cutoff: int
    weight_max: int
    yamada_threshold: int
    max_two_slot_spin: int
    e_top_depth: int
    checks_stress_dunn_input: bool
    meets_yamada_threshold: bool
    proves_einfty_endpoint: bool
    two_slot_terms: tuple["TwoSlotTerm", ...]
    missing_two_slot_terms: tuple["TwoSlotTerm", ...]


@dataclass(frozen=True)
class TwoSlotTerm:
    """One binary OPE slot in the ordered bar differential."""

    left_spin: int
    right_spin: int
    required_spin_cutoff: int


def two_slot_required_spin(left_spin: int, right_spin: int) -> int:
    """Uniform two-slot bound: an (a,b) collision needs spin a+b-1."""

    if left_spin < 2 or right_spin < 2:
        raise ValueError("spin slots must be at least 2")
    return left_spin + right_spin - 1


def two_slot_window_terms(weight_max: int) -> tuple[TwoSlotTerm, ...]:
    """Enumerate two-slot OPE requirements in a bounded weight window."""

    if weight_max < 2:
        raise ValueError("weight_max must be at least 2 for W-algebra slots")
    return tuple(
        TwoSlotTerm(
            left_spin=left,
            right_spin=right,
            required_spin_cutoff=two_slot_required_spin(left, right),
        )
        for left, right in combinations_with_replacement(range(2, weight_max + 1), 2)
    )


def max_two_slot_spin_for_window(weight_max: int) -> int:
    """Largest spin cutoff demanded by the two-slot window arithmetic."""

    return max(term.required_spin_cutoff for term in two_slot_window_terms(weight_max))


def yamada_threshold(weight_max: int) -> int:
    """Uniform Yamada threshold N0(w_max) = 2*w_max - 1."""

    if weight_max < 1:
        raise ValueError("weight_max must be positive")
    if weight_max == 1:
        return 1
    return max_two_slot_spin_for_window(weight_max)


def finite_rung_e_top_depth(spin_cutoff: int) -> int:
    """A finite W_N spin cutoff through spin N gives E_{N+1}."""

    if spin_cutoff < 2:
        raise ValueError("spin_cutoff must be at least 2")
    return spin_cutoff + 1


def finite_window_diagnostic(spin_cutoff: int, weight_max: int) -> WindowDiagnostic:
    """Classify a finite Winfty window."""

    terms = two_slot_window_terms(weight_max)
    threshold = yamada_threshold(weight_max)
    meets_threshold = spin_cutoff >= threshold
    missing_terms = tuple(
        term for term in terms if term.required_spin_cutoff > spin_cutoff
    )
    return WindowDiagnostic(
        spin_cutoff=spin_cutoff,
        weight_max=weight_max,
        yamada_threshold=threshold,
        max_two_slot_spin=max_two_slot_spin_for_window(weight_max),
        e_top_depth=finite_rung_e_top_depth(spin_cutoff),
        checks_stress_dunn_input=spin_cutoff >= weight_max,
        meets_yamada_threshold=meets_threshold,
        proves_einfty_endpoint=False,
        two_slot_terms=terms,
        missing_two_slot_terms=missing_terms,
    )


def spin4_window_diagnostic() -> WindowDiagnostic:
    """The manuscript's spin <= 4 finite-window test."""

    return finite_window_diagnostic(spin_cutoff=4, weight_max=4)


def minimal_spin_cutoff_for_window(weight_max: int) -> int:
    """Smallest spin cutoff that meets the uniform Yamada threshold."""

    return yamada_threshold(weight_max)
