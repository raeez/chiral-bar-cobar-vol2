# Agent 12 Register / Status Audit

Scope: active Vol II TeX only, as read from `main.tex` by excluding commented
`\input{...}` lines. Active graph size: 105 files, matching
`metadata/theorem_registry.md` (`Active files in main.tex | 105`).

Normative inputs used:
- `CLAUDE.md:152-166`: forbidden manuscript register: bookkeeping vocabulary,
  process labels, drafting-history language, meta-narration.
- `CLAUDE.md:437-438`: claim-status tags are reader-facing bookkeeping; default
  to `\ClaimStatusConjectured` when uncertain.
- `chapters/connections/concordance.tex:1-10`: concordance governs
  chapter-local status disagreements.
- `metadata/theorem_registry.md:9-37`: 2351 `ProvedHere` claims, 2971 tagged
  claims, 105 active files.
- `metadata/claims.jsonl`: label/status/file anchors for current theorem tags.

I did not edit shared TeX. Heal items below are exact proposed deletions,
demotions, or replacements.

## Cycle 1: Forbidden Bookkeeping / Draft-History Register

**ATTACK.** The active manuscript still contains reader-facing process labels,
draft history, retraction history, and campaign vocabulary forbidden by
`CLAUDE.md:152-166`.

Exact anchors:
- `chapters/connections/fractional_ghost_chain_level_platonic.tex:86`: "stated
  in an earlier draft at".
- `chapters/connections/fractional_ghost_chain_level_platonic.tex:570`: "is
  superseded".
- `chapters/connections/fractional_ghost_chain_level_platonic.tex:649`: "wave-14
  anchor".
- `chapters/connections/bv_brst.tex:629-631`: remark title "Earlier draft errors
  corrected" and body "The earlier draft of".
- `chapters/connections/modular_pva_quantization_core.tex:2697,2725`: "wave-14".
- `chapters/theory/pva-expanded-repaired.tex:18`: "wave-14 universal holography
  master theorem".
- `chapters/theory/pva-descent-repaired.tex:21`: "wave-14 anchors".
- `chapters/theory/bp_chain_level_strict_platonic.tex:148`: "wave-14 climax".
- `chapters/theory/wn_tempered_closure_platonic.tex:533-537,553`: "supersedes
  Candidates A/B", "SUPERSEDED", "wave-14".
- `chapters/theory/foundations.tex:850`: "Vol II first-principles cache entry".
- `chapters/theory/super_chiral_yangian.tex:226,301,304,326`: AP-coded labels
  (`rem:ap138-absorbed`, `lem:ap107-sign`, `eq:ap107-sign`,
  `rem:ap105-absorbed`) and `super_chiral_yangian.tex:1125`: "bookkeeping".

**HEAL.**
- Delete drafting-history clauses rather than rewriting them as history.
- Replace process titles with mathematical titles:
  - `Earlier draft errors corrected` -> `BV-BRST Scope Correction`.
  - `anchor: non-principal DS as universal-conductor input` -> `Non-principal DS
    input for conductor comparison`.
- Replace wave/campaign phrases by theorem names:
  - "wave-14 universal holography master theorem" -> `Theorem~\ref{thm:universal-holography-functor}`.
  - "wave-14 climax" -> `the universal holography theorem`.
- Rename AP labels to mathematical labels:
  - `rem:ap138-absorbed` -> `rem:super-yangian-gl-osp-parity`.
  - `lem:ap107-sign` / `eq:ap107-sign` -> `lem:super-yangian-odd-odd-sign` /
    `eq:super-yangian-odd-odd-sign`.
  - `rem:ap105-absorbed` -> `rem:super-yangian-sign-normalization`.
- Replace `foundations.tex:850` sentence with a primary mathematical anchor or
  delete it. No cache-entry citation belongs in active TeX.

## Cycle 2: Prohibited Provenance Comments

**ATTACK.** Persistent source comments in active TeX mention prohibited
provenance. The hard rule excludes provenance comments from repository text
even when they are not typeset.

Exact anchors:
- `chapters/connections/fractional_ghost_chain_level_platonic.tex:16`: source
  provenance comment.
- `chapters/theory/bp_chain_level_strict_platonic.tex:59`: source provenance
  comment.
- `chapters/connections/log_ht_monodromy_frontier.tex:677`: source provenance
  comment before the chromatic sections.
- `chapters/connections/log_ht_monodromy_frontier.tex:686`: `%%% See AP-CHR,
  AP-RED, AP-TOWER in CLAUDE.md.`

**HEAL.**
- Delete the two source-provenance comments outright.
- Delete `log_ht_monodromy_frontier.tex:677` and `:686`, or replace with a
  mathematical comment only:
  `% Chromatic sections: synthetic spectra, transchromatic character maps, and height towers.`

## Cycle 3: Undefined / Invalid Claim-Status Tags

**ATTACK.** Active TeX uses two status macros not defined in `main.tex`, whose
defined status macros are only `ProvedHere`, `ProvedElsewhere`, `Open`,
`Conjectured`, `Heuristic`, `Conditional`, and `NeedsVerification`
(`main.tex:102-106,216-217`).

Exact anchors:
- `chapters/theory/topologization_class_m_original_complex_platonic.tex:135`:
  `\ClaimStatusRetracted` is undefined.
- `chapters/examples/examples-complete-proved.tex:1017`:
  `\ClaimStatusProvedHereConditional` is undefined.

**HEAL.**
- `topologization_class_m_original_complex_platonic.tex:135`: do not add a new
  status macro. Remove the active chapter from `main.tex`, or convert the opening
  block to `\ClaimStatusConjectured`/`\ClaimStatusNeedsVerification` only if a
  mathematically current claim remains. The current text says the chapter is a
  historical record, so the correct heal is to remove it from the active graph.
- `examples-complete-proved.tex:1017`: replace
  `\ClaimStatusProvedHereConditional` with `\ClaimStatusConditional`.

## Cycle 4: Unsupported `ProvedHere` / Registry Drift

**ATTACK.** The independent-verification auditor fails:

`python3 compute/scripts/audit_independent_verification.py --tex-root . --tests-dir compute/tests --show-orphans`

Result:
- 1747 `ProvedHere`-tagged labels found by the auditor.
- 193 with independent verification (11.0%).
- 1554 without independent verification.
- 9 orphan registry entries.
- 74 test modules failed to import because `pytest`/`sympy` are unavailable in
  this environment; these are not counted as coverage.

The fatal register/status issue is the orphan set: tests decorate labels that
do not exist as current TeX claims.

Exact orphan anchors:
- `compute/tests/test_fm81_fractional_ghost.py:203` decorates
  `prop:three-lane-fm81`, but the current active label is
  `prop:three-lane-fractional-ghost` at
  `chapters/connections/fractional_ghost_chain_level_platonic.tex:525`
  (`metadata/claims.jsonl:583`).
- `compute/tests/test_fm81_fractional_ghost.py:339` decorates
  `cor:fm81-healed-non-principal`, but the current active label is
  `cor:fractional-ghost-healed-non-principal` at
  `fractional_ghost_chain_level_platonic.tex:488`
  (`metadata/claims.jsonl:582`).
- `compute/tests/test_universal_holography_functor_fm_iv.py:36,78,129,172,211,267,325`
  decorate `prop:uhf-fm125-*`, `prop:uhf-fm126-*`, `prop:uhf-fm185-*`,
  `prop:uhf-fm186-*`, `prop:uhf-fm187-*`, `prop:uhf-fm188-*`,
  `prop:uhf-fm214-*`.
  Current labels are:
  - `prop:uhf-koszul-triangle-projection`
    (`universal_holography_functor.tex:698`, `metadata/claims.jsonl:2160`).
  - `prop:uhf-global-triangle`
    (`universal_holography_functor.tex:734`, `metadata/claims.jsonl:2161`).
  - `prop:uhf-shadow-vs-holographic`
    (`universal_holography_functor.tex:764`, `metadata/claims.jsonl:2162`).
  - `prop:uhf-symplectic-polarization`
    (`universal_holography_functor.tex:799`, `metadata/claims.jsonl:2163`).
  - `prop:uhf-kel06-chirality`
    (`universal_holography_functor.tex:824`, `metadata/claims.jsonl:2164`).
  - `prop:uhf-hkr-disentangled`
    (`universal_holography_functor.tex:862`, `metadata/claims.jsonl:2165`).
  - `prop:uhf-universal-scope`
    (`universal_holography_functor.tex:906`, `metadata/claims.jsonl:2166`).

The same missing `prop:uhf-fm*` labels are still referenced in active
`chapters/connections/part_vi_platonic_introduction.tex:370-374,534-536,562-578`.

**HEAL.**
- Change test decorator claims to the current labels listed above.
- Change `part_vi_platonic_introduction.tex` references:
  - `prop:uhf-fm125-koszul-triangle-projection` ->
    `prop:uhf-koszul-triangle-projection`.
  - `prop:uhf-fm126-global-triangle` -> `prop:uhf-global-triangle`.
  - `prop:uhf-fm185-shadow-vs-holographic` ->
    `prop:uhf-shadow-vs-holographic`.
  - `prop:uhf-fm186-symplectic-polarization` ->
    `prop:uhf-symplectic-polarization`.
  - `prop:uhf-fm187-kel06-chirality` -> `prop:uhf-kel06-chirality`.
  - `prop:uhf-fm188-hkr-disentangled` -> `prop:uhf-hkr-disentangled`.
  - `prop:uhf-fm214-universal-scope` -> `prop:uhf-universal-scope`.
- Change `prop:three-lane-fm81` -> `prop:three-lane-fractional-ghost`.
- Change `cor:fm81-healed-non-principal` ->
  `cor:fractional-ghost-healed-non-principal`.

## Cycle 5: Theorem / Prose / Status Drift Against Concordance

**ATTACK 5.1.** `topologization_class_m_original_complex_platonic.tex` is
actively included by `main.tex:1976`, but its opening says it is a historical
record of a retracted dichotomy. It also keeps current `\ClaimStatusProvedHere`
tags on retracted theorem blocks:
- `topologization_class_m_original_complex_platonic.tex:327-329`
- `topologization_class_m_original_complex_platonic.tex:437-439`
- `topologization_class_m_original_complex_platonic.tex:608-611`
- `topologization_class_m_original_complex_platonic.tex:712-715`
- `topologization_class_m_original_complex_platonic.tex:777-780`

The surrounding active chapters state the opposite current result:
`tempered_stratum_characterization_platonic.tex:152` says the corollary is
retracted; `wn_tempered_closure_platonic.tex:384-405` proves the healed
principal `W_N` dichotomy.

**HEAL 5.1.** Remove
`\input{chapters/theory/topologization_class_m_original_complex_platonic}` from
`main.tex`, or quarantine the whole file outside the active graph. Do not leave
reader-facing `ProvedHere` tags that the chapter itself says are superseded.

**ATTACK 5.2.** Topologisation ladder status drift. The chapter itself says
antighost BRST-commutativity is not proved for spins `n,m >= 4`:
`e_infinity_topologization.tex:425-475`. But
`thm:e-infinity-specialisation-WN` is `\ClaimStatusProvedHere` for all `N` at
`e_infinity_topologization.tex:732-750`, and its proof asserts the missing
step at `:777-782`.

**HEAL 5.2.** Split the theorem:
- `N=2,3`: keep `\ClaimStatusProvedHere`.
- `N>=4`: change to `\ClaimStatusConditional`, conditional on axiom
  `tower:antighost-commutativity` and jet-action hypotheses through spin `N`.
- Replace lines `777-782` with: "For `N>=4` this is precisely the conditional
  hypothesis of Axiom~\ref{tower:antighost-commutativity}; the theorem is
  unconditional only in the low-spin cases isolated in
  Remark~\ref{rem:axiom-T5-scope}."

**ATTACK 5.3.** The `W_\infty` endpoint overpromotes the same missing axiom.
`w_infty_e_infty_endpoint_platonic.tex:436-458` marks the endpoint
`\ClaimStatusProvedHere`, and `:680-706` says the conditional clause is
replaced. This contradicts `e_infinity_topologization.tex:472-475`, which says
the `W_\infty` specialization inherits conditional status until all-spin
antighost commutativity is derived.

**HEAL 5.3.** Change the endpoint theorem to `\ClaimStatusConditional` unless
the all-spin antighost proof is inscribed. Replace `:692-706` with a conditional
statement: GGL/CKL/PRS verify structure-constant convergence and truncation,
but do not prove all-spin antighost BRST-commutativity.

**ATTACK 5.4.** Off-by-one threshold drift in the `W_\infty` endpoint.
`w_infty_e_infty_endpoint_platonic.tex:374-408` states
`N_0(w_max)=2w_max-1`, but the proof itself says the GGL threshold requires
`N >= max(...)=2w` at `:395-398`, then concludes `2w-1` at `:399-408`.

**HEAL 5.4.** Either change the proposition to
`N_0(w_max)=2w_max`, or add a separate lemma proving triangular stabilization
at `2w-1` from the cited recursion. Without that lemma, demote the sharpened
`2w-1` claim to `\ClaimStatusConjectured` and use `2w` in theorem statements.

**ATTACK 5.5.** Modular Swiss-cheese status overreach. Agent 02's earlier audit
is confirmed against active TeX:
- `modular_swiss_cheese_operad.tex:1350-1372` marks `prop:extraction-functor`
  `\ClaimStatusProvedHere` while claiming higher-genus faithfulness. This is
  stronger than formal-collision extraction.
- `modular_swiss_cheese_operad.tex:1478-1490` marks all-genus modular
  homotopy-Koszulity `\ClaimStatusProvedHere`, while the proof has to pass from
  genus-0 local homotopy-Koszulity to full modular operation spaces.
- `modular_swiss_cheese_operad.tex:4489-4560` puts K3/Hilbert-scheme
  Grojnowski--Nakajima stabilization inside the local modular Swiss-cheese
  chapter as `\ClaimStatusProvedHere`, but that is global geometric
  representation theory, not a consequence of local SC modular formality.

**HEAL 5.5.**
- `prop:extraction-functor`: retain `\ClaimStatusProvedHere` only for
  construction and restriction compatibility. Delete or demote
  higher-genus faithfulness/equivalence clauses to `\ClaimStatusConjectured`
  unless a global reconstruction theorem is added.
- `thm:modular-hkoszul-SC`: restrict to the formal local model, or change the
  all-genus statement to `\ClaimStatusConditional` on global modular formality.
- Move K3/Hilbert-scheme results out of Route A/local `SCmod`, or demote to
  `\ClaimStatusConjectured` with explicit global factorization-base hypotheses.

**ATTACK 5.6.** Factorization Swiss-cheese status drift. Concordance says the
recognition/local-shadow statements are conditional
(`concordance.tex:53,57,77`). The active chapter has improved scoping at
`factorization_swiss_cheese.tex:1725-1755`, but still marks
`thm:factorization-SC-koszul` `\ClaimStatusProvedHere` at `:2066-2095` for
all-genus Feynman-transform recovery, and `thm:chiral-RH` `\ClaimStatusProvedHere`
at `:3510-3528` for a broad chiral Riemann--Hilbert correspondence.

**HEAL 5.6.**
- Change `thm:factorization-SC-koszul` to `\ClaimStatusConditional` for
  all-genus recovery, with genus-0 recovery separated as `\ClaimStatusProvedHere`.
- Change `thm:chiral-RH` to `\ClaimStatusConditional` unless the analytic
  curved/coderived comparison theorem is supplied in the same chapter.

## Priority Register

1. Remove the active retracted `topologization_class_m_original_complex` chapter
   from `main.tex`, or demote every retained claim and quarantine it from reader
   flow.
2. Fix undefined status macros: `\ClaimStatusRetracted` and
   `\ClaimStatusProvedHereConditional`.
3. Remove persistent source-provenance comments.
4. Fix independent-verification orphan labels and matching Part VI stale refs.
5. Split/demote topologisation ladder and `W_\infty` endpoint claims according
   to the antighost-commutativity gap.
6. Demote all-genus modular/factorization Swiss-cheese claims unless the missing
   global comparison hypotheses are inscribed.
