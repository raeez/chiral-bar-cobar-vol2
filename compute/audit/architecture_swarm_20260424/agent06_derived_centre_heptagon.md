# Agent 06 - Derived Centre / SC Heptagon Audit

Date: 2026-04-24

Owned surface: `compute/audit/architecture_swarm_20260424/agent06_derived_centre_heptagon.md`.
No shared TeX was edited.

## Executive Verdict

The derived-centre dictionary is mostly present in the Vol II chapters, but one central type error remains: `chapters/theory/sc_chtop_heptagon.tex` promotes the bar coalgebra `B^{ch}(A)` itself to a coloured `\SCchtop`-coalgebra. That conflicts with the local-shadow architecture in `factorization_swiss_cheese.tex`, where `\barB(F)` is only an `E_1` dg coassociative factorization coalgebra over `(ChirAss)^!`; the `\SCchtop` structure emerges on the two-coloured derived-centre pair `(Z^{der}_{ch}(A), A)`, computed by using the bar complex as a resolution.

The remaining defects are status and scope drifts around this same boundary: chain-level `E_3` is over-stated in `chiral_higher_deligne.tex` and echoed in `hochschild.tex`; a stale duplicate in `brace.tex` still claims an arbitrary logarithmic SC bulk-cochains comparison after `hochschild.tex` has narrowed it; and the heptagon's Drinfeld-centre face must not be allowed to imply the conjectural equality between the Drinfeld centre of the double and the Hochschild derived centre.

## Five-Object Invariant

Use this as the local correction key.

| Object | Correct role | Do not conflate with |
|---|---|---|
| `A` | boundary/chiral algebra | its bar coalgebra or bulk |
| `B(A)` / `\barB^{ch}(A)` | bar coalgebra / resolution with bar differential and deconcatenation coproduct | `A^!` or `Z^{der}_{ch}(A)` |
| `A^i = H^*B(A)` | Koszul dual coalgebra | Verdier-dual algebra |
| `A^! = ((A^i)^\vee)` | Koszul/Verdier dual algebra | bar-cobar inversion `\Omega B(A)=A` |
| `Z^{der}_{ch}(A)=C^\bullet_{ch}(A,A)` | Hochschild derived centre / bulk | `B(A)` or `A^!` |

Anchors:
- Vol I `CLAUDE.md:293-300`: the five objects are explicitly separated; `\Omega(B(A))=A` is inversion, `A^!` comes by Verdier duality, and the bulk comes by Hochschild cochains.
- `chapters/theory/sc_chtop_heptagon.tex:86-96`: the heptagon introduction correctly places `\SCchtop` on `(Z^{der}_{ch}(A),A)`.
- `chapters/theory/factorization_swiss_cheese.tex:1033-1043`: the bar object is an `E_1` dg coassociative factorization coalgebra and does not itself carry the `\SCchtop` structure.
- Vol I `chapters/theory/theorem_C_refinements_platonic.tex:52-77` and `120-133`: full brace dg equivalence of derived centres under Koszul duality is conjectural, not Theorem C.

## ATTACK -> HEAL Cycles

### Cycle 1 - Bar Complex Promoted To `\SCchtop`

ATTACK.

`chapters/theory/sc_chtop_heptagon.tex:333-336` identifies the two operations of the bar coalgebra `B^{ch}(A)` with the two coloured factorisation maps of `\SCchtop`. The theorem proof at `sc_chtop_heptagon.tex:388-390` then says `d_B` and `\Delta_B` assemble into a coloured dg `\SCchtop`-coalgebra structure on `B^{ch}(A)`.

This is the main conflation. `B(A)` is not the two-coloured bulk-boundary datum. The source that states the correct architecture is `chapters/theory/factorization_swiss_cheese.tex:1037-1043`: the bar differential comes from holomorphic collision residues, the coproduct is deconcatenation, and the result is an `E_1` dg coassociative factorization coalgebra over `(ChirAss)^!`; the `\SCchtop` structure appears on `(C^\bullet_{ch}(A,A),A)` after using the bar complex as a resolution.

HEAL.

In `thm:bar-diff-eq-holfact`, replace the object-level conclusion by:

```tex
The operations \(d_B\) and \(\Delta_B\) make \(B^{ch}(A)\) an
\(E_1\) dg coassociative factorization coalgebra over
\((\mathrm{ChirAss})^!\).  They are the resolution-level
holomorphic and topological shadows from which the two-coloured
\(\SCchtop\)-structure on
\((Z^{der}_{ch}(A),A)=(C^\bullet_{ch}(A,A),A)\) is computed.
```

Also replace the surrounding phrase "two coloured factorisation maps of `\SCchtop`" by "the holomorphic bar differential and topological deconcatenation shadow feeding the derived-centre pair." This preserves the useful calculation while removing the category error.

### Cycle 2 - Generic `E_3` Lift Without Topologisation Hypothesis

ATTACK.

`chapters/theory/chiral_higher_deligne.tex:442-462` defines the strict `E_3` lane as requiring a topological direction, for example a conformal-vector/topologisation mechanism. But `chiral_higher_deligne.tex:464-492` states a canonical `E_3`-chiral action on `Z^{der}_{ch}(A)` for the Koszul locus, and the proof at `528-545` uses conformal grading and `L_0` as if every Koszul-locus object has the required strict topological direction.

This overstates the result and conflicts with `chapters/connections/brace.tex:54-123`, where the chain-level genuinely `E_1` chiral Deligne-Tamarkin case remains conjectural, while the `E_\infty`-chiral locus is proved.

HEAL.

Split the theorem into the actual lanes:

1. General Koszul/chiral Hochschild lane: `Z^{der}_{ch}(A)` has the cohomological `E_2`/brace structure, with chain-level status following `brace.tex:54-123`.
2. Two-coloured lane: `(Z^{der}_{ch}(A),A)` carries the `\SCchtop` bulk-boundary structure when the heptagon hypotheses are met.
3. Strict `E_3` lane: available only with explicit topologisation data, such as an inner conformal vector at non-critical level or the weight-completed class-M hypotheses already separated later in the chapter.

The proof must not infer a topological `E_1` direction from `L_0` alone.

### Cycle 3 - Conditional Universality Proved In The Proof

ATTACK.

`chapters/theory/chiral_higher_deligne.tex:494-518` correctly says that the universal two-coloured statement needs a contracting homotopy for the full two-coloured cobar construction on `(SC)^!`, and that Vol I supplies only the single-colour Positselski shadow. But the proof at `554-572` asserts the needed chain-level lift by applying the Vol I theorem to `(SC)^!`.

That is an internal contradiction. The remark says the two-coloured lift is open; the proof treats it as established.

HEAL.

Keep clause (2) conditional and rewrite the proof step as an assumption-dependent construction:

```tex
Assuming a filtered contracting homotopy for the two-coloured cobar
construction on \((\SCchtop)^!\), the single-colour Positselski
comparison upgrades to the mixed-sector universal property.
Without that additional datum this paragraph proves only the
single-colour shadow and the cohomological compatibility already
recorded above.
```

Do not cite Vol I Theorem B/C as proving the two-coloured `\SCchtop` cobar homotopy. Vol I is a shadow here, not the missing mixed-sector construction.

### Cycle 4 - Hochschild Echo Overstates The `E_3` Result

ATTACK.

`chapters/connections/hochschild.tex:2789-2805` states, with `\ClaimStatusProvedElsewhere`, that for any logarithmic SC algebra `Z^{der}_{ch}(A)` carries a canonical `E_3`-algebra structure refining `E_2`. This imports the over-scoped statement from `chiral_higher_deligne.tex` without its later caveats.

The same status drift appears in the class-M discussion: `hochschild.tex:2531-2586` first presents the global triangle gap, then says the full DS-boundary extension is closed with chain-level identifications, while `chiral_higher_deligne.tex:494-518`, `828-905`, and `933-985` still mark chain-level `E_3` and universal SC lifting as conditional.

HEAL.

Change the Hochschild echo to:

```tex
The derived centre \(Z^{der}_{ch}(A)\) carries the canonical
chiral brace/\(E_2\) structure.  A strict \(E_3\)-chiral refinement
is available under the topologisation hypotheses of
Chapter~\ref{...}; in the genuinely two-coloured universal case it
remains conditional on the \((\SCchtop)^!\)-cobar contracting
homotopy.
```

For class M, split the closed part from the open part: cohomological and weight-completed boundary-linear comparisons may be closed; the raw direct-sum and chain-level strict `E_3` comparison remain conditional unless the relevant homotopy has been constructed.

### Cycle 5 - Stale Brace Bulk-Cochains Statement

ATTACK.

`chapters/connections/brace.tex:704-715` still states a canonical filtered quasi-isomorphism from the chiral-topological Hochschild object to bulk observables for an arbitrary logarithmic SC algebra. This is broader than the narrowed theorem in `chapters/connections/hochschild.tex:392-409`, `423-425`, and `887-948`, which restricts the comparison to HT prefactorization realizations in the scope of the physics bridge and to product-formal local shadows.

The stale brace statement reintroduces the global-SC inference that `hochschild.tex` has already removed.

HEAL.

Mirror the Hochschild scope in `brace.tex`:

```tex
Let \(A\) be an HT prefactorization boundary algebra in the scope of
the physics bridge, with product-formal local \(\SCchtop\)-shadow.
Then the chiral-topological Hochschild object computes the local
bulk cochains in that shadow.
```

Avoid "arbitrary logarithmic SC algebra" unless a global factorization-algebra comparison and the required compact-generation/derived-centre hypotheses are explicitly present.

### Cycle 6 - Drinfeld-Centre Face Can Collapse Into A Conjecture

ATTACK.

`chapters/theory/sc_chtop_heptagon.tex:1133-1172` states a Drinfeld-centre face as a proved equivalence between the factorization Drinfeld centre of boundary modules and `Rep_fact(Z^{der}_{ch}(A))^{E_2}`. On its own this is not necessarily wrong, but it sits dangerously close to the explicitly conjectural double/bulk equality in `chapters/connections/hochschild.tex:5039-5059`.

`hochschild.tex:5061-5075` separates the Drinfeld centre of the double from the Hochschild derived centre, and `5114-5156` says the compatibility is not yet proved. The heptagon face must therefore not be read as proving `Z(U_A) \simeq Z^{der}_{ch}(A)`.

HEAL.

Add scope to the heptagon theorem:

```tex
This is the module-category/half-braiding face of the local
\(\SCchtop\) shadow.  It does not identify the Drinfeld centre of
the ordered double \(U_A\) with the Hochschild derived centre; that
stronger comparison is Conjecture~\ref{conj:drinfeld-center-equals-bulk}.
```

Use "compatible with the conjectural double/bulk comparison" rather than "identifies the centres" when moving between these two objects.

### Cycle 7 - Theorem C Is Not Full Derived-Centre Equivalence

ATTACK.

Vol I Theorem C gives complementarity data, not a proved brace dg equivalence of derived centres. The precise Vol I refinement says:

- `chapters/theory/higher_genus_complementarity.tex:540-610`: Theorem C is the homotopy eigenspace decomposition and Verdier perfect-duality pairing.
- `chapters/theory/theorem_C_refinements_platonic.tex:52-77` and `120-133`: the full brace dg equivalence
  `Z^{der}_{ch}(A) \simeq Z^{der}_{ch}(A^!)` is conjectural.
- `chapters/examples/landscape_census.tex:1580-1624`: scalar witnesses give family-dependent complementarity constants.
- `chapters/examples/landscape_census.tex:1911-1948`: the value `8` is a Vol III `\mathsf B`-family enlargement, conditional on the chiral-side construction, while the self-contained classical Vol I ceiling is `{0,13,250/3,98/3}`.

Any Vol II sentence that uses "Theorem C derived-centre complementarity" must not silently upgrade scalar/Verdier complementarity to a chain-level derived-centre equivalence.

HEAL.

Use this wording wherever the derived-centre complementarity is invoked:

```tex
Theorem C supplies Verdier/Koszul complementarity and scalar
\(\kappa+\kappa^!\) constraints.  The brace dg equivalence of
derived centres is the separate conjectural refinement
\(\ref{conj:derived-center-koszul-equivalence}\).
```

For constants, distinguish the self-contained classical Vol I ceiling from the Vol III `\mathsf B`-row enlargement:

```tex
Classical Vol I: \(\{0,13,250/3,98/3\}\).
Cross-volume enlargement with the conditional \(\mathsf B\)-row:
\(\{0,8,13,250/3,98/3\}\).
```

## SC Heptagon Coherence Check

The heptagon is coherent after the following discipline is enforced.

1. The bar face is a resolution face: `d_B` and `\Delta_B` live on `B(A)` as an `E_1` coalgebra, not as the full two-coloured SC datum.
2. The derived-centre face is the bulk face: `Z^{der}_{ch}(A)=C^\bullet_{ch}(A,A)` is where Hochschild/brace operations live.
3. The boundary face remains `A`.
4. The mixed face is the action of the bulk on the boundary, encoded by brace/mixed operations `\mu_{k;m}` as in `chapters/connections/brace.tex:558-575`.
5. The Drinfeld-centre face is categorical and local-shadow scoped; it must not prove the ordered-double conjecture.
6. The `E_3`/topological face is conditional on explicit topologisation data.
7. The global HT bulk-cochains face is restricted to the physics-bridge/product-formal local-shadow hypotheses unless the global factorization comparison is separately proved.

## Concrete Patch Targets For The Integrator

1. `chapters/theory/sc_chtop_heptagon.tex:333-336`, `388-390`: replace the `B^{ch}(A)`-as-`\SCchtop` conclusion by the `E_1` coalgebra/resolution-shadow statement above.
2. `chapters/theory/chiral_higher_deligne.tex:464-492`, `528-545`, `554-572`: split `E_2`, `\SCchtop`, and strict `E_3` lanes; keep universality conditional.
3. `chapters/connections/hochschild.tex:2531-2586`, `2789-2805`: downgrade the universal `E_3` echo and clarify class-M closure.
4. `chapters/connections/brace.tex:704-715`: narrow the bulk-cochains theorem to the same HT prefactorization/product-formal local-shadow scope as `hochschild.tex`.
5. `chapters/theory/sc_chtop_heptagon.tex:1133-1172`: add a non-collapse warning separating the categorical Drinfeld-centre face from `conj:drinfeld-center-equals-bulk`.
6. Any Theorem C cross-reference in this cluster: specify Verdier/scalar complementarity, and cite the derived-centre brace equivalence only as conjectural.

## Final Status

Fatal issue found: yes, the bar complex is incorrectly typed as carrying the full `\SCchtop` coalgebra structure in the heptagon theorem.

Mathematically safe repair: yes, replace the claim by the resolution-level `E_1` coalgebra statement and route the two-coloured structure through `(Z^{der}_{ch}(A),A)`.

Residual open obligations:
- Construct the two-coloured `(SC)^!` cobar contracting homotopy.
- Prove or scope the chain-level strict `E_3` lift outside the topologised/weight-completed loci.
- Prove the ordered-double Drinfeld-centre comparison, or keep it conjectural.
