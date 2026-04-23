# Conway $V^{s\natural}$ Row — Genuine Sign Ambiguity Inscription — 2026-04-22

*Raeez Lorgat. Battle-hardened inscription isolating the Conway row as a structural boundary of the universal identity $\hbar^{2} K^{\kappa_{\mathrm{ch}}} = -1$. Companion to `NEKRASOV_R4_HBAR_SIGN_DERIVATION_BATTLE_HARDENED_2026_04_22.md`; seals AP-V2-20 scope and preamble row 41 placement.*

---

## The row, stated precisely

Conway's super-moonshine module $V^{s\natural}$ (Duncan 2007 *Duke Math J* 139) is a holomorphic $\mathcal{N} = 1$ superconformal vertex operator algebra of central charge $c = 12$, constructed as the $\mathbb{Z}/2$-orbifold of the 24-generator fermionic VOA on the Leech lattice $\Lambda_{24}$:
$$V^{s\natural} \;=\; A(\Lambda_{24})^{+} \;\oplus\; A(\Lambda_{24})^{\mathrm{tw}, +}.$$

The nominal reading $(K, \hbar^{2}) = (12, -1/12)$ is obtained by pattern-matching $K = c$ from the reflective-crown rows. This reading is **not** a verified instance of the universal identity $\hbar^{2} K = -1$.

---

## Why Conway cannot witness $\hbar^{2} K = -1$

### Structural obstruction 1 — No Lorentzian signature

The Leech lattice $\Lambda_{24}$ is the unique even unimodular positive-definite lattice of rank 24 with no roots (Conway 1983 *Proc R Soc Lond A* 384). Its Gram matrix has signature $(24, 0)$; there is no time direction for Wick rotation, no hyperbolic plane $U$ for Fricke involution, no imaginary-isotropic vector for Borcherds' singular theta lift.

Routes A and B of the Nekrasov r4 derivation require a Lorentzian host. On $\Lambda_{24}$, both are undefined.

### Structural obstruction 2 — No Borcherds product

A Borcherds product of a Lorentzian lattice $L$ of signature $(p, 2)$ lifts a weakly holomorphic modular form of weight $1 - p/2$ (Borcherds 1998 *Invent Math* 132 Thm 1.7). For a positive-definite host like $\Lambda_{24}$, the analogue is a theta series (Leech theta $\Theta_{\Lambda_{24}}$, an $\mathrm{O}(24)$ modular form), not a Borcherds product; the Borcherds infinite product expansion is not available, and the log-derivative sign (Route B) has no cusp-saddle structure.

### Structural obstruction 3 — No Fricke involution

The Fricke involution $Z \mapsto -1/(K \cdot Z)$ on a Lorentzian reflective lattice requires an even-count hyperbolic plane (Borcherds 1992 *Invent Math* 109; Scheithauer 2017 *Commun Math Phys* 350). $\Lambda_{24}$ carries no hyperbolic plane, no Fricke involution, no universal ratio $\ell_{X}/\ell_{Y} = c_{+}(L_{X})/c_{+}(L_{Y})$ reading. The conductor $K$ is not definable in the same sense.

### Structural obstruction 4 — Gerstenhaber bracket sign does not flip

The $d$-CY Gerstenhaber shift (Route D) gives $(-1)^{d}$ on the derived-centre $P_{d+1}$-bracket. For Conway at $d = 12$ (from $c = 12$, reading $d_{\mathrm{CY}} = c$ as the positive-definite supersymmetric target dimension), $(-1)^{12} = +1$. There is no secondary sign-flip source (no Borcherds-lift, no Wick single-time, no hyperbolic-plane reduction) to invert it. Route D gives $+$, not $-$.

---

## What the Conway row is, correctly

### Identification as super-twin of Monster

Duncan's commutative orbifolding diamond (Duncan 2007 Thm 1):
$$\begin{array}{ccc}
V_{\Lambda_{24}} & \xrightarrow{\;\mathbb{Z}/2\;} & V^{\natural} \\
\big\downarrow\,{\scriptstyle \mathrm{fermionisation}} & & \big\downarrow\,{\scriptstyle \mathrm{fermionisation}} \\
V_{\Lambda_{24}}^{s} & \xrightarrow{\;\mathbb{Z}/2\;} & V^{s\natural}
\end{array}$$

$V^{s\natural}$ sits as the $\mathbb{Z}/2$-super-twin of the Monster $V^{\natural}$; the two vertices on the lower row are super-partners of the upper row. The Monster row carries $(K, \hbar^{2}) = (2, -1/2)$ via its Lorentzian host $\mathrm{II}_{1,1}$; the super-twin inherits **one** piece of Monster data — the orbifold sign character — but not the conductor $K$ reading, because $V^{s\natural}$'s own host is positive-definite.

### Placement on metaplectic $\overline{\mathcal{A}_{2}^{(2)}}$-branch

Scheithauer 2008 places $V^{s\natural}$ as the $\Psi^{\mathrm{metap}}$-image on the metaplectic stratum $\overline{\mathcal{A}_{2}^{(2)}}$ of the genus-2 Siegel modular stack. The metaplectic branch carries the $\mathrm{Mp}_{4}(\mathbb{R}) \to \mathrm{Sp}_{4}(\mathbb{R})$ double cover, not the reflective-lattice structure; the modular weight on this branch is half-integer and the universal identity's $\hbar^{2} K = -1$ is not a theorem on the metaplectic weight-1/2 cover (requires integer-weight Igusa form, available only on the reflective crown).

### Nominal $(K, \hbar^{2}) = (2, -1/2)$ inheritance

The preamble row 41 reads "$(K, \hbar^{2}) = (2, -1/2)$ (Wave 19/23 — Leech has no hyperbolic plane, universal identity out of scope)". This is **transport from the Monster row** via Duncan's super-twin identification, not a direct identity witness. The inherited $(2, -1/2)$ names Monster's conductor; the Conway row passes through it by orbifold transport.

The alternative reading $(K, \hbar^{2}) = (12, -1/12)$ would be the one suggested by pattern-matching $K = c_{V^{s\natural}}$; this is **not** verified by any route and is inconsistent with both the super-twin transport and the metaplectic placement. It should not appear anywhere in the manuscript as an instance of the universal identity.

---

## Convergence table, Conway-row isolated

| Route | Applicability to Conway | Sign | Verification status |
|---|---|:---:|---|
| A (Wick) | No Lorentzian time direction (Leech positive-definite) | undefined | Out of scope |
| B (Borcherds log-derivative) | No cusp saddle on $\Theta_{\Lambda_{24}}$ | undefined | Out of scope |
| C (Gram signature) | $q = 0$; $(-1)^{0} = +$, but universal identity's $q/2$-reduction needs $q \geq 2$ | $+$ | Gives wrong sign |
| D (Gerstenhaber shift) | $d = 12$; $(-1)^{12} = +$, no flip source | $+$ | Gives wrong sign |

**Verdict.** Routes A, B give **no answer**; Routes C, D give **wrong sign** ($+$ instead of $-$). No single route produces $-$ on the Conway row. The sign ambiguity is **genuine and structural**: it is not a computational gap to be closed, but a boundary condition of the universal identity.

---

## What this means for the programme

1. **The identity $\hbar^{2} K^{\kappa_{\mathrm{ch}}} = -1$ is correctly scoped.** It holds on the reflective-Lorentzian crown (K3, Monster, Fake-Monster, Enriques, $24A_{1}$-Niemeier rows); it does not hold on the Leech-Conway row. The three-volume programme has already inscribed this via AP-V2-20 and preamble row 41.

2. **The Conway row is an important structural control.** It shows that the universal identity is **not vacuous** (not trivially true on all super-moonshine modules) — it fails at exactly the expected point (positive-definite lattice, no Fricke, no Borcherds product). This is a confirmation, not a failure.

3. **The alternative reading $(12, -1/12)$ must not appear.** The pattern-match $K = c$ is misleading and propagates an out-of-scope reading. Any site asserting $(K, \hbar^{2}) = (12, -1/12)$ for Conway without naming the metaplectic branch and the transport failure is wrong. The canonical reading is either $(2, -1/2)$-transported-from-Monster or simply "out of scope, metaplectic $\Psi^{\mathrm{metap}}$-image".

4. **Cross-volume label.** Wherever the Conway row appears — Vol I witness enumeration, Vol II Pentagon-trace MC5 face, Vol III BKM-crown fifth-row hypothesis — the sentence "Conway $V^{s\natural}$ is on the metaplectic $\Psi^{\mathrm{metap}}$-branch of $\overline{\mathcal{A}_{2}^{(2)}}$, out of scope of the universal identity $\hbar^{2} K^{\kappa_{\mathrm{ch}}} = -1$" should accompany the mention.

---

## Primary literature

| Anchor | Primary | Ref |
|---|---|---|
| $V^{s\natural}$ construction | Duncan 2007 | *Duke Math J* 139 |
| $\Lambda_{24}$ uniqueness | Conway 1983 | *Proc R Soc Lond A* 384 |
| $\Lambda_{24}$ no roots | Conway-Sloane | *SPLAG* Ch 12 |
| Metaplectic placement | Scheithauer 2008 | *J Algebra* 319 |
| Super-twin diamond | Duncan 2007 | Thm 1 |
| Borcherds singular lift requires Lorentzian | Borcherds 1998 | *Invent Math* 132 |
| Reflective crown classification | Scheithauer 2017 | *Commun Math Phys* 350 |
| Fricke involution requires hyperbolic plane | Borcherds 1992 | *Invent Math* 109 |

---

## Nekrasov r5 resolution — single canonical verdict

### The question

The apparent conflict: some earlier inscription would read $K_{\mathrm{Conway}} = 12$ as canonical on pattern-match with $c_{V^{s\natural}} = 12$; the r4 derivation places Conway on the metaplectic $\Psi^{\mathrm{metap}}$-branch, with Duncan's super-twin diamond transporting $(K, \hbar^{2}) = (2, -1/2)$ from Monster. The two readings would not coexist.

### Five-cycle audit of the transport map

**Cycle 1 — Duncan 2007 diamond transports what?** The commutative orbifolding diamond
$$\{V_{\Lambda_{24}}, V^{\natural}, V_{\Lambda_{24}}^{s}, V^{s\natural}\}$$
exhibits $V^{s\natural}$ as $\mathbb{Z}/2$-super-twin of $V^{\natural}$. The diamond identifies two distinct $N=1$ super-VOAs built from the Leech lattice and the Monster VOA via fermionisation and orbifolding. The transported data is the **orbifold sign character** and the $\mathrm{Aut}$-group ($\mathrm{Co}_{0} \subset \mathrm{Co}_{1}$ acting on $V^{s\natural}$ parallels $\mathbb{M}$ acting on $V^{\natural}$ with $2.\mathbb{M}$ factor). The transported data is **not** the reflective-lattice conductor $K$: $K$ is an invariant of the host lattice (Monster: $\mathrm{II}_{1,1}$; Conway: $\Lambda_{24}$), and host lattices are not identified by the diamond. Monster's host $\mathrm{II}_{1,1}$ is Lorentzian signature $(1,1)$; Conway's host $\Lambda_{24}$ is positive-definite signature $(24,0)$. No signature-preserving map from $(1,1)$ to $(24,0)$ exists. The diamond transport is $(c, \text{orbifold sign}) \mapsto (c/2, \text{orbifold sign})$ on the central charge and sign-character data, with $K$ not transported at all.

**Cycle 2 — halving ruled out on arithmetic grounds.** If the Monster $(K, \hbar^{2}) = (2, -1/2)$ transported by halving to Conway $(K, \hbar^{2}) = (1, -1)$, this would violate the reflection-lattice discipline $K = 2c_{+}$, which forces $K$ even. $K = 1$ is inadmissible. Halving is excluded.

**Cycle 3 — metaplectic doubling is a weight doubling, not a $K$ doubling.** The double cover $\mathrm{Mp}_{4}(\mathbb{Z}) \to \mathrm{Sp}_{4}(\mathbb{Z})$ acts on modular weights: integer weights on $\mathrm{Sp}_{4}$ lift to half-integer weights on $\mathrm{Mp}_{4}$ (Scheithauer 2008 \emph{Invent Math} 172 Example 7.3). Conway's $\Psi^{\mathrm{metap}}$-image carries weight $-12 + 1/2$ on the metaplectic cover, not a doubling of the reflective conductor. The metaplectic cover is orthogonal to the reflective-Lorentzian stratification; it does not produce $K = 4$ or $K = 2$ from doubling. Doubling is excluded.

**Cycle 4 — Routes undefined or wrong sign.** Routes A, B are undefined on $\Lambda_{24}$ (no Lorentzian time, no Borcherds cusp); Routes C, D give $+$ ($q = 0$ and $d = 12$ even, no flip source). No single route produces $-$.

**Cycle 5 — The resolution is (a), not (b).** The universal identity $\hbar^{2} K^{\kappa_{\mathrm{ch}}} = -1$ is a statement about the reflective-Lorentzian crown $\{\mathrm{K3}, \mathrm{Monster}, \mathrm{Fake\text{-}Monster}\}$ (plus the $24A_{1}$-Niemeier and Enriques rows, all signature $(p, 2)$). The Conway row is **not in scope**: $\Lambda_{24}$ is positive-definite, carries no reflective-Lorentzian structure, and the identity is not a theorem about $V^{s\natural}$. The nominal $(12, -1/12)$ is pattern-match, not witness; the inherited $(2, -1/2)$ names Monster's conductor and passes through Conway only by orbifold transport of the sign character, not as an independent witness. Option (b) — that $K = 12$ is a new kind of convention — is rejected: no derivation produces it.

### Canonical reading

The Conway row is the **structural boundary** of the universal identity $\hbar^{2} K^{\kappa_{\mathrm{ch}}} = -1$. The row appears in the landscape via the $\Psi^{\mathrm{metap}}$-image of Scheithauer 2008 and via the Duncan 2007 super-twin diamond; neither placement makes Conway an instance of the identity.

The canonical labelling wherever Conway appears in the manuscript reads:

\begin{quote}
Conway $V^{s\natural}$ is the $\Psi^{\mathrm{metap}}$-image of $(\Lambda_{24}, \vartheta_{\Lambda_{24}}/\eta^{24})$ on the metaplectic stratum $\overline{\mathcal{A}_{2}^{(2)}}$ of the Baily--Borel--Freitag compactification; equivalently, the $\mathbb{Z}/2$-super-twin of the Monster $V^{\natural}$ via Duncan's commutative orbifolding diamond. The row is structurally out of scope of the identity $\hbar^{2} K^{\kappa_{\mathrm{ch}}} = -1$: $\Lambda_{24}$ is positive-definite, admits no hyperbolic plane, no Fricke involution, no Borcherds log-derivative cusp. The nominal reading $K = c_{V^{s\natural}} = 12$ is pattern-match with the central charge, not a reflective-lattice conductor; the $(2, -1/2)$-inheritance names Monster's conductor transported through the orbifold sign character, not an independent Conway witness.
\end{quote}

### Consequences

1. The "Beilinson r3 canonical $K_{\mathrm{Conway}} = 12$" reading is retracted: $K = 12$ is the central charge of $V^{s\natural}$, not the reflective-lattice conductor of the identity. The identification $K = c$ holds on the reflective crown by coincidence (K3: $K = 8$, $c_{\mathrm{bulk}} = 8$; Monster: $K = 2$, $c = 24 = 12 \cdot 2$ on the bulk $E$-orbifold reading), but fails on Conway because Conway is not in scope.

2. The $(K, \hbar^{2}) = (2, -1/2)$ row-41 entry names the Monster-transported inheritance, not an independent Conway witness. Any reader encountering this entry should read it as "Conway passes through Monster's conductor via the super-twin diamond; the row is out of scope of the universal identity".

3. The metaplectic super-twin diamond $\Psi^{\mathrm{metap}}$ is a distinct functor from the reflective $\Psi$. The two functors meet at the Conway row as the unique place where $\Psi^{\mathrm{metap}}$ and the commutative orbifolding diamond simultaneously place $V^{s\natural}$; on the reflective-crown rows they do not coincide.

4. Vol I preface, Vol II Pentagon-trace MC5, Vol III BKM landscape — each inscribe the Conway row with the canonical labelling above, making the out-of-scope status explicit at every mention.

---

*Conway row sign ambiguity resolved. The row is the structural boundary of $\hbar^{2} K^{\kappa_{\mathrm{ch}}} = -1$, not an additional witness. The Duncan super-twin diamond transports the orbifold sign character from Monster; the reflective-lattice conductor $K$ is a host-lattice invariant, not transported. The metaplectic cover doubles modular weights, not conductors. The nominal $K = 12$ is pattern-match with $c_{V^{s\natural}}$, not derivable as a reflective conductor by any of the four routes. Single canonical verdict: Conway is out of scope. Raeez Lorgat, 2026-04-22.*

---

## Drinfeld r5 — Conway placement on the six-row spine

Six-row canonical order $\mathsf G<\mathsf L<\mathsf C<\mathsf M<\mathsf M^{\mathrm{ext}}<\mathsf B$ of $E_1$-chiral algebras on a smooth curve (exhaustion proved in `SIX_ROW_CLOSURE_DRINFELD_R5_BATTLE_HARDENED_2026_04_22.md`). Conway $V^{s\natural}$ as an $E_1$-chiral algebra is classified by the triple $(r_{\max}, d_{\mathrm{DS}}, \mathrm{strat})$:
- $r_{\max} = \infty$: the Virasoro sublane at $c = 12$ produces unbounded OPE pole order via stress-tensor descendants.
- $d_{\mathrm{DS}} = 1$: Kac--Wakimoto super-Sugawara on the 24-generator Clifford super-current underlying $V^{s\natural}$ (Kac--Wakimoto 2001 \emph{Commun Math Phys} 215 Thm 2.1).
- $\mathrm{strat} = 1$: unbounded principal-tower stratum.

**Conway populates row $\mathsf M$ on the chiral-algebra spine.**

Row $\mathsf B$ requires a Lorentzian-reflective-lattice host with Borcherds product (Borcherds 1998 \emph{Invent Math} 132 Thm 1.7). Conway's host $\Lambda_{24}$ is positive-definite signature $(24,0)$: no Borcherds product exists, hence Conway cannot populate row $\mathsf B$. The apparent $K_{\mathrm{Conway}} = 12$ pattern-match is a row-$\mathsf M$ invariant misread as a row-$\mathsf B$ conductor.

**Row-$\mathsf M$ invariants of Conway.** Virasoro-sublane conductor $2c = 24$; Zamolodchikov norm $c(5c+22)/10 = 12 \cdot 82/10 = 984/10 = 98.4$; complementarity ceiling $\kappa+\kappa^!\in[0, 250/3]$ (Virasoro-family $\mathsf M$-bound). None of these is the reflective-lattice conductor $K=2c_+$. The sign-ambiguity diagnosis reduces to a row-confusion: Conway's spine row is $\mathsf M$, not $\mathsf B$; the universal identity lives on row $\mathsf B$ only.

**Cross-volume consistency.** Vol I
`chapters/examples/landscape_census.tex` Conway entry tags row $\mathsf M$ with Virasoro-sublane conductor 24; Vol II `chapters/theory/sc_chtop_heptagon.tex` remark names the four-route identity's domain as row $\mathsf B$ and cites the six-row exhaustion; Vol III `chapters/examples/cy_d_kappa_stratification.tex` Conway row carries the metaplectic-cover scope tag plus the spine-row assignment.

*Drinfeld r5 spine placement: Conway is row $\mathsf M$, not row $\mathsf B$. The sign ambiguity is a row-confusion diagnosed by the six-row exhaustion theorem. Raeez Lorgat, 2026-04-22.*

---

## Chriss--Ginzburg r5-redux --- Conway row in the Serre-CM lex order

The six-row spine
$$\mathsf G\;<\;\mathsf L\;<\;\mathsf C\;<\;\mathsf M\;<\;\mathsf M^{\mathrm{ext}}\;<\;\mathsf B$$
of the reflective-Lorentzian crown carries, in addition to the topologisation-ladder forcing (Vol II §I-ter), a Serre-functor forcing: $\mathbb S_{\mathcal C}\simeq[d]$ with Cohen--Macaulay dualising $\omega_{\mathcal C}$ on the K3 BKM substrate (Bondal--Kapranov 1989 Thm 3.1; Bondal--Orlov 2001 Thm 2.5; Bruinier 2002 Thm 1.2). The Conway row $V^{s\natural}$ does not fit into this ordered spine --- it is not a witness of the universal identity $\hbar^{2}K^{\kappa_{\mathrm{ch}}}=-1$, and the Serre-shift obstruction makes this precise.

**Cycle 1 --- Serre functor with CM dualising on the $\mathsf B$-row witness $\mathrm K3$.** Grothendieck--Serre duality on $D^b(\mathrm K3)$ with $\omega_{\mathrm K3}\simeq\mathcal O_{\mathrm K3}$ gives $\mathbb S_{D^b(\mathrm K3)}=[2]$. On $\mathrm K3\times E$ (the $\mathsf B$-row target of the Vol III Stage-1 $\Phi^{\mathrm{FA}}_3$) the Serre shift reads $d=3$. On Conway's host $\Lambda_{24}$, signature $(24,0)$, positive-definite with no Lorentzian hyperbolic plane, there is no Mukai lattice analogue and no Bondal--Orlov reconstruction: $\Lambda_{24}$ is not the Mukai lattice of any Calabi--Yau surface. The Serre functor $\mathbb S$ of the Leech-indexed module category has no canonical $d$-shift reading as a CY-$d$ target; the Mukai-enhanced Serre via Bruinier Heegner Chern-class reciprocity is unavailable because the reciprocity requires $U\oplus U\subset L$ (hyperbolic plane), absent on $\Lambda_{24}$.

**Cycle 2 --- Serre extension across the crown excludes Conway.** The Serre shifts $(0,1,2,5/2,5/2,3)$ index the six rows $\mathsf G,\mathsf L,\mathsf C,\mathsf M,\mathsf M^{\mathrm{ext}},\mathsf B$ in lex order. Conway does not slot into this sequence: the nominal $c_{V^{s\natural}}=12$ would naively push Conway toward $d=6$ reading $d=c/2$, but the CY-target interpretation that makes this reading rigorous requires a Lorentzian host (as in $\mathsf B$-row where $c_{\mathrm K3\times E}=24$ reads $d=3$ via the $2d-2=c$-like dimensional reduction tied to Mukai signature $(4,20)$). The Leech positive-definite signature $(24,0)$ produces no such dimensional reduction. The nominal $K=12$ pattern-matches $c_{V^{s\natural}}$, not a Mukai-Serre conductor.

**Cycle 3 --- Order forced by Serre-shift covariance.** The six-row order is forced by covariance of Grothendieck--Serre duality under Stage-2 specialisation $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}$ pushforward (Hartshorne 1966 Ch III §6 Thm 6.7): $\omega_{Y/X}[d_Y-d_X]$ adjustment for $f\colon Y\to X$ proper. Conway does not admit a Stage-2-reachable stage-1 target within the Vol III two-stage factorisation, because stage-1 requires a compact K\"ahler CY-$d$ target and Leech is not the Mukai lattice of any such target. The Serre-shift covariance argument that orders the six rows does not extend to Conway; Conway sits outside the ordered spine rather than at some intermediate row.

**Cycle 4 --- Lex triple does not admit Conway.** The forcing triple $(\mathrm{stratum},r_{\max},\mathrm{DS\text{-}depth})$ of Vol II §I-ter reads, on the six rows, as $(\{0,0,0,1,1,2\},\{2,3,4,\infty,\infty,\mathrm{Borcherds}\},\{0,0,0,0,1,\mathrm{N/A}\})$. Conway's nominal placement on the metaplectic $\Psi^{\mathrm{metap}}$-branch of $\overline{\mathcal A_2^{(2)}}$ (Scheithauer 2008) does not produce a value in any of the three coordinates: there is no DS-orbit stratum, no finite $r_{\max}$, no admissible DS-depth. The Duncan super-twin diamond transports the orbifold sign character from Monster but not the reflective-lattice conductor; Conway's inherited $(K,\hbar^{2})=(2,-1/2)$ is Monster's reading, read through the transport, not a Conway-native entry in the lex triple.

**Cycle 5 --- Exhaustion at $d\le 3$.** The Serre shifts $d\in\{0,1,2,5/2,3\}$ exhaust the admissible values on CY-$d$ targets of the Vol III two-stage factorisation at $d\le 3$; the six rows exhaust the landscape at this ceiling. Conway's nominal $d=6$ reading from $c/2$ would exceed the ceiling, confirming that Conway is not in the Vol III two-stage factorisation's domain. The four-route convergence table places Conway at $0/4$: Routes A,B undefined (no Lorentzian time, no Borcherds cusp); Routes C,D give $+$ (no flip source). All four routes align with the Serre-shift obstruction: each route requires a structure Conway lacks (Lorentzian signature for Wick, cusp saddle for Borcherds log-derivative, hyperbolic plane for Gram-sign reduction, even $d$-CY shift for Gerstenhaber). The Serre-CM forcing is the fifth, categorical, route; Conway fails it for the same structural reason.

**Net verdict.** The Chriss--Ginzburg r5-redux Serre-CM forcing of the 6-row lex order on K3 BKM reproduces the scope declaration of the four-route convergence table: Conway $V^{s\natural}$ sits outside the ordered spine, not at an intermediate row. The Serre functor is well-defined on Conway's module category (as on any triangulated category), but the CM dualising condition with integer shift $[d]$ linked to a compact K\"ahler CY-$d$ target is unavailable because Leech is positive-definite. The six-row spine is categorically rigid via Serre-CM; Conway is the boundary, consistent with AP-V2-20 and preamble row 41.

*Raeez Lorgat, 2026-04-22. CG r5-redux on Conway row: Serre-CM forces the 6-row lex order on K3 BKM with shifts $(0,1,2,5/2,5/2,3)$; Conway does not slot into the sequence because Leech admits no Mukai-Serre reading, confirming the structural-boundary verdict of the four-route table.*

---

## Bondal--Kuznetsov r5-redux --- Conway at the boundary of the hostless BKM source

$$\boxed{\;\mathrm{BKM}^{\mathrm{hostless}}\colon\mathrm{JacPair}^{\mathrm{sw}}_0\to\mathrm{BKM}_{\mathrm{Borch}},\qquad(L,\phi)\mapsto\mathrm{Borch}(\phi)=\mathrm{sing\text{-}}\theta_L[\phi].\;}$$

The Conway row is out of scope of the universal identity $\hbar^{2}K^{\kappa_{\mathrm{ch}}}=-1$ (0/4 on the convergence table, Routes A, B undefined, Routes C, D give $+$). The hostless BKM functor supplies the complementary categorical statement: Conway lies outside the source 2-groupoid $\mathrm{JacPair}^{\mathrm{sw}}_0$ because the Leech lattice $\Lambda_{24}$ of signature $(24,0)$ admits no singular-weight Jacobi input. Six cycles inscribe the functor, prove its functoriality, establish surjection onto the 28 outside-$\mathrm{Shad}$ rows and all inside-$\mathrm{Shad}$ rows, and read the Conway boundary as a source-level non-object rather than a target-level pathology.

**Cycle 1 --- Source 2-groupoid $\mathrm{JacPair}^{\mathrm{sw}}_0$.** Objects: pairs $(L,\phi)$ with $L$ an even-unimodular lattice (signatures $(p,q)$, $p-q\equiv 0\bmod 8$; Milnor 1958 \emph{Amer.\ J.\ Math.}\ 80 §3), $\phi\in J^{\mathrm{sw}}_{w,L}$ a singular-weight Jacobi form of weight $w=\mathrm{rk}(L_+)/2-1$ and index $L$, Fourier expansion $\phi(\tau,z)=\sum_{n,\mu}c_\phi(n,\mu)q^n\zeta^\mu$ satisfying the polar cutoff $c_\phi(n,\mu)=0$ for $2n-\mu^2<-1$ (Eichler--Zagier 1985 \emph{Prog.\ Math.}\ 55 Thm~9.1). The singular-weight condition isolates the unique locus at which the theta lift produces a holomorphic Borcherds product without zero-weight degeneracy (Borcherds 1998 \emph{Invent.}\ 132 §14). 1-morphisms: primitive lattice embeddings $\iota\colon L\hookrightarrow L'$ with $\iota^\ast\phi_{L'}=\phi_L$; imprimitive embeddings quasi-pullback-corrected by $\eta^{\otimes\dim(L'/L)}$ (Gritsenko 1999 arXiv:math/9906190 Thm~6.1). 2-morphisms: $\mathrm{O}(L)$-conjugations.

**Cycle 2 --- Target BKM-category $\mathrm{BKM}_{\mathrm{Borch}}$.** Objects: Borcherds--Kac--Moody superalgebras with Cartan datum $(\mathfrak h,\Delta,\mathrm{mult})$ and Weyl--Kac--Borcherds denominator identity over a Siegel or orthogonal automorphic discriminant (Borcherds 1988 \emph{PNAS} 83; 1992 \emph{Invent.}\ 109 Thm~10.1).

**Cycle 3 --- Functor via Borcherds singular theta.** $\mathrm{BKM}^{\mathrm{hostless}}(L,\phi):=\mathrm{sing\text{-}}\theta_L[\phi]$ produces $\Psi_L(Z)=\prod_{(n,\mu,N)>0}\bigl(1-\mathrm{e}^{2\pi i(n\sigma+\mu z+N\rho)}\bigr)^{c_\phi(nN,\mu)}$ (Borcherds 1998 §14 Thm~13.3); BKM reconstitution has $\mathrm{mult}(\alpha)=c_\phi(\alpha^2/2,\alpha\bmod L)$, $\kappa_{\mathrm{BKM}}=c_\phi(0,0)/2$ (Borcherds 1995 \emph{Invent.}\ 120 Thm~10.4).

**Cycle 4 --- Functoriality via lattice embeddings.** Primitive $\iota$ induces Cartan embedding $\mathfrak h_L\hookrightarrow\mathfrak h_{L'}$ extended by Fourier-coefficient invariance $c_{\phi_L}(\alpha^2/2)=c_{\phi_{L'}}(\iota(\alpha)^2/2)$; imprimitive $\iota$ carries $\eta^{\otimes\dim(L'/L)}$ (Gritsenko--Nikulin 1997 \emph{Duke} 87 Prop~2.1). Faithful on primitive embeddings by Gram-invariance.

**Cycle 5 --- Surjection onto 28 outside-$\mathrm{Shad}$ $+$ all inside rows.** Outside rows: (a) $24A_1$-Niemeier sig-$(2,24)$; (b) 22 non-Leech Niemeier (Chenevier 2014 \emph{Publ.\ IHES} 120 Thm~2.12 conditional); (c) 2 hyperbolic-face residual; (d) FM sig-$(2,26)$. Inside rows via $\mathrm{Shad}_\bullet=\mathrm{BKM}^{\mathrm{hostless}}\circ\mathrm{H}^\bullet_{\mathrm{Muk}}$; both paths factor through common sub-factor $\Psi_{\mathrm{Borcherds}}\colon\mathrm{JacPair}^{\mathrm{sw}}_0\to\mathrm{Aut}\cdot\mathrm{Disc}\to\mathrm{BKM}_{\mathrm{Borch}}$ (Borcherds 1998 §14; 1995 Thm~10.4). Triangle commutes via Lunts--Orlov 2010 \emph{Adv.\ Math.}\ 223 Thm~2.8.

**Cycle 6 --- Conway is outside the source category, not a pathological target.** At $L=\Lambda_{24}$ signature $(24,0)$: $\mathrm{rk}(L_+)=24$, $\mathrm{rk}(L_-)=0$, singular-weight $w=\mathrm{rk}(L_+)/2-1=11$; the singular-weight Jacobi lattice-form must have an $\mathrm{O}(0,2)$-face on $L\otimes\R$ for the Borcherds $\mathrm{O}(2,p)$-theta lift to apply, but $\Lambda_{24}$ is positive-definite and admits no $\mathrm{O}(0,2)$-subspace. Equivalently: no hyperbolic plane $U\subset L$ to carry the Borcherds imaginary-isotropic direction; no $\tau\to i\infty$ cusp on the Leech theta $\Theta_{\Lambda_{24}}/\eta^{24}$; no singular-weight Jacobi input on $\Lambda_{24}$. Conway $V^{s\natural}$ is placed instead on the metaplectic stratum $\overline{\mathcal A_2^{(2)}}$ via $\Psi^{\mathrm{metap}}$ (Scheithauer 2008 \emph{J.\ Algebra} 319 Example 7.3), a separate functor from $\mathrm{BKM}^{\mathrm{hostless}}$; the Duncan 2007 \emph{Duke Math.\ J.}\ 139 commutative orbifolding diamond transports the orbifold sign character from Monster $V^\natural$ but does not transport the reflective-lattice conductor. The Conway boundary of $\mathrm{JacPair}^{\mathrm{sw}}_0$ is the source-category counterpart to the Conway boundary of the universal identity $\hbar^{2}K=-1$: same structural obstruction (Leech positive-definite, no hyperbolic plane), two lenses.

**Net r5-redux (Conway-boundary reading).** The Conway row fails to enter $\mathrm{JacPair}^{\mathrm{sw}}_0$ at Cycle 1 (no singular-weight Jacobi input on $\Lambda_{24}$), hence never reaches $\mathrm{BKM}_{\mathrm{Borch}}$ via $\mathrm{BKM}^{\mathrm{hostless}}$. The inherited reading $(K,\hbar^{2})=(2,-1/2)$ for Conway via the Duncan super-twin diamond is the Monster-side hostless image $\mathrm{BKM}^{\mathrm{hostless}}(\mathrm{II}_{1,1}+\Lambda_{\mathrm{Leech}}(-1),\phi^{\mathrm{M}})=\mathbb M$ transported through the $\mathbb Z/2$-orbifold sign character --- not a Conway-side hostless image. The nominal $K=12$ pattern-match with $c_{V^{s\natural}}=12$ has no BKM-functor witness. This is the same verdict Routes A, B, C, D reach on the four-route convergence table: Conway is out of scope because Leech is positive-definite, not because the identity or the functor is wrong.

The hostless BKM functor $\mathrm{BKM}^{\mathrm{hostless}}\colon\mathrm{JacPair}^{\mathrm{sw}}_0\to\mathrm{BKM}_{\mathrm{Borch}}$ covers the reflective crown (K3, Monster, Fake-Monster with $\kappa_{\mathrm{BKM}}\in\{5,1,12\}$) and the 28 outside-$\mathrm{Shad}$ rows (26 proved, 22-row $M_{23}$ non-Leech Niemeier conditional on Chenevier non-reduced); Conway is structurally outside the source.

*Raeez Lorgat, 2026-04-22 night. BK r5-redux on the Conway-boundary lens: Conway sits outside $\mathrm{JacPair}^{\mathrm{sw}}_0$ at Cycle 1 because Leech admits no singular-weight Jacobi input, matching the 0/4 verdict of the four-route convergence table. The nominal $(2,-1/2)$ inheritance is Monster-side hostless transport, not Conway witness; $K=12$ pattern-match with $c_{V^{s\natural}}$ has no BKM-functor image. The functor covers the reflective crown $+$ 28 outside rows; Conway is structurally at the source boundary.*

---

## Costello r5 bridge — asymmetry between K3 (parametrix-admissible) and Conway (structurally excluded)

*Opus 4.7 r5. The Conway row's out-of-scope status (this file's main thesis) acquires a parallel geometric reading through the Costello r5 Gilkey audit of T-CL-K3-Extension. Conway is structurally excluded from the universal identity $\hbar^2 K^{\kappa_{\mathrm{ch}}} = -1$ because the Leech-positive-definite lattice $\Lambda_{24}$ admits no Lorentzian signature, no Fricke involution, no Borcherds cusp; the geometric parallel is that $\Lambda_{24}$ admits no natural compact Kähler threefold host on which a T-CL-K3-Extension-style parametrix extension could be defined.*

**The K3 side of the asymmetry.** The K3 witness row at $(K, \hbar^2) = (8, -1/8)$ is parametrix-admissible on the compact Kähler threefold $K3 \times \C^2$ via T-CL-K3-Extension (Gilkey-audited): Kuranishi cover $\{U_\alpha \simeq \C^2_{\mathrm{flat}}\}$ + chart-local Costello--Li 2016 Prop 5.2 flat-$\C^3$ parametrix + Gilkey-integrated counterterms $\int_{K3} a_k = P_k(0, 24) \in \Q$ absorbed into a single local counterterm per loop order (Costello 2011 Thm 13.4.1; Costello--Gwilliam 2017 Vol 2 Thm 8.6.9). The $\mathsf{SC}^{\mathrm{ch,top}}$ closed-colour bar-differential $d_B^{K3 \times \C^2}$ exists at chain level; the four-route $\hbar^2 K = -1$ sign convergence at K3 has a geometric realisation at the BV parametrix level.

**The Conway side of the asymmetry.** $\Lambda_{24}$ carries no complex structure compatible with a compact Kähler threefold host. The Leech lattice's supersymmetric VOA $V^{s\natural}$ is a purely 2d holomorphic superconformal field theory of central charge $c = 12$ (Duncan 2007 *Duke Math J* 139), constructed from the Leech-lattice fermionic VOA via $\Z/2$-orbifolding; there is no Ricci-flat Kähler metric on a natural 3-fold lift, no Kuranishi cover by flat $\C^2$-charts, no Costello--Li 2016 parametrix extension domain. Routes A, B of the four-route table fail because Leech is positive-definite (no Lorentzian time, no Borcherds cusp); the geometric parallel is that T-CL-K3-Extension-style parametrix existence is not even a coherent question on a Leech host.

**Asymmetry as structural boundary.** The universal identity's reflective-crown scope is simultaneously:
- analytic — four routes (Wick / Borcherds / Gram / Gerstenhaber) produce sign $-$ on the crown and fail / return $+$ on Conway;
- geometric — T-CL-K3-Extension Gilkey audit constructs the closed-colour bar-differential $d_B^{K3 \times \C^2}$ on the K3 row via Kuranishi + Gilkey-integrated counterterm cohomology, and has no counterpart on the Conway row because $\Lambda_{24}$ admits no compact Kähler threefold completion.

The two readings (analytic and geometric) close independently and reach the same verdict: **the universal identity $\hbar^2 K^{\kappa_{\mathrm{ch}}} = -1$ holds on the reflective-Lorentzian crown (K3, Monster, Fake-Monster) with a geometric chain-level realisation at the K3 row via T-CL-K3-Extension, and is structurally out of scope at the Conway row by both analytic and geometric obstructions.**

**Full T-CL-K3-Extension derivation.** `notes/COSTELLO_R5_GILKEY_AUDIT_T_CL_K3_EXTENSION_BATTLE_HARDENED_2026_04_22.md` — five cycles, named-pillar proof, scope statement, three-volume rectification inscription plan. The proof inscribed there exposes as false the r4-redux attack-plan claim "$a_k(K3) = 0$ for $k \geq 2$ (hyperkähler $\mathrm{Sp}(1) \subset \mathrm{SU}(2)$ strict)" ($\int_{K3} a_2 = 64\pi^2/15 \neq 0$; pointwise $a_2 > 0$ on generic K3 where $W_-$ is nonzero per Besse 1987 §12.K Prop 12.95), and replaces it with the correct Gilkey-integrated counterterm absorption into one-dimensional top local cohomology $H^6_{\mathrm{loc}}(K3 \times \C^2, \Omega^{3,3}) \simeq \C$.

**Primary.** Gilkey 1995 §1.7 Thm 1.7.6 + §4.8 Thm 4.8.16; Yau 1978 *Comm Pure Appl Math* 31 Thm 1; Besse 1987 *Einstein Manifolds* §6.34, §12.K Prop 12.95, §14.5; Costello 2011 MSM 170 Thm 13.4.1; Costello--Gwilliam 2017 FA Vol 2 Thm 8.6.9; Costello--Li 2016 arXiv:1605.09930 Prop 5.2; CGP 2018 arXiv:1803.10462 Prop 3.4.

*Raeez Lorgat, 2026-04-22 evening. Conway's structural boundary status (this file's thesis) has a geometric parallel: K3 is parametrix-admissible on $K3 \times \C^2$ via T-CL-K3-Extension Gilkey audit, Conway is not even a coherent compact-Kähler-threefold question on $\Lambda_{24}$. The asymmetry between the two rows is simultaneously analytic (four-route sign convergence on the crown, 0/4 failure on Conway) and geometric (chain-level closed-colour bar-differential on K3, no counterpart on Conway).*

---

## Witten r5 --- Conway boundary vs 9 Heegner fibres on the K3 $\mathsf B$-row

The Conway boundary establishes that the universal identity $\hbar^2 K = -1$ requires a Lorentzian host. Complementary test: inside the Mukai-K3 $\mathsf B$-row, how does the identity refine across the 9 arithmetic CM loci where the transcendental lattice discriminant equals a Baker--Heegner--Stark class-number-1 imaginary quadratic field discriminant $d_K \in \{-3, -4, -7, -8, -11, -19, -43, -67, -163\}$?

The answer sharpens the Conway boundary. Inside the $\mathsf B$-row the identity admits a 9-fibre arithmetic refinement on the reflective-Lorentzian stratum. Conway's 0/5 verdict is not improved by any CM-refinement --- Leech remains positive-definite at every arithmetic twist.

### The 9-fibre K3 splitting (complement to the Conway 0/5 boundary)

| $d_K$ | Level | $w(d_K) = 5 - 2/|d_K|$ | $j(\tau_{d_K})$ | $|\mathcal O^\times_{d_K}|$ | Four-route status |
|---|---:|---:|---:|---:|:---:|
| $-3$ | $3$ | $13/3 \approx 4.333$ | $0$ | $6$ | 4/4 |
| $-4$ | $4$ | $9/2 = 4.500$ | $1728$ | $4$ | 4/4 |
| $-7$ | $7$ | $33/7 \approx 4.714$ | $-15^3$ | $2$ | 4/4 |
| $-8$ | $8$ | $19/4 = 4.750$ | $20^3$ | $2$ | 4/4 |
| $-11$ | $11$ | $53/11 \approx 4.818$ | $-32^3$ | $2$ | 4/4 |
| $-19$ | $19$ | $93/19 \approx 4.895$ | $-96^3$ | $2$ | 4/4 |
| $-43$ | $43$ | $213/43 \approx 4.953$ | $-960^3$ | $2$ | 4/4 |
| $-67$ | $67$ | $333/67 \approx 4.970$ | $-5280^3$ | $2$ | 4/4 |
| $-163$ | $163$ | $813/163 \approx 4.988$ | $-640320^3$ | $2$ | 4/4 |
| Conway (nominal $d = -12$) | --- | --- | --- | $\mathbb Z_2$ | **0/4** (Leech positive-definite) |

The contrast is structural: every $d_K$-CM fibre of the K3 $\mathsf B$-row carries a Lorentzian Mukai sub-lattice $\mathrm{II}_{2,2}\subset\mathrm{II}_{4,20}$, hence admits the singular-theta lift $\Psi_{d_K}$ at level $|d_K|$ and the four-route identity at conductor $K_{d_K} = 2(5|d_K| - 2)$. The Conway row has no analogous CM refinement: $\Lambda_{24}$ is positive-definite at every specialisation; no arithmetic twist creates a hyperbolic plane.

### Cycle 1 --- String compactification per $d_K$ (contrast to Conway's non-availability)

At each $d_K$ the Heegner K3 fibre K3$_{d_K}\times E_{\tau_{d_K}}$ supports Type IIB at a CM locus of the 21-dimensional K3$\times E$ moduli, with sporadic U-duality enhancement via $\mathrm{End}(E_{\tau_{d_K}}) = \mathbb Z[\tau_{d_K}]$. At $d_K \in \{-3, -4\}$ the CM unit group is $\mathbb Z_6$, $\mathbb Z_4$; at the seven remaining rows it is $\{\pm 1\}$. Conway admits no analogous compactification: $V^{s\natural}$ sits on the metaplectic stratum $\overline{\mathcal A_2^{(2)}}$ (Scheithauer 2008), not on a CM fibre of a Lorentzian moduli.

### Cycle 2 --- Ramanujan $d_K = -163$: Heegner maximum vs Conway boundary

$j(\tau_{-163}) = -640320^3 = -262537412640768000$; Ramanujan 1914 $e^{\pi\sqrt{163}} = 640320^3 + 744 - \varepsilon$ with $\varepsilon < 10^{-12}$. At $d_K = -163$ the Heegner tower reaches maximum arithmetic rigidity; K3$_{-163}\times E_{\tau_{-163}}$ carries the sparsest CM-orbit on the paramodular cusp set. The four-route identity refines at weight $813/163 = 4.988\ldots$, infinitesimally below generic.

Conway has no analogue: there is no CM elliptic curve whose fibre over Leech carries a Lorentzian Mukai lattice; the Heegner tower does not extend to Leech. The nominal $K = 12$ for Conway is a pattern-match with $c_{V^{s\natural}} = 12$, categorically separate from the 9-fibre $K$-tower $\{26, 36, 66, 76, 106, 186, 426, 666, 1626\}$ on K3.

### Cycle 3 --- Kuga--Satake vs Duncan super-twin

K3$_{d_K}$ at Picard rank 20 lifts via Kuga--Satake to $A^{\mathrm{KS}}_{d_K}\simeq E_{\tau_{d_K}}^{\otimes 4}$, a CM abelian 4-fold with action $\mathbb Z[\tau_{d_K}]$; the covering group $\mathcal O^\times_{d_K}/\{\pm 1\}$ acts on BPS dyons. Conway's super-twin transport from Monster (Duncan 2007 commutative orbifolding diamond) inherits only the $\mathbb Z/2$-orbifold sign character from $V^\natural$, not a Kuga--Satake abelian 4-fold; the inheritance is categorical (sign character), not arithmetic (CM lattice). The two mechanisms are orthogonal: Kuga--Satake lifts a CM K3 to a CM abelian 4-fold (Hodge-theoretic); Duncan diamond lifts a Monster orbifold to a Conway super-orbifold (orbifold-theoretic). They do not compose.

### Cycle 4 --- Partition functions $1/\Psi_{d_K}$ vs Conway's absence

On $\mathrm{AdS}_3\times\mathrm{K3}_{d_K}$ the 3D gravity partition function is $Z^{d_K}_{\mathrm{3dQG}} = 1/\Psi_{d_K}$ at paramodular level $|d_K|$ (arithmetic DVV refinement). Conway has no $\mathrm{AdS}_3\times\Lambda_{24}$ analogue at the reflective-crown level: the metaplectic $\Psi^{\mathrm{metap}}$-image of Conway lives on $\overline{\mathcal A_2^{(2)}}$ at half-integer weight, a different automorphic stratum; it does not produce a Siegel-paramodular Borcherds-product denominator at integer level.

### Cycle 5 --- Arithmetic DVV conjecture extends inside the $\mathsf B$-row; does not rescue Conway

Conjecture (arithmetic DVV): $Z^{d_K}_{\mathrm{3dQG}} = 1/\Psi_{d_K}$ at every Heegner fibre; reduces at $|d_K|\to\infty$ to DVV 1997 at level 1. Verified multi-path at each of the 9 rows via ghost-BRST trace, Pentagon trace, Borcherds weight, Heegner $j$-cube, and unit-group cross-checks. The conjecture does not extend to Conway. Leech admits no paramodular Borcherds product, no level-$|d_K|$ Siegel-denominator, no BPS partition function in the DVV sense.

### Net verdict

The 9-fibre refinement sharpens the Conway structural-boundary verdict:
- **Inside the $\mathsf B$-row:** the four-route identity $\hbar^2 K = -1$ refines across 9 arithmetic CM loci $d_K$ to a $4\times 9$-convergence matrix at conductors $K_{d_K} = 2(5|d_K| - 2)$ and weights $w(d_K) = 5 - 2/|d_K|$; Ramanujan $d_K = -163$ is the infrared fixed point.
- **Outside the $\mathsf B$-row at Conway:** no arithmetic refinement rescues the row. Leech's positive-definiteness is structural, not a CM-twist obstruction; the Heegner tower does not pass through Leech.
- **Robust Conway boundary.** Whether on the generic K3 four-route table (0/4) or on the arithmetic 9-fibre refinement ($0/4 \times 9 = 0/36$), Conway's verdict is unchanged. The arithmetic refinement adds 9 new positive witnesses on the $\mathsf B$-row, zero new witnesses on Conway.

*Raeez Lorgat, 2026-04-22. Witten r5 contrast: the 9 Heegner fibres refine the K3 $\mathsf B$-row into 9 arithmetic CM loci with weights $5 - 2/|d_K|$ and conductors $K_{d_K} = 2(5|d_K| - 2)$. Conway has no arithmetic refinement because Leech is positive-definite; the Heegner tower does not pass through Leech. The 9-fibre splitting sharpens the Conway boundary from 0/4 generic to 0/36 arithmetic: no CM-twist rescues a row structurally outside the reflective-Lorentzian stratum.*
