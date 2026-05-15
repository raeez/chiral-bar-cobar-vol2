"""Tests for F6 / DK-5 / B2: reduced-resolution Yangian + filtered comparison.

Tests the f6_dk5_reduced_yangian_engine module: PBW filtration, Mittag-Leffler
witness, Khoroshkin-Tolstoy quantum double, and the three independent routes
for B2 algebraic identification.
"""

from __future__ import annotations

import sympy as sp

from compute.lib.f6_dk5_reduced_yangian_engine import (
    DrinfeldGenerator,
    YangianFilteredStage,
    khoroshkin_tolstoy_quantum_double_sl2,
    mittag_leffler_witness,
    reduced_resolution_filtered_comparison,
    route_a_beyond_eval_verma_and_dual_sl2,
    route_b_reduced_yangian_via_quantum_double,
    route_c_latyntsev_sphere,
)


# =========================================================================
# Drinfeld generators and filtration
# =========================================================================


def test_drinfeld_generator_filtration():
    """Drinfeld generator x_{i, r}^{eps} sits in PBW filtration F^{r+1}."""
    g0 = DrinfeldGenerator(i=1, r=0, eps="+")
    g1 = DrinfeldGenerator(i=1, r=1, eps="+")
    g2 = DrinfeldGenerator(i=1, r=2, eps="-")
    assert g0.filtration_degree() == 1
    assert g1.filtration_degree() == 2
    assert g2.filtration_degree() == 3


def test_yangian_filtered_stage_generator_count():
    """Y_{<= N} for sl_2 (rank 1) has 3 * 1 * N = 3N generators (E, F, H at
    each of N depths)."""
    stage = YangianFilteredStage(N=1, rank=1)
    assert stage.num_generators_at_stage() == 3
    stage = YangianFilteredStage(N=3, rank=1)
    assert stage.num_generators_at_stage() == 9


def test_yangian_filtered_stage_sl3():
    """Y_{<= N} for sl_3 (rank 2) has 3 * 2 * N = 6N generators."""
    stage = YangianFilteredStage(N=2, rank=2)
    assert stage.num_generators_at_stage() == 12
    stage = YangianFilteredStage(N=4, rank=2)
    assert stage.num_generators_at_stage() == 24


def test_yangian_filtered_stage_has_serre_at_N_2():
    """Drinfeld Serre relations enter at depth >= 2."""
    assert not YangianFilteredStage(N=0, rank=1).has_serre_relations()
    assert not YangianFilteredStage(N=1, rank=1).has_serre_relations()
    assert YangianFilteredStage(N=2, rank=1).has_serre_relations()
    assert YangianFilteredStage(N=5, rank=2).has_serre_relations()


# =========================================================================
# Mittag-Leffler property
# =========================================================================


def test_mittag_leffler_witness_sl2():
    """The PBW tower {Y_{<= N}}_N has constant transition rank
    3 * rank = 3 for sl_2; ML holds by Weibel 3.5.7 (surjective inverse
    system)."""
    stages = [YangianFilteredStage(N=k, rank=1) for k in range(0, 5)]
    witness = mittag_leffler_witness(stages)
    assert witness["mittag_leffler_status"] == "proved"
    assert witness["expected_transition_rank"] == 3
    assert all(t == 3 for t in witness["transition_ranks"])


def test_mittag_leffler_witness_sl3():
    """For sl_3 (rank 2), transition rank is 6 per step."""
    stages = [YangianFilteredStage(N=k, rank=2) for k in range(0, 4)]
    witness = mittag_leffler_witness(stages)
    assert witness["mittag_leffler_status"] == "proved"
    assert witness["expected_transition_rank"] == 6


# =========================================================================
# Khoroshkin-Tolstoy 1996 quantum double for sl_2
# =========================================================================


def test_khoroshkin_tolstoy_quantum_double_sl2():
    """Y_hbar(sl_2) = Y_hbar^-(sl_2) >< Y_hbar^+(sl_2) as quantum double.

    The minimal resolution length for rank 1 is 2 (the Koszul resolution
    of a 2-step PBW filtration)."""
    kt = khoroshkin_tolstoy_quantum_double_sl2()
    assert kt["minimal_resolution_length"] == 2
    assert "Y_hbar(sl_2) = Y_hbar^-(sl_2) >< Y_hbar^+(sl_2)" in str(
        kt["quantum_double_identity"]
    )


# =========================================================================
# Reduced-resolution filtered comparison
# =========================================================================


def test_reduced_resolution_filtered_comparison_sl2():
    """For rank 1 (sl_2), B2 is PROVED by Khoroshkin-Tolstoy 1996."""
    cmp = reduced_resolution_filtered_comparison(rank=1)
    assert cmp["rank_g"] == 1
    assert cmp["lie_algebra"] == "sl_2"
    assert "Molev" in cmp["PBW_theorem"]
    assert cmp["B2_status_rank_1"] == "proved (Khoroshkin-Tolstoy 1996)"


def test_reduced_resolution_filtered_comparison_sl3():
    """For rank 2 (sl_3), B2 is CONDITIONAL on F5 rank-2 seed."""
    cmp = reduced_resolution_filtered_comparison(rank=2)
    assert cmp["rank_g"] == 2
    assert cmp["lie_algebra"] == "sl_3"
    assert "F5" in cmp["B2_status_rank_2"]


def test_reduced_resolution_filtered_comparison_higher_rank():
    """For rank >= 3, conditional on compact-completion conjecture."""
    cmp = reduced_resolution_filtered_comparison(rank=3)
    assert cmp["rank_g"] == 3
    assert cmp["lie_algebra"] == "sl_4"
    assert "compact-completion" in cmp["B2_status_rank_n"]


# =========================================================================
# Three independent routes
# =========================================================================


def test_route_a_beyond_eval_verma_sl2():
    """ROUTE A: explicit Verma + dual modules for sl_2 Yangian.

    The Drinfeld polynomial P_lambda(u) = prod_{i=0}^{lambda - 1} (u -
    (a + i hbar)) encodes the Verma M_lambda(a) of Y_hbar(sl_2).
    Matches the underlying sl_2 BGG."""
    route = route_a_beyond_eval_verma_and_dual_sl2()
    assert "drinfeld_polynomial" in route
    assert "verma" in route
    assert "dual_verma" in route
    assert route["matches_BGG"]


def test_route_b_reduced_yangian():
    """ROUTE B: Mittag-Leffler + reduced Yangian via quantum double."""
    route = route_b_reduced_yangian_via_quantum_double()
    assert "drinfeld_1985" in route
    assert "khoroshkin_tolstoy_1996" in route
    assert "Y_hbar(g) ~ Omega(Bar(Y^{red}(g)))" in route["filtered_comparison"]


def test_route_c_latyntsev_sphere():
    """ROUTE C: Latyntsev's quantum-group sphere construction."""
    route = route_c_latyntsev_sphere()
    assert "latyntsev_2023_arxiv" in route
    assert route["latyntsev_2023_arxiv"] == "2303.04123"
    assert "small_sphere_construction" in route
    assert "FRT presentation at eval point" in route["local_match"]
