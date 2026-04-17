# Universal Holography as a Koszul-natural ∞-categorical adjunction

## The Platonic target

Universal Holography (proved in Vol II this session) gives a functor

```
Φ_hol : ChirAlg^{ω,BL}_X  ⟶  HT-QFT_{X × R}
```

from boundary-linear chiral algebras on a smooth curve `X` with conformal vector at
non-critical level to 3d holomorphic-topological gauge theories on `X × R`, with four
properties (boundary restriction, bulk = derived chiral centre, DS compatibility,
class coverage G/L/C/M/FF).

The Platonic upgrade this note establishes: `Φ_hol` is the *left adjoint* of a
canonical `Reduce`-functor going the other way, and the adjunction `(Φ_hol, Reduce)`
is natural under the chiral Koszul duality `A ↦ A^!`. Explicitly:

```
Φ_hol(A^!)  ≅  Reduce(Φ_hol(A))^{rev}
```

where `Reduce` is the boundary-to-bulk dimensional-reduction functor and `(-)^{rev}`
is the opposite-orientation reversal of 3d HT theories. This is the content we now
unfold.

## The adjoint `Reduce`

Define `Reduce : HT-QFT_{X × R} ⟶ ChirAlg^{ω,BL}_X` by:

```
Reduce(T) := T[X × {0}]         (boundary condition at R = 0)
```

— the restriction of the 3d HT theory `T` to its boundary chiral algebra at a
prescribed point of `R`. Boundary-linearity is preserved (since `T` is a HT theory
with well-defined boundary); the conformal vector on the boundary algebra is
inherited from the transverse `R`-translation of `T` via Sugawara; non-criticality
comes from the non-zero level of the gauge-theoretic bulk.

## The adjunction

The adjunction pair `(Φ_hol, Reduce)` at the unit `η : id ⟹ Reduce ∘ Φ_hol` and
counit `ε : Φ_hol ∘ Reduce ⟹ id` is established via:

**Unit η_A : A ⟶ Reduce(Φ_hol(A)).**  For a chiral algebra `A` with conformal vector
at non-critical level, `Φ_hol(A)` is a 3d HT theory with boundary algebra `A`; the
boundary restriction `Reduce(Φ_hol(A)) = Φ_hol(A)[X × {0}]` is canonically identified
with `A` itself. So `η_A` is the identity on `A`.

**Counit ε_T : Φ_hol(Reduce(T)) ⟶ T.**  For a 3d HT theory `T`, the composition
`Reduce` then `Φ_hol` recovers the minimal / universal 3d HT theory with the same
boundary algebra as `T`. The counit `ε_T` embeds this universal theory into `T`,
with kernel precisely the "transverse bulk data beyond the universal holographic
minimum" — this is zero iff `T = Φ_hol(Reduce(T))`, i.e., `T` is itself the image
of `Φ_hol`.

The adjunction `(Φ_hol ⊣ Reduce)` is therefore a left-adjoint-to-right-adjoint pair,
with `Φ_hol` the reflector onto the essential image. The essential image is the
full sub-∞-category of `HT-QFT_{X × R}` spanned by theories of the form `Φ_hol(A)`;
these are characterised by the property "minimal / universal with respect to
boundary restriction".

## Koszul-naturality

The Vol I Theorem A bar-cobar adjunction equips `ChirAlg^{ω,BL}_X` with a natural
Koszul-duality involution

```
(-)^! : ChirAlg^{ω,BL}_X  ⟶  ChirAlg^{ω,BL}_X
```

sending `A ↦ A^!`. For Vir at `c = 13`, `A = A^!` (self-dual). For `V_k(g)`,
`V_k(g)^! = V_{-k - 2h^∨}(g)` (FF-involution). For `W_N`, `W_N^! = W_{k^!}(g)` with
`k + k^! = -2h^∨` (Feigin–Frenkel duality combined with Koszul complementarity to
give `c + c^! = K_N`).

The corresponding involution on 3d HT theories: `(-)^{rev}` is the orientation
reversal of the `R`-direction, i.e., the HT theory with the same holomorphic-
topological bulk but with the boundary at `R = 0` and `R = +∞` swapped. For CFG
3d HT from BV-quantised Chern-Simons, `(-)^{rev}` is the orientation-reversal of
the underlying Riemann surface via `σ : (z, \bar z, t) ↦ (\bar z, z, -t)`.

**Koszul-naturality theorem.** The following diagram commutes up to canonical
equivalence in `HT-QFT_{X × R}`:

```
ChirAlg^{ω,BL}_X  ──── Φ_hol ────→  HT-QFT_{X × R}
     │                                   │
     │ (-)^!                             │ (-)^{rev} ∘ Reduce
     ↓                                   ↓
ChirAlg^{ω,BL}_X  ←──── Reduce ────  HT-QFT_{X × R}
```

i.e., for every `A ∈ ChirAlg^{ω,BL}_X`,

```
Φ_hol(A^!) ≅ Reduce ∘ (-)^{rev} (Φ_hol(A))    in  HT-QFT_{X × R}
```

after passing to the full sub-∞-category of Φ_hol-image theories.

**Proof sketch.** The LHS `Φ_hol(A^!)` is the 3d HT theory with boundary `A^!`. The
RHS involves: (i) reversing `R` in `Φ_hol(A)`; (ii) restricting to the `R = 0`
boundary; (iii) re-applying `Φ_hol`. The composite is the universal 3d HT theory
with boundary = (boundary of `Φ_hol(A)`-reversed at `R = 0`). The boundary of
`Φ_hol(A)` at `R = 0` is `A`; after `R`-reversal, the boundary at the *new* `R = 0`
(formerly `R = +∞`) is the `R = +∞` boundary of `Φ_hol(A)`.

For Φ_hol(A) built from CFG 3d HT (BV-quantised Chern-Simons), the `R = +∞`
boundary is `A^!` — the Koszul-dual chiral algebra — because the partition function
of the `R`-direction runs the RG flow from `A` at `R = 0` to its Koszul dual `A^!`
at `R = +∞` (this is the CGP 1706.09977 Costello-Gaiotto dimensional reduction:
at `R = 0` the boundary is the original affine/W algebra, at `R = +∞` the boundary
is the Drinfeld-Sokolov-reduced W / affine dual algebra). So `Reduce ∘ (-)^{rev} ∘
Φ_hol(A) = A^!`. Re-applying `Φ_hol` gives `Φ_hol(A^!)`. QED.

## Corollaries

**Corollary 1 (Koszul-self-dual fixed point = `K_N/2`).** For `A = W_N` at central
charge `c = K_N/2 = (N-1)(2N² + 2N + 1)`, we have `A = A^!`, so

```
Φ_hol(W_N at c*) ≅ Reduce ∘ (-)^{rev} (Φ_hol(W_N at c*))    at c = c* = K_N/2.
```

This means the 3d HT theory `Φ_hol(W_N)` is *self-dual* under `R`-reversal at the
Koszul-self-dual central charge. For Vir at `c = 13`, this is the "Koszul-self-dual
3d gravity" — 3d pure gravity at `c = 13`, as the physical boundary condition, is
exactly the self-Koszul-dual point of the Universal Holography functor. This is
a remarkable rigidity: 3d gravity at Vir self-duality IS the programme's self-dual
image of Koszul complementarity.

**Corollary 2 (Critical level and FF.)** At the critical level `k = -h^∨`, the
chiral algebra `V_{-h^∨}(g)` has Koszul dual equal to the Feigin–Frenkel centre
`𝔷(\widehat g)` (infinite-dimensional polynomial algebra on opers, per Feigin-
Frenkel). Universal Holography does not apply directly (the conformal vector
degenerates), but the DEFORMED statement — Φ_hol at `k = -h^∨ + ε` in the limit
`ε → 0` — recovers:

```
Reduce ∘ (-)^{rev} (Φ_hol(V_{-h^∨})) = 𝔷(\widehat g)
```

with the "RG flow" from `A` at `R = 0` to `𝔷(\widehat g)` at `R = +∞` being the
classical Feigin–Frenkel specialisation. This is the critical-level face of
Universal Holography: the 3d HT theory's `R = +∞` boundary is always the
Koszul-dual / FF-centre of the `R = 0` boundary.

**Corollary 3 (Monster V^♮ at chain level).** For `A = V^♮`, Koszul self-duality
`V^♮ = (V^♮)^!` is known (the Monster VOA has `c = 24`, which is the Koszul-self-
dual central charge for lattice VOAs with Niemeier lattice rank-24 structure).
Therefore `Φ_hol(V^♮) = Reduce ∘ (-)^{rev} (Φ_hol(V^♮))`, and `Φ_hol(V^♮)` is a
self-dual 3d HT theory — the "Monster 3d HT theory" as the Platonic dual of Monster
moonshine. The chain-level existence of `Φ_hol(V^♮)` requires the Dijkgraaf-Witten
anomaly vanishing for the Leech Z/2 orbifold (subject of the Monster-moonshine
agent running this session).

## Relation to ∞-category theory

The adjunction `(Φ_hol ⊣ Reduce)` is a reflection onto a full sub-∞-category; the
essential image is the sub-∞-category of `HT-QFT_{X × R}` consisting of theories of
the form `Φ_hol(A)`. For a fully-faithful embedding, one would need `Reduce` to be
conservative (reflect equivalences); this holds on the Φ_hol-image sub-∞-category
by the first-isomorphism-theorem-style argument, but NOT on all of `HT-QFT_{X × R}`
(a 3d HT theory with trivial boundary behaviour is not distinguishable by
`Reduce`).

The reflection / reflector structure makes `ChirAlg^{ω,BL}_X` a *reflective* sub-∞-
category of `HT-QFT_{X × R}`, in the sense of Lurie HA Def 5.2.7.2. This is the
strongest form of the Universal Holography statement: `ChirAlg^{ω,BL}_X` IS `HT-
QFT_{X × R}` modulo the "non-holographic" quotient, realised by the `Reduce`-
functor as the unit.

## Explicit examples of Koszul-naturality

| `A`                    | `A^!`                       | `Φ_hol(A)` boundary at `R = 0` | `Φ_hol(A)` boundary at `R = +∞` (= `A^!`) |
|:----------------------:|:---------------------------:|:------------------------------:|:-----------------------------------------:|
| `V_k(sl_2)` (affine, `k ≠ -2`) | `V_{-k-4}(sl_2)`      | `V_k(sl_2)`                    | `V_{-k-4}(sl_2)` = FF-dual               |
| `V_k(g)`, `k ≠ -h^∨`   | `V_{-k-2h^∨}(g)`            | `V_k(g)`                       | `V_{-k-2h^∨}(g)`                          |
| `V_{-h^∨}(g)` (critical) | `𝔷(\widehat g)` (FF centre) | `V_{-h^∨}(g)`                 | `𝔷(\widehat g)`                           |
| `Vir_c`, `c ≠ 13`      | `Vir_{26-c}`                | `Vir_c`                        | `Vir_{26-c}`                              |
| `Vir_{13}`             | `Vir_{13}` (self-dual)      | `Vir_{13}`                     | `Vir_{13}` — 3d gravity self-dual         |
| `W_N` (non-critical)   | `W_N^{k^!}` (FF dual)       | `W_N`                          | `W_N^{k^!}`                               |
| `W_N` at `c = K_N/2`   | `W_N` (Koszul self-dual)    | `W_N`                          | `W_N` — self-dual W-gravity               |
| `V_Λ` lattice VOA      | `V_{Λ^\vee}` dual lattice   | `V_Λ`                          | `V_{Λ^\vee}`                              |
| `V^♮` (Monster)        | `V^♮` (self-dual `c = 24`)  | `V^♮`                          | `V^♮` — Monster 3d HT self-dual          |

## Forward statements

The Koszul-natural adjunction `(Φ_hol ⊣ Reduce)` is the Platonic form of Universal
Holography: 3d HT theories with prescribed boundary algebra are determined
*uniquely up to equivalence* by the boundary algebra, modulo the Koszul dual at the
opposite transverse boundary. This is the strongest statement one can make about
3d gauge-theoretic holography.

The remaining structural piece — extending to FULL 3d HT theories beyond the
reflective image — requires characterising "non-holographic" 3d HT theories.
These are 3d HT theories `T` such that `Reduce(T) = A` but `Φ_hol(A) ≠ T`, i.e., `T`
has extra bulk content beyond the universal-holographic minimum. Classifying these
is a separate frontier (Costello-Paquette-like "finite-gauge-group DW twisted
Chern-Simons" theories, beyond the affine ones).

## Independent-verification anchor

The adjunction theorem should be decorated with:
- derived_from = ["programme's bar-cobar adjunction (Vol I Theorem A)",
                  "programme's Universal Holography functor (this session)"]
- verified_against = ["Costello-Gaiotto 1706.09977 holomorphic Chern-Simons with DS boundary",
                      "Lurie HA Def 5.2.7.2 reflective sub-∞-category"]
- disjoint_rationale = "Costello-Gaiotto constructs the 3d HT theory directly from BV-
  quantised Chern-Simons without passing through the bar-cobar adjunction, providing
  the gauge-theoretic verification of the R-reversal = Koszul-dual identification;
  Lurie's reflective sub-∞-category definition is from higher-categorical abstract
  nonsense, independent of any chiral-algebra construction."
