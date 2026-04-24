# Agent 10: Compute Evidence / Claim Registry Examiner

Date: 2026-04-24.
Scope owned: `compute/audit/architecture_swarm_20260424/agent10_compute_evidence.md` only.
Shared TeX edited: no.
Compute source edited: no.
Commits/pushes: no.

## Surfaces Read

- `CLAUDE.md`, `AGENTS.md`.
- `metadata/theorem_registry.md`, `metadata/claims.jsonl`.
- `scripts/generate_metadata.py`.
- `compute/lib/independent_verification.py`.
- `compute/scripts/audit_independent_verification.py`.
- `compute/lib/recognition_theorem_engine.py`.
- `compute/tests/test_recognition_theorem_engine.py`.
- `compute/lib/swiss_cheese_virasoro_wheels.py`.
- `compute/tests/test_swiss_cheese_virasoro_wheels.py`.
- `compute/tests/test_universal_holography_functor.py`.
- `compute/tests/test_universal_holography_functor_fm_iv.py`.
- `compute/tests/test_climax_theorems_iv.py`.
- `compute/tests/test_climax_theorems_wave17_iv.py`.
- `compute/tests/test_part_vi_platonic_introduction.py`.
- `compute/tests/test_monster_chain_level_e3_top.py`.
- `compute/tests/test_schellekens_71_alpha_classification.py`.
- Targeted TeX anchors in `chapters/connections/universal_holography_functor.tex`, `chapters/connections/part_vi_platonic_introduction.tex`, `chapters/connections/monster_chain_level_e3_top_platonic.tex`, `chapters/connections/schellekens_71_alpha_classification_platonic.tex`, `chapters/examples/w-algebras-stable.tex`, `chapters/theory/foundations.tex`, `chapters/theory/locality.tex`, `chapters/connections/conclusion.tex`.

## Commands Run

```text
git status --short
```

Observed a heavily dirty worktree, including shared TeX, compute tests, compute libraries, and metadata. I treated all pre-existing changes as external work.

```text
PYTHONDONTWRITEBYTECODE=1 compute/.venv/bin/python -m pytest compute/tests/test_recognition_theorem_engine.py -q -ra
46 passed in 1.99s

PYTHONDONTWRITEBYTECODE=1 compute/.venv/bin/python -m pytest compute/tests/test_swiss_cheese_virasoro_wheels.py -q -ra
106 passed in 2.08s

PYTHONDONTWRITEBYTECODE=1 compute/.venv/bin/python -m pytest compute/tests/test_universal_holography_functor.py compute/tests/test_universal_holography_functor_fm_iv.py -q -ra
9 passed in 0.07s

PYTHONDONTWRITEBYTECODE=1 compute/.venv/bin/python -m pytest compute/tests/test_climax_theorems_iv.py compute/tests/test_part_vi_platonic_introduction.py compute/tests/test_monster_chain_level_e3_top.py compute/tests/test_schellekens_71_alpha_classification.py -q -ra
33 passed in 0.08s

PYTHONDONTWRITEBYTECODE=1 compute/.venv/bin/python -m pytest compute/tests/test_climax_theorems_wave17_iv.py -q -ra
20 passed in 0.08s

PYTHONDONTWRITEBYTECODE=1 compute/.venv/bin/python -m pytest compute/tests/test_independent_verification_infra.py -q -ra
7 passed in 0.10s
```

```text
PYTHONDONTWRITEBYTECODE=1 compute/.venv/bin/python compute/scripts/audit_independent_verification.py --show-orphans
AUDIT RESULT: FAIL
ProvedHere claims found in .tex: 1747
Claims with independent verification: 245 (14.0%)
Claims WITHOUT independent verification: 1502
Tautological registry entries: 0
Orphan registry entries: 10
```

The orphan entries include `thm:universal-holography`, `prop:three-lane-fm81`, `cor:fm81-healed-non-principal`, and all seven `prop:uhf-fmXXX-*` UHF labels.

```text
PYTHONDONTWRITEBYTECODE=1 compute/.venv/bin/python - <<'PY'
from scripts.generate_metadata import get_active_files, get_all_tex_files, extract_claims
...
PY
generated_claims 2989
generated_status_counts {'ProvedHere': 2358, 'ProvedElsewhere': 273, 'Conjectured': 221, 'Heuristic': 39, 'Conditional': 97, 'Open': 1}
metadata_claims 2971
metadata_status_counts {'ProvedHere': 2351, 'ProvedElsewhere': 271, 'Conjectured': 217, 'Heuristic': 38, 'Conditional': 93, 'Open': 1}
delta_labels_generated_minus_metadata 19
delta_labels_metadata_minus_generated 1
```

I did not run `scripts/generate_metadata.py` directly because it writes shared metadata files.

## Executive Findings

1. Fatal: independent-verification audit fails. Ten decorated test claims are orphaned from live TeX labels. The UHF FM decorators target stale labels such as `prop:uhf-fm125-koszul-triangle-projection`, while live TeX uses `prop:uhf-koszul-triangle-projection` and siblings.
2. Fatal: the claim registry counts are not stable evidence. `metadata/theorem_registry.md` reports 2351 `ProvedHere` claims, but a no-write invocation of the generator over the current tree finds 2358. The independent-verification scraper finds only 1747 ProvedHere-tagged labels.
3. High: 818 metadata `ProvedHere` claims are unlabeled synthetic entries (`__unlabeled_*`). They cannot be targeted by label-based independent verification in a durable way.
4. High: the recognition engine is a local-shadow smoke-test engine, not proof-grade evidence for `thm:recognition-SC`. Live TeX marks `thm:recognition-SC` and `thm:recognition` Conditional, while the engine returns success flags by construction.
5. High: the Virasoro wheel engine supports finite symbolic/numerical probes, but it does not prove the all-arity claim `m_k != 0` for every `k >= 3`. The live reference `prop:vir-all-mk` is only a phantom label in `conclusion.tex`.
6. High: universal-holography and climax tests pass, but much of the evidence is structural dictionaries, hardcoded constants, decorator metadata, or `assert True`. These tests should not be counted as independent computational verification of `ProvedHere`.

## ATTACK -> HEAL Cycles

### Cycle 1: ProvedHere Count Integrity

**ATTACK.** `metadata/theorem_registry.md:9-10` says 2351 `ProvedHere` claims and 2971 total tagged claims. A no-write run of the generator functions in `scripts/generate_metadata.py:489-515` over the current tree finds 2358 `ProvedHere` and 2989 total. The registry is stale relative to the current source surface.

**HEAL.** Add a non-writing check mode to `scripts/generate_metadata.py` and a targeted test:

```text
python3 scripts/generate_metadata.py --check
```

The check should fail if generated counts differ from `metadata/claims.jsonl` or `metadata/theorem_registry.md`. Do not rely on committed metadata after shared TeX changes until this passes.

### Cycle 2: Independent-Verification Orphans

**ATTACK.** `compute/scripts/audit_independent_verification.py --show-orphans` exits 2. Seven UHF FM tests decorate labels at `compute/tests/test_universal_holography_functor_fm_iv.py:35-36`, `77-78`, `128-129`, `171-172`, `210-211`, `266-267`, `324-325`. Live TeX labels are instead `prop:uhf-koszul-triangle-projection`, `prop:uhf-global-triangle`, `prop:uhf-shadow-vs-holographic`, `prop:uhf-symplectic-polarization`, `prop:uhf-kel06-chirality`, `prop:uhf-hkr-disentangled`, `prop:uhf-universal-scope` at `universal_holography_functor.tex:698`, `734`, `764`, `799`, `824`, `862`, `906`.

**HEAL.** Update the decorators to the live labels or add explicit TeX alias labels if the `fmXXX` names remain canonical. Then rerun:

```text
PYTHONDONTWRITEBYTECODE=1 compute/.venv/bin/python compute/scripts/audit_independent_verification.py --show-orphans
```

Acceptance criterion: zero orphan entries.

### Cycle 3: Unlabeled ProvedHere Claims

**ATTACK.** `metadata/claims.jsonl` contains 818 synthetic `__unlabeled_*` `ProvedHere` claims: 303 theorems, 256 propositions, 123 corollaries, 94 computations, 34 lemmas, 6 remarks, 2 maintheorems. These are not durable claim identities. The IV registry can only decorate stable labels.

**HEAL.** Introduce a claim-registry lint that fails for unlabeled `ProvedHere` theorem-like environments, except for an explicit allowlist. Minimum target: every `theorem`, `proposition`, `corollary`, `computation`, and `lemma` with `\ClaimStatusProvedHere` must have a non-`eq:` label in the environment header.

### Cycle 4: Recognition Engine Overclaim

**ATTACK.** `compute/lib/recognition_theorem_engine.py:375` sets `descent_verified = True` unconditionally. `product_weiss_descent_dimensions` returns `product_structure = True` at line 796. `recognition_theorem_check` states kappa consistency is verified but sets `kappa_consistent = True` at line 827 and never uses it. The target theorem is Conditional in live TeX: `chapters/theory/locality.tex:431-448`; the foundations alias is also Conditional at `chapters/theory/foundations.tex:2460-2462`.

**HEAL.** Rename the engine output to `local_shadow_smoke_test` or add actual falsifying checks: non-product covers, failed H1/H2/H3/H4 examples, and real equality/quasi-isomorphism assertions. Do not count this engine as evidence for a `ProvedHere` recognition theorem unless the TeX status is changed by a proof.

### Cycle 5: C-Direction Factorization False Positive

**ATTACK.** The C-factorization helper reports success even when its own dimensions disagree. Probe output:

```text
factorization 2 disk_dims [6, 6] tensor 36 union 6 holds_flag True
factorization 3 disk_dims [6, 6, 6] tensor 216 union 6 holds_flag True
```

The cause is `verify_c_direction_factorization` computing the union as the convex hull interval at `recognition_theorem_engine.py:947-954`, then returning `factorization_holds = True` at `956-963`.

**HEAL.** Represent disjoint unions as disjoint unions, not the bounding interval. Add assertions:

```text
assert result["tensor_product_dim"] == result["union_dim"]
assert not verify_c_direction_factorization(...bad union...)["factorization_holds"]
```

Until then, this test is a structural smoke test, not evidence for factorization.

### Cycle 6: Virasoro Wheel All-Arity Claim

**ATTACK.** The wheel tests cover `m_k != 0` only through `k=6` in `compute/tests/test_swiss_cheese_virasoro_wheels.py:486-511`. The code for `m_4` says the computation is partial and returns a note at `swiss_cheese_virasoro_wheels.py:529-640`. The recursive numerical method says it tracks only total magnitude and non-vanishing, not exact coefficients, at `692-714`; middle-slot sesquilinearity is simplified at `866-870`. `wheel_integral_form_degree` returns `non_degenerate = True` at `1208-1217` without evaluating the integral.

**HEAL.** State compute support as: exact symbolic check for `m_3`; numerical Stasheff-style probes for bounded arity; combinatorial wheel-count smoke tests. To support `m_k != 0` for all `k`, add either a symbolic recurrence with a nonzero leading monomial for all `k` or downgrade the theorem status to bounded computational evidence plus conjectural all-arity extrapolation.

### Cycle 7: Phantom Label `prop:vir-all-mk`

**ATTACK.** `chapters/examples/w-algebras-stable.tex:1024-1026` and `1093-1096` invoke `Proposition~\ref{prop:vir-all-mk}` for the all-arity Virasoro wheel claim. The only live label is a phantom label in `chapters/connections/conclusion.tex:2219-2224`, not attached to the proposition at `w-algebras-stable.tex:171-181`.

**HEAL.** Put `\label{prop:vir-all-mk}` on the actual proposition or update all references to the live theorem/proposition label. Add a metadata lint: a theorem dependency edge must not resolve to a `\phantomsection` label unless it is explicitly marked as a forward-reference placeholder and excluded from `ProvedHere` dependency evidence.

### Cycle 8: UHF / Climax Tests as Bibliographic Scaffold

**ATTACK.** `compute/lib/independent_verification.py:166-241` enforces disjoint source strings and records a registry entry; it does not verify that the decorated test computes a theorem consequence. Several tests are explicitly structural constants:

- `test_universal_holography_functor.py:121-183` compares hand-written dictionaries.
- `test_climax_theorems_iv.py:335-342` and `449-457` include `assert True`.
- `test_climax_theorems_wave17_iv.py:23-28` warns that decorator bodies are bibliographic scaffolding, not numerical cross-verification.
- `test_universal_holography_functor_fm_iv.py:17-19` says the same, but a previous explicit "Do NOT count" flag has been removed in the current diff.

**HEAL.** Add a decorator flag such as `evidence_kind="bibliographic_scaffold"` versus `evidence_kind="computed"`. The coverage report should distinguish them and must not report scaffold-only entries as computational IV coverage.

### Cycle 9: Hardcoded Architecture Constants

**ATTACK.** The Part VI, Monster, and Schellekens tests hardcode the constants they claim to verify:

- `test_part_vi_platonic_introduction.py:67-88` sets `c_chiral = 26`, computes `c/2`, and asserts the chosen result.
- `test_part_vi_platonic_introduction.py:129-144` defines depth as `N - 1` and asserts `2 + depth == N + 1`.
- `test_part_vi_platonic_introduction.py:250-274` sets `c_Vnatural = 24`, `leech_rank = 24`, and `dw_anomaly_class = 0`.
- `test_monster_chain_level_e3_top.py:175-195` derives the trivial DW class after assigning the trivial fixed lattice and trivial epsilon restriction; `203-205` hardcodes `196_884`.
- `test_schellekens_71_alpha_classification.py:104-133` hardcodes `24`, `1`, `71`, `46`, and all alpha values as zero.

**HEAL.** Move the constants into independently parsed source artifacts or executable derivations: a small Niemeier table, a Conway frame-shape table, a group-cohomology computation for `H^3(BZ/n; U(1))`, and a character-coefficient parser for the Monster/Leech series. Tests should fail if those sources disagree with the theorem constants.

## Highest-Risk Unsupported Claims

1. `thm:universal-holography-functor`: has one structural test, but UHF consequence decorators are orphaned or scaffold-only. The live theorem remains much stronger than compute evidence.
2. `prop:uhf-*` consequence block: the seven tests point to stale `prop:uhf-fmXXX-*` labels and do not cover the live labels until corrected.
3. `thm:recognition-SC` / `thm:recognition`: live status Conditional; compute engine should not be treated as `ProvedHere` support.
4. `prop:vir-all-mk`: all-arity Virasoro wheel non-vanishing is referenced through a phantom label and supported by bounded/simplified compute, not an all-arity proof.
5. Aggregate `ProvedHere` totals: current metadata, generator output, and IV scraper disagree materially; registry counts should not be quoted as evidence until reconciled.
6. Schellekens 71 and Monster alpha-zero claims: current tests are useful consistency checks but rely heavily on hardcoded classification counts and zero anomaly assignments.

## Files Changed

- Added this report only:
  `compute/audit/architecture_swarm_20260424/agent10_compute_evidence.md`.
