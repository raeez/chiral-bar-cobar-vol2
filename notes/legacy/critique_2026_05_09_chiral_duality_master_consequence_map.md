# Critique of 2026-05-09 (Chiral Duality Master Critique) — Exhaustive Consequence Map for Reconstitution

> **STATUS: First-pass; superseded by `critique_2026_05_09_chiral_duality_master_consequence_map_v2.md`.**
> v2 promotes the architectural fact to a Master Architectural Theorem (universal stage chain
> $\mathsf{P} \to \mathsf{C} \to \mathsf{S} \to \mathsf{Z} \to \mathsf{A}$), unifies the two
> structural lanes of the critique via heptagon face (6), classifies the cuts as five *licensing-data
> types* (α/β/γ/δ/ε), introduces the bicoloured primitive package (closed-colour primitive added),
> articulates the cyclic-Hochschild four-object discipline at level $\mathsf{Z}$, names four open
> Construction Problems, scaffolds a `make verify-licensing` build-system gate, reorganises phasing
> honestly to 25-35 sessions, and runs a reflexive adversarial audit of itself. Read v2 for the
> strongest form. v1 below is preserved for diff history; §s 1-9 of v1 are subsumed by v2 §s 1-14.

**Source**: `~/Desktop/ChatGPT - Chiral Duality Master Critique.pdf`, ten pages.
**Subject**: Triage of false ideas across five active programmes — Vol I (chiral-bar-cobar),
Vol II (chiral-bar-cobar-vol2), Vol III (calabi-yau-quantum-groups), mixed-holomorphic-topological-strings, igusa-cusp-form.
**Result**: 17 named dismissals + one master pattern (`shadow = object`) + the Beilinson cut (`primitive objects first, shadows second, scalar modular forms last`).
**Status of Vol II as of 2026-05-09**: 9 of 17 already disciplined; 4 disciplined-with-qualification; 4 conditional with discipline gaps. The reconstitution work is unification + propagation, not first-time correction.

This note is the workshop-floor companion to the rectification campaign. It maps every consequence — large (architectural) and small (file-level, theorem-level, macro-level, AP-level, IV-level, voice-level) — and gives a phased execution order.

---

## 0. The architectural fact

The critique names the pattern explicitly: every false idea on the list is an instance of

> **shadow = object.**

A bar complex, a κ-scalar, a partition function, a positive Hall half, a finite-spin numerical agreement, a quadratic Maurer--Cartan datum, a formal-local Hamiltonian model — each is a *shadow* of something larger. The false move is to *promote* the shadow to the whole structure. Each of the 17 dismissals is one such promotion.

The corresponding licensing rule (the Beilinson cut):

> A statement is not allowed to be primitive if it is only true after choosing a boundary
> object, passing to a trace, averaging from ordered to symmetric, taking a protected index,
> completing a category, imposing endpoint hypotheses, or installing descent data.

Stated positively: **primitive objects first, shadows second, scalar modular forms last.**

This rule is *retroactive*: every existing claim in the manuscripts is to be checked against it. It is *forward-looking*: every new claim is to be written so the licensing chain is visible. It is *cross-volume*: the same shadow may appear as a primitive in one programme and as a shadow in another, and the discipline is volume-relative — Vol II's "primitive open object" is *not* the same as Vol III's "primitive CY datum," and conflating them is itself an instance of the shadow-equals-object pattern.

The critique's contribution is not new mathematics but a single architectural commitment that absorbs many local rectifications already made by Wave-13 (Vol III K3/BKM), Wave-14 (Vol II handoff queue), the 2026-04-22 cross-volume sharpenings, and the prior Beilinson-rectification swarms (`notes/beilinson_swarm_audit_vol2_2026_04_17.md`, `notes/deep_beilinson_rectification_maximal_attack.md`, etc.). Reconstitution = consolidate that commitment as the **architectural layer**, and propagate it to the chapters where prior rectification did not reach.

---

## 1. The five Beilinson cuts (architectural reconstitutions)

Each cut is a single structural commitment that absorbs several dismissals.

### Cut A — The seven-tuple primitive package

The primitive open object is not an algebra but a tangentially-decorated open factorization dg-category with a trace pair:

$$
\bigl(X,\, D,\, \tau;\; \cC^{\mathrm{op}},\; b,\; A_b,\; Z^{\mathrm{der}}_{\mathrm{ch}}(\cC),\; \Theta_C,\; \mathrm{Tr}_C\bigr).
$$

A boundary algebra $A_b = \mathrm{End}_\cC(b)$ is *only after* choosing a boundary vacuum $b$. That choice is a chart, not an invariant. Modularity is `trace + clutching` *on the open category*, with modular consequences for the closed shadow.

**Absorbs**: dismissals 1, 4, 5, partially 13.

**Vol II status**: foundations + sc_chtop_heptagon + foundations_recast_draft introduce the seven-tuple before any single-algebra claim. The primitive-package label `thm:gravity-mc-primitive-package` exists at `main.tex:762` and is used in `chapters/connections/3d_gravity.tex:4526` (subsec) and `:4814` (theorem). The discipline is *carried* but is *not articulated as the architectural layer*.

**Reconstitution work**: extract the seven-tuple into a single named *Architectural Definition* in `chapters/theory/foundations.tex` (or, better, a new `chapters/frame/primitive_package.tex`) and have every theorem in Vol II that begins "Let $A$ be..." cite it.

### Cut B — Bar / centre separation

The bar complex is *not* the bulk. It is a single-colour $E_1$-chiral dg coalgebra carrying twisting, coupling, and Koszul-comparison data. The bulk is the derived chiral centre:

$$
Z^{\mathrm{der}}_{\mathrm{ch}}(A) \;\simeq\; \mathrm{ChirHoch}^\bullet(A,A).
$$

The Vol I/II Theorem A bar--cobar adjunction is an *inversion in twisting data*, not a bulk--boundary identification. The 2d $\rightsquigarrow$ 3d HT passage is the chiral Deligne--Tamarkin / Swiss-cheese principle — boundary $A_\infty$-chiral object $\rightsquigarrow$ derived centre $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ — *not* an "extra interval direction." The bar direction is the computational model, not the explanatory mechanism.

**Absorbs**: dismissals 2, 3, partially 13, 17.

**Vol II status**: explicitly refuted at `hochschild.tex:547`, `foundations_recast_draft.tex:293`. Label `rem:bar-not-bulk` at `main.tex:729`. APs `AP-SC-BAR`, `AP-V2-101`, `AP25/34/50`, `AP163` enforce. Discipline is in place.

**Reconstitution work**: a *single canonical statement* of the cut, anchored in `chapters/frame/` or `chapters/connections/bar-cobar-review.tex`, that every "centre / bulk / Hochschild" passage cites. Currently the same content is restated locally in roughly a dozen places; consolidate to one authoritative passage with cross-references.

### Cut C — The κ-tuple (no scalar collapse)

For a CY-target chiral algebraic datum, the primitive *κ-content* is a five-row tuple, not a scalar:

$$
\bigl(\kappa_{\mathrm{cat}},\;\; \kappa_{\mathrm{ch}}^{\mathrm{Hodge}},\;\; \kappa_{\mathrm{ch}}^{\mathrm{Heis}},\;\; \kappa_{\mathrm{BKM}},\;\; \kappa_{\mathrm{fiber}}\bigr).
$$

The K3$\times E$ witness:

$$
\bigl(\kappa_{\mathrm{cat}},\; \kappa_{\mathrm{ch}}^{\mathrm{Hodge}},\; \kappa_{\mathrm{ch}}^{\mathrm{Heis}},\; \kappa_{\mathrm{BKM}}(\Delta_5),\; \kappa_{\mathrm{fiber}}\bigr) \;=\; (0,\; 0,\; 3,\; 5,\; 24).
$$

The additive identity $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\cO_{\mathrm{fiber}})$ **fails** at every $N \in \{1,2,3,4,6\}$ (Vol III `chapters/examples/k3e_cy3_programme.tex:4564`). The Vol II conductor face $K^{\kappa_{\mathrm{ch}}} = 8 = \mathrm{ord}(H_1)$ on the $\cB$-family is a *separate* invariant: the Mukai/Heegner conductor at the Humbert wall, satisfying $\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = -1$. It is **not** $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$ and not $\kappa_{\mathrm{BKM}}$. Five names, five invariants, one universal trace identity (Vol III $c_N(0)/2$) that ties them along the Pentagon-trace axis.

**Absorbs**: dismissal 6.

**Vol II status**: Vol III has the counterexample at `chapters/examples/k3e_cy3_programme.tex:4750–4762`. Vol II `chapters/theory/introduction.tex:1972` correctly names $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3$ as a separate post-reduction Cartan-rank invariant. The five-archetype ceiling table at `introduction.tex:1980` records sums $\kappa + \kappa^!$ only.

**Reconstitution work**:
1. Add a verbatim K3$\times E$ row to `chapters/connections/concordance.tex` and to `chapters/connections/programme_climax_platonic.tex` (climax chapter), so the counterexample is *inscribed* in Vol II, not only cross-referenced from Vol III.
2. Audit `chapters/theory/theorems_C_D_native_vol2_platonic.tex` — every $\rho_K$ statement must name *which* κ enters $\rho_K = \kappa(A) + \kappa(A^!)$ (it is $\kappa_{\mathrm{ch}}$ in the Hodge-supertrace sense, not $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$, not $\kappa_{\mathrm{BKM}}$).
3. Macro discipline: introduce `\kappaCat`, `\kappaChHodge`, `\kappaChHeis`, `\kappaBKM`, `\kappaFiber` so that no `\kappa` appears unscoped.

### Cut D — Two-stage CY $\rightsquigarrow$ chiral functor

The functor from CY-categorical data to chiral-algebraic data is *not* one-stage. It factorises:

$$
\Phi_d \;=\; \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},\, C} \;\circ\; \Phi^{\mathrm{FA}}_d
\quad:\quad
\mathrm{CY}_d\text{-Cat} \;\longrightarrow\; E_d\text{-HolFA}(X) \;\longrightarrow\; \mathrm{ChirAlg}(C).
$$

Stage 1 produces a canonical $E_d$-holomorphic factorisation algebra on the CY-$d$ target via Kontsevich--Tamarkin formality + Costello--Gwilliam--Li factorisation-homology BV. Stage 2 specialises along a $(d-1)$-cycle $\Sigma_{d-1}$ and a reference curve $C$ via factorisation-homology pushforward $\int_{\Sigma_{d-1}}$. The Swiss-cheese closed colour = stage 1; open colour = stage 2; the directional restriction encodes "stage 2 is specialisation of stage 1, never inversion."

The positive-half / Drinfeld-double distinction is the same architectural cut at the Hall side: $Y^+(X) = H^\bullet_{\mathrm{eq}}(\cM^+_{\mathrm{eff}}(X), \phi_W)$ is *only* the positive half. The full quantum group $G(X) = D(Y^+(X))$ requires Hall pairing + completion + integral form + stable-envelope transport + descent data. In particular $\mathrm{CoHA}(\C^3) = Y^+(\fgl_1)$, **not** $W_{1+\infty}$ — the latter appears only after Drinfeld double / Fock evaluation of the completed double.

**Absorbs**: dismissals 7, 8.

**Vol II status**: two-stage factorisation inscribed at Vol III `main.tex:1006` + Vol II `sc_chtop_heptagon.tex:136–206` (`rem:heptagon-two-stage-CY-to-chiral`) + `factorization_swiss_cheese.tex:2069–2115` (`rem:pentagon-two-stage`). APs V2-25/26/27/28/29 (and V2-AP128/129/130/131/132) protect. Vol II `log_ht_monodromy_frontier.tex:154–224` correctly stages SV positive-half + completed Yangian. Vol II `unified_chiral_quantum_group.tex:675–677, 1594–1619` correctly names positive-half + Drinfeld-double-or-vertex-completion.

**Reconstitution work**:
1. *Promote* `rem:heptagon-two-stage-CY-to-chiral` from a remark to a named architectural lemma whose statement is referenced by every chapter using $\Phi_d$, $\Phi^{\mathrm{FA}}_d$, $\mathrm{Sp}^{\mathrm{ch}}$. Currently it lives only as a remark.
2. Vol III: elevate `Y^+(X) = H^\bullet_{\mathrm{eq}}(\dots)$ and $G(X) = D(Y^+(X))$` from main-text prose at lines 550–564 to a load-bearing theorem statement in a Vol III chapter. Cross-reference into Vol II at `unified_chiral_quantum_group.tex` and `log_ht_monodromy_frontier.tex`.
3. Macro discipline: ensure `\PhiFA`, `\SpCh`, `\HolFA`, `\EdHolFA`, `\intSigma` appear consistently; audit Vol II for stale single-stage `\Phi_d` invocations that escaped the 2026-04-22 sweep (the cluster-2 survey found none, but a final mechanical grep of theory + connections is owed).

### Cut E — Operator vs shadow stratification (with conditional-locus discipline)

A scalar — automorphic form, partition function, Borcherds denominator, finite-spin numerical agreement, MC injection, formal-local Hamiltonian, even an entire positive Hall half — is a *protected trace* of an operator-level object. The operator-level object is the primitive; the scalar is the shadow. A statement of the form "scalar X is the operator algebra Y" requires the comparison map, not just numerical agreement. Symmetrically, an *endpoint claim* (e.g. "$W_\infty[\lambda] \Rightarrow E_\infty$") requires the endpoint hypotheses (Prochazka triangular truncation, Creutzig--Kanade--Linshaw parafermion compatibility, Pope--Romans--Shen / Bakas, Yamada weight-window) named *at every invocation*.

Sub-instances:

- **Igusa $\Delta_5$**: virtual $K_0$-determinant package + Borcherds denominator algebra. The missing primitive is the operator-level $\mathfrak D_X$ whose protected Pfaffian is $\Delta_5$. Inscribed in `~/igusa-cusp-form/main.tex:94–98, 110–118`.
- **Scalar BPS partition function** $Z_{\mathrm{BPS}}^{K3 \times E} = \Delta_5^{-2}$: shadow. The promotion to a gravity-line partition function is the Hall--Borcherds comparison residual, recorded as `conj:gravity-line-hall-borcherds-comparison` (Vol II `3d_gravity.tex:8429`).
- **6d hCS one-loop obstruction**: quartic $\int_X \mathrm{Tr}_{\mathrm{ad}} A(F_A)^3$, *not* a cubic Casimir. Inscribed in Vol III `chapters/theory/quantum_chiral_algebras.tex:402–403, 465–469`. 6d hCS supplies the $\Phi^{\mathrm{FA}}_3$ realisation only on verified formal / object-level loci; 3d-CS knot intuition is an *analogy*, not an identification.
- **Formal local HT model** $\R^2_{\mathrm{top}} \times \C^2_{\mathrm{hol}}$ + Hamiltonian BF: local. Global completion requires sheaf of local Hamiltonians + vanishing of holomorphic de Rham obstruction (period class in $H^1(X, \C_X)$). Inscribed in `~/mixed-holomorphic-topological-strings/main.tex:3200–3210, 3232–3233`.
- **PVA λ-Jacobi**: classical gauge invariance only. All-loop boundary VA + $E_3$-lift + analytic renormalised closed-open package = extra data (KZ analytic SDR, Stokes choices, reflected weights, lift of $T = [Q_{\mathrm{tot}}, G]$).
- **Quadratic chiral duality**: Gui--Li--Zeng injection $\mathrm{Hom}(A, B) \hookrightarrow \mathrm{MC}(A^! \otimes B)$. Bijectivity is *special* (Koszul effectiveness). Theorem A is bar--cobar, not Koszul duality per se; Koszulness is a separate theorem.
- **Class M chain-level**: false in ordinary $\mathrm{Ch}(\mathrm{Vect})$; true in weight-completed / pro / $J$-adic ambient. Stated correctly in Vol I `mc5_class_m_chain_level_platonic.tex:10–42` and Vol II `weight_completed_topologization_class_m_platonic.tex:1–80`; the discipline is to *name the ambient at every claim*.
- **Universal Holography functor** (the climax theorem): boundary = $A$, bulk = $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$, interaction = $\SCchtop$-brace. For $A = \mathrm{Vir}_c$, this is the holographic boundary-CFT reading of pure 3d gravity, *not* a dynamical-metric path integral. Scope qualifier carried at `programme_climax_platonic.tex:56–76`.

**Absorbs**: dismissals 9, 10, 11, 12, 13, 14, 15, 16, 17.

**Vol II status**: most sub-instances disciplined locally; the unifying architectural commitment is not articulated as a single layer.

**Reconstitution work**:
1. Add a single "shadow-vs-operator manifest" in `chapters/frame/` or top of `chapters/connections/bar-cobar-review.tex` that lists the eight shadows (`\Bar(A), B_{\mathrm{ord}}(A), \Theta_A, \kappa, \Delta_5, \Phi_{10}^{-1}, Y^+(X), \mathrm{CoHA}(\C^3)$, finite-spin checks, MC injections) and the operator-level primitive each one traces.
2. Per-shadow audit (see §3 below) of every chapter where the shadow appears.
3. "Endpoint hypotheses must be named" sub-discipline for $W_\infty / E_\infty$ — see Cut E section in §3.

---

## 2. The 17-dismissal cascade table

| #  | False slogan                                                                        | True statement                                                                                                                                | Vol II status                                                            | Cross-volume status                                                       | Action                                                                                                |
| -- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 1  | Boundary algebra = primitive open object                                             | Primitive = open factorisation dg-category seven-tuple; $A_b = \mathrm{End}_\cC(b)$ after choosing $b$                                        | Disciplined throughout; no naked claim                                   | Vol I, Vol III parallel                                                   | Cut A — articulate as architectural Definition; cross-volume macro `\primPkg`                          |
| 2  | $\mathrm{Bar}(A)$ = bulk                                                            | $\mathrm{Bar}(A)$ = twisting/coupling coalgebra; $Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq \mathrm{ChirHoch}^\bullet(A,A)$ = bulk            | Explicitly refuted; `rem:bar-not-bulk` at main.tex:729                  | Vol I `chapters/theory/...` parallel                                      | Cut B — consolidate canonical statement                                                                |
| 3  | $2d \rightsquigarrow 3d$ HT via $E_1$-bar direction                                 | Chiral Deligne--Tamarkin / Swiss-cheese: boundary $A_\infty$-chiral $\rightsquigarrow Z^{\mathrm{der}}_{\mathrm{ch}}(A)$; bar = computational | `chiral_higher_deligne.tex:256` + `foundations_recast_draft.tex:302`     | Vol I parallel                                                            | Cut B — anchor at Deligne--Tamarkin theorem statement                                                  |
| 4  | Global open sector on plain curve $X$                                                 | Tangential log curve $(X, D, \tau)$; open sector on real-oriented blowup / log boundary                                                       | Disciplined; no dedicated AP                                             | Vol III log discipline parallel                                           | New AP V2-AP-OPEN-LOG; macro `\logCurve`; audit `factorization_swiss_cheese.tex`, `sc_chtop_heptagon.tex`, `log_ht_monodromy*.tex`, `raviolo*.tex` |
| 5  | Modularity = property of closed algebra                                             | Modularity = trace + clutching on open category; closed shadow has modular consequences                                                       | Stated with qualification; `modular_swiss_cheese_operad.tex:998, 1233` could be sharpened | Vol III modular-PVA parallel                                | New AP V2-AP-MOD-CLOSED; `modular_pva_quantization*.tex`, `modular_swiss_cheese_operad.tex` voice sweep |
| 6  | Five $\kappa$-numbers = one invariant                                               | Tuple $(\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}^{\mathrm{Hodge}}, \kappa_{\mathrm{ch}}^{\mathrm{Heis}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}})$; K3$\times E = (0,0,3,5,24)$; additive collapse fails at $N=1$ | Distinguished in `introduction.tex:1972, 1980`; counterexample not yet inscribed in climax / concordance | Vol III `k3e_cy3_programme.tex:4564, 4750–4762` has counterexample | Cut C — inscribe K3×E row into Vol II climax + concordance; macros `\kappaCat` etc.; new AP V2-AP-KAPPA-TUPLE |
| 7  | $\mathrm{CY}_d$-cat $\to \mathrm{ChirAlg}$ direct                                   | Two-stage $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$                                                  | Inscribed at `sc_chtop_heptagon.tex:136–206` + `factorization_swiss_cheese.tex:2069–2115`; APs V2-25 to V2-29 | Vol III `main.tex:1006` Theorem; APs V2-AP128–132 mirror | Cut D — promote remark to architectural Lemma; final mechanical grep for stale one-stage $\Phi_d$ |
| 8  | Quantum group already present at positive half; $\mathrm{CoHA}(\C^3) = W_{1+\infty}$ | $Y^+(X) \neq G(X) = D(Y^+(X))$; $\mathrm{CoHA}(\C^3) = Y^+(\fgl_1)$, $W_{1+\infty}$ via Drinfeld double / Fock evaluation | `log_ht_monodromy_frontier.tex:154–224, 187–198, 227–249` + `unified_chiral_quantum_group.tex:675–677, 1594–1619` correct | Vol III `main.tex:550–564` content present, theorem-grade presentation owed | Cut D — Vol III: elevate to theorem; Vol II: cross-reference; new AP V2-AP-Y-PLUS-NOT-G |
| 9  | 6d hCS = 3d Chern--Simons in disguise                                                | 6d hCS realises $\Phi^{\mathrm{FA}}_3$ on verified loci; one-loop obstruction quartic $\int_X \mathrm{Tr}_{\mathrm{ad}} A(F_A)^3$; 3d CS = analogy, not identification | `six_d_hcs_e3_chiral_avatar_platonic.tex:150–161` labelled as analogy; FRONTIER.md identifies 6d hCS Level-3 = $E_3$ | Vol III `quantum_chiral_algebras.tex:402–403, 465–469` quartic explicit | Cut E — discipline carried; consolidate as remark cross-referencing both volumes |
| 10 | Formal local HT $\Rightarrow$ compact global theory                                  | Local model $\R^2_{\mathrm{top}} \times \C^2_{\mathrm{hol}}$ + formal Hamiltonian BF; global = sheaf of local Hamiltonians + vanishing $H^1(X, \C_X)$ obstruction | **GAP**: `bv_ht_physics.tex`, `holomorphic_topological.tex` import local model without re-stating obstruction | Mixed-HT-strings `main.tex:3200–3210, 3232–3233` explicit | Cut E — re-inscribe global obstruction at every Vol II HT-import site; new AP V2-AP-HT-GLOBAL |
| 11 | Igusa $\Delta_5$ = compact BPS Hilbert space                                         | $\Delta_5$ = virtual $K_0$-determinant + Borcherds denominator; missing primitive is $\mathfrak D_X$ with protected Pfaffian = $\Delta_5$    | `3d_gravity.tex:4466–4499` correct disclaimer; `conj:gravity-line-hall-borcherds-comparison` records gap | Igusa `main.tex:94–98, 110–118` explicit                         | Cut E — discipline carried; lift conjecture into a named "operator-level construction problem"        |
| 12 | Scalar partition function = operator algebra                                         | $Z_{\mathrm{BPS}} = \Delta_5^{-2}$ is shadow; promotion to gravity-line partition function = Hall--Borcherds residual                         | `3d_gravity.tex:4495–4499, 12748–12751` carries disclaimer at every locus | N/A (Vol II is source)                                                    | Cut E — discipline carried; consolidate as a single subsection in `3d_gravity.tex` |
| 13 | Universal Holography = dynamical metric path integral                                | Boundary = $A$, bulk = $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$, interaction = $\SCchtop$-brace; for $A = \mathrm{Vir}_c$, holographic boundary-CFT, NOT path integral | `programme_climax_platonic.tex:56–76` explicit qualifier; "literal QG" $\ClaimStatusConjectured$ | N/A                                                                       | Cut E — discipline carried; tighten by adding sentence to `rem:climax-qg-scope` listing the four required hypotheses (modular invariance + vacuum dominance + saddle + Brown--Henneaux dictionary) |
| 14 | $W_\infty[\lambda] \Rightarrow E_\infty$ proved by finite-spin checks               | Conditional on Prochazka triangular truncation + Creutzig--Kanade--Linshaw parafermion compatibility + Pope--Romans--Shen / Bakas + Yamada weight-window | **GAP**: `e_infinity_topologization.tex:1163–1241` names four hypotheses but in different language (Gaberdiel--Gopakumar / Linshaw / generic-c); spin-≤8 checks evidence not theorem | N/A                                                                       | Cut E — rewrite the four hypotheses to match the published source attribution; new AP V2-AP-W-INF-ENDPOINT; cross-reference `wn_tempered_closure_platonic.tex`, `tempered_stratum_characterization_platonic.tex`, `irrational_cosets_tempered_platonic.tex`, `logarithmic_wp_tempered_analysis_platonic.tex` |
| 15 | Class M works chain-level in ordinary complexes                                     | False in $\mathrm{Ch}(\mathrm{Vect})$; true in weight-completed / pro / $J$-adic                                                              | Disciplined; ambient named at every claim in `weight_completed_topologization_class_m_platonic.tex:1–80`, `equivalence.tex:145` | Vol I `chapters/theory/mc5_class_m_chain_level_platonic.tex:10–42` source | Cut E — discipline carried; consolidate as a "class M ambient discipline" remark referenced by all class-M chapters |
| 16 | PVA $\lambda$-Jacobi = whole quantum theory                                          | Classical gauge invariance only; quantum requires KZ analytic SDR + Stokes choices + reflected weights + lift of $T = [Q_{\mathrm{tot}}, G]$ | **GAP**: `pva-descent.tex:25–43` names H1–H4 but not tied to the four critique conditions; `modular_pva_quantization_core.tex:40–60` lists external inputs but not at theorem statements | N/A                                                                       | Cut E — re-state H1–H4 with explicit critique conditions at theorem statement, not only in introduction; new AP V2-AP-PVA-CLASSICAL-VS-QUANTUM |
| 17 | Quadratic chiral duality = full chiral Koszul duality                                | Gui--Li--Zeng: $\mathrm{Hom}(A,B) \hookrightarrow \mathrm{MC}(A^! \otimes B)$ injective; bijectivity Koszul-effectiveness-special; Theorem A = bar--cobar, Koszulness separate | **GAP**: `bar-cobar-review.tex:174–181` cites 4.5 as bijection without "injection in general" caveat at theorem locus; caveat lives at `modular_pva_quantization_core.tex:40–51` | Vol I Theorem B (Positselski) parallel                                    | Cut B + Cut E — add caveat at theorem statement; audit Vol II `theorems_C_D_native_vol2_platonic.tex` for Koszul-vs-quadratic separation; cross-reference `feedback_koszul_formality_distinction.md` (Koszul ≠ SC-formal) memory |

---

## 3. Cross-volume propagation matrix

| Dismissal      | Vol I (`~/chiral-bar-cobar`) | Vol II (`~/chiral-bar-cobar-vol2`) | Vol III (`~/calabi-yau-quantum-groups`) | mixed-HT-strings (`~/mixed-...`) | Igusa (`~/igusa-cusp-form`) |
| -------------- | :--------------------------: | :--------------------------------: | :-------------------------------------: | :------------------------------: | :-------------------------: |
| 1 (primitive)  | parallel: `chapters/theory/` | disciplined; articulate as Defn    | parallel: CY datum primitive            | parallel                          | parallel                    |
| 2 (Bar ≠ bulk) | parallel                     | refuted; consolidate canonical     | parallel                                | --                                | --                          |
| 3 (2d→3d)      | parallel                     | disciplined                        | --                                      | local-model context only          | --                          |
| 4 (log curve)  | parallel: log Beilinson      | discipline; new AP                 | parallel: stratified period domains     | parallel: brane completion        | --                          |
| 5 (modularity) | parallel                     | sharpen; new AP                    | parallel: PVA quantisation              | --                                | parallel: Borcherds modular |
| 6 (κ-tuple)    | parallel: 5-archetype ceiling | inscribe K3×E row in climax + concordance | source of counterexample        | --                                | parallel: $\Delta_5$ weight |
| 7 (two-stage)  | --                           | discipline carried                 | source                                  | --                                | --                          |
| 8 (Y⁺ ≠ G)     | --                           | discipline carried                 | elevate to theorem                      | --                                | parallel: $\mathfrak D_X$   |
| 9 (6d hCS)     | --                           | discipline carried                 | source of quartic obstruction           | --                                | --                          |
| 10 (HT global) | --                           | **GAP**: re-inscribe at each import site | --                              | source                            | --                          |
| 11 (Δ₅ Hilbert)| --                           | discipline carried                 | --                                      | --                                | source                      |
| 12 (Z = ops)   | --                           | source; consolidate disclaimer     | --                                      | --                                | parallel                    |
| 13 (Univ Hol)  | --                           | discipline carried; tighten        | --                                      | --                                | --                          |
| 14 (W∞ → E∞)   | --                           | **GAP**: rename hypotheses to published attribution | --                  | --                                | --                          |
| 15 (class M)   | source                       | discipline carried                 | --                                      | --                                | --                          |
| 16 (PVA classical)| --                        | **GAP**: tie hypotheses at theorem statement | parallel: PVA quantisation     | --                                | --                          |
| 17 (Koszul)    | parallel: Theorem B Positselski | **GAP**: caveat at theorem statement | --                                  | --                                | --                          |

**Reading**: 4 GAPs (#10, 14, 16, 17) require Vol II prose work. 3 promotions (#6 inscription, #7 remark→lemma, #8 prose→theorem) require Vol II + Vol III work. The remaining 10 dismissals are disciplined; their reconstitution work is consolidation, not correction.

---

## 4. Macro layer — preamble additions

These are *new* macros, all to be added to Vol II `main.tex` preamble + every Vol I and Vol III preamble that references the same objects, with `\providecommand` stubs in the chapters that reference them.

### 4.1 Primitive package (Cut A)

```latex
% Primitive open package (seven-tuple)
\providecommand{\primPkg}[3]{(#1, D, \tau;\, \cC^{\mathrm{op}},\, b,\, A_{b},\, \Zderch{\cC},\, \Theta_{C},\, \mathrm{Tr}_{C})}
\providecommand{\primPkgX}{\primPkg{X}{}{}}
\providecommand{\openFactCat}{\cC^{\mathrm{op}}}
\providecommand{\bdyVac}{b}
\providecommand{\bdyAlg}{A_{b}}
\providecommand{\Zderch}[1]{Z^{\mathrm{der}}_{\mathrm{ch}}(#1)}
\providecommand{\TraceC}{\mathrm{Tr}_{C}}
\providecommand{\HalfBraid}{\Theta_{C}}
\providecommand{\logCurve}{(X, D, \tau)}
```

### 4.2 Bar / centre (Cut B)

The existing `\Bbar`, `\Barch`, `\Barchord`, `\ChirHoch`, `\bulk`, `\Abulk` are sufficient. Add a *named* identification macro:

```latex
\providecommand{\BarTwc}[1]{\overline{B}^{\mathrm{ch}}(#1)}  % twisting/coupling coalgebra
\providecommand{\bulkOf}[1]{\Zderch{#1}}
\providecommand{\bulkChirHoch}[1]{\mathrm{ChirHoch}^{\bullet}(#1, #1)}
```

The discipline at the prose level: every appearance of "bulk" in displayed math must be `\bulkOf{A}` or `\Zderch{A}` (or `\Abulk` where `A` is implicit), never `\Bbar A` or `\Barch A`.

### 4.3 κ-tuple (Cut C)

```latex
% Five-row kappa tuple
\providecommand{\kappaCat}{\kappa_{\mathrm{cat}}}
\providecommand{\kappaChHodge}{\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}}
\providecommand{\kappaChHeis}{\kappa_{\mathrm{ch}}^{\mathrm{Heis}}}
\providecommand{\kappaBKM}{\kappa_{\mathrm{BKM}}}
\providecommand{\kappaFiber}{\kappa_{\mathrm{fiber}}}
\providecommand{\kappaTuple}[1]{(\kappaCat, \kappaChHodge, \kappaChHeis, \kappaBKM, \kappaFiber)(#1)}
% Mukai/Heegner conductor face (separate from kappaCh)
\providecommand{\Kkappa}{K^{\kappa_{\mathrm{ch}}}}
```

The discipline: a bare `\kappa` is forbidden; every invocation must specify which row.

### 4.4 Two-stage CY-chiral (Cut D)

The existing `\PhiFA`, `\SpCh`, `\HolFA`, `\EdHolFA`, `\EnHolFA`, `\intSigma`, `\hCS` are sufficient. Add Hall side:

```latex
\providecommand{\Yplus}[1]{Y^{+}(#1)}
\providecommand{\Gquant}[1]{G(#1)}
\providecommand{\Drinfdouble}[1]{D(#1)}
\providecommand{\CoHA}[1]{\mathrm{CoHA}(#1)}
\providecommand{\Wonepinf}{W_{1+\infty}}
```

### 4.5 Shadow vs operator (Cut E)

```latex
% Shadow vs operator: every shadow names its operator-level primitive
\providecommand{\protectedShadow}[1]{\overline{#1}^{\mathrm{shadow}}}
\providecommand{\operatorPrim}[1]{\mathfrak{D}_{#1}}  % e.g. \operatorPrim{X} for the operator-level object on X
\providecommand{\protectedPfaff}[1]{\mathrm{Pf}_{\mathrm{prot}}(#1)}
\providecommand{\Deltafive}{\Delta_{5}}
\providecommand{\Phiten}{\Phi_{10}}
\providecommand{\Phitenun}{\Phi_{10}^{\mathrm{un}}}
\providecommand{\ZBPS}{Z_{\mathrm{BPS}}}
```

The discipline: `\Deltafive`, `\Phitenun`, `\ZBPS`, `\Yplus`, `\CoHA{\C^3}` appearing without a same-paragraph reference to `\operatorPrim{\cdot}` (or a Hall--Borcherds / Drinfeld-double construction) is a Cut-E violation.

### 4.6 Conditional-locus (Cut E sub)

```latex
% Conditional-locus discipline: name the hypotheses at every endpoint
\providecommand{\hypProchazka}{(\mathrm{HP1}_{\text{Prochazka triangular truncation}})}
\providecommand{\hypCKL}{(\mathrm{HP2}_{\text{Creutzig--Kanade--Linshaw parafermion compatibility}})}
\providecommand{\hypPRSh}{(\mathrm{HP3}_{\text{Pope--Romans--Shen / Bakas}})}
\providecommand{\hypYamada}{(\mathrm{HP4}_{\text{Yamada weight-window}})}
\providecommand{\hypAmbientWtCpl}{(\mathrm{HM1}_{\text{weight-completed ambient}})}
\providecommand{\hypHTGlobalDR}{(\mathrm{HG1}_{\text{vanishing }H^{1}(X, \C_X)\text{ de Rham obstruction}})}
\providecommand{\hypKZSDR}{(\mathrm{HQ1}_{\text{KZ analytic SDR}})}
\providecommand{\hypStokes}{(\mathrm{HQ2}_{\text{Stokes choices}})}
\providecommand{\hypReflWts}{(\mathrm{HQ3}_{\text{reflected weights}})}
\providecommand{\hypTLift}{(\mathrm{HQ4}_{T = [Q_{\mathrm{tot}}, G]\text{ lift}})}
```

The point of these: at every theorem in `e_infinity_topologization.tex`, `wn_tempered_closure_platonic.tex`, `pva-descent.tex`, `bv_ht_physics.tex`, and parallel chapters, the relevant hypothesis tags appear *in the theorem statement*, not in a remark or introduction. This makes the conditional locus mechanically auditable.

---

## 5. Antipattern + cache row additions

### 5.1 New V2-AP entries to append to `notes/antipatterns_catalogue.md`

The catalogue is at 10157 lines. Append (in catalogue voice):

| Tag                            | Trigger                                                                                                                 | Counter-construction                                                                                                                                                          |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **V2-AP-OPEN-LOG**             | "open sector on the curve $X$" or "global open colour on $X$" without tangential log data                              | Replace with $(X, D, \tau)$ tangential log curve; open sector lives on real-oriented blowup / log boundary                                                                  |
| **V2-AP-MOD-CLOSED**           | "the closed chiral algebra is modular" (or equivalent)                                                                  | Modularity = trace + clutching on the open category; closed colour carries modular consequences only as image of open trace                                                  |
| **V2-AP-KAPPA-TUPLE**          | bare $\kappa$ used as a single scalar invariant                                                                         | Specify which row of $(\kappaCat, \kappaChHodge, \kappaChHeis, \kappaBKM, \kappaFiber)$; cite K3$\times E = (0,0,3,5,24)$                                                  |
| **V2-AP-Y-PLUS-NOT-G**         | "$\mathrm{CoHA}(\C^3) = W_{1+\infty}$" or "$Y^+(X) =$ quantum group" without Drinfeld double                            | $Y^+(X) = $ positive half; $G(X) = D(Y^+(X))$ requires Hall pairing + completion + integral form + stable-envelope transport + descent                                       |
| **V2-AP-HT-GLOBAL**            | local HT model imported without global obstruction                                                                      | Re-state vanishing $H^1(X, \C_X)$ holomorphic de Rham obstruction (or sheaf of local Hamiltonians) at every import site                                                       |
| **V2-AP-Δ5-HILBERT**           | "$\Delta_5$ = compact BPS Hilbert space" (or "$\Delta_5$ encodes the operator algebra")                                | $\Delta_5 = $ Borcherds denominator / virtual $K_0$ shadow; missing primitive is $\mathfrak D_X$ with $\mathrm{Pf}_{\mathrm{prot}}(\mathfrak D_X) = \Delta_5$                |
| **V2-AP-Z-PATH-INTEGRAL**      | "scalar automorphic form = 3d gravitational path integral" without Hall--Borcherds residual                            | Scalar automorphic form = protected trace of still-to-be-constructed operator package; Hall--Borcherds residual is the missing comparison                                    |
| **V2-AP-UNIVHOL-DYNAMIC**      | "Universal Holography functor constructs the quantum gravity path integral"                                             | Functor identifies $(\mathrm{boundary}, \mathrm{bulk}, \mathrm{interaction})$; for $A = \mathrm{Vir}_c$ this is the holographic boundary-CFT reading; not a metric integral |
| **V2-AP-W-INF-ENDPOINT**       | "$W_\infty[\lambda] \Rightarrow E_\infty$" without Prochazka + CKL + PRSh + Yamada hypotheses                          | Name all four hypotheses at theorem statement; finite-spin numerical agreement is evidence, not theorem                                                                       |
| **V2-AP-CLASS-M-AMBIENT**      | "class M chain-level holds" without naming ambient (ordinary $\mathrm{Ch}(\mathrm{Vect})$ vs weight-completed / pro / $J$-adic) | Ambient is part of statement; ordinary complexes give $S_4(\mathrm{Vir}_c) \neq 0$; weight-completed / pro / $J$-adic gives chain-level                                       |
| **V2-AP-PVA-CLASSICAL-QUANTUM**| "PVA $\lambda$-Jacobi $\Rightarrow$ all-loop quantum HT"                                                                  | $\lambda$-Jacobi $\Rightarrow$ classical gauge invariance only; quantum requires KZ SDR + Stokes + reflected weights + $T$-lift; name at every passage                       |
| **V2-AP-QUAD-KOSZUL**          | "quadratic chiral duality $\Rightarrow$ Koszul duality theorem"                                                          | Quadratic dual gives candidate dual + MC comparison map; bijectivity is Koszul-effective-special; Koszulness is a separate theorem (Vol I Theorem B / Positselski)            |
| **V2-AP-SHADOW-EQUALS-OBJECT** | (master pattern) any of {bar, $\kappa$, $\Delta_5$, $\Phi_{10}$, $Y^+$, $\mathrm{CoHA}$, finite-spin, MC injection} promoted to operator-level identity | Shadow identifies the protected trace of a primitive object; primitive object construction is separate. Apply Cut E.                                                          |

### 5.2 First-principles cache rows (append to `notes/first_principles_cache.md` or `_comprehensive.md`)

For each new AP, a corresponding cache row recording the *first-principles statement* the discipline rests on. The cache currently has 11104 + 474 lines. Pattern: each row gives the failure mode, the licensing chain, the canonical primary citation, and a one-line repair recipe.

Skeleton (one row per dismissal pair):

```
- ROW: <NUMBER>. Cut <X> — <pattern name>.
  Failure: <what goes wrong if discipline absent>.
  Licensing: <what data must be installed before the implication is licensed>.
  Source: <Vol III chapter:line / Vol II chapter:line / external paper>.
  Repair: <one-line recipe; cite macro / AP / cross-volume remark>.
```

The 12 rows correspond to the 12 new APs above plus the master pattern V2-AP-SHADOW-EQUALS-OBJECT.

---

## 6. Compute / IV obligations

The independent-verification audit runs through `compute/scripts/audit_independent_verification.py` and the `compute/tests/test_*_iv.py` decorators. Each Cut has an IV consequence:

- **Cut A (primitive package)**: no new compute. The seven-tuple is structural, not numerical. Discipline is enforced at TeX-compile / hook level.
- **Cut B (bar ≠ bulk)**: existing engines (`compute/lib/chiral_hochschild.py` and parallel) compute $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ for tabulated $A$. Audit: each $Z^{\mathrm{der}}_{\mathrm{ch}}$ test marked with `@independent_verification` should also assert "this is *not* $\mathrm{Bar}(A)$ in the trivial-coproduct sense" — currently implicit in the pairing structure. Add a test `test_bar_neq_bulk_iv.py` that for the five-archetype $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}/\mathsf{B}$ exhibits one Hochschild generator that does not lift to $\mathrm{Bar}(A)$ in the natural quasi-iso direction.
- **Cut C (κ-tuple)**: add `compute/tests/test_kappa_tuple_iv.py` computing all five rows for the five-archetype landmarks plus K3$\times E$. Independent-route witnesses: $\kappaCat$ via Künneth Euler char; $\kappaChHodge$ via Hodge supertrace; $\kappaChHeis$ via Cartan-rank reduction; $\kappaBKM$ via Borcherds $c_N(0)/2$; $\kappaFiber$ via fibre rank. Assert the five values for K3$\times E$ are $(0, 0, 3, 5, 24)$ and that the additive identity fails at $N \in \{1, 2, 3, 4, 6\}$.
- **Cut D (two-stage Φ + $Y^+ \neq G$)**:
  - `test_phi_two_stage_iv.py`: for $d = 2, 3$, verify that stage-1 output is $E_d$-holomorphic factorisation algebra and stage-2 specialisation lands in $E_1$-chiral; assert the directional restriction $\mathsf{SC}^{\mathrm{ch,top}}(\ldots, \mathsf{top}, \ldots; \mathsf{cl}) = \varnothing$.
  - `test_y_plus_vs_g_iv.py`: for $X = \C^3$, assert $\mathrm{CoHA}(\C^3) \cong Y^+(\fgl_1)$ at the Cartan / PBW level; assert that $W_{1+\infty}$ is recovered only after Drinfeld double + Fock evaluation (concretely: pole structure of vacuum module).
- **Cut E (shadow vs operator)**:
  - `test_delta_5_shadow_iv.py`: assert that $\Delta_5$ as Borcherds $\Phi_{10}$ scalar is a shadow of a $K_0$ class, and that no chain-level operator with $\mathrm{Pf}_{\mathrm{prot}} = \Delta_5$ is currently constructed; flag as `@open_problem`.
  - `test_w_inf_endpoint_iv.py`: assert that $W_\infty[\lambda]$ stress tower convergence is conditional on the four hypotheses; mark spin-≤8 numerical witnesses as `@evidence`, not `@theorem`.
  - `test_class_m_ambient_iv.py`: for ordinary $\mathrm{Ch}(\mathrm{Vect})$ ambient, assert $S_4(\mathrm{Vir}_c) \neq 0$ at generic $c$; for weight-completed ambient, assert $S_4 \to 0$ in the inverse limit.
  - `test_quad_vs_koszul_iv.py`: for non-Koszul quadratic chiral dual, assert $\mathrm{Hom}(A, B) \to \mathrm{MC}(A^! \otimes B)$ is injective but not surjective; for Koszul quadratic, assert bijection.

These tests are independent-verification: each must use a *disjoint* construction path from the chapter's proof. Add `@independent_verification(disjoint_route="...")` decorators.

---

## 7. Voice / CG-rectification consequences

The Chriss--Ginzburg voice rule: every theorem statement names its mathematical object directly, with conditional loci stated *at the theorem*, not in introductions or remarks. The 17 dismissals translate into prose-level forbidden constructions to add to `notes/cg_rectify_redo_queue.md` (currently the active queue):

**Forbidden phrasings** (replace each with the corresponding allowed phrasing):

| Forbidden                                                                  | Allowed                                                                                                                                                            |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Let $A$ be a chiral algebra"                                              | "Let $\primPkgX$ be the open factorisation primitive package on the tangentially-decorated curve $\logCurve$, and $A_b = \mathrm{End}_{\openFactCat}(\bdyVac)$" |
| "the bar complex is the bulk"                                              | "$\bulkOf{A} = \bulkChirHoch{A}$ is the bulk; $\BarTwc{A}$ is the twisting/coupling coalgebra"                                                                       |
| "the $E_1$-bar direction explains $2d \to 3d$ HT"                          | "the boundary $A_\infty$-chiral object passes to the one-dimension-up acting object $\bulkOf{A}$ via chiral Deligne--Tamarkin; the bar is a computational model"   |
| "the open colour on $X$"                                                   | "the open colour on $\logCurve$"                                                                                                                                    |
| "the closed chiral algebra is modular"                                     | "the open category carries cyclic trace compatible with clutching; the closed colour shadow has modular consequences"                                              |
| "$\kappa = $ \dots" (single scalar)                                         | "the $\kappa$-tuple $\kappaTuple{A}$ takes values \dots"                                                                                                            |
| "$\Phi_d : \mathrm{CY}_d\text{-Cat} \to \mathrm{ChirAlg}$"                  | "$\Phi_d^{(\Sigma_{d-1}, C)} = \SpCh \circ \PhiFA_d$"                                                                                                                |
| "$\mathrm{CoHA}(\C^3) = W_{1+\infty}$"                                      | "$\mathrm{CoHA}(\C^3) = \Yplus{\fgl_1}$; $\Wonepinf$ is the Fock evaluation of $\Drinfdouble{\Yplus{\fgl_1}}$"                                                       |
| "6d hCS = 3d Chern--Simons in disguise"                                    | "6d hCS realises $\PhiFA_3$ on verified loci; the one-loop obstruction is quartic $\int_X \mathrm{Tr}_{\mathrm{ad}} A(F_A)^3$; 3d-CS is an analogy"                |
| "formal local HT $\Rightarrow$ global compact theory"                       | "formal local HT + descent + QME + anomaly + locality $\Rightarrow$ candidate compact background, conditional on $\hypHTGlobalDR$"                                  |
| "$\Delta_5$ is the compact BPS Hilbert space"                              | "$\Delta_5$ is the Borcherds denominator; the operator-level $\operatorPrim{X}$ with $\protectedPfaff{\operatorPrim{X}} = \Deltafive$ is the construction problem" |
| "$Z_{\mathrm{BPS}}$ is the gravitational path integral"                    | "$Z_{\mathrm{BPS}} = \Phitenun^{-1} = \Deltafive^{-2}$ is the protected scalar shadow; gravity-line promotion is the Hall--Borcherds residual"                     |
| "Universal Holography constructs 3d quantum gravity"                       | "Universal Holography functor identifies $(\bdyAlg, \bulkOf{A}, \SCchtop\text{-brace})$; for $A = \mathrm{Vir}_c$ this is the holographic boundary-CFT reading"      |
| "$W_\infty[\lambda] \Rightarrow E_\infty$"                                  | "$W_\infty[\lambda] \Rightarrow E_\infty$ conditional on $\hypProchazka, \hypCKL, \hypPRSh, \hypYamada$"                                                              |
| "class M chain-level holds"                                                | "class M chain-level holds in the weight-completed ambient ($\hypAmbientWtCpl$); fails in $\mathrm{Ch}(\mathrm{Vect})$"                                              |
| "PVA $\lambda$-Jacobi $\Rightarrow$ quantum theory"                         | "PVA $\lambda$-Jacobi $\Rightarrow$ classical gauge invariance; quantum theory conditional on $\hypKZSDR, \hypStokes, \hypReflWts, \hypTLift$"                     |
| "quadratic chiral duality = Koszul duality"                                | "quadratic chiral dual gives candidate dual + MC injection; Koszulness (Vol I Theorem B / Positselski) is separate"                                                |

This table is to be added to `notes/cg_rectify_redo_queue.md` as a Wave-N entry. Apply via `chriss-ginzburg-rectify` skill chapter-by-chapter.

---

## 8. Phasing / sequencing

The reconstitution work has natural dependencies. Eight phases, with explicit blocking relations:

**Phase 1 — Architectural macro layer (1–2 sessions, no chapter prose work)**

1. Add Cut A through Cut E macros to Vol II `main.tex` preamble (§4 above).
2. Add `\providecommand` stubs to chapters that already use the underlying objects (chiefly: `bar-cobar-review.tex`, `hochschild.tex`, `programme_climax_platonic.tex`, `3d_gravity.tex`, `sc_chtop_heptagon.tex`, `factorization_swiss_cheese.tex`, `unified_chiral_quantum_group.tex`, `log_ht_monodromy_frontier.tex`, `e_infinity_topologization.tex`, `weight_completed_topologization_class_m_platonic.tex`, `pva-descent.tex`, `bv_ht_physics.tex`, `concordance.tex`, `theorems_C_D_native_vol2_platonic.tex`).
3. Cross-volume: mirror the same macros into Vol I `main.tex` and Vol III `main.tex` preambles (where the underlying object already lives there).

**Phase 2 — Architectural Definition + canonical statements (2–3 sessions)**

4. **Cut A**: write `chapters/frame/primitive_package.tex` (or extend `chapters/theory/foundations.tex`) with a single named Architectural Definition of the seven-tuple; cross-reference from each Vol II theorem that begins "Let $A$ be \dots".
5. **Cut B**: consolidate the bar/centre canonical statement at the top of `chapters/connections/bar-cobar-review.tex` (or `chapters/theory/foundations.tex`); add `\label{def:bar-twc-coalgebra}` and `\label{def:bulk-derived-centre}`. Every "bulk" appearance in Vol II refers to one of these labels.
6. **Cut C**: inscribe the K3$\times E$ five-row κ tuple at `chapters/connections/concordance.tex` (table) and `chapters/connections/programme_climax_platonic.tex` (climax remark). Audit all $\rho_K = \kappa(A) + \kappa(A^!)$ uses in `chapters/theory/theorems_C_D_native_vol2_platonic.tex` and `chapters/theory/introduction.tex`.
7. **Cut D**: promote `rem:heptagon-two-stage-CY-to-chiral` and `rem:pentagon-two-stage` from remarks to a single Architectural Lemma in `chapters/theory/sc_chtop_heptagon.tex` (or, better, a frame chapter). Cross-reference from every $\Phi_d$ usage.
8. **Cut D Vol III work** (cross-volume blocker for #8): elevate $G(X) = D(Y^+(X))$ from main-text prose to a load-bearing theorem statement in Vol III `chapters/theory/quantum_chiral_algebras.tex` or a successor chapter; cross-reference from Vol II.
9. **Cut E**: write `chapters/frame/shadow_vs_operator_manifest.tex` (new) listing the eight shadows + operator-level primitives + comparison-map status.

**Phase 3 — Antipattern + cache row append (1 session)**

10. Append the 12 new V2-APs to `notes/antipatterns_catalogue.md`.
11. Append corresponding 12 first-principles cache rows to `notes/first_principles_cache.md` and `_comprehensive.md`.

**Phase 4 — Per-dismissal prose audit (the GAPs) — 4–6 sessions**

12. **Dismissal 10 (HT global obstruction)**: at every Vol II HT-import site (`bv_ht_physics.tex`, `holomorphic_topological.tex`, `affine_half_space_bv.tex`, `physical_origins.tex`, `ht_bulk_boundary_line*.tex`), add a paragraph re-stating the global obstruction with cross-reference to `~/mixed-holomorphic-topological-strings/main.tex:3200–3210, 3232–3233`. Tag with `\hypHTGlobalDR`.
13. **Dismissal 14 (W∞ → E∞ endpoint)**: in `chapters/theory/e_infinity_topologization.tex:1163–1241`, rewrite the four hypotheses to cite Prochazka 1809.06993, Creutzig--Kanade--Linshaw 1704.08023, Pope--Romans--Shen / Bakas, Yamada weight-window. Mirror in `wn_tempered_closure_platonic.tex`, `tempered_stratum_characterization_platonic.tex`, `irrational_cosets_tempered_platonic.tex`, `logarithmic_wp_tempered_analysis_platonic.tex`. Tag spin-≤8 numerical results as `\ClaimStatusEvidence`, not `\ClaimStatusProvedHere`.
14. **Dismissal 16 (PVA classical vs quantum)**: rewrite `pva-descent.tex:25–43` so H1–H4 are stated as $\hypKZSDR, \hypStokes, \hypReflWts, \hypTLift$ at the theorem statement, not in introduction. Mirror in `pva-descent-repaired.tex`, `pva-expanded-repaired.tex`, `modular_pva_quantization_core.tex:40–60`.
15. **Dismissal 17 (quadratic vs Koszul)**: at `bar-cobar-review.tex:174–181`, add the "injection in general; bijection only under Koszul effectiveness" caveat at the theorem locus. Audit `theorems_C_D_native_vol2_platonic.tex` for Theorem A vs Theorem B separation. Cross-reference `MEMORY.md` row `feedback_koszul_formality_distinction.md` (Koszul ≠ SC-formal).

**Phase 5 — Per-dismissal voice sweep (CG-rectification) — 2–3 sessions, by skill**

16. Run `chriss-ginzburg-rectify` on each of the 17 chapters touched by Phase 4, with the §7 voice table loaded as input. Skill loop: gate-0 → forbidden-phrasing flag → replacement → gate audit. The skill is already configured.

**Phase 6 — Compute / IV scaffolding (3–4 sessions)**

17. Add the test files listed in §6: `test_bar_neq_bulk_iv.py`, `test_kappa_tuple_iv.py`, `test_phi_two_stage_iv.py`, `test_y_plus_vs_g_iv.py`, `test_delta_5_shadow_iv.py`, `test_w_inf_endpoint_iv.py`, `test_class_m_ambient_iv.py`, `test_quad_vs_koszul_iv.py`. Each with disjoint-route witnesses and `@independent_verification` decorators.
18. Run `make verify-independence`. Each new test corresponds to a `\ClaimStatusProvedHere` theorem updated in Phases 2–4.

**Phase 7 — Cross-volume integrity audit (1 session)**

19. Run a `concordance.tex` re-render confirming all cross-volume macros resolve (Vol I, Vol II, Vol III).
20. Re-run the `propagate` skill to verify cross-volume κ-tuple, two-stage Φ, $Y^+$ vs $G$, and shadow-vs-operator agreements.
21. Build `make` (full pass) — confirm `out/main.pdf` resolves all `\providecommand` stubs.

**Phase 8 — Final Beilinson cut audit (1 session)**

22. Run `audit` skill (`Deep Beilinson audit for Vol II`) with the §0 architectural fact loaded as the licensing rule. Each surviving primitive claim must satisfy the licensing chain. Each surviving shadow claim must point to its operator-level primitive.

**Total estimate**: 14–20 working sessions, parallelisable across Phase 4 (5 sessions for 4 GAPs, can run as 4-agent swarm) and Phase 6 (test files independent). Phases 1–3 strictly sequential; Phases 7–8 strictly final.

---

## 9. What is already inscribed in the manuscripts (so we do not redo it)

The critique recapitulates corrections that are *already in the prose* in 9 of 17 cases. Reconstitution is consolidation, not first-time correction. Concretely:

- `main.tex:729` `rem:bar-not-bulk` — Cut B carrier.
- `main.tex:762` `thm:gravity-mc-primitive-package` — Cut A carrier.
- `chapters/connections/3d_gravity.tex:4108, 4146, 4526, 4814` — primitive package and gravity MC theorem.
- `chapters/connections/3d_gravity.tex:4466–4499, 8429, 12748–12771` — Cut E (shadow vs operator) for $\Delta_5$ and $Z_{\mathrm{BPS}}$, with `conj:gravity-line-hall-borcherds-comparison` at the centre.
- `chapters/connections/programme_climax_platonic.tex:56–76` — Cut E for Universal Holography (does not construct dynamical metric).
- `chapters/connections/hochschild.tex:547`, `chapters/theory/foundations_recast_draft.tex:293` — Cut B explicit refutation.
- `chapters/connections/sc_chtop_heptagon.tex:136–206` (`rem:heptagon-two-stage-CY-to-chiral`), `chapters/theory/factorization_swiss_cheese.tex:2069–2115` (`rem:pentagon-two-stage`) — Cut D.
- `chapters/connections/log_ht_monodromy_frontier.tex:154–224` — Cut D ($Y^+$ side, Schiffmann--Vasserot + Drinfeld double).
- `chapters/theory/unified_chiral_quantum_group.tex:675–677, 1594–1619` — Cut D (Drinfeld double).
- `chapters/theory/weight_completed_topologization_class_m_platonic.tex:1–80` — Cut E (class M ambient).
- `chapters/theory/equivalence.tex:145` — Cut E (class M ambient cross-reference).
- `chapters/theory/introduction.tex:1972, 1980` — Cut C ($\kappaChHeis = 3$ vs $K^{\kappaCh} = 8$ Mukai conductor).
- Vol III `chapters/examples/k3e_cy3_programme.tex:4564, 4750–4762` — Cut C source counterexample.
- Vol III `chapters/theory/quantum_chiral_algebras.tex:402–403, 465–469` — Cut E (6d hCS quartic obstruction).
- Vol III `main.tex:1006` — Cut D source theorem.
- `~/mixed-holomorphic-topological-strings/main.tex:3200–3210, 3232–3233` — Cut E (HT global obstruction source).
- `~/igusa-cusp-form/main.tex:94–98, 110–118` — Cut E ($\Delta_5$ operator-level construction problem).

The 4 genuine GAPs requiring new prose: dismissal 10 (HT import to Vol II), dismissal 14 (W∞ endpoint hypotheses citation), dismissal 16 (PVA hypotheses at theorem statement), dismissal 17 (quadratic-vs-Koszul caveat at theorem statement).

---

## 10. The reconstitution invariant

After Phases 1–8, the manuscript across all five programmes has the following invariant:

1. **Every primitive object is named through its full data.** No "Let $A$ be a chiral algebra" without the seven-tuple. No bare "the curve $X$" without $(X, D, \tau)$. No bare "$\kappa$" without a tuple row.
2. **Every shadow is named through the operator-level primitive it traces.** No "$\Delta_5$ is the Hilbert space"; instead "$\Delta_5 = \protectedPfaff{\operatorPrim{X}}$ is the protected Pfaffian shadow of the operator-level $\operatorPrim{X}$" — and where $\operatorPrim{X}$ is not yet constructed, the construction problem is explicitly named.
3. **Every implication chain has its hypotheses stated at the implication, not in introductions.** No "$W_\infty[\lambda] \Rightarrow E_\infty$" without $\hypProchazka, \hypCKL, \hypPRSh, \hypYamada$ in the same display.
4. **Every cross-volume identification is two-staged where it is two-staged.** No $\Phi_d : \mathrm{CY}_d\text{-Cat} \to \mathrm{ChirAlg}$ without $\PhiFA_d$ and $\SpCh$ separately written. No $Y^+(X) = G(X)$ without the Drinfeld double.
5. **Every modularity claim is at the open-category trace level.** No naked "the closed algebra is modular."
6. **Every chain-level claim names its ambient.** No naked "class M holds chain-level."
7. **Every Koszul claim is separate from its quadratic shadow.** No naked "quadratic dual gives Koszul duality."
8. **Every analogy is labelled as analogy.** 6d hCS / 3d CS, formal-local / global, finite-spin / endpoint, scalar-form / path-integral — all analogies declared.

Stated negatively:

> Once the reconstitution lands, no statement in any of the five manuscripts is allowed to be primitive if it is only true after choosing a boundary object, passing to a trace, averaging from ordered to symmetric, taking a protected index, completing a category, imposing endpoint hypotheses, or installing descent data.

That is the architectural commitment the critique purchases. The prose is unchanged where it was already disciplined; the prose is sharpened where it was qualified-but-loose; new prose closes the four genuine GAPs; and the macro + AP + cache + IV + voice layers consolidate the discipline into a *visible architectural surface* that future swarms cannot quietly violate.

The work is finite, sequenced, and partly already done. The Beilinson cut is therefore *not a retraction* but a *compression*: the same theorems, more cleanly licensed.

---

## Appendix A — One-line recipe per dismissal

1. Replace bare $A$ with $\primPkgX$. *(chapters touched: foundations, frame, every theorem opening)*
2. Replace bare "bulk = $\BarTwc{A}$" with "bulk = $\bulkOf{A} = \bulkChirHoch{A}$." *(consolidate at bar-cobar-review.tex)*
3. Cite `thm:chiral-deligne-tamarkin-2d-3d` instead of "$E_1$-bar direction." *(chiral_higher_deligne.tex anchor)*
4. Replace bare $X$ with $\logCurve = (X, D, \tau)$ at every open-sector use. *(factorization_swiss_cheese.tex, sc_chtop_heptagon.tex, log_ht_monodromy*.tex, raviolo*.tex)*
5. Replace "the closed algebra is modular" with "the open category carries cyclic trace + clutching; closed shadow modular." *(modular_swiss_cheese_operad.tex, modular_pva_quantization*.tex, celestial chapters)*
6. Replace bare $\kappa$ with $\kappaTuple{A}$. Inscribe K3$\times E$ row. *(introduction.tex, theorems_C_D_native, climax, concordance)*
7. Replace $\Phi_d$ with $\PhiFA_d$ + $\SpCh$. Cite the architectural Lemma. *(every chapter using $\Phi_d$)*
8. Replace $\mathrm{CoHA}(\C^3) = \Wonepinf$ with $\mathrm{CoHA}(\C^3) = \Yplus{\fgl_1}$, $\Wonepinf = \mathrm{Fock}(\Drinfdouble{\Yplus{\fgl_1}})$. *(unified_chiral_quantum_group, log_ht_monodromy_frontier, celestial chapters; Vol III: elevate to theorem)*
9. Tag 6d-hCS/3d-CS as analogy; cite quartic obstruction. *(six_d_hcs_e3_chiral_avatar_platonic, kontsevich_integral, feynman_diagrams)*
10. At every Vol II HT-import site, add $\hypHTGlobalDR$ paragraph + cross-reference. *(bv_ht_physics, holomorphic_topological, affine_half_space_bv, ht_bulk_boundary_line\*)*
11. Replace "$\Delta_5 = $ BPS Hilbert" with "$\Delta_5 = \protectedPfaff{\operatorPrim{X}}$; $\operatorPrim{X}$ = construction problem." *(programme_climax_platonic, 3d_gravity, celestial_moonshine_bridge, thqg_3d_gravity_movements_vi_x)*
12. Replace "$Z_{\mathrm{BPS}} = $ path integral" with "$\ZBPS = \Phitenun^{-1} = \Deltafive^{-2}$ = protected scalar shadow; gravity-line via Hall--Borcherds residual." *(3d_gravity, modular_pva_quantization, anomaly_completed_topological_holography)*
13. Tighten `rem:climax-qg-scope` with the four required hypotheses. *(programme_climax_platonic.tex)*
14. Rewrite `e_infinity_topologization.tex:1163–1241` four hypotheses with Prochazka / CKL / PRSh / Yamada citations. Mirror in $W$-tempered chapters. *(e_infinity_topologization, wn_tempered_closure_platonic, tempered_stratum_characterization_platonic, irrational_cosets_tempered_platonic, logarithmic_wp_tempered_analysis_platonic)*
15. At every "class M chain-level" claim, name the ambient. *(class_m_direct_sum_obstruction_platonic, weight_completed_topologization_class_m_platonic, topologization_class_m_original_complex_platonic, koszulness_moduli_M_kosz, theorems_C_D_native_vol2_platonic)*
16. At every "PVA $\to$ quantum" passage, name $\hypKZSDR, \hypStokes, \hypReflWts, \hypTLift$ at theorem statement. *(pva-descent, pva-descent-repaired, pva-expanded-repaired, modular_pva_quantization_core)*
17. Add "injection in general; bijection only under Koszul effectiveness" caveat at `bar-cobar-review.tex:174–181`. Audit `theorems_C_D_native_vol2_platonic.tex`. *(bar-cobar-review, equivalence, theorems_C_D_native_vol2_platonic, foundations)*

## Appendix B — Status flag for every manuscript output

After Phase 8, the following invariant holds across every Vol II PDF (and analogous across Vol I, Vol III, mixed-HT-strings, igusa):

| Element                                       | Status                                                                                                                                         |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Architectural Definition: primitive package   | Inscribed in `chapters/frame/primitive_package.tex` (or `foundations.tex`); cited by every theorem opening                                      |
| Architectural Lemma: two-stage CY-chiral      | Inscribed in `chapters/theory/sc_chtop_heptagon.tex`; cited by every $\Phi_d$ use                                                              |
| Architectural Manifest: shadow vs operator    | Inscribed in `chapters/frame/shadow_vs_operator_manifest.tex`; cited by every shadow use                                                       |
| Bar/centre canonical statement                | Inscribed in `chapters/connections/bar-cobar-review.tex` top; cited by every "bulk" use                                                        |
| K3$\times E$ κ-tuple row                       | Inscribed in `concordance.tex` table + `programme_climax_platonic.tex` remark                                                                  |
| 12 V2-APs                                     | Appended to `notes/antipatterns_catalogue.md`                                                                                                  |
| 12 cache rows                                 | Appended to `notes/first_principles_cache.md` (+ comprehensive)                                                                                |
| 8 IV test files                               | Added to `compute/tests/`; passed by `make verify-independence`                                                                                |
| Voice sweep (17-line table)                   | Applied via `chriss-ginzburg-rectify` to every chapter touched in Phase 4                                                                      |
| Cross-volume macro layer                      | Mirrored in Vol I, Vol II, Vol III main.tex preambles                                                                                          |
| Cross-volume integrity                        | `make` passes; `propagate` skill confirms agreement                                                                                            |
| Beilinson final audit                         | `audit` skill confirms licensing rule on every primitive and shadow                                                                            |

**End state**: the five manuscripts share a single visible architectural layer; the "shadow = object" pattern is mechanically caught; the four GAPs are closed; nothing is silently promoted; nothing is silently downgraded; the prose is exactly as ambitious as the underlying theorems license — and no more.
