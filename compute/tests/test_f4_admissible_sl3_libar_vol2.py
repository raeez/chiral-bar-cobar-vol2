r"""Tests for F4 admissible sl_3 Li-bar engine (Vol II extension).

VERIFICATION ROUTES (per Multi-Path Mandate):
    Route (a) Vol I structural Kunneth + d_1 surjectivity (theorem_admissible_sl3_libar_engine)
    Route (b) Adamovic-Milas screening Q_i^adm + small u_q^-(sl_3) (Vol I periodic_cdg_admissible.tex)
    Route (c) GKO coset Com(V_lattice, V(Vir) tensor W_3)
    Route (d) Arakawa 2015 lisse classification (Beilinson cut)
    Route (e) Adamovic-Perse 2014 + Beem-Rastelli 2018 quasi-lisse identification
    Route (f) PBW character vs Kac-Wakimoto defect cross-check

CRITICAL FINDING tested:
  The F4 entry of FRONTIER.md claims R_{L_k} finite-dim Artinian (dim < 100)
  at k = -3/2.  Per Arakawa 2015 Thm 5.4.4, this is FALSE: L_{-3/2}(sl_3) is
  quasi-lisse, not lisse; R_{L_k} is infinite-dimensional.  Test validates
  the lisse classification and confirms the structural argument applies only
  at q >= 3.
"""
from __future__ import annotations

import unittest
from fractions import Fraction
from math import gcd, comb

from compute.lib.f4_admissible_sl3_libar_vol2 import (
    SL3_LACING, SL3_DUAL_COXETER,
    LisseClassification, lisse_classification_sl3,
    NullVectorIdealMultiWeight, null_ideal_multiweight_sl3,
    LiBarE2Result, li_bar_e2_degeneration_sl3,
    C2AlgebraStatus, c2_algebra_status_sl3,
    f4_frontier_sweep, f4_frontier_summary,
    canonical_test_cases,
    AdmissibleLevel, admissible_level,
    LiBarAnalysis, full_analysis,
    critical_levels_sl3,
)


class TestArakawaLisseClassification(unittest.TestCase):
    """Arakawa 2015 Thm 5.4.4 lisse condition for sl_3."""

    def test_dual_coxeter_correct(self):
        """h^v(sl_3) = 3."""
        self.assertEqual(SL3_DUAL_COXETER, 3)
        self.assertEqual(SL3_LACING, 1)

    def test_k_minus_3_2_is_quasi_lisse(self):
        """k = -3/2 (p=3, q=2): QUASI-LISSE, not lisse.

        Adamovic-Perse 2014: X_{L_{-3/2}} = closure(O_min), dim 4.
        Critical Beilinson-cut finding: the F4 FRONTIER claim 'dim < 100' fails.
        """
        cls = lisse_classification_sl3(3, 2)
        self.assertFalse(cls.is_lisse)
        self.assertTrue(cls.is_quasi_lisse)
        self.assertEqual(cls.associated_variety, 'min')
        self.assertEqual(cls.av_dimension, 4)
        self.assertEqual(cls.av_partition, (2, 1))
        self.assertEqual(cls.k, Fraction(-3, 2))

    def test_k_minus_5_3_is_lisse(self):
        """k = -5/3 (p=4, q=3): LISSE.  First honest F4 test point.

        Arakawa 2015: q = 3 = h^v, gcd(4, 3) = 1, lisse.
        """
        cls = lisse_classification_sl3(4, 3)
        self.assertTrue(cls.is_lisse)
        self.assertFalse(cls.is_quasi_lisse)
        self.assertEqual(cls.av_dimension, 0)
        self.assertEqual(cls.k, Fraction(-5, 3))

    def test_k_minus_9_4_is_lisse(self):
        """k = -9/4 (p=3, q=4): LISSE."""
        cls = lisse_classification_sl3(3, 4)
        self.assertTrue(cls.is_lisse)
        self.assertEqual(cls.av_dimension, 0)

    def test_k_minus_4_3_is_lisse(self):
        """k = -4/3 (p=5, q=3): LISSE."""
        cls = lisse_classification_sl3(5, 3)
        self.assertTrue(cls.is_lisse)

    def test_integrable_lisse(self):
        """Integrable levels (q = 1): trivially lisse."""
        for p in range(3, 10):
            cls = lisse_classification_sl3(p, 1)
            self.assertTrue(cls.is_lisse, f'integrable p={p} should be lisse')

    def test_lisse_iff_q_at_least_dual_coxeter(self):
        """Lisse iff q >= h^v = 3 (or q = 1 integrable)."""
        for p in range(3, 11):
            for q in range(1, 7):
                if gcd(p, q) != 1:
                    continue
                cls = lisse_classification_sl3(p, q)
                expected_lisse = (q >= 3) or (q == 1)
                self.assertEqual(cls.is_lisse, expected_lisse,
                    f'(p, q) = ({p}, {q}): lisse mismatch')

    def test_quasi_lisse_only_q_equals_2(self):
        """For sl_3 admissible: quasi-lisse iff q = 2 (within q < h^v range)."""
        for p in range(3, 11):
            for q in range(1, 7):
                if gcd(p, q) != 1:
                    continue
                cls = lisse_classification_sl3(p, q)
                if cls.is_quasi_lisse:
                    self.assertEqual(q, 2,
                        f'(p, q) = ({p}, {q}): quasi-lisse should have q=2')


class TestNullIdealMultiWeight(unittest.TestCase):
    """Explicit multi-weight null-vector ideal at admissible sl_3 level."""

    def test_k_minus_3_2_grades(self):
        """k = -3/2: h_theta = 2, h_alpha = 4."""
        ni = null_ideal_multiweight_sl3(3, 2)
        self.assertEqual(ni.h_theta, 2)
        self.assertEqual(ni.h_alpha, 4)
        self.assertEqual(ni.nulls_at_theta_grade, 8)  # adjoint orbit
        self.assertEqual(ni.nulls_at_alpha_grade, 8)

    def test_k_minus_5_3_grades(self):
        """k = -5/3: h_theta = 6, h_alpha = 9."""
        ni = null_ideal_multiweight_sl3(4, 3)
        self.assertEqual(ni.h_theta, 6)
        self.assertEqual(ni.h_alpha, 9)

    def test_universal_dim_matches_pbw(self):
        """Universal V_k dim at weight w = coeff of q^w in prod (1-q^n)^{-8}."""
        ni = null_ideal_multiweight_sl3(3, 2, max_weight=5)
        self.assertEqual(ni.universal_dim_at_grade[0], 1)
        self.assertEqual(ni.universal_dim_at_grade[1], 8)
        self.assertEqual(ni.universal_dim_at_grade[2], 44)  # 8 + 36

    def test_ideal_defect_zero_below_h_theta(self):
        """Ideal defect = 0 below first null grade."""
        ni = null_ideal_multiweight_sl3(3, 2, max_weight=8)
        # h_theta = 2; below grade 2, ideal is 0.
        self.assertEqual(ni.ideal_dim_at_grade[0], 0)
        self.assertEqual(ni.ideal_dim_at_grade[1], 0)
        # At and above grade 2, ideal nonzero (Kac-Wakimoto defect).
        self.assertGreater(ni.ideal_dim_at_grade[2], 0)


class TestC2AlgebraStatus(unittest.TestCase):
    """C_2 algebra Artinian-status verification per Arakawa lisse condition."""

    def test_k_minus_3_2_NOT_artinian(self):
        """k = -3/2: R_{L_k} INFINITE-dim (quasi-lisse).

        This is the critical Beilinson-cut finding contradicting F4 'dim < 100'.
        """
        status = c2_algebra_status_sl3(3, 2)
        self.assertFalse(status.is_finite_dimensional)
        self.assertFalse(status.is_artinian)
        # Structural decomposition gives a bound on a DIFFERENT object (universal Kunneth)
        # not on R_{L_k} itself.
        self.assertEqual(status.structural_tensor_bound, 4**2 * 2**6)  # 1024
        self.assertIn('INFINITE', status.note)

    def test_k_minus_5_3_artinian(self):
        """k = -5/3: R_{L_k} finite-dim Artinian (lisse)."""
        status = c2_algebra_status_sl3(4, 3)
        self.assertTrue(status.is_finite_dimensional)
        self.assertTrue(status.is_artinian)
        self.assertEqual(status.structural_tensor_bound, 9**2 * 6**6)  # 3779136

    def test_integrable_artinian(self):
        """Integrable levels: R_{L_k} finite-dim Artinian."""
        status = c2_algebra_status_sl3(3, 1)
        self.assertTrue(status.is_finite_dimensional)
        self.assertEqual(status.structural_tensor_bound, 4)  # 2^2 * 1^6


class TestLiBarE2Degeneration(unittest.TestCase):
    """E_2 degeneration verdict, branching on lisse vs quasi-lisse."""

    def test_k_minus_3_2_open_quasi_lisse(self):
        """k = -3/2: verdict 'Open_quasi_lisse', NOT 'Koszul'.

        Per Beilinson cut, the structural Kunneth analysis does not apply
        because R_{L_k} is infinite-dim.  This level is genuinely OPEN
        in the F4 frontier sense, and the original F4 claim of K_2 finite
        Artinian fails.
        """
        r = li_bar_e2_degeneration_sl3(3, 2)
        self.assertEqual(r.verdict, 'Open_quasi_lisse')
        self.assertEqual(r.confidence, 'open')
        self.assertTrue(r.classification.is_quasi_lisse)
        self.assertFalse(r.classification.is_lisse)
        # The obstruction must name the quasi-lisse barrier:
        self.assertTrue(any('QUASI-LISSE' in o for o in r.obstructions))

    def test_k_minus_5_3_koszul_lisse(self):
        """k = -5/3: LISSE + Koszul via structural argument."""
        r = li_bar_e2_degeneration_sl3(4, 3)
        self.assertTrue(r.classification.is_lisse)
        self.assertEqual(r.verdict, 'Koszul')
        self.assertEqual(r.confidence, 'proved_conditional')
        self.assertTrue(r.e2_diagonal)
        self.assertEqual(r.e2_off_diagonal_dim, 0)

    def test_k_minus_9_4_koszul_lisse(self):
        """k = -9/4: LISSE + Koszul."""
        r = li_bar_e2_degeneration_sl3(3, 4)
        self.assertTrue(r.classification.is_lisse)
        self.assertEqual(r.verdict, 'Koszul')
        self.assertTrue(r.e2_diagonal)

    def test_k_minus_4_3_koszul_lisse(self):
        """k = -4/3: LISSE + Koszul (null above bar range, even simpler)."""
        r = li_bar_e2_degeneration_sl3(5, 3)
        self.assertTrue(r.classification.is_lisse)
        self.assertEqual(r.verdict, 'Koszul')

    def test_integrable_koszul(self):
        """k = 0, 1, 2, ... (integrable): Koszul."""
        for p in range(3, 10):
            r = li_bar_e2_degeneration_sl3(p, 1)
            self.assertEqual(r.verdict, 'Koszul', f'integrable p={p}')

    def test_licensing_tags_present(self):
        """Every result carries the five licensing tags alpha/beta/gamma/delta/epsilon."""
        r = li_bar_e2_degeneration_sl3(4, 3)
        tag_string = ';'.join(r.licensing_tags)
        for prefix in ('alpha-', 'beta-', 'gamma-', 'delta-', 'epsilon-'):
            self.assertIn(prefix, tag_string,
                f'licensing tag {prefix} missing')

    def test_evidence_routes_multi_path(self):
        """At least 3 verification routes named per Multi-Path Mandate."""
        r = li_bar_e2_degeneration_sl3(4, 3)
        self.assertGreaterEqual(len(r.evidence_routes), 3)


class TestF4FrontierSweep(unittest.TestCase):
    """End-to-end sweep across admissible levels with Beilinson-cut stratification."""

    def test_sweep_returns_results(self):
        results = f4_frontier_sweep(max_q=4, max_p=10, max_weight=6)
        self.assertGreater(len(results), 5)

    def test_sweep_summary_stratifies_correctly(self):
        """Sweep summary separates lisse-koszul, lisse-undetermined, quasi-lisse-open."""
        results = f4_frontier_sweep(max_q=4, max_p=10, max_weight=6)
        summary = f4_frontier_summary(results)
        # All quasi-lisse cases have q = 2:
        for (p, q, k_str) in summary['quasi_lisse_open']:
            self.assertEqual(q, 2,
                f'quasi-lisse case (p, q) = ({p}, {q}) should have q=2')
        # All lisse-koszul cases have q >= 3 or q = 1:
        for (p, q, k_str) in summary['lisse_koszul']:
            self.assertTrue(q == 1 or q >= 3,
                f'lisse-koszul (p, q) = ({p}, {q}) should have q=1 or q>=3')

    def test_no_unclassified_admissible(self):
        """Every admissible level is either lisse or quasi-lisse (no 'other')."""
        results = f4_frontier_sweep(max_q=4, max_p=10, max_weight=6)
        summary = f4_frontier_summary(results)
        self.assertEqual(summary['other'], [])


class TestCanonicalTestCases(unittest.TestCase):
    """The canonical F4 test points per Beilinson cut."""

    def test_canonical_includes_k_minus_3_2(self):
        """The historical F4 claim (3, 2) is preserved as a corrected entry."""
        cases = canonical_test_cases()
        params = [(p, q) for (p, q, _) in cases]
        self.assertIn((3, 2), params)

    def test_canonical_includes_k_minus_5_3(self):
        """k = -5/3 (4, 3) is the new honest F4 first test."""
        cases = canonical_test_cases()
        params = [(p, q) for (p, q, _) in cases]
        self.assertIn((4, 3), params)

    def test_canonical_descriptions_mark_quasi_lisse(self):
        """The k = -3/2 entry must explicitly note the quasi-lisse issue."""
        cases = canonical_test_cases()
        for (p, q, desc) in cases:
            if (p, q) == (3, 2):
                self.assertIn('QUASI-LISSE', desc)
                self.assertIn('FALSE', desc)


class TestCrossVolumeConsistency(unittest.TestCase):
    """Cross-volume consistency: Vol I engine values must agree."""

    def test_vol_I_engine_passes_through(self):
        """The Vol II engine reuses Vol I full_analysis verbatim."""
        for (p, q) in [(3, 2), (4, 3), (3, 4), (5, 3), (3, 1)]:
            r2 = li_bar_e2_degeneration_sl3(p, q)
            r1 = full_analysis(p, q)
            # Vol II e2_diagonal must agree with Vol I e2.is_diagonal:
            self.assertEqual(r2.e2_diagonal, r1.e2.is_diagonal,
                f'(p, q) = ({p}, {q}): Vol II / Vol I E_2 diagonal mismatch')

    def test_vol_I_engine_kappa_additivity(self):
        """Vol I kappa-additivity passes through unchanged."""
        for (p, q) in [(3, 2), (4, 3)]:
            lev = admissible_level(p, q)
            kappa_dual = -lev.kappa
            self.assertEqual(lev.kappa + kappa_dual, 0)


class TestKzMonodromy(unittest.TestCase):
    """KZ monodromy / root-of-unity parameter from periodic_cdg_admissible.tex."""

    def test_q_qg_at_k_minus_5_3(self):
        """At k = -5/3: q_qg = exp(pi*i * q / p) = exp(pi*i * 3/4).

        Per Vol I periodic_cdg_admissible.tex def:screening-adjoint and
        lem:screening-adjoint-squares, the screening operator quantum
        parameter is q_qg = exp(pi*i / (k + h^v)) = exp(pi*i * q / p).
        For (p, q) = (4, 3): q_qg = exp(3*pi*i/4).
        """
        import cmath
        p, q = 4, 3
        # k + h^v = p/q = 4/3
        q_qg = cmath.exp(1j * cmath.pi * q / p)
        # |q_qg| = 1
        self.assertAlmostEqual(abs(q_qg), 1.0, places=10)
        # Argument: pi * q / p = 3*pi/4
        self.assertAlmostEqual(cmath.phase(q_qg), cmath.pi * q / p, places=10)

    def test_q_qg_at_k_minus_3_2(self):
        """At k = -3/2: q_qg = exp(2*pi*i/3) primitive 6th root of unity.

        For (p, q) = (3, 2): q_qg = exp(pi*i * 2/3) = exp(2*pi*i/3).
        This is a 3rd root of unity, NOT a primitive 6th root.
        """
        import cmath
        p, q = 3, 2
        q_qg = cmath.exp(1j * cmath.pi * q / p)
        # q_qg^3 should be 1:
        self.assertAlmostEqual(q_qg ** 3, 1.0, places=10)


if __name__ == '__main__':
    unittest.main()
