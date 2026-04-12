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

## Task Intake - Prompt Geometry

Before any nontrivial work, lock these seven items:

1. the exact target file, theorem, formula, bridge, or live surface;
2. the task type: question-answering, audit, rectification, formula verification, build triage, or frontier synthesis;
3. the convention bridge: grading, shifts, OPE modes versus lambda-brackets, open/closed colors, genus and arity scope, Vol I versus Vol II versus Vol III normalization;
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

### Dirty Collision Surface Snapshot (2026-04-10)

This snapshot is a prior, not permission to skip `git status`.

- Vol I dirty surface is compute-heavy right now: `AGENTS.md`, eight chapter `.tex` files, twenty-six `compute/lib` files, twelve tests, thirteen standalones, many PDFs, and build logs are dirty.
- Vol II dirty surface is concentrated: `chapters/connections/thqg_perturbative_finiteness.tex` plus rebuilt PDFs are dirty.
- Vol III dirty surface is bridge-heavy: `chapters/connections/cy_holographic_datum_master.tex`, `chapters/examples/toroidal_elliptic.tex`, `chapters/theory/introduction.tex`, seven `compute/lib` files, six tests, two physics notes, PDFs, and `main.log` are dirty.

Rule: rerun `git status --short` across every repo you touch before trusting any narrative summary. Dirty files are first-class collision surfaces, not background noise.

## Cross-Volume Anti-Pattern Scope

All shared anti-patterns remain live:

- Vol I `CLAUDE.md`: `AP1` through `AP141` for the shared formula, status, propagation, and workflow hazards.
- Vol II `CLAUDE.md`: `V2-AP1` through `V2-AP35` for the local `E_1/E_infinity` hierarchy, lambda-bracket, standalone, and connective-drift hazards.
- Vol III `CLAUDE.md`: `AP-CY1` through `AP-CY19` for center discipline, conditionality propagation, CY3 existence boundaries, and cross-volume bridge hazards.

`AGENTS.md` compresses them into a smaller family-level operating surface. If a task touches one of those domains, open the relevant `CLAUDE.md` slice and the matching skill before editing.

## Claude-To-Codex Parity Map

Claude-side workflows in this repo must have an explicit Codex-side home.

### Command / Skill parity

- Claude `/audit` -> Codex `$vol2-deep-audit`
- Claude `/rectify` -> Codex `$vol2-beilinson-rectification`
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
- genus/arity/filtration/family scope;
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
- Vol III bridge statements may carry conditionality from unconstructed CY3 objects.

## Codex Local Infrastructure

Repo-local Codex playbooks live in `.agents/skills/`:

- `$vol2-deep-audit`
  Findings-first mathematical audit and review surface.
- `$vol2-beilinson-rectification`
  Deep audit/rectify/fortify loop on a chapter, theorem, or live surface.
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
