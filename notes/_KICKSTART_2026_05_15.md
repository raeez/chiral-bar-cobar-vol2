# KICKSTART — Vol II platonic reconstitution (resume from 2026-05-15)

> This file is a self-contained re-entry prompt for a fresh `/clear` Claude session. Read it, read the anchors it names, then begin work. Do not re-acknowledge state; act on the live frontier.

---

## 1. What this is

You are continuing the platonic-ideal reconstitution of `~/chiral-bar-cobar-vol2` — the chiral bar-cobar Vol II monograph (~2424 pages, 105+ chapters). The thesis, anchors, voice discipline, licensing types, Construction Problems, and architectural cuts are all stated in `CLAUDE.md`. Read that first; this file extends it with the current state and live frontiers.

---

## 2. What is closed (do not redo)

- **Seven-part platonic structure** (I OBJECT · II CHART · III LADDER · IV CHARACTERISTIC DATUM · V LANDSCAPE · VI CLIMAX · VII FRONTIER) is in `main.tex`; Part VIII has been folded into VII; III/IV inversion repaired.
- **Voice rectification** across all chapters: zero sentence-initial / paragraph-initial "We compute / construct / prove / verify / show / define / derive / exhibit" sites; zero "we now / we will see / notably / in the present work" meta-narration. Mathematical-convention "we" (we have, we record, we call) is retained, as in Witten / Etingof / Costello.
- **Inline licensing tags α/β/γ/δ/ε** on the nine load-bearing theorems:
  - `thm:bicoloured-primitive-universality` (α+β) — `chapters/theory/foundations.tex`
  - `lem:heptagon-two-stage-CY-to-chiral` (α+β) — `chapters/theory/sc_chtop_heptagon.tex`
  - `thm:cyclic-hochschild-stage-stratification` (β+γ+ε) — `chapters/connections/hochschild.tex`
  - `thm:chirhoch-virasoro-concentration` (β) — `chapters/connections/hochschild.tex`
  - `thm:chiral-positselski-cross-volume` (β+ε) — `chapters/connections/bar-cobar-review.tex`
  - `thm:universal-holography-master` (α+β+γ+δ) — `chapters/connections/programme_climax_platonic.tex`
  - `thm:programme-climax` (α+β+γ+δ) — same file
  - `cor:universal-holography-via-bicoloured-universality` (α+β) — same file
  - `thm:kappa-tuple-primitivity-orthogonal-shimura` (α), `thm:kappa-tuple-primitivity-class-B` (α+γ) — same file
  - `thm:construction-problem-stage-stratification` (α+β+γ+δ+ε) — same file
- **κ-tuple discipline** propagated (bare-κ count = 0; use `\kappaCat`, `\kappaChHodge`, `\kappaChHeis`, `\kappaBKM`, `\kappaFiber`, `\kappaTuple`, `\Kkappa`).
- **Concordance** (`chapters/connections/concordance.tex`) is wired into `main.tex` aftermatter.
- **FRONTIER** (`FRONTIER.md`) carries the Construction Problem status snapshot with per-CP gap analysis.
- **IV tests**: eight disjoint-route witnesses at `compute/tests/test_{bar_neq_bulk,kappa_tuple,phi_two_stage,y_plus_vs_g,delta_5_shadow,w_inf_endpoint,class_m_ambient,quad_vs_koszul}_iv.py`.
- **Build**: clean at 2424 pages. Run `export MKD_BUILD_NS="kickstart-$$"; make fast`.
- **Licensing gate**: green. Run `bash scripts/verify_licensing.sh`; expect 0 blocking violations, ≤2 warnings (legitimate meta-references to the voice table).

---

## 3. Live frontier (what to work on next)

The live mathematics is the four open Construction Problems and the residual endpoint-chapter hypothesis-tag audit. Everything else is bookkeeping.

### 3a. The four Construction Problems

Per `FRONTIER.md` Open Construction Problems and `chapters/connections/programme_climax_platonic.tex` `thm:construction-problem-stage-stratification`:

| CP | Stage transport | Gap |
|:---:|------|-----|
| **P1** | $\mathsf{S} \to \mathsf{Z}$ (trace + CY lane) | Construct $\mathfrak{D}_X$ on $X = K3 \times E$ with $\mathrm{Pf}_{\mathrm{prot}}(\mathfrak{D}_X) = \Delta_5$ at chain level |
| **P2** | $\mathsf{S} \to \mathsf{A}$ (open lane via Pentagon trace) | Construct the gravity-line operator algebra realising the six-route Hall–Borcherds bridge |
| **P3** | $\mathsf{Z} \to \mathsf{Z}$ inside open lane (classical to quantum) | Install $\hypKZSDR + \hypStokes + \hypReflWts + \hypTLift$; close the all-loop quantum lift |
| **P4** | $\mathsf{S} \to \mathsf{Z}$ on open lane outside Vol I positive-energy ambient | Refined $\hypAmbientWtCpl$ for non-positive-energy / log / non-rational chiral algebras |

These are **open mathematics**, not editorial cleanup. Cross-volume anchors: P1 at `~/igusa-cusp-form/main.tex:94--118`; P2 at `chapters/connections/3d_gravity.tex:8429`; P3 at `chapters/theory/pva-descent.tex` + `thm:iterated-sugawara-construction`; P4 at `~/chiral-bar-cobar` Vol I `theorem_B_scope_platonic.tex`.

### 3b. Endpoint-chapter hypothesis-tag audit (warnings, not blockers)

`scripts/verify_licensing.sh` reports a list of endpoint-chapter theorems lacking `\hyp*` / `\eff*` macros in the body. Total ~103 theorems across `bv_ht_physics.tex` (5), `e_infinity_topologization.tex` (13), `3d_gravity.tex` (70), `programme_climax_platonic.tex` (15). These are **informational**, not blocking. Many are genuinely unconditional; some carry the hypothesis package as scope text rather than as named macros.

**Discipline.** Audit theorem-by-theorem: if the theorem holds at chain level under finite assumptions, no hypothesis tag is needed (e.g., `thm:iterated-sugawara-construction`). If it requires endpoint convergence, install the named macro (e.g., `thm:e-infinity-weightwise-inverse-limit` already carries `\hypProchazka, \hypCKL, \hypPRSh, \hypYamada`). Do **not** mechanically inscribe tags to satisfy the audit; the discipline is to make the conditional structure visible where it is load-bearing.

### 3c. Cross-volume consistency

Verify against `~/chiral-bar-cobar` (Vol I), `~/calabi-yau-quantum-groups` (Vol III), `~/chiral-bar-cobar-vol4` (Vol IV), `~/mixed-holomorphic-topological-strings`, `~/igusa-cusp-form`. The bicoloured primitive universality, the heptagon two-stage CY-to-chiral lemma, and the κ-tuple primitivity claims are the cross-volume gates. **Disagreement is the deliverable** — deep semantic merge, never reset --hard / restore.

---

## 4. Architectural anchors (read first)

- `CLAUDE.md` — manifesto, voice canon, licensing types, Construction Problems, 17-forbidden-slogan voice table.
- `notes/legacy/critique_2026_05_09_chiral_duality_master_consequence_map_v2.md` — universal stage chain $\mathsf{P} \to \mathsf{C} \to \mathsf{S} \to \mathsf{Z} \to \mathsf{A}$ + five licensing types + four Construction Problems.
- `notes/legacy/vol2_platonic_architecture.md` — the seven-part platonic form Vol II yearns to be.
- `MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md` — Witten · Etingof · Polyakov · Dirac · Feynman · Costello · Gaiotto. Mandatory.
- `FRONTIER.md` — proved-core table, open frontiers F1–F12, Construction Problem status snapshot.
- `MEMORY.md` (in the auto-memory directory) — architectural commitment + validated discipline.

---

## 5. Working discipline (Vol II canon)

- Every edit is mathematics, not bookkeeping (CLAUDE.md §10).
- Russian-school + math-physics voice (CLAUDE.md §11). Show don't tell. Titles name objects. Definitions preceded by the question.
- Branch / worktree reconciliation: **deep semantic merge only**. Never `reset --hard`, never `restore`, never force-push to obliterate divergence (CLAUDE.md §22). Work loss is irrecoverable.
- Commits by Raeez Lorgat. **No AI attribution anywhere** — no Claude / Anthropic / Co-Authored-By / Generated with / robot emoji.
- Long-form proof harness for theorem repair / cross-volume synthesis: 30–60 minute sessions, deepest model, highest reasoning budget, multi-route independent derivations, attack-heal loops. **Disagreement is the deliverable.**
- Large user-authorised swarms permitted when the task spans the volume. Subagents return evidence; main thread integrates via deep semantic merge.

---

## 6. Immediate entry point

1. `git status` — confirm clean tree on `main`.
2. `cat CLAUDE.md` — full re-read.
3. `cat FRONTIER.md` — current open frontiers.
4. Pick one: a Construction Problem CP1–CP4 (open mathematics, highest value), or a specific F-frontier from `FRONTIER.md` (e.g., F1 BV/BRST = bar at chain level for class M, g ≥ 2).
5. Build internal outline before the first edit. Identify load-bearing identities. Seek independent derivations by multiple routes. Run the attack-heal loop until the theorem closes or the obstruction is precisely named.

Build verification command: `export MKD_BUILD_NS="session-$$"; make fast`. Licensing gate: `bash scripts/verify_licensing.sh`.

---

## 7. Recent commit trail (for context, not for replay)

```
398f40f Vol II: inscribe licensing tags on Universal Holography master theorem and programme climax
38d2476 FRONTIER: Construction Problems status snapshot
c2ac81d Vol II: paragraph-initial voice sweep -- zero remaining We-verb meta-narration
140d90c (earlier sweep) Second passive sweep: 22 more sentence-initial We-verb -> declarative
a011333 Vol II: codify Supremum Discipline failed-theorem-surface protocol
```

Do not amend these; create new commits.

---

End of kickstart. The mathematics follows.
