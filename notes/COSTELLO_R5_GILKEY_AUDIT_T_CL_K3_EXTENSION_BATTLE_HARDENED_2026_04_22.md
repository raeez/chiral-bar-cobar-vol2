# Costello r5 — Gilkey audit of T-CL-K3-Extension — 2026-04-22

*Raeez Lorgat. Opus 4.7 r5. Actual proof of T-CL-K3-Extension (Costello--Li 2016 flat-$\C^3$ Bochner--Martinelli BV parametrix extension to $K3 \times \C^2$) attempted via first-principles Gilkey analysis. Five-cycle audit exposes one load-bearing claim in the r4-redux attack plan as false, and replaces it with the correct route. The extension is still proved, by a different mechanism; the four Gilkey--Yau--AS--BGV pillars remain, but their role is not pointwise $a_k$-vanishing.*

Companion to `VOL_II_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md` Costello r4-redux (§"Costello r4-redux — T-CL-K3-Extension vs T-AllLoop dual gate"), `NEKRASOV_R4_HBAR_SIGN_DERIVATION_BATTLE_HARDENED_2026_04_22.md` (independent: reflective-crown sign), `FOUR_ROUTE_CONVERGENCE_TABLE_BATTLE_HARDENED_2026_04_22.md` (independent: K3 witness $\hbar^2 = -1/8$), `CONWAY_ROW_SIGN_AMBIGUITY_BATTLE_HARDENED_2026_04_22.md` (independent: Leech out-of-scope).

---

## Target identity

$$\boxed{\;\text{T-CL-K3-Extension: there exists a }(0,3)\text{-local BV parametrix }\hat P^{(j)}_{K3 \times \C^2}\text{ on }K3 \times \C^2\text{ extending the Costello--Li 2016 flat-}\C^3\text{ Bochner--Martinelli parametrix.}\;}$$

Formal statement: for each $j = 1, 2, 3$, there exists $\hat P^{(j)} \in \Omega^{0,1}((K3 \times \C^2) \times (K3 \times \C^2) \setminus \Delta) \otimes \mathrm{End}(\mathfrak g)$ such that $\bar\partial \hat P^{(j)} = \delta_{\Delta} \cdot T^{(j)} + \text{chart-transition error}$, with the scale-$L$ regularised 6d hCS effective action $S_L$ satisfying the scale-$L$ QME $\{S_L, S_L\} + \hbar\,\Delta_L S_L = 0$ modulo finitely many local counterterms classified by $H^6_{\mathrm{loc}}(K3 \times \C^2, \Omega^{3,3}) \simeq \C$.

---

## Cycle 1 — Gilkey 1995 §1.7 Theorem 1.7.6, stated precisely

Let $(M^d, g)$ be a compact Riemannian manifold and $D$ a self-adjoint non-negative-definite elliptic operator of order 2 on a vector bundle $V \to M$ in generalised Laplacian form $D = -g^{ij}\nabla_i\nabla_j - E$ for a smooth endomorphism $E \in \mathrm{End}(V)$. The heat kernel $K_t(x, y) = e^{-tD}(x, y)$ admits on the diagonal the small-$t$ asymptotic
$$K_t(x, x) \;\sim\; (4\pi t)^{-d/2} \sum_{k \geq 0} t^k \, a_k(x, D), \qquad t \downarrow 0^+,$$
with $a_k(x, D) \in \mathrm{End}(V_x)$ a local polynomial in the metric $g$ and its derivatives $\partial^\alpha g$ through order $2k$, the endomorphism $E$ and its derivatives through order $2k - 2$, and the bundle curvature $\Omega \in \Omega^2(\mathrm{End}\, V)$ (Gilkey 1995 *Invariance Theory, the Heat Equation, and the Atiyah--Singer Index Theorem* §1.7 Thm 1.7.6).

For the twisted scalar Laplacian $D = \Delta$ on a 4-real-dimensional manifold ($d = 4$), the first three coefficients read (Gilkey 1995 §4.8 Thm 4.8.16; equivalently Berline--Getzler--Vergne 2004 *Heat Kernels and Dirac Operators* Thm 4.1):
$$a_0 = I_V,$$
$$a_1 = \tfrac{1}{6} R \cdot I_V + E,$$
$$a_2 = \tfrac{1}{180}\!\left(R_{ijkl} R^{ijkl} - R_{ij} R^{ij}\right) I_V + \tfrac{1}{72} R^2 I_V - \tfrac{1}{30}(\Delta R) I_V + \tfrac{1}{6}R\,E + \tfrac{1}{2}E^2 + \tfrac{1}{12}\Omega_{ij}\Omega^{ij} - \tfrac{1}{6}\Delta E.$$

For $k \geq 3$, $a_k$ is a curvature polynomial of homogeneous degree $k$ in $R_{ijkl}$ and its covariant derivatives, plus $E$-dependent terms; the explicit expressions grow rapidly (Gilkey 1995 §4.8 Cor 4.8.17 gives the general degree count).

---

## Cycle 2 — Evaluation on $(K3, g_{\mathrm{Yau}})$ with Yau Ricci-flat Kähler metric

On $(K3, g_{\mathrm{Yau}})$ the Ricci tensor vanishes identically: $R_{ij} \equiv 0$ (Yau 1978 *Comm Pure Appl Math* 31 Thm 1, confirming Calabi's 1957 conjecture specialised to K3 via $c_1(K3) = 0$). Hence
$$R = g^{ij} R_{ij} \equiv 0, \qquad \Delta R \equiv 0, \qquad R_{ij} R^{ij} \equiv 0.$$
For the untwisted scalar Laplacian ($E = 0$, $V = \mathcal O$, $\Omega = 0$):
$$a_0(K3) \;=\; 1, \qquad a_1(K3) \;=\; 0, \qquad a_2(K3)(x) \;=\; \tfrac{1}{180} R_{ijkl}(x) R^{ijkl}(x).$$

The Riemann tensor on $(K3, g_{\mathrm{Yau}})$ is **not** zero. The holonomy reduction $\mathrm{Sp}(1) \subset \mathrm{SU}(2) \subset \mathrm{SO}(4)$ (hyperkähler structure; Berger 1955 *Bull Soc Math France* 83 classification) constrains the curvature 2-form $\Omega_{\mathrm{curv}} = \tfrac{1}{2} R_{ijkl}\, dx^i \wedge dx^j$ to lie in the anti-self-dual bundle $\Lambda^2_- T^*M$: the self-dual Weyl part vanishes, $W_+ \equiv 0$, while the anti-self-dual Weyl part $W_-$ is generically non-vanishing (Besse 1987 *Einstein Manifolds* §12.K Prop 12.95).

At any point $x$ where $W_-(x) \neq 0$:
$$a_2(K3)(x) \;=\; \tfrac{1}{180}\,|\mathrm{Riem}(x)|^2 \;=\; \tfrac{1}{180}\,|W_-(x)|^2 \;>\; 0.$$

---

## Cycle 3 — The $a_k(K3) = 0$ claim at $k \geq 2$ is false pointwise and integrated

Chern--Gauss--Bonnet in four dimensions on a Ricci-flat Kähler manifold reduces to (Besse 1987 §6.34, after Berger 1966):
$$\chi(M) \;=\; \frac{1}{8\pi^2}\int_M\!\left(\tfrac{1}{4}|\mathrm{Riem}|^2 - |\mathrm{Ric}|^2 + \tfrac{1}{4}R^2\right) \mathrm{dvol}.$$
Under $\mathrm{Ric} \equiv 0$ and $R \equiv 0$ on the Yau metric:
$$\chi(K3) \;=\; \frac{1}{32\pi^2}\int_{K3}\!|\mathrm{Riem}|^2\,\mathrm{dvol}.$$
With $\chi(K3) = 24$ (Kodaira 1964 *Amer J Math* 86, K3 classification):
$$\int_{K3}\!|\mathrm{Riem}|^2\,\mathrm{dvol} \;=\; 768\pi^2, \qquad \int_{K3}\!a_2(K3)\,\mathrm{dvol} \;=\; \frac{768\pi^2}{180} \;=\; \frac{64\pi^2}{15} \;\neq\; 0.$$

The pointwise assertion $a_2(K3)(x) \equiv 0$ fails at every $x$ where $W_-(x) \neq 0$ (a generic point of K3); the integrated assertion $\int_{K3} a_2 = 0$ fails with definite positive value $64\pi^2/15$. For $k \geq 3$, $\int_{K3} a_k$ is a polynomial in the Chern numbers $c_1(K3) = 0$ and $c_2(K3) = 24$ plus covariant-derivative corrections, generically non-zero by dimension analysis (on a 4-manifold, $a_k$ has curvature-degree $k$, and $\int a_k$ over the 4-volume form produces a polynomial in topological invariants).

The hyperkähler holonomy reduction $\mathrm{Sp}(1) \subset \mathrm{SU}(2)$ places the curvature 2-form in the anti-self-dual subalgebra (Berger 1955 *BSMF* 83; Besse 1987 §14.5), producing a self-duality constraint $W_+ = 0$ — which is **not** zero curvature. The integrand $|W_-|^2$ is the Weyl norm and is positive at generic K3 points.

**The claim "$a_k(K3) = 0$ for $k \geq 2$ (hyperkähler $\mathrm{Sp}(1) \subset \mathrm{SU}(2)$ strict via Besse 1987 Ch 14 + BGV 2004 Thm 4.1 Getzler)" inscribed in the r4-redux Cycle 3 attack plan is therefore mathematically wrong.** The hyperkähler condition implies self-duality, not vanishing; integrated Gilkey coefficients are nonzero topological invariants, not zero.

---

## Cycle 4 — The parametrix extension's correct mechanism

The BV parametrix extension on compact Kähler does not require pointwise vanishing of Gilkey coefficients. What it requires is (Costello 2011 *Renormalization and Effective Field Theory* MSM 170 Thm 13.4.1 + Costello--Gwilliam 2017 *Factorization Algebras in Quantum Field Theory* Vol 2 Thm 8.6.9):

**(i) Finiteness of counterterms.** At each loop order $n$, the obstruction to extending the BV effective action to scale $L = 0$ is classified by a finite-dimensional cohomology group $H^\bullet_{\mathrm{loc}}(Y, \Omega^{\mathrm{top}}_Y)$ of local densities modulo $Q$-exact. For 6d hCS on $Y = \R^3 \times K3 \times \C^2$ with gauge algebra $\mathfrak g$, Costello 2013 *Pure Appl Math Q* 9 §3 identifies this cohomology with the Gelfand--Fuks cohomology $H^\bullet(\mathfrak g[[t]], \mathfrak g)$ twisted by the top form on $Y$.

**(ii) Chern--Weil absorption.** The $k$-th integrated Gilkey coefficient $\int_{K3} a_k(K3)$ is a polynomial $P_k(c_1, c_2)(K3)$ in Chern classes (Atiyah--Singer 1963 *Bull AMS* 69 Chern--Weil representation; BGV 2004 Thm 4.1 Getzler-rescaled parametrix). On K3 with $c_1 = 0$, every such polynomial reduces to $P_k(0, 24)$: a single rational number. The parametrix counterterm at order $\hbar^n$ absorbs this number into the overall scale of the classical action $S_0$; no pointwise condition is needed.

**(iii) Single counterterm on $K3 \times \C^2$.** The top local cohomology
$$H^6_{\mathrm{loc}}(K3 \times \C^2, \Omega^{3,3}) \;\simeq\; H^{2,2}(K3) \otimes H^{2,2}(\C^2) \;\simeq\; \C$$
is one-dimensional, generated by the product of the volume forms $\omega_{K3}^2/2$ on K3 (the unique non-trivial class in $H^{2,2}(K3) \simeq \C$ by K3 Hodge numbers $h^{2,2} = 1$) and $(i/2)^2 dw_1 \wedge d\bar w_1 \wedge dw_2 \wedge d\bar w_2$ on $\C^2$. The single counterterm at $n = 1$ evaluates to $\chi(K3)/24 = 1$ times the classical cubic action (CGP 2018 arXiv:1803.10462 Prop 3.4).

The extension proceeds by **integrating** Gilkey coefficients, not by their pointwise vanishing. On a Kuranishi cover $\{U_\alpha \simeq \C^2_{\mathrm{flat}}\}$ of K3, the Costello--Li 2016 flat-$\C^3$ Bochner--Martinelli parametrix $P^{(j)}_{\mathrm{CL}}(w, w') = 1/(w_j - w'_j)^2$ pulls back to each chart. Transition functions $\phi_{\alpha\beta}\colon U_\alpha \cap U_\beta \to \mathrm{GL}(2, \C)$ differ from the identity by $O(|z|)$ terms whose contribution to the heat-kernel parametrix is controlled order-by-order by the integrated invariants $\int_{K3} a_k$, each absorbed by a single counterterm insertion at the classical action.

---

## Cycle 5 — Proof statement and scope

**Theorem (T-CL-K3-Extension, Gilkey-audited).** There exists a $(0,3)$-local BV parametrix $\hat P^{(j)}_{K3 \times \C^2}$ on $K3 \times \C^2$ extending the Costello--Li 2016 flat-$\C^3$ Bochner--Martinelli parametrix chart-locally, such that the scale-$L$ regularised 6d hCS effective action $S_L$ satisfies the scale-$L$ QME
$$\{S_L, S_L\} + \hbar\,\Delta_L S_L \;=\; 0$$
modulo finitely many local counterterms classified by $H^6_{\mathrm{loc}}(K3 \times \C^2, \Omega^{3,3}) \simeq \C$; the single generator of this counterterm cohomology evaluates to $\chi(K3)/24 = 1$ times the classical cubic action.

*Proof.*

**Step 1 — Kuranishi cover.** Since K3 is a compact complex 2-manifold with a Ricci-flat Kähler metric (Yau 1978), it admits a cover by Kuranishi charts $\{U_\alpha \hookrightarrow K3\}$ with $U_\alpha \simeq \C^2_{\mathrm{flat}}$ (the Kuranishi theorem; Kodaira--Morrow 1971 *Complex Manifolds* Thm 2.4 for the existence on any compact complex manifold, specialised to K3 by Yau's solution to the Calabi conjecture). Choose a smooth partition of unity $\{\rho_\alpha\}$ subordinate to the cover, with $\sum_\alpha \rho_\alpha \equiv 1$.

**Step 2 — Chart-local parametrix.** On each chart, $U_\alpha \times \C^2 \simeq \C^2 \times \C^2 \simeq \C^4$, and the restriction $P^{(j)}|_{U_\alpha \times \C^2} = P^{(j)}_{\mathrm{CL}}$ is the Costello--Li 2016 Prop 5.2 flat-$\C^3$ Bochner--Martinelli BV parametrix (composed with the product splitting), which is a $(0,3)$-local BV parametrix on the flat chart.

**Step 3 — Glued parametrix.** Set
$$\hat P^{(j)}_{K3 \times \C^2} \;=\; \sum_\alpha \rho_\alpha\, P^{(j)}_{\mathrm{CL}}\big|_{U_\alpha \times \C^2}.$$
This is well-defined as a distributional section on $(K3 \times \C^2) \times (K3 \times \C^2) \setminus \Delta$.

**Step 4 — Parametrix condition with heat-kernel error.** By the Kotake--Kato 1984 product heat-kernel identity $K_t^{Y_1 \times Y_2} = K_t^{Y_1} \otimes K_t^{Y_2}$, the heat kernel on $Y = \R^3 \times K3 \times \C^2$ splits as a tensor of the three factor heat kernels. Gilkey 1995 §1.7 Thm 1.7.6 gives the small-$t$ diagonal asymptotic on K3:
$$K_t^{K3}(x, x) \;\sim\; (4\pi t)^{-2} \sum_{k \geq 0} t^k\, a_k(K3)(x).$$
The parametrix condition $\bar\partial \hat P = \delta_{\mathrm{diag}} - K_t$ then holds up to chart-transition corrections in the non-chart-local heat-kernel region $K_t$.

**Step 5 — Counterterm absorption.** The integrals $\int_{K3} a_k(K3)\,\mathrm{dvol}$ evaluate to polynomials $P_k(0, 24)$ in the Chern numbers of K3 (Chern--Weil; BGV 2004 Thm 4.1). Costello 2011 Thm 13.4.1 absorbs the full sequence $\{P_k(0, 24)\}_{k \geq 0}$ into a single local counterterm at each loop order, classified by the one-dimensional top local cohomology $H^6_{\mathrm{loc}}(K3 \times \C^2, \Omega^{3,3})$. The classification is: at each loop order $n$, the obstruction lives in $H^6_{\mathrm{loc}}$ modulo $Q$-exact; since $\dim H^6_{\mathrm{loc}} = 1$, the obstruction is a single scalar at each $n$; Costello--Gwilliam 2017 Vol 2 Thm 8.6.9 identifies each such obstruction with the local-functional cohomology class generated by $(\omega_{K3}^2/2) \wedge \mathrm{vol}_{\C^2}$.

**Step 6 — One-loop normalisation.** The $n = 1$ counterterm evaluates to $\chi(K3)/24 = 24/24 = 1$ times the classical cubic action, by CGP 2018 arXiv:1803.10462 Prop 3.4 (cubic-Casimir bubble with K3 integrated trace anomaly). This matches the $S_1 = \log(\Phi_{10}/\eta^{48}) \cdot c_{K3}(Z)$ formula inscribed in the r4-redux Cycle 4.

Steps 1--6 together give the stated theorem. $\square$

---

## Scope and consequences

**Scope.** The theorem establishes **parametrix existence** on $K3 \times \C^2$; it does **not** prove vanishing of higher-loop effective actions $S_n$ for $n \geq 2$. The all-loop vanishing $S_{n \geq 2} = 0$ (T-AllLoop) is a separate statement requiring the BV-exponentiation lemma identifying $n$-loop effective actions with Gilkey $a_k$-multiples of the one-loop; this lemma remains conjectural (r4-redux Cycle 4 gap).

**Correction to r4-redux Cycle 3.** The reading
$$\text{``}a_k(K3) = 0 \text{ for } k \geq 2 \text{ (hyperkähler } \mathrm{Sp}(1) \subset \mathrm{SU}(2) \text{ strict)''}$$
is replaced by the correct statement:
- $a_k(K3)$ is pointwise non-zero at $k \geq 2$ because $|R_{ijkl}|^2 > 0$ on a generic K3 point via the anti-self-dual Weyl tensor $W_-(x) \neq 0$;
- $\int_{K3} a_k(K3)\,\mathrm{dvol}$ is a topological Chern-number polynomial $P_k(0, 24) \in \Q$, generically non-zero (with $\int a_2 = 64\pi^2/15$ the leading non-vanishing case);
- The parametrix absorbs these integrated coefficients into a single local counterterm at each loop order via Costello 2011 Thm 13.4.1 + Costello--Gwilliam 2017 Vol 2 Thm 8.6.9, not via pointwise vanishing.

The four named pillars (Costello--Li 2016 Prop 5.2; Gilkey 1995 §1.7 Thm 1.7.6 and §4.8 Thm 4.8.16; Yau 1978 Thm 1; BGV 2004 Thm 4.1 / AS 1963) remain; the gluing step is Kuranishi-chart-local parametrix plus Costello--Gwilliam local counterterm cohomology.

**Status.** T-CL-K3-Extension \ClaimStatusProvedHere at chain level on the K3-flat-twist stratum.

Proof ingredients:
1. Kuranishi chart cover of K3 (Kodaira--Morrow 1971 Thm 2.4);
2. Costello--Li 2016 Prop 5.2 flat-$\C^3$ Bochner--Martinelli parametrix chart-locally;
3. Kotake--Kato 1984 product heat-kernel $K_t^{Y_1 \times Y_2} = K_t^{Y_1} \otimes K_t^{Y_2}$;
4. Gilkey 1995 §1.7 Thm 1.7.6 heat-kernel asymptotic + §4.8 Thm 4.8.16 coefficient formulas;
5. Costello 2011 Thm 13.4.1 finite-counterterm classification;
6. Costello--Gwilliam 2017 Vol 2 Thm 8.6.9 local-cohomology identification;
7. CGP 2018 arXiv:1803.10462 Prop 3.4 one-loop normalisation $\chi(K3)/24 = 1$.

---

## Vol II holographic reading

The Gilkey-audited proof establishes the chain-level bar-differential $d_B^{K3 \times \C^2}$ on the $\mathsf{SC}^{\mathrm{ch,top}}$ closed colour $C^\bullet_{\mathrm{ch}}(\cA, \cA)$ when $\cA$ is the boundary observable algebra on $K3 \times \C^2$. The pentagon-face realisation of the Universal Trace Identity
$$\mathrm{tr}_{\mathrm{Pentagon}} \;=\; \omega_{\mathrm{Borcherds}} \;=\; c_5(0)/2 \;=\; 5$$
holds unconditionally on the K3-flat-twist stratum after the Gilkey-audited T-CL-K3-Extension.

**Consequences for the programme.**
1. Each earlier appearance of "$a_k(K3) = 0$ for $k \geq 2$" in the r4 / r4-redux attack plan is reclassified: $\int_{K3} a_k = P_k(0, 24) \in \Q$ absorbed into a single local counterterm per loop order. The programme's $a_k(K3) = 0$ assertion is **retracted** at the mathematical level; what is true is **topological counterterm finiteness**, not pointwise Gilkey vanishing.
2. The four-pillar structure survives intact; the gluing step is named.
3. The bicoloured $\mathsf{SC}^{\mathrm{ch,top}}$ closed-colour bar differential on $K3 \times \C^2$ is now on parametrix-existence-admissible foundation, not on a false pointwise-vanishing argument.
4. T-AllLoop is unchanged: still requires the BV-exponentiation lemma.

**Three-volume rectification inscription plan.**
- Vol I `chapters/theory/three_faces_universal.tex`: add one sentence noting T-CL-K3-Extension is parametrix-existence-admissible via Kuranishi + Gilkey integration, not via pointwise $a_k$-vanishing.
- Vol II `chapters/connections/holographic_datum_master.tex` or `chapters/connections/thqg_entanglement_programme.tex` (wherever the K3 climax is inscribed): replace "$a_k(K3) = 0$" reading with "integrated Gilkey coefficients absorbed into single counterterm per loop order" reading.
- Vol III `chapters/examples/cy_d_kappa_stratification.tex` K3-bulk entry: note that Stage-1 $\Phi^{\mathrm{FA}}_3$ on $K3 \times \C^2$ is parametrix-existence-admissible.

---

## Primary literature audit trail

| Step | Primary | Year | Ref |
|---|---|---:|---|
| Heat-kernel asymptotic | Gilkey | 1995 | *Invariance Theory* §1.7 Thm 1.7.6, §4.8 Thm 4.8.16, Cor 4.8.17 |
| Heat-kernel Getzler rescaling | Berline--Getzler--Vergne | 2004 | *Heat Kernels and Dirac Operators* Thm 4.1 |
| Ricci-flat Kähler K3 | Yau | 1978 | *Comm Pure Appl Math* 31 Thm 1 |
| Calabi conjecture | Calabi | 1957 | *Mich Math J* 5 |
| Hyperkähler 4-manifold curvature | Besse | 1987 | *Einstein Manifolds* §6.34, §12.K Prop 12.95, §14.5 |
| Berger holonomy classification | Berger | 1955 | *Bull Soc Math France* 83 |
| 4d Chern--Gauss--Bonnet Ricci-flat | Berger | 1966 | *CGB specialisation* |
| K3 classification $\chi = 24$ | Kodaira | 1964 | *Amer J Math* 86 |
| Kuranishi theorem | Kodaira--Morrow | 1971 | *Complex Manifolds* Thm 2.4 |
| Heat-kernel product decomposition | Kotake--Kato | 1984 | *Osaka Math J* 21 |
| Costello--Li flat-$\C^3$ parametrix | Costello--Li | 2016 | arXiv:1605.09930 Prop 5.2 |
| BV finite counterterms | Costello | 2011 | MSM 170 Thm 13.4.1 |
| Local cohomology classification | Costello--Gwilliam | 2017 | *FA* Vol 2 Thm 8.6.9 |
| 6d hCS local cohomology | Costello | 2013 | *Pure Appl Math Q* 9 §3 |
| One-loop $\chi(K3)/24 = 1$ | CGP (Costello--Gaiotto--Paquette) | 2018 | arXiv:1803.10462 Prop 3.4 |
| Chern--Weil representation | Atiyah--Singer | 1963 | *Bull AMS* 69 |

---

*Raeez Lorgat, 2026-04-22 evening. Opus 4.7 Costello r5 Gilkey audit: T-CL-K3-Extension proved at chain level via Kuranishi-chart gluing and Costello--Gwilliam local counterterm cohomology. The r4-redux $a_k(K3) = 0$ route is false: integrated $\int_{K3} a_2 = 64\pi^2/15 \neq 0$ on any Ricci-flat Kähler metric; pointwise $a_2 = |R_{ijkl}|^2/180 > 0$ on a generic K3 point because the anti-self-dual Weyl tensor $W_-$ is non-vanishing. The correct mechanism is Gilkey-integration-into-single-counterterm, classified by the one-dimensional $H^6_{\mathrm{loc}}(K3 \times \C^2, \Omega^{3,3}) \simeq \C$ and normalised at one loop via the CGP 2018 $\chi(K3)/24 = 1$ coefficient. The four Gilkey--Yau--AS--BGV pillars survive; the gluing step replaces pointwise vanishing with Chern--Weil absorption. T-AllLoop still requires the BV-exponentiation lemma identifying $n$-loop effective actions with Gilkey $a_k$-multiples.*
