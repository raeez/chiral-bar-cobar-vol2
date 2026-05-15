"""Tests for F1: BV/BRST = Bar at chain level for class M, g >= 2.

Three independent verification routes:

  ROUTE A: Felder BRST + Zamolodchikov norm
  ROUTE B: Chiral Higher Deligne + curved-Dunn H^2 = 0
  ROUTE C: Mittag-Leffler antighost-commutativity ladder

Disjointness rationale:
  Route A derives from Felder BRST (Felder 1989) + BPZ four-point
  normalisation (Belavin-Polyakov-Zamolodchikov 1984) at special c values.
  Route B derives from chiral Higher Deligne (Vol II
  thm:chiral-higher-deligne) + curved-Dunn H^2 vanishing (Vol II
  thm:curved-dunn-H2-vanishing-all-genera) at g >= 2; no use of S_4 formula
  except as cross-check on the brace coproduct output.
  Route C derives from Vol I MC5 pro-ambient theorem
  thm:mc5-class-m-chain-level-pro-ambient + iterated Sugawara antighost
  commutativity; the h_N contracting homotopy is defined without reference
  to S_4 (the absorption coefficient enters through m_0 = kappa * omega_g,
  determined by the central charge alone).

Agreement among the three routes is the main test, with the witness that
Route A's S_4 must equal Route B's c_r coefficient, and Route C's h_N
must absorb the same harmonic class.
"""

from __future__ import annotations

from fractions import Fraction

import pytest
from sympy import Rational, S, simplify, Symbol

from compute.lib.f1_bv_bar_classm_higher_genus import (
    LAMBDA_FP_2,
    LABEL_V1_MC5,
    LABEL_V2_BV_BAR_WC,
    LABEL_V2_CHIRAL_HIGHER_DELIGNE,
    LABEL_V2_CURVED_DUNN_H2,
    LABEL_V2_ZAMOLODCHIKOV,
    S4_virasoro,
    attack_heal_class_M_probes,
    chiral_higher_deligne_brace_action_route_B,
    curvature_m_0,
    felder_brst_chain_witness_route_A,
    kac_determinant_level_4,
    kappa_ch_Hodge_virasoro,
    mittag_leffler_homotopy_route_C,
    run_F1_summary,
    verify_three_routes_agree,
    virasoro_quasi_primary_at_c,
    zamolodchikov_bpz_norm,
)


# =========================================================================
# Cross-anchor smoke tests: labels exist and engine returns sane data
# =========================================================================


def test_labels_anchored():
    assert LABEL_V1_MC5 == "thm:mc5-class-m-chain-level-pro-ambient"
    assert LABEL_V2_BV_BAR_WC == "prop:bv-bar-class-m-weight-completed"
    assert LABEL_V2_CURVED_DUNN_H2 == "thm:curved-dunn-H2-vanishing-all-genera"
    assert (
        LABEL_V2_CHIRAL_HIGHER_DELIGNE
        == "thm:chiral-higher-deligne"
    )
    assert (
        LABEL_V2_ZAMOLODCHIKOV
        == "prop:zamolodchikov-cocycle-direct-sum-witness"
    )


def test_lambda_fp_genus_2_matches_faber_pandharipande():
    """lambda_2^FP = 7/5760 (Faber-Pandharipande)."""
    assert LAMBDA_FP_2 == Rational(7, 5760)


# =========================================================================
# (V1) Zamolodchikov BPZ norm <-> Kac determinant cross-check
# =========================================================================


@pytest.mark.parametrize(
    "c_val",
    [Rational(1), Rational(25), Rational(26),
     Rational(1, 2), Rational(7, 10)],
)
def test_zamolodchikov_self_pairing_equals_kac_det_over_5(c_val):
    """<Lambda, Lambda>_BPZ = det G_4(c) / 5 (BPZ + Kac)."""
    sp = zamolodchikov_bpz_norm(c_val)
    kd = kac_determinant_level_4(c_val)
    # SP = c(5c+22)/10; KD = c(5c+22)/2; ratio = 1/5
    if kd == 0:
        assert sp == 0
    else:
        ratio = simplify(sp / kd)
        assert ratio == Rational(1, 5), (
            f"At c={c_val}: SP/KD = {ratio} != 1/5"
        )


def test_S4_virasoro_inverse_of_self_pairing():
    """S_4(Vir_c) = 10 / (c (5c + 22)) inverts <Lambda, Lambda>_BPZ * 10/c(5c+22)."""
    c = Symbol('c')
    sp = zamolodchikov_bpz_norm(c)  # c(5c+22)/10
    s4 = S4_virasoro(c)  # 10 / (c(5c+22))
    product = simplify(sp * s4)
    # sp * s4 = (c(5c+22)/10) * (10/(c(5c+22))) = 1
    assert product == 1


def test_S4_diverges_at_c_zero_and_minimal_M_2_5():
    """S_4 -> infty at c = 0 and c = -22/5 (Lambda null)."""
    assert S4_virasoro(0) == float('inf')
    assert S4_virasoro(Rational(-22, 5)) == float('inf')


def test_kac_determinant_level_4_formula():
    """det G_4(c) = c(5c + 22) / 2 (Kac 1979)."""
    c = Symbol('c')
    kd = kac_determinant_level_4(c)
    expected = c * (5 * c + 22) / 2
    assert simplify(kd - expected) == 0


# =========================================================================
# (V2) ROUTE A:  Felder BRST + Zamolodchikov at c in {1, 25, 26}
# =========================================================================


def test_route_A_at_c_equal_1_free_boson():
    """Vir_c at c=1: free boson; S_4 = 10/27."""
    res = felder_brst_chain_witness_route_A(Rational(1))
    assert res['route'] == "A_felder_brst_zamolodchikov"
    # S_4(1) = 10 / (1 * (5 + 22)) = 10/27
    assert simplify(res['S4_structure_constant'] - Rational(10, 27)) == 0
    assert res['c_4_harmonic_coeff'] == res['S4_structure_constant']
    assert res['chain_level_in_raw_direct_sum'] is True
    assert "alpha + epsilon" in res['licensing']


def test_route_A_at_c_equal_25_w3_critical():
    """Vir_c at c=25: W_3 critical level intersection."""
    res = felder_brst_chain_witness_route_A(Rational(25))
    # S_4(25) = 10 / (25 * (125 + 22)) = 10 / (25 * 147) = 10/3675 = 2/735
    expected = Rational(10, 25 * 147)
    assert simplify(res['S4_structure_constant'] - expected) == 0
    # gcd: 10/3675 = 2/735
    assert expected == Rational(2, 735)


def test_route_A_at_c_equal_26_bosonic_string():
    """Vir_c at c=26: critical dimension; Q_BRST^2 = 0."""
    res = felder_brst_chain_witness_route_A(Rational(26))
    # S_4(26) = 10 / (26 * (130 + 22)) = 10 / (26 * 152) = 10 / 3952
    # = 5 / 1976
    expected = Rational(10, 26 * 152)
    assert simplify(res['S4_structure_constant'] - expected) == 0
    assert expected == Rational(5, 1976)


def test_route_A_at_c_zero_special_point():
    """Vir_c at c=0: S_4 diverges; Lambda is null."""
    res = felder_brst_chain_witness_route_A(Rational(0))
    assert res['special_point_c0'] is True
    assert res['chain_level_in_raw_direct_sum'] is False  # cocycle vanishes


def test_route_A_at_c_equal_minus_22_over_5_minimal_M_2_5():
    """Vir_c at c=-22/5: minimal model M(2,5); Lambda is null."""
    res = felder_brst_chain_witness_route_A(Rational(-22, 5))
    assert res['special_point_min'] is True
    assert res['chain_level_in_raw_direct_sum'] is False


# =========================================================================
# (V3) ROUTE B:  Chiral Higher Deligne + curved-Dunn H^2 = 0
# =========================================================================


@pytest.mark.parametrize(
    "c_val,bar_weight,expected_m0_power",
    [
        (Rational(1), 4, 1),     # m_0^1
        (Rational(25), 4, 1),    # m_0^1
        (Rational(26), 6, 2),    # m_0^2 at bar weight 6
        (Rational(26), 8, 3),    # m_0^3 at bar weight 8
    ],
)
def test_route_B_brace_action_factor_through_m0(c_val, bar_weight, expected_m0_power):
    """Brace action: delta_r^harm = c_r(A) * m_0^{floor(r/2) - 1}."""
    res = chiral_higher_deligne_brace_action_route_B(
        c_val, bar_weight, genus=2
    )
    expected_power_str = f"m_0^{expected_m0_power}"
    assert expected_power_str in res['delta_r_harmonic']
    assert res['e2_brace_chiral_action'] is True
    assert res['curved_dunn_H2_vanishes_at_genus'] is True


def test_route_B_below_weight_4_is_zero():
    """No class M discrepancy below bar weight 4
    (low-weight vanishing, prop:chain-level-three-obstructions)."""
    res = chiral_higher_deligne_brace_action_route_B(
        Rational(1), bar_weight=2, genus=2
    )
    assert res['c_r_harmonic_coeff'] == Rational(0)


def test_route_B_curved_dunn_requires_g_geq_2():
    """Curved-Dunn H^2 = 0 holds at g >= 2 only."""
    res_g1 = chiral_higher_deligne_brace_action_route_B(
        Rational(1), bar_weight=4, genus=1
    )
    res_g2 = chiral_higher_deligne_brace_action_route_B(
        Rational(1), bar_weight=4, genus=2
    )
    assert res_g1['curved_dunn_H2_vanishes_at_genus'] is False
    assert res_g2['curved_dunn_H2_vanishes_at_genus'] is True


# =========================================================================
# (V4) ROUTE C:  Mittag-Leffler antighost-commutativity ladder
# =========================================================================


def test_route_C_homotopy_polynomial_degree():
    """h_N has degree floor(N/2) - 1 in m_0."""
    for N in [2, 4, 6, 8, 10]:
        res = mittag_leffler_homotopy_route_C(
            Rational(1), truncation_N=N, genus=2
        )
        assert res['h_N_degree'] == max(0, N // 2 - 1)


def test_route_C_mittag_leffler_surjective_lim1_zero():
    """Strong filtration -> surjective bonding -> lim^1 = 0."""
    res = mittag_leffler_homotopy_route_C(
        Rational(25), truncation_N=8, genus=2
    )
    assert res['mittag_leffler_surjective_bonding'] is True
    assert res['lim_1_vanishes'] is True
    assert res['pro_object_strict_qis'] is True
    assert res['antighost_commutativity_chain_level'] is True


def test_route_C_at_truncation_zero_yields_empty_homotopy():
    """N=0 truncation has h_N = 0 (no harmonic absorption needed)."""
    res = mittag_leffler_homotopy_route_C(
        Rational(1), truncation_N=0, genus=2
    )
    assert res['h_N_polynomial_in_m_0'] == S.Zero


# =========================================================================
# (V5) THREE-ROUTE INTEGRATION:  m_0 = kappa_ch^Hodge * omega_g
# =========================================================================


@pytest.mark.parametrize(
    "c_val", [Rational(1), Rational(25), Rational(26),
              Rational(1, 2), Rational(7, 10)],
)
def test_three_routes_share_S4_coefficient_at_bar_weight_4(c_val):
    """Routes A, B agree on the harmonic coefficient at bar weight 4."""
    cA = felder_brst_chain_witness_route_A(c_val)['c_4_harmonic_coeff']
    cB = chiral_higher_deligne_brace_action_route_B(
        c_val, bar_weight=4, genus=2
    )['c_r_harmonic_coeff']
    diff = simplify(cA - cB)
    assert diff == 0, (
        f"Routes A and B disagree at c={c_val}: route A = {cA},"
        f" route B = {cB}, diff = {diff}"
    )


def test_kappa_ch_Hodge_virasoro_equals_central_charge():
    """kappa_ch^Hodge(Vir_c) = c (Vol II standard normalisation)."""
    for c_val in [Rational(1), Rational(25), Rational(26),
                   Rational(1, 2), Rational(7, 10)]:
        assert kappa_ch_Hodge_virasoro(c_val) == c_val


def test_curvature_m_0_structure():
    """m_0 = kappa_ch^Hodge(A) * omega_g of cohomological degree 2."""
    m0 = curvature_m_0(Rational(1), genus=2)
    assert m0['m_0_cohomological_degree'] == 2
    assert m0['kappa_ch_Hodge'] == 1
    assert "omega_2" in m0['m_0_symbolic']


def test_genus_2_free_energy_from_FP():
    """F_2(A) = kappa(A) * lambda_2^FP = kappa * 7/5760 (Theorem D)."""
    m0 = curvature_m_0(Rational(1), genus=2)
    assert m0['genus_g_free_energy'] == Rational(1) * Rational(7, 5760)
    assert m0['genus_g_free_energy'] == Rational(7, 5760)


# =========================================================================
# (V6) FORBIDDEN SLOGAN ENFORCEMENT
# =========================================================================


def test_forbidden_slogan_15_class_M_chain_level():
    """CLAUDE.md §8 forbidden slogan #15:
    "class M chain-level" -> "conditional on hyp:ambient-wt-cpl;
    fails in Ch(Vect)"."""
    summary = run_F1_summary(verbose=False)
    msg = summary['forbidden_15']
    assert "chain-level" in msg
    assert "Ch(Vect)" in msg
    assert "hyp:ambient-wt-cpl" in msg


def test_raw_direct_sum_witness_via_Zamolodchikov_cocycle():
    """xi_Lambda witnesses d^2 != 0 in Ch(Vect) at c outside {0, -22/5}.
    Conditional on hyp:ambient-wt-cpl, the witness is absorbed by h_N
    in pro-Ch(Vect)."""
    # The witness is non-zero at generic c
    sp = zamolodchikov_bpz_norm(Rational(1))
    assert sp != 0
    # At c=0 or c=-22/5 the pairing vanishes (Lambda null)
    assert zamolodchikov_bpz_norm(Rational(0)) == 0
    # Kac det also vanishes at c=0 and c=-22/5
    assert kac_determinant_level_4(Rational(0)) == 0
    assert kac_determinant_level_4(Rational(-22, 5)) == 0


# =========================================================================
# (V7) ATTACK-HEAL PROBES
# =========================================================================


def test_attack_heal_class_m_probes_count():
    """8 attack-heal probes covering the class M landscape."""
    probes = attack_heal_class_M_probes()
    assert len(probes) == 8


def test_attack_heal_coherence_breaks_at_critical_level_and_nontrivial_cocycle():
    """Critical W_N level and non-trivial-cocycle algebras genuinely break
    chain-level coherence; all other class M probes close."""
    probes = attack_heal_class_M_probes()
    breaks_count = sum(1 for p in probes if p.coherence_breaks)
    assert breaks_count == 2
    breaking = [p for p in probes if p.coherence_breaks]
    breaking_names = {p.name for p in breaking}
    assert any("critical level" in n for n in breaking_names)
    assert any("Non-trivial-cocycle" in n for n in breaking_names)


def test_attack_heal_vir_special_points_do_not_break_due_to_null():
    """Vir_c at c=0 and c=-22/5: Lambda is null, so no obstruction to absorb;
    coherence closes vacuously."""
    probes = attack_heal_class_M_probes()
    for p in probes:
        if p.name.startswith("Vir_c at c=0") or "M(2,5)" in p.name:
            assert not p.coherence_breaks
            assert "null" in p.failure_mode


def test_attack_heal_bershadsky_polyakov_non_rational_requires_J_adic():
    """Bershadsky-Polyakov at non-rational level: weight-completion alone
    insufficient; needs J-adic refinement with transcendental k."""
    probes = attack_heal_class_M_probes()
    for p in probes:
        if "Bershadsky-Polyakov" in p.name:
            assert not p.coherence_breaks
            assert "J-adic" in p.failure_mode or "J-adic" in (p.surviving_route or "")


# =========================================================================
# (V8) MULTI-PATH AGREEMENT (Beilinson disagreement-is-the-deliverable)
# =========================================================================


@pytest.mark.parametrize(
    "c_val",
    [Rational(1), Rational(25), Rational(26),
     Rational(1, 2), Rational(7, 10)],
)
def test_three_routes_agree_at_each_test_c(c_val):
    """Routes A, B, C agree on the m_0 = kappa * omega_g structure
    and on the harmonic absorption profile at bar weight 4, genus 2.

    Disagreement is the Beilinson deliverable; agreement validates the
    reconstruction theorem at the tested c values.
    """
    result = verify_three_routes_agree(c_val, genus=2)
    assert result['three_routes_agree'] is True, (
        f"Three routes disagree at c={c_val}:\n"
        f"  route A = {result['route_A']}\n"
        f"  route B = {result['route_B']}\n"
        f"  route C = {result['route_C']}"
    )


def test_run_F1_summary_top_level():
    """Top-level summary returns frontier metadata and per-c results."""
    summary = run_F1_summary(verbose=False)
    assert summary['frontier'] == "F1"
    assert "BV/BRST" in summary['title']
    assert "Bar at chain level" in summary['title']
    assert len(summary['three_routes_summary']) == 6
    assert len(summary['attack_heal_probes']) == 8
    # all summary entries should agree
    for entry in summary['three_routes_summary']:
        assert entry['three_routes_agree'] is True
