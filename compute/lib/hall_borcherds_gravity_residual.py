"""K3 x E scalar shadow versus Hall--Borcherds gravity-line data."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import FrozenSet, Iterable, Tuple


@dataclass(frozen=True)
class K3BorcherdsScalarShadow:
    """Numerical scalar data of the K3 x E Borcherds shadow."""

    c1_zero: int = 10
    delta5_weight: int = 5
    phi10_weight: int = 10
    delta5_square_power: int = 2
    bps_phi10_power: int = -1

    @property
    def bkm_weight(self) -> Fraction:
        return Fraction(self.c1_zero, 2)

    def scalar_equalities_hold(self) -> bool:
        return (
            self.bkm_weight == self.delta5_weight
            and self.phi10_weight == self.delta5_square_power * self.delta5_weight
            and self.bps_phi10_power == -1
        )


POSITIVE_HALF_HALL_BORCHERDS = "positive_half_e1_chiral_bialgebra"
DRINFELD_DOUBLE_COMPLETION = "drinfeld_double_completion"
CURRENT_ENVELOPE_ON_E = "current_envelope_on_E"
SCCHTOP_GRAVITY_LINE_MORPHISM = "filtered_SCchtop_gravity_line_morphism"
DERIVED_CENTER_TRACE_COMPATIBILITY = "derived_center_trace_compatibility"

REQUIRED_CHAIN_DATA: Tuple[str, ...] = (
    POSITIVE_HALF_HALL_BORCHERDS,
    DRINFELD_DOUBLE_COMPLETION,
    CURRENT_ENVELOPE_ON_E,
    SCCHTOP_GRAVITY_LINE_MORPHISM,
    DERIVED_CENTER_TRACE_COMPATIBILITY,
)


def normalize_blocks(blocks: Iterable[str]) -> FrozenSet[str]:
    return frozenset(blocks)


def missing_chain_data(blocks: Iterable[str]) -> Tuple[str, ...]:
    available = normalize_blocks(blocks)
    return tuple(block for block in REQUIRED_CHAIN_DATA if block not in available)


def can_promote_scalar_to_gravity_line(blocks: Iterable[str]) -> bool:
    """Return whether the named chain-level data suffice for promotion.

    The scalar Borcherds equalities are deliberately not an input here:
    they fix the automorphic character but do not supply any chain map.
    """

    return not missing_chain_data(blocks)


def classify_k3_hall_bridge(blocks: Iterable[str]) -> str:
    missing = missing_chain_data(blocks)
    if missing:
        return "scalar_shadow_only"
    return "conditional_chain_level_candidate"

