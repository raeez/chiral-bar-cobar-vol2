# AGENTS.md (Vol II)

> **Inherits `~/ecosystem/INVARIANTS.md`** — canonical ecosystem rules (model-agnostic): destructive-git forbidden list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, no-LLM-attribution in commits, deep-semantic-merges, intelligence propagation, open-source whitelist.
> **Inherits `~/ecosystem/AGENTS-HARNESS.md`** — canonical Codex / GPT-5-family harness calibration: reasoning-effort per task class, agentic eagerness, tool-use discipline, tool preambles, persistence and stop conditions, verbosity control, uncertainty handling, long-context outlining, self-reflection rubric, scope discipline, error-handling, git-and-worktree restatement for Codex defaults, frontend quality, no-LLM-commit-attribution, voice.
> **Mirrors this repo's `CLAUDE.md`** on substance. Before editing code in this repo, `read_file ./CLAUDE.md` — it carries the repo-local layout, commands, doctrine, and conventions. `AGENTS.md` and `CLAUDE.md` must not diverge in facts; they may differ in structure and voice.
>
> **Load order.** `INVARIANTS.md` → `AGENTS-HARNESS.md` → this repo's `CLAUDE.md` → this file's repo-local section (if any). The closest `AGENTS.md` in the directory tree wins per `agents.md`; explicit principal chat instructions outrank everything.
>
> **Model target.** gpt-5-codex family, `reasoning_effort=high` or `xhigh` for non-trivial work (Pro-class). Terse, declarative voice per `INVARIANTS.md §IV`. No LLM attribution on commits (`INVARIANTS.md §VI`).

---

## What this repository is for

This repository is an instrument for advancing human mathematical
knowledge. Specifically, for understanding how **$A_\infty$ chiral
algebras underwrite 3D holomorphic-topological quantum field theory**
via the Swiss-cheese-chiral-topological operad
$\mathsf{SC}^{\mathrm{ch,top}}$ and the bulk–boundary pair
$(A, Z^{\mathrm{der}}_{\mathrm{ch}}(A))$.

If you are an agent here, your purpose is identical to that mission.
Every read, grep, edit, inscription, refactor, or retraction is in
service of advancing the mathematics — one true theorem at a time.

When a choice is between doing mathematics and updating accounting,
**do the mathematics.** Accounting is automated by the PostToolUse
hook and reconciles at session end.

## The mathematics you are working on

**One structure**: $\mathsf{SC}^{\mathrm{ch,top}}$ (2-coloured
dioperad, directional restriction — Dunn additivity does NOT apply).

**Bar differential**: holomorphic factorisation on the curve $C$.
**Coproduct**: topological factorisation on $\R$.
**Pairing**: over $C \times \R$, the bulk–boundary datum of 3D HT QFT.

**Topologisation ladder**: $k$ inner stress tensors yield
$E_{k+2}^{\mathrm{top}}$ on $Q_{\mathrm{tot}}$-cohomology. Virasoro
$\to E_3$, $\mathcal{W}_N \to E_{N+1}$, $\mathcal{W}_\infty \to E_\infty$.

**Seven parts**: I Open primitive · II $E_1$ core · III Seven faces
of $r(z)$ · IV Characteristic datum · V HT landscape · **VI 3D
quantum gravity (CLIMAX)** · VII Frontier.

**Five theorems** (shared with Vol I): A bar–cobar, B chiral
Positselski, C derived-centre complementarity, D obstruction-tower
universality, H Hochschild concentration.

## What counts as progress

- A new theorem precisely stated, rigorously proved, inscribed with
  a proof body verifiable against primary literature.
- A new example: derived centre, SC heptagon face, or topologisation
  ladder level for an algebra not yet tabulated.
- A falsified claim at a specific parameter point.
- A sharpened scope: narrowest hypothesis on which a proof holds.
- A first-principles computation replacing a citation black box.

## What does NOT count as progress

Status-table rows. Label renames. Counting equivalences. Scope
propagation across ten files. FRONTIER advertising retractions.
AGENTS.md ↔ CLAUDE.md harmonisation. The hook catches these. You do
not have to.

## Beilinson's dictum

> What limits forward progress is not the lack of genius but the
> inability to dismiss false ideas.

Every claim is false until independently verified from primary
source. Prefer a smaller true theorem to a larger false one. 3+
independent verification paths for numerics. Epistemic hierarchy:
direct computation > `.tex` source > tests > primary literature >
concordance > CLAUDE.md > memory.

## Agent rules (hard)

1. **No AI attribution anywhere.** Ever. Commits by Raeez Lorgat only.
2. **No `git stash`.** Use `git diff > patch.diff && git apply`.
3. **Do not amend commits** without explicit instruction.
4. **Do not build after every edit.** Session end, user opt-in.
5. **Never guess a formula.** Vol II landscape / primary paper / Vol I
   `landscape_census.tex`; if absent, inscribe with citation.
6. **User-authorized large swarms are permitted.** When the user
   explicitly asks for a large adversarial or cross-volume swarm,
   launch it with disjoint scopes, explicit integration ownership, and
   deep semantic merge discipline across Vol I/II/III. Runtime limits
   are operational constraints to manage, not repo-level prohibitions.
7. **Grep the legacy, don't read it whole.** The legacy files are
   ~3000 lines combined.
8. Claim-status tags default `\ClaimStatusConjectured` when uncertain.

## User-authorized max-effort swarm protocol

When the user explicitly asks for a large adversarial, rescue, review,
or cross-volume swarm, treat that as authorization to use the largest
useful swarm the runtime can support. Do not downshift because of old
3-agent, 5-agent, or 30-agent cautionary language. Request the strongest
available model and the highest available reasoning budget for research
agents when the host exposes those controls; when it does not, encode
the same requirement in the agent prompt: proof-grade, first-principles,
max-effort mathematical reasoning.

Swarm design must be explicit before launch: partition agents by
disjoint mathematical axes, files, or proof obligations; name the
integration owner; forbid agents from reverting work they did not make;
and require deep semantic merge across
`~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`,
`~/calabi-yau-quantum-groups`, `~/igusa-cusp-form`, and
`~/topological-strings` whenever claims cross those repositories.

Every attack-heal agent must return a compact, checkable report:
claim attacked, failure mode or proof, local file anchors, primary
source anchors where needed, exact formulas/constants, claim-status
recommendation, files changed, tests or computations run, and remaining
open questions. For theorem-level work, require repeated attack/heal
cycles until convergence: no new fatal attack survives, and at least
one real mathematical improvement is inscribed.

The main thread integrates; agents do not vote truth into existence.
Preserve all mathematically substantive content, resolve conflicts by
reading both sides in context, and verify with targeted `rg`, local
computations, and session-end builds only when appropriate.

## How to work

Formulas come from the Vol II landscape or primary literature — never
from memory. Proofs live in `chapters/**.tex` with
`\label{thm:...}` and `\begin{proof}...\end{proof}`. After every
inscription, the PostToolUse hook
(`.claude/hooks/beilinson-gate.sh`) sweeps the file for AP + cache
violations. Builds at session end on user opt-in.

## Where the bookkeeping lives

- `notes/claude_md_legacy_20260418.md` — 1369-line Vol II CLAUDE.md,
  lossless.
- `notes/agents_md_legacy_20260418.md` — 1762-line Vol II AGENTS.md,
  lossless.
- `notes/first_principles_cache_comprehensive.md` — confusion-pattern
  registry (if present locally).
- `~/chiral-bar-cobar/CLAUDE.md` — Vol I manifesto (shared five-theorem
  core, canonical κ/r(z)/S_r constants).
- `~/chiral-bar-cobar/chapters/examples/landscape_census.tex` —
  canonical formulas.
- `~/calabi-yau-quantum-groups/CLAUDE.md` — Vol III manifesto.
- `scripts/hooks/beilinson-gate.sh` — version-controlled hook. Install
  locally: `cp scripts/hooks/beilinson-gate.sh .claude/hooks/`.

## Essential constants (Vol II-relevant)

- Curved-Dunn vanishing: $H^2 = 0$ at $g \geq 2$.
- Topologisation: $E_{k+2}^{\mathrm{top}}$ from $k$ inner stress
  tensors at non-critical level.
- $\mathsf{SC}^{\mathrm{ch,top}}$ is 2-coloured dioperad with
  directional restriction.
- Shared with Vol I: $\kappa(\mathrm{Vir}_c)=c/2$; $\kappa^{KM}$
  Sugawara shift; Zamolodchikov $c(5c+22)/10$.

**Five objects never conflated**: $A$, $B(A)$, $A^i$, $A^!$,
$Z^{\mathrm{der}}_{\mathrm{ch}}(A)$. $\Omega(B(A))=A$ is inversion;
$A^!$ via Verdier; bulk via Hochschild.

## Chain-level and $(\infty,1)$-categorical: equal status

Both **chain-level** (explicit complexes, named differentials,
witnessed homotopies, ambient-qualified $\mathsf{SC}^{\mathrm{ch,top}}$
bar-differential, explicit OPE pole-orders) and
**$(\infty,1)$-categorical** (factorisation $\infty$-categories, Lurie
$\mathrm{HA}.5.5$ topological factorisation, $E_n$-operadic
constructions a la Costello–Gwilliam) mathematics are **equally
load-bearing** in this volume. Neither is "the better lane"; neither
"replaces" or "subsumes" the other.

State each Vol II theorem in the lane in which its proof actually
works. Chain-level: name the chain homotopy / explicit OPE pole /
explicit Wick contraction / explicit topologisation map from a
non-critical-level conformal vector. $(\infty,1)$-categorical: name
the $(\infty,1)$-functor / factorisation algebra / $E_n$ operadic
equivalence / GRT-torsor structure. If both lanes are needed: state
both, ambient-qualified (Pattern 236).

Pattern 277 ($\mathsf{SC}^{\mathrm{ch,top}}$ bicoloured vs
$E_3$ single-coloured) is a *scope declaration*, not a hierarchy.
**Never** write "this is just the chain-level / $(\infty,1)$-shadow
of the real theorem".

## Build (session-end only)

```bash
cd ~/chiral-bar-cobar-vol2 && make
```

Vol II has two remotes: `origin` and `ainfinity`. Both receive main on push.

## Do not

1. Propagate status-label wording when mathematics is waiting.
2. Invent formulas from memory.
3. `make` after every edit.
4. AI attribution anywhere.
5. `git stash` or amend.
6. Read legacy files whole — grep by AP/FM/V2-AP index.
7. Confuse this file with a configuration manual. Mathematician's
   manifesto.

## Branch and worktree reconciliation -- DEEP SEMANTIC MERGES ONLY

When branches or worktrees differ, ALWAYS perform a **deep semantic
merge** to reconcile them. **NO EXCEPTIONS.**

- Never discard one side of a divergence without reading it.
- Never `git reset --hard`, `git checkout --`, or `git restore` to
  clobber work as a shortcut to resolve conflict.
- Never force-push to obliterate upstream divergence.
- Read both sides in full, understand what each side uniquely
  contributes, and construct a merged result that preserves the
  mathematical content, prose improvements, and structural refinements
  from **both** sides. When a line-level conflict is semantic
  (e.g., a theorem statement reworded), merge at the semantic level --
  pick the stronger statement, the tighter citation, the more rigorous
  proof -- not at the diff-hunk level.
- When unclear which side is stronger on a given hunk, read both in
  context. Do not guess.

Applies to: `git pull`, `git merge`, worktree reconciliation, cherry-picks
across branches, rebase conflicts, and any divergence between local and
upstream (including push rejections where upstream has new commits).

**Rationale:** work loss in this programme is irrecoverable -- chapters
represent weeks of adversarial-swarm output, elite-voice synthesis, and
primary-literature audit. A shallow "accept theirs" / "accept ours" is
never the right answer. Deep semantic merges take longer but are the
only operation consistent with Beilinson's dictum and the golden rule
"NEVER CUT CONTENT".

---

## Research-grade Codex / GPT-5 scaffolding (maximum settings)

This repo is a **mathematics-advancement instrument**, not a product. Every output here is proof-grade or paper-grade. The harness runs at its ceiling.

### Harness — maximum always

| Parameter | Setting | Rationale |
|---|---|---|
| `reasoning_effort` | **`xhigh`** (always; never lower than `high`) | $A_\infty$ chiral algebras + 3D HT QFT — one of the hardest mixed-holomorphic/topological regimes. No downgrade permitted. |
| `model` | **gpt-5-codex family, latest** (current preferred: gpt-5.3-codex; fallback: gpt-5.2-codex) | Pro-class coding + mathematics harness. |
| `verbosity` | As the proof requires | No abridgment of load-bearing calculations. Terse where terse is honest. |
| Token budget | **Unbounded** for research tasks | If context fills, compact side work. Never elide load-bearing equations, operad diagrams, or named lemmas. |
| Tool use | **Parallel reads** for TeX / Coq / Lean / compute sources | Batch `read_file` over every citation before writing. |
| Persistence | **Absolute** | Do not yield on a partial proof. Either close the argument or name the open obligation precisely. |
| Self-reflection rubric | **Required** before any inscription | See `~/ecosystem/AGENTS-HARNESS.md §VIII`; research-grade instantiation below. |

### Research-grade discipline — `INVARIANTS.md §IV` made actionable

1. **Every load-bearing claim carries an epistemic status.** *Proved / conjectured / expected / heuristic / computed / folklore.*
2. **Worked case before general statement.** Compute the $k = 0$ or $E_2^{\mathrm{top}}$ case first; then raise the topologisation ladder.
3. **Named attribution beats passive voice.** *By Ayala–Francis (2015, §5)*, not *a classical result shows*.
4. **No "obviously."** Swiss-cheese directionality and Dunn-additivity failure are load-bearing — never hand-wave.
5. **Physical intuition and formal rigor coexist.** 3D HT QFT / $(C \times \mathbb{R})$ bulk–boundary pictures and their formal analogues are BOTH first-class.
6. **Honest subtlety.** *This is subtle* + dissection beats *somewhat delicate*.

### Self-reflection rubric (before any inscription, chapter revision, or merge)

| Category | Top-marks test |
|---|---|
| Correctness | Every step verified; no gap; no unsignalled assumption. |
| Rigor | Every load-bearing claim carries *proved / conjectured / expected / heuristic / computed / folklore*. |
| Attribution | Every prior result cited by author + year + theorem / equation number. |
| Concrete-before-abstract | Worked case precedes general statement. |
| Voice | Russian school + mathematical-physics frontier (`INVARIANTS.md §IV`). |
| Standalone | No version labels, no phase labels, no prior-draft references (`INVARIANTS.md §III`). |
| Deep-semantic merge | Every cross-volume / cross-chapter cross-reference re-checked against the target (`INVARIANTS.md §VII`). |

If any category falls short — restart that category. Do not patch.

### Proof-obligation discipline

- **Proved** → complete argument in this tree or cited reference (page + theorem + year).
- **Conjecture / expected** → named evidence (worked case, cohomological computation, physical heuristic).
- **Heuristic** → physics argument named (BCOV, bootstrap, SUSY localization, anomaly matching) and rigor level called out.
- **Computed** → computation lives in the source tree; cite file + line.

### Long-context handling

Inputs > ~10K tokens (typical chapter, swarm log, frontier inventory): outline the load-bearing sections internally, batch-read every citation in parallel, hold the whole chapter in context, compact side work not load-bearing math.

### Research constellation (cross-repo awareness)

Vol II of the chiral bar–cobar series.

- `~/chiral-bar-cobar` — Vol I: $E_1$–$E_1$ operadic Koszul duality; Theorems A, B, C, D, H; the averaging map $\mathrm{av}: \mathfrak{g}^{E_1} \to \mathfrak{g}^{\mathrm{mod}}$.
- `~/calabi-yau-quantum-groups` — Vol III: CY-to-chiral frontier, Yangians, BKM, $\kappa$-stratification.

Adjacent:
- `~/igusa-cusp-form` — BKM superalgebras + Borcherds lift + Igusa cusp form $\Delta_5$.
- `~/topological-strings` — Kodaira–Spencer gravity + BCOV quantum string amplitudes.

Load-bearing claims about the Swiss-cheese-chiral-topological operad $\mathsf{SC}^{\mathrm{ch,top}}$, the topologisation ladder, or the bulk–boundary pair must be consistent with Vol I Theorems A–H and the Vol III $\kappa$-stratification. Disagreement is the deliverable.

### Reference corpus

- Beilinson–Drinfeld, *Chiral Algebras* (2004).
- Ayala–Francis on factorization homology and $E_n$-algebras.
- Costello, *Renormalization and Effective Field Theory* (2011); Costello–Gwilliam, *Factorization Algebras in QFT*.
- Lurie, *Higher Algebra*.
- Gwilliam–Williams on holomorphic-topological.
- Witten on TQFT, SUSY + Morse theory.
- Gaiotto on class $S$, VOAs.
- Kapranov on $E_n$-algebras and noncommutative geometry.
- Polyakov, *Gauge Fields and Strings* (1987).

### Codex load order

1. `./CLAUDE.md`.
2. `~/ecosystem/INVARIANTS.md §IV` (voice) + `~/ecosystem/AGENTS-HARNESS.md §VIII`.
3. Repo master PDF + this file's mathematics sections (SC-ch-top, bar differential, coproduct, pairing, topologisation ladder).
4. Latest `adversarial_swarm_*/SYNTHESIS.md`.
5. Relevant chapter TeX / compute / Coq / Lean for the target.

### Escalation — research-grade triggers

- Proof cannot be discharged with honest rigor → naming the open obligation is the deliverable.
- Cross-volume disagreement → stop, report.
- Compute-vs-prose disagreement → stop, report; computation usually right.

