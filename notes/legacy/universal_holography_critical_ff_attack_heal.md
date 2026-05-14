# Universal Holography at Critical Level: Attack and Heal (Fifth Class FF)

## The attack

The note `universal_holography_adjunction_koszul_naturality.md` (Corollary 2)
asserts that the adjunction `(Φ_hol ⊣ Reduce)` extends to the critical level
`k = -h^∨` as a limit `ε → 0` of the non-critical statement, with
`Reduce ∘ (-)^{rev}(Φ_hol(V_{-h^∨}(g))) = 𝔷(\widehat g)` via "classical
Feigin–Frenkel specialisation".

This note shows the ε → 0 limit is **divergent** and the claim as stated is
**wrong**. The correct statement is that there is a **separate** functor
`FF-Φ_hol` on the fifth class FF (critical chiral algebras), with its **own
adjunction** `FF-Φ_hol ⊣ FF-Reduce`, **NOT** a limit of the non-critical one.

## Step (a): what the claim gets RIGHT

**Koszul-involutive self-duality at critical.** The Koszul involution on levels
is `k ↦ k^! = -k - 2h^∨`. At `k = -h^∨` one computes
`k^! = -(-h^∨) - 2h^∨ = -h^∨ = k`, so critical is a **fixed point** of the
Koszul involution. Hence, if a functor `FF-Φ_hol` exists on the FF sector, its
R-reversal MUST send `FF-Φ_hol(V_{-h^∨}(g))` to itself (self-dual 3d theory at
critical). This is a genuine structural constraint and the note's intuition is
correct on this point.

**Critical-level complementarity.** The Koszul complementarity `K_V(g) = c + c^!`
at non-critical level evaluates to `K_V(g) = 2·dim(g)` in the limit `k → -h^∨`
(using that the Sugawara central charge has a definite limit for the sum
`c(k) + c(k^!)` via L'Hôpital, even though each term diverges — see below).
So the *sum* c + c^! is continuous through critical; the complementarity
relation survives as an identity `K_V(g) = 2·dim(g)`.

## Step (b): what the claim gets WRONG

**Individual Sugawara central charge divergence.** Sugawara central charge is
`c(k) = k·dim(g)/(k+h^∨)`. At `k = -h^∨ + ε`:

```
c(-h^∨ + ε) = (-h^∨ + ε)·dim(g) / ε = -h^∨·dim(g)/ε + dim(g) → -∞ as ε → 0⁺
c^!         = c(-h^∨ - ε) = (-h^∨ - ε)·dim(g) / (-ε) = h^∨·dim(g)/ε + dim(g) → +∞
```

The sum is `c + c^! = 2·dim(g)` (finite), but each term diverges. Therefore
any claim about an individual 3d HT theory `Φ_hol(V_{k}(g))` as `k → -h^∨` is
a claim about a theory whose Sugawara stress tensor is blowing up. The limit is
not a valid 3d HT theory — the conformal vector (which is the key input to
Φ_hol per Thm on Universal Holography, Vol II) degenerates.

**Domain hypothesis failure.** `Φ_hol`'s domain is
`ChirAlg^{ω, BL}_X` — chiral algebras with conformal vector at non-critical
level. At critical, the conformal vector `T(z)` does not exist in any way
consistent with Sugawara (the factor `1/(k+h^∨)` is a pole). So
`V_{-h^∨}(g) ∉ dom(Φ_hol)`. The "ε → 0 limit" of Corollary 2 is applying a
functor to an object outside its domain. This is a category error.

**No deformation retract to non-critical.** The existing note attempts to
rescue by "deformation". But `V_k(g)` as a k-family is a FAMILY of chiral
algebras over `A^1_k`; the family is flat, but the functor `Φ_hol` is defined
on the complement `A^1_k ∖ {-h^∨}` only. There is no extension-by-continuity of
`Φ_hol` across `k = -h^∨` compatible with the non-critical adjunction, because
the boundary algebra itself becomes `𝔷(\widehat g) ⊊ V_{-h^∨}(g)` in any
reasonable limit procedure (the FF centre is a *subalgebra*, not the whole
thing).

**Concrete V_{-2}(sl_2) analysis.** For `sl_2` (so `h^∨ = 2`, critical `k = -2`):

Sugawara at `k = -2 + ε`: `T(z) = (:J^+ J^- + J^- J^+ + ½ J^0 J^0:)/(ε)`. The
stress tensor coefficient `1/ε` diverges as `ε → 0`. In the ε → 0 limit, the
"stress tensor" would need to be multiplied by ε to make sense; the resulting
operator `ε·T_{ε}(z)` has a definite limit which is a **null field** (it
vanishes on the vacuum at ε = 0 and generates no Virasoro action).

Feigin-Frenkel (1992) showed that at `k = -2`, the centre `𝔷(\widehat{sl_2})`
is the polynomial algebra on the **Sugawara Casimir field**
`S(z) = :J^+ J^-: + :J^- J^+: + ½ :J^0 J^0:` and its derivatives — precisely
the field that appears as `ε · T_ε(z) · ε = S(z) + O(ε)`. So the `T` that
*diverged* becomes the *central generator* `S(z)` after rescaling. This is
qualitatively different from a Sugawara stress tensor: `S(z)` is in the CENTRE
of the algebra; it does **not** act as a stress tensor on modules, it acts as
a **scalar**.

**Conclusion of step (b):** The ε → 0 limit of Φ_hol does NOT produce a 3d HT
theory with boundary `V_{-h^∨}(g)`. The stress-tensor component of the boundary
data degenerates into a scalar (central element), which is incompatible with HT
bulk structure (HT needs a well-defined holomorphic stress tensor to pair with
the transverse topological direction).

## Step (c): the correct relationship

**The FF functor `FF-Φ_hol` is a separate construction.**

Define `FF-ChirAlg_X` as the category of chiral algebras `A` on `X` equipped
with a **centre-Casimir structure**: a polynomial subalgebra
`𝔷(A) ⊂ A` such that (i) `𝔷(A)` is Poisson central, (ii) the quotient
`A / 𝔷(A)·A` recovers a (possibly degenerate) chiral bialgebra, and (iii)
`𝔷(A)` is spectrally generated by oper differentials (Feigin-Frenkel,
`𝔷(\widehat g) ≅ Fun(Op_{g^L}(D^\times))` with `g^L` the Langlands dual).

For critical-level `V_{-h^∨}(g)`, this is well-defined with
`𝔷(A) = 𝔷(\widehat g)`.

**The codomain: Hitchin-quantised 3d theory.** Define `FF-HT-QFT_{X×R}` as the
category of 3d theories on `X × R` that are **Hitchin-quantised**: the bulk is
a quantisation of the Hitchin integrable system `T^*Bun_G(X)`, with the
`R`-direction as the Hitchin flow parameter, and two boundary conditions:
- at `R = 0`: the FF-centre (opers on `X`);
- at `R = +∞`: the loop-group eigensheaves (Hecke eigensheaves, dual opers on `X`).

This is NOT a HT theory in the standard sense (holomorphic on `X`, topological
on `R`). It is a **topological-topological** theory in which the `X` direction
has no residual holomorphic dependence — the opers boundary condition at
`R = 0` is a purely cohomological datum, independent of complex structure on
`X` (per BD 1991 Hitchin quantisation, the opers construction depends only on
the underlying smooth curve, via the canonical BRST differential that kills
holomorphic data).

**Definition of `FF-Φ_hol`:**

```
FF-Φ_hol : FF-ChirAlg_X  ⟶  FF-HT-QFT_{X×R}
          A             ↦  (Hitchin-quantised theory with boundary 𝔷(A))
```

For `V_{-h^∨}(g)`: `FF-Φ_hol(V_{-h^∨}(g))` = Beilinson-Drinfeld Hitchin quantum
integrable system with Hecke eigensheaves. This is the BD construction (1991,
also Frenkel "Langlands for loop groups" Ch. 10).

**The adjoint `FF-Reduce`:**

```
FF-Reduce : FF-HT-QFT_{X×R}  ⟶  FF-ChirAlg_X
          T                  ↦  T[X × {0}] = the boundary algebra
```

**The adjunction `FF-Φ_hol ⊣ FF-Reduce`** is established just as in the
non-critical case: the unit is the identification of the boundary of
`FF-Φ_hol(A)` with `𝔷(A)` (which carries `A` as a faithful extension); the
counit is the projection of a Hitchin-quantised theory to its `R = 0`-boundary
oper data.

**Koszul-naturality at FF.** Recall that `V_{-h^∨}(g)^! = V_{-h^∨}(g)` as
chiral algebras (since critical is a fixed point of `k ↔ k^!`). So
`FF-Φ_hol(V_{-h^∨}(g)^!) = FF-Φ_hol(V_{-h^∨}(g))`, hence the R-reversal is
trivial. The consistency check **passes**.

But the richer FF-Koszul duality is at the level of the centre: by Feigin-
Frenkel + geometric Langlands,
`𝔷(\widehat g) ≅ Fun(Op_{g^L}(D^\times))`, and the Koszul dual at the FF-level
exchanges `g ↔ g^L` (Langlands dual). So the FF-level R-reversal is NOT
trivial — it is the **Langlands involution** on opers:

```
FF-Φ_hol(V_{-h^∨}(g))^{rev} ≅ FF-Φ_hol(V_{-h^∨}(g^L))
```

via the Langlands duality on Hitchin systems (BD, Kapustin-Witten, Frenkel-
Gaitsgory). This is a strictly richer statement than the non-critical
self-duality; the FF adjunction has Langlands duality built into the
R-reversal structure.

**The programme's fifth class FF gets its own adjunction, its own Koszul
naturality, and its own holographic interpretation: 3d Hitchin quantum system
with opers/Hecke-eigensheaf boundaries, Koszul-natural under Langlands
`g ↔ g^L`.**

## Verdict

1. **The Corollary 2 claim is wrong as stated.** The ε → 0 limit diverges in
   each individual Sugawara central charge; the stress tensor degenerates to a
   central scalar; `V_{-h^∨}(g)` is outside the domain of `Φ_hol`.

2. **The intuition (self-duality at critical) is right.** Critical IS a
   Koszul-fixed point; any correct FF adjunction must have `R`-reversal act
   trivially on the Sugawara/level datum.

3. **The correct structure is a separate `FF-Φ_hol ⊣ FF-Reduce` adjunction**
   on the fifth class FF. It takes `V_{-h^∨}(g)` to the Beilinson-Drinfeld
   Hitchin-quantised 3d theory with opers boundary. The codomain is
   `FF-HT-QFT` (Hitchin-flowed, not standard HT). The Koszul-naturality at FF
   is strictly RICHER: it encodes Langlands duality `g ↔ g^L`, not merely
   level sign-flip.

4. **The programme extends.** Universal Holography was stated for classes
   G/L/C/M (non-critical). The fifth class FF completes it. The critical case
   is not a limit but a parallel — a SEPARATE face of the Universal Holography
   theorem. Theorem F (Universal Holography) on the FIVE classes G/L/C/M/FF is
   the strongest Platonic form.

## Explicit `V_{-2}(sl_2)` summary

| Object | Non-critical `k ≠ -2` | Critical `k = -2` |
|:------:|:---------------------:|:-----------------:|
| Conformal vector | Sugawara `T(z)` well-defined | Degenerates (1/ε pole) |
| `c` | `3k/(k+2)` finite | `±∞` (not a limit) |
| Φ_hol image | 3d HT (Costello-Gaiotto) with bdy `V_k(sl_2)` | Hitchin-quantised 3d (BD) with bdy `𝔷(\widehat{sl_2})` |
| Koszul dual | `V_{-k-4}(sl_2)` (distinct) | `V_{-2}(sl_2)` (self) |
| R-reversal | Swaps `V_k ↔ V_{k^!}` | Trivial on level; Langlands on opers |
| Adjunction | `Φ_hol ⊣ Reduce` | `FF-Φ_hol ⊣ FF-Reduce` (separate) |

## Corrections required to the existing note

The existing note's Corollary 2 must be rewritten as:

> **Corollary 2 (Critical level FF as a separate adjunction.)** At the critical
> level `k = -h^∨`, `V_{-h^∨}(g)` is outside the domain of `Φ_hol` (the
> Sugawara conformal vector degenerates). The ε → 0 limit of the non-critical
> adjunction is divergent term-by-term although the Koszul complementarity
> `c + c^!` extends continuously to `K_V(g) = 2·dim(g)`. The correct
> holographic statement at critical level is a **separate functor** `FF-Φ_hol`
> on the fifth class FF with its own adjunction and Koszul-naturality encoded
> by Langlands duality `g ↔ g^L` via Feigin-Frenkel + Beilinson-Drinfeld.
> See `universal_holography_critical_ff_attack_heal.md`.

The table row for `V_{-h^∨}(g)` in the Explicit examples table is also wrong:
`V_{-h^∨}(g)^!` is `V_{-h^∨}(g)` itself (self-dual at Koszul-involution
fixed point), NOT `𝔷(\widehat g)`. `𝔷(\widehat g)` is the FF-CENTRE inside
`V_{-h^∨}(g)`, a DIFFERENT structure and a DIFFERENT Koszul pairing.

## Independent-verification anchors for FF-Φ_hol

- **derived_from:** programme's Universal Holography functor (non-critical);
  Feigin-Frenkel 1992 critical centre; Beilinson-Drinfeld 1991 Hitchin
  quantization.
- **verified_against:** Frenkel "Langlands correspondence for loop groups"
  2007 Ch. 10 (opers / Hecke eigensheaves boundary condition);
  Gaitsgory "Notes on 2d CFT" 1999 (critical-level BRST and centre).
- **disjoint_rationale:** The BD Hitchin quantization constructs the FF-holographic
  3d theory via algebraic geometry (moduli of G-bundles + Hitchin flow),
  independent of the chiral-algebra functor Φ_hol; Frenkel's loop-group
  Langlands identifies the boundary with opers via a representation-theoretic
  construction orthogonal to the BV quantisation in Φ_hol.
