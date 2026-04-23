# Vol II Anti-Patterns Catalogue

Author: Raeez Lorgat.

## Canonical values at the latest-wave verdict (2026-04-21)

When any entry in this catalogue or the first-principles cache appears
to assert one value while a later entry asserts another, the **latest
wave's verdict takes precedence**. The registry below pins the
canonical value for every quantity that has flipped at any point across
Waves 1-26. Every AP/cache entry that names an older value does so only
in retraction context (explicitly flagged as "wrong claim" / "old draft"
/ "retracted").

| Quantity | Canonical value (latest-wave verdict) | Retracted earlier values | Lock |
|---|---|---|---|
| $(c_{4d}, c_{2d})$ of $\mathcal T[A_1, \Sigma_{0, 24}]$ | $(107/6, -214)$ (Wave 15 Gaiotto) | $(26, -312)$ (Wave 14 error); $(23/4, -69)$ (Wave 25 Gaiotto agent error) | WOV-2 |
| Trinion/tube count at $n=24$ | $(n_v, n_h) = (63, 88)$ | $(21, 27)$ (Wave 25 confusion of trinion/tube count with multiplicities) | Chacaltana--Distler 2010 §5.14 |
| Universal $c_{4d}$ formula, $A_1$ genus 0 | $c_{4d} = (5n - 13)/6$ | $(12(g-1) + 7n)/6$ (Wave 14 error — fails $\mathrm{SU}(2)$ $N_f = 4$) | Shapere--Tachikawa 2008 |
| Monster BKM Cartan rank | $2$ (on $\mathrm{II}_{1,1}$) | $26$ (Wave 16 confusion with Fake-Monster) | Borcherds 1992 *Invent Math* 109 |
| Fake-Monster Cartan rank | $26$ (on $\mathrm{II}_{25,1}$) | --- | Borcherds 1992 |
| K3-BKM Cartan rank | $3$ (on $\Lambda^{2,1}_{II}$) | --- | Gritsenko--Nikulin 1998 §3 |
| $c_3$ (Borcherds coefficient) | $-8$ in Bruinier reduced-class convention | $176256$ (= $p_{24}(5)$, Wave 16 error; also the Gritsenko--Nikulin Cartan-matrix value with conversion factor $-22032$) | WOV-5 |
| $\zeta(3,3,3,3)$ numerical value | $0.000295999\ldots$ (depth-4, weight 12) | $0.0028565$ (Wave 17 draft, 10× error) | Brown 2012 motivic basis |
| $c(1, 2, \pm 2)$ heterotic lift coefficient | $-2$ (Wave 22 Witten) | $+1$ (Wave 21 error) | $\eta^{18} \theta_1^2$ direct expansion + DMZ 2012 + holomorphic-anomaly (three-path) |
| Humbert $H_4$ arithmetic description | $(2, 2)$-isogeny quotient of $E_1 \times E_2$ with $\mathrm{End} \supset \mathbb{Z}[2i]$; monodromy order 2 | $\mathbb{Q}(\sqrt 2)$-RM locus (Wave 15 imprecise; that is $H_8$, not $H_4$) | van der Geer 1988 Ch IX |
| Theorem B scope (Koszul locus) | $\overline{\mathcal A_2} \setminus \bigcup_{n \,\mathrm{admissible}} H_n$ (all admissible Heegner divisors) | $\overline{\mathcal A_2} \setminus (H_1 \cup H_4)$ (Wave 15 narrow) | Wave 18 Beilinson tightening |
| K3-BKM Weyl denominator | $\Delta_5 = \mathrm{Grit}(\eta^9 \vartheta_1) \in S_5(K(1))$ (additive) | $\Phi_{12}$ attempted (Fake-Monster, $\mathrm{II}_{25,1}$, multiplicative — different object) | Gritsenko 1999 Thm 6.1 |
| Umbral $A_{N-1}$ labelling rule | $(N-1) \mid 24$; at $N = 6$ reanchor to Niemeier $6 D_4$ | $N \mid 24$ (Wave 18 error) | Wave 19 Gaiotto |
| Leech lattice simple root norm | $2$; $r_\lambda = (\lambda; 1, 1 - \lambda^2/2) = (\lambda; 1, -1)$ at $\lambda^2 = 4$ | $6$ (Wave 24 Nekrasov formula error, using $r_\lambda = (\lambda; e + (\lambda^2 - 2)/2\,f)$) | Conway 1983 *Proc R Soc Lond A* 384; SPLAG Ch 27 |
| Fake-Monster Weyl vector | $\rho = e = (0_\Lambda; 1, 0)$ lightlike, $\rho_\Lambda = 0$ | Sign-inconsistent Wave-23 draft | Borcherds 1992 Thm 10.1 |
| $\Phi_{12}$ automorphic home | Orthogonal Shimura variety $\mathcal{D}_{\mathrm{II}_{26,2}} = O(26, 2)^+ / (O(26) \times O(2))$, complex dim 26, singular weight $12 = (26 - 2)/2$ | Siegel $\mathrm{Sp}_{26}(\mathbb Z)$ (impossible, $\mathbb H_{26}$ has dim 351); Jacobi-in-26-variables (no torus direction) | Borcherds 1992 |
| Restriction sublattice for $\Phi_{12} \to \Phi_{10}$ | Primitive $\mathrm{II}_{2,2} \hookrightarrow \mathrm{II}_{25,1}$, giving $O^+(\mathrm{II}_{2,2}) \cong \mathrm{Sp}_4(\mathbb Z)$ | $\mathrm{II}_{2,1}$ (Wave 23 error — sig $(2,1)$ carries no holomorphic modular form) | Gritsenko--Nikulin 1998 |
| Master $L$-value identification | $\log Z^{(1)}_{\mathbf H_{\Delta_5}} = -\log \Delta_5 - \kappa_{\mathrm{BGS}} \cdot L'(0, \Delta_5, \mathrm{std}) + \log C$, $\kappa_{\mathrm{BGS}} = 24$ | $L'(0, \Delta_{10}, \mathrm{ad}^0)$ (Wave 24 Costello — CAP-reducible, conflates three $L$-functions); $L'(0, \mathrm{ad}^0 \rho_{\Delta_{12}})$ (Wave 25 Gaiotto agent alternative, incompatible regulator) | Bruinier--Kühn 2003 Thm 4.11; Yoshikawa 2004 Thm 5.7 |
| Bloch--Kato Selmer on representation of $\mathbf H_{\Delta_5}$ deformation | $\dim H^1_f(\mathbb Q, \mathrm{std}\,\rho_{\Delta_5}) = 1$ (paramodular cyclotomic Hida family tangent) | $\dim H^1_f(\mathrm{ad}^0 \rho_{\Delta_{10}}) = 1$ (Wave 24 — right number, wrong representation; the adjoint spinor is rigid, dim 0) | Pilloni 2011 + Urban 2011 + Poor--Yuen 2015 + Thorne 2020 |
| Bridgeland $\dim \mathrm{Stab}(K3 \times E)$ | $48 = \mathrm{rk}\,\mathcal N(K3 \times E) = 24 \cdot 2$ | $26$ (Wave 23 claimed "codim-0 slice" — actual Künneth image has codim $22 = \mathrm{rk}\,T_{K3}$) | Bridgeland 2007 Thm 1.2 |
| Codim of $\mathrm{Stab}^\Phi$ inside ambient | $22$ | $0$ (Wave 23 error) | via four independent paths |
| Rank of $u_{\zeta_8}^{\mathrm{tilt}}$-mod | $162 = 27 \cdot 6 = (\ell' - 1)^3 \cdot \lvert S_3 \rvert$ | --- | Andersen--Polo--Wen 1994 |
| Structure of rank-$162$ MTC | $(A_1)_{k=2}^{\otimes 3} \rtimes S_3$ ($S_3$-crossed braided fusion) | $(A_1)_{k=2}^{\otimes 3} \boxtimes \mathbb Z[S_3]$ (Wave 23 tensor claim — $\mathrm{Vec}_{S_3}$ non-modular) | Turaev 2000; ENO 2010 |
| Conway $V^{s\natural}$ central charge | $c = 12$ | $c = 24$ (Wave 23 inherited from Monster error) | Duncan 2007 *Duke Math J* 139 |
| Conway $V^{s\natural}$ $\Psi$-placement | $\Psi^{\mathrm{metap}}$-image on metaplectic $\overline{\mathcal A_2^{(2)}}$ branch | Bosonic $\Psi$-image with $(K, \hbar^2) = (2, -1/2)$ (Wave 19/23 — Leech has no hyperbolic plane, universal identity out of scope) | Scheithauer 2008 |
| "Four is all" citation chain | Scheithauer 2017 + Dittmann--Ma--Scheithauer 2021 + Scheithauer 2006 (three papers) | Scheithauer 2017 alone (Wave 23/24 incomplete) | Scope: GN-reflective signature-$(2, n)$ with $n \ge 3$ |
| Fifth Borcherds product outside GN-scope | $24 A_1$ Niemeier product (Borcherds 1995 *Invent Math* 120 §13), reflective automorphic on sig-$(2, 24)$ singular weight 12 but fails GN-reflectivity (divisor non-rational-quadratic-hyperplane components) | --- | Borcherds 1995 |
| Pentagon admissibility congruence variable | $D_n = (n - 3)/2 \pmod 4 \in \{0, 1\}$, equivalently $n \equiv 3, 5 \pmod 8$ | $n \not\equiv 0, 3 \pmod 4$ (loose restatement) | Eichler--Zagier 1985 Thm 9.1 |
| Humbert--Heegner admissible $n \in [3, 36]$ | $\{3, 5, 11, 13, 19, 21, 27, 29, 35\}$ (nine values) | All Padovan-positive $n$ (loose) | Eichler--Zagier 1985 Thm 9.3 + Gritsenko--Nikulin 1998 |
| First admissible non-vanishing $\phi^{(n)}$ | $\phi^{(5)} = -2 \cdot [\mathrm{gen}]^{\otimes 5}$ | --- | Gritsenko--Nikulin 1998 Table 2 |
| Padovan $d_n$ reference table ($n \le 12$) | $(d_3, \dots, d_{12}) = (1, 0, 1, 1, 1, 2, 2, 2, 3, 4)$ with $d_n = d_{n-2} + d_{n-3}$, seeds $(1, 0, 1)$ | Fibonacci recurrence | Brown 2012 *Ann Math* 175 Thm 1 |
| $\phi^{(n)} \ne 0$ on K3-Humbert iff | (i) $n \equiv 3, 5 \pmod 8$ AND (ii) $d_n > 0$ AND (iii) $D_n \le 1$ (polar cutoff) | Padovan-only (AP-V2-24 / V2-AP127) | Eichler--Zagier Thm 9.3; Gritsenko--Nikulin 1998 |
| $\Psi$-functor completeness | **Four** sibling functors $\{\Psi, \Psi^{\deg}, \Psi^{\mathrm{tor}}, \Psi^{\mathrm{metap}}\}$ (disjoint union surjective) | $\Psi$ alone surjective (Wave 23 claim falsified) | Baily--Borel--Freitag stratification of $\overline{\mathcal A_2}$ |
| $\mathrm{grt}_1^{(1/2)}$ extension status | Non-split, non-abelian, non-central (three distinct properties) | "Split because central" (Wave 24 conflation) | Lie $H^2_{\mathrm{Lie}}(\mathfrak q; \mathrm{grt}_1)$ via van Est transgression |
| Obstruction cohomology type | Lie $H^2_{\mathrm{Lie}}$ via van Est transgression from group $H^1_{\mathrm{grp}}$ (Saito--Kurokawa Eichler cocycle) | Group $H^1$ only (Wave 24 misattribution) | Costello--Gwilliam 2017 BV realisation |
| $[\widetilde\sigma_2, \widetilde\sigma_2]$ | $288 \widetilde\sigma_4$ via $\tau(2)^2 / 2 = 288$ | --- | $\tau(2) = -24$ |
| $e_5$ vs $W_5$ | $e_5 = W_5$ identically at every $c$ | --- | Wang 1998 *Prog Theor Phys* Prop 4.2 three-leg uniqueness |
| $e_4$ at $c = -214$ | $:T \partial^2 T: - (3/2):(\partial T)^2: + (321/10) \partial^4 T + \hbar\mathrm{qt}(J^{(4)})$; pairing $(65193/10) \mathrm{Vol}(E) (2\pi i)^4$ | --- | Pope--Romans--Shen 1990; Wang 1998 |
| Chiral-Hochschild $e_k$ motivic home | Single-valued $\mathrm{zv}^{\mathrm{sv}}_{3k}$ (Brown 2014; Schnetz 2013) | Full motivic $\mathrm{Per}^{\mathrm{mot}}_{3k}$ (Wave 23 naive Costello cross-cut) | BGS analytic torsion on Shimura varieties forces SV |
| Pseudo-character target | Chenevier 2014 determinant $D_{\Delta_{10}}$ of dim 4 | Pseudo-representation (loses mod-$\ell^n$ Cayley--Hamilton for reducible $\rho_{\Delta_{10}}$) | Chenevier 2014 *Ann Inst Fourier* 64 |
| Hecke field of $\Delta_{10}$ | $\mathbb Q$ (since $\dim S_{26}(\mathrm{SL}_2(\mathbb Z)) = 1$); minimal coefficient ring $\mathbb Z$ | --- | Standard |
| Humbert divisor / AD correspondence | Humbert divisor $= $ Argyres--Douglas point at $E_{\tau_1} \times E_{\tau_2}$ (SW curve degenerates to pair of elliptic curves → $(A_1, A_{2N-1})$) | --- | GMN 2009 *Adv Theor Math Phys* 13 Ex 8.3 |
| $\kappa_\bullet$ indexing (K3 $\times$ E) | Four distinct values: $\kappa_{\mathrm{cat}} = 0$ (multiplicative Künneth), $\kappa_{\mathrm{ch}}^K = 3$ (additive), $\kappa_{\mathrm{BKM}}$ family-specific, $\kappa_{\mathrm{fibre}}(K3) = 2$ | Naive "$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal O_{\mathrm{fibre}})$" (fails for $N \ge 2$ — $N = 1$ accident only) | Always name the $\kappa_\bullet$ index |
| $\kappa_{\mathrm{BKM}}(\mathbf H_{\Delta_5})$ cross-volume value | **Pending AP5 lock** — Vol I abstract says 12, Vol III abstract says 5 (different $N$-index conventions for $c_N(0)/2$); every site must name the input denominator (Fake-Monster $\Phi_{12}$ vs paramodular $\Phi_{10} = \Delta_5^2$) | Both values occur in published inscriptions; resolve via landscape-census audit | Open AP5 audit |
| CoHA vs chiral-algebra type | $\mathrm{CoHA}_{K3 \times E}$ is $E_1$-associative (Hall product); chiralisation via $\Phi_3$-arrow gives $\mathbf H_{\Delta_5} = \Phi_3(\mathcal D_\hbar(\mathcal Y^{\mathrm{Hall}}(\mathrm{CoHA}_{K3 \times E})))$ | "CoHA is a chiral algebra" (type error) | Schiffmann--Vasserot + $\Phi_d$-functor framework |
| $\mathrm{CoHA}(\mathbb C^3)$ identification | $Y^+(\widehat{\mathfrak{gl}}_1)$ — the **positive half** of the affine Yangian | $W_{1+\infty}$ (classical limit only); full Yangian $Y$ | Schiffmann--Vasserot |
| $W_{1+\infty}$ vs $W_\infty[c]$ | $W_{1+\infty} = W_\infty[c] \otimes \mathcal H$ (Heisenberg); different objects | Conflating the two | Pope--Romans--Shen 1990 |
| Two-$\hbar$ discipline | $\hbar^{\mathrm{Drinfeld}} = 2\pi i / \ell$ (root-of-unity) vs $\hbar^{\mathrm{BV}}$ (loop-counting); semantically distinct but agree numerically at $\hbar^2 = -1/8$ for $\ell = 8$ | Using bare $\hbar$ without subscript | AP151 bridge |
| Bar cohomology class-$\mathbf M$ at $E_3$-level | $6^g$ (cohomological dim at $g \in \{1, 2, 3\}$; chain level is infinite) | "Infinite at cohomological level" | Wave 12 Vol III |
| $\kappa_{\mathrm{cat}}(K3 \times E)$ | $0$ (total space, Künneth multiplicative $\chi(\mathcal O_{K3}) \chi(\mathcal O_E) = 2 \cdot 0$) | $2$ (fiber only) | AP-CY68/AP234 discipline |

**Every cache/AP entry citing an older value must appear in a "Wrong
Claim" / "retracted" / "earlier draft" context. Any standalone assertion
of an older value is itself a latent AP violation; report it via
Gate 0 on sight.**


## Compatible dual readings (non-contradictions)

Some statements appear in different waves with apparently conflicting
framings yet describe the **same mathematical object** through two
compatible frames. An agent reading only one framing may mistake the
pair for a contradiction and attempt to "fix" one side, destroying
content. Every entry below is a certified **non-contradiction**: both
framings are correct simultaneously and reconcile through the named
mechanism. Do not flatten either reading. Do not treat this as an AP
retraction list; treat it as a frame-compatibility registry.

| Statement A (frame 1) | Statement B (frame 2) | Compatibility mechanism | Primary reference |
|---|---|---|---|
| Conway $V^{s\natural}$ is the $\Psi^{\mathrm{metap}}$-image on the metaplectic $\overline{\mathcal A_2^{(2)}}$ branch (canonical preamble, row 41). | Conway $V^{s\natural}$ is the $\mathbb Z/2$-super-twin of $V^\natural$ via Duncan's commutative orbifolding diamond (W20.2 healing). | Same VOA-super-algebra read from the $\Psi$-functor / $\overline{\mathcal A_2}$-stratification side and from the commutative-orbifolding-diamond side; the metaplectic $\Psi$-image equals the super-twin of the Leech CFT via the Duncan 2007 Frame-change. | Duncan 2007 *Duke Math J* 139; Scheithauer 2008. |
| $\kappa_{\mathrm{BKM}}(\mathbf H_{\Delta_5}) = 12$ (Vol I three-faces identity, Fake-Monster $\Phi_{12}$ input). | $\kappa_{\mathrm{BKM}}(\mathbf H_{\Delta_5}) = 5$ (Vol III Borcherds-weight count on paramodular $\Delta_5$). | Reconciled via W26.8: the two values index different input denominators ($\Phi_{12}$ vs $\Phi_{10} = \Delta_5^2$) under the same $c_N(0)/2$ rule. Each site must name the input denominator; the two are $(c_{\Phi_{12}}(0)/2, c_{\Delta_5}(0)/2) = (12, 5)$. | Borcherds 1992; Gritsenko 1999 Thm 6.1; canonical preamble row 57. |
| $e_4 = W_4 - (107/11)\Lambda_Z$ in the $W$-basis (Vol III abstract, $c = -214$). | $e_4 = {:}T\partial^2 T{:} - (3/2){:}(\partial T)^2{:} + (321/10)\partial^4 T + \hbar\,\mathrm{qt}(J^{(4)})$ in the Virasoro-composite basis (canonical preamble row 51). | Same cocycle class, two bases. Pope--Romans--Shen projection $W_k = e_k + (-c/22)\Lambda_Z$ converts between $W$-basis and Virasoro-composite basis; the scalar $-107/11 = c/22$ at $c = -214$ is the frame-change constant. | Pope--Romans--Shen 1990; Wang 1998 Prop 4.2. |
| Archetype $\mathbf B$ row: $\kappa + \kappa^! = 8$ (Vol I five-archetype table, $r(z)$-families). | K3 Mukai pairing $K = 2c_+ = 8$ (Vol III Mukai form on $\Lambda^{3,19}$). | Three faces of the same canonical $K = 8$: (i) derived-centre complementarity sum $\kappa + \kappa^!$; (ii) Mukai pairing $K = 2c_+$ with $c_+ = 4$; (iii) Lusztig reflection length $\ell_{\mathrm{Lusztig}} = 8$ at $\zeta_8$. All three equal $8$ because $K3 \times \mathrm{elliptic}$ pairs with $\mathbf H_{\Delta_5}$ through a single self-dual lattice indexing. | Borcherds--Mukai pairing; Lusztig 1989 at $\zeta_8$; Gritsenko--Nikulin 1998. |
| Padovan counts $d_n = d_{n-2} + d_{n-3}$ give MZV basis dimensions in weight $n$ (Brown 2012 conjecture). | Humbert-Heegner divisor filter selects arithmetically admissible $n \equiv 3, 5 \pmod 8$ on $\phi^{(n)}$ (Vol I / Vol III pentagon admissibility row). | Orthogonal filters. Padovan counts basis vectors; Humbert-Heegner selects admissible embedding points. The two do not compete: Padovan $d_n$ governs the motivic dimension; Humbert-Heegner governs the arithmetic non-vanishing locus. Compatible because $\phi^{(n)}$ lives in a weight-$n$ MZV-period space filtered further by admissibility. | Brown 2012; Eichler--Zagier 1985 Thm 9.1 (canonical row 44). |
| $(\infty, 1)$-obstruction tower (W21.2) gives the Maurer--Cartan tower of universal obstructions in an $(\infty, 1)$-stable category. | $(\infty, 2)$-adjunction AR structure (W22.1) exhibits bar--cobar as an adjunction in an $(\infty, 2)$-category with an Auslander--Reiten sequence. | The $(\infty, 2)$ structure is the $2$-categorical lift of the $(\infty, 1)$ obstruction tower: AR sequence at object level descends to the MC obstruction tower at morphism level. Both proved, both load-bearing. | Lurie HA 5.5; Riehl--Verity 2020. |
| Six-path $\chi_3$ (W22.6): six independent verification paths for the third Chern character. | Seven-path $\chi_3$ (W25.4): seven paths including a derived-deformation check. | Six independent paths plus one additional derived-deformation path, consistent with prior comparison. The seventh path refines the six without contradicting them. Every path reports the same $\chi_3$ value. | Beilinson multi-path verification discipline; W25.4 cache entry. |
| Four sibling functors $\{\Psi, \Psi^{\deg}, \Psi^{\mathrm{tor}}, \Psi^{\mathrm{metap}}\}$ parametrise the Baily--Borel--Freitag stratification of $\overline{\mathcal A_2}$ (canonical preamble row 46). | Five $\Psi$-image rows including the Conway $V^{s\natural}$ row on the metaplectic branch (W20.2 table). | The four siblings parametrise the four strata; each sibling has one image row, and the $\Psi^{\mathrm{metap}}$ sibling hosts two rows (Conway $V^{s\natural}$ and a second metaplectic image). Row count $5 = 4$ siblings with one extra Conway row on the metaplectic branch. | Baily--Borel--Freitag; Duncan 2007. |
| Absolute Kuznetsov HPD blocked on $K3 \times E$ (obstruction from the non-trivial Brauer class on $K3 \times E$). | Relative HPD over $E$ works (the relative $E$-base kills the obstruction by descent). | Obstruction at the absolute level; healing at the relative level. Both statements are proved theorems; relative HPD is the correct home for the $K3 \times E$ Kuznetsov lift. | Kuznetsov 2007; Perry 2019 relative HPD. |
| Pseudo-character framework (Taylor 1991) is sufficient on reduced rings for Galois deformations of $\rho_{\Delta_{10}}$. | Chenevier determinant framework (2014) is necessary on non-reduced rings (where mod-$\ell^n$ Cayley--Hamilton fails for reducible $\rho$). | Compatible hierarchy, not competing frameworks. Taylor's pseudo-character suffices on reduced; Chenevier's determinant is the correct lift to non-reduced. Each dominates in its natural domain; neither refutes the other. Canonical preamble row 53 pins the non-reduced case to Chenevier; reduced-ring calculations may still cite Taylor. | Taylor 1991 *Invent Math* 116; Chenevier 2014 *Ann Inst Fourier* 64. |

**Operating rule.** If you encounter two inscriptions that seem to
contradict, before editing either side **check this table**. If the
pair matches an entry, both are correct. If not, escalate through
Gate 0: the confusion is a candidate for a new compatibility mechanism,
not a candidate for retraction.


---

Scope: Vol II ($A_\infty$ Chiral Algebras and 3D HT QFT). Patterns discovered during Waves 14-24 attack-heal programme.

*Relocated to `notes/` per Manuscript Metadata Hygiene: anti-pattern
catalogues are working-notes scaffolding and do not belong in the
typeset manuscript.*

## Severity levels

| Level    | Meaning                                                    | Action                                 |
| -------- | ---------------------------------------------------------- | -------------------------------------- |
| Critical | Theorem status wrong (conjecture $\to$ theorem) or scope inflation at climax | Immediate fix; audit all instances     |
| High     | Numerical or structural error propagates                   | Fix before next build                  |
| Medium   | Convention clash or ambiguity                              | Fix in current session                 |
| Low      | Cosmetic or cross-reference staleness                      | Fix in batch                           |

## Section 1: Bar-cobar structure and the Swiss-cheese octachotomy

### AP-V2-1: Swiss-cheese octachotomy as colouring
**Severity**: Critical
**Trigger**: Assertion that the eight bar-cobar ambients
(fibrewise / single-monodromy / bi-unipotent / tri-unipotent /
weight-completed / $A_\infty$-corrected / $(\infty,1)$-$\mathrm{Perf}$ /
Kontsevich-formal) are interchangeable or that the octachotomy is a
mere indexing convention.
**Ghost**: Each of the 8 ambients corresponds to a specific
$\mathsf{SC}^{\mathrm{ch,top}}$ colouring stratum on the Swiss-cheese
operadic cover of the boundary-bulk pair; the octachotomy is a
stratification of the coloured operadic cover, not a choice of
formalism.
**Error**: Category error: moving a bar-cobar statement across
ambients (e.g., from bi-unipotent to Kontsevich-formal) requires
crossing a coloured stratum and may incur $\mathrm{grt}_1$-torsor
obstructions that do not appear in any single stratum.
**Correction**: Construction: label each bar-cobar statement with its
ambient $\mathcal A^{(i)}$, $i \in \{1,\dots,8\}$; $\mathsf{SC}^{\mathrm{ch,top}}$
carries a 2-colouring $\mathfrak c: \{e, o\} \to \{1,\dots,8\}$ whose
strata refine Dunn's additive dichotomy. Remark: Pattern 277 is the
local-to-global restatement; each colouring stratum carries its own
adjunction $\Omega^{\mathrm{ch}}_{(i)} \dashv B^{\mathrm{ch}}_{(i)}$
and the crossing maps are non-trivial natural transformations
$\Omega^{\mathrm{ch}}_{(i)} \Rightarrow \Omega^{\mathrm{ch}}_{(j)}$.
**Primary**: Francis--Gaitsgory 2012 *Selecta Math* 18 §2.4 (Ran-space
factorisation stratification); Voronov 1998 *Math Ann* 312
(Swiss-cheese operads); Tamarkin 2003 *Lett Math Phys* 66 (GRT torsor
structure).
**Inscription**: `chapters/theory/sc_chtop_octachotomy.tex`, Thm 2.1
(\texttt{thm:sc-octachotomy-colouring}).
**Cross-ref**: Vol I Pattern 269 (adjunction-strictness conflation);
Vol III AP-CY33 (chain vs rational).

### AP-V2-2: Universal $k$-tower genus formula
**Severity**: High
**Trigger**: Omitting the genus-dependent upper bound
$k_{\max}(g) = g(g+1)/2$ on the Swiss-cheese coloured coherence tower,
or asserting a genus-independent bound.
**Ghost**: The coloured coherence tower on $\overline{\mathcal M_g}$
truncates at height $k_{\max}(g) = g(g+1)/2$, controlled by the rank
of the intersection form on $H^1(\Sigma_g, \mathbb Z)$ via
Mumford--Morita--Miller classes.
**Error**: Claiming chain-level $E_n$-coherences up to arbitrary $n$
at all genera ignores the symplectic rank bottleneck; the higher
coherences simply do not exist above $k_{\max}(g)$.
**Correction**: Construction: for each genus $g$, the Swiss-cheese
coloured coherence tower stabilises at $k_{\max}(g) = g(g+1)/2$;
at $g=0$ trivial, $g=1$ height $1$, $g=2$ height $3$, $g=3$ height
$6$. Remark: matches triangular numbers $T_g$ and equals
$\dim_{\mathbb Q} H^1(\Sigma_g, \mathbb Q)^{\wedge 2} / (\text{image of } \cup)$.
**Primary**: Morita 1989 *Invent Math* 90 (Mumford--Morita--Miller);
Costello--Gwilliam 2021 Vol 2 §7.3 (genus-scaling of BV anomaly);
Hain 1997 *Invent Math* 128 (mapping-class group cohomology).
**Inscription**: `chapters/theory/higher_genus_modular_koszul.tex`,
Prop 4.2 (\texttt{prop:coloured-tower-genus-bound}).
**Cross-ref**: Vol I AP27 (propagator weight); Vol III AP-CY12
(shadow class from full tower).

### AP-V2-3: Codim-4 admissible Heegner quadruple emptiness
**Severity**: High
**Trigger**: Asserting emptiness of admissible Heegner quadruples in
codimension 4 on $\overline{\mathcal A_2}$ by dimensional argument
alone ($\dim = 3$, so codim-4 strata are empty).
**Ghost**: Dimension count gives the correct answer (codim-4 strata
are indeed empty on $\overline{\mathcal A_2}$), but the genuine proof
is arithmetic: Bruinier--Humbert rank obstruction via regularised
theta lift rules out admissible quadruples by $L$-function
non-vanishing at $s=0$.
**Error**: Dimensional argument is insufficient because the stratum
closure locus can exceed ambient dimension under Baily--Borel
compactification; only the arithmetic obstruction rules out
admissible quadruples unconditionally.
**Correction**: Construction: Bruinier 2002 *Lecture Notes 1780*
Thm 5.11 regularised theta-lift non-vanishing + Humbert divisor
arithmetic gives admissibility rank bound; a codim-4 admissible
quadruple would produce an $L$-value of the wrong sign at $s=0$.
Remark: dimensional argument is a heuristic shadow of the arithmetic
content.
**Primary**: Bruinier 2002 *Lecture Notes Math* 1780 §5.3;
Humbert 1899 *Liouville J* 5 Ser 5 (Humbert surfaces);
Borcherds--Katzarkov--Pantev--Shepherd-Barron 1998 *Compositio* 122
(Picard-modular singular weight).
**Inscription**: `chapters/theory/codim4_heegner_emptiness.tex`,
Thm 3.2 (\texttt{thm:codim4-bruinier-humbert}).
**Cross-ref**: Vol III AP-CY42 (pentagon admissibility mod 4).

## Section 2: $(\infty,1)$ and $(\infty,2)$-categorical lifts

### AP-V2-4: Compatibility data canonicality
**Severity**: Critical
**Trigger**: Writing the bar-cobar compatibility homotopy as "chosen"
data or as a choice made by the author, rather than as the image of a
canonical torsor.
**Ghost**: The space of compatibility data is the canonical torsor
$\mathrm{Data}(A) \simeq B\mathrm{Aut}^h_{L_\infty}(\mathfrak g^{\infty,1}_A)$
(the classifying space of $L_\infty$-homotopy automorphisms of the
underlying $(\infty,1)$-algebra), not an arbitrary choice.
**Error**: Headline-vs-full-structure confusion: stating the
compatibility homotopy as "a choice" truncates the higher structure to
the 0-truncation and loses the $L_\infty$-automorphism $(\infty,1)$-group
action that governs deformation theory.
**Correction**: Construction: $\mathrm{Data}(A)$ is an
$(\infty,0)$-groupoid, canonically equivalent to
$B\mathrm{Aut}^h_{L_\infty}(\mathfrak g^{\infty,1}_A)$ where
$\mathfrak g^{\infty,1}_A = \mathrm{Der}^\bullet(A)[1]$ is the tangent
$L_\infty$-algebra. Any two compatibility data are canonically
equivalent through a unique-up-to-contractible $L_\infty$-automorphism.
Remark: the full $(\infty,1)$-structure is essential for the $\mathrm{grt}_1$
action on the bar-cobar GRT-torsor.
**Primary**: Lurie 2017 *Higher Algebra* §5.5.4 (canonical equivalence
in presentable $\infty$-categories); Pridham 2010 *Adv Math* 224
(deformation theory via $L_\infty$); Hinich 1997 *Comm Algebra* 25
(homotopy automorphisms).
**Inscription**: `chapters/theory/compatibility_torsor.tex`, Thm 2.4
(\texttt{thm:compatibility-torsor-canonical}).
**Cross-ref**: Vol I AP8 (canonical-vs-chosen);
Vol III AP-CY30 (factored $\neq$ solved).

### AP-V2-5: $(\infty,2)$-adjunction headline vs 2-morphism content
**Severity**: Critical
**Trigger**: Presenting the bar-cobar $(\infty,2)$-adjunction only via
its unit/counit (1-morphism data) without the Auslander--Reiten
triangular structure on 2-morphisms.
**Ghost**: The $(\infty,2)$-adjunction $\Omega^{\mathrm{ch}} \dashv B^{\mathrm{ch}}$
lives in an $(\infty,2)$-category whose 2-morphisms carry
Auslander--Reiten triangles; the 1-truncation captures only the
headline, losing the triangular Hom-functor structure that encodes
the derived centre.
**Error**: 1-truncation throws away the AR-triangle content; the unit
and counit are 1-morphisms, but the content lies in the 2-morphism
$\mathrm{Hom}$-spaces and their triangular composition.
**Correction**: Construction: state the adjunction in
$\mathrm{Cat}^{(\infty,2)}_{\mathrm{chiral}}$; 2-morphisms form
Auslander--Reiten triangles
$\tau X \to \mathrm{Hom}(X, Y) \to X \oplus Y$
where $\tau$ is the AR translation induced by the chiral Serre
functor. Remark: the 1-truncation is $\mathrm{Cat}^{(\infty,1)}$
and suffices for the adjunction headline; the 2-morphism content is
essential for the derived-centre complementarity theorem (Theorem C).
**Primary**: Gaitsgory--Rozenblyum 2017 *A Study in Derived Algebraic
Geometry I* §I.1.1 ($(\infty,2)$-categories);
Auslander--Reiten 1975 *Comm Algebra* 3 (AR triangles);
Lurie 2009 *$(\infty,2)$-Categories and the Goodwillie Calculus I*.
**Inscription**: `chapters/theory/infty2_adjunction_ar.tex`, Thm 3.1
(\texttt{thm:adjunction-infty2-ar-triangles}).
**Cross-ref**: Vol I AP24 (three-functor conflation); Vol III AP-CY3
($E_2 \neq$ commutative).

## Section 3: Chiral Kontsevich formality

### AP-V2-6: Kontsevich smooth-manifold transport
**Severity**: Critical
**Trigger**: Direct transport of Kontsevich 1997 smooth-manifold
formality across $\overline{\mathcal A_2}$ without restricting to the
Koszul admissible locus $U^{\mathrm{adm}}$.
**Ghost**: Kontsevich formality requires a smooth ambient manifold;
$\overline{\mathcal A_2}$ is stratified with Humbert divisor
singularities, so the direct transport fails. The valid transport
goes through $U^{\mathrm{adm}} \subset \overline{\mathcal A_2}$ via
Francis--Gaitsgory $\infty$-operadic and Tamarkin operadic formality.
**Error**: Smoothness hypothesis violation: $\overline{\mathcal A_2}$
carries codimension-1 Humbert divisors and the symmetric-square
stratum along the hyperelliptic locus; Kontsevich's construction does
not extend to stratified ambients without per-stratum correction.
**Correction**: Construction: restrict chiral formality to
$U^{\mathrm{adm}} = \overline{\mathcal A_2} \setminus
\bigcup_n H_n^{\mathrm{non-adm}}$; on $U^{\mathrm{adm}}$, combine
Francis--Gaitsgory $\infty$-operadic formality with Tamarkin operadic
formality to obtain a quasi-isomorphism
$B^{\mathrm{ch}}(A)|_{U^{\mathrm{adm}}} \simeq \mathrm{Tam}(A)|_{U^{\mathrm{adm}}}$.
Remark: on Humbert divisors, the formality fails with explicit
obstruction class in $H^2_{\mathrm{Kont}}|_{H_n}$.
**Primary**: Kontsevich 1997 *Lett Math Phys* 66 §7 (smooth manifolds
only); Francis--Gaitsgory 2012 *Selecta Math* 18;
Tamarkin 2003 *Lett Math Phys* 66; Willwacher 2015 *Invent Math* 200
(stratified-ambient obstructions).
**Inscription**: `chapters/theory/chiral_kontsevich_formality.tex`,
Thm 4.3 (\texttt{thm:chiral-formality-admissible-locus}).
**Cross-ref**: Vol I AP34 (stratified-ambient scope).

### AP-V2-7: Per-wall vs global Kontsevich obstruction sheaf
**Severity**: High
**Trigger**: Conflating the per-Humbert-divisor obstruction
$\mathrm{ob}^{\mathrm{Kont}}_n$ (local on $H_n$) with the global
pushforward sheaf $\mathrm{ob}^{\mathrm{Kont}}$ on
$\overline{\mathcal A_2}$.
**Ghost**: $\mathrm{ob}^{\mathrm{Kont}}_n$ is a sheaf on the Humbert
divisor $H_n$, cohomology class in $H^2(H_n)$; the global
$\mathrm{ob}^{\mathrm{Kont}} = \bigoplus_n (\iota_n)_* \mathrm{ob}^{\mathrm{Kont}}_n$
on $\overline{\mathcal A_2}$ is the pushforward, cohomology class in
$H^2_{\{H_n\}}(\overline{\mathcal A_2})$.
**Error**: Scope error: writing "the Kontsevich obstruction vanishes"
as a global statement when the vanishing holds only per-wall, or vice
versa, confuses local and global contributions.
**Correction**: Construction: $\mathrm{ob}^{\mathrm{Kont}}_n
\in H^2(H_n, \mathcal N^\vee_{H_n/\overline{\mathcal A_2}})$ (local);
$\mathrm{ob}^{\mathrm{Kont}} = \sum_n (\iota_n)_* \mathrm{ob}^{\mathrm{Kont}}_n
\in H^2_{\{H_n\}}(\overline{\mathcal A_2}, \mathcal N^\vee)$ (global).
Remark: per-wall vanishing does not imply global vanishing; a
residual class in $H^3(\overline{\mathcal A_2})$ can appear via
$E_2^{\mathrm{Leray}}$ spectral sequence.
**Primary**: Hartshorne 1977 *Algebraic Geometry* III.8 (local
cohomology); Willwacher 2015 *Invent Math* 200 §4 (per-wall
obstructions); Bruinier--Funke 2004 *J Reine Angew Math* 570
(regularised theta-lift on Humbert divisors).
**Inscription**: `chapters/theory/chiral_kontsevich_formality.tex`,
Prop 4.7 (\texttt{prop:kont-obstruction-local-vs-global}).
**Cross-ref**: Vol III AP-CY13 (stale Part references, scope error
as cousin).

## Section 4: BD factorisation compatibility

### AP-V2-8: Bi-unipotent pro-ambient vs BD $\mathcal D$-module
**Severity**: Critical
**Trigger**: Asserting the bi-unipotent bar-cobar ambient is merely a
bounded-derived pro-object (e.g., $\mathrm{Pro}(D^b_{\mathrm{coh}})$)
without the genuine BD factorisation-$\mathcal D$-module structure.
**Ghost**: The bi-unipotent ambient carries a genuine
Beilinson--Drinfeld factorisation-$\mathcal D$-module structure on
$\mathrm{Ran}\,X$; the pro-object description is a shadow that loses
the factorisation compatibility and the 1-loop counterterm content.
**Error**: Type error: $\mathrm{Pro}(D^b)$ is a category, not a
$\mathcal D$-module; the factorisation structure
$\Delta_* \mathcal A \simeq \mathcal A \boxtimes \mathcal A$ along
the diagonal is essential and is not captured by the pro-object
description.
**Correction**: Construction: the bi-unipotent ambient is a BD
factorisation $\mathcal D$-module $\mathcal A^{\mathrm{BD}}_{\mathrm{bi-uni}}$
on $\mathrm{Ran}\,X$ with factorisation isomorphism
$\mathcal A^{\mathrm{BD}}_{\mathrm{bi-uni}}|_{\mathrm{Ran}\,X_1 \sqcup \mathrm{Ran}\,X_2}
\simeq \mathcal A^{\mathrm{BD}}_{\mathrm{bi-uni}}|_{\mathrm{Ran}\,X_1}
\boxtimes \mathcal A^{\mathrm{BD}}_{\mathrm{bi-uni}}|_{\mathrm{Ran}\,X_2}$
along disjointness opens. Remark: Costello--Gwilliam 2021 Vol 2
Thm 7.1.1 gives the 1-loop counterterm $= 8$ which verifies the BD
structure (not the pro-object shadow); the specific value $8$ is the
Euler characteristic contribution of the bi-unipotent stratum.
**Primary**: Beilinson--Drinfeld 2004 *Chiral Algebras* Ch 3;
Francis--Gaitsgory 2012 *Selecta Math* 18; Costello--Gwilliam 2021
Vol 2 *Factorization Algebras in Quantum Field Theory* Thm 7.1.1;
Gwilliam 2012 Northwestern thesis.
**Inscription**: `chapters/theory/bi_unipotent_bd_structure.tex`,
Thm 5.2 (\texttt{thm:bi-uni-bd-factorisation}).
**Cross-ref**: Vol I AP165 (B(A) is E_1 coalgebra, not SC);
Vol III AP-CY30 (factored $\neq$ solved).

## Section 5: Theorem H Vol II $\leftrightarrow$ Vol III hinge

### AP-V2-9: Theorem H concentration $d$-independence
**Severity**: Critical
**Trigger**: Asserting chiral Hochschild concentration
$\mathrm{ChirHoch}^\bullet(A) \in \{0,1,2\}$ holds at all dimensions
$d$ of the CY input, without scope qualifier.
**Ghost**: Theorem H concentration $\{0,1,2\}$ is the **ambient-curve
scope** statement (Vol II, $X$ an algebraic curve); on the
$\Phi_d$-enlarged ambient with a CY-$d$ transverse direction, the
concentration enlarges to $\{0,1,2,d\}$ (Vol III, scope for
$d \geq 2$).
**Error**: Scope inflation: the Vol II statement is tight on curves
($d=1$); transporting to CY-$d$ without enlarging to $\{0,1,2,d\}$
misses the transverse direction contribution and gives wrong
Hochschild spectral-sequence page.
**Correction**: Construction: Vol II Theorem H (on curves):
$\mathrm{ChirHoch}^\bullet(A) \in \{0,1,2\}$ for $A$ a chiral algebra
on curve $X$. Vol III enlargement via $\Phi_d$: for $d \geq 2$,
$\mathrm{ChirHoch}^\bullet(\Phi_d(\mathcal C)) \in \{0,1,2,d\}$ where
the extra $d$-entry is the transverse-direction contribution.
Remark: the hinge is the Koszul-locus equivalence
$\mathrm{ChirHoch}^\bullet_{\mathrm{Vol II}}|_{U^{\mathrm{Koszul}}}
\simeq \mathrm{ChirHoch}^\bullet_{\mathrm{Vol III}}|_{U^{\mathrm{Koszul}}}$
which holds on the Koszul locus only.
**Primary**: Francis 2013 *Compositio* 149 §3 (Hochschild
concentration for $E_n$-algebras); Gaitsgory--Lurie 2019 *Weil
Conjecture for Function Fields* Ch 4 (chiral Hochschild); Costello
2011 *Renormalization and Effective Field Theory* §5.
**Inscription**: `chapters/theory/theorem_h_hinge_vol2_vol3.tex`,
Thm 6.1 (\texttt{thm:theorem-h-scope-hinge}).
**Cross-ref**: Vol I Theorem H statement; Vol III AP-CY17 (MF CY
dimension, transverse-direction analogue).

## Section 6: Cyclic chiral homology (Feigin--Tsygan 5th verification path)

### AP-V2-10: Classical Feigin--Tsygan verbatim transport
**Severity**: Critical
**Trigger**: Applying classical Feigin--Tsygan cyclic homology
directly to chiral bialgebras via verbatim transport of the classical
constructions.
**Ghost**: Classical Feigin--Tsygan is built for associative algebras;
chiral bialgebras are non-associative (the chiral product is defined
only on disjoint support), so verbatim transport fails. Five chiral
steps are required for the genuine chiral-cyclic homology.
**Error**: Associativity mismatch: Connes $B$ operator on a chiral
bialgebra requires an $S^1$-action on the bar complex that respects
the factorisation structure; the classical $B$ does not respect
factorisation.
**Correction**: Construction: five-step chiral Feigin--Tsygan: (i)
Francis--Gaitsgory $E_1$-operadic upgrade of the chiral bar complex;
(ii) $S^1$-action providing Connes $B^{\mathrm{ch}}$ on $B^{\mathrm{ch}}(A)$;
(iii) SBI invertibility on $U^{\mathrm{adm}}$ via Kontsevich formality
spectral-sequence collapse at $E_2$-page; (iv) CoHA-to-cyclic matching
through admissible-graph integral
$\int_{\mathrm{Graphs}^{\mathrm{adm}}_n} \omega_{\mathrm{Kont}}$;
(v) explicit Serre-dual numerical evaluation giving
$\chi_3^{\mathrm{ch}} = c(5c+22)/10$-normalised cyclic
characteristic. Remark: the five steps are independently checkable;
each provides a verification path.
**Primary**: Feigin--Tsygan 1987 *K-Theory* 1 (classical cyclic);
Francis--Gaitsgory 2012 *Selecta Math* 18 §5 ($E_1$-operadic upgrade);
Kassel 1987 *J Pure Appl Algebra* 48 (Connes $B$); Kontsevich--Soibelman
2009 arXiv:0606241 (CoHA cyclic structure).
**Inscription**: `chapters/theory/cyclic_chiral_homology.tex`, Thm 7.2
(\texttt{thm:chiral-feigin-tsygan-five-step}).
**Cross-ref**: Vol I AP35--43 (epistemic anti-patterns);
Vol III AP-CY23 ($E_1$ not $E_\infty$ bialgebra).

### AP-V2-11: Three cyclic theories conflation
**Severity**: High
**Trigger**: Conflating any two of: ordinary algebraic cyclic
$\mathrm{HC}^\bullet_{\mathrm{alg}}$, topological
$\mathrm{TC}/\mathrm{TP}$, chiral cyclic $\mathrm{HC}^\bullet_{\mathrm{ch}}$.
**Ghost**: The three theories are distinct and their distinctness is
load-bearing: conflating any two collapses the fifth $\chi_3$
verification path (the one that uses independence of the three).
**Error**: Structural collapse: ordinary $\mathrm{HC}^\bullet_{\mathrm{alg}}$
is $\pi$-exact for DG-algebras; $\mathrm{TC}/\mathrm{TP}$ is defined
on spectra via Bokstedt; chiral $\mathrm{HC}^\bullet_{\mathrm{ch}}$ is
defined on $\mathrm{Ran}\,X$ via factorisation. They agree on
commutative rational input but differ for non-commutative or
non-rational input.
**Correction**: Construction: state for each use which cyclic theory
is invoked; triangulation via all three (direct algebraic / topological
via Bokstedt / chiral via factorisation) gives a fifth $\chi_3$ path
independent of Serre duality. Remark: the three theories fit into a
diagram of natural transformations
$\mathrm{HC}^\bullet_{\mathrm{alg}} \to \mathrm{TC} \to
\mathrm{HC}^\bullet_{\mathrm{ch}}$; each arrow is an equivalence on
the respective semiprime locus but not elsewhere.
**Primary**: Loday 1998 *Cyclic Homology* §4 (algebraic);
Bokstedt--Hsiang--Madsen 1993 *Invent Math* 111 (topological);
Francis 2013 *Compositio* 149 §5 (chiral).
**Inscription**: `chapters/theory/three_cyclic_theories.tex`, Prop 7.5
(\texttt{prop:three-cyclic-distinct}).
**Cross-ref**: Vol I AP152 ("ordered" ambiguity, cousin-collapse).

## Section 7: NC Hodge Mukai--Hochschild

### AP-V2-12: Kaledin degeneration scope
**Severity**: Critical
**Trigger**: Transporting Kaledin 2008 noncommutative Hodge
degeneration from smooth-proper DG-scheme scope to
factorisation-$\infty$-categorical scope on $\overline{\mathcal A_2}$
without checking the Humbert-stratum obstructions.
**Ghost**: Kaledin degeneration holds in smooth-proper DG-scope; on
$\overline{\mathcal A_2}$ the Humbert strata carry non-zero
Heegner--Bruinier obstruction classes that feed into higher-page
$d_r$ of the Hodge-to-de-Rham spectral sequence, so global
degeneration fails.
**Error**: Scope inflation: Kaledin's Cor 5.5 requires the ambient to
be smooth-proper; $\overline{\mathcal A_2}$ is not, and the
Hodge-to-de-Rham $E_2$-page carries non-zero $d_2$ on Humbert divisors.
**Correction**: Construction: Hodge-to-de-Rham degenerates on the
complement $\overline{\mathcal A_2} \setminus \bigcup H_n$;
on Humbert divisors $H_n$, the $d_2$ differential is the
Heegner--Bruinier class
$d_2([\alpha]) = [\alpha] \smile \mathrm{ob}^{\mathrm{HB}}_n$.
Remark: higher-page differentials $d_r$ for $r \geq 3$ can be
non-zero even on the complement, via arithmetic of iterated Humbert
intersections.
**Primary**: Kaledin 2008 *J Pure Appl Algebra* 212 Thm 1.1 (smooth
proper DG); Kaledin 2010 *Ann Inst Fourier* 60 Cor 5.5 (Serre
duality); Bruinier 2002 *Lecture Notes Math* 1780 §5 (Heegner
obstruction).
**Inscription**: `chapters/theory/nc_hodge_mukai_hochschild.tex`,
Thm 8.3 (\texttt{thm:kaledin-scope-humbert}).
**Cross-ref**: Vol III AP-CY1 (CY dim $\neq$ cpx dim).

### AP-V2-13: Mukai--Hochschild pairing triangulation
**Severity**: High
**Trigger**: Computing the Mukai--Hochschild pairing
$\langle[\chi_3], [\chi_3^\vee]\rangle = 2\,\mathrm{Vol}(E)(2\pi i)^3$
by a single-path argument, without independent triangulation.
**Ghost**: The pairing value $2\,\mathrm{Vol}(E)(2\pi i)^3$ is the
correct numerical answer, but its derivation requires triangulation
via three independent paths: (i) Kaledin 2010 Cor 5.5 Serre duality;
(ii) BV Serre-dual cup product; (iii) Siegel--Eisenstein period
cross-check.
**Error**: Single-path insufficiency: the factor
$2\,\mathrm{Vol}(E)$ arises from $\chi_{\mathrm{top}}(E) \cdot \mathrm{Vol}$,
the $(2\pi i)^3$ from degree-$3$ NC Hodge structure; a single path
can produce the correct numeric by chance but fails multi-path
triangulation.
**Correction**: Construction: triangulate via (i) Kaledin 2010
Cor 5.5 applied to $\mathrm{Perf}(E) \times \mathrm{Perf}(K3)$
Serre-dual trace; (ii) BV Serre-dual cup product in
$\mathrm{HH}^\bullet_{\mathrm{BV}}(\mathcal A)$ using
Costello--Gwilliam 2021 Vol 2 Thm 5.2.3; (iii) Siegel--Eisenstein
period cross-check through Pitale--Saha--Schmidt 2014 $L$-value at
$s=0$. All three paths converge on $2\,\mathrm{Vol}(E)(2\pi i)^3$.
Remark: absence of any one path indicates a computation error.
**Primary**: Kaledin 2010 *Ann Inst Fourier* 60 Cor 5.5;
Costello--Gwilliam 2021 Vol 2 *Factorization Algebras* Thm 5.2.3;
Pitale--Saha--Schmidt 2014 *Memoirs AMS* 232 §7;
Shimura 1976 *Comm Pure Appl Math* 29 (Eisenstein periods).
**Inscription**: `chapters/theory/mukai_hochschild_pairing.tex`,
Thm 8.5 (\texttt{thm:mh-pairing-triangulation}).
**Cross-ref**: Vol III AP-CY40 (master $L$-value triangulation).

## Section 8: CY-4 HK-restricted $\Phi_4$

### AP-V2-14: Generic CY-4 $\Phi_4$ existence
**Severity**: Critical
**Trigger**: Asserting that the CY-to-chiral functor $\Phi_4$ exists
on generic CY-4 input without scope restriction.
**Ghost**: $\Phi_4$ existence is BLOCKED on generic CY-4 by
Kapustin--Rozansky--Saulina 3d/4d dichotomy: the Rozansky--Witten
twist producing 3d HT content requires hyperkähler structure on the
CY-4 target (not merely holomorphic symplectic). Scope-restricted
existence on hyperkähler CY-4 via twistor-$S^1$ reduction holds.
**Error**: Scope inflation: Rozansky--Witten produces a 3d B-twist on
hyperkähler targets; generic CY-4 (holomorphic symplectic but not
hyperkähler) lacks the $S^1$-twistor family needed for the reduction.
**Correction**: Construction: $\Phi_4^{\mathrm{HK}}$ defined on
hyperkähler CY-4 via Rozansky--Witten 1997 + twistor-$S^1$ reduction
+ Kapustin--Rozansky--Saulina 2009 3d/4d dichotomy. Generic CY-4
$\Phi_4$ conjectural; hyperkähler scope unconditional.
Remark: hyperkähler CY-4 examples: $K3 \times K3$, $K3^{[2]}$,
generalised Kummer $K_2(A)$.
**Primary**: Rozansky--Witten 1997 *Selecta Math* 3 (3d B-twist);
Kapustin--Rozansky--Saulina 2009 *Nucl Phys B* 823 (3d/4d dichotomy);
Huybrechts 1999 *Invent Math* 135 (hyperkähler topology).
**Inscription**: `chapters/theory/phi4_hk_restricted.tex`, Thm 9.1
(\texttt{thm:phi4-hk-scope}).
**Cross-ref**: Vol III AP-CY6 ($A_X$ at $d=3$, parallel scope).

### AP-V2-15: K3$\times$K3 pairing triangulation
**Severity**: High
**Trigger**: Computing the CY-4 HK-restricted pairing
$\langle \Phi_4(K3_1), \Phi_4(K3_2)\rangle = 4\,\mathrm{Vol}(K3_1)\mathrm{Vol}(K3_2)(2\pi i)^4$
by single-path argument.
**Ghost**: The pairing value is correct but requires triangulation via
three independent paths: (i) Cao--Kool--Monavari DT-4 MacMahon vertex;
(ii) Nekrasov 8d prepotential equivariant localisation;
(iii) Dijkgraaf--Moore--Verlinde--Verlinde 1997 second-quantised
elliptic genus.
**Error**: Single-path insufficiency analogous to AP-V2-13; the
coefficient $4 = 2 \cdot 2$ combines $\chi_{\mathrm{top}}(K3) = 24$
with the hyperkähler double-cover factor.
**Correction**: Construction: triangulate via (i) Cao--Kool--Monavari
2021 *J Differ Geom* 117 DT-4 MacMahon vertex on $K3_1 \times K3_2$;
(ii) Nekrasov 2003 8d prepotential equivariant localisation (genus
$0$ contribution only, by HK-restriction);
(iii) DMVV 1997 *Commun Math Phys* 185 second-quantised elliptic
genus at $K3 \times K3$. All three paths converge on
$4\,\mathrm{Vol}(K3_1)\mathrm{Vol}(K3_2)(2\pi i)^4$. Remark: the
$(2\pi i)^4$ encodes degree-$4$ NC Hodge structure; the $4$
encodes chi-top halving.
**Primary**: Cao--Kool--Monavari 2021 *J Differ Geom* 117 DT-4
MacMahon; Nekrasov 2003 *Adv Theor Math Phys* 7 8d prepotential;
Dijkgraaf--Moore--Verlinde--Verlinde 1997 *Commun Math Phys* 185.
**Inscription**: `chapters/theory/k3k3_pairing_triangulation.tex`,
Thm 9.4 (\texttt{thm:k3k3-pairing-three-path}).
**Cross-ref**: Vol III AP-CY15 (README inflation), AP-CY40 ($L$-value
triangulation).

## Section 9: Plancherel super-quasi-Hopf

### AP-V2-16: Plancherel measure on simples vs projectives
**Severity**: High
**Trigger**: Defining the Plancherel measure on simples $L_\lambda$
of a non-semisimple chiral quantum group, without replacing by
projective covers $P_\lambda$.
**Ghost**: Non-semisimple Kerler--Lyubashenko MTCs force the
Plancherel measure to be supported on projective covers $P_\lambda$,
not simples $L_\lambda$; simples have zero quantum dimension in the
non-semisimple case, so the measure degenerates.
**Error**: Semisimple-only error: in a semisimple MTC, simples equal
their own projective covers; in non-semisimple MTCs (e.g., small
quantum group at root of unity), $P_\lambda \neq L_\lambda$ and
$\dim_q(L_\lambda) = 0$ for non-projective simples.
**Correction**: Construction: $\mu^{\mathrm{Pl}}_{\mathrm{KL}}(\lambda)
= \dim_q(P_\lambda) / \sum_\mu \dim_q(P_\mu)$; for small quantum
group at root of unity, this gives a non-degenerate measure on
$\{P_\lambda\}$. Remark: Kerler--Lyubashenko modified trace
$\mathrm{tr}^{\mathrm{mod}}_{P_\lambda}$ encodes the projective
measure.
**Primary**: Kerler--Lyubashenko 2001 *Non-Semisimple Topological
Quantum Field Theories for 3-Manifolds with Corners* (projective covers);
Geer--Kujawa--Patureau-Mirand 2018 *Selecta Math* 24 (modified trace);
Costantino--Geer--Patureau-Mirand 2014 *Quantum Topol* 5.
**Inscription**: `chapters/theory/plancherel_superquasihopf.tex`,
Thm 10.1 (\texttt{thm:plancherel-projective}).
**Cross-ref**: Vol III AP-CY37 (non-semisimple tilting MTC).

### AP-V2-17: Convergence mode
**Severity**: High
**Trigger**: Claiming the Plancherel decomposition
$\mathbbm 1 = \sum_\lambda \mu^{\mathrm{Pl}}(\lambda)\,\Pi_\lambda$
converges in norm or weak-$*$ sense.
**Ghost**: The convergence is Mittag--Leffler pro-stabilisation in
$\mathrm{Pro}(\mathrm{Mod}_H)$ (category of pro-objects), not norm or
weak-$*$; the pro-structure is essential for infinite-dimensional
chiral representations.
**Error**: Topological-convergence error: for infinite-dimensional
chiral representations, norm convergence is not available
(chiral-module norms do not exist canonically) and weak-$*$ requires
a dual pairing that the chiral category does not carry.
**Correction**: Construction: the Plancherel decomposition converges
as a pro-object limit
$\mathbbm 1 = \lim_{N \to \infty} \sum_{\lambda : |\lambda| \leq N}
\mu^{\mathrm{Pl}}(\lambda)\,\Pi_\lambda$ in $\mathrm{Pro}(\mathrm{Mod}_H)$
with Mittag--Leffler stability. Remark: Mittag--Leffler stabilisation
holds because the truncated sums are eventually constant in
$\mathrm{Pro}$ on any compactly-supported object.
**Primary**: Artin--Mazur 1969 *Etale Homotopy* (pro-objects);
Beilinson 1986 *K-Theory* 2 (pro-$\mathcal D$-modules);
Lurie 2017 *Higher Algebra* §6 (pro-categories).
**Inscription**: `chapters/theory/plancherel_convergence.tex`,
Prop 10.3 (\texttt{prop:plancherel-pro-ml}).
**Cross-ref**: Vol I AP142 (pro-object discipline); Vol III AP-CY33
(chain-level pro-structure).

### AP-V2-18: MO-extension super-quasi-Hopf via dynamical twist
**Severity**: Medium
**Trigger**: Attempting to extend the Maulik--Okounkov construction
to the super-quasi-Hopf setting without the Etingof--Kazhdan
dynamical twist.
**Ghost**: The MO-extension goes through Etingof--Kazhdan dynamical
twist $\partial_Z \log \Phi_{10}$ where $\Phi_{10}$ is the Igusa cusp
form; this specific twist is the unique $H^2$-rigidity class (up to
gauge).
**Error**: Non-canonical choice error: a generic dynamical twist
would break super-quasi-Hopf associativity; the EK-twist
$\partial_Z \log \Phi_{10}$ is uniquely determined (up to gauge) by
$H^2$-rigidity of the super-quasi-Hopf deformation.
**Correction**: Construction: EK dynamical twist $J(Z) = \exp(\hbar
\partial_Z \log \Phi_{10}(Z))$ where $Z \in \mathbb H_2$ Siegel upper
half-space; the twist satisfies the dynamical pentagon
equation and realises the unique $H^2$-rigidity class on super-quasi-Hopf
deformations. Remark: $H^2$-rigidity follows from
$\dim H^2(\mathfrak g; \mathfrak g^\vee) = 1$ with generator
$\partial_Z \log \Phi_{10}$.
**Primary**: Etingof--Kazhdan 1996 *Selecta Math* 2 (dynamical
twist); Maulik--Okounkov 2012 arXiv:1211.1287 (MO geometric
R-matrix); Gritsenko--Nikulin 1998 *Invent Math* 129 ($\Phi_{10}$
Igusa form).
**Inscription**: `chapters/theory/mo_superquasihopf.tex`, Thm 10.6
(\texttt{thm:mo-ek-dynamical}).
**Cross-ref**: Vol III AP-CY39 ($\Phi_{10}$ automorphic home).

## Section 10: Universal ratio-of-levels and three-faces identity

### AP-V2-19: Universal ratio-of-levels scope
**Severity**: High
**Trigger**: Asserting the universal ratio-of-levels identity
$\ell_X/\ell_Y = c_+(L_X)/c_+(L_Y)$ holds uniformly across all Mukai
lattice data, including the Leech--Conway row.
**Ghost**: The universal ratio ties Lusztig-level quantisation $\ell$
to Mukai-signature data $c_+$; the identity holds for the four
Gritsenko--Nikulin reflective rows plus the $24A_1$ Niemeier row, but
**breaks for Leech--Conway** (no Fricke involution on the positive-definite
Leech lattice).
**Error**: Scope inflation: the identity requires a Fricke involution
to compare $c_+(L_X)$ across rows; Leech (positive-definite) and
Conway $V^{s\natural}$ (super-lattice) do not admit Fricke involutions,
so the ratio is undefined.
**Correction**: Construction: universal ratio
$\ell_X/\ell_Y = c_+(L_X)/c_+(L_Y)$ holds for rows
$\{\mathrm{II}_{2,2}, \mathrm{II}_{10,2}, \mathrm{II}_{18,2}, \mathrm{II}_{26,2}\}$
(reflective Lorentzian, Fricke-involution available) plus $24A_1$
Niemeier. Fails on Leech row (no Fricke). Remark: the failure is
structural, not an error; it distinguishes reflective from
positive-definite data.
**Primary**: Lusztig 1990 *Geom Dedicata* 35 (levels); Mukai 1988
*Nagoya Math J* 116 (Mukai vector); Borcherds 1992 *Invent Math* 109
(Fricke involution on reflective lattices); Scheithauer 2017
*Commun Math Phys* 350.
**Inscription**: `chapters/theory/universal_ratio_levels.tex`,
Thm 11.1 (\texttt{thm:universal-ratio-levels-scope}).
**Cross-ref**: Vol III AP-CY34 (Conway $V^{s\natural}$ scope).

### AP-V2-20: Three-faces universal identity undercounting
**Severity**: Critical
**Trigger**: Treating any of the three faces (Vol I conductor $K$,
Vol II one-loop Quillen exponent, Vol III Borcherds weight) of the
universal identity $\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = -1$ in
isolation.
**Ghost**: The three faces are three independent cross-volume
realisations of the **same** universal identity; at the distinguished
point $(K, \hbar^2) = (8, -1/8)$ all three reconcile on
$\hbar^2 K^{\kappa_{\mathrm{ch}}} = -1$, and any isolated-face
treatment is structural undercounting.
**Error**: Triangulation failure: treating only the Vol II face
loses the Vol I conductor arithmetic and the Vol III Borcherds weight
content; all three are needed for multi-path verification.
**Correction**: Construction: state the identity with all three faces
named: (a) Vol I conductor face $K = \mathrm{cond}(A)$, chiral algebra
$A$; (b) Vol II one-loop Quillen exponent
$\hbar^2 = \exp(2\pi i \cdot Q_{\mathrm{Quillen}})$;
(c) Vol III Borcherds weight $\kappa_{\mathrm{ch}} = \mathrm{wt}_{\mathrm{Borch}}(\Phi)$.
Distinguished point $(K, \hbar^2) = (8, -1/8)$:
$\hbar^2 \cdot K^{\kappa_{\mathrm{ch}}} = (-1/8) \cdot 8^{\kappa_{\mathrm{ch}}} = -1$
forces $\kappa_{\mathrm{ch}} = 1$ on the distinguished stratum.
Remark: the three faces are pairwise independent; their mutual
constraint determines $(K, \hbar^2, \kappa_{\mathrm{ch}})$ uniquely
on each reflective row.
**Primary**: Borcherds 1992 *Invent Math* 109 (Borcherds weight);
Quillen 1985 *Invent Math* 82 (one-loop determinant);
Scheithauer 2006 *Commun Math Phys* 266 (conductor).
**Inscription**: `chapters/theory/three_faces_universal.tex`, Thm 11.4
(\texttt{thm:three-faces-identity}).
**Cross-ref**: Vol I AP151 ($\hbar$ convention); Vol III AP-Vol-III-prop-1
(bare $\kappa$).

## Section 11: Chain-level vs cohomological

### AP-V2-21: Class M $E_3$-bar dimensionality
**Severity**: High
**Trigger**: Asserting the class-M $E_3$-bar cohomology is
infinite-dimensional at all lanes, or equivalently, claiming it is
$6^g$ at chain level.
**Ghost**: Class M $E_3$-bar cohomology is $6^g$ at the
**cohomological** level (finite, controlled by Euler-characteristic data
of $E_3$ to the power $g$), and **infinite-dimensional** at the
**chain** level (because the differential is not rationally exact);
mixing the lanes gives wrong genus-scaling.
**Error**: Lane conflation: Vol III AP-CY21 notes that $E_3$-bar for
class M is infinite-dimensional at chain level because $d_4$ survives;
at cohomological level, $d_4$ kills everything except a finite
$6^g$-dimensional quotient by the universal class-M coherence
spectral sequence collapse.
**Correction**: Construction: class M $E_3$-bar at chain level:
infinite-dimensional (Pattern 236 chain-level scope); at cohomological
level: $6^g$-dimensional. Remark: $6$ is the Euler-characteristic-weighted
$E_3$ contribution on a class-M generator with sign discipline;
$6^g$ matches the genus-$g$ tensor power structure.
**Primary**: Francis 2013 *Compositio* 149 §4 (chain vs cohomological
for $E_n$); Costello--Gwilliam 2021 Vol 2 §9 (BV chain vs
cohomological).
**Inscription**: `chapters/theory/class_m_e3_bar.tex`, Thm 12.1
(\texttt{thm:class-m-e3-bar-lane}).
**Cross-ref**: Vol III AP-CY21 ($E_3$ bar class M); Vol I AP33 (chain
vs rational).

## Section 12: Five-archetype landscape cross-volume

### AP-V2-22: Four-archetype vs five-archetype landscape
**Severity**: Critical
**Trigger**: Treating the G/L/C/M four-archetype landscape as
exhaustive of the $\kappa + \kappa^! \in \{0, 13, 250/3, 98/3\}$
complementarity table.
**Ghost**: The four-archetype classification extends to **five
archetypes** G/L/C/M/**B** via a BKM-crown row B at $\kappa + \kappa^! = 8$;
the B-row is populated by Borcherds--Kac--Moody algebras ($\Phi_{12}$
fake-Monster; $\Phi_{10}$ Igusa) and extends the Virasoro-ended
classification by one reflective row.
**Error**: Cross-volume scope inflation: the four-archetype table is
scoped to Vol I's standard landscape; the BKM crown row B appears
**only** when Vol III's CY-to-chiral functor $\Phi$ imports
Borcherds-product data, enlarging the complementarity table. Treating
four as exhaustive misses the crown content and undercounts by one
row.
**Correction**: Construction: extended complementarity table
$\kappa + \kappa^! \in \{0, 8, 13, 250/3, 98/3\}$ over five
archetypes G ($= 0$, Heisenberg), B ($= 8$, BKM crown), L
($= 13$, affine Kac--Moody), C ($= 98/3$, $\beta\gamma$), M
($= 250/3$, Virasoro) **[RETRACTED AP5 per W25.C6 cross-volume audit
2026-04-20: the per-row assignment L = 13 / C = 98/3 / M = 250/3 is
WRONG relative to Vol I `chapters/examples/landscape_census.tex` L1576-
1579 canonical: $\kappa(\widehat{\fg}_k) + \kappa(\widehat{\fg}_k^!) = 0$,
$\kappa(\beta\gamma_\lambda) + \kappa((\beta\gamma_\lambda)^!) = 0$,
$\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_c^!) = 13$; the values
$250/3$ and $98/3$ are W-extensions on the M-row
($\mathsf{M}$-ext $\mathcal{W}_3^k$ and $\mathrm{BP}_k$ per
landscape\_census.tex L1756, L1758), NOT the native L/C/M assignments.
Canonical per-row: G = 0 ($r_{\max} = 2$), L = 0 ($r_{\max} = 3$),
C = 0 ($r_{\max} = 4$), M = 13 ($r_{\max} = \infty$), B = 8
($r_{\max} = \infty$); $\mathsf{M}$-ext values $250/3, 98/3$ sit on
the M-row via principal-W and minimal-W specialisations. See Vol I
AP357 L1316-1327 + Vol II `first_principles_cache_comprehensive.md`
L3207-3211 for the correct per-row table.]** Remark: the B-row is
Vol II's contribution to the cross-volume synthesis; its value $8$
matches the Costello--Gwilliam 1-loop counterterm of AP-V2-8 and the
$(K, \hbar^2) = (8, -1/8)$ distinguished point of AP-V2-20.
**Primary**: Borcherds 1992 *Invent Math* 109 (BKM algebras);
Gritsenko--Nikulin 1998 *Invent Math* 129 ($\Phi_{10}$ Igusa);
Scheithauer 2017 *Commun Math Phys* 350 (reflective crown);
Costello--Gwilliam 2021 Vol 2 §7 (1-loop value).
**Inscription**: `chapters/theory/five_archetype_bkm_crown.tex`,
Thm 13.2 (\texttt{thm:five-archetype-landscape}).
**Cross-ref**: Vol I Theorem C (derived-centre complementarity);
Vol III AP-CY8 (Borcherds $\neq$ bar Euler), AP-Vol-III-prop-2
($N=1$ coincidence inflation).

## Statistics

| Category                                              | Count |
| ----------------------------------------------------- | ----: |
| Bar-cobar structure (AP-V2-1--3)                      |     3 |
| $(\infty,1)/(\infty,2)$-categorical (AP-V2-4--5)      |     2 |
| Chiral Kontsevich formality (AP-V2-6--7)              |     2 |
| BD factorisation compatibility (AP-V2-8)              |     1 |
| Theorem H Vol II $\leftrightarrow$ Vol III (AP-V2-9)  |     1 |
| Cyclic chiral homology (AP-V2-10--11)                 |     2 |
| NC Hodge Mukai--Hochschild (AP-V2-12--13)             |     2 |
| CY-4 HK-restricted $\Phi_4$ (AP-V2-14--15)            |     2 |
| Plancherel super-quasi-Hopf (AP-V2-16--18)            |     3 |
| Universal ratio and three-faces (AP-V2-19--20)        |     2 |
| Chain-level vs cohomological (AP-V2-21)               |     1 |
| Five-archetype landscape (AP-V2-22)                   |     1 |
| **Total catalogued (Wave 20-24)**                     |  **22** |
| Critical severity                                     |    10 |
| High severity                                         |    11 |
| Medium severity                                       |     1 |
| Low severity                                          |     0 |

Three Wave-20-24 anti-patterns have already driven 5+ independent
fixes across the Vol II chapter corpus: AP-V2-1 (Swiss-cheese
octachotomy, 7 fixes across `sc_chtop_octachotomy.tex` +
`heptagon_edge_34_*.tex` + downstream cross-references); AP-V2-9
(Theorem H scope hinge, 6 fixes reconciling Vol II/Vol III ambient
statements); AP-V2-22 (five-archetype B-row, 5 fixes enlarging the
complementarity table across `chiral_center_theorem.tex` and
cross-volume references).

---

## Historical K3-BKM / 3d HT-QFT anti-patterns (Waves 14-22, Vol II frame)

- **V2-AP56 -- $(c_{4d}, c_{2d})$ central-charge reversal (Critical).**
  Wave-14 retraction to $(26, -312)$ fails $\mathrm{SU}(2)$ $N_f = 4$
  cross-check. Canonical $(107/6, -214)$ at $n = 24$ via $(5n-13)/6$;
  WOV-2 locks.
- **V2-AP57 -- Monster vs Fake-Monster rank (Critical).**
  Monster rank 2 ($\mathrm{II}_{1,1}$), Fake-Monster rank 26
  ($\mathrm{II}_{25,1}$), K3-BKM rank 3 ($\Lambda^{2,1}_{II}$).
- **V2-AP58 -- $c_3$ normalisation (High).**
  Bruinier reduced-class: $c_3 = -8$. Conversion factor $-22032$ to
  Gritsenko--Nikulin Cartan-matrix convention.
- **V2-AP59 -- Umbral Niemeier labelling (High).**
  $(N-1) \mid 24$ for $A_{N-1}$ umbral; $N = 6$ reanchored to $6D_4$.
- **V2-AP60 -- $\zeta(3,3,3,3)$ value (High).**
  $0.000295999\ldots$, not $0.0028565$. Depth-4 MZV at weight 12.
- **V2-AP61 -- $c(1,2,\pm 2) = -2$ (High).**
  Integer heterotic lift; sign-flip corrected via three-path
  cross-check.
- **V2-AP62 -- $H_4$ vs $H_8$ (High).**
  $H_4$ is $(2,2)$-isogeny with $\mathrm{End} \supset \mathbb{Z}[2i]$.
- **V2-AP63 -- Theorem B scope (Medium).**
  Exclude all admissible $H_n$, not just $H_1 \cup H_4$.
- **V2-AP64 -- Borcherds vs Gritsenko weight (Medium).**
  K3-BKM denominator $\Delta_5$ (Grit additive), not $\Phi_{12}$
  (Borch multiplicative).
- **V2-AP65 -- Two-$\hbar$ (High).**
  $\hbar^{\mathrm{Drinfeld}} \ne \hbar^{\mathrm{BV}}$ semantically.
  Name the $\hbar$ at every site.
- **V2-AP66 -- Sylvester vs Feingold--Frenkel (Medium).**
  Use eigenvalue signature $\{+4, +4, -2\}$, not Sylvester
  $(2, 0, -32)$ trap.
- **V2-AP67 -- Schmidt parameter pair (Medium).**
  $(17/2, 15/2)$ for $\Delta_{10}$; $(7/2, 5/2) \otimes \mathrm{sgn}_\mathbb{R}$
  for $\Delta_5$ Maass-spin cover.
- **V2-AP68 -- CoHA $\ne$ chiral (Critical).**
  $\mathbf{H}_{\Delta_5} = \Phi_3(\mathcal{D}_\hbar(\mathcal{Y}^{\mathrm{Hall}}(\mathrm{CoHA})))$.
- **V2-AP69 -- $\kappa_\bullet$ Künneth (High).**
  $\kappa_{\mathrm{cat}}(K3 \times E) = 0$ (multiplicative), not 2.


---

## V2-AP1 through V2-AP20: E_1/E_inf Locality Hierarchy (re-extracted 2026-04-21)

The canonical Vol II register of locality and pole-structure anti-patterns,
re-extracted from the E_1/E_inf Locality Hierarchy section of the legacy
CLAUDE.md. These were the scrub-cascade casualty identified in V2-AP51.

**Canonical statement.** $E_1$ vs $E_\infty$ is about LOCALITY, not poles.
$E_\infty$ = LOCAL = $\Sigma_n$-equivariant; $E_1$ = NONLOCAL. OPE poles
are compatible with $E_\infty$. Three-tier picture WITHIN $E_\infty$:
(i) pole-free ($R = \tau$, e.g. BD "commutative chiral algebra" — STRICT
SUBCLASS of $E_\infty$); (ii) VA with poles ($R \ne \tau$ but DERIVED
from local OPE); (iii) genuinely $E_1$ ($R \ne \tau$, independent input).
Tiers (i)+(ii) BOTH $E_\infty$. **Kac--Moody, Virasoro, Heisenberg, $W$-algebras
are ALL $E_\infty$** — poles do not break $E_\infty$. Discriminant
$E_1$ vs $E_\infty$ is PROVENANCE of $R(z)$, not its value. BD do NOT study $E_1$.
$E_1$-chiral algebra is a NEW concept of THIS manuscript.

- **V2-AP1**: $E_\infty$-chiral INCLUDES ALL vertex algebras. KM, Virasoro,
  Heisenberg are ALL $E_\infty$-chiral. NEVER write "VAs are not
  $E_\infty$-chiral."
- **V2-AP2**: $R(z) \ne \tau$ does NOT imply genuinely $E_1$-chiral. For
  $E_\infty$ with poles, $R(z)$ is derived from local OPE; for $E_1$-chiral,
  $R(z)$ is independent input. Discriminant is PROVENANCE, not value.
- **V2-AP3**: Three bars: $B^{FG}$ (zeroth pole only) $\ne B^\Sigma$ (all poles
  $+$ coinvariants) $\ne B^{\mathrm{ord}}$ (all poles $+$ ordering).
  Maps: $B^{\mathrm{ord}} \to B^\Sigma$ (coinvariants);
  $\mathrm{gr}(B^\Sigma) \to B^{FG}$ (filtration).
- **V2-AP4**: Ordered-to-unordered descent is $R$-matrix twisted:
  $B^\Sigma_n = (B^{\mathrm{ord}}_n)^{R\text{-}\Sigma_n}$.
  Naive quotient only for pole-free.
- **V2-AP5**: NEVER equate $E_\infty$-chiral with "no OPE poles." BD
  "commutative chiral algebra" (no poles) is a STRICT SUBCLASS of
  $E_\infty$-chiral.
- **V2-AP6**: BD do NOT study $E_1$. $E_1$-chiral algebra = NEW concept
  of THIS manuscript.
- **V2-AP7**: Heisenberg $R$-matrix $= \exp(k \hbar / z)$, NOT trivial.
  Collision residue $k/z$. Monodromy $\exp(-2\pi i k)$.
- **V2-AP8**: NEVER add restrictive parenthetical glosses. "$E_\infty$-chiral
  ($=$ BD commutative $=$ no poles)" NARROWS the term.
- **V2-AP9**: NEVER say VA "is not $E_\infty$-chiral." KM, Virasoro,
  Heisenberg, $W$-algebras are ALL $E_\infty$-chiral. Poles do not break
  $E_\infty$-chirality.
- **V2-AP10**: NEVER "$E_\infty$-chiral implies $R(z) = \tau$" without
  pole-free qualifier. Correct: "For POLE-FREE $E_\infty$-chiral, $R(z) = \tau$."
- **V2-AP11**: NEVER conflate $E_\infty$-chiral with BD "commutative."
  BD Chapter 4 "commutative" = pole-free = strict subclass.
- **V2-AP12**: $E_1$- vs $E_\infty$-chiral is about LOCALITY, not poles.
- **V2-AP13**: NEVER trust agent claim "VAs are not $E_\infty$-chiral."
  This exact error caused cascading damage.
- **V2-AP14**: NEVER oscillate between conventions in single session.
- **V2-AP15**: NEVER edit $E_1$/$E_\infty$ language without author confirmation.
- **V2-AP16**: Three-tier picture is WITHIN $E_\infty$-chiral, not a
  division between $E_\infty$-chiral and $E_1$-chiral. (i) + (ii) both
  $E_\infty$-chiral. Only (iii) is $E_1$-chiral.
- **V2-AP17**: NEVER revert file based on false premise. Surgical removal only.
- **V2-AP18**: Author's explicit statements override agent literature searches.
- **V2-AP19**: NEVER batch-propagate unverified corrections. ONE edit,
  verify, THEN propagate.
- **V2-AP20**: NEVER add "in the sense of [reference]" without verification.

---

## V2-AP21 through V2-AP48: legacy extension (re-extracted 2026-04-21)

Continuation of the legacy V2-AP register re-extracted from
`notes/claude_md_legacy_20260418.md` and
`~/chiral-bar-cobar/notes/cross_volume_aps.md`.

### Section L.3: Hierarchy and chromatic (V2-AP21--V2-AP24)

- **V2-AP21**: PVA $\ne$ $P_\infty$-chiral. PVA is the CLASSICAL
  shadow (descend to cohomology); $P_\infty$-chiral is the HOMOTOPY
  intermediate. Opposite directions.
- **V2-AP22**: Full hierarchy: commutative associative $\subset$ PVA
  $\subset$ $E_\infty$-chiral $\subset$ $P_\infty$-chiral $\subset$
  $E_1$-chiral. Bar/Koszul at the $E_\infty$ and $E_1$ levels only.
- **V2-AP23**: Chromatic: the classical theory is height $0$.
  $L_{K(n)}(B(A)) = 0$ for $n \ge 1$. Pole order $\ne$ chromatic
  height.
- **V2-AP24**: $S$-transform (closed, complex structure) $\ne$
  Wick rotation of $R$ (open, $E_1$ ordering). Different algebraic
  data.

### Section L.4: Empirical anti-patterns from error archaeology (V2-AP25--V2-AP39)

- **V2-AP25**: Complex-analytic sign. $\mathrm{Im}(f) = (f - \bar f)
  / (2 i)$; $\bar\partial \,\mathrm{Im}(f) = (i/2) \bar\partial \bar f$,
  NOT $1 / (2 i)$. Identity $-1 / (2 i) = i / 2$ is a common
  confusion. Verify at EACH propagation site.
- **V2-AP26**: NEVER hardcode Part/chapter numbers. Always
  `\ref{part:...}`. 24+ stale refs after $10 \to 7$ Part
  restructuring.
- **V2-AP27**: Duplicated content across files FORBIDDEN. Use
  `\input{}` or `\ref{}`, never copy-paste theorem environments.
- **V2-AP28**: Test expected values from 2+ independent sources with
  documented derivation. Engine and test from the same mental model
  share the same error. $\lambda_3 = 1/82944$ was WRONG (correct:
  $31/967680$) because both used the same faulty computation.
- **V2-AP29**: AI-slop cleanup mandatory post-generation. Grep for:
  moreover, additionally, notably, crucially, remarkably, "it is
  worth noting", em dashes, "We now", passive "can be shown."
- **V2-AP30**: After architecture restructuring: grep
  `Part~[IVXL]` in `chapters/`; also `\ref{part:` to verify targets.
- **V2-AP31**: AP4 at write time. Before `\begin{proof}`, verify the
  preceding environment is theorem/proposition/lemma with
  `\ClaimStatusProvedHere`. If conjecture: use
  `\begin{remark}[Evidence]` instead. 25-instance fix commit.
- **V2-AP32**: Standalone-document artifact leak. Chapter files
  `\input`'d into `main.tex` MUST NOT contain `\title{}`,
  `\begin{abstract}`, `\tableofcontents`, `\date{}`, `\author{}`.
- **V2-AP33**: `RECTIFICATION-FLAG` must NOT become permanent debt.
  Zero tolerance for unresolved flags at session end.
- **V2-AP34**: Divided-power convention in $\lambda$-brackets. Vol II
  uses $\{T_\lambda T\} = (c / 12) \lambda^3$ (divided power). OPE
  mode $T_{(3)} T = c/2 \mapsto (c/2)/3! = c/12$. Grep
  `c/2.*lambda^3`; if found, almost certainly wrong (should be
  $c/12$). $\mathcal W_3$: $c/3 \cdot \lambda^5$ wrong; correct
  $c/360$.
- **V2-AP35**: Unresolved logical connectives after correction.
  Audit all "therefore"/"hence"/"it follows" within 5 lines.
- **V2-AP36**: Terminology rename atomicity. Enumerate all variant
  forms; grep all three volumes; complete replacements in a SINGLE
  commit. "shadow Postnikov tower" $\to$ "shadow obstruction tower"
  needed 5 commits.
- **V2-AP37**: Arakelov form canonical normalisation.
  $\omega_1 = (i / (2 \,\mathrm{Im}\,\tau)) dz \wedge d\bar z$
  (integral $= +1$);
  $\omega_{\mathrm{Ar}} = -(\pi / \mathrm{Im}\,\tau) dz \wedge d\bar z$
  (integral $= -1$); $\omega_1 = -\omega_{\mathrm{Ar}} / (2\pi)$.
  Same error fixed THREE times.
- **V2-AP38**: Phantom label retirement. After chapter migration,
  366 phantoms across 2 commits after Vol I $\to$ Vol II migration.
- **V2-AP39**: Macro portability after migration. After migrating
  Vol I $\to$ Vol II: compile; grep "Undefined control sequence";
  add `\providecommand` for each. 7 macros across 2 commits.

### Section L.5: Wave-17-19 synthesis legacy (V2-AP40--V2-AP48)

- **V2-AP40**: NO anti-pattern tags or metadata leakage into the
  typeset manuscript. AP identifiers, FM identifiers, session codes,
  commit hashes, meta-stamps, visible-label leaks, session dates
  in body prose MUST NOT appear in any `.tex` file compiled into
  the monograph PDF or standalone paper PDF. Six subclauses:
  V2-AP40a (bibkey), V2-AP40b (label), V2-AP40c (index/hyperref),
  V2-AP40d (environment/section title), V2-AP40e (monospace
  filename), V2-AP40f (math-mode label leak).
- **V2-AP41**: Internal theorem-statement-vs-proof formula
  inconsistency. A main theorem states one formula; the immediate
  proof cites a different formula diverging at boundary cases.
  Example: $\beta_{W_N} = (N+1)(N+2)/2$ stated, Stirling-dominance
  proof cites $\beta_N = 12(H_N - 1)$; agree at $N = 2, 3$;
  diverge $N \ge 4$.
- **V2-AP42**: $(\infty, 2)$-adjunction bar-cobar. 1-truncation does
  NOT capture Auslander--Reiten triangular structure on
  compatibility 2-morphisms. Specify $(\infty, 1)$ or
  $(\infty, 2)$; never elide 2-morphism coherence.
- **V2-AP43**: Chiral Kontsevich formality fails on stratified
  $\overline{\mathcal A_2}$. Francis--Gaitsgory $+$ Tamarkin
  transport holds ONLY on Koszul locus $U^{\mathrm{adm}}$; Humbert
  strata are OBSTRUCTED. Name the ambient and the locus at every
  invocation.
- **V2-AP44**: Swiss-cheese colouring is an OCTACHOTOMY. Eight
  bar-cobar ambients correspond to eight specific
  $\mathsf{SC}^{\mathrm{ch,top}}$ colourings; treating them as
  interchangeable is a category error.
- **V2-AP45**: CY-4 HK-restricted $\Phi_4$. Generic CY-4 $\Phi_4$
  BLOCKED by Kapustin--Rozansky--Saulina 3d/4d dichotomy;
  scope-restricted to hyperkähler CY-4 via twistor-$S^1$ reduction.
- **V2-AP46**: Francis--Gaitsgory cyclic chiral homology needs
  $E_1$-operadic ambient upgrade; classical Feigin--Tsygan verbatim
  transport is a FIVE-STEP FAILURE.
- **V2-AP47**: NC Hodge Kaledin degeneration scope. Smooth-proper DG
  scope $\ne$ factorisation $\infty$-category scope; Humbert strata
  carry non-zero Heegner--Bruinier obstruction classes feeding
  higher-page $d_r$.
- **V2-AP48**: Theorem H hinge enlarges under $\Phi_d$. Ambient-curve
  $\mathrm{ChirHoch}$ concentration $\{0, 1, 2\}$ ENLARGES to
  $\{0, 1, 2, d\}$ under $\Phi_d$.

---

## Waves 1-13 pre-synthesis anti-patterns (V2-AP100--V2-AP125)

Distilled from the Vol II pre-Wave-14 programme record: SC foundations,
Dimofte integration, Swiss-cheese / seven faces, and the 3D QG climax.
Numbering is disjoint from `V2-AP1--V2-AP48` and `AP-V2-1--AP-V2-22`.

### Section W.1: $\mathsf{SC}^{\mathrm{ch,top}}$ foundations (V2-AP100--V2-AP105)

- **V2-AP100**: $\mathsf{SC}^{\mathrm{ch,top}}$ is a TWO-COLOURED
  dioperad with directional restriction (closed output cannot
  receive open input). Dunn additivity does NOT apply; the correct
  promotion is through Voronov's degeneration plus the
  product-forced locality hypothesis, NOT Dunn.
- **V2-AP101**: $B(A)$ is an $E_1$ COASSOCIATIVE coalgebra, NOT a
  $\mathsf{SC}^{\mathrm{ch,top}}$-coalgebra (cf. Vol I AP165). The
  $\mathsf{SC}$ structure emerges in the DERIVED CENTRE PAIR
  $(C^\bullet_{\mathrm{ch}}(A, A), A)$, not on $B(A)$.
- **V2-AP102**: Bar differential on the curve is HOLOMORPHIC
  FACTORISATION; coproduct on $\mathbb R$ is TOPOLOGICAL
  FACTORISATION. The $\mathsf{SC}^{\mathrm{ch,top}}$ datum is the
  pairing over $C \times \mathbb R$. Conflation collapses
  bulk-boundary.
- **V2-AP103**: Homotopy retract is DATA. Chain homotopy,
  Mittag--Leffler witness, or explicit MC element must be named;
  disc $\ne$ point, $\mathbb P^1 \ne \mathbb A^1$ (cf. Vol I
  AP142 / B53 / FM23).
- **V2-AP104**: Costello--Gwilliam bar differential $\ne$ chiral
  bar differential verbatim. CG's holomorphic factorisation
  framework provides the AMBIENT; the chiral bar differential is
  constructed via explicit OPE poles on the curve.
- **V2-AP105**: $E_{k+2}^{\mathrm{top}}$ topologisation ladder
  requires conformal vector at NON-CRITICAL level. Affine KM
  reaches $E_3^{\mathrm{top}}$ (PROVED; cf. Vol I
  AP167 / B59 / FM28); general chiral-with-conformal is
  CONJECTURAL. $\mathcal W_N$ reaches $E_{N+1}^{\mathrm{top}}$;
  $\mathcal W_\infty$ is the Platonic endpoint.

### Section W.2: Dimofte integration and Drinfeld double (V2-AP106--V2-AP112)

- **V2-AP106**: Slab $=$ bimodule. Dimofte slab geometry on
  $C \times [0, 1]$ produces an $(A, B)$-bimodule structure; the
  two ends carry distinct chiral algebras.
- **V2-AP107**: Drinfeld double identification is a CONJECTURE.
  $Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq \mathcal D(A)$ only on
  Koszul locus; beyond the locus, open.
- **V2-AP108**: Line operators live on $\mathbb R$, not on the
  curve. Topological-factorisation coproduct along $\mathbb R$
  generates line operators; holomorphic-factorisation bar
  differential on $C$ does not.
- **V2-AP109**: $\hat Z$-invariants are CONJECTURAL cross-volume
  objects. Gukov--Pei--Putrov--Vafa $\hat Z$ sit at the 3d-boundary
  of Vol II's HT setup; identification with Vol III's
  Borcherds-side quantities is open.
- **V2-AP110**: Holomorphic blocks $\ne$ conformal blocks. A
  holomorphic block on $C \times \mathbb R$ is a chiral bundle
  section; a conformal block is a BD-factorisation-sheaf section
  on $\mathrm{Ran}\,X$. Coincide on genus-$0$ degeneration only.
- **V2-AP111**: 3D quantum gravity CLIMAX (Part VI) requires ALL
  prior parts. Asserting the climax from a subset is a
  dependency-inflation error.
- **V2-AP112**: Genus-1 Bernard--Felder propagator involves theta
  functions and quasi-periodicity under $z \to z + \tau$. The
  genus-$0$ limit is a DEGENERATION, not a specialisation.

### Section W.3: Early Swiss-cheese and seven faces (V2-AP113--V2-AP119)

- **V2-AP113**: Voronov 1998 Swiss-cheese $\ne$
  $\mathsf{SC}^{\mathrm{ch,top}}$ of Vol II. Voronov uses
  $\mathrm{FM}_{k,m}(\mathbb H, \partial \mathbb H)$ (boundary
  fixed to $\partial \mathbb H$); $\mathsf{SC}^{\mathrm{ch,top}}$
  uses $\mathrm{FM}_k(\mathbb C) \times E_1(m)$ (product). The
  latter is a DEGENERATION of the former.
- **V2-AP114**: Seven faces of $r(z)$ chain F1--F7 is a STAR
  GRAPH: F1 hub, six spokes; plus external F5 $\leftrightarrow$ F6
  (Drinfeld--STS 1983--85). NEVER "seven equivalent."
- **V2-AP115**: F5 (Yangian, level-independent) vs F7 (Gaudin,
  level-shifted by $k + h^\vee$) CONFLATED at multiple sites. At
  $k = 0$: Yangian $r(z) \ne 0$; Gaudin $r(z) = \Omega / h^\vee
  \ne 0$; level-stripped $r = 0$.
- **V2-AP116**: F1 $\Leftrightarrow$ F4 is INJECTION, not
  bijection. $r(z)$ determines the KZ 1-form; the Drinfeld
  associator $\Phi_{\mathrm{KZ}}$ has MZV coefficients invisible
  to $r(z)$.
- **V2-AP117**: Heptagon edge 3-4 is associator-INDEPENDENT.
  Associator enters in edge 2-3 through $\mathrm{GRT}_1$-equivariant
  lift.
- **V2-AP118**: Heptagon edge 3-4 $\mathrm{GRT}$-equivariant heal.
  Associator-dependence in edge 2-3 is healed by passage to
  $\mathrm{GRT}_1$-equivariant category.
- **V2-AP119**: Genus-1 seven faces require KZB connection as the
  elliptic analogue of KZ. Felder propagator provides F6 at
  genus 1; genus $\ge 2$ degenerates via pair-of-pants
  factorisation.

### Section W.4: Drinfeld-double gap and frontier (V2-AP120--V2-AP125)

- **V2-AP120**: Drinfeld double gap.
  $Z^{\mathrm{der}}_{\mathrm{ch}}(A) \simeq \mathcal D(A)$ OPEN in
  general; proved on Koszul locus only. Gap is the OBSTRUCTION
  CLASS in $H^2(\mathrm{grt}_1; \widehat{\mathrm{Imag}})$.
- **V2-AP121**: Conway $V^{s\natural}$ is NOT an independent
  $\Psi$-image row. Duncan 2007 \emph{Duke Math.\ J.}\ 139
  constructs $V^{s\natural} = A(\Lambda_{24})^+ \oplus
  A(\Lambda_{24})^{\mathrm{tw}, +}$ as $\mathbb Z / 2$-orbifold of
  the 24-generator fermionic VOA on the Leech lattice;
  super-twin of $V^\natural$ on the Monster row. Three earlier
  defects: VENUE (Duke 139, not MRL 14), CONSTRUCTION (Leech
  fermionic VOA, not $E_8$ super-lattice), SIGNATURE
  ($c_+(\Lambda_{24}) = 24$, not $0$).
- **V2-AP122**: Six routes to $G(K3 \times E)$ are six DIFFERENT
  constructions ($\Phi$, Borcherds lift, lattice VOA, Kummer,
  sigma model, BLLPR), NOT six applications of the same functor.
- **V2-AP123**: Class M $E_3$-bar cohomology is $6^g$
  (COHOMOLOGICAL level), infinite-dimensional (CHAIN level).
  Mixing lanes gives WRONG genus-scaling. $g = 1$ bar profile
  $[0, 3, 3, 0]$.
- **V2-AP124**: $\zeta(3, 3, 3, 3) = 0.000295999\ldots$, NOT
  $0.0028565$. Depth-4 MZV at weight 12. Brown 2011 motivic MZV
  basis confirmation.
- **V2-AP125**: Fricke LDP variance $\sigma_k^2 = \pi / (2 \sin^2
  \theta_k^*)$ (inverse-density), NOT $(\pi^2 / 2) \cos^{-2}
  \theta_k^*$ (density-curvature, DIVERGES at finite-density
  nodes).

### Section W.5: Single-valued MZV scope on chiral-Hochschild periods (V2-AP126)

- **V2-AP126 -- Single-valued MZV scope of chiral-Hochschild
  periods (Critical).**
  (a) **Ghost.** The Deligne-Goncharov 2005 *Ann Sci ENS* 38
  mixed-Tate motivic framework gives the full motivic Galois
  $\mathrm{grt}_1^{\mathrm{mot}}$ acting on the motivic MZV ring
  $\mathrm{MZV}^{\mathrm{mot}}$; the chiral-Hochschild period
  $2\mathrm{Vol}(E)(2\pi i)^3$ is a genuine period with a natural
  motivic home. The Vol II one-loop Quillen exponent (Path E) and
  the Costello-Gwilliam factorisation-cyclic-homology $\chi_3$
  pairing on $\mathsf{SC}^{\mathrm{ch,top}}$-algebras $a\text{-}priori$
  expand in $\mathrm{MZV}^{\mathrm{mot}}$.
  (b) **Precise error.** Asserting that the chiral-Hochschild
  period identity $\chi_3 = 2\mathrm{Vol}(E)(2\pi i)^3$ lies in the
  full motivic ring $\mathrm{MZV}^{\mathrm{mot}}$ is a scope
  inflation. The Arnold forms $\eta_{ij} = d\log|z_{ij}|^2$ that
  witness the chain-level $\chi_3$ cocycle are **single-valued
  real**; the period pairing factors through Brown 2013 *Ann Math*
  175 projection $\mathrm{proj}: \mathrm{MZV}^{\mathrm{mot}} \to
  \mathrm{MZV}^{\mathrm{sv}}$. At weight 2, $\zeta^{\mathrm{sv}}(2)
  = 0$; conflating the two rings overcounts admissible periods and
  would predict $\zeta(2)$-weighted Hochschild contributions that
  do not survive the single-valued projection.
  (c) **Correct.** Chiral-Hochschild periods live in
  $\zeta^{\mathrm{sv}}$ (Brown 2013 single-valued MZVs), **not**
  in $\mathrm{grt}_1^{\mathrm{mot}}$-stable full motivic MZVs.
  Three sites must be distinguished:
  **chain-level** (explicit $\eta_{ij}$-integrals on
  $\mathrm{Conf}_n(X)$, rational-coefficient),
  **motivic** ($\mathrm{MZV}^{\mathrm{mot}}$ target of the period
  map),
  **single-valued** ($\zeta^{\mathrm{sv}}$ image under Brown's
  projection). Canonical identifications:
  $\zeta^{\mathrm{sv}}(2) = 0$,
  $\zeta^{\mathrm{sv}}(2k+1) = 2\zeta(2k+1)$ at odd weight, and
  $\zeta^{\mathrm{sv}}$ is a **proper** subring at depth $\ge 2$
  (Schnetz 2014 *Commun Num Theor Phys* 8; Panzer 2015
  *Commun Num Theor Phys* 9).
  **Vol II reading.** The single-valued scope constrains Vol II's
  one-loop Quillen exponent / Costello-Gwilliam
  factorisation-cyclic-homology reading of the $\chi_3$ pairing.
  The Vol II cyclic chiral homology (Path E) lands in
  $\zeta^{\mathrm{sv}}$ via the Francis-Gaitsgory
  cyclic-factorisation trace composed with the Brown single-valued
  projection. The Theorem H amplitude bound
  $\mathrm{ChirHoch}^\bullet \in \{0, 1, 2\}$ is recovered as a
  **single-valued consequence** of $\zeta^{\mathrm{sv}}(2) = 0$,
  not imposed as a separate concentration axiom.
  **Counter**: never equate chiral-Hochschild periods with
  $\mathrm{MZV}^{\mathrm{mot}}$; always name the Brown 2013
  projection and land in $\zeta^{\mathrm{sv}}$.
  Cross-reference Vol I AP901 and Theorem
  `thm:sv-scope-restriction-chiralhoch` in
  `/Users/raeez/chiral-bar-cobar/chapters/theory/motivic_shadow_tower.tex`.
  Related: AP888 (shadow-ChirHoch bridge) and the seven-path
  $\chi_3$ comparison theorem.
  **Primary citations**: Brown 2013 "Mixed Tate motives over
  $\mathbb Z$" *Ann Math* 175; Brown 2013 *Ann Sci ENS* 46
  single-valued multiple polylogarithms; Schnetz 2014 single-valued
  zeta; Deligne-Goncharov 2005; Panzer 2015 single-valued
  algorithms.

---

## Cross-reference index

- Legacy `V2-AP1--V2-AP48` (this file: sections directly above
  plus re-extracted V2-AP1-20 block) is verbatim from
  `notes/claude_md_legacy_20260418.md` and
  `~/chiral-bar-cobar/notes/cross_volume_aps.md`. Number preservation:
  `V2-APN` is the historical trigger; `AP-V2-N` (top of this file)
  is the current Platonic-synthesis scheme. Independent numberings.
- Waves 1-13 (sections W.1--W.4, `V2-AP100--V2-AP125`) distilled
  from session archives in `~/chiral-bar-cobar/notes/session_*`
  $+$ `project_dimofte_full_integration.md`
  $+$ `project_sc_chtop_concrete_programme.md`
  $+$ `project_preface_geometric_escalation.md`.
- Waves 14-19 entries appear as `V2-AP56--V2-AP69` distilled from
  `~/calabi-yau-quantum-groups/notes/ADJUDICATION_LEDGER_WAVES_14_TO_19.md`.
- Waves 20-24 entries appear as `AP-V2-1--AP-V2-22` distilled from
  `~/chiral-bar-cobar/notes/GRAND_SYNTHESIS_WAVES_20_22.md`.

## Per-wave coverage table

| Wave(s)     | Count | Scheme                | Focus                                                      |
| ----------- | ----: | --------------------- | ---------------------------------------------------------- |
| Waves 1-9   |    16 | V2-AP1--V2-AP16       | $E_1 / E_\infty$ locality hierarchy                        |
| Waves 1-9   |     4 | V2-AP17--V2-AP20      | Process and workflow guards                                |
| Waves 10-13 |     4 | V2-AP21--V2-AP24      | Hierarchy and chromatic                                    |
| Waves 10-13 |    15 | V2-AP25--V2-AP39      | Empirical error archaeology                                |
| Waves 17-19 |     9 | V2-AP40--V2-AP48      | Wave-17-19 synthesis legacy                                |
| Waves 1-13  |    26 | V2-AP100--V2-AP125    | SC foundations, Dimofte, Swiss-cheese, seven faces, climax |
| Waves 14-19 |    14 | V2-AP56--V2-AP69      | K3-BKM / 3d HT-QFT adjudication                            |
| Waves 20-24 |    22 | AP-V2-1--AP-V2-22     | Octachotomy, Theorem H hinge, BKM crown, five-archetype    |
| Wave 27     |     1 | AP-V2-23              | Chenevier determinant (not pseudo-character)               |
| Wave 28     |     1 | V2-AP126              | Single-valued MZV scope on chiral-Hochschild periods       |
| Wave 29     |     1 | AP-V2-24 / V2-AP127   | Humbert--Heegner admissibility filter $n\equiv 3,5\pmod 8$ |
| Wave 14 cross | 5 | AP-V2-25--AP-V2-29 / V2-AP128--V2-AP132 | hCS / KT formality torsor, MNOP centre trace, Swiss-cheese compatibility, $\mathbb E_n$ ambient vs category, non-isolated LG critical locus (Vol III AP-CY160--172 cross-append) |
| **Total**   | **118** | legacy + synthesis  | Vol II anti-patterns                                       |

---

### AP-V2-23: Chenevier determinant, not Taylor-Wiles pseudo-character (arithmetic anchor for $\mathbf H_{\Delta_5}$)

**Trigger**: "Taylor 1991 pseudo-character $S^{\mathrm{ps}} :
\mathbb T^{\mathrm{par}}_1 \to \mathcal O_E$ with axioms (symmetry /
multiplicativity / dimension)" attached to the Galois-side invariants
of the BKM crown algebra $\mathbf H_{\Delta_5}$.

**Ghost**: the Taylor-Wiles pseudo-character $S^{\mathrm{ps}}$ is a
real object (Taylor 1991 Duke 63 Thm 2.1; Rouquier 1996); the
Hecke-algebra 4-tuple $(S_1, S_2, S_3, S_4)$ computed from the
Saito-Kurokawa lift Satake parameters of $\Delta_{10}$ is correct
data; the bridge to a Galois representation $\rho_{\Delta_{10}} :
\mathrm{Gal}(\overline{\mathbb Q} / \mathbb Q) \to \mathrm{GSp}_4(\mathcal O_E)$
works on reduced rings (Chenevier 2014 Thm 2.12 equivalence
pseudo-characters $\leftrightarrow$ determinants on reduced rings).

**Precise error**: conflates the Taylor-Wiles pseudo-character
(older, weaker, multilinear symmetric trace functions) with the
Chenevier 2014 determinant (newer, stronger, single homogeneous
polynomial law with multiplicativity, unitality, Cayley-Hamilton).
On non-reduced rings — exactly the deformation rings that Vol II's
one-loop Quillen norm and BV 3d HT-QFT partition function feel — the
two objects differ; the determinant captures strictly more structure
(nilpotent Cayley-Hamilton witnesses that the pseudo-character
silently drops).

**Correct**: $D^{\mathrm{Chen}} : \mathbb T^{\mathrm{par}}_1 \to
\mathcal O_E \otimes \mathbb Z_\ell$ is a 4-dimensional Chenevier
determinant. Its graded components $(\Sigma_1, \Sigma_2, \Sigma_3,
\Sigma_4)$ at Hecke generators $T_p$ recover $(a_p(f_{16}) + p^8 +
p^9, \ldots, p^{32})$ via the reciprocal spinor $L$-factor expansion
$\prod_{i=1}^4 (1 - \alpha_i x) = 1 - \Sigma_1 x + \Sigma_2 x^2 -
\Sigma_3 x^3 + \Sigma_4 x^4$. Verified at 46 primes $p \le 199$.

**Vol II framing**: the Vol II arithmetic reading ties Vol II's
one-loop Quillen norm and BV 3d HT-QFT partition function to the
Galois-side $L$-function data via the Chenevier determinant; the
older "pseudo-character" framing was a proxy sufficient for W20.4's
trace identities on reduced rings but insufficient for Vol II's
scheme-valued path-integral refinements (deformation rings around
the Saito-Kurokawa lift are non-reduced, and the BV anomaly
measures the nilpotent Cayley-Hamilton witnesses that $S^{\mathrm{ps}}$
cannot see). The universal identity on the B-row
(three-faces, AP-V2-20) reads off from $D^{\mathrm{Chen}}$, not from
$S^{\mathrm{ps}}$.

**Primary**: Chenevier 2014 arXiv:1301.0635 Sec 1.2 Def/Prop 1.9,
Thm 2.12 (determinant $=$ pseudo-character on reduced rings; strict
inequality on non-reduced); Taylor 1991 Duke 63 Thm 2.1
(pseudo-character original definition); Ikeda 2001 Ann Math 154
Cor 16.2 (Saito-Kurokawa lift); Weissauer 2005 LNM 1868 (spinor
Galois representation); Laumon 2005 Publ IHES 102 (geometric
Satake on $\mathrm{GSp}_4$).

**Cross-ref**: Vol I AP902 / Remark
`rem:dl-w25-determinant-not-pseudocharacter` in
`chapters/theory/derived_langlands.tex` and cache entry 422; Vol III
cache entry at `appendices/first_principles_cache.md` row 8 (tagged);
Vol III `ADJUDICATION_LEDGER` §III.C; Pattern 295
(Creutzig-Ridout / Lyubashenko coend pseudo-traces on non-semisimple
MTCs — DISTINCT object, do NOT conflate: coend pseudo-traces live
on modular tensor categories, not on Hecke algebras, and satisfy a
different (Kerler-Lyubashenko modified-trace) axiom set).

### AP-V2-24 / V2-AP127: Humbert--Heegner admissibility filter $n\equiv 3,5\pmod 8$ on the pentagon coboundary tower $\phi^{(n)}$

**Trigger**: any Vol II assertion that $\phi^{(n)}\ne 0$ on the
K3--Humbert regime of the $\mathsf{SC}^{\mathrm{ch,top}}$ coloured bar
differential from the sole datum $d_n>0$ (Padovan motivic-MZV
dimension, Brown 2012 *Ann Math* 175 Thm 1), without installing the
Humbert--Heegner admissibility filter
$n\equiv 3,5\pmod 8$ and the Eichler--Zagier 1985 polar-support cutoff
$\Delta\ge -1$ on the paramodular index-1 K3 elliptic genus.

**Ghost**: the pentagon coboundary tower $\{\phi^{(n)}\}_{n\ge 3}$ of
Definition \texttt{def:phi-n-pent-EK} (Vol I
\texttt{chapters/theory/shadow\_tower\_higher\_coefficients.tex}) has a
well-defined three-filter admissibility structure on the K3
$A_\infty$-Humbert regime: (i) Padovan $d_n = d_{n-2}+d_{n-3}$ counts
the motivic-MZV transcendence basis at weight $n$ (real theorem, Brown
2012); (ii) Eichler--Zagier 1985 polar-support cutoff $C(\Delta)=0$ for
$\Delta < -m^2 = -1$ on the index-1 weak Jacobi form $\phi^{K3}_{0,1}$
is a real theorem (Eichler--Zagier *Prog Math* 55 Thm 9.3 with
$C(-1)=2$, $C(0)=20$); (iii) Gritsenko--Nikulin 1998 *J Reine Angew
Math* 507 paramodular lift of the K3 elliptic genus gives explicit
$c_{\Phi_{10}/\eta^{24}}$ Fourier data.

**Precise error**: bare Padovan-dimension $d_n$ count WITHOUT the
Humbert--Heegner admissibility filter overcounts. Most
Padovan-admissible $n\ge 3$ (all $n\ge 3$ except $n=4$) are
Humbert--Heegner-FORBIDDEN on the K3--Humbert regime: the paramodular
lattice sum $\sum_{4NM-\ell^2=-D_n} c_{\Phi_{10}/\eta^{24}}(N,\ell,M)$
with $D_n = (n-3)/2$ is non-empty iff $D_n\bmod 4\in\{0,1\}$, which
forces $n\equiv 3,5\pmod 8$. Asserting a non-zero $\phi^{(n)}$ on the
Vol II Swiss-cheese coloured-bar reading on the sole basis of $d_n>0$
(e.g., at $n=7,9,12,24,26,\dots$) silently conflates the
MZV-transcendence count with the paramodular Humbert--Heegner
signature and misses the Heegner--Bruinier obstruction class
$\mathrm{ob}^{\mathrm{HB}}_n\in H^2(H_n,\mathrm{Sym}^2 T^{\mathrm{poly}}_{\mathrm{ch}}|_{H_n})$
of Bruinier-torsion order $c_n$ (Bruinier 2002 LNM 1780 Chern class on
Heegner divisors).

**Correct**:
$\phi^{(n)}\big|_{\mathrm{K3\text{-}Humbert}}\ne 0$ iff (i)
$n\equiv 3,5\pmod 8$ AND (ii) the $d_n$-dimensional Brown canonical
basis is non-empty AND (iii) $D_n\le 1$ (Eichler--Zagier polar cutoff).
First non-vanishing cases: $\phi^{(3)}$ = Drinfeld pentagon cocycle
($D_3=0$, $C(0)=20\ne 0$); $\phi^{(5)} = -2\cdot[\mathrm{gen}]^{\otimes 5}$
with Gritsenko--Nikulin 1998 Table 2 sign on $\Phi_{10}/\eta^{24}$
($D_5=1$, $C(-1)=2\ne 0$). Humbert--Heegner admissible $n\in[3,36]$:
$\{3,5,11,13,19,21,27,29,35\}$. Padovan-positive HH-forbidden $n$
(e.g., $4,6,7,8,9,10,12,14,15,16,17,18,20,22,23,24,25,26,28,30,31,32,33,34,36$)
all give $\phi^{(n)}=0$ on K3--Humbert. HH-admissible $n\ge 11$ give
$\phi^{(n)}=0$ on K3--Humbert by Eichler--Zagier polar support
($D_n\ge 4 > 1$).

**Condensed reference table** $(n, d_n, D_n, \mathrm{HH}, \phi^{(n)}\text{-K3})$:
$(3,1,0,Y,\text{non-zero})$; $(4,0,1/2,-,0)$;
$(5,1,1,Y,-2[\mathrm{gen}]^{\otimes 5})$; $(6,1,3/2,-,0)$;
$(7,1,2,N,0)$; $(8,2,5/2,-,0)$; $(9,2,3,N,0)$; $(10,2,7/2,-,0)$;
$(11,3,4,Y,0\,\text{polar})$; $(12,4,9/2,-,0)$;
$(13,5,5,Y,0\,\text{polar})$; $(19,17,8,Y,0\,\text{polar})$;
$(21,28,9,Y,0\,\text{polar})$; $(27,90,12,Y,0\,\text{polar})$;
$(29,149,13,Y,0\,\text{polar})$; $(35,504,16,Y,0\,\text{polar})$.

**Vol II framing (Swiss-cheese coloured-bar reading)**: the
Humbert--Heegner admissibility filter is the Humbert-stratification
refinement of the $\mathsf{SC}^{\mathrm{ch,top}}$ coloured bar
differential on $\overline{\mathcal A_2}$. Each coloured face of the
$\mathsf{SC}^{\mathrm{ch,top}}$ operadic resolution at weight $n$
couples to the paramodular K3 elliptic-genus polar slice $\Delta\ge -1$;
a face colouring is admissible iff the discriminant $D_n=(n-3)/2$ lies
in $\{0,1\}\bmod 4$, equivalently $n\equiv 3,5\pmod 8$. Non-admissible
coloured faces carry the Heegner--Bruinier obstruction class
$\mathrm{ob}^{\mathrm{HB}}_n$ of Bruinier-torsion order $c_n$; the
Kontsevich formality per-wall obstruction of AP-V2-6 and the
Hodge-to-de-Rham $d_2$ differential of AP-V2-12 both read off from this
same Heegner--Bruinier class. The filter locks which of the eight
bar-cobar ambient colourings of AP-V2-1 is admissible at each weight
$n$. Every Vol II $\phi^{(n)}$ reference on the coloured bar
differential (all Wave-20-28 entries) carries the HH admissibility
scope or a pointer to Theorem \texttt{thm:phi-n-humbert-heegner-admissibility}
inscribed in Vol I \texttt{chapters/theory/shadow\_tower\_higher\_coefficients.tex}
(lines 4364-4433).

**Three verification paths for the filter**: (i) discriminant-form
signature — the index-$1$ paramodular form $4NM-\ell^2\equiv -\ell^2\pmod 4$
takes values in $\{0,-1\}\pmod 4$, so $-D_n$ is representable iff
$D_n\in\{0,1\}\pmod 4$, forcing $n\equiv 3,5\pmod 8$ by odd-$n$
integrality; (ii) Eichler--Zagier 1985 weak-Jacobi-form polar-support
cutoff ($C(\Delta)=0$ for $\Delta<-m^2=-1$, real theorem); (iii)
Gritsenko--Nikulin 1998 paramodular lift of the K3 elliptic genus with
explicit $c_{\Phi_{10}/\eta^{24}}$ Fourier table (real object).

**Primary**: Eichler--Zagier 1985 *Prog Math* 55 Thm 9.3
(polar-support cutoff); Gritsenko--Nikulin 1998 *J Reine Angew Math*
507 (Humbert--Heegner structure, paramodular $\Phi_{10}/\eta^{24}$ sign
convention Table 2); Bruinier 2002 LNM 1780 §5 (Chern class on Heegner
divisors, torsion orders $c_n$); Brown 2012 *Ann Math* 175 Thm 1
(Padovan motivic-MZV dimension).

**Cross-ref**: Vol I Theorem \texttt{thm:phi-n-humbert-heegner-admissibility}
in \texttt{/Users/raeez/chiral-bar-cobar/chapters/theory/shadow\_tower\_higher\_coefficients.tex}
(lines 4364-4433); Vol I cache row 304 (AP890) + Pattern 299
comprehensive; Vol I \texttt{notes/antipatterns\_catalogue.md}
AP903-HH; Vol III \texttt{notes/antipatterns\_catalogue.md} AP-CY142
(partner entry); Vol III \texttt{appendices/first\_principles\_cache.md}
tip-table row V16; Vol III
\texttt{notes/first\_principles\_cache\_comprehensive.md} AP-CY142 long
form. Cross-links Vol II AP-V2-1 (eight Swiss-cheese bar-cobar
ambients), AP-V2-6 (chiral Kontsevich formality on Humbert strata),
AP-V2-12 (Kaledin Hodge-to-de-Rham scope) — the HH filter locks the
admissible coloured-bar ambient at each weight $n$.

### AP-V2-25 / V2-AP128: Swiss-cheese colours framed without stage-1/stage-2 identification (Vol III two-stage factorisation, 2026-04-22)

**Trigger**: any Vol II statement of the two-coloured operad
$\mathsf{SC}^{\mathrm{ch,top}}$ in which the CLOSED colour
($\mathrm{FM}_k(\mathbb{C})$, $E_2$-holomorphic) and the OPEN colour
($\mathrm{Conf}_m(\mathbb{R})$, $E_1$-topological) are declared as two
independent colour indices without naming the Vol III two-stage
factorisation identifying each colour with a stage of
$\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$.

**Ghost**: Vol III's CY-to-chiral programme produces a canonical
$E_d$-homotopy factorisation algebra on the CY-$d$ target in
\emph{stage 1} $\Phi^{\mathrm{FA}}_d$ (Kontsevich--Tamarkin formality
plus Costello--Gwilliam--Li factorisation-homology BV quantisation),
then pushes forward via $\int_{\Sigma_{d-1}}$ to a reference curve $C$
in \emph{stage 2} $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$, landing
on an $E_1$-chiral shadow. The two colours of
$\mathsf{SC}^{\mathrm{ch,top}}$ are exactly the two stages: CLOSED =
stage-1 $\Phi^{\mathrm{FA}}_d$ on local observables of an
$E_d$-holomorphic factorisation algebra on a formal disc in the CY
target ($\mathrm{FM}_k(\mathbb{C})$); OPEN = stage-2
$\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$ landing on the reference
curve ($\mathrm{Conf}_m(\mathbb{R})$); MIXED operations
(closed-input $\to$ open-output) = factorisation-homology pushforward
$\int_{\Sigma_{d-1}}$, with the directional restriction
$\mathsf{SC}^{\mathrm{ch,top}}(\ldots, \mathsf{top}, \ldots;
\mathsf{cl}) = \varnothing$ expressing that stage~2 is a specialisation
of stage~1, never an inversion.

**Precise error**: writing $\mathsf{SC}^{\mathrm{ch,top}}$ as a pure
combinatorial datum (closed colour, open colour, mixed operations),
decoupled from $\Phi_d$, loses (i) the specialisation direction from
Vol III stage~1 to Vol III stage~2, (ii) the identification of the
mixed-operation pushforward with $\int_{\Sigma_{d-1}}$, and (iii) the
directional-restriction asymmetry as a shadow of the fibre-integration
arrow. Framing the colours purely operadically hides the Vol III
anchor and leaves the Vol II $\leftrightarrow$ Vol III bridge
diagrammatic.

**Correction**: every $\mathsf{SC}^{\mathrm{ch,top}}$ statement that
carries cross-volume content names the stage identification in its
preamble or a nearby remark:
\[
\text{CLOSED} = \text{stage-1 } \Phi^{\mathrm{FA}}_d |_{\text{local obs}},
\quad
\text{OPEN} = \text{stage-2 } \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C},
\quad
\text{MIXED} = \int_{\Sigma_{d-1}}.
\]
Inscribed at `chapters/theory/sc_chtop_heptagon.tex` Remark
\texttt{rem:heptagon-two-stage-CY-to-chiral} and
`chapters/theory/factorization_swiss_cheese.tex` Remark
\texttt{rem:pentagon-two-stage}; cross-volume macros
$\PhiFA, \SpCh, \HolFA, \EdHolFA, \EnHolFA, \intSigma, \hCS$ declared in
`main.tex` preamble with `\providecommand` mirrors in affected
chapters.

**Severity**: Critical — load-bearing for the Vol II / Vol III bridge
and for the heptagon / pentagon coherence diagrams.

**Primary**: Kontsevich 2003 *Lett Math Phys* 66 (deformation
quantisation on $\mathbb{R}^d$); Tamarkin 2003 *Lett Math Phys* 66
(GRT-torsor structure); Costello--Gwilliam 2017 / 2021 Vols 1--2 (BV
factorisation quantisation); Ayala--Francis 2015 *J Topol* 8
($\mathrm{Conf}_m(\mathbb{R})$ and $E_1$-factorisation homology);
Voronov 1998 *Math Ann* 312 (classical Swiss-cheese); Francis--Gaitsgory
2012 *Selecta Math* 18 (Ran-space factorisation stratification).

**Cross-ref**: Vol II CLAUDE.md "Two-stage factorisation: Vol III
alignment" section (lines 281--318); Vol III
\texttt{notes/antipatterns\_catalogue.md} AP-CY two-stage entry
(2026-04-22 wave); AP-V2-1 (eight bar-cobar ambient colourings refined
by the stage identification); AP-V2-9 (Theorem H hinge crosses stages
at $d \ge 2$); AP-V2-14 (CY-4 HK-restricted $\Phi_4$ inherits the
two-stage structure on the HK locus).

### AP-V2-26 / V2-AP129: Single-stage $\Phi_d$ framing of Vol III output (2026-04-22)

**Trigger**: any Vol II reference to Vol III's CY-to-chiral functor
that writes the output as a unified $\Phi_d$ without naming it as the
stage-2 shadow
$\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$.

**Ghost**: Vol III's $\Phi_d$ factors canonically as stage-1
$\Phi^{\mathrm{FA}}_d$ (the $E_d$-holomorphic factorisation algebra)
followed by stage-2 $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$
(specialisation to a reference curve $C$ via factorisation-homology
pushforward along $\Sigma_{d-1}$). A CY-$d$ category admits a
\emph{family} of $E_1$-chiral shadows
$\{\Phi_d(\mathcal C; \Sigma_{d-1}, C)\}_{(\Sigma_{d-1}, C)}$
parametrised by the polarisation of the CY target.

**Precise error**: treating $\Phi_d$ as a unified functor forgets the
$(\Sigma_{d-1}, C)$-parameter family and the stage-2 reference-curve
choice; the stage-2 pushforward is not canonical (it depends on the
polarisation of $\text{CY}_d$ locally). Vol II cross-references
invoking $\Phi_d$ must carry the stage scope, or default to stage-1
$\Phi^{\mathrm{FA}}_d$ when the statement lives on the CY side.

**Correction**: Vol II cross-references to Vol III output use one of
three precise forms:
$\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ
\Phi^{\mathrm{FA}}_d$ (both stages named), stage-1
$\Phi^{\mathrm{FA}}_d$ (CY-side claim), or stage-2
$\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$ (curve-side claim). The
six primary Vol II files touching Vol III output have been aligned to
this convention; new inscriptions follow it from the first keystroke.

**Severity**: Critical — every cross-volume claim on
$\Phi_d(\mathcal C)$ carries the stage scope.

**Primary**: Kontsevich--Tamarkin formality (stage-1 existence);
Costello--Gaiotto--Li BV quantisation (stage-1 $E_d$ structure);
Ayala--Francis factorisation-homology pushforward (stage-2
specialisation).

**Cross-ref**: Vol II CLAUDE.md two-stage section (lines 281--318);
Vol III `chapters/theory/cy_to_chiral.tex` (stage-1 / stage-2
canonical construction); Vol III AP-CY two-stage entries (2026-04-22);
related to AP-V2-25 (closed/open colour identification); AP-V2-9
(Theorem H hinge at $d \ge 2$).

### AP-V2-27 / V2-AP130: 3D HT QFT scope without two-stage anchor (2026-04-22)

**Trigger**: statements about the Vol II 3D holomorphic-topological
QFT framework (bulk $\mathsf{SC}^{\mathrm{ch,top}}$ pairing, derived
centre $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ as bulk algebra) that omit
the cross-volume anchor identifying the $\mathsf{SC}^{\mathrm{ch,top}}$
structure with the Vol III two-stage factorisation at $d = 2, 3$.

**Ghost**: the Vol II 3D HT QFT framework is intrinsically a
Swiss-cheese / factorisation-operadic construction; its natural
ambient at the CY target is the stage-1 $\Phi^{\mathrm{FA}}_d$ output.
$\Phi^{\mathrm{FA}}_3$ exists canonically by Kontsevich--Tamarkin
formality plus Costello--Gwilliam--Li factorisation-homology BV
quantisation; stage-2 $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_2, C}$ lands
the Vol II data on a reference curve.

**Precise error**: presenting the 3D HT QFT framework as
self-contained on the curve $C$, without flagging that the CLOSED
colour of $\mathsf{SC}^{\mathrm{ch,top}}$ is the stage-1 CY-side datum
and the OPEN colour is the stage-2 curve-side datum, hides (i) the
$(\Sigma_{d-1}, C)$ parameter, (ii) the $\int_{\Sigma_{d-1}}$-
pushforward as the MIXED operation, and (iii) the existence of
$\Phi^{\mathrm{FA}}_3$ as a named object. The 3D HT QFT content is
cross-volume: it lives at the Swiss-cheese layer = the two-stage
interface.

**Correction**: Vol II 3D HT QFT statements in reader-facing prose
name the two-stage anchor at first mention per chapter, via a
parenthetical or a remark: "the $\mathsf{SC}^{\mathrm{ch,top}}$
pairing on $C \times \mathbb{R}$ is the stage-2 shadow of the Vol III
$E_3$-holomorphic factorisation algebra $\Phi^{\mathrm{FA}}_3$, with
$\int_{\Sigma_2}$ the MIXED factorisation-homology pushforward". The
existence of $\Phi^{\mathrm{FA}}_3$ as a canonical stage-1 object is
itself a Vol III theorem (Kontsevich--Tamarkin + CGL); Vol II does not
re-prove it, only invokes it at the bridge.

**Severity**: High — Vol II's 3D HT QFT framework is the main
contribution of Parts V--VI; the two-stage anchor is its natural place
in the cross-volume architecture.

**Primary**: Costello--Gwilliam 2017 / 2021 Vols 1--2 (BV quantisation
on factorisation algebras); Kontsevich 2003 (deformation quantisation);
Costello--Gaiotto 2019 (5d / 3d HT twists); Costello--Li 2023
(holomorphic Chern--Simons factorisation); Ayala--Francis 2015
(factorisation-homology pushforward).

**Cross-ref**: Vol II CLAUDE.md two-stage section (lines 281--318);
AP-V2-25 (closed / open colour = stage-1 / stage-2); AP-V2-26
(single-stage $\Phi_d$ framing); AP-V2-1 (bar-cobar ambient
octachotomy refined by stage-1 vs stage-2).

### AP-V2-28 / V2-AP131: Manifesto conflations inherited from Vol III (2026-04-22)

**Trigger**: any Vol II reference to a Vol III canonical value that
re-states an earlier-retracted reading, in particular:
$\kappa_{\mathrm{cat}}(K3 \times E) = 2$;
$\mathrm{CoHA}(\mathbb{C}^3) = \mathcal{W}_{1+\infty}$; "six routes to
$G(K3 \times E)$ are six $\Phi_3$-applications"; Fake-Monster placed at
$d = 3$.

**Ghost**: four canonical readings of cross-programme objects bind at
every Vol II cross-reference site:
- $\kappa_{\mathrm{cat}}(K3 \times E) = \chi(\mathcal O_{K3})
  \cdot \chi(\mathcal O_E) = 2 \cdot 0 = 0$ on the total space
  (Künneth-multiplicative);
- $\mathrm{CoHA}(\mathbb{C}^3) = Y^+(\widehat{\mathfrak{gl}}_1)$,
  the \emph{positive half} of the affine Yangian (not the full
  $\mathcal{W}_{1+\infty}$ algebra, not $\mathcal{W}_\infty[c]$);
- the six routes to $G(K3 \times E)$ (CoHA, Schiffmann--Vasserot,
  Maulik--Okounkov, Borcherds, Toda, DMVV) are six \emph{different
  constructions}, each taking a different CY-input category, each
  producing the same $\Phi_3$-output through a pentagon colimit; NOT
  six applications of $\Phi_3$;
- the Fake-Monster BKM sits at $d = 5$ (signature
  $\mathrm{II}_{25,1}$, Borcherds 1992 *Invent Math* 109), NOT at
  $d = 3$ where the K3-BKM $\mathbf H_{\Delta_5}$ lives (signature
  $\Lambda^{2,1}_{II}$, Gritsenko--Nikulin 1998).

**Precise error**: Vol II cross-references inheriting fibre
$\kappa_{\mathrm{cat}}(K3) = 2$ at the total-space site (naive
Künneth-additive confusion); conflating $\mathrm{CoHA}(\mathbb{C}^3)$
with $\mathcal{W}_{1+\infty}$ (classical-limit vs full positive half);
or placing Fake-Monster on the $d = 3$ row that belongs to K3-BKM.
These propagate via status tables, landscape maps, and remark
cross-references; each re-statement is a latent canonical-preamble
violation (rows 20--22, 32, 59, 61--62, 65--66).

**Correction**: every Vol II cross-reference to a Vol III canonical
value cites as named in the preamble (lines 5--67 of this catalogue)
or names the preamble explicitly. Concretely:
- $\kappa_{\mathrm{cat}}(K3 \times E) = 0$ always (name the total
  space); the fibre value $2$ is $\kappa_{\mathrm{fiber}}(K3)$, a
  different $\kappa_\bullet$ index;
- $\mathrm{CoHA}(\mathbb{C}^3) = Y^+(\widehat{\mathfrak{gl}}_1)$
  (positive half; $\mathcal{W}_{1+\infty}$ is a classical-limit
  current subalgebra);
- six routes to $G(K3 \times E)$ are six distinct constructions
  producing the same $\Phi_3$ output;
- Fake-Monster at $d = 5$ with $\Phi_{12}$; K3-BKM at $d = 3$ with
  $\Phi_{10} = \Delta_5^2$.

**Severity**: High — each conflation has re-appeared across waves
(Wave 16 Fake-Monster rank, Wave 23 $\kappa_{\mathrm{cat}}$ drift);
the canonical preamble is the binding register.

**Primary**: Schiffmann--Vasserot 2012 *Publ IHES* 115 (CoHA);
Borcherds 1992 *Invent Math* 109 (Fake-Monster); Gritsenko--Nikulin
1998 (K3-BKM); Mukai 1984 (K3 Mukai lattice).

**Cross-ref**: Canonical preamble rows 20--22, 32, 59--63; AP-V2-22
(five-archetype landscape); AP-V2-20 (three-faces universal
identity); V2-AP68 / V2-AP69 (CoHA / $\kappa_\bullet$ discipline);
V2-AP122 (six routes = six constructions); Vol III
\texttt{chapters/examples/cy\_d\_kappa\_stratification.tex} (canonical
$\kappa_\bullet$ table); Vol III CLAUDE.md key-facts block.

### AP-V2-29 / V2-AP132: Structural voice discipline — `\begin{warning}` and bookkeeping vocabulary in reader-facing Vol II prose (2026-04-22)

**Trigger**: any reader-facing Vol II `.tex` under `chapters/`,
`frame/`, `examples/`, `theory/`, `connections/`, or `bibliography/`
containing (i) a `\begin{warning}` environment, or (ii) bookkeeping
tokens such as `AP-V2-N`, `V2-APN`, `Pattern N`, `Wave N`,
`cache-canonical`, `CLAUDE.md`, `manifesto`, `Beilinson-standard`,
`HZ-N`, `DNA strand`, `cache entry`, `CG-rectify pass`, `round K`, or
`batch M`.

**Ghost**: the Vol II manuscript is self-complete, self-coherent,
self-consistent. Reader-facing prose is written in the
Chriss--Ginzburg voice. Bookkeeping vocabulary — waves, rounds, AP
indices, cache entries, rectification passes, CLAUDE.md pointers —
belongs in `notes/`, `FRONTIER.md`, commit messages, and the local
`memory/`. `\begin{warning}` is a bookkeeping environment (the reader
sees a "warning" rather than a mathematical statement) and is
reserved for `notes/` scaffolding if anywhere.

**Precise error**: V2-AP51 earlier recorded that reader-facing prose
containing `Wave N` / `AP\d+` / `DNA` tags triggered CG-rectify scrubs
that removed substantive mathematical inscriptions as collateral
(cache entry 89, 2026-04-20/21). `\begin{warning}` in reader-facing
`.tex` is a parallel failure mode: it presents bookkeeping to the
reader as if it were mathematics.

**Correction**: reader-facing inscriptions contain (a) no
`\begin{warning}` environments, (b) no bookkeeping tokens listed in
the Trigger. Named section / subsection / remark titles denote
mathematical objects; equations carry mathematical labels. Hedging
that the mathematics does not earn is forbidden; the equals sign is a
theorem. Retroactive rectification runs per-chapter through the
`chriss-ginzburg-rectify` skill; forward inscriptions follow the CG
voice from the first keystroke. The "Session antipatterns — manuscript
hygiene (2026-04-22)" block below (CGCLEAN-1..55) enumerates the
specific vocabulary patterns with canonical repair.

**Severity**: High — the scrub-cascade mechanism is real (V2-AP51 +
cache entry 89); the forward fix is cheap; per-chapter sweep when
introducing new content.

**Primary**: Vol II CLAUDE.md "Writing standard: Chriss--Ginzburg
north star" section (lines 128--192); V2-AP51 (scrub-cascade
causality); cache entry 89 (hook-cascade content loss).

**Cross-ref**: Vol II CLAUDE.md lines 128--192; V2-AP51 (legacy
scrub-cascade AP); the "Session antipatterns — manuscript hygiene
(2026-04-22)" block below (CGCLEAN-1..55) is the detailed sibling
register (this AP-V2-29 is the upstream reader-facing voice-discipline
AP; CGCLEAN-1..55 are its per-vocabulary repair rows); Vol III
\texttt{notes/antipatterns\_catalogue.md} voice-discipline entry
(2026-04-22 wave); Vol I
\texttt{notes/antipatterns\_catalogue.md} corresponding voice-discipline
AP (parallel constraint across all three volumes).

## Session antipatterns — manuscript hygiene (2026-04-22)

**Standing principle** (from CLAUDE.md of all three volumes). The manuscript is self-complete, self-coherent, self-consistent. The current version stands for itself and only itself. All reader-facing LaTeX is standalone and up-to-date. No references to previous versions, intermediate ansätze, earlier drafts, retracted values, superseded formulas, or drafting-history commentary. When a mathematical retraction is genuinely informative, state the failed argument and its Gap/Flaw as mathematics, not as drafting record. Bookkeeping, meta-narration, and version-history apparatus belong in `notes/`, `FRONTIER.md`, commit messages, and `memory/` — never in the manuscript.

Conservative scope reminder. `cascade`, `homological retraction`, `deformation retract`, `retracts onto` are legitimate mathematical terms. `Borcherds programme` is legitimate (proper noun). `Platonic solid` is legitimate. Forbidden forms: `Platonic Theorem~A`, `our programme`, `programme-canonical`, `platonic chapter`, `\begin{warning}`, `\ClaimStatusRetracted`, `narrative counterpart`, `History of the claim`, drafting-dated remarks.

### Group A — Bookkeeping vocabulary

| Code | Pattern | Why it fails | Canonical repair |
|---|---|---|---|
| CGCLEAN-1 | `Wave $N$` / `Wave-$N$ / W$N$` in manuscript prose | Session-tracking label; the manuscript is timeless | Delete the label; if the content is a real mathematical result, state the theorem directly with its canonical name |
| CGCLEAN-2 | `AP-CY$n$` / `AP$n$` / `AP-CAT-$N$` in manuscript prose | Antipattern registry index; belongs in notes/, not LaTeX | Delete the bracketed code; if the underlying mathematical hazard is load-bearing, inscribe the hazard as a Remark or scope statement |
| CGCLEAN-3 | `FM$n$` (formula-mechanical marker) in manuscript | Hook / cache index; not a mathematical object | Delete; replace with the named mathematical content |
| CGCLEAN-4 | `HZ-$N$` / `HZ-IV` / `HZ discipline` in manuscript | Internal hierarchy label | Delete; replace with the actual hierarchy (primary source > direct computation > build system, stated in-line if relevant) |
| CGCLEAN-5 | `DNA strand S$x$` / `S-strand` in manuscript | Swarm-workflow metaphor | Delete; inscribe the mathematical content without the workflow layer |
| CGCLEAN-6 | `CG-rectify pass $k$` / `rectification pass $N$` in manuscript | Drafting workflow artefact | Delete; if rectification changed the content, the current text already reflects it |
| CGCLEAN-7 | `cache entry $n$` / `Cached Confusion` / `Cache anchor` / `Cache append` in manuscript | `notes/` apparatus leak | Delete; cite the primary mathematical reference instead |
| CGCLEAN-8 | `Wave $N$ spec` / `Wave $N$ verdict` / `Wave $N$ witnessing` in manuscript | Session-audit meta-language | Delete; the verdict is the mathematical statement that survives |
| CGCLEAN-9 | `programme-canonical` / `programme canonical value` | Meta-registry term; the manuscript has canonical values, not "programme-canonical" values | Replace with "canonical" or delete the adjective; the value stands for itself |
| CGCLEAN-10 | `type-error registry entry T$n$` / `type-error T$n$` | Registry index | Delete; if a genuine type error is the point, describe it as a mathematical mismatch (e.g., "CoHA is $E_1$-associative; the bar complex is a coalgebra") |

### Group B — Meta-narration

| Code | Pattern | Why it fails | Canonical repair |
|---|---|---|---|
| CGCLEAN-11 | `narrative counterpart` / `narrative arc` | Signals prose-as-explanation rather than mathematics-as-construction | Delete; replace with a direct mathematical statement of the construction |
| CGCLEAN-12 | `story` / `saga` / `odyssey` / `journey` (as nouns in manuscript prose) | Narrates author's intent instead of stating the theorem | Delete the noun; state the result |
| CGCLEAN-13 | `Platonic ideal` / `Platonic form` / `platonic chapter` / `platonic architecture` / `Platonic ensemble` / `platonic synthesis` in manuscript | "Platonic" is a workflow/aspirational tag, not a mathematical adjective | Delete; the chapter either inscribes the structure or does not |
| CGCLEAN-14 | `Platonic Theorem~A` / `Platonic Theorem~B` etc. | Theorems are named, not platonicised | Replace with "Theorem~A" (with the canonical reference) |
| CGCLEAN-15 | `This chapter's function is to...` / `The function of this section is...` | Meta-narration of authorial intent | Delete; the chapter performs its function by being read |
| CGCLEAN-16 | `we now turn to` / `having established` / `let us now` / `this brings us to` / `with this in hand` | Signpost phrases | Replace with a direct mathematical transition or a single-sentence summary of what is proved next |
| CGCLEAN-17 | `in the present work` / `the author` / `our programme` / `we have argued` / `it is worth noting` | Self-referential authorial voice | Delete; the work is the manuscript, not a framing around it |
| CGCLEAN-18 | Meta-paragraphs like `This chapter closes the ...` | Closing narration | Delete; if the section boundary earns three sentences, those sentences should be mathematics (what was established, what is the next obstruction, what resolves it) |
| CGCLEAN-19 | `the opening paragraphs of this preface` / `as noted in the preface` | Cross-reference within own manuscript via drafting geography | Replace with a theorem / section label cross-reference (`\ref{thm:...}` / `\S\ref{sec:...}`) |
| CGCLEAN-20 | `Earlier in the volume` / `Later in the volume` | Drafting-order navigation | Replace with the actual label or delete if redundant |

### Group C — Version-history

| Code | Pattern | Why it fails | Canonical repair |
|---|---|---|---|
| CGCLEAN-21 | `retracted` / `retraction` / `now retracted` / `the retracted $X$` in manuscript | Drafting history; the manuscript is the current version | Delete the retracted claim and its retraction both; only the live claim remains |
| CGCLEAN-22 | `superseded` / `supersedes` / `superseded by` in manuscript | Drafting history | Delete; cite the correct current result as the single statement |
| CGCLEAN-23 | `earlier draft` / `previous version` / `intermediate ansatz` / `prior derivation` | Drafting history | Delete; state only the current derivation |
| CGCLEAN-24 | `previously conjectural` / `previously open` / `previously unresolved` / `previously obstructing` | Temporal status markers | Delete "previously"; state the current status directly |
| CGCLEAN-25 | `now resolved` / `now proved` / `now known` | Temporal status marker | Delete the temporal qualifier; state the result |
| CGCLEAN-26 | `double-retraction` / `triple-retraction` | Drafting history | Delete; state the mathematics that survives |
| CGCLEAN-27 | `Three successive evaluations appear in the drafting record` / `History of the claim` | Explicit drafting-record exposition | Delete entirely; if the failed arguments are informative, state each as a Gap/Flaw lemma with its mathematical obstruction, not as "evaluation $k$" |
| CGCLEAN-28 | `drafting record` / `drafting trajectory` / `drafting history` | Self-narration of the process | Delete |
| CGCLEAN-29 | `\ClaimStatusRetracted` tag / environment | Retraction status embedded in tag system | Remove the tag; if the claim is wrong, delete it; if the failure is load-bearing, inscribe a named Gap/Flaw lemma |
| CGCLEAN-30 | Dated remarks (`2026-04-17`, `Wave 14 verdict`, etc.) in manuscript prose | Drafting timestamps | Delete the date; the statement is timeless |
| CGCLEAN-31 | `\index{retraction!...}` entries | Retraction-indexed navigation | Remove; indexing should be mathematical (`\index{Borcherds product}`, not `\index{retraction!$c_3$}`) |

### Group D — Bookkeeping-content references

| Code | Pattern | Why it fails | Canonical repair |
|---|---|---|---|
| CGCLEAN-32 | `\texttt{notes/...}` as a reader-facing reference | `notes/` is not reader-facing apparatus | Either (a) promote the content to the manuscript if load-bearing, or (b) delete the reference |
| CGCLEAN-33 | Absolute home paths `/Users/raeez/...` in manuscript | Personal filesystem path | Replace with a repo-relative label, a `\ref`, or delete |
| CGCLEAN-34 | `% TODO: librarian verification` / author-note comments | Editorial comment | Delete; either verify and inscribe, or remove the claim |
| CGCLEAN-35 | `% ALIAS` / `% LEGACY ALIAS` comments | Label-rename bookkeeping | Delete the alias comment; if a label rename is needed, change the label and run references |
| CGCLEAN-36 | `% Source: NEW CHAPTER` / `% Source: Wave N` markers | Provenance comments | Delete |
| CGCLEAN-37 | Compute-engine filenames like `*_waveN_*.py` cited in manuscript | Session-indexed filename leaks | Rename the engine to drop `waveN`; cite by canonical descriptive name |
| CGCLEAN-38 | Function names `waveN_foo` cited in manuscript | Session-indexed function leak | Rename; cite the canonical mathematical functionality |

### Group E — Warning / hedge environments

| Code | Pattern | Why it fails | Canonical repair |
|---|---|---|---|
| CGCLEAN-39 | `\begin{warning} ... \end{warning}` environment | Warnings hedge the mathematics; the manuscript either proves or conjectures, never warns | Replace with a `\begin{remark}` that states the mathematical scope cleanly, or delete if the scope is already carried by the theorem hypotheses |
| CGCLEAN-40 | `do not confuse` / `don't be fooled` / `beware` / `be careful` | Hedging / scolding the reader | Delete; the reader confuses nothing if the mathematics is stated with sufficient precision |
| CGCLEAN-41 | `we must be careful` | Self-hedging | Delete; state the scope, do not announce caution |
| CGCLEAN-42 | gratuitous `scope-restricted` / `scope-bounded` as adjectives | Meta-scope commentary | Delete; state the actual scope ("on the Koszul locus", "for affine $A$", etc.) |
| CGCLEAN-43 | `verdict` as a label for a mathematical statement | Meta-adjudication language | Replace with `theorem`, `proposition`, `lemma`, `corollary`, or `remark` as appropriate |

### Group F — Structural meta-naming

| Code | Pattern | Why it fails | Canonical repair |
|---|---|---|---|
| CGCLEAN-44 | Chapter filename `*_platonic.tex` | File-level meta-tag | Rename to the canonical mathematical content; update `\input` in `main.tex` |
| CGCLEAN-45 | Chapter label `ch:*-platonic` | Label-level meta-tag | Rename to `ch:*` matching the content; update all `\ref` |
| CGCLEAN-46 | Section label `sec:*-platonic` | Label-level meta-tag | Rename to `sec:*`; update all `\ref` |
| CGCLEAN-47 | Theorem label `thm:*-waveN-*` | Label carries session index | Rename to the canonical mathematical content; update `\ref` |
| CGCLEAN-48 | `\index{compute module!...}` entries | Index entry for internal compute apparatus | Remove; the manuscript indexes mathematics |
| CGCLEAN-49 | `\index{cache!...}` entries | Index entry for the cache registry | Remove |
| CGCLEAN-50 | `\index{retraction!...}` entries | Retraction navigation | Remove |

### Group G — Edge cases

| Code | Pattern | Why it fails | Canonical repair |
|---|---|---|---|
| CGCLEAN-51 | `Five attack-heal calibrations` | Swarm-workflow count | Delete; if five theorems or five checks are the substance, list the five objects, not the five calibrations |
| CGCLEAN-52 | `Reconstitution if the cancellation fails` | Workflow-contingent phrasing | Delete; state either the cancellation theorem or the obstruction lemma as live mathematics |
| CGCLEAN-53 | `Inversion of the programme perspective` | Meta-framing | Delete; state the dual construction directly |
| CGCLEAN-54 | `Gold-standard HZ-IV disjoint verification` | Epistemic-hierarchy-label meta-claim | Delete; if the verification is multi-path, list the paths (direct computation, primary source, build test) as three concrete checks |
| CGCLEAN-55 | `Three successive evaluations appear in the drafting record` (verbatim) | Direct drafting-record callout | Delete; if a Gap/Flaw triptych is mathematically useful, inscribe as three named lemmas with their precise obstructions |

**Cross-references.** These 55 entries appear in parallel across the three volumes. Vol I: `notes/antipatterns_catalogue.md` session entry (2026-04-22) with identical codes CGCLEAN-1..55; Vol III: same. Cache entries in `notes/first_principles_cache_comprehensive.md` (this volume) register the regex + 5-step DETECT/LOCALISE/MATH-CHECK/REPAIR/VERIFY protocol. Reader-oriented summary rows in `notes/first_principles_cache.md`. Hook signatures in `.claude/hooks/beilinson-gate.sh` (violation codes CGCLEAN-1..55).

## Section 14: Cross-programme imports from Vol III wave-12 synthesis (2026-04-22)

The following entries propagate Vol III wave-12 crystallisations not
already covered by AP-V2-25--29 (Vol III two-stage factorisation
family, manifesto conflations, structural voice discipline). Each
entry names the Vol III wave-12 source file and pins the precise scope
at which the underlying mathematics binds Vol II content. Numbering
continues from AP-V2-29 without gaps.

### AP-V2-30 / V2-AP133: Pattern 273 — chain-level statement vs $(\infty,1)$-categorical functor claim on $(B_{E_1}, B_{E_2}, B_{E_\infty})$
**Severity**: Critical
**Trigger**: Vol II's three-sector bar complex
$(B_{E_1}, B_{E_2}, B_{E_\infty})$ stated as an equivalence of
$(\infty,1)$-categories without a proof of morphism preservation; or
any wording that conflates the chain-level filtered quasi-isomorphism
$B_{E_1}A \twoheadrightarrow B_{E_2}A \twoheadrightarrow B_{E_\infty}A$
with an ambient $(\infty,1)$-categorical-functor claim.
**Ghost**: the chain-level filtered equivalence is a genuine theorem
at the explicit complex level, carrying the Kontsevich--Tamarkin
$E_d$-formality inputs and the Costello--Li holomorphic-locality
inputs (AP-V2-33). The $(\infty,1)$-categorical-functor statement is
a distinct claim on morphism spaces that has not been established in
full generality; it is the functorial lift of the chain-level
filtered equivalence to an $(\infty,1)$-categorical map between bar
constructions of chiral-topological algebras.
**Precise error**: Pattern 273 scope conflation (chain-level vs
$(\infty,1)$-categorical functor). Neither lane subsumes the other;
the chain-level statement supports explicit factorisation-algebra
readings of $\mathsf{SC}^{\mathrm{ch,top}}$, the
$(\infty,1)$-categorical claim would support ambient functorial
pushforwards. Merging the two loses precision at the exact site where
Beilinson's dictum operates (chain-level proofs are auditable against
primary sources; $(\infty,1)$-categorical claims are auditable against
Lurie *Higher Algebra* and Francis 2013 in restricted scopes).
**Correction**: state the filtered equivalence as a chain-level
theorem with explicit inputs (Kontsevich--Tamarkin $E_d$-formality,
Drinfeld associator choice, Costello--Li holomorphic locality). Tag
any $(\infty,1)$-functor lift as conjectural and named
(AP-V2-36). Both readings are load-bearing at their precise scopes;
neither is a shadow of the other.
**Primary**: Kontsevich 2003 *Lett Math Phys* 66 (formality); Tamarkin
2003 *Lett Math Phys* 66 (GRT and formality); Costello--Li 2016
arXiv:1605.09439 (holomorphic locality); Francis 2013 *Compositio* 149
(factorisation homology).
**Inscription**: `chapters/theory/bar_chain_models.tex`; Vol III
wave-12 source `notes/wave12_a1_bar_cobar_gelfand.tex`; Vol III
`notes/wave12_a1_phi_functor_foundations.tex` (chain-level vs
functorial scope in the $\Phi$-construction).
**Cross-ref**: Vol III AP-CY Pattern 273; Vol I Pattern 273 cross-ref
hook; Vol II AP-V2-1 (eight bar-cobar ambients) sets the chain-level
home for this filtered equivalence; AP-V2-36 (frontier conjectural
lift).

### AP-V2-31 / V2-AP134: Bare $\kappa$ without subscript in chiral-topological statements
**Severity**: Critical
**Trigger**: any Vol II inscription containing $\kappa$ without a
$\mathrm{ch}/\mathrm{cat}/\mathrm{BKM}/\mathrm{fiber}$ subscript, in
prose, theorem statement, equation, or label.
**Ghost**: four genuinely distinct invariants track four different
mathematical structures on a CY-to-chiral datum. $\kappa_{\mathrm{ch}}$
is the chiral-side Hodge supertrace via $\Phi$.
$\kappa_{\mathrm{cat}} = \chi(\mathcal O_X)$ is
Künneth-multiplicative on products; $\kappa_{\mathrm{cat}}(K3 \times E)
= 0$ on the total space, NOT $2$ (which is $\kappa_{\mathrm{fiber}}(K3)$,
a different object on a different domain). $\kappa_{\mathrm{BKM}}(\Phi_N)
= c_N(0)/2$ is the Borcherds weight; at $N=1$ this is $5$ for the
paramodular $\Delta_5$ convention or $12$ for the Fake-Monster
$\Phi_{12}$ convention (AP5 dual-indexing).
$\kappa_{\mathrm{fiber}}$ is the fibre/lattice correction. Each
satisfies a different functoriality and enters a different face of
$r_{\mathrm{CY}}$.
**Precise error**: bare $\kappa$ collapses four distinct objects into
one symbol. On the $\mathsf{SC}^{\mathrm{ch,top}}$ Swiss-cheese
reading of $\mathbf H_{\Delta_5}$, substituting one for the other
silently forces wrong Borcherds-product denominators. The three-faces
identity AP-V2-20 requires subscripted $\kappa$ to triangulate
correctly across Vol I / Vol II / Vol III.
**Correction**: every $\kappa$ in Vol II carries its subscript from
the first keystroke. At cross-volume linking points (Theorem C
five-archetype table, three-faces universal identity, Borcherds-weight
anchor), pin the subscript to the site it enters through. AP-V2-22
B-row coupling $\kappa + \kappa^! = 8$ is precise only under the
subscripted reading.
**Primary**: Vol III CLAUDE.md and
`chapters/examples/cy_d_kappa_stratification.tex`; Borcherds 1995
*Invent Math* 120; Gritsenko 1999 *Algebra i Analiz* 11.
**Inscription**: all Vol II chapters touching the CY-to-chiral face;
Vol III wave-12 source
`notes/wave12_a2_kappa_invariants_universal_borcherds.tex`.
**Cross-ref**: Vol III AP-CY bare-$\kappa$ family and HZ-7 subscript
discipline; Vol I bare-$\kappa$ AP hook; Vol II
`first_principles_cache.md` canonical preamble rows 59--62 and 65--66
for the four $\kappa_\bullet$ values; AP-V2-28 (manifesto conflations
inherited from Vol III) names the $\kappa_{\mathrm{cat}}(K3 \times E)
= 2$ retraction.

### AP-V2-32 / V2-AP135: $\mathrm{CoHA}(\mathbb C^3) = Y^+$ as evaluation image, not $\mathcal W_{1+\infty}$ isomorphism
**Severity**: Critical
**Trigger**: Vol II inscription identifying the
cohomological-Hall-algebra image of $\mathbb C^3$ with
$\mathcal W_{1+\infty}$, or implying the Schiffmann--Vasserot arrow
is an isomorphism rather than a map to the positive half of the
affine Yangian.
**Ghost**: Schiffmann--Vasserot 2012 / 2020 identify
$\mathrm{CoHA}(\mathbb C^3) = Y^+(\widehat{\mathfrak{gl}}_1)$, the
positive half of the affine Yangian. The image in
$\mathcal W_{1+\infty}$ exists via an evaluation arrow that factors
through a further quotient and is only an isomorphism at the classical
/ $\hbar = 0$ limit. Miki $S_3$-triality on $Y^+$ pins the
$\mathcal W_{1+\infty}$ slice; the curved-Dunn $H^2 = 0$ closure
question (AP-V2-34) is the extension-ladder problem for pulling
$\mathcal W_{1+\infty}$ back to the chiral-topological Vol II site.
**Precise error**: treating the evaluation arrow $Y^+ \to
\mathcal W_{1+\infty}$ as an isomorphism; missing the Miki triality
structure on $Y^+$ (Miki 2007 generators); collapsing the extension
ladder between $Y^+$, $\mathcal W_\infty[c]$, and
$\mathcal W_{1+\infty}$ into a single line.
**Correction**: state $\mathrm{CoHA}(\mathbb C^3) = Y^+$;
$\mathcal W_{1+\infty} = $ image of the evaluation slice under
Miki-triality; $\mathcal W_{1+\infty} = \mathcal W_\infty[c] \otimes
\mathcal H$ as a tensor with the Heisenberg algebra (preamble row 63).
Curved-Dunn closure is a separate chiral-topological step with
$H^2$-obstruction living in the Costello--Gwilliam BV cohomology of
the Vol II factorisation assembly.
**Primary**: Schiffmann--Vasserot 2012 *Publ IHES* 115; Schiffmann--
Vasserot 2020 *Duke Math J* 169; Pope--Romans--Shen 1990 *Phys Lett B*
236; Miki 2007 *J Math Phys* 48; Costello--Gwilliam 2021 Vol 2 (BV
curved Dunn).
**Inscription**: `chapters/theory/coha_chiralisation.tex`; Vol III
wave-12 source `notes/wave12_a11_coha_y_plus_vs_w_infty.tex`.
**Cross-ref**: Vol II AP-V2-18 (MO-extension super-quasi-Hopf) via
the $Y^+$ side; Vol III AP-CY CoHA-vs-vertex-algebra family;
`first_principles_cache.md` canonical preamble rows 62--63; AP-V2-28
(manifesto conflations inherited from Vol III, CoHA row).

### AP-V2-33 / V2-AP136: Canonical chiral algebra is a conjunction of Costello--Li and Kontsevich--Tamarkin
**Severity**: High
**Trigger**: Vol II inscription citing either Costello--Li holomorphic
locality or Kontsevich--Tamarkin $E_d$-formality as the sole input to
the "canonical chiral algebra on $X$", treating one as sufficient.
**Ghost**: Costello--Li 2016 establishes holomorphic locality of
$\Phi$ on a CY datum (inputs from the Costello--Gwilliam BV
framework); Kontsevich--Tamarkin $E_d$-formality establishes rigidity
of the formality quasi-isomorphism on Hochschild complexes. Both are
load-bearing and both enter the canonical chiral algebra construction.
Neither is a shadow of the other; holomorphic locality without
formality produces a chain-level cocycle without homotopy control;
formality without holomorphic locality produces a rigidity statement
without the specifically-holomorphic factorisation structure.
**Precise error**: single-citation treatment allows silently dropping
a load-bearing input. The $\mathsf{SC}^{\mathrm{ch,top}}$ Vol II
assembly uses both inputs at distinct stages of the Dunn--curved-Dunn
tower; citing only one hides where the other enters.
**Correction**: the canonical chiral algebra is the conjunction of
Costello--Li holomorphic locality on a factorisation datum AND
Kontsevich--Tamarkin formality on its Hochschild cochains. Inscribe
both as hypotheses; at stage transitions (AP-V2-25), name which input
supports which stage.
**Primary**: Costello--Li 2016 arXiv:1605.09439; Kontsevich 2003
*Lett Math Phys* 66; Tamarkin 2003 *Lett Math Phys* 66; Francis 2013
*Compositio* 149.
**Inscription**: `chapters/theory/canonical_chiral_algebra.tex`; Vol
III wave-12 source `notes/wave12_a1_phi_functor_foundations.tex`.
**Cross-ref**: Vol II AP-V2-6 (Kontsevich formality scope); AP-V2-25
(stage-1/stage-2 identification); AP-V2-30 (chain vs $(\infty,1)$-
functor); Vol III Pattern 273 / Pattern 236.

### AP-V2-34 / V2-AP137: $E_n$ on the wrong object — $A$ is $E_1$ at $d \ge 3$; $E_2$ lives on $Z(\mathrm{Rep}(A))$
**Severity**: Critical
**Trigger**: Vol II inscription asserting an $E_2$- or $E_n$-algebra
structure directly on $A$ for a CY$_d$ input at $d \ge 3$, or claiming
Dunn additivity produces an $E_2$-bracket on $A$ itself.
**Ghost**: at $d \ge 3$, the $\Phi$-image $A$ is $E_1$-associative
(chiral-associative on a punctured complex disc); the $E_2$-structure
lives on the Drinfeld centre $Z(\mathrm{Rep}(A))$, not on $A$. The
Swiss-cheese $\mathsf{SC}^{\mathrm{ch,top}}$ closed colour is $E_2$
on the braided-monoidal representation category, not on the
associative algebra directly.
**Precise error**: categorical-layer confusion. Dunn additivity
$\int_{\mathbb R^2} E_1 \simeq E_2$ raises $E_1$ on a $0$-dimensional
input to $E_2$ on a $2$-dimensional integral; at $d \ge 3$ the
integration target shifts and the $E_2$ lives on
$Z(\mathrm{Rep}(A))$, visible through the Deligne conjecture and
categorical Hochschild. Placing $E_2$ on $A$ collapses the
Drinfeld-centre face of $r_{\mathrm{CY}}$ and forces nonsensical
monoidal conditions on an $E_1$-algebra.
**Correction**: label every chiral-topological $E_n$-assertion with
the object it sits on. $A$ itself: $E_1$-associative at $d \ge 3$.
$Z(\mathrm{Rep}(A))$: $E_2$-braided. $\mathsf{SC}^{\mathrm{ch,top}}$
closed colour at $d \ge 3$: $E_2$ on $Z(\mathrm{Rep}(A))$, not on $A$.
At $d = 2$, $A$ itself carries $E_2$-structure via the PTVV row
$(d, \mathrm{shift}, E_n^{\mathrm{cl}}) = (2, -2, E_2)$; the
categorical layering is $d$-dependent.
**Primary**: Lurie *Higher Algebra* Ch 5 (Dunn); Francis 2013
*Compositio* 149; Ayala--Francis 2015 (factorisation homology on
stratified spaces).
**Inscription**: `chapters/theory/e_n_hierarchy_dimensional.tex`; Vol
III wave-12 source `notes/wave12_a8_en_hierarchy_kapranov.tex`.
**Cross-ref**: Vol III AP-CY $E_n$-output-scope family; Vol I Pattern
236 ambient discipline; Vol II AP-V2-1 (Swiss-cheese closed colour
carries the right $E_2$ scope only on $Z(\mathrm{Rep}(A))$ at $d \ge 3$);
AP-V2-37 (the $E_2$-braiding specialisation of this AP).

### AP-V2-35 / V2-AP138: PTVV $d$-dependent shift table $(d, \mathrm{shift}, E_n^{\mathrm{cl}})$
**Severity**: Critical
**Trigger**: Vol II inscription treating the PTVV shift as
$d$-independent in the chiral-topological specialisation, or stating a
single uniform $\Phi$-output type across CY dimensions.
**Ghost**: the CY-to-chiral functor output is dimensionally stratified
by a shifted-symplectic PTVV input of degree $2 - d$. At $d = 2$ shift
$-2$, classical limit $E_2$-Poisson; at $d = 3$ shift $-1$,
$E_1$-Poisson; at $d = 4$ shift $0$, $E_0$-Poisson; at $d = 5$ shift
$+1$, $E_5$-Poisson and the direction reverses. The table
$(d, \mathrm{shift}, E_n^{\mathrm{cl}}) \in \{(2,-2,E_2), (3,-1,E_1),
(4,0,E_0), (5,+1,E_5\text{-Poisson})\}$ controls the Vol II
chiral-topological specialisation on each row.
**Precise error**: uniform $\Phi$-output treatment erases the PTVV
staircase and collapses the three-faces universal identity (AP-V2-20)
into a single-shift identity, losing the $d$-dependent matching
between shift, $E_n$-class, and Quillen exponent.
**Correction**: every $\Phi$-application carries the $d$-subscript
$\Phi_d$ and the associated $(d, \mathrm{shift}, E_n^{\mathrm{cl}})$
triple. At cross-volume linking points, pin the row; the K3 $\times$ E
site sits at $d = 3$ via AP-V2-25.
**Primary**: Pantev--Toën--Vaquié--Vezzosi 2013 *Publ IHES* 117 (PTVV);
Costello--Gwilliam 2021 Vol 2 §3 (BV version of PTVV); Calaque--Pantev--
Toën--Vaquié--Vezzosi 2017 *Selecta Math* 23.
**Inscription**: `chapters/theory/ptvv_staircase.tex`; Vol III wave-12
source `notes/wave12_a1_phi_functor_foundations.tex`.
**Cross-ref**: Vol III $\Phi$-output-scope family; Vol II AP-V2-14
(generic CY-4 $\Phi_4$ existence) uses row $d = 4$ shift $0$;
AP-V2-20 three-faces identity carries row-specific Quillen exponents;
AP-V2-34 ($E_n$-on-wrong-object) depends on this row.

### AP-V2-36 / V2-AP139: Dunn--Lurie $\int_{\Sigma_2} E_3 \simeq E_1$ real-vs-complex conflation
**Severity**: High
**Trigger**: Vol II inscription transporting Dunn--Lurie additivity
$\int_{\Sigma_2} E_3 \simeq E_1$ to a holomorphic setting without
separating real and complex integration dimensions, or applying the
real-dimension additivity count to a complex curve without tracking
the transverse normal bundle.
**Ghost**: Dunn--Lurie additivity is a real-dimension statement:
$\int_{\mathbb R^2} E_3 \simeq E_1$ uses real-dimension-$2$
integration. In the holomorphic chiral-topological setting,
integration is along a complex curve $C$ of complex dimension $1$ =
real dimension $2$ with transverse normal bundle $N_C$ of complex
codimension $d - 1$; the additivity bookkeeping must keep real and
complex dimensions explicit, and the transverse normal bundle enters
the $E_n$-count via the $\mathrm{Td}(N_C)$ factor.
**Precise error**: slip between real and complex dimensions: writing
$\int_{C} E_3 \simeq E_1$ as a clone of the real Dunn--Lurie identity
without the transverse normal-bundle correction silently omits the
holomorphic-versus-smooth distinction and gives wrong $E_n$-types in
the Swiss-cheese closed colour. The MIXED-operation
$\int_{\Sigma_{d-1}}$ of AP-V2-25 is specifically the
holomorphic-factorisation-homology pushforward, not the smooth
Dunn--Lurie integral.
**Correction**: Vol II chiral-topological integrals are written
$\int^{\mathrm{hol}}_{C} E_n \simeq E_{n-2}$ with explicit
$\mathrm{Td}(N_C)$ and normal-bundle weighting, labelling real- vs
complex-dimension at every step. Dunn--Lurie remains the ambient
real-dimension additivity statement; the holomorphic refinement is
Costello--Li holomorphic factorisation homology.
**Primary**: Lurie *Higher Algebra* Thm 5.1.2.2 (Dunn); Costello--Li
2016 arXiv:1605.09439 (holomorphic locality); Francis 2013
*Compositio* 149.
**Inscription**: `chapters/theory/holomorphic_dunn.tex`; Vol III
wave-12 source `notes/wave12_f2_bv_brst_to_chiral_ce.tex`.
**Cross-ref**: Vol II AP-V2-34 ($E_n$-on-wrong-object); Vol III
$E_n$-output-scope family; Vol I Pattern 236 ambient discipline;
AP-V2-25 MIXED operation as the holomorphic pushforward.

### AP-V2-37 / V2-AP140: Iterated-Sugawara $\mathcal W_{1+\infty}$-endpoint conjecture — chain-level scope with three inputs
**Severity**: High (conjectural; tag \ClaimStatusConjectured)
**Trigger**: Vol II inscription asserting the iterated-Sugawara
$\mathcal W_{1+\infty}$ endpoint as a theorem without naming the three
load-bearing inputs: Miki $S_3$-triality on $Y^+$, $\mathcal W_{1+\infty}$
as the evaluation slice, and curved-Dunn $H^2 = 0$ closure.
**Ghost**: the proposed endpoint composes three structures. (i) Miki
$S_3$-triality on $Y^+(\widehat{\mathfrak{gl}}_1)$ pins the
$\mathcal W_{1+\infty}$ slice inside $Y^+$; (ii)
$\mathcal W_{1+\infty}$ is the evaluation-slice image of $Y^+$ under
the Schiffmann--Vasserot arrow (AP-V2-32); (iii) curved-Dunn $H^2 = 0$
closure is the Costello--Gwilliam BV condition that the curved-Dunn
assembly of the Vol II chiral-topological factorisation algebra lifts
$\mathcal W_{1+\infty}$ to the iterated-Sugawara tower without anomaly.
**Precise error**: treating the endpoint as a single citation-level
theorem glosses all three inputs; each is independently load-bearing
and independently conjectural at present.
**Correction**: state the endpoint as a conditional theorem. "If
(i)-(ii)-(iii) hold, then the Vol II chiral-topological iterated-
Sugawara tower converges to $\mathcal W_{1+\infty}$ via the curved-Dunn
closure." Tag \ClaimStatusConjectured until the three inputs are
independently verified. The chain-level formulation is where each
input can be checked directly.
**Primary**: Miki 2007 *J Math Phys* 48 (triality); Schiffmann--
Vasserot 2020; Costello--Gwilliam 2021 Vol 2 §4 (curved Dunn).
**Inscription**: `chapters/frontier/w_infty_endpoint_conjecture.tex`;
Vol III wave-12 source `notes/wave12_a11_coha_y_plus_vs_w_infty.tex`.
**Cross-ref**: Vol II AP-V2-32 (CoHA evaluation scope); AP-V2-37 flag
propagates to AP-V2-38 (class M $E_3$-bar cohomology) via the closure
hypothesis; AP-V2-41 (frontier conjectural bar-filtered equivalence).

### AP-V2-38 / V2-AP141: Class $\mathbf M$ $E_3$-bar cohomology is $6^g$ with per-handle tricomplex $P_{E_4}(t) = 3t + 3t^2$
**Severity**: High
**Trigger**: Vol II inscription asserting class-$\mathbf M$ $E_3$-bar
is infinite at cohomology, or finite at chain level, at genus
$g \in \{1, 2, 3\}$.
**Ghost**: class-$\mathbf M$ $E_3$-bar has chain-level
infinite-dimensional and cohomology $6^g$-dimensional via the kernel
of $d_4$ on the single-generator tricomplex with per-handle Poincaré
polynomial $P_{E_4}(t) = 3t + 3t^2$. The factor $6$ per handle is the
closed-form Euler-characteristic count $2 \cdot 3$ with sign
discipline; the $6^g$-scaling matches the genus-$g$ tensor power of
the per-handle profile. The wave-12 contribution is the explicit
tricomplex that AP-V2-21 named without unpacking.
**Precise error**: lane conflation (cf.\ AP-V2-21), strengthened by
the explicit tricomplex structure from wave-12. Treating the
$6^g$-count as a chain-level count, or the infinite-dimensional
chain level as the cohomological answer, gives wrong genus-scaling in
either direction.
**Correction**: cohomology is $6^g$, chain level infinite; state both
lanes and the spectral-sequence collapse at $d_4$, with the per-handle
Poincaré polynomial $P_{E_4}(t) = 3t + 3t^2$ written explicitly.
**Primary**: Francis 2013 *Compositio* 149; Costello--Gwilliam 2021
Vol 2 §9.
**Inscription**: `chapters/theory/class_m_e3_bar.tex`; Vol III wave-12
source `notes/wave12_a10_class_m_e3_bar.tex`.
**Cross-ref**: AP-V2-21 (original class-M AP, strengthened here with
per-handle tricomplex); Vol III AP-CY21; Vol II
`first_principles_cache.md` canonical preamble row 65; AP-V2-41
(filtered equivalence on $E_3$-bar is the conjectural lift).

### AP-V2-39 / V2-AP142: $E_2$-braiding on $Z(\mathrm{Rep}(A))$, not on $A$
**Severity**: Critical
**Trigger**: Vol II inscription asserting an $E_2$-braiding directly
on $A$ for a chiral-topological datum at $d \ge 3$, or placing the
Drinfeld centre content on the underlying algebra rather than on its
representation category.
**Ghost**: at $d \ge 3$ the $E_2$-braided-monoidal structure lives on
the Drinfeld centre $Z(\mathrm{Rep}(A))$ (a fusion-categorical
layer), not on $A$ itself, which is $E_1$-associative. This is the
braiding-face specialisation of AP-V2-34.
**Precise error**: placing the $E_2$-braiding on the wrong
categorical layer collapses the Drinfeld-centre face of
$r_{\mathrm{CY}}$ and forces nonsensical monoidal conditions on an
$E_1$-algebra. The $\mathsf{SC}^{\mathrm{ch,top}}$ closed colour at
$d \ge 3$ acts on the centre; the open colour acts on $A$; conflating
the two destroys the two-stage factorisation of AP-V2-25.
**Correction**: state every $E_2$-braiding fact as a statement about
$Z(\mathrm{Rep}(A))$; the underlying $A$ carries $E_1$-associative
structure only. Deligne centre and categorical Hochschild are the
machine that raises $E_1$ on $A$ to $E_2$ on the centre.
**Primary**: Lurie *Higher Algebra* 5.3 (Drinfeld centre); Etingof--
Nikshych--Ostrik 2005 *Ann Math* 162; Ayala--Francis 2015.
**Inscription**: `chapters/theory/drinfeld_centre_braiding.tex`; Vol
III wave-12 source `notes/wave12_a3_MO_E2_etingof.tex`.
**Cross-ref**: AP-V2-34 ($E_n$-on-wrong-object, parent AP); Vol III
Drinfeld-centre-vs-averaging family; Vol I Pattern 236 ambient
discipline; AP-V2-25 closed-colour identification with stage-1
$\Phi^{\mathrm{FA}}_d$.

### AP-V2-40 / V2-AP143: Six routes to $G(K3 \times E)$ are six distinct constructions, NOT six $\Phi_3$-applications
**Severity**: High
**Trigger**: Vol II inscription treating the six routes (CoHA,
Schiffmann--Vasserot, Maulik--Okounkov, Borcherds, Toda, DMVV) as six
applications of a single functor $\Phi_3$ to one object, rather than
six distinct constructions on six different CY-input categories that
produce the same $\Phi_3$-output via a pentagon colimit.
**Ghost**: each of the six routes takes a different CY-input
category and a different intermediate structure (Hall, stable-envelope,
Fock-space, Borcherds-product, topological-vertex, wall-crossing) and
produces $\mathbf H_{\Delta_5} = G(K3 \times E)$ as its
$\Phi_3$-image. The pentagon that unifies them is a colimit
diagram, not a single-object application of $\Phi_3$ six times. This
is the Vol III K3$\times$E specific crystallisation; Vol II's bar-
cobar / pentagon / heptagon cross-volume readings must respect it.
**Precise error**: single-functor framing of the six routes implies
six applications of $\Phi_3$ to one CY-input category and hides the
six distinct CY-input structures.
**Correction**: name the six distinct CY-input categories and name
the pentagon colimit that produces the shared output. Each route's
$\Phi_3$-image is $\mathbf H_{\Delta_5}$; the routes agree at the
colimit, not through single-object application.
**Primary**: Schiffmann--Vasserot 2012 (CoHA); Maulik--Okounkov 2019
(stable envelope); Borcherds 1992 / Gritsenko--Nikulin 1998
(Borcherds product); Toda 2013 (DT wall-crossing); Dijkgraaf--Moore--
Verlinde--Verlinde 1997 (DMVV).
**Inscription**: `chapters/theory/six_routes_pentagon.tex`; Vol III
wave-12 source `notes/wave12_a12_six_routes_k3_e.tex`.
**Cross-ref**: AP-V2-28 (manifesto conflations, row 3); Vol III
CLAUDE.md key-facts block (six routes bullet); Vol II
`first_principles_cache.md` canonical preamble rows 59--62.

### AP-V2-41 / V2-AP144: $(B_{E_1}, B_{E_2}, B_{E_\infty})$ filtered equivalence at chain level — frontier conjecture
**Severity**: Medium (frontier open question; tag
\ClaimStatusConjectured)
**Trigger**: Vol II inscription claiming the three-sector filtered
equivalence
$B_{E_1}A \twoheadrightarrow B_{E_2}A \twoheadrightarrow B_{E_\infty}A$
as a proved theorem without naming the chain-level scope where it
could be made rigorous, or dismissing it as inaccessible without
naming that scope.
**Ghost**: the filtered equivalence is a frontier open question from
the wave-12 cross-volume synthesis. Conjecturally, the filtered
equivalence holds at chain level for $\Phi$-image algebras when the
three inputs of AP-V2-33 are assembled, with the $E_2$-layer sitting
on $Z(\mathrm{Rep}(A))$ per AP-V2-39 and the real-vs-complex dimension
discipline per AP-V2-36.
**Precise error**: asserting the equivalence as theorem without
naming filtered bar models; alternatively, dismissing it as
inaccessible without naming the chain-level site where it becomes
rigorous.
**Correction**: log as conjecture at chain level with explicit
prerequisites. Scope: for $A = \Phi_d(X)$ with $X$ a CY$_d$ datum
satisfying Costello--Li holomorphic locality and Kontsevich--Tamarkin
$E_d$-formality, the filtered bar tower $B_{E_n}A$ has graded
quotients controlled by the kernel of $d_4$ on the per-handle
tricomplex (cf.\ AP-V2-38). Chain-level verification at small $g$ and
small $d$ is the route; $(\infty,1)$-categorical-functor lift (cf.\
AP-V2-30) is a separate conjecture.
**Primary**: Francis 2013 *Compositio* 149; Kontsevich--Tamarkin
2003; Costello--Gwilliam 2021 Vol 2.
**Inscription**: `chapters/frontier/bar_filtered_equivalence_conjecture.tex`;
Vol III wave-12 source `notes/wave12_a1_bar_cobar_gelfand.tex`.
**Cross-ref**: Vol II AP-V2-30 (chain vs $(\infty,1)$-functor);
AP-V2-38 (class M $E_3$-bar cohomology supplies the per-handle
obstruction); AP-V2-33 (two-input canonical chiral algebra supplies
the prerequisite inputs); Vol III Pattern 273 / Vol I Pattern 273
hook; AP-V2-37 (iterated-Sugawara endpoint uses the same three-input
closure).

## Section 15: 6d hCS audit session antipatterns (2026-04-22)

The following eighteen APs record precise errors caught during the
2026-04-22 audit of the Vol II 6d holomorphic Chern--Simons computation
(partition function $Z_{\mathrm{hCS}}$, Feynman coefficients, Deligne
exceptional series, weak-Jacobi / Siegel / paramodular denominators,
and the Vol III two-stage factorisation alignment for the $E_3$-chiral
avatar).

### AP-V2-42 / V2-AP145: Casimir quadratic-for-quartic in 6d hCS 1-loop (2026-04-22)

**Trigger**: any Vol II 6d hCS 1-loop amplitude statement that writes
$c_2(\mathfrak g)/24$ against a 3-factor propagator integrand for the
one-loop bubble / counterterm.

**Ghost**: the 6d hCS one-loop amplitude on $\mathbb R^4 \times C$ with
colour factor $\mathrm{tr}_{\mathrm{adj}}(T^a T^b T^c T^d)$ contracts
the adjoint quartic Casimir against the four-factor
$c(\bar\partial c)^3/(2\pi i)^3$ integrand of the BV propagator
(Costello 2017 *M-theory / $\Omega$-background*; Costello--Gaiotto
2019; CFG 2026).

**Precise error**: substituting $c_2(\mathfrak g)/24$ (the quadratic
Casimir normalisation used for a 3-factor integrand) for the quartic
Casimir $\mathrm{tr}_{\mathrm{adj}}(T^{(a}T^b T^c T^{d)})$ against the
4-factor propagator integrand. The error appears at
\texttt{chapters/connections/thqg\_perturbative\_finiteness.tex:4005-4015}.
The quadratic Casimir contracts an $(a, b)$ pair; the 6d hCS
one-loop amplitude requires the symmetric quartic invariant on the
adjoint because the Feynman graph has four external colour legs and
three internal propagators, giving the $c(\bar\partial c)^3/(2\pi i)^3$
weight.

**Correction**: replace $c_2(\mathfrak g)/24 \cdot (\cdots 3\text{-factor})$
with $\mathrm{tr}_{\mathrm{adj}}(T^{(a}T^b T^c T^{d)}) \cdot (\cdots
c(\bar\partial c)^3/(2\pi i)^3 )$, where the symmetrisation runs over
the four colour indices and $\bar\partial c$ is the BV propagator
one-form on $\mathrm{Conf}_2(\mathbb C^3)$ restricted to the one-loop
fibre. The anomaly-cancellation condition reduces to the vanishing
of $\mathrm{tr}_{\mathrm{adj}} T^{(a} T^b T^c T^{d)}$ on the Deligne
exceptional series except $E_6$ (see AP-V2-54 below).

**Severity**: Critical. The error propagates into every downstream
anomaly and 1-loop-finiteness claim. Per-sweep when editing 6d hCS
amplitude computations.

**Primary**: Costello 2017 arXiv:1610.04144 "M-theory in the
$\Omega$-background and 5d/4d correspondence"; Costello--Gaiotto
2019 arXiv:1812.05516 "Twisted supergravity and Koszul duality";
Costello--Francis--Gaiotto 2026 (6d hCS one-loop formulae, in
preparation as of the 2026-04-22 audit); Costello--Gwilliam 2021
*Factorization Algebras Vol 2* §9-11 (BV propagator conventions).

**Cross-ref**: \texttt{chapters/connections/thqg\_perturbative\_finiteness.tex:4005-4015}
(error site); V2-AP54 / AP-V2-54 (Deligne-safe anomaly list); V2-AP146
/ AP-V2-43 (theta-graph two-loop miscount); V2-AP149 / AP-V2-49
($E_1$-per-$\mathbb C$ Dunn scope); Canonical preamble rows 59-66
($\kappa_\bullet$ indexing).

### AP-V2-43 / V2-AP146: Feynman graph Euler miscount — theta labelled 1-loop (2026-04-22)

**Trigger**: any Vol II Feynman graph labelling that tags the theta
graph ($V = 2$, $E = 3$) as 1-loop, or asserts a 2-leg 1-loop
amplitude with three internal edges.

**Ghost**: for a connected Feynman graph, Euler's relation
$V - E + L = 1$ (equivalently, $L = 1 + E - V$) gives the loop number
$L$; the theta graph has $V = 2$, $E = 3$ and therefore $L = 2$. The
1-loop 2-leg amplitude is the bubble graph ($V = 2$, $E = 2$,
$L = 1$). This is undergraduate-level Feynman graph topology; the
error is a bookkeeping slip, not a framework failure.

**Precise error**: site
\texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:120-122}
labels the theta graph (two vertices connected by three parallel
edges) as 1-loop. Correct count: $L = 1 + E - V = 1 + 3 - 2 = 2$;
the theta is 2-loop. The 1-loop 2-leg graph is the bubble
($V = 2$, $E = 2$, $L = 1$), which is topologically distinct and
has a different symmetry factor.

**Correction**: retag the theta graph as 2-loop; reassign the
1-loop 2-leg amplitude to the bubble graph. The symmetry factors
and integral measures change accordingly (theta: symmetry factor
$1/12$ over $S_3 \times \mathbb Z_2$; bubble: $1/2$ over $\mathbb Z_2$).

**Severity**: High. Propagates into the loop-expansion-order
counting of every amplitude downstream.

**Primary**: Peskin--Schroeder 1995 §4.4 (Feynman graph topology);
Itzykson--Zuber 1980 §6-2-2 (Euler characteristic of connected
graphs).

**Cross-ref**: \texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:120-122}
(error site); AP-V2-42 / V2-AP145 (quartic Casimir / 3-factor
propagator — adjacent bookkeeping); AP-V2-46 / V2-AP149 (wedge of
1-forms — adjacent topology slip).

### AP-V2-44 / V2-AP147: Weak Jacobi form polar coefficient $c_{\phi_{-2,1}}(-1) = 24$ false (2026-04-22)

**Trigger**: any Vol II citation of $c_{\phi_{-2,1}}(-n) = 24$ for
$n \ge 1$, or the identification of $24$ as a weak Jacobi form polar
Fourier coefficient of $\phi_{-2,1}$.

**Ghost**: the weak Jacobi form $\phi_{-2,1}(\tau, z)$ of weight
$-2$ and index $1$ has Fourier expansion
$\phi_{-2,1}(\tau, z) = \sum c_{\phi_{-2,1}}(n, \ell) q^n y^\ell$; the
polar coefficients $c_{\phi_{-2,1}}(-n, \ell) = 0$ for $n \ge 1$
by Eichler--Zagier polar-support cutoff
$c(\Delta) = 0$ for $\Delta = 4nm - \ell^2 < -m^2 = -1$ at
index $m = 1$ (Eichler--Zagier 1985 *Prog Math* 55 Thm 9.1, standard).

**Precise error**: sites
\texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:130-131}
and
\texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:186-188},
and
\texttt{chapters/connections/thqg\_perturbative\_finiteness.tex:4184}
assert $c_{\phi_{-2,1}}(-1) = 24$. The value $24$ arises either as
$\chi(\mathrm{K3})$ (the topological Euler characteristic of K3) or
as $|c_{1/\Delta_5}(q^1)|$ (a paramodular / $1/\Delta_5$-expansion
coefficient), NOT as a polar Fourier coefficient of
$\phi_{-2,1}$. Polar coefficients of index-1 weak Jacobi forms
vanish identically for $\Delta < -1$.

**Correction**: $c_{\phi_{-2,1}}(-n) = 0$ for all $n \ge 1$ by
Eichler--Zagier polar-support cutoff. When $24$ is the intended
value, replace with $\chi(\mathrm{K3}) = 24$ (topological Euler
characteristic, Hirzebruch 1966) or with
$|c_{1/\Delta_5}(q^1)| = 24$ (paramodular index-1 $q$-expansion
coefficient, Gritsenko 1999 *St Petersburg Math J* 11 Thm 6.1).

**Severity**: High. The error conflates three different combinatorial
objects (topological Euler characteristic, paramodular $q$-coefficient,
polar weak-Jacobi coefficient) that all happen to equal 24. The
downstream Feynman coefficient claim is false; the correction
changes amplitude formulas.

**Primary**: Eichler--Zagier 1985 *Prog Math* 55 Thm 9.1
(polar-support cutoff); Gritsenko 1999 (paramodular $\Delta_5$
expansion); Hirzebruch 1966 (K3 Euler characteristic).

**Cross-ref**: \texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:130-131, 186-188}
and \texttt{chapters/connections/thqg\_perturbative\_finiteness.tex:4184}
(error sites); AP-V2-24 / V2-AP127 (Humbert--Heegner admissibility
filter using the same Eichler--Zagier cutoff); Canonical preamble
row 45 (Humbert--Heegner admissibility).

### AP-V2-45 / V2-AP148: Stuffle dimensional failure — $\zeta(3)^2$ mixed-weight (2026-04-22)

**Trigger**: any Vol II identity for $\zeta(3)^2$ that mixes weights
or drops the stuffle relation to a non-homogeneous right-hand side.

**Ghost**: Euler stuffle relation for multiple zeta values
$\zeta(a) \zeta(b) = \sum \zeta(\cdots)$ preserves weight: both
sides are homogeneous of weight $a + b$. For $\zeta(3)^2$ the
stuffle expansion gives
$\zeta(3)^2 = 2\zeta(3, 3) + \zeta(6)$, all of weight 6
(Zagier 1994 *Prog Math* 120 Eq 4; Waldschmidt 2011 Exp 5).

**Precise error**: sites
\texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:334, 382}
assert $\zeta(3)^2 = 3\zeta(3, 3) + 6\zeta(5)/5$. The right-hand
side mixes $\zeta(3, 3)$ (weight 6) with $\zeta(5)$ (weight 5);
this is dimensionally illegal under the weight grading of the MZV
algebra. The correct stuffle yields $2\zeta(3, 3) + \zeta(6)$, not
$3\zeta(3, 3) + (6/5)\zeta(5)$.

**Correction**: $\zeta(3)^2 = 2\zeta(3, 3) + \zeta(6)$
(Zagier 1994 *Prog Math* 120 Eq 4). Under Euler's $\zeta(2n)$
closed form, $\zeta(6) = \pi^6/945$. If the computation needs a
$\zeta(5)$ term, it must come from a separate weight-5 identity
(e.g., shuffle $\zeta(2)\zeta(3) = \zeta(2, 3) + \zeta(3, 2) +
\zeta(5)$), not from the stuffle of $\zeta(3)^2$.

**Severity**: Critical. The mixed-weight RHS falsifies the
stuffle relation as a graded algebra identity; downstream MZV
algebra claims inherit the type error.

**Primary**: Zagier 1994 *Prog Math* 120 "Values of zeta functions
and their applications" Eq 4; Waldschmidt 2011 "Lectures on
Multiple Zeta Values" Exp 5; Brown 2012 *Ann Math* 175 Thm 1
(motivic MZV algebra grading).

**Cross-ref**: \texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:334, 382}
(error sites); cache row 129 (Vol II weight-12 MZV
$\zeta(3, 3, 3, 3)$); V2-AP124 (MZV numerical value).

### AP-V2-46 / V2-AP149: Wedge of 1-forms $\eta_{12}^{\wedge 3} = 0$ (2026-04-22)

**Trigger**: any Vol II iterated-integral formula of the form
$\int_{\cdots} \eta_{ij}^{\wedge k}$ with $k \ge 2$ for a fixed
1-form $\eta_{ij}$.

**Ghost**: for any 1-form $\eta$ on any manifold,
$\eta \wedge \eta = 0$ by graded anticommutativity of the exterior
algebra (Spivak 1979 Vol 1 Ch 7). Iterated Chen / Bott--Taubes
integrals require $k$ \emph{distinct} 1-forms on $k$ \emph{distinct}
configuration slots; degenerate evaluations with repeated forms
vanish identically.

**Precise error**: site
\texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:253-255}
asserts $\int_{z_2} \eta_{12}^{\wedge 3} = \zeta(3)$. But
$\eta_{12}^{\wedge 3} = 0$ identically because $\eta_{12}$ is a
single 1-form wedge-anticommuting with itself. The $\zeta(3)$
identity requires the Kontsevich / Hanamura / Brown three-distinct-form
integral
$\int \eta_{12} \wedge \eta_{23} \wedge \eta_{13}$ over
$\mathrm{Conf}_4$ or similar nondegenerate configuration
(Kontsevich 1994 *Prog Math* 120; Brown 2012 *Ann Math* 175).

**Correction**: replace $\eta_{12}^{\wedge 3}$ with a nondegenerate
wedge of three distinct 1-forms such as
$\eta_{12} \wedge \eta_{23} \wedge \eta_{31}$ (cubic Arnold) or
$\eta_{12} \wedge \eta_{13} \wedge \eta_{14}$ (star) on
$\mathrm{Conf}_n$ for $n \ge 4$; compute the resulting integral
against the appropriate holomorphic propagator.

**Severity**: High. The $\zeta(3)$ identification is the load-bearing
anchor of Vol II's weight-3 one-loop amplitude; the degenerate form
destroys the identification on the nose.

**Primary**: Spivak 1979 Vol 1 Ch 7 (graded-commutative exterior
algebra); Kontsevich 1994 *Prog Math* 120 "Feynman diagrams and
low-dimensional topology"; Brown 2012 *Ann Math* 175 (motivic MZV
basis, iterated integrals).

**Cross-ref**: \texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:253-255}
(error site); cache row 17 (Kontsevich integral conventions).

### AP-V2-47 / V2-AP150: Residue ill-typed — $\mathrm{Res}_{\Phi_{10} = 0}(Z_{\mathrm{hCS}}) = 1/\Phi_{10}$ (2026-04-22)

**Trigger**: any Vol II identification of
$\mathrm{Res}_{\Phi_{10} = 0}(Z_{\mathrm{hCS}}) = 1/\Phi_{10}$, or a
residue identification at the Igusa cusp-form vanishing locus that
produces a denominator rather than a numerator.

**Ghost**: the residue operator
$\mathrm{Res}_{f = 0} : \Omega^n_X \to \Omega^{n-1}_{\{f = 0\}}$
\emph{removes} the denominator $1/f$; if $\omega = g/f \cdot dz$
near $\{f = 0\}$, then
$\mathrm{Res}_{f = 0}(\omega) = g|_{f = 0}$. The statement
$\mathrm{Res}_{\Phi_{10} = 0}(Z_{\mathrm{hCS}}) = 1/\Phi_{10}$
is type-wrong: a residue cannot be a denominator of the same form.

**Precise error**: site
\texttt{chapters/connections/thqg\_perturbative\_finiteness.tex:4246-4277}
writes
$\mathrm{Res}_{\Phi_{10} = 0}(Z_{\mathrm{hCS}}) = 1/\Phi_{10}$.
The correct identification is
$Z_{\mathrm{3d\,QG}}(\tau, \tau') = 1/\Phi_{10}(\tau, z, \tau')$
\emph{directly} (Dijkgraaf--Verlinde--Verlinde 1997 *NPB* 484,
the exact Igusa cusp form
Siegel denominator of 3d quantum gravity partition function),
with the Costello effective action giving the Borcherds singular
theta lift of the chiral genus (Borcherds 1998 *Invent Math*
132 Thm 1.7).

**Correction**:
$Z_{\mathrm{3d\,QG}}(\tau, z, \tau') = 1/\Phi_{10}(\tau, z, \tau')$
(DVV 1997). The residue / Borcherds lift identification is
$Z^{\mathrm{eff}}_{\mathrm{Cost}} = -\log \Phi_{10}$ as a
singular theta lift of the elliptic genus; no residue step
produces $1/\Phi_{10}$ from a 1-form.

**Severity**: Critical. The identification anchors the 3d quantum
gravity Part VI climax; the residue-as-denominator framing is
false on the nose.

**Primary**: Dijkgraaf--Verlinde--Verlinde 1997 *NPB* 484
"Counting dyons in $\mathcal N = 4$ string theory"; Borcherds
1998 *Invent Math* 132 Thm 1.7 (singular theta lifts);
Costello 2017 (effective action); Griffiths--Harris 1978 Ch 1.1
(residue operator).

**Cross-ref**: \texttt{chapters/connections/thqg\_perturbative\_finiteness.tex:4246-4277}
(error site); AP-V2-48 / V2-AP151 ($\eta^{24}$ denominator);
Canonical preamble row 28 ($\Phi_{10} = \Delta_5^2$ K3-BKM
denominator).

### AP-V2-48 / V2-AP151: Single $\eta^{24}$ denominator — both elliptic-curve factors needed (2026-04-22)

**Trigger**: any Vol II holomorphic partition function of the form
$(\Phi_{10}/\eta^{24})^\hbar$ or $\Phi_{10}/\eta(\tau)^{24}$ with a
single $\eta$-factor in the denominator.

**Ghost**: the Igusa cusp form $\Phi_{10}(\tau, z, \tau')$ is a
Siegel modular form of weight 10 on $\mathrm{Sp}_4(\mathbb Z)$
with variables $(\tau, z, \tau') \in \mathbb H_2$; the two torus
moduli $\tau, \tau'$ parametrise the two elliptic-curve factors
$E_\tau \times E_{\tau'}$ in the Kummer / Humbert-divisor local
geometry. The canonical 3d quantum gravity / DVV partition function
has Kontsevich-style weight cancellation requiring
$\Phi_{10}/(\eta(\tau)^{24} \eta(\tau')^{24})$ (two $\eta^{24}$
factors, one per elliptic curve).

**Precise error**: site
\texttt{chapters/connections/thqg\_perturbative\_finiteness.tex:4240-4264}
writes $(\Phi_{10}/\eta^{24})^\hbar$ with a single $\eta^{24}$
denominator. The single denominator does not cancel the second
torus weight; under the transformation
$\mathrm{Sp}_4(\mathbb Z) \to \mathrm{SL}_2(\mathbb Z)_\tau
\times \mathrm{SL}_2(\mathbb Z)_{\tau'}$, only $\eta(\tau)^{24}$
is restored while $\eta(\tau')^{24}$ is missed.

**Correction**:
$Z_{\mathrm{hCS}} = \Phi_{10}/(\eta(\tau)^{24} \eta(\tau')^{24})$.
Both elliptic-curve weight factors appear; the combined denominator
has weight $10 - 12 - 12 = -14$ under $\mathrm{Sp}_4$, exhibiting
the expected singular-weight-$10$ numerator cancellation against
the two weight-$12$ cusp denominators, yielding the weight-$(-14)$
Siegel meromorphic form.

**Severity**: High. The single-factor denominator breaks the
modular weight balance and changes the 3d QG partition function
asymptotics.

**Primary**: DVV 1997 *NPB* 484; Gritsenko--Nikulin 1998
*J Reine Angew Math* 507 §3; Borcherds 1998 *Invent Math* 132
(singular theta lifts).

**Cross-ref**: \texttt{chapters/connections/thqg\_perturbative\_finiteness.tex:4240-4264}
(error site); AP-V2-47 / V2-AP150 (residue type error); Canonical
preamble row 28 ($\Phi_{10} = \Delta_5^2$ two-elliptic-curve
denominator).

### AP-V2-49 / V2-AP152: Dunn $E_1$-per-$\mathbb C$ — three commuting $E_1$ from three complex coordinates (2026-04-22)

**Trigger**: any Vol II statement that the three complex coordinates
$(z_1, z_2, z_3)$ on $\mathbb C^3$ yield three commuting $E_1$-algebra
structures.

**Ghost**: Dunn's additivity theorem
$E_n \otimes E_m \simeq E_{n+m}$ applies to the \emph{topological}
little-disks operads. A single complex coordinate on $\mathbb C$
supplies an $E_2$-structure topologically (since
$\mathrm{FM}_k(\mathbb C)$ is real-dim $2k$ in topological form); the
$E_1$-structure (linear ordering) emerges only after
$\bar\partial$-cohomology is taken (Costello--Gwilliam 2017 *FA*
Vol 2 Ch 5). Three $\mathbb C$ coordinates give $E_6$ topologically,
descending to $E_3$ after Dolbeault cohomology in each coordinate
(CG Vol II Ch 5 Thm 5.6.1).

**Precise error**: site
\texttt{chapters/connections/six\_d\_hcs\_e3\_chiral\_avatar\_platonic.tex:462-465}
asserts three commuting $E_1$ algebras from three complex
coordinates on $\mathbb C^3$, combining via Dunn to give $E_3$.
The combinatorial shape is correct ($E_3$ output) but the input
types are wrong: each $\mathbb C_j$ supplies $E_2$ topologically
(real-dim 2), not $E_1$; the $E_1$ reduction happens only at the
Dolbeault-cohomology level. Naïve Dunn additivity across three
$E_1$'s would give $E_3$; the correct derivation is $E_6
\to E_3$ via Dolbeault.

**Correction**: each $\mathbb C$ coordinate carries an
$E_2$-holomorphic factorisation structure topologically; three
coordinates compose via Dunn to $E_6$; Dolbeault cohomology in
each $\bar\partial_j$ direction reduces each $E_2$ to $E_1$, so
$E_6 \to E_3$. The $E_3$ output on $\mathbb C^3$ after Dolbeault
is what matches the 6d hCS factorisation structure (Costello--Li
2016 arXiv:1605.09930 §6).

**Severity**: High. The Dunn-composition framing has been widely
repeated; the correct derivation shows the $E_3$-level is forced
by Dolbeault (not by independent $E_1$-structures), which is
load-bearing for the $E_3$-chiral avatar of the Vol II
$\mathsf{SC}^{\mathrm{ch,top}}$ heptagon.

**Primary**: Costello--Gwilliam 2017 *FA* Vol 2 Ch 5 Thm 5.6.1
(Dolbeault reduction $E_{2d} \to E_d$); Costello--Li 2016
arXiv:1605.09930 §6 (6d hCS factorisation structure);
Dunn 1988 *J Pure Appl Algebra* 50 (Dunn additivity).

**Cross-ref**: \texttt{chapters/connections/six\_d\_hcs\_e3\_chiral\_avatar\_platonic.tex:462-465}
(error site); AP-V2-50 / V2-AP153 (Willwacher wheel-to-$\zeta$
convention); cache row 141 (ambient $\mathbb E_n$-level discipline);
Canonical preamble ambient-$\mathbb E_n$ row.

### AP-V2-50 / V2-AP153: Willwacher wheel-to-$\zeta$ convention-sensitive (2026-04-22)

**Trigger**: any Vol II identification of an $n$-spoke wheel
Feynman / Kontsevich graph with a specific zeta value without
naming the convention (Willwacher 2014 vs Brown--Schnetz
variant).

**Ghost**: Willwacher 2014 *Invent Math* 200 Thm 1.2 proves
$\mathrm{GRT}_1(\mathbb Q)$-freedom on Kontsevich graph cohomology
generated by $n$-spoke wheels $W_n$; in Willwacher's convention,
$W_n \leftrightarrow \zeta(2n - 1)$ (odd zeta value at weight
$2n - 1$). The Brown--Schnetz variant (Brown 2013 *Ann Sci ENS*
46; Schnetz 2014 *Commun Num Theor Phys* 8) uses
$W_n \leftrightarrow \zeta(2n + 1)$ with shifted indexing. Both
are correct; the distinction is convention on the wheel index.

**Precise error**: sites
\texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:366-368}
and
\texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:541}
identify a 3-spoke wheel with $\zeta(5)$ without naming the
convention. Under Willwacher 2014 a 3-spoke wheel $W_3$ couples
to $\zeta(2 \cdot 3 - 1) = \zeta(5)$; under Brown--Schnetz a
3-spoke wheel $W_3$ couples to $\zeta(2 \cdot 3 + 1) = \zeta(7)$.
The unnamed convention leaves the identification ambiguous.

**Correction**: state the convention at first use. Vol II default
is Willwacher 2014: $W_n \leftrightarrow \zeta(2n - 1)$; so the
3-spoke wheel $\leftrightarrow \zeta(5)$, the 4-spoke wheel
$\leftrightarrow \zeta(7)$, etc. Flag any cross-reference to
Brown--Schnetz with the shifted convention explicitly.

**Severity**: Medium. The convention is a named choice; fixing it
once at the top of the amplitude chapter suffices. The ambiguity
is not a falsification, but it does propagate into every downstream
$\zeta$-coefficient.

**Primary**: Willwacher 2014 *Invent Math* 200 Thm 1.2
"$M$. Kontsevich's graph complex and the Grothendieck--Teichmüller
Lie algebra"; Brown 2013 *Ann Sci ENS* 46 (single-valued periods);
Schnetz 2014 *Commun Num Theor Phys* 8.

**Cross-ref**: \texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:366-368, 541}
(error sites); AP-V2-49 / V2-AP152 ($E_1$-per-$\mathbb C$ Dunn scope,
same Willwacher framework); cache row 138 ($\mathrm{GRT}_1(\mathbb Q)$-torsor
chain-level $E_2$).

### AP-V2-51 / V2-AP154: K3-type MHS pollution — Feynman period on $K3 \times \mathbb C^2$ is not motivic MZV (2026-04-22)

**Trigger**: any Vol II assertion that a Feynman period integral on
$K3 \times \mathbb C^2$ lies in the motivic MZV algebra
$\mathrm{MZV}^{\mathrm{mot}}$.

**Ghost**: Brown 2012 *Ann Math* 175 proves that periods of
rational K-theory classes on mixed-Tate motives over $\mathbb Z$
generate $\mathrm{MZV}^{\mathrm{mot}}$. K3 surfaces are NOT mixed
Tate: the K3 period lattice carries a K3-type MHS with genuine
$H^{2,0}(K3)$ non-Tate classes (Kulikov 1977 *Izv Akad Nauk* 41
structure theorem). Periods of forms supported on $K3 \times X$
for any $X$ inherit the K3-type pollution and escape the
motivic MZV algebra.

**Precise error**: site
\texttt{chapters/connections/thqg\_perturbative\_finiteness.tex:4132}
asserts a Feynman period on $K3 \times \mathbb C^2$ lies in
$\mathrm{MZV}^{\mathrm{mot}}$. The K3 holomorphic 2-form
$\omega_{K3} \in H^{2,0}(K3)$ contributes a transcendental period
(the K3 Hodge structure) that is independent of MZVs; the total
period lattice is the tensor product $\mathrm{MHS}_{K3} \otimes
\mathrm{MHS}_{\mathbb C^2}$ and only the $\mathbb C^2$ factor is
mixed Tate.

**Correction**: Feynman periods on $K3 \times X$ lie in
$\mathrm{MHS}_{K3} \otimes \mathrm{MZV}^{\mathrm{mot}}(X)$ if $X$
is mixed Tate (e.g., $X = \mathbb C^n$ with logarithmic forms).
The K3-type MHS component is a separate Hodge-theoretic invariant
and must be named distinctly. Identifications
"$\text{period} \in \mathrm{MZV}^{\mathrm{mot}}$" hold only after
explicit restriction to a mixed-Tate subquotient of the K3 period
sheaf (typically via a Humbert-divisor stratification; see
AP-V2-6 for the Humbert / Kontsevich interplay).

**Severity**: High. Mixed-Tate vs K3-type MHS is a categorical
distinction; conflation falsifies every motivic identification on
K3-containing geometries.

**Primary**: Brown 2012 *Ann Math* 175 Thm 1 (motivic MZV =
mixed-Tate over $\mathbb Z$); Kulikov 1977 *Izv Akad Nauk* 41
(K3 degeneration / MHS structure); Deligne 1971 Hodge II (MHS
foundations); Griffiths 1969 (K3 period map).

**Cross-ref**: \texttt{chapters/connections/thqg\_perturbative\_finiteness.tex:4132}
(error site); AP-V2-6 (Humbert strata / chiral Kontsevich scope);
AP-V2-12 (Kaledin NC Hodge scope on Humbert); cache row 136
($\zeta^{\mathrm{sv}}$ vs motivic scope).

### AP-V2-52 / V2-AP155: AFT 2017 miscited for smooth-product factorisation homology (2026-04-22)

**Trigger**: any Vol II citation of Ayala--Francis--Tanaka 2017
Thm 4.1.3 in the context of factorisation homology of smooth
products.

**Ghost**: Ayala--Francis 2015 *J Topol* 8 Thm 3.16 establishes
factorisation-homology Fubini for smooth-product manifolds
$\int_{M \times N} \mathcal F = \int_M \int_N \mathcal F$ with
$\mathcal F$ a locally constant factorisation algebra on
$\mathrm{Disk}(M \times N)$. Ayala--Francis--Tanaka 2017
arXiv:1312.3745 extends to stratified spaces with
stratified-locally-constant sheaves; Thm 4.1.3 of AFT 2017 is the
stratified Fubini, not the smooth one.

**Precise error**: sites
\texttt{chapters/connections/celestial\_holography.tex:2496, 2517}
cite AFT 2017 Thm 4.1.3 for smooth-product factorisation Fubini.
The correct citation is AF 2015 Thm 3.16 (smooth); AFT 2017 is
about stratified spaces and its Thm 4.1.3 covers
\emph{stratified} Fubini with a different hypothesis set
(conical smoothness, constructible).

**Correction**: replace "AFT 2017 Thm 4.1.3" with "AF 2015 Thm 3.16"
for smooth-product applications. Use AFT 2017 Thm 4.1.3 only when
the ambient is genuinely stratified (e.g., compactified Heegner
divisor strata on $\overline{\mathcal A_2}$, AP-V2-6).

**Severity**: Medium. Attribution error; the smooth Fubini is a
true theorem but is due to Ayala--Francis alone. Mixed citation
blurs the stratified / smooth distinction, which matters for the
Humbert-stratum content of Vol II.

**Primary**: Ayala--Francis 2015 *J Topol* 8 Thm 3.16 "Factorization
homology of topological manifolds" (smooth Fubini); Ayala--Francis--Tanaka
2017 arXiv:1312.3745 Thm 4.1.3 (stratified Fubini).

**Cross-ref**: \texttt{chapters/connections/celestial\_holography.tex:2496, 2517}
(error sites); AP-V2-6 (Kontsevich formality on Humbert strata —
stratified context where AFT 2017 does apply); AP-V2-12 (Kaledin
stratified Hodge scope).

### AP-V2-53 / V2-AP156: Costello 2011 Thm 13.4.1 applied non-compact (2026-04-22)

**Trigger**: any Vol II citation of Costello 2011 *Renormalization
and Effective Field Theory* Thm 13.4.1 for a non-compact total
space such as $\mathbb R^3 \times K3 \times \mathbb C^2$.

**Ghost**: Costello 2011 Thm 13.4.1 (BV quantisation existence /
obstruction) is proved for compact-support observables OR for
theories with compactly supported fields on a compact manifold. On
non-compact total spaces the theorem requires a compact-support
hypothesis or a modified version; Costello--Gwilliam 2021 *FA*
Vol 2 Ch 4 extends with the modified hypothesis.

**Precise error**: sites
\texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:145, 433}
invoke Costello 2011 Thm 13.4.1 on the non-compact total space
$\mathbb R^3 \times K3 \times \mathbb C^2$ (or equivalent
non-compact 6d hCS setting). Without a compact-support hypothesis
or the CG 2021 Vol 2 Ch 4 modified statement, the theorem does
not apply.

**Correction**: either (i) restrict observables to compact support
and invoke Costello 2011 Thm 13.4.1 on the compact-support
subalgebra, or (ii) cite Costello--Gwilliam 2021 *FA* Vol 2 Ch 4
(the modified BV quantisation theorem on non-compact spaces with
appropriate IR regularisation). State the chosen hypothesis
explicitly.

**Severity**: Medium. The theorem is true in the intended
application; the error is a hypothesis-verification gap, fixable
by citing the correct version.

**Primary**: Costello 2011 *Renormalization and Effective Field
Theory* Thm 13.4.1; Costello--Gwilliam 2021 *Factorization
Algebras Vol 2* Ch 4 (modified BV quantisation on non-compact
total spaces).

**Cross-ref**: \texttt{chapters/theory/six\_d\_hcs\_feynman\_coefficients.tex:145, 433}
(error sites); AP-V2-42 / V2-AP145 (quartic Casimir in 6d hCS
amplitude); cache row 138 (chain-level $E_2$ GRT-torsor / BV
quantisation).

### AP-V2-54 / V2-AP157: CANONICAL-ANOM-LOCUS (form c) — $E_6$ strict exclusion, $A_2$ refined/unrefined distinguished (2026-04-22, canonical form propagated)

**Trigger**: any Vol II listing of the 6d hCS anomaly-free locus
that either (a) strips $\{E_6, A_2\}$ from Deligne without
distinguishing $A_2$-refined / $A_2$-unrefined and without the
$K^{-1/2}$-refinement clause, or (b) strips $\{E_6\}$ alone while
admitting $A_2$ without qualifier.

**Ghost**: the 6d hCS quartic Casimir
$d^{abcd} = \mathrm{tr}_{\mathrm{adj}}(T^{(a}T^b T^c T^{d)})$
vanishes universally on the Deligne series via
$\mathrm{tr}_{\mathrm{adj}}T^4 = \alpha_{\mathfrak g}
(\mathrm{tr}_{\mathrm{adj}}T^2)^2$ factorisation. A separate cubic
obstruction $d^{abc} = \mathrm{tr}_{\mathrm{adj}}(T^{(a}T^b T^{c)})$
arises for $E_6$ (cubic Jordan invariant on $\mathrm{Sym}^3(\mathbf{27})$,
non-zero, equal to the Jordan algebra product on
$\mathfrak j_3^{\mathbb O}$) and for $A_2 = \mathfrak{su}(3)$
(Gell-Mann $d$-tensor). Two distinct obstructions operate.

**Wrong claims flagged**:
- \textbf{Form (a) strict}: anomaly-free $\iff$ Deligne $\setminus
  \{E_6, A_2\}$ with no refinement clause; this misses that
  $A_2$-refined (with critical twist + Dimofte slab) sits INSIDE
  the locus.
- \textbf{Form (b)}: anomaly-free $\iff$ Deligne $\setminus \{E_6\}$
  alone, admitting undifferentiated $A_2$; this wrongly admits
  $A_2$-unrefined with live cubic $d^{abc}$ and live critical-level
  quadratic obstruction.

**Precise error**: both (a) and (b) misrepresent the native-ambient
locus. Form (a) is too coarse on $A_2$ (lumps refined with
unrefined); form (b) is too permissive (admits $A_2$-unrefined).
The canonical native form distinguishes four contributions and
carries the $K^{-1/2}$-refinement clause explicitly.

**Correction — CANONICAL-ANOM-LOCUS (form c)**: the native-ambient
anomaly-free locus reads
$$\mathrm{Anom}_1 = 0 \iff \mathfrak g \in
\bigl(\mathrm{Deligne}^{\mathrm{exc}} \setminus
\{E_6,\, A_2\text{-unrefined}\}\bigr) \cup \{\mathrm{abelian}\}
\cup \{\mathrm{super-str}_{\mathrm{ad}} = 0\}
\cup \{\widehat{\mathfrak g}_{-h^\vee} \otimes K^{-1/2}
\text{-refined}\}.$$
Native-ambient distinctions:
- $E_6$ STRICTLY excluded. No refinement in the programme's
  toolkit kills $\mathrm{Sym}^3(\mathbf{27})$ cubic Jordan invariant
  $d^{abc} \ne 0$ within native ambient; the $K^{-1/2}$ critical
  twist addresses the quadratic obstruction, not the cubic.
- $A_2$-unrefined excluded: live Gell-Mann $d_{abc}$ and live
  critical-level quadratic obstruction.
- $A_2$-refined INSIDE the locus: Feigin--Frenkel critical-level
  $K^{-1/2}$ twist kills the quadratic; Dimofte-slab
  anomaly-inflow from Vol II Part V provides Green--Schwarz cubic
  cancellation.
- $\{A_1, G_2, D_4, F_4, E_7, E_8\}$ unconditionally inside
  (quartic factorises via Deligne; cubic $d^{abc}$ vanishes
  identically on these six).
Two obstructions distinguished: quartic adjoint Casimir
(Deligne-killed across the series via factorisation,
including for $A_2, E_6$) vs cubic $d^{abc}$ (nonzero for $A_2, E_6$;
cured only in native ambient by Green--Schwarz-type inflow,
operative for $A_2$-refined, not for $E_6$).

**Regex trigger**: flag BOTH
- \verb|Deligne.*\\setminus.*\\\{E_6,\\s*A_2\\\}(?!.*refined)|
  (form a: strict $\{E_6, A_2\}$ without refinement);
- \verb|Deligne.*\\setminus.*\\\{E_6\\\}(?!.*A_2)|
  (form b: exclude-only-$E_6$);
relative to canonical (c) form which includes
``$A_2\text{-unrefined}$'' qualifier and the explicit
$K^{-1/2}$-refined clause.

**Severity**: Critical. Both (a) and (b) forms propagate into
downstream 3D HT QFT anomaly arguments; form (a) wrongly excludes
a live sector ($A_2$-refined via Dimofte slab), form (b) wrongly
admits a dead sector ($A_2$-unrefined with live cubic).

**Primary**: Deligne 1996 *C R Acad Sci Paris* 322 "La série
exceptionnelle de groupes de Lie"; Cvitanović 2008 *Group Theory*
Ch 20 ($E_6$ cubic invariant); Baez 2002 *Bull Amer Math Soc* 39
(Jordan algebra structure on $\mathfrak j_3^{\mathbb O}$);
Feigin--Frenkel 1992 *Comm Math Phys* 147 (critical-level
$K^{-1/2}$ twist); Dimofte 2014 slab anomaly-inflow.

**Cross-ref**: wherever the Deligne exceptional series is invoked
for anomaly cancellation in Vol II; AP-V2-42 / V2-AP145 (quartic
Casimir in 6d hCS 1-loop amplitude); AP-V2-53 / V2-AP156
(non-compact hCS hypothesis); Vol I AP979 (canonical-ambient
twin); AP-CY262 (Vol III cubic vs quadratic Casimir);
AP-CY50-E14 (cross-volume ledger).

### AP-V2-55 / V2-AP158: Conway $V^{s\natural}$ as bosonic $\Psi$-sibling (2026-04-22)

**Trigger**: any Vol II placement of Conway $V^{s\natural}$ as
the fifth row of the bosonic $\Psi$-sibling table, or as an
independent image of the bosonic $\Psi$-functor.

**Ghost**: the $\Psi$-functor has four sibling branches
$\{\Psi, \Psi^{\deg}, \Psi^{\mathrm{tor}}, \Psi^{\mathrm{metap}}\}$
covering the Baily--Borel--Freitag stratification of
$\overline{\mathcal A_2}$; Conway $V^{s\natural}$ is a super
chiral algebra at $c = 12$ on the metaplectic branch
$\Psi^{\mathrm{metap}}$ via Duncan 2007 *Duke* 139 (Leech
fermionic orbifold $A(\Lambda_{24})^+$, $c = 12$, NOT $c = 24$).
It is NOT a bosonic $\Psi$-image.

**Precise error**: any Vol II site placing Conway $V^{s\natural}$
as a bosonic $\Psi$-image at $c = 24$ or as the fifth independent
$\Psi$-sibling row. The correct placement is on the
$\Psi^{\mathrm{metap}}$ branch at $c = 12$ via the metaplectic
extension; the Leech lattice has no hyperbolic plane, so the
bosonic $\Psi$-image universal identity $(K, \hbar^2) = (2, -1/2)$
(Canonical preamble row 41) does not apply.

**Correction**: place Conway $V^{s\natural}$ on the
$\Psi^{\mathrm{metap}}$ branch at $c = 12$ via Duncan 2007 Leech
fermionic orbifolding $A(\Lambda_{24})^+$. Four siblings of the
$\Psi$-functor cover the Baily--Borel--Freitag stratification:
$\Psi$ (principal), $\Psi^{\deg}$ (cuspidal), $\Psi^{\mathrm{tor}}$
(toric), $\Psi^{\mathrm{metap}}$ (metaplectic); Conway is on the
fourth branch.

**Severity**: High. The Conway placement on the metaplectic branch
is load-bearing for the Part VI 3d gravity climax (the Conway
module / elliptic genus feeds Mathieu moonshine and the paramodular
/ Humbert identification).

**Primary**: Duncan 2007 *Duke Math J* 139 "Super-moonshine for
Conway's largest sporadic group"; Scheithauer 2008 *Adv Math* 220
(Freitag $\Psi$-functor sibling classification); Canonical preamble
rows 40-42 (Conway placement pinned).

**Cross-ref**: Canonical preamble rows 40-42 (Conway $c = 12$ on
$\Psi^{\mathrm{metap}}$); AP-V2-22 (five-archetype B-row);
V2-AP121 (Conway legacy placement AP).

### AP-V2-56 / V2-AP159: CHL Siegel weight ladder $\{\kappa(\Phi_N)\} = \{5, 4, 3, 2, 1\}$ false (2026-04-22)

**Trigger**: any Vol II identification of the CHL (Chaudhuri--Hockney--Lykken)
Siegel-weight ladder as $\{5, 4, 3, 2, 1\}$.

**Ghost**: the CHL construction orbifolds heterotic on
$T^6/\mathbb Z_N$ with $N \in \{2, 3, 5, 7, 11\}$; the resulting
1/4-BPS partition function is $1/\Phi_{k_N}$ with
$k_N = 24/(N+1) - 2$ (David--Jatkar--Sen 2006 JHEP 04:018 Eq
3.14). So $(k_2, k_3, k_5, k_7, k_{11}) = (6, 4, 2, 1, 0)$ in
the DJS indexing; with $N = 1$ (no orbifold, heterotic on
$T^6$) one gets $k_1 = 10$ (Igusa $\Phi_{10}$); including
$N = 1$ the sequence is $(10, 6, 4, 3, 2)$ for
$N \in \{1, 2, 3, 5, 7\}$ (David--Jatkar--Sen Eq 3.14 with
$N = 1$ the Igusa; tables in Persson--Volpato 2012 Table 1).

**Precise error**: any Vol II site writing
$\{\kappa(\Phi_N)\} = \{5, 4, 3, 2, 1\}$ for the CHL ladder.
The correct weight ladder is
$k_N = 24/(N + 1) - 2$, giving
$(k_1, k_2, k_3, k_5, k_7) = (10, 6, 4, 3, 2)$ across the five
CHL orbifolds. The stated $\{5, 4, 3, 2, 1\}$ sequence matches
neither the DJS weight nor the Siegel lifting weight
$\kappa(\Phi)$.

**Correction**: CHL weight ladder is
$k_N = 24/(N + 1) - 2$; explicit values
$(k_1, k_2, k_3, k_5, k_7) = (10, 6, 4, 3, 2)$. The Igusa
$\Phi_{10}$ is $k_1$; the $\mathbb Z_2$ CHL gives $\Phi_6$; the
$\mathbb Z_3$ CHL gives $\Phi_4$; etc. State the formula, not the
numerical sequence, as the load-bearing relation.

**Severity**: Critical. The weight ladder anchors the
BKM-$\Phi_N$ family across the Vol II / Vol III bridge; the
wrong sequence propagates into every CHL-dependent identification.

**Primary**: David--Jatkar--Sen 2006 JHEP 04:018 Eq 3.14;
Persson--Volpato 2012 arXiv:1212.0471 Table 1 (CHL Siegel weights);
Chaudhuri--Hockney--Lykken 1995 (original CHL orbifolds).

**Cross-ref**: Canonical preamble rows 28, 32-33 ($\Phi_{10}$,
$\Phi_{12}$, $\Phi_N$ placements); AP-V2-57 / V2-AP160
($\kappa_{\mathrm{BKM}}$ scope 5 vs 12).

### AP-V2-57 / V2-AP160: $\kappa_{\mathrm{BKM}}$ scope 5 vs 12 — $\Psi$-sibling-indexed (2026-04-22)

**Trigger**: any Vol II bare assertion of $\kappa_{\mathrm{BKM}}
= 5$ or $\kappa_{\mathrm{BKM}} = 12$ without naming the
$\Psi$-sibling denominator.

**Ghost**: $\kappa_{\mathrm{BKM}}$ is the Borcherds-weight
invariant of the BKM algebra; its numerical value is indexed by
the $\Psi$-sibling ($\Phi_N$ denominator) driving the lift. K3-BKM
(Gritsenko--Nikulin paramodular, $\Delta_5$ input) gives
$\kappa_{\mathrm{BKM}}^{\mathrm{K3}} = 5$; Fake-Monster
(Borcherds 1992, $\Phi_{12}$ input) gives
$\kappa_{\mathrm{BKM}}^{\mathrm{FM}} = 12$. Implicit conflation
loses the $\Psi$-sibling index.

**Precise error**: any Vol II site asserting $\kappa_{\mathrm{BKM}}$
bare (no sub/superscript denominator); the two legitimate values
$5$ and $12$ correspond to two distinct $\Phi_N$ inputs. The
AP5-audit / Canonical preamble row 60 pins this as pending
landscape-census lock: both values occur in published
inscriptions under different $N$-index conventions.

**Correction**: every Vol II $\kappa_{\mathrm{BKM}}$ reference
carries a superscript / subscript identifying the $\Psi$-sibling
denominator:
$\kappa_{\mathrm{BKM}}^{\mathrm{K3}} = 5$ for
$\Delta_5$ (paramodular, Gritsenko--Nikulin 1998);
$\kappa_{\mathrm{BKM}}^{\mathrm{FM}} = 12$ for $\Phi_{12}$
(Fake-Monster, Borcherds 1992). State the input $\Phi_N$ on every
inscription.

**Severity**: Critical. Flagged AP5-pending in Canonical preamble
row 60; unresolved conflation silently propagates.

**Primary**: Gritsenko--Nikulin 1998 *J Reine Angew Math* 507
(paramodular $\Delta_5$); Borcherds 1992 *Invent Math* 109
(Fake-Monster $\Phi_{12}$); Canonical preamble row 60
($\kappa_{\mathrm{BKM}}(\mathbf H_{\Delta_5})$ dual-indexing AP5
header).

**Cross-ref**: Canonical preamble row 60 (pending AP5 lock);
cache row 123 (five-archetype B-row witness); AP-V2-56 / V2-AP159
(CHL weight ladder); Cache header AP5 dual-indexing preamble
(lines 5-13).

### AP-V2-58 / V2-AP161: Three Yangian variants — four types in programme (2026-04-22)

**Trigger**: any Vol II assertion of "three Yangian types in the
programme" without naming the four canonical variants.

**Ghost**: the programme distinguishes four Yangian types on
different ambient spaces with different primary structures
(feedback entry \texttt{feedback\_yangian\_type\_distinction.md}
in MEMORY.md):
(i) \emph{classical Yangian} $Y(\mathfrak g)$ on the spectral line
$\mathbb C_u$ (Drinfeld 1985 *Sov Math Dokl* 32);
(ii) \emph{chiral Yangian} on the curve $C$ with $E_1$-chiral
structure (Vol II standalone "On the Integrable Theory of Chiral
Yangians");
(iii) \emph{spectral Yangian} on the torus $E_\tau$ via KZB
(Costello--Witten--Yamazaki 2018);
(iv) \emph{dg-shifted affine Yangian} on $T^* \mathbb C$ with
BV shift (Kodera--Nakajima 2018 arXiv:1602.06499;
Feigin--Frenkel--Rybnikov 2010).

**Precise error**: any Vol II site stating "three Yangian types"
conflates either (i) and (iv) (classical and dg-shifted) or drops
(iii) (spectral). Correct count is four.

**Correction**: state four Yangian types: classical, chiral,
spectral, dg-shifted affine. Name each with its ambient space
and primary reference at first use per chapter.

**Severity**: Medium. The conflation is a scope drift; fixing it
once per chapter clarifies the ambient-space structure of each
variant.

**Primary**: Drinfeld 1985 *Sov Math Dokl* 32 (classical Yangian);
Costello--Witten--Yamazaki 2018 arXiv:1709.09993 (spectral
Yangian); Kodera--Nakajima 2018 arXiv:1602.06499 (dg-shifted
affine Yangian); Vol II standalone "On the Integrable Theory of
Chiral Yangians" (chiral Yangian).

**Cross-ref**: MEMORY.md
\texttt{feedback\_yangian\_type\_distinction.md}; Vol II standalone
chiral-Yangians paper (protagonist of the programme identity);
Canonical preamble rows on four-types-of-centre discipline.

### AP-V2-59 / V2-AP162: $\Phi_d$ Stage-1 / Stage-2 unnamed in 6d hCS context (2026-04-22)

**Trigger**: any Vol II reference to 6d hCS as "$E_3$ on
$\mathbb C^3$" without naming the two-stage factorisation
$\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}
\circ \Phi^{\mathrm{FA}}_d$.

**Ghost**: the Vol III two-stage factorisation pins
$\Phi_d$ as Stage-1 (the canonical $E_d$-holomorphic factorisation
algebra on the CY-$d$ target via Kontsevich--Tamarkin formality
plus Costello--Gwilliam--Li locality) followed by Stage-2 (the
factorisation-homology pushforward $\int_{\Sigma_{d-1}}$ and
restriction to a reference curve $C$; Vol II CLAUDE.md lines
281-318). 6d hCS on $\mathbb C^3$ fits this framework as
Stage-1 $\Phi^{\mathrm{FA}}_3$, not as an independent $E_3$
construction.

**Precise error**: any Vol II site referring to 6d hCS as
"$E_3$ on $\mathbb C^3$" without naming Stage-1 $\Phi^{\mathrm{FA}}_3$
and the pushforward structure. The unnamed-stage framing hides
the CY-side canonical origin and the $(\Sigma_{d-1}, C)$-family
parametrisation of the $E_1$-chiral shadows on $C$.

**Correction**: every Vol II reference to 6d hCS (or $E_3$
$\mathbb C^3$-factorisation algebra content) names:
Stage-1 $\Phi^{\mathrm{FA}}_3$ as the canonical $E_3$-holomorphic
factorisation algebra on the CY-$3$ target; Stage-2
$\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_2, C}$ as the
$\int_{\Sigma_2}$-pushforward to the reference curve $C$; the
$E_1$-chiral shadow on $C$ is the output, parametrised by
$(\Sigma_2, C)$.

**Severity**: High. Part of the 2026-04-22 two-stage factorisation
wave (AP-V2-25..AP-V2-29); unnamed stages break the cross-volume
$\Phi_d$ framework.

**Primary**: Vol II CLAUDE.md two-stage factorisation section
(lines 281-318); Vol III
\texttt{chapters/theory/cy\_to\_chiral.tex}; Costello 2013
arXiv:1303.2632; Costello--Li 2016 arXiv:1605.09930;
Kontsevich 2003 *Lett Math Phys* 66; Tamarkin 2003
*Lett Math Phys* 66.

**Cross-ref**: AP-V2-25 / V2-AP128 (closed/open colour =
Stage-1 / Stage-2); AP-V2-26 / V2-AP129 (single-stage $\Phi_d$
framing); AP-V2-27 / V2-AP130 (3D HT QFT two-stage anchor);
AP-V2-28 / V2-AP131 (manifesto conflations from Vol III);
AP-V2-49 / V2-AP152 ($E_1$-per-$\mathbb C$ Dunn / Dolbeault).


### 2026-04-22: 15 cross-volume AP entries added from Vol III Wave 11-19

Fifteen cross-volume entries mirror the Vol III Wave 11-19 error/retraction
catalogue (six errors E\_A--E\_F, nine retractions R1--R9) into the Vol II
registry with Vol II-specific manifestations on the Swiss-cheese two-colour
structure, 3D HT QFT framework, class-$\mathcal S$ / AGT / Gaiotto curve
chapters, Pentagon single-colour coherence, and modular PVA quantisation.
AP tags AP-V2-60 / V2-AP163 through AP-V2-74 / V2-AP177 follow after the
AP-V2-59 / V2-AP162 inscription. Each entry shares a signature with the
corresponding Vol I AP (AP939--AP953) and the Vol III AP-CY primary form.

### AP-V2-60 / V2-AP163: Künneth multiplicative on products; partition function factorisation (2026-04-22)
**Severity**: High (load-bearing for class-$\mathcal S$ partition
function factorisation)
**Trigger**: Vol II partition-function factorisation on a product
CY ambient (e.g., $K3 \times E$ Swiss-cheese pairing, $K3 \times T^2$
class-$\mathcal S$ reduction) cites
$\kappa_{\mathrm{cat}}(K3 \times E) = 2$ or treats the fibre-K3 value
$\chi(\cO_{K3}) = 2$ as the total-space invariant. The partition-
function factorisation $Z(K3 \times E) = Z(K3) \cdot Z(E)$ at the
$\mathsf{SC}^{\mathrm{ch,top}}$ Swiss-cheese level requires the
Künneth-multiplicative $\kappa_{\mathrm{cat}}$ rule; additive or
fibre-only framing breaks the factorisation and inflates the one-loop
Quillen exponent.
**Ghost**: categorical Euler on a product is Künneth-multiplicative:
$\kappa_{\mathrm{cat}}(X \times Y) = \chi(\cO_X) \cdot \chi(\cO_Y)$,
giving $\kappa_{\mathrm{cat}}(K3 \times E) = 2 \cdot 0 = 0$. This is
load-bearing for the Vol II Swiss-cheese one-loop Quillen exponent
$\exp(2\pi i Q_{\mathrm{Quillen}})$ and for class-$\mathcal S$
partition functions over product compactifications.
**Precise error**: bare $\kappa$ on a product loses the Künneth-
multiplicative structure; the fibre-K3 value $2$ is presented as the
total-space value; Vol II partition-function factorisation breaks.
**Correction**: every Vol II site citing $\kappa$ on a product CY
subscripts: $\kappa_{\mathrm{cat}}(K3 \times E) = 0$ (total space,
Künneth-multiplicative), $\kappa_{\mathrm{fiber}}(K3) = 2$ (fibre
only). Partition-function factorisation reads $Z(K3 \times E) =
Z(K3) \cdot Z(E)$ with $Z(E) = 0$-level consistent with $\chi(\cO_E) = 0$.
**Primary**: Vol III
\texttt{chapters/examples/cy\_d\_kappa\_stratification.tex} canonical
table; canonical preamble row 66; Vol III AP-CY primary form (E\_A).
**Inscription**: Vol II
\texttt{chapters/theory/sc\_chtop\_partition\_factorisation.tex};
cross-volume $\kappa_{\mathrm{cat}}$, $\kappa_{\mathrm{fiber}}$
subscripts.
**Cross-ref**: Vol III AP-CY (E\_A primary form); Vol I AP939
(partner); Vol II canonical preamble rows 59, 66; AP-V2-28 /
V2-AP131 (manifesto conflation); V2-AP68 / V2-AP69.

### AP-V2-61 / V2-AP164: Central charge $-1312/11$ at $c_{4d} = 107/6$ via two independent verification routes (2026-04-22)
**Severity**: High (load-bearing for
$\mathcal T[A_1, \Sigma_{0, 24}]$ landscape anchor)
**Trigger**: Vol II class-$\mathcal S$ / AGT chapters citing the
$(c_{4d}, c_{2d})$ central-charge pair for
$\mathcal T[A_1, \Sigma_{0, 24}]$ use the retracted Wave 14 value
$(26, -312)$ or the retracted Wave 25 Gaiotto-agent value
$(23/4, -69)$, or cite the canonical $(107/6, -214)$ without
two-route verification.
**Ghost**: canonical preamble row 17 pins $(c_{4d}, c_{2d}) = (107/6,
-214)$ for $\mathcal T[A_1, \Sigma_{0, 24}]$ via Wave 15 Gaiotto
verification against the universal formula $c_{4d} = (5n - 13)/6$
(canonical preamble row 19, Shapere--Tachikawa 2008).
**Precise error**: single-route citation of a load-bearing structure
constant whose Wave 14 value was retracted; AP274-style citation-as-
derivation.
**Correction**: every Vol II $(c_{4d}, c_{2d})$ citation for
$\mathcal T[A_1, \Sigma_{0, 24}]$ uses $(107/6, -214)$ with two
independent verification routes named: Shapere--Tachikawa 2008
universal formula $c_{4d} = (5n - 13)/6$ at $n = 24$; direct
Sugawara-denominator recomputation on the Gaiotto curve.
**Primary**: Vol III Wave 15 Gaiotto verdict; canonical preamble
rows 17, 19; Shapere--Tachikawa 2008.
**Inscription**: Vol II
\texttt{chapters/connections/class\_s\_gaiotto.tex} two-route
verification block.
**Cross-ref**: Vol III AP-CY (E\_B primary form); Vol I AP940
(partner); canonical preamble rows 17--19; AP-V2-19 (universal
ratio-of-levels).

### AP-V2-62 / V2-AP165: $\eta^{-48}$ Heisenberg--Mukai identity in modular PVA quantisation chapters, not Virasoro minimal-model (2026-04-22)
**Severity**: Medium (modular PVA quantisation anchor)
**Trigger**: Vol II modular PVA quantisation chapters
(\texttt{chapters/theory/pva-expanded.tex},
\texttt{chapters/connections/modular\_pva\_quantisation.tex}) frame
the $\eta^{-48}$ factor in $V_{24}$ character as a Virasoro minimal-
model expansion; the correct reading is the Heisenberg--Mukai lattice
partition function $\eta^{-48} = \prod_n (1 - q^n)^{-24}$ on the Mukai
lattice $\mathrm{II}_{1, 1} \otimes \cO_{K3}$.
**Ghost**: iterated Drinfeld--Sokolov reduction $V_{24} =
\mathrm{DS}^{24}(\mathrm{Heis}_{\mathrm{II}_{1,1}})$ produces
$\eta^{-48}$; character identity $\chi_{V_{24}} = \eta^{-48}$ holds by
iterated-DS contraction + Borcherds lift on the Mukai lattice. The
Virasoro minimal-model reading would give a finite-dimensional
character with no $\eta$-denominator.
**Precise error**: conflates two distinct vertex-algebra presentations
of the same generating function; Heisenberg--Mukai has a free-field
factor, Virasoro minimal-model does not.
**Correction**: every Vol II $\eta^{-48}$ reference names the
Heisenberg--Mukai lattice VOA and the iterated Drinfeld--Sokolov chain
$V_{24} = \mathrm{DS}^{24}(\mathrm{Heis}_{\mathrm{II}_{1,1}})$;
the modular PVA quantisation lands on the Heisenberg--Mukai positive-
half vertex-operator trace.
**Primary**: Vol III Wave 15--17 three-path verification;
Mukai 1988; Frenkel--Kac construction; canonical preamble row 52.
**Inscription**: Vol II \texttt{chapters/theory/pva-expanded.tex}
$V_{24}$ paragraph;
\texttt{chapters/connections/modular\_pva\_quantisation.tex}.
**Cross-ref**: Vol III AP-CY (E\_C, R5 primary form); Vol I AP941
(partner); AP-V2-49 / V2-AP152 ($V_{24}$ iterated-DS partner);
canonical preamble row 52 (chiral-Hochschild $e_k$ motivic home).

### AP-V2-63 / V2-AP166: Macdonald framework inapplicable to non-minimal Pentagon structures (2026-04-22)
**Severity**: Medium (Pentagon single-colour coherence scope)
**Trigger**: Vol II Pentagon single-colour coherence chapters invoke
the Macdonald difference-operator framework at non-minimal targets
(W-algebras at non-admissible level, logarithmic triplet VOAs,
parafermion cosets) Pentagon vertices.
**Ghost**: Macdonald framework is theorem for Cherednik DAHA and
admissible-level affine Lie algebras with minimal-model /
integrable structure. Pentagon single-colour coherence at admissible
level reduces to Macdonald-polynomial diagonalisation; at non-
admissible level the positive-part Yangian is not diagonal in the
Macdonald basis.
**Precise error**: Macdonald framework extended beyond its
admissibility domain; Pentagon coboundary $\phi^{(n)}$ silently
relies on admissibility.
**Correction**: every Vol II Pentagon / Macdonald invocation names
the admissibility constraint — minimal target, admissible level
$k + h^\vee = p / q$ with $(p, q) = 1$, finite-dimensional bar at
each weight. Non-minimal Pentagon uses Kac--Roan 2014 integrable-
system residue or Feigin--Frenkel centre on $\mathrm{Op}$-side.
**Primary**: Vol III Wave 18 Gaiotto verdict on admissibility;
Macdonald 1995; Cherednik 2005; canonical preamble row 44.
**Inscription**: Vol II
\texttt{chapters/theory/pentagon\_single\_colour.tex} admissibility-
scope remark.
**Cross-ref**: Vol III AP-CY (E\_D primary form); Vol I AP942
(partner); canonical preamble rows 44--48.

### AP-V2-64 / V2-AP167: Eight-form position $\ne$ Borcherds weight in Swiss-cheese Borcherds-lift inscriptions (2026-04-22)
**Severity**: Medium (Swiss-cheese Borcherds-lift catalogue)
**Trigger**: Vol II Swiss-cheese Borcherds-lift chapters use position-
in-catalogue as stand-in for Borcherds weight; weights are non-
monotone: $(w_1, \ldots, w_8) = (5, 2, 1, 1, 1/2, 1, 1/4, 0)$ with
Fourier coefficients $c_N(0) \in \{10, 4, 2, 2, 1, 2, 1/2, 0\}$.
**Ghost**: eight-form catalogue is enumerated by $\mathrm{Sp}_4(\Z)$-
cover refinement — integral ($\mathrm{Sp}_4(\Z)$), half-integral
($\mathrm{Mp}_4$), quarter-integral ($\widetilde{\mathrm{Mp}}_4$) — not
by weight; the weight-0 form is the degenerate terminal fibre.
**Precise error**: enumeration index confused with mathematical
invariant; "the $k$-th form" without weight specification loses
$c_N(0)/2$ identification.
**Correction**: every Vol II citation of the eight-form catalogue
names the cover group and the weight adjacent to each form; universal
identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ stated with the
$(w_k, c_k(0))$ pair.
**Primary**: Gritsenko--Clery 2018; Vol III
\texttt{chapters/examples/cy\_d\_kappa\_stratification.tex} Theorem
\texttt{thm:borcherds-weight-kappa-BKM-universal}.
**Inscription**: Vol II
\texttt{chapters/examples/sc\_chtop\_borcherds\_lift.tex} eight-form
$(w, c(0))$-pairs.
**Cross-ref**: Vol III AP-CY (E\_E primary form); Vol I AP943
(partner); canonical preamble row 28 (K3-BKM Weyl denominator);
AP-V2-62 / V2-AP165 (Heisenberg--Mukai $\eta^{-48}$).

### AP-V2-65 / V2-AP168: Twined convention $c_2(0) \in \{4, 8\}$ declared at every Swiss-cheese cross-citation with Vol III (2026-04-22)
**Severity**: Medium (cross-volume convention discipline)
**Trigger**: Vol II Swiss-cheese cross-citations to Vol III Borcherds-
weight Fourier coefficients $c_N(0)$ silently switch between Gritsenko
1999 ($c_2(0) = 4$) and Cheng--Duncan 2013 umbral ($c_2(0) = 8$).
**Ghost**: the two conventions differ by a normalisation factor of $2$
at $N = 2$; both are published, both self-consistent. Vol III uses
Gritsenko; Vol II cross-citations not declaring convention risk silent
switch.
**Precise error**: convention-dependent structure constant cited bare;
ambient-qualifier drop (AP281 partner).
**Correction**: every Vol II reference to twined $c_N(0)$ names the
Borcherds automorphic form and the convention: "Gritsenko 1999
twined coefficients ($c_2(0) = 4$)" or "Cheng--Duncan 2013 umbral
coefficients ($c_2(0) = 8$)". Vol II defaults to Gritsenko for
cross-citations to Vol III.
**Primary**: Gritsenko 1999 Thm 6.1; Cheng--Duncan 2013.
**Inscription**: Vol II
\texttt{chapters/theory/sc\_chtop\_borcherds\_lift.tex} convention
declaration.
**Cross-ref**: Vol III AP-CY (E\_F primary form); Vol I AP944
(partner); AP281 partner (ambient-qualifier drop); canonical
preamble row 28.

### AP-V2-66 / V2-AP169: Feingold--Frenkel $F_3$ real-root subalgebra at Vol II Swiss-cheese genus-1 BKM sites (2026-04-22)
**Severity**: High (genus-1 BKM real-root identification)
**Trigger**: Vol II Swiss-cheese genus-1 BKM chapters frame the real-
root subalgebra of $\mathfrak g_{\Delta_5}$ as
$\widehat{\mathfrak{sl}_3}$; correct identification is the Feingold--
Frenkel rank-3 hyperbolic Kac--Moody algebra $F_3$.
**Ghost**: $F_3$ (Feingold--Frenkel 1983) has rank-3 hyperbolic Cartan
matrix $\begin{pmatrix} 2 & -2 & 0 \\ -2 & 2 & -1 \\ 0 & -1 & 2
\end{pmatrix}$, indefinite type, imaginary-root Weyl chamber non-
empty. Affine $\widehat{\mathfrak{sl}_3}$ has rank-2 Cartan plus
central element, no imaginary roots, cannot carry Humbert-divisor
structure of K3-BKM genus-1 anchor.
**Precise error**: conflates affine Lie algebra with rank-3 hyperbolic
Kac--Moody algebra at real-root subalgebra site.
**Correction**: every Vol II genus-1 BKM real-root reference cites
Feingold--Frenkel 1983 $F_3$ with rank-3 hyperbolic Cartan matrix
and names Humbert-divisor matching on K3 fibre.
**Primary**: Feingold--Frenkel 1983 *Math Ann* 263; Gritsenko--
Nikulin 1998 Table 2.
**Inscription**: Vol II
\texttt{chapters/theory/sc\_chtop\_genus1.tex} real-root
identification.
**Cross-ref**: Vol III AP-CY (R1 primary form); Vol I AP945
(partner); canonical preamble row 28; AP-V2-62 / V2-AP165
(Heisenberg--Mukai).

### AP-V2-67 / V2-AP170: $L_{-6}(\mathfrak{e}_8) \to$ iterated Drinfeld--Sokolov reduction for $V_{24}$ at 3D HT QFT bulk (2026-04-22)
**Severity**: High (3D HT QFT bulk $V_{24}$ presentation)
**Trigger**: Vol II 3D HT QFT bulk sites frame $V_{24}$ as
$L_{-6}(\mathfrak{e}_8)$; correct presentation is iterated Drinfeld--
Sokolov reduction from a higher-rank source.
**Ghost**: $V_{24} = \mathrm{DS}^{24}(\mathrm{Heis}_{\mathrm{II}_{1,1}})$
iterated-DS output with 24 singular iterations; $c(V_{24}) = 24$.
$L_{-6}(\mathfrak{e}_8)$ has $c = -992/11$, so identification fails
at central-charge level.
**Precise error**: conflates affine VOA at specific level with
iterated-DS output of higher-rank chain; central charges disagree.
**Correction**: every Vol II $V_{24}$ reference cites iterated-DS
chain with source, level, nilpotent orbit; central-charge match
$c(V_{24}) = 24$ is the anchor.
**Primary**: Vol III Wave 15 iterated-DS chain; Kac--Roan 2000;
Adamovic--Milas 1997.
**Inscription**: Vol II
\texttt{chapters/theory/ht\_qft\_bulk\_v24.tex} iterated-DS
presentation.
**Cross-ref**: Vol III AP-CY (R2 primary form); Vol I AP946
(partner); AP-V2-62 / V2-AP165 ($\eta^{-48}$); canonical preamble
row 52.

### AP-V2-68 / V2-AP171: $\kappa_{\mathrm{BKM}}$ not additive; universal $c_N(0)/2$ on HT top-form dimension (2026-04-22)
**Severity**: High ($\kappa_\bullet$ discipline)
**Trigger**: Vol II 3D HT QFT HT top-form dimension calculations
factorise $\kappa_{\mathrm{BKM}}$ additively as
$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\cO_{\mathrm{fiber}})$
across $N$-family.
**Ghost**: additive relation is FALSE at every
$N \in \{1, 2, 3, 4, 6\}$: at $N = 1$, left $= 5$, right $=
\kappa_{\mathrm{ch}}(K3 \times E) + \chi(\cO_E) = 0 + 0 = 0$; at
$N = 2$, left $= 4$, right $= 1$. Universal formula is
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ (Borcherds weight).
**Precise error**: additive decomposition of Borcherds-lift Fourier
coefficient into CY-categorical and fibre-Euler pieces has no lift-
functoriality; Borcherds lift is multiplicative, not additive.
**Correction**: every Vol II $\kappa_{\mathrm{BKM}}$ identity reads
with scope-split — Borcherds-weight side uses multiplicative lift on
Mukai lattice; $\kappa_{\mathrm{ch}}$ / $\kappa_{\mathrm{fiber}}$
bookkeeping is CY-categorical denominator; the two scopes meet at
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ as universal identity,
not additive decomposition.
**Primary**: Vol III
\texttt{chapters/examples/cy\_d\_kappa\_stratification.tex} Theorem
\texttt{thm:borcherds-weight-kappa-BKM-universal}; Borcherds 1995;
Gritsenko 1999.
**Inscription**: Vol II
\texttt{chapters/theory/ht\_qft\_kappa\_split.tex} scope-split
discipline.
**Cross-ref**: Vol III AP-CY (R3 primary form); Vol I AP947
(partner); canonical preamble row 59; AP-V2-60 / V2-AP163 (Künneth
multiplicative).

### AP-V2-69 / V2-AP172: Fake Monster at $d = 5$ on HT top-form dimension; $d = 5$ Poisson-$E_5$ corner closure (2026-04-22)
**Severity**: High (CY-dimension discipline)
**Trigger**: Vol II HT top-form dimension cites Fake Monster BKM as
$d = 3$ object or omits $d = 5$ Poisson-$E_5$ corner closure from
PTVV / HT top-form table.
**Ghost**: Fake Monster Cartan rank $26$ on $\mathrm{II}_{25, 1}$
(Borcherds 1992), natural CY home $K3 \times K3 \times E$ at $d = 5$
with $\Phi_{12}$ Borcherds lift; $d = 5$ PTVV shift $-4$, Poisson-
$E_5$ corner closure via Dunn--Lurie $E_3 \otimes E_2 = E_5$. K3-BKM
(Cartan rank $3$ on $\Lambda^{2, 1}_{\mathrm{II}}$) is $d = 3$ sibling.
**Precise error**: CY-dimension confusion Fake Monster ($d = 5$,
$\Phi_{12}$) vs K3-BKM ($d = 3$, $\Phi_{10} = \Delta_5^2$); HT top-
form table truncated at $d = 4$.
**Correction**: every Vol II HT top-form / PTVV / Fake-Monster
reference names $d$, lattice signature, Borcherds-lift denominator:
$d = 5$ on $\mathrm{II}_{25, 1}$ with $\Phi_{12}$ for Fake Monster;
$d = 3$ on $\Lambda^{2, 1}_{\mathrm{II}}$ with $\Phi_{10}$ for K3-BKM;
HT top-form table extends to $d = 5$ Poisson-$E_5$.
**Primary**: Borcherds 1992 *Invent Math* 109; Pantev--Toen--Vaquie--
Vezzosi 2013 *Publ IHES* 117; Vol III Wave 18 PTVV extension;
canonical preamble rows 20--22.
**Inscription**: Vol II
\texttt{chapters/theory/ht\_top\_form\_table.tex} $d = 5$ row;
\texttt{chapters/theory/ptvv\_shifted\_symplectic.tex} Poisson-$E_5$.
**Cross-ref**: Vol III AP-CY (R4, R8 primary forms); Vol I AP948,
AP952 (partners); canonical preamble rows 20--22.

### AP-V2-70 / V2-AP173: Direct $\chi_{V_{24}} = \eta^{-48}$ match via three-path verification (2026-04-22)
**Severity**: Medium (character-match verification discipline)
**Trigger**: Vol II $V_{24}$ character inscription cites
$\chi_{V_{24}} = \eta^{-48}$ as direct character identity without
naming the three-path verification.
**Ghost**: three-path verification: (i) iterated-DS character
contraction from $L_k(\mathfrak{e}_8)$ source; (ii) Sugawara-
denominator recomputation on Heisenberg--Mukai lattice; (iii)
Borcherds lift on the Mukai lattice.
**Precise error**: load-bearing identity cited without derivation;
direct-match framing hides the three-path verification.
**Correction**: every Vol II site citing $\chi_{V_{24}} = \eta^{-48}$
names the three verification paths and the iterated-DS construction
of $V_{24}$.
**Primary**: Vol III Wave 15--17 three-path verification;
AP-V2-67 / V2-AP170 (iterated-DS).
**Inscription**: Vol II \texttt{chapters/theory/pva-expanded.tex} /
\texttt{chapters/theory/ht\_qft\_bulk\_v24.tex} three-path block.
**Cross-ref**: Vol III AP-CY (R5 primary form); Vol I AP949
(partner); AP-V2-62 / V2-AP165 ($\eta^{-48}$); AP-V2-67 / V2-AP170
(iterated DS).

### AP-V2-71 / V2-AP174: Gaiotto curve $\Sigma_{0, 24}$ with 24 punctures, not $\Sigma_{2, 0}$ (2026-04-22)
**Severity**: High (class-$\mathcal S$ / AGT curve identification)
**Trigger**: Vol II class-$\mathcal S$ / AGT / Gaiotto curve chapters
frame the Gaiotto curve for $\mathcal T[A_1, K3]$ or K3-BKM landscape
as $\Sigma_{2, 0}$ closed genus-2.
**Ghost**: correct Gaiotto curve is $\Sigma_{0, 24}$: genus-0 with
24 simple $A_1$ punctures (regular / $\mathrm{SU}(2)$-flavour).
Puncture count $24$ matches $\chi(K3) = 24$ and the $24 I_1$ nodes
of the Pentagon construction. Trinion/tube count $(n_v, n_h) =
(63, 88)$ (canonical preamble row 18, Chacaltana--Distler 2010).
**Precise error**: puncture-count / genus confusion; moduli dimension
$6g - 6 + 2n = 42$ for $\Sigma_{0, 24}$ vs $6$ for $\Sigma_{2, 0}$.
**Correction**: every Vol II Gaiotto-curve reference uses
$\Sigma_{0, 24}$ with 24 $A_1$ punctures; trinion/tube count
$(63, 88)$ named.
**Primary**: Vol III Wave 15 Gaiotto verdict; canonical preamble
rows 17--18; Gaiotto 2009 *JHEP* 1208; Chacaltana--Distler 2010.
**Inscription**: Vol II
\texttt{chapters/connections/class\_s\_gaiotto.tex};
\texttt{chapters/connections/agt\_correspondence.tex}.
**Cross-ref**: Vol III AP-CY (R6 primary form); Vol I AP950
(partner); canonical preamble rows 17--19; AP-V2-61 / V2-AP164
(two-route central-charge).

### AP-V2-72 / V2-AP175: MC5 sewing theorem on Stage 2 of two-stage factorisation (2026-04-22)
**Severity**: High (sewing-theorem cross-volume anchor)
**Trigger**: Vol II MC5 sewing theorem is inscribed without
identifying its home on Stage 2 of the Vol III two-stage factorisation
$\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ
\Phi^{\mathrm{FA}}_d$; sewing theorem is the stage-2 pushforward
$\int_{\Sigma_{d-1}}$ identification, not a free-standing construction.
**Ghost**: MC5 sewing theorem recovers the $E_1$-chiral shadow on
the reference curve $C$ from the $E_d$-holomorphic factorisation
algebra on the CY-$d$ ambient via factorisation-homology pushforward.
6D hCS at Level 3 realises the $E_3$-algebra underlying the 3D HT QFT,
which in turn lives on the OPEN colour of $\mathsf{SC}^{\mathrm{ch,top}}$
as stage-2 specialisation (AP-V2-25 / V2-AP128).
**Precise error**: MC5 inscribed as free-standing; two-stage anchor
missing; stage-2 specialisation scope lost.
**Correction**: every Vol II MC5 inscription names Stage 2
$\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$, the factorisation-
homology pushforward $\int_{\Sigma_{d-1}}$, and the family parameter
$(\Sigma_{d-1}, C)$; 6D hCS realisation of $E_3$ named at stage-2
boundary.
**Primary**: Ayala--Francis 2015 *J Topol* 8; Costello 2013
arXiv:1303.2632; Vol III two-stage factorisation wave 2026-04-22.
**Inscription**: Vol II \texttt{chapters/theory/mc5\_sewing.tex}
Stage-2 bridge clause.
**Cross-ref**: Vol III AP-CY (R7 primary form); Vol I AP951
(partner); AP-V2-25 / V2-AP128 (closed/open colour = stage);
AP-V2-26 / V2-AP129 (single-stage framing); AP-V2-59 / V2-AP162
(6d hCS Stage-1).

### AP-V2-73 / V2-AP176: PTVV table to $d = 5$ Poisson-$E_5$ corner closure in Vol II (2026-04-22)
**Severity**: Medium (PTVV $d$-table completeness)
**Trigger**: Vol II PTVV chapter closes the $(d, \mathrm{shift},
E_n^{\mathrm{cl}})$ table at $d = 4$; correct closure is at $d = 5$
with $(5, -4, \mathrm{Poisson}\text{-}E_5)$.
**Ghost**: PTVV extends to all $d$ with shift $-2d + 2$ on the CY-$d$
moduli; Dunn--Lurie $E_3 \otimes E_2 = E_5$ gives Poisson-$E_5$
corner closure at $d = 5$. HT top-form dimension at $d = 5$ matches
$d = 5$ Fake Monster CY home.
**Precise error**: incomplete dimensional enumeration; AP-V2-35 /
V2-AP138 partner at $d = 5$.
**Correction**: Vol II PTVV table includes $d = 5$ row with Poisson-
$E_5$ corner closure; full sequence $(d, \mathrm{shift},
E_n^{\mathrm{cl}}) = (1, 0, E_0), (2, -2, E_1), (3, -2,
\mathrm{Poisson}\text{-}E_3), (4, -2, \mathrm{Poisson}\text{-}E_4),
(5, -4, \mathrm{Poisson}\text{-}E_5)$.
**Primary**: Pantev--Toen--Vaquie--Vezzosi 2013 *Publ IHES* 117;
Vol III Wave 18 PTVV extension.
**Inscription**: Vol II
\texttt{chapters/theory/ptvv\_shifted\_symplectic.tex} $d = 5$ row.
**Cross-ref**: Vol III AP-CY (R8 primary form); Vol I AP952
(partner); AP-V2-35 / V2-AP138; AP-V2-69 / V2-AP172 (Fake Monster).

### AP-V2-74 / V2-AP177: Pentagon single-colour coherence $H^3$ class-dependent at 24 $I_1$ nodes (2A $\in \Z/2$, 2B $\in \Z/4$) (2026-04-22)
**Severity**: Medium (Pentagon $H^3$ Mathieu-class refinement)
**Trigger**: Vol II Pentagon single-colour coherence at 24 $I_1$
nodes on Gaiotto curve $\Sigma_{0, 24}$ states $H^3$ cocycle
uniformly across Mathieu conjugacy classes.
**Ghost**: $H^3 \in \Z/2$ for class 2A (fixing two points of
$\Omega_{24}$), $H^3 \in \Z/4$ for class 2B (fixing one point and
one 2-cycle), per-class for all 25 classes in $M_{24}$. $H^3$ is
a Mathieu-class invariant, not universal.
**Precise error**: conjugacy-class-dependent torsion presented as
class-independent; Mathieu-moonshine refinement lost.
**Correction**: every Vol II Pentagon $H^3$ coherence statement
names Mathieu conjugacy class and torsion value: 2A $\in \Z/2$,
2B $\in \Z/4$, and per-class entries for all 25 classes.
**Primary**: Vol III Wave 18 Mathieu class-dependent $H^3$;
Eguchi--Ooguri--Tachikawa 2010 (Mathieu moonshine for K3);
Conway--Sloane SPLAG Ch 10.
**Inscription**: Vol II
\texttt{chapters/theory/pentagon\_single\_colour.tex} Mathieu-class
table;
\texttt{chapters/connections/mathieu\_moonshine.tex}.
**Cross-ref**: Vol III AP-CY (R9 primary form); Vol I AP953
(partner); AP-V2-63 / V2-AP166 (Macdonald inapplicability);
AP-V2-71 / V2-AP174 (Gaiotto curve 24 punctures); canonical preamble
row 39 (rank-162 MTC).

### AP-V2-75 / V2-AP178: Cubic $d^{abc}$ vs quartic Casimir on $E_2$-bar bulk-boundary anomaly; CANONICAL-ANOM-LOCUS (form c) (2026-04-22)
**Severity**: Critical (6D hCS / 3D HT QFT bulk anomaly discipline; Vol III AP-CY262 partner)
**Trigger**: Vol II $\SC^{\mathrm{ch,top}}$ / 3D HT QFT bulk-boundary
anomaly at the $E_2$-bar $\partial\mathrm{hCS}$ interface cites
only quadratic Casimir $C_2 = 2h^\vee$ for anomaly-free locus, or
admits $E_6$ in a ``cubic-free'' safe list, or cites Deligne
$\setminus \{E_6, A_2\}$ without $A_2$-refined / $A_2$-unrefined
distinction.
**Ghost**: two obstructions operate — \emph{quartic}
$\mathrm{tr}_{\mathrm{adj}}(T^{(a}T^bT^cT^{d)})$ factorising across
the Deligne exceptional series (Cohen--de Man 1996) with the
residual $(F^2)^2$ absorbed by Green--Schwarz, and \emph{cubic}
$d^{abc} = \mathrm{tr}_{\mathrm{adj}}(T^{(a}T^bT^{c)})$ nonzero on
$E_6$ (Jordan cubic on $\mathrm{Sym}^3(\mathbf{27}) =
\mathfrak j_3^{\mathbb O}$) and on $A_2 = \mathfrak{su}(3)$
(Gell-Mann $d$-tensor), zero on $\{A_1, G_2, D_4, F_4, E_7, E_8\}$.
**Precise error**: quadratic-only reading; cubic-only reading with
$E_6$ in safe list; form (a) Deligne $\setminus \{E_6, A_2\}$
strict; form (b) Deligne $\setminus \{E_6\}$ admitting unrefined
$A_2$.
**Correction — CANONICAL-ANOM-LOCUS (form c)**: $\mathrm{Anom}_1 = 0
\iff \mathfrak g \in (\mathrm{Deligne}^{\mathrm{exc}} \setminus
\{E_6, A_2\text{-unrefined}\}) \cup \{\mathrm{abelian}\} \cup
\{\mathrm{super-str}_{\mathrm{ad}} = 0\} \cup
\{\widehat{\mathfrak g}_{-h^\vee} \otimes K^{-1/2}\text{-refined}\}$.
$E_6$ strictly excluded; $A_2$-refined (Feigin--Frenkel critical
twist $K^{-1/2}$ + Dimofte-slab anomaly-inflow from Vol II Part V)
inside; $\{A_1, G_2, D_4, F_4, E_7, E_8\}$ unconditionally inside.
Every Vol II bulk-boundary anomaly inscription names both
obstructions and carries the $A_2$-refined qualifier plus
$K^{-1/2}$-refinement clause.
**Primary**: Deligne 1996 \emph{CRAS} 322; Cohen--de Man 1996
\emph{CRAS} 322; Cvitanović 2008 \emph{Group Theory} Ch 20;
Baez 2002 \emph{Bull AMS} 39; Frampton--Kephart 1983 \emph{Phys
Rev Lett} 50, 1347; Witten 1984 \emph{Comm Math Phys} 92, 455;
Feigin--Frenkel 1992 \emph{Comm Math Phys} 147; Dimofte 2014
slab anomaly-inflow; Vol III AP-CY262; AP-V2-54 / V2-AP157
(earlier Vol II form).
**Inscription**: Vol II
\texttt{chapters/connections/thqg\_perturbative\_finiteness.tex};
\texttt{chapters/theory/e2\_bar\_bulk\_boundary\_anomaly.tex}.
**Cross-ref**: Vol III AP-CY262 (primary form); Vol I AP979 /
Pattern 445; AP-V2-54 / V2-AP157 (earlier Deligne scope);
AP-CY50-E14 (cross-volume ledger); canonical preamble rows
40--42 ($\Psi$-sibling / $V^{s\natural}$ placement).

### AP-V2-76 / V2-AP179: PTVV shift $n = d - 4$ CY-dimension law at $d = 2$ gives shift $-2$; $E_2$-observables (2026-04-22)
**Severity**: High (Vol II $E_2$-scope PTVV discipline; Vol III AP-CY263 partner)
**Trigger**: Vol II PTVV / shifted-symplectic chapters cite the
$(-1)$-shift for hCS-type theories without naming the CY-dimension
$d$; at $d = 2$ (K3, $T^4$, bielliptic) the correct shift is $-2$
with $E_2$-observables, directly within Vol II's $E_2$-bar scope.
**Ghost**: hCS CY-dimension law $(n, E_k) = (d - 4, k = d - 2)$:
shift and $E_n$-index sum to $d - 2$ (the holomorphic disc
dimension after Dolbeault cohomology). At $d = 2$: $n = -2$,
$E_2$-observables; at $d = 3$: $n = -1$, $E_1$-observables; at
$d = 4$: $n = 0$, $E_0$-observables.
**Precise error**: uniform $(-1)$-shift collapses the $d$-dependent
hierarchy; Vol II's natural $E_2$-bar home at $d = 2$ hidden
behind a $d = 3$ quotation.
**Correction**: every Vol II PTVV / hCS / BV / Costello--Gwilliam
reference on CY$_d$ carries its shift $n = d - 4$ and
$E_{d-2}$-observable index; $d = 2$ entries explicitly note
shift $-2$ and $E_2$-factorisation on two holomorphic
disc-directions.
**Primary**: Pantev--Toen--Vaquie--Vezzosi 2013 \emph{Publ IHES}
117 Thm 2.5; Calaque--Pantev--Toen--Vaquie--Vezzosi 2017
arXiv:1506.03699 Prop 2.6; Lurie \emph{HA} \S 5.3; Costello--
Gwilliam 2021 Vol II \S 10--11; Vol III AP-CY263; AP-V2-35 /
V2-AP138 (Vol II PTVV shift / $d$-dependence).
**Inscription**: Vol II
\texttt{chapters/theory/ptvv\_shifted\_symplectic.tex} $d = 2$
shift-$(-2)$ row; \texttt{chapters/theory/e2\_bar.tex} PTVV
anchor.
**Cross-ref**: Vol III AP-CY263 (primary form); AP-V2-35 /
V2-AP138 (PTVV shift / $d$-dependence); AP-V2-73 / V2-AP176
(PTVV $d = 5$ closure).

### AP-V2-77 / V2-AP180: $\HH^0_{E_3}$ vs $\HH^0_{E_2}$ rank at bulk-boundary balance; compact-vs-open $E_2$ dualizability (2026-04-22)
**Severity**: Critical (Vol II $E_2$-dualizability discipline; Vol III AP-CY265 partner)
**Trigger**: Vol II $\SC^{\mathrm{ch,top}}$ bulk-boundary balance
statements cite $E_3$-Hochschild rank finiteness on open $\C^3$,
or conflate $\HH^0_{E_3}$-rank on $\C^3$ with $\HH^0_{E_2}$-rank
on $\C^2$ at the 3D HT QFT bulk / 2D boundary interface.
**Ghost**: on non-compact $\C^3$, $\HH^0_{E_3}(\Obs_{\mathrm{hCS}}
(\C^3, \mathfrak g)) \simeq \mathbb C[\![\tau_1, \tau_2, \tau_3]\!]$
(infinite rank, not dualizable in $\mathrm{Ch}$); on compact CY$_3$
$X$, $\HH^0_{E_3}(\Obs_{\mathrm{hCS}}(X, \mathfrak g)) \simeq
\bigoplus_q h^{0,q}(X) \cdot \HH^*_{\mathrm{Lie}}(\mathfrak g,
\mathbb C)^{[q]}$ (finite rank via Hodge truncation). The
$E_3$-dualizability gap is decisive for the bulk-boundary balance:
3D HT QFT on compact CY$_3$ lifts to a fully extended framed 3-TFT
(Lurie 2009 Thm 2.4.6); $\C^3$-locus does not.
**Precise error**: compactness dropped silently; $E_3$-dualizability
tied to $E_1$-output scope only; bulk-boundary balance breaks
when rank-infinity meets $E_2$-boundary finite-rank target.
**Correction**: every Vol II bulk-boundary statement at the
3D HT QFT / $E_2$-bar interface names compactness of the bulk
CY$_3$; $\C^3$-locus arguments explicitly flagged as
non-dualizable and non-extendable to compact CY$_3$. The
$\HH^0_{E_3}$ / $\HH^0_{E_2}$ rank match on the bulk-boundary
interface requires compact bulk.
**Primary**: Lurie 2009 \emph{On the classification of TFTs}
Thm 2.4.6; Gwilliam--Williams 2021 arXiv:2009.05037 Prop 5.3.2;
Francis 2013 \emph{Compos Math} 149 Thm 3.4; Ayala--Francis 2015
\emph{J Topology} 8 Thm 1.1; Calaque--Pantev--Toen--Vaquie--
Vezzosi 2017 arXiv:1506.03699; Vol III AP-CY265.
**Inscription**: Vol II
\texttt{chapters/theory/sc\_cht\_bulk\_boundary\_balance.tex};
\texttt{chapters/connections/thqg\_perturbative\_finiteness.tex}.
**Cross-ref**: Vol III AP-CY265 (primary form); AP-V2-34 /
V2-AP137 ($E_n$-on-wrong-object); AP-V2-25 / V2-AP128 (mixed
holomorphic pushforward); AP-V2-59 / V2-AP162 (6D hCS two-stage).

### AP-V2-78 / V2-AP181: $\HH^2_{E_2}$ rigidity non-critical vs critical Kac--Moody level (2026-04-22)
**Severity**: High (Vol II $E_2$-bar level-scope discipline; Vol III AP-CY266 partner)
**Trigger**: Vol II $E_2$-bar rigidity / deformation-theoretic
chapters state $\HH^2_{E_2}(\partial\mathrm{hCS}_5(\mathfrak{sl}_n),
-) = 0$ as uniform across all Kac--Moody levels, including critical
$k = -h^\vee$; directly in Vol II's $E_2$-bar domain.
**Ghost**: at \emph{generic} (non-critical) level, the Francis
chiral-tangent identification $\HH^2_{E_2}(\partial\mathrm{hCS}_5
(\mathfrak{sl}_n), -) \simeq H^2_{\mathrm{ch}}
(\widehat{\mathfrak{sl}}_n, V^{\mathrm{vac}}_k)$ reduces rigidity
to Whitehead 2 on semisimple Lie cohomology via Francis
spectral-sequence degeneration. At critical level $k = -h^\vee$,
$V^{\mathrm{vac}}_{-h^\vee}$ is NOT simple: its centre
$Z(V^{\mathrm{vac}}_{-h^\vee}) \simeq \mathrm{Fun}(\mathrm{Op}_
{\mathfrak{sl}_n^\vee})$ (Feigin--Frenkel; Frenkel--Ben-Zvi 2004
Thm 18.4.2) is polynomial in infinitely many generators; rigidity
requires separate analysis via opers-moduli smoothness.
**Precise error**: uniform-rigidity claim elides critical-level
subtlety; Whitehead 2 does not extend; Feigin--Frenkel
oper-smoothness argument dropped.
**Correction**: every Vol II $\HH^2_{E_2}$ rigidity statement for
affine Kac--Moody vertex algebras specifies level scope: generic
(non-critical) via Whitehead 2 + formality of $V^{\mathrm{vac}}_k$
+ Getzler--Kapranov spectral sequence; critical via Feigin--
Frenkel centre-as-functions on $\mathrm{Op}_{\mathfrak{sl}_n^\vee}$
+ oper moduli smoothness. The two arguments are distinct.
**Primary**: Francis 2013 \emph{Compos Math} 149 Thm 1.1, 2.29;
Frenkel--Ben-Zvi 2004 \emph{Vertex Algebras and Algebraic Curves}
Thm 3.4.3, 18.4.2; Feigin--Frenkel 1992 \emph{IJMPA} 7 S1A;
Whitehead 1937; Vol III AP-CY266.
**Inscription**: Vol II
\texttt{chapters/theory/e2\_bar\_rigidity.tex} level-scope clause;
\texttt{chapters/theory/kac\_moody\_deformations.tex}.
**Cross-ref**: Vol III AP-CY266 (primary form); AP-V2-34 /
V2-AP137 ($E_n$-on-wrong-object); canonical preamble central-charge
discipline; AP-V2-58 / V2-AP161 (Yangian-type discipline,
critical-level sibling).

### AP-V2-79 / V2-AP182: $\Lambda^{3,3}$-envelope rank-6 GBKM vs Fake-Monster $\mathrm{II}_{25,1}$ confusion (2026-04-22)
**Severity**: High (Vol II rank-6 envelope / Humbert-divisor discipline; Vol III AP-CY267 partner)
**Trigger**: Vol II Swiss-cheese / rank-6 envelope references place
$\mathfrak g_{\Delta_5}$ inside the Fake-Monster Lie algebra
$\mathfrak g_{\Phi_{12}}$ via a codimension-one timelike restriction
$\Lambda^{3,2} \hookrightarrow \Lambda^{3,3}$.
**Ghost**: $\Lambda^{3,3} = U \oplus U \oplus U$ is the unique
even unimodular lattice of rank 6 signature $(3,3)$ (Milnor;
Conway--Sloane Ch 15); the envelope GBKM on it has Cartan rank 6
signature $(3,3)$, hosting $\mathrm{Sp}_4(\mathbb Z)/\{\pm I\}
\simeq \mathrm{SO}_+(\Lambda^{3,2})$ at the Humbert-divisor level
(Gritsenko--Nikulin 1998 \emph{Duke} 94). The Fake-Monster lives
on $\mathrm{II}_{25,1}$ (rank 26, signature $(25,1)$, at $d = 5$
per canonical preamble / AP-V2-69), an entirely distinct lattice.
The Humbert-divisor fibre $\mathfrak g_{\Delta_5} \subset
\mathfrak g_{\Lambda^{3,3}}$ is a genuine codimension-one BKM
restriction, NOT a specialisation of the Fake Monster.
**Precise error**: rank-26 Fake-Monster ambient conflated with
rank-6 $\Lambda^{3,3}$-envelope ambient; two entirely distinct
BKM structures on two entirely distinct lattices.
**Correction**: every Vol II rank-6 envelope / $\mathfrak g_{\Delta_5}$
ambient statement names host lattice: $\Lambda^{3,3}$ rank 6 is
the Pfaffian envelope (heterotic BPS lift, Harvey--Moore 1996);
$\mathrm{II}_{25,1}$ rank 26 is the Fake-Monster non-compact host;
these do not inclusion-compare.
**Primary**: Borcherds 1995 \emph{Invent Math} 120 \S 13
(restriction theorem); Gritsenko--Nikulin 1998 \emph{Duke} 94
\S 2 ($\mathrm{Sp}_4 \simeq \mathrm{SO}(3,2)$); Harvey--Moore
1996 hep-th/9510182 eqs (4.15)--(4.20); Nikulin 1979 \emph{Izv AN
SSSR} 43; Vol III AP-CY267.
**Inscription**: Vol II
\texttt{chapters/connections/rank\_six\_envelope.tex};
\texttt{chapters/theory/humbert\_divisor\_restriction.tex}.
**Cross-ref**: Vol III AP-CY267 (primary form); AP-V2-69 /
V2-AP172 (Fake-Monster $d = 5$); canonical preamble rows 20--21
(Monster / Fake-Monster Cartan-rank discipline);
AP-V2-66 / V2-AP169 ($F_3$ real-root subalgebra of
$\mathfrak g_{\Delta_5}$).

### AP-V2-80 / V2-AP183: Chiral Booth--Lazarev as three-obstruction programme vs associative packaging on Vol II curved coderived (2026-04-22)
**Severity**: High (Vol II curved coderived framework discipline; Vol III AP-CY268 partner)
**Trigger**: Vol II curved-coderived / chiral-bar--cobar chapters
cite chiral Booth--Lazarev $\mathrm{FactCoAlg}^{\mathrm{cpt}}_
{\mathrm{crv}}(\mathrm{Ran}(C)) \simeq \mathrm{ChirAlg}(C)$ as
automatic lift of the associative curved bar--cobar Quillen
equivalence via ``factorisation-tensor packaging''.
**Ghost**: three distinct structural obstructions are unsettled.
(i) \emph{Ran-space Smith recognition}: $\mathrm{Ran}(C)$ is a
colimit of schemes $C^n / S_n$; generating cofibrations must be
stratification-compatible with $j_n^*$ restrictions pulling back
into lower-$m$ generators; conilpotence stratified by the
Ran-space filtration, not a single unstratified filtration.
(ii) \emph{Genus-tower curvature as operadic section}: curvature
$m_0^{(g,n)}$ is a family of sections of $\lambda_g \otimes
H^2(\mathcal A)$ on $\overline{\mathcal M}_{g,n}$ satisfying
boundary-clutching compatibility (separating + non-separating);
a modular form on $\overline{\mathcal M}$ with sewing as operadic
structure, not a scalar in $\mathcal A^2$.
(iii) \emph{Analytic IndHilb sewing}: the algebraic coderived
category and the Moriwaki IndHilb analytic sewing envelope are
distinct; comparison requires nuclearity + trace-class check
on topological vector spaces that Booth--Lazarev's purely
algebraic setup does not address.
**Precise error**: conjectural three-obstruction lift stated as
``the Quillen equivalence on Ran-space coalgebras''; overstates
theorem-status relative to Vol II's curved-coderived framework.
**Correction**: every Vol II chiral Booth--Lazarev citation
carries the three-obstruction qualifier;
$\kappa_{\mathrm{ch}}$-curving $m_0^{(g)} = \kappa_{\mathrm{ch}}
\cdot \lambda_g$ is the \emph{boundary-descent datum} on
$\overline{\mathcal M}_{g,n}$, not a derived-category-level
packaging. The three obstructions (Ran-space Smith,
genus-tower curvature operadic structure, analytic sewing)
named jointly.
**Primary**: Booth--Lazarev 2023 arXiv:2304.08409 (associative
coderived Quillen); Beilinson--Drinfeld 2004 \emph{Chiral
Algebras} AMS Colloq Publ 51 Ch 3 (Ran space, factorisation);
Francis 2013 \emph{Compos Math} 149 ($E_n$-tangent, operadic
model structure); Kontsevich--Soibelman 2010
\emph{Deformation Theory} Ch 3 ($L_\infty$ on smooth schemes);
Vol III AP-CY268.
**Inscription**: Vol II
\texttt{chapters/theory/curved\_coderived.tex} three-obstruction
qualifier; \texttt{chapters/theory/chiral\_bar\_cobar.tex}.
**Cross-ref**: Vol III AP-CY268 (primary form); AP-V2-72 /
V2-AP175 (MC5 sewing on Stage 2); AP-V2-30 / V2-AP133 (chain-level
vs $(\infty,1)$-functor lift); AP-V2-41 / V2-AP144 (frontier
$(\infty,1)$-equivalence).


### AP-V2-81 / V2-AP184: $\widehat{\mathfrak{sl}}_2$ vs $\widehat{\mathfrak{gl}}(1|1)$ scope-discipline on compact-Koszul descents (2026-04-23, sibling Vol III AP-CY305).
$\mathrm{CoHA}(Y^{\mathrm{conifold}}) \cong Y^+(\widehat{\mathfrak{gl}}(1|1))$ is the primary Vol III identification (Li-Yamazaki arXiv:2003.08909 §8.3.6.3); $Y^+(\widehat{\mathfrak{sl}}_2)$ is the ungraded shadow via supertrace projection of the central Cartan. On Vol II curved-coderived compact-Koszul descents the two appear at distinct scopes: the supergraded form appears on $E_3$-factorisation over $\mathbf Y$ (primary), the ungraded form via the semisimple quotient. **Counter**: Vol II compact-Koszul applications to conifold-type CY$_3$ must specify the super graded scope.

### AP-V2-82 / V2-AP185: Super 5D hCS $\to$ $E_1$-chiral all-orders is OPEN on super gauge algebras (2026-04-23, sibling Vol III AP-CY298).
CGY arXiv:1810.01970 5D hCS $\to$ Yangian VOA all-orders requires simply-laced Lie $\mathfrak g$ with non-degenerate Killing. For $\mathfrak g = \mathfrak{gl}(m|n)$ the Killing is degenerate and super-KT is $E_2$-only; all-orders extension OPEN. **Counter**: Vol II $E_1$-chiral claims on super gauge algebras must carry the OPEN flag beyond 1-loop.

### AP-V2-86 / V2-AP186: Super-KT formality is $E_2$-only; $E_3$ open (2026-04-23, sibling Vol III AP-CY299).
Kontsevich-Tamarkin $E_n$-formality extends to super dg-Lie in the Ginzburg-Schedler arXiv:0807.0174 sense only to $E_2$. Vol II $E_3$-chiral statements that invoke super-formality must carry OPEN flag at $E_3$. **Counter**: super-formality on Vol II $E_3$-factorisation constructions must specify $E_2$.

### AP-V2-87 / V2-AP187: Two-chart Čech atlas is not a Weiss cover — QC descent vs factorisation locality (2026-04-23, sibling Vol III AP-CY308).
Wrong: treating the two-chart Čech atlas $\{U_+, U_-\}$ of a resolved CY$_3$ (e.g. conifold, where each $U_\pm \cong \mathbb C^3$) as a "factorisation-algebra gluing" datum on Vol II $E_n$-factorisation constructions. Correct: Weiss covers (Costello-Gwilliam arXiv:2210.13036 Def 6.1.6) require every finite configuration of points to embed simultaneously into a single open; a two-chart atlas fails this whenever a configuration has points on both charts. Hence the two-chart atlas recovers QC-descent for $\mathrm{CoHA}$-as-sheaf (Kontsevich-Soibelman arXiv:1006.2706 §6.3) but NOT factorisation-algebra locality (Beilinson-Drinfeld, Francis-Gaitsgory arXiv:1103.5803 Thm 3.6.2, Francis arXiv:1303.0305, Lurie HA §5.5.4); the latter requires the Weiss refinement $\mathfrak D^{\sqcup}$ of disjoint unions of contractible discs. **Counter**: Vol II $E_n$-factorisation on toric CY$_3$ specifies QC-descent (minimal refinement sufficient) vs factorisation-locality (Weiss refinement required); these are not interchangeable.

### AP-V2-88 / V2-AP188: $\kappa_{\mathrm{ch,BV}}$ is a genuinely new subscripted invariant distinct from $\kappa_{\mathrm{ch}}$ on non-compact CY$_3$ (High, sibling Vol III AP-CY324).
Wrong: identifying three apparent values $\{+1, 0, -1\}$ for "$\kappa_{\mathrm{ch}}$(conifold)" as alternative computations of one invariant on Vol II BV / $E_n$-factorisation content. Correct: they are three distinct subscripted invariants under one chain-level convention (Kontsevich-Soibelman DT / Costello-Li holomorphic BV): $\kappa_{\mathrm{ch}}$ (DT / motivic BPS count), $\kappa_{\mathrm{cat}} = \chi(\mathcal O_X)$ (holomorphic Euler characteristic), $\kappa_{\mathrm{ch,BV}}$ (Costello-Li BCOV 1-loop curving via Polyakov 1981 Ch.~9 ghost supertrace, value $\mathrm{str}_{\mathfrak{gl}(1|1)}(\mathrm{ghost}) = -1$ at BRST $c = -2$). Polyakov ghost-mode balance $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch,BV}} = \kappa_{\mathrm{cat}}$ holds on $\mathsf G$-class free-field CY$_3$ with $\chi_{\mathrm{top}} = 2$, NOT universal. **Counter**: Vol II BV / BCOV content on non-compact CY$_3$ must use the five-$\kappa$ ladder $\{\kappa_{\mathrm{ch}}, \kappa_{\mathrm{cat}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}, \kappa_{\mathrm{ch,BV}}\}$; $\kappa_{\mathrm{ch,BV}}$ is a load-bearing new subscript for BV-anomaly-sensitive content.

### AP-V2-89 / V2-AP189: 5D hCS BV anomaly on super gauge: 1-loop VERIFIED, 2-loop+ OPEN (Medium, sibling Vol III AP-CY323).
Wrong: Vol II BV / factorisation content citing "Costello-Yagi all-orders theorem applies to $\mathfrak{gl}(1|1)$ / super gauge" without specifying obstruction status. Correct: the BV anomaly coefficient is $d^{abc} = \mathrm{str}(t^a \{t^b, t^c\})$; on $\mathfrak{gl}(1|1)$ direct basis computation gives $d^{abc} = 0$ identically (Cartan $\mathrm{str}(H^2) = \mathrm{str}(N^2) = 0$; odd pair $\psi^\pm$ carries opposite supertrace signs), so the 1-loop wheel is verified to vanish. Higher-loop local cohomology $H^1_{\mathrm{loc}}(\mathfrak{gl}(1|1), \mathcal O_{\mathrm{loc}})^{\geq 2}$ is not auto-killed (super-KT is $E_2$-only); 2-loop and higher OPEN. **Counter**: Vol II BV-anomaly stratifies on super gauge: 1-loop verified via basis, higher-loop OPEN per $E_2$-only super-KT.

### AP-V2-90 / V2-AP190: Bialgebra vs Hopf on $E_n$-factorisation positive halves (Medium, sibling Vol III AP-CY327).
Wrong: labelling $Y^+(\mathfrak g)$ (positive half of a Yangian / quantum affine algebra) as "Hopf" on Vol II $E_n$-factorisation content. Correct: $Y^+$ is an associative bialgebra; the antipode $S$ lives only on the Drinfeld double $D(Y^+) = Y$. Super positive halves (from $\widehat{\mathfrak{gl}}(1|1)$-type data) are $\mathbb Z_2$-graded bialgebras in super-vector-spaces. Strict-Hopf on rational / trigonometric / toroidal equivariance strata; elliptic case is quasi-Hopf with Felder-Jimbo-Konno dynamical associator. **Counter**: Vol II $E_n$-factorisation on positive-half quantum affinisations uses "bialgebra" / "$\mathbb Z_2$-graded bialgebra" / "quasi-Hopf" per stratum; never blanket "Hopf".

### AP-V2-91 / V2-AP191: BCOV cocycle target is $H^{0,1}(X, \mathcal O_X)$, not $H^{0,1}(X, \mathrm{Sym}^{\leq 2} T_X^*)$ (Medium, sibling Vol III AP-CY341).
Wrong: writing BCOV 1-loop anomaly class on Vol II BV / $E_n$-factorisation as $\alpha_{\mathrm{BCOV}}(X) = (\chi(X) / 24)[\Omega_X]^{0,1} \in H^{0,1}(X, \mathrm{Sym}^{\leq 2} T_X^*)$. Correct: BCOV anomaly class lives in $H^{0,1}(X, \mathcal O_X)$ — the $[\Omega_X]^{0,1}$ Dolbeault class is an $\mathcal O_X$-coefficient class (the $(0, 1)$-Dolbeault lift of the Atiyah class of the CY trivialisation $\omega_X \cong \mathcal O_X$), not a polyvector-field class. Primary: Costello-Li arXiv:1606.00365 Prop 5.2; BCOV hep-th/9309140; Polyakov 1981 Ch.~9. **Counter**: Vol II BCOV-target claims place the $(\chi / 24)$ class in $H^{0,1}(X, \mathcal O_X)$; higher-symbol targets are category errors.

### AP-V2-92 / V2-AP192: BCOV factor-split admits four vanishing mechanisms on compact / non-compact CY$_3$ (Low, sibling Vol III AP-CY342).
Wrong: claiming $\alpha_{\mathrm{BCOV}}(X) \neq 0$ on all non-quintic compact CY$_3$ in Vol II BV / (O2)-obstruction content. Correct: the factor-product $(\chi(X) / 24) \cdot [\Omega_X]^{0,1}$ admits four distinct vanishing mechanisms — (i) conifold / non-compact retractable: $[\Omega_{\mathbf Y}]^{0,1} = 0$ via retraction $\mathbf Y \simeq \mathbb P^1$; (ii) strict quintic / $h^{0,1} = 0$: Dolbeault factor vanishes; (iii) $K3 \times E$ Künneth: $\chi = 24 \cdot 0 = 0$ topological prefactor; (iv) generic CY$_3$ with abelian factor: product vanishes. Only compact CY$_3$ without abelian factor and with $h^{0,1} > 0$ carries genuinely non-zero $\alpha_{\mathrm{BCOV}}$. **Counter**: Vol II (O2)-obstruction statements identify which vanishing mechanism applies; blanket "compact $\Rightarrow$ non-zero $\alpha_{\mathrm{BCOV}}$" is wrong.

### AP-V2-93 / V2-AP193: 4 compact-CY$_3$ obstructions reduce to 2.5, not 4 independent (Medium, sibling Vol III AP-CY309).
Wrong: listing (O1) toric fan-completeness, (O2) BCOV $\alpha_{\mathrm{BCOV}}$, (O3) $\mathrm{Aut}^0$ rigidity, (O4) finite-quiver equivariance as 4 independent obstructions to compact-CY$_3$ chart-wise factorisation-algebra assembly on Vol II $E_n$ content. Correct: direct logical reductions give (O1) $\Leftrightarrow$ (O3) (two facets of Bogomolov-Matsumura rigidity) and (O1) $\Rightarrow$ (O4), with only (O2) logically independent. Effective count is 2.5: (O1 $\equiv$ O3) + (O2) with (O4) downstream. BCOV curving (O2) is independent because it sources from 1-loop BV counter-term, not automorphism geometry. **Counter**: Vol II compact-CY$_3$ obstruction statements derive the 2.5-count explicitly; "four independent obstructions" obscures the Bogomolov-Matsumura origin.

### AP-V2-94 / V2-AP194: $B_3$-braid on local $\mathbb P^2$ via $\pi_1(\mathrm{Conf}_3(\mathbb C))$, not Bondal-Orlov 2002 alone (Medium, sibling Vol III AP-CY340).
Wrong: citing Bondal-Orlov arXiv:math/0206295 as the primary source for the $B_3$-braid mutation action on local $\mathbb P^2$ nine-arrow quiver in Vol II factorisation / derived-category content. Correct: Bondal-Orlov 2002 is a derived-equivalence paper and does NOT establish braid-group action on mutations. Correct primary sources: Bondal-Polishchuk 1993 (helix autoequivalences); Kuznetsov arXiv:math/0610957 ($B_n$-action on exceptional collections); Bridgeland arXiv:0909.4299 ($B_3 = \pi_1(\mathrm{Conf}_3(\mathbb C))$ on 3-vertex derived categories); Seidel-Thomas arXiv:math/0001043 (spherical-twist braid relations from Ext-adjacency). **Counter**: $B_3$-mutation-action citations in Vol II factorisation content separate helix autoequivalence (Bondal-Polishchuk), exceptional-collection mutation (Kuznetsov), configuration-space identification (Bridgeland), and spherical-twist braid (Seidel-Thomas); Bondal-Orlov 2002 alone is insufficient.
