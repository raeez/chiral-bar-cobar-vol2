"""Finite models for the Steinberg tautological bridge.

The module does not model the derived Steinberg stack itself. It models the
linear consequence used in the manuscript: a tautological relation annihilates
the operator only when the virtual Borel-Moore weights assigned to the boundary
strata are compatible with clean clutching pullback.  The split finite model
records the three numerical obstructions in the virtual pullback formula:
orientation sign, excess Euler class, and stable-graph automorphism order.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping, Sequence


RationalLike = int | Fraction


def _fraction(value: RationalLike) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def _product(values: Sequence[RationalLike]) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= _fraction(value)
    return result


def permutation_sign(reference_order: Sequence[str], actual_order: Sequence[str]) -> int:
    """Return the determinant sign of the permutation from reference to actual."""

    if len(set(reference_order)) != len(reference_order):
        raise ValueError("reference_order contains repeated labels")
    if len(set(actual_order)) != len(actual_order):
        raise ValueError("actual_order contains repeated labels")
    if set(reference_order) != set(actual_order):
        raise ValueError("orders must contain the same labels")

    positions = {label: index for index, label in enumerate(reference_order)}
    word = [positions[label] for label in actual_order]
    inversions = sum(
        1
        for i, left in enumerate(word)
        for right in word[i + 1 :]
        if left > right
    )
    return -1 if inversions % 2 else 1


@dataclass(frozen=True)
class TautologicalRelation:
    """A finite tautological relation among boundary strata."""

    name: str
    coefficients: tuple[tuple[str, Fraction], ...]

    @classmethod
    def from_mapping(
        cls, name: str, coefficients: Mapping[str, RationalLike]
    ) -> "TautologicalRelation":
        return cls(
            name=name,
            coefficients=tuple(
                (stratum, _fraction(coeff))
                for stratum, coeff in coefficients.items()
                if _fraction(coeff) != 0
            ),
        )


@dataclass(frozen=True)
class OrientationComparison:
    """Determinant-line comparison defining epsilon_Gamma in a finite model."""

    reference_edge_order: tuple[str, ...] = ()
    actual_edge_order: tuple[str, ...] = ()
    reference_cycle_order: tuple[str, ...] = ()
    actual_cycle_order: tuple[str, ...] = ()
    determinant_sign: int = 1

    def __post_init__(self) -> None:
        if self.determinant_sign not in (-1, 1):
            raise ValueError("determinant_sign must be +1 or -1")
        if bool(self.reference_edge_order) != bool(self.actual_edge_order):
            raise ValueError("edge orders must be given together")
        if bool(self.reference_cycle_order) != bool(self.actual_cycle_order):
            raise ValueError("cycle orders must be given together")

    @property
    def edge_sign(self) -> int:
        return permutation_sign(self.reference_edge_order, self.actual_edge_order)

    @property
    def cycle_sign(self) -> int:
        return permutation_sign(self.reference_cycle_order, self.actual_cycle_order)

    @property
    def epsilon(self) -> int:
        return self.determinant_sign * self.edge_sign * self.cycle_sign


def split_virtual_pullback_weight(
    vertex_weights: Sequence[RationalLike],
    *,
    automorphism_order: int = 1,
    excess_euler: RationalLike = 1,
    orientation_sign: int = 1,
) -> Fraction:
    """Scalar form of epsilon*e(E)*prod_v(weight_v)/|Aut(Gamma)|."""

    if automorphism_order <= 0:
        raise ValueError("automorphism_order must be positive")
    if orientation_sign not in (-1, 1):
        raise ValueError("orientation_sign must be +1 or -1")
    return (
        Fraction(orientation_sign)
        * _fraction(excess_euler)
        * _product(vertex_weights)
        / automorphism_order
    )


@dataclass(frozen=True)
class SteinbergPullbackData:
    """Scalar shadow of a split finite Steinberg virtual pullback."""

    parent_weight: RationalLike
    vertex_weights: tuple[RationalLike, ...]
    automorphism_order: int = 1
    excess_euler: RationalLike = 1
    orientation_sign: int = 1

    def __post_init__(self) -> None:
        if self.automorphism_order <= 0:
            raise ValueError("automorphism_order must be positive")
        if self.orientation_sign not in (-1, 1):
            raise ValueError("orientation_sign must be +1 or -1")
        object.__setattr__(self, "parent_weight", _fraction(self.parent_weight))
        object.__setattr__(
            self,
            "vertex_weights",
            tuple(_fraction(weight) for weight in self.vertex_weights),
        )
        object.__setattr__(self, "excess_euler", _fraction(self.excess_euler))

    @property
    def expected_pullback_weight(self) -> Fraction:
        return split_virtual_pullback_weight(
            self.vertex_weights,
            automorphism_order=self.automorphism_order,
            excess_euler=self.excess_euler,
            orientation_sign=self.orientation_sign,
        )

    @property
    def defect(self) -> Fraction:
        return self.parent_weight - self.expected_pullback_weight

    @property
    def is_clean_compatible(self) -> bool:
        return self.defect == 0


def keel_mbar04_relation() -> TautologicalRelation:
    """Return the genus-zero boundary relation D12|34 = D13|24.

    In the finite model the two boundary points of Mbar_{0,4} are represented
    by the labels D12_34 and D13_24. The relation is D12_34 - D13_24 = 0.
    """

    return TautologicalRelation.from_mapping(
        "Mbar_0_4 boundary relation",
        {"D12_34": 1, "D13_24": -1},
    )


def tautological_operator_defect(
    relation: TautologicalRelation,
    steinberg_weights: Mapping[str, RationalLike],
) -> Fraction:
    """Evaluate the one-dimensional operator defect for a relation.

    The Steinberg cap-push in a one-dimensional target sends a boundary stratum
    to its virtual Borel-Moore weight. A relation annihilates the operator iff
    the weighted sum is zero.
    """

    missing = [
        stratum
        for stratum, _coeff in relation.coefficients
        if stratum not in steinberg_weights
    ]
    if missing:
        raise KeyError(f"Missing Steinberg weights for strata: {missing!r}")

    return sum(
        coeff * _fraction(steinberg_weights[stratum])
        for stratum, coeff in relation.coefficients
    )


def relation_annihilates_operator(
    relation: TautologicalRelation,
    steinberg_weights: Mapping[str, RationalLike],
) -> bool:
    return tautological_operator_defect(relation, steinberg_weights) == 0


@dataclass(frozen=True)
class CleanPullbackData:
    """Numerical shadow of the clean virtual pullback formula."""

    parent_weight: RationalLike
    left_weight: RationalLike
    right_weight: RationalLike
    automorphism_order: int = 1
    excess_euler: RationalLike = 1
    orientation_sign: int = 1

    def __post_init__(self) -> None:
        if self.automorphism_order <= 0:
            raise ValueError("automorphism_order must be positive")
        if self.orientation_sign not in (-1, 1):
            raise ValueError("orientation_sign must be +1 or -1")
        object.__setattr__(self, "parent_weight", _fraction(self.parent_weight))
        object.__setattr__(self, "left_weight", _fraction(self.left_weight))
        object.__setattr__(self, "right_weight", _fraction(self.right_weight))
        object.__setattr__(self, "excess_euler", _fraction(self.excess_euler))

    @property
    def expected_pullback_weight(self) -> Fraction:
        return split_virtual_pullback_weight(
            (self.left_weight, self.right_weight),
            automorphism_order=self.automorphism_order,
            excess_euler=self.excess_euler,
            orientation_sign=self.orientation_sign,
        )

    @property
    def defect(self) -> Fraction:
        return self.parent_weight - self.expected_pullback_weight

    @property
    def is_clean_compatible(self) -> bool:
        return self.defect == 0


def clean_pullback_defect(data: CleanPullbackData) -> Fraction:
    """Return parent minus clean/excess virtual pullback prediction."""

    return data.defect


PullbackData = CleanPullbackData | SteinbergPullbackData


def weights_from_parent_pullbacks(
    pullbacks: Mapping[str, PullbackData],
) -> dict[str, Fraction]:
    """Extract parent weights indexed by boundary stratum."""

    return {
        stratum: _fraction(data.parent_weight)
        for stratum, data in pullbacks.items()
    }


def weights_from_expected_pullbacks(
    pullbacks: Mapping[str, PullbackData],
) -> dict[str, Fraction]:
    """Extract epsilon-euler-automorphism pullback weights by stratum."""

    return {
        stratum: data.expected_pullback_weight
        for stratum, data in pullbacks.items()
    }


def clean_pullback_relation_defect(
    relation: TautologicalRelation,
    pullbacks: Mapping[str, PullbackData],
) -> Fraction:
    """Evaluate sum c_Gamma(parent - predicted pullback)."""

    missing = [
        stratum
        for stratum, _coeff in relation.coefficients
        if stratum not in pullbacks
    ]
    if missing:
        raise KeyError(f"Missing Steinberg pullback data for strata: {missing!r}")

    return sum(
        coeff * pullbacks[stratum].defect
        for stratum, coeff in relation.coefficients
    )


def predicted_clutching_relation_defect(
    relation: TautologicalRelation,
    pullbacks: Mapping[str, PullbackData],
) -> Fraction:
    """Evaluate the boundary relation using predicted clutching weights."""

    return tautological_operator_defect(
        relation,
        weights_from_expected_pullbacks(pullbacks),
    )
