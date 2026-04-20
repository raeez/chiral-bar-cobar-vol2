# CLAUDE.md (Vol II)

## What this repository is for

This repository is an instrument for advancing human mathematical
knowledge. Specifically, for understanding how **$A_\infty$ chiral
algebras underwrite 3D holomorphic-topological quantum field theory**,
and what the Swiss-cheese-chiral-topological operad
$\mathsf{SC}^{\mathrm{ch,top}}$ implies about the bulk–boundary
structure of the chiral (co)homology adjoint pair.

Every tool call, every edit, every agent decision made here has one
purpose: to advance that understanding, one true theorem at a time.

When a choice presents itself between doing mathematics and updating
accounting, **do the mathematics.** Accounting is handled automatically
by the PostToolUse hook and can always be reconciled at session end.

## The mathematics

**One structure**: the two-coloured Swiss-cheese-chiral-topological
operad $\mathsf{SC}^{\mathrm{ch,top}}$ governing $(\text{bulk},
\text{boundary})$ pairs. On $A_\infty$ chiral algebras $\cA$, the bar
differential is **holomorphic factorisation** on the curve $C$, and the
coproduct is **topological factorisation** on $\R$. Their pairing over
$C \times \R$ is the bulk–boundary datum of a 3D holomorphic-topological
quantum field theory.

**One tower**: the iterated Sugawara ladder — $k$ inner stress tensors
$T^{(n)} = [Q_{\mathrm{tot}}, G^{(n)}]$ promote the chiral direction to
$E_{k+2}$-topological on $Q_{\mathrm{tot}}$-cohomology. Affine
Kac–Moody ($N=2$) reaches $E_3^{\mathrm{top}}$; $\mathcal{W}_N$
reaches $E_{N+1}^{\mathrm{top}}$; $\mathcal{W}_\infty$ reaches
$E_\infty^{\mathrm{top}}$ — the Platonic endpoint.

**Seven parts** hold the Vol II structure:

| Part | Content |
|---|---|
| I | Open primitive — $\mathsf{SC}^{\mathrm{ch,top}}$ foundations |
| II | $E_1$ core — ordered chiral homology, Yangian-like structures |
| III | Seven faces of $r(z)$ — Drinfeld–Kohno, Sklyanin, Gaudin |
| IV | Characteristic datum — shadow tower, higher-genus, modular Koszul |
| V | HT landscape — chiral / affine / W / lattice / Yangian families |
| **VI** | **3D quantum gravity — the CLIMAX** (Virasoro + $w_{1+\infty}$, celestial holography, holographic codes) |
| VII | Frontier |

**Five theorems** crystallise across the trilogy (shared with Vol I):
A (bar–cobar), B (chiral Positselski), C (derived-centre complementarity),
D (obstruction-tower universality), H (Hochschild concentration).

Everything in this repository is a concentric ring around those
theorems, with Vol II-specific contributions: the topologisation tower,
curved-Dunn $H^2 = 0$ at $g \geq 2$, the $\mathsf{SC}^{\mathrm{ch,top}}$
heptagon, chiral higher Deligne, universal celestial holography,
periodic-CDG on admissible Kazhdan–Lusztig, unified
$Q_g^{k, f, \mu}$ chiral quantum group.

## What counts as progress

- A new theorem precisely stated, rigorously proved, inscribed with a
  proof body verifiable against primary literature.
- A new example: compute the derived centre, SC heptagon faces, or
  topologisation ladder for an algebra not yet tabulated.
- A falsified claim: demonstrating an asserted identity fails at a
  specific parameter point.
- A sharpened scope: narrowest hypothesis on which a proof holds.
- A first-principles computation replacing a citation-only black box.

**Progress is *not*** updating a status-table row, renaming a label,
counting strengthenings, propagating scope across ten files, editing
FRONTIER to match CLAUDE.md, or editing AGENTS.md. Those are
bookkeeping. The PostToolUse hook catches them. You do not have to.

## Beilinson's dictum

> What limits forward progress is not the lack of genius but the
> inability to dismiss false ideas.

Every claim is false until independently verified from primary source.
Prefer a smaller true theorem to a larger false one. Every numerical
claim should have 3+ independent verification paths.

**Epistemic hierarchy** (higher wins):
1. Direct computation.
2. `.tex` source ±100 lines.
3. Build system / tests.
4. Published literature (primary).
5. `chapters/connections/concordance.tex` (Vol II) or shared references.
6. This file.
7. Memory.

## How to work

**Formulas come from the Vol II landscape or primary literature** —
never from memory. Cross-volume consistency: consult Vol I
`chapters/examples/landscape_census.tex` for $\kappa$, $r(z)$, central
charges.

**Proofs are inscribed in the chapter, not in notes.** A proof in
`notes/` or a swarm log is a draft. Move it into `chapters/**.tex`
with a `\label{thm:...}` and a `\begin{proof}...\end{proof}` body.

**After every inscription** (theorem, proposition, lemma, corollary,
definition, proof, remark), the PostToolUse hook
(`.claude/hooks/beilinson-gate.sh`) scans the file for anti-pattern
signatures and cached confusion patterns. Address what it flags;
return to the mathematics.

**Builds at session end only, by user opt-in**. No `make` after every
edit. The hook does not nag about builds.

```bash
# Session end only
cd ~/chiral-bar-cobar-vol2 && make
```

## Essential constants (Vol II-relevant)

- Curved-Dunn vanishing: $H^2(\text{curved-Dunn}) = 0$ at $g \geq 2$.
- $\mathsf{SC}^{\mathrm{ch,top}}$ is a 2-coloured dioperad with
  directional restriction; Dunn additivity does **not** apply.
- Topologisation: $E_{k+2}^{\mathrm{top}}$ from $k$ inner stress
  tensors at non-critical level.
- Shared with Vol I: $\kappa(\mathrm{Vir}_c) = c/2$;
  $\kappa(V_k(\mathfrak{g})) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$;
  Zamolodchikov norm $c(5c+22)/10$.

**Five objects, never conflate**: $A$ (chiral algebra) — $B(A)$ (bar
coalgebra) — $A^i = H^\star B(A)$ — $A^! = ((A^i)^\vee)$ —
$Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ (derived centre = bulk).
$\Omega(B(A)) = A$ is **inversion**, not Koszul duality. $A^!$ via
**Verdier**. Bulk via **Hochschild** cochains.

## Chain-level and $(\infty,1)$-categorical: equal status

Both **chain-level** mathematics (explicit complexes, named
differentials, witnessed homotopies, $L_\infty$-formalism, Mittag–Leffler
towers, ambient-qualified statements like the chain-level
$\mathsf{SC}^{\mathrm{ch,top}}$ bar-differential) and
**$(\infty,1)$-categorical** mathematics (factorisation
$\infty$-categories, Lurie $\mathrm{HA}.5.5$ topological factorisation,
$E_n$-operadic constructions a la Costello–Gwilliam, Francis–Gaitsgory)
are **equally load-bearing** in this volume. Neither is "the better
lane"; neither "replaces" or "subsumes" the other.

Vol II in particular owes its content to *both* lanes simultaneously:

- The chain-level $\mathsf{SC}^{\mathrm{ch,top}}$ bar-differential (as
  the holomorphic factorisation map at coincident points) is what lets
  you compute the OPE pole orders, the explicit Wick contractions, the
  $\beta\gamma$ Heisenberg pairing, and the topologisation chain
  homotopy from a non-critical-level conformal vector.
- The $(\infty,1)$-categorical formulation (factorisation
  $\infty$-categories, the topological-factorisation coproduct as a
  Lurie $\mathrm{HA}.5.5$ structure, $E_n$ promotion via Dunn
  additivity restated as an $\infty$-operadic equivalence) is what
  lets you state the seven-faces-of-$r(z)$ as an
  $\mathrm{GRT}$-torsor, the 3D HT QFT culmination as a
  fully-extended TFT, and the bar–coproduct duality as an inversion
  in an $\infty$-stable category.

**Operating rule**: state every theorem in the lane in which its proof
actually works. If chain-level: name the chain homotopy, the explicit
Mittag–Leffler witness, the explicit MC element, the explicit OPE pole.
If $(\infty,1)$-categorical: name the $(\infty,1)$-functor /
adjunction / colimit / fibre sequence. If both lanes are needed:
state both, label which lane each status applies to (Pattern 236
ambient-qualifier discipline). **Never** write "this is just the
chain-level / $(\infty,1)$-categorical shadow of the real theorem":
both shadows are real, both are the theorem, viewed through different
lenses.

Pattern 277 ($\mathsf{SC}^{\mathrm{ch,top}}$ vs $E_3$ conflation) is
a *scope declaration*, not a hierarchy: the chain-level bicoloured
operad and the $(\infty,1)$-categorical $E_3$-promotion under
topologisation are **two different theorems** about two different
mathematical objects, both proved, both load-bearing.

## Where the bookkeeping lives

- **`notes/claude_md_legacy_20260418.md`** — full prior CLAUDE.md,
  1369 lines, lossless. Contains the Vol II AP catalogue (V2-AP*),
  the detailed theorem status table, Vol II-specific cross-volume
  awareness, prior reconstitution drafts. Grep by index when needed.
- **`notes/agents_md_legacy_20260418.md`** — full prior AGENTS.md,
  lossless.
- **`notes/first_principles_cache_comprehensive.md`** (if present) —
  confusion-pattern registry.
- **`~/chiral-bar-cobar/CLAUDE.md`** — Vol I manifesto (mathematics
  here harmonises with Vol I's shared five-theorem core).
- **`~/chiral-bar-cobar/chapters/examples/landscape_census.tex`** —
  canonical formulas per family. Source of truth for $\kappa$, $r(z)$.
- **`~/calabi-yau-quantum-groups/CLAUDE.md`** — Vol III manifesto
  (CY-to-chiral functor $\Phi$).
- **`scripts/hooks/beilinson-gate.sh`** — version-controlled hook;
  install via `cp scripts/hooks/beilinson-gate.sh .claude/hooks/`.

## Git and authorship

All commits by **Raeez Lorgat** only. Never any AI attribution anywhere:
no `Claude`, no `Anthropic`, no `Co-Authored-By`, no `Generated with`,
no 🤖, in commits, comments, docstrings, or manuscripts. Pre-commit
hook nudges; remove offending content.

Two remotes: `origin` (GitHub primary) and `ainfinity` (mirror). Both
receive main on push.

`git stash` forbidden (use `git diff > patch.diff && git apply`). Do
not amend commits.

## LaTeX

Macros in `main.tex` preamble. Inside chapters, `\providecommand`, not
`\newcommand`. Memoir + EB Garamond.

Claim-status tags (`\ClaimStatusProvedHere`, etc.) are reader-facing
bookkeeping — default `\ClaimStatusConjectured` when uncertain.

## Ambient hooks

- **`PreToolUse(Agent)`** → cache-injection (if installed locally).
- **`PreToolUse(Bash, git commit)`** → no AI attribution reminder.
- **`PostToolUse(Edit|Write)`** → `beilinson-gate.sh` AP + cache sweep.
- **`Stop`** → session-end summary (if installed).

## Do not

1. Spawn 30 parallel Codex agents for an audit (serialised + silently
   budget-cut; throughput ~1 deliverable per session window).
2. Propagate status-label wording when mathematics is waiting.
3. Invent formulas from memory.
4. Run `make` after every edit.
5. Add AI attribution anywhere.
6. `git stash` or amend.
7. Read `notes/claude_md_legacy_20260418.md` whole — grep by index.
8. Confuse this file with a configuration manual. This is a
   mathematician's working manifesto. Shrink if it grows.

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
