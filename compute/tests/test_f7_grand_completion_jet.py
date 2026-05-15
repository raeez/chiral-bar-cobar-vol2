r"""Tests for F7 grand completion: jet principle on K3-Heisenberg.

Covers:
1. K3 Mukai Gram form construction (signature (4, 20), unimodular, even, rank 24).
2. K3-Heisenberg bar windows K_1, K_2, K_3.
3. Yangian r-matrix jets (only z^{-1} non-trivial for Gaussian).
4. Jet principle verification on the K3-Heisenberg (vacuous).
5. Cross-check on sl_2_hat (also vacuous beyond q = 2).
6. Honest gap-naming on Virasoro (jet principle requires reformulation).
"""
from __future__ import annotations

import numpy as np
import pytest

from compute.lib.f7_grand_completion_jet import (
    BarWindow,
    JetPrincipleVerdict,
    RMatrixJets,
    e8_gram_negative,
    f7_grand_completion_jet_principle_report,
    hyperbolic_plane_gram,
    k3_heisenberg_bar_window,
    k3_heisenberg_yangian_rmatrix,
    mukai_gram_form,
    verify_jet_principle_k3_heisenberg,
    verify_jet_principle_sl2_hat,
    verify_mukai_signature_and_unimodularity,
    virasoro_jet_principle_status,
)


# =========================================================================
# 1. MUKAI GRAM FORM
# =========================================================================


def test_hyperbolic_plane_signature_and_det():
    U = hyperbolic_plane_gram()
    assert U.shape == (2, 2)
    eigs = np.linalg.eigvalsh(U)
    p = sum(e > 0 for e in eigs)
    q = sum(e < 0 for e in eigs)
    assert p == 1 and q == 1, f"U signature should be (1, 1), got ({p}, {q})"
    assert abs(np.linalg.det(U) - (-1.0)) < 1e-9


def test_e8_negative_signature():
    E8m = e8_gram_negative()
    assert E8m.shape == (8, 8)
    eigs = np.linalg.eigvalsh(E8m)
    p = sum(e > 1e-9 for e in eigs)
    q = sum(e < -1e-9 for e in eigs)
    assert p == 0 and q == 8, f"E_8(-1) signature should be (0, 8), got ({p}, {q})"
    # E_8 is unimodular: det = 1 for E_8, so det(E_8(-1)) = (-1)^8 = 1.
    assert abs(np.linalg.det(E8m) - 1.0) < 1e-7, f"det(E_8(-1)) = {np.linalg.det(E8m)}"


def test_mukai_gram_signature_4_20():
    G = mukai_gram_form()
    assert G.shape == (24, 24)
    sig_data = verify_mukai_signature_and_unimodularity(G)
    assert sig_data['signature'] == (4, 20), \
        f"Mukai signature should be (4, 20), got {sig_data['signature']}"
    assert sig_data['rank'] == 24
    assert sig_data['is_unimodular'], f"Mukai not unimodular: det = {sig_data['det']}"
    assert sig_data['is_even'], "Mukai should be even unimodular"
    assert sig_data['is_consistent']


def test_mukai_gram_is_symmetric():
    G = mukai_gram_form()
    assert np.allclose(G, G.T), "Mukai Gram form must be symmetric"


def test_mukai_gram_diagonal_even():
    """II_{4,20} is an even lattice: all diagonal entries should be even."""
    G = mukai_gram_form()
    for i in range(G.shape[0]):
        assert abs(G[i, i] - round(G[i, i])) < 1e-9, \
            f"G[{i},{i}] = {G[i, i]} not integer"
        assert int(round(G[i, i])) % 2 == 0, \
            f"G[{i},{i}] = {G[i, i]} not even"


# =========================================================================
# 2. K3-HEISENBERG BAR WINDOWS
# =========================================================================


def test_bar_window_q1_has_24_generators():
    G = mukai_gram_form()
    K1 = k3_heisenberg_bar_window(G, q=1)
    assert isinstance(K1, BarWindow)
    assert K1.q == 1
    assert K1.content['generators']['count'] == 24


def test_bar_window_q2_carries_gram():
    G = mukai_gram_form()
    K2 = k3_heisenberg_bar_window(G, q=2)
    assert K2.q == 2
    assert 'binary_residue' in K2.content
    assert np.allclose(K2.content['binary_residue']['gram'], G)
    assert K2.content['binary_residue']['signature'] == 4


def test_bar_window_q3_is_trivial_extension():
    G = mukai_gram_form()
    K3 = k3_heisenberg_bar_window(G, q=3)
    assert K3.q == 3
    assert 'cubic_residue' in K3.content
    assert K3.content['cubic_residue']['is_trivial_extension']
    assert K3.content['cubic_residue']['cofree_coalgebra_only']
    assert K3.content['cubic_residue']['gram_cubic'] is None


# =========================================================================
# 3. YANGIAN r-MATRIX JETS
# =========================================================================


def test_k3_heisenberg_rmatrix_only_z_inv_jet():
    G = mukai_gram_form()
    rmat = k3_heisenberg_yangian_rmatrix(G)
    assert isinstance(rmat, RMatrixJets)
    assert rmat.all_orders() == [1], \
        f"K3-Heisenberg should have only z^{{-1}} jet, got {rmat.all_orders()}"
    jet1 = rmat.get_jet(1)
    assert np.allclose(jet1, G), \
        "z^{-1} jet should equal the Mukai Gram form (Casimir)"


def test_rmatrix_jet_pole_shift_by_one():
    r"""AP19: OPE pole order n -> r-matrix jet z^{-(n-1)}.

    For K3-Heisenberg, OPE has only n = 2, so r-matrix has only z^{-1}.
    """
    G = mukai_gram_form()
    rmat = k3_heisenberg_yangian_rmatrix(G)
    # Only z^{-1} jet, corresponding to OPE pole n=2.
    assert 1 in rmat.jets
    assert 2 not in rmat.jets


# =========================================================================
# 4. JET PRINCIPLE VERIFICATION
# =========================================================================


def test_jet_principle_k3_heisenberg_vacuously_passes():
    verdict = verify_jet_principle_k3_heisenberg()
    assert isinstance(verdict, JetPrincipleVerdict)
    assert verdict.passes, \
        f"K3-Heisenberg jet principle should pass (vacuously), got {verdict}"
    assert verdict.jet_pole_shift_verified
    assert verdict.K3_heisenberg_class == 'G'
    assert 'Gaussian' in verdict.triviality_reason
    assert 'vacuous' in verdict.triviality_reason.lower() or \
           'VACUOUSLY' in verdict.triviality_reason.upper()


def test_jet_principle_k3_heisenberg_details():
    verdict = verify_jet_principle_k3_heisenberg()
    d = verdict.details
    assert d['mukai_signature'] == (4, 20)
    assert d['mukai_rank'] == 24
    assert d['mukai_unimodular']
    assert d['K2_match_jet1']
    assert d['K3_cubic_trivial']
    assert 1 in d['jet_orders_present']


# =========================================================================
# 5. CROSS-CHECK ON sl_2_hat
# =========================================================================


def test_jet_principle_sl2_hat_vacuously_passes():
    verdict = verify_jet_principle_sl2_hat()
    assert verdict.K3_heisenberg_class == 'L'
    # Passes because no z^{-2} jet exists.
    assert verdict.passes
    assert verdict.jet_pole_shift_verified
    assert verdict.non_gaussian_extension_open


def test_sl2_hat_casimir_in_K2():
    verdict = verify_jet_principle_sl2_hat()
    Omega_K2 = np.array(verdict.details['K2_Omega'])
    jet1 = np.array(verdict.details['jet1'])
    assert np.allclose(Omega_K2, jet1)


# =========================================================================
# 6. VIRASORO ADVERSARIAL TEST: GAP NAMING
# =========================================================================


def test_virasoro_naive_jet_principle_fails():
    status = virasoro_jet_principle_status()
    assert status['OPE_poles'] == [4, 2, 1]
    assert status['r_matrix_jets'] == [-3, -1, 0]
    # The naive jet principle fails at q = 3 because K_3 cubic shadow
    # does not correspond to a z^{-2} jet.
    assert 'FAILS' in status['naive_jet_principle_at_q3']
    assert status['open_for_class_M']
    # The reformulation invokes Drinfeld's spectral filtration on the Yangian.
    refor = status['reformulation_needed']
    assert 'Drinfeld' in refor and 'spectral filtration' in refor.lower()


# =========================================================================
# 7. FULL REPORT
# =========================================================================


def test_f7_full_report_structure():
    report = f7_grand_completion_jet_principle_report()
    assert 'sub_conjecture' in report
    assert 'witnesses' in report
    assert 'K3_Heisenberg' in report['witnesses']
    assert 'sl_2_hat' in report['witnesses']
    assert 'Virasoro' in report['witnesses']
    assert 'PARTIAL' in report['overall_status']
    # The jet principle in its naive z^{-q} form is corrected.
    assert 'corrected from the naive z^{-q} reading' in report['sub_conjecture']
    assert len(report['honest_gaps']) >= 4
    # Licensing tags present
    assert any('beta' in tag for tag in report['licensing_tags'])
    assert any('gamma' in tag for tag in report['licensing_tags'])
    assert any('delta' in tag for tag in report['licensing_tags'])


def test_f7_report_records_AP19_shift():
    report = f7_grand_completion_jet_principle_report()
    honest_gaps = report['honest_gaps']
    # The off-by-one must be one of the honest gaps.
    assert any('OFF BY' in gap and 'AP19' in gap for gap in honest_gaps), \
        f"AP19 off-by-one gap not recorded: {honest_gaps}"


def test_f7_report_recommends_reformulation():
    report = f7_grand_completion_jet_principle_report()
    rec = report['frontier_recommendation']
    assert 'Drinfeld spectral filtration' in rec
    assert 'ConjecturedOpen' in rec or 'Conjectured' in rec
    # The K3-Heisenberg witness is named as degenerate.
    assert 'degenerate' in rec.lower() or 'not discriminating' in rec
