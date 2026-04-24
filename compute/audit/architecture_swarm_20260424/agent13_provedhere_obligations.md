# Agent 13 Audit: `ProvedHere` Obligations Without Local First-Principles Proof

Scope: active Vol II architecture/design/master-synthesis surfaces, especially
`factorization_swiss_cheese`, `modular_swiss_cheese_operad`,
`relative_feynman_transform`, `chiral_higher_deligne`, `hochschild`,
`brace`, and Part VI/topologisation.

No source files were edited. No build was run. The generic deep-audit skill asks
for `compute/audit/linear_read_notes.md`, but the owned write scope for this
agent is this file only, so the actionable notes are recorded here.

Targeted checks run:

- `rg -n -F '\input{' main.tex`: confirms all audited files are active inputs
  (`main.tex:1813`, `1970`--`1972`, `1984`, `2077`--`2080`, `2088`).
- Metadata extraction from `metadata/claims.jsonl`: target files contain many
  `ProvedHere` claims, including the labels below.
- `python3 compute/scripts/audit_independent_verification.py --verbose --show-orphans | rg ...`:
  audit reports `1744` `ProvedHere` labels, `FAIL`, and flags several targets
  as uncovered by IV, including `thm:chiral-RH`,
  `thm:factorization-SC-koszul`, `thm:recognition-relative-ft`,
  `thm:three-routes-equivalence`, `thm:ds-hochschild-bridge`, and
  `prop:geometric-braces-well-defined-brace`.
- `pytest` targeted surfaces:
  `test_chiral_higher_deligne.py`, `test_part_vi_platonic_introduction.py`,
  `test_e3_topological_ds_general.py`, `test_e3_topological_free_pva.py`:
  `10 passed`.
  `test_e_infinity_topologization.py`, `test_w_infty_endpoint.py`,
  `test_climax_theorems_wave17_iv.py`, `test_climax_theorems_iv.py`:
  `47 passed`.
  Several passed tests are only structural/bibliographic scaffolds with
  `assert True` bodies; they do not close the proof gaps below.

## Cycle 1: Factorization Swiss-Cheese Koszul Duality

**ATTACK.** `thm:factorization-SC-koszul`
(`chapters/theory/factorization_swiss_cheese.tex:2066`--`2109`) is marked
`\ClaimStatusProvedHere` and claims all-genus Feynman-transform recovery of the
curved factorization algebra plus derived/coderived placement. The proof at
`:2111`ff. proves genus-0 recovery from local homotopy-Koszulity, then imports
closed-colour Getzler--Kapranov involutivity. That does not prove mixed
Swiss-cheese factorization duality on
`Ran(Sigma_g) x Ran(R)`, nor the curved coderived equivalence.

Cross-volume anchor: Vol I `higher_genus_modular_koszul.tex:382`--`399` states
genus-graded Koszul duality under explicit modular Koszulity and convergence
hypotheses; it does not supply the missing mixed all-genus theorem.

**HEAL.** Split the statement:

- bar construction as factorization coalgebra: `ProvedHere`;
- genus-0 local recovery via `SC^{ch,top}` homotopy-Koszulity: `ProvedHere`;
- closed-colour modular Feynman involutivity: `ProvedElsewhere`;
- mixed all-genus factorization recovery and curved derived/coderived
  equivalence: `Conditional` or `Conjectured`, pending a mixed factorization
  duality theorem.

Targeted grep/test: IV audit flags `thm:factorization-SC-koszul` uncovered; no
dedicated test decorates it.

## Cycle 2: Chiral Riemann-Hilbert / Curved Chain Map

**ATTACK.** `thm:chiral-RH`
(`factorization_swiss_cheese.tex:3510`--`3554`) is `ProvedHere` and asserts a
quasi-isomorphism
`(B_hol, Dg) -> (B_Ar, dfib)` satisfying
`Phi_g Dg = dfib Phi_g` while also asserting
`Dg^2 = 0` and `dfib^2 = kappa omega_g`. If `Phi_g` is an invertible coalgebra
chain map in the displayed sense, then `dfib^2 Phi_g = Phi_g Dg^2 = 0`; for
`kappa omega_g != 0` this contradicts the curved target. The later
`thm:three-models-gauge-orbit` (`relative_feynman_transform.tex:1778`--`1887`)
recognises a residual curvature term at `:1827`--`:1831`, but still concludes
same package by citing the derived-coderived comparison.

**HEAL.** Replace ordinary chain-map language by curved morphism/gauge-transport
language. Narrow true statement: the holomorphic and Arakelov representatives
are related by a gauge transformation in the curved coderivation/MC formalism;
strict intertwining is valid only when the curvature vanishes. The all-genus
comparison should be `Conditional`; the genus-1 Heisenberg computation can
remain `ProvedHere` where explicitly computed.

Targeted grep/test: IV audit flags `thm:chiral-RH` uncovered. No dedicated test
decorates it.

## Cycle 3: Modular Homotopy-Koszulity / Genus-g Formality

**ATTACK.** `thm:modular-hkoszul-SC`
(`modular_swiss_cheese_operad.tex:1478`--`1490`) is `ProvedHere` for full
all-genus modular homotopy-Koszulity of `SCmod`. Its proof depends on
`thm:genus-g-formality` (`:1907`--`1927`), which asserts formality of
`C_*(FM_k(Sigma_g))` for every smooth projective curve using prime-form
configuration integrals. The cited external checks in
`compute/tests/test_climax_theorems_wave17_iv.py:527`--`545` are explicitly
genus-0 sources; the test file itself says at `:23`--`:28` that bodies in that
module are `assert True` bibliographic scaffolding.

There is also a structural issue: `FM_k(Sigma_g)` at fixed positive genus is a
global configuration space, not by itself the formal-disc operad governing
local collision insertions unless a local-screen/framing extraction is stated.

**HEAL.** Keep `ProvedHere` for the genus-0/local-screen
`SC^{ch,top}` specialization and for formal collision-screen boundary
cancellations. Downgrade full `SCmod` modular homotopy-Koszulity and
all-genus formality to `Conditional` or `Conjectured` until the positive-genus
operadic composition, formality, and mixed compatibility are proved as
theorems.

Targeted grep/test: `pytest test_climax_theorems_wave17_iv.py` passed, but the
relevant IV body is scaffolding; `test_climax_theorems_wave16_iv.py:101`--`115`
decorates `thm:modular-hkoszul-SC` with `assert True`.

## Cycle 4: Relative Feynman Transform / Three-Route Equivalence

**ATTACK.** `thm:recognition-relative-ft`
(`relative_feynman_transform.tex:1208`--`1238`) is plausibly formal and even
says it does not recover monodromy or the curved Arakelov representative.
However, downstream `thm:three-routes-equivalence`
(`:2932`--`2953`) is `ProvedHere` and asserts that global factorization and
local operadic bar-complex models are connected at every genus by the relative
Feynman transform and the chiral exponential map. Its proof at
`:2955`--`2972` depends exactly on `thm:chiral-RH` and the Positselski
comparison, so Cycle 2 propagates here.

**HEAL.** Keep the recognition theorem `ProvedHere` only as a formal statement
for a chosen modular bar datum and stable-graph bicomplex. Downgrade
`thm:three-routes-equivalence` and `thm:derived-coderived-full` to
`Conditional` on: mixed factorization Koszul duality, a correct curved
Riemann-Hilbert morphism, and explicit Positselski hypotheses.

Targeted grep/test: IV audit flags `thm:recognition-relative-ft` and
`thm:three-routes-equivalence` uncovered. No dedicated pytest target covers
these labels.

## Cycle 5: Chiral Higher Deligne Mixed Status

**ATTACK.** `thm:chiral-higher-deligne`
(`chiral_higher_deligne.tex:464`--`494`) is honestly scoped in the source:
clause (1) is `ProvedHere`, clauses (2)--(3) are `Conditional`. But
`metadata/claims.jsonl` records the whole theorem as `ProvedHere`, and
`test_chiral_higher_deligne.py:127`--`150` decorates the whole label while
admitting the checks verify the underlying `E_2` content and that the `E_3`
upgrade is new. The text itself says the two-coloured
`(SC^{ch,top})^!` contracting homotopy is not established
(`chiral_higher_deligne.tex:496`--`518`).

**HEAL.** Split the theorem label or status accounting:

- `E_2` chiral brace action on `ChirHoch`: `ProvedHere`;
- two-coloured universal `SC^{ch,top}` bulk-boundary property:
  `Conditional`;
- strict `E_3` refinement: `Conditional` on named topologisation data.

Targeted grep/test: `pytest test_chiral_higher_deligne.py` passed, but the
test verifies the `E_2` cross-check, not the two-coloured contracting homotopy
or strict `E_3` lift.

## Cycle 6: Part VI All-N Ladder

**ATTACK.** `thm:part-vi-ladder-exists`
(`part_vi_platonic_introduction.tex:287`--`306`) is `ProvedHere` for every
`N`, including `N = infinity`. It depends on
`thm:e-infinity-specialisation-WN`
(`e_infinity_topologization.tex:732`--`786`), but that proof uses
`Axiom (T5)` at `:777`--`:782`. The same chapter explicitly says
antighost BRST-commutativity is postulated for `n,m >= 4` and not derived
(`e_infinity_topologization.tex:425`--`475`). The `W_infty` endpoint then
promotes the conditional clause away (`w_infty_e_infty_endpoint_platonic.tex:436`--`458`,
`:690`--`:706`).

**HEAL.** Status should be:

- `N=2` Virasoro and `N=3`/`W_3` low-spin cases: `ProvedHere`, if the finite
  OPE verification is present;
- `N >= 4`: `Conditional` on antighost BRST-commutativity through spin `N`;
- `W_infty -> E_infty`: `Conditional` or `Conjectured` until T5 is proved at
  all spins.

Targeted grep/test: `pytest test_e_infinity_topologization.py` and
`test_part_vi_platonic_introduction.py` passed, but
`test_e_infinity_topologization.py:262`--`272` is an `assert True` agreement
check for spin-tower existence, not a proof of antighost commutativity.

## Cycle 7: Hochschild Bulk and DS-Hochschild Bridge

**ATTACK.** `thm:bulk_hochschild`
(`hochschild.tex:392`--`410`) is `ProvedHere`, but has no local proof body; it
points forward to a prefactorization/factorization-homology model. The sharper
brace-file version is already downgraded:
`brace.tex:707`--`725` is `ClaimStatusConditional` and explicitly restricts to
product-formal HT shadows. The later `thm:bulk-CHC`
(`hochschild.tex:887`--`896`) has a proof, but it relies on the product-formal
recognition theorem and physics-bridge hypotheses.

`thm:ds-hochschild-bridge` (`hochschild.tex:3208`--`3252`) is more severe:
the preceding scope remark says the bounded-shift criterion is open for
`W_N`, `N >= 3`, and generic `W^k(g)` (`:3198`--`:3205`), while the theorem
claims unconditional chain-level class-M bulk/Hochschild for all of them
(`:3225`--`:3228`, `:3249`--`:3251`).

**HEAL.** Downgrade `thm:bulk_hochschild` to `Conditional` unless it is only a
roadmap/restatement of `thm:bulk-CHC` under a chosen HT prefactorization model.
For DS-Hochschild, keep a cohomological or explicitly verified
boundary-linear/generic-Virasoro statement; mark full chain-level class-M
coverage `Conditional` on the bounded-shift criterion and chiral HKR
smoothness hypotheses.

Targeted grep/test: `pytest test_climax_theorems_iv.py` passed, but
`test_climax_theorems_iv.py:456`--`457` is `assert True`, and IV audit flags
`thm:ds-hochschild-bridge` uncovered.

## Cycle 8: Strict Brace Identities

**ATTACK.** `prop:geometric-braces-well-defined-brace`
(`brace.tex:668`--`675`) is `ProvedHere` and says the geometric brace
operations strictly satisfy the brace identities. But
`chiral_higher_deligne.tex:367`--`380` says the identities hold up to explicit
chain homotopies, and strict braces require an associator-fixed
strictification. Thus the strict version is overmarked.

**HEAL.** Narrow the proposition to: geometric braces are well-defined
homotopy brace operations; Stokes gives explicit higher homotopies. A strict
brace dg algebra can be used only after choosing a Drinfeld associator/cofibrant
strictification. The deformation theorem should be phrased through the homotopy
convolution `L_infty` algebra unless the strictification data is fixed.

Targeted grep/test: IV audit flags `prop:geometric-braces-well-defined-brace`
uncovered. No dedicated pytest target decorates this label.

## Compact Status Table

| Label | Current active status | Recommended status |
|---|---:|---:|
| `thm:factorization-SC-koszul` | `ProvedHere` | split; all-genus mixed recovery `Conditional/Conjectured` |
| `thm:chiral-RH` | `ProvedHere` | `Conditional`; strict chain-map wording false when curvature nonzero |
| `thm:modular-hkoszul-SC` | `ProvedHere` | local/genus-0 `ProvedHere`; full `SCmod` `Conditional/Conjectured` |
| `thm:genus-g-formality` | `ProvedHere` | local-screen statement `ProvedHere`; global all-genus formality `Conditional` |
| `thm:three-routes-equivalence` | `ProvedHere` | `Conditional` on Cycles 1--2 |
| `thm:chiral-higher-deligne` | mixed in text, `ProvedHere` in registry | split clause labels/statuses |
| `thm:part-vi-ladder-exists` | `ProvedHere` | `N<=3 ProvedHere`; `N>=4` and `infinity` `Conditional` |
| `thm:bulk_hochschild` | `ProvedHere` | `Conditional` or restatement of scoped `thm:bulk-CHC` |
| `thm:ds-hochschild-bridge` | `ProvedHere` | cohomological/generic verified cases only; full class-M chain-level `Conditional` |
| `prop:geometric-braces-well-defined-brace` | `ProvedHere` | homotopy braces `ProvedHere`; strict braces after associator |

Residual open obligation: none of these should be repaired by metadata-only
status churn. The mathematically correct repair is to split statements at their
proved boundary, then prove the missing mixed/global/topologisation inputs or
downgrade them explicitly.
