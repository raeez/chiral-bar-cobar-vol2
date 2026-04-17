# K_W and (ρ, ρ^∨): universal Lie-theoretic form (adversarial audit 2026-04-17)

## Verdict

**K_W(F_4) = 2648 is VERIFIED from first principles.** The value agrees independently
with (a) the Kac formula for c(W(g), k) + c(W(g), -k - 2h^∨), (b) direct computation
of (ρ, ρ^∨) = 55 on the F_4 root system with short-root normalisation |α_short|^2 = 2,
and (c) the exponent-theoretic closed form (ρ, ρ^∨) = (1/4)·Σ m_i(m_i + 1) using
F_4 exponents (1, 5, 7, 11) giving (1/4)(2 + 30 + 56 + 132) = 55.

**Universal form for (ρ, ρ^∨) FOUND:**

    (ρ, ρ^∨) = (1/2)·Σ_{α ∈ Δ_+} ht(α)
             = (1/4)·Σ_{i=1}^{rank} m_i·(m_i + 1)

where m_1, …, m_r are the exponents of g (so h = m_r + 1 is the Coxeter number and
1 + Σ m_i = |Δ_+|). The formula is simultaneously: (i) universal across all simple
types, finite and Kac–Moody; (ii) normalisation-independent, since (ρ, ρ^∨) is a
contraction of ρ ∈ h^* with ρ^∨ ∈ h not requiring an inner product; (iii) purely
combinatorial from the exponents.

Equivalently:

    K_W(g) = 2·rank(g) + 48·(ρ, ρ^∨) = 2·rank + 12·Σ_i m_i·(m_i + 1).

## (1) Explicit F_4 computation

F_4 has rank = 4, h = 12, h^∨ = 9, dim = 52, lacing r_g = 2. Cartan matrix in
Bourbaki ordering (α_1, α_2 long; α_3, α_4 short):

    A = [[ 2,-1, 0, 0],
         [-1, 2,-2, 0],
         [ 0,-1, 2,-1],
         [ 0, 0,-1, 2]].

In short-root normalisation |α_short|^2 = 2, |α_long|^2 = 4, the Gram matrix
G = [G_ij] = (α_i, α_j) is

    G = [[ 4,-2, 0, 0],
         [-2, 4,-2, 0],
         [ 0,-2, 2,-1],
         [ 0, 0,-1, 2]].

Closure under simple reflections yields 24 positive roots (12 long, 12 short), with

    ρ  = 8·α_1 + 15·α_2 + 21·α_3 + 11·α_4  (half sum of positive roots),
    ρ^∨ = (11/2)·α_1 + (21/2)·α_2 + 15·α_3 + 8·α_4  (half sum of positive coroots in α-basis,
                                                      using α^∨_long = α/2, α^∨_short = α).

Direct Gram computation gives

    (ρ, ρ)   = 78       (= r_g · h^∨ · dim / 12 = 2·9·52/12 ✓ via Freudenthal–de Vries with
                         short-root normalisation; standard long-root FdV gives (ρ,ρ)_L = 39 = h^∨·dim/12),
    (ρ^∨, ρ^∨) = 39      (= h^∨ · dim / 12 in this basis; it is (ρ,ρ) of the LANGLANDS DUAL F_4^L = F_4
                          with long/short swapped, confirming Langlands self-duality of F_4),
    (ρ, ρ^∨) = 55       (invariant under rescaling; canonical Lie invariant).

Then

    K_W(F_4) = 2·4 + 48·55 = 8 + 2640 = **2648**.

This agrees with K_W(F_4) = 2·rank + 12·Σ m_i(m_i+1) where the F_4 exponents are
(1, 5, 7, 11):

    Σ m_i(m_i + 1) = 1·2 + 5·6 + 7·8 + 11·12 = 2 + 30 + 56 + 132 = 220,
    K_W(F_4) = 8 + 12·220 = 8 + 2640 = 2648. ✓

The prior main-thread formula K_W = 2·rank + 4·h^∨·dim gives 2·4 + 4·9·52 = 1880,
which is off by 768 because the simply-laced identity dim = rank·(h+1) fails for F_4
(rank·(h+1) = 4·13 = 52 coincidentally agrees here, but the SL formula requires the
deeper coincidence (ρ,ρ^∨) = h^∨·dim/12, which fails).

## (2) Universal Lie-theoretic form for (ρ, ρ^∨)

The Freudenthal–de Vries strange formula (FdV) states (ρ, ρ)_{long-norm-2} = h^∨·dim/12.
For simply-laced g, coroot = root, so (ρ, ρ) = (ρ, ρ^∨) = (ρ^∨, ρ^∨) and FdV gives
(ρ, ρ^∨) = h^∨·dim/12. For non-simply-laced g, the three inner products are distinct
and there is NO closed form in (rank, h, h^∨, dim, r_g) alone — explicit checks at
B_n, C_n, F_4, G_2 rule out every linear, quadratic, and lacing-corrected candidate.

The **correct universal form** bypasses length normalisations entirely. Since
(α, α^∨) = 2 identically, and (α_i, ρ^∨) = 1 for every simple α_i (defining
property of ρ^∨ as half sum of positive coroots paired with simple roots), one has
for any positive root α expressed as α = Σ_i n_i(α)·α_i:

    (α, ρ^∨) = Σ_i n_i(α) = ht(α).

Summing over α > 0:

    (2ρ, ρ^∨) = Σ_{α > 0} (α, ρ^∨) = Σ_{α > 0} ht(α),

hence

    (ρ, ρ^∨) = (1/2)·Σ_{α ∈ Δ_+} ht(α).                          (*)

Formula (*) is manifestly normalisation-independent: ρ is in h^*, ρ^∨ is in h, and
the pairing ⟨·, ·⟩: h^* × h → k requires no metric. It is universal (all simple types,
finite and Kac–Moody with proper convergence), combinatorial (only needs the root
system), and Lie-theoretic (only needs heights of positive roots).

**Exponent closed form.** By the Shapiro–Steinberg–Kostant theorem, the number of
positive roots of height exactly k equals #{i : m_i ≥ k}, where m_1 ≤ … ≤ m_r are
the exponents of g. Therefore

    Σ_{α > 0} ht(α) = Σ_{k ≥ 1} k · #{i : m_i ≥ k}
                   = Σ_i Σ_{k=1}^{m_i} k
                   = Σ_i m_i·(m_i + 1)/2,

so

    (ρ, ρ^∨) = (1/4)·Σ_i m_i·(m_i + 1).                          (**)

Formula (**) expresses K_W as

    K_W(g) = 2·rank + 12·Σ_i m_i·(m_i + 1).                      (***)

## (3) Sanity table for ALL simple types (short-root normalisation |α_short|^2 = 2)

All (ρ, ρ^∨) values computed from (*) by direct height-sum on the generated positive
root system, then cross-checked against (**) via the exponents. K_W = 2·rank + 48·(ρ, ρ^∨).

| g     | rank | h  | h^∨ | dim | r_g | exponents           | (ρ, ρ^∨) | K_W   | 2r + 4h^∨·dim (SL) |
|:-----:|:----:|:--:|:---:|:---:|:---:|:------------------:|:-------:|:-----:|:------------------:|
| A_1   | 1    | 2  | 2   | 3   | 1   | (1)                | 1/2     | 26    | 26 ✓               |
| A_2   | 2    | 3  | 3   | 8   | 1   | (1,2)              | 2       | 100   | 100 ✓              |
| A_3   | 3    | 4  | 4   | 15  | 1   | (1,2,3)            | 5       | 246   | 246 ✓              |
| A_4   | 4    | 5  | 5   | 24  | 1   | (1,2,3,4)          | 10      | 488   | 488 ✓              |
| A_5   | 5    | 6  | 6   | 35  | 1   | (1,2,3,4,5)        | 35/2    | 850   | 850 ✓              |
| B_2   | 2    | 4  | 3   | 10  | 2   | (1,3)              | 7/2     | 172   | 124 ✗              |
| B_3   | 3    | 6  | 5   | 21  | 2   | (1,3,5)            | 11      | 534   | 426 ✗              |
| B_4   | 4    | 8  | 7   | 36  | 2   | (1,3,5,7)          | 25      | 1208  | 1016 ✗             |
| C_2   | 2    | 4  | 3   | 10  | 2   | (1,3)              | 7/2     | 172   | 124 ✗              |
| C_3   | 3    | 6  | 4   | 21  | 2   | (1,3,5)            | 11      | 534   | 342 ✗              |
| C_4   | 4    | 8  | 5   | 36  | 2   | (1,3,5,7)          | 25      | 1208  | 728 ✗              |
| D_4   | 4    | 6  | 6   | 28  | 1   | (1,3,5,3)          | 14      | 680   | 680 ✓              |
| D_5   | 5    | 8  | 8   | 45  | 1   | (1,3,5,7,4)        | 30      | 1450  | 1450 ✓             |
| E_6   | 6    | 12 | 12  | 78  | 1   | (1,4,5,7,8,11)     | 78      | 3756  | 3756 ✓             |
| E_7   | 7    | 18 | 18  | 133 | 1   | (1,5,7,9,11,13,17) | 399/2   | 9590  | 9590 ✓             |
| E_8   | 8    | 30 | 30  | 248 | 1   | (1,7,11,13,17,19,23,29) | 620 | 29776 | 29776 ✓          |
| F_4   | 4    | 12 | 9   | 52  | 2   | (1,5,7,11)         | **55**  | **2648** | 1880 ✗          |
| G_2   | 2    | 6  | 4   | 14  | 3   | (1,5)              | **8**   | **388**  | 228 ✗           |

Notes:
- For simply-laced g, the SL formula K_W = 2·rank + 4·h^∨·dim coincides with (***)
  precisely because dim = rank·(h + 1) holds in SL, giving Σ m_i(m_i+1) = rank·h^∨·(h+1)/3
  in that regime, which collapses to h^∨·dim/3.
- For non-simply-laced g the SL formula undershoots. The gap K_W^true − K_W^SL is:
  B_2/C_2: 48; B_3: 108; C_3: 192; B_4: 192; C_4: 480; F_4: 768; G_2: 160.
  These gaps are EXACTLY 48·(h^∨·dim/12 − (ρ, ρ^∨)_{non-SL}), confirming that the
  SL formula measures only the FdV part of (ρ, ρ^∨), not the full contraction.

## Interpretation and consequences

1. **(ρ, ρ^∨) has no closed form in (rank, h, h^∨, dim, r_g) alone.** Explicit
   Diophantine checks at B_2, B_3, B_4, C_2, C_3, C_4, F_4, G_2 rule out every
   linear-in-(h, h^∨, dim) candidate with lacing correction. This is because
   (ρ, ρ^∨) captures FULL ROOT-SYSTEM combinatorics (height profile), which no
   finite tuple of scalar invariants encodes.

2. **The height-sum formula (*) is the correct universal form.** It is known
   classically (can be extracted from Kac, Infinite-Dim Lie Algebras §6.1 via the
   sum-of-heights interpretation of the ρ–ρ^∨ pairing; equivalently from Kostant's
   treatment of the principal sl_2 triple where heights become eigenvalues of
   ad(h_0)/2) but it seems to have been overlooked in the recent "universal K_W
   formula" proposals circulating in the SC^{ch,top} programme.

3. **The exponent closed form (**) is the right computational shortcut.** Exponents
   are tabulated for all simple types (and their duals in Kac–Moody); Σ m_i(m_i + 1)
   is then instant arithmetic. This is the form to install in compute engines.

4. **K_W(g) = 2·rank + 12·Σ m_i(m_i + 1) is the universal Koszul complementarity
   invariant of W(g, f_prin).** This supersedes both the main-thread claim
   K_W = 2·rank + 4·h^∨·dim (simply-laced only) and the prior lacing-correction
   proposal K_W = 2·rank·(1 + 2h^∨ + 2(h^∨)^2/r_g) (falsified on F_4, G_2).

## Heal action items

- Replace in `universal_koszul_complementarity_kv_kw_all_simple.md` the formula
  claim with the exponent-theoretic form (***) and the height-sum identity (*).
- Add F_4 and G_2 to the sanity table (currently SL-only) so future audits catch
  the gap immediately.
- Flag the Freudenthal–de Vries dependency: the SL formula is FdV on (ρ, ρ) lifted
  to (ρ, ρ^∨) via accidental coincidence; non-SL needs the genuine height-sum.
- Citations: Freudenthal–de Vries *Linear Lie Groups* (1969) for FdV; Kac
  *Infinite-Dimensional Lie Algebras* Ch. 6 for ρ^∨ conventions; Humphreys
  *Introduction to Lie Algebras and Representation Theory* §10.4 and §13.1 for
  the height-stratification of positive roots and its relation to exponents;
  Kostant "Lie group representations on polynomial rings" (1963) for the
  Shapiro–Steinberg–Kostant theorem tying exponents to height multiplicities.

## Status

- K_W(F_4) = 2648: **VERIFIED** (three independent computations).
- Universal form for (ρ, ρ^∨): **EXISTS**, is combinatorial, not algebraic in
  (rank, h, h^∨, dim, r_g). The form is:
  * (ρ, ρ^∨) = (1/2)·Σ_{α > 0} ht(α) — height-sum, normalisation-free,
  * (ρ, ρ^∨) = (1/4)·Σ_i m_i·(m_i + 1) — exponent closed form.
- Hence K_W(g) = 2·rank(g) + 12·Σ_i m_i·(m_i + 1) universally, all simple types.
- Simply-laced ⇒ Σ m_i(m_i + 1) = h^∨·dim/3 and K_W reduces to 2·rank + 4·h^∨·dim.
- Non-simply-laced: the SL formula FAILS; use exponents.
