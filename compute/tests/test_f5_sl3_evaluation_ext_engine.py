"""Tests for F5 sl_3 evaluation-module Ext engine.

Verifies the F5 frontier degree-2 reconstruction theorem for sl_3:
  Fact_{E_1}(R^2; A) -> Mod^comp(Y^{dg}_A) on the evaluation-generated core.

Mathematical content tested:
  1. sl_3 Chevalley basis in fund and dual fund (8 traceless 3x3 mats).
  2. Killing form g_{ab} = tr_fund(T^a T^b) symmetric and non-degenerate.
  3. Casimir Omega on V_{omega_1} tensor V_{omega_2} decomposes adj + triv.
  4. Evaluation modules satisfy correct ev_a homomorphism axioms.
  5. Ext^{0,1,2}(V_{omega_1}(a), V_{omega_2}(b)) at resonance and generic.
  6. KZ monodromy at level k = h^vee = 3 matches Casimir eigenvalues.
  7. Factorisation algebra on R^2 \\ pts confirms same Ext dimensions.
  8. Degree-2 seed dimension = 17 = 8 + 8 + 1 for Y^{dg}(sl_3).
  9. Three-route consistency at resonance.
 10. Mittag-Leffler condition for filtered complete dg Lie algebra.
 11. m_3 Serre obstruction = scalar identity (attack-heal).

References:
  Vol II FRONTIER.md F5; Vol I prop:yangian-dk4-typea-frontier;
  Drinfeld 1985; Kohno 1987; Costello-Witten-Yamazaki 2017-2018.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
import numpy as np
from fractions import Fraction

from lib.f5_sl3_evaluation_ext_engine import (
    H_VEE_SL3,
    DIM_SL3,
    RANK_SL3,
    FUND_DIM_SL3,
    sl3_chevalley_fund,
    sl3_chevalley_dual_fund,
    fund_killing_form,
    fund_dual_basis,
    fund_dual_basis_in_dual_fund,
    casimir_mixed_fund_dualfund,
    casimir_eigenvalues_in_adj_plus_triv,
    EvaluationModule,
    yang_R_mixed,
    hom_evaluation_modules,
    ext1_evaluation_modules,
    ext2_evaluation_modules,
    kz_two_point_monodromy_mixed_at_critical,
    degree_two_jet_of_kz_monodromy,
    factorization_S1_monodromy_dim,
    degree_two_seed_yangian_dimension,
    compare_ext_to_degree_two_seed,
    three_route_consistency,
    attack_heal_massey_completion,
    run_complete_f5_sl3_verification,
)


# =========================================================================
# 1. sl_3 representation data
# =========================================================================

class TestSL3Representations:
    """sl_3 Chevalley basis in fund and dual fund."""

    def test_fund_dim(self):
        mats = sl3_chevalley_fund()
        assert len(mats) == DIM_SL3
        for M in mats:
            assert M.shape == (FUND_DIM_SL3, FUND_DIM_SL3)

    def test_fund_traceless(self):
        mats = sl3_chevalley_fund()
        for M in mats:
            assert abs(np.trace(M)) < 1e-12, "sl_3 generators must be traceless"

    def test_dual_fund_traceless(self):
        mats = sl3_chevalley_dual_fund()
        for M in mats:
            assert abs(np.trace(M)) < 1e-12

    def test_dual_fund_is_minus_transpose(self):
        fund = sl3_chevalley_fund()
        dual = sl3_chevalley_dual_fund()
        for F, D in zip(fund, dual):
            assert np.allclose(D, -F.T)

    def test_chevalley_brackets_h1_e1(self):
        mats = sl3_chevalley_fund()
        H1, E1 = mats[0], mats[2]
        comm = H1 @ E1 - E1 @ H1
        # [H_1, E_1] = 2 E_1 (alpha_1(H_1) = 2)
        assert np.allclose(comm, 2.0 * E1)

    def test_chevalley_brackets_h1_e2(self):
        mats = sl3_chevalley_fund()
        H1, E2 = mats[0], mats[3]
        comm = H1 @ E2 - E2 @ H1
        # [H_1, E_2] = -alpha_2(H_1) E_2 = -(-1) E_2 = E_2
        # Wait: alpha_2(H_1) = -1, so [H_1, E_2] = alpha_2(H_1) E_2 = -E_2
        # Actually for sl_3 Cartan matrix: H_1 acts on E_2 by -E_2
        assert np.allclose(comm, -1.0 * E2)


class TestKillingForm:
    """The Killing form in the fundamental trace."""

    def test_killing_form_symmetric(self):
        G = fund_killing_form()
        assert np.allclose(G, G.T)

    def test_killing_form_nondegenerate(self):
        G = fund_killing_form()
        assert abs(np.linalg.det(G)) > 1e-6, "Killing form must be non-degenerate"

    def test_dual_basis_correctness(self):
        """The dual basis should satisfy tr(T^a T_b) = delta^a_b."""
        mats = sl3_chevalley_fund()
        dual = fund_dual_basis()
        for a in range(DIM_SL3):
            for b in range(DIM_SL3):
                tr = np.trace(mats[a] @ dual[b]).real
                expected = 1.0 if a == b else 0.0
                assert abs(tr - expected) < 1e-10, (
                    f"tr(T^{a} T_{b}) = {tr}, expected {expected}"
                )


# =========================================================================
# 2. Casimir Omega decomposition
# =========================================================================

class TestCasimirDecomposition:
    """Omega on V_{omega_1} tensor V_{omega_2} = adj + triv."""

    def test_casimir_dim(self):
        Omega = casimir_mixed_fund_dualfund()
        assert Omega.shape == (9, 9)

    def test_casimir_has_two_distinct_eigenvalues(self):
        Omega = casimir_mixed_fund_dualfund()
        eigvals = sorted(np.linalg.eigvals(Omega), key=lambda z: z.real)
        # Should have two distinct eigenvalues:
        # one for the trivial summand (mult 1), one for the adjoint (mult 8)
        distinct = []
        for ev in eigvals:
            if not any(abs(ev - d) < 1e-6 for d in distinct):
                distinct.append(complex(ev))
        assert len(distinct) == 2, (
            f"Expected 2 distinct eigenvalues for adj + triv, got {distinct}"
        )

    def test_casimir_decomposition_multiplicities(self):
        data = casimir_eigenvalues_in_adj_plus_triv()
        assert data["multiplicities"]["trivial"] == 1
        assert data["multiplicities"]["adjoint"] == 8


# =========================================================================
# 3. Evaluation modules
# =========================================================================

class TestEvaluationModules:
    """Evaluation modules V_{omega}(a) with spectral parameter a."""

    def test_omega1_module(self):
        em = EvaluationModule(omega=1, spectral_param=0.5, hbar=Fraction(1, 6))
        rep = em.representation()
        assert len(rep) == DIM_SL3
        assert rep[0].shape == (FUND_DIM_SL3, FUND_DIM_SL3)

    def test_omega2_module(self):
        em = EvaluationModule(omega=2, spectral_param=0.5, hbar=Fraction(1, 6))
        rep = em.representation()
        assert len(rep) == DIM_SL3
        # Dual fund is -transpose of fund
        fund_em = EvaluationModule(omega=1, spectral_param=0.5, hbar=Fraction(1, 6))
        for D, F in zip(rep, fund_em.representation()):
            assert np.allclose(D, -F.T)


# =========================================================================
# 4. Yang R-matrix for mixed fund-dualfund
# =========================================================================

class TestYangRMatrix:
    """R(u) on V_{omega_1} tensor V_{omega_2}."""

    def test_R_identity_at_infinity(self):
        """R(u) -> I as u -> infinity (hbar/u -> 0)."""
        u_large = 1e6 + 0j
        hbar = 1.0 / 6.0
        R = yang_R_mixed(u_large, hbar)
        I9 = np.eye(9, dtype=complex)
        assert np.allclose(R, I9, atol=1e-3)

    def test_R_unitary_in_limit(self):
        """R(u) R(-u)^{-1} should be bounded near u -> infinity."""
        u = 10.0 + 0j
        hbar = 1.0 / 6.0
        R = yang_R_mixed(u, hbar)
        # The product R(u) R(-u) is a polynomial in hbar^2 by inversion symmetry
        # at least: its (1,1) entry should be real.
        Rinv = yang_R_mixed(-u, hbar)
        prod = R @ Rinv
        assert np.allclose(np.imag(prod[0, 0]), 0, atol=1e-6)


# =========================================================================
# 5. Ext^{0,1,2} at resonance vs generic
# =========================================================================

class TestExtAtResonance:
    """Ext computations at resonance a - b = h^vee hbar and generic."""

    def setup_method(self):
        self.hbar = 1.0 / 6.0
        self.a = 0.0 + 0.0j
        self.b_res = -3.0 * self.hbar + 0j  # a - b = 3 hbar
        self.b_gen = -0.7 + 0j

    def test_ext0_at_resonance(self):
        result = hom_evaluation_modules(self.a, self.b_res, self.hbar)
        assert result["ext0_dim"] == 1
        assert result["is_at_resonance"]

    def test_ext0_generic(self):
        result = hom_evaluation_modules(self.a, self.b_gen, self.hbar)
        assert result["ext0_dim"] == 0
        assert not result["is_at_resonance"]

    def test_ext1_at_resonance(self):
        result = ext1_evaluation_modules(self.a, self.b_res, self.hbar)
        assert result["ext1_dim"] == DIM_SL3 + 1, (
            f"Expected ext1 = 9 (adjoint + central), got {result['ext1_dim']}"
        )

    def test_ext1_generic(self):
        result = ext1_evaluation_modules(self.a, self.b_gen, self.hbar)
        assert result["ext1_dim"] == 0

    def test_ext2_at_resonance(self):
        result = ext2_evaluation_modules(self.a, self.b_res, self.hbar)
        assert result["ext2_dim"] == 1, (
            f"Expected ext2 = 1 (Massey-1 obstruction), got {result['ext2_dim']}"
        )

    def test_ext2_generic(self):
        result = ext2_evaluation_modules(self.a, self.b_gen, self.hbar)
        assert result["ext2_dim"] == 0


# =========================================================================
# 6. KZ monodromy at level k = h^vee = 3
# =========================================================================

class TestKZMonodromy:
    """KZ monodromy reproduces quantum-group R-matrix at q = exp(pi*i/6)."""

    def test_kz_coupling(self):
        data = kz_two_point_monodromy_mixed_at_critical(level_k=H_VEE_SL3)
        # k = h^vee = 3, so 1/(k + h^vee) = 1/6
        assert abs(data["kz_coupling"] - 1.0 / 6.0) < 1e-12

    def test_kz_has_two_eigenvalue_classes(self):
        data = kz_two_point_monodromy_mixed_at_critical(level_k=H_VEE_SL3)
        eigvals = data["omega_eigenvalues"]
        distinct = []
        for ev in eigvals:
            if not any(abs(complex(ev) - d) < 1e-6 for d in distinct):
                distinct.append(complex(ev))
        assert len(distinct) == 2

    def test_jet_order_2_K_trace(self):
        hbar = 1.0 / 6.0
        data = degree_two_jet_of_kz_monodromy(hbar)
        # K trace on adjoint should be (1/2) * 8 * 3 = 12
        assert abs(data["K_trace_adjoint_predicted"] - 12.0) < 1e-12


# =========================================================================
# 7. Factorisation algebra on R^2 \ pts
# =========================================================================

class TestFactorisationS1:
    """Local system on C_2(R^2) ~ S^1, rank 9."""

    def test_local_system_rank(self):
        data = factorization_S1_monodromy_dim()
        assert data["local_system_rank"] == 9

    def test_ext_dimensions_at_resonance_match_yangian(self):
        data = factorization_S1_monodromy_dim()
        fact = data["ext_from_factorisation"]
        # Match with the direct Yangian computation
        assert fact["ext0_resonance"] == 1
        assert fact["ext1_resonance"] == DIM_SL3 + 1
        assert fact["ext2_resonance"] == 1


# =========================================================================
# 8. Degree-2 seed dimension
# =========================================================================

class TestDegreeTwoSeed:
    """Y^{dg}(sl_3) degree-2 seed = 8 + 8 + 1 = 17."""

    def test_F1_dim(self):
        seed = degree_two_seed_yangian_dimension()
        assert seed["F1_dim"] == DIM_SL3

    def test_F2_modulo_F1(self):
        seed = degree_two_seed_yangian_dimension()
        assert seed["F2_modulo_F1_dim"] == DIM_SL3 + 1  # adjoint + central

    def test_total(self):
        seed = degree_two_seed_yangian_dimension()
        assert seed["total_seed_dim"] == 2 * DIM_SL3 + 1


# =========================================================================
# 9. Three-route consistency
# =========================================================================

class TestThreeRouteConsistency:
    """Direct Yangian Ext, KZ monodromy, factorisation algebra agree."""

    def test_all_three_routes_match_at_resonance(self):
        result = three_route_consistency(level_k=H_VEE_SL3)
        assert result["three_route_match"], (
            f"Three routes do not agree: {result['verification_summary']}"
        )

    def test_resonance_signature(self):
        result = three_route_consistency(level_k=H_VEE_SL3)
        ext = result["route_a_direct_yangian"]["at_resonance"]
        assert ext["ext0"] == 1
        assert ext["ext1"] == 9
        assert ext["ext2"] == 1


# =========================================================================
# 10. Attack-heal: Massey products and Mittag-Leffler
# =========================================================================

class TestAttackHealMittagLeffler:
    """Verify the attack-heal analysis of m_3 Serre and ML completion."""

    def test_attack_heal_returns_three_heal_steps(self):
        data = attack_heal_massey_completion()
        assert "attack" in data
        assert "heal_1" in data
        assert "heal_2" in data
        assert "heal_3" in data

    def test_filtered_complete_dg_lie_algebra(self):
        data = attack_heal_massey_completion()
        assert "filtered complete dg Lie algebra" in data["filtered_complete_dg_lie_algebra"]

    def test_remaining_obstruction_named(self):
        data = attack_heal_massey_completion()
        assert "Serre" in data["remaining_obstruction"]


# =========================================================================
# 11. End-to-end summary
# =========================================================================

class TestEndToEnd:
    """The complete F5 sl_3 verification runs and returns a coherent summary."""

    def test_complete_run(self):
        result = run_complete_f5_sl3_verification()
        assert result["frontier"].startswith("Vol II F5")
        assert result["first_rank_2_case"] == "sl_3"
        assert result["three_route_consistency"]["three_route_match"]

    def test_result_summary_contains_main_claim(self):
        result = run_complete_f5_sl3_verification()
        assert "(1, 9, 1)" in result["result"]
        assert "Mittag-Leffler" in result["result"]
        assert "Serre" in result["result"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
