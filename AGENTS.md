# AGENTS.md (Vol II)

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
6. **Do not spawn 30 parallel Codex agents.** Serialised + silent
   budget cuts; ~1 deliverable per session window. Direct edits are
   higher throughput.
7. **Grep the legacy, don't read it whole.** The legacy files are
   ~3000 lines combined.
8. Claim-status tags default `\ClaimStatusConjectured` when uncertain.

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
