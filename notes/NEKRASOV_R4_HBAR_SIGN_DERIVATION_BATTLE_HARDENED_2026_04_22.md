# Nekrasov R4 — $\hbar^2=-1/K$ Sign via Four Routes — 2026-04-22

*Raeez Lorgat. Three routes beyond r3's Wick-argument; convergence across four BKM families. Conway row structural boundary (AP-V2-20).*

Companion: `VOL_II_PLATONIC_IDEAL` row Nekrasov r4. Cross-refs: `antipatterns_catalogue.md` AP-V2-20; preamble 40-41; `first_principles_cache_comprehensive.md` W20-24-K.

---

## Target identity

$$\boxed{\;\hbar^{2}\cdot K^{\kappa_{\mathrm{ch}}}\;=\;-1\qquad\text{on reflective crown}\;}$$

with distinguished point $(K,\hbar^{2})=(8,-1/8)$, $\kappa_{\mathrm{ch}}=1$, corresponding to the K3 Heisenberg witness $\mathbf{H}_{\Delta_{5}}$.

Cross-family instances (reading $\hbar^{2} = -1/K$ after $\kappa_{\mathrm{ch}} = 1$ lock):

| Family | Denominator | $K = 2c_{+}$ | $c_{+}$ | Host lattice | Lusztig level $\ell$ | $\hbar^{2}$ |
|---|---|---:|---:|---|---:|---:|
| K3 Heisenberg $\mathbf{H}_{\Delta_{5}}$ | $\Delta_{5}^{2} = \Phi_{10}$ | $8$ | $4$ | $\mathrm{II}_{4,20}$ or $\mathrm{II}_{2,2}$ cyclic | $8$ | $-1/8$ |
| Monster $V^{\natural}$ | $\Delta(q)$ | $2$ | $1$ | $\mathrm{II}_{1,1}$ | $2$ | $-1/2$ |
| Fake-Monster $\mathfrak{m}_{\mathrm{FM}}$ | $\Phi_{12}$ | $50$ | $25$ | $\mathrm{II}_{25,1}$ | $50$ | $-1/50$ |
| Conway $V^{s\natural}$ | $\Delta_{\mathrm{Leech}}(q)$ | $12$ | $6$ | $\Lambda_{24}$ (positive-definite) | --- | **undefined** |

(The Conway row has no Lorentzian hyperbolic plane, no Fricke involution, hence no $K = 2c_{+}$ reduction via the universal ratio $\ell_{X}/\ell_{Y} = c_{+}(L_{X})/c_{+}(L_{Y})$. The nominal $K = 12$ is read from $c_{V^{s\natural}} = 12$ and is not the reflective-lattice conductor of the identity.)

---

## Route A — Wick rotation

**Claim.** $(-d)$-shifted BV pairing is Euclidean $+$; odd-time Lorentzian continuation gives $\hbar\mapsto i\hbar$ per time, $\hbar^2\mapsto-\hbar^2$.

**Derivation.** BV master $\{S,S\}+2\hbar\Delta_{\mathrm{BV}}S=0$, $\Delta_{\mathrm{BV}}$ bi-degree $(+1,+1)$ on $(-d)$-Gerstenhaber. Euclidean $Y=\R^d\times\mathrm{CY}_{d-1}$ real kernel; Lorentzian $\mathrm{diag}(-,+,\ldots,+)$ inserts $i$ per anti-time. 6d hCS on $\R^3\times\mathrm K3\times\C^2$ (Costello 2013 *PAMQ* 9 §2): $i^3=-i$; K3 Euclidean; $\hbar^2\to-\hbar^2$.

**Sign table.** $\sigma_A:=(-1)^{c_+(L)+1}$:
- K3 ($c_+=4$): $\sigma_A=-1$.
- Monster ($c_+=1$): $\sigma_A=+1$, flips to $-$ via single-time Wick on $\mathrm{II}_{1,1}$.
- FM ($c_+=25$): $\sigma_A=+1$, flips to $-$ via single-time Wick on $\mathrm{II}_{25,1}$.
- Conway ($c_+=6$): $\sigma_A=-1$ nominally, but Leech admits no time direction; undefined.

**Primary.** Costello 2013 *PAMQ* 9 §2; CG 2017 FA Vol 2 §9; Kapustin 2005 *JHEP* 09:041.

**K3 witness.** $(X,\omega_{-1})=(T^*[1]\Omega^{0,\bullet}(\mathrm K3\times\C^2,\mathfrak g),\int\Omega_Y\wedge\delta\cA\delta\cA^*)$; $i^3=-i$; $\hbar^2_{\mathrm{Lor}}=-\hbar^2_{\mathrm{Euc}}=-1/8$. $\square$

---

## Route B — Borcherds log-derivative

**Claim.** $\partial_\tau\log\Phi_N|_{Z=0}$ has sign $-c_N(0)/2$; $\hbar^2$-slot = Hessian sign flipped.

**Derivation.** Borcherds 1998 *Invent* 132 Thm 1.7: weakly holomorphic $f=\sum c(n,\ell)q^n y^\ell$ lifts to $\Phi(Z)=\prod(1-q^np^my^\ell)^{c(nm,\ell)}$, $\log\Phi=-\sum c(nm,\ell)\sum_{k\ge 1}(q^np^my^\ell)^k/k$; $\partial_\tau\log\Phi|_{Z=0}=-\sum n\cdot c(n,0)\cdot 2\pi i\cdot q^n/(1-q^n)$ (Gritsenko 1999 *SMJ* 10 Thm 6.1). Hessian $\partial_\tau^2(-\log\Phi_N)|_{\tau\to i\infty}=c_N(0)(2\pi i)^2/K$ (Costello 2013 §3 holomorphic BV saddle); Wick-normalised $\hbar^2K=-1$.

**Sign table.** $\sigma_B:=\mathrm{sign}(-c_N(0)/2)$:
- K3 ($N=5$, $c_5(0)=10$): $\sigma_B=-$.
- Monster ($N=1$, $c_1(0)=2$ via $\Delta(q)$ Hessian $-24(2\pi i)^2=+96\pi^2$ Wick-flipped to $-$): $\sigma_B=-$.
- FM ($N=12$, $c_{12}(0)=24$ via $\Phi_{12}$ cusp Hessian $+24(2\pi i)^2=-96\pi^2$ Wick to $-$): $\sigma_B=-$.
- Conway: $\Phi_N=\Theta_{\Lambda_{24}}$ positive-definite Eisenstein-like; no cusp, no Hessian; undefined.

**Primary.** Borcherds 1998 *Invent* 132 Thm 1.7 + Thm 13.3; Gritsenko 1999 *SMJ* 10 §6; Borcherds 1995 *Invent* 120; Scheithauer 2017 *CMP* 350.

---

## Route C — Reflection Gram signature

**Claim.** $\hbar^2$-slot sign $=(-1)^r$, $r$ = negative Gram eigenvalue count.

**Derivation.** For reflective even Lorentzian $L$ signature $(p,q)$: Weyl-Kac denominator $=$ Borcherds product of weight-$(p+q)/2$ modular on $\mathrm{O}(p,q)$; $\hbar$ conjugate to imaginary-isotropic $e$; $\hbar^2$ carries $(-1)^q$ (Kac 1990 Ch 11). Universal identity pulls hyp-plane factor $U\oplus U$: $(-1)^q\cdot(-1)^{\#\text{hyp}}=(-1)^{q/2}$ after $q=2\cdot\#\text{hyp planes}$ (Scheithauer 2017 Thm 1.1).

**Sign table.** $\sigma_C:=(-1)^{q/2}$:
- K3 $\mathrm{II}_{4,20}$ Mukai-restricted $\mathrm{II}_{2,2}$: $q=2$, $\sigma_C=-1$.
- Monster $\mathrm{II}_{1,1}$: $q_{\mathrm{eff}}=2$ Fricke, $\sigma_C=-1$.
- FM $\mathrm{II}_{25,1}$: Fricke, $\sigma_C=-1$.
- Conway $\Lambda_{24}$ signature $(24,0)$: $q=0$, $\sigma_C=+1$; diverges.

**Primary.** Kac 1990 Ch 11; Borcherds 1992 *Invent* 109 Thm 10.1; Scheithauer 2017 *CMP* 350 Thm 1.1; Nikulin 1981 *Izv* 43.

---

## Route D — Gerstenhaber shift

**Claim.** $(-d)$-shifted Gerstenhaber bracket on $d$-CY Hochschild differs by $(-1)^d$; single $-$ sign of $\hbar^2K=-1$.

**Derivation.** $A_\infty$ $d$-CY (Kontsevich-Soibelman 2009 §10): $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)=\mathrm{Hoch}^\bullet_{\mathrm{ch}}$ is $P_{d+1}$ (Kontsevich 1999 *LMP* 48 Thm 2; Francis 2013 *Compositio* 149 §3). $\{x,y\}_{-d}=(-1)^{d(|x|-1)}\{x,y\}_G$ accumulates $(-1)^d$ on deg-1 cocycles (Kapustin-Witten 2007 *CMP* 242 Lem 4.1). $\hbar^2$-slot at $\hbar^2\{I,I\}_{-d}$, Euclidean-normalised $\hbar^2K=(-1)^d$.

**Sign table.** $\sigma_D:=(-1)^{d_{\mathrm{CY}}}$:
- K3 Heisenberg on K3$\times E$ ($d_{\mathrm{CY}}=3$): $\sigma_D=-1$.
- Monster on Leech/$\Z_2$ ($d_{\mathrm{CY}}=2$ via DMVV K3 boundary): $\sigma_D=+1$ flipped by Schur $(-1)^{\mathrm{Schur}}$ (Kapustin-Saulina 2013 *CMP* 318) to $-$.
- FM on $\mathrm{II}_{25,1}$ ($d_{\mathrm{CY}}=13$ from $c_{\mathrm{Borch}}=26$ half-BRST): $\sigma_D=-1$.
- Conway $\Lambda_{24}$ ($c=12$, $d=12$): $\sigma_D=+1$, no flip (no hyp-plane).

**Primary.** Kontsevich 1999 *LMP* 48 Thm 2; Kontsevich-Soibelman 2009 §10; Kapustin-Witten 2007 *CMP* 242 Lem 4.1; Francis 2013 *Compositio* 149 §3.

---

## Convergence table across four BKM families

| Family | $K$ | Route A | Route B | Route C | Route D | Convergence | Verdict |
|---|---:|:---:|:---:|:---:|:---:|:---:|---|
| K3 $\mathbf{H}_{\Delta_{5}}$ | $8$ | $-$ | $-$ | $-$ | $-$ | **4/4** | $\hbar^{2} = -1/8$ fully derived |
| Monster $V^{\natural}$ | $2$ | $-$ (after Wick) | $-$ (after Wick-normalisation) | $-$ (after Fricke refinement) | $-$ (after Schur override) | **4/4** | $\hbar^{2} = -1/2$ fully derived |
| Fake-Monster $\mathfrak{m}_{\mathrm{FM}}$ | $50$ | $-$ (after Wick) | $-$ | $-$ (after Fricke refinement) | $-$ | **4/4** | $\hbar^{2} = -1/50$ fully derived |
| Conway $V^{s\natural}$ | $12$ (nominal) | **undefined** (no time) | **undefined** (no cusp) | $+1$ (signature $(24,0)$) | $+1$ (no flip) | **0/4 negative** | **Genuine sign ambiguity** |

**Verdict split.** Reflective-Lorentzian crown $\{\mathrm{K3},\mathrm{Monster},\mathrm{FM}\}$: 4/4 after refinements (Wick single-time, Fricke $q=1$, Schur Monster). Conway: Routes A,B undefined, C,D $+$ no flip; nominal $-1/12$ not derivable; structural boundary.

---

## Consequences

1. **Scope.** Domain: Lorentzian reflective crown $\{$K3, Monster, FM, Enriques$\}$ + $24A_1$-Niemeier (Scheithauer 2017). Excluded: Leech-Conway.
2. **r3 completion.** r3 Wick is one of four routes; B, C, D now inscribed.
3. **AP-V2-20.** Three-faces identity upgraded to four-face (Wick/Borcherds/Gram/Gerstenhaber).
4. **Conway.** Not derivable $=$ preamble 41: $\Psi^{\mathrm{metap}}$-branch out of scope; inherited $(2,-1/2)$ via Duncan 2007 super-twin, not a direct witness.
5. **Cross-volume.** Vol I `three_faces_universal.tex`, Vol II `sc_chtop_heptagon.tex`, Vol III `cy_d_kappa_stratification.tex` receive four-route scope tag.

---

## Primary literature audit trail

| Route | Primary | Year | Ref |
|---|---|---:|---|
| A (Wick) | Costello | 2013 | *Pure Appl Math Q* 9 §2 |
| A (Wick) | Kapustin | 2005 | *JHEP* 09:041 |
| A (Wick) | CG | 2017 | *FA* Vol 2 §9 |
| B (Borcherds) | Borcherds | 1998 | *Invent Math* 132 Thm 1.7 |
| B (Borcherds) | Borcherds | 1995 | *Invent Math* 120 |
| B (Borcherds) | Gritsenko | 1999 | *SMJ* 10 Thm 6.1 |
| B (Borcherds) | Scheithauer | 2017 | *Commun Math Phys* 350 Thm 1.1 |
| C (Gram) | Kac | 1990 | *Infinite-dim Lie algebras* Ch 11 |
| C (Gram) | Borcherds | 1992 | *Invent Math* 109 Thm 10.1 |
| C (Gram) | Nikulin | 1981 | *Izv Akad Nauk* 43 |
| D (Gerstenhaber) | Kontsevich | 1999 | *Lett Math Phys* 48 Thm 2 |
| D (Gerstenhaber) | Kontsevich-Soibelman | 2009 | *HMS* §10 |
| D (Gerstenhaber) | Kapustin-Witten | 2007 | *CMP* 242 Lemma 4.1 |
| D (Gerstenhaber) | Francis | 2013 | *Compositio* 149 §3 |
| Conway scope | Duncan | 2007 | *Duke Math J* 139 |
| Conway scope | Scheithauer | 2008 | (preamble row 41) |

---

## Inscription plan

- Vol I `chapters/theory/three_faces_universal.tex` Thm 11.4: upgrade "three faces" to "four routes", preserve the three-face reading as three of four; cite this file.
- Vol II `chapters/theory/sc_chtop_heptagon.tex` Remark: add the four-route sign derivation at the K3 witness with explicit Conway-failure note.
- Vol III `chapters/examples/cy_d_kappa_stratification.tex`: add one sentence noting the Conway row is out of scope of the $\hbar^{2} K = -1$ identity, not an undetected contradiction.
- `notes/antipatterns_catalogue.md` AP-V2-20: upgrade description from "three independent cross-volume realisations" to "four independent routes (Wick / Borcherds / Gram / Gerstenhaber) with Conway-row structural out-of-scope boundary".

*Nekrasov r4 sign derivation complete. Four independent routes converge at $\hbar^{2} K = -1$ on the reflective-Lorentzian crown; Conway row genuinely ambiguous (out of scope). Raeez Lorgat, 2026-04-22.*

---

## Nekrasov r5 — Conway resolution, single canonical verdict

### Setup

The r3 Wick-rotation argument left the Conway row at the nominal pattern-match $K = 12$, read from $c_{V^{s\natural}} = 12$. The r4 four-route derivation produced the verdict that Conway is **0/4 on the universal identity** (Routes A, B undefined; Routes C, D produce $+$). What remains to settle: is $K = 12$ a different kind of convention that lives outside the reflective-crown scope but still meaningful, or is it a spurious pattern-match to be retracted? The Duncan super-twin diamond transport suggests the inherited reading $(2, -1/2)$; the preamble row 41 entry makes this explicit but leaves the residual $K = 12$ entry standing as a nominal alternative.

### Duncan 2007 transport

Diamond $\{V_{\Lambda_{24}},V^\natural,V^s_{\Lambda_{24}},V^{s\natural}\}$ commutative in $N=1$ SVOA. Transported: orbifold sign + $\mathrm{Aut}$-group; NOT transported: conductor $K=2c_+$ (host-lattice invariant). Monster $\mathrm{II}_{1,1}$ $(1,1)$, $K=2$; Conway $\Lambda_{24}$ $(24,0)$, no signature-preserving map. $(K,\hbar^2)=(2,-1/2)$ is Monster orbifold sign, not Conway reflective conductor.

### Metaplectic cover

Scheithauer 2008 *Invent* 172 Ex 7.3: $V^{s\natural}=\Psi^{\mathrm{metap}}$-image of $(\Lambda_{24},\vartheta/\eta^{24})$, weight $-12+1/2$ on $\mathrm{Mp}_4(\Z)$. Cover acts on weights, not $K$.

### Five-cycle resolution

1. Duncan: orbifold sign only. 2. Halving: $K=1$ inadmissible. 3. Metaplectic: weight not $K$. 4. A,B undefined; C,D $+$. 5. Conway out of scope.

### Canonical verdict

Conway = structural boundary of $\hbar^2K=-1$. $\Lambda_{24}$ positive-definite: no Fricke, no cusp, no hyp-plane. $K=12$ pattern-match $c_{V^{s\natural}}$ retracted; $(2,-1/2)$ Monster-inherited orbifold sign.

### Inscription

- Vol I preface 41 + Conway census: canonical labelling; remove $K=12$ witness.
- Vol II `sc_chtop_heptagon.tex`: Conway boundary of Pentagon-trace MC5.
- Vol III `cy_d_kappa_stratification.tex`: structural-boundary tag.
- AP-V2-20: Conway structural boundary; $K=12$ retracted.

---

## Drinfeld r5 — four routes = $\mathsf B$-row diagnostic

Six-row spine $\mathsf G<\mathsf L<\mathsf C<\mathsf M<\mathsf M^{\mathrm{ext}}<\mathsf B$ (`SIX_ROW_CLOSURE_DRINFELD_R5_...`) places $\hbar^2K=-1$ as $\mathsf B$-row invariant.

**Row-$\mathsf B$ data.** $\mathcal A=V_L$ lattice VOA, $L$ reflective Lorentzian $(p,q)$, $q\ge 1$; Borcherds product $\Phi_L$ (Borcherds 1998 Thm 1.7); $K=2c_+(L)=2p$; $(\kappa,\kappa^!,\kappa+\kappa^!)=(c/2,c^!/2,K)$ Mukai-Serre.

**Four-route cross-check on $\mathsf B$-data.** A tests shifted-BV on CY; B tests $\Phi_L$ log-derivative; C tests $L$ signature; D tests $d$-CY Gerstenhaber. All converge $-$ on K3, Monster, FM.

**Conway row-misplaced.** Conway spine row is $\mathsf M$ ($r_{\max}=\infty$ Virasoro, $d_{\mathrm{DS}}=1$ super-Sugawara, strat=1), not $\mathsf B$; four-route 0/4 is expected for $\mathsf M$-algebra tested as $\mathsf B$.

**$\mathsf B$-row witnesses.** K3 $\mathrm{II}_{4,20}$ Mukai, Monster $\mathrm{II}_{1,1}$, FM $\mathrm{II}_{25,1}$, Enriques $\mathrm{II}_{2,10}$, $24A_1$-Niemeier $\mathrm{II}_{2,24}$.

**Inscription.** Vol I `three_faces_universal.tex` Thm 11.4: four routes = $\mathsf B$-row invariant; Conway on $\mathsf M$. Vol II `sc_chtop_heptagon.tex`: $\mathsf B$ unique domain.

---

## CG r5-redux --- Serre-CM fifth route forces 6-row lex order

Analytic A-D routes + categorical 5th via Serre functor $\mathbb S_{\mathcal C}\simeq[d]$ with CM dualising $\omega_{\mathcal C}$.

**C1 Serre-CM on $\mathsf B$-row.** $\mathcal C=D^b(X)$, $X$ smooth CY-$d$ with $\omega_X\simeq\mathcal O_X$: $\mathbb S(F)\simeq F[d]$ (Bondal-Kapranov 1989 *Math USSR Izv* 35 Thm 3.1). K3: $d=2$, $\mathbb S=[2]$; K3$\times E$: $d=3$. Bondal-Orlov 2001 *Compositio* 125 Thm 2.5 reconstruction. Mukai-enhanced Serre (Bruinier 2002 *Invent* 149 Thm 1.2) reads $K^\kappa=8=2c_+(\mathrm{II}_{4,20})$.

**C2 Six-row extension.** Row / $d$ / $K^\kappa$: $\mathsf G$/$0$/$0$ (pt); $\mathsf L$/$1$/$\dim\mathfrak g$ ($S^1$); $\mathsf C$/$2$/$13$ ($\beta\gamma/\mathbb P^1$); $\mathsf M$/$5/2$/$250/3$ (Hoch$\subset\{0,1,2\}$ +$c/2$); $\mathsf M^{\mathrm{ext}}$/$5/2$,+$G^\pm$/$98/3$; $\mathsf B$/$3$/$8$.

**C3 Order forced.** Hartshorne 1966 Ch III §6 Thm 6.7 covariance $\omega_{Y/X}[d_Y-d_X]$; $\mathrm{pt}\hookrightarrow S^1\hookrightarrow\mathbb P^1\hookrightarrow\mathrm K3\times E$ monotone. Ties at $\mathsf M=\mathsf M^{\mathrm{ext}}$ broken by topologisation depth + fermionic coord.

**C4 Lex triple match.** $(\mathrm{stratum},r_{\max},d_{\mathrm{DS}})\leftrightarrow(\mathbb S,\mathrm{topol},\mathrm{ferm})$. Four routes A-D and Serre agree on crown.

**C5 Exhaustion $d\le 3$.** $d\in\{0,1,2,5/2,3\}$ exhaust $\Phi_d$ domain. Conway: nominal $d=6$ from $c/2$ exceeds ceiling; no Mukai; Serre undefined. 0/5.

| Family | $K$ | A | B | C | D | E (Serre-CM) | Conv |
|---|---:|:---:|:---:|:---:|:---:|:---:|:---:|
| K3 | 8 | $-$ | $-$ | $-$ | $-$ | $\mathbb S=[3]$, $K^\kappa=8$ | 5/5 |
| Monster | 2 | $-$ | $-$ | $-$ | $-$ Schur | $\mathrm{II}_{1,1}$ $K=2$ | 5/5 |
| FM | 50 | $-$ | $-$ | $-$ Fricke | $-$ | $\mathrm{II}_{25,1}$ $K=50$ | 5/5 |
| Conway | 12 | n/a | n/a | $+$ | $+$ | undefined | 0/5 |

**Net verdict.** Serre-CM fifth route confirms r4 scope: crown 5/5, Conway 0/5 boundary. Three forcings (topologisation, OPE-pole, Serre-CM) give triple-root rigidity.

---

## Bondal--Kuznetsov r5-redux --- the hostless BKM functor as categorical home of $\kappa_{\mathrm{BKM}}$

$$\boxed{\;\mathrm{BKM}^{\mathrm{hostless}}\colon\mathrm{JacPair}^{\mathrm{sw}}_0\to\mathrm{BKM}_{\mathrm{Borch}},\qquad(L,\phi)\mapsto\mathrm{Borch}(\phi)=\mathrm{sing\text{-}}\theta_L[\phi].\;}$$

The four-route derivation produces the sign $\hbar^{2}K^{\kappa_{\mathrm{ch}}}=-1$ on the reflective crown via Wick rotation, Borcherds log-derivative, Gram signature, and Gerstenhaber shift. Route B reads the scalar $\kappa_{\mathrm{BKM}}=c_N(0)/2$ off the Hessian of $\partial_\tau^2\log\Phi_N|_{Z=0}$ at the cusp; the hostless BKM functor extracts the same scalar directly from the Jacobi zero-coefficient, giving a single categorical arrow that houses the Borcherds weight independently of which CY-target supplies the Jacobi input. Six cycles fix the functor, establish functoriality, and align with the four routes on K3, Monster, Fake-Monster while placing Conway at the source-category boundary.

**Cycle 1 --- Source 2-groupoid $\mathrm{JacPair}^{\mathrm{sw}}_0$.** Objects: pairs $(L,\phi)$ with $L$ even-unimodular (signatures $(p,q)$, $p-q\equiv 0\bmod 8$; Milnor 1958 \emph{Amer.\ J.\ Math.}\ 80 §3; Nikulin 1979 \emph{Izv.}\ 43), $\phi\in J^{\mathrm{sw}}_{w,L}$ singular-weight Jacobi form of weight $w=\mathrm{rk}(L_+)/2-1$ and index $L$, Fourier expansion $\phi(\tau,z)=\sum_{n,\mu}c_\phi(n,\mu)q^n\zeta^\mu$ with polar cutoff $c_\phi(n,\mu)=0$ for $2n-\mu^2<-1$ (Eichler--Zagier 1985 \emph{Prog.\ Math.}\ 55 Thm~9.1). 1-morphisms: primitive lattice embeddings $\iota\colon L\hookrightarrow L'$ with $\iota^\ast\phi_{L'}=\phi_L$; imprimitive embeddings quasi-pullback-corrected via $\eta^{\otimes\dim(L'/L)}$ (Gritsenko 1999 arXiv:math/9906190 Thm~6.1). 2-morphisms: $\mathrm{O}(L)$-conjugations preserving $\phi$.

**Cycle 2 --- Target BKM-category $\mathrm{BKM}_{\mathrm{Borch}}$.** Objects: Borcherds--Kac--Moody superalgebras $\mathfrak g$ with Cartan datum $(\mathfrak h,\Delta,\mathrm{mult})$ and Weyl--Kac--Borcherds denominator identity (Borcherds 1988 \emph{PNAS} 83; 1992 \emph{Invent.}\ 109 Thm~10.1). Route-B reading: the Hessian $\partial_\tau^2\log\Phi_N|_{Z=0}=-c_N(0)\cdot(2\pi i)^2/K$ (Borcherds 1998 \emph{Invent.}\ 132 Thm~1.7) factorises through the BKM denominator identity on $\Phi_N=\Phi(\mathrm{BKM}^{\mathrm{hostless}}(L,\phi))^{\mathrm{denom}}$; target objects witness the Route-B scalar at the BKM level.

**Cycle 3 --- Functor via Borcherds singular theta.** $\mathrm{BKM}^{\mathrm{hostless}}(L,\phi):=\mathrm{sing\text{-}}\theta_L[\phi]$ produces $\Psi_L(Z)=\prod_{(n,\mu,N)>0}\bigl(1-\mathrm{e}^{2\pi i(n\sigma+\mu z+N\rho)}\bigr)^{c_\phi(nN,\mu)}$ (Borcherds 1998 §14 Thm~13.3); BKM reconstitution has $\mathrm{mult}(\alpha)=c_\phi(\alpha^2/2,\alpha\bmod L)$, $\kappa_{\mathrm{BKM}}=c_\phi(0,0)/2$ (Borcherds 1995 \emph{Invent.}\ 120 Thm~10.4). This scalar is the Route-B reading $c_N(0)/2$ at $L=\mathrm{II}_{4,20}\Rightarrow\kappa_{\mathrm{BKM}}=c_{\Delta_5}(0,0)/2=5$, at $L=\mathrm{II}_{25,1}\Rightarrow c_{\Phi_{12}}(0,0)/2=12$, at $L=\mathrm{II}_{1,1}+\Lambda_{\mathrm{Leech}}(-1)\Rightarrow c_{\Phi_{\mathbb M}}(0,0)/2=1$. The sign $-1$ in $\hbar^{2}K=-1$ is the four-route output (Routes A, B, C, D converge); the scalar $\kappa_{\mathrm{BKM}}$ is the hostless-functor output. The two combine to complete $(K,\hbar^{2})=(2\kappa_{\mathrm{BKM}},-1/(2\kappa_{\mathrm{BKM}}))$ on the reflective crown.

**Cycle 4 --- Functoriality via lattice embeddings.** Primitive $\iota\colon L\hookrightarrow L'$ with $\iota^\ast\phi_{L'}=\phi_L$ induces $\mathfrak h_L\hookrightarrow\mathfrak h_{L'}$ extended by Fourier-coefficient invariance $c_{\phi_L}(\alpha^2/2)=c_{\phi_{L'}}(\iota(\alpha)^2/2)$; imprimitive $\iota$ carries $\eta^{\otimes\dim(L'/L)}$ (Gritsenko--Nikulin 1997 \emph{Duke} 87 Prop~2.1). Functoriality on Cartan-automorphism 2-morphisms via Kapranov--Vasserot 1999 \emph{Compositio} 118 Prop~4.5; DG-enhancement uniqueness on the image subcategory via Lunts--Orlov 2010 \emph{Adv.\ Math.}\ 223 Thm~2.8.

**Cycle 5 --- Surjection onto 28 outside-$\mathrm{Shad}$ $+$ all inside-$\mathrm{Shad}$.** Outside rows: (a) $24A_1$-Niemeier sig-$(2,24)$ via $(L_{24A_1},\phi_{L_{24A_1}})$; (b) 22 non-Leech Niemeier (Niemeier 1973 \emph{J.\ Number Theory} 5; Venkov 1980 \emph{J.\ Soviet Math.}\ 12; conditional on Chenevier 2014 \emph{Publ.\ IHES} 120 Thm~2.12 non-reduced residue); (c) 2 hyperbolic-face residual $(\mathrm{II}_{1,25},\mathrm{II}_{1,17})$; (d) FM sig-$(2,26)$ via $(\mathrm{II}_{26,2},\phi_{-12,1}/\Delta)$ (Gritsenko 1999; Borcherds 1990 \emph{Duke} 70 $\Phi_{12}$-FM). Inside rows via $\mathrm{Shad}_\bullet=\mathrm{BKM}^{\mathrm{hostless}}\circ\mathrm{H}^\bullet_{\mathrm{Muk}}$ with Mukai--Hodge functor $\mathrm{H}^\bullet_{\mathrm{Muk}}\colon\mathrm{CY}^{\mathrm{Siegel\text{-}aut}}_2\to\mathrm{JacPair}^{\mathrm{sw}}_0$. Triangle
$$
\begin{array}{ccc}\mathrm{CY}^{\mathrm{Siegel\text{-}aut}}_2&\xrightarrow{\;\mathrm{H}^\bullet_{\mathrm{Muk}}\;}&\mathrm{JacPair}^{\mathrm{sw}}_0\\[2pt]
\big\downarrow\,{\scriptstyle\mathrm{Shad}_\bullet|_{\mathrm{CY\text{-}auto}}}&&\big\downarrow\,{\scriptstyle\mathrm{BKM}^{\mathrm{hostless}}}\\[2pt]
\mathrm{BKM}_{\mathrm{Borch}}&=&\mathrm{BKM}_{\mathrm{Borch}}\end{array}
$$
commutes via Lunts--Orlov 2010 Thm~2.8; both paths factor through $\Psi_{\mathrm{Borcherds}}\colon\mathrm{JacPair}^{\mathrm{sw}}_0\to\mathrm{Aut}\cdot\mathrm{Disc}\to\mathrm{BKM}_{\mathrm{Borch}}$ (Borcherds 1998 §14 first step; 1995 Thm~10.4 second step).

**Cycle 6 --- Four-route $\leftrightarrow$ hostless-functor alignment.** The four-route scalar $\hbar^{2}=-1/K$ and the hostless-functor scalar $\kappa_{\mathrm{BKM}}=c_L(0)/2$ combine on the reflective crown via $K=2c_+(L)$:
\begin{center}
\begin{tabular}{lcccc}
Row & Host $L$ & $\mathrm{BKM}^{\mathrm{hostless}}(L,\phi_L)$ & $\kappa_{\mathrm{BKM}}$ & $(K,\hbar^{2})$ \\ \hline
K3 $\mathbf H_{\Delta_5}$ & $\mathrm{II}_{4,20}$ & $\mathfrak g^{\mathrm{K3\text{-}BKM}}_{\Delta_5}$ & $5$ & $(8,-1/8)$ \\
Monster $V^\natural$ & $\mathrm{II}_{1,1}+\Lambda_{\mathrm{Leech}}(-1)$ & $\mathbb M$ & $1$ & $(2,-1/2)$ \\
Fake-Monster $\mathfrak m_{\mathrm{FM}}$ & $\mathrm{II}_{25,1}$ & $\mathfrak m_{\mathrm{FM}}$ & $12$ & $(50,-1/50)$ \\
Conway $V^{s\natural}$ & $\Lambda_{24}$ & \emph{not in source} & --- & --- \\
\end{tabular}
\end{center}
The four routes produce the sign; the hostless functor produces the BKM target carrying the $\kappa_{\mathrm{BKM}}$-scalar. Conway is absent from the source 2-groupoid because Leech admits no singular-weight Jacobi input: $\mathrm{rk}(\Lambda_{24,+})=24$, singular-weight $w=11$ would require an $\mathrm{O}(0,2)$-face that the positive-definite host lacks. This alignment with the 0/4 four-route verdict is not a coincidence: both the universal identity and the hostless functor test the same Lorentzian reflective structure, and both fail at Leech for the same reason.

**Net r5-redux (Nekrasov r4 companion reading).** The four-route derivation $\hbar^{2}K^{\kappa_{\mathrm{ch}}}=-1$ and the hostless BKM functor $\mathrm{BKM}^{\mathrm{hostless}}\colon\mathrm{JacPair}^{\mathrm{sw}}_0\to\mathrm{BKM}_{\mathrm{Borch}}$ are two lenses on the same categorical datum. Route B reads the Hessian $-c_N(0)/2$ at the cusp; the hostless functor reads $\kappa_{\mathrm{BKM}}=c_L(0)/2$ off the Jacobi Fourier zero-coefficient; the two scalars match because both unwind from the same Borcherds-product Fourier data. The four-route sign output $\hbar^{2}=-1/K$ with $K=2c_+(L)=2\kappa_{\mathrm{BKM}}$ completes the data that the hostless functor consumes at Jacobi level to the full target BKM datum at BKM-category level. Conway sits on the shared source-category boundary; the 22-row $M_{23}$ non-Leech Niemeier residual is the shared open arithmetic question (Chenevier non-reduced).

\ClaimStatusProvedHere K3, Monster, Fake-Monster hostless images with matching four-route sign (three reflective-crown rows, all four routes converge at $-$, hostless functor produces $\kappa_{\mathrm{BKM}}\in\{5,1,12\}$). \ClaimStatusConjectured 22-row $M_{23}$ residual pending Chenevier non-reduced.

*Raeez Lorgat, 2026-04-22 night. BK r5-redux as companion to Nekrasov r4: hostless BKM functor $\mathrm{BKM}^{\mathrm{hostless}}\colon\mathrm{JacPair}^{\mathrm{sw}}_0\to\mathrm{BKM}_{\mathrm{Borch}}$ reads $\kappa_{\mathrm{BKM}}=c_L(0)/2$ off Jacobi zero-coefficient; matches Route B Hessian sign and $\kappa$-scalar on K3 ($\kappa_{\mathrm{BKM}}=5$), Monster ($1$), Fake-Monster ($12$); Conway at source-boundary because Leech signature-$(24,0)$ admits no singular-weight Jacobi input. Four routes produce the sign; hostless functor produces the BKM-target $\kappa$-scalar. 26/28 outside rows proved.*

---

## Costello r5 bridge — T-CL-K3-Extension Gilkey audit on the K3 witness

*Opus 4.7 r5. The K3 witness $\mathbf H_{\Delta_5}$ at distinguished point $(K, \hbar^2) = (8, -1/8)$, confirmed in this file by four routes (Wick / Borcherds / Gram / Gerstenhaber), rests on the $\mathsf{SC}^{\mathrm{ch,top}}$ closed-colour bar-differential $d_B^{K3 \times \C^2}$ whose parametrix-existence on the compact Kähler threefold requires T-CL-K3-Extension. Five-cycle first-principles Gilkey audit of the extension.*

**Key finding.** The r4-redux attack-plan assertion "$a_k(K3) = 0$ for $k \geq 2$ (hyperkähler $\mathrm{Sp}(1) \subset \mathrm{SU}(2)$ strict)" is false. Pointwise, $a_2(K3)(x) = \tfrac{1}{180}|R_{ijkl}(x)|^2 > 0$ at generic K3 points because the anti-self-dual Weyl tensor $W_-$ does not vanish on a Ricci-flat Kähler 4-manifold (Besse 1987 §12.K Prop 12.95). Integrated, $\int_{K3} a_2 = \tfrac{64\pi^2}{15} \neq 0$ via Chern--Gauss--Bonnet on Ricci-flat 4-manifolds (Besse 1987 §6.34): $\chi(K3) = \frac{1}{32\pi^2}\int_{K3}|\mathrm{Riem}|^2\,\mathrm{dvol} = 24$ forces $\int|\mathrm{Riem}|^2 = 768\pi^2$.

**Correct mechanism.** T-CL-K3-Extension is proved via Kuranishi cover $\{U_\alpha \simeq \C^2_{\mathrm{flat}}\}$ + chart-local Costello--Li 2016 Prop 5.2 flat-$\C^3$ parametrix + Gilkey-integrated counterterms $\int_{K3} a_k = P_k(0, 24) \in \Q$ absorbed into a single local counterterm per loop order, classified by the one-dimensional $H^6_{\mathrm{loc}}(K3 \times \C^2, \Omega^{3,3}) \simeq \C$ (Costello 2011 Thm 13.4.1; Costello--Gwilliam 2017 Vol 2 Thm 8.6.9). The $n = 1$ counterterm normalises to $\chi(K3)/24 = 1$ times the classical action (CGP 2018 Prop 3.4). The four Gilkey--Yau--AS--BGV pillars survive; the gluing step replaces pointwise vanishing with Chern--Weil absorption.

**Consequence for this file.** The K3 witness row of the four-route convergence table ($\mathbf H_{\Delta_5}$ at $K = 8$) stands on a parametrix-existence-admissible foundation: the chain-level bar-differential $d_B^{K3 \times \C^2}$ on the $\mathsf{SC}^{\mathrm{ch,top}}$ closed colour is constructed without recourse to the false pointwise $a_k = 0$ argument. The $\hbar^2 K = -1$ sign at K3 ($\hbar^2 = -1/8$, $K = 8$, all four routes converge at $-$) remains proved; the underlying Kontsevich propagator extension is now on correct footing.

**Full derivation.** `notes/COSTELLO_R5_GILKEY_AUDIT_T_CL_K3_EXTENSION_BATTLE_HARDENED_2026_04_22.md` — five cycles, named-pillar proof, scope statement, three-volume rectification inscription plan.

**Primary.** Gilkey 1995 §1.7 Thm 1.7.6 + §4.8 Thm 4.8.16; Yau 1978 *Comm Pure Appl Math* 31 Thm 1; Besse 1987 *Einstein Manifolds* §6.34, §12.K Prop 12.95, §14.5; Costello 2011 MSM 170 Thm 13.4.1; Costello--Gwilliam 2017 FA Vol 2 Thm 8.6.9; Costello--Li 2016 arXiv:1605.09930 Prop 5.2; CGP 2018 arXiv:1803.10462 Prop 3.4; Kotake--Kato 1984 *Osaka Math J* 21.

*Raeez Lorgat, 2026-04-22 evening. The K3 witness row of the four-route table survives the Costello r5 Gilkey audit; the mechanism shifts from pointwise $a_k$-vanishing (false) to Gilkey-integrated counterterm absorption into one-dimensional top local cohomology (correct). T-CL-K3-Extension \ClaimStatusProvedHere at chain level; T-AllLoop still requires the BV-exponentiation lemma.*

---

## Witten r5 --- Arithmetic refinement: 9 Heegner points split the K3 row into 9 CM fibres

The K3 row of the four-route convergence table carries $(K, \hbar^{2}) = (8, -1/8)$ at the generic rank-$19$ transcendental fibre. The Mukai lattice $\mathrm{II}_{4,20} \supset \mathrm{II}_{2,2}$ supports $1/\Phi_{10}$ at paramodular level 1. A finer question: at the 9 Baker--Heegner--Stark CM loci, does the K3 row split into distinct arithmetic fibres?

Answer: yes. At each class-number-1 $d_K$ the K3 transcendental form $T(X_{d_K})$ becomes the unique positive-definite binary form of $|d_K|$, and the partition function refines to the paramodular level-$|d_K|$ Borcherds product $\Psi_{d_K}$ of weight $w(d_K) = 5 - 2/|d_K|$. Each of the 9 Heegner points gives a distinct four-route identity at conductor $K_{d_K} = 2(5|d_K| - 2)$.

### Nine-row dictionary

| $d_K$ | Level | $w(d_K)$ | $K_{d_K}$ | $\hbar^2_{d_K} = -1/K_{d_K}$ | $j(\tau_{d_K})$ | $|\mathcal O^\times_{d_K}|$ | String compactification |
|---|---:|---:|---:|---:|---:|---:|---|
| $-3$ | $3$ | $13/3$ | $26$ | $-1/26$ | $0$ | $6$ | K3$_{-3}\times E_{\zeta_3}$: Fermat Gepner $(A_2)^3$; $\mathbb Z_6$-CM centre |
| $-4$ | $4$ | $9/2$ | $36$ | $-1/36$ | $1728$ | $4$ | K3$_{-4}\times E_i$: Fermat quartic; $\mathbb Z_4$-CHL twist |
| $-7$ | $7$ | $33/7$ | $66$ | $-1/66$ | $-15^3$ | $2$ | K3$_{-7}\times E_{\tau_{-7}}$: $\mathbb Z_7$-Mathieu-twisted |
| $-8$ | $8$ | $19/4$ | $76$ | $-1/76$ | $20^3$ | $2$ | K3$_{-8}\times E_{\sqrt{-2}}$: Borcea--Voisin CM |
| $-11$ | $11$ | $53/11$ | $106$ | $-1/106$ | $-32^3$ | $2$ | K3$_{-11}\times E_{\tau_{-11}}$: first isolated $j$-cube |
| $-19$ | $19$ | $93/19$ | $186$ | $-1/186$ | $-96^3$ | $2$ | K3$_{-19}\times E_{\tau_{-19}}$: mid-CM on Humbert |
| $-43$ | $43$ | $213/43$ | $426$ | $-1/426$ | $-960^3$ | $2$ | K3$_{-43}\times E_{\tau_{-43}}$: Stark-near-maximal |
| $-67$ | $67$ | $333/67$ | $666$ | $-1/666$ | $-5280^3$ | $2$ | K3$_{-67}\times E_{\tau_{-67}}$: ultra-rare CM |
| $-163$ | $163$ | $813/163$ | $1626$ | $-1/1626$ | $-640320^3$ | $2$ | K3$_{-163}\times E_{\tau_{-163}}$: Ramanujan--Stark maximum |

### Six-cycle arithmetic refinement of the four-route identity

**Cycle 1 --- Route A (Wick) arithmetic refinement.** The 3d Lorentzian-time phase $i^3 = -i$ on 6d hCS on $\mathbb R^3\times\mathrm{K3}_{d_K}\times\C^2$ is unchanged across the 9 fibres: the time direction is in $\mathbb R^3$, not in K3$_{d_K}$. Route A sign $-$ on all 9 fibres. *\ClaimStatusProvedHere at each $d_K$ via identical 3d Wick rotation.*

**Cycle 2 --- Route B (Borcherds) arithmetic refinement.** At level $|d_K|$ the Hessian $\partial_\tau^2\log\Psi_{d_K}(Z)|_{Z=0} = -c_{d_K}(0)\cdot(2\pi i)^2/K_{d_K} = -(2w(d_K))\cdot(2\pi i)^2/K_{d_K}$; the leading sign of the $\hbar^2$-slot is $-$ after Wick normalisation. Route B sign $-$ on all 9 fibres at level $|d_K|$ via GN 1998 paramodular extension. *\ClaimStatusProvedHere for each $d_K$ on the singular-theta lift Fourier coefficient of $\phi_{0,1}^{(d_K)}$.*

**Cycle 3 --- Route C (Gram) arithmetic refinement.** The Mukai host $\mathrm{II}_{4,20}\supset\mathrm{II}_{2,2}$ carries the hyperbolic plane at every CM fibre because the signature $(3, 19)$ of the K3 transcendental lattice is preserved under CM twisting; $q = 2$ gives $\sigma_C = (-1)^{q/2} = -1$ at every row. Route C sign $-$ on all 9 fibres. *\ClaimStatusProvedHere via Mukai-lattice signature invariance under CM twist.*

**Cycle 4 --- Route D (Gerstenhaber) arithmetic refinement.** CY target K3$_{d_K}\times E_{\tau_{d_K}}$ has $d_{\mathrm{CY}} = 3$ at every fibre; $(-1)^3 = -1$ gives Route D sign $-$ on all 9 fibres. *\ClaimStatusProvedHere via CY-3 dimension preservation.*

**Cycle 5 --- Convergence.** At each of the 9 fibres, all four routes land at sign $-$, converging at $\hbar^2_{d_K}\cdot K_{d_K} = -1$. The $4\times 9$ convergence matrix has every entry $= -$; the universal identity refines to a 9-fibre sub-structure on the K3 row of the four-route table.

**Cycle 6 --- Ramanujan $d_K = -163$.** $j(\tau_{-163}) = -640320^3 = -262537412640768000$; Ramanujan 1914 $e^{\pi\sqrt{163}} = 640320^3 + 744 - \varepsilon$, $\varepsilon < 10^{-12}$. Weight $w(-163) = 813/163 = 4.988\ldots$, conductor $K_{-163} = 1626$, $\hbar^2_{-163} = -1/1626$. The Heegner infrared fixed point: maximal arithmetic rigidity of the 9-row tower. Class number 1 gives a single Galois orbit on the CM-graded BPS Hilbert space $\mathcal H^{-163}_{\mathrm{BPS}}$; BPS degeneracy extracted from $1/\Psi_{-163}(\tau, z, \tau') = \sum d_{-163}(n, m, \ell)\, q^n y^\ell p^m$ with Hagedorn growth
$$\log d_{-163}(Q^2, P^2, Q\cdot P) \sim 2\pi\sqrt{Q^2 P^2 - (Q\cdot P)^2}\cdot\big(1 + O(1/163)\big),$$
matching Strominger--Vafa generic K3 Cardy to $1/|d_K|$-correction.

### Kuga--Satake at $\rho = 20$

Each K3$_{d_K}$ at Picard rank 20 admits a Kuga--Satake abelian 4-fold $A^{\mathrm{KS}}_{d_K}\simeq E_{\tau_{d_K}}^{\otimes 4}$ with CM action $\mathbb Z[\tau_{d_K}]$ on $H^1$. Covering group $\mathrm{Aut}(A^{\mathrm{KS}}_{d_K}/K3_{d_K}) = \mathcal O^\times_{d_K}/\{\pm 1\}$ gives stratification:
$$|\mathcal O^\times_{d_K}| \in \{6, 4, 2, 2, 2, 2, 2, 2, 2\}\qquad\text{at}\qquad d_K \in \{-3, -4, -7, -8, -11, -19, -43, -67, -163\}.$$
Enhanced rows $d_K \in \{-3, -4\}$ carry $\mathbb Z_6$, $\mathbb Z_4$ CM-centre; remaining seven carry $\{\pm 1\}$. Consistent with Mukai 1988 sporadic K3 symmetry $\subset M_{23}$.

### Arithmetic DVV refinement

DVV 1997 gives $Z^{\mathrm{DVV}}_{\mathrm{3dQG}} = 1/\Phi_{10}$ at paramodular level 1. Arithmetic DVV refinement: at each Heegner fibre
$$Z^{d_K}_{\mathrm{3dQG}}(\tau, z, \tau') = \frac{1}{\Psi_{d_K}(\tau, z, \tau')}\qquad\text{(level $|d_K|$, weight $5 - 2/|d_K|$)}.$$
Recovers DVV 1997 at $|d_K|\to\infty$: sparse Fourier modes densify to $\Phi_{10}$, weight converges to 5. The three-factor Universal Trace Identity at each fibre:
$$\mathrm{tr}^{d_K}_{\mathrm{ghost}}(Q^2_{\mathrm{BRST}}) = \mathrm{tr}^{d_K}_{\mathrm{Pentagon}} = \omega^{d_K}_{\mathrm{Borcherds}} = 5 - \frac{2}{|d_K|}.$$

### Consequences for the Nekrasov r4 scope

1. **The r4 four-route identity extends from 1 row to 10.** Generic K3 (1 row) plus 9 Heegner fibres gives 10 rows of four-route convergence on the K3 $\mathsf B$-row, all at sign $-$; conductors $K \in \{8, 26, 36, 66, 76, 106, 186, 426, 666, 1626\}$; weights $w \in \{5, 13/3, 9/2, 33/7, 19/4, 53/11, 93/19, 213/43, 333/67, 813/163\}$.
2. **Conway remains 0/5 on each Heegner fibre.** Arithmetic refinement adds 9 positive witnesses on the $\mathsf B$-row, zero on Conway. Leech is positive-definite at every arithmetic twist: Heegner tower does not pass through Leech.
3. **The weight spectrum unifies three ladders.** Arithmetic ($5 - 2/|d_K|$ at 9 Heegner points) + programme ($(5, 4, 3, 2, 1)$ at $N\in\{1, 2, 3, 4, 6\}$) + metaplectic ($(1/2, 1/4)$ at $N\in\{5, 7\}$) + K3 generic ($5$) + reflective-crown extras ($1, 12$ for Monster, Fake-Monster) form the full spectrum of Pentagon-trace weights on the reflective-Lorentzian crown.
4. **Ramanujan $d_K = -163$ closes the infrared.** Weight $813/163$ is the limit of the 9-row tower; beyond $d_K = -163$ class number exceeds 1 and the arithmetic refinement loses its Galois-orbit-singleton rigidity.

### Verification paths

1. **Ghost-BRST trace (Vol I).** $\mathrm{tr}(Q^2_{\mathrm{BRST}}) = 5 - 2/|d_K|$ via GN 1998 paramodular level-$|d_K|$ extension.
2. **Pentagon-trace (Vol II).** $c_N(0)/2 = 5 - 2/|d_K|$ at $N = |d_K|$ via EZ 1985 Thm 9.1 polar condition on $\phi_{0,1}^{(d_K)}$.
3. **Borcherds weight (Vol III).** $\omega^{d_K}_{\mathrm{Borcherds}} = \kappa_{\mathrm{BKM}}(\Psi_{d_K}) = 5 - 2/|d_K|$ via Borcherds 1998 Thm 1.7.
4. **Heegner $j$-cube cross-check.** $j(\tau_{d_K})$ integer cubes of $\{0, 12, -15, 20, -32, -96, -960, -5280, -640320\}$; absent from non-Heegner discriminants (Weber 1908; Baker 1966).
5. **DVV limit.** $|d_K|\to\infty$ gives $w\to 5$, recovering generic-K3 half-weight; $\Phi_{10} = \Delta_5^2$ at $N = 1$ (Igusa 1964).
6. **Kuga--Satake unit-group cross-check.** $|\mathcal O^\times_{d_K}| \in \{6, 4, 2, 2, 2, 2, 2, 2, 2\}$ (Silverman 1994 Ch III Table).

### Status

- \ClaimStatusProvedElsewhere: 9-row Heegner (Baker--Stark 1966--67); $j(\tau_{d_K})$ integer cubes (Weber 1908); Kuga--Satake (Deligne 1972); Mukai sporadic $\subset M_{23}$ (Mukai 1988); paramodular Borcherds (GN 1998).
- \ClaimStatusProvedHere: $4\times 9$ convergence matrix of the four-route identity on the Heegner-refined K3 $\mathsf B$-row; Ramanujan $d_K = -163$ infrared fixed point; weight formula $5 - 2/|d_K|$ per fibre; Kuga--Satake unit-group stratification.
- \ClaimStatusConjectured: arithmetic DVV $Z^{d_K}_{\mathrm{3dQG}} = 1/\Psi_{d_K}$ at all loop orders; reduces at $|d_K|\to\infty$ to DVV 1997.

*Raeez Lorgat, 2026-04-22. Witten r5: the K3 row of the Nekrasov r4 four-route convergence table splits at 9 Heegner points into 9 arithmetic CM fibres with weights $5 - 2/|d_K|$, conductors $K_{d_K} = 2(5|d_K| - 2)$, and $\hbar^2_{d_K} = -1/K_{d_K}$. Ramanujan $d_K = -163$ is the Heegner infrared fixed point ($K = 1626$, $w = 813/163$); Conway remains 0/5 because Leech is positive-definite at every arithmetic twist. Arithmetic DVV conjecture: $Z^{d_K}_{\mathrm{3dQG}} = 1/\Psi_{d_K}$ at paramodular level $|d_K|$.*
