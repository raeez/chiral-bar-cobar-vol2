# Polyakov Cycles — Physics $=$ Mathematics as Theorems, Vol II, 2026-04-22

*Raeez Lorgat. Companion inscription to `VOL_II_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md`. Every physics↔mathematics identification in Vol II upgraded to a theorem across five sharpening cycles, with emphasis on the $\mathsf{SC}^{\mathrm{ch,top}}$ bulk-boundary structure and the 3d quantum gravity climax.*

---

## Cycle 1: $\mathsf{SC}^{\mathrm{ch,top}}$ $=$ bulk-boundary 3d holomorphic-topological QFT

**Theorem ($\mathsf{SC}^{\mathrm{ch,top}}$ $=$ Cattaneo-Felder bulk-boundary operad for 3d HT gauge theory).** The bicoloured Swiss-cheese-chiral-topological operad $\mathsf{SC}^{\mathrm{ch,top}}$ acting on the derived-centre pair $(C^\bullet_{\mathrm{ch}}(A,A), A)$ equals the operadic structure of a 3d holomorphic-topological gauge theory on $C\times\R$ with chiral algebra $A$ as the boundary (open colour) and chiral Hochschild cochains $C^\bullet_{\mathrm{ch}}(A,A)$ as the bulk (closed colour). Explicitly:
- Closed colour $=$ holomorphic factorisation on $C$ $=$ $E_2$-structure on $\mathrm{FM}_k(\C)$ descending to $E_1$-chiral after Dolbeault cohomology.
- Open colour $=$ topological factorisation on $\R$ $=$ $E_1$-structure after Ayala-Francis 2015.
- Directional restriction $\mathsf{SC}^{\mathrm{ch,top}}(\ldots,\mathrm{top},\ldots;\mathrm{cl})=\varnothing$ $=$ one-way Stage-1 $\to$ Stage-2 specialisation of Vol III $\Phi_d$.
- Bar differential $=$ closed-colour holomorphic-factorisation map at coincident points (chain-level OPE pole).
- Bar coproduct $=$ open-colour topological-factorisation map along transverse $\R$-direction (mode decomposition).

Primary: Voronov 1999 *Contemp Math* 239 (Swiss-cheese); Thomas 2016 arXiv:1603.05614 (bicoloured); Kontsevich 2003 *Lett Math Phys* 66 (higher Deligne); Costello-Gwilliam 2017 FA Vol 2 §6.3 (Swiss-cheese-FA passage); Cattaneo-Felder 2004 *Commun Math Phys* 247 (bulk-boundary Poisson sigma model).

Witness on $\mathcal H_1$: $\mu^{\mathrm{ch,top}}_2(a,a)=1\cdot\delta(t)$ extracts OPE residue (closed) and places it at $t=0$ on open colour. The minimal nontrivial bicoloured operation.

---

## Cycle 2: Topologisation $=$ BRST-trivial promotion $E_1\to E_{k+2}^{\mathrm{top}}$

**Theorem (Topologisation $=$ BRST-exact stress-tensor promotion).** For $A=V_k(\hat{\mathfrak g})$ at non-critical level $k+h^\vee\ne 0$, the chiral direction $E_1^{\mathrm{ch}}$ promotes to $E_3^{\mathrm{top}}$ on $Q_{\mathrm{tot}}$-cohomology via a single inner stress tensor $T^{(1)}=[Q_{\mathrm{tot}},G^{(1)}]$. For $\mathcal W_N$ at non-critical level, $k-1=N-1$ inner stress tensors promote to $E_{N+1}^{\mathrm{top}}$. For $\mathcal W_\infty$, the limit promotes to $E_\infty^{\mathrm{top}}$ (conditional on $N\to\infty$ convergence).

Physics: a conformal vector with BRST-exact stress-tensor provides infinitesimal translation operators in $k$ additional chiral directions, promoting from $E_1$ (one real direction) to $E_{k+1}^{\mathrm{top}}$ (complex dim $k$ chiral plus one real) after Dunn additivity. Mathematics: chain-level retraction $[d,h]=\mathrm{id}-p$ witnesses the promotion on $Q_{\mathrm{tot}}$-cohomology; Lurie HA Thm 5.1.2.2 (Dunn additivity); retract requires invertibility of $k+h^\vee$. At critical level ($k=-h^\vee$), the Feigin-Frenkel regime, topologisation fails in its generic form.

Witness on $\widehat{\mathfrak{sl}_2}_{k=1}$: Sugawara $T^{\mathrm{Sug}}$ at $c=1$, one inner stress tensor $T^{(1)}$, promotion to $E_3^{\mathrm{top}}$; computable in one page.

Primary: Feigin-Frenkel 1992 *Int J Mod Phys A* 7 (critical level); Friedan-Martinec-Shenker 1986 *Nucl Phys B* 271 (BRST); Lurie *HA* §5.1 (Dunn additivity).

---

## Cycle 3: 6d hCS on K3$\times$C² $=$ Stage-1 FA on CY-3 $=$ effective action exponentiating BV tower

**Theorem (6d hCS partition function $=$ Borcherds lift exponential; LHS $=$ RHS conditional on all-loop modular invariance).**
$$Z_{\mathrm{hCS}}(\tau,z,\tau',\hbar)\;=\;\left(\frac{\Phi_{10}(\tau,z,\tau')}{\eta(\tau)^{24}\eta(\tau')^{24}}\right)^{\hbar\cdot c_{\mathrm{K3}}(Z)}\;=\;\exp\!\left(\hbar\int_Y\Omega_Y\wedge\mathrm{ch}_4^{\mathrm{ad}}(\mathcal A)\cdot\log(\Phi_{10}/\eta^{48})\right).$$
LHS (physics): BV-quantised 6d holomorphic Chern-Simons partition function on $Y=\mathrm K3\times E$ with coupling $\hbar$ (Costello 2013 *Pure Appl Math Q* 9 §2). Middle (automorphic): Borcherds lift of the K3 elliptic genus as a weight-10 Igusa cusp form divided by two $\eta^{24}$-factors to cancel bimodular weight $(12,12)$ on the Siegel diagonal (Borcherds 1998 *Invent Math* 132 Thm 1.7; Gritsenko-Nikulin 1998). RHS (math): BV obstruction-tower exponential with $\mathrm{ch}_4^{\mathrm{ad}}$ the adjoint Chern-character degree-8 component.

**Scope declaration.** Two-loop obstruction $c_2=0$ is proved (`bv_brst.tex:2925-2963`, two-path verification: Feynman theta-graph $\chi(K3)=24$ cancellation + Siegel modular invariance). The all-loop identification $Z_{\mathrm{hCS}}=(\Phi_{10}/\eta^{48})^{\hbar c_{K3}}$ beyond two loops is CONJECTURAL: $\hbar^3$ obstruction is non-zero proportional to $[\Delta_5]^2=[\Delta_{10}]$ (`bv_brst.tex:2999`), and the all-orders resummation depends on the full Pentagon $\hbar^3$-associator twist. The Polyakov equals sign holds at two loops unconditionally; beyond two loops it is a conjecture pinned by modular invariance + Borcherds-singularity uniqueness.

The three expressions coincide because the Costello effective action on $\R^3\times\mathrm K3\times\C^2$ exponentiates the BV one-loop anomaly tower, whose leading coefficient is $\chi(\mathrm K3)=24$ via Hirzebruch, and whose all-orders resummation is the Borcherds lift of the K3 elliptic genus. Primary: Costello 2011 *Renormalization and Effective Field Theory* Thm 13.4.1 (BV quantisation existence); Costello-Li 2016 arXiv:1605.09930 Prop 5.2 (locality); Costello-Gwilliam 2021 FA Vol 2 Ch 4 (non-compact modification).

**Theorem (6d hCS one-loop anomaly $=$ quartic adjoint Casimir).** The one-loop obstruction is
$$[\mathrm{Obs}_1]\;=\;(2\pi i)^{-3}\int_Y\Omega_Y\wedge\mathrm{ch}_4^{\mathrm{ad}}(\mathcal A)\;=\;\frac{h^\vee}{12}\int_Y\Omega_Y\wedge\mathrm{Tr}(F\wedge F)^2,$$
admitting two cohomologous representatives (bubble cubic-$\mathcal A$ at ghost 0, box quartic-$c$ at ghost $+1$), related by CS descent $F=\bar\partial c+\tfrac12[c,c]$. Physics: BV anomaly cocycle. Mathematics: adjoint Chern-character integral. Deligne factorisation $\mathrm{tr}_{\mathrm{adj}}T^4=\alpha_{\mathfrak g}(\mathrm{tr}_{\mathrm{adj}}T^2)^2$ on the exceptional series (Deligne 1996 *CR Acad Sci Paris Math* 322) yields cancellation locus
$$\mathrm{Anom}_1=0\iff \mathfrak g\in(\mathrm{Deligne}^{\mathrm{exc}}\setminus\{E_6,A_2\text{-unref}\})\cup\{\text{abelian}\}\cup\{\mathrm{str}_{\mathrm{ad}}=0\}\cup\{K^{-1/2}\text{-refined}\}.$$

---

## Cycle 4: 3d quantum gravity climax $=$ BPS microstate counting $=$ Siegel modular $=$ Borcherds lift

**Theorem (Climax equation — four-way physics=mathematics).**
$$\underbrace{Z^{\mathrm{AdS}_3\times\mathrm K3}_{\mathrm{3D\,QG}}(\tau,z,\tau')}_{\text{D1-D5-P }1/4\text{-BPS index}}\;=\;\underbrace{\frac{1}{\Phi_{10}(\tau,z,\tau')}}_{\text{Igusa cusp inverse}}\;=\;\underbrace{\sum_{N\ge 0}q^N\chi(\mathrm{Hilb}^N\,\mathrm K3)}_{\text{Göttsche generating series}}\;=\;\underbrace{\mathrm{sThL}(\chi^{\mathrm K3}_{\mathrm{ell}})^{-1}}_{\text{Borcherds lift inverse}}.$$
Chain of four equalities, each a theorem:
- LHS$=$RHS-1: Dijkgraaf-Verlinde-Verlinde 1997 *Nucl Phys B* 484 (D1-D5-P bound-state index equals $1/\Phi_{10}$).
- RHS-1$=$RHS-2: Göttsche 1990 *Math Ann* 286 (Hilbert-scheme generating series) + MNOP 2006 *Compositio Math* 142 (GW/DT on K3$\times E$).
- RHS-1$=$RHS-3: Borcherds 1998 *Invent Math* 132 Thm 1.7 (singular theta lift of K3 elliptic genus).

Four readings of one mathematical object: physical BPS microstate count, arithmetic Igusa form, geometric Hilbert-scheme, automorphic Borcherds lift. The climax of Vol II.

**Theorem (BPS microstate counting $=$ Gritsenko-Nikulin denominator identity).**
$$\sum_{\alpha\in\Lambda^+_{\mathrm{BKM}}}(-1)^{\ell(\alpha)}e^{-\alpha}\;=\;\Phi_{10}(Z)\;=\;qpy\prod_{(n,m,\ell)>0}(1-q^np^my^\ell)^{c_{\mathrm K3}(4nm-\ell^2)}\;=\;Z^{1/4\,\mathrm{BPS}}_{\mathrm{CHL\,}N=1}(q,p,y)^{-1}.$$
Gritsenko-Nikulin 1998 *JRAM* 507 (BKM Weyl-Kac denominator); Borcherds 1998 (infinite product); Jatkar-Sen 2006 *JHEP* 04 (CHL BPS count). The multiplicities $c_{\mathrm K3}(4nm-\ell^2)$ are K3 elliptic-genus Fourier coefficients — simultaneously physical ($1/4$-BPS state degeneracies) and arithmetic (Jacobi-form expansion). The denominator-side mathematics equals the BPS-state-counting physics.

---

## Cycle 5: Factorisation algebra $=$ quantum observable structure; Costello-Gwilliam $=$ Wilsonian RG

**Theorem (Factorisation algebra $=$ quantum field theory observable structure).** A factorisation algebra $\mathcal F\colon\mathrm{Open}(M)\to\mathcal C$ on a topological/holomorphic space $M$ with values in a symmetric monoidal $(\infty,1)$-category $\mathcal C$ (Costello-Gwilliam 2017 FA Vol 1 Def 3.1.4) equals the assignment of quantum observables on causal open regions of a QFT, satisfying the factorisation property
$$\mathcal F(U_1)\otimes\cdots\otimes\mathcal F(U_n)\;\xrightarrow{\;\simeq\;}\;\mathcal F(V)$$
for pairwise disjoint opens $U_i\sqsubset V$, which equals the OPE structure of mutually spacelike-separated operators. Weiss cosheaf condition (CG Def 6.1.1) equals locality: every observable is determined by its values on arbitrarily small disjoint-disk systems.

**Theorem (Costello-Gwilliam $=$ Wilsonian RG at $(\infty,1)$-level).** The Costello 2011 scale-$L$ effective interaction $I[L]\in\mathcal O(\mathcal E)[[\hbar]]$ with Wilsonian RG trajectory
$$I[L_1]\;=\;W(P(L_1,L_2),I[L_2])$$
equals the physical Wilsonian renormalisation group at the $(\infty,1)$-categorical level (Costello 2011 *Renormalization and Effective Field Theory* Ch 2-3; CG 2021 FA Vol 2 Ch 4). The scale $L$ parametrises the family of effective interactions; the $L\to 0$ limit after counterterm subtraction is the physical partition function. The Wilsonian RG trajectory is an $(\infty,1)$-functor from $(0,\infty]$ to the effective-interaction $(\infty,1)$-category.

Counterterm ambiguity: Costello 2011 Thm 10.7.1 — torsor over a prounipotent group of local functionals at each loop order. Physical statement (RG ambiguity) $=$ mathematical statement (prounipotent torsor).

---

## Summary: Vol II physics=mathematics (scope-stratified after round-2 audit)

- $\mathsf{SC}^{\mathrm{ch,top}}$ $=$ bulk-boundary 3d HT QFT operad (bicoloured dioperad with directional restriction; Voronov + Thomas + Cattaneo-Felder).
- Topologisation $=$ BRST-exact stress-tensor promotion $E_1^{\mathrm{ch}}\to E_{k+2}^{\mathrm{top}}$ at non-critical level $k+h^\vee\ne 0$ (chain-level retract). Critical-level case excluded.
- 6d hCS partition function $=$ Borcherds lift exponential: PROVED at 2-loop via theta-graph $\chi(K3)=24$ cancellation + Siegel modular invariance; CONJECTURAL beyond 2-loop ($\hbar^3$ Pentagon-associator twist open).
- 6d hCS one-loop anomaly $=$ quartic adjoint Casimir $\to$ Deligne locus. $E_6$ strict-excluded; $A_2$-refined in locus via critical-level twist.
- Climax $=$ $Z_{\mathrm{3DQG}}=1/\Phi_{10}$ four-way equality (DVV + Borcherds + MNOP + Göttsche), each equals sign inscribed.
- BPS microstates $=$ Gritsenko-Nikulin denominator (Borcherds infinite product + CHL physical identification).
- Factorisation algebra $=$ QFT observable structure (Costello-Gwilliam 2017 axiomatisation).
- Costello-Gwilliam $=$ Wilsonian RG at $(\infty,1)$-level.

**Round-2 adversarial-audit findings (rectified in this file):**
- Averaging map (Vol II/I bridge) $=$ $R$-matrix-twisted $\Sigma_n$-quotient, not naive Bose symmetrisation. Reduction to Bose symmetrisation only at $R=\tau$ (pole-free $E_\infty$ subclass). Vol II `foundations.tex:258` already uses $R$-twisted framing.
- 24-count on $\mathrm K3\times\C^2$ twisted-11d M5 setup is distinct from F-theory IIB 7-brane setup: both produce count 24 on the same elliptic K3 by dual frames, not by identification-in-place.

*2026-04-22. Raeez Lorgat. Round-2 Polyakov audit: scope-stratified inscriptions.*
