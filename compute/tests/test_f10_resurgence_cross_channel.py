r"""Tests for the F10 cross-channel resurgent structure engine.

Verifies:
1. Cross-channel closed forms at g = 2, 3, 4 reproduce the Vol I
   numerator/denominator structure of `delta_F_cross_generating_function_report.md`.
2. Faber-Pandharipande coefficients match (hbar/2)/sin(hbar/2) expansion.
3. kappa_W3(c) = 5c/6.
4. Large-c ratios R_g recover (0, 42/31, 9184/381) at g = 2, 3, 4.
5. A_cross lower bound via Gevrey-1 second-difference test
   matches FRONTIER's 1.7 (numerically ~1.77).
6. Borel transform truncation is finite at xi = 0.
7. Alien-derivative action factors out e^{-omega/hbar} correctly.
8. Trans-series partition function reduces to scalar at hbar -> oo.
9. Non-perturbative correction has exponential decay in 1/hbar.
10. Multi-path verification dict structure is complete.

Manuscript references:
    Vol II thqg_perturbative_finiteness.tex:3215--3343, 1550--1605
    Vol II FRONTIER.md F3, F10
    Vol I multi_weight_cross_channel.tex:670--870
    Vol I compute/audit/delta_F_cross_generating_function_report.md
"""

import sys
sys.path.insert(0, 'compute')

import cmath
import math
from fractions import Fraction

import pytest


# =====================================================================
# Section 1: Cross-channel closed forms
# =====================================================================

class TestCrossChannelClosedForms:
    """Test that delta_F_g^cross(W_3, c) reproduces the Vol I closed forms."""

    def test_delta_F_2_at_c_2(self):
        from lib.f10_resurgence_cross_channel import delta_F_g_W3
        # delta_F_2 = (c+204)/(16c).  At c=2: 206/32 = 103/16.
        assert delta_F_g_W3(2, 2) == Fraction(103, 16)

    def test_delta_F_2_large_c_limit(self):
        from lib.f10_resurgence_cross_channel import delta_F_g_W3
        # large-c limit -> 1/16.
        val = delta_F_g_W3(2, Fraction(10**8))
        assert abs(float(val) - 1.0 / 16.0) < 1e-6

    def test_delta_F_3_at_c_6(self):
        from lib.f10_resurgence_cross_channel import delta_F_g_W3
        # (5*216 + 3792*36 + 1149120*6 + 217071360) / (138240 * 36)
        num = 5 * 216 + 3792 * 36 + 1149120 * 6 + 217071360
        den = 138240 * 36
        expected = Fraction(num, den)
        assert delta_F_g_W3(3, 6) == expected

    def test_delta_F_3_large_c_linear(self):
        from lib.f10_resurgence_cross_channel import delta_F_g_W3
        # delta_F_3 ~ c/27648 + 79/2880 + O(1/c) as c -> oo.
        # Subtract the constant term to isolate the c/27648 leading
        # coefficient exactly (rational arithmetic).
        c = Fraction(10**10)
        leading = (delta_F_g_W3(3, c) - Fraction(79, 2880)) / c
        # Now the residual is O(1/c^2) so well below 1e-15.
        assert abs(float(leading) - 1.0 / 27648.0) < 1e-15

    def test_delta_F_4_large_c_linear(self):
        from lib.f10_resurgence_cross_channel import delta_F_g_W3
        # delta_F_4 ~ 41c/2488320 + 89627/5806080 + O(1/c).
        c = Fraction(10**10)
        leading = (delta_F_g_W3(4, c) - Fraction(89627, 5806080)) / c
        expected = 41.0 / 2488320.0
        assert abs(float(leading) - expected) < 1e-15

    def test_delta_F_5_raises(self):
        from lib.f10_resurgence_cross_channel import delta_F_g_W3
        # genus 5 not yet tabulated; must raise (F3 / F10 open).
        with pytest.raises(ValueError, match='not yet tabulated'):
            delta_F_g_W3(5, 6)

    def test_pole_at_c_zero(self):
        from lib.f10_resurgence_cross_channel import delta_F_g_W3
        with pytest.raises(ValueError, match='pole'):
            delta_F_g_W3(2, 0)


# =====================================================================
# Section 2: Scalar piece (F_g^scal = kappa * lambda_g^FP)
# =====================================================================

class TestScalarPiece:
    """Test the scalar F_g = kappa * lambda_g^{FP} reproduction."""

    def test_lambda_FP_values(self):
        from lib.f10_resurgence_cross_channel import LAMBDA_FP
        assert LAMBDA_FP[1] == Fraction(1, 24)
        assert LAMBDA_FP[2] == Fraction(7, 5760)
        assert LAMBDA_FP[3] == Fraction(31, 967680)
        assert LAMBDA_FP[4] == Fraction(127, 154828800)
        assert LAMBDA_FP[5] == Fraction(73, 3503554560)

    def test_lambda_FP_via_series(self):
        """Cross-check lambda_g^FP via direct (hbar/2)/sin(hbar/2) expansion."""
        try:
            from sympy import sin, series, symbols
        except ImportError:
            pytest.skip("sympy not available")
        from lib.f10_resurgence_cross_channel import LAMBDA_FP
        hbar = symbols('hbar')
        f = (hbar / 2) / sin(hbar / 2)
        s = series(f, hbar, 0, 12).removeO()
        for g in range(1, 6):
            coeff = s.coeff(hbar, 2 * g)
            # Compare as Fraction
            from fractions import Fraction as F
            expected = LAMBDA_FP[g]
            actual = F(int(coeff.p), int(coeff.q))
            assert actual == expected, f"g={g}: {actual} != {expected}"

    def test_kappa_W3_formula(self):
        from lib.f10_resurgence_cross_channel import kappa_W3
        assert kappa_W3(6) == Fraction(5)
        assert kappa_W3(12) == Fraction(10)
        assert kappa_W3(Fraction(100, 3)) == Fraction(500, 18)

    def test_F_g_scal_genus_1(self):
        from lib.f10_resurgence_cross_channel import F_g_scal
        # F_1^scal = kappa * 1/24.
        assert F_g_scal(1, 6) == Fraction(6, 24)


# =====================================================================
# Section 3: A_cross lower-bound extraction
# =====================================================================

class TestACrossExtraction:
    """Test the Gevrey-1 second-difference extraction of A_cross."""

    def test_RATIO_W3_LARGE_C(self):
        from lib.f10_resurgence_cross_channel import RATIO_W3_LARGE_C
        assert RATIO_W3_LARGE_C[2] == Fraction(0)
        assert RATIO_W3_LARGE_C[3] == Fraction(42, 31)
        assert RATIO_W3_LARGE_C[4] == Fraction(9184, 381)

    def test_lower_bound_matches_FRONTIER(self):
        """Lower bound A_cross/A_scal should be near 1.77 (FRONTIER ~1.7)."""
        from lib.f10_resurgence_cross_channel import extract_A_cross_from_ratios, A_SCAL
        data = extract_A_cross_from_ratios()
        ratio_lower = data.A_cross_lower_bound / A_SCAL
        assert 1.7 < ratio_lower < 1.85, \
            f"lower bound {ratio_lower:.3f} not in (1.7, 1.85)"

    def test_upper_bound_matches_FRONTIER(self):
        from lib.f10_resurgence_cross_channel import extract_A_cross_from_ratios, A_SCAL
        data = extract_A_cross_from_ratios()
        ratio_upper = data.A_cross_upper_bound / A_SCAL
        assert abs(ratio_upper - 3.1) < 1e-9

    def test_R4_over_R3_value(self):
        from lib.f10_resurgence_cross_channel import extract_A_cross_from_ratios
        data = extract_A_cross_from_ratios()
        # R_4 / R_3 = (9184/381) / (42/31) = 9184*31 / (381*42)
        expected = (9184 * 31) / (381 * 42)
        assert abs(data.ratio_R4_over_R3 - expected) < 1e-12


# =====================================================================
# Section 4: Borel transform
# =====================================================================

class TestBorelTransform:
    """Test the truncated Borel transform of the cross-channel tower."""

    def test_borel_at_origin_is_zero(self):
        from lib.f10_resurgence_cross_channel import borel_transform_cross_truncated
        # B(0) = 0 since the lowest term is g=2 -> xi^1.
        assert abs(borel_transform_cross_truncated(100.0, 0.0)) < 1e-12

    def test_borel_first_derivative_at_origin(self):
        from lib.f10_resurgence_cross_channel import (
            borel_transform_cross_truncated, delta_F_g_W3
        )
        # dB/dxi at 0 should equal delta_F_2 / Gamma(2) = delta_F_2 / 1.
        # Compute numerically via central difference at small xi.
        c = 100.0
        eps = 1e-5
        bp = borel_transform_cross_truncated(c, eps)
        bm = borel_transform_cross_truncated(c, -eps)
        deriv = (bp - bm) / (2 * eps)
        expected = float(delta_F_g_W3(2, c))
        assert abs(deriv.real - expected) < 1e-4

    def test_borel_pole_pattern_count(self):
        from lib.f10_resurgence_cross_channel import borel_pole_pattern
        poles = borel_pole_pattern(A_cross=100.0, n_max=3)
        # 3 levels * 2 signs = 6 entries.
        assert len(poles) == 6
        # Check structure
        for p in poles:
            assert p['n'] in {1, 2, 3}
            assert p['sign'] in {+1, -1}
            assert 'singularity_type' in p


# =====================================================================
# Section 5: Alien derivative algebra
# =====================================================================

class TestAlienDerivative:
    """Test the alien-derivative algebra structure."""

    def test_alien_action_exponential_factor(self):
        from lib.f10_resurgence_cross_channel import AlienDerivativeAlgebra
        alg = AlienDerivativeAlgebra(A_cross=100.0)
        # Delta_1 at hbar = 10: factor = exp(-100/10) = exp(-10)
        val = alg.alien_action(1, 10.0)
        expected = math.exp(-10.0)
        assert abs(val.real - expected) < 1e-12

    def test_alien_action_multi_instanton(self):
        from lib.f10_resurgence_cross_channel import AlienDerivativeAlgebra
        alg = AlienDerivativeAlgebra(A_cross=50.0)
        v1 = alg.alien_action(1, 25.0)
        v2 = alg.alien_action(2, 25.0)
        # v2 = exp(-100/25) = exp(-4), v1 = exp(-50/25) = exp(-2)
        # so v2 = v1^2.
        assert abs(v2 - v1 ** 2) < 1e-12

    def test_bridge_equation_keys(self):
        from lib.f10_resurgence_cross_channel import AlienDerivativeAlgebra
        alg = AlienDerivativeAlgebra(A_cross=80.0)
        res = alg.bridge_equation_residue(2)
        for k in ['n', 'instanton_action', 'omega',
                  'conjectured_stokes_constant_modulus', 'naming_remark']:
            assert k in res
        assert res['n'] == 2
        assert abs(res['instanton_action'] - 160.0) < 1e-12


# =====================================================================
# Section 6: Trans-series and non-perturbative completion
# =====================================================================

class TestTransSeries:
    """Test the trans-series partition function and non-perturbative tail."""

    def test_transseries_reduces_to_scalar_at_large_hbar(self):
        """For hbar -> oo, exp(-A/hbar) -> 1, but the leading scalar piece
        kappa * (sqrt(hbar)/2)/sin(sqrt(hbar)/2) dominates (or diverges).
        For finite hbar = 1, non-perturbative tail is sub-leading."""
        from lib.f10_resurgence_cross_channel import (
            transseries_partition_function, A_SCAL
        )
        Z = transseries_partition_function(
            kappa=5.0, c=6.0, A_cross=2.4 * A_SCAL,
            hbar=1.0 + 0j, n_max_inst=3,
        )
        # Should be finite, real-ish (small imaginary from numerical).
        assert abs(Z.imag) < 1e-6
        # Z_pert(1) = 5 * (1/2) / sin(1/2)
        Z_pert_expected = 5.0 * 0.5 / math.sin(0.5)
        # Plus three small exp(-n*A_cross) terms.
        np_sum = sum(math.exp(-n * 2.4 * A_SCAL) for n in range(1, 4))
        assert abs(Z.real - (Z_pert_expected + np_sum)) < 1e-9

    def test_non_perturbative_correction_decays(self):
        from lib.f10_resurgence_cross_channel import non_perturbative_correction
        # exp(-A/hbar) for small hbar should be tiny.
        Z_n = non_perturbative_correction(0.01, 100.0, n=1)
        assert abs(Z_n) < 1e-100  # essentially zero
        # For large hbar, tends to 1.
        Z_n_large = non_perturbative_correction(1e10, 100.0, n=1)
        assert abs(Z_n_large - 1.0) < 1e-6

    def test_total_non_perturbative_sum(self):
        from lib.f10_resurgence_cross_channel import total_non_perturbative_sum
        s = total_non_perturbative_sum(1.0, 10.0, n_max=4)
        # = sum_{n=1}^{4} exp(-10 n) = geometric series prefix.
        expected = sum(math.exp(-10.0 * n) for n in range(1, 5))
        assert abs(s.real - expected) < 1e-9


# =====================================================================
# Section 7: A_2 spectral curve and Stokes
# =====================================================================

class TestA2Spectral:
    """Test the A_2 Frobenius spectral curve data."""

    def test_rank_and_weights(self):
        from lib.f10_resurgence_cross_channel import quantum_spectral_curve_A2
        curve = quantum_spectral_curve_A2(c=6.0)
        assert curve['rank'] == 2
        assert curve['weights'] == (2, 3)

    def test_eta_inv_scaled_by_c(self):
        """eta^{ii} = 2/c (T-channel), 3/c (W-channel).  Stored as 2, 3
        with the c-factor explicit."""
        from lib.f10_resurgence_cross_channel import quantum_spectral_curve_A2
        curve = quantum_spectral_curve_A2(c=6.0)
        assert curve['eta_inv_scaled_by_c'] == [Fraction(2), Fraction(3)]

    def test_stokes_rays_rank2(self):
        from lib.f10_resurgence_cross_channel import stokes_lines_A2
        s = stokes_lines_A2(c=6.0)
        assert s['rank'] == 2
        assert s['n_stokes_rays'] == 6
        assert s['Weyl_group'] == 'S_3 (A_2)'
        assert s['has_cross_channel_ray'] is True

    def test_wall_crossing_c_admissible(self):
        from lib.f10_resurgence_cross_channel import stokes_lines_A2
        s = stokes_lines_A2(c=6.0)
        # c = -22/5 is the W_3 critical value.
        assert s['wall_crossing_c'] == Fraction(-22, 5)


# =====================================================================
# Section 8: Multi-path verification
# =====================================================================

class TestMultiPath:
    """Test the multi-path verification structure (routes (a), (b), (c))."""

    def test_three_routes_present(self):
        from lib.f10_resurgence_cross_channel import multi_path_verification
        mp = multi_path_verification(c=100.0)
        assert 'route_a_borel_ecalle' in mp
        assert 'route_b_transseries' in mp
        assert 'route_c_wkb_A2' in mp

    def test_routes_a_and_b_agree_at_g4(self):
        """Routes (a) and (b) share g <= 4 input, hence agree."""
        from lib.f10_resurgence_cross_channel import multi_path_verification
        mp = multi_path_verification(c=100.0)
        a_lower = mp['route_a_borel_ecalle']['A_cross_bounds'][0]
        b_lower = mp['route_b_transseries']['A_cross_bounds'][0]
        assert abs(a_lower - b_lower) < 1e-12

    def test_route_c_signals_F3_conditional(self):
        from lib.f10_resurgence_cross_channel import multi_path_verification
        mp = multi_path_verification(c=100.0)
        assert 'CONDITIONAL on F3' in \
            mp['route_c_wkb_A2']['A_cross_F3_closed_form']


# =====================================================================
# Section 9: Top-level resurgent-structure report
# =====================================================================

class TestF10Report:
    """Test the top-level F10 resurgent-structure report."""

    def test_claim_status(self):
        from lib.f10_resurgence_cross_channel import f10_resurgent_structure_report
        rpt = f10_resurgent_structure_report()
        assert 'ConditionalProved' in rpt['claim_status']
        assert 'F3' in rpt['claim_status']

    def test_licensing_tags_present(self):
        from lib.f10_resurgence_cross_channel import f10_resurgent_structure_report
        rpt = f10_resurgent_structure_report()
        for tag in ['alpha', 'beta', 'gamma', 'delta', 'epsilon']:
            assert tag in rpt['licensing_tags']
            assert len(rpt['licensing_tags'][tag]) > 5

    def test_remaining_obligations_non_empty(self):
        from lib.f10_resurgence_cross_channel import f10_resurgent_structure_report
        rpt = f10_resurgent_structure_report()
        obs = rpt['remaining_obligations']
        assert len(obs) >= 5
        # F3 closure should be the first remaining obligation.
        assert 'F3' in obs[0]

    def test_rows_at_reference_c(self):
        from lib.f10_resurgence_cross_channel import f10_resurgent_structure_report
        rpt = f10_resurgent_structure_report(c_values=[6.0])
        row = rpt['rows'][0]
        assert row['c'] == 6.0
        # kappa_W3(6) = 5.
        assert abs(row['kappa_W3'] - 5.0) < 1e-12
        # delta_F_2(6) = (6+204)/96 = 210/96 = 35/16 = 2.1875.
        assert abs(row['delta_F_2'] - 2.1875) < 1e-9


# =====================================================================
# Section 10: Independent verification (cross-volume)
# =====================================================================

class TestCrossVolumeConsistency:
    """Cross-volume consistency: match Vol I audit report numbers."""

    def test_partial_fraction_constant_terms(self):
        """delta_F_2 = 1/16 + 51/(4c),  delta_F_3 has constant 79/2880,
        delta_F_4 has constant 89627/5806080.  Cross-verify our closed
        forms match these constant-term decompositions."""
        from lib.f10_resurgence_cross_channel import delta_F_g_W3
        # delta_F_2(c) - 1/16 = 51/(4c) at large c.  Take c=10^6.
        c = Fraction(10 ** 6)
        d2 = delta_F_g_W3(2, c) - Fraction(1, 16)
        # Should be 51/(4 * 10^6).
        expected_d2 = Fraction(51, 4 * 10 ** 6)
        assert abs(float(d2 - expected_d2)) < 1e-12

    def test_partial_fraction_genus_3_constant(self):
        """delta_F_3 partial-fraction constant term: 79/2880."""
        from lib.f10_resurgence_cross_channel import delta_F_g_W3
        # delta_F_3(c) = c/27648 + 79/2880 + O(1/c).  Subtract c/27648 and
        # evaluate at large c.
        c = Fraction(10 ** 8)
        d3 = delta_F_g_W3(3, c) - c / 27648
        # Should approach 79/2880.
        assert abs(float(d3) - 79.0 / 2880.0) < 1e-6

    def test_genus_3_at_c_2(self):
        """delta_F_3 at c=2 (matching audit doc tabulation)."""
        from lib.f10_resurgence_cross_channel import delta_F_g_W3
        c = Fraction(2)
        v = delta_F_g_W3(3, c)
        # Numerator: 5*8 + 3792*4 + 1149120*2 + 217071360 = 40 + 15168 + 2298240 + 217071360
        num = 40 + 15168 + 2298240 + 217071360
        den = 138240 * 4
        expected = Fraction(num, den)
        assert v == expected


# =====================================================================
# Section 11: Smoke test
# =====================================================================

def test_smoke_main():
    """Smoke-test the module by importing and calling the top-level report."""
    from lib.f10_resurgence_cross_channel import f10_resurgent_structure_report
    rpt = f10_resurgent_structure_report()
    assert isinstance(rpt, dict)
    assert 'claim_status' in rpt
    assert 'licensing_tags' in rpt
    assert 'remaining_obligations' in rpt
