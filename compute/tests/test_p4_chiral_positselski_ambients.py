"""Tests for p4_chiral_positselski_ambients.py.

Per-locus PASS / CONDITIONAL report on the refined hypAmbientWtCpl for
the four CP4 obstruction loci of bar-cobar-review.tex
rem:chiral-positselski-residual.

These tests are structural: they verify that the auxiliary filtration
data we record per locus satisfies the formal book-keeping conditions
(W1)-(W4), not that the bar coalgebra of any specific algebra realises
them. The numerical verification on representative algebras is a
separate compute task (cf. compute/tests/test_critical_level_*.py for
critical-level Kac-Moody / Feigin-Frenkel and
compute/tests/test_log_*.py for triplet W(p)).
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.p4_chiral_positselski_ambients import (
    all_obstruction_loci,
    critical_kac_moody_ambient,
    log_cft_ambient,
    non_positive_energy_ambient,
    non_rational_curve_ambient,
    summarise_cp4_status,
)


class TestCriticalLevelKacMoody:
    def test_auxiliary_grading_is_kazhdan(self):
        amb = critical_kac_moody_ambient()
        assert "Kazhdan" in amb.auxiliary_grading

    def test_conilpotency_restored(self):
        amb = critical_kac_moody_ambient()
        assert amb.conilpotency_restored

    def test_ml4_restored_on_diagonal(self):
        amb = critical_kac_moody_ambient()
        assert amb.ML4_holds_on_diagonal

    def test_refined_ambient_passes(self):
        amb = critical_kac_moody_ambient()
        assert amb.passes_refined_hypAmbientWtCpl(), \
            "critical-level Kac-Moody refined hypAmbientWtCpl should hold"


class TestLogCFT:
    def test_auxiliary_grading_is_log_degree(self):
        amb = log_cft_ambient()
        assert "log" in amb.auxiliary_grading.lower()

    def test_lex_order(self):
        amb = log_cft_ambient()
        assert amb.order_type == "lex"

    def test_refined_ambient_passes(self):
        amb = log_cft_ambient()
        assert amb.passes_refined_hypAmbientWtCpl(), \
            "logarithmic CFT refined hypAmbientWtCpl should hold"


class TestNonPositiveEnergy:
    def test_auxiliary_grading_is_spectral_flow(self):
        amb = non_positive_energy_ambient()
        assert "spectral-flow" in amb.auxiliary_grading.lower() or \
               "spectral flow" in amb.auxiliary_grading.lower()

    def test_refined_ambient_passes(self):
        amb = non_positive_energy_ambient()
        assert amb.passes_refined_hypAmbientWtCpl(), \
            "non-positive-energy refined hypAmbientWtCpl should hold"


class TestNonRationalCurve:
    """The non-rational curve locus is genuinely CONDITIONAL: the
    refinement requires Vol II Frontier F1 (chain-level BV/BRST = bar
    for class M at g >= 2)."""

    def test_conditional_on_Vol_II_F1(self):
        amb = non_rational_curve_ambient()
        anchors = " ".join(amb.extra_hypotheses)
        assert "F1" in anchors, \
            "non-rational curve locus must declare Vol II F1 dependency"

    def test_refined_ambient_does_not_pass_unconditionally(self):
        amb = non_rational_curve_ambient()
        assert not amb.passes_refined_hypAmbientWtCpl(), \
            "non-rational curve locus is conditional on F1, not absolute"


class TestAggregate:
    def test_four_loci(self):
        assert len(all_obstruction_loci()) == 4

    def test_three_loci_pass_one_conditional(self):
        status = summarise_cp4_status()
        passes = sum(1 for _name, ok, _ in status if ok)
        conditional = sum(1 for _name, ok, _ in status if not ok)
        # Three obstruction loci admit a refined hypAmbientWtCpl
        # construction unconditionally; the non-rational-curve locus is
        # conditional on Vol II Frontier F1.
        assert passes == 3
        assert conditional == 1
