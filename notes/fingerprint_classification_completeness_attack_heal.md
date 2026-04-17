# Fingerprint Classification Completeness: Attack and Heal

**Subject.** Vol II Theorem G (Infinite Fingerprint Classification), canonical fingerprint
$\varphi(A) = (p_{\max}, r_{\max}, \chi_{\mathrm{VOA}}, n_{\mathrm{strong}}, \mathrm{coset})$
of a chirally Koszul algebra $A$. Claim (statement in `CLAUDE.md` line 770;
theorem `thm:fingerprint-completeness-conditional` in
`chapters/examples/examples-complete-proved.tex:1017`): the five-slot
fingerprint is a COMPLETE invariant of the Koszul-bar-complex structure on
the standard landscape.

**Attack lens.** Russian school (Feigin--Frenkel, Arakawa, Creutzig--Kanade--McRae)
+ Chriss--Ginzburg (fingerprint as "KL basis" over the Steinberg variety
$\overline{\mathcal M}_{g,n}^{\mathrm{fam}}$) + Miyamoto (modular-invariance
as independent data).

---

## I. Attack: three classes of candidate collisions

### (1) Within-family level collisions: $V_k(\mathfrak g)$ and $V_{k'}(\mathfrak g)$ with same $c(k)$, different $k$

The affine central charge $c_k(\mathfrak g) = k\dim\mathfrak g / (k + h^\vee)$ is
a RATIONAL function of $k$. At generic $k$ the map $k \mapsto c_k$ is
2-to-1 (except for $k = h^\vee(\dim\mathfrak g - 1)/(\dim\mathfrak g - c_k - 1)$
branch points): for each central charge, two distinct levels realize it.

- For $\mathfrak{sl}_2$: $c_k = 3k/(k+2)$. Solving for $k$ given $c$: $k = 2c/(3-c)$.
  This map is 1-to-1 so $\mathfrak{sl}_2$ escapes this collision.
- For $\mathfrak{sl}_N$, $N \ge 3$: $c_k = k(N^2-1)/(k+N)$ inverts as
  $k = Nc/(N^2-1-c)$, still 1-to-1 in $k$.
- But: if one relaxes to the FULL landscape, $V_1(\mathfrak{sl}_N)$ and the
  $\mathcal W$-algebra $W_{k'}(\mathfrak g')$ for some different $\mathfrak g'$
  at level $k'$ can share $c$, $p_{\max}$, and even $n_{\mathrm{strong}}$.
  The `coset` slot is the separating datum. **Verdict: within pure affine family, level is recovered from coset.**

### (2) Coincident-fingerprint pairs across DS transport

$V_k(\mathfrak{sl}_2)$ and $\mathrm{Vir}_{c(k)} = \mathrm{DS}(V_k(\mathfrak{sl}_2))$
have different $n_{\mathrm{strong}}$ (3 vs 1) and different $p_{\max}$ (2 vs 4).
**No collision.** DS transport acts nontrivially on each of four slots
(Vol II CLAUDE.md FM108 heal, slot-wise action theorem).

### (3) CRITICAL CANDIDATE COLLISION: triplet $W(2)$ vs singlet $M(2)$ vs lattice $V_{\sqrt{2}A_1}$

Adamovi\'c--Milas triplet $W(2)$ is the $\mathbb Z_2$-orbifold of the rank-1 lattice VOA
$V_{\sqrt{2}\mathbb Z}$; it shares central charge $c = -2$ with its $\mathbb Z_2$-sibling
singlet $M(2)$ and with the lattice itself. Comparison of fingerprints (to the
extent the five slots are defined outside the standard landscape):

| slot | $V_{\sqrt{2}\mathbb Z}$ | $W(2)$ triplet | $M(2)$ singlet |
|------|----------|-------|-------|
| $p_{\max}$ | $2$ | $2$ | $2$ |
| $r_{\max}$ | $2$ (class G) | $\infty$ (class M, logarithmic) | $\infty$ (class M) |
| $\chi_{\mathrm{VOA}}$ | even | even ($\mathbb Z_2$-invariants) | even |
| $n_{\mathrm{strong}}$ | $3$ | $4$ | $2$ |
| coset | trivial (abelian) | Vir at $c = -2$ | Vir at $c = -2$ |

So triplet vs singlet ALREADY differ on $n_{\mathrm{strong}}$ (4 vs 2), AND
the lattice itself is a $r_{\max}$-distinct class from its orbifold. So
these three are NOT a fingerprint collision — but the manuscript warns
(`examples-complete-proved.tex:1079-1091`) that $W(p)$'s FREE strong
generation is not proved (V1-AP67), so $n_{\mathrm{strong}}$ is only
a candidate invariant there.

### (4) The real collision: BILINEAR $\beta\gamma$ vs $bc$ at same central charge

Symplectic boson $\beta\gamma$ ($c = 2$, even parity) and the charged $(b,c)$
ghost system with the same $c = 2$ (odd parity, with $h_b + h_c = 1$):

| slot | $\beta\gamma$ | $bc$ (tuned to $c=2$) |
|------|------|------|
| $p_{\max}$ | $1$ | $1$ |
| $r_{\max}$ | $2$ (class G; tower trivial) | $2$ (class G) |
| $\chi_{\mathrm{VOA}}$ | $+$ (even) | $-$ (odd) |
| $n_{\mathrm{strong}}$ | $2$ | $2$ |
| coset | Sp$(2)$ | OSp$(1|2)$ |

FM106 already names this case: $\chi_{\mathrm{VOA}}$ SIGN + coset structure
$\mathrm{Sp}$ vs $\mathrm{OSp}$ do separate them. **Heal successful.**

### (5) THE HIDDEN COLLISION: level $k$ vs $k'$ outside affine families

Two abelian Heisenberg algebras $\mathcal H_k$ and $\mathcal H_{k'}$
at levels $k \ne k'$ both have $p_{\max} = 2$ (double OPE pole), $r_{\max} = 2$,
$\chi_{\mathrm{VOA}} = +$, $n_{\mathrm{strong}} = 1$ (single field $\alpha(z)$),
coset trivial. **Fingerprint is IDENTICAL**.

But $\mathcal H_k$ and $\mathcal H_{k'}$ are NOT isomorphic as chiral algebras:
their R-matrices differ ($R_k(z) = \exp(k\hbar/z)$ vs $R_{k'}(z) = \exp(k'\hbar/z)$,
V2-AP7), their bar complexes carry DIFFERENT curvatures
$d_B^2 = \kappa_{\mathrm{ch}} \cdot \omega_g$ with $\kappa_{\mathrm{ch}} = k$
(AP39). **This is a genuine collision.**

The level $k$ is a Koszul-bar-complex invariant not captured by the five slots.
It is the "central extension class" of the Lie coalgebra $B(\mathcal H_k)$,
equivalently the first Chern class of the Kac--Moody central extension.

---

## II. What the 5-slot fingerprint gets RIGHT

- $r_{\max}$ captures shadow-depth stratification (FM105/FM107/FM110).
- $\chi_{\mathrm{VOA}}$ separates symplectic boson from fermion (FM106).
- Coset resolves GKO-style decompositions (Arakawa--Creutzig--Linshaw
  coset theorems install this as `thm:coset-conformal-inheritance`).
- $n_{\mathrm{strong}}$ resolves triplet/singlet/lattice triple in $W(p)$
  lineage IF free strong generation is independently proved.
- Quaternitomy $G/L/C/M$ recovered as coarse projection is CORRECT.

## III. What it gets WRONG (6th slot needed)

- **Level $k$** (equivalently $\kappa_{\mathrm{ch}}(A)$, the
  central-extension/curvature class) is NOT functorially recoverable from
  the other five slots.
- The collision in (5) above is not a marginal case: it is generic within
  the standard landscape. Every Heisenberg and every affine Kac-Moody level
  witness a continuous family of non-isomorphic chiral algebras sharing the
  same fingerprint.
- Worse: the R-matrix gauge class (MO dynamical cocycle class under flop,
  the wall-crossing invariant) is an INDEPENDENT analytic datum not encoded
  in any of the five slots; even at fixed level $k$, two chiral algebras with
  identical $k, p_{\max}, \ldots$ can differ on the cohomology class of their
  classical r-matrix inside $H^2(\mathfrak g, \mathbb C)$.

## IV. Correct relationship (Heal)

Strongest honest form of Theorem G:

> $\varphi'(A) = (p_{\max}, r_{\max}, \chi_{\mathrm{VOA}}, n_{\mathrm{strong}},
> \mathrm{coset}, \kappa_{\mathrm{ch}})$
>
> where $\kappa_{\mathrm{ch}} \in H^2(\overline{\mathcal M}_{g,n}^{\mathrm{fam}}, \mathbb Q)$
> is the pullback of the universal Arakelov $\kappa$ class (Theorem IV.C) to
> the moduli point $[A]$, is a complete invariant of $A$ up to
> Francis--Gaitsgory bar Quillen equivalence on the standard landscape.

Equivalently, the sixth slot is the CENTRAL EXTENSION CLASS / LEVEL /
CURVATURE, and it is precisely the datum that ties the fingerprint to the
modular stack via Theorem IV.C. This is NOT a downgrade: the strongest form
of G becomes tightly coupled to the strongest form of D (Universal Arakelov
$\kappa$ class). Six slots, not five.

**Consequence for the programme.** The existing theorem
`thm:fingerprint-completeness-conditional` is `\ClaimStatusProvedHereConditional`
with scope restricted to non-critical level AND fixed $\kappa_{\mathrm{ch}}$. The
Platonic form is $\varphi'$ with six slots; the five-slot $\varphi$ is the
coarse projection $\Pi_\kappa \circ \varphi'$ quotienting out central-extension
class. The quaternitomy becomes a DOUBLE coarse projection
$\varphi' \to \varphi \to (G/L/C/M/\mathrm{FF})$.

**Literature crosscheck.** Arakawa (Invent. Math. 2007) classifies
$W_k(\mathfrak g)$ up to $k$-dependence; the level is an explicit invariant
in his classification. Feigin--Frenkel (1992) establishes the critical-level
$k = -h^\vee$ as its own stratum (class FF in our notation) — confirming
that $k$ separates strata. Creutzig--Kanade--McRae (2019) tensor-category
treatment of VOSA extensions shows that extensions inside a fixed tensor
category are controlled by $H^2$-cocycle classes that depend on $k$. Miyamoto
(2004) modular-invariance theory distinguishes $V_k(\mathfrak g)$ at different
rational $k$ via distinct modular $S$-matrices — another witness of the
missing sixth slot.

**Final deliverable.** The 5-slot fingerprint is NOT complete. A 6th slot
$\kappa_{\mathrm{ch}}$ (level / central-extension class / curvature) is
required to distinguish the continuous family $\{\mathcal H_k\}_{k \in \mathbb C^*}$
of Heisenberg algebras. The refined $\varphi' = (\varphi, \kappa_{\mathrm{ch}})$ is
complete on the standard landscape, and via Theorem IV.C couples to the
universal Arakelov class, making the fingerprint a
$\overline{\mathcal M}_{g,n}^{\mathrm{fam}}$-valued invariant rather than
a discrete tuple.
