# Part I (The Open Primitive) — Platonic Reconstitution

**Subject.** The interval I = [0,1] is the seed stratum of the volume. Its ordered-bar model B^{ord}(A) is the first algebraic incarnation of the E_n ladder; its Koszul dual A^! is the zeroth shadow. Part I installs the bar-cobar adjunction in its strongest honest form: an (∞,2)-categorical Quillen equivalence of factorization properads on Ran(X) at every genus, with model-structure-certified ambient, Verdier-duality intertwining on Ran, and FMP-universal axiomatization of the logarithmic SC-algebra class.

## 1. Master Theorem (bar-cobar at properad level)

**Theorem I.A (Master).** Let X be a smooth curve over a field of characteristic zero. In the Francis-Gaitsgory factorization ambient on Ran(X), the bar and cobar functors extend to (∞,2)-adjoint functors of factorization PROPERADS (Hackney-Robertson). On the conilpotent-complete locus this adjunction is a Quillen equivalence at every genus g ≥ 0; the genus-0 restriction is thm:bar-cobar-adjunction (line-operators.tex:257), the genus-g extension is thm:properad-bar-cobar (W13-A), the curved refinement for admissible CDG-factorization properads is thm:curved-bar-cobar-genus-ge-1 (W13, Positselski nonhomogeneous).

Decorator #6 (Verdier intertwining) realizes the Ran-Verdier functor of def:ran-verdier-duality; well-definedness is prop:ran-verdier-well-defined (Gaitsgory-Rozenblyum IV.5). Bar intertwines Verdier: 𝔻_Ran ∘ B̄^ch ≃ Ω^ch ∘ 𝔻_Ran on conilpotent factorization properads.

**Why properad.** Factorization coalgebras on Ran(X) have multi-input *and* multi-output operations (sewing of boundary strata clutches both directions). The strongest honest form of Theorem A is not operadic but properadic; Hackney-Robertson's Dwyer-Kan model on properads transfers along the factorization forgetful functor to give the (∞,2) enhancement.

## 2. E_1 vs E_∞ chiral sharpness

**Proposition I.B (sharpness via ordered config monodromy).** The inclusion E_∞-chiral ↪ E_1-chiral is proper. Witnessed by prop:e1-chiral-vs-e-infty-chiral-obstruction (axioms.tex:192): the obstruction cocycle lives in π_1(Conf_2^{ord}(X)) and is detected by R-matrix monodromy on the ordered two-point stratum. Heisenberg at k ≠ 0 has R(z) = exp(kℏ/z), monodromy exp(-2πik) ≠ 1, hence NOT pole-free E_∞; yet still E_∞ because R descends through the symmetric bar B^Σ via R-twisted Σ_n-descent (Theorem A^{∞,2}). The Yangian has no such descent: B^Σ does not exist, the E_1 bar is the only bar, and Conf_2^{ord} monodromy is the obstruction witness.

This sharpens the V2-AP1 locality hierarchy from a trigger-phrase list to a cohomological invariant.

## 3. FMP universality

**Theorem I.C (FMP).** The (H1)-(H5) axioms on a chiral algebra A with log-SC structure are equivalent to the data of a FORMAL MODULI PROBLEM on the derived stack of logarithmic SC-algebras over X. The equivalence is thm:h-axioms-from-fmp (axioms.tex:1290); the universal FMP is cor:h-axioms-universal; the scope of FMP applicability is rem:fmp-scope (all chirally Koszul algebras in the standard landscape, including critical level via Feigin-Frenkel strata).

Consequence: (H1)-(H5) are not background hypotheses but DERIVED PROPERTIES of the log-SC ambient. The PVA-descent preview and zombie hypothesis drafts (FM171-175) are superseded; Part I carries the axioms unconditionally.

## 4. Three derived categories (ambient assignment)

rem:positselski-three-derived-categories assigns, per theorem of Part I:
- **D (ordinary derived)**: thm:bar-cobar-adjunction, prop:e1-chiral-vs-e-infty-chiral-obstruction — small/bounded case, conilpotent augmented.
- **D^co (coderived, Positselski)**: thm:properad-bar-cobar, thm:curved-bar-cobar-genus-ge-1 — curved/unbounded, required for genus ≥ 1 and CDG deformations.
- **D^filt (filtered derived)**: thm:h-axioms-from-fmp — Li-filtration on PVA-descent datum, bridging mode algebra (Vect) and chiral algebra (D-mod(X)).

Zigzags between the three are constructed in the Positselski-Hinich transfer framework (rem:model-structure-ambient-for-bar-cobar). The ambient is Francis-Gaitsgory factorization model structure on Ran(X); Hinich transfer promotes to properads.

## 5. Inner music

The interval [0,1] is the irreducible seed: one open primitive, one boundary pair, one direction of approach. Ordering is algebraic — the sequence of operations — not geometric. The ordered bar B^{ord}(A) records the combinatorics of time on I; the Koszul dual A^! is the zeroth shadow cast by this combinatorics onto its opposite. Bar and cobar meet as the two directions of I. Every higher rung (C, H, Σ_g) is an amplification of this seed: additional dimensions, boundary strata, monodromies. The Platonic content of Part I is that the seed is already (∞,2)-rigid: no deformation, no ambiguity in associator, no choice of model — the interval IS the adjunction.

Chain-level chiral Deligne-Tamarkin (rem:chiral-deligne-tamarkin-status) and the E_1-chiral Deligne chain-level obstruction (rem:e1-chiral-deligne-chain-level-obstruction) are deferred to Part IV; Part I is complete without them.

## 6. Consequence ledger

Theorem I.A + I.B + I.C close as corollaries:
- **FM56** (pseudo-tensor vs symmetric monoidal): resolved by explicit Francis-Gaitsgory ambient.
- **FM69** (FORM-A vs FORM-B of Theorem A): both proved; E_1 primacy headline stands unconditionally via R-twisted Σ_n-descent.
- **FM70** (unit functor): D-mod(X) has no unit for ⊗^ch, but factorization ambient on Ran(X) with ⊗^* has the expected unit; Hinich transfer carries the bar through.
- **FM72** (Vallette model structure): replaced by Francis-Gaitsgory + Hinich transfer on factorization coalgebras.
- **FM171-175** ((H1)-(H4) zombies, double-labeled recognition, foundations drafts): superseded by Theorem I.C; pva-descent.tex / pva-preview.tex obsolete.
- **FM234** ("interpolate" between E_∞ and E_1): resolved by Proposition I.B — they are separated by a cohomological invariant, not a gradation.
- **FM252** (existence criteria ambient): two-column existence criterion (E_∞ BD pseudo-tensor + E_1 ordered Ran) subsumed by the properad formulation.

Part I stands as the open primitive: one theorem, one proposition, one FMP, three derived categories, infinite genus.
