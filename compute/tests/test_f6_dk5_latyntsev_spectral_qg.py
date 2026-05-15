"""Tests for F6 / DK-5 / B4: Latyntsev spectral-QG comparison.

Tests the f6_dk5_latyntsev_spectral_qg_engine module: local Latyntsev sphere,
cosheaf descent, C-W-Y 4D Chern-Simons realisation, and the bridge criterion
status at each rank.
"""

from __future__ import annotations

import sympy as sp

from compute.lib.f6_dk5_latyntsev_spectral_qg_engine import (
    LatyntsevSpectralQG,
    b4_local_shadow_proved,
    bridge_criterion_status,
    cwy_4d_chern_simons_realisation,
    factorisation_cosheaf_axiom,
    latyntsev_sphere_sl2,
    match_via_FRT_pairing_sl2,
    route_i_frt_at_eval_sl2,
    route_ii_cosheaf_descent,
    route_iii_cwy_4d_cs,
)


# =========================================================================
# Latyntsev local sphere Phi_q(sl_2)
# =========================================================================


def test_latyntsev_sphere_sl2_rank():
    """Phi_q(sl_2) has rank 1, type A."""
    sphere = latyntsev_sphere_sl2()
    assert sphere["rank"] == 1
    assert sphere["lie_type"] == "A"
    assert sphere["is_FRT_bialgebra_of_Y_hbar_sl2"]


def test_latyntsev_sphere_sl2_R_matrix():
    """The Yang R-matrix R(u) = u I - hbar P is the R-matrix of Phi_q(sl_2)."""
    sphere = latyntsev_sphere_sl2()
    assert "u I - hbar P" in str(sphere["R_matrix"])


def test_latyntsev_sphere_sl2_unitarity():
    """The Yang R-matrix satisfies R(u) R(-u) = (hbar^2 - u^2) I."""
    sphere = latyntsev_sphere_sl2()
    assert "(hbar^2 - u^2) I" in str(sphere["unitarity"])


def test_latyntsev_sphere_sl2_vol1_anchor():
    """The FRT-Y_hbar(sl_2) identification is Vol I prop:dk5-sl2-frt."""
    sphere = latyntsev_sphere_sl2()
    assert sphere["anchor_vol1"] == "prop:dk5-sl2-frt"


# =========================================================================
# Cosheaf descent on Ran(C)
# =========================================================================


def test_factorisation_cosheaf_axiom():
    """The Latyntsev cosheaf on Ran(C) satisfies the Beilinson-Drinfeld
    2004 factorisation axiom: F(D_1 sqcup D_2) ~ F(D_1) otimes F(D_2)
    for disjoint disks."""
    axiom = factorisation_cosheaf_axiom()
    assert "F(D_1 sqcup D_2) ~ F(D_1) ot F(D_2)" in str(axiom["axiom_statement"])
    assert "constructible cosheaf on Ran(C)" in str(axiom["Ran_C_structure"])


# =========================================================================
# Local shadow proved, global open
# =========================================================================


def test_b4_local_shadow_proved():
    """Vol II thm:lines_factorisationQG: the local factorisation quantum-group
    shadow is PROVED (monoidal, meromorphic tensor, braiding, local
    factorisation); the global Latyntsev Ran-cosheaf remains CONJECTURAL."""
    status = b4_local_shadow_proved()
    assert "PROVED" in status["monoidal_local"]
    assert "PROVED" in status["meromorphic_tensor_local"]
    assert "PROVED" in status["braiding_local"]
    assert "PROVED" in status["local_factorisation_shadow"]
    assert "CONJECTURAL" in status["global_Ran_cosheaf"]
    assert "CONJECTURAL" in status["rep_category_comparison"]


# =========================================================================
# Match via FRT pairing
# =========================================================================


def test_match_via_FRT_pairing_sl2():
    """The FRT pairing < t_{ij}(u), t_{kl}(v) > = R(u-v)_{ki, jl} gives
    Mod^{comp}(Y_hbar(sl_2)) ~ Rep^{spec}(Phi_q(sl_2))^{op}."""
    match = match_via_FRT_pairing_sl2()
    assert "FRT_pairing" in match
    assert "module_equivalence_sl2" in match
    assert match["vol1_anchor"] == "prop:dk5-sl2-frt"


# =========================================================================
# C-W-Y 4D Chern-Simons realisation
# =========================================================================


def test_cwy_4d_chern_simons_realisation():
    """Costello-Witten-Yamazaki 2017/2018: 4D CS on C x R^2 with gauge g
    has line-operator algebra = Y_hbar(g) (Yangian)."""
    cwy = cwy_4d_chern_simons_realisation()
    assert cwy["theory"] == "4D Chern-Simons on C x R^2"
    assert cwy["spectral_parameter"] == "position z on C"
    assert cwy["R_matrix_origin"] == "4D propagator dz / z"
    assert cwy["line_operator_algebra"] == "Y_hbar(g) (Yangian)"


# =========================================================================
# Three independent routes for B4
# =========================================================================


def test_route_i_frt_at_eval_sl2():
    """ROUTE I: FRT presentation at the eval point for sl_2 (LOCAL B4 shadow)."""
    route = route_i_frt_at_eval_sl2()
    assert route["rank"] == 1
    assert route["lie_type"] == "A"


def test_route_ii_cosheaf_descent():
    """ROUTE II: cosheaf descent on Ran(C) (Beilinson-Drinfeld 2004 ch. 3)."""
    route = route_ii_cosheaf_descent()
    assert "axiom_statement" in route
    assert "Ran_C_structure" in route


def test_route_iii_cwy_4d_cs():
    """ROUTE III: C-W-Y 4D CS realisation."""
    route = route_iii_cwy_4d_cs()
    assert "Y_hbar(g)" in route["line_operator_algebra"]


# =========================================================================
# Bridge Criterion status
# =========================================================================


def test_bridge_criterion_status_rank_1():
    """At rank 1 (sl_2): B1 + B2 proved; B4 LOCAL shadow proved; B4 GLOBAL
    Ran-cosheaf open. Eval-core triple bridge CLOSED; full triple bridge
    open (B4 global)."""
    status = bridge_criterion_status(rank=1)
    assert status["lie_algebra"] == "sl_2"
    assert "proved" in status["B1_status"]
    assert "proved" in status["B2_status"]
    assert "proved" in status["B4_local_status"]
    assert "open" in status["B4_global_status"]
    assert status["triple_bridge_eval_core"] == "closed"
    assert status["triple_bridge_full"] == "open (B4 global)"


def test_bridge_criterion_status_rank_2():
    """At rank 2 (sl_3): all three conditional on F5 rank-2 seed."""
    status = bridge_criterion_status(rank=2)
    assert status["lie_algebra"] == "sl_3"
    assert "conditional" in status["B1_status"]
    assert "conditional" in status["B2_status"]
    assert "conditional" in status["B4_status"]
    assert status["triple_bridge"] == "open"


def test_bridge_criterion_status_rank_3():
    """At rank >= 3: all conditional on compact-completion conjecture."""
    status = bridge_criterion_status(rank=3)
    assert status["lie_algebra"] == "sl_4"
    assert "compact-completion" in status["all_three_conditional_on"]
    assert status["triple_bridge"] == "open"
