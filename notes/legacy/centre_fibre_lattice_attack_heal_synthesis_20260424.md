# Centre-Fibre Lattice Attack-Heal Synthesis

Date: 2026-04-24.

Scope: synthesis of the architecture swarm, earlier Vol II attack-heal
reports, and the 21-pass ecosystem attack-heal run on fixed-bulk
families of `E_1` chiral boundary algebras, derived centres, lattices,
posets, and mixed holomorphic-topological observables.

Execution discipline: all passes were read-only; no chapter file,
metadata file, compute file, git state, or build product was modified.
The new run used 21 attack-heal passes, batched with at most six live at
once.

## Executive Verdict

The derived-centre construction does not itself produce a canonical
lattice, poset, or meet-join structure on `E_1` chiral algebras.

The native object is the fixed-bulk Morita homotopy fibre of the
derived-centre / bulk functor.  A coarse poset appears only after adding
extra data: a fixed ambient open-sector category, admissible
localisations, and a Hochschild-excision condition forcing the centre
defect to vanish.  A lattice requires still stronger closure theorems;
it is not presently proved.

The correct geometry is not a product of a curve configuration space and
an open `E_1` poset.  It is an incidence version of the mixed
open-closed HT Ran geometry.  The local `\mathsf{SC}^{\mathrm{ch,top}}`
operad is the formal collision shadow of that geometry; the global
object must retain Type III mixed faces, monodromy, periods, curvature,
KZ/KZB transport, and coderived Positselski data.

The same-bulk slogan has one precise meaning:

```tex
\mathfrak B \simeq Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal C)
       \simeq C^\bullet_{\mathrm{ch}}(A_b,A_b)
```

for a chosen closed/bulk object `\mathfrak B`, an open sector
`\mathcal C`, a compact generator `b`, and
`A_b = \mathrm{RHom}_{\mathcal C}(b,b)`.  Different boundary algebras
may occupy the same fixed-bulk fibre.  Non-Morita arrows between them
are not maps inside the fibre; they are relative Hochschild spans or
correspondences.

## Prior Swarm Synthesis

The previous architecture and heptagon swarms converge on these points.

1. The global carrier is `\mathrm{Ran}^{oc}_{HT}(\Sigma_g,I)`, not
   `\mathrm{Ran}(\Sigma_g) \times \mathrm{Ran}(I)`.
2. The local `\mathsf{SC}^{\mathrm{ch,top}}` structure is the formal
   collision shadow of the mixed HT Ran geometry.
3. The relative Feynman transform is a stable-graph bicomplex skeleton.
   It is not a global equivalence without the positive-genus
   comparison theorems.
4. The bulk-boundary object is
   `(Z^{\mathrm{der}}_{\mathrm{ch}}(A),A)`, not `B(A)`.
5. `B(A)` is an `E_1` bar resolution; `\Omega B(A) \simeq A` is
   inversion.  It is not the bulk.
6. Generic strict `E_3` language is unsafe.  The generic bulk has the
   `E_2` chiral brace/derived-centre structure; `E_{k+2}^{top}` appears
   only after an explicit topologisation certificate.
7. Ordered-double Drinfeld-centre equals Hochschild bulk remains
   conjectural unless the exact comparison theorem is supplied.
8. Boundary-linear LG is the clean proved same-bulk sector; global
   all-HT comparisons are conditional or conjectural.

## Fixed-Bulk Fibre

Definition-level object:

```tex
\mathrm{Bnd}^{Mor}_{\mathfrak B}(\Sigma_g,I)
 :=
\mathrm{Bnd}^{Mor}_{HT}(\mathrm{Ran}^{oc}_{HT})
\times^h_{\mathrm{Bulk}_{HT}}
\{\mathfrak B\}.
```

An object is a triple `(C,b,eta)`:

```tex
b \in \mathcal C \quad\text{compact generator},\qquad
A_b := \mathrm{RHom}_{\mathcal C}(b,b),
```

with a specified equivalence

```tex
\eta:
\mathfrak B \simeq Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal C)
\simeq C^\bullet_{\mathrm{ch}}(A_b,A_b).
```

Morphisms inside the fibre are Morita equivalences preserving `eta`.
The specified equivalence is part of the data; otherwise automorphisms
of `\mathfrak B` are lost and the fibre is not homotopy-correct.

Status: definition.  The boundary-linear exact sector is proved locally
in the existing manuscript.  The global mixed HT version is conditional
on the derived-centre functor, descent, and bulk-Hochschild comparison
in that scope.

## Localisation Poset

The attack-heal conclusion is that "localisation lattice" is too strong
at present.  The safe object is the admissible localisation poset.

For a fixed `Z`-linear open sector `\mathcal C`, a kernel `K` is
centre-neutral Hochschild-excisive if:

1. `K` is `Z`-stable, localising, compactly generated, and admissible
   enough for the quotient `\mathcal C/K` to stay in the ambient HT
   category.
2. The chiral Hochschild localisation/excision triangle exists.
3. The centre defect vanishes:

```tex
\Delta_Z(K)
 :=
\mathrm{fib}\bigl(
Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal C)
 \to
Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal C/K)
\bigr)
\simeq 0.
```

Then such kernels form a preorder under inclusion, and a poset after
quotienting by equivalence.  Meet and join formulas

```tex
K_1 \wedge K_2 = K_1 \cap K_2,\qquad
K_1 \vee K_2 = \mathrm{Loc}_Z(K_1\cup K_2)
```

are conditional on accessibility, compact generation, and a Mayer-
Vietoris theorem for the centre defect:

```tex
\Delta_Z(K_1\vee K_2)
\simeq
\Delta_Z(K_1)
\oplus_{\Delta_Z(K_1\cap K_2)}
\Delta_Z(K_2).
```

Status: definition plus conditional theorem schema.  Do not call this a
lattice until the closure and defect-Mayer-Vietoris theorem is proved.

## Incidence HT Ran Geometry

The proposed geometric carrier is an incidence prestack over the mixed
open-closed HT Ran geometry, not a separated product:

```tex
\mathrm{Ran}^{cf,oc}_{HT}
 :=
\int_{\iota\in \mathrm{Inc}_{cf}}
\mathrm{Ran}^{oc}_{HT}(C_\iota,D_\iota,\tau_\iota).
```

An incidence object records:

1. a curve or degeneration stratum;
2. a chosen fixed-bulk datum;
3. an `E_1` chiral reduction or specialisation flag;
4. a localisation flag;
5. the mixed Type III open-closed face data.

Observables should be organised as a constructible factorisation cosheaf
on the exit category of this incidence geometry.  This is where the
bulk theory stratifies over boundary presentations: the strata are not
abstract lattice points, but incidence cells carrying boundary algebras,
centre identifications, and mixed HT collision data.

Status: prestack definition and research programme.  Stack descent,
conical smoothness, exit-path constructibility, and centre-functoriality
remain proof obligations.

## Operadic and Properadic Structure

The safe operadic object is a `P`-indexed local
`\mathsf{SC}^{\mathrm{ch,top}}` opfibration:

```tex
\pi:
\mathsf{SC}^{\mathrm{ch,top}}_{P,loc}
\longrightarrow
\mathrm{Exit}(P).
```

For `p in P`, the colours are

```tex
c_p = Z^{\mathrm{der}}_{\mathrm{ch}}(A_p),
\qquad
o_p = A_p.
```

For an incidence arrow `alpha:p -> q`, transport data are not automatic.
They require centre-preserving maps or spans:

```tex
r^c_\alpha:c_p\to c_q,\qquad
r^o_\alpha:o_p\to o_q,
```

or, for non-Morita arrows, a relative Hochschild correspondence

```tex
Z^{\mathrm{der}}_{\mathrm{ch}}(A)
\leftarrow
C^\bullet_{\mathrm{ch}}(A,M_F,A')
\rightarrow
Z^{\mathrm{der}}_{\mathrm{ch}}(A').
```

Cross-index operations are generated by transport along exit paths to
the output stratum followed by the fibrewise
`\mathsf{SC}^{\mathrm{ch,top}}` operation.  There are no open-to-closed
outputs and no Dunn-additivity collapse to a single-coloured `E_3`
object.

Status: conditional construction.  The descent/coherence theorem and
span-composition theorem are unproved.

## Formal Moduli

The tangent theory of a fixed-bulk boundary is not just `HH^2(A,A)`.
After choosing the bulk equivalence, the governing complex is the
homotopy fibre of the derived-centre deformation map:

```tex
\mathfrak g_A
 :=
\mathrm{Def}_{E_1^{ch}}(A)
\simeq
\mathrm{Conv}((E_1^{ch})^!,\mathrm{End}_A)^{m_A},
```

```tex
dZ_A:\mathfrak g_A\to \mathfrak g_{\mathfrak B},
\qquad
\mathfrak g_{A|\mathfrak B}
 :=
\mathrm{hofib}(dZ_A)
\simeq
\mathrm{Cone}(dZ_A)[-1].
```

Then

```tex
\mathrm{Def}_{A|\mathfrak B}(R)
\simeq
\mathrm{MC}(\mathfrak g_{A|\mathfrak B}\otimes\mathfrak m_R).
```

With this convention, infinitesimals are `H^1`, automorphisms are
`H^0`, and obstructions are `H^2` of the fixed-bulk deformation
complex.  Existing brace-complex wording should be checked for degree
shift drift.

Status: conditional on the chain-level `dZ_A` map and the two-coloured
higher-Deligne / bulk-comparison package outside the exact sector.

## Same-Bulk Examples

Proved or narrow theorem-level:

1. Boundary-linear LG with `W=<y,F(x)>`:
   `Z^{der}(B_{L,W}) \simeq HH(B_{L,W})
   \simeq O(T^*[-1]Z_F^{der}) \simeq O(dCrit(W))`.
2. Affine half-space Neumann/Dirichlet in the strict linear chiral
   Koszul pair: same mixed BF/CS or affine PVA half-space bulk, with
   narrow hypotheses.
3. Compact-generator changes inside an exact boundary-linear category:
   true up to Morita equivalence and chosen centre equivalence.

Conditional same-bulk:

1. Affine / DS / `W` / Virasoro hCS boundary menus at non-critical
   level with good grading, DS-improved stress tensor, and boundary
   theorem in hand.
2. General finite-type PVA half-space models after the relevant
   boundary conditions are constructed and matched to the same bulk.
3. HT Yang-Mills boundaries in the twisted, Koszul-admissible sector.

Same shadow only unless upgraded by extra theorems:

1. Class S / Schur / AGT.
2. Celestial OPEs and genus-zero bar shadows.
3. K3, `\Delta_5`, `\Phi_{10}`, twisted holography, and scalar BPS or
   automorphic identities.
4. BTZ, Maloney-Witten, Page, JT, and other partition-function shadows
   outside the DS exact sector.

## False Friends

These claims should be refused, repaired, or demoted.

1. Same bulk defines a lattice.
2. Same central charge determines the bulk.
3. Arbitrary quotient, invariant, screening, or orbifold preserves the
   derived centre.
4. Nilpotent orbit closure is a lattice of `E_1` chiral boundary
   algebras.
5. A local collision shadow automatically globalises to a D-module or
   factorisation algebra on the full curve.
6. `A_2^* \cong A_2` as an integral/even lattice.
7. `B(A)` is the bulk.
8. Drinfeld centre equals Hochschild bulk without the ordered-double /
   bulk comparison theorem.
9. Pure topological TFT centre is enough for the Vol II HT bulk.
10. Ordinary algebra maps automatically induce maps on derived centres.

## Repair Targets

The following local anchors should be checked before any theorem-level
inscription of the centre-fibre programme.

1. `chapters/theory/foundations.tex:1151` and `:1328`: bulk-Hochschild
   scope is too broad relative to `chapters/connections/hochschild.tex`.
2. `chapters/theory/sc_chtop_heptagon.tex:1166`: Drinfeld-centre face
   is overmarked unless the exact comparison theorem is supplied.
3. `chapters/theory/factorization_swiss_cheese.tex:1511`: Lurie
   citation for stratified factorisation / exit paths should be checked
   against the actual statement.
4. `chapters/connections/ht_bulk_boundary_line_frontier.tex:2946`:
   `A_2^* \cong A_2` is false as an integral/even lattice statement.
5. `chapters/theory/brace.tex:785`: possible degree-shift drift in
   infinitesimals and obstructions.
6. `chapters/connections/bar-cobar-review.tex:1017`: covariance /
   contravariance mismatch around `\Omega(f^*)` versus `\Omega(B(f))`.
7. `chapters/connections/unified_chiral_quantum_group.tex:852`:
   arbitrary-nilpotent DS centre-preservation is too broad without the
   DS-Hochschild compatibility theorem.
8. `compute/tests/test_chd_ds_hochschild_iv.py:43`: boolean oracle
   risks promoting all good gradings at non-critical level.
9. `compute/lib/hochschild_bulk_bridge.py:205`: lattice VOA handling is
   rank-only and cannot see discriminant/simple-current data.
10. `compute/lib/hochschild_bulk_bridge.py:379`: bulk and chiral
    Hochschild dimensions are currently same-source formulas, not
    independent verification.
11. `chapters/theory/curved_dunn_higher_genus.tex:2064` and
    `chapters/theory/pva-descent-repaired.tex:1779`: `kappa_ch^{K3}=24`
    should be renamed/scoped as fibre or topological Euler data.
12. `chapters/theory/infinite_fingerprint_classification.tex:181`:
    `kappa_BKM = kappa_ch + chi(O_fiber)` is not a theorem; at `N=1`
    it is at most convention-mixing numerology.

## Compute Surface

The compute layer should support the programme by finite, falsifiable
witnesses, not by theorem inflation.

Recommended additions:

1. Boundary-linear LG centre-equality witness: compute `Jac(x^3/3) =
   C[x]/(x^2)` independently, compute algebraic centre by centraliser
   matrices, and compare multiplication tables.
2. Centre-defect localisation engine: nodes encode sector and curvature
   visibility; edges carry explicit centre-defect data.
3. Relative Hochschild span sanity tests: degree support, finite rank,
   Euler/rank consistency, span inclusion.
4. Lattice discriminant/simple-current checks using Gram matrices and
   Smith normal form; in particular `A_2` has determinant `3` and
   discriminant group `Z/3`.
5. DS `sl_5` obstruction fixture for a non-principal/non-hook or
   underdocumented good-grading case, returning `conditional` or
   `unsupported` unless explicit data are supplied.

Do not test global Drinfeld-centre equals bulk, all-good-graded DS, or
bulk-Hochschild equality by comparing two implementations of the same
formula.

## Proposed AP / Cache Guards

Candidate pattern guards for a future cache update:

1. Same bulk does not define a lattice.
2. Same central charge is not same bulk.
3. Quotients do not preserve centres by default.
4. DS orbit closure is not a lattice of chiral structures.
5. Local shadow does not globalise automatically.
6. `A_2^* \ne A_2` as a lattice.
7. Bar is not bulk.
8. Drinfeld centre is not Hochschild bulk without the conjecture.
9. Pure TFT centre is only a projection.

These are proposed entries only; no cache or registry file was edited in
this run.

## Inscription Package

If the manuscript receives a new centre-fibre section, the safe order is:

1. Definition: fixed-bulk Morita homotopy fibre.
2. Definition: centre-neutral Hochschild-excisive localisation.
3. Proposition: admissible localisations form a localisation poset after
   quotienting by equivalence; do not call it a lattice.
4. Conditional proposition: fixed-bulk transport along admissible arrows.
5. Definition: centre-fibre incidence HT Ran prestack.
6. Conjecture: incidence descent to an HT Ran stack.
7. Conditional construction: exit-path indexed Swiss-cheese opfibration.
8. Definition: relative Hochschild span for non-Morita arrows.
9. Conjecture: span functoriality.

Suggested section title: "Fixed-Bulk Centre Fibres".

Suggested subsections:

1. Morita Fibres of the Derived Centre.
2. Centre-Neutral Localisations.
3. Incidence over the Mixed HT Ran Geometry.
4. Exit Transport and Relative Hochschild Spans.

Forbidden phrases until the missing theorems are proved:

1. localisation lattice;
2. centre-fibre lattice;
3. universal fixed-bulk theorem;
4. all localisations preserve the centre;
5. non-Morita arrows in the fixed-bulk fibre;
6. the incidence stack, before descent is proved;
7. boundary-to-bulk exit arrow;
8. Dunn additivity identifies the two-coloured object with `E_3`.

## Open Proof Obligations

1. Construct the derived-centre / bulk functor in the mixed HT Ran
   setting with the required Morita localisation.
2. Prove chiral Hochschild localisation/excision for admissible kernels.
3. Prove the centre-defect Mayer-Vietoris formula.
4. Establish descent for the incidence HT Ran prestack, including Type
   I-IV face compatibility.
5. Prove exit-path constructibility and the coherence theorem for the
   indexed `\mathsf{SC}^{\mathrm{ch,top}}` opfibration.
6. Prove composition for relative Hochschild spans and compatibility
   with `\mathsf{SC}^{\mathrm{ch,top}}` directionality.
7. Supply global KZB / prime-form / monodromy comparisons for positive
   genus.
8. Establish Positselski cone/coacyclicity hypotheses in the curved
   sectors.
9. Build the two-coloured cobar contracting homotopy needed for strict
   chain-level refinements.
10. Prove or demote the ordered-double Drinfeld-centre / bulk
    comparison.
11. Separate cross-volume `kappa` conventions: `kappa_ch`, `kappa_cat`,
    `kappa_BKM`, `kappa_fiber`, and Vol I `K^kappa`.

## Stable Core

The strongest synthesis is therefore:

The observables of a mixed HT bulk geometry stratify not over a bare
lattice of chiral algebras, but over a centre-fibre incidence geometry
whose points are boundary presentations equipped with a specified
derived-centre equivalence to a common bulk.  The fixed-bulk part is a
Morita homotopy fibre.  The reducible/combinatorial part is an
admissible localisation poset only after Hochschild-excision and
centre-neutrality are imposed.  Non-Morita moves are relative
Hochschild spans.  The local operadic shadow is
`\mathsf{SC}^{\mathrm{ch,top}}`; the global HT object is the incidence
open-closed Ran geometry with curvature, monodromy, and topologisation
data retained.

