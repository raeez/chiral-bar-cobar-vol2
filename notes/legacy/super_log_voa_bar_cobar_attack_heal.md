# Super and Logarithmic VOAs: Bar-Cobar Adjunction — Attack and Heal

## Scope

Vol I Theorem A (Francis-Gaitsgory bar-cobar Quillen/(infty,2) equivalence
between augmented E_1-chiral algebras and conilpotent dg coalgebras on
Ran(X)) was stated for ORDINARY (bosonic, Z/2-ungraded, semisimple-on-simples)
chiral algebras. Attack surface: N=2 SCVOA (fermionic
supercurrents G^+/G^- weight 3/2), N=4 SCVOA (BLLPR small/large at c=-3n),
and triplet W(p) for p >= 2 (logarithmic, non-semisimple, with
non-trivial Ext^1 between simples). Does the adjunction close, or
break?

## (a) What Thm A gets RIGHT in the bosonic case

Three structural inputs. (I) Ambient category: the BD pseudo-tensor
on D-mod(X) lifted to Ran(X) via Francis-Gaitsgory (GR17 IV.5);
bar is B^ch(A) = T^c(s^{-1}\bar A) with deconcat coproduct plus the
chiral OPE-induced differential d_B. (II) Conilpotent completion:
augmented A has \bar A nilpotent on filtration pieces, so B^ch(A) is
conilpotent and the counit epsilon: Omega^ch B^ch(A) -> A is a
quasi-isomorphism. (III) Semisimplicity on simples: for bosonic A
with PBW filtration (Heisenberg, affine KM at generic k, Virasoro
generic c, principal W_N), the associated graded gr A = Sym(V) for
V a weight-graded Sym_n-equivariant D-module; standard PP05/LV12 Koszul
duality closes. The proof of Thm A factors through: A augmented
=> B^ch(A) conilpotent => bar-cobar unit/counit qiso at the Koszul
locus. Nowhere does bosonic-ness enter essentially EXCEPT through
(III), namely through the assumption that Sym_n acts (not Sym-super_n).

## (b) What gets WRONG at super / logarithmic

**Super (N=2, N=4).** Three distinct failures of a naive bosonic
recapitulation.

(b1) Permutation-operad signs. The ordered bar uses T^c(s^{-1}\bar A),
which is Sym-free. The Sym-coinvariant bar B^Sigma (the one that
Thm A^{infty,2} relates to B^ord via R-twisted Sigma_n-descent) assumes
Sigma_n acts; for super A this is KOSZUL-SIGNED Sym-super_n with
(-1)^{|a||b|} permutation. Direct descent along Ran(X)^ord -> Ran(X)
is WRONG for super A (it uses the wrong sign convention on the monodromy
local system L_R).

(b2) R-matrix parity. The R-matrix R_s(u) = u + hbar P_s with
super-permutation P_s(e_i ⊗ e_j) = (-1)^{|i||j|} e_j ⊗ e_i. Naive
R-twisted Sigma-descent using bosonic P is off by Koszul signs at
every odd-odd crossing. AP107 flags this: r^coll differs from
Laplace-transform r for odd generators — concretely, G^+G^- at triple
pole in N=2 and psi^+ psi^- at simple pole in symplectic fermions
each carry a parity sign in the bar differential.

(b3) Conformal weight parity. For N=2, G^± have weight 3/2 ≡ 1 mod 2,
matching their fermionic parity. For N=4 BLLPR, the supercharges G^{i}
have weight 3/2 matching parity. This is automatic, but only because
the chapter files already adopt the "conformal-weight-mod-2 parity
assignment" (super_chiral_yangian.tex:791). A naive Thm A statement
without this assignment leaves G^± with bosonic signs and fails AP107.

**Logarithmic (W(p), p >= 2).** The genuinely new failure mode.

(b4) Non-semisimplicity breaks the augmentation-conilpotence bridge.
For W(p) at p >= 2, the category of modules is NOT semisimple:
Adamovic-Milas 2008 Theorem 4.1 gives dim Zhu(W(p)) = 2p with
nilpotent radical of dimension p. The projective covers of simple
modules have length 2 with non-trivial Ext^1 (CKL 2019). The bar
complex B^ch(W(p)) then carries Ext^1-contributions invisible to
the bosonic B^ch formula: the differential d_B picks up off-diagonal
"logarithmic" terms from the Jordan blocks of L_0 on projective covers.

(b5) Koszul involution k <-> -k - 2h^v. For affine KM at bosonic
generic level, k <-> -k - 2h^v is the Feigin-Frenkel involution
realising the Koszul dual. For W(p), the Koszul involution sits on
the Virasoro sub-channel (c(p) = 1 - 6(p-1)^2/p, under c <-> 26-c)
but the WW channel (pole 2(2p-1)) is NOT involution-stable without
a separate super-Koszul correction. The naive involution
k <-> -k - 2h^v fails because triplet generators W^a are not in
the Feigin-Frenkel kernel; they constitute the logarithmic obstruction.

(b6) Free strong generation open for p >= 4. AP67/prop:wp-free-
strong-generation (logarithmic_wp_tempered_analysis_platonic.tex:239)
records: at p >= 4, the first candidate null-vector appears at
weight 2(2p-1) = 4p-2, detected as a Massey product
<Omega, Omega, Omega> in arity 3 bar cohomology. The bar-cobar counit
fails strict quasi-isomorphism at this arity; conilpotent completion
needs weight-stratified pro-category.

## (c) Correct relationship

Theorem A EXTENDS — not as a single statement but as a three-branch
refinement, each branch respecting the PLATONIC form of the programme
(no downgrades, only refinements).

**Branch 1: Super Thm A (SVOA).** Replace Ass/Ass^c by the Z/2-graded
signed versions Ass_s/Ass_s^c with Sym-super permutations
(Koszul signs (-1)^{|a||b|}). The (infty,2) Quillen equivalence holds
verbatim on super-conilpotent super-augmented SVOAs, with:
- super-deconcat coproduct (eq:super-deconcat)
- super-shadow tower S_r^super = S_r^bos + (-1)^r S_r^fermion
  (super_chiral_yangian.tex:709-717, thm:super-shadow-well-defined)
- super-Koszul dual (Ysuper_hbar)^! = Ysuper_{-hbar}^theta (theta =
  Chevalley-Kac involution, thm:super-yangian-koszul-dual
  super_chiral_yangian.tex:545)
- GRT^super = GRT_1(Q) ⋊ (Z/2)^{|odd|} parameterising faces
  (see Vol II CLAUDE.md "Super-variant" of GRT seven faces).

N=2 SCVOA Koszul complementarity: NOT 2·sdim(N=2)·(1-c/3). The
correct form is the coset subtraction
kappa(N=2, c) = (6-c)/(2(3-c)) = (k+4)/4 with c = 3k/(k+2)
(examples-worked.tex:4349), and the complementarity IS kappa(c) +
kappa(6-c) = 1 under the Koszul involution c <-> 6-c = k <-> -k-4
(the Feigin-Frenkel involution of the underlying sl_2 coset).
sdim(N=2) = 2 - 2 = 0 (two bosons T, J and two fermions G^+, G^-)
and does NOT enter the kappa formula; kappa is captured by the
Virasoro-plus-Heisenberg even core minus the coset-by-U(1) correction.
For N=2 minimal models c = 3(1 - 2/p), Koszul involution is the
Kazama-Suzuki parafermion dual.

**Branch 2: N=4 BLLPR at c=-3n.** Small-N=4 SCVOA at c = -3n falls in
Branch 1 with the additional sl(2) R-symmetry gauged. Bar-cobar closes
via the coset chi[T[X]]/u(1)_R (n2_scvoa_coset_ds_hoch_bridge_platonic.md):
composite DS + Heisenberg-coset functor, chain-level HPL both steps,
C_2-cofiniteness via AKM 2020 (arXiv:2006.12692). Large-N=4 adds a
second Heisenberg; same mechanism, two-step coset.

**Branch 3: Logarithmic W(p).** Bar-cobar closes ONLY after replacing
the ambient category: the target category is no longer dg-coalg^{conil}
but PERIODIC-CDG coalg in the Positselski sense — coalgebras with
curvature absorbed into a filtered CDG structure. The Koszulness
moduli scheme M_Kosz(W(p)) is non-empty on the logarithmic chart
Phi_log (see Koszulness Moduli Atlas, Branch U_7 / Branch log).
The k <-> -k - 2h^v involution is REPLACED by the CKL logarithmic
Koszul involution that absorbs the Ext^1-block data into the dual's
filtration. Adamovic-Milas 2008 + CKL 2019 supply the null-vector
control; weight-completed chain-level closure is prop:bv-bar-class-
m-weight-completed (Vol II Cross-Volume Bridges, W-algebras row (4)).

Temperedness (logarithmic_wp_tempered_analysis_platonic.tex:128)
ensures that the three-channel decomposition
S_r(W(p)) = S_r^TT + S_r^TW + S_r^WW has each channel analytically
tempered; the shadow tower converges weight-by-weight; Thm A closes
in the weight-completed pro-category.

## Summary (what changes, what survives)

Survives verbatim: (∞,2) equivalence structure, Quillen model,
universal property as adjunction. Changes:

- Ambient category: super case needs Sym-super signs; logarithmic
  case needs Positselski periodic-CDG coalg.
- Differential: super case picks up parity signs on odd-odd
  permutations; logarithmic case picks up Jordan-block terms from L_0.
- Koszul involution: super case uses Chevalley-Kac theta (hbar-flip
  at all orders); logarithmic case uses CKL log-involution (not the
  bosonic k <-> -k - 2h^v).
- Shadow tower: super case uses super-Euler character super-Koszul
  normalisation; logarithmic case uses three-channel decomposition.

Super structure does NOT require a separate formalism — Sym_n
replaced by Sym-super_n is a uniform twist across all Koszul duality
machinery (Gow-Molev 2010, Positselski-Polishchuk 2005 super extension).
Logarithmic W(p) DOES require category replacement (periodic-CDG
coalg instead of plain dg coalg), following FM251/conj:periodic-cdg
closure. Both branches are refinements, NOT exclusions.

## Report (under 200 words)

Bar-cobar (Vol I Thm A) extends to super and logarithmic VOAs, but
through two different refinements. SUPER (N=2, N=4 BLLPR): a uniform
Koszul-sign twist (Sym_n -> Sym-super_n) plus the Chevalley-Kac
involution theta replacing the Chevalley involution yields the
super-Yangian Koszul dual (Ysuper)^! = Ysuper_{-hbar}^theta
(super_chiral_yangian.tex:545). The N=2 SCA Koszul complementarity is
kappa(c) + kappa(6-c) = 1 with kappa = (6-c)/(2(3-c)), NOT
2·sdim·(1-c/3); sdim = 0 and the coset subtraction (Kazama-Suzuki
dual) captures the correct kappa. N=4 BLLPR closes via the coset
chi[T[X]]/u(1)_R (AKM 2020). LOGARITHMIC W(p): category replacement
— dg-coalg^conil -> Positselski periodic-CDG coalg. Non-semisimple
Ext^1 between simples, Jordan-block d_B terms, and the CKL log-Koszul
involution (not the bosonic k <-> -k - 2h^v). Free strong generation
open for p >= 4 (AP67); bar-cobar closure is weight-completed via
the three-channel (TT, TW, WW) tempered decomposition. Neither super
nor logarithmic requires a SEPARATE formalism; both are refinements
within the Koszulness Moduli Atlas M_Kosz — super as a Z/2-signed
chart, logarithmic as a periodic-CDG chart.
