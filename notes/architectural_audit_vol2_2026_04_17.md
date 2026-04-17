# Architectural Audit, Vol II --- 2026-04-17

Adversarial first-principles audit of Vol II's part/chapter sequencing. Scope: `main.tex` backbone (lines 1327--1665), Part IV `\input` inventory (~26 chapters), Part III GRT_1(Q)-torsor advertisement, Part VI bloat, Part VII frontier duplication, Part VIII as new terminal part. Method: Chriss--Ginzburg + Beilinson + Drinfeld --- no AI slop, no em dashes, lossless rearrangement only. Attribution: Raeez Lorgat.

---

## 1. Executive summary

Five top findings, in descending severity.

**(F1) Part IV is not a part, it is a junk drawer.** Part~IV \emph{The Characteristic Datum and Modularity} holds 26 inputs (examples + Hochschild/brace + modular-SC + GRT-parametrized seven faces + unified chiral QG + SC heptagon + curved-Dunn + class-M cluster of 10 chapters + BP + FM81 + relative Feynman + modular PVA + HT physical origins). Parts I--III hold 7--13 each. Part~IV's \emph{chapters} span five distinct topics: boundary-algebra examples, Hochschild/brace bulk calculus, modular operadic structure, class-M tempering, and PVA-quantization bridges. Cutting Part~IV into IV(a)~\emph{Boundary Examples + Hochschild}, IV(b)~\emph{Modular Structure and Shadow Tempering}, is the single highest-value architectural move.

**(F2) Part~III's GRT_1(Q)-torsor headline is aspirational, not enacted.** None of the 7 core chapters in Part~III (dnp, spectral-braiding-core, ht-bulk-boundary-line-core, celestial-boundary-transfer-core, affine-half-space-bv, fm3-planted-forest-synthesis, kontsevich-integral) contains a single `GRT_1(\mathbb{Q})` reference in body text (grep: 0 hits). The GRT-parametrized master theorem lives in Part~IV (`grt_parametrized_seven_faces.tex`) and the F8/F9 enumeration in `notes/part_III_platonic_reconstitution.md`. The \emph{torsor} is Part~IV content; Part~III is the \emph{star of seven faces} without associator parametrization.

**(F3) Theorem F (Universal Holography) is architecturally mislocated in Part~VI.** `universal_holography_functor.tex` (1142 lines, `\ch:universal-holography-functor`, `\thm:universal-holography`) is Vol~II's native climax theorem. Placing it as chapter~13 of 18 inside Part~VI buries the functorial statement under nine `thqg_*` expansions of 3d gravity. The natural home is \emph{either} a dedicated Part~VI(a) \emph{Universal Holography} with the one-chapter functor at its head, or the final chapter of Part~VII \emph{Climax}. Current placement contradicts the preface's "two Vol~II-native theorems" framing.

**(F4) Part~VII Frontier is a duplicate index, not a part.** Eight `*_frontier` chapters (spectral-braiding-frontier, ht_bulk_boundary_line_frontier, celestial_boundary_transfer_frontier, w-algebras-frontier, modular_pva_quantization_frontier, ordered_associative_chiral_kd_frontier, celestial_holography_frontier, log_ht_monodromy_frontier, anomaly_completed_frontier, examples-complete-conditional) each shadow a core chapter split into \texttt{\_core}/\texttt{\_frontier}. The \texttt{\_frontier} file is the conditional/conjectural residue. Current Part~VII is a union of residues, not a coherent frontier chapter. Collapsing \texttt{\_frontier} content into one subsection per core chapter (named "Open problems" or "Conditional extensions") is standard practice.

**(F5) Part~VIII's synthesis is 483 lines pointing at theorems already proved in Parts~IV/V/VI.** `part_viii_synthesis.tex` header says "Synthesis-only file. Cross-references existing theorems by `\label`; contains NO new theorem statements." The two new chapters `koszulness_moduli_M_kosz.tex` (143 lines) and `infinite_fingerprint_classification.tex` (138 lines) contain brief definition/theorem sketches. Part~VIII is a \emph{pointer} part, not a content part. Its proper role is either a narrative epilogue (`\chapter*{Synthesis}` at the end of Part~VI/VII) or the content is absorbed into `concordance.tex`. If retained, Theorems F and G (the two Vol~II-native theorems per preface §II) should live in Part~VIII as their natural destination, not in Part~VI/IV respectively.

---

## 2. Part-by-part adversarial attack

### Part I (The Open Primitive, 13 chapters)

(a) \textbf{Claim.} Primitive datum of 3d~HT theory on $\mathbb{C}_z \times \mathbb{R}_t$ is the open/closed factorization dg-category $\mathcal{C}$; Swiss-cheese operad $\SCchtop$; bar complex as coalgebraic shadow. (b) \textbf{Right.} The \emph{ambient} geometric/operadic setting is correctly front-loaded. foundations, locality, axioms, equivalence, factorization\_swiss\_cheese, raviolo, fm-calculus, orientations, fm-proofs establish the stage. PVA-descent closes the loop to $\lambda$-brackets. (c) \textbf{Wrong.} The chapter `bv-construction.tex` is a Part~IV-style construction (BV bracket on the derived center) masquerading as a foundation. `foundations_overclaims_resolved.tex` and `foundations_recast_draft.tex` exist but are not `\input{}`'d --- FM174 zombie drafts. `pva-descent.tex` (zombie, superseded by `pva-descent-repaired.tex`) still exists on disk per FM172. (d) \textbf{Move.} Delete the two foundations drafts and the zombie pva-descent.tex (merge canonical content); relocate `bv-construction.tex` to Part~V (Standard HT Landscape, BV-BRST cluster) where it belongs as a physics construction rather than a foundational axiom.

### Part II (The $E_1$ Core, 8 chapters)

(a) \textbf{Claim.} Ordered bar $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ with deconcatenation is the native Swiss-cheese open-colour object; carries R-matrix, KZ associator, Yangian. (b) \textbf{Right.} bar-cobar-review + line-operators + ordered-associative-chiral-KD-core + dg-shifted-factorization-bridge make the E_1 core cohere. Gravitational Yangian and type-A Baxter-Rees-theta are E_1-chiral constructions. (c) \textbf{Wrong.} Part~II advertises `E_1 Core` but contains \emph{two separate E_1 stories}: (i) bar-cobar + ordered-associative (abstract E_1 machinery); (ii) type-A Baxter-Rees, shifted RTT, Casimir divisor, gravitational Yangian (\emph{worked Yangian examples}). The split is load-bearing per FM169 ("gravitational Yangian as Hopf" vs classical). `dg_shifted_factorization_bridge.tex` is the single chapter that belongs at the intersection. (d) \textbf{Move.} Relocate `typeA_baxter_rees_theta.tex`, `shifted_rtt_duality_orthogonal_coideals.tex`, `casimir_divisor_core_transport.tex`, `thqg_gravitational_yangian.tex` into a new Part~III(a) "Concrete chiral quantum groups" between the abstract Part~II E_1 core and the Part~III faces. This leaves Part~II at 4 chapters (bar-cobar-review, line-operators, ordered-associative-chiral-KD-core, dg-shifted-factorization-bridge), lean and abstract.

### Part III (The Faces of $r(z)$: a GRT_1(Q)-torsor, 7 chapters)

(a) \textbf{Claim.} Seven guises of $r(z)$: Drinfeld--Kohno, spectral R-matrix, Sklyanin, Koszul-dual line-side, celestial OPE, dg-shifted Yangian, holographic boundary-to-bulk. (b) \textbf{Right.} The seven faces are real; F1 (dnp bar hub) through F7 (kontsevich integral) map cleanly to the 7 chapters. (c) \textbf{Wrong.} \textbf{The GRT_1(Q)-torsor framing is NOT enacted anywhere in the 7 core chapters}, per grep: 0 hits of `GRT_1` across dnp, spectral-braiding-core, ht-bulk-boundary-line-core, celestial-boundary-transfer-core, affine-half-space-bv, fm3-planted-forest-synthesis, kontsevich-integral. The GRT-parametrized master theorem lives in Part~IV (`chapters/theory/grt_parametrized_seven_faces.tex`). F8 (Brown motivic) and F9 (Willwacher operadic) are canonical orbit additions per `notes/part_III_platonic_reconstitution.md`. Part~III's title overclaims. (d) \textbf{Move.} Either (i) \emph{promote} `grt_parametrized_seven_faces.tex` from Part~IV to Part~III's opening chapter, and add F8/F9 bodies as Part~III's final two chapters (9 total); or (ii) \emph{demote} Part~III title to "The Faces of $r(z)$" and note the GRT-torsor upgrade in Part~IV via explicit cross-reference. Option (i) is lossless; option (ii) is honest. Option (i) preferred.

### Part IV (The Characteristic Datum and Modularity, 26 chapters --- BLOATED)

(a) \textbf{Claim.} Each algebra family is a test case for the open/closed architecture; chiral derived center = bulk; genus-zero SC^{ch,top} extends to all genera. (b) \textbf{Right.} The pentagon of examples--Hochschild--modular is real. Rosetta--examples-computing--examples-worked give the Heisenberg/KM/W bench; Hochschild + brace implement the bulk; modular-SC-operad + curved-Dunn + class-M cluster + GRT-seven-faces give modular structure; relative-Feynman + modular-PVA + HT-physical-origins close the physics bridges. (c) \textbf{Wrong.} This is five parts compressed into one:

  (IV.A) Boundary algebra examples: `rosetta_stone`, `examples-computing`, `examples-complete-proved`, `examples-worked`, `w-algebras-virasoro`, `w-algebras-w3` (6 chapters).

  (IV.B) Bulk calculus: `hochschild`, `brace`, `sc_chtop_heptagon` (3 chapters).

  (IV.C) Modular structure: `modular_swiss_cheese_operad`, `grt_parametrized_seven_faces`, `curved_dunn_higher_genus`, `unified_chiral_quantum_group` (4 chapters).

  (IV.D) Class-M tempering cluster: `class_m_direct_sum_obstruction_platonic`, `topologization_class_m_original_complex_platonic`, `tempered_stratum_characterization_platonic`, `wn_tempered_closure_platonic`, `beta_N_closed_form_all_platonic`, `logarithmic_wp_tempered_analysis_platonic`, `irrational_cosets_tempered_platonic`, `super_chiral_yangian`, `bp_chain_level_strict_platonic`, `fm81_fractional_ghost_platonic` (10 chapters).

  (IV.E) PVA/physics bridges: `relative_feynman_transform`, `modular_pva_quantization_core`, `ht_physical_origins` (3 chapters).

(d) \textbf{Move.} Split Part~IV along the IV.A + IV.B = new Part~IV "Boundary Examples and Bulk Calculus" (9 chapters) and IV.C + IV.D + IV.E = new Part~V "Modularity, Shadow Tempering, and PVA Quantization" (17 chapters). Alternate cut: fold IV.A into the existing Part~V "Standard HT Landscape" (it is already a landscape); keep IV.B with Theorem~H (chiral\_higher\_deligne) as a dedicated "Bulk and Brace" part; let IV.C + IV.D + IV.E remain as "Modularity and Tempering." Either cut halves the Part~IV line count.

### Part V (The Standard HT Landscape, 13 chapters)

(a) \textbf{Claim.} Yang--Mills, celestial, log-HT, anomaly completion are successive readings of $\Theta^{\mathrm{oc}}$. (b) \textbf{Right.} The chapter list (ym\_boundary, ym\_higher\_body, ym\_instanton, celestial\_holography, log\_ht\_monodromy, anomaly\_completed, thqg\_holographic\_reconstruction, thqg\_modular\_bootstrap, holomorphic\_topological, feynman\_diagrams, feynman\_connection, bv\_brst) does cover the HT landscape. (c) \textbf{Wrong.} Two chapters are climax-level, not landscape-level: `thqg_holographic_reconstruction` and `thqg_modular_bootstrap`. They are \emph{preparation for Theorem~F (Universal Holography)}. Placing them as chapters~7--8 of Part~V hides their role. Feynman-diagrams and feynman-connection are physics-bridge chapters migrated from Vol~I and belong with `bv_brst` as a single BV cluster, not scattered. (d) \textbf{Move.} Relocate `thqg_holographic_reconstruction.tex` and `thqg_modular_bootstrap.tex` to Part~VI(a) \emph{Universal Holography} preamble (they are preparation chapters). Cluster the three BV chapters (feynman\_diagrams, feynman\_connection, bv\_brst) at the end of Part~V as a single three-chapter BV-BRST block.

### Part VI (Three-Dimensional Quantum Gravity, 18 chapters)

(a) \textbf{Claim.} The climax: Virasoro $\lambda$-bracket generates 3d gravity. Ten movements. (b) \textbf{Right.} part\_vi\_platonic\_introduction + thqg\_gravitational\_complexity + 3d\_gravity + e\_infinity\_topologization + w\_infty\_e\_infty\_endpoint + programme\_climax\_platonic + thqg\_3d\_gravity\_movements\_vi\_x + thqg\_critical\_string\_dichotomy + thqg\_perturbative\_finiteness + thqg\_soft\_graviton\_theorems + thqg\_symplectic\_polarization are genuinely 3d-gravity-climax content. (c) \textbf{Wrong.} Three chapters break the 3d-gravity theme: `chiral_higher_deligne.tex` is Theorem~H (universal construction, not 3d-gravity-specific); `universal_holography_functor.tex` is Theorem~F (the \emph{other} Vol~II-native theorem); `celestial_moonshine_bridge.tex`, `soft_graviton_mellin_shadow_bridge_platonic.tex`, `monster_chain_level_e3_top_platonic.tex`, `schellekens_71_alpha_classification_platonic.tex` are celestial/Monster/Schellekens expansions. Part~VI is in fact \emph{two} parts: (i) 3d gravity proper (11 chapters); (ii) Theorems~F, H + celestial/Monster/Schellekens (7 chapters). `universal_celestial_holography.tex` is Part~V (celestial) content. (d) \textbf{Move.} Extract Theorems F and H. Let Part~VI be 11 chapters of 3d gravity proper. Create Part~VII(a) "Universal Holography and Chiral Higher Deligne" with universal\_holography\_functor + chiral\_higher\_deligne + universal\_celestial\_holography (3 chapters). Let the celestial--Monster--Schellekens cluster go to Part~V (they are landscape data on the non-logarithmic standard landscape).

### Part VII (The Frontier, ~10 chapters, all \_frontier)

(a) \textbf{Claim.} Conditional/conjectural extensions of the proved core. (b) \textbf{Right.} Every \texttt{\_frontier} chapter is the residue of a \texttt{\_core}/\texttt{\_frontier} split of an earlier parent chapter; the residue is legitimately frontier material. (c) \textbf{Wrong.} The split-into-core-plus-frontier convention generates \emph{parallel duplicate TOC entries}. A reader sees `celestial_boundary_transfer_core` in Part~III AND `celestial_boundary_transfer_frontier` in Part~VII and has to reconstruct the pairing. Intra-chapter organization (core material + "Open problems" subsection) is standard; inter-part separation is unusual. Also: `ym_synthesis_frontier.tex` is DISABLED in main.tex (line 1604: `% DISABLED: content refactored into ym_instanton_screening`) but still exists on disk --- stale file. (d) \textbf{Move.} Absorb each \texttt{\_frontier} chapter as a final "Open questions and conditional extensions" section of its \texttt{\_core} parent. Delete `ym_synthesis_frontier.tex`. If a genuine frontier cluster remains, name it precisely (e.g. "Frontier: logarithmic VA and irrational-coset landscape").

### Part VIII (From Frontier to Theorem, 3 chapters)

(a) \textbf{Claim.} Promote the four genuine frontiers (curved-Dunn $H^2$, class-M chain-level, periodic-CDG, chiral Deligne-Tamarkin) to theorems. (b) \textbf{Right.} The four frontiers are real research opens. Writing a chapter inscribing each closure is legitimate. (c) \textbf{Wrong.} Three of the four closures are proved \emph{in earlier parts}: curved-Dunn is `curved_dunn_higher_genus.tex` in Part~IV; class-M DS-Hoch is `chiral_higher_deligne.tex` in Part~VI; periodic-CDG is Vol~I's `periodic_cdg_admissible.tex` (not Vol~II at all). The \emph{synthesis} file (`part_viii_synthesis.tex`, 483 lines) explicitly contains no new theorems. The two new chapters `koszulness_moduli_M_kosz.tex` (143 lines) and `infinite_fingerprint_classification.tex` (138 lines) are thin. This is not a part; it is an afterword plus two short chapters that belong in Part~IV's "Modular Structure" cluster (they are classification data parametrized by GRT). (d) \textbf{Move.} Promote Theorem~G (Infinite Fingerprint) and the Koszulness Moduli Scheme into Part~IV's modular structure cluster. Let `part_viii_synthesis.tex` become `chapters/frame/synthesis.tex`, a final chapter (not a part) after Part~VI-climax and before the conclusion. This reduces the part count from 8 back to 7 and collects the Platonic-reconstitution inscriptions with the chapters they close. Alternatively, retain Part~VIII but reposition: Theorem~F (Universal Holography) and Theorem~G (Infinite Fingerprint) are the two Vol~II-native theorems and should co-locate in Part~VIII.

---

## 3. The seven-theorem / part-structure tension

The preface declares two theorems native to Vol~II (Theorem~F Universal Holography, Theorem~G Infinite Fingerprint) and five theorems inherited from Vol~I (A, B, C, D, H). The remaining Vol~II-native climax is the E_3-topologization theorem and the chiral Higher Deligne theorem. Current placement:

| Theorem | Native to | Location in Vol II | Architectural role |
|---------|-----------|--------------------|--------------------|
| A (bar-cobar properad ∞,2-eq) | Vol I | Part I–II (ambient) | Foundation |
| B (inversion Koszul locus) | Vol I | Part II (E_1 core) | Foundation |
| C (shifted-symplectic) | Vol I | Part IV (modular) | Load-bearing modular |
| D (tensor-Arakelov κ) | Vol I | Part IV (modular) | Load-bearing modular |
| H (chiral Higher Deligne) | Vol I | Part VI (gravity) | **MISPLACED** |
| F (Universal Holography) | Vol II | Part VI (gravity) | **MISPLACED** |
| G (Infinite Fingerprint) | Vol II | Part VIII (frontier) | **ISOLATED** |
| E_3-topologization | Vol II | Part VI (gravity) | Correct |
| E_∞-topologization | Vol II | Part VI (gravity) | Correct |

The tension: Vol II's two native theorems (F, G) are architecturally scattered --- F is buried in Part~VI chapter~13 among nine thqg_* expansions; G is isolated in Part~VIII with 138 lines of development. Theorem~H is a universal construction (applies to all chiral algebras, not just gravitational) and does not belong in the gravity part.

A cleaner map: 7~theorems ⟷ 7~parts, with A+B as Part~I--II foundations, C+D as Part~IV modular, H as Part~IV(b) bulk/brace, F as Part~VI(a) universal holography, G as Part~IV(c) classification, and E_∞-topologization + 3d gravity proper as Part~VI climax. This would treat Part~VIII as an \emph{epilogue}, not a 4-chapter part.

Alternate map (stronger claim): 8~parts with Theorems~F and G co-located in Part~VIII as the \emph{terminal theorems}. This makes Part~VIII a genuine content part (theorems not inherited from Vol~I), and the 4 frontier closures (curved-Dunn, class-M chain-level, periodic-CDG, Deligne-Tamarkin) become \emph{corollaries} rather than the part's content.

---

## 4. Lossless rearrangement proposal

Every move below preserves all mathematical content. No deletions; only renaming, relocation, and absorption of \texttt{\_frontier} residues into their \texttt{\_core} parents. Zombie files (foundations drafts, pva-descent.tex, ym_synthesis_frontier.tex) are deletion-candidates but are strictly optional.

### Proposed new part sequence

| Part | Name | Chapter count | Inputs |
|------|------|---------------|--------|
| I | The Open Primitive | 11 | foundations, locality, axioms, equivalence, factorization_swiss_cheese, raviolo, raviolo-restriction, fm-calculus, orientations, fm-proofs, pva-descent-repaired, pva-expanded-repaired |
| II | The E_1 Core | 4 | bar-cobar-review, line-operators, ordered_associative_chiral_kd_core, dg_shifted_factorization_bridge |
| III | The Faces of r(z) as GRT_1(Q)-torsor | 10 | grt_parametrized_seven_faces (promoted from IV), dnp_identification_master, spectral-braiding-core, ht_bulk_boundary_line_core, celestial_boundary_transfer_core, affine_half_space_bv, fm3_planted_forest_synthesis, kontsevich_integral, F8 Brown motivic (to write), F9 Willwacher operadic (to write) |
| III(a) | Concrete Chiral Quantum Groups | 4 | typeA_baxter_rees_theta, shifted_rtt_duality_orthogonal_coideals, casimir_divisor_core_transport, thqg_gravitational_yangian (relocated from II) |
| IV | Boundary Examples and Bulk Calculus | 9 | rosetta_stone, examples-computing, examples-complete-proved, examples-worked, w-algebras-virasoro, w-algebras-w3, hochschild, brace, sc_chtop_heptagon |
| IV(b) | Modular Structure and Classification | 6 | modular_swiss_cheese_operad, unified_chiral_quantum_group, curved_dunn_higher_genus, koszulness_moduli_M_kosz (relocated from VIII), infinite_fingerprint_classification (relocated from VIII) |
| IV(c) | Shadow Tempering Cluster (class M) | 10 | class_m_direct_sum_obstruction_platonic, topologization_class_m_original_complex_platonic, tempered_stratum_characterization_platonic, wn_tempered_closure_platonic, beta_N_closed_form_all_platonic, logarithmic_wp_tempered_analysis_platonic, irrational_cosets_tempered_platonic, super_chiral_yangian, bp_chain_level_strict_platonic, fm81_fractional_ghost_platonic |
| IV(d) | PVA Quantization and HT Bridges | 3 | relative_feynman_transform, modular_pva_quantization_core, ht_physical_origins |
| V | The Standard HT Landscape | 14 | ym_boundary_theory, ym_higher_body_couplings, ym_instanton_screening, celestial_holography_core, log_ht_monodromy_core, anomaly_completed_core, holomorphic_topological, celestial_moonshine_bridge (from VI), soft_graviton_mellin_shadow_bridge_platonic (from VI), monster_chain_level_e3_top_platonic (from VI), schellekens_71_alpha_classification_platonic (from VI), universal_celestial_holography (from VI), feynman_diagrams, feynman_connection, bv_brst |
| VI | Three-Dimensional Quantum Gravity | 12 | part_vi_platonic_introduction, thqg_gravitational_complexity, 3d_gravity, e_infinity_topologization, w_infty_e_infty_endpoint_platonic, thqg_3d_gravity_movements_vi_x, thqg_critical_string_dichotomy, thqg_perturbative_finiteness, thqg_soft_graviton_theorems, thqg_symplectic_polarization, thqg_holographic_reconstruction (from V), thqg_modular_bootstrap (from V) |
| VII | Universal Holography and Chiral Higher Deligne (two Vol II-native theorems) | 3 | universal_holography_functor (from VI), chiral_higher_deligne (from VI), programme_climax_platonic (from VI) |
| VIII | The Frontier | absorbed | (each *_frontier chapter absorbed as final section of its *_core parent; Part VIII deleted) |

Alternative: keep Part~VIII with F+G+H as its theorem content (reducing Parts VII→Part~VI climax, VIII→Part~VII terminal theorems). Both shapes are lossless; the table above is the stronger version (8 part ⟶ 7 part + subparts).

### Justification summary per move

- Part~II ⟶ Part~II + III(a): separates abstract E_1 from concrete Yangian examples, per FM169 bialgebra-vs-Hopf scope distinction.
- Part~III promote grt_parametrized_seven_faces from Part~IV: enacts the GRT_1(Q)-torsor headline; adds F8/F9 as new canonical orbit representatives per `notes/part_III_platonic_reconstitution.md`.
- Part~IV split ⟶ IV + IV(b) + IV(c) + IV(d): 26 chapters become 9 + 6 + 10 + 3 = 28 (two chapters added from Part~VIII), distributed thematically.
- Part~V gain celestial + Monster + Schellekens + universal-celestial: these are landscape data (non-logarithmic standard landscape), not gravity climax.
- Part~V gain thqg_holographic_reconstruction + thqg_modular_bootstrap ⟶ Part~VI: these are preparatory chapters for Theorem F, belong with gravity.
- Part~VI loses universal_holography_functor + chiral_higher_deligne + programme_climax_platonic: they are \emph{terminal theorems}, belong in Part~VII.
- Part~VII new = three chapters (F, H, climax): the two Vol~II-native theorems plus the climax statement that ties them together.
- Part~VIII absorbed: synthesis file becomes `chapters/frame/synthesis.tex`, a chapter (not a part); each \texttt{\_frontier} merges into its \texttt{\_core}.

---

## 5. Risks and blockers

\textbf{Safe moves (low risk, label-preserving).} Promoting `grt_parametrized_seven_faces.tex` from Part~IV to Part~III: only the \texttt{\\input\{\}} line moves; no `\label{}` changes, no `\ref{}` breakage. Same for relocating `thqg_holographic_reconstruction.tex` and `thqg_modular_bootstrap.tex` into Part~VI. Same for moving `universal_holography_functor.tex`, `chiral_higher_deligne.tex`, `programme_climax_platonic.tex` into a new Part~VII.

\textbf{Label-sensitive moves (medium risk).} Splitting Part~IV into IV + IV(b) + IV(c) + IV(d): introduces new `\label{part:...}` labels. Any `\ref{part:examples}` in Vol~II or Vol~I's cross-volume bridges would need updating --- per V2-AP26, \emph{grep all three volumes for `\\ref\{part:}` before the split}. Grep result: `\ref{part:examples}` hits ~24 per V2-AP26 historical record; current state unknown. Must be verified before cut.

\textbf{Parallel-session conflicts (high risk).} The active parallel session is editing `chapters/frame/part_viii_synthesis.tex`, `koszulness_moduli_M_kosz.tex`, and `infinite_fingerprint_classification.tex`. If the audit proposes moving these files out of Part~VIII and into Part~IV(b), the parallel session's inscription work could conflict. Coordination required: freeze Part~VIII file moves until parallel session completes; apply Part~VIII decisions as a post-inscription architectural pass.

\textbf{Blocker: absorbing \texttt{\_frontier} files.} Each \texttt{\_frontier} file has its own chapter label (e.g. `\label{chap:celestial-boundary-transfer-frontier}`). Absorbing into \texttt{\_core} parent requires converting chapter label to section label AND updating every `\ref{chap:...-frontier}` to `\ref{sec:...-frontier}`. Mechanical but tedious; ~10 chapters × ~5 internal refs each ≈ 50 refs to update. Safe to automate with a script; unsafe to do by hand piecemeal. Recommend: absorb in a dedicated commit, not mixed with other architectural changes.

\textbf{Blocker: Part VIII parallel-session inscription.} The parallel session's Part~VIII is advertised as containing Theorem~F + Theorem~G (the two Vol II-native theorems). If the audit's recommendation to co-locate F and G in Part~VIII is accepted, the parallel session is on the right track; if the audit's recommendation to absorb Part~VIII into Parts IV/VII is accepted, the parallel session should be paused. Beilinson-rectified decision required from the author.
