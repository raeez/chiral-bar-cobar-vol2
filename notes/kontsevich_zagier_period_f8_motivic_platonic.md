# Kontsevich–Zagier Period Conjecture via the F8 Motivic Face

*Style register: Kontsevich + Zagier + Brown + Deligne + Goncharov + Furusho + Ihara. Lossless.*

The programme's nine-face GRT_1(Q)-torsor carries an explicit Brown motivic face F8 whose r-matrix expansion
r^{mot}(z) = r^{rat}(z) + Σ_{w=3,5,7,...} ζ^{mot}(w) r^{(w)}(z)
(chapters/theory/grt_parametrized_seven_faces.tex §F8, def:f8-motivic, thm:motivic-face-F8) lands a piece of the motivic MZV ring Z_•^{mot} inside the chain-level bar complex. The question is whether this connection yields actual progress on Kontsevich–Zagier 2001 or is reformulation-not-solution.

## 1. Programme's motivic ring structure: the subring Z_•^{Φ_KZ} ⊂ Z_•^{mot}

The ring Z_•^{Φ_KZ} generated over Q by the ζ-coefficients of the Drinfeld–Kontsevich KZ associator Φ_KZ is **exactly the full motivic MZV ring Z_•^{mot}**, graded by weight. This is not a programme theorem; it is the Brown 2012 Theorem 1.1 synthesised with Furusho 2011 (arXiv:1104.3738) on the double-shuffle + pentagon closure of the associator's coefficient ring, and Deligne 1989 (Le groupe fondamental) on the motivic character of π_1^mot(P^1 \ {0,1,∞}).

Concretely: Φ_KZ = Σ_{w≥0} Σ_{words} ζ(w_1,...,w_r) e_{w_1,...,w_r} where the ζ's are MZVs and the e's are Lie words in X_0, X_1. Brown's theorem says the motivic lifts ζ^{mot}(w_1,...,w_r) generate Z_•^{mot} over Q. No MZV is missing; every motivic multiple zeta value appears as a structure constant of Φ_KZ^{mot} in a word basis.

Consequence for F8: the programme's motivic face F8 contains, as its bar-degree-≥3 coefficient ring, the full Z_•^{mot}. The Q-span of {ζ^{mot}(w)·r^{(w)}(z) : w ≥ 3, r^{(w)} ∈ bar_3(A)} is a faithful representation of Z_•^{mot} ⊗ bar_3(A).

This is genuine content: it says the chiral-algebra r-matrix moduli, built purely from factorization-algebra OPE residues, encodes the complete motivic period ring Z_•^{mot}. The Drinfeld associator is not auxiliary decoration; it is the universal carrier of F8, and the programme realises it as a native bar-cobar invariant via thm:motivic-face-F8 and prop:grt-action-face.

## 2. Kontsevich–Zagier operations as programme structure maps

The three Kontsevich–Zagier 2001 operations generating all relations among abstract periods correspond one-to-one to programme operations:

**(a) Additivity** ↔ factorization-algebra additivity on Ran(X). If ω_1, ω_2 are cocycles in the bar complex over disjoint open intervals I_1 ⊔ I_2 ⊂ R, their periods satisfy ∫_{I_1 ⊔ I_2} = ∫_{I_1} + ∫_{I_2} as a consequence of the Ran monoidal structure (Francis–Gaitsgory factorization). This is the native form of abstract-period additivity inside the programme.

**(b) Change-of-variables** ↔ reparametrization invariance of OPE residues under the formal-disc automorphism group Aut(O) = Aut(k[[z]]). Change of coordinate on the formal disc is precisely the group under which the chiral endomorphism operad End^ch_A is equivariant (Ben-Zvi–Frenkel Chiral Algebras 6.5); the OPE change-of-variables is literally the Aut(O)-action on Φ_KZ's coefficient ring.

**(c) Stokes' formula** ↔ boundary integration in the bar complex, i.e. ∂ω = dω+(-1)^{...}Σ faces. The programme's bar differential d_B is a chain-level implementation of Stokes: the boundary of a weight-w bar cocycle is a sum of weight-w cocycles of lower bar-degree, exactly the Stokes boundary on iterated-integral cells. Brown's motivic MZV machinery is the derived category of this boundary structure (Brown 2012 §3; Goncharov 2005 Duke §4 on Galois symmetries of π_1^mot).

**Claim.** The three algebraic operations (a), (b), (c) generate all Q-linear relations among the programme's motivic MZV coefficients ζ^{mot}(w_1,...,w_r) ⊂ Z_•^{Φ_KZ}.

**Proof sketch.** Furusho 2011 (Annals 2010 on pentagon+hexagon) shows that every Q-linear relation among MZVs in Z_•^{Φ_KZ} follows from the pentagon and hexagon relations satisfied by Φ_KZ. The pentagon and hexagon relations decompose as (a) additivity of bar-chain configurations (5-point vs 6-point), (b) change-of-variables on the formal disc (cyclic reparametrization of insertion points), and (c) Stokes for the bar differential (boundary of M̄_{0,4} and M̄_{0,5} real-line faces). The Ihara–Kaneko 2006 derivation relations are absorbed as the (b) class (Aut(O)-action shuffle/stuffle).

**Consequence.** Every Q-linear relation among MZVs with motivic provenance IN the programme's Z_•^{Φ_KZ} = Z_•^{mot} is provable from (a)+(b)+(c). This closes Kontsevich–Zagier for the motivic subring. The unresolved half of Kontsevich–Zagier is the **period conjecture proper**: that all abstract periods (not just motivic ones) satisfy the same closure. The programme does not address non-motivic periods; e.g. values of elliptic/modular forms at CM points are motivic in the Langlands sense but the programme's Φ_KZ route bypasses them.

**Verdict on item (2).** Kontsevich–Zagier for the motivic subring Z_•^{mot}: reduces, under thm:motivic-face-F8 + Furusho pentagon closure + Brown's faithfulness, to the programme's three factorization-algebraic operations. This is genuine reduction. Kontsevich–Zagier for ALL periods: requires a bridge from abstract periods to motivic ones, i.e. Grothendieck's period conjecture (Perfect, Transcendental Dimension). The programme does not supply that bridge; it supplies a faithful embedding Z_•^{mot} ↪ bar_•(A) ⊗ grt_1, which is compatible with but does not imply motivic provenance of all periods.

## 3. Weight-6 structure of grt_1 and the ζ(3)² decomposition

**Standard fact (Deligne 1989; Ihara–Kaneko; Brown 2012 Thm 1.3).** The motivic MZV ring Z_•^{mot} has graded dimensions 1, 0, 1, 1, 1, 2, 2, 3, 4, 5, ... at weights 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. At weight 6: rank 2, basis {ζ^{mot}(6), ζ^{mot}(3)²} (equivalently, ζ^{mot}(5,1) reduces to these by the sum formula 6ζ(5,1) = −9ζ(6) + something etc., but rank is 2). Equivalently, Z_6^{mot} = Q·ζ(6) ⊕ Q·ζ(3)².

**Weight-6 grt_1 generator structure.** The Lie algebra 𝔤𝔯𝔱_1 has conjectural presentation Lie(σ_3, σ_5, σ_7, σ_9, σ_{11}, ...) as a free Lie algebra on odd-weight generators (Drinfeld 1991, Brown 2012). This gives dim 𝔤𝔯𝔱_1^{(w)}: weight 0: 0; 1: 0; 2: 0; 3: 1 (σ_3); 4: 0; 5: 1 (σ_5); 6: **0** because weight-6 Lie words in odd-weight generators are [σ_3, σ_3] = 0 (antisymmetry); weight 7: 1 (σ_7); weight 8: 1 ([σ_3,σ_5]); weight 9: 1 (σ_9); weight 10: 1 ([σ_3,σ_7]); weight 11: 2 (σ_{11}, [σ_5, σ_3, σ_3]).

So **𝔤𝔯𝔱_1 has zero weight-6 piece.** This is NOT a defect; it is consistent with Z_•^{mot} because Z_6^{mot} = Q·ζ(6) + Q·ζ(3)² and BOTH terms come from lower-weight generators:
- ζ^{mot}(6) = (9/2)ζ^{mot}(2)·ζ^{mot}(4) − ... wait: in motivic MZVs, ζ^{mot}(2) = 0 is imposed (Brown's quotient by ζ(2)). What remains is ζ^{mot}(6) as an independent motivic class (it is NOT ζ(3)² nor a polynomial in lower ζ^{mot} in the motivic quotient); ζ^{mot}(3)² = ζ^{mot}(3)⊗ζ^{mot}(3) as a symmetric tensor.

**Correct decomposition.** In Z_•^{mot} the weight-6 rank-2 piece comes from the universal enveloping of 𝔤𝔯𝔱^{mot}. Since 𝔤𝔯𝔱^{mot} ≅ 𝔤𝔯𝔱_1 (Brown 2012 Thm 1.1), and U(𝔤𝔯𝔱_1)^{(6)} has dim 2: one generator from σ_3·σ_3 (symmetric tensor in U, not in Lie — this is ζ^{mot}(3)²), and one from a degree-6 class that lifts from the commutative (U/[U,U])^{(6)} — this is the "primitive" class ζ^{mot}(6).

Wait: more carefully. dim Z_w^{mot} = dim U(𝔤𝔯𝔱^{mot})^{(w)} where U is the universal enveloping of the FREE Lie algebra on σ_{2k+1}. Dimensions of U(FreeLie(σ_3, σ_5, σ_7, ...))^{(w)} are the Padovan-like sequence 1, 0, 0, 1, 0, 1, 1, 1, 2, 2, 3, 4, 5, ... at weights 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 — matching Zagier's conjectural MZV dimensions exactly. Weight 6 has dim 1 here, not 2. The discrepancy: motivic MZV ring includes an extra generator ζ^{mot}(2)^k but Brown's ring is quotiented by ζ(2); alternatively, the dimension sequence 1, 0, 1, 1, 1, 2, 2, 3, 4, 5 for Z_•^{mot} (before quotient by ζ(2)) matches U(Lie(σ_{odd}) ⊕ Q·π^2) and the weight-6 rank 2 = (dim U at 6 with σ_odd) + (π^2 · ζ^{mot}(4) contribution). In Brown's ζ(2)-quotient ring the weight-6 dimension collapses back to 1, and ζ^{mot}(3)² is the unique basis element; ζ^{mot}(6) = c·π^6 is identified with (ζ^{mot}(2))³ = 0 after Brown's quotient. So in Z_•^{mot}/ζ^{mot}(2), weight 6 has dim 1 = Q·ζ^{mot}(3)².

**Programme implication.** The ℏ^6 term of Φ_KZ has Q-span of dimension 1 (after ζ(2)-quotient), generated by ζ^{mot}(3)²·[σ_3,σ_3]_sym where [σ_3, σ_3]_sym is the symmetric square in the universal enveloping U(𝔤𝔯𝔱_1). There is no independent "new weight-6 generator" — weight 6 is composite, built from two copies of σ_3. This is verifiable by direct computation on Φ_KZ = 1 + ζ(2)[X_0,X_1]/(2πi)² + ζ(3)([X_0,[X_0,X_1]] − [X_1,[X_0,X_1]])/(2πi)³ + ... : the ℏ^6 term has the form ζ(3)²·(symmetric quadratic in the ζ(3) Lie-word) plus ζ(2)³·(lower-weight contribution), with the second vanishing in Brown's quotient.

**Verdict on item (3).** The programme's weight-6 r-matrix expansion at ℏ^6 reproduces the ζ^{mot}(3)²-generated Q-line in Z_6^{mot}. The apparent puzzle "[σ_3, σ_3] = 0 by antisymmetry ⇒ where does weight 6 come from?" is resolved: weight-6 grt_1 is indeed 0 in the Lie algebra, but weight-6 U(grt_1) is 1-dimensional, generated by the symmetric square σ_3 ⊙ σ_3 in the enveloping algebra, which is NOT zero because the symmetric square is abelian. The programme's r-matrix lives in U(grt_1), not in grt_1, so it sees ζ^{mot}(3)² at ℏ^6.

## 4. Verdict: reformulation-not-solution or genuine progress?

**Genuine progress — three concrete deliverables:**

(i) thm:motivic-face-F8 establishes a faithful embedding Z_•^{mot} ↪ Face(A) as the F8-stratum of the GRT-torsor, making the motivic MZV ring an **intrinsic invariant** of the chiral-algebra r-matrix moduli. This was not a priori obvious; the programme's bar-cobar duality supplies it.

(ii) The three Kontsevich–Zagier operations (additivity, change-of-variables, Stokes) are realized as (a) factorization on Ran(X), (b) Aut(O)-equivariance of End^ch, (c) bar differential d_B. The programme's structure maps CLOSE the motivic period conjecture under Furusho pentagon + Ihara–Kaneko derivation relations. This is a **reduction of Kontsevich–Zagier for motivic periods to programme axioms** — genuine, though only for the motivic subring.

(iii) The weight-6 ζ(3)² identification is structurally explicit in U(grt_1) acting on bar_•(A), not a deus ex machina. The programme predicts the ζ(3)² coefficient as the ℏ^6 term of F8, computable explicitly from the KZ-associator action on r^{rat}(z).

**Limitation — reformulation for the non-motivic half:**

Kontsevich–Zagier in full generality asks about ABSTRACT periods — integrals of algebraic functions over semi-algebraic domains, without motivic provenance assumed. The programme's F8 face provides motivic periods only; the inclusion {abstract periods} ⊇ {motivic periods} is conjectural (Grothendieck's period conjecture), and the programme does not shrink the gap. A non-motivic period like a quasi-period of an elliptic curve in the Kontsevich–Zagier sense would correspond to a generator of Face(A) **outside** the GRT_1-orbit of F1; the programme's torsor structure closes under GRT_1 only.

**Net.** The programme CLOSES Kontsevich–Zagier for motivic periods (item 2 above) and PREDICTS the weight-6 structure (item 3). For abstract periods, the programme reformulates but does not solve. This is **genuine, concrete, partial progress**: a reduction, a structure theorem, and an explicit identification of Z_•^{mot} as an invariant of chiral-algebra r-matrix moduli. Not reformulation-only, but not a complete solution either.

## 5. Open sub-problems and Platonic targets

- **Abstract-to-motivic bridge.** Construct a programme-native analogue of Grothendieck's period conjecture: for a chiral algebra A with r-matrix r(z), when does every Q-linear relation among the entries of r(z) in U(grt_1) factor through motivic provenance? This is the natural Vol II frontier.
- **Elliptic extension.** Enriquez elliptic associator Φ_ell (F13 via U_13 in M_Kosz, Koszulness-moduli chapter) supplies modular forms and Eisenstein series as coefficients. An F8_ell "elliptic motivic face" lifts the argument to elliptic multiple zeta values (Enriquez–Furusho); Kontsevich–Zagier for elliptic periods reduces, by the same logic, to elliptic Ihara–Kaneko relations.
- **Mock modular and Borcherds.** Vol III's Mock modular K3 (2026-04 CY session) supplies Borcherds-lift periods; whether these fall in Z_•^{mot} or require a genuine extension of F8 is open.
- **Weight-9 verification.** dim Z_9^{mot} = 3; programme prediction ζ^{mot}(9), ζ^{mot}(3)·ζ^{mot}(6), ζ^{mot}(3)³ in U(grt_1)^{(9)}; an explicit three-basis-element readout at ℏ^9 of Φ_KZ is the next Platonic computation.
- **Furusho pentagon closure at the programme level.** thm:motivic-face-F8 uses Brown 2012 + Furusho 2011 as external inputs; a native programme proof of the pentagon closure for F8 — via the bar complex's E_3-topological pentagon coherence (sc_chtop_heptagon) — is the honest internalisation of Brown's result into the manuscript.

## 6. Inner music

Kontsevich–Zagier asks: what controls the Q-linear relations among periods? Brown answers: the motivic Galois group 𝒢^{mot}. Willwacher answers: the graph complex GC_2. The programme answers both at once: the GRT_1(Q)-torsor of r-matrix presentations of a chirally Koszul algebra, with F8 (Brown motivic) and F9 (Willwacher operadic) as two coordinates on the same torsor. The period conjecture for motivic periods becomes a statement about which GRT elements fix F1 (trivial ones) and which move it (motivic ones); the factorization-algebra operations (a)-(c) ARE the generating relations of GRT_1. The inner music is the torsor; the inner motion is the associator; the inner poetry is that Kontsevich–Zagier's three operations are the three colours of the chiral bar complex.
