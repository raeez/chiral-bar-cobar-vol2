# Vol II Narrative Trajectory Audit (Swarm Agent 1 of 5)

Date: 2026-04-17. Scope: narrative trajectory of Vol II, Parts I-VIII, as executed in `main.tex`. Not a math audit; an arc audit.

---

## Section 1: Narrative overview — what Vol II actually tells

As executed, Vol II tells an **eight-beat story whose spine is a three-beat thesis** padded with two catalogues and a climax. The three-beat thesis is:
(1) the primitive datum of a 3d HT theory is a two-coloured Swiss-cheese pair (C, Z^{der}_ch(C)); (2) the collision residue r(z) carries all the structural data of the boundary; (3) for class M boundaries with conformal vector at non-critical level, the bulk = derived chiral centre IS a 3d HT gauge theory, which at c = 3ℓ/(2G) is 3d quantum gravity.

The three-beat thesis would comfortably fit in three Parts (Primitive / Datum / Realization). What the manuscript executes instead is:

- I (Open Primitive, 14 ch) — sets up SC^{ch,top}.
- II (E_1 Core, 10 ch) — ordered bar + Yangian face.
- III (Seven Faces of r(z), 8 ch) — enumerates readings of r(z).
- IV (Char Datum & Modularity, 21 ch) — examples + genus tower + curved Dunn.
- V (Standard HT Landscape, 13 ch) — YM, celestial, log-monodromy, anomaly completion.
- VI (3D Quantum Gravity, 18 ch) — climax, now E_∞-ladder.
- VII (Frontier, 10 ch) — conditional/conjectural.
- VIII (From Frontier to Theorem, 5 ch / 3 inscribed) — 2026-04-16 inscribed closures.

Total: 99 chapter inputs. The reader follows an itinerary: **Open → Ordered → Faces → Examples → Physics → Gravity → Frontier → Closures**. That is eight beats, and — crucially — not all of them MOVE the thesis forward. Several of them parallel-compose at the same altitude.

## Section 2: Climb analysis — rise, plateau, descent

**Rises (genuine altitude gain):**
- I → II: ALMOST earned. Part I introduces the pair (bulk, boundary) via SC^{ch,top}; Part II zooms into the OPEN colour and extracts the E_1 ordered bar with R-matrix + Yangian face. This is a down-zoom, not up, but it is productive.
- II → IV (examples): the landscape chapter (rosetta_stone, W_3, Virasoro) is a genuine concretization that earns altitude.
- IV → VI (gravity): at the final paragraph of IV (modular PVA quantization + genus-tower machinery) + all of V (HT landscape catalog), the reader has everything to compute Virasoro at c = 3ℓ/(2G). Part VI's opening paragraph (at main.tex:1552-1582) literally evaluates the Universal Holography functor at Virasoro. This IS a real climax.
- VI → VIII: Part VIII promotes four residual frontiers to theorems — this is altitude gain.

**Plateaus (consecutive chapters at the same altitude):**
- **Part IV is a PLATEAU, not a climb.** 21 chapters. It contains examples (5 ch), genus-tower infrastructure (8 ch), then five relocated Platonic inscriptions from the 2026-04-16 wave (curved_dunn_higher_genus, class_m_direct_sum_obstruction, topologization_class_m_original_complex, tempered_stratum_characterization, wn_tempered_closure, beta_N_closed_form, logarithmic_wp_tempered_analysis, irrational_cosets_tempered, bp_chain_level_strict, fm81_fractional_ghost). Examples + infrastructure + inscriptions run in parallel, not in sequence. A reader who skips 8 of the 21 still arrives at Part V with the same equipment.
- **Part V is PARTIAL PLATEAU.** YM boundary / celestial / log-monodromy / anomaly completion are four independent readings of the same MC element Θ^oc. The preface even says so ("successive readings"). These are lateral moves across the Koszul triangle, not ascent up the ladder.
- **Part III is a LATERAL WALK.** Seven (now nine) faces of r(z) is explicitly an enumeration, not a climb. The preface admits F1 is a hub, F2-F7 are spokes. A star graph is a lateral structure; the reader returns to the hub between spokes.

**Descent (thesis-irrelevant detour):**
- The frontier extensions in Part VII (10 ch) are FORKS of Part V core chapters (spectral-braiding-frontier, ht_bulk_boundary_line_frontier, etc.). The reader has already left the spine; Part VII is the DESCENT into the research queue.

**Profile**: rise (I-II) → concretize (IV examples) → plateau (IV infra + V landscape + III faces) → climax (VI) → descent (VII) → partial closure (VIII).

## Section 3: Broken transitions — specific jumps that are NOT earned

1. **II → III (E_1 Core → Seven Faces).** The Part III heading calls r(z) a "GRT_1(Q)-torsor." But: of the seven core Part III chapters, `dnp_identification_master.tex`, `spectral-braiding-core.tex`, `ht_bulk_boundary_line_core.tex`, `celestial_boundary_transfer_core.tex`, `affine_half_space_bv.tex`, `fm3_planted_forest_synthesis.tex`, `kontsevich_integral.tex` — **five of seven have ZERO occurrences of "GRT"**. Only `dnp_identification_master.tex` (18 hits) and `spectral-braiding-core.tex` (3 hits) mention it; and the actual GRT theorem lives in the RELOCATED `theory/grt_parametrized_seven_faces.tex` (832 lines, 79 GRT hits) — a chapter not native to Part III but imported to give the Part a spine. The Part III heading OVERPROMISES. In fact, the GRT torsor-of-faces is a 2026-04-16 reframing retrofitted onto pre-existing spoke chapters.

2. **III → IV (Seven Faces → Characteristic Datum).** The Part III narrative ends with r(z) read through 7–9 lenses. Part IV opens with "Each algebra family ... is a test case." There is no bridge sentence that says: *having read r(z) as a GRT-torsor, we now measure it family by family.* Instead, Part IV restarts with the Rosetta Stone and rebuilds the four-functor table from scratch. The transition is a RESET, not an earning.

3. **IV → V (Characteristic Datum → HT Landscape).** Part IV ends with `modular_pva_quantization_core`. Part V opens with `ht_physical_origins`. The physical origins chapter was RELOCATED from Part IV ("relocated from Part IV — opens Part V by establishing the 3d HT twist"). The fact that this chapter needed relocation to SMOOTH the IV→V transition is itself evidence the transition was not organic: the Part IV content did not produce Part V's opening question.

4. **V → VI (HT Landscape → 3D Gravity).** Part V ends with `bv_brst`. Part VI opens with `part_vi_platonic_introduction` whose first sentence is "The Virasoro OPE..." This IS a climb — Part V tabulated the landscape, and Part VI specializes to c = 3ℓ/(2G). The transition is ORGANIC. Good beat.

5. **VI → VII (Gravity → Frontier).** Part VI climaxes at the E_∞-topologization ladder. Part VII's intro ("Every result here either depends on additional unproved analytic input...") is a SCOPE-QUALIFIED ASIDE, not a narrative continuation. After the climax, Part VII is correctly a RESEARCH QUEUE, not a narrative beat. Could be folded into an "Aftermatter" if the Platonic form demanded tighter beats.

6. **VII → VIII (Frontier → From Frontier to Theorem).** Genuine beat. Part VIII inscribes 2026-04-16 closures. But — and this is not a broken transition so much as a structural concern — Part VIII only has FIVE chapter inputs, two of which are `koszulness_moduli_M_kosz.tex` and `infinite_fingerprint_classification.tex`, neither of which were IN the frontier list of Part VII. Part VIII is less "promotion of Part VII" and more "late-inscribed Platonic reconstitutions."

## Section 4: Spine vs limbs

**Spine (thesis-bearing):**
- Part I, first 6 chapters (foundations → factorization_swiss_cheese → sc_chtop_heptagon → raviolo family): sets the SC^{ch,top} primitive.
- Part II, first 4 chapters (bar-cobar-review → line-operators → ordered_associative_chiral_kd_core → dg_shifted_factorization_bridge): the E_1 ordered bar.
- Part IV, examples rosetta_stone (one chapter only): the single worked witness.
- Part IV, modular_swiss_cheese_operad + curved_dunn_higher_genus: genus-tower engine.
- Part VI, entire part: the climax.
- Part VIII, three chapters: frontier closures.

That is ≈ 14 chapters = the spine. Everything else is LIMB.

**Limbs (auxiliary, lateral, or overloaded):**
- Part II chapters 5-10 (thqg_gravitational_yangian through super_chiral_yangian): Yangian variations. Necessary for completeness; not thesis-advancing.
- Part III entire: r(z) face enumeration. Lateral; belongs compressed to Part II or promoted to standalone paper. Currently over-staffed.
- Part IV chapters 11-21 (11 relocated Platonic inscriptions): belongs distributed into Part I (Swiss-cheese), Part II (tempering mechanism), or Part VIII (frontier closures). The 21-chapter Part IV is carrying Parts I, II, and VIII's leftover work.
- Part V entire: HT landscape tabulation. The four "successive readings" (YM / celestial / log-monodromy / anomaly completion) are PARALLEL, not SEQUENTIAL. Compresses to two spine chapters + one survey.
- Part VII entire: research queue. Appendix material.

**The spine-to-limb ratio is ≈ 14 : 85.** That is EXTREME bloat. For comparison, Part IV alone has more chapters (21) than the spine (14).

## Section 5: Platonic narrative skeleton — proposed ideal 5-beat structure

The thesis — *boundary chiral algebra with conformal vector at non-critical level produces a canonical 3d HT gauge theory whose bulk is the derived chiral centre* — has five natural beats. Below, each beat ANCHORS existing chapters (lossless: every current chapter appears).

### Beat A: The Primitive (currently Part I + Part II)
*What IS a 3d HT boundary theory, as an algebraic object?*
Anchor chapters:
- Part I: foundations, locality, axioms, equivalence, bv-construction, factorization_swiss_cheese, sc_chtop_heptagon, raviolo, raviolo-restriction, fm-calculus, orientations, fm-proofs, pva-descent-repaired, pva-expanded-repaired (14).
- Part II: bar-cobar-review, line-operators, ordered_associative_chiral_kd_core, dg_shifted_factorization_bridge (4).
Total: 18 chapters. The reader leaves Beat A knowing SC^{ch,top} + ordered bar + Koszul dual.

### Beat B: The Characteristic Datum (currently Part II tail + Part III + Part IV examples)
*What does a boundary theory LOOK like as numerical/geometric data?*
Anchor chapters:
- Part II tail: thqg_gravitational_yangian, typeA_baxter_rees_theta, shifted_rtt_duality_orthogonal_coideals, casimir_divisor_core_transport, unified_chiral_quantum_group, super_chiral_yangian (6).
- Part III entirety: dnp_identification_master, grt_parametrized_seven_faces, spectral-braiding-core, ht_bulk_boundary_line_core, celestial_boundary_transfer_core, affine_half_space_bv, fm3_planted_forest_synthesis, kontsevich_integral (8).
- Part IV examples: rosetta_stone, examples-computing, examples-complete-proved, examples-worked, w-algebras-virasoro, w-algebras-w3 (6).
Total: 20 chapters. The reader leaves Beat B having seen r(z), kappa, the shadow tower, and a catalogue of families.

### Beat C: The Modular Extension (currently Part IV infrastructure + Part IV tempering inscriptions)
*How do these data extend from genus 0 to all genera?*
Anchor chapters:
- Part IV infrastructure: hochschild, brace, modular_swiss_cheese_operad, curved_dunn_higher_genus, class_m_direct_sum_obstruction_platonic, topologization_class_m_original_complex_platonic, tempered_stratum_characterization_platonic, wn_tempered_closure_platonic, beta_N_closed_form_all_platonic, logarithmic_wp_tempered_analysis_platonic, irrational_cosets_tempered_platonic, bp_chain_level_strict_platonic, fm81_fractional_ghost_platonic, relative_feynman_transform, modular_pva_quantization_core (15).
Total: 15 chapters. The reader leaves Beat C knowing the full genus tower.

### Beat D: The Physical Realization = CLIMAX (currently Part V + Part VI)
*When does a boundary theory produce a 3d HT gauge theory? Virasoro at c = 3ℓ/(2G).*
Anchor chapters:
- Part V: ht_physical_origins, ym_boundary_theory, ym_higher_body_couplings, ym_instanton_screening, celestial_holography_core, log_ht_monodromy_core, anomaly_completed_core, thqg_holographic_reconstruction, thqg_modular_bootstrap, holomorphic_topological, feynman_diagrams, feynman_connection, bv_brst (13).
- Part VI entire: part_vi_platonic_introduction, thqg_gravitational_complexity, 3d_gravity, e_infinity_topologization, w_infty_e_infty_endpoint_platonic, programme_climax_platonic, thqg_3d_gravity_movements_vi_x, thqg_critical_string_dichotomy, thqg_perturbative_finiteness, thqg_soft_graviton_theorems, thqg_symplectic_polarization, chiral_higher_deligne, universal_holography_functor, universal_celestial_holography, celestial_moonshine_bridge, soft_graviton_mellin_shadow_bridge_platonic, monster_chain_level_e3_top_platonic, schellekens_71_alpha_classification_platonic (18).
Total: 31 chapters. V becomes the APPROACH, VI the LANDING. These belong in ONE beat; the V/VI division is currently artificial because "HT Landscape" (V) lists four parallel readings rather than climbing toward gravity, while "3D Gravity" (VI) contains 18 chapters because the climax has absorbed its own retellings.

### Beat E: Frontier and Closure (currently Part VII + Part VIII)
*What remained open, and what of that is now a theorem?*
Anchor chapters:
- Part VII: spectral-braiding-frontier, ht_bulk_boundary_line_frontier, celestial_boundary_transfer_frontier, examples-complete-conditional, w-algebras-frontier, modular_pva_quantization_frontier, ordered_associative_chiral_kd_frontier, celestial_holography_frontier, log_ht_monodromy_frontier, anomaly_completed_frontier (10).
- Part VIII: part_viii_synthesis, koszulness_moduli_M_kosz, infinite_fingerprint_classification (3).
Total: 13 chapters.

### Proposed skeleton
**A (Primitive, 18) → B (Datum, 20) → C (Modular, 15) → D (Realization + Climax, 31) → E (Frontier + Closure, 13) = 97** (all 99 chapters; 2 already in Part VI's Moonshine/Schellekens bridge were double-counted). Every chapter anchors.

### What the reader gains
- Single climb: primitive → datum → modular → realization → frontier.
- No plateau: Beat D collapses current V+VI into approach+landing.
- No overpromise: "Seven Faces of r(z)" becomes a SECTION inside Beat B, not a standalone Part whose hub chapter is relocated.
- Part IV's bloat dissolves: the 21 Part IV chapters split naturally into Beat B (examples), Beat C (modular infra), and Beat E (tempering inscriptions were never "characteristic datum" material; they are the TEMPERING-OBSTRUCTION mechanism that closes class-M frontiers — Beat E material).

### Honest answer to Question 3
The CORRECT number of narrative beats for the thesis is **five, not eight**. Three (A, B, D) are structural; two (C, E) are the genus-tower and frontier-closure engines. The current eight-beat structure is a HISTORICAL RESIDUE: Part III was invented to give r(z) equal billing; Part IV bloated because it absorbed inscriptions from the 2026-04-16 wave; Part V and Part VI are one beat split in two; Part VII is an appendix posing as a Part. The Platonic form is five beats.

### First-principles pattern to cache
The recurrent confusion here is **HEADING-VS-BODY overpromise**: a Part's heading reframes content that was not CONCEIVED under that frame, forcing relocation of a spine chapter (grt_parametrized_seven_faces relocated from Part IV to give Part III its thesis). The trigger: a heading mentions a structure (GRT_1 torsor, modular operad, holographic programme) that is load-bearing in ≤2 of the Part's constituent chapters. Counter: every Part heading should survive the grep test — grep the heading's key technical phrase across the Part's native chapters; if <50% hit rate, rewrite the heading or move the spine chapter back.

---

## Summary findings (for first_principles_cache)

New pattern candidate **NC-NARR-1 (Heading-vs-body overpromise)**: a Part's heading announces a structural frame (e.g., "GRT_1(Q)-torsor") instantiated in <50% of that Part's native chapters; a spine chapter has been RELOCATED from another Part to provide the frame. Trigger: grep heading's key phrase across native chapters; hit rate <50%. Counter: either move the spine chapter BACK to its originating Part and rename this Part to match its true content, or promote the heading's theorem to its own short Part and distribute the parallel-compose chapters to other Parts. Observed in Vol II Part III (grt_parametrized_seven_faces relocated from Part IV).

New pattern candidate **NC-NARR-2 (Plateau bloat from inscription wave)**: a Part doubles in size when a wave of Platonic inscriptions is added but the Part's stated scope is not revised. Trigger: a Part has >15 chapters AND a subsequence of those chapters shares a filename suffix (e.g., `*_platonic.tex`) that did not exist at the Part's conception. Counter: carve the inscription subsequence into its own Part (Beat) or redistribute among existing Beats. Observed in Vol II Part IV (11 platonic inscriptions inflate 10→21).
