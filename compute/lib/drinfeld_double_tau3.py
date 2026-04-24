"""Exact arity-three obstruction checks for the chiral Drinfeld double.

The engine computes the rational affine sl2 CYBE term

    [Omega_12, Omega_13] / (z12 z13)
  + [Omega_12, Omega_23] / (z12 z23)
  + [Omega_13, Omega_23] / (z13 z23)

with Omega = e tensor f + f tensor e + (1/2) h tensor h and
z13 = z12 + z23.  Clearing denominators leaves two tensor
coefficients, both zero by the infinitesimal braid relations.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, Mapping, Tuple

Basis = str
TensorKey = Tuple[Basis, Basis, Basis]
Tensor3 = Dict[TensorKey, Fraction]
OmegaTerm = Tuple[Basis, Basis, Fraction]


SL2_BRACKETS: Mapping[Tuple[Basis, Basis], Mapping[Basis, Fraction]] = {
    ("e", "f"): {"h": Fraction(1)},
    ("h", "e"): {"e": Fraction(2)},
    ("h", "f"): {"f": Fraction(-2)},
}

SL2_OMEGA: Tuple[OmegaTerm, ...] = (
    ("e", "f", Fraction(1)),
    ("f", "e", Fraction(1)),
    ("h", "h", Fraction(1, 2)),
)


@dataclass(frozen=True)
class Tau3ObstructionReport:
    """Exact report for the cleared arity-three MC obstruction."""

    level: Fraction
    commutator_12_13: Tensor3
    commutator_12_23: Tensor3
    commutator_13_23: Tensor3
    z12_coefficient: Tensor3
    z23_coefficient: Tensor3

    @property
    def obstruction_vanishes(self) -> bool:
        return not self.z12_coefficient and not self.z23_coefficient

    @property
    def tau3_filler(self) -> str:
        return "0" if self.obstruction_vanishes else "unresolved"


def sl2_bracket(left: Basis, right: Basis) -> Mapping[Basis, Fraction]:
    """Return [left, right] in the Chevalley basis e, h, f."""

    if (left, right) in SL2_BRACKETS:
        return SL2_BRACKETS[(left, right)]
    if (right, left) in SL2_BRACKETS:
        return {basis: -coeff for basis, coeff in SL2_BRACKETS[(right, left)].items()}
    return {}


def _add_tensors(*tensors: Mapping[TensorKey, Fraction]) -> Tensor3:
    result: defaultdict[TensorKey, Fraction] = defaultdict(Fraction)
    for tensor in tensors:
        for key, coeff in tensor.items():
            result[key] += coeff
    return {key: coeff for key, coeff in result.items() if coeff}


def _scale_tensor(tensor: Mapping[TensorKey, Fraction], scalar: Fraction) -> Tensor3:
    return {key: scalar * coeff for key, coeff in tensor.items() if scalar * coeff}


def _commutator_omega_12_13(omega: Iterable[OmegaTerm] = SL2_OMEGA) -> Tensor3:
    result: defaultdict[TensorKey, Fraction] = defaultdict(Fraction)
    terms = tuple(omega)
    for a, b, coeff_ab in terms:
        for c, d, coeff_cd in terms:
            for bracket_basis, bracket_coeff in sl2_bracket(a, c).items():
                result[(bracket_basis, b, d)] += coeff_ab * coeff_cd * bracket_coeff
    return {key: coeff for key, coeff in result.items() if coeff}


def _commutator_omega_12_23(omega: Iterable[OmegaTerm] = SL2_OMEGA) -> Tensor3:
    result: defaultdict[TensorKey, Fraction] = defaultdict(Fraction)
    terms = tuple(omega)
    for a, b, coeff_ab in terms:
        for c, d, coeff_cd in terms:
            for bracket_basis, bracket_coeff in sl2_bracket(b, c).items():
                result[(a, bracket_basis, d)] += coeff_ab * coeff_cd * bracket_coeff
    return {key: coeff for key, coeff in result.items() if coeff}


def _commutator_omega_13_23(omega: Iterable[OmegaTerm] = SL2_OMEGA) -> Tensor3:
    result: defaultdict[TensorKey, Fraction] = defaultdict(Fraction)
    terms = tuple(omega)
    for a, b, coeff_ab in terms:
        for c, d, coeff_cd in terms:
            for bracket_basis, bracket_coeff in sl2_bracket(b, d).items():
                result[(a, c, bracket_basis)] += coeff_ab * coeff_cd * bracket_coeff
    return {key: coeff for key, coeff in result.items() if coeff}


def sl2_omega_commutators() -> Tuple[Tensor3, Tensor3, Tensor3]:
    """Return A, B, C for the three Casimir commutators."""

    return (
        _commutator_omega_12_13(),
        _commutator_omega_12_23(),
        _commutator_omega_13_23(),
    )


def arity_three_cybe_numerator(level: Fraction | int = Fraction(1)) -> Tau3ObstructionReport:
    """Clear denominators in the rational arity-three obstruction.

    With u = z12, v = z23, z13 = u + v, the numerator is

        v A + (u + v) B + u C,

    where A = [Omega_12, Omega_13], B = [Omega_12, Omega_23], and
    C = [Omega_13, Omega_23].  The u coefficient is B + C and the
    v coefficient is A + B.  The affine level contributes the scalar
    factor level^2.
    """

    k = Fraction(level)
    A, B, C = sl2_omega_commutators()
    level_square = k * k
    return Tau3ObstructionReport(
        level=k,
        commutator_12_13=_scale_tensor(A, level_square),
        commutator_12_23=_scale_tensor(B, level_square),
        commutator_13_23=_scale_tensor(C, level_square),
        z12_coefficient=_scale_tensor(_add_tensors(B, C), level_square),
        z23_coefficient=_scale_tensor(_add_tensors(A, B), level_square),
    )


def infinitesimal_braid_relations_hold() -> bool:
    """Check [Omega_12, Omega_13 + Omega_23] and its companion."""

    A, B, C = sl2_omega_commutators()
    return not _add_tensors(A, B) and not _add_tensors(B, C) and C == A


def virasoro_tau2_collision_residue(central_charge: Fraction | int) -> Mapping[str, Fraction]:
    """Return the Virasoro binary term in the collision-residue convention."""

    c = Fraction(central_charge)
    return {
        "central_z_minus_3": c / 2,
        "stress_tensor_z_minus_1": Fraction(2),
    }

