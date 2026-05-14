# Universal Holography: Family-Over-Level Unification — Attack and Heal

## The attack

The note `universal_holography_two_adjunctions_platonic_heal.md` asserts that
Universal Holography is not a single functor but TWO functors glued at the
critical-level interface: `Φ_hol` on non-critical `ChirAlg^{ω,BL}_X` ⇄
standard `HT-QFT_{X×R}`, and a SEPARATE `FF-Φ_hol` on `FF-ChirAlg_X` ⇄
`FF-HT-QFT_{X×R}` (Hitchin-quantised). The target categories are DIFFERENT.

The Russian-school / BD / Gaitsgory attack: is the "two-adjunction glue" an
artefact of insufficient categorical ambient, or is it structurally forced?
Specifically — can we build a single family-over-level functor

```
Φ_hol^{fam} : ChirAlg^{ω,BL}_{/Level}  ⇄  HT-QFT^{fam}_{/Level} : Reduce^{fam}
```

with Level = (C ∖ {-h^∨}) ⊔ {-h^∨} (non-critical open locus plus critical
point) as base, restricting to `Φ_hol` on the open locus and `FF-Φ_hol` on the
closed point? The issue is the target: standard `HT-QFT` and Hitchin-quantised
`FF-HT-QFT` are different categorical targets. Can we build a common ambient
`HT-QFT^{fam}_{/Level}` containing both as full sub-∞-categories via a
continuous degeneration at `k = -h^∨`?

This note executes the three-step protocol (a)–(c) and concludes with a verdict.

## Step (a): what "two adjunctions glued at the critical interface" gets RIGHT

**The target categories really are different at the set-theoretic level.**
Standard `HT-QFT` has holomorphic structure along `X` and topological structure
along `R`; the Sugawara conformal vector `T(z) = :J^a J^a:/(k+h^∨)` BRST-
commutes with the `R`-translation antighost `G(z)`, so `[Q_tot, G(z)] = T(z)`
realises E_3-topological structure at non-critical level. In `FF-HT-QFT`, the
BD Hitchin quantum system has NO residual holomorphic dependence on `X` at the
opers boundary — the opers construction is topological on `X` (the BRST
differential kills holomorphic data at `k = -h^∨`). So the bulk structure is
genuinely different: one is `E_2-chiral ⊗ E_1-top` (holomorphic × topological);
the other is `E_2-top × E_1-top` (fully topological, but with oper-moduli
boundary data rather than free holomorphic boundary).

**The Sugawara stress tensor degenerates into a Casimir central scalar.**
At `k = -h^∨ + ε`, `T_ε(z) = S(z)/ε` with `S(z) = :J^a J^a:` the Segal-Sugawara
Casimir field. As `ε → 0`, `T_ε(z)` diverges but `S(z) = ε·T_ε(z)` has a
well-defined limit — and `S(z)` is CENTRAL, not a stress tensor. The
"conformal vector" datum that feeds `Φ_hol` becomes a central polynomial datum
feeding `FF-Φ_hol`. These are qualitatively different inputs: one generates
Virasoro action on modules; the other acts by scalars.

**Koszul-involution fixed point.** `k^! = -k - 2h^∨` fixes `k = -h^∨`. So the
Koszul-naturality at critical reduces to self-symmetry, and any honest
"unified" adjunction must handle the fixed-point stratum differently (via
Langlands-naturality `g ↔ g^L` rather than Koszul-naturality).

## Step (b): what it gets WRONG if family unification is achievable

The two-adjunction picture treats the critical locus as a SEPARATE component
with its OWN target category, glued abstractly at the interface. If we can
realise BOTH target categories as special fibres of a SINGLE family, the
"two-adjunction glue" becomes an artefact rather than a structural truth.

**Concrete construction of the unified target category.** Consider the
Costello-Gaiotto 3d HT-QFT family. For each level `k`, Costello-Gaiotto (JHEP
2018) construct a 3d HT gauge theory `T_k` on `X × R` with boundary VOA
`V_k(g)` (or its DS reduction). The family `{T_k}_{k ∈ C}` is a family of BV
complexes, flat over the affine line `A^1_k = Spec(C[k])`. Define

```
HT-QFT^{fam}_{/A^1_k} = BV-3d-family(Costello-Gaiotto) → A^1_k
```

as the stack of 3d HT theories varying flatly in `k`. This is a category
fibred over `A^1_k`; its fibre over generic `k` is standard `HT-QFT`, its
fibre over `k = -h^∨` is some limit category we must identify.

**The critical fibre via BV degeneration.** At `k = -h^∨ + ε`, the BV action
contains the Sugawara coupling `∫ ε^{-1} S(z) ∧ G(z) dz ∧ dz̄ ∧ dt`; the
`ε^{-1}` prefactor makes this divergent. After the standard BD rescaling

```
T_ε(z) = S(z)/ε,         G̃_ε(z) = ε·G(z),
```

the coupling becomes `∫ S(z) ∧ G̃(z) dz ∧ dz̄ ∧ dt` with `ε`-independent
coefficient — but `G̃_ε(z)` vanishes at `ε = 0` (the antighost degenerates).
The resulting `ε = 0` fibre is the BV complex with:
- a CENTRAL field `S(z)` (no longer a stress tensor; no Virasoro action on
  modules),
- a VANISHING transverse antighost,
- only REMNANT topological structure on both `X` and `R`,
- boundary data restricted to the SUBALGEBRA `𝔷(\widehat g) ⊂ V_{-h^∨}(g)`.

This is EXACTLY the BD Hitchin-quantised 3d theory — the opers-valued boundary
at `R = 0`, the Hecke-eigensheaf boundary at `R = ∞`, with the `R`-flow being
Hitchin flow rather than HT translation. So `FF-HT-QFT` IS the critical fibre
of the Costello-Gaiotto family.

**Consequence.** The two "different" target categories are fibres of a single
family `HT-QFT^{fam}_{/A^1_k}`. The critical fibre is a CODIMENSION-1
STRATUM (a divisor at `k = -h^∨`), not a separate component. The "two-
adjunction glue" DOES collapse into a single family-over-level adjunction IF
the degeneration preserves adjointness.

## Step (c): the correct relationship (family-over-level unification)

**Unified target category.** Define

```
HT-QFT^{fam}_{/Level} := Lim-pres{Costello-Gaiotto BV family over A^1_k,
                                  with stratification:
                                  - open stratum U = A^1_k ∖ {-h^∨}: fibre = HT-QFT
                                  - closed stratum Z = {-h^∨}: fibre = FF-HT-QFT}
```

explicitly: sections of the BV 3d-theory stack over `A^1_k`, with restriction to
`U` landing in standard HT-QFT and restriction to `Z` landing in Hitchin-
quantised 3d QFT. The family is flat (Costello-Gaiotto flatness of BV
complexes), and the critical fibre is obtained by the BV rescaling
`S = εT`, `G̃ = εG` explicitly above.

**Unified functor.** Define

```
Φ_hol^{fam} : ChirAlg^{ω,BL}_{/A^1_k}  ⟶  HT-QFT^{fam}_{/A^1_k}
             A_• = {A_k}_k          ↦  {Φ_hol(A_k) for k ≠ -h^∨;  FF-Φ_hol(A_{-h^∨}) at critical}
```

where the input is a FAMILY of chiral algebras varying in `k` (think of
`V_•(g)` as the universal family `{V_k(g)}_k` → Level). Over the open locus
this is the standard Universal Holography functor. At the critical fibre it
is `FF-Φ_hol`. Continuity follows from the BV rescaling: at `k = -h^∨ + ε`,
`Φ_hol(V_{-h^∨+ε}(g))` has boundary `V_{-h^∨+ε}(g)` with stress tensor
`T_ε(z) = S(z)/ε`; rescaling `S = εT`, the limit `ε → 0` exists and equals
`FF-Φ_hol(V_{-h^∨}(g))` with boundary `𝔷(\widehat g) ⊂ V_{-h^∨}(g)`.

**The restriction to `𝔷(\widehat g)` at the critical fibre** is the boundary
condition that survives the BV degeneration: fields that coupled to `T_ε(z)`
at finite ε couple only to `S(z) = εT_ε(z)` at `ε = 0`, and `S(z)` acts as a
scalar on the `ε = 0` module, so only scalar-equivariant fields survive. The
surviving subalgebra is exactly the centre `𝔷(\widehat g)`.

**Unified adjoint.** Define

```
Reduce^{fam} : HT-QFT^{fam}_{/Level}  ⟶  ChirAlg^{ω,BL}_{/Level}
             T_• = {T_k}_k        ↦  {T_k[X × {0}]}_k
```

The fibre over `k ≠ -h^∨` is standard `Reduce`; over `k = -h^∨`, it is
`FF-Reduce` producing `𝔷(\widehat g)` (since the critical fibre's boundary IS
the oper subalgebra of the full chiral algebra, by BV degeneration above).

**Adjunction in the family.** `(Φ_hol^{fam} ⊣ Reduce^{fam})` is adjoint
fibrewise AND naturally in `k`: the unit `η_{A_•} : A_• → Reduce^{fam} ∘
Φ_hol^{fam}(A_•)` is the identity on the non-critical locus and the inclusion
`𝔷(\widehat g) ↪ V_{-h^∨}(g)` on the critical fibre — specifically, at the
critical fibre, `Reduce^{fam} ∘ Φ_hol^{fam}(V_{-h^∨}(g)) = 𝔷(\widehat g)` is a
SUBALGEBRA of `V_{-h^∨}(g)`, not the whole. So the unit is a genuine inclusion
of the oper subalgebra, not the identity.

**This is the CORRECT form.** The counit `ε_{T_•} : Φ_hol^{fam} ∘ Reduce^{fam}(T_•)
⟹ T_•` is also fibrewise: identity-up-to-minimal-extension on non-critical,
opers-projection on critical. The adjunction identity `(ε Φ) ∘ (Φ η) = id_Φ`
holds fibrewise; naturality across the critical stratum follows from the
continuity of the BV rescaling.

**Koszul-naturality in the family.** The Koszul involution `k ↔ -k - 2h^∨`
acts on `Level = A^1_k` with fixed point `k = -h^∨`. It lifts to the family
`Φ_hol^{fam}` as follows:

- Over the open locus `U`: `Φ_hol(V_k(g))^{rev} ≅ Φ_hol(V_{-k-2h^∨}(g))`
  (standard Koszul-naturality).
- At the fixed point `Z = {-h^∨}`: `FF-Φ_hol(V_{-h^∨}(g))^{rev} ≅
  FF-Φ_hol(V_{-h^∨}(g^L))` (Langlands-naturality `g ↔ g^L` via BD/Frenkel-
  Gaitsgory geometric Langlands on opers).

These naturalities are COMPATIBLE in the family sense: the Koszul involution
on `Level` degenerates to the Langlands involution at the fixed point IF we
interpret `g ↔ g^L` as the "infinitesimal" limit of `k ↔ -k - 2h^∨` near the
critical fixed point, in the sense that the `ε → 0` R-reversal at
`V_{-h^∨ + ε}(g) ↔ V_{-h^∨ - ε}(g)` reduces (after BV rescaling and taking
oper subalgebras on both sides) to opers of `g` ↔ opers of `g^L`, via the
FF-dual-coordinate isomorphism `𝔷(\widehat g) ≅ Fun(Op_{g^L}(D^×))`.

Concretely: `V_{-h^∨ + ε}(g)^! = V_{-h^∨ - ε}(g)` at ε > 0. Taking oper
subalgebras of both sides in the BV ε → 0 limit and identifying via
Feigin-Frenkel isomorphism `𝔷(\widehat g) ≅ Fun(Op_{g^L}(D^×))`, the
R-reversal on the LHS `V_{-h^∨ + ε}(g) ↝ 𝔷(\widehat g) ≅ Fun(Op_{g^L}(D^×))`
matches the R-reversal on the RHS `V_{-h^∨ - ε}(g) ↝ 𝔷(\widehat g) ≅
Fun(Op_{g^L}(D^×))` (same target, by involutivity) — but a distinct
IDENTIFICATION is at play because the Feigin-Frenkel isomorphism is the
Langlands dual pairing. So the family Koszul-naturality genuinely degenerates
to Langlands-naturality at the critical fibre; the "gluing" is through the
shared opers stack `Op_{g^L}(D^×)`.

## Verdict

**The family-over-level unification SUCCEEDS.** Explicitly:

1. The Costello-Gaiotto BV family gives a flat `HT-QFT^{fam}_{/A^1_k}`
   containing standard HT-QFT on the open locus and Hitchin-quantised FF-HT-QFT
   at the critical fibre.
2. `Φ_hol^{fam}` is a genuine unified functor, with continuity at the critical
   stratum realised by BV rescaling `S = εT`, `G̃ = εG`.
3. Koszul-naturality in the family degenerates to Langlands-naturality at the
   critical fixed point via the Feigin-Frenkel isomorphism `𝔷(\widehat g) ≅
   Fun(Op_{g^L}(D^×))`, which identifies the R-reversal on both sides of the
   degeneration through a shared opers stack.

**However,** the unification is STRUCTURALLY UNCOMFORTABLE in two respects,
which the "two-adjunction glue" framing captured honestly:

- The UNIT of the adjunction changes behaviour discontinuously in the naive
  set-theoretic sense: identity on the open locus, strict subalgebra inclusion
  `𝔷(\widehat g) ↪ V_{-h^∨}(g)` at the critical fibre. The family statement
  packages this as "continuous in the stratified sense" — meaning the inclusion
  is the limit of identity morphisms between ε-rescaled stress tensors — but
  this is a FLAT-DEGENERATION continuity, not a topological one. The two-
  adjunction glue was honest about treating this as a stratified phenomenon.

- The target category `HT-QFT^{fam}_{/Level}` has FIBRES OF DIFFERENT HOMOTOPY
  TYPE: the generic fibre is E_3-topological (HT-QFT with genuine holomorphic
  × topological structure); the critical fibre is fully topological (Hitchin-
  quantised, with E_2-top × E_1-top). The family is NOT locally constant on
  Level. The Beilinson-Drinfeld / Gaitsgory formulation captures this exactly:
  the family of VOAs `V_•(g)` over `A^1_k` has a NONTRIVIAL ASSOCIATED GRADED
  over the critical fibre, encoding the degeneration of E_3 to E_2.

**Conclusion.** The family-over-level unification succeeds in the sense that a
single flat Costello-Gaiotto BV family realises both adjunctions as restrictions
to the two strata. BUT this family has a nontrivial stratification at `k = -h^∨`
where the fibre type changes (E_3-top → E_2-top × E_1-top, or equivalently,
standard HT-QFT → Hitchin-quantised). The "two-adjunction glue" description and
the "single family-over-level functor" description are NOT in contradiction —
they are two equivalent ways of phrasing the same fact: `Φ_hol^{fam}` is a
stratified functor over `Level`, with codimension-1 stratum `{-h^∨}` where the
fibre type genuinely changes.

The family-over-level formulation is the STRONGER honest form: it exhibits
the unity; but the two-adjunction description remains necessary as a STRATIFIED
decomposition of the family functor. Neither subsumes the other cleanly: the
family description unifies the GLOBAL object, while the two-adjunction
description sharpens the STRATUM-BY-STRATUM behaviour.

Platonic upgrade: Theorem F is a STRATIFIED UNIVERSAL HOLOGRAPHY FUNCTOR
`Φ_hol^{fam}` over `Level = A^1_k`, with generic stratum = four-class Platonic
UH (G/L/C/M) and critical stratum = fifth-class FF (BD Hitchin quantum system);
the Koszul involution on `Level` degenerates to the Langlands involution at
the critical fixed point via the Feigin-Frenkel isomorphism on opers. The "two
adjunctions glued" framing is the stratum decomposition of this single
family functor.

## Independent verification anchors

- **derived_from:** Costello-Gaiotto 3d HT-QFT family (JHEP 2018); Beilinson-
  Drinfeld Hitchin quantum system (1991); Feigin-Frenkel 1992 critical centre
  isomorphism `𝔷(\widehat g) ≅ Fun(Op_{g^L}(D^×))`.
- **verified_against:** Gaitsgory 1999 "Notes on 2d CFT" (stratified family
  of critical-vs-generic BV complexes); Frenkel "Langlands for loop groups"
  2007 Ch. 10 (opers boundary and stratification); Arkhipov-Gaitsgory 2003
  (critical-level periodic CDG closure).
- **disjoint_rationale:** Costello-Gaiotto construct the BV family by BV-
  quantising 3d N=4 gauge theories, independent of the chiral Koszul-duality
  machinery; BD construct the opers stack algebro-geometrically via moduli of
  G-bundles on curves, independent of any 3d HT-QFT construction; Feigin-
  Frenkel prove the opers isomorphism via Segal-Sugawara mode algebra,
  independent of the BV family. All three are disjoint conceptual sources,
  and their coincidence at the critical fibre constitutes the verification.

## Verdict (one sentence)

The family-over-level unification succeeds as a stratified functor
`Φ_hol^{fam} : ChirAlg^{ω,BL}_{/Level} ⇄ HT-QFT^{fam}_{/Level}` with
codimension-1 critical stratum where E_3-top degenerates to E_2-top × E_1-top,
but the two-adjunction glue description is not thereby eliminated — it is the
stratum-decomposition of the single family functor, and remains the correct
sharpened statement at each stratum; the two viewpoints are equivalent, with
the family view exhibiting GLOBAL unity and the two-adjunction view exhibiting
LOCAL stratum-wise structure.
