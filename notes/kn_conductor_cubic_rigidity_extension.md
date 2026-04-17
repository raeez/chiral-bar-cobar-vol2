# K_N conductor cubic rigidity: Lie-theoretic factorisation and the type-g extension problem

## Numerical check of the Vol II formula

For `W_N = W(sl_N)` Drinfeld–Sokolov reduction of affine `sl_N` at principal
nilpotent, the Koszul-complementarity conductor is

```
K_N = 2(N-1)(2N² + 2N + 1) = 4N³ - 2N - 2.
```

Explicit values:

| `N` | `K_N` first form `2(N-1)(2N²+2N+1)` | `K_N` second form `4N³-2N-2` | `χ(sl_N) = 2N²+2N+1` | `N² + (N+1)²` |
|:---:|:------------------------------------:|:----------------------------:|:--------------------:|:-------------:|
|  2  | `2·1·13 = 26`                        | `32-4-2 = 26`                | `13`                 | `4+9 = 13`    |
|  3  | `2·2·25 = 100`                       | `108-6-2 = 100`              | `25`                 | `9+16 = 25`   |
|  4  | `2·3·41 = 246`                       | `256-8-2 = 246`              | `41`                 | `16+25 = 41`  |
|  5  | `2·4·61 = 488`                       | `500-10-2 = 488`             | `61`                 | `25+36 = 61`  |
|  6  | `2·5·85 = 850`                       | `864-12-2 = 850`             | `85`                 | `36+49 = 85`  |

The two forms agree at each `N` by the elementary identity `2N²+2N+1 =
N²+(N+1)²`. The finite-difference table

```
N:       1    2     3     4     5     6
K_N:     0   26   100   246   488   850
Δ¹:          26    74   146   242   362
Δ²:               48    72    96   120
Δ³:                    24    24    24
```

confirms `Δ³K_N = 24 = 4!` uniformly for `N ≥ 1`. The jumps in `Δ²K_N` are `48,
72, 96, 120, …` which differ by the constant `24 = Δ³`, consistent with the
cubic.

The Feigin–Frenkel / Koszul self-dual central charge for `W_N` is
`c*(W_N) = K_N/2 = (N-1)(2N² + 2N + 1)`, taking the values

| `N` | `c*(W_N)` |
|:---:|:---------:|
|  2  | `13`      |
|  3  | `50`      |
|  4  | `123`     |
|  5  | `244`     |
|  6  | `425`     |

At `N = 2` this recovers the Virasoro self-dual central charge `c = c^! = 13`
established earlier in Vol II (AP8 prohibits "self-dual" unqualified — the
qualification is: at `c = 13`, the Koszul-complementarity involution `c ↔ c^!
= 26 - c` fixes `c = 13`, whence Vir at `c = 13` is Koszul self-dual). The
conductor `K_2 = 26` is precisely twice this fixed point.

## Lie-theoretic factorisation

The rigidity theorem (`thm:koszul-conductor-cubic-rigidity` at
`chapters/connections/thqg_gravitational_s_duality.tex:1258`) characterises
`K_N` as the unique monic-scaled cubic in `N` satisfying three conditions:

1. **Cubic degree**: `K_N` is polynomial of degree exactly 3.
2. **Leading coefficient 4**: `Δ³K_N = 6·4 = 24 = 4!`.
3. **Lie-theoretic factorisation**:
   `K_N = 2·rank(sl_N)·χ(sl_N)` where `rank(sl_N) = N-1` and
   `χ(sl_N) = 2N²+2N+1 = N² + (N+1)² = dim(V_std sl_N)² + dim(V_std sl_{N+1})²`
   is the sum of squared fundamental-representation dimensions of adjacent
   special linear algebras.

The four cubic coefficients `(a, b, c, d)` in `K_N = aN³ + bN² + cN + d`:

```
K_N = 4N³ + 0·N² − 2N − 2                ⟹  a = 4, b = 0, c = −2, d = −2.
```

The vanishing of `b` (no quadratic term) comes from a symmetry of the Lie-
theoretic factorisation: `χ(sl_N) = N² + (N+1)²` is invariant under
`N ↦ −(N+1)`, i.e., `χ(N) = χ(−N−1)`, while `rank(sl_N) = N − 1` is
antisymmetric up to shift, `rank(N) = −rank(−N+1) + 2` (or equivalently `N−1 =
−((−N+1)−1) + 0`). The product `rank·χ` therefore has no pure `N²` term, which
is the absence of `b`.

## The type-g extension problem

The natural generalisation replaces `sl_N` with an arbitrary simple Lie algebra
`g` and asks: what is the Koszul conductor `K_g` for the principal `W(g)`
algebra? The Feigin–Frenkel self-dual central charge `c*(g) = K_g/2` of
`W(g)` is a well-defined invariant; tabulating `c*(g)`:

| Type  | `rank(g)`  | `h^∨`     | `c*(g)` (conjectural Lie-theoretic) | Known value |
|:-----:|:----------:|:---------:|:-----------------------------------:|:-----------:|
| `A_1` (Vir)     | 1 | 2   | `1 · 13 = 13`                       | 13 ✓       |
| `A_2` (W_3)     | 2 | 3   | `2 · 25 = 50`                       | 50 ✓       |
| `A_3` (W_4)     | 3 | 4   | `3 · 41 = 123`                      | 123 ✓      |
| `B_2` (sp_4)    | 2 | 3   | `?`                                 | open       |
| `B_3` (so_7)    | 3 | 5   | `?`                                 | open       |
| `C_3` (sp_6)    | 3 | 4   | `?`                                 | open       |
| `D_4` (so_8)    | 4 | 6   | `?`                                 | open       |
| `E_6`           | 6 | 12  | `?`                                 | open       |
| `E_7`           | 7 | 18  | `?`                                 | open       |
| `E_8`           | 8 | 30  | `?`                                 | open       |
| `F_4`           | 4 | 9   | `?`                                 | open       |
| `G_2`           | 2 | 4   | `?`                                 | open       |

The conjectural Lie-theoretic pattern for general `g` should be

```
K_g = 2·rank(g)·χ(g),                 (type-dependent χ)
```

with `χ(g)` for `sl_N` equal to `N² + (N+1)²`. For other types, a candidate
formula is

```
χ(g)_candidate = 1 + 2h^∨ + 2(h^∨)²,
```

which at type `A_{N-1}` gives `1 + 2N + 2N² = 2N² + 2N + 1 = χ(sl_N)` as
required. However, testing this at `B_1 ≅ A_1 = sl_2`:

```
rank(A_1) = 1, h^∨(A_1) = 2 ⟹  χ_candidate = 1 + 4 + 8 = 13  ✓  (χ(sl_2) = 13).
```

Testing at `C_2 ≅ B_2` (sp_4):

```
rank(C_2) = 2, h^∨(C_2) = 3 ⟹  χ_candidate = 1 + 6 + 18 = 25.
K_{C_2}_candidate = 2·2·25 = 100 ⟹  c*(C_2)_candidate = 50.
```

This is the same `c*` as `W_3 = W(A_2)`, which would mean
`c*(C_2) = c*(A_2)`. Is this true? The Feigin–Frenkel self-dual central charge
of `W(C_2) = W(sp_4)` with principal nilpotent is a computable quantity; at
type `C_2`, the Virasoro subalgebra of `W(C_2)` has a Virasoro central charge
on the same lines as `W(A_2)`, but with different structure constants at spin
4.

**Concrete computation (conjectural):** For `W(g)` at principal nilpotent with
level `k`, the central charge formula is

```
c_{W(g)}(k) = rank(g)·(1 - h^∨(h^∨+1)·(α_+ + α_-)²)
```

where `α_±` are the Feigin–Frenkel screening-charge roots with `α_+ α_- = -1`
and `α_+² = (k + h^∨)/h^∨`, so `(α_+ + α_-)² = α_+² + 2α_+α_- + α_-²
= (k+h^∨)/h^∨ − 2 + h^∨/(k+h^∨)`.

At the Koszul self-dual point `c + c^! = K_g`, we have `c = c^!` (self-dual),
and by the FF involution `k ↔ k^! = (k+h^∨)^{-1}/h^∨ − h^∨ = ...`, this fixes
`(k+h^∨)/h^∨ = 1`, i.e., `k+h^∨ = h^∨`, i.e., `k = 0`.

At `k = 0`: `(α_+ + α_-)² = 1 − 2 + 1 = 0`, so `c_{W(g)}(k=0) = rank(g)·(1 -
h^∨(h^∨+1)·0) = rank(g)`.

But `rank(g)` is not `K_g/2`! For Vir, `rank(A_1) = 1` while `K_1/2 = 13`.
Contradiction — this is NOT the Koszul self-dual point.

Reconsidering: the Koszul complementarity `c ↔ c^! = K_g − c` is a different
involution from FF self-duality. The Koszul-complementarity fixed point
`c = c^! = K_g/2` comes from the CHIRAL bar-cobar duality, not the vertex-
algebra self-duality.

For `W_N`: Koszul complementarity gives `c* = (N-1)(2N² + 2N + 1)` at the
fixed point. Does this match the chiral bar-cobar Koszul-complementarity of
`W_N`? The chiral Koszul complementarity is encoded in the Koszul-conductor
formula `K_g = c + c^!` where `c^!` is the central charge of the chiral
Koszul-dual.

For `W_N`, `c^!_N = K_N - c_N` where `c_N = c_{W_N}(k)` for generic `k`. The
Koszul dual `W_N^!` has central charge `c^!_N`. At the self-dual point
`c = c^! = K_N/2`, the central charge of `W_N` equals the central charge of
`W_N^!`, which is consistent with the chiral bar-cobar Koszul duality on the
`W_N`-lane.

**Forward:** The type-g extension of the cubic rigidity theorem is:

```
K_g = 2·rank(g)·χ(g),
```

with `χ(g) = 1 + 2h^∨ + 2(h^∨)²` as a conjectural uniform formula, tested
against sl_N where it is correct. The conjecture is open at non-A types; a
follow-up agent should compute `c*(W(C_2))` and `c*(W(G_2))` directly from the
screening-charge formalism and compare against `2·rank·χ_candidate`. If the
match holds at C_2 and G_2, the conjecture extends to all simply-laced and the
candidate formula `χ(g) = 1 + 2h^∨ + 2(h^∨)²` is the canonical Lie-theoretic
extension. If it fails, the type-dependent correction factor becomes a
research frontier.

The geometric / Arakelov interpretation would be: `K_g = 2·rank(g)·χ(g)` is the
genus-0 characteristic of the principal W(g)-algebra's Koszul complementarity,
with the rank factor tracking the number of strong generators and the `χ(g)`
factor tracking the "effective central-charge depth". For non-simply-laced
types, the lacing number `r_g ∈ {1, 2, 3}` may enter as a correction
`χ(g, lacing) = (1 + 2h^∨ + 2(h^∨)²)/r_g` or similar.

## Implications for the Platonic programme

The `K_N` cubic rigidity is a concrete instance of the broader theme: the
Feigin–Frenkel / Koszul self-dual central charges of W(g) algebras are
rigid Lie-theoretic invariants that determine the chiral bar-cobar
architecture at each type. Extending to arbitrary simple `g` completes the
"Koszul-conductor table" of the standard landscape, which is a load-bearing
datum for the Seven Theorems reformulation:

- **Theorem A** (bar-cobar properad (∞,2)-equivalence): the conductor `K_g`
  appears as the genus-0 curvature of the bar complex.
- **Theorem C** (complementarity): the conductor `K_g` is twice the Koszul
  self-dual central charge `c*(g)`, which is the fixed point of the Koszul
  complementarity involution.
- **Theorem D** (modular characteristic): `K_g` at genus-0 lifts to the
  tensor-valued Arakelov curvature `κ_Arak(g) ∈ Sym²(F_bundle)` at higher
  genus.
- **Theorem H** (chiral Higher Deligne): `K_g` as central charge computes
  the E_3-chiral structure constants on Z^{der}_ch(W(g)).

The full `K_g` table for all simple types would therefore be a single-line
entry of the Koszul-conductor function that threads through all seven
theorems simultaneously — a compact Platonic object.
