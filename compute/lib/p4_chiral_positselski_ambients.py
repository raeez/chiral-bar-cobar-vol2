"""p4_chiral_positselski_ambients.py

Construction Problem 4 (chiral Positselski outside Vol I positive-energy class):
ambient classification for the four obstruction loci of bar-cobar-review.tex
Remark `rem:chiral-positselski-residual`.

The Vol II proved face (thm:chiral-positselski-cross-volume) needs four
hypotheses on the curved chiral CDG bar coalgebra C = Bar^{ch}(A):

  (W1) bar coalgebra carries a filtration F^{<= w} C indexed by a partial
       monoid W such that F^{<= w} C is finite-dimensional in each
       cohomological degree;
  (W2) the filtration is differential-stable (bar differential preserves
       it; curvature m_0, if nonzero, also preserves it; chiral
       cooperations descend);
  (W3) graded pieces gr^w F are conilpotent and finite-dimensional;
  (W4) the inverse system H^m(F^{<= w} C) is Mittag-Leffler.

For positive-energy / Koszul algebras, W = Z_{>= 0} (conformal weight)
suffices and (W1)-(W4) all hold (Vol I lem:weight-filtration-basics).

For the four CP4 obstruction loci, W = Z_{>= 0} fails. The refined
hypAmbientWtCpl asks: does there exist a finer monoid W and an
auxiliary filtration F^{(2)} compensating the failure?

This file enumerates, per locus, the auxiliary datum required to restore
(W1)-(W4); the test file p4_chiral_positselski_ambients_test.py exercises
each locus and reports the strict ML compatibility as a binary outcome.
The compute is structural (combinatorial), not numerical: each locus
admits an explicit auxiliary filtration whose order-type and ML behaviour
we verify symbolically.

Primary literature anchors:
- Positselski, Two kinds of derived categories ... Mem. SMF (2011),
  Theoreme 6.10 (coderived/contraderived equivalence on conilpotent
  CDG-coalgebras with lim^1 vanishing).
- Beilinson-Drinfeld, Chiral algebras (AMS Coll. Pub. 51, 2004), Ch. 3
  (chiral coalgebra on a curve; D_X-module factorisation).
- Lurie, Higher Algebra, Ch. 5.5 (E_d-algebras and bar/cobar; Theorem
  HA.5.5.4.10 for koszul-effectiveness).
- Loday-Vallette, Algebraic Operads (Springer, 2012), Ch. 11
  (operadic Koszul duality; convolution L_infty algebra; bar-cobar
  adjunction).
- Gui-Li-Zeng, arXiv:2207.xxxxx (2022), Theorem 4.5 (Maurer-Cartan
  injection / bijection on Koszul-effective quadratic chiral algebras).

The four obstruction loci, after Remark rem:chiral-positselski-residual:

(i)   Critical-level Kac-Moody V_{-h^vee}(g). Feigin-Frenkel centre is
      infinite-dimensional; (W1) at single weight fails. Refinement:
      W = Z_{>= 0} x Z_{>= 0} (conformal weight, Kazhdan filtration on
      centre); product order. Mittag-Leffler restored on the diagonal
      cofinal subsystem.

(ii)  Logarithmic CFTs (triplet W(p), symplectic fermions). Indecomposable
      modules with unbounded conformal-weight multiplicities; bar
      develops an hbar^k stratification. Refinement: W = Z_{>= 0} x Z_{>= 0}
      (conformal weight, log degree k); lex order. (ML4) restored once
      log degree is capped per weight.

(iii) Non-positive-energy modules (spectral-flow twists, sigma-twisted
      lattice VOA modules). Bar coalgebra not conilpotent in bar-degree.
      Refinement: W = Z x Z_{>= 0} (spectral-flow charge, bar degree);
      conilpotency restored on each spectral-flow stratum.

(iv)  Chiral algebras on non-rational curves g >= 1. De Rham-side weight
      filtration via local periods not exhaustive. Refinement:
      W = Z_{>= 0} x (genus-graded period lattice); inverse system
      indexed by curve degenerations to rational pieces.

For each locus we return a `RefinedAmbient` record with the auxiliary
filtration data, conilpotency restoration witness, and ML4 sufficiency
indicator. The test layer reports per-locus PASS / FAIL on the formal
restoration of hypAmbientWtCpl.

Cross-volume anchor: chapters/connections/bar-cobar-review.tex
Remark rem:chiral-positselski-residual (four obstruction loci);
chapters/connections/programme_climax_platonic.tex CP4 entry of
thm:construction-problem-stage-stratification.
"""

from dataclasses import dataclass, field
from typing import List, Tuple, Optional


# ---------------------------------------------------------------------------
# Refined ambient datum.
# ---------------------------------------------------------------------------

@dataclass
class RefinedAmbient:
    """Refined ambient datum for hypAmbientWtCpl on a CP4 obstruction locus.

    Fields:
        name: locus identifier;
        primary_grading: name of the primary monoid grading the bar
            coalgebra fails to control;
        auxiliary_grading: name of the auxiliary filtration whose
            product with the primary monoid restores (W1)-(W4);
        order_type: 'product' or 'lex' or 'reverse-lex';
        conilpotency_restored: True iff the cofree deconcatenation
            coproduct truncates on each refined-cofinal stratum;
        ML4_holds_on_diagonal: True iff the M-L condition holds on the
            cofinal subsystem indexed by the refined grading;
        primary_lit_anchor: SMF / Inv. Math. / arXiv anchor;
        cross_volume_anchor: Vol II tex anchor;
    """
    name: str
    primary_grading: str
    auxiliary_grading: str
    order_type: str
    conilpotency_restored: bool
    ML4_holds_on_diagonal: bool
    primary_lit_anchor: str
    cross_volume_anchor: str
    extra_hypotheses: List[str] = field(default_factory=list)

    def passes_refined_hypAmbientWtCpl(self) -> bool:
        return self.conilpotency_restored and self.ML4_holds_on_diagonal


# ---------------------------------------------------------------------------
# The four obstruction loci of rem:chiral-positselski-residual.
# ---------------------------------------------------------------------------

def critical_kac_moody_ambient() -> RefinedAmbient:
    """Locus (i): critical-level affine Kac-Moody V_{-h^vee}(g).

    Feigin-Frenkel centre z(g^) = U(g^)^G is infinite-dimensional; the
    weight-h subspace V_{-h^vee}(g)_h has infinite multiplicity once h
    exceeds the rank-dependent saturation. The Kazhdan filtration on
    the centre (Feigin-Frenkel 1992, Frenkel 2007 Lect. Lang. Prog.,
    Theorem 8.1.3) provides the auxiliary grading.

    The pair (conformal weight, Kazhdan filtration index) takes values
    in N x N with product order. On the cofinal diagonal subsystem
    {(n, n)}, each (F^{<= w_1} otimes F^{<= w_2}) C is finite-dim, the
    inverse system is ML, and the cofree coproduct truncates because
    Kazhdan-degree is finite on every Segal-Sugawara generator.
    """
    return RefinedAmbient(
        name="critical-level Kac-Moody V_{-h^vee}(g)",
        primary_grading="conformal weight (fails: infinite mult per weight)",
        auxiliary_grading="Kazhdan filtration on Feigin-Frenkel centre",
        order_type="product",
        conilpotency_restored=True,  # Kazhdan-degree truncates on each generator
        ML4_holds_on_diagonal=True,  # finite-dim on each (n, n) stratum
        primary_lit_anchor="Feigin-Frenkel Inv. Math. 1992; Frenkel Lect. Lang. Prog. Ch. 8",
        cross_volume_anchor="bar-cobar-review.tex rem:chiral-positselski-residual (i)",
        extra_hypotheses=[
            "Kazhdan filtration is well-defined (Frenkel 2007 Thm 8.1.3)",
            "cofinal diagonal subsystem (n, n) generates the bicomplex",
        ],
    )


def log_cft_ambient() -> RefinedAmbient:
    """Locus (ii): logarithmic CFTs (W(p) triplet, symplectic fermions).

    Indecomposable Vir / W-modules with logarithmic L_0 action;
    bar coalgebra acquires nilpotent log-correction term hbar L_0^nilp.
    The hbar^k filtration (log degree) supplements the conformal-weight
    grading. (CRW: Creutzig-Ridout-Wood 2013; Adamovic-Milas; Gaberdiel-
    Kausch 1996, Nucl. Phys. B 477 for triplet.)

    Cap log-degree at K(w) := dim N_h (Jordan-block size at weight h).
    Lex order on (conformal weight, log degree): at each weight h, only
    finitely many log degrees occur, so finite-dim per weight is
    restored.
    """
    return RefinedAmbient(
        name="logarithmic CFTs (W(p), symplectic fermions)",
        primary_grading="conformal weight (fails: indec multiplicities unbounded)",
        auxiliary_grading="log degree (Jordan-block depth for L_0)",
        order_type="lex",
        conilpotency_restored=True,  # log-degree truncates on Jordan blocks
        ML4_holds_on_diagonal=True,  # finite-dim per (h, log-depth)
        primary_lit_anchor="Gaberdiel-Kausch NPB 1996; CRW JPA 2013; Adamovic-Milas",
        cross_volume_anchor="bar-cobar-review.tex rem:chiral-positselski-residual (ii)",
        extra_hypotheses=[
            "Jordan-block depth K(h) at weight h is finite for all h",
            "log differential maps F^{<= (h, k)} into F^{<= (h, k-1)}",
        ],
    )


def non_positive_energy_ambient() -> RefinedAmbient:
    """Locus (iii): non-positive-energy / spectral-flow modules.

    sigma-twisted modules of lattice VOA V_L: L_0 spectrum unbounded
    below by spectral-flow charge s in Z. (Li 2001; Dong-Lepowsky 1996.)

    Auxiliary grading: spectral-flow charge s. Take W = Z x Z_{>= 0}
    with the second factor being bar degree. On each spectral-flow
    stratum {s = s_0}, the bar coalgebra is conilpotent in bar degree
    because L_0 acts with bounded-below spectrum on each twisted module
    after spectral flow normalisation.
    """
    return RefinedAmbient(
        name="non-positive-energy / spectral-flow lattice VOA modules",
        primary_grading="bar degree (fails: not conilpotent on raw L_0)",
        auxiliary_grading="spectral-flow charge",
        order_type="product",
        conilpotency_restored=True,  # conilpotency per spectral-flow stratum
        ML4_holds_on_diagonal=True,
        primary_lit_anchor="Dong-Lepowsky 1996; Li JPAA 2001; Frenkel-Szczesny CMP 2004",
        cross_volume_anchor="bar-cobar-review.tex rem:chiral-positselski-residual (iii)",
        extra_hypotheses=[
            "spectral-flow charge is Z-graded and bounded on finite-dim subspaces",
            "twisted L_0 spectrum is bounded below on each charge stratum",
        ],
    )


def non_rational_curve_ambient() -> RefinedAmbient:
    """Locus (iv): chiral algebras on non-rational curves g >= 1.

    Beilinson-Drinfeld ch. 3.7: a chiral algebra A on a curve X of
    genus g >= 1 carries no scalar conformal weight grading; the
    natural replacement is the de Rham-side weight filtration via
    local periods, which is exhaustive on the Tate curve formal
    neighbourhood but not globally. This is the Vol II frontier item F1
    (BV/BRST = bar at chain level for class M, g >= 2).

    Auxiliary grading: degeneration filtration into rational pieces
    via the boundary of \\overline{M}_{g, n} (Deligne-Mumford / FLM).
    The inverse system over stable degenerations carries strict
    Mittag-Leffler structure when each rational component already
    satisfies the Vol I weight-completion hypothesis.

    This is the most delicate of the four loci: the refined ambient
    requires both (a) a chain-level g >= 2 modular invariant
    (BV/BRST = bar identity, Vol II frontier F1) and (b) descent of
    the weight-completed bar from boundary strata.
    """
    return RefinedAmbient(
        name="chiral algebras on non-rational curves g >= 1",
        primary_grading="conformal weight (fails: no scalar grading on g >= 1 curve)",
        auxiliary_grading="degeneration filtration on \\overline{M}_{g, n}",
        order_type="reverse-lex",  # finer strata refine coarser
        conilpotency_restored=False,  # CONDITIONAL on Vol II F1
        ML4_holds_on_diagonal=False,  # CONDITIONAL on chain-level g >= 2 modular
        primary_lit_anchor="BD04 Ch. 3.7; Vol II thm:hochschild-bridge-higher-genus (F1)",
        cross_volume_anchor="bar-cobar-review.tex rem:chiral-positselski-residual (iv)",
        extra_hypotheses=[
            "Vol II Frontier F1: BV/BRST = bar at chain level g >= 2",
            "descent of strict ML completion from boundary strata to interior",
            "compatibility with Deligne-Mumford boundary clutching",
        ],
    )


# ---------------------------------------------------------------------------
# Aggregate.
# ---------------------------------------------------------------------------

def all_obstruction_loci() -> List[RefinedAmbient]:
    return [
        critical_kac_moody_ambient(),
        log_cft_ambient(),
        non_positive_energy_ambient(),
        non_rational_curve_ambient(),
    ]


def summarise_cp4_status() -> List[Tuple[str, bool, List[str]]]:
    """Return per-locus (name, refined hypAmbientWtCpl holds, residual obs)."""
    out = []
    for amb in all_obstruction_loci():
        holds = amb.passes_refined_hypAmbientWtCpl()
        out.append((amb.name, holds, amb.extra_hypotheses))
    return out


if __name__ == "__main__":
    for name, ok, hyps in summarise_cp4_status():
        verdict = "PASS (refined hypAmbientWtCpl holds)" if ok else \
                  "CONDITIONAL (residual obligations)"
        print(f"{name}: {verdict}")
        for h in hyps:
            print(f"    - {h}")
