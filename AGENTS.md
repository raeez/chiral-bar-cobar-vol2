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

### SC^{ch,top} Is Not E_3; SC Is The Generic Case

SC^{ch,top} is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply to coloured operads. E_3 requires topologization: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL (NOT E_3-chiral). Without conformal vector: stuck at SC^{ch,top}. At critical level k = -h^v: Sugawara undefined, topologization fails.

SC^{ch,top} is the GENERIC case. E_3-topological is a SPECIAL CASE requiring conformal vector. Most chiral algebras do NOT have conformal vector (critical level KM, E_1-chiral algebras, CY functor outputs). SC^{ch,top} must be understood as a first-class object with five redundant presentations: operadic, Koszul dual, factorization, BV/BRST, convolution.

Status (updated 2026-04-13):
- thm:E3-topological-km: PROVED for affine KM V_k(g) at non-critical level (Costello-Li + Sugawara antighost).
- thm:E3-topological-DS: PROVED for ALL W-algebras via principal DS (Costello-Gaiotto + DS-transported antighost).
- thm:E3-topological-DS-general: PROVED for ALL W-algebras via ANY nilpotent (improvement term is always Cartan).
- thm:E3-topological-free-PVA: PROVED for ALL conformal VAs with freely-generated PVA associated graded (Khan-Zeng 3d Poisson sigma model + half-space BV).
- conj:E3-topological-general: CONJECTURAL only for non-free PVAs. Monster VOA V^♮: orbifold route identified (rem:monster-orbifold-route) — V_Leech^+ is E₃-top NOW (Z/2-invariants of E_n preserve E_n); full V^♮ conditional on orbifold BV of abelian CS (bounded, one paper).
- SC^{ch,top} pentagon: ALL 10/10 edges proved (thm:pentagon-factorization-convolution via direct Koszul duality, bypassing operadic Künneth).
- Modular operad: genus-0 product decomposition PROVED; π_1(Σ_g) PROVED for all affine KM at all genera (KZB flatness); COMPOSITION ASSOCIATIVITY PROVED at genus 0 all levels + all genera integrable levels (thm:affine-composition-associativity, KZ pentagon + KL regularity); EQUIVARIANCE PROVED (prop:qt-equivariance, quasi-triangularity + YBE); UNITALITY PROVED all genera all shadow classes (prop:modular-operad-unitality, unit vertex simply connected → Mon(R)=id). Full modular operad for Heisenberg: PROVED (prop:heisenberg-full-modular-operad). Sole remaining gap: composition at generic non-integral level, genus ≥ 1 (Stokes gap: KZB regularity at M̄_{g,n} boundary divisors).
- Global triangle: PROVED for classes G/L/C (boundary-linear families). OPEN for class M (Virasoro, W_N). Gap: DS-Hochschild compatibility (HPL transfer for RHom through DS SDR).
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

### Three Hochschild Theories

(i) Topological HH: E_1-algebra input -> E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input -> concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input -> E_2 with CY shifted Poisson. The geometry determines which Hochschild: curve X -> chiral, R -> topological, CY category -> categorical. NEVER conflate. Bare "Hochschild" MUST carry qualifier (chiral/topological/categorical) in non-historical contexts.

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

- Vol I: FRONTIER.md and CLAUDE.md updated with Vol II session results (page count 1,704pp, E_3-top hierarchy, pentagon 10/10, modular operad breakthroughs). Compute surface unchanged.
- Vol II: CLEAN working tree. All worktrees pruned. 1,704pp, 0 errors. Session produced 17 theorems, FM58-FM68, AP176-AP182, 25 arXiv papers, ~3,000 lines new content across 20+ files. All committed.
- Vol III: ~533pp, 30,613 tests, ~410 engines. CY-A_3 PROVED (inf-cat). K3 abelian Yangian PROVED. ZTE correction EXISTS. AP-CY35-40 added.

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
- AP175: Pentagon of equivalences. UPDATED 2026-04-12: all 10/10 pairwise equivalences PROVED (thm:pentagon-factorization-convolution closes the last edge via direct Koszul duality, bypassing operadic Künneth). The star topology through the operadic hub provides independent verification for each pair.

**Session 2026-04-12 Corrections (AP176-AP182):**

- AP176: E₁ fiber integration uses flatness, NOT Cauchy. The quasi-isomorphism B^{D*}(A) → B^{S^1}(A) holds for E₁ algebras by FLATNESS of the shifted KZ connection + homotopy invariance of monodromy (topological argument). Cauchy's theorem does not apply to formal Laurent series. The retraction ρ_t is non-holomorphic and cannot appear in the proof. CORRECT argument: flat connection → holonomy depends only on homotopy class → all circles in C* are homotopic → Mon(R) radius-independent.
- AP177: lem:operadic-kunneth chain-level decomposition is WRONG at chain level. The bar differential of SC^{ch,top}_mix has cross-terms d_mix from open edge contractions between mixed vertices (the map μ₁ combining closed inputs). The CORRECT statement is: the decomposition holds on the ASSOCIATED GRADED with respect to the closed-input-excess filtration. The pentagon theorem does NOT depend on this lemma (direct Koszul duality suffices).
- AP178: Modular operad (iii) is NOT proved. thm:modular-bar proves D²=0 for the ABSTRACT modular bar datum. The concrete operadic associativity of O^{A_∞-ch} clutching maps (iterated B^ann sewing with R-matrix monodromy) is OPEN. Even genus-1 clutching (constr:genus1-ainf-chiral-operations) is CONJECTURAL. π₁ well-definedness is PROVED (prop:affine-modular-operad-all-genera) but is necessary, not sufficient.
- AP179: Khan-Zeng covers ALL freely-generated PVAs. For any conformal VA whose Li-filtration associated graded is a freely-generated PVA, the Khan-Zeng 3d Poisson sigma model provides the 3d HT bulk, and the conformal vector upgrades to fully topological. This covers ALL standard families (G, L, C, M). conj:E3-topological-general is open ONLY for non-freely-generated VAs (Monster VOA).
- AP180: Eberhardt Route D for R=PT. Eberhardt (arXiv:2309.11540) proves uniqueness of the fusion kernel via difference Galois theory for b² irrational. The bar-cobar R-matrix satisfies the same shift equations (pentagon + degenerate eigenvalues, both proved). Gap reduces to: meromorphicity of bar-cobar R-matrix in external momenta. Level-by-level rationality PROVED (prop:level-rationality-R-bar).
- AP181: Global triangle sharp boundary. PROVED for classes G/L/C (thm:global-triangle-boundary-linear). OPEN for class M only. The class M gap reduces to DS-Hochschild compatibility: HPL transfer for RHom through the DS SDR (rem:class-M-DS-transport-strategy).
- AP182: Curved Dunn three-level refinement. Level 1 (genus 0): PROVED. Level 2 (obstruction theory): obstruction in H²(Hom(B(E₁^tr), gr^g(B_mod(SC)))). Level 3 (twisted Künneth): full modular bar = twisted tensor product B_mod(SC) ⊗^{Mon(R)} B(E₁^tr). Genus-1 twisted tensor product PROVED (prop:genus1-twisted-tensor-product). Full genus tower OPEN.

## Cross-Volume: Vol III Final Session Impact (2026-04-13)

Vol III deployed ~170 agents in the final session (cumulative: ~533pp, 30,613 tests, ~410 engines). Key Vol II-relevant results:

- **E_1-chiral bialgebra verified at all spins for K3 Yangian**: axioms (H1)-(H5) verified with 80+ tests across e1_chiral_bialgebra_engine, chiral_coproduct_spin3_engine, wilson_line_coproduct_engine, sl2_matrix_lax_engine, and k3_nonabelian_coproduct. Universal coproduct from Miura: Delta_z(e_s) = sum C(N_R-b,k) z^k e_a^L*e_b^R. Coassociativity trivial via Miura multiplicativity. Averaging-forgets-Hopf PROVED. Vol II cross-ref: rem:e1-chiral-bialgebra-vol3 (foundations_recast_draft.tex).
- **Swiss-cheese derived inf-categorical formulation**: the factorization tensor product ⊗_{E_1,z} = colim over ordered configs is NOT symmetric, IS strictly associative (ordered config space contractible). np.kron = E_inf quotient kills Hopf (AP-CY23). This is the concrete E_1 content of the SC^{ch,top} datum.
- **Wilson lines = stratified FH defects**: Wilson line coproduct engine (30 tests) implements Delta_z on Wilson line observables, connecting Vol II's abstract SC^{ch,top} defect language to 5d/6d hCS constructions.
- **Shadow tower = A_inf coproduct corrections**: S_k = coefficient of delta^{(k)}. Shadow-Feynman dictionary: L-loop = S_{L+1}. Class M Borel summability PROVED.
- **ZTE failure**: factored S=RRR fails ZTE at O(kappa^2). E_3 corrections exist (rank 35/36). Connects to A_inf coproduct via shadow tower.
- **E_2 -> E_3 promotion**: derived center HH*(B,B) via higher Deligne, NOT iterated Drinfeld center. 3d->5d->6d = E_1->E_2->E_3.

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
