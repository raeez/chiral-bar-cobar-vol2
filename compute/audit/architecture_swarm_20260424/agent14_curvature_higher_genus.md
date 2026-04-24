# Agent 14 - curvature / higher-genus local-global audit

Date: 2026-04-24.
Owned write scope: `compute/audit/architecture_swarm_20260424/agent14_curvature_higher_genus.md`.
Shared files changed: none.
Builds run: none.

## Verdict

The current curvature / higher-genus local-global story contains a true
core, but the live manuscript overstates its proof status. The safe core is:

1. The genus-0 formal-disc / local operadic model is flat.
2. The genus-1 elliptic/Arakelov model has an explicit monodromy and
   curvature lane, subject to a convention-locked normalization.
3. For `g >= 2`, the scalar statement
   `d_fib^2 = kappa(A) * omega_g` can be used only as the manuscript's
   scalar higher-genus lane, not as an all-purpose chain-level theorem.
4. The derived-vs-coderived comparison is conditional for `g > 1`,
   exactly as `relative_feynman_transform.tex` already says.

The unsafe extension is the claim that all-genus modular-bootstrap
`H^2`-vanishing, curved-Dunn `H^2`-vanishing, and chiral exponential
flat/curved equivalence are proved unconditionally. Those should be
downgraded to conditional unless a separate proof of the bridge
quasi-isomorphism, the bootstrap `H^2` computation, and the
bounded-filtered Positselski criterion is inserted.

## Read Surface

- Vol II doctrine: `CLAUDE.md`.
- Main Vol II files:
  - `chapters/theory/curved_dunn_higher_genus.tex`
  - `chapters/theory/factorization_swiss_cheese.tex`
  - `chapters/theory/modular_swiss_cheese_operad.tex`
  - `chapters/connections/relative_feynman_transform.tex`
  - `compute/tests/test_curved_dunn_higher_genus.py`
- Cross-volume consumers:
  - Vol I: `/Users/raeez/chiral-bar-cobar/notes/five_frontiers_synthesis.md`
  - Vol I: `/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex`
  - Vol III: `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_c_six_routes_convergence.tex`
- Local swarm context:
  - `compute/audit/architecture_swarm_20260424/agent01_factorization_primary.md`
  - `compute/audit/architecture_swarm_20260424/agent03_relative_feynman_transform.md`
  - `compute/audit/architecture_swarm_20260424/agent10_compute_architecture.md`
  - `compute/audit/architecture_swarm_20260424/agent11_kappa_stratification.md`

## Formula Status Ledger

Use exact formulas below only at the stated status.

| Formula / constant | Local anchors | Status |
|---|---:|---|
| `int_{\overline{M}_{1,1}} c_1(lambda_1) = 1/12`; convention `omega_1 := 12 c_1(lambda_1)` | `curved_dunn_higher_genus.tex:341-349` | Locally stated standard normalization; acceptable as a convention, but this audit did not independently rederive the stack normalization. |
| `d_fib^2 = kappa(A) * omega_g` | `factorization_swiss_cheese.tex:911-922`, `1014-1022`, `1046-1059`, `1451-1453` | Conditional scalar-lane statement. It is not ordinary D-module curvature and not a full multiweight all-genus theorem. |
| Holomorphic prime-form propagator `K^(g)(z,w)=partial_z log E(z,w) dz` | `factorization_swiss_cheese.tex:1340-1358` | Locally supported by Fay reference. Accept only as the holomorphic/multivalued model. |
| Arakelov propagator correction constants/signs | `factorization_swiss_cheese.tex:947-960`, `1367-1445`; `relative_feynman_transform.tex:1870-1876` | Not safe as exact formula. The manuscript contains sign/index inconsistencies; mark conditional until convention-locked against a primary source. |
| Genus-1 monodromy `Mon(R)=exp(int_A r(z) dz)` | `curved_dunn_higher_genus.tex:367-374` | Conditional. The period cycle, normalization, and identification with the program's `R`-matrix must be fixed before use beyond the elliptic example. |
| All-genus `H^2(TCo_g(A),d_0)=0` | `curved_dunn_higher_genus.tex:403-455` | Not proved by the current text. Conditional on the bridge `H^2`-isomorphism plus independent bootstrap `H^2`-vanishing. |

## Primary Verification Debt

These are the named primary sources the manuscript already invokes or
needs before any conditional claim above is upgraded.

- Fay, Chapter II: prime form and trisecant identities. Needed for the
  holomorphic propagator and any exact higher-genus Arnold identity.
- Arakelov/Faltings normalization of the Green kernel: needed for the
  signs and constants in `K_Ar` and `bar_partial K_Ar`.
- Beilinson--Drinfeld 2004, Section 3.4.11: factorization module
  structure for the mixed sector; locally cited at
  `factorization_swiss_cheese.tex:820-824`.
- Ayala--Francis recognition/factorization comparison: locally cited at
  `factorization_swiss_cheese.tex:765-768` and
  `modular_swiss_cheese_operad.tex:1316-1323`.
- Getzler--Kapranov modular operads/involutivity: needed for modular
  graph stratification and Feynman transform claims; not by itself a
  derived-coderived comparison.
- Positselski, comodule-contramodule correspondence: locally cited at
  `factorization_swiss_cheese.tex:3972-3988`; needed only after the
  curvature element, conilpotent completion, and finite-type hypotheses
  are fixed.

## ATTACK -> HEAL Cycles

### Cycle 1 - Literal `Ran(Sigma_g) x Ran(R)`

ATTACK.
`factorization_swiss_cheese.tex:750-862` defines the mixed sector by
closed `D`-modules on `Ran(Sigma_g)` and locally constant open
factorization on `Ran(R)`, which is the right direction. But later the
text promotes this to a bar coalgebra on the literal product
`Ran(Sigma_g) x Ran(R)` at `factorization_swiss_cheese.tex:2075-2079`,
and `modular_swiss_cheese_operad.tex:1267-1269`, `1354-1358` use the
same literal product in the extraction functor. `relative_feynman_transform.tex:1609-1618`
also repeats the product phrase.

The literal product forgets the open-closed incidence and directional
bulk-to-boundary restriction. It is safe as mnemonic notation only; it
is not the actual global HT configuration object.

HEAL.
Replace literal product statements by a colored open-closed HT Ran
geometry:

```
FactAlg_SC(Ran_HT^oc(Sigma_g,I))
```

or, more concretely, by strata

```
Conf_k(Sigma_g \ D_boundary) x Conf_m^ord(I)
```

with collision maps, boundary restriction, and the no open-to-closed
operation built into the colored structure. A product
`Ran(Sigma_g) x Ran(R)` may remain only as a notation for the associated
graded separate closed/open variables after the mixed incidence has
already been specified.

STATUS RECOMMENDATION.
`prop:extraction-functor` should be split: genus-0 formal completion is
proved/standard under the local comparison; higher-genus faithfulness
and non-fullness are conditional on the corrected open-closed Ran
geometry.

### Cycle 2 - Curvature Is Not D-Module Curvature

ATTACK.
`factorization_swiss_cheese.tex:864-881` says the Gauss-Manin connection
on the family induces a connection on the bar complex whose curvature is
`d_fib^2 = kappa(A) * omega_g`, "arising from the monodromy of the
D-module connection around B-cycles." `factorization_swiss_cheese.tex:1028-1031`
again calls this D-module monodromy.

This is too strong. A `D`-module connection is flat in the usual sense.
The curvature here belongs to the projective/family/bar-differential
or Arakelov representative lane. It measures the obstruction created by
choosing a single-valued non-holomorphic propagator and contracting its
defect with OPE data; it is not the curvature of an ordinary flat
`D`-module.

HEAL.
Use:

```
The underlying BD D-module is flat. The scalar curvature
d_fib^2 = kappa(A) * omega_g is the curvature of the chosen
single-valued Arakelov representative of the bar differential, or
equivalently the projective/anomaly class of the family. It is invisible
to formal-disc extraction but visible in the global factorization
package.
```

For moduli-space language, distinguish curve form and Hodge class:

```
fixed curve: omega_g in H^{1,1}(Sigma_g)
family/moduli: obstruction proportional to the relevant Hodge class
```

STATUS RECOMMENDATION.
Retain the scalar curvature statement only with this ambient
qualification. Do not state it as an ordinary `D`-module curvature
theorem.

### Cycle 3 - Arakelov Formula Constants and Signs

ATTACK.
The Arakelov propagator formulas conflict internally.

- `factorization_swiss_cheese.tex:947-960` uses a `-2 pi i` correction
  and gets `bar_partial_z K_Ar = -2 pi i omega_g`.
- `factorization_swiss_cheese.tex:1367-1377` uses a `+ pi` correction
  with holomorphic differential at `z`.
- `factorization_swiss_cheese.tex:1412-1445` derives
  `bar_partial_z K_Ar = -omega_Ar`, with
  `omega_Ar = -pi/(2i) sum (Im tau)^-1 omega_alpha wedge bar omega_beta`.
- `relative_feynman_transform.tex:1870-1876` cites the same correction
  as satisfying `bar_partial_z R^(g) = +omega_Ar`, opposite to
  `factorization_swiss_cheese.tex:3635-3639`.

The text also mixes `nu_j(w)` and `omega_alpha(z)` in the correction
term. Without a locked convention for which variable the one-form lives
in, the exact signs and constants are not reliable.

HEAL.
Insist on a separate convention lemma before using exact formulas:

```
Fix normalized differentials omega_i with int_{A_j} omega_i = delta_ij,
period matrix tau, prime form E(z,w), and an explicit choice of
one-form variable. Define K_Ar by the unique single-valued logarithmic
one-form with residue +1 along the diagonal and mean-zero Arakelov
normalization. Then record the resulting bar_partial identity with
that convention.
```

Until that lemma is proved from Fay/Arakelov primary formulas, use only:

```
K_Ar = K_hol + smooth non-holomorphic correction,
bar_partial K_Ar is proportional to the Arakelov (1,1)-form.
```

STATUS RECOMMENDATION.
`prop:propagator-explicit` should not remain `ProvedHere` for exact
constants/signs. Mark exact constants conditional on the convention
lemma; keep the qualitative three-propagator distinction.

### Cycle 4 - Fay/Arnold Flatness Does Not Prove the Arakelov Defect

ATTACK.
`modular_swiss_cheese_operad.tex:157-203` gives a reasonable genus-1
Fay/Weierstrass flatness check. `factorization_swiss_cheese.tex:965-992`
then asserts an all-genus defective Arnold relation for Arakelov-corrected
forms, and `factorization_swiss_cheese.tex:1046-1059` sketches
`d_fib^2 = kappa(A) * omega_g` by splitting `eta^(g)=h+R`.

The holomorphic Fay identity proves flatness for the prime-form model
on the universal cover. It does not automatically prove the exact
single-valued Arakelov defective Arnold formula at all genera. The
displayed defect

```
eta_12^g wedge eta_23^g + eta_23^g wedge eta_31^g
  + eta_31^g wedge eta_12^g
= omega_g(z_3) * (dz_1-dz_2) wedge (dz_2-dz_3) + cyclic
```

has not been locally or primarily verified in this audit, and its
type/variable bookkeeping is not obviously consistent.

HEAL.
Split the story:

1. Holomorphic prime-form model: Fay gives the local cancellation and
   `D_g^2=0` on the chosen multivalued/cover presentation.
2. Arakelov model: the smooth correction introduces a non-holomorphic
   `(1,1)` defect. Contracting that defect with scalar OPE data gives
   the scalar curvature lane, conditional on the convention lemma and
   residue computation.

Use this replacement statement:

```
The Fay identity kills the purely holomorphic double-residue term.
The Arakelov correction is smooth in the collision variable and changes
the representative by a non-holomorphic form whose bar_partial is
proportional to the Arakelov form. On the scalar OPE lane this produces
the curvature class kappa(A) * omega_g.
```

STATUS RECOMMENDATION.
The displayed all-genus defective Arnold formula should be marked
conditional/conjectural until checked from Fay plus an Arakelov
normalization lemma.

### Cycle 5 - Curved-Dunn Bridge and `H^2` Vanishing

ATTACK.
`curved_dunn_higher_genus.tex:140-166` states the bridge proposition
with `ClaimStatusProvedHere`, including `H^2(Phi)` an isomorphism.
The proof step at `curved_dunn_higher_genus.tex:244-259` says the
associated-graded map is a Kunneth decomposition iso on each stratum.
This is exactly the theorem that needs proof; it is not established by
the preceding construction.

The all-genus vanishing theorem at `curved_dunn_higher_genus.tex:403-455`
then uses:

```
bootstrap H^2 = 0
bridge H^2-isomorphism
therefore curved-Dunn H^2 = 0
```

But `curved_dunn_higher_genus.tex:429-441` treats MC solvability as
equivalent to `H^2=0`, which is circular unless the obstruction complex
and its homotopy contraction have already been computed.

The test file does not close the gap. `compute/tests/test_curved_dunn_higher_genus.py:35-75`
hardcodes the predicted zeros, and `compute/tests/test_curved_dunn_higher_genus.py:133-173`
checks agreement among those surrogates. That is smoke coverage, not
independent verification.

HEAL.
Use the conditional theorem:

```
Assume:
(i) the bridge Phi is a filtered quasi-isomorphism through degree 2,
or at least H^2(Phi) is an isomorphism;
(ii) the modular-bootstrap complex has H^2 = 0 at genus g;
(iii) the genus filtration spectral sequences converge strongly on the
finite-type/completed lane in use.
Then H^2(TCo_g(A),d_0)=0 and the curved-Dunn obstruction transports.
```

For the current manuscript, the genus-1 bridge may remain a separate
explicit calculation after fixing the Gauss-Manin/Arakelov normalization.
For `g >= 2`, the all-genus bridge is conditional.

STATUS RECOMMENDATION.
Downgrade:

- `prop:modular-bootstrap-to-curved-dunn-bridge`: `Conditional`
- `lem:modular-bootstrap-H2-vanishing`: `Conditional` or
  `Conjectured` for `g >= 2`
- `thm:curved-dunn-H2-vanishing-all-genera`: `Conditional`

### Cycle 6 - Genus 1 Does Not Automatically Globalize to All Genus

ATTACK.
The genus-1 proof in `curved_dunn_higher_genus.tex:318-384` uses a
Gauss-Manin uncurving, Arakelov pairing, and
`Mon(R)=exp(int_A r(z) dz)`. Even before the all-genus jump, the proof
contains a suspect assertion at `curved_dunn_higher_genus.tex:333-337`:
`c_1(lambda_2)` is said to be `nabla^GM`-exact on the moduli stack.
That is not a safe formulation of a Chern class of the Hodge/local
system package. It also fixes an A-cycle monodromy, while other local
curvature passages discuss B-cycle monodromy.

HEAL.
The true replacement is narrower:

```
At genus 1, after fixing the elliptic normalization of the Arakelov
form and the chosen period cycle, the elliptic propagator/Legendre
calculation gives an explicit twisting cochain tau_1. The resulting
twisted tensor product computes the genus-1 scalar lane. The proof does
not imply the genus-g bridge for g >= 2.
```

The Gauss-Manin step should be restated as a statement about the
projectively flat connection/anomaly class or about exactness after
passing to the chosen de Rham representative, not as literal exactness
of `c_1(lambda_2)` for a flat local system.

STATUS RECOMMENDATION.
`prop:genus1-twisted-tensor-product` should be `Conditional` until the
cycle convention and exactness wording are fixed. Once fixed, it can be
`ProvedHere` only for the genus-1 scalar/elliptic lane.

### Cycle 7 - Derived vs Coderived and the Chiral Exponential

ATTACK.
`factorization_swiss_cheese.tex:3561-3613` defines an all-genus chiral
exponential map by summing graph integrals over `FM_n(Sigma_g)`.
`factorization_swiss_cheese.tex:3620-3705` then proves it is a
quasi-isomorphism between the holomorphic and Arakelov models.

This is too strong for the curved target. The target has
`d_fib^2 = kappa * omega_g`, so ordinary chain homotopy language is not
available without the coderived/coacyclic ambient. The graph-integral
formula also needs convergence/renormalization and a proof that the cone
is coacyclic. By contrast, `relative_feynman_transform.tex:1549-1576`
already states the correct conditional comparison: filtered curved
factorization model, constructed `Phi_g`, and bounded-filtered
Positselski criterion.

HEAL.
Make `relative_feynman_transform.tex:1549-1576` the canonical status:

```
At genus 1, the comparison is explicit after the Arakelov/Legendre
calculation. For g > 1, Phi_g is conditional on construction of the
filtered morphism and on Positselski's bounded-filtered criterion for
its cone.
```

The formula at `factorization_swiss_cheese.tex:3567-3581` should be
presented as an ansatz/construction on the completed finite-type lane,
not as an unconditional formula for a quasi-isomorphism.

STATUS RECOMMENDATION.
Downgrade `thm:chiral-RH` and the all-genus `Phi_g` proof to
`Conditional` for `g > 1`. Keep `thm:derived-coderived-full` as
`Conditional`; it is already correctly scoped.

### Cycle 8 - Positselski Hypotheses and Curvature Element

ATTACK.
`factorization_swiss_cheese.tex:3889-3951` states curved co-contra
duality at genus `g` as `ProvedHere`. It is more careful than the
chiral-exponential section, but it still treats `kappa * omega_g` as a
"scalar curvature datum" at `factorization_swiss_cheese.tex:3901-3910`.
The construction of Positselski's framework at
`factorization_swiss_cheese.tex:3813-3818` allows a scalar curvature
or a curvature element in degree 2. The manuscript must choose the
ambient where `omega_g` is a central degree-2 curvature element, not a
literal scalar in the ground field.

HEAL.
Use:

```
On a fixed convention-locked Arakelov representative, kappa * omega_g
is a central degree-2 curvature element in the curved coalgebra over
the chosen de Rham/factorization base. If the genus-g bar coalgebra is
conilpotent with finite-dimensional graded pieces, and the completed
dual is taken in the corresponding completed topology, Positselski's
comodule-contramodule correspondence applies stagewise.
```

This theorem should not be used to identify the result with plain
`A^!` or with an ordinary derived category. The text already says this
at `factorization_swiss_cheese.tex:3928-3934`, `3945-3949`; preserve
that limitation.

STATUS RECOMMENDATION.
Either mark `thm:curved-koszul-genus-g` `Conditional`, or leave
`ProvedHere` only after explicitly adding the central curvature element,
finite-dimensional graded pieces, conilpotent completion, and completed
dual hypotheses to the statement.

## Cross-Volume Propagation

### Vol I

Vol I active synthesis records the scalar genus statement with the
needed lane distinction: `/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:579-585`
says the uniform-weight modular Koszul lane has
`obs_g(A)=kappa(A) lambda_g` at all genera, while genus 1 is
unconditional and `g >= 2` multiweight algebras acquire a cross-channel
term. This is compatible with the healed Vol II story.

Vol I frontier synthesis also uses the curved-Dunn bridge in the CY-C
summary: `/Users/raeez/chiral-bar-cobar/notes/five_frontiers_synthesis.md:56-60`
says higher-genus EOT reduces to genus one via modular-bootstrap
`H^2=0`. If Vol II downgrades the all-genus `H^2` theorem, this Vol I
sentence must inherit: "conditional on the Vol II bridge/vanishing
theorem" or "on the scalar cohomological lane."

### Vol II

The local/global split is already mostly present:
`factorization_swiss_cheese.tex:1062-1123` distinguishes flat
associated-graded, holomorphic prime-form, and Arakelov curved models,
and explicitly says the curved model is coderived. The inconsistent
parts are the later `ProvedHere` all-genus bridge and chiral-exponential
claims.

### Vol III

Vol III uses the Vol II theorem as a live premise:

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_c_six_routes_convergence.tex:370-373`
  reduces higher-genus Harvey-Moore compatibility using Vol II
  modular-bootstrap vanishing.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_c_six_routes_convergence.tex:391-418`
  states a `ProvedHereConditional` reduction of higher-genus EOT to
  genus 1 and treats Vol II `H^2_MB(g)=0` as unconditional input.

If the Vol II bridge remains conditional, Vol III must say:

```
Conditional on the Vol II modular-bootstrap bridge and H^2-vanishing
surface, the higher-genus EOT/Harvey-Moore discrepancy class vanishes.
Without that input, the reduction is not an unconditional theorem.
```

This does not affect Vol III's separate kappa stratification result
unless it imports the scalar `kappa * lambda_g` lane as a full
multiweight all-genus theorem. Keep the Vol III split between
`kappa_ch`, BKM lattice invariants, and fiber constants.

## Precise Replacement Statements

### Replacement A - Global HT Ran Geometry

```
Let Ran_HT^oc(Sigma_g,I) denote the colored open-closed configuration
geometry whose closed strata are finite subsets of Sigma_g, whose open
strata are ordered finite subsets of the interval I, and whose mixed
strata carry only bulk-to-boundary restriction maps. A BD factorization
Swiss-cheese algebra is a factorization object on this colored geometry.
The notation Ran(Sigma_g) x Ran(R) denotes only the separated associated
graded closed/open variables and is not the global mixed geometry.
```

### Replacement B - Curvature Lane

```
The underlying BD D-module data is flat. The curvature
d_fib^2 = kappa(A) * omega_g is the scalar curvature of the chosen
Arakelov representative of the genus-g bar differential. It is produced
by the non-holomorphic correction to the single-valued propagator and
is invisible to formal-disc extraction. For g >= 2 this statement is
proved only on the scalar/uniform-weight lane unless the multiweight
cross-channel terms have been separately controlled.
```

### Replacement C - Fay/Arnold

```
Fay's identity proves the vanishing of the purely holomorphic
three-point Arnold obstruction for the prime-form model. The Arakelov
single-valued model differs from it by a smooth non-holomorphic
correction whose bar_partial is proportional to the Arakelov form.
The exact all-genus defective Arnold formula is conditional on a
convention-locked Arakelov propagator lemma.
```

### Replacement D - Curved-Dunn Bridge

```
Assume Phi from the modular-bootstrap complex to the curved-Dunn
twisting-cochain complex is a filtered quasi-isomorphism through degree
2, and assume H^2 of the modular-bootstrap complex vanishes at genus g.
Then H^2(TCo_g(A),d_0)=0 and the genus-g curved-Dunn obstruction is
gauge-removable. Without these two inputs the all-genus vanishing is a
conditional theorem, not a proved theorem.
```

### Replacement E - Derived/Coderived Comparison

```
At genus 1 the flat-derived / curved-coderived comparison is the
explicit elliptic Arakelov/Legendre calculation, after fixing
normalization. For g > 1 the comparison is conditional on construction
of a filtered chiral exponential Phi_g and on the bounded-filtered
Positselski criterion proving its cone coacyclic.
```

## Status Recommendations

| Claim | Current local status | Recommended status |
|---|---|---|
| `prop:extraction-functor` | `ProvedHere` | Split: genus-0 local extraction proved; higher-genus faithfulness/non-fullness conditional on corrected open-closed Ran geometry. |
| `prop:propagator-explicit` | `ProvedHere` | Conditional for exact Arakelov constants/signs; qualitative prime-form/Arakelov distinction retained. |
| `prop:genus1-twisted-tensor-product` | effectively `ProvedHere` | Conditional until Gauss-Manin exactness wording, A/B cycle choice, and normalization are fixed; then proved only for genus-1 scalar lane. |
| `prop:modular-bootstrap-to-curved-dunn-bridge` | `ProvedHere` | Conditional. The `H^2(Phi)` isomorphism is not proved by the current spectral-sequence paragraph. |
| `lem:modular-bootstrap-H2-vanishing` | `ProvedHere` | Conditional or conjectural for `g >= 2`; needs an independent homotopy contraction/cohomology computation. |
| `thm:curved-dunn-H2-vanishing-all-genera` | `ProvedHere` | Conditional on bridge `H^2`-isomorphism plus bootstrap `H^2=0`. |
| `thm:factorization-SC-koszul` | `ProvedHere` | Split: genus-0/local part proved; all-genus recovery via Feynman transform conditional. |
| all-genus `Phi_g` / `thm:chiral-RH` | `ProvedHere` surface | Conditional for `g > 1`; genus 1 explicit after normalization. |
| `thm:derived-coderived-full` | `Conditional` | Keep as canonical status. |
| `thm:curved-koszul-genus-g` | `ProvedHere` | Conditional unless central curvature element/completion/finite-type hypotheses are made explicit. |

## Minimum Safe Patch Strategy

No shared files were edited by this agent. If the main thread patches
the manuscript, the smallest mathematically honest intervention is:

1. Replace literal `Ran(Sigma_g) x Ran(R)` global claims by colored
   open-closed HT Ran geometry.
2. Replace "D-module curvature" phrasing by "Arakelov representative /
   projective anomaly / curved bar differential" phrasing.
3. Insert one convention-locked Arakelov propagator lemma before any
   exact sign/constant formulas are used.
4. Downgrade the all-genus bridge, all-genus `H^2` vanishing, and
   all-genus chiral-exponential comparison to `Conditional`.
5. Propagate that conditional status to Vol I CY-C summaries and Vol III
   higher-genus EOT/Harvey-Moore reductions.
