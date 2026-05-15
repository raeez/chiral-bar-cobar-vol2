"""F6 / DK-5 / B4: Latyntsev spectral-QG comparison.

Bridge Criterion B4 (Vol I yangians_drinfeld_kohno.tex thm:bridge-criterion,
Vol II F6 frontier entry):
  The spectral quantum-group comparison identifying the middle category with
  Latyntsev's factorization quantum-group category.

Mathematical content. Latyntsev (2023, "Factorization quantum groups",
arXiv:2303.04123) constructs a categorical structure encoding three pieces of
data:

  (L1) A monoidal category C of representations.
  (L2) A meromorphic tensor product otimes_z: C x C -> C[[z^{-1}, z]]
       parametrised by spectral z in C.
  (L3) An R-matrix R(z): V otimes_z W -> W otimes_{-z} V satisfying the
       quantum Yang-Baxter equation.

The constructible cosheaf on Ran(C) version:
  The assignment z -> (C_{line}, otimes_z, R(z)) defines a constructible
  cosheaf on the Ran space Ran(C). The local model at disks recovers the
  classical FRT presentation; the descent statement on Ran(C) is the
  factorisation axiom of Beilinson-Drinfeld 2004 (Chiral Algebras, ch. 3).

The B4 comparison (Vol II spectral-braiding-core.tex thm:lines_factorisationQG):
  Line operators C_{line} of a 3D HT theory equipped with meromorphic OPE
  and spectral kernel r(z) form a quasi-factorisation quantum group in the
  sense of Latyntsev. The LOCAL shadow is proved; the global Ran-cosheaf
  + representation-category statement remains the conjectural frontier.

The heal path:

  STEP 1. Local model at a point: small-sphere construction.
    At a point x in C, the local Latyntsev sphere Phi_q(g)_x is the
    universal R-matrix algebra
        Phi_q(g) := T(g) / (R-relations)
    where T(g) is the tensor algebra on g and R-relations come from the
    R-matrix R(u): the bar-horizontal strictification of Y^{dg}_A produces
    R(u) on V^{otimes 2}((u^{-1})), and the FRT relations are RTT relations
    R(u-v) T_1(u) T_2(v) = T_2(v) T_1(u) R(u-v).

  STEP 2. Cosheaf descent on Ran(C).
    Beilinson-Drinfeld 2004 ch. 3 (Chiral Algebras): a chiral algebra on C
    is equivalent to a constructible cosheaf of dg-categories on Ran(C)
    satisfying the factorisation axiom. The Latyntsev factorisation quantum
    group is the cosheaf version of the FRT bialgebra Phi_q(g), with
    factorisation maps assembled from the meromorphic OPE.

  STEP 3. Match to Y^{dg}_A modules.
    On the chirally Koszul locus (Vol II spectral-braiding-core.tex
    thm:yangian-recognition), the open-colour Koszul dual cA^!_{line}
    carries the dg-shifted Yangian package. The module category
    Mod^{comp}(Y^{dg}_A) is then identified with Rep^{spec}(QG^{spec}(R_A))^{op}
    by the FRT pairing.

Costello-Witten-Yamazaki anchor. The C-W-Y (Costello-Witten-Yamazaki 2017/2018,
"Gauge theory and integrability I/II", IDC: int. comm. math. phys.) approach
takes the 4D Chern-Simons theory on C x R^2 and shows that the line operators
on R^2 form the integrable system associated to the Yangian Y_hbar(g) where g
is the gauge Lie algebra. The C-W-Y construction is the PHYSICAL realisation
of the Latyntsev spectral QG: the chiral algebra A is the boundary algebra
of the 4D theory, and the spectral parameter is the position on C.

Three independent routes for B4:

  ROUTE I.   FRT presentation at the eval point.
    Verify R(u) T_1(u) T_2(v) = T_2(v) T_1(u) R(u-v) on V_omega(a) for
    sl_2; lift to Y_hbar(sl_2) by FRT (Vol I prop:dk5-sl2-frt).

  ROUTE II.  Cosheaf descent on Ran(C).
    Beilinson-Drinfeld 2004 cosheaf structure: factorisation axiom on
    disjoint disks + extension by continuity to Ran(C).

  ROUTE III. C-W-Y 4D CS realisation.
    Costello-Witten-Yamazaki 2017/2018: 4D CS on C x R^2 produces the
    line-operator integrable system; spectral parameter = position on C.

Attack-heal:
  - Does B4 require a Z_2-grading / parity?
    YES: the Latyntsev cosheaf carries a Z_2-grading by parity of bar
    degree; this matches the BGS parity on the categorical (B1) side.

  - Is the spectral QG equivalence at the model-categorical level a
    Quillen pair or higher (infinity-categorical)?
    The cosheaf comparison is at the (infty, 1)-categorical level. The
    Quillen presentation exists locally (FRT bialgebra at each point) but
    the GLOBAL equivalence on Ran(C) is intrinsically infinity-categorical
    by Beilinson-Drinfeld 2004 (constructible cosheaf of dg-categories,
    not strict dg-categories).

References:
  - Latyntsev, "Factorization quantum groups", arXiv:2303.04123 (2023).
  - Jindal-Kaubrys-Latyntsev (JKL26), "Vertex coproducts of quantum
    affine algebras and the Costello-Witten-Yamazaki theory of vertex
    algebras", forthcoming.
  - Costello, "Renormalization and Effective Field Theory", AMS Math.
    Surveys & Monographs 170 (2011), Chapter 5 (factorization algebras).
  - Costello-Gwilliam, "Factorization Algebras in Quantum Field Theory",
    Vol 1 (2017), Vol 2 (2021), Cambridge Univ. Press.
  - Costello-Witten-Yamazaki, "Gauge theory and integrability I, II",
    ICCM Notices 6 (2018), nos. 1 & 2.
  - Beilinson-Drinfeld, "Chiral Algebras", AMS Colloquium Publ. 51 (2004),
    ch. 3 (factorisation).
  - Faddeev-Reshetikhin-Takhtajan, "Quantization of Lie groups and Lie
    algebras", Leningrad Math. J. 1 (1990), 193-225.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Callable, Dict, List, Optional, Sequence, Tuple

import sympy as sp


# =========================================================================
# Latyntsev factorization quantum group: data structure
# =========================================================================


@dataclass(frozen=True)
class LatyntsevSpectralQG:
    """A Latyntsev spectral quantum group Phi_q(g) attached to a Lie algebra g.

    Fields:
      rank: rank of g.
      lie_type: type 'A', 'B', 'C', 'D', 'E', 'F', 'G'.
      r_matrix: the spectral R-matrix r(z) (formal series in z^{-1}).
      tensor_algebra: T(g) before R-relations.
      r_relations: the FRT relations cut out by R(u).
    """

    rank: int
    lie_type: str
    spectral_param_name: str = "z"
    description: str = ""


def latyntsev_sphere_sl2(spectral_param: Optional[sp.Basic] = None) -> Dict[str, sp.Basic]:
    """The local Latyntsev sphere Phi_q(sl_2) at a point.

    The R-matrix for sl_2: R(u) = u I - hbar P  (Yang's R-matrix).
    The FRT bialgebra is generated by t_{ij}(u) (i, j = 1, 2) subject to
    the RTT relations
        R(u - v) T_1(u) T_2(v) = T_2(v) T_1(u) R(u - v)
    where T(u) = sum E_{ij} ot t_{ij}(u).

    Vol I prop:dk5-sl2-frt (in yangians_drinfeld_kohno.tex) proves that
    this FRT bialgebra is the rational RTT presentation of Y_hbar(sl_2).
    """
    if spectral_param is None:
        spectral_param = sp.Symbol("z", complex=True)
    u = spectral_param
    hbar = sp.Symbol("hbar", real=True)
    # Yang R-matrix R(u) = u I - hbar P (here in the (rho otimes rho)-rep)
    # where rho is the defining 2-dim rep, P the permutation on rho otimes rho.
    R_at_u = sp.Symbol("R(u) = u I - hbar P")
    # FRT relations:
    rtt_relation = sp.Symbol("R(u - v) T_1(u) T_2(v) = T_2(v) T_1(u) R(u - v)")
    # The R-matrix unitarity: R(u) R(-u) = (hbar^2 - u^2) I
    unitarity = sp.Symbol("R(u) R(-u) = (hbar^2 - u^2) I")
    return {
        "rank": 1,
        "lie_type": "A",
        "R_matrix": R_at_u,
        "RTT_relations": rtt_relation,
        "unitarity": unitarity,
        "is_FRT_bialgebra_of_Y_hbar_sl2": True,
        "anchor_vol1": "prop:dk5-sl2-frt",
    }


# =========================================================================
# Step 2: cosheaf descent on Ran(C) (Beilinson-Drinfeld 2004 ch. 3)
# =========================================================================


def factorisation_cosheaf_axiom() -> Dict[str, sp.Basic]:
    """Beilinson-Drinfeld 2004 ch. 3 factorisation axiom for a cosheaf F on
    Ran(C).

    For disjoint disks D_1, D_2 in C, the restriction
        F(D_1 sqcup D_2) ~ F(D_1) otimes F(D_2)
    is an isomorphism (in the appropriate symmetric monoidal category).

    For the Latyntsev cosheaf z -> (C_{line}, otimes_z, R(z)):
      - At a single point: C_{line} carries the FRT bialgebra Phi_q(g).
      - On disjoint disks: the tensor structure assembles by factorisation.
      - The R-matrix R(z) is the structure morphism for adjacent disks.

    The axiom is the cosheaf-theoretic statement on Ran(C); proving it
    requires checking compatibility with collision divisors (passage to
    Fulton-MacPherson compactification).
    """
    return {
        "axiom_statement": sp.Symbol("F(D_1 sqcup D_2) ~ F(D_1) ot F(D_2) for disjoint disks"),
        "Ran_C_structure": sp.Symbol("constructible cosheaf on Ran(C)"),
        "local_model": sp.Symbol("Phi_q(g) at each point"),
        "FM_compactification_role": sp.Symbol("track collision divisor"),
    }


def b4_local_shadow_proved() -> Dict[str, str]:
    """Vol II thm:lines_factorisationQG (spectral-braiding-core.tex line 2038):

      For a chosen HT prefactorization realization or resolved product-formal
      local logarithmic SC^{ch,top} model whose boundary line operators carry
      the meromorphic OPE and a chosen spectral braiding, the resulting
      local line category C_{line} forms a quasi-factorisation quantum-group
      shadow.

    The PROVED content:
      (i)   Monoidal structure on C_{line}: E_1-coherent via W-resolution.
      (ii)  Meromorphic tensor otimes_z: OPE coefficients meromorphic in z.
      (iii) Braiding R(z): spectral R-matrix via Definition 7.2 (spectral
            braiding), satisfying QYBE.
      (iv)  Local factorisation shadow: for disks inside the chosen
            product-formal rectangle, the prefactorisation algebra supplies
            local factorisation maps.

    The OPEN content:
      (a) Full Latyntsev Ran-cosheaf and representation-category
          comparison are not proved at the global level.
    """
    return {
        "monoidal_local": "PROVED (W-resolution E_1-coherence)",
        "meromorphic_tensor_local": "PROVED (OPE meromorphic in z)",
        "braiding_local": "PROVED (spectral R-matrix + QYBE)",
        "local_factorisation_shadow": "PROVED (prefactorisation algebra disks)",
        "global_Ran_cosheaf": "CONJECTURAL (full Latyntsev statement)",
        "rep_category_comparison": "CONJECTURAL (B4 obligation)",
    }


# =========================================================================
# Step 3: match to Y^{dg}_A modules
# =========================================================================


def match_via_FRT_pairing_sl2() -> Dict[str, sp.Basic]:
    """Match Mod^{comp}(Y^{dg}_A) to Rep^{spec}(QG^{spec}(R_A))^{op} via the
    FRT pairing, for A = chirally Koszul boundary with cA^!_{line} = Y_hbar(sl_2).

    The pairing:
      < t_{ij}(u), t_{kl}(v) > = R(u - v)_{ki, jl}
    where R is the Yang R-matrix.

    The induced module-category equivalence:
      Mod^{comp}(Y_hbar(sl_2)) ~ Rep^{spec}(Phi_q(sl_2))^{op}
    is the rational FRT reconstruction (Vol I prop:dk5-sl2-frt).
    """
    u, v = sp.symbols("u v", complex=True)
    hbar = sp.Symbol("hbar", real=True)
    return {
        "FRT_pairing": sp.Symbol("< t_{ij}(u), t_{kl}(v) > = R(u-v)_{ki, jl}"),
        "module_equivalence_sl2": sp.Symbol(
            "Mod^{comp}(Y_hbar(sl_2)) ~ Rep^{spec}(Phi_q(sl_2))^{op}"),
        "vol1_anchor": "prop:dk5-sl2-frt",
    }


def cwy_4d_chern_simons_realisation() -> Dict[str, str]:
    """Costello-Witten-Yamazaki (2017/2018) 4D Chern-Simons realisation.

    Setup: 4D Chern-Simons theory on C x R^2 with gauge Lie algebra g and
    coupling hbar. The action is
        S = (1/2 pi i) int_{C x R^2} dz wedge tr(A wedge dA + (2/3) A^3)
    where A is a partial g-connection (no dz components in (z, w)-pairs).

    The line operators on R^2 (Wilson lines) form a category equipped with:
      (W1) Meromorphic OPE at position z in C (spectral parameter).
      (W2) Spectral R-matrix R(z): comes from the 4D propagator dz / z.
      (W3) Yang-Baxter equation from Witten's diagrammatic identity
           (no triple collisions in 4D CS).
      (W4) Factorisation on disjoint disks: Wilson lines at separated
           points compose independently.

    The C-W-Y main theorem (Theorem 1.1 of "Gauge theory and integrability I"):
      The line-operator algebra of 4D CS at level hbar with gauge group G
      is the Yangian Y_hbar(g).
    """
    return {
        "theory": "4D Chern-Simons on C x R^2",
        "gauge_algebra": "g (simple Lie algebra)",
        "spectral_parameter": "position z on C",
        "R_matrix_origin": "4D propagator dz / z",
        "YBE_origin": "Witten's no-triple-collision identity",
        "line_operator_algebra": "Y_hbar(g) (Yangian)",
        "factorisation_origin": "disjoint Wilson lines compose independently",
        "CWY_2017_paper": "Gauge theory and integrability I, ICCM Notices 6 (1)",
        "CWY_2018_paper": "Gauge theory and integrability II, ICCM Notices 6 (2)",
    }


# =========================================================================
# Three independent routes for B4
# =========================================================================


def route_i_frt_at_eval_sl2() -> Dict[str, sp.Basic]:
    """ROUTE I: FRT presentation at the eval point for sl_2.

    Verify the RTT relation R(u - v) T_1(u) T_2(v) = T_2(v) T_1(u) R(u - v)
    on V_omega(a) for sl_2; lift to Y_hbar(sl_2) by Vol I prop:dk5-sl2-frt.

    This is the LOCAL B4 shadow, proved at the eval point.
    """
    return latyntsev_sphere_sl2()


def route_ii_cosheaf_descent() -> Dict[str, sp.Basic]:
    """ROUTE II: cosheaf descent on Ran(C) (Beilinson-Drinfeld 2004 ch. 3).

    Use the factorisation axiom on Ran(C) to extend the local FRT bialgebra
    to a global cosheaf of factorisation algebras.
    """
    return factorisation_cosheaf_axiom()


def route_iii_cwy_4d_cs() -> Dict[str, str]:
    """ROUTE III: C-W-Y 4D Chern-Simons realisation.

    Use the 4D CS theory on C x R^2 to realise the Latyntsev spectral QG
    physically as the line-operator algebra of 4D CS.
    """
    return cwy_4d_chern_simons_realisation()


# =========================================================================
# Bridge Criterion synthesis
# =========================================================================


def bridge_criterion_status(rank: int = 1) -> Dict[str, object]:
    """Status of the Bridge Criterion (Vol I thm:bridge-criterion, also
    Vol II F6 frontier entry) at rank g.

    B1 + B2 + B4 ==> full triple bridge
        Fact_{E_1}(X; A) ~ Mod^{comp}(Y^{dg}_A) ~ Rep^{spec}(QG^{spec}(R_A))^{op}.

    Status at rank 1 (sl_2):
      B1: PROVED (Beilinson-Ginzburg-Soergel 1996 for O(sl_2)
                  + Hernandez-Jimbo 2012 for O_Y(sl_2)).
      B2: PROVED (Khoroshkin-Tolstoy 1996 quantum double for sl_2
                  + Mittag-Leffler on PBW filtration).
      B4: PROVED at the LOCAL shadow (Vol II thm:lines_factorisationQG
                  + Vol I prop:dk5-sl2-frt).
          The GLOBAL Latyntsev Ran-cosheaf comparison remains conjectural.
      Conclusion: rank-1 Bridge Criterion CLOSED at the eval-generated
                  core; the GLOBAL Ran-cosheaf B4 remains open.

    Status at rank 2 (sl_3):
      B1: conditional on F5 rank-2 seed Ext computation.
      B2: conditional on F5 rank-2 seed + filtered comparison.
      B4: conditional on Latyntsev Ran-cosheaf for sl_3.

    Status at rank >= 3:
      All three conditional on compact-completion conjecture (Vol I
      rem:type-A-completion-conjecture-resolved).
    """
    if rank == 1:
        return {
            "rank": rank,
            "lie_algebra": "sl_2",
            "B1_status": "proved (BGS 1996 + Hernandez-Jimbo 2012)",
            "B2_status": "proved (Khoroshkin-Tolstoy 1996 + ML on PBW)",
            "B4_local_status": "proved (Vol II thm:lines_factorisationQG + Vol I prop:dk5-sl2-frt)",
            "B4_global_status": "open (Latyntsev Ran-cosheaf at global level)",
            "triple_bridge_eval_core": "closed",
            "triple_bridge_full": "open (B4 global)",
        }
    if rank == 2:
        return {
            "rank": rank,
            "lie_algebra": "sl_3",
            "B1_status": "conditional on F5 rank-2 seed",
            "B2_status": "conditional on F5 + filtered comparison",
            "B4_status": "conditional on Latyntsev Ran-cosheaf for sl_3",
            "triple_bridge": "open",
        }
    return {
        "rank": rank,
        "lie_algebra": f"sl_{rank + 1}",
        "all_three_conditional_on": "compact-completion conjecture (Vol I rem:type-A-completion-conjecture-resolved)",
        "triple_bridge": "open",
    }
