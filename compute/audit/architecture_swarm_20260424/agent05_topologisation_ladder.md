# Agent 05: Topologisation Ladder Examiner

Date: 2026-04-24.
Scope owned: `compute/audit/architecture_swarm_20260424/agent05_topologisation_ladder.md` only.
Shared TeX edited: no.
Commits/pushes: no.

## Surfaces Read

- `CLAUDE.md`, `AGENTS.md`, `main.tex`.
- `chapters/connections/e_infinity_topologization.tex`.
- `chapters/connections/w_infty_e_infty_endpoint_platonic.tex`.
- `chapters/theory/topologization_class_m_original_complex_platonic.tex`.
- `chapters/theory/wn_tempered_closure_platonic.tex`.
- `chapters/examples/w-algebras-virasoro.tex`, `chapters/examples/w-algebras-w3.tex`, and targeted grep/chunks over `chapters/examples/w-algebras*.tex`.
- Vol I `~/chiral-bar-cobar/chapters/examples/landscape_census.tex`.
- Vol III `~/calabi-yau-quantum-groups/CLAUDE.md`.
- Focused tests:
  `compute/tests/test_e_infinity_topologization.py`,
  `compute/tests/test_w_infty_endpoint.py`,
  `compute/tests/test_wn_tempered_closure.py`,
  `compute/tests/test_topologization_class_m_original_complex.py`.

## Tests Run

```text
compute/.venv/bin/python -m pytest \
  compute/tests/test_e_infinity_topologization.py \
  compute/tests/test_w_infty_endpoint.py \
  compute/tests/test_wn_tempered_closure.py \
  compute/tests/test_topologization_class_m_original_complex.py -q -ra

33 passed in 3.08s
```

The tests are mostly structural/decorator tests. They do not catch the status contradictions below; in fact several docstrings still encode superseded claims.

## Executive Findings

1. Fatal: the central finite-depth ladder is overmarked as `\ClaimStatusProvedHere` beyond `N <= 3`. The text itself says antighost BRST-commutativity is only an axiom for spins `>= 4`.
2. Fatal: the derivation equating higher-spin zero modes with higher holomorphic jets is not proved and is generally false without an extra jet-action hypothesis.
3. Fatal: the `W_\infty` endpoint chapter closes GGL/OPE convergence, but it does not close the missing antighost BRST-commutativity theorem. The endpoint remains conditional unless a new antighost-OPE theorem is inserted.
4. Moderate: the `k`/`N` indexing has off-by-one errors in the ladder theorem, the forgetful maps, the endpoint proof, and truncation-locus companion.
5. Moderate: the original-complex status layer is inconsistent across active chapters and tests; `\ClaimStatusRetracted` also appears undefined in the active input graph.

## ATTACK -> HEAL Cycles

### Cycle 1: `k` Inner Stress Tensors -> `E_{k+2}^{top}`

**ATTACK.** In `e_infinity_topologization.tex:543-572`, the theorem ranges over `0 <= k <= N-1` and calls every rung `E_{k+2}^{top}`. But the proof only obtains the first topological promotion after the spin-2 antighost: `e_infinity_topologization.tex:581-592` calls this the `k = 1` rung. The theorem also says the forgetful map discards `G^{(k+1)}` at `e_infinity_topologization.tex:561`, while the proof correctly discards `G^{(k+2)}` at `e_infinity_topologization.tex:646-649`.

**HEAL.** Insert immediately before `e_infinity_topologization.tex:543`:

> The index `k` counts the number of stress-tower antighosts actually used. The baseline `k=0` object is the derived-centre `E_2` Deligne structure; the topological ladder starts at `k=1`, using `G^{(2)}` and yielding `E_3^{top}`. For `1 <= k <= N-1`, the antighosts `G^{(2)},...,G^{(k+1)}` yield `E_{k+2}^{top}`.

Then replace `discarding the highest antighost G^{(k+1)}` by `G^{(k+2)}` at line 561.

### Cycle 2: Higher-Spin Modes vs Holomorphic Jets

**ATTACK.** The construction says `T^{(n)}_{(0)}` acts as `partial_z^{n-1}/(n-1)!` on primary fields (`e_infinity_topologization.tex:174-184`) and uses this to identify `T^{(n)}=[Q,G^{(n)}]` with exactness of higher holomorphic derivatives (`e_infinity_topologization.tex:296-304`, `595-610`). For vertex algebras, the conformal vector gives translation through `T_{(0)} = L_{-1}`. A higher-spin zero mode is a `W`-charge/differential operator on modules, not automatically the `(n-1)`-jet of the coordinate. This is the main mathematical gap in the ladder.

**HEAL.** Replace the assertion at `e_infinity_topologization.tex:174-184` with a named hypothesis:

> Jet-action hypothesis `J_n`: the spin-`n` Casimir field has a mode, or a specified linear combination of modes and descendants, whose action on the relevant bulk factorisation algebra represents the `(n-1)`-st holomorphic jet generator. The equality with `partial_z^{n-1}/(n-1)!` is part of the hypothesis unless proved by an explicit OPE computation.

Then state the ladder theorem conditional on `J_3,...,J_N`; keep `N=2` proved.

### Cycle 3: BRST Primitive Formula

**ATTACK.** `thm:iterated-sugawara-construction` is marked proved at `e_infinity_topologization.tex:332-364`, but the primitive formula is internally inconsistent: equation `G-n-formula` uses coefficients `1/j` (`352-360`), while the proof uses `1/n` (`390-397`). If `[Q,\bar c_a]=J_a`, the naive primitive of a degree-`n` monomial is a signed sum over one-slot substitutions; a universal `1/n` normalization needs a convention, and `1/j` is not justified. The proof also assumes every generating current of the DS boundary algebra is `Q_tot`-exact (`372-383`), which is stronger than the cited spin-2 DS identity.

**HEAL.** Downgrade `thm:iterated-sugawara-construction` to a conditional construction for `n >= 3`:

> If the DS boundary current system admits bulk antighost lifts with `[Q_tot,\bar c_a]=J_a` and if normal-ordering/contact terms are cancelled by explicit quantum corrections, then a primitive is given by the signed one-slot substitution formula
> `G_P = sum_j (-1)^{epsilon_j} :J_1 ... \bar c_j ... J_n:`
> after fixing the normalization of `[Q,\bar c]`.

Insertion anchor: replace `e_infinity_topologization.tex:332-364`; add a verification obligation after `425-450`.

### Cycle 4: Antighost Commutativity and Finite `W_N`

**ATTACK.** The file honestly says axiom `(T5)` is not derived from Linshaw/BMP (`e_infinity_topologization.tex:425-449`) and is postulated for `n,m >= 4` (`452-475`). But `thm:e-infinity-specialisation-WN` is marked `\ClaimStatusProvedHere` for all `N` at `732-750`; its proof then treats the classical Poisson bracket of stress tensors as if it proves antighost commutativity (`777-782`), contradicting the earlier warning.

**HEAL.** Split the W_N statement at `e_infinity_topologization.tex:732`:

> `N=2,3`: `\ClaimStatusProvedHere`, using the explicit low-spin OPE verification.
> `N>=4`: `\ClaimStatusConditional`, conditional on axiom `(T5)` and the jet-action hypotheses through spin `N`.

The proof line `777` should become: "Axiom (T5) is an additional hypothesis for `N >= 4`; for `N=3` it reduces to the finite `[G^{(2)},G^{(3)}]` computation."

### Cycle 5: `W_\infty -> E_\infty` Endpoint

**ATTACK.** `w_infty_e_infty_endpoint_platonic.tex:436-458` promotes the endpoint to `\ClaimStatusProvedHere`, and `680-706` says the conditional clause is replaced. The chapter proves or asserts GGL/OPE stabilisation, uniform weight-window bounds, and an inverse-limit operadic assembly. None of these proves antighost BRST-commutativity for all spins, the missing axiom isolated in the ladder file. Thus the endpoint closes the wrong conditional.

**HEAL.** At `w_infty_e_infty_endpoint_platonic.tex:436`, change the theorem scope to:

> At generic `(c,\lambda)`, the GGL/OPE and weight-window inverse-limit part is proved. The resulting `E_\infty^{top}` structure on the derived chiral centre is conditional on all-spin antighost BRST-commutativity and the jet-action hypotheses unless Proposition X proves these in the `W_\infty` bulk BV complex.

If the intended heal is an unconditional endpoint, insert a new theorem before `436` proving:

> `[G^{(n)},G^{(m)}]` is `Q_tot`-exact for all `n,m >= 4` in the Costello-Gaiotto/6d hCS defect BV model, with an explicit antighost OPE calculation.

### Cycle 6: Endpoint Off-by-One for Finite `W_N`

**ATTACK.** In the endpoint proof, finite `W_N` rungs are said to use spins `2,3,...,N+1` (`w_infty_e_infty_endpoint_platonic.tex:463-467`). But principal `W_N` has generators of spins `2,...,N` (`e_infinity_topologization.tex:737-743`; `w-algebras-frontier.tex:319-325`). The truncation companion repeats the same shift by saying `T^{(n)}` for `n > N+1` is absent (`w_infty_e_infty_endpoint_platonic.tex:548-555`).

**HEAL.** Replace `spins 2,3,...,N+1` by `spins 2,3,...,N` at line 467. Replace `n > N+1` by `n > N` at line 552. Keep the output `E_{N+1}^{top}`: it comes from `N-1` stress tensors plus the baseline/tangential/transverse count, not from a spin `N+1` generator.

### Cycle 7: Uniform Threshold `2w_max - 1`

**ATTACK.** `w_infty_e_infty_endpoint_platonic.tex:374-415` claims the uniform threshold is `N_0(w_max)=2w_max-1`. But the proof says the intermediate spin and structure constants satisfy `n_i <= 2w` and `max(n_1,n_2,n_3,k)=2w` (`391-408`), which by its own GGL threshold requires `N >= 2w`, not `2w-1`. The line "the max ... is exactly 2w and the required bound is N >= 2w - 1" is arithmetically unsupported. The compute test at `test_w_infty_endpoint.py:291-309` only asserts the formula tautologically.

**HEAL.** Either:

- use the safe proved bound `N_0(w_max)=2w_max`, or
- add the missing convention converting "spin `2w` intermediate" to truncation depth `2w-1` and prove that the spin-`2w` channel is absent or projected out in the bar-weight window.

Also change `w_infty_e_infty_endpoint_platonic.tex:417-426`: `2w_max-1` is not "sharper" than `w_max-1`; it is larger. The healed remark should say the previous bound was weight-one-at-a-time and insufficient for arity-two bar differentials.

### Cycle 8: Original-Complex Status Drift

**ATTACK.** The active input graph includes `topologization_class_m_original_complex_platonic.tex` (`main.tex:1976`). That chapter begins with a retraction notice (`133-181`) but uses `\ClaimStatusRetracted`, which is not defined in `main.tex` or the chapters. The same file keeps `\ClaimStatusProvedHere` on retracted statements (`608-648`, `712-821`). Newer `wn_tempered_closure_platonic.tex:187-207` says every generic principal `W_N` is tempered and original-complex `E_3` exists unconditionally, while `w-algebras-frontier.tex:1248-1261` still says the original-complex class-M statement is open/false. The tests still encode the obsolete `1/e` obstruction at `test_topologization_class_m_original_complex.py:1-55`.

**HEAL.** Insert a short active-status theorem near `topologization_class_m_original_complex_platonic.tex:133`:

> Current status: the dichotomy/`1/e` obstruction statements below are not active theorem content. The active theorem is the tempered-stratum result and its W_N closure.

Use an existing status macro or define `\ClaimStatusRetracted` in `main.tex` if the historical block remains active. Then update `w-algebras-frontier.tex:1248-1261` and the test docstring to the superseding status from `wn_tempered_closure_platonic.tex:187-207`.

### Cycle 9: Non-Critical-Level Hypotheses

**ATTACK.** The Virasoro specialisation says "non-critical central charge `c != 0`" (`e_infinity_topologization.tex:702-714`). For DS/Sugawara, non-critical is a level condition `k != -h^\vee`; Vol I explicitly says critical level breaks Sugawara, not Koszulness (`landscape_census.tex:1456-1461`). The condition `c != 0` is a separate curvature/nondegeneracy condition and is not equivalent to non-critical DS level.

**HEAL.** Replace the hypothesis with:

> Let `Vir_c` arise from principal DS reduction of `\widehat{\mathfrak{sl}}_2` at affine level `k != -2`; impose `c != 0` only where the curvature or shadow denominators require it.

For `W_N`, state `k != -N` and separate it from genericity/null-vector exclusions.

### Cycle 10: OPE Pole-Order and `E_\infty` Language in `W_3`

**ATTACK.** `w-algebras-w3.tex:884-892` says the quintic `WW` pole gives `W_3` an `E_\infty`-chiral algebra. A high pole order or infinite shadow depth is not an `E_\infty`-chiral structure. The correct conclusion is class-M/infinite-depth/non-formality, not commutativity up to all coherences. The pole-order convention itself is otherwise correctly stated elsewhere: the bar collision residue has one lower pole order (`w-algebras-w3.tex:802-804`; Vol I `landscape_census.tex:638-777`).

**HEAL.** Replace the `E_\infty`-chiral phrase at `w-algebras-w3.tex:891` with:

> the quintic pole places `W_3` in class `M` with infinite transferred `A_\infty` depth; it does not by itself produce an `E_\infty`-chiral structure.

## Exact Theorem Scopes Recommended

1. `thm:e-infinity-specialisation-Vir`: proved, after replacing "non-critical central charge `c != 0`" by the DS level condition plus separate `c != 0` where needed.
2. `thm:e-infinity-specialisation-WN`: proved for `N=2,3`; conditional for `N>=4` on antighost BRST-commutativity and jet-action hypotheses.
3. `conj:e-infinity-specialisation-Winfty`: keep conjectural/conditional unless a new all-spin antighost OPE theorem is inserted.
4. `thm:w-infty-e-infty-topologization-endpoint`: proved only for GGL/OPE stabilisation and inverse-limit assembly; conditional for full `E_\infty^{top}` topologisation for the same reason as (3).
5. `thm:climax-restatement-3d-infty`: should inherit conditional status from the `W_\infty` endpoint. The Virasoro `N=2` shadow remains proved.

## Residual Verification Obligations

- Prove or explicitly assume a jet-action theorem: higher-spin fields must act as the relevant formal holomorphic jet generators on the bulk factorisation algebra.
- Prove all-spin antighost BRST-commutativity in the BV model, not only stress-tensor OPE closure.
- Fix finite-depth indexing: stress spins `2..N` produce `E_{N+1}^{top}`; there is no spin `N+1` generator in `W_N`.
- Replace tautological endpoint tests with tests that catch off-by-one thresholds and status drift.
- Reconcile original-complex status across `topologization_class_m_original_complex_platonic.tex`, `wn_tempered_closure_platonic.tex`, `w-algebras-frontier.tex`, and the compute tests.

## Files Changed

- Added this report only:
  `compute/audit/architecture_swarm_20260424/agent05_topologisation_ladder.md`.
