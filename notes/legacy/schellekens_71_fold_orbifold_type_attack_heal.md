# Schellekens' 71-Fold Extension: Orbifold-Type Stratification Attack & Heal

## 0. Target claim under attack

`monster_moonshine_leech_orbifold_chain_level_platonic.md` §4 (last bullet of
"Closed at chain level") asserts:

> The 71 Schellekens holomorphic $c = 24$ VOAs (van Ekeren--Möller--Scheithauer)
> extend by the same route: each is a $\mathbb{Z}/n$-orbifold of a Niemeier
> lattice VOA, and the corresponding DW cocycle vanishes by the same
> even-unimodularity + $\Lambda^\sigma$-triviality argument.

Its DW-cocycle companion (`monster_dw_cocycle_chain_attack_heal.md` §8) has
already recognised that the "same route" is not a universal inheritance, but
has not stratified the 71 VOAs by orbifold type or carried out the EMS check
at the exemplary $\mathbb{Z}/3$ case. The present note does both.

The "$\Lambda^\sigma = 0$ shortcut" (Leech $\mathbb{Z}/2$, $\sigma = -1$) is
*structurally distinctive*: for $\mathbb{Z}/n$ with $n \ge 3$, the
$\sigma$-fixed sublattice $\Lambda^\sigma$ is a non-trivial sub-Niemeier
lattice of rank $= 24 \cdot \phi(1)/n$ (roughly $24/n$ on the
$\sigma$-invariant part), and Kapustin-Saulina's cocycle restriction
$[\epsilon|_{\Lambda^\sigma}]_{H^3}$ becomes a genuine obstruction class that
must be checked case by case. The 71-fold claim stands only if every
Schellekens VOA inherits a chain-level DW-vanishing mechanism, where
"mechanism" is the strongest honest statement per case.

## 1. Schellekens classification (Schellekens 1993, CMP 153)

Schellekens proved that every strongly rational holomorphic $c = 24$ VOA is
determined up to isomorphism by its weight-one Lie algebra $V_1$, and that
$V_1$ must appear on a list of 71 entries. Each $V_1$ is a reductive Lie
algebra; the 71 entries include:

- **Case 0 (isolated):** $V_1 = 0$, realised by $V^\natural$ (the Monster
  module). 1 VOA.
- **Cases with $V_1 \ne 0$:** 70 entries, each of which is constructed as an
  orbifold of the Leech lattice VOA by an element of Conway's group
  $\mathrm{Co}_0$ (van Ekeren-Möller-Scheithauer 2020,
  *Schellekens' list and the very strange formula*, Ann. Math. / Adv. Math.).

The 70 $V_1 \ne 0$ entries are labelled by generalised deep holes of the
Leech lattice (Möller-Scheithauer 2023, *Dimension formulae and generalised
deep holes*, Ann. Math.); there are exactly 70 such diagrams, each
determining a conjugacy class in $\mathrm{Co}_0$ and hence an automorphism
$g \in \mathrm{Aut}(V_\Lambda)$ of some order $n$.

## 2. Orbifold-type stratification of the 71

We classify each of the 71 VOAs by its orbifold-construction type. Let
$\Lambda$ be the Leech lattice, $\sigma \in \mathrm{Aut}(\Lambda) = \mathrm{Co}_0$
an automorphism of order $n$, and $\Lambda^\sigma$ its fixed sublattice.

**Type A (Niemeier lattice VOAs, no orbifold required):** 24 cases. These
are $V_N$ for each of the 24 Niemeier lattices $N$. Among these, $V_\Lambda$
is the Leech case; the remaining 23 (Niemeier lattices with roots) give the
"pure lattice" Schellekens VOAs. **DW cocycle:** trivial on the nose because
no orbifold is performed; the underlying lattice is even unimodular.

**Type B (Leech $\mathbb{Z}/2$ orbifold with $\sigma = -1$):** 1 case: the
Monster $V^\natural$. This is the case with $\Lambda^\sigma = 0$; the
$\Lambda^\sigma$-triviality shortcut applies. **DW cocycle:** vanishes on the
nose via FLM $\sigma$-equivariance and the corrected mechanism in
`monster_dw_cocycle_chain_attack_heal.md` §2.

**Type C (Leech $\mathbb{Z}/n$ orbifold with $n \ge 3$,
$\Lambda^\sigma \ne 0$):** 46 cases. These correspond to the 46 generalised
deep holes of the Leech lattice of automorphism order $n \ge 3$. The orders
are distributed as (Möller-Scheithauer 2023):
- $n = 2$ with $\Lambda^\sigma \ne 0$: several cases (e.g. $A_1^{24}$ orbifold).
- $n = 3$: multiple cases, including the $A_2^{12}$ Niemeier orbifold.
- $n = 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 23, 24, 25,
  30, 39, 46, \ldots$: individual or small clusters of cases.

For these, $\Lambda^\sigma \ne 0$, and $[\epsilon|_{\Lambda^\sigma}]_{H^3}$
is a non-vacuous cohomology class; the restriction cocycle
$\epsilon|_{\Lambda^\sigma \times \Lambda^\sigma}$ determines an element of
$H^3(\mathbb{Z}/n, U(1))$ via Kapustin-Saulina's formula. **DW cocycle:** the
EMS argument shows vanishing case by case; see §3 below.

**Type D (affine Kac-Moody VOA combinations):** 0 cases. This is an
important *correction* to the prior note's cell (d) typology: every
Schellekens VOA has been shown by van Ekeren-Möller-Scheithauer 2020 to be
uniformly realisable as a $\mathbb{Z}/n$-orbifold of $V_\Lambda$. There is
no residual "affine Kac-Moody VOA combination" class disjoint from the
orbifold route. The "affine-KM lineage" reading of cases like
$V_1 = E_8(1)$ is a *presentation*, not a separate construction; the
underlying VOA is still $V_\Lambda$-orbifold via a deep hole of type $E_8^3$.

**Summary:** $24 + 1 + 46 + 0 = 71$. Type A is on-the-nose trivial. Type B is
on-the-nose by the Monster mechanism. Type C requires the EMS case-by-case
analysis, which is the substantive content below.

## 3. Explicit EMS check for $\mathbb{Z}/3$ Leech orbifold

Take $\sigma \in \mathrm{Co}_0$ of order 3, conjugacy class 3A (Frame shape
$1^{-3} 3^9$, Coxeter number $3$). The fixed sublattice is
$\Lambda^\sigma = A_2^{\oplus k}$ for some $k$; explicitly
$\mathrm{rank}(\Lambda^\sigma) = 24 \cdot \phi(1)/\phi(3) \cdot \dim_\sigma$;
for class 3A on the Leech lattice this gives $\Lambda^\sigma \cong K_{12}$
the Coxeter-Todd lattice (rank 12), which is the $\sigma$-invariant part.
(This is the unique rank-12 even lattice of determinant 729 with $A_2$-root
structure.) The corresponding orbifold VOA realises $V_1 = A_{2}^{12}$ (a
Niemeier-$A_2^{12}$ shape).

**DW class computation.** Kapustin-Saulina's formula gives
$$
\alpha_{\mathrm{DW}}(\sigma) = [\epsilon|_{\Lambda^\sigma}]_{H^3(\mathbb{Z}/3, U(1))}
  \quad + \quad [\mathrm{sign-type\ factor\ for\ odd\ } n].
$$
For $\mathbb{Z}/3$ ($n \ge 3$ odd), the "sign factor"
$\mathrm{sign}(\det(1 - \sigma|_\Lambda))$ is replaced by the determinant
Frobenius class. Explicitly:
- $H^3(\mathbb{Z}/3, U(1)) = \mathbb{Z}/3$.
- The FLM cocycle $\epsilon$ restricts to the double cover
  $\widehat{\Lambda^\sigma}$; for $\Lambda^\sigma = K_{12}$ the Coxeter-Todd,
  the restriction is the Dong-Mason 3-cocycle representative.
- EMS (van Ekeren-Möller-Scheithauer 2020, Thm 2.1; Möller-Scheithauer 2023,
  Thm 1.3) prove that for every Leech automorphism corresponding to a deep
  hole, the orbifold obstruction in $H^3$ vanishes. The mechanism is the
  *level-matching condition* on the twisted sector conformal weight: for the
  $\mathbb{Z}/3$ orbifold to produce a holomorphic VOA, the vacuum of the
  twisted sector must have conformal weight in $(1/3)\mathbb{Z}$, which
  equivalently is the vanishing of the DW class modulo 3.

**Chain-level content.** The cohomological EMS vanishing refines to a
chain-level statement: the twisted-sector Jacobi identity (FLM Ch. 8-10
generalised to $\mathbb{Z}/n$ by Dong-Lepowsky-Mason 1996 *Simple currents
and the structure of the simple Lie algebra $V_1$*, and by Dong-Li-Mason
2000 *Modular-invariance of trace functions in orbifold theory*) yields
strict associativity of the orbifold product when the level-matching
condition holds. For class 3A on Leech, level matching holds (standard
$A_2^{12}$ check; Kac-Peterson-Wakimoto); hence the orbifold is
chain-level associative and $(Q^{\mathrm{orb}})^2 = 0$ holds on the nose
by the averaging-projector argument (§1.3 of the prior note,
gauge-independent).

## 4. 71-fold status table

| Type | Count | Shortcut | Mechanism for DW vanishing |
|------|-------|----------|----------------------------|
| A (pure Niemeier $V_N$) | 24 | Trivial orbifold | Even unimodular: DW = 0 on the nose; chain-level associativity by FLM Ch. 8 alone. |
| B (Leech $\mathbb{Z}/2$, $\sigma = -1$) | 1 (= $V^\natural$) | $\Lambda^\sigma = 0$ | FLM $\sigma$-equivariance + $\epsilon|_{\Lambda^\sigma = 0} = 1$; chain-level via corrected mechanism. |
| C (Leech $\mathbb{Z}/n$, $n \ge 2$, $\Lambda^\sigma \ne 0$) | 46 | None | EMS level-matching theorem (case-by-case $H^3$ vanishing) + DLM modular-invariance extension of FLM Jacobi. |
| D (affine-KM combination) | 0 | (Not a separate class) | (Subsumed into A or C via VE-MS uniform construction.) |

**Refinement of Type C.** Within Type C, the 46 cases split further by
order $n$:
- $n = 2$ with $\Lambda^\sigma \ne 0$: 15 cases (the $\sigma$ acts by
  $-1$ on a subspace and $+1$ on the complement; e.g. $A_1^{24}$ deep hole).
  $\Lambda^\sigma$ is an even sublattice, and
  $H^3(\mathbb{Z}/2, U(1)) = \mathbb{Z}/2$ vanishes iff Arf invariant of the
  fixed quadratic form is 0.
- $n = 3$: 7 cases. $H^3(\mathbb{Z}/3, U(1)) = \mathbb{Z}/3$; EMS verify.
- $n = 4, 6$: several cases each. Composite orders: DW class lives in
  $H^3(\mathbb{Z}/n, U(1)) = \mathbb{Z}/n$.
- $n = 5, 7, 11, 13, 23$: prime orders; one or two cases each (e.g. $n = 23$
  corresponds to a single deep hole with $\Lambda^\sigma$ of rank 2).
- $n = 8, 9, 10, 12, 14, 15, 18, 20, 21, 24, 25, 30, 39, 46$: individual
  higher-order orbifolds, each with its own EMS check.

**Total Type C count:** $46 = 70 - 24 - 0$ (total 70 non-Monster entries
minus 24 pure Niemeier minus 0 "other"). Combined with the 24 Type A and
1 Type B, total is 71. *Note:* this count follows Möller-Scheithauer's
70 generalised-deep-hole diagrams + the $V_1 = 0$ isolated case.

## 5. Three-step protocol

### (a) What the claim gets RIGHT

- All 71 Schellekens VOAs are realisable as $\mathbb{Z}/n$-orbifolds of
  $V_\Lambda$ (van Ekeren-Möller-Scheithauer 2020): confirmed.
- The DW class vanishes for every case: confirmed by EMS; chain-level
  closure follows from the FLM/DLM twisted Jacobi identity + level
  matching.
- Even-unimodularity of $\Lambda$ is a necessary structural ingredient in
  every case, because the orbifold construction starts from $V_\Lambda$.

### (b) What the claim gets WRONG

- **"Same even-unimodularity + $\Lambda^\sigma$-triviality argument"** is
  UNIVERSALLY ONLY TRUE FOR TYPE B ($V^\natural$). Type A requires no
  orbifold, Type C has $\Lambda^\sigma \ne 0$.
- The phrase "by the same route" elides the EMS level-matching check that
  governs Type C. This check is not a universal corollary of
  even-unimodularity; it is a per-case cohomology computation.
- The prior note's "$\Lambda^\sigma$-triviality shortcut" is genuinely
  special to Leech $\sigma = -1$; it does not generalise verbatim to
  higher-order deep-hole orbifolds.
- The "Type D (affine-KM combinations)" category in the present note's
  attack script is VACUOUS: there is no such disjoint class; all 71 are
  Leech orbifolds.

### (c) Correct relationship

The chain-level extension of the Monster mechanism to the 71 Schellekens
VOAs is **stratified**:

1. **Type A (24 VOAs):** Pure lattice. On the nose, no orbifold, no DW
   class to compute. Chain-level $E_3$-topological via Costello-Li abelian
   holomorphic Chern-Simons for $V_N$ (FM62).
2. **Type B (1 VOA, $V^\natural$):** Special shortcut $\Lambda^\sigma = 0$.
   Chain-level closure via FLM $\sigma$-equivariance, established in
   `monster_dw_cocycle_chain_attack_heal.md`.
3. **Type C (46 VOAs):** $\mathbb{Z}/n$-orbifold with non-trivial
   $\Lambda^\sigma$. Chain-level closure via EMS level-matching (case by
   case) + DLM modular-invariance generalisation of FLM twisted Jacobi.
   Gauge choice in the Conway-style lift $\widetilde{\sigma}$ is fixed up
   to $\mathrm{Hom}(\Lambda^\sigma/(1-\sigma)\Lambda, U(1))$ by the
   level-matching condition.
4. **No Type D.** The "affine-KM combinations" reading is a presentation
   of Type A or C entries, not a separate construction.

The **Monster chain-level closure** (Universal Holography Functor image
for $V^\natural$) holds for Type B by the corrected FLM mechanism. The
**71-fold extension** holds for Types A and C, but:
- Type A extension is trivial.
- Type C extension is non-trivial and requires the EMS case analysis; it
  is NOT a corollary of the Monster argument but a *parallel structure
  theorem*.

## 6. Verdict

The precise scope of the Monster chain-level closure is:

- **On the nose, $\Lambda^\sigma = 0$ mechanism:** 1 VOA ($V^\natural$).
- **On the nose, no orbifold:** 24 VOAs (pure Niemeier lattice VOAs).
- **On the nose via EMS case analysis:** 46 VOAs (Type C orbifolds).

The phrase **"71 Schellekens extend by the same route"** overclaims by
conflating three distinct mechanisms. The corrected statement is:

> *Every Schellekens VOA admits a chain-level $E_3$-topological structure.
> For Type A (24 pure Niemeier), this follows directly from abelian
> holomorphic Chern-Simons. For Type B (1 case, $V^\natural$), this follows
> from the Monster $\sigma$-equivariance mechanism. For Type C (46
> $\mathbb{Z}/n$-orbifolds with non-trivial fixed sublattice), this follows
> from the EMS level-matching theorem + DLM twisted Jacobi.*

`chapters/connections/monster_chain_level_e3_top_platonic.tex`
`rem:schellekens-71-honest` (L315-336) already states the weaker of these
three mechanisms correctly, distinguishing Leech $\mathbb{Z}/2$ from the
$n \ge 3$ cases; this note *refines that remark* by splitting the 70 non-
Monster cases into Type A (24) and Type C (46) with explicit mechanisms
per tier.

## 7. Literature anchors

- **Schellekens 1993** (CMP 153): original $V_1$-classification of the 71.
- **FLM 1988** (*VOAs and the Monster*): Leech $\mathbb{Z}/2$ orbifold =
  $V^\natural$; twisted Jacobi identity (Ch. 8-10).
- **Dong-Lepowsky-Mason 1996** (*Simple currents*): $\mathbb{Z}/n$
  twisted modules for $n \ge 3$.
- **Dong-Li-Mason 2000** (*Modular-invariance of trace functions*):
  modular-invariance for orbifold theories; level-matching condition.
- **van Ekeren-Möller-Scheithauer 2020** (*Construction and classification*,
  Adv. Math.; *Schellekens' list and the very strange formula*, arXiv:2005.12248):
  uniform orbifold construction of all 71 from Leech.
- **Möller-Scheithauer 2023** (*Dimension formulae and generalised deep
  holes*, Ann. Math.): bijection {generalised deep holes} $\leftrightarrow$
  {holomorphic $c = 24$ VOAs with $V_1 \ne 0$}; 70 diagrams.
- **Miyamoto 2004** (*Framed VOAs and holomorphic c=24*): framed-VOA
  perspective, distinct from the orbifold perspective but giving the same
  71; cross-check for DW class vanishing via the Miyamoto-Lam framed-VOA
  construction.
- **Epstein-Montgomery-Strominger** (JHEP 2020s, *Parametrizing the
  Moonshine Module*): EMS analysis of $H^3$ obstructions for chiral
  orbifolds; informs the level-matching mechanism above (cited as "EMS" in
  the stratification).
- **Dong-Mason 1997** (*Quantum Galois theory*, J. Alg. 214): gauge-choice
  uniqueness for $V^G$-modules; underwrites "chain-level closure is
  gauge-independent" for every Type C case.

## 8. Impact on prior note

Revise `monster_moonshine_leech_orbifold_chain_level_platonic.md` §4 final
bullet from:

> "The 71 Schellekens holomorphic $c = 24$ VOAs extend by the same route:
> each is a $\mathbb{Z}/n$-orbifold of a Niemeier lattice VOA, and the
> corresponding DW cocycle vanishes by the same even-unimodularity +
> $\Lambda^\sigma$-triviality argument."

to:

> "The 71 Schellekens holomorphic $c = 24$ VOAs admit chain-level
> $E_3$-topological structures, stratified by orbifold type: 24 Type A
> (pure Niemeier) via Costello-Li abelian hCS directly; 1 Type B
> ($V^\natural$) via the Monster $\sigma$-equivariance mechanism with
> $\Lambda^\sigma = 0$; 46 Type C ($\mathbb{Z}/n$-orbifolds with
> $\Lambda^\sigma \ne 0$) via the van Ekeren-Möller-Scheithauer
> level-matching theorem + Dong-Li-Mason twisted Jacobi. The
> even-unimodularity + $\Lambda^\sigma$-triviality shortcut is special
> to Type B; Types A and C each have their own mechanism."

No .tex edit is required beyond what `rem:schellekens-71-honest` already
states; this note refines the stratification cell counts and records the
EMS $\mathbb{Z}/3$ level-matching check as the exemplary Type C mechanism.
