"""Exact checks for the Drinfeld-double arity-three MC obstruction."""

from __future__ import annotations

import os
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from compute.lib.drinfeld_double_tau3 import (
    arity_three_cybe_numerator,
    infinitesimal_braid_relations_hold,
    sl2_omega_commutators,
    virasoro_tau2_collision_residue,
)
from compute.lib.independent_verification import independent_verification


REPO = Path(__file__).resolve().parents[2]
ORDERED_TEX = REPO / "chapters/connections/ordered_associative_chiral_kd_frontier.tex"


def _negate(tensor):
    return {key: -coeff for key, coeff in tensor.items()}


@independent_verification(
    claim="comp:drinfeld-double-sl2-tau3",
    derived_from=[
        "Kohno 1987 infinitesimal braid relations cited in the manuscript proof",
        "Loday-Vallette convolution Maurer-Cartan arity filtration used for prop:drinfeld-double-tau3-mc",
    ],
    verified_against=[
        "Direct Chevalley-basis tensor expansion with brackets [e,f]=h, [h,e]=2e, [h,f]=-2f",
        "Cleared-denominator polynomial identity with z13=z12+z23",
    ],
    disjoint_rationale=(
        "The proof cites the infinitesimal braid relations and the operadic "
        "MC filtration. The test expands the Casimir commutators directly "
        "in the sl2 Chevalley basis and clears spectral denominators; no "
        "braid-relation theorem or convolution-filtration result is used to "
        "produce the expected zero."
    ),
)
def test_sl2_tau3_obstruction_vanishes_by_exact_tensor_expansion():
    A, B, C = sl2_omega_commutators()

    assert A
    assert B == _negate(A)
    assert C == A
    assert infinitesimal_braid_relations_hold()

    report = arity_three_cybe_numerator(Fraction(7, 3))
    assert report.commutator_12_13
    assert report.commutator_12_23 == _negate(report.commutator_12_13)
    assert report.commutator_13_23 == report.commutator_12_13
    assert report.z12_coefficient == {}
    assert report.z23_coefficient == {}
    assert report.obstruction_vanishes
    assert report.tau3_filler == "0"


def test_sl2_tau3_vanishes_for_all_level_prefactors_sampled():
    for level in (0, 1, -2, Fraction(5, 2), Fraction(-9, 4)):
        report = arity_three_cybe_numerator(level)
        assert report.level == Fraction(level)
        assert report.obstruction_vanishes


def test_manuscript_cybe_display_has_three_signed_summands():
    source = ORDERED_TEX.read_text()

    assert "\\label{comp:drinfeld-double-sl2-tau3}" in source
    assert "\\frac{[\\Omega_{12},\\Omega_{13}]}{z_{12}z_{13}}" in source
    assert "+\\frac{[\\Omega_{12},\\Omega_{23}]}{z_{12}z_{23}}" in source
    assert "+\\frac{[\\Omega_{13},\\Omega_{23}]}{z_{13}z_{23}}" in source


def test_virasoro_tau3_filler_remains_exact_open_obligation():
    residue = virasoro_tau2_collision_residue(13)

    assert residue["central_z_minus_3"] == Fraction(13, 2)
    assert residue["stress_tensor_z_minus_1"] == Fraction(2)

    source = ORDERED_TEX.read_text()
    assert "\\label{eq:drinfeld-double-virasoro-tau3-open}" in source
    assert "No explicit chain $\\tau_{(3)}^{\\mathrm{Vir}}$" in source
