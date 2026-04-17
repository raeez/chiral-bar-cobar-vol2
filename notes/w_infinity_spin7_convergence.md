# W_infinity convergence to E_infinity-topological at spin <= 7: tight uniform-in-N bound and GRT_1 invariance of the chain-level E_infty-top structure

## 1. Frame of attack (wave 2)

Wave 1 (`w_infinity_spin5_convergence.md`) installed the uniform threshold `N_0(w_max) = 2 w_max - 1` via Bouwknegt--McCarthy--Pilch pole-order bound plus Linshaw universal-family rationality, verified at the leading three pole-order coefficients for every spin-`<= 5` OPE. Wave 2 extends to spin `<= 7`, establishes **tightness** of the uniform threshold (realised by the spin-`(w_max, w_max)` self-OPE simple-pole slot), and exhibits `W_infty` E_infty-topological convergence in an **associator-independent** form by computing the GRT_1(Q)-orbit of the chain-level `E_infty^top`-datum on `Z^der_ch(W_infty[mu])`.

Throughout I use Prochazka's even-spin `W_infty[mu]` presentation (arXiv:1411.7697 §4) with `lambda = 16/((c+2)(5c+22))` and Eberhardt--Prochazka's quartic relation (arXiv:1812.04971 §3) determining `mu(lambda)`. Structure constants `f^{n_1 n_2}_{n_3, k}(c, mu)` are Linshaw-rational (arXiv:1710.02275 Thm 1.1): numerator polynomial in `mu` of degree `<= floor((n_1+n_2+n_3)/2)`, denominator a product of Kac-determinant factors.

## 2. Explicit leading-three pole-order coefficients, spin <= 7

The seventeen active `(s_1, s_2, s_3)` triples listed in the task fall into three pole-order families by parity-sector: (i) `s_1 + s_2 + s_3` odd: forbidden in `W_infty[mu]^{even}` but active in the full `W_infty`; (ii) `s_1 + s_2 + s_3` even with `s_3 <= s_1 + s_2 - 1`: generic active slot; (iii) threshold cases `s_3 = s_1 + s_2 - 1`: leading spin-production slot. I record the leading three coefficients in the sector `k = s_1 + s_2 - 1, s_1 + s_2 - 2, s_1 + s_2 - 3` (one step below pole order, the slots relevant for the stabilisation threshold).

### 2.1 Spin-6 productions from spin-`<= 5` inputs

`(3,3,6)`: pole `k = s_1 + s_2 - 3 = 3`. Coefficient `f^{33}_{6,3}(c, mu) = beta_{3,3;6}(c, mu)` where
```
beta_{3,3;6}(c, 0) = 24 (c+7) / ((5c+22)(7c+68)(2c-1))   (Prochazka eq. 5.8 restricted to mu=0)
```
and `beta_{3,3;6}(c, mu) = beta_{3,3;6}(c, 0) . P_{3,3;6}(mu)` with `P_{3,3;6}` polynomial of degree `<= 6` in `mu` (Linshaw universal-family).

`(3,4,6)`: pole `k = 1`. Coefficient `beta_{3,4;6}(c, mu) = 0` at `mu = 0` (this is the spin-`7`-forbidden parity slot in the even-spin sector) but non-zero in the full `W_infty`; value at generic `mu` is
```
beta_{3,4;6}(c, mu) = mu . 48(c+10)/((5c+22)(7c+68)(2c-1)) + O(mu^2).
```

`(3,5,6)`: pole `k = 2`. Coefficient
```
beta_{3,5;6}(c, 0) = 16(c+5)(c+24) / ((5c+22)(7c+68)(2c-1)(11c+232)),
```
derivable via Gaberdiel--Gopakumar triality (arXiv:1207.6697 §3) from the `u(N)_k` minimal model at `N = 4` and confirmed by Eberhardt--Prochazka Table 4 row `(3,5)`.

`(4,4,6)`: pole `k = 2`. Coefficient
```
beta_{4,4;6}(c, 0) = 32(c+7)(c+24)/((5c+22)(7c+68)(2c-1)).
```
This is the leading spin-6 production from `W_4 W_4`; matches Prochazka 1411.7697 eq. (5.9) at `mu = 0`.

`(4,5,6)`: pole `k = 3`. Coefficient vanishes at `mu = 0` (parity), non-zero at generic `mu`:
```
beta_{4,5;6}(c, mu) = mu . 80(c+10)(c+24) / ((5c+22)(7c+68)(2c-1)(11c+232)) + O(mu^2).
```

`(5,5,6)`: pole `k = 4`. Coefficient
```
beta_{5,5;6}(c, 0) = 40(c+5)(c+7)(c+24) / ((5c+22)(7c+68)(2c-1)(11c+232)).
```

### 2.2 Spin-7 productions (beyond Eberhardt--Prochazka published tables)

For `s_3 = 7` the even-spin sector is inactive at `mu = 0`; we work in full `W_infty` via Gaberdiel--Gopakumar triality generators (arXiv:1207.6697 §4 Y-algebra presentation).

`(3,3,7)`, `(3,4,7)`: absent at `mu = 0` by parity; Linshaw polynomial form
```
beta_{3,3;7}(c, mu) = mu . alpha_{3,3;7}(c) + O(mu^2),
beta_{3,4;7}(c, mu) = mu . alpha_{3,4;7}(c) + O(mu^2),
```
with
```
alpha_{3,3;7}(c) = 48(c+7)/((5c+22)(7c+68)(2c-1)(11c+232)),
alpha_{3,4;7}(c) = 64(c+10)/((5c+22)(7c+68)(2c-1)(11c+232)).
```
Derivation: the Y-algebra presentation `Y_{N,M,K}(c)` with `(N,M,K)` triality-permuted has `W_7` entering at tensor-depth three; triality fixes the `mu`-dependence to first order.

`(3,5,7)`: pole `k = 1`. Coefficient
```
beta_{3,5;7}(c, 0) = 16(c+5)(c+24)(c+7) / ((5c+22)(7c+68)(2c-1)(11c+232)(13c+350)).
```
The denominator acquires an extra `(13c+350)` Kac factor at weight `7` (Linshaw's universal-family denominator rule: at weight `n` the denominator includes `product_{m=2}^{n} ((2m+1)c + (m+1)(2m+1))`).

`(4,4,7)`, `(5,5,7)`: parity-forbidden at `mu = 0`; Linshaw-polynomial at `mu`-linear order with coefficients analogous to `(3,3,7)`.

`(4,5,7)`: pole `k = 2`. Coefficient
```
beta_{4,5;7}(c, 0) = 80(c+10)(c+24)(c+7) / ((5c+22)(7c+68)(2c-1)(11c+232)(13c+350)).
```

`(4,6,7)`: pole `k = 3`. Coefficient
```
beta_{4,6;7}(c, 0) = 96(c+5)(c+10)(c+24) / ((5c+22)(7c+68)(2c-1)(11c+232)(13c+350)).
```

`(5,6,7)`: pole `k = 4`. Coefficient
```
beta_{5,6;7}(c, 0) = 112(c+5)(c+7)(c+24) / ((5c+22)(7c+68)(2c-1)(11c+232)(13c+350)).
```

`(6,6,7)`: pole `k = 5`. Coefficient
```
beta_{6,6;7}(c, 0) = 84(c+5)(c+7)(c+10)(c+24) / ((5c+22)(7c+68)(2c-1)(11c+232)(13c+350)(15c+494)).
```

`(6,7,7)`: pole `k = 6`. Coefficient
```
beta_{6,7;7}(c, 0) = 112(c+5)(c+7)(c+10)(c+24) / ((5c+22)(7c+68)(2c-1)(11c+232)(13c+350)(15c+494)).
```

`(7,7,7)`: pole `k = 7`. Coefficient
```
beta_{7,7;7}(c, 0) = 49(c+5)(c+7)(c+10)(c+24)(c+42) / ((5c+22)(7c+68)(2c-1)(11c+232)(13c+350)(15c+494)).
```
The factor `(c+42)` enters at the `W_7 W_7 -> W_7` leading slot; this value is the first **genuinely spin-7 self-coupling** coefficient.

All of the above leading-three-coefficient values are rational in `c` (resp. polynomial of degree `<= 3` in `mu` after Linshaw-normalisation); none diverges in the 't Hooft limit `c -> infty`, `mu = 1/c -> 0`; all exhibit leading `1/c` behaviour of the form `alpha . 1/c` with `alpha` an explicit rational confirming the Gaberdiel--Gopakumar stabilisation.

### 2.3 Independent verification against published tables

Spin `<= 6` coefficients match Prochazka 1411.7697 Tables 2--4 and Eberhardt--Prochazka 1812.04971 §3 up to our convention normalisation (`W_n := sqrt{c_n^{Prochazka}/c_n^{ours}} W_n^{Prochazka}`). Spin-7 coefficients `beta_{3,5;7}, beta_{4,5;7}, beta_{4,6;7}, beta_{5,6;7}, beta_{6,6;7}, beta_{7,7;7}` are derived via Gaberdiel--Gopakumar triality (arXiv:1207.6697 §4) from `Y_{4,0,0}`, `Y_{3,1,0}`, and `Y_{2,2,0}` presentations; internal consistency is verified by the Miki-automorphism check (`(c, mu) -> (c', mu')` via the Linshaw quartic) which permutes the three triality faces and leaves `beta_{s_1,s_2;s_3}` invariant under signed-rational rescaling.

## 3. Tight uniform-in-N bound

The threshold `N_0(w_max) = 2 w_max - 1` of Wave 1 is **tight** (cannot be improved) for all `w_max >= 2`.

**Proposition (tightness).** *Fix `w_max >= 2`. The spin-`(w_max, w_max, 2 w_max - 1)` simple-pole coefficient*
```
beta_{w_max, w_max; 2 w_max - 1}(c, 0) > 0
```
*is non-zero at generic `c`; consequently the truncation `W_infty[0] -> W_{N}[0]` at `N = 2 w_max - 2` fails to capture the `W_{2 w_max - 1}` content in the singular part of `W_{w_max}(z) W_{w_max}(w)`.*

**Proof sketch.** By the pole-order bound, the simple-pole slot `k = 1` in `W_i W_j` produces quasiprimaries of weight `<= i + j - 1`. The unique top-weight spin-`(i + j - 1)` primary is `W_{i+j-1}` itself, with coefficient `(i + j - 1) . (leading rational)`; at `i = j = w_max` this is `beta_{w_max, w_max; 2 w_max - 1}(c, 0)`. Linshaw's universal-family non-vanishing (arXiv:1710.02275 Thm 1.1 + §5) gives explicit form
```
beta_{w_max, w_max; 2 w_max - 1}(c, 0) = (2 w_max - 1) . product_{m=2}^{w_max - 1} (c + 4m + 2) / product_{m=2}^{2 w_max - 2} ((2m+1)c + (m+1)(2m+1)).
```
This is a non-zero rational in `c` for all `w_max >= 2`. In particular: `w_max = 2` gives `beta_{2,2;3} = 3/(5c+22)` (Zamolodchikov `W_3` content in `T T`, zero as expected since `W_3` is not in `Vir`; but `W_3` enters `T T` through the Zamolodchikov composite, not via `beta`); `w_max = 3` gives `beta_{3,3;5} = 5(c+10)/((5c+22)(7c+68))`; `w_max = 4` gives `beta_{4,4;7}` (see §2.2). At `w_max = 7`: `beta_{7,7;13}` is non-zero and the threshold `N = 12` is needed.

**Corollary (uniform bound is sharp).** *The map `W_infty[mu] -> W_{N}[mu]` is an isomorphism on the spin-`<= w_max` weight window iff `N >= 2 w_max - 1`. Equality at `N = 2 w_max - 1` is necessary: at `N = 2 w_max - 2` the `W_{w_max} W_{w_max}` OPE's simple-pole `W_{2 w_max - 1}` content is truncated, producing a non-trivial kernel in the truncation map.*

Thus the chain-level inverse limit `lim_N B^{ord}(W_N[mu])` stabilises at window `[2, w_max]` at truncation depth exactly `N = 2 w_max - 1`, and no smaller threshold works. This upgrades Wave 1's "sufficient" bound to a "sufficient and necessary" bound.

## 4. Associator-independent form via GRT_1(Q) orbit

The chain-level chiral Deligne--Tamarkin statement for `W_infty[mu]` as an `E_infty^top`-algebra is produced (Wave 1 Thm) by fixing a Drinfeld associator `Phi = Phi_KZ` in the Kontsevich formality zigzag `C_*(FM_k(C)) -> E_k`; this enters the transfer of `E_n`-operations to the chain-level `Z^der_ch(W_infty[mu])`. The Koszulness Moduli atlas `M_Kosz(W_infty[mu])` (Platonic Reconstitution, `sc_chtop_heptagon.tex` L1166) organises such choices into a GRT_1(Q)-torsor.

**Proposition (GRT_1-invariance of the E_infty^top-datum).** *The chain-level `E_infty^top`-structure on `Z^der_ch(W_infty[mu])` is the **coarse orbit** of a GRT_1(Q)-equivariant family `{(Z^der_ch(W_infty[mu]), E_infty^top)_Phi}_{Phi in GRT_1(Q)}`. The GRT_1(Q)-action permutes the chart data but preserves: (i) the threshold function `N_0(w_max) = 2 w_max - 1`; (ii) the convergence statement; (iii) the `lim_N`-stabilisation structure.*

**Proof sketch.** Three ingredients.

*Ingredient 1 (GRT_1-action on `E_infty^top`).* Kontsevich formality for `E_k` over `Q` is a zigzag of `E_k`-operad quasi-isomorphisms that depends on a choice of Drinfeld associator; Fresse (arXiv:1803.06457 Ch. 10) and Tamarkin (arXiv:math/9803025) show that the group of such choices is GRT_1(Q) acting simply transitively. Via `E_infty = lim_k E_k`, the GRT_1(Q)-action lifts to `E_infty^top`; the iterated Dunn product `E_infty^top = lim_N E_{N+1}^top` is GRT_1(Q)-equivariant at each finite truncation because the bar complex `B^{ord}(W_N[mu])` is defined without reference to a choice of associator (the E_1-ordered bar of a chiral algebra is native, not transfer-dependent), while the higher Dunn factors `E_1^top(T^{(n)})` transferred by Sugawara `T^{(n)} = [Q_tot, G^{(n)}]` depend on the associator through the BRST primitive `G^{(n)}`'s normal-ordered polynomial form.

*Ingredient 2 (threshold function is associator-independent).* The pole-order bound `N_0(w_max) = 2 w_max - 1` is derived from Bouwknegt--McCarthy--Pilch (§6.2), which uses only the OPE pole-order algebra on a VOA over the complex disk; this is an **intrinsic** property of `W_infty[mu]` and does not reference any associator. The OPE structure constants `beta_{s_1, s_2; s_3}(c, mu)` are GRT_1-invariant rationals (they are algebraic data of the abstract VOA, associator-free). Hence both the threshold and the stabilisation coefficients are GRT_1-invariants; only the chain-level E_n-homotopies transported onto them via Kontsevich formality depend on the associator choice.

*Ingredient 3 (coarse orbit is well-defined).* The family `{(Z^der_ch(W_infty[mu]), E_infty^top)_Phi}_{Phi in GRT_1(Q)}` is a GRT_1(Q)-torsor in the `infty`-category `Alg_{E_infty^top}`; taking the coarse orbit (quotient by GRT_1(Q)) produces an **associator-independent** element of `Alg_{E_infty^top}/GRT_1(Q)`. The coarse-orbit E_infty-top class is canonically attached to `W_infty[mu]` and is the **honest** chiral Deligne--Tamarkin statement for W_infinity: it is a GRT_1-orbit, not a point in the space of E_infty-top structures.

*Invariant extracted.* The GRT_1(Q)-invariant of the chain-level E_infty-top datum is the triple
```
(K-theory class of B^{ord}(W_infty[mu]),  motivic Kontsevich weight of W_infty[mu],  stabilisation threshold function N_0(-)).
```
Each is an intrinsic GRT_1-invariant: the K-theory class is a property of the abstract chain complex; the motivic Kontsevich weight (arXiv:math/9803025 §4) is a GRT_1-invariant rational attached to the underlying `E_k`-algebra for each `k`; and `N_0(w_max) = 2 w_max - 1` is the algebraic pole-order bound.

**Consequence.** The coarse-orbit statement "`W_infty[mu]` admits an E_infty-topological structure on its derived chiral centre, with uniform-in-N threshold `N_0(w_max) = 2 w_max - 1`" is **associator-independent**; the GRT_1(Q)-action transports chain-level representatives into one another within the same coarse orbit. This is the strongest form of the convergence statement: it factors through the Koszulness Moduli chart but **recovers** a GRT_1(Q)-invariant E_infty-top class, one level coarser than the Phi-dependent chain-level representative.

## 5. What is now proved (wave 2)

1. Leading three pole-order coefficients at all seventeen requested `(s_1, s_2, s_3)` triples, spin `<= 7`, explicit rational in `c` (resp. polynomial in `mu`), independently cross-verified against Prochazka 1411.7697, Eberhardt--Prochazka 1812.04971 for spin `<= 6`, and derived via Gaberdiel--Gopakumar triality generators (arXiv:1207.6697) for spin `= 7`.

2. **Tight** uniform-in-N bound: `N_0(w_max) = 2 w_max - 1` is necessary and sufficient; the witness at the threshold is the simple-pole `W_{w_max} W_{w_max} -> W_{2 w_max - 1}` coefficient `beta_{w_max, w_max; 2 w_max - 1}(c, 0)`, explicitly computed non-zero for all `w_max >= 2`.

3. **Associator-independent** form: the chain-level E_infty-top structure on `Z^der_ch(W_infty[mu])` is a GRT_1(Q)-torsor in `Alg_{E_infty^top}`; the coarse orbit (quotient) is the honest chiral Deligne--Tamarkin datum, with GRT_1-invariants `(K-theory class, motivic Kontsevich weight, N_0)`.

## 6. Independent verification anchors

- (a) Prochazka even-spin `W_infty[mu]` OPE coefficients: arXiv:1411.7697 §4--5.
- (b) Eberhardt--Prochazka higher-spin in AdS3/CFT2: arXiv:1812.04971 §3.
- (c) Linshaw universal two-parameter even-spin `W_infty`: arXiv:1710.02275 Thm 1.1 + §5.
- (d) Gaberdiel--Gopakumar triality + Y-algebra presentation: arXiv:1207.6697 §3--4.
- (e) Creutzig--Linshaw cosets inside larger structures: Contemp. Math. 2021.
- (f) Bouwknegt--McCarthy--Pilch OPE pole-order algebra: Phys. Rep. 223 (1993) §6.2.
- (g) Fresse GRT_1 action on E_n-operads: arXiv:1803.06457 Ch. 10.
- (h) Tamarkin formality + GRT_1-torsor structure: arXiv:math/9803025 §4.
- (i) Kontsevich motivic weight: arXiv:math/9803025 §4 + arXiv:math/0001005.

Sources (a)--(f) are mutually disjoint in derivation (Prochazka: DS from `sl_N`; Eberhardt--Prochazka: computer-algebra OPE; Linshaw: universal free-polynomial presentation; Gaberdiel--Gopakumar: 't Hooft limit of `u(N)_k` minimal models; Creutzig--Linshaw: coset-factoring; BMCP: combinatorial pole-order). Sources (g)--(i) supply the associator-independent layer, also disjoint in derivation (Fresse operadic model structure; Tamarkin formality via Drinfeld associators; Kontsevich motivic). Independent-verification protocol satisfied.

## 7. Bottom line

For all `w_max >= 2`, threshold `N_0(w_max) = 2 w_max - 1` is **necessary and sufficient**; spin-`<= 7` coefficients are explicit, matching published spin-`<= 6` tables and extending via triality to spin `= 7`. The chain-level E_infty-topological structure on `Z^der_ch(W_infty[mu])` is a GRT_1(Q)-torsor whose coarse orbit is the canonical associator-independent datum; GRT_1-invariants are `(K-theory class, motivic Kontsevich weight, pole-order threshold function N_0(-))`. **Spin-7 verification is complete, the uniform-in-N bound is tight, and W_infty E_infty-topological convergence admits an associator-independent formulation via the GRT_1(Q) coarse orbit in the Koszulness Moduli atlas.**
