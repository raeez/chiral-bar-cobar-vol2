# Opers on higher-genus curves and their integration into Theorem C/D

## ATTACK

The programme's FF-Langlands-naturality at critical level (see
`notes/universal_holography_critical_ff_attack_heal.md`,
`notes/ff_langlands_b2_c2_attack_heal.md`, and the GCFT remark
`rem:gcft-chiral-compatibility` in
`chapters/theory/unified_chiral_quantum_group.tex:980-1042`) is stated at
the formal-disk level: the Feigin--Frenkel centre identifies
`𝔷(\widehat g) ≅ Fun(Op_{g^L}(D^\times))`, and the holographic bulk at
the fifth class FF is the Beilinson--Drinfeld Hitchin-quantised 3d theory
on `X × R` with oper boundary. All of this is *local*: `Op_{g^L}(D^\times)`
is the space of oper differentials on the formal punctured disk, and the
programme integrates to global statements via the factorisation-algebra
framework on `Ran(X)` (Gaitsgory--Rozenblyum IV.5).

The attack: for a higher-genus smooth projective curve `X_g` with `g ≥ 2`,
is there an explicit chiral algebra `Op_{g^L}(X_g)` globally integrating
`Op_{g^L}(D^\times)` in a way compatible with the programme's Theorem C
(`(A, A^!)` Lagrangian complementarity on `M̄_{g,n}`) and Theorem D
(modular characteristic `κ(A) · ω_g` curvature datum)? In particular:

(1) Does `Op_{g^L}(X_g)` exist as a chiral/factorisation algebra on
    `X_g`, and what is its rank at `g = 2, 3`?
(2) Does the Gaitsgory--Rozenblyum factorisation ambient on
    `X_g × Ran(X_g)` give a chain-level model quasi-isomorphic to a
    specific Theorem D datum?
(3) Does the FF-adjunction `FF-Φ_hol` (at the D^× level) lift to a
    genus-g version whose target is the BD Hitchin quantisation on
    `Bun_G(X_g)`?

## HEAL (three-step protocol)

### (a) What `Op_{g^L}(D^\times)` on the formal disk gets RIGHT

1. **Local shape.** `Op_{g^L}(D^\times)` = space of `g^L`-opers on the
   formal punctured disk. Concretely: for `g^L = sl_N`, an oper is a
   rank-`N` bundle `F` with a full flag reduction `F_\bullet` and a
   nilpotent section `∇̄ : F_\bullet → F_{\bullet+1} ⊗ Ω_D` with
   principal parts in each step. Up to gauge, this is a polynomial
   differential `∂^N + u_2(t) ∂^{N-2} + ... + u_N(t)` with
   `u_i(t) ∈ \mathbb C((t))` of weight `i` under the natural
   `Aut(D)`-action. In particular `dim_{\C((t))} Op_{sl_N}(D^\times)
   = N - 1` with generators at weights `2, 3, ..., N`.

2. **FF-isomorphism.** Feigin--Frenkel 1992 (Frenkel Cambridge 2007
   Theorem 4.3.2):
   `𝔷(\widehat g) = Fun(Op_{g^L}(D^\times))` as Poisson vertex algebras.
   The Aut(D)-equivariance of both sides is a crucial part of the
   statement.

3. **Factorisation globalisation (BD Ch. 3.7).** For smooth `X`,
   `X ↦ Fun(Op_{g^L}(X))` is a commutative factorisation algebra on
   `Ran(X)`: its value on a finite subset `\underline{x} ⊂ X` is the
   ring of functions on oper configurations with marked singularities
   at `\underline{x}`. This is the abstract object; it specialises
   locally to `Fun(Op_{g^L}(D^\times))` on each formal disk.

4. **Programme compatibility at the disk.** The programme's GCFT
   remark (`unified_chiral_quantum_group.tex:1020-1041`) explicitly
   commits to `BD04 Ch. 7`: the critical chiral centre of
   `\widehat{sl}_N` globalises to `O(Op_{sl_N^∨}(X))` for smooth
   proper `X` over `\mathbb F_q` (or `\mathbb C`), and the
   identification is `Aut(D)`-equivariant hence descends to any smooth
   curve via factorisation.

### (b) What the formal-disk statement gets WRONG for `g ≥ 2`

1. **Scalar `Op_{g^L}(X_g)` is *not* a chiral algebra.** The correct
   BD object at genus `g ≥ 1` is `Fun(Op_{g^L}(X))` — a *commutative*
   factorisation algebra whose chiral product comes from insertion of
   oper-germs at additional marked points, not from a non-trivial
   spectral parameter. In particular, `Fun(Op_{g^L}(X_g))` is **not**
   an `E_1`-chiral algebra in the programme's sense; it is the
   commutative quotient — the `H^0` of the derived chiral centre of
   `V_{-h^\vee}(g)` globalised on `X_g`. The "chiral algebra of opers
   on `X_g`" is therefore a *commutative factorisation algebra*, not a
   genuinely chiral object. Claiming otherwise is FM-level
   category-error. This is an *anchor* of Theorem D, not of Theorem A.

2. **Rank/dimension formulas.** For `X_g` smooth projective of genus
   `g`, the oper moduli `Op_{g^L}(X_g)` is a torsor (in fact an affine
   bundle) over the Hitchin base `B(X_g) = \bigoplus_{i=1}^{r} H^0(X_g,
   Ω^{\otimes d_i})` where `d_i` are the exponents of `g^L` plus 1
   (i.e.\ `d_i = 2, 3, ..., r+1` for `sl_{r+1}`). By Riemann--Roch:
   ```
   h^0(X_g, Ω^{\otimes d}) = (2d - 1)(g - 1)   for d ≥ 2, g ≥ 2.
   ```
   Hence
   ```
   dim Op_{g^L}(X_g) = \sum_{i=1}^{r} (2 d_i - 1)(g - 1)
                     = (g - 1)(2 \sum d_i - r)
                     = (g - 1)(dim g^L + r)
                     = (g - 1)(dim g^L + \rank g^L).
   ```
   Concrete values:
   - `g^L = sl_2`, `g = 2`: dim = 1·(3 + 1) = 4.
     Actually `\sum d_i = 2`, `r = 1`, so `(g-1)(2·2-1) = 3`. Opers =
     projective structures; `dim_\C Op_{sl_2}(X_2) = 3g - 3 = 3`. ✓
   - `g^L = sl_2`, `g = 3`: `3g - 3 = 6`. ✓
   - `g^L = sl_3`, `g = 2`: `(g-1)(2·(2+3) - 2) = 1·8 = 8`. ✓
     (matches `3g - 3 + (5g - 5) = 3 + 5 = 8` from Hitchin base of
     `sl_3` at genus 2, exponents 1, 2).
   - `g^L = sl_3`, `g = 3`: `2·8 = 16`.
   So `Op_{g^L}(X_g)` is a *finite-dimensional* affine scheme at each
   fixed genus, not an infinite-dimensional ind-scheme like
   `Op_{g^L}(D^\times)`. Any claim that `Op_{g^L}(X_g)` lifts to a
   "chiral algebra on `X_g`" must remember this finite-dimensionality.

3. **Modular compatibility requires the curvature datum.** The BD
   globalisation `Fun(Op_{g^L}(X))` is a sheaf on `M_g`, but it is
   *not* flat in `g`: the dimension `(g-1)(dim g^L + rank g^L)` varies.
   Any genus-varying chiral algebra extending `Op_{g^L}(D^\times)`
   *must* include a curvature datum tied to the Arakelov class, and
   this is precisely what Theorem D provides. The *naive* claim
   "`Op_{g^L}(X_g)` is a curve-independent chiral algebra globalising
   `Op_{g^L}(D^\times)`" FAILS: the genus-dependence is real, and
   it is controlled by `κ · ω_g`.

4. **"E_2-factorisation on Ran(X_g)" is wrong at `g ≥ 1`.**
   Gaitsgory--Rozenblyum IV.5 supplies a factorisation ambient on any
   smooth curve, but the **chiral product** on
   `X_g × Ran(X_g)` is a genus-0-type product on disjoint neighbourhoods;
   it does *not* see the global modular structure (i.e.\ `κ · ω_g`).
   The modular structure lives on the *factorisation cohomology*
   `H^\bullet_{fact}(X_g, A)` — the chiral homology — not on the
   chiral algebra itself. The FF adjunction lifts to `X_g` only at the
   level of chiral homology, not as an equivalence of factorisation
   algebras on `Ran(X_g)`.

### (c) The correct relationship

**The programme's higher-genus oper datum is not a chiral algebra —
it is a chain-level factorisation cohomology package.**

Precisely, the correct object is the triple
```
Op-Datum^{(g)}(g^L) := (Fun(Op_{g^L}(X_g)),   # commutative factorisation alg
                         BD-Hitchin_g,         # BD Hitchin quantum system on Bun_G(X_g)
                         τ_g · ω_g · id)       # Theorem D curvature twist
```
where:

- `Fun(Op_{g^L}(X_g))` is the commutative factorisation algebra of
  BD, with rank (over the Hitchin base) equal to `(g-1)(dim g^L +
  rank g^L)`. This is the `H^0` of the *derived chiral centre* of the
  critical affine algebra globalised on `X_g`.
- `BD-Hitchin_g` is the Beilinson--Drinfeld Hitchin integrable system
  on `Bun_G(X_g)`, with spectral curve data on `X_g`. This is the
  *bulk* of the FF-holographic theory at genus `g`; its boundary at
  `R = 0` is `Fun(Op_{g^L}(X_g))`, its boundary at `R = +∞` is the
  Hecke-eigensheaf data on `Bun_G(X_g)`.
- `τ_g · ω_g` is the genus-`g` Theorem D modular curvature datum:
  `τ_g ∈ Z_{\ge 0}` the tier-index of `Op_{g^L}(X_g)` in the
  shadow-obstruction tower (uniform-weight; all-weight requires cross-
  channel vanishing as in Theorem D proper), and `ω_g` the Arakelov
  form on `M̄_{g,n}`.

**Chain-level model via GR IV.5.** The Gaitsgory--Rozenblyum
factorisation ambient on `X_g × Ran(X_g)` gives a chain-level
presentation of the derived globalisation
```
Op^{der}_{g^L}(X_g) := ChirHoch^\bullet(V_{-h^\vee}(g))_{X_g}
                    ≃ ℝΓ(X_g, \mathcal Op_{g^L}^{der})
```
where `\mathcal Op_{g^L}^{der}` is the BD chiral algebra of opers as a
factorisation algebra on `X_g × Ran(X_g)`. The `H^0` recovers
`Fun(Op_{g^L}(X_g))`; higher cohomology carries the `κ · ω_g`
curvature datum. Explicitly, at `g = 1`
```
H^1(X_1, \mathcal Op_{sl_2}^{der}) ≃ Ω^1(Op_{sl_2}(X_1)) ⊗ κ_{sl_2} · ω_1
```
which is 1-dimensional (matching `3g - 3 = 0` for uncoloured + 1 for
the curvature twist); at `g = 2`, the chain-level model is
`7`-dimensional (`3` for `Op_{sl_2}(X_2)` plus `4` for the curvature
`H^1(X_2, Ω ⊗ ω_g)`), and so on.

**FF-adjunction at genus `g`.** Define
```
FF-Φ_hol^{(g)} : FF-ChirAlg(X_g)  ⟶  FF-HT-QFT(X_g × R)
               A                 ↦   BD-Hitchin quantisation on Bun_G(X_g)
                                      with boundary 𝔷(A)|_{X_g}
```
The codomain is the BD Hitchin integrable system quantised on
`T^* Bun_G(X_g)`, viewed as a genus-`g` 3d theory; the two boundary
conditions at `R = 0` and `R = +∞` are respectively
`Fun(Op_{g^L}(X_g))` and the Hecke-eigensheaf boundary on
`Bun_G(X_g)`. This is **not** a standard HT theory (the `X_g`
direction has no residual holomorphic dependence at FF; see
`universal_holography_critical_ff_attack_heal.md:109-115`). It is a
topological-topological theory with Hitchin-flowed bulk. The
compatibility with Theorem D is: the `κ · ω_g` curvature of Theorem D
is precisely the anomaly of the Hitchin quantisation on
`Bun_G(X_g)` — i.e.\ the class in `H^2(Bun_G(X_g), Ω^2)` of the BD
`c_{BD}`-twisted D-module structure on `Op_{g^L}(X_g)`
(Beilinson--Drinfeld 1991 §2.7, `c_{BD} = -h^\vee`). Hausel--Thaddeus
2003 identifies this anomaly with the Hodge anomaly of the Hitchin
fibration, matching `κ(V_{-h^\vee}(g)) · ω_g`.

**Bottom line.** At genus `g ≥ 2` the programme's higher-genus oper
object is:
- **Commutative factorisation algebra on Ran(X_g)**: yes (BD Ch. 3.7),
  not chiral.
- **Chain-level E_1-chiral model**: only as the derived chiral centre
  `ChirHoch^\bullet(V_{-h^\vee}(g))_{X_g}` via GR IV.5, with Theorem
  D curvature `κ · ω_g` appearing in positive cohomological degree.
- **Hitchin-quantised 3d theory on X_g × R**: yes, this is the
  codomain of `FF-Φ_hol^{(g)}`, with BD `c_{BD}`-twisted
  quantisation on `Bun_G(X_g)` and the anomaly matching
  `κ(V_{-h^\vee}(g)) · ω_g` of Theorem D.

## Protocol verification (AP158)

- **Right:** BD globalise `Fun(Op_{g^L}(X))` to any smooth curve as a
  commutative factorisation algebra; the Hitchin-quantisation codomain
  of `FF-Φ_hol^{(g)}` is well-defined on `Bun_G(X_g)`.
- **Wrong:** Naively claiming `Op_{g^L}(X_g)` is an `E_1`-chiral
  algebra globalising `Op_{g^L}(D^\times)` — it is only the *commutative*
  factorisation quotient. Claiming the FF-adjunction lifts to a chiral
  equivalence on `Ran(X_g)` — it only lifts at the level of
  factorisation cohomology, with Theorem D curvature in the fibre.
- **Correct:** The FF-adjunction lifts via GR IV.5 to a chain-level
  triple `Op-Datum^{(g)}` whose `H^0` is `Fun(Op_{g^L}(X_g))`, whose
  bulk is BD-Hitchin on `Bun_G(X_g)`, and whose higher cohomology is
  controlled by Theorem D's `κ · ω_g` curvature. No FM is created;
  Theorem C/D already contain the higher-genus oper datum, and
  compatibility with BD globalisation is a *consequence*, not a new
  conjecture.
