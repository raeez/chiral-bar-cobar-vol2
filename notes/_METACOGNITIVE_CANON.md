# Metacognitive Canon — current state of agent-steering signals

> **Last updated.** 2026-05-09. This file is the single entry-point for "what should an agent read before steering work." Read this first to know which signals are live and which are archival. The hook chain enforces but does not duplicate this index; the index is the human-facing map.

---

## Live canon (read these to steer)

| File | Purpose | Status |
|------|---------|--------|
| `./CLAUDE.md` | Platonic-form manifesto for Claude family | **canonical 2026-05-09** |
| `./AGENTS.md` | Platonic-form manifesto for Codex / GPT-5 family | **canonical 2026-05-09** |
| `./MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md` | Mandatory writing standard (Witten · Etingof · Polyakov · Dirac · Feynman · Costello · Gaiotto) | **canonical 2026-05-09** |
| `notes/legacy/critique_2026_05_09_chiral_duality_master_consequence_map_v2.md` | Architectural reconstitution map (universal stage chain, five licensing types, four Construction Problems, 17-line voice table) | **canonical** — supersedes v1 |
| `notes/legacy/vol2_platonic_architecture.md` | Seven-part form Vol II yearns to be | **canonical** |
| `notes/_KICKSTART_PLATONIC_RECONSTITUTION.md` | Fresh-session kickstart prompt: maximally parallel reconstitution swarms (8 swarms × disjoint scopes; 6 phases A–F) | **canonical** — invoke deliberately |
| `FRONTIER.md` | 14 open frontiers F1–F14 with hypothesis packages and heal paths | **canonical** |
| `notes/antipatterns_catalogue.md` | Live AP registry; consulted at Gate 0 by `chriss-ginzburg-rectify` | **live** (Vol I import block + HT-strings AP2181–2189 appended; do not read whole, grep by index) |
| `notes/first_principles_cache_comprehensive.md` | Live confusion-pattern registry | **live** (Vol I import block appended) |
| `~/ecosystem/INVARIANTS.md` | Cross-volume ecosystem rules | **canonical (parent)** |
| `~/ecosystem/AGENTS-HARNESS.md` | Codex / GPT-5 harness calibration | **canonical (parent)** |
| `~/chiral-bar-cobar/CLAUDE.md` · `~/chiral-bar-cobar/chapters/examples/landscape_census.tex` | Vol I manifesto + canonical κ / r(z) / S_r constants | **canonical (sibling)** |
| `~/calabi-yau-quantum-groups/CLAUDE.md` | Vol III manifesto | **canonical (sibling)** |

---

## Hooks (silent enforcement)

| Hook | Path | Fires on |
|------|------|----------|
| Beilinson gate | `scripts/hooks/beilinson-gate.sh` (version-controlled); install: `cp scripts/hooks/beilinson-gate.sh .claude/hooks/` | `PostToolUse(Edit\|Write)` on `.tex`/`.py`; AP + cache + voice-table sweep |
| Cache injection | `scripts/hooks/cache-injection.sh` (if installed) | `PreToolUse(Agent)` |
| Convergence gate | `scripts/hooks/convergence-gate.sh` (if installed) | session boundary |

The hooks reference `notes/antipatterns_catalogue.md` and `notes/first_principles_cache_comprehensive.md` as their gate sources. Whole-volume audit: `make verify-licensing` (mechanical grep against the 17-line voice table at `./CLAUDE.md §8`).

---

## Archival reference (mathematics may still be valid; framing is superseded)

These files contain real mathematical work from prior campaigns. Their HEADERS frame their content with bygone-wave / session-dated language that has been folded into the architectural cut. Read them only when chasing a specific mathematical detail; do not steer current work from them.

**2026-04 swarm and audit dossiers** (`notes/`, archival banners applied):
- `beilinson_swarm_audit_vol2_2026_04_17.md`, `session_20260417_master_synthesis.md`
- `swarm_vol2_abstract_platonic_audit_2026_04_17.md`, `swarm_vol2_connective_tissue_2026_04_17.md`, `swarm_vol2_convergence_synthesis_2026_04_17.md`, `swarm_vol2_dependency_dag_2026_04_17.md`, `swarm_vol2_narrative_trajectory_2026_04_17.md`, `swarm_vol2_seven_theorem_placement_2026_04_17.md`

**2026-04-22 battle-hardened dossiers** (`notes/`):
- `CONWAY_ROW_SIGN_AMBIGUITY_BATTLE_HARDENED_2026_04_22.md`, `COSTELLO_R5_GILKEY_AUDIT_T_CL_K3_EXTENSION_BATTLE_HARDENED_2026_04_22.md`, `FOUR_ROUTE_CONVERGENCE_TABLE_BATTLE_HARDENED_2026_04_22.md`, `NEKRASOV_R4_HBAR_SIGN_DERIVATION_BATTLE_HARDENED_2026_04_22.md`, `POLYAKOV_CYCLES_PHYSICS_MATH_2026_04_22.md`, `SIX_ROW_CLOSURE_DRINFELD_R5_BATTLE_HARDENED_2026_04_22.md`, `VOL_II_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md`

**2026-04 procedural / cron architecture** (`notes/`):
- `cg_rectify_kickstart.md`, `cg_rectify_interactive_resume.md`, `cg_rectify_redo_queue.md` — describe a 2026-04-17 cron architecture for `chriss-ginzburg-rectify`. The architecture itself is fine; the file's "Reference implementation: Vol III, trigger trig_01EwyA6My2f9sdmBdMYCcMZD, queue file..., commit b5648b4 (2026-04-17)" anchors are stale.
- `wave17_spoils_dossier_20260424.md` — Wave 17 closure dossier.

**2026-04-30 Vol I imports and `claude_md_legacy_20260418.md` / `agents_md_legacy_20260418.md`** — preserved lossless. Grep by AP / V2-AP / FM index; do not read whole.

**Archived elsewhere**:
- `archive/2026-04/FRONTIER_layered.md` — full prior FRONTIER content with Wave-13 / Wave-14 / DEFINITIVE STATUS layers.
- `archive/2026-04/ROADMAP_85_TO_100.md` — historical roadmap.
- `archive/2026-04/kickstart_2apr2026.md` — 2 April 2026 session dossier (270 lines, lossless).

---

## Deprecated framings (do not use)

- "Wave $N$" framing in chapters or current `notes/` files. Wave numbers belong in archive only.
- "DEFINITIVE STATUS as of 2026-04-22" or earlier. The 2026-05-09 architectural cut supersedes all prior layered status declarations; FRONTIER.md and the v2 consequence map are the current state.
- "Round $K$ of session $X$" framing. Sessions are ephemeral; mathematics survives in chapters.
- "AP$n$ inscription" in chapters. AP-numbering belongs in `notes/antipatterns_catalogue.md`; chapters never reference AP numbers.
- "DNA strand", "kickstart pass", "CG-rectify pass $k$" — bookkeeping vocabulary forbidden in chapters per `./MATHEMATICAL_PHYSICS_*WRITING_STANDARDS.md §I`.
- The v1 consequence map `notes/legacy/critique_2026_05_09_chiral_duality_master_consequence_map.md` — superseded by v2; v1 retains diff-history value, do not steer from it.

---

## What an agent should do at session start

1. Read `./CLAUDE.md` (Claude) or `./AGENTS.md` (Codex / GPT-5).
2. Read this file (`notes/_METACOGNITIVE_CANON.md`) to identify live vs archival.
3. Read `notes/legacy/critique_2026_05_09_chiral_duality_master_consequence_map_v2.md` for architectural commitments.
4. Read `notes/legacy/vol2_platonic_architecture.md` for the seven-part form.
5. Read `FRONTIER.md` for the 14 open frontiers.
6. Load target chapter + dependencies + bibliography + cross-volume anchors.
7. Build internal outline. Begin work.

If a `notes/` file is in the **archival reference** list above, read it only when chasing a specific mathematical detail referenced from a live source. Do not let archival headers steer current work.

---

## Reflexive note

This file is itself part of the metacognitive layer. When the architectural cut next moves, this file moves with it. When it stops being the right entry-point, it gets archived too. The canon is what the agent reads to act; the archive is what historians read to remember.

The corpus has one job: to make every agent's first read accurate.
