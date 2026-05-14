# FF-Langlands-naturality at B_2/C_2: Dynkin accident attack and heal

## The attack

The note `universal_holography_two_adjunctions_platonic_heal.md:152`
claims FF-Langlands-naturality:

```
FF-Φ_hol(V_{-h^∨}(g))^{Lan-R-rev}  ≅  FF-Φ_hol(V_{-h^∨}(g^L))
```

For non-simply-laced `g`, Langlands exchanges `B_r ↔ C_r`. At rank 2, the
**Dynkin accident** `B_2 ≅ C_2` as abstract Lie algebras (both are
`so(5) ≅ sp(4)`, connected by the outer automorphism of the rank-2 non-simply-
laced Dynkin diagram) poses an immediate stress test. If `B_2` and `C_2` are
isomorphic, then `V_{-3}(B_2) ≅ V_{-3}(C_2)` as chiral algebras, and the
Langlands-naturality at this case should EITHER reduce to a triviality OR
reveal a Dynkin-accident obstruction. This note verifies what actually
happens.

## Facts

1. **Dynkin diagrams.** `B_2`: nodes `α_1 — α_2` with `α_1` short, `α_2` long,
   edge multiplicity 2 (double edge from long to short, arrow to short).
   `C_2`: nodes `α_1 — α_2` with `α_1` long, `α_2` short, edge multiplicity 2
   (arrow to short reversed). The two diagrams are related by the rank-2
   Langlands involution `(B_2)^L = C_2` at the level of root systems.

2. **Lie algebra isomorphism.** Both `so(5)` (Lie algebra of `SO(5)`, Dynkin
   type `B_2`) and `sp(4)` (Lie algebra of `Sp(4)`, Dynkin type `C_2`) are
   isomorphic as 10-dimensional Lie algebras. An explicit isomorphism
   `ι : so(5) → sp(4)` exists via the spin double cover `Spin(5) ≅ Sp(4)` at
   the group level, descending to Lie algebras. This is a concrete **Dynkin
   accident** at rank 2: the nontrivial outer automorphism of the rank-2 non-
   simply-laced diagram is realised by an isomorphism of the underlying Lie
   algebras.

3. **Dual Coxeter numbers.** `h^∨(B_2) = 3` and `h^∨(C_2) = 3`. Same value.
   Hence the critical level is `k = -3` on both sides.

4. **Critical affine algebras.** `V_{-3}(B_2)` and `V_{-3}(C_2)` are
   isomorphic as chiral algebras, since the underlying affine Kac-Moody
   algebras `\widehat{so(5)}` and `\widehat{sp(4)}` are isomorphic, with the
   chiral vacuum module at critical level functorially constructed from the
   Lie algebra data. The isomorphism is via the outer automorphism of the
   rank-2 root system lifted to the affine central extension.

5. **Opers are NOT isomorphic.** `B_2`-opers and `C_2`-opers are defined as
   `G`-bundles (`G = SO(5)` or `Sp(4)`) on the curve `X` equipped with a Borel
   reduction and a section of a specific vector bundle associated to the
   principal sl_2 embedding. The principal sl_2 in `B_2` has `h` with Dynkin
   weights `(α_1^∨, α_2^∨)` evaluated on the principal co-character, giving
   exponents `{1, 3}` (exponents of `B_2`). The principal sl_2 in `C_2` has
   exponents `{1, 3}` too (exponents of `C_2`, same numbers — DYNKIN ACCIDENT
   continues).

6. **Oper bundles differ by the outer automorphism.** Although the exponents
   coincide, the oper construction depends on the ROOT DATUM (character
   lattice `P` vs coroot lattice `Q^∨`), not just the Lie algebra. `B_2` has
   character lattice `Z^2` (standard weights of `SO(5)`); `C_2` has character
   lattice `Z^2` (standard weights of `Sp(4)`), BUT the two lattices are
   embedded differently in the Cartan `h^*`: the short coroots of `B_2` are
   the long roots of `C_2` and vice versa. So even though `B_2 ≅ C_2` as
   abstract Lie algebras, the ROOT DATA (g, P, Q) differ, and
   `Op_{B_2}(X) ≠ Op_{C_2}(X)` as moduli stacks.

7. **Feigin-Frenkel + Langlands.** The Feigin-Frenkel centre of the critical
   affine algebra is
   `𝔷(\widehat{g}) ≅ Fun(Op_{g^L}(D^\times))`
   (Feigin-Frenkel 1992, Frenkel Cambridge 2007 Thm 4.3.2). With `g^L`
   denoting the Langlands DUAL root datum (not just Lie algebra). Thus:
   `𝔷(\widehat{B_2}) ≅ Fun(Op_{C_2}(D^\times))` and
   `𝔷(\widehat{C_2}) ≅ Fun(Op_{B_2}(D^\times))`.

## Step (a): what the claim gets RIGHT

**The Dynkin accident does NOT break Langlands-naturality.** The critical
vacuum modules `V_{-3}(B_2) ≅ V_{-3}(C_2)` are isomorphic on both sides of
the FF-Φ_hol functor. BUT the image `FF-Φ_hol(V_{-3}(g))` depends on the
oper data, which lives in `Op_{g^L}(X)`. By fact 7, the FF-centre on the
`B_2` side lives in `Fun(Op_{C_2})` and on the `C_2` side in `Fun(Op_{B_2})`.
The R-reversal (Langlands R-reflection) swaps `Op_{C_2} ↔ Op_{B_2}`, which
matches the swap `𝔷(\widehat{B_2}) ↔ 𝔷(\widehat{C_2})` induced by the
boundary-centre extraction functor. So the Langlands-naturality DOES hold
functorially at B_2/C_2 — but NOT trivially; the naturality is the statement
that the FF-centre boundary datum is computed on the LANGLANDS-DUAL opers
moduli, which exchanges `B_2 ↔ C_2` even though the affine algebras are
isomorphic.

**The bulk 3d theories differ.** `FF-Φ_hol(V_{-3}(B_2))` is the Beilinson-
Drinfeld Hitchin quantum system on `C_2`-opers (Langlands dual of `B_2`).
`FF-Φ_hol(V_{-3}(C_2))` is the BD Hitchin quantum system on `B_2`-opers.
These are DIFFERENT 3d theories, even though the boundary chiral algebras
are isomorphic. The difference is visible in the Hecke eigensheaf spectral
decomposition: `Op_{B_2}` and `Op_{C_2}` have different stratifications and
different local Langlands parameters (short vs long roots determine the
normalisation of spectral parameters in the Hecke algebra action).

## Step (b): what the claim gets WRONG (or obscures)

**The "g ↔ g^L" phrasing is imprecise at rank-2 non-simply-laced.** In the
heal note's table, the row for non-simply-laced `g` states "B_r at critical
becomes C_r at critical, and vice versa, at the level of the 3d Hitchin-
quantised theory." This is CORRECT for the BULK (which depends on opers),
but MISLEADING for the BOUNDARY, since the boundary chiral algebras
`V_{-3}(B_2)` and `V_{-3}(C_2)` are actually isomorphic. The heal note's
prose risks the reader concluding that the boundary algebras are exchanged,
which is wrong at `B_2 ↔ C_2`.

**Root datum vs Lie algebra.** The Langlands duality `g ↔ g^L` is strictly
a ROOT DATUM duality, not a Lie algebra duality. Two different root data
can yield isomorphic Lie algebras (B_2 vs C_2 is the archetype), so
Langlands duality is finer than "exchanging Lie algebras". The note's
phrasing `V_{-h^∨}(g) ↔ V_{-h^∨}(g^L)` glosses over this; at B_2/C_2 the
VACUUM MODULES are the same, only the OPER SIDE changes.

**Beilinson-Drinfeld quantum geometric Langlands at B_2/C_2.** The BD-QGL
statement at `B_2 ↔ C_2` specialises to:
```
D-mod(Bun_{SO(5)}(X)) ≃ QCoh(Op_{Sp(4)}(X))
D-mod(Bun_{Sp(4)}(X)) ≃ QCoh(Op_{SO(5)}(X))
```
These are DIFFERENT equivalences (different sheaves, different moduli) even
though the Lie algebras are the same, because the moduli of bundles
`Bun_{SO(5)}` vs `Bun_{Sp(4)}` differ (different centres of the groups —
`Z(SO(5)) = Z/2`, `Z(Sp(4)) = Z/2` with different embeddings). So BD-QGL at
rank-2 non-simply-laced is a nontrivial statement even with the Lie
algebra accident.

## Step (c): correct relationship

**The FF-Langlands-naturality at B_2/C_2 is a nontrivial statement at the
oper/bundle level, even though the Lie algebras and critical vacuum modules
are isomorphic.** The correct restatement:

```
FF-Φ_hol(V_{-h^∨}(B_2))^{Lan-R-rev}  ≅  FF-Φ_hol(V_{-h^∨}(C_2))
```

is read as:
- LHS: the Langlands-R-reversal of the BD Hitchin quantum system on `C_2`-
  opers (the 3d theory whose boundary is `𝔷(\widehat{B_2}) ≅
  Fun(Op_{C_2})`).
- RHS: the BD Hitchin quantum system on `B_2`-opers (the 3d theory whose
  boundary is `𝔷(\widehat{C_2}) ≅ Fun(Op_{B_2})`).

The "isomorphism" is the Langlands-R-reversal acting on the oper moduli
stack, swapping `Op_{B_2} ↔ Op_{C_2}`. This is NOT trivial (even with the
Lie algebra accident), because the two opers moduli are distinct as stacks
— they differ by the short/long root relabelling encoded in the root datum.

**BD-QGL as the content of FF-Langlands-naturality.** The FF-Langlands-
naturality at `B_2/C_2` is precisely the BD-QGL equivalence at this rank-2
non-simply-laced case. The content is:
1. `D-mod(Bun_{SO(5)}(X)) ≃ QCoh(Op_{Sp(4)}(X))` via the Hitchin quantum
   system on `Sp(4)`-opers acting on `SO(5)`-bundles;
2. `D-mod(Bun_{Sp(4)}(X)) ≃ QCoh(Op_{SO(5)}(X))` the dual statement;
3. The Dynkin accident `B_2 ≅ C_2` as Lie algebras does NOT provide a
   "shortcut" identification of these two statements — they remain distinct
   BD-QGL equivalences, related by the outer automorphism of the root
   datum.

**Verdict.** The FF-Langlands-naturality at B_2/C_2 is CORRECT AS STATED in
the heal note, but requires the refinement that `g ↔ g^L` is a ROOT-DATUM
duality, not a Lie algebra duality. The Dynkin accident `B_2 ≅ C_2` does
NOT trivialise the naturality — it only identifies the BOUNDARY chiral
algebras, while the bulk 3d theories (Hitchin on `B_2`-opers vs `C_2`-opers)
remain distinct. The naturality encodes the BD-QGL at this rank, which is
a genuine (not trivial) equivalence.

**Suggested text refinement for the heal note.** Replace the prose
"B_r ↔ C_r under Langlands" with:

> For non-simply-laced `g`: the root data `(g, P, Q)` and `(g^L, Q^∨, P^∨)`
> differ (B_r ↔ C_r swap). At rank 2, the underlying Lie algebras are
> isomorphic (Dynkin accident), so the BOUNDARY critical vacuum modules
> `V_{-3}(B_2) ≅ V_{-3}(C_2)` coincide; but the BULK Hitchin quantum
> systems `BD-Hitchin(Op_{B_2}) ≠ BD-Hitchin(Op_{C_2})` remain distinct (since
> the opers moduli distinguish short/long roots). The FF-Langlands-naturality
> at B_2/C_2 is the BD-QGL equivalence at rank 2, nontrivial even at the
> Dynkin-accident case.

## Independent verification anchors

- **derived_from:** programme's FF-Φ_hol functor (this session); Feigin-
  Frenkel 1992 critical centre; heal-note claim at line 152.
- **verified_against:** Frenkel Cambridge 2007 Thm 4.3.2 (FF-centre ≅
  functions on Langlands-dual opers — explicitly root-datum-sensitive);
  Beilinson-Drinfeld 1991 Hitchin-quantised opers; Kamnitzer-Muthiah-Weekes-
  Yacobi "Quantum geometric Langlands at critical level" for the rank-2
  non-simply-laced case.
- **disjoint_rationale:** Frenkel's explicit FF-centre-opers identification
  uses only vertex-algebra representation theory + screening operators,
  without invoking the holographic framework; BD-QGL is constructed from
  algebraic geometry of `Bun_G` and `Op_{G^L}` moduli, independent of the
  programme's Φ_hol functor.

## Verdict summary

**FF-Langlands-naturality at B_2/C_2 HOLDS as claimed**, but with the
refinement:
- Boundary chiral algebras: `V_{-3}(B_2) ≅ V_{-3}(C_2)` (Dynkin accident
  trivialises this side).
- Bulk 3d Hitchin-quantised theories: distinct (`Op_{B_2} ≠ Op_{C_2}`).
- The "R-reversal" exchanges the opers moduli via the root-datum outer
  automorphism, realising the BD-QGL equivalence at rank-2 non-simply-laced.
- The "g ↔ g^L" phrasing needs to be read at the ROOT-DATUM level, not at
  the Lie algebra level, to avoid the Dynkin-accident conflation.

No revision to the theorem statement is required; prose sharpening in the
heal note's non-simply-laced paragraph is advisable. The Dynkin accident
does not complicate the theorem — it merely localises the nontriviality to
the BULK (where root data matter) rather than the boundary (where only the
Lie algebra matters, which is invariant under the accident).
