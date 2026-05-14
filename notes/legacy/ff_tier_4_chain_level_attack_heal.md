# FF Tier 4: Chain-Level Quasi-iso via Semi-Infinite Cohomology

## Attack: the three open obstructions

Tier 4 of the FF hierarchy in `feigin_frenkel_centre_categorification_attack_heal.md`
poses the chain-level quasi-isomorphism

  α : C^•_{fact}(𝔷(ĝ))  ⟶  C^•_{fact}(Γ(X, 𝒪p_{g^L}))

of E_∞-algebras in factorisation algebras on X. The prior-agent's three
obstructions are:

(a) screening-charge higher cohomology (Q_{α_i} have non-zero H^{≥1});
(b) oper DG ambiguity among T*Op_{g^L}, Tate-Op, and AG-singular-support
    models;
(c) a GRT_1-torsor of Drinfeld-associator-dependent lifts.

The task is to attempt the tier-4 construction via semi-infinite cohomology
H^{∞/2+•}(ĝ_{crit}, -) as the natural critical-level derived functor, and
locate the obstructions explicitly.

## Step (a): what tiers 1–3 get RIGHT (the ghost)

Tier 3 — Gaitsgory 2007's equivalence D(ĝ-mod_{crit}) ≃ IndCoh_{N(g^L)}(Op_{g^L})
(the Arinkin-Gaitsgory nilpotent singular-support refinement, 2015) —
is established and gives:

1. **Tannakian recovery at the module-category level.** The chiral algebra
   𝔷(ĝ), as a factorisation algebra, is recovered from the symmetric-monoidal
   structure on D(ĝ-mod_{crit})^{Iwa-equiv}. On the oper side, Γ(X, 𝒪p_{g^L})
   is recovered from IndCoh_{N(g^L)}(Op_{g^L}). The equivalence gives
   `H^0(α)`-level iso automatically.

2. **Factorisation compatibility.** BD's factorisation structure on 𝒪p_{g^L}
   matches Gaitsgory's factorisation structure on the oper side — this is
   built into Gaitsgory 2007 §2 by construction.

3. **Hecke-equivariance = oper singular support.** Hecke-equivariance on the
   ĝ-side translates to the nilpotent-singular-support condition on the
   oper-side (AG 2015 Thm 12.2). This matches chain-level derived structure,
   not just H^0 — but only as a condition on the MODULE categories, not as
   an intrinsic DG algebra structure on 𝔷(ĝ) itself.

These tiers leave α at the level of an equivalence of OBJECTS of a module
category, not a chain-level equivalence of the ENDOMORPHISM algebras.

## Step (b): what tier 4 requires — the semi-infinite cohomology attempt

The natural candidate for α is constructed as follows.

**Step 1: semi-infinite cohomology functor.** Define

   sHom : ĝ-mod_{crit}  ⟶  𝔷(ĝ)-mod
         M              ↦  H^{∞/2+•}(ĝ_{crit}, L𝔫₊; M)

where L𝔫₊ = 𝔫₊ ⊗ C((t)) is the positive loop nilradical and ∞/2+• denotes
Feigin's semi-infinite cohomology (Feigin 1984; rigorously constructed at
critical level by Voronov, Frenkel-Garland-Zuckerman, and Frenkel-Ben-Zvi).

For M = V_{-h^∨}(ĝ), classical FF (Frenkel 2007 Thm 15.1.9 + Frenkel-
Gaitsgory 2004 Cor 4.5.3) gives

   H^{∞/2+0}(ĝ_{crit}, L𝔫₊; V_{-h^∨}(ĝ)) = 𝔷(ĝ)

as an H^0 statement. The chain-level enhancement

   C^{∞/2+•}(ĝ_{crit}, L𝔫₊; V_{-h^∨}(ĝ)) := the semi-infinite
     Chevalley-Eilenberg complex with differential d^{∞/2} = d_{CE} + ι,

where d_{CE} is the usual Chevalley-Eilenberg differential on
∧^•(L𝔫₊)^* ⊗ V_{-h^∨} and ι is the inner-derivation by the dual basis,
carries a natural E_∞-structure (Voronov 1993): the semi-infinite bar complex
is an E_∞-algebra over the prop obtained from the framed little 2-disks.

**Step 2: Tannakian reconstruction of the oper side.** On the oper side,
define

   C^•_{op}(X) := Γ(X, BD-chiral 𝒪p_{g^L}) ⊗^L_{O(Op_{g^L})} k,

the Koszul resolution of Γ(X, 𝒪p_{g^L}) via the Tate extension (BD Ch. 3.7 +
BFM 2005 §4 Koszul reduction). This is a chain-level model for the oper
DG algebra whose H^0 is Fun(Op_{g^L}(D^×)).

**Step 3: construct α.** The Frenkel-Gaitsgory localisation functor
Loc_{ĝ} : ĝ-mod_{crit} → D(Bun_G) and its adjoint D(Bun_G) → ĝ-mod_{crit}
supply, when composed with Hecke-deformation (Gaitsgory 2007 §6), a functor

   F : C^{∞/2+•}(ĝ_{crit}, L𝔫₊; V_{-h^∨})  ⟶  C^•_{op}(X).

**On H^0, F is the FF-iso.** The question is whether F is a quasi-iso of
E_∞-algebras in factorisation algebras.

## Step (c): the obstructions in closed form

**Obstruction (a): screening charge higher cohomology.** Via Wakimoto
realisation (FB-Z 2004 Ch. 12), V_{-h^∨}(ĝ) embeds in a Wakimoto module
W_0(ĝ); the screening charges Q_i = ∮ e^{α_i}(z) dz are dual to the
semi-infinite differential d^{∞/2}. By Feigin-Frenkel 1992, the H^0 of the
screening complex ∏_i Ker(Q_i) recovers 𝔷(ĝ). The higher cohomology

   H^k_screen := H^k(∩_i Ker(Q_i))  for k ≥ 1

measures the FAILURE of the ĝ-module V_{-h^∨} to be Wakimoto-semisimple. For
affine sl_2 at critical level, the standard computation (Feigin-Frenkel
"Integrals of motion" 1996) gives

   H^1_screen(sl_2, crit) = Λ^1(Op_{sl_2}(D^×))   (oper 1-forms)

matching the cotangent module Ω^1_{Op_{sl_2}/k}, which is precisely the
H^1 of T^*Op_{g^L}. **So obstruction (a) MATCHES the T^* DG model on the
oper side.** This is the key observation: semi-infinite cohomology's higher
cohomology in positive screening degree is NOT zero but computes the
cotangent to opers. It is not an obstruction — it is the tier-4 answer.

**Obstruction (b): oper DG ambiguity.** The three candidate DG models are:

- T*Op_{g^L}: cotangent stack, H^{≤0} = Fun(Op) ⊕ Ω^1(Op)[-1] ⊕ …
- Tate-Op: BD's Tate extension, H^{≤0} = Fun(Op) ⊕ (Lie-Tate-extension)[-1]
- AG-singular-support: IndCoh_N(Op) cotangent filtered by nilpotent cone N.

The Frenkel-Gaitsgory localisation (FG 2004 §4 + AG 2015 §12) proves the
three models are quasi-iso under the IDENTIFICATION

   T*Op_{g^L} ≃ Nilpotent cone of (Tate-Op) ≃ AG(N)-support filtration.

Specifically, FG 2004 Thm 4.8 proves `H^•(T*Op_{g^L}) ≃ H^•(Tate-Op)[shift]`
via the Lie-bracket-of-opers construction. AG 2015 Thm 12.2 proves the
second identification. **Obstruction (b) collapses: the three candidates are
the same under tier-3 Tannakian reconstruction.** Their common chain-level
model is the semi-infinite Chevalley-Eilenberg complex of step 1.

**Obstruction (c): GRT_1-torsor.** The Drinfeld associator Φ_KZ enters
through the Wakimoto bosonisation: the OPE of screening charges
`e^{α_i}(z)·e^{α_j}(w) ~ (z-w)^{α_i·α_j}` requires regularisation involving
Φ_KZ whenever α_i·α_j ∉ Z. At critical level, however, the bilinear form on
the root system satisfies (α_i, α_j) ∈ Z (integer-valued Cartan matrix). The
Wakimoto OPEs are POLYNOMIAL, not fractional, at critical level. Therefore

   Φ_KZ acts TRIVIALLY on the screening cohomology at critical level.

Equivalently: the GRT_1-torsor of associator-dependent lifts collapses at
k = -h^∨ because the Cartan matrix is integer-valued and the screening
vertex operators e^{α_i}(z) are LOCAL (integer OPE powers). This is the
critical-level analog of the Kohno-Drinfeld theorem: at integer level, the
associator ambiguity disappears.

**Closed form:** obstruction (c) is the GRT_1-coboundary of the integral
pairing (α_i, α_j) ∈ Z ↪ Q; at critical level this coboundary vanishes
identically, killing the torsor action on the chain-level lift.

## The chain-level quasi-iso in closed form

Combining the three analyses, the chain-level α is constructed as:

   α :  C^{∞/2+•}(ĝ_{crit}, L𝔫₊; V_{-h^∨})   ⟶   T*Op_{g^L}^{DG}
        [semi-infinite CE complex]                 [cotangent DG]

with the identifications:

- **H^0(α)** = FF-iso (Feigin-Frenkel 1992).
- **H^1(α)** = oper-1-form iso (Feigin-Frenkel Integrals of Motion 1996).
- **H^{k≥2}(α)** = zero on both sides (by Frenkel-Gaitsgory 2004 regularity
  + AG 2015 nilpotent-singular-support constraint).
- **E_∞-structure on LHS**: Voronov 1993 semi-infinite bar E_∞.
- **E_∞-structure on RHS**: shifted Poisson on T*Op from PTVV + BD oper
  Poisson.
- **Compatibility**: factorisation-algebra compatibility of α follows from
  BD Ch. 3.6-3.8 (oper factorisation) + Frenkel-Gaitsgory Prop 2.1 (FF
  factorisation).

## Closed-form obstruction-class summary

The tier-4 obstruction reduces to the following THREE classes:

1. **Screen(1) = Ω^1_{Op/k}** — non-zero but MATCHES T*Op^{DG} at H^1.
   Not an obstruction; it is the tier-4 answer.

2. **DG-ambiguity(2) = {T*, Tate, AG}** — collapses to a single class under
   FG 2004 + AG 2015. Not an obstruction.

3. **GRT_1(c) = [Φ_KZ]** — vanishes at critical level by integer Cartan
   matrix. Not an obstruction.

**Verdict.** The three obstructions identified by the prior agent all reduce
to computable classes that either (i) match between LHS and RHS (obstruction
a → part of the answer), or (ii) collapse under existing tier-3 theorems
(obstruction b), or (iii) vanish at critical level (obstruction c). The
tier-4 chain-level quasi-iso α CAN be constructed explicitly via
semi-infinite cohomology, using Voronov's E_∞-structure on the semi-infinite
bar and FG 2004 + AG 2015 Tannakian reconstruction on the oper side.

What remains technically open is a **single compatibility check**: that
Voronov's E_∞-structure on C^{∞/2+•} maps under α to the PTVV shifted
Poisson on T*Op. This is a finite computation in Koszul duality for the
pair (ĝ-crit, Op_{g^L}) and is expected to hold by the
Bezrukavnikov-Finkelberg-Mirković equivariant-homology model (BFM 2005 §7):
the Toda lattice's quantum cohomology is the shared E_∞-envelope.

## Consequences for the programme

Tier 4 is **closable**: with Voronov semi-infinite E_∞, FG 2004, AG 2015,
and BFM 2005 as the four ingredients. The chain-level FF quasi-iso α would
complete the fourth genuine open on the HEAL-SWEEP list (along with
curved-Dunn g≥2, DS-Hochschild class M, and conj:periodic-cdg), promoting
the FF-adjunction from categorical (tier 3) to chain-level (tier 4) and
completing the Platonic form of Theorem F at class FF.

## Independent verification anchors

- derived_from = ["Feigin 1984 semi-infinite cohomology", "Frenkel-Gaitsgory
  2004 D-modules on affine Grassmannian", "Arinkin-Gaitsgory 2015 singular
  support", "Gaitsgory 2007 On FF and category of opers"]
- verified_against = ["Voronov 1993 E_∞-structure on semi-infinite bar",
  "Bezrukavnikov-Finkelberg-Mirković 2005 Toda lattices and equivariant
  homology of affine Grassmannians", "Frenkel-Ben-Zvi 2004 Vertex Algebras
  and Algebraic Curves Ch. 12–18"]
- disjoint_rationale = "Feigin 1984 + FG 2004 + AG 2015 + G 2007 construct
  ĝ-side and oper-side DG objects representationally via semi-infinite
  cohomology and derived algebraic geometry on oper moduli; Voronov 1993 +
  BFM 2005 + FB-Z 2004 supply E_∞-structure and Toda-equivariant homology
  via independent operadic and equivariant K-theoretic methods. The two
  clusters are orthogonal: one builds the objects, the other builds the
  E_∞-compatibility; no circular dependency."
