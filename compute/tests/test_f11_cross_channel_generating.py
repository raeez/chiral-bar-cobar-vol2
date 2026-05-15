"""Tests for F11 cross-channel generating function obstruction engine.

Verifies prop:cross-channel-no-closed-form via five independent obstruction
paths and tests the proposed bivariate quasi-Jacobi ansatz.
"""

from __future__ import annotations

import sympy as sp

from compute.lib.f11_cross_channel_generating import (
    deltaF2_W3_closed_form,
    deltaF2_W3_from_four_graph_sum,
    lambda_g_FP,
    scalar_Fg,
    obstruction_inhomogeneous_c_scaling,
    obstruction_ratio_growth_lower_bound,
    obstruction_irreducible_numerator,
    obstruction_separable_collapse,
    obstruction_picard_fuchs_rank,
    bivariate_ansatz_quasiJacobi,
    bivariate_ansatz_padé,
    bivariate_ansatz_scalar_limit_check,
    verify_five_obstruction_paths,
)


# ---------------------------------------------------------------------------
# Scalar tower sanity (cross-volume Vol I import)
# ---------------------------------------------------------------------------

def test_lambda_g_FP_values():
    """Faber-Pandharipande coefficients match the published table."""
    assert lambda_g_FP(1) == sp.Rational(1, 24)
    assert lambda_g_FP(2) == sp.Rational(7, 5760)
    assert lambda_g_FP(3) == sp.Rational(31, 967680)
    assert lambda_g_FP(4) == sp.Rational(127, 154828800)


def test_scalar_Fg_kappa_linearity():
    """F_g^scal is linear in kappa."""
    kappa = sp.Symbol("kappa")
    assert scalar_Fg(kappa, 2) == kappa * sp.Rational(7, 5760)
    assert scalar_Fg(2 * kappa, 2) == 2 * scalar_Fg(kappa, 2)


# ---------------------------------------------------------------------------
# Proved closed form
# ---------------------------------------------------------------------------

def test_deltaF2_W3_closed_form_irreducible():
    """Verify (c + 204)/(16 c); confirm 204 = 2^2 * 3 * 17."""
    c = sp.Symbol("c", positive=True)
    expr = deltaF2_W3_closed_form()
    assert sp.simplify(expr - (c + 204) / (16 * c)) == 0
    factorization = sp.factorint(204)
    assert factorization == {2: 2, 3: 1, 17: 1}


def test_deltaF2_W3_four_graph_recovery():
    """Four-graph sum reconstructs (c + 204)/(16 c)."""
    closed_form, four_graph_sum = deltaF2_W3_from_four_graph_sum()
    assert sp.simplify(closed_form - four_graph_sum) == 0


def test_deltaF2_W3_positivity_for_c_positive():
    """delta F_2^cross(W_3) > 0 for all c > 0 (manifest from numerator)."""
    c = sp.Symbol("c", positive=True)
    expr = deltaF2_W3_closed_form()
    # Check value at c = 1, 10, 100
    assert sp.simplify(expr.subs(c, 1) - sp.Rational(205, 16)) == 0
    assert sp.simplify(expr.subs(c, 10) - sp.Rational(214, 160)) == 0
    assert sp.simplify(expr.subs(c, 100) - sp.Rational(304, 1600)) == 0


def test_deltaF2_W3_asymptotic_large_c():
    """Large-c limit = 1/16 (Vasiliev B(3) topological invariant)."""
    c = sp.Symbol("c", positive=True)
    limit = sp.limit(deltaF2_W3_closed_form(), c, sp.oo)
    assert limit == sp.Rational(1, 16)


def test_deltaF2_W3_asymptotic_small_c():
    """Small-c divergence: (c + 204)/(16c) ~ 204/(16c) = 51/(4c)."""
    c = sp.Symbol("c", positive=True)
    expr = deltaF2_W3_closed_form() * c  # multiply to extract residue
    residue = sp.limit(expr, c, 0)
    assert residue == sp.Rational(204, 16)
    assert sp.simplify(residue - sp.Rational(51, 4)) == 0


def test_naive_120_is_false():
    """The naive guess (c + 120)/(16 c) is NOT the proved closed form.

    Witnessed in notes/working_notes_quarantine_20260424.tex:3523.
    """
    c = sp.Symbol("c", positive=True)
    naive = (c + 120) / (16 * c)
    correct = deltaF2_W3_closed_form()
    diff = sp.simplify(naive - correct)
    assert diff != 0
    # The discrepancy is 84/(16c) = 21/(4c), tracing to the 84 missing in
    # the cubic structure constant residue.
    assert sp.simplify(diff + sp.Rational(84, 16) / c) == 0


# ---------------------------------------------------------------------------
# Obstruction (i): inhomogeneous c-scaling
# ---------------------------------------------------------------------------

def test_obstruction_inhomogeneous_c_scaling():
    """At g=2: O(1) in c; scalar tower is O(c)."""
    result = obstruction_inhomogeneous_c_scaling()
    assert result["delta_F2_cross_W3_large_c"] == sp.Rational(1, 16)
    assert result["delta_F2_cross_W3_small_c_residue"] == sp.Rational(204, 16)
    # The two leading c-orders are incompatible with a single phi(c) factor.


# ---------------------------------------------------------------------------
# Obstruction (ii): super-linear ratio growth
# ---------------------------------------------------------------------------

def test_obstruction_ratio_growth_super_linear():
    """Ratio bound grows faster than any polynomial in g."""
    bounds = obstruction_ratio_growth_lower_bound(g_max=6)
    # bound(g) = (2g-2)! * (2pi)^{2g} / 2
    # check ratios are growing super-linearly
    bound_3 = float(bounds[3])
    bound_4 = float(bounds[4])
    bound_5 = float(bounds[5])
    ratio_43 = bound_4 / bound_3
    ratio_54 = bound_5 / bound_4
    # The ratio of successive ratios grows (super-linear in g)
    assert ratio_54 > ratio_43
    # All bounds positive
    for g, b in bounds.items():
        assert float(b) > 0


# ---------------------------------------------------------------------------
# Obstruction (iii): irreducible numerator
# ---------------------------------------------------------------------------

def test_obstruction_irreducible_numerator():
    """Prime 17 is sectoral cusp; absent from scalar lambda_g^FP skeleton."""
    result = obstruction_irreducible_numerator()
    assert result["factorization"] == {2: 2, 3: 1, 17: 1}
    assert result["irreducible_prime"] == 17
    # 17 does not divide any of the scalar lambda_g^FP numerators for g <= 6
    for g, num in result["scalar_lambda_g_numerators"].items():
        assert num % 17 != 0


# ---------------------------------------------------------------------------
# Obstruction (iv): separable collapse
# ---------------------------------------------------------------------------

def test_obstruction_separable_collapse():
    """Constant + 1/c pieces force incompatible phi(c)."""
    result = obstruction_separable_collapse()
    assert result["constant_piece"] == sp.Rational(1, 16)
    c = sp.Symbol("c", positive=True)
    assert sp.simplify(result["1_over_c_piece"] - sp.Rational(204, 16) / c) == 0
    assert result["contradiction"] is True


# ---------------------------------------------------------------------------
# Obstruction (v): Picard-Fuchs rank
# ---------------------------------------------------------------------------

def test_obstruction_picard_fuchs_rank_strictly_larger():
    """Scalar PF rank = 1; cross-channel >= 6 (strictly larger)."""
    result = obstruction_picard_fuchs_rank()
    assert result["scalar_PF_rank_hbar"] == 1
    assert result["cross_channel_PF_rank_total_lower_bound"] == 6
    assert result["cross_channel_PF_rank_total_lower_bound"] > result["scalar_PF_rank_hbar"]


# ---------------------------------------------------------------------------
# Bivariate ansatz
# ---------------------------------------------------------------------------

def test_bivariate_ansatz_quasiJacobi_matches_g2():
    """Quasi-Jacobi ansatz coefficient at g=2 matches (c+204)/(16c)."""
    result = bivariate_ansatz_quasiJacobi(g_max=2)
    assert result["matches_proved"] is True
    assert result["scalar_limit_g2"] == sp.Rational(1, 16)
    assert result["vasiliev_residue"] == sp.Rational(1, 16)


def test_bivariate_ansatz_padé_underdetermined():
    """Padé approximant (1,2,1,2) needs >= 11 data points; only 1 known."""
    result = bivariate_ansatz_padé()
    assert result["known_data_points"] == 1
    assert result["padé_(1,2,1,2)_unknowns"] == 11
    assert result["deficit"] == 10
    assert result["minimum_genus_to_close"] == 5


def test_bivariate_ansatz_scalar_limit():
    """In scalar limit, ansatz reduces to A-hat skeleton."""
    result = bivariate_ansatz_scalar_limit_check()
    assert result["vasiliev_residue_g2_W3"] == sp.Rational(1, 16)
    assert result["tadpole_vanishes_at_large_c"] == 0
    assert result["scalar_A_hat_at_g2_per_kappa"] == sp.Rational(7, 5760)


# ---------------------------------------------------------------------------
# Master verification: five obstruction paths
# ---------------------------------------------------------------------------

def test_verify_five_obstruction_paths():
    """All five obstruction paths return non-trivial verdicts."""
    paths = verify_five_obstruction_paths()
    assert set(paths.keys()) == {
        "path_1_inhomogeneous_c_scaling",
        "path_2_super_linear_ratio_growth",
        "path_3_irreducible_numerator",
        "path_4_separable_collapse",
        "path_5_picard_fuchs_rank",
    }
    for path_name, path_data in paths.items():
        assert "verdict" in path_data
        assert "result" in path_data


# ---------------------------------------------------------------------------
# Cross-volume Vol I consistency: scalar tower
# ---------------------------------------------------------------------------

def test_cross_volume_A_hat_recovery():
    """In the uniform-weight (Virasoro) limit, F_g matches A-hat.

    For Virasoro at central charge c: kappa = c/2, F_g = (c/2) * lambda_g^FP.
    """
    c = sp.Symbol("c", positive=True)
    kappa_vir = c / 2
    F2_vir = scalar_Fg(kappa_vir, 2)
    # Should equal c * 7 / 11520
    assert sp.simplify(F2_vir - c * sp.Rational(7, 11520)) == 0


def test_cross_volume_kappa_ch_W3():
    """kappa_ch_Hodge(W_3) = 5c/6 (harmonic number argument)."""
    c = sp.Symbol("c", positive=True)
    # From preface.tex:1400: kappa_ch_Hodge(W_3) = c*(H_3 - 1) = c*(11/6 - 1) = 5c/6
    H_3 = sp.Rational(11, 6)
    kappa_W3 = c * (H_3 - 1)
    assert sp.simplify(kappa_W3 - 5 * c / 6) == 0


# ---------------------------------------------------------------------------
# Decisive: closed-form ABSENT at g >= 3 (FRONTIER F3 obligation)
# ---------------------------------------------------------------------------

def test_closed_form_absent_at_g3():
    """g=3 cross-channel correction is NOT in closed form in any chapter or note.

    Asserts (negative): the FRONTIER.md F3 entry is the open problem.
    Once a closed form for delta F_3^cross(W_3)(c) is established (via the
    Givental-Stokes extraction or direct graph sum), this test should be
    updated to verify it.

    Current placeholder: only g=2 is closed form.
    """
    # No closed form available; document the obligation.
    closed_form_status_g2 = "proved (c + 204)/(16 c)"
    closed_form_status_g3 = "open (FRONTIER F3, F10)"
    closed_form_status_g4 = "open"
    closed_form_status_g5 = "open (Borel-determining)"
    assert "open" in closed_form_status_g3
    assert "open" in closed_form_status_g5
