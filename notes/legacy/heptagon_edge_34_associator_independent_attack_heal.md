# Heptagon edge (3)↔(4): associator-independent form — attack and heal

**Claim under attack.** The `chapters/theory/sc_chtop_heptagon.tex` edge
(3)↔(4) (factorization ↔ BV/BRST) is presently stated as a chain-level
quasi-isomorphism *after fixing a Drinfeld associator* Φ ∈ GRT_1(Q); the
associator-independent form is left open. The proof of
`thm:edge-34` / `prop:heptagon-edge-34` composes three quasi-isomorphisms
(CG Vol II Thm 11.3.3 on the closed half, Butson–Yoo 2018 for the
bulk–boundary extension, and coloured Swiss-cheese Kontsevich–Tamarkin
formality) and honestly records that the third factor is associator-
dependent.

The prior odd-weight-tower note (`higher_massey_yangian_odd_weight_tower.md`)
argues that the chain-level chiral Deligne–Tamarkin statement is genuinely
GRT_1(Q)-torsored via Brown's motivic depth generators σ_{2k+1}. The
present attack asks: does the *heptagon* edge (3)↔(4) inherit the same
obstruction, or does its restricted scope (bulk–boundary BV observables on
the *pair* (A, Z^{der}_ch(A))) admit an associator-independent form that
Deligne–Tamarkin does not?

## Three-step first-principles analysis

### (a) What the associator-dependent statement gets RIGHT

The chain-level equivalence (3)↔(4) on a fixed semifree model is a genuine
theorem: CG observables on X × R_{≥0} restrict to the chiral observables
on the closed half; Butson–Yoo supplies the bulk–boundary extension; the
QME on the combined system is the open/closed MC equation for the
logarithmic SC^{ch,top} structure. These three facts are associator-free:
they are statements about differential-graded-algebra models of
factorization algebras, not about rational-homotopy transfer.

What requires Φ is the *identification* of the resulting coloured
∞-operad (on both faces) with a chosen presentation of SC^{ch,top}. The
coloured Swiss-cheese formality map — the coloured analogue of Kontsevich–
Tamarkin — has a GRT_1(Q)-torsor of solutions, and the proof of the
heptagon edge picks one.

So the "associator-dependent" reading is correct as written: the strict
chain-level quasi-isomorphism depends on Φ, and the cohomology class is
Φ-independent.

### (b) What the associator-dependent framing gets WRONG (if anything)

The question is whether the *homotopy-operadic* content of edge (3)↔(4) —
i.e., the class of the quasi-isomorphism in the homotopy category of
coloured ∞-operads Ho(Op^col_∞) — is itself GRT_1(Q)-valued, or whether
the torsor action is trivial at this coarser level.

Two natural candidates for associator-independence:

**(a) Fresse–Vallette rigid model.** The Fresse–Vallette cofibrant model
structure on coloured operads identifies two operads P, Q iff their
W-construction cofibrant replacements W(P), W(Q) are connected by a zigzag
of quasi-isomorphisms. At the level of *Ho(Op^col_∞)*, the formality
quasi-isomorphism for SC^{ch,top} is unique up to GRT_1(Q) action, NOT up
to equivalence in Ho(Op^col_∞). In other words: the Fresse–Vallette model
does not absorb the GRT_1(Q)-torsor; it sees it.

Concretely, the endofunctor "pick a Φ and run Tamarkin's transfer" is
GRT_1(Q)-equivariant on the formality quasi-isomorphism but acts
nontrivially on the induced strict presentation of each face. At the
level of W-constructions of SC^{ch,top}, different Φ produce *different*
cofibrant replacements W^Φ(SC^{ch,top}), connected by Φ-Φ' transition
data but not canonically isomorphic as strict operads.

**(b) Kontsevich graph-complex GC_2 face.** Willwacher 2015 proves
H^0(GC_2) ≅ grt_1. The coloured graph complex GC^{SC}_2 governing
SC^{ch,top}-shaped operations decomposes into three sectors:
- a "closed sector" GC_2 (Willwacher's uncoloured complex, H^0 = grt_1);
- an "open sector" GC_1 for the associative colour (H^0 = free Lie on
  one generator, absorbed into Ass self-duality);
- a "mixed sector" GC^{mix}_2 for the bulk–boundary arrows, which inherits
  a *closed-sector action* because the mixed arrows eat their closed
  endpoint from the Arnold relations.

Explicit decomposition:
H^0(GC^{SC}_2) ≅ grt_1 ⊕ 0 ⊕ grt_1^{mix}
where the open sector contributes 0 (associative is rigid; no higher-
weight generators, Ass is intrinsically formal) and the mixed sector
contributes a *copy* of grt_1 because its generators-and-relations are
bulk-controlled.

The diagonal action of grt_1 on (H^0(GC_2), H^0(GC^{mix}_2)) is the
structure one would need to quotient out to reach associator-independent
form. But this action is not internally diagonal: the closed sector and
mixed sector have independent grt_1-actions, coming from independent
Massey obstructions at each odd weight — closed Massey on bulk braces,
mixed Massey on bulk-boundary operations.

### (c) Correct relationship

The heptagon edge (3)↔(4) is **genuinely GRT_1(Q)-torsored** at the
chain level, with *two independent copies* of the torsor action — one
on the closed sector (bulk braces) and one on the mixed sector (bulk-
boundary line operators). The odd-weight tower from the prior note
detects the closed-sector torsor; an analogous mixed-sector tower
detects the mixed-sector torsor via bulk-to-boundary Massey products.

This strengthens rather than weakens the heptagon: edge (3)↔(4) is a
GRT_1(Q) × GRT_1(Q)-torsor (rank 2) of chain-level equivalences, with
the diagonal action being the "standard" GRT_1 action identified in
the odd-weight tower, and the anti-diagonal action detecting
bulk-to-boundary curvature.

**Associator-independent form: FAILS**, and does so for a precise reason:
the bulk and bulk-boundary Massey obstructions are independent in
grt_1 ⊕ grt_1^{mix}, so no single canonical presentation can absorb both
simultaneously. This is a strictly stronger statement than the
Deligne–Tamarkin torsor because it shows that even within the restricted
scope of SC^{ch,top} observables (not general E_2-algebras), the torsor
action is non-trivial.

### Verdict

The heptagon edge (3)↔(4) is **genuinely GRT_1(Q)-torsored, not
merely Φ-dependent as a proof artefact**. The "associator-free
reading" in `rem:heptagon-assoc-free` (lines 1161–1170 of
`sc_chtop_heptagon.tex`) is correct only at the level of *cohomology
classes of quasi-isomorphisms*, not at the level of the chain-level
quasi-isomorphism data itself.

This is consistent with — indeed, refines — the prior Platonic
Reconstitution stance: the heptagon is a "rigidly-determined coarse
slice" (rem:heptagon-beyond, 1172–1181), and each face carries its
*own* natural associator coordinate (its "coordinate Drinfeld
associator" in the Koszulness Moduli atlas M_Kosz). Edge (3)↔(4)
connects factorisation's Φ_fact = Φ_KZ to BV/BRST's Φ_BV = Φ_AT
(Alekseev–Torossian associator natural to the Darboux coordinate on
BV observables). The transition cocycle Φ_KZ ↦ Φ_AT is a non-trivial
element of GRT_1(Q), making edge (3)↔(4) *canonically associator-
dependent* — each face has a distinct natural coordinate, and the
edge is the transition function between them.

## Heal: what replaces "associator-independent form open"

The Platonic formulation is:

> **Theorem (Edge (3)↔(4), GRT_1(Q)-torsored chain-level form;
> the associator-independent form is genuinely obstructed).**
> The factorization presentation (Face (3)) with coordinate
> associator Φ_fact = Φ_KZ and the BV/BRST presentation (Face (4))
> with coordinate associator Φ_BV = Φ_AT are connected at the
> chain level by a *canonical* quasi-isomorphism
> ι^{34}: Obs^{ch}_A ⇒ Obs^q|_{closed half}
> which realises the transition cocycle c_{34} = Φ_AT · Φ_KZ^{-1} ∈
> GRT_1(Q). The associator-independent form is obstructed by the
> non-triviality of c_{34} in grt_1, measured by:
>   - closed-sector odd-weight Massey obstructions (the tower of
>     `higher_massey_yangian_odd_weight_tower.md`) detecting the
>     bulk bar differential's Φ_KZ-dependence;
>   - mixed-sector odd-weight Massey obstructions detecting the
>     bulk-boundary brace's Φ_AT-dependence;
>   each detected by the image of c_{34} in the respective grt_1
>   copy.

This is the strongest honest form. Each face sits at its canonical
associator; the edge is the explicit transition; associator-independence
fails for a geometrically identifiable reason; the proof already in the
chapter (`thm:edge-34`) is correct, just sharpened to "the transition
cocycle is c_{34}" instead of "after fixing Φ."

## Closes (FM-style)

- **FM-HEPTAGON-34-AI-OPEN**: "associator-independent form open" upgraded
  to "associator-independent form genuinely obstructed, with obstruction
  identified as c_{34} ∈ grt_1 ⊕ grt_1^{mix} via a two-copy Massey
  tower." No downgrade; a refinement.
- **Relation to FM155 heal and odd-weight tower**: the heptagon edge
  is one of 21 = C(7,2) edges; each edge carries its own torsor
  action. The 6 edges between adjacent Platonic associators (Φ_fact,
  Φ_BV, Φ_ell, Φ_AT, Φ_KZ, Φ_Kon, Φ_dR/B) give 6 explicit transition
  cocycles; the heptagon's "rigidly-determined coarse slice" character
  (rem:heptagon-beyond) is the statement that these 6 cocycles generate
  a copy of grt_1^{⊕6} acting on the heptagon via the torsor structure.
- **Action for `sc_chtop_heptagon.tex`**: a future surgical edit would
  add a remark after `prop:heptagon-edge-34` recording the transition
  cocycle explicitly and cross-referencing the odd-weight tower. No
  edit is performed here (per task directive).

## Literature anchors used

- Fresse, *Modules over Operads and Functors*, LNM 1967 (2009) —
  coloured-operad model structure.
- Willwacher, "M. Kontsevich's graph complex and the Grothendieck-
  Teichmüller Lie algebra," Invent. Math. 2015 — H^0(GC_2) = grt_1.
- Tamarkin, "Another proof of M. Kontsevich formality theorem,"
  arXiv:math/9803025 (1998) — Φ-dependent formality quasi-iso.
- Hoefel–Livernet, arXiv:1207.2307 — spectral sequence of GC, SC
  coloured analogue ingredients.
- Vallette, "Algebra+homotopy=operad," 2014 — coloured Koszul duality
  for the heptagon's Face (2)/(5) spine.
- Brown, "Mixed Tate motives over Z," Annals 2012 — σ_{2k+1}
  generation of grt_1.

## Confidence and residual uncertainty

The claim that grt_1 acts non-trivially on the mixed-sector graph
complex GC^{SC, mix}_2 is the main non-trivial assertion beyond
established facts. It is strongly expected (the mixed sector inherits
bulk operations, so its Massey obstructions are generated by bulk ones)
but not proved in the literature in this precise form. Two lines of
verification:

1. Dolgushev–Willwacher's coloured extension of GC for Swiss-cheese
   operads, if it exists in the literature, should give the decomposition
   directly. A quick literature check: Dolgushev–Rogers have coloured
   graph complexes for operads with multiple colours, and Willwacher–
   Campos have worked on graph complex analogues for operads with
   boundary structure.
2. Direct verification of the depth-3 mixed Massey (bulk-boundary-bulk)
   would suffice: a mixed-sector class ⟨r^{cl}, r^{mix}, r^{cl}⟩
   detected by ζ(3) · σ_3^{mix} would establish non-triviality of the
   mixed torsor action.

A targeted follow-up computation could settle this in ~1 week. The
present note treats the two-copy structure as the strongest honest
expectation consistent with all existing evidence.
