# AGENTS.md - Volume II: A_infinity Chiral Algebras and 3D Holomorphic-Topological QFT

## Purpose

This file is the Codex runtime constitution for Volume II. `CLAUDE.md` may contain a larger anti-pattern atlas, historical archaeology, and Claude-oriented orchestration, but `AGENTS.md` must stand on its own as the always-on operating system for Codex/GPT-5.4 in this repo.

Use this file for:

- durable repo-wide invariants;
- task routing and mode selection;
- claim-status discipline;
- verification and convergence discipline;
- cross-volume propagation discipline;
- compaction-safe context and memory hygiene;
- the bridge from manuscript work to compute, tests, build hygiene, and dirty-surface awareness.

Do not use this file as a dumping ground for temporary plans, local chatter, or a second copy of the full anti-pattern catalogue. Keep it compressive and load-bearing.

## Why This File Looks Like This

This constitution is deliberately shaped around current best practice for agentic reasoning and tool use:

- exact scope beats broad vibes;
- issue-shaped prompts beat essays;
- interleaving reasoning with tool actions beats pure prose;
- reflective memory beats repeating the same failed attempt;
- multiple independent checks beat greedy single-derivation confidence;
- symbolic and computational verification paired with natural-language reasoning beats either alone;
- progressive disclosure beats stuffing every workflow into the always-on prompt.

Operational consequence:

- keep the root rules compact;
- move deep repeated workflows into repo skills;
- move deterministic enforcement into hooks;
- require observable artifacts rather than hidden confidence;
- prefer smaller true claims to larger false ones.

## What The Engine Computes

Volume I built the categorical logarithm: the bar construction `B(A)` for chiral algebras on curves, with theorems proving existence, inversion, branch structure, leading coefficient, and coefficient ring. Volume II reads that machine in three dimensions.

The bar complex `B(A)` is an E_1 chiral coassociative coalgebra carrying two structures:

- a differential `d_B` from OPE residues on `FM_k(C)`, encoding the holomorphic chiral product;
- a coproduct `Delta` from ordered deconcatenation on `Conf_k(R)`, encoding the topological interval-cutting.

These make `B(A)` a dg coassociative coalgebra. It is NOT an `SC^{ch,top}`-coalgebra: `B(A)` is a single E_1 coalgebra, not a two-colored SC datum.

The `SC^{ch,top}` structure emerges in the chiral derived center construction. The chiral Hochschild cochain complex `C^bullet_{ch}(A,A)` (defined via the chiral endomorphism operad `End^{ch}_A` with spectral parameters from `FM_k(C)`, NOT via topological Hochschild cochains `RHom_{A^e}(A,A)`) carries brace operations and a Gerstenhaber bracket. The pair `(C^bullet_{ch}(A,A), A)` is the `SC^{ch,top}` datum: bulk (chiral Hochschild cochains) acts on boundary (the algebra `A`) via braces. Open-to-closed is empty: bulk restricts to boundary, not conversely.

Critical distinction:

- `B(A)` is an E_1 coassociative coalgebra classifying twisting morphisms (Theorem A);
- the `SC^{ch,top}` structure lives on the pair `(C^bullet_{ch}(A,A), A)`, NOT on `B(A)`;
- bulk observables are the chiral derived center `Z^{der}_{ch}(A) = H^*(C^bullet_{ch}(A_b, A_b))` of a boundary chart, Morita-invariant in the open-sector factorization dg-category.

At genus `g >= 1`, the curved structure is essential: the non-vanishing of higher `A_infinity` operations is the curved bar structure `d^2 = kappa(A) * omega_g`. Formality fails because the logarithm acquires monodromy.

## /chriss-ginzburg-rectify TOP-LEVEL INJUNCTION (CONSTITUTIONAL)

When the user invokes `/chriss-ginzburg-rectify` (or the skill `chriss-ginzburg-rectify`) on a target file, Phase 1 (Global Diagnostic) is NOT OPTIONAL and is NOT ABBREVIATED. You must analyse the **whole file**, **chunk by chunk**, **linearly progressing from start to finish**, with **small chunk size** (~250-500 lines per Read call, at most). Every line must pass under your eyes.

**Binding rules:**
- The skill's wording "For files >3000 lines: sample strategically" is OVERRIDDEN. Do NOT sample. Do NOT jump. Do NOT read section heads via Grep and call it Phase 1. Do NOT read only opening + closing + dense midsection.
- **Linear progression**: start at line 1. Each subsequent Read starts exactly where the previous one ended (offset = prev_offset + prev_limit).
- **Coverage is a proof obligation**. Before leaving Phase 1, verify: the sum of (limit) across all Phase 1 Reads equals the file line count, and the starting offsets form a contiguous cover of [1, EOF].
- If a Read fails with the 25000-token cap, cut the `limit` in half and retry. Never "skip ahead past the oversized region."

**Scope of /chriss-ginzburg-rectify (author directive, 2026-04-17):** the ENTIRE file must be analysed, chunk by chunk, linearly progressing from start to finish, with SMALL CHUNK SIZE (50-100 lines). A V2-AP40 sweep is a necessary subset of Gate 5 but NOT a substitute for Gates 1-4 (mathematical truth, define-before-use, concept motivation, physical realization) and NOT a substitute for the linear chunk sweep across the whole file. Every chunk passes all five gates before the cursor advances.

## Programme Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type.

### Bar Complex Is E_1-Coassociative; SC^{ch,top} Emerges On The Derived Center

The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output.

Forbidden claims:

- "B(A) is a coalgebra over SC^{ch,top}"
- "the bar complex presents the Swiss-cheese algebra"
- "the bar differential is the closed color"
- "the bar coproduct is the open color"

### The E_n Ladder (E_1 -> E_2 -> E_3-TOPOLOGICAL)

The volume climbs the E_n ladder. Each rung adds one E_1 factor via Dunn additivity applied to the CENTER, not to the algebra. The rungs:

- E_1 (Parts I-II): Ordered bar complex, Koszul duality, line operators. A is E_1.
- E_2 (Parts III-IV): Derived center Z^{der}_{ch}(A) carries E_2 from Deligne conjecture. E_2 lives on Z(A) and Mod_A, NEVER on A. Quantum groups are E_1; Rep(U_q(g)) is E_2 in Cat.
- Modular (Part IV continued): Curved bar d^2 = kappa * omega_g at genus >= 1.
- E_3 (Parts V-VI = CLIMAX): E_3 = E_2 x E_1 by Dunn on Z(A). E_3-chiral requires a 3d HT theory. E_3-TOPOLOGICAL requires BOTH a 3d HT theory AND conformal vector at non-critical level.
- E_∞ (Part VI extension, UPGRADE-SWEEP 2026-04-16): **Iterated Sugawara ladder theorem** (`thm:e-infinity-topologization-ladder` in `chapters/connections/e_infinity_topologization.tex`). If A carries k inner stress tensors at spins {n_1 < … < n_k}, each with BRST primitive G^{(n_i)} satisfying T^{(n_i)} = [Q_tot, G^{(n_i)}], then Z^{der}_ch(A) is E_{k+2}-topological via Dunn: E_2-chiral (Deligne on Z^der_ch) ⊗_Dunn E_1-top(T^{(n_1)}) ⊗_Dunn … ⊗_Dunn E_1-top(T^{(n_k)}). Specializations: Virasoro (N=2) → E_3-top (Vol II climax as rung 1); principal W_N (T, W^{(3)}, …, W^{(N)}) → E_{N+1}-top; W_∞ → E_∞-top (Platonic endpoint). Antighosts G^{(n_i)} BRST-commute via higher-spin W-commutativity. Climax restatement: the true climax is E_∞-topological; E_3 is the first visible rung.
- **β_N closed form** (`thm:beta-N-closed-form-proved-all-N` in `chapters/theory/beta_N_closed_form_all_platonic.tex`, 2026-04-17): β_N = 12(H_N - 1) for all N ≥ 2, per-spin-s lane contribution β_s = 12/s. Rational (not integer) for N ≥ 5. Table: β_2 = 6, β_3 = 10, β_4 = 13, β_5 = 77/5, β_6 = 87/5. Rules out prior candidates (N+1)(N+2)/2 (gives 15 at N=4) and N²−N+4 (gives 16 at N=4). This is now the correct Banach-radius denominator ρ_* = |c|/β_A in the tempered-stratum bound; the Programme-Climax coupling inherits β_N from this closed form.
- **Curved-Dunn H²=0 at all genera** (`thm:curved-dunn-H2-vanishing-all-genera` in `chapters/theory/curved_dunn_higher_genus.tex`, 2026-04-16): modular-bootstrap-to-curved-Dunn bridge chain map Φ (`prop:modular-bootstrap-to-curved-dunn-bridge`) plus explicit genus-1 twisted Künneth via Gauss–Manin uncurving + Arakelov pairing (`prop:genus1-twisted-tensor-product`, resolves the former phantom label) plus Jimbo–Miwa irregular-singular KZB (`thm:irregular-singular-kzb-regularity`) close modular operad composition at generic non-integral level, all genera. FM67/FM88/FM91/FM92/FM192/FM215 closed.

### SC^{ch,top} Is Not E_3; SC Is The Generic Case

SC^{ch,top} is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply to coloured operads. E_3 requires topologization: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL (NOT E_3-chiral). Without conformal vector: stuck at SC^{ch,top}. At critical level k = -h^v: Sugawara undefined, topologization fails.

SC^{ch,top} is the GENERIC case. E_3-topological is a SPECIAL CASE requiring conformal vector. Most chiral algebras do NOT have conformal vector (critical level KM, E_1-chiral algebras, CY functor outputs). SC^{ch,top} must be understood as a first-class object with SEVEN redundant presentations (heptagon, post-UPGRADE-SWEEP 2026-04-16): operadic, Koszul dual, factorization, BV/BRST, convolution, Drinfeld-centre, derived-algebraic-geometry.

Status (updated 2026-04-13):
- thm:E3-topological-km: PROVED for affine KM V_k(g) at non-critical level (Costello-Li + Sugawara antighost).
- thm:E3-topological-DS: PROVED for ALL W-algebras via principal DS (Costello-Gaiotto + DS-transported antighost).
- thm:E3-topological-DS-general: PROVED for ALL W-algebras via ANY nilpotent (improvement term is always Cartan).
- thm:E3-topological-free-PVA: PROVED for ALL conformal VAs with freely-generated PVA associated graded (Khan-Zeng 3d Poisson sigma model + half-space BV).
- conj:E3-topological-general: CONJECTURAL only for non-free PVAs. Monster VOA V^♮: orbifold route identified (rem:monster-orbifold-route) — V_Leech^+ is E₃-top NOW (Z/2-invariants of E_n preserve E_n); full V^♮ conditional on orbifold BV of abelian CS (bounded, one paper).
- SC^{ch,top} heptagon (7 equivalent presentations, UPGRADE-SWEEP 2026-04-16): all seven edge theorems proved in `chapters/theory/sc_chtop_heptagon.tex` (1141 lines). Five classical faces (operadic / Koszul dual / factorization / BV-BRST / convolution) + face (6) Drinfeld-centre `Z(Rep_fact(A)) ≃ Rep_fact(Z^der_ch(A))^{E_2}` via categorified bar-cobar with half-braiding (AP-CY25) + face (7) derived-algebraic-geometry via PTVV on `Map(X×R_≥0, B SC-Alg)`. Edge 3↔4/4↔5 compositional qiso + Dunn assembly at `prop:heptagon-edge-34/45`. `thm:pentagon-factorization-convolution` survives as one edge (factorization ↔ convolution) via direct Koszul duality.
- Modular operad [RECONCILED 2026-04-17]: genus-0 product decomposition PROVED; π_1(Σ_g) PROVED for all affine KM at all genera (KZB flatness); COMPOSITION ASSOCIATIVITY PROVED at genus 0 all levels + all genera integrable levels (thm:affine-composition-associativity, KZ pentagon + KL regularity); generic non-integral level, genus ≥ 1 now CLOSED via thm:curved-dunn-H2-vanishing-all-genera + Jimbo-Miwa irregular-singular KZB framework (Stokes gap absorbed into irregular-singular monodromy classification). EQUIVARIANCE PROVED (prop:qt-equivariance, quasi-triangularity + YBE); UNITALITY PROVED all genera all shadow classes (prop:modular-operad-unitality). Heisenberg: PROVED (prop:heisenberg-full-modular-operad). Residual: associator specification (associator-dependent chain-level vs associator-independent formal question).
- Global triangle [RECONCILED 2026-04-17]: PROVED for classes G/L/C (boundary-linear, thm:global-triangle-boundary-linear). CLASS M CLOSED chain-level via thm:chd-ds-hochschild (\ClaimStatusProvedHere) + cor:universal-holography-class-M; four-step proof (Arakawa C_2-cofiniteness + HKR + HPL + DS-bar intertwining). Closes FM126/FM185/FM186/FM214.
- R=PT: Route D (Eberhardt shift-equation uniqueness) reduces gap to meromorphicity of bar-cobar R-matrix. Level-by-level rationality PROVED (prop:level-rationality-R-bar).

### The E_N Definition Ladder: Chiral vs Topological

E_N-CHIRAL != E_N-TOPOLOGICAL. Chiral depends on complex structure. Topological does not. The conformal vector enables TOPOLOGIZATION: chiral -> topological.

- E_1-chiral (def:e1-chiral-algebra): E_1-algebra in D-modules on X. Ordered OPE data.
- E_1-topological (def:e1-topological-algebra): E_1-algebra, no holomorphic dependence.
- E_2-chiral (def:E2-chiral-algebra): E_2 on Z^{der}_{ch}(A), NOT on A. R-matrix R(z) with spectral parameter.
- E_2-topological (def:E2-topological-algebra): requires conformal vector to topologize.
- E_3-chiral: E_2-chiral x E_1-top. The HT bulk. Requires a 3d HT theory.
- E_3-topological: E_2-top x E_1-top = full TQFT. Requires BOTH 3d HT theory AND conformal vector.

### Five Notions Of E_1-Chiral Algebra

(A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has its own derived center. (B)<->(C) via Drinfeld associator on the Koszul locus. NEVER conflate.

**WARNING (AP-CY63):** The chiral endomorphism operad End^{ch}_A in notion (B) is the ALGEBRAIC model (formal Laurent series). The BD chiral operad is the GEOMETRIC model (D-module maps). These are isomorphic after formal-disk restriction + coordinate choice (4-step bridge). Never write "the chiral endomorphism operad" without specifying BD (D-module, coordinate-free) or algebraic (formal Laurent series, coordinate-dependent). The bridge proposition assembling all 4 steps is ABSENT from the manuscript.

**WARNING (AP-CY67):** "Spectral parameters from FM_k(C)" is narration, not construction. End^ch_A has formal algebraic variables lambda_i. Their relationship to FM configuration spaces is mediated by the local-global identification theorem (a comparison, not a definition). Never write "spectral parameters from FM_k(C)"; write "spectral parameters from End^ch_A, identified with FM relative positions via comparison."

### Three Hochschild Theories

(i) Topological HH: E_1-algebra input -> E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input -> concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input -> E_2 with CY shifted Poisson. The geometry determines which Hochschild: curve X -> chiral, R -> topological, CY category -> categorical. NEVER conflate. Bare "Hochschild" MUST carry qualifier (chiral/topological/categorical) in non-historical contexts.

**WARNING (AP-CY62): Geometric vs algebraic ChirHoch model.** Two chain-level models exist for chiral Hochschild cochains: (a) geometric (FM compactification, log forms, 3-component differential), (b) algebraic (End^ch_A, Gerstenhaber bracket differential). Quasi-isomorphic for logarithmic chiral algebras. At genus >= 1, the geometric model carries curve-dependent data the algebraic model lacks. The comparison is only a REMARK (rem:comparison-geometric-hoch), not a named theorem. DANGEROUS CONFLATION SITES: any chain-level E_n claim about ChirHoch that does not specify the model.

**WARNING (AP-CY64): ChirHoch / HH* / H*_GF three-way confusion.** Do NOT claim "ChirHoch is finite while THH is infinite" -- HH*(Weyl) = 1-dimensional, even MORE concentrated. The genuine "fails to concentrate" object is H*_GF (Gel'fand-Fuchs continuous Lie cohomology, unbounded polynomial ring). The three coincide in cohomology for Koszul algebras but differ structurally (E_2 enrichment). At critical level k = -h^v, ChirHoch* becomes infinite (Feigin-Frenkel centre); HH* stays finite. This is the ONLY regime where dimensions genuinely differ. DANGEROUS CONFLATION SITES: hochschild.tex (the comparison theorems), any discussion of Theorem H scope.

**WARNING (AP-CY65): Spectral parameter provenance.** The spectral parameter z in R(z) comes from evaluation modules (representation theory), NOT from the center construction. The claim "topological Drinfeld center has no spectral parameters" is FALSE: the Yangian Y(g) HAS evaluation modules V_u in its (purely topological) Drinfeld center. The correct distinction: chiral bar DIFFERENTIAL is z-dependent; topological bar COPRODUCT is z-independent. DANGEROUS CONFLATION SITES: spectral-braiding-core.tex, ht_bulk_boundary_line_core.tex.

**WARNING (AP-CY66): BZFN ambient category is not tunable.** The two derived centres come from two DIFFERENT ALGEBRAS (A in D-mod, A_mode in Vect), NOT from applying BZFN in different ambient categories to the "same" algebra. S in the BZFN theorem is fixed. DANGEROUS CONFLATION SITES: hochschild.tex (Drinfeld center comparison), foundations_recast_draft.tex (BZFN discussion).

## The Operating Stack

This repo uses a six-layer Codex-native stack:

1. `AGENTS.md`
   Constitutional layer: invariant truths, task routing, convergence rules, and compaction-safe execution habits.
2. `.agents/skills/`
   Progressive-disclosure playbooks for rectification, formula verification, propagation, build triage, and frontier research.
3. `.codex/hooks.json`
   Deterministic guardrails for session routing, shell safety, verification nudges, and convergence enforcement.
4. `compute/audit/linear_read_notes.md`
   Persistent findings ledger. Failed checks and repaired claims belong here so the next compaction does not erase them.
5. The live truth surface
   `main.tex`, the active `\input` graph, the current dirty diff, build logs, compute/tests, and the narrowest executable slice that can falsify a claim.
6. The cross-volume bridge surface
   `~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`, `~/calabi-yau-quantum-groups`, plus still-misleading superseded split files, README surfaces, and bridge notes.

Architectural rules:

- keep the root instruction layer load-bearing and compaction-safe;
- put long repeated workflows into skills;
- put deterministic enforcement into hooks;
- let the audit ledger remember what chat history may forget;
- never bloat the constitutional layer with a second prose copy of every anti-pattern.

## Codex / GPT-5.4 Operating Stance

This file is optimized for Codex/GPT-5.4 mathematical work:

- default deliverable is a verified result, not a plan;
- read before editing;
- think and prompt in issue form: target, files, labels, conventions, acceptance checks, propagation surface;
- externalize only artifacts that survive compaction: exact hypotheses, theorem labels, grep targets, test names, open risks, next falsifier;
- keep reasoning effort at `medium` by default;
- escalate to `high` or `xhigh` only for proof surgery, nonlocal architecture, or stalled frontier synthesis after the loop itself has been sharpened;
- current chat context, prior agent prose, and repo lore are operational hints, not evidence.

Prompt-shape rule from practice: prompts work best when they look like a good GitHub issue rather than an inspirational essay. File paths, theorem labels, nearby diffs, convention notes, and explicit acceptance checks matter.

## GPT-5.4 Prompt Architecture

When composing prompts for Codex/GPT-5.4 delegated tasks (via skills, hooks, or direct invocation), use XML-tagged blocks to structure the prompt. Each block type serves a distinct cognitive function and helps the model allocate effort correctly.

### Block Types

- `<task>`: The concrete deliverable. One sentence. File paths, theorem labels, acceptance criteria. This is the only mandatory block.
- `<structured_output_contract>`: The exact output format expected. Use when the deliverable is structured (findings ledger, formula verification table, propagation report). Omit for free-form prose work.
- `<verification_loop>`: The falsification discipline. Which checks must pass before the task is declared done. Maps to the Resonance Loop steps 3-8. Include when the task involves mathematical claims.
- `<grounding_rules>`: Convention locks and anti-pattern reminders relevant to this specific task. Pull from the Core Failure Families or the AP catalogue. Include the narrowest relevant subset, not the entire catalogue.
- `<missing_context_gating>`: What to do when context is insufficient. Options: (a) read the specified file, (b) ask the user, (c) flag the gap and proceed with the weaker claim. Default is (a). Use (b) only for irreversible architecture decisions.
- `<completeness_contract>`: The propagation surface. After the core task, which other files, volumes, or surfaces must be checked for consistency. Maps to Resonance Loop step 7.
- `<dig_deeper_nudge>`: A prompt to escalate reasoning effort when the first pass yields ambiguous results. Include when the task is frontier synthesis or stalled audit work. Maps to the `high` or `xhigh` effort escalation.
- `<action_safety>`: Guardrails for destructive operations. Include when the task involves git operations, file deletion, large-scale rename, or cross-volume propagation. Maps to the Pre-Commit Gate.

### Usage Discipline

- Every delegated task gets at least `<task>`.
- Mathematical work gets `<task>` + `<verification_loop>` + `<grounding_rules>`.
- Audit and rectification get all blocks except `<dig_deeper_nudge>` (which is reserved for frontier stalls).
- NEVER stuff all blocks into every prompt. Unused blocks waste context and dilute signal.
- Block content should be terse: file paths, labels, grep targets, and one-sentence rules. Not prose essays.

## Task Intake - Prompt Geometry

Before any nontrivial work, lock these seven items:

1. the exact target file, theorem, formula, bridge, or live surface;
2. the task type: question-answering, audit, rectification, formula verification, build triage, or frontier synthesis;
3. the convention bridge: grading, shifts, OPE modes versus lambda-brackets, open/closed colors, genus and degree scope, Vol I versus Vol II versus Vol III normalization;
4. the live evidence surface: local file, nearby context, current diff, compute/tests, logs, and citations if any;
5. the narrowest falsifier that could kill the current claim;
6. the propagation surface if the claim changes;
7. the dirty collision surface in all touched repos.

If the user prompt is underspecified, infer the smallest defensible scope only after reading the live surface. Ask only when theorem status, convention choice, or irreversible architecture would change.

## Live Truth Surface

Prefer the live surface over archival memory:

- `main.tex`;
- the files currently `\input`'d;
- the current git diff;
- current build logs and generated warnings after a clean-enough rerun;
- the narrowest relevant compute modules and tests;
- superseded files only as collision surfaces when they still advertise the same claim;
- README, notes, and working notes only after the live manuscript surface is understood.

Default read order for nontrivial work:

1. target file;
2. local neighboring context;
3. active `\input` map from `main.tex`;
4. dirty diff;
5. relevant compute/tests or logs;
6. propagation surface across Vol I, Vol II, and Vol III when the claim is cross-volume.

### Dirty Collision Surface Snapshot (2026-04-13)

This snapshot is a prior, not permission to skip `git status`.

- Vol I: FRONTIER.md and CLAUDE.md updated with Vol II session results (page count 1,704pp, E_3-top hierarchy, SC^{ch,top} heptagon 7/7 edges post-UPGRADE-SWEEP 2026-04-16, modular operad breakthroughs). Compute surface unchanged.
- Vol II: CLEAN working tree. All worktrees pruned. 1,704pp, 0 errors. Session produced 17 theorems, FM58-FM68, AP176-AP182, 25 arXiv papers, ~3,000 lines new content across 20+ files. All committed.
- Vol III: ~693pp, ~34,000 tests, ~460 engines. 10 proofs at publication standard. Clean build: 0 undef refs, 0 undef cites. CY-A_3 PROVED (inf-cat). K3 abelian Yangian PROVED. ZTE T COMPUTED (exact rational, 35 tests). Shadow tower through m_8 (160 tests, S_8=4144720/19683). m_5 verified (G_5^{conn}=775/5184). Chiral volume conjecture FORMULATED (Abel-Jacobi period). Mock modular K3: THEOREM at d=2. CY-D dimension-stratified. CY-C abelian: C(g,q)=D(Y^+(g_{K3})). BKM Serre P_2=0 EXACT. E_8xE_8 (24,24) c=24. Root-of-unity N=2: 324 modules. Mathieu: all 25 M_24 classes. Incompatibility strengthened. 7-part structure + reading paths. AP-CY35-40 added.

Rule: rerun `git status --short` across every repo you touch before trusting any narrative summary. Dirty files are first-class collision surfaces, not background noise.

## Cross-Volume Anti-Pattern Scope

All shared anti-patterns remain live:

- Vol I `CLAUDE.md`: `AP1` through `AP141` + `B1`-`B85` for the shared formula, status, propagation, and workflow hazards. **B74-B85 (new, 2026-04-13):** formal-series/analytic confusion, chain-vs-cohomology level, abstract-machine non-sequiturs, stale classification lists, Khan-Zeng scope, orbifold route.
- Vol II `CLAUDE.md`: `V2-AP1` through `V2-AP39` + `FM58`-`FM68` for the local `E_1/E_infinity` hierarchy, lambda-bracket, standalone, and session-specific hazards.
- Vol III `CLAUDE.md`: `AP-CY1` through `AP-CY19` for center discipline, conditionality propagation, CY3 existence boundaries, and cross-volume bridge hazards.

`AGENTS.md` compresses them into a smaller family-level operating surface. If a task touches one of those domains, open the relevant `CLAUDE.md` slice and the matching skill before editing.

### Structural And SC Corrections (AP150-AP175, April 2026)

These APs arose from the SC adversarial audit and deep mathematical audit sessions. They are load-bearing for Vol II.

**Agent and structural confabulation (AP150-AP157):**

- AP150: Agent confabulation of mathematical structures. Agents stitch together disparate results from different categorical levels into claimed structures that do not exist. Counter: verify each arrow independently against .tex source.
- AP151: Convention clash within single file. Two definitions of hbar in one file cascade into wrong q (real instead of root of unity). Counter: grep all definitions of hbar after writing any formula involving it.
- AP152: "Ordered" ambiguity (labeled vs time-ordered). "Ordered configurations" on a curve means LABELED (non-coinvariant), not totally ordered. The bar complex is MIXED: holomorphic differential (from OPE on C) + topological coproduct (from deconcatenation along R). Counter: always specify which "ordered."
- AP153: E_3 scope inflation. E_3 via HDC requires B-bar^Sigma to exist as E_2-coalgebra. For E_inf-chiral (vertex algebras): exists, E_3 follows. For genuinely E_1-chiral (Yangians): B-bar^Sigma does NOT exist, only E_2 via classical Deligne. Counter: every E_3 claim must specify E_inf vs E_1 input.
- AP154: Two distinct E_3 structures. (a) Algebraic E_3: from HDC on E_2 bar coalgebra, no conformal vector needed. (b) Topological E_3: from Sugawara topologisation, requires conformal vector at non-critical level. These are NOT the same; identification conjectural. Counter: always specify which E_3.
- AP155: "New invariant" overclaiming. The ordered chiral homology framework recovers known invariants (KZB from Bernard 1988, elliptic R-matrix from Felder 1994). Novelty is ARCHITECTURAL, not COMPUTATIONAL. Counter: check Bernard/Felder/Etingof-Varchenko/Calaque-Enriquez-Etingof.
- AP156: Quasi-periodicity convention for wp_1. Two functions both called wp_1: theta_1'/theta_1 (periodic under z->z+1) vs Weierstrass zeta_tau (quasi-periodic under both). Different monodromy formulas. Counter: always specify which function.
- AP157: Degeneration-dependent "invariants." A formula computed from a specific degeneration is NOT an invariant unless degeneration-independence is proved. Counter: always specify degeneration type and state whether independence is proved.

**SC^{ch,top} corrections (AP158-AP165):**

- AP158: SC^{ch,top} != E_3. SC is two-coloured with directionality. Dunn does NOT apply. E_3 requires topologization: SC^{ch,top} + conformal vector = E_3-TOPOLOGICAL (NOT E_3-chiral). The conformal vector KILLS the chiral direction. Without conformal vector: stuck at SC^{ch,top}. At critical level: Sugawara undefined, topologization fails.
- AP159: Four Yangian types on different geometric spaces. (1) Classical Y_hbar(g): E_1-topological on R. (2) dg-shifted Y^{dg}_hbar(g): at point/formal disk. (3) Chiral Y(g)^{ch}: E_1-chiral on curve X. (4) Spectral: factorization on A^1_u. Conflating any two is a type error.
- AP160: Three Hochschild theories. (i) Topological HH: E_1 -> E_2. (ii) Chiral ChirHoch: E_inf-chiral -> {0,1,2}. (iii) Categorical HH: dg category -> E_2 with CY shifted Poisson. Bare "Hochschild" MUST carry qualifier.
- AP161: Five notions of E_1-chiral algebra are NOT interchangeable. (A)-(E) each have own derived center. (B)<->(C) on Koszul locus only. Counter: specify which notion.
- AP162: E_3 requires conformal vector. NEVER claim E_3 without stating: (a) conformal vector exists, (b) level non-critical, (c) T(z) Q-exact in bulk. Status: PROVED for affine KM; CONJECTURAL for general. Proof cohomological; class M chain-level open.
- AP163: "Lives on R x C" unjustified for E_1-chiral algebras. The SC bar complex is a coalgebra over a PRODUCT operad, NOT a factorization algebra on R x C. Counter: passage to factorization algebra requires chiral Deligne-Tamarkin principle.
- AP164: Chiral Gerstenhaber != topological Gerstenhaber. Chiral bracket uses OPE residues on FM_k(C). Topological uses little 2-disks. Agree for E_inf via formality; diverge for E_1. Counter: always specify "chiral" or "topological."
- AP165: B(A) is NOT an SC^{ch,top}-coalgebra. B(A) is E_1 chiral coassociative. SC^{ch,top} emerges in the derived center pair (C^bullet_{ch}(A,A), A). FORBIDDEN: "B(A) coalgebra over SC", "bar presents Swiss-cheese", "bar differential is closed color", "bar coproduct is open color."

**SC adversarial audit corrections (AP166-AP175):**

- AP166: SC^{ch,top} is NOT Koszul self-dual. SC^! = (Lie^c, Ass^c, shuffle-mixed) with closed dim = (n-1)!. SC = (Com, Ass) with closed dim = 1. MANIFESTLY DIFFERENT. FORBIDDEN: "(SC^{ch,top})^! ~ SC^{ch,top}." CORRECT: Koszul duality exchanges Com <-> Lie while preserving Ass; the duality functor is an involution.
- AP167: Topologization scope. thm:topologization PROVED for affine KM V_k(g) at non-critical level. General: CONJECTURAL. Proof cohomological; class M chain-level open. Counter: every topologization reference must carry scope qualifier.
- AP168: E_3 is TOPOLOGICAL, not chiral. Sugawara makes C-translations Q-exact, complex structure irrelevant in cohomology, two SC colors collapse, E_2^{hol} x E_1^{top} -> E_3^{top} via Dunn. FORBIDDEN: "E_3-chiral." CORRECT: "E_3-topological."
- AP169: SC^{ch,top} is the GENERIC case; E_3 is special. Most chiral algebras lack conformal vector. SC^{ch,top} is the FINAL answer for these; treat as first-class object.
- AP170: Two incompatible Yangian definitions. def:e1-chiral-yangian (weaker) vs def:chiral-yangian-datum (stronger, four axioms). Equivalence OPEN.
- AP171: Associator dependence dichotomy. Cohomological derived center = associator-independent. Cochain-level = associator-dependent. Bar-side invariants (kappa, shadow tower) associator-FREE.
- AP172: A^! is an SC^!-algebra, NOT an SC-algebra. Closed = Lie (Sklyanin bracket), Open = Ass (Yangian product). This is (Lie, Ass)-algebra, not (Com, Ass)-algebra. FORBIDDEN: "A^! is an SC-algebra."
- AP173: Yangian derived center not computed. Z^{der}_{ch}(Y(g)^{ch}) not computed anywhere. Predicted infinite-dimensional. For E_1 input: only E_2, not E_3 (B^Sigma does not exist).
- AP174: Chiral QG equivalence scope. Proved abstractly on Koszul locus. Concrete verification: sl_2 Yangian and affine KM only. Elliptic partial; toroidal absent. FORBIDDEN: "equivalence for all four families."
- AP175: Pentagon of equivalences. UPDATED 2026-04-12 (all 10/10 pairwise edges closed via thm:pentagon-factorization-convolution, direct Koszul duality, bypassing operadic Künneth). **UPGRADED to heptagon 2026-04-16** (sc_chtop_heptagon.tex, 1141 lines): face (6) Drinfeld-centre Z(Rep_fact(A)) ≃ Rep_fact(Z^der_ch(A))^{E_2} via categorified bar-cobar with half-braiding (AP-CY25); face (7) derived-algebraic-geometry via PTVV on Map(X×R_≥0, B SC-Alg); compositional qiso + Dunn assembly at prop:heptagon-edge-34/45. All 7 presentations equivalent via the operadic hub; seven edge theorems provide independent verification for each presentation. "Pentagon" stands as the five-face chain-level result; "heptagon" is the full Platonic form post-UPGRADE-SWEEP.

**Session 2026-04-12 Corrections (AP176-AP182):**

- AP176: E₁ fiber integration uses flatness, NOT Cauchy. The quasi-isomorphism B^{D*}(A) → B^{S^1}(A) holds for E₁ algebras by FLATNESS of the shifted KZ connection + homotopy invariance of monodromy (topological argument). Cauchy's theorem does not apply to formal Laurent series. The retraction ρ_t is non-holomorphic and cannot appear in the proof. CORRECT argument: flat connection → holonomy depends only on homotopy class → all circles in C* are homotopic → Mon(R) radius-independent.
- AP177: lem:operadic-kunneth chain-level decomposition is WRONG at chain level. The bar differential of SC^{ch,top}_mix has cross-terms d_mix from open edge contractions between mixed vertices (the map μ₁ combining closed inputs). The CORRECT statement is: the decomposition holds on the ASSOCIATED GRADED with respect to the closed-input-excess filtration. The pentagon theorem does NOT depend on this lemma (direct Koszul duality suffices).
- AP178: Modular operad status [RECONCILED 2026-04-17 vs CLAUDE.md FM68 + HEAL §"The four irreducible opens ALL CLOSED"]. thm:modular-bar proves D²=0 for the ABSTRACT modular bar datum. Concrete operadic associativity: PROVED genus 0 all levels + all genera integrable (thm:affine-composition-associativity, KZ pentagon + KL regularity); PROVED genus ≥ 2 generic non-integral levels via thm:curved-dunn-H2-vanishing-all-genera + Jimbo-Miwa irregular-singular KZB (curved-Dunn bridge chain map Φ closes cross-genus MC equation unconditionally). Equivariance PROVED (prop:qt-equivariance); unitality PROVED all genera (prop:modular-operad-unitality); π₁ well-definedness PROVED (prop:affine-modular-operad-all-genera). Sole residual technical condition: specifying the Drinfeld associator Φ (associator-dependent chain-level; associator-independent formulation open as a formal question).
- AP179: Khan-Zeng covers ALL freely-generated PVAs. For any conformal VA whose Li-filtration associated graded is a freely-generated PVA, the Khan-Zeng 3d Poisson sigma model provides the 3d HT bulk, and the conformal vector upgrades to fully topological. This covers ALL standard families (G, L, C, M). conj:E3-topological-general is open ONLY for non-freely-generated VAs (Monster VOA).
- AP180: Eberhardt Route D for R=PT. Eberhardt (arXiv:2309.11540) proves uniqueness of the fusion kernel via difference Galois theory for b² irrational. The bar-cobar R-matrix satisfies the same shift equations (pentagon + degenerate eigenvalues, both proved). Gap reduces to: meromorphicity of bar-cobar R-matrix in external momenta. Level-by-level rationality PROVED (prop:level-rationality-R-bar).
- AP181: Global triangle [RECONCILED 2026-04-17 vs CLAUDE.md Bridge table + HEAL §661]. PROVED for classes G/L/C (thm:global-triangle-boundary-linear). CLASS M CLOSED at chain level via thm:chd-ds-hochschild (\ClaimStatusProvedHere, chiral_higher_deligne.tex:652-654) plus cor:universal-holography-class-M — four-step proof: (1) Arakawa C_2-cofiniteness, (2) HKR identification both sides, (3) HPL transfer through DS strong deformation retract, (4) DS-bar intertwining from Vol I thm:ds-koszul-intertwine. Closes FM126/FM185/FM186/FM214 unconditionally on principal and hook-type nilpotents at generic k ≠ -h^v.
- AP182: Curved Dunn three-level refinement [RECONCILED 2026-04-17 vs CLAUDE.md HEAL §661]. Level 1 (genus 0): PROVED (prop:genus0-product-decomposition). Level 2 (obstruction theory): obstruction in H²(Hom(B(E₁^tr), gr^g(B_mod(SC)))) VANISHES at all genera via thm:curved-dunn-H2-vanishing-all-genera (\ClaimStatusProvedHere, curved_dunn_higher_genus.tex:375-377) through modular-bootstrap-to-curved-Dunn bridge chain map Φ (prop:modular-bootstrap-to-curved-dunn-bridge). Level 3 (twisted Künneth): genus-1 PROVED (prop:genus1-twisted-tensor-product); genus ≥ 2 PROVED through H²=0 bridge + Jimbo-Miwa irregular-singular KZB framework. Full genus tower CLOSED.

## Cross-Volume: Vol III Final Session Impact (2026-04-13, updated with FINAL documentation wave)

Vol III deployed ~230 agents through the comprehensive wave (cumulative: ~693pp, ~34,000 tests, ~460 engines, 10 proofs at publication standard, clean build). Key Vol II-relevant results:

- **E_1-chiral bialgebra verified at all spins for K3 Yangian**: axioms (H1)-(H5) verified with 80+ tests across e1_chiral_bialgebra_engine, chiral_coproduct_spin3_engine, wilson_line_coproduct_engine, sl2_matrix_lax_engine, and k3_nonabelian_coproduct. Universal coproduct from Miura: Delta_z(e_s) = sum C(N_R-b,k) z^k e_a^L*e_b^R. Coassociativity trivial via Miura multiplicativity. Averaging-forgets-Hopf PROVED. Vol II cross-ref: rem:e1-chiral-bialgebra-vol3 (foundations_recast_draft.tex).
- **Swiss-cheese derived inf-categorical formulation**: the factorization tensor product ⊗_{E_1,z} = colim over ordered configs is NOT symmetric, IS strictly associative (ordered config space contractible). np.kron = E_inf quotient kills Hopf (AP-CY23). This is the concrete E_1 content of the SC^{ch,top} datum.
- **Wilson lines = stratified FH defects**: Wilson line coproduct engine (30 tests) implements Delta_z on Wilson line observables, connecting Vol II's abstract SC^{ch,top} defect language to 5d/6d hCS constructions.
- **Shadow tower = A_inf coproduct corrections**: S_k = coefficient of delta^{(k)}. Shadow-Feynman dictionary: L-loop = S_{L+1}. Class M Borel summability PROVED.
- **ZTE failure**: factored S=RRR fails ZTE at O(kappa^2). E_3 corrections exist (rank 35/36). Connects to A_inf coproduct via shadow tower.
- **E_2 -> E_3 promotion**: derived center HH*(B,B) via higher Deligne, NOT iterated Drinfeld center. 3d->5d->6d = E_1->E_2->E_3.

**FINAL documentation wave additions (Vol II-relevant):**
- **Chain-level incompatibility theorem**: mu_3 != 0 forces mu_2 = 0 on augmentation. Explains why E_1-chiral bialgebra lives on B^{ord}(A), reinforcing the Vol II SC^{ch,top} architecture (B(A) is E_1 coalgebra, SC emerges on derived center).
- **CY-B at d=3 (131 tests)**: E_1-chiral Koszul duality (inducing E_2 on Drinfeld center) extended via inf-cat CY-A_3. At d=3 A is E_1; the E_2 braided equivalence lives on Z(Rep^{E_1}(A)). The bar-cobar adjunction on CY_3 categories connects to Vol II's abstract SC^{ch,top} bar-cobar framework.
- **kappa_ch deep mechanism**: Hodge-filtered supertrace str_{F^0}(q^{L_0}). At d=2 coincides with chi(O_X)/2 (Serre duality). At d=3 diverges. Vol II's modular characteristic D is the d=2 case.
- **CY-D deep issue**: chi(O_{K3xE}) = 0 != 3 = kappa_ch. Target-space anomaly (chi) != worldsheet anomaly (kappa_ch) at d=3. This does NOT affect Vol II (which works at d=2 where they agree).

## Claude-To-Codex Pdegree Map

Claude-side workflows in this repo must have an explicit Codex-side home.

### Command / Skill parity

- Claude `/audit` -> Codex `$vol2-deep-audit`
- Claude `/rectify` -> Codex `$vol2-beilinson-rectification`
- Claude `/chriss-ginzburg-rectify` -> Codex `$vol2-chriss-ginzburg-rectify`
- Claude `/verify` -> Codex `$vol2-formula-verification`
- Claude `/propagate` -> Codex `$vol2-cross-volume-propagation`
- Claude `/build` -> Codex `$vol2-build-surface`
- Claude `/compute-engine` -> Codex `$vol2-compute-engine`
- Claude `/research-swarm` -> Codex `$vol2-research-swarm`
- Claude master/route architecture specs -> Codex `$vol2-six-layer-architecture`

### Hook parity

- Claude pre-commit reminder hook -> Codex `.codex/hooks/pre_bash_guard.sh`
- Claude Beilinson post-edit gate -> Codex `.codex/hooks/post_bash_review.sh` plus the Post-Edit Gates in this file
- Claude convergence gate -> Codex `.codex/hooks/stop_convergence.sh`
- Claude prompt routing by slash-command intent -> Codex `.codex/hooks/user_prompt_router.sh`
- Claude session context injection -> Codex `.codex/hooks/session_start_context.sh`

### Runtime limitation

Current Codex repo hooks can mechanically intercept Bash tools, but not every non-Bash edit event that Claude can annotate. Therefore every Claude-side hook must exist at two Codex layers:

1. mechanically where Codex hooks can enforce it;
2. cognitively in `AGENTS.md` and the matching repo skill where runtime enforcement is not yet available.

Do not treat this as optional duplication. It is how parity is achieved.

## Truth Hierarchy

The order of trust in this repo is:

1. a local proof whose nontrivial steps can be named and checked;
2. an exact citation to a result that really states the needed claim under the needed hypotheses;
3. an independent computation or test that genuinely verifies the mathematical statement being used;
4. cross-surface consistency between theorem, proof, example, compute layer, and build/test output;
5. prose explanation.

Not evidence:

- confidence;
- repetition across files;
- a claim-status macro by itself;
- inheritance from older drafts;
- README or notes being more ambitious than `.tex`;
- a previous agent summary that was not rechecked locally;
- a generated PDF when the source, labels, or logs have not been reread.

### Status Ledger

Every substantial statement must land in one of these buckets:

- proved here;
- proved elsewhere;
- consequence of `Definition def:log-SC-algebra`;
- conditional on `Theorem thm:physics-bridge`;
- conjectural;
- heuristic;
- open.

Rules:

- theorem/proposition/lemma/corollary environments are for proof-bearing claims only;
- conjectural or heuristic material belongs in matching environments, not theorem-like ones;
- if a statement changes, update the theorem environment, claim-status tag, nearby proof or evidence remark, and downstream advertisements in the same session;
- README, notes, and summaries may not outclaim the live manuscript.

## Mode Routing

The always-on layer is small. Deep workflows are triggered.

### Mode 1 - Default Research Mode

Use for ordinary manuscript, proof, notation, and compute tasks.

Loop:

1. identify the exact target;
2. read the local source before editing;
3. inspect the live diff and nearby dependencies;
4. make the smallest correction that can be defended;
5. run the narrowest verification that can falsify the change;
6. propagate any shared formula or status correction;
7. stop only after the modified surface is coherent.

### Mode 2 - Deep Beilinson Rectification

Trigger when the user asks to audit, rectify, tighten, fortify, converge, or pressure-test a chapter, theorem, appendix, or live surface.

Use:

- `$vol2-beilinson-rectification`

### Mode 3 - Formula Verification

Trigger when the user asks whether a formula, coefficient, invariant, table entry, or test oracle is correct.

Use:

- `$vol2-formula-verification`

### Mode 4 - Cross-Volume Propagation Sweep

Trigger whenever you change a shared formula, theorem status, definition, notation, convention, summary sentence, or hardcoded expected value.

Use:

- `$vol2-cross-volume-propagation`

### Mode 5 - Build Surface Triage

Trigger when the question depends on build logs, warning classification, `make fast`, or targeted `pytest`.

Use:

- `$vol2-build-surface`

### Mode 6 - Frontier Research

Trigger for new theorems, new definitions, research programmes, or speculative architectural synthesis.

Use:

- `$vol2-frontier-research`

## The Resonance Loop

For any nontrivial task, run this loop until convergence.

### 0. Scope Lock

Identify:

- the exact target statement or surface;
- labels, hypotheses, and dependencies;
- whether the task is question-answering, audit, rectification, formula verification, build triage, or frontier synthesis.

Start with a short progress update naming the target and first verification step. For substantial work, register the loop in `update_plan`.

### 1. Invariant Lock

Before trusting any local argument, lock the conventions:

- grading and shifts;
- bar/cobar/Koszul-dual object identity;
- open/closed color directionality;
- lambda-bracket versus OPE-mode conventions;
- genus/degree/filtration/family scope;
- Vol I versus Vol II versus Vol III terminology.

### 2. Read The Surface

Read the live target before editing anything. Never patch by pattern alone.

### 3. RED Pass

Attack logic and mathematics:

- hidden hypotheses;
- circularity;
- sign or degree errors;
- formula drift;
- overclaimed biconditionals;
- false identifications;
- unconstructed objects masquerading as built objects.

### 4. BLUE Pass

Attack consistency:

- theorem/proof mismatch;
- label or dependency drift;
- stale status prose;
- duplicate formulations;
- build-log collisions;
- compute/manuscript disagreement;
- propagation failures;
- README or note surfaces stronger than the theorem surface.

### 5. GREEN Pass

Attack structural gaps:

- missing definitions;
- dangling references;
- unproved lemmas;
- objects used before axiomatization;
- places where a weaker but true statement should replace a stronger false one.

### 6. Patch In Dependency Order

Fix `CRITICAL` and `SERIOUS` findings first, then `MODERATE`.

For each fix:

1. reread the local context;
2. recompute or re-derive independently;
3. make the smallest truthful edit that closes the bug;
4. immediately search for downstream advertisements of the old claim.

### 7. Propagate

After any mathematical or status change:

- grep the active Vol II surface;
- grep superseded split files if they still advertise the same statement;
- grep `~/chiral-bar-cobar`;
- grep `~/calabi-yau-quantum-groups` when the bridge is genuinely cross-volume;
- update compute/tests, README, or notes if the old claim is still being sold there.

### 8. Verify

Run the narrowest verification that can actually falsify the change:

- targeted `pytest`;
- targeted grep;
- label or reference check;
- log inspection;
- `make fast` for load-bearing manuscript rewrites;
- broader build/test only when the local slice passes and scope demands it.

### 9. Reflect And Externalize

After each major phase, externalize the state that must survive compaction:

- target;
- best current status;
- open risk;
- next falsifier.

Record nontrivial findings in `compute/audit/linear_read_notes.md` with date, target, severity, class, location, issue, fix, and status.

### 10. Re-Audit

Hostilely reread your own rewrite. This is not celebration. It is attempted refutation of the patch you just made.

### 11. Convergence

A task is converged only when:

- no actionable finding at severity `MODERATE` or above remains on the modified surface; and
- the narrowest relevant verification passes.

Rectification sessions end only with:

- `CONVERGED`
- `BLOCKED: <one-sentence blocker>`

## Cross-Volume Empirical Priors (Last 100 Commits Per Repo)

The recent history across all three volumes gives strong priors about where Codex most often fails:

1. environment/status drift is systemic:
   `AP40`, `AP4`, `AP125`, `V2-AP31`, `AP-CY6`, and `AP-CY14` keep recurring. The model overpromotes, leaves proofs under conjectures, or forgets to relabel.
2. convention-paste errors are the second major cluster:
   `AP126`, `V2-AP34`, `AP44`, `AP45`, `AP46`, `AP49`, and `AP113` recur across manuscript and compute layers.
3. scope and qualifier drift persists:
   `AP32`, `V2-AP26`, `V2-AP30`, `AP47`, `AP48`, `AP-CY11`, `AP-CY13`, and `AP-CY15` show that local proofs are repeatedly sold as global theorems.
4. propagation failures remain common:
   fixes land in one theorem while intros, frontier chapters, superseded split files, README, notes, docstrings, or tests still sell the old statement.
5. engine/test false corroboration is real:
   `AP128` and `V2-AP28` recur because the engine and test inherit the same wrong derivation.
6. artifact leakage and build noise are not harmless:
   `V2-AP32`, `V2-AP33`, stale PDFs/logs, and standalone-document commands inside chapter inputs recur in the last-100-commit archaeology.
7. prose slop and connective drift correlate with truth drift:
   `V2-AP29`, `V2-AP35`, and `AP121` are not cosmetic cleanup; they often mark overclaim, stale reasoning, or hidden assumptions.
8. current dirty worktrees matter:
   Vol I is compute-heavy right now, Vol II is concentrated in perturbative finiteness, and Vol III is concentrated in CY3 compute/test plus bridge exposition. Read these before making cross-volume claims.

Treat these as empirical priors, not curiosities.

## Core Failure Families

The large anti-pattern register compresses into seven load-bearing families. Think in families first, not isolated bugs.

### Family O - Object Conflation

If two objects coincide in a special case, assume they diverge in the general case until proved otherwise.

Rules:

- there are at least five distinct objects in play: `A`, `B(A)`, `A^i`, `A^!`, and `Z^{der}_{ch}(A)`;
- `Omega(B(A)) = A` is inversion; it does not produce `A^!`;
- `A^!` is read by Verdier/factorization duality, not by cobar inversion;
- the bar complex is not the bulk algebra;
- the primitive datum is the open-sector factorization dg-category; a boundary algebra is a chart;
- the ordered bar, symmetric bar, and Francis-Gaitsgory bar are different complexes;
- Drinfeld center and derived/chiral center are distinct constructions unless hypotheses are stated.

### Family S - Scope And Status Inflation

If a theorem is proved on a lane, do not silently upgrade it to all lanes.

Rules:

- theorem environment must match claim status;
- proof-after-conjecture is forbidden;
- evaluation-generated core is not the full category;
- bulk `simeq` derived center is rigorous on the boundary-linear exact lane, not automatically global;
- genus-0 or genus-1 statements are not all-genera statements unless explicitly proved;
- unconstructed CY3 objects remain conditional downstream if the proof chain touches them;
- README and notes may not claim stronger status than the live `.tex`;
- conditionality propagates through downstream results and summaries.

### Family C - Convention Drift

Most manuscript damage comes from silent convention changes.

Rules:

- affine `r`-matrices keep their level prefix: check `k = 0 -> r = 0`;
- Vol II lambda-brackets use divided powers;
- desuspension lowers degree;
- `d_bar^2 = 0` always; curved structure is the fiberwise or genuswise statement, not the bar differential itself;
- `kappa` is family-specific, and in Vol III the subscript is mandatory;
- `eta(q)` includes `q^(1/24)`;
- pole order is not chromatic height;
- Vol I uses OPE modes, Vol II uses lambda-brackets, Vol III may use motivic or categorical normalizations;
- never paste formulas across volumes without explicit conversion.

### Family P - Propagation Failure

Local truth does not excuse global drift.

Rules:

- after any load-bearing change, grep active Vol II chapters, appendices, superseded split files, Vol I, Vol III, README, notes, and compute/tests as relevant;
- label renames, theorem downgrades, and terminology migrations are atomic only if every still-live `\ref`, summary, and hardcoded expectation is updated in the same session;
- hardcoded Part numbers are forbidden; use `\ref{part:...}`;
- docstrings and hardcoded expected values are part of the truth surface, not aftercare.

### Family D - Dirty-Surface Blindness

The active dirty worktree is where collisions actually happen.

Rules:

- read dirty files before editing around them;
- generated PDFs, `.log`, `.aux`, and stale warnings are collision surfaces, not mathematical evidence;
- chapter files `\input`'d into `main.tex` must not contain standalone-document commands such as `\title`, `\author`, `\date`, `\begin{abstract}`, or `\tableofcontents`;
- `RECTIFICATION-FLAG` must not become permanent debt; resolve it or leave an explicit tracked TODO with owner;
- after correcting a formula, audit nearby `therefore`, `hence`, and `it follows` within a few lines to catch stale logic.

### Family E - E_infinity / E_1 / Center Confusion

Do not let a parenthetical gloss or a literature reflex smuggle in false restrictions.

Rules:

- all ordinary vertex algebras are `E_infinity`-chiral, even with OPE poles;
- `E_1` versus `E_infinity` is about locality and provenance, not merely `R(z) != tau`;
- open-to-closed in the Swiss-cheese picture is empty;
- PVA is a classical or cohomological shadow, not the same object as `P_infinity`-chiral algebra;
- the `R`-matrix comes from bulk-boundary composition, not automatically from a universal quantum-group `R`;
- CoHA is associative, not automatically an `E_1`-chiral algebra or the `E_1` sector of an unconstructed object;
- Drinfeld center and derived center are not interchangeable.

### Family W - Workflow Self-Deception

The agent layer can amplify error faster than the mathematics layer.

Rules:

- never patch before reading;
- never batch-propagate an unverified correction;
- never trust a previous agent summary over the live repo conventions;
- engine and test sharing the same wrong derivation is not independent evidence;
- plans are scaffolds, not deliverables;
- long summaries, elegant slogans, and clean prose are not proof;
- do not let compaction erase open risks: keep the audit ledger and explicit handoff state current.

### Family F - Vol II Failure Modes (FM40-FM57) And Meta-Patterns (MP1-MP6)

These are CRITICAL Vol II-specific errors from the 2026-04-12 session (55+ agents). They compress into three clusters: categorical level errors, factorisation/coproduct conflation, and E_3 overclaiming.

**Categorical level errors (the most dangerous class):**

- FM40: Dunn on A instead of Z(A). Applied "E_1 x E_1 = E_2" to the boundary algebra A. WRONG. A is E_1. Dunn applies to Z(A) (bulk/derived center) or Mod_A (module category). Counter: before ANY Dunn claim, verify the target is Z(A) or Mod_A, NEVER A.
- FM41: R-matrix makes A into E_2. WRONG. R-matrix makes Mod_A braided (E_2 in Cat). A remains E_1. Quantum groups U_q(g) are E_1; Rep(U_q(g)) is E_2 in Cat. Counter: E_2 lives one categorical level up from A.
- FM42: YBE = A_inf associativity. WRONG. YBE is the COMPATIBILITY condition between two E_1 structures (braiding coherence). A_inf associativity is coherence of a SINGLE E_1. Counter: separate associativity (single E_1) from compatibility (interaction of two E_1s).

**Factorisation homology errors:**

- FM43: Bar = factorisation homology of R. WRONG. int_R A = A (trivial). B(A) = k otimes_A^L k = int_{[0,1]}^{k,k} A (interval with augmentation boundary). Counter: factorisation homology of a contractible manifold without boundary is the algebra itself.
- FM44: Bar complex = "chain model for factorisation cohomology." Imprecise. B(A) is a factorisation COALGEBRA. Chiral homology is derived global sections of this coalgebra, a separate non-trivial operation. Counter: never conflate local (coalgebra) with global (cohomology).

**Coproduct conflation errors:**

- FM45: Deconcatenation = chiral coproduct. WRONG. Deconcatenation is the structural cofree coalgebra coproduct on B(A). The Hopf-type chiral coproduct Delta: A -> A otimes A is independent structure on A. Different coproducts on different objects. Counter: always specify WHICH coproduct and on WHICH object.
- FM46: r-matrix sufficient for quantum group. WRONG. r-matrix is the classical shadow. Full quantum group needs: coproduct + full R(z) + quasi-triangularity + antipode. The coproduct is NOT visible in the shadow tower. Counter: "r-matrix is necessary but not sufficient."

**E_3 overclaiming errors:**

- FM47: E_inf -> E_3-chiral automatic. WRONG. E_2 on Z(A) is automatic (Deligne conjecture). E_3-chiral requires a 3d HT theory whose boundary is A. For KM: proved (holomorphic CS). For GENERAL vertex algebras: requires quantizing the Poisson vertex model (hard open work). Counter: nothing beyond E_2 on Z(A) is automatic.
- FM48: E_3-topological from E_inf alone. WRONG. Conformal vector is ADDITIONAL STRUCTURE. E_3-topological requires BOTH a 3d HT theory AND a conformal vector at non-critical level. Counter: E_3-top needs two independent inputs.

**Notation errors:**

- FM49: Y_z^hbar notation. Changed Y_hbar to Y_z^hbar across 531 occurrences. WRONG. The algebra Y_hbar(g) does not depend on z. The spectral parameter z lives on Delta_z, R(z), T(z), ev_z, not on the algebra itself. Reverted. Counter: NEVER put the spectral parameter in the algebra symbol.
- FM50: Ordered configuration spaces = geometric ordering on R subset X. WRONG. The E_1 ordering is ALGEBRAIC (operations depend on sequence). It does NOT require embedding R into X. Counter: the E_1 structure is operadic/algebraic, not geometric.

**Structural pattern errors:**

- FM51: "Emergent third dimension" from bar degree. WRONG. Bar degree is a grading on a chain complex. An E_1 structure requires operations and coherences. A grading provides none. Counter: a grading is not an operadic structure.
- FM52: Within-surface SC = holographic bulk-boundary. WRONG. Within-surface SC (R subset C) governs restriction to a real locus. Holographic bulk-boundary goes through derived center (Hochschild). Counter: SC governs within-surface; holography goes through Hochschild.
- FM53: Two "independent" E_1 structures. WRONG. Within-surface E_1 and transverse E_1 are Koszul dual through the Hom functor: C*(A,A) = Hom(B(A), A). Counter: Koszul dual, not independent.
- FM54: Spectral R(z) = categorical braiding. WRONG. Spectral R-matrix R(z) (family of maps with parameter) differs from E_2 braiding from Dunn (single natural transformation, no parameter). Counter: spectral != categorical; the relationship needs a theorem.

**Additional structural errors:**

- FM55: RT invariants = unordered E_1 chiral homology. WRONG. RT invariants arise from E_inf factorisation homology (CFG E_3 trace on BV-quantised CS). Counter: RT = E_inf factorisation homology trace, NOT E_1 ordered bar complex.
- FM56: "Symmetric monoidal category of chiral algebras." WRONG. Chiral algebras form a PSEUDO-TENSOR category (BD), NOT a symmetric monoidal category. Counter: say "D-modules on X" or "factorisation algebras on X."
- FM57: Costello-Gaiotto already provides 3d HT for Virasoro. The gap for Virasoro E_3-chiral is NOT "quantize the PV model" but the specific BRST identity T_DS = [Q_tot, G'] in the DS-modified BV complex. Counter: cite Costello-Gaiotto for the 3d HT theory; state the gap as the BRST identity.

**Meta-patterns (from the error catalogue):**

- MP1: CATEGORICAL LEVEL CHECK. Before any E_n or Dunn claim, verify: which categorical level? Algebra (E_1) / Module category (E_2 in Cat) / Center (E_2). NEVER skip.
- MP2: AUTOMATIC vs REQUIRES CONSTRUCTION. E_2 on Z(A) is automatic (Deligne). Everything above E_2 requires a specific construction. Never say "automatic" above E_2.
- MP3: DISTINGUISH SIMILAR OBJECTS. When two objects look similar (deconcatenation vs chiral coproduct, spectral vs categorical braiding), EXPLICITLY NAME AND DISTINGUISH before using either.
- MP4: NOTATION CHANGES NEED MATHEMATICAL JUSTIFICATION. Before ANY bulk notation change: verify mathematically correct, consistent with literature, no conflict with existing usage.
- MP5: GRADING != OPERADIC STRUCTURE. A filtration/grading on a complex is NOT an E_n structure. An E_n structure requires operations parametrised by configuration spaces.
- MP6: SINGLE vs PAIR. Before any claim that two structures interact (Dunn, braiding, compatibility), verify: intrinsic to ONE structure, or governing how TWO structures compose? YBE governs interaction of two E_1s. A_inf governs a single E_1.

## Multi-Path Verification Mandate

Every computational claim, formula, coefficient, table entry, theorem advertisement, or hardcoded expected value should be backed by multiple genuinely independent paths whenever feasible.

For load-bearing mathematics in this repo, the preferred triangle is:

1. direct local derivation or proof tracing;
2. a structurally different check;
3. an executable or searchable witness.

Recommended path taxonomy:

1. direct computation from the definition;
2. structurally different equivalent formula;
3. limiting or degenerate case;
4. symmetry, duality, or reduction;
5. cross-family consistency or functoriality;
6. literature comparison with convention check;
7. degree, weight, sign, or units analysis;
8. numerical evaluation at sample parameters;
9. operadic or factorization consistency;
10. descent consistency to the PVA, classical shadow, or categorical shadow.

Minimum standard:

- manuscript formula: at least three paths when the claim is load-bearing;
- compute test: at least two methods in code or one method plus one structural invariant;
- table value copied across volumes: never trust the copy without a fresh convention conversion.

Cross-volume convention alert:

- Vol I uses OPE modes;
- Vol II uses lambda-brackets with divided powers;
- Vol III may use motivic or categorical normalizations.

If independent paths disagree, the claim is unstable. Downgrade, isolate, or keep auditing. Do not average the disagreement into confidence.

## Context And Memory Hygiene

Codex handles long-horizon work better when intermediate state is made explicit.

For substantial tasks:

- keep a short explicit plan;
- after each major phase, restate target, best current status, open risk, and next falsifier;
- anchor conclusions to exact file paths, theorem labels, and test names;
- prefer stable note files under `compute/audit/` for substantive audit artifacts;
- do not let summaries harden into truth without rereading the source;
- preserve failed verification attempts as evidence, not just successful runs.

## Hostile Examiners

Dense passages should be inspected through these lenses:

- **Beilinson**: is the claim really proved, or only asserted?
- **Witten**: does the physical interpretation match the mathematical statement, with honest scope?
- **Costello**: are the factorization and mixed-color constructions actually well-formed?
- **Gaiotto**: do VOA, DS, and W-algebra identifications survive reductions and edge cases?
- **Drinfeld**: are the transport, quantum-group, and monodromy structures structurally correct?
- **Kontsevich**: are the operadic and formality statements precise, functorial, and non-circular?
- **Compiler**: does the intended workflow fit Codex's actual runtime constraints, tools, hooks, and skill surface?

## Post-Edit Gates

### Beilinson Gate

After editing any `.tex` or `.py` file, explicitly check:

- did the edit change truth conditions or only exposition;
- is claim status still honest;
- do environment, label prefix, and surrounding prose still agree;
- if an `r`-matrix or lambda-bracket changed, did you perform the level-prefix or divided-power check;
- if a formula changed, did you audit nearby `therefore`, `hence`, and `it follows`;
- if chapter structure changed, did you grep for hardcoded Part references and standalone-document commands;
- if `RECTIFICATION-FLAG` appeared, is it resolved or tracked explicitly with owner;
- if a shared formula, status, or terminology changed, did you propagate across active Vol II, superseded files, Vol I, Vol III, README/notes, and compute/tests as appropriate;
- if compute expected values changed, were they derived independently from the engine output;
- if bulk, center, or CY3 bridge language was touched, is scope and conditionality still honest.

### Convergence Gate

If the session is an audit or rectification session, do not stop until you can honestly say one of:

- `CONVERGED`
- `BLOCKED: <exact blocker>`

### Pre-Commit Gate

Before any commit:

1. run the narrowest build/test verification that matches the change;
2. inspect the diff for build artifacts, PDFs, and accidental noise;
3. ensure there is no AI attribution in commit message or metadata;
4. ensure all commits remain authored by Raeez Lorgat only.

## Standing Hypotheses - Made Explicit

The algebraic framework is unconditional. The former standing hypotheses are no longer background fog:

| Hypothesis | Content | Current status |
|---|---|---|
| `(H1)` | BV data, one-loop finiteness | Condition of `Theorem thm:physics-bridge`; only for physical realizations |
| `(H2)` | Propagator meromorphic in `C`, exponentially decaying in `R` | Consequence of the physics bridge for physical realizations |
| `(H3)` | FM compactification, logarithmic forms, AOS relations, Stokes exactness | Axiomatically packaged by `Definition def:log-SC-algebra`; analytic consequences proved by `Theorem thm:FM-calculus` |
| `(H4)` | Compatibility with `C_*(W(SC^{ch,top}))` | Recognition theorem `thm:recognition-SC` |

Definition `def:log-SC-algebra` is the clean algebraic entry point:

- a `C_*(W(SC^{ch,top}))`-algebra whose closed-color `A_infinity` operations are defined by logarithmic weight forms factoring as `omega_k = omega_k^hol otimes omega_k^top` on `FM_k(C) x Conf_k(R)`.

## Current Load-Bearing Boundaries

These are the places where overclaiming is easiest and most damaging:

- `B(A)` is an E_1 coassociative coalgebra classifying twisting morphisms; it does NOT carry `SC^{ch,top}` structure; the SC structure emerges in the chiral derived center pair `(C^bullet_{ch}(A,A), A)`;
- bulk `simeq` derived center is rigorous on the boundary-linear exact lane, not automatically for every boundary condition globally;
- open-to-closed in the Swiss-cheese picture is empty;
- formality failure at `d' = 1` is the curved bar structure, not a defect;
- the `R`-matrix comes from bulk-boundary composition, not automatically from a universal quantum-group `R`;
- spectral strictification is proved for simple Lie algebras with root multiplicity one; the frontier remains Kac-Moody multiplicity `> 1`;
- any bridge statement whose proof chain depends on an unconstructed CY3 object remains conditional downstream.

## Critical Mathematical Pitfalls

Inherited from Vol I:

- cohomological grading, `|d| = +1`;
- bar uses desuspension;
- `m_1^2(a) = [m_0,a]` with the commutator sign convention;
- Sugawara is undefined at critical level `k = -h^vee`;
- Virasoro self-duality is at `c = 13`, not `26`.

Specific to Vol II and the bridges around it:

- open-to-closed is empty;
- the PVA on `H^bullet(A,Q)` is `(-1)`-shifted;
- ordinary vertex algebras remain `E_infinity`-chiral even with poles;
- `R(z) != tau` does not by itself imply genuine `E_1`;
- the Koszul dual lives on the boundary, not in the bulk;
- CoHA is associative, not automatically an `E_1`-chiral algebra;
- Drinfeld center is not the same construction as derived center;
- Vol III bridge statements: CY-A_3 is now PROVED (inf-cat). CY-C (quantum group realization) remains CONJECTURAL. Bridge statements through CY-A are now unconditional; those through CY-C remain conditional.

## Codex Local Infrastructure

Repo-local Codex playbooks live in `.agents/skills/`:

- `$vol2-deep-audit`
  Findings-first mathematical audit and review surface.
- `$vol2-beilinson-rectification`
  Deep audit/rectify/fortify loop on a chapter, theorem, or live surface.
- `$vol2-chriss-ginzburg-rectify`
  Full five-phase Chriss-Ginzburg fortification + Beilinson rectification. Platonic ideal convergence on a chapter. Supersedes `$vol2-beilinson-rectification` for deep structural work.
- `$vol2-compute-engine`
  Compute-engine scaffolding and test-surface discipline for Vol II.
- `$vol2-formula-verification`
  Multi-path checking for formulas, invariants, coefficients, tables, and test oracles.
- `$vol2-cross-volume-propagation`
  Grep-and-propagate workflow across Vol I, Vol II, Vol III, superseded files, and compute layers.
- `$vol2-build-surface`
  Build, test, log, and warning triage.
- `$vol2-frontier-research`
  Frontier synthesis and research design, local by default and swarm-enabled only with explicit user authorization.
- `$vol2-research-swarm`
  Explicit delegation/swarm workflow for user-authorized parallel frontier work.
- `$vol2-six-layer-architecture`
  Codex entry point for the master/Route A/B/C architecture specs under `.claude/specs/`.

Repo-local Codex hooks live in `.codex/hooks.json`:

- `SessionStart`: injects the Vol II live-surface reminder.
- `UserPromptSubmit`: routes rectification-like prompts toward the correct playbooks.
- `PreToolUse`: blocks destructive shell habits and guards commits.
- `PostToolUse`: refuses to let failing verification output be silently ignored.
- `Stop`: nudges unfinished rectification sessions to declare `CONVERGED` or `BLOCKED`.

Hook note:

- Codex hooks are deterministic guardrails, not a substitute for judgment;
- current Codex `PreToolUse` and `PostToolUse` hook Bash only, so the mental gates in this file close the rest;
- if a workflow repeats and is too large for always-on context, move it to a skill instead of bloating `AGENTS.md`.

## Active Build Graph

`main.tex` is authoritative. Read it, not an old memory, when you need the exact chapter order.

**Frame**

- `chapters/frame/preface`

**Theory**

- `chapters/theory/introduction`
- `chapters/theory/foundations`
- `chapters/theory/locality`
- `chapters/theory/axioms`
- `chapters/theory/equivalence`
- `chapters/theory/bv-construction`
- `chapters/theory/factorization_swiss_cheese`
- `chapters/theory/raviolo`
- `chapters/theory/raviolo-restriction`
- `chapters/theory/fm-calculus`
- `chapters/theory/orientations`
- `chapters/theory/fm-proofs`
- `chapters/theory/pva-descent-repaired`
- `chapters/theory/pva-expanded-repaired`
- `chapters/theory/modular_swiss_cheese_operad`

**Examples**

- `chapters/examples/rosetta_stone`
- `chapters/examples/examples-computing`
- `chapters/examples/examples-complete-proved`
- `chapters/examples/examples-worked`
- `chapters/examples/w-algebras-virasoro`
- `chapters/examples/w-algebras-w3`
- `chapters/examples/examples-complete-conditional`
- `chapters/examples/w-algebras-frontier`

**Connections - Part II**

- `chapters/connections/bar-cobar-review`
- `chapters/connections/line-operators`
- `chapters/connections/ordered_associative_chiral_kd_core`
- `chapters/connections/dg_shifted_factorization_bridge`
- `chapters/connections/thqg_gravitational_yangian`
- `chapters/connections/typeA_baxter_rees_theta`
- `chapters/connections/shifted_rtt_duality_orthogonal_coideals`
- `chapters/connections/casimir_divisor_core_transport`

**Connections - Part III**

- `chapters/connections/dnp_identification_master`
- `chapters/connections/spectral-braiding-core`
- `chapters/connections/ht_bulk_boundary_line_core`
- `chapters/connections/celestial_boundary_transfer_core`
- `chapters/connections/affine_half_space_bv`
- `chapters/connections/fm3_planted_forest_synthesis`
- `chapters/connections/kontsevich_integral`

**Connections - Part IV**

- `chapters/connections/hochschild`
- `chapters/connections/brace`
- `chapters/connections/relative_feynman_transform`
- `chapters/connections/modular_pva_quantization_core`
- `chapters/connections/ht_physical_origins`

**Connections - Part V**

- `chapters/connections/ym_synthesis_core`
- `chapters/connections/ym_boundary_theory`
- `chapters/connections/ym_higher_body_couplings`
- `chapters/connections/ym_instanton_screening`
- `chapters/connections/celestial_holography_core`
- `chapters/connections/log_ht_monodromy_core`
- `chapters/connections/anomaly_completed_core`
- `chapters/connections/thqg_holographic_reconstruction`
- `chapters/connections/thqg_modular_bootstrap`
- `chapters/connections/holomorphic_topological`

**Connections - Part VI**

- `chapters/connections/thqg_gravitational_complexity`
- `chapters/connections/3d_gravity`
- `chapters/connections/thqg_3d_gravity_movements_vi_x`
- `chapters/connections/thqg_critical_string_dichotomy`
- `chapters/connections/thqg_perturbative_finiteness`
- `chapters/connections/thqg_soft_graviton_theorems`
- `chapters/connections/thqg_symplectic_polarization`

**Frontier**

- `chapters/connections/spectral-braiding-frontier`
- `chapters/connections/ht_bulk_boundary_line_frontier`
- `chapters/connections/celestial_boundary_transfer_frontier`
- `chapters/connections/modular_pva_quantization_frontier`
- `chapters/connections/ordered_associative_chiral_kd_frontier`
- `chapters/connections/ym_synthesis_frontier`
- `chapters/connections/celestial_holography_frontier`
- `chapters/connections/log_ht_monodromy_frontier`
- `chapters/connections/anomaly_completed_frontier`

**Aftermatter**

- `chapters/connections/conclusion`

**Appendices**

- `appendices/brace-signs`

**Superseded But Still Audit-Relevant**

- `spectral-braiding.tex`
- `ht_bulk_boundary_line.tex`
- `celestial_boundary_transfer.tex`
- `modular_pva_quantization.tex`
- `ordered_associative_chiral_kd.tex`
- `ym_synthesis.tex`
- `celestial_holography.tex`
- `log_ht_monodromy.tex`
- `anomaly_completed_topological_holography.tex`
- `examples-complete.tex`
- `w-algebras.tex`
- `physical_origins.tex`
- `holomorphic_topological.tex`
- `bv_ht_physics.tex`
- `concordance.tex`

## Build

Preferred manuscript build prelude:

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
make fast
```

Full build when needed:

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
make
```

Compute verification lives under `compute/tests/`.

For cross-volume bridge edits, run the narrowest relevant check in every affected repo. Do not assume one volume's green build certifies another's bridge language.

## LaTeX Rules

- use `\providecommand`, not `\newcommand`, for new macros;
- do not add `\newtheorem` in chapter files;
- claim tags: `\ClaimStatusProvedHere`, `\ClaimStatusProvedElsewhere`, `\ClaimStatusConjectured`, `\ClaimStatusHeuristic`, `\ClaimStatusOpen`;
- key macros include `\cA`, `\Ainf`, `\Linf`, `\barB`, `\Omegach`, `\hh`, `\HH`, `\Sym`, `\End`;
- do not add packages without checking the preamble;
- do not duplicate Vol I definitions that should be referenced textually;
- do not create new chapter files when the content belongs in an existing live chapter;
- chapter files `\input`'d into `main.tex` must not contain `\title`, `\author`, `\date`, `\begin{abstract}`, or `\tableofcontents`;
- never hardcode Part numbers in prose; use `\ref{part:...}`;
- after writing `.tex`, grep the touched surface for Markdown artifacts, banned slop phrases, backticks, and em-dashes.

## Git - Hard Rule

All commits are authored by Raeez Lorgat.

Never add:

- `Co-authored-by`
- `Generated by`
- AI attribution of any kind in commit messages, source files, manuscript text, or metadata

Never use destructive recovery commands like `git reset --hard` or `git checkout --` unless the user explicitly requests them.

## The Aesthetic

Show, do not bluff. Every construction should feel inevitable because the proof architecture makes it inevitable, not because the prose is smooth.

The bar complex is the E_1 coassociative coalgebra.
The chiral derived center is the bulk.
The pair (derived center, boundary algebra) is the SC datum.
The complementarity potential presents the nonlinear modular shadow.

The music matters, but only after the score compiles.

## Failure Modes from 2026-04-14 CG Campaign

FM42: Bulk replace "arity"→"degree" corrupts singularity→singuldegree, complementarity→complementdegree, unitarity→unitdegree, etc. Never bulk-replace short substrings inside common words. Grep `ldegree|ndegree|rdegree|pdegree|tdegree` after any bulk replace.

FM43: Φ outputs E_1 at d≥3, not E_2. Always scope E_n with `(n=2 for d≤2; n=1 for d≥3)`.

FM44: >10 concurrent agents → mass rate limiting. Batch in 3s.

FM45: Subagents lack the full 15K-word skill. Good for bulk scanning; insufficient for deep reconstitution.

## Independent Verification Protocol (cross-volume, 2026-04-16)

**STANDALONE.** Motivated by the 2026-04-16 Vol III adversarial audit finding `\ClaimStatusProvedHere` theorems backed by tautological tests (engines hardcoded `FRAME_SHAPE_DATA[N] = (weight, c_0, ...)` with verified identity `weight := c_0/2` built into the row). Rules ("always verify", "never hardcode") proved ineffective. Protocol is a mechanical invariant.

**Mechanical invariant.** Every test for a ProvedHere theorem declares:
- `derived_from`: canonical names of data/papers/conventions the formula came from.
- `verified_against`: canonical names of independent data/papers/conventions for the expected value.
- One-sentence `disjoint_rationale`.
If `derived_from ∩ verified_against` is nonempty (case/whitespace-insensitive), the test module fails to import. Tautology = audit failure, not silent pass.

**Decorator API (use verbatim):**

```python
from compute.lib.independent_verification import independent_verification

@independent_verification(
    claim="thm:phi-k3-explicit",
    derived_from=["HKR isomorphism on D^b(Coh(K3))", "Hodge diamond of K3"],
    verified_against=["Mukai 1984 lattice rank 24 for H^*(K3, Z)",
                      "Classical Betti numbers b_0 + b_2 + b_4 = 24"],
    disjoint_rationale=("HKR reconstructs total_dim via polyvector cohomology "
                        "on K3; Mukai/Betti gives the rank as a topological "
                        "invariant from the K3 lattice without any HH_* or "
                        "chiral construction. Independent derivations."),
)
def test_total_dimension_24():
    ...
```

**Enforcement.** `make verify-independence` summary; `make verify-independence-verbose` lists every uncovered claim. Scrapes `chapters/`, `appendices/`, `notes/`, `working_notes.tex` for `\ClaimStatusProvedHere`; imports test modules; reports ProvedHere count, coverage, tautological decorations (should be 0; fail at import), orphans. Exit 0/2. Coverage % is metric, not gate.

**Three healings when honest decoration fails:**
1. Find a disjoint source.
2. Restrict scope (replace `theorem` with scoped `proposition`; note general case conjectural).
3. Downgrade status (replace `\ClaimStatusProvedHere` with `\ClaimStatusConjectured`).

Audit surfaces the choice; does not choose.

**Files (cross-volume, identical code):**
- `compute/lib/independent_verification.py` — decorator + registry + disjointness check
- `compute/scripts/audit_independent_verification.py` — lint
- `compute/tests/test_independent_verification_infra.py` — 7-test self-test
- `notes/INDEPENDENT_VERIFICATION.md` — protocol doc

**Coverage snapshot (2026-04-16):** Vol I 0/2275; Vol II 0/1134 at installation, expanded to 61/1322 on 2026-04-16 campaign continuation; Vol III 22/290. All three volumes: AUDIT RESULT PASS (zero tautologies, zero orphans). Cross-volume totals: 132 disjointly-verified ProvedHere claims / 4108 total (3.2%).

## V2-AP40 Six Subclauses + V2-AP41 (2026-04-17 refinement)

V2-AP40 is the single most cross-file-violated invariant in the manuscript proper. Reader-facing prose in `chapters/` and `standalone/` must never contain AP/FM/HZ/RS/WAVE/session-date/commit-hash tokens.

**Mechanical detection grep** (run against `chapters/` and `standalone/` before every `.tex` commit):
```
grep -nE 'AP[0-9]+|FM[0-9]+|\(AP-CY[0-9]+|commit \\texttt|cached confusion|Beilinson-rectified|working note|RS-[0-9]|HZ-[0-9]|\bC[0-9]+:|\bB[0-9]+:|AP-RMATRIX|AP-OC|HEAL-(SWEEP|MODE)|UPGRADE-SWEEP|PLATONIC ANCHOR|WAVE-[0-9]+' chapters/ standalone/
```

**Subclauses:**

- **V2-AP40a** (bibkey-named-after-ledger-token). `\cite{Vol2-FM81-platonic}` leaks "FM81" into the rendered bibliography. `.bib` keys must be content-named.
- **V2-AP40b** (label-named-after-ledger-token). `\label{rem:AP172-...}`, `\label{cor:FM134-healed}`, `\label{rem:chapter-retracted-2026-04-17}` propagate the token through the PDF's link graph and every `\ref{}`. Labels must be content-named.
- **V2-AP40c** (index-entry / hyperref anchor). `\index{AP###!...}` and `\hyperref[AP##]{AP##}` lift the token into the compiled index and in-text navigation. Delete outright; rephrase surrounding prose to state mathematical content.
- **V2-AP40d** (theorem-environment title). `\begin{remark}[AP172: Koszul dual is an SCchtop^! -algebra]`, `\section{Anti-pattern register: AP171, AP172, AP174}` show ledger tokens in TOC and environment headers. Retitle by content.
- **V2-AP40e** (monospaced filename or chapter-label pointer). `\texttt{e_infinity_topologization.tex}`, `\texttt{chap:universal-conductor}` leak filesystem basenames. Replace with `\ref{thm:...}` / `\cref{chap:...}` or prose.
- **V2-AP40f** (math-mode label leak). `$\mathrm{conj}{:}\mathrm{periodic\text{-}cdg}$` dresses a source-code label as mathematics; bypasses the five-pattern grep. Either use `\ref{}` to a real label or write prose.

**V2-AP41 (internal theorem-statement-vs-proof formula inconsistency).** A main theorem states one formula in its hypothesis/case-split, then the immediate proof-detail paragraph cites a different formula that diverges at boundary cases. Example (Vol II introduction, 2026-04-17): Programme Climax theorem stated Arnold coupling $\beta_{W_N} = (N+1)(N+2)/2$ for principal $W_N$, then Stirling-dominance pillar proof cited proved closed form $\beta_N = 12(H_N - 1)$. Agree at $N = 2, 3$; diverge at $N \ge 4$: $(5)(6)/2 = 15$ vs $12 \cdot 13/12 = 13$. Incorrect value would widen Banach radius and forgive spurious convergence. Counter: theorem statement must be consistent with proof it governs; grep surrounding chapter for same symbol, verify per-row agreement at first boundary case ($N = 4, d = 3, g = 2$).

## Wave 6-12 Cross-Volume FM Registry (2026-04-16 adversarial campaign)

Full per-FM content in CLAUDE.md §"Session 2026-04-16 Adversarial Campaign — Waves 1-6 (FM69-FM118)" through §"Wave 12 supplement ctd. (FM248-FM257)". Operational digest only below.

### Wave 6 continuation (FM119-FM129, lattice/Monster/moonshine/3D-gravity/celestial)

- **FM119**: κ(K3) subscripting — κ_ch=2 vs κ_fiber=24 both correct with different subscripts; bare κ usage violates AP113.
- **FM120** [CLOSED 2026-04-17]: Monster V^♮ = V_Leech^+ DW anomaly vanishing proved explicit via Kapustin-Saulina formula + Conway Λ^σ=0 + FLM twisted Jacobi + Dong-Mason uniqueness (α=0 unconditional).
- **FM121**: prop:symn-twist-vanishing q^0 torus amplitude → use generator-count additivity (weight-1 current / stress-tensor counting), not q^0 torus alone.
- **FM122**: Moonshine G→M class transition collapsed one step — class change happens at V_Λ^+ (already class M by lone-Virasoro lane).
- **FM123**: Sym^N K3 κ = c/3 treated as law → drop "ϱ=c/3" rule; c/κ=3 at c=6 is coincidence, not additive.
- **FM124**: Moonshine Koszul dual → "Koszul dual of Vir_{24} subalgebra", not of V^♮ itself.
- **FM125**: thm:gravity-koszul-triangle projection vs equivalence → "projection onto saddle-point reading"; Bulk≈C[[c]] is not a derived equivalence.
- **FM126** [CLOSED via DS-Hochschild bridge]: stale label + LG/chiral conflation — bulk = dCrit for commutative Landau-Ginzburg superpotentials, NOT the chiral G/L/C triangle; chiral G/L/C triangle rests on separate HH computations; class M closed via thm:chd-ds-hochschild (chiral_higher_deligne.tex:652-654).
- **FM127**: "Perturbative finiteness" — split algebraic finiteness (Proved) vs physical UV finiteness (subject to class-M chain-level E_3 gap).
- **FM128** [CLOSED 2026-04-17]: V^♮ chain-level E_3-topological PROVED unconditional via thm:monster-chain-level-e3-top; no longer a research expectation.
- **FM129**: Ramanujan bound via shadow tower claims to bypass Weil → rephrase as structural refinement via Langlands functoriality inputs (not independent of Weil/Deligne).

### Wave 7 (FM130-FM142, W-algebras + Yangians + YM/anomaly/log bridges)

- **FM130**: thm:wn-obstruction cross-term vanishing — proved N=2,3 directly; computationally verified N≤6; N≥7 CONJECTURAL without cross-channel curvature hypothesis.
- **FM131**: BP self-dual proof — missing de Boer-Tjin 1993 free strong generation citation (required hypothesis of CLNS24 hook transport).
- **FM132**: "Inherits Koszulness" — W(2)=SF^{Z_2} orbifold generically breaks free strong generation; AM generators PBW universality OPEN.
- **FM133**: N=2 SCA verified "through weight 6" — no independent_verification decorator; AP-CY49 tautological test risk.
- **FM134**: Y-algebra triality preservation of shadow class/PBW collapse page — CONJECTURAL; verified for small L,M,N only.
- **FM135**: W_3 holographic datum standalone "controls every 3d HT QFT" — install decorators per Vol II protocol; downgrade "controls every" to "conjecturally controls; verified for standard landscape."
- **FM136**: Open_B = B^ch(A_B) ≃ C^{∞/2+•}(A_B) "for Koszul-admissible A_B" — scope to affine + principal W lineage.
- **FM137**: Mass-gap theorem vacuous-hypothesis — retitle "Algebraic mass-gap reduction principle."
- **FM138**: "Yang-Mills" unmodified → global rename "HT-twisted N=2 YM boundary"; keep unmodified only when discussing Clay problem explicitly.
- **FM139**: "Central screening sequence" borrows VOA screening terminology without content → rename "central q-adic annihilator sequence."
- **FM140**: "Logarithmic HT monodromy" = log-FM, NOT logarithmic VOA. Prepend Scope Remark distinguishing.
- **FM141**: "Critical string dichotomy" at c=26 — retitle to emphasize Clifford-degeneration content.
- **FM142**: "Anomaly-completed Yangian completion theorem" floats between universal-algebra and physical-identification levels; applicability to specific physical Y+Θ pair is CONJECTURAL.

### Wave 8 (FM143-FM170, Kontsevich + PVA descent + SC pentagon + Yangians cluster)

- **FM143**: Re/Im swap in prop:propagator-restriction — write Im (or "real 1-form coefficients on S^1"); add glossary.
- **FM144**: Arnold cancellation proof — redo sign bookkeeping OR cite Getzler-Jones and drop explicit calc.
- **FM145**: prop:general-orient-sign ProvedHere uniform formula but Corollary says "requires more care" — scope-restrict to fixed coordinate ordering OR downgrade Corollary to Remark.
- **FM146**: Kontsevich formality "exactly this statement" — excise "exactly"; keep construction env; identification as theorem conjectural.
- **FM147**: "4T = Arnold" — 4T descends from Arnold + STU + graded commutativity, NOT Arnold alone. Cite Bar-Natan 1995 §3.
- **FM148**: thm:PVA-descent-roadmap universal "for any logarithmic SC^{ch,top}-algebra" — restrict to classes G/L/C; class M gives P_∞-chiral not PVA.
- **FM149**: D6 transverse closedness hidden → add explicit hypothesis; class M outside scope.
- **FM150**: raviolo R-matrix twist absent — Mon(R) must appear in the equivalence relation; E_1 seeds supply it externally.
- **FM151**: Internal tension prop:chain-D-vs-S1 — "qiso of underlying chain complexes; E_2 + spectral R(z) survive only on punctured-disk side."
- **FM152**: Y(a,z) reconstructed only at leading order — full reconstruction requires d_B + translation T, not μ|_0.
- **FM153**: Raviolo coinvariants via Lie-algebra framing → name Sugawara/Zhu bridge or define chiral coinvariants directly.
- **FM154**: D2-D6 README shorthand "proved" compresses log-SC scope + worked-example-vs-universal → "D2-D6 proved for logarithmic SC-algebras (classes G, L, C); sl_2 worked; class M descent separate theorem."
- **FM155**: Phantom label `prop:sc-koszul-dual-three-sectors` — write the proposition with Vallette coloured Koszul duality computation OR downgrade thm:dual-sc-algebra to Conjectured.
- **FM156**: Koszul dual closed sector Com^! = Lie — closed sector of (SC^{ch,top})^! is E_2^{shifted} (Gerstenhaber self-dual up to shift), NOT Com.
- **FM157**: Liv06 mis-binding across 7+ files — rebind to Hoefel arXiv:0809.4623 or Hoefel-Livernet arXiv:1207.2307.
- **FM158**: thm:homotopy-Koszul Step 2 overstates Kontsevich formality as strict dg-operad map — reword as zigzag of ∞-operads with fixed Drinfeld associator.
- **FM159**: SC^{ch,top} ≠ sub-operad of Voronov's SC — add lemma "product-collapse qiso map of homotopy operads."
- **FM160**: Edge (3↔4) chain-level overclaim — "QME ↔ MC at level of quasi-iso classes; chain-level equality after fixed gauge/semifree model."
- **FM161**: Y(g) Koszulness via PP05 — replace with filtered-CDG-Koszul deformation; restrict to classical types or use GRW18 for exceptional.
- **FM162**: Exceptional-type PBW uncited — add Guay-Regelskis-Wendlandt 2018 citation.
- **FM163**: Y(g)^! = Y(g)^{ℏ→-ℏ} handwave — verify R^{-1} under trace pairing to all orders.
- **FM164**: Bar-cobar Yangian completion — use \hat{Ω}^ch \hat{B}^ch(A) → \hat{A} qiso in pro-nilpotent completion.
- **FM165**: Gaudin from MC "projection" handwave — replace with CYBE + r-matrix computation on eval tensors (FFR).
- **FM166**: Jones polynomial from ordered-E_1 bar — split into (i) bar monodromy = braid rep (proved); (ii) Jones = RT functor on MTC quotient (cite Reshetikhin-Turaev).
- **FM167**: Y(g)^! = Y(g^v) non-simply-laced — tag simply-laced (proved via automorphism) vs non-simply-laced (Langlands conjecture) separately.
- **FM168**: Gravitational Yangian CYBE = formal-series identity only; genuine algebraic interpretation requires specifying Vir-module category.
- **FM169**: "Gravitational Yangian" as Hopf algebra — rename "Gravitational dg Lie bialgebra"; Hopf promotion open.
- **FM170**: k_max = 2 landscape exclusion missing super-qualifier — add "bosonic"; note superconformal exception (AP107).

### Wave 9 (FM171-FM181, foundations + RTT/Baxter/coideals)

- **FM171**: (H1)-(H2)=(a)-(c) misidentification — bridge hypotheses (a)-(c) IMPLY (H1)-(H4) as derived log-SC properties; do not equate.
- **FM172**: Zombie pva-descent.tex — delete or rewrite to cite log-SC hypothesis.
- **FM173**: Double-labeled recognition theorem — single canonical label + cross-references.
- **FM174**: Zombie foundations drafts coexist with foundations.tex — merge canonical; delete drafts (V2-AP27).
- **FM175**: gr-splitting "second proof" not independent — demote to Remark; explicitly name the Gerstenhaber→Poisson collapse.
- **FM176**: Type-A scope drifts gl_N vs sl_N — fix uniform notation Y_ℏ(sl_N).
- **FM177**: "Baxter-Rees family" has no Baxter operator — rename "weight-Rees spectral-telescope family" OR construct Q + verify TQ. Closed 2026-04-16 via Hernandez-Jimbo prefundamental q-oscillator + QQ system.
- **FM178**: thm:pairwise-to-all-point-reconstruction hides slot-commutativity hypothesis — add explicit hypothesis.
- **FM179**: thm:quotient-coideal-descent proves sub-dg-module, claims subcoalgebra — weaken to sub-dg-module OR add coideal verification.
- **FM180**: thm:pbw-recurrence imports Riordan GF externally — ProvedElsewhere-layered; "Assuming bar GF = Riordan, ..." status.
- **FM181**: "Orthogonal coideal" terminology collides with Letzter-Kolb — add scope remark; alternative "pairing-annihilator coideal."

### Wave 9-10 (FM182-FM196, Hochschild/brace/holographic + Vol II standalones)

- **FM182**: hochschild.tex:575 unqualified "HH^0" — named sub-lemma "ChirHoch^0_{δ_Q-only}(A_∂) = Z(A_∂)."
- **FM183**: Missing named bridge algebraic vs geometric chiral-Hoch models — introduce thm:chiral-hochschild-models-equivalent for logarithmic SC^{ch,top}.
- **FM184**: brace.tex:9-11 "terminal local chiral open/closed pair" overclaims — "universal-at-cohomology after fixing a Drinfeld associator."
- **FM185** [CLOSED via DS-Hochschild bridge]: thqg_holographic_reconstruction ProvedHere G/L/C/M — now split: thm:shadow-reconstruction (all classes, formal) + thm:holographic-reconstruction (G/L/C Proved; M Closed via chd-ds-hochschild).
- **FM186** [CLOSED via DS-Hochschild bridge]: thqg_symplectic_polarization silent ProvedHere upgrade for class M — class M resolved via Universal Holography closure.
- **FM187**: hochschild.tex Kel06+BZFN10 cite elides chirality upgrade (AP-CY67) — two-step derivation.
- **FM188**: hochschild.tex triple conflation HH^•(A_∂) ≃ O(T^*[-1]L_b) ≃ O(M_vac)|_{L_b} — cohomological proposition after global-triangle datum; chain-level → Conjectured for class M.
- **FM189**: brace.tex strict brace presentation cited without associator disclosure — promote remark to numbered Convention.
- **FM190**: bar_chain conflates geometric vs algebraic chiral Hochschild; invokes classical Deligne for chiral E_2 — state ChirHoch model explicitly; chiral Deligne at chain level CONJECTURAL.
- **FM191**: bar_chain thm:topologise ProvedHere for KM but scope-creeps — keep scope to KM non-critical; conjectural extensions in remarks.
- **FM192**: stokes_gap_kzb_regularity hides SECOND conjecture (R(z)-twisted clutching + curved-Dunn H²) — state both explicitly; downgrade "reduces to" to "conditional on two open problems."
- **FM193**: class_m_global_triangle weight-by-weight HPL convergence argument absent — state level-level vs level-sum convergence gap.
- **FM194**: bar_chain Schiffmann-Vasserot coproduct RECONSTRUCTED but framed as "produced" — "reproduces the SV coproduct as consistency check."
- **FM195**: bar_chain cites [Theorem A]{Vol I} as authority for bar-cobar (wrong theorem) — cite correct Vol I theorem; grep-verify all cross-volume labels.
- **FM196**: bar_chain β_{M,N}(z) = R(z)·σ conflates spectral parameter with E_2 categorical braiding — separate nat transformation from family.

### Wave 11 (FM197-FM206, Vol I N-paper series)

- **FM197**: N1 (vii) "factorization homology concentrated in degree 0 for all g" — tag "uniform-weight g=0 unconditional; g≥2 scalar-lane only."
- **FM198**: N1 "twelve equivalences / ten unconditional" overclaim — honest count "core-5 + 5 conditional + 2 conjectural."
- **FM199**: N2 MC3 proves evaluation-generated core only — retitle "thick generation on eval-generated core of DK_g."
- **FM200**: N3 "dg Lie on pseudo-tensor codomain" — restrict to scalar lane / genus 0 tree level OR prove ribbon convolution closes.
- **FM201**: N3 "five theorems A-D,H lift to ordered" — prove each lift individually OR downgrade to "Theorem D lifts; B, C, H conjectural."
- **FM202**: N4 V_k(g) "strong completion tower" axiom (4) fails literally unless curved A_∞ with mu_0 = κ_dp absorbed — rename "curved strong completion tower."
- **FM203**: N4 W_{N+1} → W_N projection "strict morphism" without OPE-closure verification — replace "strict" with "up to homotopy" OR prove closure.
- **FM204**: N4 "Twenty-one standing conjectures resolved" — produce explicit list or delete.
- **FM205**: N5 Vir OPE-growth bound uses N=2; cubic central term suggests N=3 — use N=3 polynomial bound.
- **FM206**: N6 "Class M consists of intrinsically non-formal algebras" — AP14 conflation; write "L_∞ non-formal on g^{mod,(0)}."

### Wave 10 (FM207-FM213, DNP + rosetta + half-space BV)

- **FM207**: rosetta_stone.tex:2039-2041 misattributes Vol II label `thm:Koszul_dual_Yangian` as Vol I — delete "Volume~I," prefix.
- **FM208**: dnp_identification_master thm:vol2-seven-faces-master ProvedHere with 4+ conditional clauses — use `\ClaimStatusProvedHereConditional` OR split.
- **FM209**: affine_half_space_bv prop:affine-is-log-SC claims BV-BRST complex IS log SC^{ch,top} — rephrase as "the PAIR (Z^{der}_{ch}(V^{Keff}), V^{Keff}) is a log SC^{ch,top}-datum via Thm H."
- **FM210**: dnp_identification_master "seven equivalent realizations" uniform while master theorem per-face qualifiers differ — "on the common locus (g=0, non-critical, classical simple g)."
- **FM211**: dnp_identification "Non-renormalization = Koszulness IS E_2-collapse" identifies two propositions without comparison theorem — tag as Conjectured until bridge lemma written.
- **FM212**: ht_physical_origins thm:cl-n4-chirality ProvedElsewhere[CL16] — add CDG20/Zeng23 citations or narrow scope.
- **FM213**: Missing file thqg_open_closed_realization.tex (phantom) — create stub or reroute pointers.

### Wave 10 continuation (FM214-FM223, Vol II preface + introduction)

- **FM214** [CLOSED via DS-Hochschild bridge]: Universal IS-claim without scope in preface/intro — "On the boundary-linear exact sector (classes G/L/C), Z^der_ch(B_∂) ≃ A_bulk"; class M closed via Universal Holography.
- **FM215**: Internal contradiction with FM82 preface Stage 9 — verify Vir gr_Li is KZ-admissible independently; otherwise scope Stage 9 to G/L/C. Closed 2026-04-16 via thm:e-infinity-topologization-ladder.
- **FM216**: Chriss-Ginzburg "precise parallel" — retitle "Structural analogy"; per-row metaphor-vs-theorem footnote.
- **FM217**: intro.tex list-before-prove (AP109) — split into 4 paragraphs; state scope per piece.
- **FM218**: "Only" universal quantifiers in preface — drop "only"/"only language."
- **FM219**: Preface inherits FM158 strictness overclaim — fix upstream line-operators.tex Step 2.
- **FM220**: Internal contradiction on modular-operad status within preface — align early ladder to Frontier formulation.
- **FM221**: Spectral-vs-categorical conflation in preface — "restrict to evaluation-module core; cite thm:affine-monodromy explicitly."
- **FM222**: Preface's declarative conjecture — "is conjectured to recover (conj:...)"; AP40 violation.
- **FM223**: Triple repetition of "complete" strictification — keep one statement; replace others with "rank-1 rigidity-based path-sector strictification."

### Wave 11 continuation (FM224-FM239, compute library decorator audit + Vol I survey)

- **FM224**: Decorator campaign at 0% (at installation; 61/1322 = 4.6% post-2026-04-16 campaign) — install decorators for top-5 climax theorems first; gate any new ProvedHere by decorator presence.
- **FM225**: Pre-existing V2-AP28 tautology live in test_adversarial_verification.py — recompute expected F_g values from Arakelov heat-kernel / zeta-regularised determinant inside the test.
- **FM226**: Dictionary self-consistency test masquerading as theorem — derive expected weights from Kac's classification independently; or use engine output from different code path.
- **FM227**: Eight engines without tests (ainfty, arnold, convention_check, fm_boundary, genus2_ordered_bar, laplace_bridge, spectral, symbolic_stasheff) — prioritize genus2_ordered_bar + spectral for scaffolding.
- **FM228**: Archival tests as AP28 danger zone — audit line-by-line; each hardcoded value needs `# VERIFIED` with independent source.
- **FM229**: convention_check engine itself lacks a test — write self-verification.
- **FM230**: Heisenberg labeled "pole-free commutative" (survey_track_b tier (a)) — rename "scalar-R abelian"; drop "pole-free."
- **FM231**: CY-A_3 abstract/body self-contradiction — unify "proved inf-cat; CY-C open"; strike "single open conjecture."
- **FM232**: Vol II/III climax content attributed to Vol I survey — strike or tag "previewed; proved in Vol II/III."
- **FM233**: Pole-free label self-contradiction in Track B — rename "abelian-R scalar" tier.
- **FM234**: "Interpolate" across E_∞/E_1 gap in introduction_full_survey — "span pole-structure gradation within E_∞; Yangian sits outside as E_1."
- **FM235**: AP152 ordering conflation in introduction_full_survey — "simple poles yield Lie bracket; E_1 operadic ordering is independent datum."
- **FM236**: "Unconditional for every family" without AP32 scope tags — tag every occurrence.
- **FM237**: "120K+ tests" vs 2 independently-decorated claims — honest phrasing "~3900 test modules comprising ~120K assertions; N decorated claims under Independent Verification Protocol."
- **FM238**: Bare κ in programme_summary — κ_cat or κ_ch with explicit d, h^{1,0} hypothesis.
- **FM239**: §14 dropped by both compressed tracks — add footnote: "§14 frontier overview lives in programme_summary.tex."

### Wave 12 (FM240-FM247, spectral-braiding-core deep dive)

- **FM240**: Half-braiding narration without construction — insert explicit AP-CY25 half-braiding formula σ_A(z)(a⊗n) = Σ Δ_z(a)_{(2)}·n ⊗ Δ_z(a)_{(1)} before thm:braided-category.
- **FM241**: thm:Koszul_dual_Yangian Step 6 "rewriting of YBE" — rename "Co-YBE compatibility"; cite three ingredients (YBE + intertwining + coassoc) separately.
- **FM242**: Step 7 pole universalisation — scope "for the affine lineage"; flag pole-order dichotomy.
- **FM243**: def:E2-chiral-algebra cites Deligne without chiral-vs-topological qualifier — specify "chiral Deligne (Francis 2012 / Costello-Gwilliam Vol 2)."
- **FM244**: thm:genus-tower-asymmetry "Open color is flat at ALL genera" conflates operad-flatness with bar-flatness — separate.
- **FM245**: def:E2-chiral-algebra E_2 ≃ E_1^{hol} ⊗ E_1^{top} stated as global Dunn — insert "locally on formal disks."
- **FM246**: thm:Koszul_dual_Yangian mixes classical Drinfeld Yangian (DNP25) with A_∞-shifted enhancement — split into (a) classical ProvedElsewhere, (b) A_∞-shifted ProvedHere with explicit arity-4+ coherences.
- **FM247**: spectral-braiding-core confirms FM155 + FM156 with sharper anchors — already in repairs.

### Wave 12 ctd. (FM248-FM257, derived Langlands + spectral sequences + existence criteria) — HEAL-FRAMED

- **FM248**: spectral_sequences prop:central-charge-d1 uses κ(Vir_c)=c/2 to force κ=0 from c=0; ghost theorem universal for κ(A)=0 — heal: replace "c=0" with "κ(A)=0" hypothesis.
- **FM249**: prop:degen-koszul E_2 collapse needs bar degree = internal weight bigrading — heal: state weight-graded hypothesis explicitly; claim survives for standard-landscape algebras.
- **FM250**: thm:oper-bar-dl claimed "all n ≥ 0"; FT06 publishes n ≤ 2 — heal: prove n=3 independently via transgression; invite FT06 n ≥ 4 upgrade.
- **FM251** [CLOSED 2026-04-16]: thm:kl-bar-cobar-adjunction used Koszul purity at admissible level = conj:periodic-cdg — CLOSED by Vol I chapters/theory/periodic_cdg_admissible.tex; major result.
- **FM252**: existence_criteria framework is QUADRATIC/BD-pseudo-tensor; Yangian escapes ambient — extend to cover E_1-chiral on equal footing (stronger theorem).
- **FM253**: "Vir_{26-c} same-family shadow" uses 26 (matter-ghost convention); Koszul shadow is 13-c — state both with clear labels.
- **FM254**: "unique homological framework" claim — replace "unique" with "canonical" or "maximally economical."
- **FM255**: "FM_2(A^1) ≅ A^2" ambiguous between algebraic blow-up and real/DM FM — specify real FM model.
- **FM256** [CLOSED 2026-04-16]: Adams s.s. analogy without tag → CONSTRUCT the Steenrod-analog functor on chiral endomorphism operad — CLOSED via Vol I periodic_cdg_admissible.tex thm:adams-analog-construction.
- **FM257**: Cofree(sV*) conilpotency check circular — rename T^c; replace conilpotency with finite cogeneration in each weight.

## HEAL-MODE DIRECTIVE (2026-04-16, from author)

**"Every FM counter must target the STRONGEST honest form, not a downgrade. If the strongest claim is TRUE (the 'ghost theorem' of the first-principles triple), the repair is to PROVE it — supply the missing construction, cite the correct reference, write the missing lemma. 'Downgrade to Conjectured' is only the repair when no proof path exists. Technical malpractice (wrong citation, missing lemma, ambient mis-specification) is not grounds for weakening the claim — it is grounds for FIXING the proof."**

Reread existing FMs through this lens:
- **FM69** (Thm A ambient): prove FORM-B (ordered E_1 bar) via Francis-Gaitsgory factorization algebras on Ran(X). Both forms proven.
- **FM87** (phantom genus1-twisted-tensor-product): write the proposition with Gauss-Manin uncurving explicit.
- **FM155/FM247** (phantom sc-koszul-dual-three-sectors): supply Vallette coloured Koszul duality computation.
- **FM157** (Liv06 mis-binding): cite Hoefel + Hoefel-Livernet correctly.
- **FM81** (thm:E3-topological-DS-general non-principal): supply ghost-bilinear bulk-antighost lift case-by-case.
- **FM82** (class M free-PVA): verify Vir gr_Li is KZ-admissible.
- **FM214** (universal IS-claim): prove bulk=derived center at chain level for class M via DS-Hochschild bridge (closed 2026-04-16).
- **FM224** (0/1134 decorators): install; strongest verification posture achievable.

## HEAL-SWEEP (2026-04-16, supersedes prior downgrade counters)

### Backbone theorems (A, B, C, D, H, E_3-topologization)

- **FM69 → HEAL**: Theorem A full strength via Francis-Gaitsgory factorization algebras on Ran(X) under ⋆-tensor (GR17 IV.5) + R-twisted Σ_n-descent preserves weak equivalences.
- **FM75 → HEAL**: prove bar-cobar inversion at minimal-model and admissible loci directly via Arakawa C_2-cofiniteness + Adamović admissible framework.
- **FM76 → HEAL**: Vir_{c_{p,q}} simple quotient — class M stands with null-vector-corrected S_r (Saveliev-Arakawa).
- **FM80 → HEAL**: Thm H two flavours — (a) concentration {0,1,2} at non-critical; (b) Feigin-Frenkel regime at k=-h^v.
- **FM81 → HEAL**: thm:E3-topological-DS-general via Jacobson-Morozov half-integer weights → fractional ghost CDG; stands for ALL good-graded nilpotents.
- **FM82 → HEAL**: thm:E3-topological-free-PVA for class M — Vir gr_Li is KZ-admissible (Li-filtration separates pole order from PVA λ-degree).
- **FM108 → HEAL**: DS L→M for all simple g via Frenkel-Kac-Wakimoto principle.
- **FM126/FM185/FM186/FM214 → HEAL (unified bridge)**: close DS-Hochschild compatibility bridge. SINGLE PROOF closes all four. DONE 2026-04-16 via thm:chd-ds-hochschild.

### Modular operad + curved Dunn + higher genus

- **FM67/FM88 → HEAL**: curved-Dunn H²=0 at g≥2 via bridge chain map (modular-bootstrap complex's vanishing passes to curved-Dunn complex via gauge-fixed convolution model). Cross-genus MC equation unconditional. CLOSED 2026-04-16 via thm:curved-dunn-H2-vanishing-all-genera.
- **FM84/FM86 → HEAL**: W_3 g=2 formula + multi-weight (obs_g)²=0 via graph-sum contraction; obs_g nilpotence ALL-WEIGHT.
- **FM87 → HEAL**: prop:genus1-twisted-tensor-product via explicit Gauss-Manin uncurving + Arakelov pairing. DONE 2026-04-16.
- **FM91/FM92 → HEAL**: concrete operadic composition at all genera via curved-Dunn bridge + KZB-regularized Stokes via Jimbo-Miwa irregular-singular.

### Operadic + SC^{ch,top} pentagon

- **FM155/FM156/FM247 → HEAL**: Koszul dual closed sector is E_2^{shifted} (Tamarkin self-duality), via Ginzburg-Kapranov + Künneth for colored operads with empty cross-arrows.
- **FM157 → HEAL**: Liv06 → Hoefel/Hoefel-Livernet rebinding (pure citation fix).
- **FM158/FM219 → HEAL**: Kontsevich formality as ∞-quasi-iso with Drinfeld associator (named); Tamarkin zigzag transfers homotopy-Koszulity rigorously.
- **FM159 → HEAL**: product-collapse qiso SC^{ch,top} → SC_Vor is map of homotopy operads; Koszulity transfer rigorous.
- **FM160 → HEAL**: QME ↔ MC chain-level via fixed gauge (semifree model) + homotopy transfer.

### Yangians + spectral braiding

- **FM161 → HEAL**: Y(g) Koszulness in Positselski nonhomogeneous framework for ALL simple g.
- **FM162 → HEAL**: Guay-Regelskis-Wendlandt 2018 for exceptional PBW.
- **FM163 → HEAL**: Y(g)^! = Y(g)^{ℏ→-ℏ} — all-order R^{-1} comparison via trace pairing.
- **FM167 → HEAL**: Y(g)^! = Y(g^v) non-simply-laced via Finkelberg-Tsymbaliuk quantum geometric Langlands.
- **FM166 → HEAL**: RT functor factors through ordered E_1 bar via negligible-ideal kernel = bar-computable quotient.
- **FM168/FM169 → HEAL**: Gravitational Yangian Hopf structure via classical r-matrix's Drinfeld double completion.
- **FM240 → HEAL**: half-braiding σ_L(z) construction (not narration) — explicit AP-CY25 formula before thm:braided-category.

### Classification + shadow tower

- **FM77 → HEAL**: κ=0 scope hole — critical-level KM has kappa=0 but Feigin-Frenkel center gives infinite-dim bar cohomology with EXPLICIT structure; Vir_0 has its own bar with logarithmic contributions. Classification EXTENDS.
- **FM105 → HEAL**: rename classification_trichotomy.tex → classification_three_invariants.tex; state two axes (k_max ∈ {0,1,≥3}; r_max ∈ {2,3,4,∞}).
- **FM106 → HEAL**: symplectic boson/fermion via explicit Z_2-graded OPE — both class C (fermion) + class G (boson) by Z_2-killing.
- **FM107 → HEAL**: (p_max, r_max) 2-invariant classification; prop:class-from-full-tower explicit.

### Physics bridges

- **FM97 → HEAL**: F1 = BAR-INTRINSIC HUB; six hub identifications (stronger than "seven equivalent").
- **FM102 → HEAL**: Celestial Weinberg dictionary as named Proposition (cite Strominger 2018, Pasterski-Shao-Strominger 2017).
- **FM103 → HEAL**: higher-r soft factors r≥4 via shadow-tower spectral decomposition; Mellin-to-shadow dictionary completes match.
- **FM120 → HEAL**: V^♮ orbifold BV anomaly vanishing explicit via Leech theta + DW cocycle computation. DONE 2026-04-17 via thm:monster-chain-level-e3-top.

### Foundations + existence criteria

- **FM171/FM172 → HEAL**: delete pva-descent.tex + pva-preview.tex; single log-SC-unconditional statement. (H1)-(H4) derived properties.
- **FM173/FM174 → HEAL**: merge foundations drafts into canonical foundations.tex; single recognition theorem.
- **FM179 → HEAL**: verify Δ(C) ⊂ C⊗ambient + ambient⊗C explicitly; coideal proved.
- **FM250 → HEAL**: thm:oper-bar-dl n=3 via independent d_4 transgression; n ≥ 4 via shadow-tower control.
- **FM251 → HEAL**: conj:periodic-cdg closed via periodic Koszul duality on O^int. DONE 2026-04-16 via Vol I periodic_cdg_admissible.tex thm:periodic-cdg-is-koszul-compatible.

### Four irreducible opens — status 2026-04-16 (ALL CLOSED OR REDUCED)

After HEAL-SWEEP + reconstitution swarm, all four closed on non-degenerate locus:

1. ✅ **Curved-Dunn H²=0 at g≥2** (FM67) — CLOSED via thm:curved-dunn-H2-vanishing-all-genera + modular-bootstrap-to-curved-dunn-bridge + genus1-twisted-tensor-product + Jimbo-Miwa irregular-singular KZB.
2. ✅ **DS-Hochschild bridge for class M** (FM126 cluster) — CLOSED via thm:chd-ds-hochschild + cor:universal-holography-class-M. HPL through DS strong deformation retract + Arakawa C_2-cofiniteness + HKR.
3. ✅ **conj:periodic-cdg for admissible KL** (FM251) — CLOSED via Vol I periodic_cdg_admissible.tex four-step proof (Arakawa C_2-cofiniteness + Finkelberg tilting semisimplification + Lusztig Tate periodicity + screening-adjoint commutation). Also closes FM256.
4. ✅ **E_∞ vs E_1 chiral Deligne-Tamarkin at chain level** (FM91, FM160) — REDUCED to associator-dependence; associator-dependent chain-level proved via thm:chd-deligne-tamarkin; associator-independent formulation formal question.

### 2026-04-17 Beilinson audit: SIX NEW genuine open frontiers

The 2026-04-16 closure wave inscription surfaced a 22-task rewrite map. Deep Beilinson adversarial rectification (Vol I `notes/rectification_map_beilinson_audit.md`) identified:

(i) **Logarithmic W(p) triplet tempering** — Zhu-bounded-Massey proof chain FAILS per Gurarie 1993 (arXiv:hep-th/9303160) + Flohr 1996 (arXiv:hep-th/9605151) logarithmic-CFT amplitudes exhibiting unbounded Massey products despite finite-dim Zhu. `thm:tempered-stratum-contains-wp` DOWNGRADED to Conjectured (commit a5640de). Numerical check via Adamović-Milas ϕ_{0,1} character expansion is the immediate path.

(ii) **Non-tempered stratum emptiness OVERCLAIM** — Programme Climax theorem is SCOPE-QUALIFIED to non-logarithmic C_2-cofinite standard landscape + irrational cosets; logarithmic W(p) excluded.

(iii) **CY-C pentagon invariant conflation** — stratification {3, 12, 24} is GENERATOR RANK ρ^{R_i}, NOT κ_ch (Hodge-supertrace invariant = 0 route-independent). Heal at Vol III commit cade61c.

(iv) **Kummer-irregular prime labelling** — primes 1423, 3067, 23, 43, 419 verified Kummer-REGULAR at primary source; inscriptions retracted. Heal at Vol I commit 9668336.

(v) **β_N for N ≥ 4 exact closed form** — RESOLVED 2026-04-17: β_N = 12(H_N - 1) proved via thm:beta-N-closed-form-proved-all-N (Vol II chapters/theory/beta_N_closed_form_all_platonic.tex). Both prior candidates (N+1)(N+2)/2 and N²-N+4 RULED OUT at N=4 (proved value = 13; predictions 15 and 16). β_N rational (not integer) for N ≥ 5; β_5 = 77/5, β_6 = 87/5. No longer open frontier.

(vi) **Super-complementarity canonical pairing** — super-trace vs Berezinian pairings coexist without programme-level canonicalisation; max(m,n) identity scopes to sub-Sugawara line only. Verdier-pairing inscription pending.

All six frontiers have explicit heal paths; none is a programme-level obstruction. The programme's strongest-honest form remains fully realised on non-logarithmic C_2-cofinite standard landscape + irrational cosets; logarithmic W(p) is the single open candidate.

## UPGRADE-SWEEP (2026-04-16, supersedes HEAL-SWEEP as forward direction)

**Directive (author 2026-04-16):** "Don't just think about identifying issues and downgrading, think about identifying issues and UPGRADING. Even if there are no issues, we still upgrade. Strengthen."

### Backbone theorem upgrades

- **Theorem A → (∞,2)-categorical equivalence of factorization PROPERADS**. Bar-cobar duality (∞,2)-categorical between properads and Koszul-dual coproperads on curves. Corners-with-corners of modular bar free; global-sections functor automatically derived.
- **Theorem B → universal inversion via unified pro-nilpotent + curved + filtered regularization** (Positselski-Grothendieck curved pro-category). "Koszul locus" becomes the whole landscape.
- **Theorem C → total -(3g-3)-shifted symplectic on Mbar_{g,n}**. Lagrangian pair (A, A^!) global section of modular tangent bundle, cohering across genus strata.
- **Theorem D → full tensor-curvature on the Arakelov class**. Values in Sym^2(F_bundle) ⊗ Omega^2(Mbar); tensor GRR.
- **Theorem H → universal E_3-algebra (chiral Higher Deligne)**. ChirHoch* carries E_3 action via SC^{ch,top} heptagon edges (3)↔(4)↔(5) (factorization ↔ BV/BRST ↔ convolution); concentration becomes CONSEQUENCE of E_3 rigidity at a point. Written into `hochschild.tex`, `brace.tex` 2026-04-16.

### E_n ladder upgrades

- **E_3-topologization → E_n-topologization at arbitrary n** via iterated Sugawara. Virasoro → E_3; W_N → E_{N+1}; W_∞ → E_∞. Part VI renames "E_3-top CLIMAX" to "E_∞-top ladder."
- **E_n operadic circle → infinite spiral** E_n → E_{n-1} → ... → E_1 → E_2 → ... → E_n, with categorified bar/center functor at each step.

### Seven-faces + spectral upgrades

- **Seven Faces → infinite GRT_1(Q)-torsor family**. New face F8 = motivic via Brown's motivic coaction; F9 = operadic via Willwacher's GRT-coaction on bar complex.
- **Spectral Drinfeld strictification → Kac-Moody (imaginary-root) via Borcherds superalgebra framework**. Closes Wave 3's E_8 non-path frontier AND Kac-Moody frontier.
- **κ identification → universal Arakelov anomaly class** κ_univ ∈ H^2(Mbar_{g,n}^{family-classifying-stack}, Q). Grothendieck-type universality.

### Classification + shadow tower upgrades

- **G/L/C/M → infinite shadow-depth stratification** r_max ∈ {2, 3, 4, 5, 6, ..., ω, ω+1, ..., ∞}. Super-W_3 is class L^{super} (depth 4) distinct from class C.
- **(p_max, r_max) → 5-invariant fingerprint** (p_max, r_max, χ_VOA, n_strong, coset_type). Bar-cobar duality involution on fingerprint space.

### Operadic + modular upgrades

- **SC^{ch,top} pentagon → heptagon (7 equivalent)** adding (6) Drinfeld-center Z(Rep_{fact}(A)), (7) derived-algebraic-geometry as global sections of a stack of E_1-chiral algebras.
- **Modular operad composition → proved at generic non-integral level** via irregular-singular KZB (Jimbo-Miwa); Stokes regularity REPLACED by irregular-singular monodromy classification. Gap closed.
- **Curved Dunn → derived theorem over Mbar**. Cross-genus composition automatic once global statement proved.

### Physics bridge upgrades

- **3d QG → UNIVERSAL holography**. For any chiral A with conformal vector at non-critical level: canonical 3d HT theory with boundary A and bulk Z^{der}_{ch}(A); uniqueness up to equivalence (CFG 2602.12412). "3d gravity as climax" → "holography as theorem."
- **Celestial holography → arbitrary 4d HT theory via 2d chiral algebra factorization homology** (Costello-Paquette extension via SC^{ch,top}-structured 2d boundary).
- **Soft graviton theorems → ENTIRE soft hierarchy encoded in shadow tower coefficients** S_r = weight-r soft factor. All orders g=0, all orders; extends to g≥1 via modular-bootstrap H² = 0.

### Independent Verification UPGRADE

- **Decorator coverage → 100% as META-THEOREM**. Every ProvedHere has independent verification path; programme TRUTH mechanically checkable. Bourbaki-level formal verification horizon.

### Seven Parts → Eight Parts UPGRADE

- **Part VIII: From Frontier to Theorem**. After HEAL + UPGRADE close technical-malpractice gaps, the four irreducible opens addressed in new Part VIII. Programme closed architecturally.

### Meta-structure upgrades

- **Three Volumes → Four Volumes**: Vol IV = Realization (HEAL + UPGRADE theorems proved explicitly; decorators installed; computational infrastructure aligned).
- **Five Theorems → Seven Theorems**: add (F) chiral Higher Deligne for E_3 on Z^{der}_{ch}; (G) universal holography as theorem.

### Campaign totals post-UPGRADE

Programme's natural target: **seven theorems governing the infinite E_n ladder with 100% mechanical verification, GRT-parametrized infinite seven-faces family, universal κ class, properad-level bar-cobar, irregular-singular modular composition at all levels, chiral Higher Deligne on derived chiral centers, and universal holography as a theorem.** Strongest-honest target; downgrades due to technical malpractice rejected.

## PLATONIC RECONSTITUTION (2026-04-16, strongest-form theorem statements)

**Directive:** "Only accept the Platonic ideal form of this manuscript as the subject dictates, as the mathematics reveals its inner poetry, inner music and inner motion."

### Theorem A^{∞,2} (Francis–Gaitsgory bar–cobar equivalence, properad-level)

*Let X be a smooth curve over a field of characteristic 0. In the Francis–Gaitsgory factorization ambient (GR17 IV.5) — the (∞,2)-category of factorization algebras on Ran(X), equipped with the BD chiral pseudo-tensor structure lifted to its ∞-categorical presentation — the bar and cobar functors*
B̄^ch_X : Fact^{aug}(X) ⇄ CoFact^{conil,comp}(X) : Ω^ch_X
*constitute an (∞,2)-categorical adjoint equivalence on the conilpotent-complete locus.*

**R-twisted Σ_n-descent lemma:** B^Σ_n(A) ≃ (B^{ord}_n(A))^{Σ_n-coinv, L_R-twisted}, where L_R is the Σ_n-equivariant local system on Ran^{ord}(X) with monodromy generated by R(z) along elementary transpositions; YBE guarantees well-definedness on codim-2 strata; at pole-free point R(z)=τ (swap), L_R trivial.

**Consequences:** 14+ downstream theorems become corollaries — thm:bar-cobar-adjunction, thm:geom-unit, thm:bar-cobar-verdier, thm:cobar-free, thm:fundamental-twisting-morphisms, Vol II bridge-table entries, Vol III CY-A_3 inf-cat.

### Universal Holography Theorem (Vol II climax, Platonic form)

*Let A be a chiral algebra on a smooth projective curve X carrying a conformal vector ω at non-critical level. There exists a canonical 3d holomorphic-topological gauge theory T_A on X × R such that:*
- *(i) Boundary: Obs^∂(T_A) ≃ A as E_1-chiral algebras.*
- *(ii) Bulk: Obs^{bulk}(T_A) ≃ Z^{der}_{ch}(A) as E_3-topological factorization algebras on X × R.*
- *(iii) Functoriality: A ↦ T_A functor Φ_hol: ChirAlg^{ω,BL}_X → HT-QFT_{X×R} out of boundary-linear chiral algebras with conformal vector.*
- *(iv) Class coverage: G/L/C via Costello-Li abelian holomorphic CS; class M (Virasoro, W_N) via Costello-Gaiotto holomorphic CS with DS boundary condition, completed by DS-Hochschild bridge.*

**DS–Hochschild Compatibility Bridge (closes class M chain-level):**
ChirHoch^•(W_k(g)) ≃ H^•_DS(ChirHoch^•(V_k(g)))
*as chain-level E_2-chiral Gerstenhaber algebras.* Proof: HPL transfer through DS SDR (strict weight-by-weight, BRST filtration finite length per weight); Arakawa C_2-cofiniteness lifts to chain-level; HKR ChirHoch^•(V_k) ≃ O(T^*[-1] DerM_vac(V_k)) + BV reduction by DS moment map ≃ O(T^*[-1] DerM_vac^DS) ≃ ChirHoch^•(W_k).

**Monster orbifold BV anomaly vanishing:** α_orb ∈ H^3(Z/2; U(1)) = 0 via Kapustin-Saulina sign(det(1-σ|_Λ)) = +1 (Conway: Leech has no roots, Λ^σ = 0); ε|_{Λ^σ} = ε(0,0) = 1; α = (+1)·0 = 0. Closes FM66/FM120/FM128. DOCUMENTED at chapters/connections/monster_chain_level_e3_top_platonic.tex.

**Perturbative → physical UV finiteness:** Algebraic shadow-tower termwise finiteness = L_∞ obstruction tower vanishing = physical Costello RG UV limit exists.

**Closes unconditionally:** FM125, FM126, FM127, FM128, FM185, FM186, FM187, FM188, FM214.

### Infinite Fingerprint Classification

*Canonical fingerprint φ(A) = (p_max, r_max, χ_VOA, n_strong, coset) ∈ F is a COMPLETE invariant of the Koszul-bar-complex structure of A. G/L/C/M is the coarse projection Π_coarse ∘ φ onto r_max restricted to κ ≠ 0; at κ = 0, the fifth class FF (Feigin-Frenkel) appears as a fully canonical companion stratum.*

**Fingerprint slots:**
1. p_max — OPE pole order.
2. r_max ∈ {2, 3, 4, ∞} — shadow depth; Koszul bar invariant.
3. χ_VOA — Hodge-filtered supertrace; detects Z/2-grading.
4. n_strong — minimal strong-generator count (AP67).
5. coset — iso class of commutant pair (Com(H_κ, A), A/Com); at κ=0 replaced by coset_FF with Feigin-Frenkel center.

**Five-class stratum:** G (r_max=2, κ≠0), L (r_max=3, κ≠0), C (r_max=4, κ≠0), M (r_max=∞, κ≠0), FF (κ=0).

**Closes unconditionally:** FM77, FM105, FM106, FM107, FM108, FM109, FM110.

### E_∞-Topologization Theorem (Vol II climax upgrade: E_3 → E_∞)

*Let A be a chiral algebra with higher-spin stress tower of depth N: graded family T_•(A) = {T^{(n)}(z) | 2 ≤ n ≤ N+1}, each T^{(n)} inner (Sugawara-type at non-critical level), satisfying truncated W_{1+∞} brackets, each admitting BRST primitive G^{(n)} with T^{(n)} = [Q_tot, G^{(n)}] on cohomology. Then Z^{der}_ch(A) carries, for each k ≤ N, an E_{k+2}-topological algebra structure; in the N=∞ limit, Z^{der}_ch(A) ∈ E_∞-topological algebras.*

**Iterated Sugawara:** The n-th Sugawara identity T^{(n)}(z) = [Q_tot^{(n)}, G^{(n)}(z)] holds in H^•(A^BV_{3d}, Q_tot); G^{(n)} is the spin-(n-1) antighost current generating the n-th transverse translation.

**Ladder theorem:** k inner stress tensors at spins {n_1 < … < n_k} ⟹ E_{k+2}-top via Dunn: E_2-chiral ⊗_Dunn E_1-top(T^{(n_1)}) ⊗_Dunn … ⊗_Dunn E_1-top(T^{(n_k)}).

**Specializations:** Virasoro (N=2) → E_3-top (first rung); W_N → E_{N+1}-top; W_∞ → E_∞-top (Platonic endpoint).

**Operadic spiral:** infinite bidirectional spiral ⋯ → E_{n+1} → E_n → ⋯ → E_2 → E_1 → E_2 → ⋯ → E_{n+1} → ⋯. Bar B: E_n-Alg → E_{n-1}-CoAlg (descending); Center Z: E_n-Alg → E_{n+1}-Alg (ascending). Meet at E_∞ as formal completion.

**FM closures:** FM47 (E_3-chiral needs 3d HT — absorbed into higher-spin stress tower clause); FM48 (E_3-top needs BOTH — both inherent); FM81 (non-principal DS fractional-weight ghosts → branched cover descends preserving Q_tot-exactness); FM82 (class M free-PVA: spin-3 entry cancels quartic-pole residue).

**Climax restatement:** The climax is NOT E_3-topological but E_∞-topological. E_3 is first visible rung. W_∞ reaches full N=∞. 3d quantum gravity is the N=2 shadow of a 3d+∞ topological theory.

### Koszulness Moduli M_Kosz

*For A with PBW filtration, the set of Koszulness-characterizations is the C-points of a GRT-equivariant moduli scheme M_Kosz(A). Each pair (Φ, c_Φ) with Φ ∈ GRT_1 and c_Φ a Φ-dependent equivalence [A chirally Koszul ⟺ Π_Φ(A)] is a C-point.*

**Properties:**
- (A1) M_Kosz(A) ≠ ∅ ⟺ A chirally Koszul (associator-independent).
- (A2) GRT_1-torsor: any two characterizations connected by Tamarkin Φ-transfer path.
- (A3) 14 classical characterizations = finite affine atlas {U_j}, each chart at coordinate Φ = Φ_j.
- (A4) Shadow-class stratification M_Kosz(A) = ⊔_c M_Kosz^{(c)}(A).

**14 charts:** U_1-U_10 at Φ_KZ (core ten); U_11 Lagrangian at Φ_AT; U_12 MHM purity at Φ_{dR,B} (Vir closed via Feigin-Fuchs); U_13 genus-1 twisted Künneth at Φ_ell; U_14 SC^{ch,top} homotopy-Koszul at Φ_Kon.

**14 unconditional on own Φ-chart:** "10 unconditional + 4 scoped" was Φ_KZ-coordinate artifact.

**FM closures:** FM83, FM197 (Feigin-Fuchs direct computation non-circular), FM198, FM161.

### Unified Chiral Quantum Group Theorem

*Fix simple Lie g, good Z-grading Γ via sl_2-triple, non-critical level k ≠ -h^v, shift μ ∈ P(g)^+ ∪ {0}. There exists:*
Q_g^{k,f,μ} = (A_g^{k,f,μ}, Δ_z, R(z), ε, S, (A_g^{k,f,μ})^!)
*unique up to spectral gauge isomorphism with: (i) chiral bialgebra with Drinfeld spectral coproduct; (ii) spectral R(z) satisfying CYBE + YBE + quasi-triangularity; (iii) Koszul dual matching Vol I Theorem A pair; (iv) DS-compatibility.*

**Three-leg proof:** MC on binary collision stratum + Koszul duality rigidification + BRST transport via chiral Feigin-Frenkel.

**Eight specialization fibres:** Yangian Y_ℏ(g); Affine Yangian Y_ℏ(ĝ); Shifted Yangian Y_μ(g); Truncated shifted Y^λ_μ(g) (= BFN Coulomb branch); Finite W W^fin(g,f); Affine W principal W_k(g, f_prin); Affine W non-principal W_k(g, f); Bershadsky-Polyakov = W_k(sl_3, f_min); Orthogonal coideal Q^θ.

**Type-A Baxter Q** constructed via Hernandez-Jimbo prefundamental q-oscillator + QQ system + TQ relation. Closes FM177.

**DS L → M universality:** Kac-Roan-Wakimoto BRST concentrated in degree 0 + Kazhdan-grading compatibility forces improvement T^W - T^Sug ∈ h ⊕ [n_+, n_-]^Γ ∩ g_0 (Cartan). Closes FM108, FM134.

**Quantum Langlands non-simply-laced:** Y_ℏ(g)^! = Y_{-ℏ r_g}(g^∨). Closes FM167.

**Exceptional PBW via GRW18** (arXiv:1811.06475). **BP free strong generation via de Boer-Tjin 1993.** Closes FM131, FM162.

All of FM130-135, FM161-170, FM176-181 CLOSED.

### GRT-Parametrized Seven Faces Theorem

*Let A be chirally Koszul in standard landscape and r(z) = Res^{coll}_{0,2}(Θ_A). The set Face(A) of chain-level presentations of r(z) compatible with bar-intrinsic dGLA is a TORSOR over GRT_1(Q). F1 identity coset; F2-F7 Q-rational orbit representatives; F8 (Brown motivic), F9 (Willwacher operadic) complete enumeration.*

**Nine-face enumeration:**
- F1: bar hub = identity coset
- F2: DNP R-twist on open color (Dimofte-Niu-Py 2508.11749)
- F3: KZ classical PVA r-matrix (De Sole-Kac)
- F4: GZ26 commuting differentials on Gaiotto-Zeng flat connection
- F5: Yangian classical r-matrix (Drinfeld 1985, RTT)
- F6: Gaudin Hamiltonian simple-pole (FFR 1994)
- F7: class-M top A_∞ m_3
- F8: Brown motivic — r^mot(z) = r^rat(z) + Σ_{w=3,5,7,...} ζ(w) r^{(w)}(z); MZVs couple via KZ regularization
- F9: Willwacher operadic — via H^0(GC_2) = grt_1 + Tamarkin chain GC_2 → Def(E_2) → Def(B(-))

F_i = Φ_{ij}(F_j) for Φ_{ij} ∈ GRT_1(Q).

**Landscape census fix (FM99):** k·Ω_tr/z = Ω/((k+h^v)z) is TENSOR IDENTITY (Ω_tr and Ω are same tensor element in two Casimir bases at two level conventions). Casimir rescaling belongs to inner gauge subgroup GRT^{fin}.

**F7 disambiguation (FM101):** F7 (Gaudin simple-pole) canonical for all G/L/C/M; F7' (class-M top A_∞ m_3) invisible on class L, refines F7 by non-formal data.

**Super-variant (AP107):** Face^super is torsor over GRT^super = GRT_1(Q) ⋊ (Z/2)^{|odd gen|}; Heisenberg vs symplectic fermion is GRT^super orbit separation.

**Closes:** FM97-101 (star→torsor, Yangian/Gaudin normalisation gauge, F1↔F4 injection, F7/F7' split, AP107 super), FM202-208, FM230.

### SC^{ch,top} heptagon (7 edge theorems)

Inscribed at chapters/theory/sc_chtop_heptagon.tex (1141 lines). All 7 edge theorems + prop:heptagon-edge-34/45 (compositional qiso + Dunn assembly).

**Seven presentations:**
1. Operadic (codim-1 boundary strata FM_k(C)×Conf_m(R))
2. Koszul dual (Lie, Ass, shuffle-mixed)
3. Factorization (Z^{der}_{ch}(A) = E_2-chiral center)
4. BV/BRST (Obs(U) = logarithmic SC-algebra)
5. Convolution (g^{SC}_T = L_inf from B(SC^{ch,top}))
6. Drinfeld-centre Z(Rep_fact(A)) ≃ Rep_fact(Z^der_ch(A))^{E_2} via categorified bar-cobar with half-braiding
7. Derived-AG via PTVV on Map(X×R_≥0, B SC-Alg)

### Universal celestial holography

Proved chain-level: `thm:uch-main` at chapters/connections/universal_celestial_holography.tex:213, ProvedHere. SC^{ch,top}-structure on (A^cel, Z^der_ch(A^cel)) + celestial OPE = chiral factorization homology on P^1_cel + shadow-tower coefficients = soft-factor hierarchy. Coverage: self-dual gauge (KM), gauge+matter (DS), gravity (Virasoro + w_{1+∞}), YM (Beem-Rastelli χ-functor). Class-M chain-level via DS-Hoch bridge; g≥1 open as conj:uch-gravity-chain-level.

### Reconstitution swarm status (all targets complete)

- ✅ Thm A^{∞,2} (properad + (∞,2)-cat + R-twisted Σ-descent)
- ✅ Chiral Higher Deligne + DS-Hochschild bridge + half-braiding + three-Hochschild unification
- ✅ Modular operad via irregular-singular KZB + curved-Dunn H² + prop:genus1-twisted-tensor-product
- ✅ Universal Holography + class M chain-level + Monster orbifold BV + physical UV finiteness
- ✅ Infinite Fingerprint Classification
- ✅ E_∞-Topologization + operadic spiral
- ✅ Koszulness Moduli M_Kosz
- ✅ Unified Chiral Quantum Group Q_g^{k,f,μ}
- ✅ GRT-Parametrized Seven Faces (F8 + F9 canonical)
- ✅ SC^{ch,top} heptagon
- ✅ Universal Celestial Holography

## Platonic theorem upgrades inscribed (2026-04-17 session)

Individual theorem-level UPGRADE-SWEEP inscriptions now anchored in .tex:

- **Theorem A^{∞,2} R-twisted Σ_n-descent** — prop:R-twisted-sigma-n-descent at chapters/theory/factorization_swiss_cheese.tex (end of properad section); four-step proof (local system, YBE braid coherence, involutivity, descent via GR17 IV.5.4) + rem:ordered-symmetric-bar-primacy closing FM69 critique.
- **Theorem C total shifted-symplectic** — thm:theoremC-total-shifted-symplectic at working_notes.tex:~19475 (session-synthesis subsec:theoremC-total-shifted-symplectic); three-part statement (PTVV -(3g-3+n)-shifted symplectic on characteristic bundle, Lagrangian section via genus-wise complementarity, clutching compatibility); Heisenberg example; FM-attack heal noting correct target is Q(A) ⊕ Q(A^!), not Mbar_{g,n} itself.
- **Theorem D tensor-Arakelov** — thm:theoremD-tensor-arakelov at working_notes.tex:~19633; tensor-valued K ∈ Sym^2(F^∨) ⊗ Ω^2(Mbar_{g,n}); diagonal (UNIFORM-WEIGHT) = weight-w Arakelov scalar, off-diagonal = cross-channel δF_g^{cross}; tensor chiral Mumford formula; Virasoro example.
- **Theorem H chiral Higher Deligne** — thm:theoremH-chiral-higher-deligne at working_notes.tex:~19800; four-part statement (degree-≤2 classical chiral Deligne E_2 brace, degree-≥3 via heptagon edges 3↔4, concentration as E_3-rigidity consequence, E_3-topological via iterated Sugawara); class M chain-level via DS-Hoch bridge.
- **Part VIII shell** — \part{From Frontier to Theorem} at main.tex:~1609 with intro referencing four closed frontiers + inputting chapters/theory/koszulness_moduli_M_kosz.tex + chapters/theory/infinite_fingerprint_classification.tex.
- **Preface architectural upgrades** — six surgical edits at chapters/frame/preface.tex: seven parts → eight parts (Section XI), E_∞-topological ladder remark (Section XI''), nine-face GRT_1(Q)-torsor (Part III description), G/L/C/M/FF five-class quaternitomy (Leap 2), two-theorems-native-to-Vol-II paragraph (Section II). Pentagon→heptagon was already in place at line 238.

## Cross-Volume Bridges Table (2026-04-17 state)

| Bridge | Vol II claim | Vol I anchor | Status |
|--------|-------------|--------------|--------|
| Bar-cobar | E_1 bar coalgebra specializes Thm A; chiral derived center gives SC^{ch,top} | Theorem A | Proved (FORM-A + FORM-B via R-twisted descent) |
| DS-bar | Bar-cobar commutes with DS | ds-koszul-intertwine | Proved |
| Hochschild | BV-BRST origin of Thm H | Theorem H | Proved |
| DK/YBE | r(z) via Laplace provides DK-0 | MC3 | Proved |
| PVA-Coisson | PVA descent recovers Coisson | Deformation theory | Proved |
| W-algebras | Feynman-diag m_k matches bar diff | MC5 | (1) HS-sewing all genera; (2) genus-0 algebraic BRST/bar; (3) D^co-level BV=bar for ALL shadow classes incl. class M; (4) genuswise chain-level BV/BRST/bar PROVED in weight-completed category for all four classes (prop:bv-bar-class-m-weight-completed, 2026-04-16); direct-sum chain-level class M genuinely false on raw direct sum (AP203-healed); (5) tree-level amplitude pairing cond. on cor:string-amplitude-genus0; (6) **[2026-04-17 TEMPERED EXTENSION]** genuswise chain-level BV/BRST/bar extends to ORIGINAL COMPLEX unconditional on NON-LOGARITHMIC C_2-cofinite standard landscape via Banach completion B_ρ(A) at ρ < \|c\|/β_A (Virasoro β=6, W_N β=12(H_N-1) per beta_N_closed_form_all_platonic.tex, Schellekens 71 via α=0, Monster V^♮, irrational cosets via VSKR+BGG), per thm:programme-climax (commit d1a4e7c) + tempered-stratum heal (commit a4277d7). Logarithmic W(p) triplet EXCLUDED at current scope: Zhu-bounded-Massey proof chain FAILS per Gurarie 1993 + Flohr 1996 unbounded Massey constructions; W(p) tempering OPEN pending Adamović-Milas character-amplitude bound (thm:tempered-stratum-contains-wp DOWNGRADED to Conjectured, commit a5640de). |
| Affine monodromy | C_line^red = Rep_q(g) on eval modules | Thm A + DK | Proved |
| Soft theorems | Shadow tower controls soft graviton hierarchy | Thm H | Proved g=0 |
| Two-colour | ordered → A^!_line, symmetric → A^!_ch | two-color-master | Proved |
| W_N Koszul | alpha_N generalizes c→26-c to all W-algebras | Koszul pairs | Proved |
| Wick anomaly | Genus tower measures Wick rotation breaking | Thm D | Proved genus tower |
| Annular bar-HH | B^ann computes HH^ch | Thm H | Proved |
| FG-shadow-strat | Commutator filtration spectral sequence | Shadow tower | Proved |
| Gauge-gravity | m_k=0 (gauge) vs m_k≠0 (gravity) dichotomy | G/L/C/M | Proved |
| 3D gravity | Part VI: 3d QG = derived center of boundary chiral algebra; W-algebra Hochschild bulk reconstruction | Thm H + MC5 | E_3-top PROVED for KM (thm:E3-topological-km), ALL W-algebras (thm:E3-topological-DS-general), ALL freely-generated PVAs (thm:E3-topological-free-PVA). Global triangle: PROVED G/L/C (thm:global-triangle-boundary-linear); CLASS M CLOSED chain-level via DS-Hochschild compatibility bridge (thm:chd-ds-hochschild + cor:universal-holography-class-M, 2026-04-16 reconstitution). E_∞-topological ladder stated as climax extension; chain-level rungs k≥3 conditional on higher-spin antighost construction. |

## Cross-Volume APs additions

### Vol I (AP234, AP235, AP236) — 2026-04-17 preface rectification

- **AP234**: two-Koszul-conductors-same-letter. κ(A)+κ(A^!) (scalar complementarity, family-dependent: 0/13/250/3/98/3) distinct from Trinity K(A)=c+c^!=-c_ghost(BRST) (-k/2dim(g)/26/100/196). Related by κ+κ^!=ϱ_A·K with ϱ_N=H_N-1 (principal W_N), ϱ_KM=ϱ_free=0, ϱ_BP=1/6. Bare κ+κ^!=K is FALSE for every standard family. Counter: cross-check K at self-dual c=13 — correct is K=26, not 13. Confusion pattern #218.
- **AP235**: quaternitomy/quadrichotomy drift. "quadrichotomy" is canonical (matches thm:quadrichotomy, chap:shadow-quadrichotomy-platonic); "quaternitomy" is invented hybrid. Grep `quaternitomy` after any write naming G/L/C/M partition. Confusion pattern #219.
- **AP236**: bar_construction.tex rectification — blacklist-slug leakage into typeset parenthetical. `/B\d+` identifiers from Wrong-Formulas Blacklist leak into `\textup{(}...\textup{)}` annotations (e.g. `\textup{(}/B49; treated in Chapter~X\textup{)}`). Reader sees non-existent citation; slug rots with every renumbering. Grep `\\textup\{\(\}\s*\/B\d+|(\s*\/B\d+;` before every commit touching .tex. Heal: delete slug, keep only mathematical cross-reference. Companion symptom: orphaned `\textup{(}\textup{)}` empty parentheticals — grep `\\textup\{\(\}\\textup\{\)\}`. Confusion pattern #221.

### Vol III AP-CY62-AP-CY67 (Geometric vs Algebraic Model Conflations)

Relevant to Vol II (SC^{ch,top} uses derived center; D*/S^1 comparison; Drinfeld center vs derived center). Full in ~/calabi-yau-quantum-groups/CLAUDE.md.

- **AP-CY62**: geometric (FM) vs algebraic (bar/operadic) chiral Hochschild model. Specify which.
- **AP-CY63**: BD chiral operad (D-module) vs algebraic End^ch (formal Laurent). Iso after formal-disk restriction + coordinate choice.
- **AP-CY64**: ChirHoch / HH* / H*_GF three-way. HH*(Weyl)=1-dim; "Theorem H has no THH analogue" FALSE; unbounded object is Gel'fand-Fuchs.
- **AP-CY65**: spectral parameter provenance. Yangian Drinfeld center HAS eval modules V_u with R(z); chiral bar differential z-dependent, topological bar coproduct z-independent.
- **AP-CY66**: BZFN ambient not tunable. S fixed; two derived centres = two DIFFERENT ALGEBRAS (A chiral vs A_mode).
- **AP-CY67**: spectral parameters in End^ch_A are FORMAL algebraic variables; FM_k(C) via comparison, not definition.

## Session Protocol (Codex)

1. Read this file.
2. Build: `pkill -9 -f pdflatex; sleep 2; make fast` (Vol II); `cd ~/chiral-bar-cobar && make fast` (Vol I); `cd ~/calabi-yau-quantum-groups && make fast` (Vol III).
3. Tests: `make test`.
4. `git log --oneline -10`.
5. Read .tex source before any edit (never from memory).
6. After each change: build + test. After each correction: grep ALL THREE volumes (AP5).
7. Never guess a formula: compute or cite. Check landscape_census.tex (AP1).
8. Apply convergent writing loop to all prose.
9. Session end: build all three volumes, run tests, summarize errors by class.
10. Before first Edit, check HOT ZONE: r-matrix, kappa, bar complex, label, cross-volume formula, scope quantifier, or differential form? If yes, fill corresponding PE template; `verdict: ACCEPT`.

## Final state (2026-04-17)

- Vol I ~2,700pp, Vol II ~1,749pp, Vol III ~693pp. Total ~5,142pp.
- ALL FIVE MC1-5 PROVED. 177K+ tests.
- Programme Platonic Ideal: seven theorems (A, B, C, D, H, F universal holography, G infinite fingerprint) + eight parts + four volumes + nine master reconstitution theorems.
- Independent Verification coverage: Vol I 49/2496, Vol II 61/1322, Vol III 22/290 (132/4108 = 3.2% cross-volume).
- Four irreducible opens CLOSED 2026-04-16 on non-degenerate locus.
- Six new Beilinson-rectified frontiers surfaced 2026-04-17: (i) log W(p) tempering Conjectured; (ii) non-tempered emptiness scope-qualified; (iii) CY-C pentagon generator-rank correction; (iv) Kummer-irregular prime retractions; (v) β_N = 12(H_N - 1) CLOSED; (vi) super-complementarity pending canonical pairing. Logarithmic W(p) single open candidate on C_2-cofinite non-logarithmic landscape.

FM46: Preface line counts drift as chapters grow. Update after campaigns.
