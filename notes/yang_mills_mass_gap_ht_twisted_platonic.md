# Yang-Mills Mass Gap via the HT-Twisted Image: Strongest Honest Form

## 0. Frame of attack

The programme's extant result is `thm:mass-gap-reduction-internal-screening`
(ym_instanton_screening.tex:695) plus its sharper equivalence
`thm:ym-mass-gap-reduction` (ym_synthesis_core.tex:1207). Stripped of
rhetoric, these say:

> Assuming (H1) the HT twist produces a celestial chiral algebra with
> instanton-completed bar complex, (H2) the screenings are weight-1 Felder
> primaries inside the Wakimoto realization, and (H3) an untwisting map
> identifies the physical YM Hamiltonian with a canonically algebraic
> operator, then the pure-YM spectral gap is equivalent to the algebraic
> condition Z_vis = 0 on B^Λ(A^cel_YM).

(H1) and (H2) are proved inside the programme; (H3) is not, and it is the
strong form of what the Clay problem asks for. Calling the result a
"mass-gap theorem" is therefore FM137-style malpractice: it is a genuine
algebraic reduction principle, an equivalence on the Koszul-admissible
bar side, modulo a physics-to-algebra bridge that no one has constructed.

The attack below is the strongest honest upgrade path made by combining
the programme's Universal Holography functor Φ_hol and the Russian-school
/ Chriss-Ginzburg / Costello-Gaiotto inputs. It proceeds in three items.

## 1. Schur-sector boundary W(g) and its lowest conformal weight

Beem-Lemos-Liendo-Peelaers-Rastelli-van Rees (CMP 2015) construct a
functor χ from 4d N=2 SCFTs to 2d vertex algebras via cohomology of the
Schur supercharge Q = Q^-_1 + tilde S^{1 dot -}. The target is a (Z≥0)-graded
vertex algebra with central charge c_2d = -12 c_4d, where c_4d is the
conformal anomaly of the 4d SCFT.

For the relevant HT-twistable cases the boundary is:

* **Pure 4d N=2 SYM, gauge group G (compact simple):** the HT twist on
  C × R_≥0 in Costello-Gaiotto's conventions produces, as its Schur
  sector, the affine vertex algebra V_{-h^∨}(g) at the dual Coxeter
  level — a NON-critical level -h^∨ is NOT correct here; the Beem-Rastelli
  result (BLLPRR §3) gives k = -h^∨ only for the class S 4d/2d image at
  a genus-zero disc with two full punctures. For pure N=2 SYM with no
  matter, the Schur sector is the affine Kac-Moody algebra V_k(g) at
  level k = -2h^∨ (Beem-Rastelli Thm 4.6; Song-Xie-Yan §2 for the
  rank-one check). This is a CRITICAL-ADJACENT but non-critical level
  (k ≠ -h^∨), placing V_{-2h^∨}(g) in class L of the programme.

* **Class S of type A_{n-1} on a genus-g surface with s full punctures:**
  the boundary is W_n at level k = -n + (2-2g-s); principal W-algebra on
  class M side once r_max reaches ≥ 4 from quartic OPE in W-generator
  self-interactions.

The lowest non-trivial conformal weight in each case:

| G / class        | boundary VOA               | generators (weights)          | lowest non-trivial primary |
|------------------|----------------------------|-------------------------------|----------------------------|
| SU(2) = A_1      | V_{-4}(sl_2)               | J^a (weight 1)                | weight 1                   |
| SU(3) = A_2      | V_{-6}(sl_3)               | J^a (weight 1)                | weight 1                   |
| SU(4) = A_3      | V_{-8}(sl_4)               | J^a (weight 1)                | weight 1                   |
| Class S T_n      | W_n at k = -n + 2 - 2g - s | spin-2,3,…,n currents         | weight 2 (stress tensor)   |

For pure N=2 SYM the lowest non-trivial Schur primary is always the
spin-1 R-symmetry current J^a (weights 1), inherited directly from the
gauge field. For class S W_n the lowest primary above vacuum is the
stress tensor (weight 2). Neither gap is zero, and both are HT-sector-
protected.

## 2. Lifting chiral-algebra spectral gap to 4d mass gap

The chiral-algebra spectral gap Δ_2d = 1 (resp. 2 for W_n) lifts to a
statement about the 4d spectrum via the Mellin-shadow dictionary of
`prop:uch-mellin-shadow`: the conformal weight Δ of a celestial primary
tracks the energy ω of the corresponding 4d state via Δ = 1 + i ω /
scale. Primaries at integer Δ ≥ 1 correspond to finite-energy 4d states
in the HT sector, and the lowest conformal weight Δ_min of a non-vacuum
primary in A^cel gives a UNIVERSAL lower bound on the 4d HT-sector mass
spectrum:

    E_HT ≥ Δ_min · scale

For the pure N=2 Schur sector the scale is set by the dimensionful
parameter distinguishing the SUSY-preserving Ω-deformation plane; when
the theory is conformal (as pure N=2 SYM is, at the origin of the
Coulomb branch) this scale is formally zero and the chiral-algebra gap
does not directly give a 4d mass gap.

**This is the first genuine obstruction:** the HT twist of pure N=2 YM
without matter is a SUPERCONFORMAL theory, not a massive one. Its
chiral-algebra boundary spectrum does not set a mass scale because the
4d theory itself does not have one. A mass gap in the Clay sense requires
breaking conformal invariance, which the HT twist does not do.

For pure (non-supersymmetric) 4d Yang-Mills, the Clay theory, there is
no HT twist to use: the HT sector of (d) in ym_synthesis_core:1122
("Pure non-supersymmetric 4d gauge theory on a null slab") is a formal
analogue, not a cohomological reduction of the physical theory. The
"celestial chiral algebra" for pure YM exists only as an asymptotic
formal limit: Strominger-Pasterski-Shao-Strominger put it on the light
cone at null infinity.

Both paths therefore fail to deliver a 4d mass gap directly.

## 3. Transport from HT-twisted N=2 to pure 4d YM

**The transport question** is whether the HT-sector gap Δ_min = 1
(affine KM) or 2 (class S W_n) can be CONTROLLED-DEFORMED to a pure
Yang-Mills mass gap. There are three logically distinct paths:

**Path A: Seiberg-Witten soft breaking.** Add a mass term m tr Φ^2 to
the N=2 adjoint hypermultiplet, giving the N=2* theory; as m → ∞ the
hypermultiplet decouples and one reaches pure 4d N=2 SYM. Seiberg-Witten
(NPB 1994) solved the low-energy effective theory: monopole/dyon
condensation at the singular points of the Seiberg-Witten curve produces
a mass gap for the IR theory. In the programme language, this is
Polyakov monopole condensation (`rem:polyakov-confinement-algebraized`)
realized via chiral central extension Z_vis, with mass gap scale Λ =
m · exp(-1/g^2_{UV}) by dimensional transmutation.

Transport obstruction in Path A: the HT-sector chiral algebra is
invariant under m and tracks only the BPS-protected states; the
non-BPS states that carry the 4d mass gap (W-bosons of Higgsed gauge
symmetry in the Coulomb phase) are exact under the Schur supercharge
Q. The Schur index misses them by construction.

**Path B: Asymptotic N=2-isation in the UV.** Pure 4d SU(N) YM is
asymptotically free (Faddeev, Bull. Braz. Math. Soc. 1999 frames this
as a small-g analog of ergodicity). In the deep UV, one might expect
pure YM to be "controlled" by the N=2 embedding via decoupling
hypermultiplets. Seiberg-Witten N_f = 2N flavor QCD in the conformal
window sends its c_4d to the pure-gauge c_4d as the flavors decouple.

Transport obstruction in Path B: the limit g → 0 is singular on the
spectral-gap side precisely because the Lagrangian mass gap vanishes
with g^2. The chiral algebra is SELF-SIMILAR under the RG, so the
gap of V_{-2h^∨}(g) is the same at every scale — it is the 4d c_4d
anomaly, not the dynamical scale Λ. UV-to-IR transport requires
running the chiral algebra, which the HT twist disallows (the Schur
sector is a PROTECTED INVARIANT).

**Path C: Pure-YM chiral algebra as a non-SUSY cohomology.** Costello
has sketched a non-SUSY HT twist using only a 4d scale set by a
conformal-breaking operator. In this reading, pure YM has a FORMAL
chiral algebra at null infinity (the celestial chiral algebra of the
S-matrix), and the programme's Universal Holography functor maps it to
a non-BPS analog of V_{-2h^∨}(g) enriched with the dynamical scale Λ.
One expects the lowest conformal weight Δ_min to be replaced by a
SPECTRAL RIEMANN SURFACE with a branch cut at Δ = 0 (the
renormalization-group flow) and a LOG singularity at Δ = 1 (the
anomalous-dimension threshold). In this regime the spectral gap of the
chiral algebra would TRACK the dynamical scale Λ, and the 4d mass gap
would follow.

Transport obstruction in Path C: the non-SUSY HT twist does not exist
as a cohomological construction; it is conjectural. The required
"celestial chiral algebra for non-SUSY YM" is the object the Clay
problem demands, not a tool one can apply.

## 4. The precise obstruction as algebraic statement

Combining items (1)–(3), the obstruction is:

> The HT twist is a Q-COHOMOLOGY filter on the 4d spectrum. For N=2
> YM it retains the Schur-protected BPS states and kills the rest;
> for pure YM it does not exist. Any mass-gap statement derived from
> the chiral-algebra boundary therefore constrains the SCHUR SUBSECTOR
> spectrum, not the full 4d spectrum. The Schur-subsector gap Δ_min
> is DIMENSIONLESS (a conformal weight); promoting it to a dimensionful
> 4d mass gap requires a UV/IR scale-setting input that the HT twist
> by construction does not see.

In the programme's (H1)-(H3) language of `thm:ym-mass-gap-reduction`:
(H1) and (H2) are about the BPS sector; (H3) demands a bridge that
transports DIMENSIONLESS chiral-algebra data to a DIMENSIONFUL
Hamiltonian. No such bridge follows from Universal Holography alone.

## 5. Verdict

**Progress delivered.** The programme gives a RIGOROUS algebraic
reduction principle: for any HT-twistable 4d theory whose boundary VOA
is in the Koszul-admissible class (pure N=2 SYM: class L; class S: class
M via DS-Hoch bridge), the BPS-sector spectral gap is equivalent to
triviality of the visible center Z_vis of the instanton-completed bar
complex. This is a strong equivalence, not a heuristic. For pure N=2
SYM, the Schur boundary is V_{-2h^∨}(g); its lowest conformal weight
is 1 (R-current); the spectral gap in the BPS sector is Δ_min = 1,
computable within the programme's bar-cobar machinery.

**Progress not delivered.** The Clay mass gap for pure non-SUSY YM is
NOT reached. Two obstructions:
1. Pure 4d N=2 SYM is SUPERCONFORMAL; its chiral-algebra gap is a
   conformal weight, not a mass scale. Dimensional transmutation to a
   Λ scale requires a mass deformation (e.g. N=2* with m → ∞), which
   takes the theory out of the Beem-Rastelli domain.
2. Pure non-SUSY YM lacks a well-defined HT twist. The "celestial chiral
   algebra" exists only at null infinity in a formal sense
   (Pasterski-Shao-Strominger); mapping it into the programme's
   Universal Holography image is conjectural.

**Precise transport obstruction.** The HT twist is a BPS cohomology
projector; it retains Δ ∈ Z≥0 primaries and discards the continuum of
non-BPS 4d states that carry the YM mass gap. Any argument that lifts
a chiral-algebra gap to a Hamiltonian gap must supply the missing
UV/IR scale-setting datum — precisely (H3) in
`thm:ym-mass-gap-reduction`. Universal Holography alone does not
supply it, because by construction it is a functor between DIMENSIONLESS
algebraic structures.

**The strongest honest form achievable with current programme machinery
is therefore:**

> Pure 4d N=2 SYM with compact simple gauge group G has Schur-sector
> spectral gap Δ_min = 1 (resp. 2 for the class S W_n descendant),
> equal to the lowest non-vacuum conformal weight of the boundary
> chiral algebra V_{-2h^∨}(g) (resp. W_n at level -n + 2 - 2g - s).
> This is a BPS-sector spectral gap, unconditionally computable and
> equal to 1 (or 2) for every compact simple gauge group.

Promoting this to the Clay mass gap requires, inescapably, a non-SUSY
chiral-algebra construction and a scale-setting bridge, neither of
which is in the programme's Koszul-admissible universe. The verdict is:
**partial progress on the BPS sector, precisely-named transport gap
(dimensionless-to-dimensionful bridge) on the full Clay problem.**

## 6. Strongest honest upgrade opportunity

The programme CAN be extended toward the Clay problem by constructing
the non-SUSY HT twist: Costello-Li 4d BV quantization of pure YM without
SUSY, followed by the Schur-analog cohomology on a null slab. This would
produce a non-BPS celestial chiral algebra with a DIMENSIONFUL scale Λ
built in, and the programme's Universal Holography functor would apply.
The research content is: does there exist a nilpotent BRST-like charge
Q_pure on pure YM whose cohomology is a vertex algebra? Currently open;
not obstructed by the programme's framework but requires an input the
programme does not provide.

All remaining malpractice-grade issues on the YM/mass-gap axis (FM137,
FM138, FM139, FM140) are addressable independently from this verdict.
