# AGENTS.md — Volume II: A∞ Chiral Algebras and 3D Holomorphic-Topological QFT

## Charter

Volume II is not a prose production line. It is a live theorem surface under adversarial verification.

The job is to make false claims die quickly, make true claims more precise, and make the proof architecture stronger after every pass.

Success means:
- every nontrivial claim is either proved, correctly sourced, computationally verified, or explicitly downgraded;
- every edit improves the live manuscript surface, not merely its rhetoric;
- every broad slogan is tethered to exact scope;
- every correction propagates to the places where the old claim was still being sold.

Failure modes:
- preserving elegance by hiding a gap;
- copying a formulation across files without rechecking conventions;
- treating status tags, repetition, or prior confidence as evidence;
- letting tool efficiency outrank mathematical completeness.

## What The Engine Computes

Volume I built the categorical logarithm: the bar construction `B(A)` for chiral algebras on curves, with theorems proving existence, inversion, branch structure, leading coefficient, and coefficient ring. Volume II reads that machine in three dimensions.

The bar complex carries two structures:
- a differential `d_B` from OPE residues on `FM_k(C)`, encoding the holomorphic chiral product;
- a coproduct `Delta` from ordered deconcatenation on `Conf_k(R)`, encoding the topological interval-cutting.

The differential lives in the `C`-direction; the coproduct lives in the `R`-direction. A bar element of degree `k` is thus parametrized by `FM_k(C) x Conf_k(R)`, the product of holomorphic and topological configuration spaces.

This product is the operadic fingerprint of a 3d holomorphic-topological QFT on `C_z x R_t`, where observables factorize holomorphically in `z` and associatively in `t`. The two-colored Swiss-cheese operad `SC^{ch,top}` has operation spaces `FM_k(C) x E_1(m)`. The bar differential is the closed color. The bar coproduct is the open color. Open-to-closed is empty: bulk restricts to boundary, not conversely.

Critical distinction:
- The bar complex does **not** equal the bulk algebra.
- The bar complex presents twisting morphisms and Swiss-cheese couplings.
- Bulk observables are the chiral derived center `Z^{der}_{ch}(A) = C^bullet_ch(A_b, A_b)` of a boundary chart, Morita-invariant in the open-sector factorization dg-category.

At genus `g >= 1`, the curved structure is essential: the non-vanishing of higher `A_infinity` operations is the curved bar structure `d^2 = kappa(A) * omega_g`. Formality fails because the logarithm acquires monodromy.

## The Metacognitive Stack

This repository now uses a five-layer Codex-native stack:

1. `AGENTS.md`
   Constitutional layer: invariant truths, task routing, scope guardrails, convergence criteria.
2. `.agents/skills/`
   Progressive-disclosure playbooks for rectification, verification, propagation, build triage, and frontier research.
3. `.codex/hooks.json`
   Deterministic guardrails for session routing, destructive shell blocking, verification nudges, and convergence enforcement.
4. `compute/audit/linear_read_notes.md`
   Persistent findings ledger. If a nontrivial audit or rectification happens, the result belongs here.
5. The live truth surface
   `main.tex`, the active `\input` graph, the dirty diff, build logs, compute/tests, and the narrowest executable slice that can falsify the claim.

Architectural rule:
- Keep root instructions load-bearing and compressive.
- Put long workflows into skills.
- Put deterministic enforcement into hooks.
- Never bloat the constitutional layer with playbook detail that can live in progressive disclosure.

## Codex-Native Operating Stance

This file is optimized for Codex/GPT-5.4 style agentic work:

- Bias toward action and closure.
  Default deliverable is a verified result, not an outline.
- No plan theater.
  Plans are internal scaffolding and must terminate in edits, checks, or an explicit blocker.
- Persistent tool use.
  Do not stop because the first plausible answer sounds good. Stop when the relevant verification has passed or a concrete blocker has been isolated.
- Dependency-first execution.
  Read before editing. Verify prerequisites before downstream actions.
- Parallel evidence gathering.
  Batch independent reads, greps, log checks, and targeted tests. Synthesize between batches.
- Skill-first specialization.
  If the task matches a repo skill, use it instead of re-deriving the workflow from scratch.
- Better workflow beats more raw reasoning.
  Prefer tighter prompts, better decomposition, stronger verification, and cleaner tool routing before turning reasoning effort up.
- Treat `AGENTS.md`, `CLAUDE.md`, specs, notes, and prior agent prose as operational guides, not mathematical evidence.

Starting posture for Codex:
- `medium` reasoning is the default interactive setting.
- Escalate to `high` or `xhigh` only for load-bearing proof surgery, nonlocal architectural rewrites, or stalled frontier synthesis after the loop itself has already been sharpened.

## Truth Hierarchy

The order of trust in this repo is:

1. A local proof whose nontrivial steps can be named and checked.
2. An exact citation to a result that really states the needed claim under the needed hypotheses.
3. An independent computation or test that genuinely verifies the mathematical statement being used.
4. Cross-surface consistency between theorem, proof, example, compute layer, and build/test output.
5. Prose explanation.

Not evidence:
- confidence;
- repetition across files;
- a claim-status macro by itself;
- inheritance from older drafts;
- "standard" without the standard being named and applicable.

### Status Ledger

Every substantial statement must fall into one of these buckets:
- proved here;
- proved elsewhere;
- consequence of `Definition def:log-SC-algebra`;
- conditional on `Theorem thm:physics-bridge`;
- conjectural;
- heuristic;
- open.

If the statement changes, update the theorem environment, claim-status tag, surrounding prose, and downstream advertisements in the same session.

## Live Truth Surface

Prefer the live surface over archival memory:

- `main.tex`
- the files currently `\input`'d
- the current git diff
- current build logs and generated warnings after a clean-enough rerun
- the narrowest relevant compute modules and tests
- superseded files only as collision surfaces when they still advertise the same claim

Default read order for nontrivial work:
1. target file;
2. local neighboring context;
3. active `\input` map from `main.tex`;
4. dirty diff;
5. relevant compute/tests;
6. propagation surface across Vol I, Vol II, and `~/calabi-yau-quantum-groups` when the claim is cross-volume.

## The Resonance Loop

For any nontrivial task, run this loop until convergence.

### 0. Scope Lock

Identify:
- the exact target statement or surface;
- labels, hypotheses, and dependencies;
- whether the task is question-answering, audit, rectification, fortification, compute verification, or frontier synthesis.

Start with a short progress update naming the target and the first verification step. For substantial work, register the loop in `update_plan`.

### 1. Invariant Lock

Before trusting any local argument, lock the conventions:
- grading and shifts;
- bar/cobar/Koszul-dual object identity;
- open/closed color directionality;
- lambda-bracket versus OPE-mode conventions;
- genus/arity/filtration/family scope;
- Vol I versus Vol II terminology.

### 2. Read The Surface

Read the live target before editing anything. Never patch by pattern alone.

### 3. RED Pass

Attack logic and mathematics:
- hidden hypotheses;
- circularity;
- sign or degree errors;
- formula drift;
- overclaimed biconditionals;
- false identifications.

### 4. BLUE Pass

Attack consistency:
- theorem/proof mismatch;
- label or dependency drift;
- stale status prose;
- duplicate formulations;
- build-log collisions;
- compute/manuscript disagreement;
- propagation failures.

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

After any mathematical change:
- grep the active Vol II surface;
- grep superseded split files if they still advertise the same statement;
- grep `~/chiral-bar-cobar`;
- grep `~/calabi-yau-quantum-groups` when the bridge is genuinely cross-volume;
- update compute/tests if the claim is executable.

### 8. Verify

Run the narrowest verification that can actually falsify the change:
- targeted `pytest`;
- targeted grep or label check;
- log inspection;
- `make fast` for load-bearing manuscript rewrites;
- broader build/test only when the local slice passes and the scope demands it.

### 9. Re-Audit

Hostilely re-read your own rewrite. Stage 9 is not celebration; it is attempted refutation of the patch you just made.

### 10. Convergence

A task is converged only when:
- no actionable finding at severity `MODERATE` or above remains on the modified surface; and
- the narrowest relevant verification passes.

Rectification sessions should end by marking the outcome explicitly:
- `CONVERGED`
- `BLOCKED: <one-sentence blocker>`

## Multi-Path Verification Mandate

Every computational claim, formula, coefficient, table entry, or test oracle should be supported by at least three genuinely independent paths whenever feasible.

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
10. descent consistency to the PVA or classical shadow.

Minimum standard:
- manuscript formula: at least 3 paths when the claim is load-bearing;
- compute test: at least 2 methods in code or one method plus one structural invariant;
- table value copied across volumes: never trust the copy without a fresh convention conversion.

Cross-volume convention alert:
- Vol I uses OPE modes.
- Vol II uses lambda-brackets with divided powers.
- The coefficient at order `n` differs by a factor of `1/n!`.

## Hostile Examiners

Dense passages should be inspected through these lenses:

- **Beilinson**: is the claim really proved, or only asserted?
- **Witten**: does the physical interpretation match the mathematical statement, with honest scope?
- **Costello**: are the factorization and mixed-color constructions actually well-formed?
- **Gaiotto**: do VOA, DS, and W-algebra identifications survive reductions and edge cases?
- **Drinfeld**: are the transport, quantum-group, and monodromy structures structurally correct?
- **Kontsevich**: are the operadic and formality statements precise, functorial, and non-circular?
- **Compiler**: does the intended workflow fit Codex's actual runtime constraints, tools, hooks, and skill surface?

## Core Failure Families

The large anti-pattern register compresses into five load-bearing families. Think in families first, not isolated bugs.

### Family O — Object Conflation

If two objects coincide in a special case, assume they diverge in the general case until proved otherwise.

Rules:
- There are four objects: `A`, `B(A)`, `A^i`, `A^!`. Never conflate them.
- `Omega(B(A)) = A` is inversion. It does not produce `A^!`.
- `A^!` is read by Verdier/factorization duality, not by cobar inversion.
- The bar complex is not the bulk algebra.
- The primitive datum is the open-sector factorization dg-category; a boundary algebra is a chart.
- The ordered bar, full symmetric bar, and Francis-Gaitsgory bar are three different complexes.

### Family S — Scope Inflation

If a theorem is proved on a lane, do not silently upgrade it to all lanes.

Rules:
- Bulk `simeq` derived center is proved rigorously in the boundary-linear exact sector; do not globalize without hypotheses.
- Evaluation-generated core is not the full category.
- A biconditional is not earned by proving one direction.
- A genus-0 theorem is not an all-genus theorem because the slogan sounds natural.
- Koszul self-dual points and critical-string points are different invariants and must not be conflated.

### Family C — Convention Drift

Most manuscript damage comes from silent convention changes.

Rules:
- The bar kernel absorbs one pole: `r(z)` has pole order one less than the OPE.
- In Vol II, lambda-bracket coefficients are divided by `n!`.
- Desuspension lowers degree.
- `kappa` is not the same invariant as `S_2` outside the special families where they happen to agree.
- `eta(q)` includes `q^(1/24)`.
- Pole order is not chromatic height.

### Family E — E_infinity / E_1 Confusion

Do not let parenthetical glosses smuggle in false restrictions.

Rules:
- All ordinary vertex algebras are `E_infinity`-chiral, even with OPE poles.
- `E_1`-chiral means ordered and genuinely nonlocal; think quantum vertex algebra, not ordinary locality with poles.
- `R(z) != tau` does not imply genuine `E_1`; it may still be derived from a local OPE.
- Never add a parenthetical that narrows a defined manuscript term to a special subclass.
- PVA is a classical/cohomological shadow; it is not the same object as a `P_infinity`-chiral algebra.

### Family P — Presentation Lies

The exposition can be mathematically false even when the formulas are right.

Rules:
- theorem environment must match claim status;
- prose must state the same mechanism as the displayed formulas;
- central objects must be defined before theorem use;
- a correct conclusion with a false proof is still a bug;
- "standard", "clearly", and similar compression words do not close gaps.

### Family W — Workflow Pathologies

The agent layer can amplify error faster than the mathematics layer.

Rules:
- never propagate an unverified correction across multiple files;
- never let a beautiful summary outrun the actual proof state;
- never stop after a plan when the user asked for a result;
- never trust a previous agent's literature summary over the live repo conventions;
- never use destructive git commands to paper over confusion.

## Standing Hypotheses — Made Explicit

The algebraic framework is unconditional. The former standing hypotheses are no longer background fog:

| Hypothesis | Content | Current status |
|---|---|---|
| `(H1)` | BV data, one-loop finiteness | Condition of `Theorem thm:physics-bridge`; only for physical realizations |
| `(H2)` | Propagator meromorphic in `C`, exponentially decaying in `R` | Consequence of the physics bridge for physical realizations |
| `(H3)` | FM compactification, logarithmic forms, AOS relations, Stokes exactness | Axiomatically packaged by `Definition def:log-SC-algebra`; analytic consequences proved by `Theorem thm:FM-calculus` |
| `(H4)` | Compatibility with `C_*(W(SC^{ch,top}))` | Recognition theorem `thm:recognition-SC` |

Definition `def:log-SC-algebra` is the clean algebraic entry point:
- a `C_*(W(SC^{ch,top}))`-algebra whose closed-color `A_infinity` operations are defined by logarithmic weight forms factoring as `omega_k = omega_k^hol otimes omega_k^top` on `FM_k(C) x Conf_k(R)`.

## Critical Mathematical Pitfalls

Inherited from Vol I:
- cohomological grading, `|d| = +1`;
- bar uses desuspension;
- `m_1^2(a) = [m_0,a]` with the commutator sign convention;
- Sugawara is undefined at critical level `k = -h^vee`;
- Virasoro self-duality is at `c = 13`, not `26`.

Specific to Vol II:
- open-to-closed is empty;
- the PVA on `H^bullet(A,Q)` is `(-1)`-shifted;
- the `R`-matrix comes from bulk-boundary composition, not by default from a universal quantum-group `R`;
- formality failure at `d' = 1` is the curved bar structure, not a defect;
- the Koszul dual lives on the boundary, not in the bulk;
- spectral strictification is proved for simple Lie algebras with root multiplicity one; the true remaining frontier is Kac-Moody root multiplicity `> 1`.

## Codex Local Infrastructure

Repo-local Codex playbooks live in `.agents/skills/`:

- `$vol2-beilinson-rectification`
  Deep audit/rectify/fortify loop on a chapter, theorem, or live surface.
- `$vol2-formula-verification`
  Multi-path checking for formulas, invariants, coefficients, tables, and test oracles.
- `$vol2-cross-volume-propagation`
  Grep-and-propagate workflow across Vol I, Vol II, Vol III, superseded files, and compute layers.
- `$vol2-build-surface`
  Build, test, log, and warning triage.
- `$vol2-frontier-research`
  Frontier synthesis and research design, local by default and swarm-enabled only with explicit user authorization.

Repo-local Codex hooks live in `.codex/hooks.json`:
- `SessionStart`: injects the Vol II live-surface reminder.
- `UserPromptSubmit`: routes rectification-like prompts toward the correct playbooks.
- `PreToolUse`: blocks destructive shell habits and guards commits.
- `PostToolUse`: refuses to let failing verification output be silently ignored.
- `Stop`: nudges unfinished rectification sessions to declare `CONVERGED` or `BLOCKED`.

Hook note:
- Codex hooks are deterministic guardrails, not a substitute for judgment.
- Current Codex `PreToolUse` and `PostToolUse` hook Bash only; design enforcement accordingly.

## File Map

**Theory** (`chapters/theory/`): Part I and Part II.
- `foundations`, `locality`, `axioms`, `equivalence`, `bv-construction`
- `raviolo`, `raviolo-restriction`
- `fm-calculus`, `pva-descent-repaired`
- `introduction`

**Examples** (`chapters/examples/`): Part IV.
- `rosetta_stone`, `examples-computing`, `examples-worked`
- `examples-complete-proved`
- `examples-complete-conditional`
- `w-algebras-stable`
- `w-algebras-conditional`

**Connections — Core**: Parts III, V, VI, VII.
- `hochschild`, `brace`, `bar-cobar-review`, `line-operators`
- `spectral-braiding-core`, `ht_bulk_boundary_line_core`, `celestial_boundary_transfer_core`
- `ht_physical_origins`
- `modular_pva_quantization_core`, `affine_half_space_bv`, `fm3_planted_forest_synthesis`, `3d_gravity`
- `ordered_associative_chiral_kd_core`, `dg_shifted_factorization_bridge`
- `ym_synthesis_core`, `celestial_holography_core`, `log_ht_monodromy_core`, `anomaly_completed_core`

**Connections — Frontier**: Part VIII.
- `spectral-braiding-frontier`, `ht_bulk_boundary_line_frontier`, `celestial_boundary_transfer_frontier`
- `modular_pva_quantization_frontier`, `ordered_associative_chiral_kd_frontier`
- `ym_synthesis_frontier`, `celestial_holography_frontier`, `log_ht_monodromy_frontier`, `anomaly_completed_frontier`

**Aftermatter**:
- `conclusion`

**Appendices**:
- `brace-signs`, `orientations`, `fm-proofs`, `pva-expanded-repaired`

**Superseded but still audit-relevant**:
- `spectral-braiding.tex`, `ht_bulk_boundary_line.tex`, `celestial_boundary_transfer.tex`, `modular_pva_quantization.tex`
- `ordered_associative_chiral_kd.tex`, `ym_synthesis.tex`, `celestial_holography.tex`, `log_ht_monodromy.tex`
- `anomaly_completed_topological_holography.tex`, `examples-complete.tex`, `w-algebras.tex`
- `physical_origins.tex`, `holomorphic_topological.tex`, `bv_ht_physics.tex`, `concordance.tex`

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

## LaTeX Rules

- Use `\providecommand`, not `\newcommand`, for new macros.
- Do not add `\newtheorem` in chapter files.
- Claim tags: `\ClaimStatusProvedHere`, `\ClaimStatusProvedElsewhere`, `\ClaimStatusConjectured`, `\ClaimStatusHeuristic`, `\ClaimStatusOpen`.
- Key macros include `\cA`, `\Ainf`, `\Linf`, `\barB`, `\Omegach`, `\hh`, `\HH`, `\Sym`, `\End`.
- Do not add packages without checking the preamble.
- Do not duplicate Vol I definitions that should be referenced textually.
- Do not create new chapter files when the content belongs in an existing live chapter.

## Git — Hard Rule

All commits are authored by Raeez Lorgat.

Never add:
- `Co-authored-by`
- `Generated by`
- AI attribution of any kind in commit messages, source files, manuscript text, or metadata

Never use destructive recovery commands like `git reset --hard` or `git checkout --` unless the user explicitly requests them.

## The Aesthetic

Show, do not bluff. Every construction should feel inevitable because the proof architecture makes it inevitable, not because the prose is smooth.

The Steinberg variety presents the Hecke algebra.
The bar complex presents the Swiss-cheese algebra.
The derived center presents the bulk.
The complementarity potential presents the nonlinear modular shadow.

The music matters, but only after the score compiles.
