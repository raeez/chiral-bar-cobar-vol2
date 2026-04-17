# Wave-4 attack-and-heal: SC^{ch,top} heptagon (Vol II sc_chtop_heptagon.tex)

Target: CLAUDE.md row "SC^{ch,top} heptagon PROVED (Vol II chapters/theory/sc_chtop_heptagon.tex, 2026-04-16)".
File: /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/sc_chtop_heptagon.tex (1325 lines, read linearly in 250-line chunks).
Voice: Beilinson/Etingof/Kapranov adversarial audit; CG rectification prose.

## Attack ledger (file:line, severity, category)

### Tier 1 — CONSTITUTIONAL (must be fixed before status can stand)

A1. **Phantom label `prop:bd-cg-equivalence`** — Severity: HIGH. Category: AP264 / AP255.
File: sc_chtop_heptagon.tex:183 (Face (3) asserts "the equivalence is Proposition~\ref{prop:bd-cg-equivalence} of Chapter~\ref{ch:factorization-swiss-cheese}"). Cross-volume grep across Vol II returns ZERO `\label{prop:bd-cg-equivalence}`. The BD-CG equivalence (Beilinson–Drinfeld algebraic factorization ≃ Costello–Gwilliam differential-geometric factorization) is load-bearing for Face (3)'s claim that the factorization face is well-defined at all. Already flagged in Vol II `compute/audit/linear_read_notes.md` as a known phantom. CG-prose footing for Face (3) is therefore a folklore citation (AP272).

A2. **Phantom label `def:factorization-swiss-cheese-operad`** — Severity: HIGH. Category: AP264 / AP255.
File: sc_chtop_heptagon.tex:132. Face (1) is DEFINED as "the homotopy colored operad of Definition~\ref{def:factorization-swiss-cheese-operad} of Chapter~\ref{ch:factorization-swiss-cheese}". Zero hits in Vol II. Face (1) therefore has no inscribed definition in the volume; the heptagon's starting vertex is an `\ref{}` into the void.

A3. **Phantom label `conj:topologization-general`** — Severity: MEDIUM. Category: AP264.
File: sc_chtop_heptagon.tex:1216 (inside `conj:heptagon-collapse-general`). Already catalogued in linear_read_notes.md:14541 and swarm_vol2_dependency_dag_2026_04_17.md:64 as phantom. Scope caveat is therefore suspended in air.

A4. **Face (6) AP274 rhetorical-functor risk — "categorified bar-cobar via half-braiding"** — Severity: HIGH. Category: AP274 / AP287.
Files: sc_chtop_heptagon.tex:383–468 (`thm:drinfeld-centre-sc-face`, Step 1–4). Step 1 exhibits `A` itself as "NOT an object of Z(Rep_fact(A))" then promotes "every element of the bar complex B^ch(A), twisted by the R-matrix to compensate ordering ambiguity" to a central object. This is AP274: the bar coalgebra B(A) (E_1 coalgebra over ChirAss^!) and the Drinfeld centre Z(Rep_fact(A)) (E_2-monoidal ∞-category one level up) are disjoint objects; "the lift of the vacuum gives the identity central object" is described, not constructed at chain level. Step 3 cites "Beilinson–Drinfeld–Zhu–Francis–Gaitsgory–Rozenblyum factorization module theory (Lurie HA~5.3.1.30; BZFN10)" as a single-line folklore pillar (AP272) and concludes `Z(Rep_fact(A)) ≃ Rep_fact(Z^der_ch(A))`. The claimed AP-CY25 half-braiding construction is INSCRIBED at `def:chiral-half-braiding` (:287–309), but the construction's correctness at (iv) "extends to all of Rep_fact(A), not only to evaluation modules" rests on "OPE pole bounds on Δ_z" — stated, not derived. HZ-IV decorator with three disjoint paths absent.

A5. **Face (7) source (2,1)-dimension vs target 2-shifted-symplectic claim inconsistency** — Severity: HIGH. Category: AP237 / AP258.
File: sc_chtop_heptagon.tex:560–606. `thm:moduli-sc-shifted-symplectic` proof (:580–597) states "the source `X × R_{≥0}` is a smooth ∞-pair (2,1)-dimensional" and "the target carries a 2-shifted symplectic structure". The integration-over-source drops degree by "2-1=1", producing a 1-shifted form. Two frictions: (a) `Remark rem:why-pair-21` (:599–606) says integration "pairs a 1-form on the source with a 2-form on the target, yielding a 1-shifted output" — "1-form on source" conflicts with the "source smooth (2,1)-dimensional" language in the proof (net source dimension = 2+1 = 3 if taken real, = 2·1+1 = 3 similarly; source integration of a 2-form against a 3-dim source does not give 1, it gives −1; AP237 degree-accounting). (b) PTVV Theorem 2.5 classically runs mapping stack source = compact oriented; `R_{≥0}` has boundary and is non-compact; the boundary condition (Dirichlet at 0, control at ∞) is nowhere stated. The anti-symmetry/closedness claim is therefore PTVV-in-spirit, not PTVV-literal. AP272 folklore-pillar risk on PTVV.

A6. **Face (7) non-degeneracy argument unscoped** — Severity: MEDIUM. Category: AP287 (scope-inheritance).
File: sc_chtop_heptagon.tex:591–596. "non-degeneracy follows from the non-degeneracy of κ_{SC^{ch,top}}: the Lie-sector Killing form is non-degenerate on SEMISIMPLE Lie-sectors; the Ass-trace is non-degenerate on FINITE-DIMENSIONAL Ass-sectors; the mixed-sector shuffle form inherits non-degeneracy…". Two scope restrictions (semisimple Lie; finite-dim Ass) are inserted silently; Face (7) is then announced without scope qualifier. For non-semisimple Lie sectors (e.g. Heisenberg = abelian KM), `κ_{SC^{ch,top}}|_{closed}` is DEGENERATE, breaking the 1-shifted symplectic claim. `cor:face-7-presents-sc` inherits without caveat.

### Tier 2 — SERIOUS (rescope, not retract)

A7. **Heptagon closure identity not traversed on any concrete witness** — Severity: MEDIUM. Category: AP254.
File: sc_chtop_heptagon.tex:1040–1052 (`thm:heptagon-closed` proof). "Compose the seven edges around the heptagon in either direction … the composed self-equivalence of Face (1) is homotopic to the identity because each edge is canonical modulo associator choice." No concrete witness (`A = V_k(sl_2)` at non-critical `k`) is run through the loop. The Beilinson falsification ledger therefore has no numerical/structural entry; AP254 (closure-date commit-floor) and AP245 (three-level numerical agreement) are missing.

A8. **Edge (6)–(7) loop-space claim uses a coloured-dioperad-specific Deligne** — Severity: MEDIUM. Category: AP258 / AP272.
File: sc_chtop_heptagon.tex:961–985. `thm:edge-67` proof:  "applied to the pair (Z^der_ch(A), A), the E_2-chiral algebra whose factorization module category is Z(Rep_fact(A)). The coloured-dioperad input is the specific case handled by `thm:chiral-higher-deligne`". This is honest (no general coloured Deligne is assumed), but `thm:chiral-higher-deligne` (Vol II `chiral_higher_deligne.tex:439`) is itself a CONSEQUENCE-style theorem whose applicability to the coloured dioperad SC^{ch,top} (as opposed to a single E_n chiral algebra) is not separately inscribed. Edge (6)–(7) therefore routes through a theorem that was proved for an uncoloured case but is being applied to the coloured case; the specialisation step is cited, not proved.

A9. **Edge (3)–(4) boundary-condition `A` not verified to satisfy Costello–Gwilliam axioms for a general E_1-chiral A** — Severity: MEDIUM. Category: AP287.
File: sc_chtop_heptagon.tex:768–791. "Costello–Gwilliam \textit{FA in QFT} Vol.~II Theorem 11.3.3 (closed sector); the bulk–boundary extension is Butson–Yoo 2018". CG Thm 11.3.3 requires (i) a free BV theory with quadratic action, (ii) elliptic propagator, (iii) boundary condition satisfying Dirichlet-like compatibility. For Kac–Moody `V_k(g)` at non-critical level these hold; for general `E_1-chiral A` (e.g. Yangian, EK quantum VA, class-M logarithmic) they are NOT verified. Edge (3)–(4) should carry a scope qualifier (at minimum: "class G + class L + class C at non-critical level").

A10. **Fourteen diagonals asserted as automatic compositions** — Severity: LOW-MEDIUM. Category: AP273.
File: sc_chtop_heptagon.tex:1122–1137 (`rem:heptagon-diagonals`). "Each diagonal has an independent direct construction in the literature; the heptagon gathers them under one roof." `binom{7}{2}-7 = 14` advertised; no diagonal is inscribed. The "each diagonal has an independent direct construction" is AP273 (admitted-redundant-item counted in independent-equivalence tally)—diagonals are compositions of edges by definition and should not be counted as independent pieces of content.

A11. **`thm:heptagon-collapse` cites `CFG2602` bibkey without Vol II `.bib`** — Severity: LOW. Category: AP281.
File: sc_chtop_heptagon.tex:1193 (`CFG~\cite{CFG2602}`). Vol II has no `references.bib` under the standard location; the CFG bibkey is programme-interior (Costello–Francis–Gwilliam 2021 arXiv:2110.XXXXX series). If unresolved at build time the citation renders `[?]`; if aliased elsewhere, AP281 alias-drift applies.

A12. **CLAUDE.md row overclaims Face (6) is "via categorified bar-cobar with half-braiding (AP-CY25)"** — Severity: MEDIUM. Category: AP256 / AP271.
The inscribed Step 2 of `thm:drinfeld-centre-sc-face` explicitly says "the centre is the categorified \emph{commutant}, not an averaging. Its right adjoint produces …" — this is the categorified COMMUTANT (right adjoint to forget), not "categorified bar-cobar". CLAUDE.md language is a rhetorical upgrade. Healing direction: CLAUDE.md row rewrites as "via Majid/Lurie right-adjoint-to-forgetful centre construction with half-braiding".

### Tier 3 — PROSE / LESSER

A13. "Koszul locus" used but never defined in this chapter (:1068, :1097, :1098). AP28 (undefined terminological qualifier across 3+ locations).
A14. `\mathrm{Sp}^1` (shifted-symplectic functor, :558) undefined-in-preamble; treated as PTVV standard. Acceptable if bibliography resolves PTVV.
A15. The prologue asserts "the $\infty$-operadic structure is determined by any one face" (:64) — this is the CONVERSE of the seven-way equivalence and is not proved separately in this chapter.

## Surviving core (3-sentence Drinfeld summary)

The heptagon is seven presentations of the coloured two-colour dioperad SC^{ch,top} — operadic `C_•(FM_k(C)) ⊗ C_•(Conf_m(R))`, Koszul dual `(Lie, Ass, shuffle-mixed)`, factorization observables on Ran(X), bulk–boundary BV, coloured convolution `L_∞`, Drinfeld centre of `Rep_fact(A)` at the categorical level one up, and a 1-shifted symplectic mapping stack — joined by seven named `∞`-quasi-isomorphisms after fixing a Drinfeld associator. The inscription PROVES: edges (1)–(2), (2)–(3), (4)–(5), (5)–(6), (7)–(1) to publication standard on the Koszul locus; edges (3)–(4) and (6)–(7) CONDITIONAL on scope-restricted boundary-condition hypotheses and the coloured-dioperad case of `thm:chiral-higher-deligne`; Face (6) at `∞`-qi chain level and Face (7) at 1-shifted symplectic level pending three phantom-label heals (A1–A3) and Killing/trace non-degeneracy scope (A6). In the generic (no conformal vector) case the heptagon is the final structure; adding a conformal vector at non-critical Kac–Moody level triggers topologisation to E_3-top (`thm:heptagon-collapse`, PROVED for `V_k(g)`, `k ≠ −h^∨`; conjectural for general, per `conj:heptagon-collapse-general` and its phantom-label caveat).

## Per-face status table (adversarial verdict)

| Face | Inscription route | Status (adversarial) | Load-bearing issue |
|------|-------------------|----------------------|--------------------|
| (1) Operadic | `def:factorization-swiss-cheese-operad` | **Phantom label (A2)**; inscribe locally or retarget | Must be healed first: entire heptagon starts here |
| (2) Koszul dual | `prop:sc-koszul-dual-three-sectors` (`spectral-braiding-core.tex:3751`) | ProvedElsewhere (resolves) | Acceptable |
| (3) Factorization | `prop:bd-cg-equivalence` | **Phantom label (A1)**; retarget to Francis–Gaitsgory 2012 Def 2.7.6 + GR17 IV.5 inscription | Must either inscribe BD ≃ CG comparison locally or downgrade to `\ClaimStatusProvedElsewhere` |
| (4) BV/BRST | `thm:edge-34` + Costello–Gwilliam Thm 11.3.3 + Butson–Yoo 2018 | ConditionalScope (A9): CG axioms verified for class G+L at non-critical level; class C/M/critical open | Add scope qualifier to `thm:edge-34` |
| (5) Convolution | Vallette/Loday–Vallette coloured convolution | ProvedElsewhere (resolves) | Acceptable |
| (6) Drinfeld centre | `thm:drinfeld-centre-sc-face` (:383) | ProvedHere at ∞-qi level; Step 3 BZFN pillar (A4, AP272); add HZ-IV decorator | Rewrite Step 1 to remove "bar complex lifts to central object" AP274 language; add `\ClaimStatusProvedHere` caveat that the construction is the Majid/Lurie right-adjoint-to-forgetful centre, NOT a categorified bar-cobar |
| (7) Derived AG | `thm:moduli-sc-shifted-symplectic` (:553) + `thm:convolution-lagrangian` (:611) | ConditionalScope (A5, A6): semisimple Lie + finite-dim Ass required for non-degeneracy; (2,1)-pair dimension-accounting needs explicit boundary condition at R_{≥0} boundary | Inscribe `rem:face-7-scope`: semisimple-or-reductive-Lie closed sector, finite-dim open sector, Dirichlet at ∂R_{≥0}; downgrade `thm:moduli-sc-shifted-symplectic` to `\ClaimStatusConditional` on boundary-condition-inscription |
| Closure | `thm:heptagon-closed` (:1028) | ProvedHere at cohomology; chain-level strict on Koszul locus only | Add `rem:heptagon-concrete-witness`: traverse loop at `A = V_k(sl_2)` at generic `k ≠ −h^∨`, check composite is identity on `Z^der_ch` dim 5 |

## Healing commit plan (no commits executed; draft for the user)

1. **Inscribe three phantom labels (A1, A2, A3)**. Options:
   (a) `def:factorization-swiss-cheese-operad` — inscribe locally in `sc_chtop_heptagon.tex` as `\begin{definition}[Coloured Swiss-cheese factorization operad]` at the start of §Face (1), with `\ClaimStatusProvedElsewhere` attribution to Voronov 1998 + BD Chiral Algebras §3.
   (b) `prop:bd-cg-equivalence` — retarget to Francis–Gaitsgory 2012 Def 2.7.6 via inline `\cite{FG12}` and delete the `\ref{prop:bd-cg-equivalence}`.
   (c) `conj:topologization-general` — either inscribe a genuine `\begin{conjecture}` body in `e_infinity_topologization.tex` (the natural home) and reference it from here, or rewrite the caveat in `conj:heptagon-collapse-general` to cite Conjecture~\ref{conj:e-infinity-specialisation-Winfty} (already inscribed per CLAUDE.md Topologization row).

2. **Rewrite Face (6) Step 1 (A4)**. Remove the "every element of the bar complex B^ch(A), twisted by the R-matrix to compensate ordering ambiguity, lifts to a central object" sentence (AP274: bar coalgebra ≠ central objects of Drinfeld centre). Replace with the Majid/Lurie right-adjoint-to-forgetful construction as the whole story, citing `def:chiral-half-braiding` as the explicit formula. Keep Step 2's honest language "the centre is the categorified commutant, not an averaging" as load-bearing.

3. **Scope-qualify Face (7) (A5, A6)**. Insert `rem:face-7-scope` right after `thm:moduli-sc-shifted-symplectic`:
   - Closed sector requires semisimple or reductive Lie; for non-semisimple (Heisenberg), the Killing form is degenerate and `ω_{SC^{ch,top}}` is only pre-symplectic.
   - Open sector requires finite-dim Ass.
   - Source `X × R_{≥0}` requires explicit boundary condition at `∂R_{≥0} = X × {0}`: the boundary-operator insertion is the `A`-module fibre over the curve, Dirichlet at infinity.
   - Downgrade `thm:moduli-sc-shifted-symplectic` to `\ClaimStatusConditional` on these scope hypotheses OR retitle as "1-shifted pre-symplectic with non-degeneracy on the semisimple/finite-dim locus".

4. **Traverse the heptagon on `V_k(sl_2)` as concrete witness (A7)**. Inscribe `rem:heptagon-witness-sl2` at the end of §"Closing the heptagon":
   ```
   Concrete witness. Let A = V_k(sl_2), k ≠ −2. The derived chiral centre
   Z^der_ch(V_k(sl_2)) has total dimension 5 (Vol I chiral_center_theorem.tex
   prop:derived-center-explicit). Traversing the seven edges once: (1) FM_k(C)
   strata; (2) (Lie_sl_2, Ass, mixed); (3) Obs^ch_A(U) as factorization algebra;
   (4) Chern–Simons BV at level k + boundary sl_2 WZW; (5) Hom^col(B(SC^{ch,top}),
   End^ch_{(A,Z)}) with MC in weight ≤ 2; (6) Rep_fact(V_k(sl_2)) affine Kazhdan–
   Lusztig category at level k, Drinfeld centre = Rep_fact(Z^der_ch) which on the
   generators lifts to the half-braiding from Δ_z^{V_k(sl_2)}; (7) M_{SC^{ch,top},X}
   at (V_k(sl_2), Z^der_ch) is locally 5-dimensional over T_{(A,Z)}. Composite
   (1)→(2)→...→(7)→(1) is the identity on FM_k(C) strata up to Φ-twist.
   ```
   This is a concrete AP245 triple-check candidate (operadic dim = centre dim = tangent dim at the witness).

5. **Scope-qualify Edge (3)–(4) (A9)**. Insert scope qualifier in `thm:edge-34`: "for boundary condition A satisfying the Costello–Gwilliam Dirichlet-compatibility axiom (verified on class G and class L at non-critical level; open for class C/M)".

6. **Demote `rem:heptagon-diagonals` (A10)**. Rewrite: "The fourteen diagonals are compositions of the seven edges around the heptagon. They are not counted as independent content; each has an independent literature construction that the heptagon organises, but the heptagon itself contains seven theorems, not twenty-one." (AP273 discipline.)

7. **Update CLAUDE.md row (A12)**.
   Before: "face (6) Drinfeld-centre via categorified bar-cobar with half-braiding (AP-CY25)"
   After: "face (6) Drinfeld-centre via Majid/Lurie right-adjoint-to-forgetful centre construction with explicit half-braiding (`def:chiral-half-braiding`); AP-CY25 half-braiding inscribed. Face (7) CONDITIONAL on semisimple-or-reductive Lie closed sector + finite-dim Ass open sector + Dirichlet boundary at `∂R_{≥0}`."

8. **HZ-IV decorators**. At minimum two faces (6 and 7) warrant HZ-IV decorators:
   - Face (6): `derived_from = Majid 1998 centre-to-forgetful adjoint`, `verified_against = Lurie HA 5.3 centre construction`, `disjoint_rationale = categorical construction independent of chiral-specific Δ_z OPE-pole bounds`.
   - Face (7): `derived_from = PTVV 2013 mapping-stack Thm 2.5`, `verified_against = Toën–Vaquié 2007 operadic moduli`, `disjoint_rationale = symplectic construction is geometric; representability is operadic`.

## Summary

The SC^{ch,top} heptagon chapter IS a substantial inscription: seven named edges, five classical + two new faces, a closure theorem, a collapse theorem, and honest scope remarks (`rem:heptagon-chain-vs-cohom`, `rem:heptagon-survives-generic`, `rem:heptagon-critical`). The chapter's working core — edges (1)–(2), (2)–(3), (4)–(5), (5)–(6), (7)–(1) — is sound on the Koszul locus. The audit finds three phantom labels (A1, A2, A3) that must be healed before the CLAUDE.md "PROVED" stands, one AP274 rhetorical-functor risk in Face (6) Step 1 (A4) that requires rewording, two unscoped non-degeneracy claims in Face (7) (A5, A6), two boundary-condition scope gaps (A9), and CLAUDE.md row language that over-advertises Face (6) as "categorified bar-cobar" when the inscribed proof is a right-adjoint-to-forgetful centre (A12). After the 8-item heal plan the heptagon row becomes: "PROVED at ∞-qi on the Koszul locus, CONDITIONAL on boundary-condition scope at Face (7); generic heptagon intact; topologisation collapse PROVED for V_k(g) at k ≠ −h^∨, CONJECTURAL for general conformal chiral."

No commits executed. Heal plan drafted for the user.
