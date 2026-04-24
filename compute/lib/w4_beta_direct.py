"""Direct W4 finite-rank attack on the harmonic beta law.

This module deliberately separates two statements.

Computed finite-rank evidence:
    In Zamolodchikov normalization, the W4 spin lanes have top OPE
    coefficients c/2, c/3, c/4. The corresponding lane contribution
    test gives 6 + 4 + 3 = 13.

Not computed here:
    The shadow-tower Riccati coefficient beta_4.  To promote the lane
    computation to beta_4, one still needs the bridge from the full W4
    OPE/Miura data to the leading Laurent coefficient A_5(W4) in the
    shadow master equation.

The point of the module is therefore adversarial: it records that the
spin-lane calculus singles out the harmonic value 13, but does not give
an independent proof of beta_4.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Optional


@dataclass(frozen=True)
class SpinLane:
    """One principal W4 spin lane in Zamolodchikov normalization."""

    spin: int
    top_ope_norm_over_c: Fraction
    beta_lane_contribution: Fraction
    source: str


@dataclass(frozen=True)
class W4AttackReport:
    """Verdict of the direct W4 attack."""

    lane_sum: Fraction
    triangular_candidate: Fraction
    quadratic_candidate: Fraction
    harmonic_candidate: Fraction
    required_bridge_ratio: Fraction
    conditional_A4_from_scaling: Fraction
    required_A5_from_bridge: Fraction
    observed_full_miura_A5: Optional[Fraction]
    proves_beta4: bool
    missing_bridge: str


@dataclass(frozen=True)
class RiccatiBridgeRequirement:
    """Exact data needed to turn the W4 lane witness into beta_4."""

    beta_candidate: Fraction
    required_ratio: Fraction
    conditional_A4_from_scaling: Fraction
    required_A5: Fraction
    observed_full_miura_A5: Optional[Fraction]
    bridge_verified: bool
    obstruction: str


def w4_spin_lanes() -> Dict[int, SpinLane]:
    """Return the three W4 spin lanes T, W3, W4.

    The top OPE norm column is the coefficient of c in
    W^(s)(z) W^(s)(w) at pole order 2s.
    """

    return {
        2: SpinLane(
            spin=2,
            top_ope_norm_over_c=Fraction(1, 2),
            beta_lane_contribution=Fraction(6),
            source="Virasoro stress-tensor top pole c/2",
        ),
        3: SpinLane(
            spin=3,
            top_ope_norm_over_c=Fraction(1, 3),
            beta_lane_contribution=Fraction(4),
            source="Fateev-Lukyanov W3 top pole c/3",
        ),
        4: SpinLane(
            spin=4,
            top_ope_norm_over_c=Fraction(1, 4),
            beta_lane_contribution=Fraction(3),
            source="W4 primary top pole c/4",
        ),
    }


def w4_kappa_over_c_from_lanes() -> Fraction:
    """Trace of the W4 diagonal kappa matrix divided by c."""

    return sum(lane.top_ope_norm_over_c for lane in w4_spin_lanes().values())


def w4_kappa_ratio_to_virasoro() -> Fraction:
    """kappa(W4)/kappa(Vir) computed from direct spin-lane norms."""

    vir_kappa_over_c = Fraction(1, 2)
    return w4_kappa_over_c_from_lanes() / vir_kappa_over_c


def w4_lane_sum_beta_candidate() -> Fraction:
    """The W4 spin-lane candidate beta value: 6 + 4 + 3 = 13."""

    return sum(lane.beta_lane_contribution for lane in w4_spin_lanes().values())


def triangular_beta4_candidate() -> Fraction:
    """Old triangular interpolation at N=4."""

    return Fraction((4 + 1) * (4 + 2), 2)


def quadratic_beta4_candidate() -> Fraction:
    """Old quadratic interpolation at N=4."""

    return Fraction(4 * 4 - 4 + 4)


def harmonic_beta4_candidate() -> Fraction:
    """Harmonic beta value at N=4."""

    return Fraction(13)


def w4_required_riccati_ratio(beta_candidate: Fraction = Fraction(13)) -> Fraction:
    """Required A_5/A_4 ratio for a proposed beta_4 value.

    The Riccati convention is A_5/A_4 = -beta_4 * 4/5.
    """

    return -beta_candidate * Fraction(4, 5)


def w4_conditional_A4_from_scaling() -> Fraction:
    """A_4(W4) obtained only after applying the kappa-scaling ansatz."""

    virasoro_A4 = Fraction(2)
    return w4_kappa_ratio_to_virasoro() * virasoro_A4


def w4_required_A5_from_bridge(beta_candidate: Fraction = Fraction(13)) -> Fraction:
    """A_5(W4) required by the Riccati bridge, conditional on scaled A_4."""

    return (
        w4_required_riccati_ratio(beta_candidate)
        * w4_conditional_A4_from_scaling()
    )


def w4_riccati_bridge_requirement() -> RiccatiBridgeRequirement:
    """Return the missing full-Miura/OPE bridge as executable data."""

    beta_candidate = harmonic_beta4_candidate()
    required_ratio = w4_required_riccati_ratio(beta_candidate)
    conditional_A4 = w4_conditional_A4_from_scaling()
    required_A5 = required_ratio * conditional_A4
    return RiccatiBridgeRequirement(
        beta_candidate=beta_candidate,
        required_ratio=required_ratio,
        conditional_A4_from_scaling=conditional_A4,
        required_A5=required_A5,
        observed_full_miura_A5=None,
        bridge_verified=False,
        obstruction=(
            "No full W4 Miura/OPE computation of A_5(W4) is present. "
            "The lane data give kappa and the candidate beta_4=13, but "
            "they do not determine the shadow-tower A_5 coefficient."
        ),
    )


def direct_w4_attack_report() -> W4AttackReport:
    """Return the W4 attack verdict.

    The lane computation selects 13 against the two polynomial
    extrapolations.  The proof flag is false because no computation here
    constructs A_5(W4) from the full W4 OPE and inserts it into the
    shadow master equation.
    """

    lane_sum = w4_lane_sum_beta_candidate()
    bridge = w4_riccati_bridge_requirement()
    return W4AttackReport(
        lane_sum=lane_sum,
        triangular_candidate=triangular_beta4_candidate(),
        quadratic_candidate=quadratic_beta4_candidate(),
        harmonic_candidate=harmonic_beta4_candidate(),
        required_bridge_ratio=bridge.required_ratio,
        conditional_A4_from_scaling=bridge.conditional_A4_from_scaling,
        required_A5_from_bridge=bridge.required_A5,
        observed_full_miura_A5=bridge.observed_full_miura_A5,
        proves_beta4=False,
        missing_bridge=(
            "Compute A_5(W4) from the full W4 Miura/OPE structure constants "
            "and verify A_5(W4)/A_4(W4) = -52/5 independently of the "
            "kappa-ratio scaling ansatz."
        ),
    )


def w4_attack_discriminates_polynomial_interpolants() -> bool:
    """Whether the direct finite-rank W4 lane value separates the candidates."""

    report = direct_w4_attack_report()
    return (
        report.lane_sum == report.harmonic_candidate
        and report.lane_sum != report.triangular_candidate
        and report.lane_sum != report.quadratic_candidate
    )
