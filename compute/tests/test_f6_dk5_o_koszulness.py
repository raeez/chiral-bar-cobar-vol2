"""Tests for F6 / DK-5 / B1: O-Koszulness beyond eval core.

Tests the f6_dk5_o_koszulness_engine module: explicit BGG resolutions in
sl_2 category O, Yangian-side BGS analogues, and attack-heal at rank >= 3.
"""

from __future__ import annotations

import sympy as sp

from compute.lib.f6_dk5_o_koszulness_engine import (
    SL2Weight,
    SL2Block,
    b1_attack_quillen_vs_infinity,
    b1_attack_rank_3,
    b1_attack_z2_parity,
    b1_obstruction_diagnostic_sl2,
    bgg_resolution_length_sl2,
    ext_dimensions_sl2,
    koszul_property_sl2,
    verma_composition_factors,
    yangian_o_block_simples_sl2,
)


# =========================================================================
# Sanity: sl_2 weight dot action
# =========================================================================


def test_sl2_dot_action_involution():
    """The dot action s . m = -m - 2 is an involution: s . (s . m) = m."""
    for m in range(-3, 4):
        w = SL2Weight(m)
        assert w.dot_action_s().dot_action_s() == w


def test_sl2_dominant_weights():
    """Dominant weights m >= 0; weights m = -1 is the singular case."""
    assert SL2Weight(0).is_dominant()
    assert SL2Weight(1).is_dominant()
    assert not SL2Weight(-1).is_dominant()
    assert not SL2Weight(-2).is_dominant()


# =========================================================================
# Verma composition factors (sl_2)
# =========================================================================


def test_verma_composition_factors_dominant():
    """For m >= 0, M_m has two composition factors L_m and L_{-m-2}."""
    factors = verma_composition_factors(0)
    assert SL2Weight(0) in factors
    assert SL2Weight(-2) in factors


def test_verma_composition_factors_singular():
    """For m = -1 (singular), M_{-1} = L_{-1} (simple Verma)."""
    factors = verma_composition_factors(-1)
    assert factors == [SL2Weight(-1)]


def test_verma_composition_factors_antidominant():
    """For m <= -2, M_m is simple with unique composition factor L_m."""
    for m in (-2, -3, -5):
        factors = verma_composition_factors(m)
        assert factors == [SL2Weight(m)]


# =========================================================================
# BGG resolution length
# =========================================================================


def test_bgg_resolution_length_sl2():
    """BGG resolution of L_0 in sl_2: 0 -> M_{-2} -> M_0 -> L_0 -> 0 has
    length 1 (one nonzero map between Vermas above L_0)."""
    assert bgg_resolution_length_sl2() == 1


# =========================================================================
# Ext dimensions in sl_2 category O
# =========================================================================


def test_ext0_is_delta():
    """Ext^0(L_i, L_j) = delta_{i, j} (Schur's lemma)."""
    exts = ext_dimensions_sl2(block_dominant_weight=0)
    assert exts[(0, 0, 0)] == 1
    assert exts[(0, -2, -2)] == 1
    assert exts[(0, 0, -2)] == 0
    assert exts[(0, -2, 0)] == 0


def test_ext1_dot_action_pair():
    """Ext^1(L_i, L_j) = 1 iff j = s . i = -i - 2 (the unique BGG ext)."""
    exts = ext_dimensions_sl2(block_dominant_weight=0)
    # Pair (0, -2) and (-2, 0) are dot-action pairs: i + j = -2
    assert exts[(1, 0, -2)] == 1
    assert exts[(1, -2, 0)] == 1
    # Self-extensions vanish:
    assert exts[(1, 0, 0)] == 0
    assert exts[(1, -2, -2)] == 0


def test_ext_higher_vanishes():
    """Ext^k = 0 for k >= 2 (sl_2 category O has global dim 1 on regular block)."""
    exts = ext_dimensions_sl2(block_dominant_weight=0)
    for i in (0, -2):
        for j in (0, -2):
            assert exts[(2, i, j)] == 0


# =========================================================================
# Beilinson-Ginzburg-Soergel Koszul property
# =========================================================================


def test_koszul_property_sl2():
    """BGS 1996 Koszul property for sl_2 category O.

    K1: non-negatively graded with semisimple degree 0.
    K2: generated in degree 1.
    K3: quadratic.
    K4: diagonal Ext-concentration (Ext^k lives in graded degree k).
    """
    props = koszul_property_sl2(block_dominant_weight=0)
    assert props["K1_nonneg_graded_with_semisimple_degree_0"]
    assert props["K2_generated_in_degree_1"]
    assert props["K3_quadratic"]


# =========================================================================
# Yangian-side category O
# =========================================================================


def test_yangian_o_block_simples_sl2():
    """Two sources of simples in Hernandez O_Y(sl_2):
       (1) V_omega(a) -- evaluation modules (in eval-generated core);
       (2) L^-(a)     -- prefundamentals (beyond eval core)."""
    simples = yangian_o_block_simples_sl2()
    labels = [s[0] for s in simples]
    assert "V_omega(a)" in labels
    assert "L^-(a)" in labels


def test_b1_obstruction_diagnostic_sl2():
    """The K_0 relation [V_omega(a)] [L^-(b)] = [L^-(b+1)] + [L^-(b-1)]
    is the categorical CG closure for sl_2 Yangian beyond the eval core,
    matching Chari-Moura 2006 multiplicity-free l-weight property."""
    diag = b1_obstruction_diagnostic_sl2()
    assert "k0_relation_V_L_minus" in diag
    assert diag["cluster_type"] == sp.Symbol("A_{infty/2}")


# =========================================================================
# Attack-heal: rank >= 3
# =========================================================================


def test_b1_attack_rank_3():
    """Attack at rank >= 3: Kazhdan-Lusztig multiplicities can exceed 1
    starting at sl_4 (rank 3), giving the first multi-weight null
    contribution that defeats the simple BGS argument.

    HEAL: lift the BGS parity grading to Y_hbar(g) via chiral Hochschild,
    conditional on the compact-completion conjecture (Vol I)."""
    result = b1_attack_rank_3(rank=3)
    assert result["rank"] == 3
    assert result["lie_algebra"] == "sl_4"
    # |S_4| = 24
    assert result["weyl_order"] == 24
    assert result["simples_in_regular_block"] == 24
    assert result["kl_multiplicities_exceed_1"]
    assert result["heal_via_parity_BGS"]
    assert result["compact_completion_status"] == "conditional"


def test_b1_attack_z2_parity():
    """Attack: does B1 require a Z_2-grading / parity Beilinson-Ginzburg-Soergel?

    YES: the full strength of BGS (1996) is the parity-mixed equivalence
    D^b(O(g)) ~ D^b(P_W(G/B))[parity-mixed]. The Z_2 grading is the parity
    of perverse sheaves on G/B w.r.t. Bruhat stratification.

    HEAL: install the parity-mixed BGS via geometric Satake (Mirkovic-Vilonen
    2007), which carries the chiral Hochschild grading to the parity grading
    on the affine Grassmannian Gr_G."""
    result = b1_attack_z2_parity()
    assert result["z2_parity_required"]
    assert result["BGS_1996_carries_parity"]
    assert result["geometric_satake_route"] == "Mirkovic-Vilonen 2007"


def test_b1_attack_quillen_vs_infinity():
    """Attack: is the bridge equivalence at the model-categorical level a
    Quillen pair, or higher (infinity-categorical adjunction)?

    The bridge target is LEVEL 4 (infinity-categorical equivalence enriched
    over the Ran-cosheaf structure). B1 / B2 / B4 operate at LEVELS 1, 2, 4
    respectively, stacked via BGS-Quillen + Lurie HA.5.5 + Latyntsev
    Ran-cosheaf."""
    result = b1_attack_quillen_vs_infinity()
    assert "LEVEL 1" in result["B1_level"]
    assert "LEVEL 2" in result["B2_level"]
    assert "LEVEL 4" in result["B4_level"]
    assert result["bridge_target_level"] == "LEVEL 4 (highest)"
