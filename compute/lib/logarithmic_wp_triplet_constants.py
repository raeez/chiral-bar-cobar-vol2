"""Structural constants and obstruction checks for logarithmic triplet W(p)."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


def _check_p(p: int) -> None:
    if p < 2:
        raise ValueError(f"triplet parameter p must be >= 2, got {p}")


def triplet_central_charge(p: int) -> Fraction:
    """Return c(p) = 1 - 6(p - 1)^2 / p."""
    _check_p(p)
    return Fraction(1) - Fraction(6 * (p - 1) ** 2, p)


def triplet_w_weight(p: int) -> int:
    """Return the conformal weight of each triplet field W^a."""
    _check_p(p)
    return 2 * p - 1


def triplet_generator_degrees(p: int) -> tuple[int, int, int, int]:
    """Return the C2 degrees of T, W^+, W^0, W^-."""
    h = triplet_w_weight(p)
    return (2, h, h, h)


def zhu_dimension(p: int) -> int:
    """Return dim A(W(p)) = 2p."""
    _check_p(p)
    return 2 * p


def ww_ope_pole_order(p: int) -> int:
    """Return the highest W-W OPE pole order 2(2p - 1)."""
    return 2 * triplet_w_weight(p)


def ww_bar_pole_order(p: int) -> int:
    """Return the dlog-absorbed W-W bar pole order."""
    return ww_ope_pole_order(p) - 1


def triplet_field_multiplicity() -> int:
    """Return the sl2-triplet multiplicity of W^a fields."""
    return 3


def triplet_pair_multiplicity() -> int:
    """Return the ordered W^a-W^b pair multiplicity."""
    return triplet_field_multiplicity() ** 2


def tt_transition_weight() -> int:
    """Return the Virasoro Riccati transition weight beta_TT."""
    return 6


def tw_transition_weight(p: int) -> int:
    """Return the finite pole-envelope T-W transition weight."""
    return triplet_field_multiplicity() * triplet_w_weight(p)


def ww_transition_weight(p: int) -> int:
    """Return the finite pole-envelope W-W transition weight."""
    return triplet_pair_multiplicity() * ww_bar_pole_order(p)


def tt_radius_candidate(p: int) -> Fraction:
    """Return the proved Virasoro-subchannel radius |c(p)| / 6."""
    return abs(triplet_central_charge(p)) / 6


def tw_radius_candidate(p: int) -> Fraction:
    """Return the formal TW-channel radius |c(p)| / (6(2p - 1))."""
    return abs(triplet_central_charge(p)) / (6 * triplet_w_weight(p))


def ww_radius_candidate(p: int) -> Fraction:
    """Return the formal WW-channel radius |c(p)| / (4p - 3)."""
    return abs(triplet_central_charge(p)) / ww_bar_pole_order(p)


def formal_radius_bottleneck(p: int) -> str:
    """Return the smallest formal channel radius among TT, TW, WW."""
    radii = {
        "TT": tt_radius_candidate(p),
        "TW": tw_radius_candidate(p),
        "WW": ww_radius_candidate(p),
    }
    return min(radii, key=radii.__getitem__)


def free_c2_hilbert_coefficients(
    generator_degrees: Iterable[int], max_weight: int
) -> list[int]:
    """Coefficients of the C2 polynomial algebra for free strong generation."""
    coeffs = [0] * (max_weight + 1)
    coeffs[0] = 1
    for degree in generator_degrees:
        if degree <= 0:
            raise ValueError(f"generator degree must be positive, got {degree}")
        for weight in range(degree, max_weight + 1):
            coeffs[weight] += coeffs[weight - degree]
    return coeffs


def finite_free_strong_generation_forbidden_by_c2_cofinite(
    p: int, witness_powers: int = 16
) -> bool:
    """Return a finite Hilbert-series witness for the C2 obstruction."""
    _check_p(p)
    coeffs = free_c2_hilbert_coefficients(
        triplet_generator_degrees(p), max_weight=2 * witness_powers
    )
    return all(coeffs[2 * n] > 0 for n in range(witness_powers + 1))


@dataclass(frozen=True)
class TripletConstants:
    p: int
    central_charge: Fraction
    w_weight: int
    zhu_dimension: int
    ww_ope_pole_order: int
    ww_bar_pole_order: int
    rho_tt: Fraction
    rho_tw: Fraction
    rho_ww: Fraction
    formal_bottleneck: str
    tt_transition_weight: int
    tw_transition_weight: int
    ww_transition_weight: int


def triplet_constants(p: int) -> TripletConstants:
    """Collect the structural constants used by the W(p) tempering tests."""
    return TripletConstants(
        p=p,
        central_charge=triplet_central_charge(p),
        w_weight=triplet_w_weight(p),
        zhu_dimension=zhu_dimension(p),
        ww_ope_pole_order=ww_ope_pole_order(p),
        ww_bar_pole_order=ww_bar_pole_order(p),
        rho_tt=tt_radius_candidate(p),
        rho_tw=tw_radius_candidate(p),
        rho_ww=ww_radius_candidate(p),
        formal_bottleneck=formal_radius_bottleneck(p),
        tt_transition_weight=tt_transition_weight(),
        tw_transition_weight=tw_transition_weight(p),
        ww_transition_weight=ww_transition_weight(p),
    )
