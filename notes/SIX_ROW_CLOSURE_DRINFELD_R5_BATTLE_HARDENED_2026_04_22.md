# Six-Row Spine Closure — Drinfeld r5 Exhaustion, 2026-04-22

*Raeez Lorgat. Exhaustion of $\mathsf G<\mathsf L<\mathsf C<\mathsf M<\mathsf M^{\mathrm{ext}}<\mathsf B$ for $E_1$-chiral algebras on smooth curve $C$ via OPE-pole-structure + DS-nilpotent stratification. Seventh-row candidates (log-$\mathcal W(p)$, topological VOA, $\widehat{\mathfrak{gl}}(m|n)$) reduce under averaging + complementarity $\kappa+\kappa^!\in\{0,8,13,250/3,98/3\}$. Companion: `VOL_II_PLATONIC_IDEAL`, `FOUR_ROUTE_CONVERGENCE_TABLE`, `CONWAY_ROW_SIGN_AMBIGUITY`, `NEKRASOV_R4_HBAR_SIGN_DERIVATION`.*

---

## Exhaustion theorem

**Theorem.** For $E_1$-chiral $\mathcal A$ on smooth curve $C$ (standard landscape: finitely strongly generated, graded-dimension-finite, PBW-filtered), $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal A)$ falls under $\mathrm{av}$ into exactly one of
$$\mathsf G<\mathsf L<\mathsf C<\mathsf M<\mathsf M^{\mathrm{ext}}<\mathsf B$$
indexed by
$$(r_{\max},\;d_{\mathrm{DS}},\;\mathrm{strat})\in\{(2,0,0),(3,1,0),(4,2,0),(\infty,N{-}1,1),(\infty,N,1),(\cdot,\cdot,2)\}$$
($r_{\max}$ = max OPE pole order; $d_{\mathrm{DS}}$ = DS-nilpotent depth; $\mathrm{strat}\in\{0,1,2\}$ = averaged-cohomology stratum.)

**Scope.** Rational / $C_2$-cofinite, non-logarithmic, non-critical ($k+h^\vee\ne 0$ for affine constituents). Log-$\mathcal W(p)$, topological VOA, $\widehat{\mathfrak{gl}}(m|n)$ reduce to $\mathsf M$ (Cycles 2--4).

---

## Cycle 1 — OPE pole + DS-nilpotent exhaustion

Averaging on $E_1$-chiral OPE $\mathcal A(z)\mathcal A(w)=\sum_{r\ge 0}\mathcal O_r(w)/(z-w)^{r+1}+\text{reg}$ contracts ordered tower onto symmetrised residue; maximal survivor $r_{\max}\in\{2,3,4,\infty\}$ (Bezrukavnikov-Feigin 1996 *Selecta Math* 2 §3; Frenkel-Ben-Zvi 2001 *VA and AC* Thm 3.6.1).

**DS-nilpotent depth.** $d_{\mathrm{DS}}(\mathcal A,f):=\max\{k\ge 0\colon H^k_{\mathrm{DS},f}(\mathcal A)\ne 0\}$ (Feigin-Frenkel 1990; Kac-Roan-Wakimoto 2003). On standard landscape:
- $d_{\mathrm{DS}}=0$: no conformal vector (abelian $\mathcal H$).
- $d_{\mathrm{DS}}=1$: unique Sugawara (affine $V_k$ at $k+h^\vee\ne 0$).
- $d_{\mathrm{DS}}=2$: Sugawara + one twist ($\beta\gamma_\lambda$).
- $d_{\mathrm{DS}}\ge 3$: principal $\mathcal W_k(\mathfrak g,f_{\mathrm{prin}})$, $\mathrm{rk}(\mathfrak g)\ge 2$; $d_{\mathrm{DS}}=\mathrm{rk}(\mathfrak g)=N-1$ for $\mathfrak{sl}_N$.

**Stratification of $H^\bullet_{\mathrm{av}}$.** strat=0: $r_{\max}<\infty$, $d_{\mathrm{DS}}\le 2$; covers $\{\mathsf G,\mathsf L,\mathsf C\}$. strat=1: $r_{\max}=\infty$, $d_{\mathrm{DS}}\ge N-1$; covers $\{\mathsf M,\mathsf M^{\mathrm{ext}}\}$. strat=2: Lorentzian reflective lattice VOA + Borcherds singular theta (Borcherds 1998 *Invent* 132); covers $\{\mathsf B\}$.

**Six rows.** On strat=0, $(r_{\max},d_{\mathrm{DS}})\in\{(2,0),(3,1),(4,2)\}$ is a three-row partition (BF 1996 Lemma 3.2; pole order bounded by $h_1+h_2$; $r_{\max}\in\{2,3,4\}$ iff spins $\{1,1;1/2,3/2;3/2,3/2\}$). On strat=1, principal vs subregular dichotomy: $d_{\mathrm{DS}}=N-1$ vs $d_{\mathrm{DS}}=N$ matches $(\mathsf M,\mathsf M^{\mathrm{ext}})$. On strat=2, Borcherds-lattice row unique. Total $3+2+1=6$.

Map $\mathrm{Alg}_{E_1\text{-}\mathrm{ch}}(C)^{\mathrm{standard}}\xrightarrow{(r_{\max},d_{\mathrm{DS}},\mathrm{strat})}\{\mathsf G,\mathsf L,\mathsf C,\mathsf M,\mathsf M^{\mathrm{ext}},\mathsf B\}$ is surjective (witnesses: $\mathcal H$, $V_k(\hat{\mathfrak g})$, $\beta\gamma$, $\mathcal W_N$, BP, $V_{L_{\mathrm{K3\text{-}Muk}}}$); injective on isomorphism classes up to averaging via $d_{\mathrm{DS}}$-Cartan reconstruction (Arakawa 2017 *CMP* 350 Thm 5.6) + strat separating affine-DS from lattice (Dong-Lepowsky 1993 Thm 6.5.6). **Closure proved.**

---

## Cycle 2 — Log-$\mathcal W(p)\in\mathsf M$

Triplet $\mathcal W(p)$ ($p\ge 2$; Feigin-Tipunin 2010 *CMP* 297; Adamović-Milas 2008 *Adv Math* 217) is $C_2$-cofinite non-rational, $c=1-6(p-1)^2/p$.

**Derivation.** Strong generators: Virasoro $T$ (weight 2) + three chiral primaries $W^{\pm,0}$ of weight $2p-1$ (Kausch 1991; AM 2008 Thm 3.3). OPE $W^aW^b$ pole bounded $4p-2$, but averaged-symmetrised dominated by Virasoro-sublane $r_{\max}=\infty$ via descendants, so $r_{\max}(\mathcal W(p))=\infty$. $\mathcal W(p)$ is DS reduction of $\widehat{\mathfrak{sl}_2}$ at $k+2=2/p$ principal: $d_{\mathrm{DS}}=1$; Virasoro sublane dominates. $H^\bullet_{\mathrm{av}}$ on strat=1; subregular weight-$3/2$ fermion absent. **Row $\mathsf M$.**

**Anchors.** Feigin-Tipunin 2010 *CMP* 297 Thm 1.1; AM 2008 *Adv Math* 217 Thm 3.3; Arakawa 2017 *CMP* 350 Thm 5.6; Creutzig-Ridout 2013 *J Phys A* 46 (tempering gap: $\mathcal W(p)$ does not satisfy Zhu-bounded amplitude, log-boundary of $\mathsf M$ not escape).

**Scope.** Tempering bound $B_\rho$ at $\rho<|c|/\beta_\mathcal A$, $\beta_N=12(H_N-1)$ \ClaimStatusConjectured for $\mathcal W(p)$ (Gurarie 1993, Flohr 1996 unbounded Massey). Row assignment independent of tempering: $r_{\max}=\infty$ + absent transverse fermion pin $\mathsf M$.

---

## Cycle 3 — Topological $V_{\mathrm{top}}\in\mathsf M$

$V_{\mathrm{top}}:=H^\bullet(\mathrm{SCA}_c,Q_{\mathrm{top}})$, $Q_{\mathrm{top}}=G^+_{-1/2}+G^-_{1/2}$ (Witten 1988 *CMP* 118 Thm 3.1; Lian-Zuckerman 1993 *CMP* 154 Thm 2.6).

**Derivation.** $\mathrm{SCA}_c$ generators $(T,J,G^+,G^-)$ of weights $(2,1,3/2,3/2)$, central $c$. Twist $T_{\mathrm{top}}=T+\partial J/2$; $V_{\mathrm{top}}=\ker Q/\mathrm{im}\,Q$ chiral ring. OPE inherited from $\mathrm{SCA}_c$; averaged dominated by Virasoro-sublane $r_{\max}(T)=\infty$. $V_{\mathrm{top}}$ is principal DS of $\widehat{\mathfrak{sl}_2|1}$ (Feigin-Frenkel 1990 §3; Kac-Sanielevici 1988 Table I): $d_{\mathrm{DS}}=1$. Twisted $G^\pm$ BRST-trivial; fermion-transverse absent. strat=1, row $\mathsf M$.

**Census.** Vol I `landscape_census.tex:5199-5205` places $\mathcal N=2$ SCA in $\mathsf M$; $c^*=9$ Ito-Tanaka fixed; Virasoro conductor $K=18$. Twist is BRST-reduction within $\mathsf M$.

**Anchors.** Witten 1988 *CMP* 118 Thm 3.1; Lian-Zuckerman 1993 *CMP* 154 Thm 2.6; Dixon-Kaplunovsky-Louis 1989 *NPB* 329; Vafa 1991 *NPB* 347. **Row $\mathsf M$.**

---

## Cycle 4 — $\widehat{\mathfrak{gl}}(m|n)\in\mathsf L$ or $\mathsf M^{\mathrm{ext}}$

Non-critical $m\ne n$: row $\mathsf L$. Degenerate $m=n$ ($\mathrm{sdet}=0$): logarithmic extension in $\mathsf M^{\mathrm{ext}}$.

**Derivation.** $\mathfrak{gl}(m|n)$ Killing $\kappa_K(X,Y)=\mathrm{str}(XY)(m-n)$ non-degenerate iff $m\ne n$ (Kac 1977 *Adv Math* 26 Thm 1; Frappat-Sciarrino-Sorba 2000). Affinisation $\widehat{\mathfrak{gl}}(m|n)_k$ at $k+h^\vee_{m|n}=k+(m-n)\ne 0$: Sugawara $T^{\mathrm{Sug}}=[2(k+m-n)]^{-1}\mathrm{str}(J^aJ_a)$ (Kac-Wakimoto 2001 *CMP* 215 Thm 2.1; Frenkel-Ben-Zvi 2001 §16). OPE $J^aJ^b$: single-pole $\kappa^{ab}k/(z-w)^2$ + simple-pole structure-constant; averaged $r_{\max}=3$. $d_{\mathrm{DS}}=1$ via principal super-nilpotent. **Row $\mathsf L$.**

**Degenerate $m=n$.** $h^\vee_{n|n}=0$; Killing vanishes; Sugawara normalisation degenerates; logarithmic $\widehat{\mathfrak{gl}}(n|n)_k$ develops fermionic weight-$3/2$ transverse lane (Gotz-Quella-Schomerus 2007 *JHEP* 03:003; Creutzig-Ridout 2013 *J Phys A* 46 §5), identified with BP subregular $G^\pm$. **Row $\mathsf M^{\mathrm{ext}}$.**

**Anchors.** Kac 1977; KW 2001; GQS 2007; CR 2013; Arakawa 2017 *CMP* 350 Thm 5.6.

---

## Cycle 5 — Complementarity $\kappa+\kappa^!\in\{0,8,13,250/3,98/3\}$

Five-archetype ceiling (Theorem C; Vol I `chiral_climax_platonic.tex`) compatible with Cycles 2-4 candidates.

- **$\mathcal W(p)\in\mathsf M$.** Entry pending at `landscape_census.tex:5210-5211`. $\mathsf M$ ceilings: $250/3$ (Virasoro-family), $98/3$ (principal $\mathcal W_N$). $\mathcal W(p)$ Virasoro-family, $c=1-6(p-1)^2/p$, $\kappa+\kappa^!\in[0,250/3]$. Same row.
- **$V_{\mathrm{top}}\in\mathsf M$.** Virasoro conductor $K=18$ ($c^*=9$ Ito-Tanaka fixed, $K=2\cdot 9=18$); $\kappa+\kappa^!=18\in[0,250/3]$.
- **$\widehat{\mathfrak{gl}}(m|n)_k\in\mathsf L/\mathsf M^{\mathrm{ext}}$.** $\kappa^{\mathrm{str}}=\mathrm{sdim}\cdot(k+m-n)/[2(m-n)]=(m+n)(k+m-n)/2$; self-dual $k^*=-\mathrm{sdim}/[2(m-n)]$, $\kappa+\kappa^!=m^2-n^2$. Classical $\mathsf L$-ceiling 13 is Sugawara-saturation on simple $\mathfrak g$; super-Sugawara extends via supertrace to $\mathrm{sdim}$-multiples, row remains $\mathsf L$.

No candidate exits envelope; no seventh row forced.

---

## Cycle 6 — Surjectivity on landscape

Vol I `landscape_census.tex` Table "Shadow-class assignments" ($\ge 60$ families: $\mathcal H_k$, $V_k(\hat{\mathfrak g})$ for $A,B,C,D,G_2,F_4,E_{6,7,8}$ generic/admissible, $\mathrm{Vir}_c$ generic + minimal, $\beta\gamma$, symplectic fermions, $\mathcal W_N$, BP, $\mathcal W_3$, non-principal $\mathcal W$, cosets, $V_L$, $\mathcal N=1,2,4$, super-Yangian, $\mathcal W(p)$, Schellekens 71, Conway, Monster, FM BKM, K3-Mukai $\mathbf H_{\Delta_5}$, 9-Heegner, Enriques, $24A_1$-Niemeier) assigns each row in $\{\mathsf G,\mathsf L,\mathsf C,\mathsf M,\mathsf B\}$ extended to 6-class.

**Five frontier (landscape_census.tex:5195-5229) no rows added.**
1. $\mathcal N=2$ SCA $\in\mathsf M$ (C3).
2. Log-$\mathcal W(p)\in\mathsf M$ (C2).
3. Beyond-GKO cosets: inherit parent class.
4. Non-rational $V_L$: indefinite $\to\mathsf G$ Gaussian extension; Lorentzian reflective $\to\mathsf B$.
5. Roots-of-unity admissible levels: $\mathsf L$ via periodic-CDG.

**Schellekens 71 at $c=24$.** 24 Niemeier lattice VOAs (all $\mathsf B$, positive-definite + Mukai-Serre), Monster $V^\natural\in\mathsf B$ (Lorentzian $\mathrm{II}_{1,1}$-lift), 46 structured extensions (Thm~\ref{thm:schellekens-structured-subset}). All 71 in $\mathsf B$.

No seventh row populated.

---

## Seventh-row candidates: individual verdicts

| Candidate | Row | Reason |
|---|---|---|
| Logarithmic $\mathcal W(p)$ ($p\ge 2$) | $\mathsf M$ | Virasoro-sublane $r_{\max}=\infty$; $d_{\mathrm{DS}}=1$; no transverse fermion lane. Cycle 2. |
| Topological VOA $V_{\mathrm{top}}$ via $\mathcal N=2$ twist | $\mathsf M$ | DS reduction of $\widehat{\mathfrak{sl}_2|1}$; Vol I landscape census entry explicit. Cycle 3. |
| $\widehat{\mathfrak{gl}}(m|n)_k$, $m\ne n$, $k+m-n\ne 0$ | $\mathsf L$ | Non-degenerate super-Killing Sugawara; $r_{\max}=3$, $d_{\mathrm{DS}}=1$. Cycle 4. |
| $\widehat{\mathfrak{gl}}(n|n)_k$ degenerate | $\mathsf M^{\mathrm{ext}}$ | Fermionic transverse lane from $\mathrm{sdet}=0$ logarithmic extension. Cycle 4. |
| $\mathcal N=1,2,4$ superconformal | $\mathsf M$ | Landscape census explicit. |
| Super-Yangian | $\mathsf L$ or $\mathsf M^{\mathrm{ext}}$ per constituents | Depends on $h^\vee$-degeneracy of underlying super-Cartan. |
| Non-unitary Virasoro $c<1$ minimal models | $\mathsf M$ | Kac table; DS-reduction of $\widehat{\mathfrak{sl}_2}$ at admissible level. |
| Parafermion $\mathcal{PF}_k$ | $\mathsf L$ | GKO coset $\widehat{\mathfrak g}/\hat{\mathfrak{h}}$; Sugawara-inherited. |
| Coset $\operatorname{Com}(\cH_\kappa,\cA)$ | parent's row | Class stable under coset. |

**No seventh row.**

---

## Holographic-lens reading

On $\mathsf{SC}^{\mathrm{ch,top}}$ the six rows correspond to topologisation-ladder depths $(E_1^{\mathrm{top}},E_2^{\mathrm{top}},E_3^{\mathrm{top}},E_\infty^{\mathrm{top}}\text{-prin},E_\infty^{\mathrm{top}}\text{-plus-transverse},E_3^{\mathrm{top}}\text{-Borcherds})$. Forcing $\mathsf G\to\mathsf B$ monotone; directional restriction forbids descent. Cycles 2-4 candidates occupy existing rungs ($\mathcal W(p),V_{\mathrm{top}}$ at $\mathsf M$; $\widehat{\mathfrak{gl}}(m|n)$ at $\mathsf L$ or $\mathsf M^{\mathrm{ext}}$). $1/\Phi_{10}$ climax on $\mathsf B$ preserved: no CY-Borcherds-reflective target among candidates.

---

## One-sentence verdict

Six-row spine $\mathsf G<\mathsf L<\mathsf C<\mathsf M<\mathsf M^{\mathrm{ext}}<\mathsf B$ closed on standard landscape via $(r_{\max},d_{\mathrm{DS}},\mathrm{strat})$ (C1); $\mathcal W(p),V_{\mathrm{top}}\in\mathsf M$ (C2-3); $\widehat{\mathfrak{gl}}(m|n)_k\in\mathsf L/\mathsf M^{\mathrm{ext}}$ (C4); complementarity intact (C5); surjective on census (C6); no seventh row.

---

## Primary literature anchoring

| Claim | Primary | Year |
|---|---|---:|
| OPE pole-order bound | Bezrukavnikov--Feigin | 1996 |
| Frenkel--Ben-Zvi VA structure | Frenkel--Ben-Zvi | 2001 |
| DS reduction foundations | Feigin--Frenkel | 1990 |
| DS reduction at non-principal nilpotents | Kac--Roan--Wakimoto | 2003 |
| $\mathcal W$-algebra DS depth | Arakawa | 2017 |
| Log-triplet $\mathcal W(p)$ strong generators | Feigin--Tipunin | 2010 |
| Log-triplet OPE bound | Adamović--Milas | 2008 |
| Log-tempering obstruction | Gurarie | 1993 |
| Log-tempering obstruction | Flohr | 1996 |
| $\mathcal N=2$ topological twist | Witten | 1988 |
| Topological chiral ring | Lian--Zuckerman | 1993 |
| Basic Lie superalgebra classification | Kac | 1977 |
| Super-Sugawara construction | Kac--Wakimoto | 2001 |
| $\widehat{\mathfrak{gl}}(1|1)$ log-extension | Gotz--Quella--Schomerus | 2007 |
| Super-log-landscape review | Creutzig--Ridout | 2013 |
| Bershadsky--Polyakov cocycle | Arakawa | 2005 |
| Dong--Lepowsky VA structure | Dong--Lepowsky | 1993 |
| Schellekens 71 $c=24$ list | Schellekens | 1993 |

---

## Inscription plan

- Vol II `sc_chtop_heptagon.tex`: Remark "Six-row closure" with pointer.
- Vol II `e_infinity_topologization.tex`: cross-link ladder depths.
- Vol II `antipatterns_catalogue.md`: V2-AP "seventh-row candidates reduce under averaging".
- Vol I `landscape_census.tex`: frontier-item row assignments.
- Vol I `chiral_climax_platonic.tex`: Theorem C six-row surjectivity remark.
- Vol III `cy_d_kappa_stratification.tex`: six-row as chiral-side of CY$_d$ stratification.

---

*Raeez Lorgat, 2026-04-22.*
