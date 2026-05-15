"""Tests for f12_scalar_saturation_engine.

LICENSING. ambient: cyclic deformation complex in fixed tensor
category Rep(g_hat_k) (gamma); chart: choice of primary strong
generators per family (alpha); comparison: Whitehead reduction
(Vol I thm:cyclic-rigidity-generic) (beta); endpoint: algebraic
semicontinuity of M(k) rank at one regular evaluation point extends
to Zariski-open dense locus (delta); effectiveness: numerical rank
computation over Q at chosen k_test value (epsilon).

Provides Layer 1 verification for F12's three candidate families
and records the bar-cohomology vs cyclic-cohomology separation.
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.f12_scalar_saturation_engine import (
    PRIMARY_LITERATURE,
    BarVsCyclicSeparation,
    CandidateFamily,
    ConstraintMatrix,
    LayerOneCertificate,
    MultiPathLayerOneCheck,
    PrimaryGenerator,
    RatPoly,
    WhiteheadDecomposition,
    family_admissible_L_k_sl3,
    family_chi_functor_quiver,
    family_parafermion_K_sl2,
    multi_path_check_sl3_admissible,
    sl3_admissible_separation,
    verify_layer_1,
    whitehead_decomposition_admissible_sl3,
)


# ---------------------------------------------------------------------------
# Sanity for the symbolic arithmetic.
# ---------------------------------------------------------------------------


def test_ratpoly_constant_evaluation():
    p = RatPoly.const(Fraction(7))
    assert p.evaluate(Fraction(2)) == Fraction(7)
    assert p.evaluate(Fraction(-13, 5)) == Fraction(7)


def test_ratpoly_affine_evaluation():
    # f(k) = 3 + k
    p = RatPoly.affine(Fraction(3), Fraction(1))
    assert p.evaluate(Fraction(0)) == Fraction(3)
    assert p.evaluate(Fraction(1)) == Fraction(4)
    assert p.evaluate(Fraction(-3)) == Fraction(0)


# ---------------------------------------------------------------------------
# Family constructors -- structural checks.
# ---------------------------------------------------------------------------


def test_L_k_sl3_admissible_has_one_primary_generator():
    fam = family_admissible_L_k_sl3(p=3, q=2)
    # Smallest non-degenerate admissible: p = 3, q = 2 (q >= 3 case from
    # `thm:admissible-sl3-non-koszul-qge3` starts at q = 3; below that
    # the bar non-Koszulness statement is not made).
    assert len(fam.primary_generators) == 1
    assert fam.primary_generators[0].name == "T"
    assert fam.primary_generators[0].conformal_weight == Fraction(2)
    assert fam.primary_generators[0].is_singlet is True


def test_L_k_sl3_q_geq_3_null_grades():
    fam = family_admissible_L_k_sl3(p=3, q=3)
    # h_theta = (p-2)q = q = 3; h_alpha = (p-1)q = 2q = 6.
    assert fam.null_vector_grades == (3, 6)


def test_parafermion_K_sl2_one_primary():
    fam = family_parafermion_K_sl2(k_num=7, k_den=3)
    assert len(fam.primary_generators) == 1


def test_chi_functor_rank_1_one_primary():
    fam = family_chi_functor_quiver(rank=1)
    assert len(fam.primary_generators) == 1


# ---------------------------------------------------------------------------
# Primary--primary space V dimension.
# ---------------------------------------------------------------------------


def test_V_dim_sl3_admissible_equals_1():
    fam = family_admissible_L_k_sl3(p=3, q=3)
    # Only the (T, T) self-pair in the singlet sector.
    assert fam.primary_primary_dim() == 1


def test_V_dim_parafermion_equals_1():
    fam = family_parafermion_K_sl2(k_num=7, k_den=3)
    assert fam.primary_primary_dim() == 1


def test_V_dim_chi_rank_1_equals_1():
    fam = family_chi_functor_quiver(rank=1)
    assert fam.primary_primary_dim() == 1


# ---------------------------------------------------------------------------
# Constraint matrix M(k) Feigin-Fuks (T,T) channel.
# ---------------------------------------------------------------------------


def test_feigin_fuks_matrix_rank_at_admissible_k():
    """For sl_3 at admissible k = -3 + p/q with p >= 3, q >= 3, the
    Feigin-Fuks (T,T) coupling lambda(k) = k + h^v = k + 3 is non-zero.
    For p=3, q=3: k = -3 + 1 = -2; lambda(-2) = 1 ≠ 0; rank 1.
    For p=4, q=3: k = -3 + 4/3 = -5/3; lambda(-5/3) = 4/3 ≠ 0; rank 1.
    """
    m = ConstraintMatrix.feigin_fuks_TT()
    # k = -2 (admissible p=3, q=3 for sl_3 has k = -3 + 3/3 = -2; but
    # gcd(3,3) = 3 is not coprime. Use p=4, q=3 with gcd(4,3)=1).
    k_admissible = Fraction(-3) + Fraction(4, 3)  # = -5/3
    assert m.rank_at(k_admissible) == 1


def test_feigin_fuks_matrix_drops_at_critical_level():
    """At k = -h^v = -3 (critical), lambda(k) = 0; rank drops to 0.
    This is the unique exceptional point in the admissible-family
    rigidity statement for sl_3."""
    m = ConstraintMatrix.feigin_fuks_TT()
    assert m.rank_at(Fraction(-3)) == 0


def test_feigin_fuks_matrix_rank_at_generic_level():
    """At generic non-critical k the rank is maximal."""
    m = ConstraintMatrix.feigin_fuks_TT()
    for k in (Fraction(1), Fraction(2), Fraction(-1), Fraction(7, 5)):
        assert m.rank_at(k) == 1


# ---------------------------------------------------------------------------
# Layer 1 certification at admissible level (PRIMARY F12 DELIVERABLE).
# ---------------------------------------------------------------------------


def test_layer_1_sl3_admissible_p4_q3():
    """L_k(sl_3) at k = -3 + 4/3 = -5/3 admissible, p=4, q=3.

    This is the first non-degenerate admissible level at sl_3 with
    q >= 3 (the regime where `thm:admissible-sl3-non-koszul-qge3`
    forces dim H^2(bar) >= 2). Layer 1 of F12 asks whether the
    CYCLIC primitive tangent space H^2_{cyc,prim} = 0 -- a DIFFERENT
    invariant from bar cohomology.

    Verification: V = C (one-dimensional, Sugawara T-T pair),
    M(k) = [lambda(k)] with lambda(-5/3) = -5/3 + 3 = 4/3 ≠ 0.
    Hence rk M(-5/3) = 1 = dim V, certifying Layer 1.
    """
    fam = family_admissible_L_k_sl3(p=4, q=3)
    m = ConstraintMatrix.feigin_fuks_TT()
    cert = verify_layer_1(
        fam,
        m,
        k_test=Fraction(-3) + Fraction(4, 3),
        exceptional_set_description=(
            "E = {k = -3} (critical level); algebraic semicontinuity "
            "extends rank-1 to all k in C \\ {-3}, including every "
            "admissible parameter k = -3 + p/q with p >= 3, q >= 3, "
            "gcd(p,q) = 1."
        ),
    )
    assert cert.layer1_holds is True
    assert cert.constraint_rank == 1
    assert cert.primary_primary_dim == 1


def test_layer_1_sl3_admissible_p5_q3():
    """L_k(sl_3) at k = -3 + 5/3 = -4/3 admissible. Second test point
    on the same Zariski-open locus."""
    fam = family_admissible_L_k_sl3(p=5, q=3)
    m = ConstraintMatrix.feigin_fuks_TT()
    cert = verify_layer_1(
        fam,
        m,
        k_test=Fraction(-3) + Fraction(5, 3),
        exceptional_set_description="E = {-3}; semicontinuity covers admissible.",
    )
    assert cert.layer1_holds is True


def test_layer_1_sl3_admissible_p5_q4():
    """Third independent admissible parameter, q = 4."""
    fam = family_admissible_L_k_sl3(p=5, q=4)
    m = ConstraintMatrix.feigin_fuks_TT()
    cert = verify_layer_1(
        fam,
        m,
        k_test=Fraction(-3) + Fraction(5, 4),
        exceptional_set_description="E = {-3}; semicontinuity covers admissible.",
    )
    assert cert.layer1_holds is True


def test_layer_1_parafermion_non_GKO():
    """Parafermion K(sl_2, k) at k = 7/3 (irrational-style rational
    outside GKO integer locus). Layer 1 holds: V = C, lambda(7/3) ≠ 0.
    """
    fam = family_parafermion_K_sl2(k_num=7, k_den=3)
    # For K(sl_2, k) the relevant coupling vanishes at k = -h^v(sl_2) = -2.
    m = ConstraintMatrix(rows=[[RatPoly.affine(Fraction(2), Fraction(1))]])
    cert = verify_layer_1(
        fam,
        m,
        k_test=Fraction(7, 3),
        exceptional_set_description="E = {-2}; non-GKO locus covered.",
    )
    assert cert.layer1_holds is True


def test_layer_1_chi_functor_rank_1():
    """chi(T_1[A_1]) at the rank-1 quiver. Beem-Rastelli chi yields
    Virasoro-type VOA with one-dimensional Defcyc; Layer 1 holds."""
    fam = family_chi_functor_quiver(rank=1)
    m = ConstraintMatrix.feigin_fuks_TT()
    cert = verify_layer_1(
        fam,
        m,
        k_test=Fraction(0),  # chi at the marginal point
        exceptional_set_description="E = empty for rank-1 chi (no critical level).",
    )
    assert cert.layer1_holds is True


# ---------------------------------------------------------------------------
# Bar-vs-cyclic separation: the CONCEPTUAL deliverable.
# ---------------------------------------------------------------------------


def test_sl3_admissible_separation_records_bar_H2_lower_bound():
    """Vol I `thm:admissible-sl3-non-koszul-qge3` gives
    dim H^2(BarB^ch(L_k(sl_3))) >= 2 at admissible q >= 3. This is
    a separate invariant from H^2_{cyc,prim}."""
    sep = sl3_admissible_separation(p=4, q=3)
    assert sep.bar_H2_lower_bound == 2
    assert len(sep.bar_H2_witness_classes) == 2


def test_sl3_admissible_separation_records_cyclic_H2_zero():
    """The cyclic primitive tangent space vanishes for L_k(sl_3)
    at admissible q >= 3. This is the F12 Layer 1 statement."""
    sep = sl3_admissible_separation(p=4, q=3)
    assert sep.cyclic_H2_prim == 0


def test_separation_invariants_are_disjoint():
    """bar_H2 >= 2 and cyclic_H2_prim = 0 simultaneously. These are
    DIFFERENT invariants of L_k(sl_3); the F12 Layer 1 claim does
    NOT contradict the Vol I bar-non-Koszulness theorem."""
    sep = sl3_admissible_separation(p=4, q=3)
    assert sep.bar_H2_lower_bound > sep.cyclic_H2_prim


# ---------------------------------------------------------------------------
# Attack-heal: try to find a counterexample where Layer 1 fails.
# ---------------------------------------------------------------------------


def test_attack_critical_level_layer_1_fails_as_expected():
    """At k = -h^v, lambda(k) = 0; rank drops to 0; Layer 1 fails.
    The critical level is the unique exceptional point. F12 Layer 1
    excludes the critical level explicitly."""
    fam = family_admissible_L_k_sl3(p=4, q=3)
    m = ConstraintMatrix.feigin_fuks_TT()
    cert = verify_layer_1(
        fam,
        m,
        k_test=Fraction(-3),
        exceptional_set_description="Critical level k = -h^v = -3.",
    )
    assert cert.layer1_holds is False
    assert cert.constraint_rank == 0


# ---------------------------------------------------------------------------
# Whitehead decomposition coherence: dim H^2_cyc = 1 (level direction)
# at every admissible parameter. The level direction is NOT shared with
# bar cohomology -- a key conceptual point.
# ---------------------------------------------------------------------------


def test_whitehead_level_direction_dim_equals_1():
    wh = whitehead_decomposition_admissible_sl3(p=4, q=3)
    assert wh.level_direction_dim == 1


def test_whitehead_primitive_dim_equals_0():
    wh = whitehead_decomposition_admissible_sl3(p=4, q=3)
    assert wh.primitive_dim == 0


def test_whitehead_total_H2_cyc_equals_1_not_2():
    """The TOTAL cyclic H^2 of L_k(sl_3) is 1, NOT 2. The bar
    cohomology of the same algebra is >= 2 (Vol I
    `thm:admissible-sl3-non-koszul-qge3`). These are different
    invariants of the same chiral algebra."""
    wh = whitehead_decomposition_admissible_sl3(p=4, q=3)
    assert wh.total_H2_cyc() == 1


# ---------------------------------------------------------------------------
# Multi-path Layer 1 verification: three independent routes must agree.
# ---------------------------------------------------------------------------


def test_multi_path_consistency_sl3_admissible_p4_q3():
    """Triple-route verification: matrix rank, Whitehead decomposition,
    Vol I `thm:algebraic-family-rigidity`. All three must agree that
    H^2_{cyc,prim} = 0 for the F12 deliverable to be solid."""
    check = multi_path_check_sl3_admissible(p=4, q=3)
    assert check.route_a_constraint_rank_max is True
    assert check.route_b_whitehead_primitive_zero is True
    assert check.route_c_alg_family_rigidity_applies is True
    assert check.consistent() is True


def test_multi_path_consistency_sl3_admissible_sweep():
    """Sweep over admissible (p, q) and verify all three routes agree
    everywhere. If any single (p, q) shows disagreement, F12 Layer 1
    is in question."""
    from math import gcd

    failures = []
    for p in range(3, 13):
        for q in range(3, 8):
            if gcd(p, q) != 1:
                continue
            check = multi_path_check_sl3_admissible(p=p, q=q)
            if not check.consistent():
                failures.append((p, q, check))
    assert failures == [], (
        f"Multi-path disagreement at admissible (p, q): {failures}"
    )


# ---------------------------------------------------------------------------
# Primary literature anchors -- the verification must cite WHY each
# constraint is justified.
# ---------------------------------------------------------------------------


def test_primary_literature_includes_kac_wakimoto():
    """Kac-Wakimoto 1989 establishes the admissible-level
    representation theory. Required for the L_k(sl_3) candidate."""
    assert "Kac-Wakimoto-1989" in PRIMARY_LITERATURE


def test_primary_literature_includes_feigin_fuks():
    """Feigin-Fuks 1983 supplies the Virasoro rigidity statement
    H^2(Vir, C_c) = C used to make M(k) = [lambda(k)] one-dimensional."""
    assert "Feigin-Fuks-1983" in PRIMARY_LITERATURE


def test_primary_literature_includes_beem_rastelli():
    """Beem-Rastelli 2018 supplies the chi-functor construction
    underlying candidate (2)."""
    assert "Beem-Rastelli-2018" in PRIMARY_LITERATURE


def test_primary_literature_includes_adamovic_milas():
    """Adamovic-Milas 1995 supplies the admissible-level Zhu algebra
    structure underpinning candidate (3)."""
    assert "Adamovic-Milas-1995" in PRIMARY_LITERATURE


def test_attack_no_known_counterexample_admissible_q_geq_3():
    """Sweep admissible levels k = -3 + p/q with p in [3, 12],
    q in [3, 7], gcd(p, q) = 1. In all cases lambda(k) ≠ 0
    (since lambda(k) = 0 only at k = -3), so Layer 1 holds."""
    from math import gcd

    m = ConstraintMatrix.feigin_fuks_TT()
    failures = []
    for p in range(3, 13):
        for q in range(3, 8):
            if gcd(p, q) != 1:
                continue
            k = Fraction(-3) + Fraction(p, q)
            if k == -3:
                continue
            fam = family_admissible_L_k_sl3(p=p, q=q)
            cert = verify_layer_1(
                fam, m, k_test=k, exceptional_set_description="E = {-3}."
            )
            if not cert.layer1_holds:
                failures.append((p, q, k))
    assert failures == [], (
        f"Counterexamples to Layer 1 at admissible q >= 3: {failures}"
    )
