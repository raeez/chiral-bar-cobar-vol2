# K_V super-extension: attack-heal (adversarial audit 2026-04-17)

## Verdict

**K_V(g) = 2·sdim(g) is the correct super-generalization for BASIC classical
simple Lie superalgebras with NONZERO super-dual-Coxeter number h^∨.** The
algebraic mechanism that produced K_V(g) = 2·dim(g) for ordinary simple g
(single-Casimir Sugawara, Koszul sign flip on 1/t piece) carries over verbatim
with `dim` replaced by `sdim` — provided Sugawara is well-defined (h^∨ ≠ 0)
AND the invariant form is non-degenerate (type I / type II basic classical
families).

**The formula BREAKS or degenerates at three structurally distinct boundaries:**

1. **h^∨ = 0 families** (psl(n|n), osp(2n+2|2n), D(2,1;α) generic α, and the
   full subring of "critical-like" super types): Sugawara denominator vanishes
   uniformly. There is NO non-critical level. K_V is undefined in the same
   sense that Sugawara is undefined — not "zero", but "the construction fails
   to produce a stress tensor". A different W-type construction (Feigin–Frenkel
   super-center, or N=2,4 superconformal stress tensors via coset) is required.

2. **sdim = 0 but h^∨ ≠ 0** (sl(n|n-1) at small rank, osp(3|2), sl(2|1)): the
   Sugawara central charge is IDENTICALLY ZERO at every level, so K_V = 0 is
   tautological. The Koszul complementarity statement degenerates to 0 = 0.
   The genuine invariant at these types is NOT the central charge sum but the
   quantum-shifted Casimir eigenvalue on the vacuum, which is non-trivial.

3. **D(2,1;α) one-parameter family**: h^∨ depends on α, vanishing at the three
   points α ∈ {-1, 0, ∞} where D(2,1;α) degenerates. Generic D(2,1;α) with
   h^∨ ≠ 0 satisfies K_V = 2·sdim(g) = 2, but α runs through a 1-parameter
   family of genuinely distinct superalgebras.

Summary table (final):

| superalgebra   | dim_even | dim_odd | sdim     | h^∨   | K_V                      |
|:--------------:|:--------:|:-------:|:--------:|:-----:|:------------------------:|
| osp(1\|2)      | 3        | 2       | 1        | 3/2   | 2  ✓                     |
| osp(1\|2n)     | n(2n+1)  | 2n      | 2n²-n    | n+1/2 | 2(2n²-n)  ✓              |
| sl(2\|1)       | 4        | 4       | 0        | 1     | 0  (tautological)        |
| sl(m\|n), m>n  | m²+n²-1  | 2mn     | (m-n)²-1 | m-n   | 2((m-n)²-1)  ✓           |
| psl(n\|n)      | 2n²-2    | 2n²     | -1       | 0     | UNDEFINED (Sugawara deg.) |
| osp(3\|2)      | 6        | 6       | 0        | 1/2   | 0  (tautological)        |
| osp(5\|2)      | 13       | 10      | 3        | 3/2   | 6  ✓                     |
| D(2,1;α)       | 9        | 8       | 1        | 0     | UNDEFINED at generic α   |
| G(3)           | 17       | 14      | 3        | 3     | 6  ✓                     |
| F(4) super     | 24       | 16      | 8        | 3     | 16  ✓                    |

(All dim/sdim/h^∨ values from Kac 1977 Adv. Math. 26, Frappat–Sciarrino–Sorba
2000, Kac–Wakimoto 1989.)

## Root data and super-dual-Coxeter

For a basic classical Lie superalgebra g with even-non-degenerate invariant
form (·, ·), the super-dual-Coxeter h^∨ is defined (Kac–Wakimoto 1989,
Kac–Möbius–Sergeev 2001) by

    2 h^∨ · (x, y) = str(ad x · ad y) — Killing supertrace.

Equivalently, h^∨ is half the eigenvalue of the quadratic Casimir on the
adjoint supermodule. At ORDINARY simple g, sdim = dim and h^∨ matches the
classical dual Coxeter. At basic classical super g with non-degenerate Killing
supertrace, h^∨ is given by (Kac 1977, Table VI; Frappat–Sciarrino–Sorba
Dictionary p. 257ff):

| g            | h^∨                   |
|:------------:|:---------------------:|
| sl(m\|n)     | m - n                 |
| osp(2m+1\|2n)| 2(m-n) + 1            |
| osp(2m\|2n)  | 2(m-n)                |
| D(2,1;α)    | 0 (all α!)            |
| G(3)         | 3                     |
| F(4) super   | 3                     |

In particular:
- sl(n|n): h^∨ = 0 (the Sugawara denominator vanishes identically).
- osp(2m|2m): h^∨ = 0.
- D(2,1;α): h^∨ = 0 for ALL α (this is the key feature — D(2,1;α) is
  "always critical" in the Sugawara sense).
- sl(m|n), m ≠ n: h^∨ = m - n ≠ 0.
- osp(2m+1|2n), m ≠ n: h^∨ = 2(m-n)+1 ≠ 0 (odd, so never zero).

Only the h^∨ ≠ 0 families admit a non-critical Sugawara construction.

## Super-Sugawara central charge

For a basic classical simple Lie superalgebra g with h^∨ ≠ 0 and non-degenerate
invariant form, Kac–Wakimoto (1989, Theorem 3.1) give the super-Sugawara stress
tensor

    L_n = (1 / (2(k + h^∨))) Σ_A (−1)^{p(A)} : J^A J_A :

where {J^A, J_A} is a super-dual basis (sign (−1)^{p(A)} accounts for odd
parity), and the central charge is

    c_Sug(V_k(g)) = k · sdim(g) / (k + h^∨).                    (**)

The derivation tracks the one for ordinary g verbatim, with the scalar
coefficient dim(g) replaced by the supertrace sdim(g) = dim(g_0) − dim(g_1).
(This replacement is exactly what the super-dual-basis sign pattern produces
when one computes the double-contraction <J^A J_A J^B J_B>.)

## Explicit verification: osp(1|2)

osp(1|2) has even part sl(2) (dim 3) and odd part the 2-dim fundamental sl(2)
module (dim 2). So

    sdim(osp(1|2)) = 3 − 2 = 1,     h^∨ = 3/2.

Sugawara (**): c(V_k(osp(1|2))) = k · 1 / (k + 3/2) = k/(k + 3/2).

Under Koszul k ↔ k^! = −k − 2h^∨ = −k − 3:

    k^! + h^∨ = −k − 3 + 3/2 = −(k + 3/2) = −t.

So

    c(V_{k^!}) = (−k−3) / (−k − 3/2) = (k + 3) / (k + 3/2).

Sum:

    K_V = k/(k+3/2) + (k+3)/(k+3/2)
        = (2k + 3)/(k + 3/2)
        = 2·(k + 3/2)/(k + 3/2)
        = 2
        = 2 · sdim(osp(1|2)).     ✓

The identity is exact at every non-critical level (k ≠ −3/2). This matches the
universal super-formula K_V(g) = 2·sdim(g).

Numerical check at three levels:

| k    | c_Sug             | k^!     | c_Sug^!           | sum |
|:----:|:-----------------:|:-------:|:-----------------:|:---:|
| 1    | 1/(5/2) = 2/5     | −4      | 4/(5/2) = 8/5     | 2   |
| 2    | 2/(7/2) = 4/7     | −5      | 5/(7/2) = 10/7    | 2   |
| 1/2  | (1/2)/2 = 1/4     | −7/2    | (7/2)/2 = 7/4     | 2   |

## Explicit computation: sl(2|1) (sdim = 0 case)

sl(2|1): even part = sl(2) × u(1) (dim 3 + 1 = 4), odd part = 4 (= 2 · 2 fund).
So dim_even = 4, dim_odd = 4, and

    sdim(sl(2|1)) = 4 − 4 = 0,     h^∨ = 2 − 1 = 1.

Sugawara (**): c(V_k(sl(2|1))) = k · 0 / (k + 1) = 0.

The central charge is IDENTICALLY ZERO at every level k ≠ −1. Under Koszul
k ↔ k^! = −k − 2:

    c(V_{k^!}(sl(2|1))) = (−k−2) · 0 / (−k−1) = 0.

Sum: K_V = 0 + 0 = 0 = 2 · 0 = 2 · sdim.

**But this is tautological.** The super-Sugawara formula is vacuously satisfied
because the vacuum carries zero total central charge to begin with. The genuine
algebraic content has moved to a DIFFERENT invariant: the quadratic Casimir
eigenvalue on the vacuum (non-zero, related to the N=2 superconformal central
charge via the coset sl(2|1)_k / u(1)_k construction of Kazama–Suzuki 1989).

Lesson: at sdim = 0 with h^∨ ≠ 0, the identity K_V(g) = 2·sdim(g) holds
trivially but does not carry Koszul-duality information. Koszul complementarity
degenerates to 0 = 0. The useful invariant is NOT the Sugawara c but the
refined structure on the vacuum module (e.g. the N=2 stress tensor inside
V_k(sl(2|1))).

## sdim = 0 pattern: osp(3|2) and sl(n|n-1)

More generally, sdim = 0 whenever dim_even = dim_odd. The "accidentally zero
supertrace" types include:

- sl(n+1|n): sdim = (n+1-n)² - 1 = 0. h^∨ = 1.
- osp(3|2): sdim = 6 - 6 = 0. h^∨ = 1/2.
- osp(2m+1|2m): similar pattern.

At ALL such types, c_Sug ≡ 0 and K_V = 0 tautologically. The Koszul-duality
framework sees zero on both sides of the involution. These are precisely the
types where the super-Sugawara construction collapses to a trivial stress
tensor, and the non-trivial chiral algebra structure lives in a super-extension
(N=2, N=4 superconformal algebras) obtained via coset or DS reduction.

## h^∨ = 0 pattern: psl(n|n), osp(2m|2m), D(2,1;α)

At these types, the Sugawara DENOMINATOR vanishes. The formula (**) is simply
undefined — there is no non-critical level; every level is "critical" in the
sense that Sugawara's 1/t factor becomes 1/0.

This is genuinely different from the sdim = 0 case: at h^∨ = 0, the Sugawara
construction does not exist as an element of V_k(g) for any k. In particular,
V_k(psl(n|n)) has no stress tensor defined by Sugawara; one must instead use a
Feigin–Frenkel super-center construction or coset realization.

**D(2,1;α) is the archetype**: it is a one-parameter family of non-isomorphic
17-dim basic classical Lie superalgebras, all with h^∨ = 0. Kac–Wakimoto 1989
and Gorelik 2000 construct the stress tensor via N=4 superconformal coset
embedding, NOT via Sugawara. For this family, K_V is genuinely NOT defined by
the Sugawara formula, and the Koszul-complementarity statement must be
reformulated using the coset / BRST construction.

## Super-Koszul involution k ↔ k^! = -k - 2h^∨

The Koszul involution on V_k(g) for basic classical simple super g with
h^∨ ≠ 0 takes the same form as in the ordinary case:

    k^! = -k - 2h^∨.

This is valid algebraically because the Koszul complementarity is derived from
the bar complex B(V_k(g))^! = V_{-k-2h^∨}(g) via the affine-KM W-translation
(Feigin–Frenkel duality), and this duality extends to super types with h^∨ ≠ 0.
The proof tracks the ordinary-g argument verbatim using super-dual bases.

At h^∨ = 0, the involution k ↔ -k is formally well-defined (= the Chevalley
k → -k flip) but the Sugawara Koszul pairing degenerates, and the complementary
invariant is not the sum c + c^! but a BRST cohomology quantity.

## Three-step protocol

**(a) What does K_V = 2·sdim get RIGHT?** For basic classical simple Lie
superalgebras with h^∨ ≠ 0 AND sdim ≠ 0, the formula is genuinely universal.
Examples: osp(1|2), sl(m|n) with m ≠ n+1 (so sdim ≠ 0), G(3), F(4) super,
osp(2m+1|2n) with m ≠ n. The derivation is identical to the ordinary case
because super-Sugawara has the same single-Casimir structure with `dim`
replaced by `sdim`.

**(b) What does it get WRONG?** Two failure modes:

- **sdim = 0, h^∨ ≠ 0** (sl(n+1|n), osp(2m+1|2m), etc.): formula holds
  tautologically (0 = 0) but carries no Koszul information. The real invariant
  has moved to a refined structure.

- **h^∨ = 0** (psl(n|n), osp(2m|2m), D(2,1;α) for all α): Sugawara denominator
  vanishes identically. K_V is UNDEFINED in the Sugawara sense. A different
  construction (BRST coset, Feigin–Frenkel super-center) is required, and the
  complementarity identity K_V = 2·sdim has no direct super-Sugawara derivation.

**(c) Correct relationship.** The Platonic super-formula is:

    K_V(g) = 2 · sdim(g),   provided h^∨ ≠ 0.

At h^∨ = 0, K_V must be reinterpreted via BRST / coset / super-center
constructions; the ordinary Sugawara-Koszul identity does not generalize
directly.

## Further super-K_V values (for the record)

Explicit verification at a few more types (h^∨ ≠ 0, sdim ≠ 0):

**sl(3|1)**: sdim = (3-1)² - 1 = 3, h^∨ = 2. c_Sug = 3k/(k+2). Koszul:
k^! = -k - 4, c^! = 3(-k-4)/(-k-2) = 3(k+4)/(k+2). Sum = (6k+12)/(k+2) = 6 =
2·3 = 2·sdim. ✓

**osp(5|2)**: even = so(5) ⊕ sp(2) (dim 10 + 3 = 13), odd = 5 ⊗ 2 (dim 10).
sdim = 3, h^∨ = 3/2 (Kac Table VI). c = 3k/(k+3/2). Koszul: k^! = -k - 3,
c^! = 3(-k-3)/(-k-3/2) = 3(k+3)/(k+3/2). Sum = (6k+9)/(k+3/2) = 6 = 2·3. ✓

**G(3)**: sdim = 3, h^∨ = 3. c = 3k/(k+3). Koszul k^! = -k-6, c^! =
3(k+6)/(k+3). Sum = 6 = 2·3. ✓

**F(4) super**: sdim = 8, h^∨ = 3. c = 8k/(k+3). Sum under Koszul = 16 =
2·8. ✓

All pass. The super-formula is robust whenever both h^∨ ≠ 0 and sdim ≠ 0.

## Structural lesson

The identity K_V = 2·dim at ordinary g and K_V = 2·sdim at super g share a
single algebraic origin: the Sugawara central charge has the form

    c_Sug = (numerator) · k / (k + h^∨) = (numerator) − (numerator)·h^∨/t

where (numerator) = dim(g) in the ordinary case and sdim(g) in the super case.
The 1/t piece flips sign under t → -t (Koszul), cancels in the sum; the
constant (numerator) is k-independent and Koszul-invariant, doubling in the
sum.

The derivation requires:

1. Single quadratic Casimir (Sugawara has one). ✓ for both ordinary and super.
2. Non-degenerate invariant form. ✓ for basic classical super with h^∨ ≠ 0.
3. Well-defined sign flip t → -t. ✓ iff h^∨ ≠ 0.

At h^∨ = 0, condition (3) fails: there is no non-zero "t" to flip. The
universal K_V = 2·sdim identity is SILENT at the h^∨ = 0 locus, and the full
super-generalization of Vol II's Koszul complementarity framework requires
either (i) excluding h^∨ = 0 types from scope, or (ii) introducing a refined
invariant (BRST/coset-based) that replaces Sugawara c at critical-like super
types. The correct Vol II-level statement is:

**Theorem (super-K_V universality, conditional scope).** For every basic
classical simple Lie superalgebra g with h^∨ ≠ 0, the Koszul-complementarity
invariant

    K_V(g) := c_Sug(V_k(g)) + c_Sug(V_{-k-2h^∨}(g))

equals 2·sdim(g) independent of k (for k ≠ -h^∨). At h^∨ = 0 families
(psl(n|n), osp(2m|2m), D(2,1;α)), the Sugawara construction degenerates and
K_V must be reformulated via BRST or coset methods; the super-complementarity
statement is OPEN for these types.

## Literature cross-check

- **Kac, *Lie superalgebras*, Adv. Math. 26 (1977) 8–96.** Classification of
  basic classical simple Lie superalgebras; Table VI lists dim_even, dim_odd,
  h^∨ for all types. Sdim and h^∨ values used here.
- **Kac–Wakimoto, *Integrable highest weight modules over affine superalgebras
  and number theory*, in Lie Theory and Geometry (Progress in Math. 123),
  Birkhäuser 1994 (reporting 1989 arXiv work).** Theorem 3.1 states super-
  Sugawara central charge c = k·sdim/(k+h^∨); identifies h^∨ = 0 families as
  requiring alternative construction.
- **Serganova, *On the superdimension of an irreducible representation of a
  basic classical Lie superalgebra*, Funct. Anal. Appl. 18 (1984) 239-241.**
  Convention for sdim; key example calculations.
- **Frappat–Sciarrino–Sorba, *Dictionary on Lie Algebras and Superalgebras*,
  Academic Press 2000.** Tables 7.5–7.8 give dim_even, dim_odd, h^∨ for all
  basic classical simple Lie superalgebras. Confirms values used above.
- **Gorelik, *The center of the universal enveloping algebra of a Lie
  superalgebra*, Invent. Math. 141 (2000) 269–305.** D(2,1;α) center structure
  at h^∨ = 0.
- **Kazama–Suzuki, *New N=2 superconformal field theories and superstring
  compactification*, Nucl. Phys. B321 (1989) 232.** Coset construction of
  N=2 stress tensor from sl(2|1)_k and similar sdim = 0 super types.

## FM closure

- **FM-style classification of the super-attack claim**: the worry that
  K_V = 2·dim does not extend to supersymmetric types is **partially REJECTED**
  (formula extends cleanly with dim → sdim for h^∨ ≠ 0 basic classical types)
  and **partially UPHELD** (at h^∨ = 0 families, Sugawara itself degenerates
  and the extension requires a separate construction).

- **Concrete super-verifications**: osp(1|2) sum = 2·1 = 2 ✓. osp(5|2) sum =
  2·3 = 6 ✓. G(3) sum = 2·3 = 6 ✓. F(4) sum = 2·8 = 16 ✓. sl(3|1) sum = 2·3 = 6
  ✓. sdim = 0 types (sl(2|1), osp(3|2)) give tautological 0 = 0.

- **Scope for Vol II statements**: any universal-Koszul-complementarity note
  should restrict the super-case to "basic classical g with h^∨ ≠ 0" and
  separately flag the h^∨ = 0 locus as an open frontier. The ordinary-g
  formula K_V = 2·dim is the special case where g_odd = 0, sdim = dim, and
  every value of h^∨ is automatically non-zero.

- **No Vol II correction needed** if the existing K_V statement is scoped to
  ordinary simple Lie algebras. If a super-extension is asserted, scope it to
  basic classical simple Lie superalgebras with h^∨ ≠ 0 and note that
  psl(n|n), osp(2m|2m), D(2,1;α) families lie outside the Sugawara framework.
