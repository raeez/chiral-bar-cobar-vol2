# Agent 08 Report: HT Physics / BV-BRST Examiner

Scope: HT field-theory origins, BV-BRST construction, boundary conditions,
factorization algebra status, QME/anomaly claims, and physical-to-mathematical
status transitions.

Files read: `CLAUDE.md`, `AGENTS.md`,
`chapters/connections/ht_physical_origins.tex`,
`chapters/connections/holomorphic_topological.tex`,
`chapters/connections/bv_brst.tex`,
`chapters/connections/bv_ht_physics.tex`,
`chapters/connections/affine_half_space_bv.tex`,
`chapters/theory/bv-construction.tex`,
`chapters/theory/factorization_swiss_cheese.tex`,
`chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex`.
Additional bridge anchor read: `chapters/theory/raviolo.tex`.

Worktree discipline: no shared TeX was edited. This report is the only file
changed by this pass. No build was run.

## Executive Finding

The present HT/BV surface is viable only if the physical claims are separated
into three layers:

1. proved BV/factorization-algebra constructions in the Costello-Gwilliam
   sense;
2. conditional Vol II bridge statements requiring a chosen factorized
   product HT gauge/parametrix and one-loop finiteness;
3. heuristic or conjectural physics-to-chiral-avatar dictionaries.

Several chapters already contain this separation, especially
`bv_brst.tex`, `bv-construction.tex`, `factorization_swiss_cheese.tex`, and
`affine_half_space_bv.tex`. The remaining danger is that
`ht_physical_origins.tex`, `bv_ht_physics.tex`, `holomorphic_topological.tex`,
and `six_d_hcs_e3_chiral_avatar_platonic.tex` sometimes promote the same
transition to "theorem" or "proved here" without carrying the bridge
hypotheses.

## ATTACK -> HEAL Cycles

### Cycle 1: Product Parametrix and QME Bridge

ATTACK. The bridge theorem correctly states four hypotheses, but its proof
surface still contains a local inconsistency: `chapters/theory/raviolo.tex:563`
to `chapters/theory/raviolo.tex:614` refers to item (b) as one-loop
finiteness, while one-loop finiteness is item (c) in
`chapters/theory/raviolo.tex:446` to `chapters/theory/raviolo.tex:483`.
The same proof also first suggests the GRW power count gives strict
improvement for loops `L >= 2` in `d'=1`, then later says correctly that
`delta = (1-d')L = 0` for every loop at `d'=1`.

HEAL. The exact bridge statement should remain conditional:
there is no implication
`Q = dbar_C + d_t` => pure tensor propagator. The theorem requires a chosen
factorized parametrix
`G(z,t) = sum_alpha K_hol,alpha(z) box H_top,alpha(t)` with
`QG = delta_C box delta_R` modulo smooth Q-exact terms, plus one-loop
finiteness and product-polynomial interactions
(`chapters/theory/raviolo.tex:489` to `chapters/theory/raviolo.tex:536`).
The QME bridge in `chapters/theory/bv-construction.tex:5` to
`chapters/theory/bv-construction.tex:17` is correct only with those four
hypotheses, and the QME formula should be read as
`hbar Delta_BV S_eff + 1/2 {S_eff,S_eff} = 0`.

Status recommendation: keep `thm:physics-bridge` conditional; repair the item
reference and the `d'=1` power-count prose before using the theorem as an
input.

### Cycle 2: Affine Half-Space Boundary Condition

ATTACK. The affine half-space chapter has a strong BV boundary construction,
but the later logarithmic `SC^{ch,top}` identification would be false if read
as an automatic consequence of the Neumann boundary condition alone. The
half-space BV theorem supplies a renormalized quantization and level shift
(`chapters/connections/affine_half_space_bv.tex:204` to
`chapters/connections/affine_half_space_bv.tex:225`), while the bridge theorem
requires the separate factorized-parametrix and one-loop-finiteness inputs.

HEAL. The current downgrade is mathematically right:
`prop:affine-is-log-SC` should remain conditional
(`chapters/connections/affine_half_space_bv.tex:1541` to
`chapters/connections/affine_half_space_bv.tex:1621`). The exact statement is:
for the affine PVA model on `X = C_z x R_t`, after choosing the factorized
gauge parametrix whose singular part is
`G_sing = K_C box H_R`, `K_C(z)=1/(2 pi z)`, `H_R(t)=Theta(t)`, and after
using the affine one-loop exactness, the bulk observables satisfy the
logarithmic `SC^{ch,top}` bridge. The boundary condition is encoded by the
derived Lagrangian/fiber-product model at
`chapters/connections/affine_half_space_bv.tex:161` to
`chapters/connections/affine_half_space_bv.tex:193`, not by a bare informal
"Neumann implies chiral" slogan.

Status recommendation: keep the half-space quantization theorem as proved
there; keep the `SC^{ch,top}` consequence conditional.

### Cycle 3: Boundary hCS Surface Versus Surface Compactification

ATTACK. `chapters/connections/bv_ht_physics.tex:59` to
`chapters/connections/bv_ht_physics.tex:94` and the embedded copy at
`chapters/connections/ht_physical_origins.tex:1378` to
`chapters/connections/ht_physical_origins.tex:1413` state boundary chiral
algebra and HT boundary-condition claims too broadly. The text mixes
holomorphic Chern-Simons boundary language on a Calabi-Yau threefold with
surface compactification divisor language and a form
`Omega in K_{\bar Sigma}(kD)`. As written, the surface formula is not a
definition of an hCS boundary condition.

HEAL. Use the following separation. A boundary chiral algebra is obtained from
a compatible, anomaly-free BV boundary condition for the HT/hCS theory and the
Costello-Gwilliam factorization algebra of boundary observables. The
curve/divisor compactification data should be called a physical source or
heuristic geometric origin unless it is explicitly pushed through the BV
boundary-condition construction. The no-open-to-closed directionality of the
actual Swiss-cheese object is anchored at
`chapters/theory/factorization_swiss_cheese.tex:755` to
`chapters/theory/factorization_swiss_cheese.tex:862`, especially the empty
open-to-closed operation space.

Status recommendation: downgrade the surface compactification boundary
condition from theorem language to heuristic/conditional physical origin, or
replace it by the derived Lagrangian boundary condition of the affine chapter.

### Cycle 4: BRST Cohomology Versus Chiral Bar Identification

ATTACK. `chapters/connections/ht_physical_origins.tex:1585` to
`chapters/connections/ht_physical_origins.tex:1593` places the bar-cobar
identification inside a general "observables = cohomology" theorem. That is
too strong. Costello-Gwilliam style BV gives observables as BRST/BV
cohomology. It does not by itself identify those observables with the chiral
bar complex for every HT boundary algebra and every genus.

HEAL. The exact repaired statement is:
physical observables are BV/BRST cohomology; the identification with
`H^0(B^{ch}(A))` is a separate Vol II bridge. In the manuscript this bridge is
heuristic at the full BV-laplacian/QME level
(`chapters/connections/bv_brst.tex:75` to
`chapters/connections/bv_brst.tex:102` and
`chapters/connections/bv_brst.tex:381` to
`chapters/connections/bv_brst.tex:400`), conditional for the configuration
space BV functor (`chapters/connections/bv_brst.tex:1562` to
`chapters/connections/bv_brst.tex:1641`), and chain-level unconditional only
for the G/L lanes described in
`chapters/theory/bv-construction.tex:60` to
`chapters/theory/bv-construction.tex:86`.

Status recommendation: split the theorem into a proved BV/BRST cohomology
claim and a conditional bar-cobar bridge claim.

### Cycle 5: Global Ran Factorization Versus Local `SC^{ch,top}` Shadow

ATTACK. Several physical-origin passages use the local operadic
`SC^{ch,top}` language as if it were globally equivalent to the BD
Ran-space factorization datum. This is false at genus `g >= 1`: period data,
monodromy, and curvature are lost under local-shadow extraction.

HEAL. The exact global/local status is already correct in
`chapters/theory/factorization_swiss_cheese.tex:35` to
`chapters/theory/factorization_swiss_cheese.tex:50`,
`chapters/theory/factorization_swiss_cheese.tex:219` to
`chapters/theory/factorization_swiss_cheese.tex:248`, and
`chapters/theory/factorization_swiss_cheese.tex:1725` to
`chapters/theory/factorization_swiss_cheese.tex:1775`: the local-shadow
functor is an equivalence only in the genus-zero affine chart, and at
positive genus it loses the curvature/period term, schematically
`kappa(A) omega_g`. Physical-to-mathematical transition statements in
`chapters/connections/holomorphic_topological.tex:109` to
`chapters/connections/holomorphic_topological.tex:169` should be read as
algebraic consequences after a boundary chiral algebra `A_T` is already
given, not as a proof that every physical HT theory produces such an algebra.

Status recommendation: every all-genera or physical-origin use of
`SC^{ch,top}` should carry "local shadow" and "conditional on the boundary
chiral algebra/bridge data" unless it is explicitly genus zero.

### Cycle 6: Twistor Deligne Locus Versus 6d hCS BV Anomaly Locus

ATTACK. There is an apparent contradiction between the twistor anomaly
selection in `chapters/connections/holomorphic_topological.tex:626` to
`chapters/connections/holomorphic_topological.tex:672`, which lists the full
Deligne exceptional series including `E6` and unrefined `A2`, and the 6d hCS
one-loop cancellation locus in `chapters/connections/bv_brst.tex:4293` to
`chapters/connections/bv_brst.tex:4528`, which excludes strict `E6` and
requires an `A2` refinement. They cannot both be the same anomaly theorem.

HEAL. Treat them as different statements unless a primary-source
identification is supplied. The twistor result is a Costello-type
quartic-Casimir selection statement for a twistor hCS/axion setting. The
Vol II 6d hCS BV anomaly formula is a separate statement involving bubble,
box, and refinement/cubic terms. If the manuscript intends one theorem, then
the cancellation condition must be harmonized before publication. If it
intends two theorems, the exact transition sentence should say:
"The Deligne twistor locus supplies the quartic-Casimir input; the Vol II
6d hCS BV cancellation locus is a refinement after the bubble and cubic
descent terms are included."

Status recommendation: mark cross-reference as conditional/refined, not
identical.

### Cycle 7: `g_Delta5` Counterterms and QME Solvability

ATTACK. `chapters/connections/bv_brst.tex:3460` to
`chapters/connections/bv_brst.tex:3535` and
`chapters/connections/bv_brst.tex:3577` to
`chapters/connections/bv_brst.tex:3614` assert all-order counterterm
vanishing and QME solvability for the `Delta_5` trace model, with reasoning
that includes "quadratic Casimir of the hyperbolic root is zero" and a
vanishing `H^1` conclusion from null-root geometry. That is not a valid BV
argument as stated. A BV counterterm is controlled by a local cohomology or
Chevalley-Eilenberg obstruction class, not by the norm of a single root.

HEAL. The exact safe statement is:
QME solvability follows only after the relevant BV obstruction cocycles in
the local functional complex are shown to vanish or to be removable by
counterterms. A null-root or Borcherds denominator identity may motivate the
expected cancellation, but it does not by itself prove `H^1=0` for the
obstruction complex. The current "five verification paths" at
`chapters/connections/bv_brst.tex:3765` to
`chapters/connections/bv_brst.tex:3790` should include an explicit local
cohomology computation or be downgraded to conditional/computed evidence.

Status recommendation: downgrade `prop:counterterms-vanish` and
`thm:costello-trace-qme-solvable` to conditional until the obstruction complex
calculation is present in the tree.

### Cycle 8: 6d hCS Chiral Avatar Dictionary

ATTACK. `chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:115`
to `chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:117` says
the side-by-side dictionary is a theorem and that each row is an equivalence
in the appropriate infinity-category. This exceeds the evidence in the same
file. For example, `chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:272`
to `chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:285` uses
the bar/BV identification that `bv_brst.tex` itself marks heuristic or
conditional in the full BV-laplacian sense.

HEAL. The exact replacement is:
"The CFG-side entries are proved constructions in the cited references; the
chiral-avatar entries are Vol II identifications. The dictionary is proved in
the rows that reduce to the algebraic bar theorem or to local genus-zero
factorization, and is conditional in the rows involving BV Laplacian, full
QME, global genus, or K3 x E boundary integration."
This respects the explicit warning that the chiral avatar on a curve is not
itself `E_3` but `SC^{ch,top}`, becoming `E_3^{top}` only after the Sugawara
topologisation ladder at non-critical level
(`chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:481` to
`chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:495`).

Status recommendation: replace "the dictionary is a theorem" by a row-wise
status table.

### Cycle 9: K3 x E / 24 M5 / BKM Identification

ATTACK. The K3 x E theorem in
`chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:588` to
`chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:653` is marked
`ClaimStatusProvedHere`, but the proof combines several nontrivial physical
and mathematical transitions: integration over K3, reduction to
`Sigma_{0,24}`, Schur-sector identification with `H_{Delta5}`,
bar cohomology as `g_{Delta5}`, and passage to
`U(g_{Delta5})`. The displayed geometry also mixes
`R^3 x K3 x C^2`, which is not a complex threefold in the literal hCS sense
used at `chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:124`
to `chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex:147`.

HEAL. The safe exact statement is:
the K3 x E / `Delta_5` identification is a physical-origin conjecture or a
conditional theorem, depending on whether the missing pushforward and boundary
Schur-sector equivalences are supplied. The `24` M5-brane count can be used as
the geometric input, but the route
`int_K3 int_R3 A_hCS ~= U(g_Delta5)` requires an explicit factorization
homology pushforward, a boundary factorization algebra construction, and a
proved comparison with the Vol III `H_{Delta5}` chiral bialgebra. Without those
inputs, it should not be `ProvedHere`.

Status recommendation: downgrade to `ClaimStatusConditional` with the missing
inputs listed, or split into conjectural physical origin plus algebraic
identification of the already-constructed `H_{Delta5}`.

### Cycle 10: K3 Two-Loop Arithmetic

ATTACK. The two-loop origin paragraph
`chapters/connections/ht_physical_origins.tex:1860` to
`chapters/connections/ht_physical_origins.tex:1879` contains a numerical
inconsistency: it says the anomaly coefficient is
`24 * 2 * chi(O_K3) = 24`, while `chi(O_K3)=2`, so the displayed product is
`96`, not `24`. The surrounding sentence about "twice chi per node summed
over 12 nodes" gives another incompatible count unless an unmentioned
normalization by four is present.

HEAL. Do not use this paragraph as a numerical proof. The repaired statement
should cite the Vol I obstruction result directly and state the normalization
separately:
"The two-loop obstruction class is the Vol I class
`prop:bvbrst-2loop-obstruction`; its vanishing in the K3 model follows after
the stated K3 normalization is imposed." The actual coefficient must be
recomputed from the primary normalization before any displayed equality is
kept.

Status recommendation: mark the numerical derivation as computed only after a
source-tree computation or primary-literature normalization is attached.

## Consolidated Status Recommendations

- Keep `thm:physics-bridge` conditional and fix its proof-local item/power
  count wording.
- Keep affine BV quantization proved, but keep affine `SC^{ch,top}` bridge
  conditional.
- Split BRST cohomology from the chiral bar-cobar identification.
- Require "local shadow" language for all positive-genus `SC^{ch,top}` uses.
- Treat the Deligne twistor locus and the 6d hCS BV anomaly locus as distinct
  unless a source proves the refinement map.
- Downgrade `g_Delta5` all-order counterterm and QME-solvability claims until
  the obstruction complex calculation is present.
- Downgrade the 6d hCS chiral-avatar dictionary from global theorem to
  row-wise proved/conditional/conjectural status.
- Downgrade K3 x E BKM hCS origin to conditional or conjectural unless the
  pushforward and boundary comparison are supplied.
- Recompute the K3 two-loop coefficient before using it as evidence.

## Verification Surface

Commands run: targeted `rg`, `git status --short`, `nl -ba ... | sed -n ...`
line reads, and directory listing of
`compute/audit/architecture_swarm_20260424`.

No LaTeX build was run, in accordance with the session-end build rule. No
formula was inserted into shared TeX. No commit or push was made.

## Files Changed

- `compute/audit/architecture_swarm_20260424/agent08_ht_bv_physics.md`

## Open Obligations

1. Primary-source check for the full N=4/HT-to-hBF theorem in the exact form
   used by `bv_ht_physics.tex`.
2. Local BV obstruction-complex computation for the `Delta_5` trace QME.
3. Explicit factorization-homology pushforward and boundary Schur-sector
   comparison for the K3 x E / `g_Delta5` theorem.
4. Recalculation of the K3 two-loop coefficient and normalization.
5. Row-wise status repair for the 6d hCS chiral-avatar dictionary.
