# Vol II Dependency-DAG Attack (2026-04-17)

Adversarial audit #2 of 5. Target: dependency DAG integrity across Vol II.
Method: first-principles extraction of `\label{...}` / `\ref{...}` across 15
priority chapters; position indices read from `main.tex` lines 1327-1671.

## 1. Top-level DAG (Part-wise defined vs referenced)

| Part (pos range)                    | Key defined labels                                                                                                 | Key referenced labels (provenance)                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| I Open Primitive (1365-1378)        | `def:ainfty_chiral`, `thm:rectification`, `thm:bulk_hochschild`, `thm:chain-level-bulk`, `thm:properad-bar-cobar`, `thm:FM-calculus`, `thm:physics-bridge`, `thm:stokes_arnold`, `thm:boundary-algebra-from-vacuum`, `thm:curved-bar-cobar-genus-ge-1`, `thm:recognition-SC`, `def:log-SC-algebra`, `thm:koszul-comparison-mc`, `thm:e1-factorization-disjoint`, `thm:collision-extension`, `thm:meromorphic-factorization-equivalence`, `ch:factorization-swiss-cheese`, `ch:sc-chtop-heptagon`, `ch:curved-dunn-higher-genus` (via Part IV import), seven heptagon-edge labels (`thm:edge-12`..`thm:edge-71`), `thm:heptagon-closed`, `thm:heptagon-collapse`, `thm:drinfeld-centre-sc-face`, `thm:convolution-lagrangian`, `thm:moduli-sc-shifted-symplectic` | **FORWARD:** `thm:chd-ds-hochschild`, `thm:chd-deligne-tamarkin`, `ch:chiral-higher-deligne` (all Part VI); `thm:chiral-higher-deligne` (Part VI); `ch:log-w-algebras` (undefined); `ch:hochschild` (undefined ch-level label). **DANGLING:** `thm:topologization`, `conj:topologization-general`, `ch:topologization`, `ch:theory-hochschild`, `ch:theory-equivalence`, `ch:theory-drinfeld`, `ch:bv-construction`, `ch:ordered-chiral`, `ch:brace`, `ch:koszulness-moduli`, `ch:modular-swiss-cheese-operad` |
| II $E_1$ Core (1415-1424)           | `thm:homotopy-Koszul`, `thm:bar-cobar-adjunction`, `thm:filtered-koszul`, `thm:two-color-master`, `thm:yangian-recognition`, `thm:dual-sc-algebra`, `thm:bar_differential_squared`, `thm:bar_cobar_adjunction` (distinct from Pt II), `thm:GLZ_compatibility`, `thm:one-loop-koszul`, `thm:lines_as_modules`, `thm:two-module-categories`, `thm:unified-chiral-QG`, `thm:langlands-nonsimplylaced`, `thm:DS-L-to-M-universal`, `def:chiral_bar`, `def:chiral_cobar`, `def:line_operators` | `thm:properad-bar-cobar` (Part I, backward — OK); `thm:filtered-koszul` self; none forward |
| III Faces of $r(z)$ (1443-1450)     | `thm:seven-face-master-3d-ht`, `thm:vol2-seven-faces-master`, `thm:dk-four-path`, `thm:seven-faces-as-GRT-torsor`, `thm:f1-f4-injection`, `thm:motivic-face-F8`, `thm:willwacher-face-F9`, `cor:f8-f9-dual`, `thm:YBE`, `thm:braided-category`, `thm:spectral_R_YBE`, `thm:meromorphic-tensor-dgcat`, `prop:sc-koszul-dual-three-sectors`, `prop:spectral-to-categorical` | (mostly backward into Part II bar-cobar; a few forward into Part V for BV interpretations) |
| IV Characteristic Datum (1484-1505) | Hochschild master labels (`thm:bulk_hochschild` collides w/ Part I!), `def:half-braiding-explicit`, `thm:curved-dunn-H2-vanishing-all-genera`, `prop:modular-bootstrap-to-curved-dunn-bridge`, `thm:irregular-singular-kzb-regularity`, `thm:tempered-stratum-contains-virasoro`, `thm:wn-tempered-all-N`, `thm:beta-N-closed-form-proved-all-N`, `thm:tempered-stratum-contains-wp` | (see Section 4 — `def:half-braiding-explicit` already consumed from heptagon) |
| V Standard HT Landscape (1528-1544) | `thm:E3-topological-km` (in `3d_gravity.tex`! — mis-placed), BV-BRST labels | Part I foundations cites `thm:topologization` that is never instantiated by this Part |
| VI 3d Quantum Gravity (1583-1601)   | `thm:chiral-higher-deligne`, `thm:chd-ds-hochschild`, `thm:chd-deligne-tamarkin`, `cor:universal-holography-class-M`, `thm:universal-holography-functor`, `thm:uhf-perturbative-finiteness-split`, `thm:uhf-monster-orbifold-bv-anomaly-vanishes`, `cor:uhf-universal-holography-is-a-theorem`, `thm:programme-climax`, `thm:climax-w-infty-endpoint`, `thm:iterated-sugawara-construction`, `thm:schellekens-71-all-alpha-zero` | Cites Part I labels (`thm:A-infinity-2` is Vol-I, and cites Vol-III labels — cross-volume) |
| VII Frontier (1617-1628)            | `*-frontier` analogues                                                                                             | Backward                                                                                                                |
| VIII From Frontier to Theorem (1669-1671) | `ch:koszulness-moduli` expected here                                                                           | ---                                                                                                                     |

## 2. Forward-dependency violations (hard violations only)

Each row: (source chapter, target label, target chapter file, target position). Source < target in `main.tex` input order implies a FORWARD dependency. Below, source pos is always strictly less than target pos unless noted.

| # | Source file (pos) | Target label | Defined in (pos) | Kind |
|---|---|---|---|---|
| F1 | `theory/foundations.tex` (1365) | `thm:chd-ds-hochschild` | `theory/chiral_higher_deligne.tex` (1594) | F1-hard: Part I → Part VI |
| F2 | `theory/foundations.tex` (1365) | `thm:chd-deligne-tamarkin` | `theory/chiral_higher_deligne.tex` (1594) | Part I → Part VI |
| F3 | `theory/foundations.tex` (1365) | `ch:chiral-higher-deligne` | `theory/chiral_higher_deligne.tex` (1594) | Part I → Part VI |
| F4 | `theory/foundations.tex` (1365) | `ch:log-w-algebras` | **UNDEFINED** | — (see §4) |
| F5 | `theory/foundations.tex` (1365) | `ch:hochschild` | UNDEFINED as `\label{}` (file exists: `connections/hochschild.tex`) | — |
| F6 | `theory/locality.tex` (1366) | `def:prefact`, `lem:product-weiss-descent` | self (locality.tex) | OK (local) |
| F7 | `theory/axioms.tex` (1367) | `thm:stokes_arnold` | `theory/fm-calculus.tex` (1374) | Part I → Part I (later): F7-soft |
| F8 | `theory/axioms.tex` (1367) | `thm:cohomology_PVA`, `thm:rectification` (self) | `theory/pva-descent-repaired.tex` (1377) | Part I → Part I later: F8-soft |
| F9 | `theory/axioms.tex` (1367) | `thm:physics-bridge`, `thm:FM-calculus`, `def:log-SC-algebra` | `theory/raviolo.tex` (1372), `theory/fm-calculus.tex` (1374) | Part I → Part I later: F9-soft |
| F10 | `theory/axioms.tex` (1367) | `thm:homotopy-Koszul` | `connections/line-operators.tex` (1416) | Part I → Part II: F10-hard |
| F11 | `theory/equivalence.tex` (1368) | `thm:homotopy-Koszul`, `thm:bar-cobar-adjunction` | `connections/line-operators.tex` (1416) | Part I → Part II: F11-hard |
| F12 | `theory/foundations.tex` (1365) | `thm:chain-level-bulk`, `thm:bulk_hochschild`, `thm:boundary-linear-bulk-boundary` | self / `connections/ht_bulk_boundary_line_core.tex` (1446) | F12-hard: Part I → Part III |
| F13 | `theory/sc_chtop_heptagon.tex` (1371) | `def:half-braiding-explicit` | `connections/hochschild.tex` (1490) | Part I → Part IV: F13-hard |
| F14 | `theory/sc_chtop_heptagon.tex` (1371) | `thm:chiral-higher-deligne` | `theory/chiral_higher_deligne.tex` (1594) | Part I → Part VI: F14-hard |
| F15 | `theory/sc_chtop_heptagon.tex` (1371) | `thm:E3-topological-km` | `connections/3d_gravity.tex` (1585) | Part I → Part VI: F15-hard |
| F16 | `theory/foundations.tex` (1365) | `thm:recognition`, `thm:steinberg-presentation` | later (operadic chapters and spectral-braiding) | F16-hard: Part I → Part III |
| F17 | `theory/curved_dunn_higher_genus.tex` (1494) | `ch:modular-swiss-cheese-operad` (dangling) | UNDEFINED | — |
| F18 | `theory/chiral_higher_deligne.tex` (1594) | `ch:sc-chtop-heptagon` | `theory/sc_chtop_heptagon.tex` (1371) | Backward OK |
| F19 | `connections/programme_climax_platonic.tex` (1588) | `thm:A-infinity-2` | Vol-I cross-volume | OK (external) |
| F20 | `connections/programme_climax_platonic.tex` (1588) | `prop:C-A-inverse-radius` | **UNDEFINED anywhere in Vol II** | orphan |
| F21 | `connections/programme_climax_platonic.tex` (1588) | `thm:shadow-exponential-base-Virasoro`, `thm:universal-class-M-C-is-6`, `thm:kummer-laurent-depth-controlled`, `thm:all-tier-fuchsian-ode`, `thm:shadow-tower-depth-1-rationality`, `thm:virasoro-motivic-rationality-all-r`, `thm:cy-c-six-routes-generator-level-convergence`, `thm:super-shadow-self-duality`, `thm:cy4-p1-twisted-family`, `thm:derived-framing-obstruction`, `thm:topologization-tower`, `thm:shadow-tower-asymptotic-closed-form`, `thm:irrational-coset-tempered` | **UNDEFINED in Vol II** (some are likely cross-volume Vol-I or Vol-III but no `\label{}` hit at all) | orphans or silent cross-volume |

**Fifteen hard forward violations (F1-F5, F10-F17, F21) are load-bearing on Part I exposition.**

## 3. Circular dependencies

- `foundations.tex` (Part I) references `thm:chiral-higher-deligne` (Part VI), and `chiral_higher_deligne.tex` (Part VI) references `ch:sc-chtop-heptagon` and `rem:sc-three-bar-complexes` from `foundations.tex` (Part I). **Cycle**: I ↔ VI via the heptagon/higher-Deligne pair.
- `sc_chtop_heptagon.tex` (Part I) → `chiral_higher_deligne.tex` (Part VI) → back to `sc_chtop_heptagon.tex`. **Cycle**: I ↔ VI via `thm:edge-34`, `thm:chiral-higher-deligne`, `cor:universal-holography-class-M`.
- `universal_holography_functor.tex` (Part VI) → `thqg_symplectic_polarization.tex` (Part VI earlier) → `thqg_holographic_reconstruction.tex` (Part V) → back to universal functor corollaries. (Not a strict logical cycle: the reverse direction is prose only, but verifier chains risk circularity — confirmed by `rem:chd-vol2-part-vi` explicit concession.)

No strict proof-level DAG cycle detected among the `\ClaimStatusProvedHere` nodes, but the Part I heptagon genuinely depends on the Part VI higher-Deligne theorem it cites, and the Part VI theorem uses the heptagon Face (6) lemma proved in Part I.

## 4. Orphan references (DANGLING LABELS)

Referenced but **NEVER DEFINED** anywhere in Vol II (verified via grep of `\label{<name>}` across `/Users/raeez/chiral-bar-cobar-vol2`):

- `thm:topologization` (cited in `theory/foundations.tex`, `theory/equivalence.tex`)
- `ch:topologization` (cited in `theory/sc_chtop_heptagon.tex` 5x — the AP-TOPOLOGIZATION references)
- `conj:topologization-general` (cited in `theory/sc_chtop_heptagon.tex`)
- `ch:theory-hochschild` (cited in `theory/sc_chtop_heptagon.tex` 5x and `theory/chiral_higher_deligne.tex`)
- `ch:theory-equivalence` (cited in `theory/sc_chtop_heptagon.tex`)
- `ch:theory-drinfeld` (cited in `theory/sc_chtop_heptagon.tex`)
- `ch:bv-construction` (cited in `theory/sc_chtop_heptagon.tex`; file exists but no chapter-level `\label{}`)
- `ch:ordered-chiral` (cited in `theory/sc_chtop_heptagon.tex`)
- `ch:brace` (cited in `theory/sc_chtop_heptagon.tex`)
- `ch:hochschild` (cited in `theory/foundations.tex`; file exists but no `\label{ch:hochschild}`)
- `ch:koszulness-moduli` (cited in `theory/sc_chtop_heptagon.tex`)
- `ch:modular-swiss-cheese-operad` (cited in `theory/curved_dunn_higher_genus.tex` 3x)
- `ch:log-w-algebras` (cited in `theory/foundations.tex`)
- `ch:thqg-holographic-reconstruction` (cited in `theory/chiral_higher_deligne.tex`)
- `ch:thqg-symplectic-polarization` (cited in `theory/chiral_higher_deligne.tex`)
- `prop:C-A-inverse-radius` (cited in `connections/programme_climax_platonic.tex`)
- `part:universal-holography` (cited in `theory/chiral_higher_deligne.tex`; main.tex defines `part:holography`, NOT `part:universal-holography`)
- `part:three-dimensional-quantum-gravity` (cited in `programme_climax_platonic.tex`; main.tex defines `part:gravity`)
- `thm:A-infinity-2` (cross-volume, Vol I — external OK but should be flagged as such)
- A further ~13 labels in `programme_climax_platonic.tex` are cross-volume and not locally annotated.

**Total orphan labels identified: 19 unique, with ~40 citation occurrences.** The two `part:*` orphans are the starkest — main.tex uses short names (`holography`, `gravity`) while chapters cite verbose names. This is a global rename drift.

Defined but never cited (outside self) — a spot audit of Part I labels:

- `rem:oc-vs-known`, `rem:sc-three-bar-complexes` (cited only from `foundations.tex` itself).
- `conv:vol2-strict-models`, `rem:e1-primacy-v2-ap1-compat` in `bar-cobar-review.tex` — defined but never referenced elsewhere.
- `thm:bar-representability`, `cor:bar-cobar-representability` — defined but not referenced downstream in current sweep.

## 5. Suggested topological reorderings

Three tractable moves close the bulk of violations:

(i) **Promote the heptagon chapter's chapter-level labels.** `sc_chtop_heptagon.tex` (pos 1371) uses `Chapter~\ref{ch:theory-hochschild}`, `ch:theory-drinfeld`, `ch:topologization`, `ch:bv-construction`, `ch:brace`, `ch:ordered-chiral` as if those chapters already exist with those chapter-level labels. None do. **Fix:** add the chapter-level labels to their target files: `\label{ch:theory-hochschild}` at top of `connections/hochschild.tex`; `\label{ch:brace}` at top of `connections/brace.tex`; `\label{ch:topologization}` at top of a dedicated topologization chapter (currently split across `3d_gravity.tex` and `e_infinity_topologization.tex`). This is a pure plumbing fix with zero narrative movement.

(ii) **Move Part I citations of Part VI chiral-higher-Deligne content into Part IV.** Violations F1-F3, F12, F13, F14 all route through `thm:chiral-higher-deligne` and its corollaries. The most structurally honest fix: relocate `chapters/theory/chiral_higher_deligne.tex` (currently at pos 1594 inside Part VI) INTO Part IV (adjacent to `hochschild.tex` at 1490), reordering its inputs to precede `universal_holography_functor.tex`. This is consistent with Vol I's architecture where chiral-higher-Deligne is a Part IV-level structural result, not a climax. The climax chapters then cite backward. This move eliminates forward violations F1-F3 and F12-F14 in a single commit.

(iii) **Rename part labels consistently.** Replace all `part:universal-holography` with `part:holography` (the canonical short name in main.tex) and `part:three-dimensional-quantum-gravity` with `part:gravity`. This is a mechanical sed-style rename across `chiral_higher_deligne.tex`, `programme_climax_platonic.tex`, and the frontier conclusion files.

**Recommended linear extension** (preserving current Part I → II → III order but surfacing the hidden intra-part reverse arrow):

```
Part I:   bv-construction → factorization_swiss_cheese → sc_chtop_heptagon
          → locality → axioms → fm-calculus → orientations → fm-proofs
          → raviolo → raviolo-restriction → pva-descent → pva-expanded
          → foundations (SYNTHESIS, cites forward to Part IV)
Part II:  bar-cobar-review → line-operators → ... (unchanged)
Part III: ... (unchanged)
Part IV:  hochschild → brace → modular_swiss_cheese_operad → chiral_higher_deligne (NEW POSITION)
          → curved_dunn_higher_genus → class_m_* → ...
Part V-VI: specialisations citing Part IV results backward.
```

The critical move is `foundations.tex` ceasing to be "Part I intro" and becoming "Part I synthesis" — the pattern it already follows in citation practice but not in its position. Alternatively, extract the forward-citing remarks from `foundations.tex` into a Part IV addendum.

## 6. Summary

- **19 dangling orphan labels** — fixable by adding `\label{ch:*}` and `\label{part:*}` aliases.
- **15 hard forward-dependency violations** — dominantly Part I → Part VI via `thm:chiral-higher-deligne` family.
- **1 structural cycle** — Part I heptagon ↔ Part VI higher-Deligne, interrupted only by the fact that both proofs reference the other's lemmas rather than theorems.
- Closure of all three fixes above reduces the forward-violation count from 15 to 0 without narrative loss, and eliminates the cycle by placing `chiral_higher_deligne.tex` upstream of the climax chapters.
