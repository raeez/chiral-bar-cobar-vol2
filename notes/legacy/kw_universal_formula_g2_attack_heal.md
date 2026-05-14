# K_W universal formula: G_2 attack-heal (adversarial audit 2026-04-17)

## Verdict

**K_W(G_2) = 228 is FALSIFIED.** From first-principles Kac / Fateev-Lukyanov /
Bouwknegt-Schoutens central charge for the principal W-algebra, K_W(G_2) = 388.
The session-proposed universal formula K_W(g) = 2·rank(g) + 4·h^∨(g)·dim(g) holds
ONLY for simply-laced g. For non-simply-laced g it fails: the correct universal
formula is K_W(g) = 2·rank(g) + 48·(ρ, ρ^∨) computed in the normalization where
LONG roots have length^2 = 2.

The existing Vol II note `universal_koszul_complementarity_kv_kw_all_simple.md`
also proposes a lacing-corrected variant K_W(g) = 2·rank·(1 + 2h^∨ + 2(h^∨)^2/r_g).
This is ALSO FALSIFIED: for G_2 it gives 236/3 (non-integer!) and for F_4 it
gives 800, while the exact values are 388 and 2648 respectively. The r_g^{-1}
correction is DIRECTIONALLY WRONG — the non-simply-laced K_W is LARGER than the
naive SL formula predicts, not smaller.

## First-principles computation

G_2 root system with long roots normalized to length^2 = 2:

- Simple roots: α_1 short (|α_1|^2 = 2/3), α_2 long (|α_2|^2 = 2), (α_1, α_2) = -1.
- Cartan matrix [[2, -1], [-3, 2]], det = 1.
- 6 positive roots: α_1, α_2, α_1+α_2, 2α_1+α_2 (short, length^2=2/3);
  α_2, 3α_1+α_2, 3α_1+2α_2 (long, length^2=2). Pos root count 6 = 2·h^∨ ·rank/2 · (fraction).
- ρ = 5α_1 + 3α_2 (half sum of positive roots).
- Coroots: α_i^∨ = 2α_i/(α_i, α_i). Short coroot = 3·(short root); long coroot = long root.
- ρ^∨ = 9α_1 + 5α_2.

Explicit inner products (long-norm-2 form):

- **(ρ, ρ) = 14/3** — matches the Freudenthal-de Vries strange formula
  (ρ, ρ) = h^∨ · dim(g) / 12 = 4·14/12 = 14/3. ✓
- **(ρ^∨, ρ^∨) = 14** — matches r_g · h^∨ · dim / 12 = 3·4·14/12 = 14. (Empirical pattern
  verified separately on C_2 below.)
- **(ρ, ρ^∨) = 8** — does NOT match h^∨·dim/12 = 14/3.

## Kac formula verification

Bouwknegt-Schoutens / Arakawa central charge for principal W-algebra:

c(W(g), k) = rank(g) - 12(ρ, ρ)/t - 12·t·(ρ^∨, ρ^∨) + 24·(ρ, ρ^∨),   t = k + h^∨.

Under Koszul partner k ↔ k^∨ = -k - 2h^∨, one has t ↔ -t, so the t-dependent
terms cancel in the sum and

K_W(g) := c(W(g), k) + c(W(g), k^∨) = 2·rank(g) + 48·(ρ, ρ^∨).

This is an IDENTITY of the Kac formula, not a conjecture. Plugging in G_2:

K_W(G_2) = 2·2 + 48·8 = **388**.

## Three-step protocol

**(a) What the attack claim K_W = 2·rank + 4·h^∨·dim GETS RIGHT.** Simply-laced
exactness: for every simply-laced g, coroot = root so (ρ, ρ^∨) = (ρ, ρ) =
h^∨·dim/12 (Freudenthal-de Vries), hence K_W(g) = 2·rank + 48·h^∨·dim/12 =
2·rank + 4·h^∨·dim. Verified numerically:

| g | rank | h^∨ | dim | (ρ, ρ^∨) | K_W exact | 2·rank + 4·h^∨·dim |
|---|---|---|---|---|---|---|
| A_1 | 1 | 2 | 3 | 1/2 | 26 | 26 ✓ |
| A_2 | 2 | 3 | 8 | 2 | 100 | 100 ✓ |
| A_3 | 3 | 4 | 15 | 5 | 246 | 246 ✓ |
| D_4 | 4 | 6 | 28 | 14 | 680 | 680 ✓ |
| E_8 | 8 | 30 | 248 | 620 | 29776 | 29776 ✓ |

Also the additional coincidence: in SL case dim = rank·(h^∨+1), so the two
candidate formulas 2·rank + 4·h^∨·dim and 2·rank·(1 + 2h^∨ + 2(h^∨)^2) are equal
on SL (purely because dim/rank = h^∨+1 there). This is why all six SL
verification points in the session match.

**(b) What the attack claim GETS WRONG.** The conjecture that A(g) := h^∨·dim
captures (ρ, ρ^∨) up to a factor of 12 is FALSE for non-simply-laced g. Explicit
computation yields:

| g | rank | h^∨ | dim | r_g | (ρ, ρ^∨) exact | h^∨·dim/12 | K_W exact | flat pred | error |
|---|---|---|---|---|---|---|---|---|---|
| C_2 | 2 | 3 | 10 | 2 | 7/2 | 5/2 | 172 | 124 | -48 |
| G_2 | 2 | 4 | 14 | 3 | 8 | 14/3 | **388** | 228 | -160 |
| F_4 | 4 | 9 | 52 | 2 | 55 | 39 | 2648 | 1880 | -768 |

The note-proposed lacing correction K_W = 2·rank·(1 + 2h^∨ + 2(h^∨)^2/r_g)
(dividing the quadratic piece by r_g) also FAILS: G_2 gives 236/3 (not integer,
immediate falsifier); F_4 gives 800 (exact is 2648). The correction has wrong
sign AND wrong magnitude — the non-simply-laced K_W is LARGER than the SL
formula, not smaller.

**(c) CORRECT RELATIONSHIP.**

K_W(g) = 2·rank(g) + 48·(ρ, ρ^∨),

where (ρ, ρ^∨) is computed with the form normalized so long roots have
(α, α) = 2. Equivalent invariant expression via Kac-Moody coroot pairing:

(ρ, ρ^∨) = (1/4) · Σ_{α ∈ Δ_+} (α, α^∨) · f_α,    f_α = 1 (α long), f_α = r_g (α short).

In simply-laced case this collapses to h^∨·dim/12. In non-simply-laced case
there is NO simple closed form in (rank, h^∨, dim, r_g) alone — it is a genuine
type-dependent root-system invariant:

| g | K_W(g) |
|---|---|
| A_n | 2n + 4(n+1)·n(n+2) |
| B_n | 2n + 48·(ρ, ρ^∨)_{B_n} (explicit per n) |
| C_n | 2n + 48·(ρ, ρ^∨)_{C_n} (explicit per n) |
| D_n | 2n + 4(2n-2)·n(2n-1) |
| E_6 | 12 + 4·12·78 = 3756 |
| E_7 | 14 + 4·18·133 = 9590 |
| E_8 | 16 + 4·30·248 = 29776 |
| F_4 | **2648** |
| G_2 | **388** |

## Heal consequences for Vol II

1. **Delete the simply-laced-only claim of universality.** The note
   `universal_koszul_complementarity_kv_kw_all_simple.md` (line 172)
   K_W(g) = 2·rank + 4·h^∨·dim is correct ONLY for simply-laced g. Restate as
   "simply-laced universal; non-simply-laced requires explicit (ρ, ρ^∨)."

2. **Delete the r_g^{-1} lacing correction.** Line 203 and line 370 of the same
   note propose K_W(g) = 2·rank·(1 + 2h^∨ + 2(h^∨)^2/r_g). FALSIFIED on G_2 (236/3
   non-integer) and F_4 (800 vs exact 2648). This correction has wrong direction.

3. **The invariant K_W is genuinely type-dependent.** No simple universal formula
   exists in the four usual invariants (rank, h^∨, dim, r_g). The Platonic form
   of the theorem is: "K_W(g) = 2·rank + 48·(ρ, ρ^∨)" — which IS universal but
   cannot be further compressed. The attempt to package it as "4·h^∨·dim" trades
   correctness for compactness.

4. **FM-class diagnosis.** This is a textbook AP-CY12 / AP109 pattern: a formula
   verified on six small SL points was projected to a universal claim, ignoring
   that the SL family satisfies an accidental identity dim = rank·(h^∨+1) that
   collapses two distinct quadratic invariants into one. The correct protocol:
   verify on at least one rank-2 non-simply-laced example (C_2 or G_2) before
   any "universal" claim.

## Status

- K_W(G_2) = 228 claim: **FALSIFIED** (exact value 388).
- K_W(g) = 2·rank + 4·h^∨·dim: **simply-laced only**.
- K_W(g) = 2·rank·(1 + 2h^∨ + 2(h^∨)^2/r_g): **FALSIFIED**.
- Universal form: **K_W(g) = 2·rank(g) + 48·(ρ, ρ^∨)_{long-norm-2}**.
- Status downgrade on Russian-school/Chriss-Ginzburg universal claim:
  restrict to simply-laced universality; non-simply-laced is per-type
  Lie-theoretic data, not a universal polynomial in (rank, h^∨, dim, r_g).
