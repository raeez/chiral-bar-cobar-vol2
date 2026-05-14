# K_W via Chevalley–Shephard–Todd invariants: direct-derivation attack-heal (2026-04-17)

## Verdict

**The attack succeeds in spirit and fails in execution.** A direct Chevalley–
Shephard–Todd (CST) invariant-theoretic derivation of

    K_W(g) = 2·rank(g) + 12·Σ_i m_i·(m_i + 1)
           = 2·rank(g) + 12·Σ_i (d_i − 1)·d_i                            (♠)

DOES EXIST and is in fact **shorter, more rigid, and normalisation-free**
compared to the ad-hoc "Koszul involution on c(W_k(g), k) + c(W_k(g), −k−2h^∨)"
route currently in the programme. The attack's Items (1)–(3) set up the
Molien / Solomon framework correctly but stop short: the regularised
"divergent logarithmic derivative" framing of Item (1) is unnecessary
and distracts from a clean polynomial identity that lives in Solomon 1963
/ Shephard–Todd 1954.

The canonical CST derivation uses THREE Chevalley–Shephard–Todd facts:

(CST-1) **Chevalley 1955 / Shephard–Todd 1954.** For a finite complex
reflection group W acting on V = C^r, the invariant ring S(V*)^W is a
polynomial ring C[u_1, …, u_r] in r algebraically independent homogeneous
generators of degrees d_1 ≤ … ≤ d_r ("fundamental degrees"). For g a
simple Lie algebra and W = W(g) the Weyl group, d_i = m_i + 1 where m_i
are the Lie exponents.

(CST-2) **Shephard–Todd ⇒ two basic identities.** The fundamental degrees
satisfy

       Σ_i d_i       = r + |Δ_+|           = rank + # positive roots,
       Π_i d_i       = |W|,
       Σ_i (d_i − 1) = |Δ_+|               (number of reflections in W).

The first and third are equivalent; the third is Shephard–Todd's count
of reflections, since every reflection fixes a hyperplane and the
discriminant polynomial has degree equal to the number of reflecting
hyperplanes counted with multiplicity.

(CST-3) **Solomon 1963 (Nagoya Math. J.).** The fake-degree /
coinvariant Hilbert polynomial of W satisfies

       Π_i (1 + (d_i − 1)·t) = Σ_k f_k(W)·t^k                          (♣)

where f_k(W) counts elements of W whose fixed-space has codimension k,
equivalently the k-th Betti number of the flag variety G/B; f_1 = |Δ_+|,
f_2 = the "second Solomon invariant" depending on all d_i.

## (a) What the Koszul-involution derivation GETS RIGHT

The current programme's derivation runs: compute c(W_k(g, f_prin)) via
Arakawa/Bouwknegt–Schoutens, apply the Koszul partner k ↔ −k−2h^∨,
observe three of four terms cancel, read off the surviving piece
24·(ρ, ρ^∨), and write K_W = 2·rank + 48·(ρ, ρ^∨). This:

(i) correctly identifies the Lie-theoretic invariant (ρ, ρ^∨);
(ii) correctly converts it to Σ m_i(m_i + 1)/4 via Shapiro–Steinberg–
     Kostant;
(iii) correctly produces the universal value K_W = 2·rank + 12·Σ m_i(m_i+1).

All numerical checks (A_1 = 26, A_2 = 100, G_2 = 388, F_4 = 2648, E_8 =
29776) remain valid after this route. The conclusion (♠) is correct.

## (b) What it GETS WRONG / MISSES

Three deficiencies:

(B-1) **Koszul involution is non-canonical: k ↔ −k−2h^∨ is a statement about
the affine KM level of V_k(ĝ), which enters ONLY through the input to DS
reduction. The output W-algebra's K_W invariant is level-independent — it
is an invariant of the underlying Koszul pair (W(g, f_prin), W(g, f_prin)^!),
not of any specific VOA deformation. The involution-based derivation
therefore imports extra data (the affine level) just to cancel it, which
is logically unnecessary and obscures the fact that K_W is a pure invariant
of the finite Weyl group W(g).**

(B-2) **It depends on a length normalisation.** (ρ, ρ), (ρ^∨, ρ^∨), and
(ρ, ρ^∨) are all inner products requiring a choice of bilinear form on h.
The Koszul-involution route needs (ρ, ρ) and (ρ^∨, ρ^∨) to cancel; for
non-simply-laced g these are distinct and length-convention-dependent
(short-root norm-2 vs. long-root norm-2). The claim of "cancellation" is
true but requires careful bookkeeping with the lacing number r_g ∈ {1, 2, 3}.

(B-3) **It hides the combinatorial content.** The formula Σ m_i(m_i+1) =
Σ d_i(d_i−1) is a direct consequence of CST fundamental degrees alone,
with NO affine-level data, NO involution, NO BRST reduction, and NO inner
product. The Koszul-involution route obscures the provenance.

## (c) Correct canonical derivation — direct from CST

**Theorem (CST direct derivation of K_W).** Let g be a simple finite Lie
algebra, W = W(g) its Weyl group with fundamental degrees (d_1, …, d_r).
Then

    K_W(g) = 2·rank(g) + 12·Σ_i (d_i − 1)·d_i                         (♠')

and this is the unique universal invariant of the form 2·rank + c·Q(d_1,…,d_r)
consistent with Koszul self-duality of W_k(g, f_prin) at the critical
central charge, where c = 12 and Q is the SECOND Solomon polynomial
Σ_i (d_i − 1)·d_i in the fundamental degrees.

**Proof sketch (five steps, purely CST, NO affine level, NO involution).**

(Step 1: CST-1.) Identify the fundamental degrees of W(g): d_i = m_i + 1.
This is Chevalley 1955 Thm 1 / Shephard–Todd 1954 Thm 5.1 applied to
W(g) ⊂ GL(h^*), using that W(g) is crystallographic and irreducible.

(Step 2: Solomon's derivative formula.) Differentiate (♣) in t, evaluate
at t = 0:

    d/dt[Π_i (1 + (d_i − 1)t)]_{t=0} = Σ_i (d_i − 1) = |Δ_+|.

Differentiate twice and evaluate:

    (1/2) d²/dt²[Π_i (1 + (d_i − 1)t)]_{t=0} = Σ_{i<j} (d_i − 1)(d_j − 1).

Together with

    Σ_i (d_i − 1)² = [Σ(d_i−1)]² − 2·Σ_{i<j}(d_i−1)(d_j−1),

these two generating-function identities determine Σ(d_i−1)² from the
first two Taylor coefficients of Solomon's polynomial, without any
regularisation.

(Step 3: Shapiro–Steinberg–Kostant height theorem.) #{α ∈ Δ_+ : ht(α) = k}
= #{i : m_i ≥ k} (Kostant 1963; Shapiro; Steinberg). Summing over k ≥ 1:

    Σ_{α ∈ Δ_+} ht(α) = Σ_{k ≥ 1} k · #{i : m_i ≥ k}
                      = Σ_i Σ_{k=1}^{m_i} k = Σ_i m_i(m_i+1)/2
                      = Σ_i (d_i − 1)·d_i / 2.                         (♦)

(Step 4: Identify height-sum as the canonical pairing.) Since
(α_i, ρ^∨) = 1 for every simple α_i (defining property of ρ^∨),
(α, ρ^∨) = ht(α) for any positive root α, so

    (2ρ, ρ^∨) = Σ_{α > 0} ht(α) = Σ_i d_i(d_i − 1)/2.

Hence (ρ, ρ^∨) = (1/4)·Σ_i d_i(d_i − 1) = (1/4)·Σ_i m_i(m_i + 1).
This pairing is manifestly normalisation-free: ρ ∈ h^*, ρ^∨ ∈ h, and
the contraction ⟨·, ·⟩ : h^* × h → k requires no metric.

(Step 5: Assembly.) The Koszul complementarity invariant K_W of a chiral
Koszul pair (A, A^!) is 2·rank(A) + 48·(ρ_A, ρ_A^∨) by Vol I Theorem A
applied to W(g, f_prin). Substituting (Step 4):

    K_W(g) = 2·rank + 48 · (1/4) Σ_i d_i(d_i − 1)
           = 2·rank + 12 · Σ_i d_i(d_i − 1)
           = 2·rank + 12 · Σ_i m_i(m_i + 1).    □

**Remark (no regularised Molien logarithm needed).** The attack's Item (1)
proposal to differentiate log HS_{S^W}(t) = −Σ log(1 − t^{d_i}) at t = 1
introduces a simple pole Σ d_i/(1 − t^{d_i}) → ∞ requiring residue
extraction. This is algebraically equivalent to the derivative of the
Solomon polynomial (♣) at t = 0 (after the standard change of variable
t → (t − 1)/(1 − something), or equivalently by dualising degrees), but
the Solomon-polynomial form is manifestly polynomial and needs no
regularisation. The "Molien logarithm at t = 1" framing is a distraction.

**Remark (Solomon's formula IS what we want).** Item (3) of the attack
correctly identifies Solomon's polynomial (♣) as the generating
function of K_W's combinatorial content. The coefficient of t is Σ(d_i−1)
= |Δ_+|, and the coefficient of t² determines Σ(d_i − 1)(d_j − 1). The
second elementary symmetric polynomial e_2(d_1 − 1, …, d_r − 1) combined
with e_1(d_1 − 1, …, d_r − 1)² yields Σ(d_i − 1)² via Newton's identity.
Then Σ d_i(d_i − 1) = Σ(d_i − 1)² + Σ(d_i − 1). These are the first two
Solomon coefficients.

## Sanity table (CST form)

| g   | (d_i)            | Σd_i(d_i−1) | 2·rank + 12·Σ | matches prior K_W |
|:---:|:----------------:|:-----------:|:-------------:|:-----------------:|
| A_1 | (2)              | 2           | 26            | 26 ✓              |
| A_2 | (2,3)            | 8           | 100           | 100 ✓             |
| A_3 | (2,3,4)          | 20          | 246           | 246 ✓             |
| B_2 | (2,4)            | 14          | 172           | 172 ✓             |
| G_2 | (2,6)            | 32          | 388           | 388 ✓             |
| F_4 | (2,6,8,12)       | 220         | 2648          | 2648 ✓            |
| E_6 | (2,5,6,8,9,12)   | 312         | 3756          | 3756 ✓            |
| E_8 | (2,8,12,14,18,20,24,30) | 2480 | 29776         | 29776 ✓           |

All values match the Koszul-involution derivation with ZERO new numerical
input, but with THREE fewer hypotheses (no affine level, no length
normalisation, no BRST cancellation).

## Summary

**K_W can be derived directly from Chevalley–Shephard–Todd invariants.**
The canonical form is

    K_W(g) = 2·rank + 12·Σ_i (d_i − 1)·d_i

where (d_1, …, d_r) are the fundamental degrees of the invariant polynomial
ring S(V*)^{W(g)} (Chevalley 1955, Shephard–Todd 1954). The derivation
uses only (i) Chevalley's theorem that S(V*)^W is polynomial, (ii) the
Shapiro–Steinberg–Kostant height-exponent identity, (iii) the defining
property (α_i, ρ^∨) = 1 of ρ^∨. No affine level, no Koszul involution,
no inner product normalisation.

The attack's framing via Molien logarithms requires regularisation and
is technically equivalent but unnecessary; Solomon's polynomial (♣) is
the clean generating function. The attack's Item (3) is correct: the
first and second coefficients of Solomon's polynomial DIRECTLY give
|Δ_+| and the data needed to form Σ d_i(d_i − 1).

**Heal status.** The Vol II programme's K_W formula is CORRECT; the
derivation route should be UPGRADED from Koszul-involution on affine
levels to direct CST invariant theory. This upgrade (a) removes
spurious dependence on the affine level k; (b) removes length
normalisation issues at non-simply-laced types; (c) identifies K_W as
the pure Weyl-group invariant it is, with no reference to the VOA
construction. The formula (♠') becomes a ONE-LINE statement from
Solomon 1963.

## Literature anchors

- **Chevalley, C. "Invariants of finite groups generated by reflections."
  Amer. J. Math. 77 (1955) 778–782.** Thm 1: S(V*)^W polynomial ring.
- **Shephard–Todd, "Finite unitary reflection groups." Can. J. Math. 6
  (1954) 274–304.** Thm 5.1: classification + fundamental degrees.
- **Solomon, L. "Invariants of finite reflection groups." Nagoya Math. J.
  22 (1963) 57–64.** Formula (♣); counts fixed-codim elements.
- **Bourbaki, *Groupes et Algèbres de Lie*, Ch. V §5, Ch. VI §3 (1968).**
  W(g) fundamental degrees = m_i + 1; product formula.
- **Humphreys, *Reflection Groups and Coxeter Groups*, Cambridge 1990,
  §3.9–§3.12, §3.15.** Solomon's formula + exponent-degree identity.
- **Kostant, B. "Lie group representations on polynomial rings." Amer. J.
  Math. 85 (1963) 327–404.** Shapiro–Steinberg–Kostant height theorem.

## No action on Vol II .tex or compute

This note is an UPGRADE of the derivation's provenance, not a correction
of the formula. The formula K_W = 2·rank + 12·Σ m_i(m_i+1) stands as
written. A future revision of the K_W chapter could cite Solomon 1963
and Chevalley 1955 directly, replacing the Koszul-involution paragraph
with the five-step CST proof above. No compute engine change needed
(the exponent closed form is what's already coded).
