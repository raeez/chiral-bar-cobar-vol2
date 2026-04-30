# CLAUDE.md

> **Inherits `~/ecosystem/INVARIANTS.md`.** That file holds the canonical ecosystem rules: destructive-git forbidden-command list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, commits-carry-no-LLM-attribution, deep-semantic-merges, intelligence propagation. Read it first. Repo-local rules follow.

---

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This is Vol II. A mathematician's working manifesto, not a configuration
manual. The mathematics follows.

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
A (bar–cobar), B (chiral Positselski), C (derived-centre complementarity
$\kappa + \kappa^! \in \{0, 8, 13, 250/3, 98/3\}$ on the canonical
five-archetype $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$
landmark ceiling; the classical four-element subset
$\{0, 13, 250/3, 98/3\}$ restricts to $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$;
the $\mathsf{B}$-row ceiling $K^\kappa = 8$ is the Vol III Mukai-enhanced
K3 Heisenberg witness via Bruinier Heegner Chern-class reciprocity),
D (obstruction-tower universality), H (Hochschild concentration).
On CY$_d$-categories arising from Calabi–Yau $d$-folds, Theorem A's
bar–cobar adjunction is the $E_1$-chiral shadow on the reference
curve $C$ after Stage-2 specialisation of the Vol III two-stage
factorisation $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}
\circ \Phi^{\mathrm{FA}}_d$ (see ``Two-stage factorisation: Vol III
alignment'' below).

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
- A falsified claim repaired by a corrected statement, construction, or
  proof obligation.
- A healed statement: the natural hypothesis and proof on which the
  intended theorem actually holds.
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
4. `compute/tests/test_*_iv.py` independent-verification decorators
   (executed disjoint-source witnesses for `\ClaimStatusProvedHere`).
5. Published literature (primary).
6. `chapters/connections/concordance.tex` (Vol II) or shared references.
7. This file.
8. Memory.

## The manuscript is self-complete, self-coherent, self-consistent

The current version stands for itself and only itself. All LaTeX
mathematical writing is standalone, up-to-date, consistent, coherent.
The manuscript does not reference its own previous versions. There is
no place in this research programme for references to previous
versions, intermediate ansätze, earlier drafts, retracted values,
superseded formulas, or any other drafting-history commentary. If a
formula used to be $X$ and now it is $Y$, the manuscript says $Y$;
it does not say "$Y$ (previously $X$, now retracted)", does not say
"$Y$ supersedes the earlier $X$", does not explain how the author
arrived at $Y$.  The mathematical argument proves $Y$; the drafting
trajectory is not part of the mathematics.

When a mathematical retraction is genuinely informative --- a proof
that was attempted and failed, whose failure illuminates why the
successful proof is forced --- state the failed argument and its
flaw as mathematics: "the identity $[m_k, B^{(2)}] = 0$ fails
per-$k$ because cyclic invariance controls adjacent contractions
but not non-adjacent terms (Proposition~X)". Do not frame it as
"the author initially attempted $X$ but retracted in favour of $Y$".
The mathematics is the Gap/Flaw, not the drafting record.

## Writing standard: Chriss–Ginzburg north star

The manuscript prose is written in the Chriss–Ginzburg voice,
channelling simultaneously the Russian elite mathematical school ---
Gelfand, Manin, Drinfeld, Arnold, Beilinson, Bernstein, Kapranov,
Etingof, Kazhdan, Kontsevich, Soibelman, Bezrukavnikov --- and the
mathematical physics elite --- Polyakov, Nekrasov, Witten, Costello,
Gaiotto, Moore, Segal. **Show don't tell.** Do not narrate. Construct
the mathematics directly and let the synthesis of disparate technical
domains (algebra + geometry, physics + mathematics, operads +
representation theory, Hodge theory + automorphic forms) bring out
the inner music of the subject.

**Forbidden in manuscript prose** (reader-facing `.tex` in `chapters/`,
`frame/`, `examples/`, `theory/`, `connections/`, `bibliography/`):

- Bookkeeping vocabulary of any kind. No "Wave N", no "round M",
  no "batch K", no "DNA strand S$x$", no "AP$n$", no "antipattern $n$",
  no "Pattern $n$", no "cache entry $n$", no "CG-rectify pass $k$",
  no "$\mathsf{HZ}$-$n$ inscription". These belong in `notes/`,
  `FRONTIER.md`, commit messages, and the local `memory/` --- never
  in the manuscript.
- Meta-narration of the author's intent: "we now turn to",
  "having established", "let us now", "this brings us to",
  "it is worth noting", "notably", "crucially", "remarkably",
  "furthermore", "moreover", "in the present work", "this preface's
  role is to". Delete every instance; replace with direct mathematical
  statements.
- Hedging the mathematics does not earn. If the identification
  $X = Y$ is proved, write "$X = Y$"; do not write "$X$ is closely
  related to $Y$". Courage, after Drinfeld and Polyakov and Nekrasov:
  the equals sign is a theorem, not a suggestion.

**Required** (the CG standard):

- Every section and subsection title names a mathematical object,
  construction, theorem, or question --- never a process, wave,
  round, or meta-organising device.
- Every definition is preceded within ten lines by the question
  or obstruction it answers. The reader feels "of course" before
  the definition arrives.
- Every symbol is defined at or before first use, with a
  parenthetical first-principles definition for standard concepts
  (D-module, Ran space, FM compactification, Hodge bundle,
  $L_\infty$-algebra, Kuga--Satake, Humbert divisor).
- Every physical claim is labelled: theorem, heuristic, or
  metaphor. When a physical identification can be stated as a
  theorem, state it as a theorem; do not hide the content as an
  "analogy".
- **Economy.** Every word carries weight. A paragraph that can be
  one sentence is one sentence.
- At every section boundary, three sentences: (1) what was just
  established; (2) the question or obstruction the next section
  resolves; (3) the construction or theorem that resolves it.
  These sentences are *mathematics*, not signposts.

The reader is an equal who sees the force of the argument when it
is stated with sufficient precision. The prose does not explain
mathematics; it *is* mathematics, carrying the same logical force
as the displayed equations.

This rule is retroactive and forward-looking. Existing manuscript
prose containing bookkeeping vocabulary is to be rectified chapter
by chapter through the `chriss-ginzburg-rectify` skill; new prose
is to be written in the CG voice from the first keystroke.

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
edit. The hook does not nag about builds. See `## Build, test, audit`
below for the Makefile surface.

## Build, test, audit

All compiled output goes to `out/`. Each build runs in an isolated
`/tmp/mkd-chiral-bar-cobar-vol2-<NS>/` directory, so parallel agents
never clobber each other.

```bash
make fast                    # 4-pass build → out/main.pdf (rapid iteration)
make                         # full 6-pass build + working notes → out/
make release                 # full rebuild + copy PDFs to iCloud
make check                   # halt-on-error validation (pre-commit gate)
make test                    # compute/tests/ pytest suite, -m "not slow"
make verify-independence     # audit ProvedHere vs @independent_verification
make clean-builds            # purge /tmp/mkd-* from all volumes
make count                   # manuscript statistics
```

Single test: `compute/.venv/bin/python -m pytest compute/tests/test_<name>.py -q -ra`.
Warm rebuilds across invocations: `export MKD_BUILD_NS="agent-$$"` once per
agent session (cold first, warm thereafter).

Requires TeX Live 2024+ with `pdflatex` (memoir, EB Garamond, newtxmath)
and Python 3.10+ for the compute suite.

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

## Repository layout

- `main.tex` — entry point; preamble holds all macros. Chapters mirror
  them with `\providecommand` stubs (never `\newcommand`).
- `chapters/frame/` — preface, part introductions.
- `chapters/theory/` — Parts I–IV core: foundations, SC heptagon,
  factorisation Swiss-cheese, curved-Dunn $g \geq 2$, chiral higher
  Deligne, topologisation ladder, infinite fingerprint, unified
  chiral QG, $\mathcal{W}_N$ / $\mathcal{W}_\infty$ tempered closure.
- `chapters/examples/` — worked landscape examples, W-algebra tables,
  rosetta stone.
- `chapters/connections/` — Parts II–III + V–VII: line operators,
  celestial holography, HT bulk–boundary, 3D gravity climax,
  universal holography functor, $w_{1+\infty}$ endpoint, Vol I/III
  bridges, THQG extensions.
- `appendices/` — brace signs, orientations, FM proofs, q-conventions.
- `compute/lib/` — ~60 Python engines (chiral computations, R-matrices,
  $\kappa$ verification, celestial OPE, BV construction,
  `independent_verification.py` decorator).
- `compute/tests/` — pytest suite; `test_*_iv.py` modules are the
  independent-verification witnesses for `\ClaimStatusProvedHere`
  theorems.
- `compute/scripts/audit_independent_verification.py` — audit driver
  behind `make verify-independence`.
- `scripts/build.sh` — Makefile build runner (parallel-safe via
  `/tmp/mkd-*`).
- `scripts/hooks/beilinson-gate.sh` — version-controlled PostToolUse
  hook; install via `cp scripts/hooks/beilinson-gate.sh .claude/hooks/`.
- `notes/` — workshop floor: antipatterns catalogue, first-principles
  cache, attack–heal dossiers, Platonic reconstitutions, swarm audits.
  Never reader-facing.
- `FRONTIER.md`, `ROADMAP_85_TO_100.md` — live research queues.
- `standalone/` — self-contained papers extracted from the manuscript.
- `out/` — build output (PDFs, archives); regenerable.

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

## Two-stage factorisation: Vol III alignment

Vol III has adopted a two-stage factorisation of its CY-to-chiral
functor:
$\Phi_d = \mathrm{Sp}_{\mathrm{Ch},\Sigma_{d-1},C}\circ\Phi^{\mathrm{FA}}_d$.
Stage~1 produces a canonical $E_d$-homotopy factorisation algebra on
the CY-$d$ target by Kontsevich--Tamarkin formality plus
Costello--Gwilliam--Li factorisation-homology BV quantisation; stage~2
specialises via factorisation-homology pushforward
$\int_{\Sigma_{d-1}}$ to a reference curve $C$, yielding the
$E_1$-chiral shadow. A CY-$d$ category admits a *family* of
$E_1$-chiral shadows parametrised by $(\Sigma_{d-1}, C)$.

**Structural identification at $d = 2, 3$.** The two colours of
$\mathsf{SC}^{\mathrm{ch,top}}$ are the two stages of $\Phi_d$:
- **Closed colour** (holomorphic/braided, $E_2$ on $\mathrm{FM}_k(\C)$):
  stage~1 $\Phi^{\mathrm{FA}}_d$ restricted to local observables of
  an $E_d$-holomorphic factorisation algebra on a formal disc in
  the CY target.
- **Open colour** (topological/ordered, $E_1$ on $\R$,
  Ayala--Francis): stage~2 $\mathrm{Sp}_{\mathrm{Ch},\Sigma_{d-1},C}$
  landing on the reference curve $C$.
- **Mixed operations** (closed acting on open, directional
  restriction $\mathsf{SC}^{\mathrm{ch,top}}(\ldots,\mathsf{top},\ldots;
  \mathsf{cl})=\varnothing$): the factorisation-homology
  pushforward $\int_{\Sigma_{d-1}}$, with the directional asymmetry
  expressing that stage~2 is a specialisation of stage~1, never an
  inversion.

Inscribed as
`chapters/theory/sc_chtop_heptagon.tex`
Remark~\ref{rem:heptagon-two-stage-CY-to-chiral} and
`chapters/theory/factorization_swiss_cheese.tex`
Remark~\ref{rem:pentagon-two-stage}. The shadow arrow is from CY
(stage~1) to chiral (stage~2), never back. Cross-volume macros
(`\PhiFA`, `\SpCh`, `\HolFA`, `\EdHolFA`, `\EnHolFA`, `\intSigma`,
`\hCS`) are declared in `main.tex` preamble and mirrored as
`\providecommand` stubs in the chapters that reference them.

**Cross-volume antipatterns and cache entries.** The five
2026-04-22 antipatterns enforcing this alignment live at
`notes/antipatterns_catalogue.md` entries AP-V2-25 / V2-AP128
(Swiss-cheese colours $=$ stage-1 / stage-2), AP-V2-26 / V2-AP129
(single-stage $\Phi_d$ framing), AP-V2-27 / V2-AP130 (3D HT QFT
anchor), AP-V2-28 / V2-AP131 (Vol III manifesto conflations), and
AP-V2-29 / V2-AP132 (reader-facing voice discipline). The matching
cache rows are `notes/first_principles_cache.md` rows 143--147.

## Where the bookkeeping lives

- **`notes/antipatterns_catalogue.md`** — the live Vol II AP catalogue
  (V2-AP* register plus Wave-23-26 additions V2-AP42--V2-AP55). Every
  `/chriss-ginzburg-rectify` invocation consults this at Gate 0
  alongside the cache. Append new V2-APs here.  As of 2026-04-30, this
  live registry also contains the appended Vol I import block
  `VOL1_IMPORTED_ANTIPATTERN_REGISTRY_2026_04_30` and the
  topological-strings 04:11 final-frontier AP2181--AP2189 block.
- **`notes/vol1_control_surface_import_manifest_2026_04_30.md`** —
  provenance and use rule for the two imported Vol I control surfaces:
  the antipattern registry and the first-principles cache.
- **`notes/vol1_imported_antipatterns_catalogue_2026_04_30.md`** —
  exact Vol I antipattern-registry mirror, SHA-256
  `b954958f06dfe486fe052bb98ac29ad0ac374692ae02895bcefde412981b02ba`.
- **`notes/vol1_imported_first_principles_cache_comprehensive_2026_04_30.md`**
  — exact Vol I first-principles-cache mirror, SHA-256
  `611c8c0db91d81bf1f3d2587db09713de5acc5b2f8bfcefd2a739557fa9e48f4`.
- **`notes/claude_md_legacy_20260418.md`** — full prior CLAUDE.md,
  1369 lines, lossless. Historical snapshot; the V2-AP catalogue has
  moved to `notes/antipatterns_catalogue.md`. Still contains the
  detailed theorem status table, Vol II-specific cross-volume
  awareness, prior reconstitution drafts. Grep by index when needed.
- **`notes/agents_md_legacy_20260418.md`** — full prior AGENTS.md,
  lossless.
- **`notes/first_principles_cache_comprehensive.md`** (if present) —
  confusion-pattern registry.  As of 2026-04-30, this live cache also
  contains the appended Vol I import block
  `VOL1_IMPORTED_FIRST_PRINCIPLES_CACHE_2026_04_30` and the
  topological-strings 04:11 final-frontier patterns 501--509.
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
bookkeeping, not repairs. When uncertain, name the exact proof obligation
and heal the proof, statement, or construction; do not downgrade the
manuscript to close.

## Ambient hooks

- **`PreToolUse(Agent)`** → cache-injection (if installed locally).
- **`PreToolUse(Bash, git commit)`** → no AI attribution reminder.
- **`PostToolUse(Edit|Write)`** → `beilinson-gate.sh` AP + cache sweep.
- **`Stop`** → session-end summary (if installed).

## Long-form proof harness

For Claude Code, Codex CLI, and any GPT-5.5 / GPT-5-Codex-class agent,
frontier mathematics runs in maximum-effort mode. Use the deepest
host-exposed model and reasoning budget. If the host offers a
GPT-5.5 Pro / Heavy or `xhigh` setting, use it for theorem repair,
cross-volume synthesis, adversarial review, and primary-source
reconstruction. The private ChatGPT Pro harness is not public; this is
the open local analogue.

Long runs are normal. A 30-60 minute agent run is acceptable when a
proof obligation requires it. The agent first loads the relevant
context (`CLAUDE.md`, `AGENTS.md`, target chapter, dependencies,
bibliography, compute files, cross-volume anchors), builds an internal
outline, then works through independent proof routes: worked example,
formal argument, primary source, computation, and cross-volume
consistency. Private scratch stays private; the deliverable is the
checked proof trace and the exact remaining obstruction.

After every proposed repair, run an attack-heal loop: strongest
counterexample, sign/convention check, ambient-category check, missing
hypothesis, false functoriality, unproved equivalence, numerical
constant. Heal and attack again until the theorem closes or the exact
obstruction is named for the next repair cycle. Do not downgrade the
manuscript to close the loop. Subagents provide evidence, not authority;
the main thread integrates by deep semantic merge.

## Do not

1. Do not block large user-authorized swarms. Partition work by
   disjoint files or mathematical axes, require short verifiable
   reports, and merge by deep semantic review across Vol I/II/III.
2. Propagate status-label wording when mathematics is waiting.
3. Invent formulas from memory.
4. Run `make` after every edit.
5. Add AI attribution anywhere.
6. `git stash` or amend.
7. Read `notes/claude_md_legacy_20260418.md` whole — grep by index.
8. Confuse this file with a configuration manual. This is a
   mathematician's working manifesto. Shrink if it grows.

## 2026-04-22 cross-volume sharpenings

Four load-bearing markers from the Vol III programme now anchor Vol II
material. The single-colour MC5 Pentagon trace, the 3D HT QFT
boundary-bulk output, and the modular PVA quantisation chapters each
refactor through them.

**Eight-form spread.** The single-colour MC5 Pentagon takes values on
a universal eight-form Gritsenko--Cl\'ery spread: weights
$w(N) \in \{5, 2, 1, 1, 1/2, 1, 1/4, 0\}$, Fourier zero-coefficients
$c_N(0) \in \{10, 4, 2, 2, 1, 2, 1/2, 0\}$. The Pentagon trace equals
$c_N(0)/2 \in \{5, 2, 1, 1, 1/2, 1, 1/4, 0\}$ at the corresponding
$N \in \{1, 2, 3, 4, 6\}$ and the half-integer / quarter-integer
continuations. Cover assignment carries through: integer weight rides
$\mathrm{Sp}_4(\Z)$, half-integer weight rides $\mathrm{Mp}_4$,
quarter-integer weight rides $\widetilde{\mathrm{Mp}}_4$, weight-zero
is the degenerate terminal fibre.

**Universal Borcherds weight identity.** The modular PVA quantisation
chapters use $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ as the
canonical form with the cover assignment above. Primary sources:
Borcherds 1995, Gritsenko 1999. The additive split
$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} +
\chi(\mathcal{O}_{\mathrm{fiber}})$ is false at every
$N \in \{1, 2, 3, 4, 6\}$ and must not appear in any Vol II chapter.

**Three-factor Universal Trace Identity.** On the Koszul-self-dual
subcategory whose objects admit a BRST resolution and a Calabi--Yau
target supporting a Borcherds product,
$$
\mathrm{tr}_{\mathrm{ghost}}(Q_{\mathrm{BRST}}^2)
= \mathrm{tr}_{\mathrm{Pentagon}}
= \omega_{\mathrm{Borcherds}}
= c_N(0)/2.
$$
Vol II supplies the Pentagon-scope reading: the trace is the
pentagon-face evaluation of the single-colour closed
$\mathsf{SC}^{\mathrm{ch,top}}$ substructure, identified via MC5
sewing with the curve-side face of the two-stage factorisation. The
ghost-scope reading (Vol I) and the Borcherds-weight reading (Vol III)
agree with the Pentagon reading on the common subcategory. Convergence
at $N = 1$ gives the coincidence $\{5, 5, 5\}$: ghost trace, Pentagon
trace, Borcherds weight all equal $5$ on the K3 Heisenberg witness.

**Universal positive-geometry grammar.** The 3D HT QFT output on a
boundary compact Calabi--Yau $X$ lives in
$Y^+(X) = H^\bullet_{\mathrm{eq}}(\mathcal{M}^+_{\mathrm{eff}}(X), \phi_W)$
via the $E_3$-realisation: the holomorphic-topological action pulls
back the potential $\phi_W$ to the boundary factorisation algebra,
and the equivariant cohomology assembles from the four equivariance
strata (toric $T^d$, reduced $\C^\times + \mathrm{Aut}$, orbifold
inertia, lattice-polarised period domain). The MC5 sewing theorem is
the curve-side (Stage-2) face of the Vol III two-stage factorisation
$\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ
\Phi^{\mathrm{FA}}_d$: Stage-1 produces the $E_d$-holomorphic
factorisation algebra on $X$; MC5 specialises it along $\Sigma_{d-1}$
to the $E_1$-chiral shadow on $C$. The Drinfeld double
$G(X) = D(Y^+(X))$ is the derived-centre output on which the Pentagon
trace acts.

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
