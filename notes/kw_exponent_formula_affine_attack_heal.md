# K_W exponent formula: affine attack-heal (adversarial audit 2026-04-17)

## Verdict

**The attack contains a category error.** The universal exponent-theoretic
formula

    K_W(W_k(g, f_prin)) = 2·rank(g) + 12·Σ_i m_i·(m_i + 1)

with m_i the FINITE simple exponents of g is ALREADY the formula for the
"affine W-algebra" in the sense of Arakawa / Feigin–Frenkel — namely the
principal W-algebra W_k(g, f_prin) obtained by Drinfeld–Sokolov reduction
of the AFFINE vertex algebra V_k(g). The attack conflates two unrelated
objects:

(I) **W_k(g, f_prin)**: the VOA output of DS reduction of V_k(ĝ). Its
central charge is governed by the FINITE simple exponents of g (not
Kac–Moody affine exponents), and the formula

    c(W_k(g, f_prin)) = rank(g) − 12(ρ, ρ)/t − 12 t (ρ^∨, ρ^∨) + 24(ρ, ρ^∨)

with t = k + h^∨ is EXACTLY the same Bouwknegt–Schoutens / Arakawa formula
that was analysed in the finite attack. The "affine" in "affine W-algebra"
refers to the input V_k(ĝ) being an affine chiral algebra, NOT to a
second affinisation of the exponent sum.

(II) **A hypothetical W((ĝ)^(1), _)**: the DS reduction of a
double-affinisation (toroidal / iterated loop). The Feigin–Frenkel /
Arakawa framework used in Vol II does NOT operate at this level. The
central charge of such a hypothetical object would not be computed by
the same Kac-style formula, because the underlying quadratic Casimir
ceases to be finite-dimensional.

Therefore the "new attack" collapses into the already-resolved finite
statement. There is no independent affine K_W to attack.

## Correct reading of the framework

The Vol II programme's W-algebras are:

- **W_k(g, f)** for g FINITE simple (A_n, ..., G_2), f a nilpotent.
- Built from V_k(ĝ) — the AFFINE vertex algebra of ĝ^(1) at level k.
- The DS reduction is taken with respect to the PRINCIPAL (or other)
  nilpotent IN THE FINITE g, not in ĝ.

The exponents entering c(W_k(g, f_prin)) are the finite exponents
{m_1, …, m_r} of g; they index the STRONG GENERATORS of W_k(g, f_prin),
one for each m_i (generator of conformal weight m_i + 1). There are
finitely many strong generators (= rank(g)), so the exponent sum
Σ_i m_i·(m_i+1) is finite and well-defined.

In particular W_k(sl_2, f_prin) = Virasoro (one strong generator, the
stress tensor T, at m_1 = 1, conformal weight 2); W_k(sl_3) = Zamolodchikov
W_3 (two strong generators T, W^(3) at m_1 = 1, m_2 = 2, weights 2, 3);
W_k(g_2) = 2 strong generators at m_1 = 1, m_2 = 5 (weights 2, 6), and so on.

There is no "infinite height" for the strong generators of W_k(g, f_prin).

## Why the attack's Item (1) fails

Item (1) proposes the enumeration of "affine exponents {m_i^fin + n·h}"
and summing Σ m(m+1) over the double index (i, n).

These "affine exponents" {m_i + n·h} ARE a real object — they are the
**affine exponents of ĝ^(1) as a Kac–Moody algebra**, appearing in:

- the Weyl denominator formula for ĝ,
- the string function and branching function asymptotics,
- Macdonald identities (eta-function power expansions),
- the finite-dimensional irreducible representations of the horizontal
  subalgebra labelled by heights.

They are NOT the exponents of the Drinfeld–Sokolov reduction. The DS
reduction is a chiral BRST construction that strictly outputs a VOA with
rank(g) strong generators (finite), and its central charge involves ONLY
(ρ, ρ), (ρ, ρ^∨), (ρ^∨, ρ^∨) of the FINITE root system.

If one naively substituted the affine exponents into the K_W formula:

    Σ_{i,n ≥ 0} (m_i + n·h)·(m_i + n·h + 1)

the sum diverges quadratically in N when truncated. Weighting by q^n
gives a generating series

    Σ_n q^n · Σ_i (m_i + n·h)(m_i + n·h + 1)
    = [const]/(1-q) + [linear]/(1-q)^2 + [quad]/(1-q)^3,

which has poles of orders 1, 2, 3 at q = 1. No finite regularisation of
this series equals the DS W-algebra central charge. The reason: the DS
reduction at a principal nilpotent of the FINITE g kills ALL affine
direction data (horizontal gradation) except through the level k, so the
infinite tower of affine exponents never enters.

## Why the attack's Item (2) fails

Item (2) asks for a regularisation of Σ (m_i + nh)(m_i + nh + 1) via
q-series or residue extraction. The following explicit check shows no
such regularisation exists that reproduces c(W_k(g, f_prin)):

**sl_2 example.** Finite exponent m_1 = 1; Coxeter h = 2. Affine exponents
{1, 3, 5, 7, …}. Naive:

    Σ_{n ≥ 0} (2n+1)(2n+2) = Σ (4n^2 + 6n + 2) = (4/3)·N^3 + …

Zeta-regularised, using Σ n = -1/12 and Σ n^2 = 0:

    4·ζ(-2) + 6·ζ(-1) + 2·ζ(0) = 0 − 6/12 − 1 = −3/2.

Then "regularised K_W(ŝl_2)" = 2 + 12·(−3/2) = −16. But the ACTUAL
K_W(W(sl_2, f_prin)) = K_W(Virasoro) = 2 + 12·1·2 = 26 (this is the
Koszul self-duality of Vir at c^Kos = 13). These do not agree.

Other regularisations (residue at q=1 of [const]/(1-q), q-derivative at
q=0, Cesàro, etc.) likewise fail to reproduce 26. The affine exponent
sum has no connection to the DS W-algebra central charge.

**sl_3 check.** Finite exponents (1, 2), h = 3. Affine exponents
{1, 2, 4, 5, 7, 8, …}. Naive Σ m(m+1) over the first two periods:
2 + 6 + 20 + 30 + … divergent. Zeta-regularised:

    Σ_i Σ_{n ≥ 0} (m_i + 3n)(m_i + 3n + 1)
    = Σ_i (ζ-regularisation of quadratic poly in n)

gives finite but arbitrary number depending on regularisation scheme.
Actual K_W(W_3) = 2·2 + 12·(2 + 6) = 100 (finite, no divergence).
No match.

## Why the attack's Item (3) fails

Item (3) proposes K_V(ĝ) = 2·sdim(ĝ) with sdim the affine
superdimension via character sum. This ALSO conflates two things:

The Vol II K_V invariant is K_V(V_k(g)) = 2·dim(g) for g FINITE simple,
computed from Sugawara's c = k·dim(g)/(k + h^∨) and the Koszul partner
k ↔ −k−2h^∨. The "dim(g)" appearing here is the FINITE dimension of g,
not an affine superdimension. The attack's Item (3) even concedes this:
"V_κ(ĝ) itself is a chiral algebra, not a Lie algebra", so "K_V(ĝ)"
is ambiguous.

The CORRECT Vol II invariant is K_V(g) = 2·dim(g), with g finite and
V_k(g) denoting the affine chiral algebra built from ĝ. There is no
"double affinisation" in the programme.

## Three-step protocol

**(a) What does the K_W exponent formula GET RIGHT?**

K_W(W_k(g, f_prin)) = 2·rank(g) + 12·Σ_i m_i·(m_i + 1) is universally
correct for ALL finite simple Lie algebras g (simply-laced and
non-simply-laced), computed with the FINITE exponents of g. Verified at:

- A_1 (Virasoro): 2·1 + 12·(1·2) = 26 ✓
- A_2 (W_3): 2·2 + 12·(1·2 + 2·3) = 4 + 96 = 100 ✓
- G_2: 2·2 + 12·(1·2 + 5·6) = 4 + 384 = 388 ✓
- F_4: 2·4 + 12·(2 + 30 + 56 + 132) = 8 + 2640 = 2648 ✓
- E_8: 2·8 + 12·Σ m(m+1) over (1,7,11,13,17,19,23,29) = 29776 ✓

The formula is universal precisely because:

(i) DS reduction produces rank(g)-many strong generators at conformal
weights m_i + 1;
(ii) Arakawa's BRST central charge formula has four pieces, three of
which cancel under the Koszul involution t → −t;
(iii) The surviving cross-term 24(ρ, ρ^∨) has a universal exponent
form (ρ, ρ^∨) = (1/4)·Σ m_i(m_i+1), via the Shapiro–Steinberg–Kostant
height-exponent theorem.

**(b) What does the AFFINE extension GET WRONG?**

The naive "affine exponents" substitution {m_i + n·h} fails because:

(i) It confuses the affine Kac–Moody exponents (Weyl denominator /
Macdonald / string functions) with the exponents entering c(W_k(g, f)).
The two are unrelated objects living in different constructions.

(ii) The DS reduction of V_k(ĝ) at a principal nilpotent of the FINITE
g outputs a VOA with rank(g) strong generators (finite, not infinite).
The exponent sum Σ_i m_i(m_i+1) over these finite exponents is already
the correct sum.

(iii) Regularising a divergent affine-exponent sum gives values that do
not match the known c(W_k(g, f_prin)). Explicit sl_2 zeta-regularisation
yields −16, not 26.

**(c) CORRECT RELATIONSHIP.**

For ALL simple finite g and ALL non-critical k ≠ −h^∨:

    K_W(W_k(g, f_prin)) = 2·rank(g) + 12·Σ_{i=1}^{rank g} m_i(m_i + 1)

with m_i the finite simple exponents. This is the complete universal
formula. There is no doubly-affine extension.

The "affine W-algebra" terminology in Arakawa / Feigin–Frenkel refers
to the INPUT being V_k(ĝ), not to a second affinisation of the output
W-algebra. The W-algebra W_k(g, f_prin) is a finitely strongly generated
chiral algebra (dimension rank(g) of strong generators) whose central
charge is controlled by finite root-system data.

## Genuine extensions (where the attack CAN be reformulated)

There exist settings where "affine W-algebras with infinite height"
genuinely appear, but they are not attacks on the universal exponent
formula — they are DIFFERENT objects:

**W_∞[μ]** (Pope-Romans-Shen, Gaberdiel-Gopakumar 2012): the W-algebra
obtained as the large-N limit of W_N at a fixed 't Hooft parameter. Its
strong generators DO form an infinite tower (T, W^(3), W^(4), …) with
conformal weights 2, 3, 4, … extending to all integers. Central charge
is an explicit analytic function c(μ, λ) computed in Gaberdiel–Gopakumar,
with no Koszul partner of the form (μ, λ) ↔ (−μ−2, λ) yielding a finite
K_W.

**Toroidal algebras** (Miki, Feigin–Odesskii, Schiffmann–Vasserot): the
affine quantum toroidal algebra U_q(gl_N^{tor}) has doubly-infinite
grading and the associated "W-algebra-at-toroidal-level" has infinitely
many strong generators. Central charges are rational functions of two
parameters, and the Koszul complementarity framework does not extend
trivially.

Neither setting falsifies the universal formula at W_k(g, f_prin). They
are distinct objects governed by distinct structure theorems.

## Status

- **Affine W-algebra in Arakawa sense**: already covered by the finite
  exponent formula. No divergence, no regularisation, no extension.
- **Double-affine (toroidal) W**: a separate genuine frontier, not
  addressed by K_W = 2·rank + 12·Σ m(m+1).
- **K_V "affinisation"**: not well-defined; Vol II K_V is always
  K_V(g) = 2·dim(g) with g finite.

The universal finite formula survives the attack unchanged. The attack's
premise (that W_k(g, f_prin) has infinitely many generators at "affine
exponents {m_i + nh}") is a category error: it conflates the Kac–Moody
affine exponents with the DS exponents, which govern different constructions.

## Literature cross-check

- **Kac, *Infinite Dimensional Lie Algebras*, 3rd ed., Ch. 7.** Affine
  exponents appear as {m_i + n·h : 1 ≤ i ≤ r, n ≥ 0} in the context of
  Weyl–Kac denominator and string functions. NOT in W-algebra construction.
- **Arakawa, "Representation theory of W-algebras", Invent. Math. 169
  (2007), 219–320.** Defines W_k(g, f) = H_{DS}^0(V_k(g)) for g finite;
  central charge formula uses finite (ρ, ρ), (ρ, ρ^∨), (ρ^∨, ρ^∨).
  No affine exponent sum.
- **Feigin–Frenkel, "Affine Kac–Moody algebras at the critical level",
  Phys. Lett. B 246 (1990) 75–81; "Affine Kac–Moody algebras and
  semi-infinite flag manifolds", Commun. Math. Phys. 128 (1990) 161–189.**
  Critical-level Feigin–Frenkel centre for V_{−h^∨}(ĝ); no affine-exponent
  K_W. Polynomial algebra in Σ_{i,n ≥ 0} T_{i,n} is the OPER STRUCTURE,
  distinct from W-algebra central charge.
- **Bouwknegt–Schoutens, "W symmetry in conformal field theory", Phys.
  Rep. 223 (1993).** §3.2 gives c(W_k(g, f_prin)) = rank(g) − 12(ρ, ρ)/t
  − 12t(ρ^∨, ρ^∨) + 24(ρ, ρ^∨) for finite g. No affine variant.
- **Frenkel–Ben-Zvi, *Vertex Algebras and Algebraic Curves*, 2nd ed.,
  AMS 2004, §15.** DS reduction in VOA language, same finite formula.

All sources confirm: the W-algebra output of DS reduction of V_k(ĝ) has
central charge governed by FINITE exponents of g. No source uses affine
exponents in c(W_k(g, f)).

## FM-class diagnosis

The attack is a textbook example of **AP-CY62-style geometric/algebraic
conflation applied to exponents**: the "affine exponents" as a Kac–Moody
Lie-theoretic object vs. the "W-algebra exponents" as the conformal-weight
shifts of strong generators. Both are called "exponents" in the literature
but refer to distinct structures:

- Kac–Moody affine exponents: asymptotic data of ĝ as an infinite-rank
  Lie algebra (Weyl denominator, string functions, Macdonald identities).
- W-algebra exponents: finite set m_1, …, m_r indexing the strong
  generators of W_k(g, f_prin).

The correct counter to the confusion: specify which construction produces
the exponents. For K_W(W_k(g, f_prin)), always the FINITE simple exponents.

## No action needed on Vol II

- No .tex edit: the manuscript already uses the finite formula correctly.
- No compute engine change: `ds_brst_sc_engine.py` and
  `modular_pva_quantization.py` both use (ρ, ρ^∨) in finite form, which
  is equivalent to Σ m(m+1)/4 via Shapiro–Steinberg–Kostant.
- No cross-volume propagation: the finite formula is the final form; no
  double-affine analogue enters Vols I, II, or III.

**K_W(W_k(g, f_prin)) = 2·rank(g) + 12·Σ_i m_i·(m_i + 1) is the complete
universal formula; no affine extension exists.**
