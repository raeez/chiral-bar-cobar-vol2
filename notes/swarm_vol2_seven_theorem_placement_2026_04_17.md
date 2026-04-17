# Vol II Seven-Theorem Structural Placement Audit (Swarm #3, 2026-04-17)

Adversarial audit of the structural placement of Theorems A, B, C, D, F, G, H in Volume II of the Modular Koszul Duality programme. Focus: is each theorem HOME'd in a chapter/part that advertises it, how buried is it, are Vol II-native F and G appropriately prominent, and does each cross-volume citation resolve to a real Vol I label?

Total Vol II chapter payload: 151,938 lines across 85 included `.tex` files + 2,274 preface + 2,714 introduction. All rush-distance percentages computed against the chapter-body total (excluding front-matter 4,988 lines).

## Section 1. Inscription locations table

| Thm | Label | Home file | Line | Chapter title | Part |
|-----|-------|-----------|------|---------------|------|
| A | `thm:A-infinity-2` (Vol I primary) | `~/chiral-bar-cobar/chapters/theory/theorem_A_infinity_2.tex` | 238 | "Theorem A^{∞,2}: Francis–Gaitsgory bar–cobar equivalence, properad level" | Vol I Part I |
| A (Vol II stage) | (no native theorem env; `\section{}`) | `chapters/theory/factorization_swiss_cheese.tex` | 2250 | "Factorization properads and Theorem A^{∞,2} at properad level" | II-I |
| B | (Vol I native; no Vol II theorem env) | (Vol I) | — | references at `chapters/examples/examples-worked.tex:311, 1092, 1136, 3173`, `rosetta_stone.tex:2254` | Vol I; invoked II-I, II-IV |
| C | `thm:theoremC-total-shifted-symplectic` | **`working_notes.tex:19490` (ORPHAN — not `\input` by `main.tex`)** | 19490 | (session-synthesis `subsec:theoremC-total-shifted-symplectic`) | No part; dead |
| D | `thm:theoremD-tensor-arakelov` | **`working_notes.tex:19634` (ORPHAN)** | 19634 | (session-synthesis `subsec:theoremD-tensor-arakelov`) | No part; dead |
| F | `thm:universal-holography-functor` | `chapters/connections/universal_holography_functor.tex` | 264 | "The Universal Holography Theorem" | II-VI |
| F (duplicate 1) | `thm:programme-climax` "Universal Holography" | `chapters/connections/programme_climax_platonic.tex` | 42 | (section inside Part VI) | II-VI |
| F (duplicate 2) | `thm:universal-holography` (×3 collisions at lines 1805, 1892, 2888) | `chapters/connections/thqg_holographic_reconstruction.tex` | 1805/1892/2888 | (chapter on holographic reconstruction) | II-V |
| G | `thm:fingerprint-complete-ch` | `chapters/theory/infinite_fingerprint_classification.tex` | 83 | "Infinite Fingerprint Classification" | II-VIII |
| H (Vol I primary) | Vol I `thm:theorem-H` (see Vol I `theorem_H_hochschild.tex`) | (Vol I) | — | — | Vol I Part I |
| H (Vol II upgrade) | `thm:chiral-higher-deligne` | `chapters/theory/chiral_higher_deligne.tex` | 419 | "Chiral Higher Deligne" | II-VI |
| H (duplicate) | `thm:chiral-higher-deligne` | `chapters/connections/hochschild.tex` | 2668 | "Chiral Hochschild Cohomology" | II-IV |
| H (Platonic upgrade) | `thm:theoremH-chiral-higher-deligne` | **`working_notes.tex:~19800` (ORPHAN; `main.tex:1617` `\ref` is DANGLING)** | ~19800 | — | No part; dead |

## Section 2. Visibility assessment

- **A**: PROMINENT in Vol I. In Vol II: BURIED (no theorem environment native to Vol II; only an ambient `\section{Factorization properads and Theorem A^{∞,2} at properad level}` at `factorization_swiss_cheese.tex:2250`, halfway through the 4,028-line ambient chapter whose title advertises "Factorization Swiss-cheese," not Theorem A). R-twisted Σ_n-descent Proposition `prop:R-twisted-sigma-n-descent` is healing but still inside the SC chapter.
- **B**: Vol I native. Vol II does not re-inscribe it. Visibility in Vol II: only five prose invocations (no theorem env). Status: REFERENCE-ONLY, appropriate for an inherited theorem — BUT the Vol II reader is given no chapter whose title keys on "bar-cobar inversion" as the Vol II face of Theorem B (ordered_associative_chiral_kd_core.tex would be the natural home).
- **C**: MISSING from main-text arc. Platonic statement lives in orphan `working_notes.tex`. The reader of the built PDF never sees `thm:theoremC-total-shifted-symplectic`.
- **D**: MISSING from main-text arc. Same orphan issue as C; `compute/tests/test_wN_tensor_arakelov_weight_distribution.py:52` decorates `claim="thm:theoremD-tensor-arakelov"` for an orphan label. Independent-verification decorator points to a label the PDF does not contain.
- **F**: DUPLICATED. Three distinct theorem environments (`thm:universal-holography-functor`, `thm:programme-climax` titled "Universal Holography," and `thm:universal-holography` with 3 label collisions inside `thqg_holographic_reconstruction.tex`). Violates AP124 (duplicate labels across and within files) and AP-LABEL-DISCIPLINE. The canonical Platonic inscription `thm:universal-holography-functor` is PROMINENT (own chapter). The two shadows should be renamed `cor:` or deleted.
- **G**: PROMINENT-but-LATE. Has its own chapter (`infinite_fingerprint_classification.tex`, 138 lines), whose chapter title names the theorem. Placed in Part VIII ("From Frontier to Theorem"), structurally the last substantive content before Conclusion.
- **H**: DUPLICATED. `thm:chiral-higher-deligne` labelled at BOTH `chapters/theory/chiral_higher_deligne.tex:419` AND `chapters/connections/hochschild.tex:2668`. AP124 violation. Platonic upgrade `thm:theoremH-chiral-higher-deligne` is orphan in `working_notes.tex`; `main.tex:1617` references this orphan — a build-time dangling `\ref`.

## Section 3. Theorem → Part home assignment

| Thm | Natural Part home | Actual home | Alignment |
|-----|-------------------|-------------|-----------|
| A | Part I (The Open Primitive) — bar complex foundation | II-I SC chapter section | OK (BURIED) |
| B | Part II (The E_1 Core) — bar-cobar inversion | Not in Vol II | SCOPE-OK as inherited |
| C | Part IV (Characteristic Datum + Modularity) | ORPHAN | BROKEN |
| D | Part IV (Characteristic Datum + Modularity) | ORPHAN | BROKEN |
| F | Part VI (Three-Dimensional Quantum Gravity) | II-VI ✓ | OK |
| G | Part IV (class M cluster) OR dedicated Part | II-VIII | DEFENSIBLE-but-BURIED |
| H | Part IV (Hochschild chapter home) + Part VI (higher Deligne upgrade) | II-IV (hochschild.tex) + II-VI (chiral_higher_deligne.tex) | OK (DUPLICATED-LABEL is the issue) |

Part-boundary crossings are justified for H (classical H in IV, E_3-higher Deligne upgrade in VI). Not justified for C and D (ORPHAN = structural rupture).

## Section 4. Vol II-native F and G placement critique

### F (Universal Holography)

`universal_holography_functor.tex` (1142 lines) is Part VI's narrative PEAK. It is placed between `thqg_symplectic_polarization` and `universal_celestial_holography`. The chapter title clearly advertises the theorem. Prose opens (lines 66-89) with the directive "what the programme calls a *climax* is a *theorem*." This is CORRECT placement. No own Part needed: F is the climax of Part VI, and Part VI is explicitly the CLIMAX of the volume.

Critique: F has TWO competing presentations in Part VI — `programme_climax_platonic.tex` (Chapter placed at main.tex:1601, earlier in Part VI) also claims the "Universal Holography" title with label `thm:programme-climax`. Plus `thqg_holographic_reconstruction.tex` in Part V contains the OLDEST shadow with triple-labelled `thm:universal-holography`. Reader reaches the "Universal Holography" theorem THREE times with three different label roots. Heal: rename the older two to `thm:holographic-reconstruction-shadow-form` and `cor:climax-specialization-virasoro`, preserving `thm:universal-holography-functor` as the unique climax label.

### G (Infinite Fingerprint)

Placed in Part VIII ("From Frontier to Theorem"), at main.tex:1684 — the absolute-last substantive chapter before Conclusion. Rush-distance: 99.9%. Two critiques:

1. The chapter is 138 lines long — stub-size (AP114 stub threshold is 50 lines, but a completeness-theorem chapter should breathe). Inside, `thm:fingerprint-complete-ch` is followed by a "proof sketch" env, with case-by-case on G/L/C/M/FF one line per case. This is not a full proof.

2. G couples TIGHTLY to Theorem D (via the sixth fingerprint slot κ_ch; see `rem:fingerprint-theoremD-coupling:128-138`). Structurally, G belongs in Part IV (Characteristic Datum and Modularity) as the COMPLETION statement of that part's landscape census, NOT orphaned into Part VIII.

Recommendation: move `infinite_fingerprint_classification.tex` to Part IV immediately after `wn_tempered_closure_platonic.tex` (where the G/L/C/M/FF classes are already assembled). Keep it stub-size for now but rescope Part VIII to ONLY the four-frontier closure narrative.

## Section 5. Rush-distance metrics (% of volume before encounter)

Chapter-body total = 151,938 lines. Percentages computed against total (preface + intro add rush-distance 3.3% on top if counted).

| Thm | First encounter (chapter line) | Cumulative line | Rush % |
|-----|-------------------------------|-----------------|--------|
| A | `factorization_swiss_cheese.tex:2250` (Part I section header) | ~8,279 | 5.4% |
| B | `bar-cobar-review.tex` (Part II, first invoked in prose) | ~18,605 | 12.2% |
| C | (ORPHAN, never reached) | — | — |
| D | (ORPHAN, never reached) | — | — |
| F | `thqg_holographic_reconstruction.tex:1805` (shadow label in Part V) | ~106,051 | 69.8% |
| F (canonical) | `universal_holography_functor.tex:264` (Part VI climax) | ~146,630 | 96.5% |
| G | `infinite_fingerprint_classification.tex:82` (Part VIII) | ~151,881 | 99.96% |
| H (Vol II) | `hochschild.tex:2668` (Part IV) | ~74,668 | 49.1% |
| H (upgrade) | `chiral_higher_deligne.tex:419` (Part VI) | ~145,905 | 96.0% |

Defensibility:
- F at 96.5% is DEFENSIBLE because the whole volume is constructed TOWARD the climax; the reader is told in the preface to expect it at the end.
- G at 99.96% is NOT defensible structurally: a "classification completeness" theorem belongs where the classification is built (Part IV class M cluster), not after the Frontier.
- C and D being UNREACHABLE is a serious structural flaw; Part IV should contain them as native inscriptions or Part VIII should input the `working_notes.tex` sections (the latter would require splitting `working_notes.tex` into small chapters).

## Section 6. Platonic-ideal placement proposal (LOSSLESS moves)

No content is deleted. Only chapter-order shifts and label renames.

### Move 1: Heal Theorems C and D (highest priority)

Extract `working_notes.tex:19476-19800` (the three `subsec:theoremC-total-shifted-symplectic`, `subsec:theoremD-tensor-arakelov`, `subsec:theoremH-chiral-higher-deligne` subsections) into a new chapter `chapters/theory/cd_h_platonic_upgrades.tex`. Input it immediately after `modular_swiss_cheese_operad.tex` in Part IV (main.tex:~1492, before `curved_dunn_higher_genus.tex`). This makes Theorems C and D REACHABLE; H upgrade gains a proper Part IV home adjacent to its classical form in `hochschild.tex`.

Result: rush-distance for C ≈ 52%, D ≈ 53%, H-upgrade ≈ 53%. C and D are no longer ORPHAN. `main.tex:1617` `\ref{thm:theoremH-chiral-higher-deligne}` now resolves.

### Move 2: Promote G to Part IV

Move `chapters/theory/infinite_fingerprint_classification.tex` input from main.tex:1684 to main.tex:~1503 (after `irrational_cosets_tempered_platonic.tex`, where the G/L/C/M/FF strata are already assembled). Rush-distance for G drops from 99.96% to ~57%. Part VIII retains only the four-frontier closure narrative + `koszulness_moduli_M_kosz.tex`.

### Move 3: Label uniqueness heal (F and H)

Inside `thqg_holographic_reconstruction.tex`: rename the THREE `thm:universal-holography` labels (lines 1805, 1892, 2888) to `thm:holographic-reconstruction-shadow-g0`, `thm:holographic-reconstruction-shadow-general`, `cor:holographic-reconstruction-summary`. Inside `programme_climax_platonic.tex`: rename `thm:programme-climax` → `cor:programme-climax-virasoro-specialization`. Keep `thm:universal-holography-functor` as the unique canonical F label.

Inside `hochschild.tex:2668`: rename `thm:chiral-higher-deligne` → `thm:chiral-higher-deligne-hochschild-form` (the Hochschild-cohomology presentation), preserving `thm:chiral-higher-deligne` at `chiral_higher_deligne.tex:419` as canonical.

Audit all `\ref{thm:chiral-higher-deligne}` and `\ref{thm:universal-holography}` sites and update to the canonical names. AP124 compliance restored.

### Move 4: Heal Theorem A^{∞,2} Vol II visibility

Currently the Vol II face of A is a `\section{}` at `factorization_swiss_cheese.tex:2250`. Extract that section into its own chapter `chapters/theory/theorem_a_infinity_2_vol2_face.tex` that opens Part I (move `factorization_swiss_cheese.tex` to the end of Part I). This puts Theorem A^{∞,2} as the FIRST non-introductory theorem the reader encounters, matching Vol I's architecture.

### Net result

After all four moves: every Platonic theorem has a chapter-title-indexed home, zero orphans, zero duplicate labels, rush-distances {A=5%, B=12% (inherited), C=52%, D=53%, F=96%, G=57%, H=49%+53%+96%}. The climax structure of Part VI is strengthened (F, H-upgrade are the only Part VI theorems, no shadow duplicates). Part VIII narrows to the four-frontier closure + koszulness moduli, matching its title "From Frontier to Theorem."

## Appendix A. Cross-volume reference spot-check (3 of 5 CORRECT; 2 BROKEN)

- `rosetta_stone.tex:2636` → Vol I `thm:A-infinity-2` at `theorem_A_infinity_2.tex:238` ✓ RESOLVES
- `programme_climax_platonic.tex:17,357` → Vol I `thm:A-infinity-2` ✓ RESOLVES
- `main.tex:1617` → `thm:theoremH-chiral-higher-deligne` ✗ DANGLING (orphan in working_notes)
- `compute/tests/test_wN_tensor_arakelov_weight_distribution.py:52` → `thm:theoremD-tensor-arakelov` ✗ DANGLING (orphan)
- `examples-worked.tex:311,1092,1136,3173` "Theorem B of Volume I" (prose, not `\ref`) — editorial; not a build-time dangling ref

Two of five load-bearing cross-volume references resolve to ORPHAN labels. The audit recommends Move 1 (extract from `working_notes.tex`) as the single highest-impact repair.
