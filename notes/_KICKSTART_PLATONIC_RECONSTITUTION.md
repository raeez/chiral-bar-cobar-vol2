# Kickstart — Platonic Reconstitution of Vol II

> **How to use.** Open a clean session in `~/chiral-bar-cobar-vol2` (Claude Opus 4.7 1M context recommended; Codex / GPT-5 with `reasoning_effort=xhigh` acceptable). Paste this entire file as the user message, or instruct the agent: "follow `notes/_KICKSTART_PLATONIC_RECONSTITUTION.md` end-to-end." The orchestrator should hold this file in context throughout.
>
> **What this does.** Reconstitutes Vol II into the platonic-ideal form locked in by the 2026-05-09 architectural cut, by maximally parallel agent swarms partitioned along disjoint mathematical axes. Voice and writing discipline per `./MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md`. Architectural discipline per `./CLAUDE.md` and `notes/legacy/critique_2026_05_09_chiral_duality_master_consequence_map_v2.md`.
>
> **Reflexive note.** This kickstart is recipe, not deliverable. The deliverable is the rectified manuscript. When the reconstitution lands, this file expires.

---

## Pre-flight: context loads (orchestrator, sequential)

Read in this order. Build the internal outline before launching any swarm.

1. `./CLAUDE.md` — platonic-form manifesto. Internalize the universal stage chain $\mathsf{P}\to\mathsf{C}\to\mathsf{S}\to\mathsf{Z}\to\mathsf{A}$, five licensing types α/β/γ/δ/ε, bicoloured primitive package, two-stage CY-chiral, κ-tuple, 17 forbidden slogans, four Construction Problems.
2. `./MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md` — Witten · Etingof · Polyakov · Dirac · Feynman · Costello · Gaiotto. The prose IS mathematics.
3. `notes/_METACOGNITIVE_CANON.md` — live vs archival index.
4. `notes/legacy/critique_2026_05_09_chiral_duality_master_consequence_map_v2.md` — full architectural reconstitution map (universal chain, licensing types, voice table, Construction Problems, phasing, audit).
5. `notes/legacy/vol2_platonic_architecture.md` — the seven-part form Vol II yearns to be.
6. `FRONTIER.md` — F1–F14 + four Construction Problems, current language.
7. `notes/antipatterns_catalogue.md` — head only; grep by V2-AP index when needed; do not read whole.
8. `notes/first_principles_cache_comprehensive.md` — head only; grep by V2-AP / FM index.

Sister volumes (open in parallel context as needed):
- `~/chiral-bar-cobar/CLAUDE.md` + `~/chiral-bar-cobar/chapters/examples/landscape_census.tex` (Vol I).
- `~/calabi-yau-quantum-groups/CLAUDE.md` (Vol III).
- `~/mixed-holomorphic-topological-strings/main.tex` (HT global obstruction source).
- `~/igusa-cusp-form/main.tex` (Δ₅ Construction Problem 1 source).

---

## Phase A — Macro foundation (orchestrator, sequential, prerequisite)

The orchestrator does this DIRECTLY (no subagent). Subsequent swarms depend on the macros being live.

### A.1  Add platonic-form macros to `main.tex` preamble

Insert into `main.tex` preamble after the existing `\providecommand{\bulk}` block (~line 140–281). Expand each list inline:

```latex
% Bicoloured primitive package (CLAUDE.md §6)
\providecommand{\primPkgBicolour}{\bigl(\openFactCat|_{\logCurve},\, \cD^{\mathrm{cl}}|_X;\, b,\, A_{b},\, F^{\mathrm{cl}};\, \HalfBraid,\, \mathrm{tr}^{\mathrm{cl}}_{X};\, \TraceC\bigr)}
\providecommand{\openFactCat}{\cC^{\mathrm{op}}}
\providecommand{\logCurve}{(X, D, \tau)}
\providecommand{\HalfBraid}{\Theta_{C}}
\providecommand{\TraceC}{\mathrm{Tr}_{C}}

% κ-tuple discipline (CLAUDE.md §8)
\providecommand{\kappaCat}{\kappa_{\mathrm{cat}}}
\providecommand{\kappaChHodge}{\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}}
\providecommand{\kappaChHeis}{\kappa_{\mathrm{ch}}^{\mathrm{Heis}}}
\providecommand{\kappaBKM}{\kappa_{\mathrm{BKM}}}
\providecommand{\kappaFiber}{\kappa_{\mathrm{fiber}}}
\providecommand{\Kkappa}{K^{\kappa_{\mathrm{ch}}}}
\providecommand{\kappaTuple}[1]{(\kappaCat, \kappaChHodge, \kappaChHeis, \kappaBKM, \kappaFiber)(#1)}

% Two-stage CY-chiral + Hall side (CLAUDE.md §7)
\providecommand{\PhiFA}{\Phi^{\mathrm{FA}}}
\providecommand{\SpCh}{\mathrm{Sp}^{\mathrm{ch}}}
\providecommand{\HolFA}{\mathrm{HolFA}}
\providecommand{\EdHolFA}{E_{d}\text{-}\HolFA}
\providecommand{\intSigma}{\textstyle\int_{\Sigma_{d-1}}}
\providecommand{\hCS}{\mathrm{hCS}}
\providecommand{\Yplus}[1]{Y^{+}(#1)}
\providecommand{\Drinfdouble}[1]{D(#1)}
\providecommand{\CoHA}[1]{\mathrm{CoHA}(#1)}
\providecommand{\Wonepinf}{W_{1+\infty}}

% Bar / centre (CLAUDE.md §3)
\providecommand{\BarTwc}[1]{\overline{B}^{\mathrm{ch}}(#1)}
\providecommand{\bulkOf}[1]{Z^{\mathrm{der}}_{\mathrm{ch}}(#1)}
\providecommand{\bulkChirHoch}[1]{\mathrm{ChirHoch}^{\bullet}(#1, #1)}
\providecommand{\Zderch}[1]{Z^{\mathrm{der}}_{\mathrm{ch}}(#1)}

% Shadow / operator stratification (CLAUDE.md §10)
\providecommand{\protectedShadow}[1]{\overline{#1}^{\mathrm{shadow}}}
\providecommand{\operatorPrim}[1]{\mathfrak{D}_{#1}}
\providecommand{\protectedPfaff}[1]{\mathrm{Pf}_{\mathrm{prot}}(#1)}
\providecommand{\Deltafive}{\Delta_{5}}
\providecommand{\Phitenun}{\Phi_{10}^{\mathrm{un}}}
\providecommand{\ZBPS}{Z_{\mathrm{BPS}}}

% Conditional locus tags (CLAUDE.md §5; carry inline at theorem statement)
\providecommand{\hypProchazka}{(\mathrm{HP1}_{\mathrm{Prochazka}})}
\providecommand{\hypCKL}{(\mathrm{HP2}_{\mathrm{CKL}})}
\providecommand{\hypPRSh}{(\mathrm{HP3}_{\mathrm{PRSh}})}
\providecommand{\hypYamada}{(\mathrm{HP4}_{\mathrm{Yamada}})}
\providecommand{\hypKZSDR}{(\mathrm{HQ1}_{\mathrm{KZSDR}})}
\providecommand{\hypStokes}{(\mathrm{HQ2}_{\mathrm{Stokes}})}
\providecommand{\hypReflWts}{(\mathrm{HQ3}_{\mathrm{reflWts}})}
\providecommand{\hypTLift}{(\mathrm{HQ4}_{T=[Q,G]})}
\providecommand{\hypAmbientWtCpl}{(\mathrm{HM1}_{\mathrm{wt\text{-}cpl}})}
\providecommand{\hypHTGlobalDR}{(\mathrm{HG1}_{H^{1}(X,\C_X)=0})}
\providecommand{\hypBHdict}{(\mathrm{HG2}_{\mathrm{Brown\text{-}Henneaux}})}
\providecommand{\hypModInv}{(\mathrm{HG3}_{\mathrm{mod\text{-}inv}})}
\providecommand{\hypVacDom}{(\mathrm{HG4}_{\mathrm{vac\text{-}dom}})}
\providecommand{\hypSadDom}{(\mathrm{HG5}_{\mathrm{sad\text{-}dom}})}
\providecommand{\effKoszul}{(\mathrm{EK1}_{\mathrm{Koszul\text{-}eff}})}
\providecommand{\effPfaffOrient}{(\mathrm{EK2}_{\mathrm{Pf\text{-}orient}})}
\providecommand{\effHCSQuartic}{(\mathrm{EK3}_{\mathrm{quartic\text{-}vanish}})}
\providecommand{\effPBWnoExtra}{(\mathrm{EK4}_{\mathrm{PBW\text{-}noExtra}})}
```

Mirror these as `\providecommand` stubs in the chapters that reference them (the orchestrator can do this lazily — first chapters touched in Phase B will inherit).

### A.2  Author `scripts/verify_licensing.sh` + `make verify-licensing` target

The script runs a mechanical grep audit of the 17-line voice table at `./CLAUDE.md §8`. For each forbidden phrasing, scan `chapters/`; flag any match outside `\begin{remark}` blocks. Also: bare `\kappa` outside the tuple-component macros; bare `\Phi_d` not adjacent to `\PhiFA` or `\SpCh`; theorem statements lacking inline `\hyp...` / `\eff...` tags.

Add to `Makefile`:
```
verify-licensing:
	@bash scripts/verify_licensing.sh
```

### A.3  Single commit (do not push)

`git add main.tex scripts/verify_licensing.sh Makefile && git commit -m "macro layer + verify-licensing scaffold for v2 reconstitution"` (author Raeez Lorgat; no AI attribution).

---

## Phase B — Maximally parallel swarms (single message, multiple `Agent` tool uses)

Launch the eight swarms below CONCURRENTLY in ONE message. Each is partitioned by disjoint files / mathematical axes and will not conflict with the others. Each subagent should read `./CLAUDE.md` + the architectural canon + their target chapter(s) before any edit; CG voice throughout; theorem statements carry α/β/γ/δ/ε licensing tags inline; deep semantic merge on integration; compact attack-heal report on return.

### Swarm 1 — Architectural Definitions (frame chapters)

> **Description.** Inscribe bicoloured primitive package + heptagon-face / licensing-type duality + bar/centre canonical statement.
>
> **Scope.** `chapters/theory/foundations.tex` (or new `chapters/frame/architectural_definition.tex`); `chapters/theory/sc_chtop_heptagon.tex`; top of `chapters/connections/bar-cobar-review.tex`. Cross-reference from every Vol II theorem opening "Let $A$ be a chiral algebra."
>
> **Deliverable.** One named Architectural Definition of the bicoloured nine-tuple. A new Remark in `sc_chtop_heptagon.tex` stating the heptagon-face / licensing-type duality (face $\leftrightarrow$ type table). A consolidated bar/centre canonical statement at the top of `bar-cobar-review.tex` (rule: every "bulk" appearance refers to this label).

### Swarm 2 — GAP closer 10: HT global obstruction

> **Description.** Re-inscribe HT global obstruction at every Vol II HT-import site.
>
> **Scope.** `chapters/connections/bv_ht_physics.tex`, `holomorphic_topological.tex`, `affine_half_space_bv.tex`, `physical_origins.tex`, `ht_bulk_boundary_line*.tex`.
>
> **Deliverable.** At each site, a paragraph re-stating the global obstruction (sheaf of local Hamiltonians + vanishing $H^{1}(X, \C_X)$ holomorphic de Rham) with cross-reference to `~/mixed-holomorphic-topological-strings/main.tex:3200--3210, 3232--3233`. Tag with $\hypHTGlobalDR$.

### Swarm 3 — GAP closer 14: $W_\infty \to E_\infty$ endpoint

> **Description.** Rewrite the four endpoint hypotheses with named primary citations.
>
> **Scope.** `chapters/theory/e_infinity_topologization.tex:1163--1241`; mirror in `wn_tempered_closure_platonic.tex`, `tempered_stratum_characterization_platonic.tex`, `irrational_cosets_tempered_platonic.tex`, `logarithmic_wp_tempered_analysis_platonic.tex`.
>
> **Deliverable.** Four hypotheses cited as Prochazka 1809.06993 + Creutzig–Kanade–Linshaw 1704.08023 + Pope–Romans–Shen / Bakas + Yamada weight-window, tagged $\hypProchazka, \hypCKL, \hypPRSh, \hypYamada$ at theorem statement. Spin-≤8 numerical results re-tagged `\ClaimStatusEvidence`, not `\ClaimStatusProvedHere`.

### Swarm 4 — GAP closer 16: PVA classical vs quantum

> **Description.** Tie PVA hypotheses to theorem statements (not introductions).
>
> **Scope.** `chapters/theory/pva-descent.tex:25--43`; mirror in `pva-descent-repaired.tex`, `pva-expanded-repaired.tex`, `chapters/connections/modular_pva_quantization_core.tex:40--60`.
>
> **Deliverable.** H1–H4 stated as $\hypKZSDR, \hypStokes, \hypReflWts, \hypTLift$ at theorem statement. The rule: the all-loop quantum lift requires the four named hypotheses; the classical $\lambda$-Jacobi result is unconditional.

### Swarm 5 — GAP closer 17: quadratic injection vs Koszul bijection

> **Description.** Add the injection-vs-bijection caveat at Theorem A locus.
>
> **Scope.** `chapters/connections/bar-cobar-review.tex:174--181`; audit `chapters/theory/theorems_C_D_native_vol2_platonic.tex` for Theorem A vs Theorem B separation.
>
> **Deliverable.** Caveat "Gui–Li–Zeng injection $\mathrm{Hom}(A,B) \hookrightarrow \mathrm{MC}(A^! \otimes B)$ is bijective only under Koszul effectiveness $\effKoszul$; the chiral Positselski theorem (Vol I Theorem B) is the separate Koszul-duality theorem" inline at theorem locus.

### Swarm 6 — κ-tuple inscription (K3$\times E$ counterexample)

> **Description.** Inscribe the K3$\times E$ five-row κ-tuple counterexample.
>
> **Scope.** `chapters/connections/concordance.tex` (table row); `chapters/connections/programme_climax_platonic.tex` (climax remark); `chapters/theory/theorems_C_D_native_vol2_platonic.tex` (counterexample as Beilinson cut witness).
>
> **Deliverable.** $\kappaTuple{K3 \times E} = (0, 0, 3, 5, 24)$ stated explicitly with the additive identity $\kappaBKM = \kappaChHodge + \chi(\cO_{\mathrm{fiber}})$ failing at every $N \in \{1,2,3,4,6\}$ (Vol III source `chapters/examples/k3e_cy3_programme.tex:4564, 4750--4762`).

### Swarm 7 — Construction Problems + cyclic Hochschild

> **Description.** Inscribe the four operator-level Construction Problems + the four-object cyclic-Hochschild discipline.
>
> **Scope.** Closing section of `chapters/connections/programme_climax_platonic.tex` (Part VII); confirm explicit listing in `FRONTIER.md`. New remark in `chapters/connections/hochschild.tex` listing $\mathrm{ChirHoch}^\bullet$ vs $\mathrm{ChirHoch}_\bullet$ vs $\mathrm{HC}^{\mathrm{cyc}}$ vs $\mathrm{HC}^-$ with the discipline that only $\mathrm{ChirHoch}^\bullet$ is the bulk; the others are shadows requiring orientation / $S^1$-equivariance / Bridgeland licensing.
>
> **Deliverable.** (1) $\operatorPrim{X}$ for K3$\times E$ with $\protectedPfaff{\operatorPrim{X}} = \Deltafive$ (igusa). (2) Gravity-line operator algebra with Pentagon-face scalar trace $= \Phitenun = \Deltafive^{2}$. (3) Unified PVA-quantum HT theory (classical $\lambda$-Jacobi limit + $E_3$-lift on $Q$-cohomology). (4) Chiral Positselski extending Vol I Theorem B at chiral generality. Plus four-object Hochschild remark.

### Swarm 8 — IV scaffolding (8 disjoint-route test files)

> **Description.** Author 8 IV test files with `@independent_verification` decorators on disjoint construction paths.
>
> **Scope.** `compute/tests/test_bar_neq_bulk_iv.py`, `test_kappa_tuple_iv.py`, `test_phi_two_stage_iv.py`, `test_y_plus_vs_g_iv.py`, `test_delta_5_shadow_iv.py`, `test_w_inf_endpoint_iv.py`, `test_class_m_ambient_iv.py`, `test_quad_vs_koszul_iv.py`. Use `compute/lib/independent_verification.py` decorator; declare `disjoint_route="..."` per the existing pattern (see `notes/INDEPENDENT_VERIFICATION.md`).
>
> **Deliverable.** Each test passes `make verify-independence`. Each is a *disjoint* construction from the chapter's proof. For Construction-Problem-related tests (test_delta_5_shadow_iv.py), assert `@open_problem` since the operator-level object is not yet constructed.

---

## Phase C — Voice sweep (`chriss-ginzburg-rectify`, batched parallel)

After Phase B swarms return, run the CG voice sweep in batches of 3–4 parallel agents. The skill is heavy (~30–60 min per chapter); do not oversubscribe. For chapters > 3000 lines, the skill marks queue partial; multiple ticks may be needed.

- **Batch C.1 (frame).** `foundations.tex`, `sc_chtop_heptagon.tex`, `factorization_swiss_cheese.tex`.
- **Batch C.2 (bar–cobar / bulk).** `bar-cobar-review.tex`, `hochschild.tex`, `equivalence.tex`.
- **Batch C.3 (climax).** `programme_climax_platonic.tex`, `3d_gravity.tex`, `anomaly_completed_topological_holography.tex`.
- **Batch C.4 (κ + Hall).** `theorems_C_D_native_vol2_platonic.tex`, `unified_chiral_quantum_group.tex`, `log_ht_monodromy_frontier.tex`.
- **Batch C.5 (PVA + topologisation).** `pva-descent.tex`, `e_infinity_topologization.tex`, `weight_completed_topologization_class_m_platonic.tex`.

---

## Phase D — Cross-volume bidirectional back-edits (3 parallel `Agent` calls)

- **D.1 Vol I.** Insert "$A = A_b$ chart" framing into `~/chiral-bar-cobar/chapters/theory/bar_cobar.tex` (or equivalent). Tag every $\kappa$ usage in Vol I as $\kappaChHodge$. Cross-reference Vol II's bicoloured primitive package.
- **D.2 Vol III.** Elevate $G(X) = \Drinfdouble{\Yplus{X}}$ from main-text prose at `main.tex:550--564` to a load-bearing theorem statement in `chapters/theory/quantum_chiral_algebras.tex`. Cross-reference from Vol II.
- **D.3 mixed-HT-strings + igusa.** Cross-cite Vol II HT-import sites (`bv_ht_physics.tex` etc.) and Vol II gravity-line conjecture (`3d_gravity.tex:8429`) in `~/mixed-holomorphic-topological-strings/main.tex` and `~/igusa-cusp-form/main.tex` respectively. Add Vol II as anchor for Construction Problem 1.

---

## Phase E — Integration + verification (orchestrator)

E.1 Deep semantic merge any conflicts. Subagents provide evidence; main thread integrates by reading both sides in full when a conflict spans chapters.

E.2 Run the full audit:
```
make check
make test
make verify-independence
make verify-licensing
make fast
```

E.3 Inspect `out/main.pdf` for build cleanliness; check page-count delta against pre-reconstitution baseline.

E.4 If any verification fails, name the obstruction precisely. Do NOT downgrade the manuscript to close. If the failure is a real proof obligation, inscribe it with `\ClaimStatusConjectured` + named hypotheses, never as a silent retreat.

E.5 Final integration report in conversation: per-swarm outcome table; per-batch CG-rectify outcome; cross-volume back-edit outcome; verification outcome; remaining open obligations; commit history.

---

## Phase F — Commit + propagate (orchestrator)

F.1 Single deep-semantic-merge commit per logical group (one for macros + one per swarm result + one per voice batch + one per cross-volume back-edit). Each commit message names the phase and what landed. Author **Raeez Lorgat**. **No AI attribution anywhere.**

F.2 Push to both `origin` and `ainfinity` remotes after the user gives explicit approval.

F.3 If any new validated discipline emerged (a pattern user-confirmed during integration), add a single feedback memory at `~/.claude/projects/-Users-raeez-chiral-bar-cobar-vol2/memory/feedback_<key>.md` and update `MEMORY.md`. Do not memoize session state, theorem state, or frontier state — those live in the manuscript and FRONTIER.md.

---

## Operating discipline (applies throughout all phases)

- Every theorem statement carries α/β/γ/δ/ε licensing tags inline (per CLAUDE.md §5).
- Every primitive object names its stage on $\mathsf{P}\to\mathsf{C}\to\mathsf{S}\to\mathsf{Z}\to\mathsf{A}$.
- Bare $\kappa$ forbidden — use tuple components.
- Bare $\Phi_d$ forbidden — use $\PhiFA_d$ and $\SpCh$ separately.
- "Wave-N" / "round-K" / "session-X" framing forbidden in chapters.
- The 17-line voice table at CLAUDE.md §8 is authoritative; the Beilinson gate enforces it.
- Subagents do not vote truth into existence. Disagreement among swarms is the deliverable, not the conflict.
- Deep semantic merge: never `git reset --hard` / `git checkout --` / `git restore` to clobber work as a shortcut. Read both sides; pick the stronger statement, the tighter citation, the more rigorous proof.
- `git stash` forbidden — use `git diff > patch.diff && git apply`.
- Builds at session end only on user opt-in. Hooks may fire mid-session (Beilinson gate); allow them to flag, do not silence them.

---

## Escalation triggers

- Proof cannot be discharged with honest rigor → naming the open obligation IS the deliverable.
- Cross-volume disagreement → stop, report to the orchestrator.
- Compute-vs-prose disagreement → stop, report; computation usually wins.
- A swarm agent blocked > 30 min on one obligation → unblock by partitioning further or delegating to `codex:rescue`.
- Hook flags a voice-table or AP violation → fix the source, not the gate.

---

## Per-swarm report format

Every subagent returns:

- **claim attacked** (one line)
- **failure mode or proof** (worked example / formal argument / primary literature / local computation / cross-volume consistency)
- **file anchors** (`chapters/...:line-line`)
- **primary source anchors** (author + year + theorem / equation)
- **exact formulas / constants** (no symbolic shorthand; full statement)
- **claim-status recommendation** (`\ClaimStatusProvedHere` / `\ClaimStatusConjectured` / `\ClaimStatusEvidence` / `\ClaimStatusRetracted`)
- **files changed** (paths + line counts)
- **tests / computations run** (file + line + outcome)
- **remaining open obligations** (named, with proof obligation language)

The orchestrator integrates these into a single deep-semantic merge.

---

## Expected outcome

After all phases land:

- macro layer added to `main.tex` preamble; `make verify-licensing` green.
- 4 GAP-closing commits (dismissals 10, 14, 16, 17) across 8+ chapters.
- κ-tuple K3$\times E$ counterexample inscribed in 3 chapters (concordance + climax + Theorems C/D).
- four Construction Problems explicitly named in Part VII closing + cross-referenced from FRONTIER.md.
- four-object cyclic-Hochschild discipline added to `hochschild.tex`.
- heptagon-face / licensing-type duality remark in `sc_chtop_heptagon.tex`.
- 8 IV test files in `compute/tests/`; `make verify-independence` green.
- 5 batches of CG-rectified chapters (~14 chapters touched) with platonic-ideal voice convergence.
- Cross-volume back-edits in Vol I, Vol III, mixed-HT-strings, igusa.
- `make fast` builds clean; `out/main.pdf` resolves; page-count delta documented.
- one feedback memory if any new user-validated discipline emerged.

The thesis stands by itself. The form Vol II yearned to be is the form Vol II is.
