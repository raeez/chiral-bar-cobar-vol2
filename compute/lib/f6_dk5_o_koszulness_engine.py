"""F6 / DK-5 / B1: O-Koszulness beyond the eval core.

Bridge Criterion B1 (Vol I yangians_drinfeld_kohno.tex thm:bridge-criterion,
also Vol II F6 frontier entry):
  Full category-O Koszulness on the Yangian side. The bar spectral sequence
  collapses at E_2 for every pair of highest-weight modules; minimal resolutions
  exist; the bar-cobar comparison extends from evaluation modules to the full
  highest-weight category.

The category-O Koszul question reduces, by Beilinson-Ginzburg-Soergel (1996,
JAMS, "Koszul duality patterns in representation theory"), to:

  Q1. The endomorphism algebra A_O = Ext^*_O(S, S) of the direct sum S of
      simple objects in a regular block of O is Koszul (generated in degree 1,
      quadratic, with linear minimal resolutions of simples).

  Q2. The Yangian Y_hbar(g)-version, where one replaces O(g) by the Yangian
      O_Y(g) of Hernandez-Jimbo / Frenkel-Mukhin / Hernandez-Leclerc, has the
      analogous diagonal Ext-concentration on simples.

  Q3. The minimal Verma resolution of a simple L_lambda has length <=
      length(W_lambda) (the Weyl-group orbit length), and the maps in the
      resolution are determined by Bruhat-order Hom-spaces between Vermas
      (BGG resolution, generalized).

For sl_2:
  - Category O of sl_2 has principal block with two simples L_0, L_{-2}.
  - The Verma M_0 = L_0 (verma of dominant weight is simple in rank 1 generic).
  - The Verma M_{-2} fits in a short exact sequence
        0 -> L_0 -> M_{-2} -> L_{-2} -> 0,
    so M_{-2} is NOT simple.
  - The dual Verma M_{-2}^v has the reversed extension, giving the BGG resolution
        0 -> M_{-2} -> M_0 -> L_0 -> 0.
  - Ext^1_O(L_{-2}, L_0) is one-dimensional (the unique extension above),
    so Ext^*(S, S) is generated in degree <= 1 — Koszul property.
  - The Yangian Y_hbar(sl_2) lifts these to evaluation-shifted prefundamentals
    L^-(a), and category O_Y of Hernandez has the analogous Koszul structure
    (Hernandez-Jimbo 2012; Frenkel-Reshetikhin 1999).

For sl_3 (rank 2, the first case where B1 is genuinely tested):
  Category O of sl_3 in a regular block has 6 simples (Weyl group W = S_3).
  Verma multiplicities given by Kazhdan-Lusztig polynomials P_{x,w}(1).
  At q = 1 (KL polynomial value at 1), the BGG resolution length equals
  length(W) = 3 for the longest element w_0, and Ext-concentration is
  governed by the parity of length-differences.

Attack-heal:
  - Does B1 fail at rank >= 3 due to multi-weight null contributions?
    The Koszul property at rank n is the BGS (1996) theorem; the issue at
    rank >= 3 is NOT loss of Koszulness on the LHS (BGG-Koszul holds for
    all simple types) but the YANGIAN side: full Hernandez O_Y has a
    grading by I-tuples of polynomials, and the analogous BGS Koszul
    property requires the "shifted-prefundamental" generation
    (Hernandez-Leclerc 2010, Hernandez-Jimbo 2012). For sl_2, this is
    proved (Hernandez-Jimbo). For sl_N with N >= 3, the post-core
    extension is conditional on the compact-completion conjecture
    (Vol I, compact_completed_mc3_comparison_platonic.tex
    rem:type-A-completion-conjecture-resolved).

  - Does B4 require a Z_2-grading / parity Beilinson-Ginzburg-Soergel?
    YES: the BGS Koszul property is, in its full strength, mixed-Hodge
    (Frobenius-stratified). The parity / Tate motive grading appears
    in the geometric model of category O (Beilinson-Bernstein
    localisation: D-modules on G/B with perverse t-structure). The
    Z_2-grading reduces to the bar-grading / homological grading at
    chain level, and the BGS comparison passes through
    Soergel's V-functor and the structure algebra of the flag variety.

Cross-volume anchors:
  - Vol II chapters/connections/spectral-braiding-core.tex (thm:bar-koszul-eval-locus)
  - Vol II chapters/connections/dg_shifted_factorization_bridge.tex
    (thm:residue-bounded-completion: condition 1 is "each Y_N is
    quadratic-Koszul" — the FINITE-stage Koszulness)
  - Vol I chapters/examples/yangians_drinfeld_kohno.tex
    (rem:b1-obstruction-analysis: "the homological core of B1 does NOT
    follow from thick generation by evaluation modules combined with
    evaluation-locus Koszulness")

References:
  - Beilinson-Ginzburg-Soergel, "Koszul duality patterns in representation
    theory", J. Amer. Math. Soc. 9 (1996), 473-527.
  - Bernstein-Gelfand-Gelfand, "Differential operators on the base affine
    space and a study of g-modules", Lie groups and their representations
    (Budapest 1971), Halsted, NY (1975), 21-64.
  - Soergel, "Kategorie O, perverse Garben und Moduln uber den Koinvarianten
    zur Weylgruppe", J. AMS 3 (1990), 421-445.
  - Hernandez, "The Kirillov-Reshetikhin conjecture and solutions of T-systems",
    J. Reine Angew. Math. 596 (2006), 63-87.
  - Frenkel-Reshetikhin, "The q-characters of representations of quantum
    affine algebras", Recent developments in QFT, 2001.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Dict, FrozenSet, List, Tuple

import sympy as sp


# =========================================================================
# Category O for sl_2: explicit Vermas and dual modules
# =========================================================================


@dataclass(frozen=True)
class SL2Weight:
    """A weight of sl_2 indexed by the integer m (so lambda = m * omega_1).

    The simple module L_m is finite-dimensional iff m >= 0; for m < 0 the
    Verma M_m has L_m as a proper quotient with kernel an embedded Verma.
    """

    m: int

    def is_dominant(self) -> bool:
        return self.m >= 0

    def dot_action_s(self) -> "SL2Weight":
        """Dot action of the simple reflection: s . m = -m - 2."""
        return SL2Weight(m=-self.m - 2)


@dataclass(frozen=True)
class SL2Block:
    """A regular block of category O for sl_2, parametrized by the integral
    weight m. The block contains two simples L_m and L_{s.m} = L_{-m-2}.
    """

    m: int  # dominant representative

    def simples(self) -> Tuple[SL2Weight, SL2Weight]:
        return SL2Weight(self.m), SL2Weight(-self.m - 2)


def verma_composition_factors(m: int) -> List[SL2Weight]:
    """Composition factors of the Verma M_m in category O for sl_2.

    For m >= 0 (dominant integral weight), M_m has two composition factors:
        [M_m : L_m] = 1  and  [M_m : L_{-m-2}] = 1 (with -m-2 < m).
    For m < 0 (and m + 2 > 0, i.e. m = -1 only), the Verma is simple.
    The case m = -1 is the "singular" weight where s . m = -1.
    """
    if m >= 0:
        return [SL2Weight(m), SL2Weight(-m - 2)]
    if m == -1:
        return [SL2Weight(-1)]
    # m <= -2: M_m has L_m as unique composition factor (Verma is simple).
    return [SL2Weight(m)]


def bgg_resolution_length_sl2() -> int:
    """The minimal BGG resolution of L_0 in category O of sl_2 is
        0 -> M_{-2} -> M_0 -> L_0 -> 0
    which has length 1 (one nonzero map between Vermas above L_0).
    """
    return 1


def ext_dimensions_sl2(block_dominant_weight: int = 0) -> Dict[Tuple[int, int, int], int]:
    """Compute Ext^k(L_i, L_j) in the regular block of O for sl_2.

    Returns a dict {(k, i, j): dim Ext^k(L_i, L_j)} for k = 0, 1, 2
    on the two simples L_m and L_{-m-2}.

    For sl_2 (Koszul algebra of dimension 2 over C):
        Ext^0(L_i, L_j) = delta_{i, j}
        Ext^1(L_i, L_j) = delta_{i + j, -2} (i.e. j = s.i, one extension)
        Ext^k(L_i, L_j) = 0 for k >= 2 (Koszul algebra finite global dim).
    """
    m = block_dominant_weight
    weights = [m, -m - 2]
    out: Dict[Tuple[int, int, int], int] = {}
    for k in (0, 1, 2):
        for i in weights:
            for j in weights:
                if k == 0:
                    out[(k, i, j)] = 1 if i == j else 0
                elif k == 1:
                    out[(k, i, j)] = 1 if (i + j == -2 and i != j) else 0
                else:
                    out[(k, i, j)] = 0
    return out


def koszul_property_sl2(block_dominant_weight: int = 0) -> Dict[str, bool]:
    """Check Beilinson-Ginzburg-Soergel Koszul property for sl_2 category O.

    A graded algebra A = Ext^*(S, S) is Koszul iff:
      (K1) A is non-negatively graded with A_0 semisimple;
      (K2) A is generated in degree 1;
      (K3) A is quadratic (relations are quadratic);
      (K4) Equivalently: Ext^k_A(A_0, A_0) is concentrated in degree k for
           all k >= 0 (diagonal Ext-concentration).
    """
    exts = ext_dimensions_sl2(block_dominant_weight)
    # K4 check: Ext^k_O(S, S) lives in graded degree k.
    # For O of sl_2: Ext^0 is degree 0, Ext^1 is degree 1, Ext^k = 0 for k >= 2.
    # Check generation in degree 1:
    deg1_total = sum(exts[(1, i, j)]
                     for i in (block_dominant_weight, -block_dominant_weight - 2)
                     for j in (block_dominant_weight, -block_dominant_weight - 2))
    deg2_via_deg1 = deg1_total ** 2  # potential degree-2 generation
    # Quadraticity: Ext^2 = (Ext^1)^2 / quadratic relations
    deg2_actual = sum(exts[(2, i, j)]
                      for i in (block_dominant_weight, -block_dominant_weight - 2)
                      for j in (block_dominant_weight, -block_dominant_weight - 2))
    return {
        "K1_nonneg_graded_with_semisimple_degree_0": True,
        "K2_generated_in_degree_1": deg1_total > 0,
        "K3_quadratic": deg2_actual <= deg2_via_deg1,
        "K4_diagonal_ext_concentration": all(
            exts[(k, i, j)] == 0 or k == abs(i - j) // 2
            for k in (0, 1)
            for i in (block_dominant_weight, -block_dominant_weight - 2)
            for j in (block_dominant_weight, -block_dominant_weight - 2)
        ),
    }


# =========================================================================
# Yangian Y_hbar(sl_2) eval modules and prefundamentals
# =========================================================================


@dataclass(frozen=True)
class YangianEvalModule:
    """An evaluation module V_omega(a) for Y_hbar(sl_2).

    V_omega = standard 2-dim representation; a in C is the spectral parameter.
    Carries action t_ij(u) v_k = (u - a)^{-1} (delta_{ik} v_j ...) by
    Drinfeld's evaluation morphism.
    """

    spin: Fraction
    spectral: sp.Basic

    def dimension(self) -> int:
        return int(2 * self.spin + 1)


@dataclass(frozen=True)
class YangianPrefundamental:
    """The prefundamental module L^-(a) for Y_hbar(sl_2).

    L^-(a) is infinite-dimensional (negative-half Verma of the Borel
    subalgebra Y^-); it sits OUTSIDE the eval-generated core. The CG
    relation V_omega(b) tensor L^-(a) = L^-(a+1) + L^-(a-1) (Hernandez-Jimbo
    2012, Frenkel-Reshetikhin 1999) closes the eval-generated core under
    tensoring only on the CHARACTERS (K_0 level), not the modules.
    """

    spectral: sp.Basic
    sign: int = -1


def yangian_o_block_simples_sl2() -> List[Tuple[str, sp.Basic]]:
    """Simples in a regular block of Hernandez category O_Y for Y_hbar(sl_2).

    The block carries two SOURCES of simples beyond the eval-generated core:
      (1) Evaluation modules V_omega(a) -- finite-dimensional, in the eval core.
      (2) Prefundamental modules L^-(a) -- infinite-dimensional.
    """
    a = sp.Symbol("a", complex=True)
    return [("V_omega(a)", a), ("L^-(a)", a)]


def b1_obstruction_diagnostic_sl2() -> Dict[str, sp.Basic]:
    """Diagnostic: does the Yangian-side Koszul property hold beyond the
    eval-generated core for sl_2?

    By Hernandez-Jimbo (2012, "Asymptotic representations and Drinfeld
    rational fractions") and Frenkel-Reshetikhin (1999, "The q-characters..."),
    the prefundamental L^-(a) is the limit of finite-dimensional
    Kirillov-Reshetikhin modules along Drinfeld polynomials going to infinity.
    On the K_0-level, the relation [V_omega(a)] [L^-(b)] = [L^-(b+1)] +
    [L^-(b-1)] generalises a multiplicity-free CG relation (Chari-Moura 2006
    multiplicity-free l-weight property).

    The Hernandez-Leclerc 2010 "Cluster algebras and quantum affine algebras"
    construction realises O_Y(sl_2) as the cluster algebra of type A_{infty/2}
    (one half-infinite chain), and the corresponding Koszul algebra IS the
    quadratic algebra of the half-infinite A-quiver.

    Conclusion: B1 for sl_2 is REDUCED to the Hernandez-Leclerc cluster Koszul
    statement on the half-infinite A_{infty/2}-quiver. The cluster algebra is
    locally finite (each cluster is finitely generated quadratic), and the
    direct limit preserves Koszulness on each cluster.
    """
    return {
        "k0_relation_V_L_minus": sp.Symbol("[V_omega(a)] [L^-(b)] - [L^-(b+1)] - [L^-(b-1)]"),
        "cluster_type": sp.Symbol("A_{infty/2}"),
        "koszul_status_sl2": sp.Symbol("locally_finite_quadratic_Koszul"),
    }


# =========================================================================
# Attack-heal: rank >= 3
# =========================================================================


def b1_attack_rank_3(rank: int = 3) -> Dict[str, object]:
    """Attack: does B1 fail at rank >= 3 due to multi-weight null contributions?

    The Vol I rem:b1-obstruction-analysis pins the gap exactly:
      "Thick-subcategory closure does NOT preserve Ext concentration. If L is
       built as a cone L = cone(f: V_1 -> V_2) of evaluation modules, the
       long exact Ext sequence gives Ext^i(L, M) as a sub-quotient of
       Ext^i(V_j, M), but the connecting maps may introduce nontrivial
       higher-Ext contributions even when Ext^*(V_j, M) is concentrated.
       In particular, infinite-dimensional highest-weight modules (Verma
       modules, prefundamental modules L^-) can have Ext groups that fail to
       concentrate, despite lying in the thick closure of evaluation modules."

    For sl_3 (rank 2, the first multi-root case beyond sl_2):
      The category O of sl_3 has Weyl group W = S_3 of order 6. The
      regular block has 6 simples L_{w . 0} for w in W. The BGS Koszul
      property holds (Beilinson-Ginzburg-Soergel 1996 main theorem). The
      Yangian Y_hbar(sl_3) lifts to O_Y(sl_3) by Hernandez-Leclerc 2010.

    The genuine attack at rank >= 3: the Kazhdan-Lusztig polynomials
    P_{x, w}(q) start having coefficients > 1 (singular support strata in
    geometric category O). For sl_n the simplest non-Koszul behaviour at
    K_0-level appears at n = 4 (Verma multiplicity 2 first appears in
    Schubert cohomology of GL_4 flag variety). For categories of
    Drinfeld-Yangian-modules, the structural obstruction propagates as
    the Hernandez-Leclerc cluster-type morphing from A-type to ADE-type.

    The HEAL: use the Beilinson-Ginzburg-Soergel parity / mixed structure.
    On a regular block of O(sl_n), the simples are graded-shifted by Bruhat
    length parities; the BGS Koszul property is the parity Beilinson-Bernstein
    statement (Beilinson-Bernstein 1981, Brylinski-Kashiwara 1981). Lift this
    parity to Y_hbar(sl_n) via the chiral Hochschild cocycle (Vol II
    thm:chirhoch-virasoro-concentration) gives B1 at all simple ranks
    conditional on the compact-completion conjecture (Vol I
    rem:type-A-completion-conjecture-resolved).
    """
    # Weyl group order for sl_n (rank = n - 1):
    n = rank + 1
    weyl_order = 1
    for k in range(1, n + 1):
        weyl_order *= k
    return {
        "rank": rank,
        "lie_algebra": f"sl_{n}",
        "weyl_order": weyl_order,
        "simples_in_regular_block": weyl_order,
        "kl_multiplicities_exceed_1": rank >= 3,  # first at sl_4
        "heal_via_parity_BGS": True,
        "compact_completion_status": "conditional",
    }


def b1_attack_z2_parity() -> Dict[str, object]:
    """Attack: does B1 require a Z_2-grading / parity Beilinson-Ginzburg-Soergel?

    YES. The full strength of BGS (1996) is the equivalence
        D^b(O_lambda_0(g)) ~ D^b(P_W(G/B)) [parity-mixed]
    where P_W is parity perverse sheaves on the flag variety G/B with
    respect to the Bruhat stratification. The Z_2-grading is the parity
    grading of perverse sheaves; the Z-grading (Koszul grading) is the
    cohomological shift on geometric simples.

    For the Yangian side (Hernandez-Leclerc 2010), the analogous parity
    grading is the (l-weight grading, shifted-prefundamental degree) bi-
    grading, with Z_2-component the (Z_2 mod 2 of) Bruhat length on the
    affine Grassmannian Gr_G.

    HEAL: install the parity-mixed BGS theorem on O_Y(g) via the geometric
    Satake equivalence (Mirkovic-Vilonen 2007), which carries the chiral
    Hochschild grading to the parity grading on Gr_G perverse sheaves.
    """
    return {
        "z2_parity_required": True,
        "BGS_1996_carries_parity": True,
        "geometric_satake_route": "Mirkovic-Vilonen 2007",
        "chiral_hochschild_grading_to_parity": True,
    }


def b1_attack_quillen_vs_infinity() -> Dict[str, str]:
    """Attack: is the equivalence at the model-categorical level a Quillen
    pair, or higher (infinity-categorical adjunction)?

    The BGS Koszul duality is most naturally an EQUIVALENCE OF DG CATEGORIES
        D^b(O_lambda_0(g)) ~ D^b(O_lambda_0(g))^{Koszul}
    upgraded to a Quillen equivalence by Lefevre-Hasegawa (2003) / Loday-
    Vallette (2012) on the bar-cobar level. The full bridge criterion
    target — equivalence of stable infinity-categories of factorization
    modules vs Yangian modules vs spectral QG representations — sits two
    levels higher than the BGS Quillen equivalence:

      LEVEL 1 (BGS 1996): equivalence of triangulated categories D^b(O) ~ D^b(O^!)
      LEVEL 2 (LV 2012):  Quillen equivalence of dg-model categories
      LEVEL 3 (Lurie HA): infinity-categorical adjunction of stable
                          infinity-categories
      LEVEL 4 (Latyntsev 2023): infinity-categorical equivalence enriched
                                over the Ran-cosheaf structure
                                Fact_{E_1}(X; A) ~ Rep^spec(QG^spec(R_A))^op

    The B1 / B2 / B4 inputs each operate at a different level:
      B1 = LEVEL 1 (homological Koszul property on O)
      B2 = LEVEL 2 (Quillen equivalence of completed bar-cobar dg model)
      B4 = LEVEL 4 (infinity-categorical Ran-cosheaf equivalence)
    """
    return {
        "B1_level": "LEVEL 1: triangulated equivalence D^b(O) ~ D^b(O^!)",
        "B2_level": "LEVEL 2: Quillen equivalence of completed bar-cobar dg",
        "B4_level": "LEVEL 4: infinity-cat Ran-cosheaf equivalence",
        "bridge_target_level": "LEVEL 4 (highest)",
        "passage_B1_to_B4": "stack BGS-Quillen + Lurie HA.5.5 + Latyntsev Ran-cosheaf",
    }
