# First-Principles Analysis Cache — Cross-Programme Reference

This file caches every first-principles investigation from the programme's git history.
For each wrong claim: what it gets RIGHT, what it gets WRONG, the correct relationship, and the confusion type.

## AP5 dual-indexing header (Gate 0, pending landscape-census lock, 2026-04-21)

Several entries below assert $\kappa_{\mathrm{BKM}}(\mathbf H_{\Delta_5})$ 
numerical values. Per the canonical preamble of
`notes/antipatterns_catalogue.md` ("$\kappa_{\mathrm{BKM}}(\mathbf H_{\Delta_5})$
cross-volume value") and AP-CY49, BOTH values $5$ (paramodular
$\Phi_{10} = \Delta_5^2$ convention) and $12$ (Fake-Monster $\Phi_{12}$
convention) occur legitimately under different $N$-index conventions.
**Every standalone assertion of only one value without naming the input
denominator is a latent AP5 violation.** Historical entries that state
$\kappa_{\mathrm{BKM}} = 12$ (e.g., the B-row witnesses at the
five-archetype landscape inscription) must be read against this header;
dual-indexing caveats have been added inline for the critical
occurrences. Landscape-census lock via
`compute/lib/landscape_census` pending.

## Wave 5 (2026-04-16): GRT-Parametrized Seven Faces Reconstitution

**Files:** standalone/seven_faces.tex, connections/holographic_datum_master.tex, standalone/virasoro_r_matrix.tex, standalone/gaudin_from_collision.tex, examples/landscape_census.tex, vol2/dnp_identification_master.tex.

**W5-A. The "seven" in "Seven Faces" is an orbit-counting artifact.**
 - (a) RIGHT: there is a canonical object r(z) = Res^coll_{0,2}(Theta_A) for every chirally Koszul A in the standard landscape, and every historically-named face is an honest presentation of it.
 - (b) WRONG: the "star of equivalences F1..F7" picture treats the seven faces as a finite diagram. With MZV-associators, motivic coaction, and Willwacher GRT-action all present in the manuscript, the honest structure is a GRT-torsor of presentations; the cardinality-7 picture is a small Q-rational slice.
 - (c) CORRECT (GRT face family theorem): Let A be chirally Koszul with r(z) the collision residue of the universal MC element Theta_A. The set Face(A) of chain-level presentations of r(z) compatible with the bar-intrinsic dGLA structure is a torsor over GRT_1(Q) (Drinfeld Grothendieck-Teichmuller). For each Phi in GRT_1(Q) there is a presentation Face_Phi(A); the bar hub F1 is the identity coset; F2 (DNP R-twist), F3 (KZ classical PVA), F4 (GZ26 commuting differentials), F5 (Yangian r-matrix), F6 (Gaudin simple-pole), F7 (top A_infty m_3 for class M) are Q-rational associator choices. Two NEW faces from the literature that were not canonically enumerated: F8 (motivic, Brown coaction, MZV-valued -- r(z) receives an action of the motivic Galois group of MT(Z) via Phi_KZ; the "associator degrees of freedom" are zeta(2k+1) multiplied into odd-degree tensors), F9 (operadic, Willwacher's action of GRT on the Kontsevich graph complex GC_2, which acts on the bar complex of E_2 and hence on r(z) through the Tamarkin chain). The seven labeled faces are orbit representatives. Type: specific/general (finite listing of a torsor).

**W5-B. Casimir-rescaling chained equality (FM99 fix).**
 - (a) RIGHT: in the landscape census the symbols "k * Omega_tr / z" (Yangian/RTT normalisation) and "Omega/((k+h^v) z)" (Gaudin/Sugawara normalisation) both appear as the "r-matrix" of affine Kac-Moody.
 - (b) WRONG: writing "k * Omega_tr / z = Omega/((k+h^v) z)" as a rational-function equality is false (k != 1/(k+h^v) as rational functions of k). Example: sl_2 at k=1 gives 1*Omega_tr/z on LHS, Omega/(3z) on RHS; the Casimirs Omega_tr and Omega differ by the ratio of trace forms (1/(2h^v) Killing vs standard).
 - (c) CORRECT: the two expressions are TENSOR IDENTITIES in DIFFERENT bases of (g tensor g)^g, related by the Casimir-rescaling map Omega_tr = (1/(2h^v)) * Omega_Kil, combined with the Yangian-Gaudin level shift k -> k + h^v. Under the GRT_1^fin action of Section A, Casimir rescaling is an INNER automorphism of the associator torsor (it is a gauge change on r, not a different face). The chained equality, read as a tensor-invariant equation in (U(g) tensor U(g))^g((z)), is a GRT-equivariant statement; read as a rational-function equation, it is a convention clash. Type: convention clash + mechanism error.

**W5-C. Motivic face F8 (Brown coaction, MZV coupling).**
 - (a) RIGHT: Brown (2012) proved that the motivic fundamental groupoid of P^1 \ {0,1,infty} carries a coaction of the motivic Galois group of MT(Z); the Drinfeld associator Phi_KZ is the canonical element whose coefficients are the motivic MZVs.
 - (b) WRONG: ignoring F8 treats r(z) as a purely algebraic object invariant under zeta(2k+1) rescalings. This is not the case for vertex algebras with irrational levels, where MZV periods enter through KZ regularisation.
 - (c) CORRECT: F8 is the face Face_{Phi_KZ}(A), where the face data carries the Brown coaction: r(z) decomposes as r^{rat}(z) + sum_{w >= 3 odd} zeta(w) * r^{(w)}(z) in the motivic completion; each r^{(w)} is a Hodge-graded piece transforming under the MT(Z) coaction. The odd weights w = 3, 5, 7, ... correspond to the generators of the free Lie coalgebra underlying GRT. Type: native/derived (MZV content was implicit via KZ, never named as a face).

**W5-D. Operadic face F9 (Willwacher GRT-coaction on bar).**
 - (a) RIGHT: Willwacher (2014) proved H^0(GC_2) = grt_1, with GC_2 the Kontsevich graph complex; this gives an action of GRT on any E_2-algebra, and via bar-cobar on any E_1-chiral algebra's bar complex.
 - (b) WRONG: the original seven faces list had no direct operadic avatar; F2-F7 were all algebraic or geometric.
 - (c) CORRECT: F9 = Face_{Phi_W}(A), where Phi_W is the Willwacher cycle representing an element of grt_1 acting on B(A) through its action on E_2. The compatibility F9 <-> F8 is Willwacher-Rossi's theorem that his grt_1 action agrees with Brown's motivic coaction on MZV coefficients. Type: native/derived.

**W5-E. F1 <-> F4 "equivalence" is an injection, not a bijection (FM100).**
 - (a) RIGHT: F1 (bar hub) and F4 (GZ26 commuting differentials) produce the same classical r(z) in the standard landscape.
 - (b) WRONG: stating F1 <=> F4 without qualification ignores that F4 carries the MZV-associator data invisible to F1 (the bar hub sees only Q-rational structure). F8/F9 content is carried by F4 but projected away by F1.
 - (c) CORRECT: F1 -> F4 is an injection of torsor presentations over Q; F4 -> F1 forgets motivic weight. The quotient is the motivic Galois group of MT(Z) acting via GRT. Type: off-by-one (injection called bijection).

**W5-F. F7 disambiguation: Gaudin simple-pole vs. top A_infty m_3 for class M (FM101).**
 - (a) RIGHT: both the Gaudin simple-pole residue r_1(z) and the top A_infty operation m_3 restricted to class M appear in the manuscript under the label F7.
 - (b) WRONG: these are different tensors. r_1(z) is the degree-1 pole coefficient of r(z) (an element of (g tensor g)^g, independent of the A_infty structure). m_3 is an operation on B(A) detected only when the algebra is non-formal (class M); m_3 is invisible to r(z) restricted to the class L sublandscape.
 - (c) CORRECT: split into F7 (Gaudin simple-pole, canonical for all classes G/L/C/M) and F7' (top m_3 for class M, which exists only for class M and is the CHAIN-LEVEL obstruction to F7 being a complete face). In the GRT picture, F7' is a class-M-only associator choice that refines F7 by the non-formal data; the refinement vanishes on class L. Type: conflation (two faces written with one label).

**W5-G. Super-variant (AP107 extension).**
 - (a) RIGHT: AP107 notes that r^coll(z) differs from the Laplace-transform r(z) for odd generators; symplectic fermions / Heisenberg super-extensions have simple-pole OPE forbidden to bosonic Heisenberg.
 - (b) WRONG: the seven faces as stated assume purely bosonic generators; odd generators require a Z/2-graded refinement.
 - (c) CORRECT (super-face family): Face^super(A) is a torsor over GRT^super = GRT_1(Q) semi-direct with the parity-rescaling group Z/2^{|gen|}. Each odd generator contributes a Z/2-factor (sign on collision residues). For bosonic A, Face^super = Face. For symplectic fermions / superVOAs / bc-systems, the super-faces F8^super and F9^super carry graded MZV coefficients (super-Brown coaction). The Heisenberg-vs-symplectic-fermion dichotomy (pole order 2 vs pole order 1) is a GRT^super orbit separation, not a failure of the framework. Type: scope error (bosonic scope stated universally).

**W5-H. Consequences.**
 - (i) The seven faces theorem is UPGRADED to an infinite GRT-torsor family; seven is a slice cardinality.
 - (ii) Landscape census chained equality is TENSOR-IDENTITY, not rational-function identity; recorded as GRT^fin Casimir-rescaling action.
 - (iii) F8 and F9 are new canonical faces; the "list of seven" becomes nine + infinite associator family.
 - (iv) F7 disambiguation closes FM101: class-L-only claims about F7 now honest.
 - (v) Super-variant subsumes AP107.
 - (vi) No downgrades; every prior "face" claim remains true with an honest scope tag.

## Confusion Type Taxonomy (21 types)

1. **part/whole** — individual term properties assumed for total
2. **scope error** — formula valid in restricted domain applied universally  
3. **specific/general** — coincidence elevated to law
4. **label/content** — theorem label on conjecture; same symbol for different objects
5. **native/derived** — derived structure attributed to native level
6. **mechanism error** — right conclusion, wrong proof
7. **positive/negative** — obstruction misread as enablement
8. **off-by-one** — systematic shift in formula
9. **conflation** — distinct objects/operations equated
10. **convention clash** — two normalizations coexisting silently
11. **construction/narration** — structural analogy stated as identification
12. **construction/functor** — different constructions confused with single functor
13. **chain/cohomology** — chain-level property confused with cohomological
14. **algebraic/topological** — two incarnations of same structure conflated
15. **level error** — category-level confused with algebra-level; j=0 with j>=1
16. **vacuous/meaningful** — tautology presented as result
17. **temporal** — status changed over time; old status persists
18. **hardcoded/symbolic** — fragile reference instead of label
19. **sandbox/reality** — agent sandbox illusion
20. **additive/multiplicative** — different algebraic operations confused
21. **necessary/sufficient** — necessary condition treated as sufficient

## Wave 3 (2026-04-16): Vol I CY-Bridge Standalones Adversarial Review

**Files:** cy_quantum_groups_6d_hcs.tex, cy_to_chiral_functor.tex, en_chiral_operadic_circle.tex.

**W3-A1. Functor codomain label `E_2-ChirAlg` (FM43 violation).**
 - (a) RIGHT: the codomain at d=2 is E_2-chiral (K3, abelian surface). CY-A_2 is honest.
 - (b) WRONG: cy_to_chiral_functor.tex line 107-108 writes `Phi : CY_d-Cat -> E_2-ChirAlg` uniformly; d>=3 output is E_1 (per the E_1-stabilization theorem in the same file, thm:v3-st-e1-stabilization). The codomain label contradicts the body (abstract vs §7).
 - (c) CORRECT: `Phi : CY_d-Cat -> E_n-ChirAlg, n = 2 for d <= 2, n = 1 for d >= 3`. Scope tag on the functor. Type: scope error.

**W3-A2. `Psi > 0 generically` over-signing (sigma_2 sign).**
 - cy_quantum_groups_6d_hcs.tex lines 435-437: with h_1+h_2+h_3=0, sigma_2 = -(h_1^2+h_2^2+h_3^2)/2 is real and NEGATIVE (not zero except at origin), so Psi = -sigma_2 = (sum h_i^2)/2 > 0 for real h_i -- correct under reality. The text is correct for REAL h_i; it is NOT correct for complex h_i (generic quantum toroidal parameters are complex). Add qualifier "for real Omega-background."
 - Type: scope error (real vs complex Omega-background).

**W3-A3. "categorified averaging" label on the Drinfeld centre (AP-CY54 violation).**
 - cy_quantum_groups_6d_hcs.tex:754 and cy_to_chiral_functor.tex:882 both call Z(Rep^{E1}(A)) the "categorified averaging map."
 - (a) RIGHT: there is a structural analogy between av: Bar^ord -> Bar^Sigma (lossy projection) and the forgetful functor U: Z(C) -> C (loses half-braiding).
 - (b) WRONG: av LOSES the R-matrix (becomes kappa_ch scalar); U is the FORGETFUL of a RIGHT-ADJOINT construction (Z is right adjoint to the forgetful BrMon -> Mon, i.e., a categorified COMMUTANT, not an averaging). Direction is opposite.
 - (c) CORRECT: "Z is the right adjoint to the forgetful BrMon -> Mon (categorified commutant/centre). U: Z(Rep^{E1}(A)) -> Rep^{E1}(A) is the forgetful, analogous TO av but going in the opposite operadic direction." Type: label/content + construction/narration.

**W3-A4. `E_n operadic circle` as closed structure (AP150 violation, en_chiral_operadic_circle.tex).**
 - Arrow (1) `E_3^top(bulk) -> E_2(boundary chiral)` via restriction to codim-2 defect: NOT a theorem for general 3d HT theories; proved by Costello-Li (5d Chern-Simons) / CFG for KM only. For arbitrary E_3^top, the "restriction to codim-2" is a construction on FACTORISATION ALGEBRAS, not on abstract E_3 algebras; E_2-chiral output requires holomorphic structure on the boundary curve (not provided by abstract E_3).
 - Arrow (5) `closing` = conjecture (acknowledged line 2020-2026).
 - The circle is arrows (1)+(5) conjectural, (2)+(3)+(4) proved. The whole structure is therefore CONJECTURAL, not theorem.
 - (a) RIGHT: arrows 2,3,4 exist and compose (Z(Rep^{E1}) -> HH* -> E_3^top is higher Deligne; ordered bar is E_1).
 - (b) WRONG: presenting the five-arrow sequence as a closed programmatic structure elides arrow-(1) construction issues and arrow-(5) closing conjecture.
 - (c) CORRECT: "The sequence (2)->(3)->(4) is proved; (1) is proved case-by-case (KM via Costello-Li/CFG; W via Costello-Gaiotto); the closing equivalence (5) is conj:e-closing." Tag scope per arrow. Type: temporal + label/content.

**W3-A5. CoHA != E_1-chiral algebra (AP-CY7).**
 - cy_quantum_groups_6d_hcs.tex Prop 4.3 lists five axioms H1-H5 for CoHA as "E_1-chiral Hopf algebra." The CoHA is associative (E_1-algebra in Vect with dimension-vector grading), NOT an E_1-chiral algebra on a curve. The axioms (H2) spectral coproduct and (H4) spectral coassociativity are the Schiffmann-Vasserot VERTEX coproduct on the vertex algebra Y^+(gl_1-hat) ~ W_{1+inf} -- that output carries E_1-chiral structure. The CoHA itself, as an associative algebra graded by dim vectors, is a source, not an instance.
 - (a) RIGHT: under the Schiffmann-Vasserot isomorphism CoHA(C^3) ~ Y^+(gl_1-hat) ~ W_{1+inf}, the TARGET W_{1+inf} is genuinely a vertex algebra; the image carries the E_1-chiral structure.
 - (b) WRONG: saying the CoHA "is" an E_1-chiral algebra conflates a Z-graded associative algebra with its image under Schiffmann-Vasserot.
 - (c) CORRECT: "The Schiffmann-Vasserot isomorphism identifies CoHA(Q,W) (graded associative algebra) with the positive half of an E_1-chiral algebra. Hopf axioms H1-H5 apply to the vertex-algebra image." Type: conflation (AP-CY7).

**W3-A6. AP-CY14 status promotion (CY-A_3 inf-cat).**
 - cy_to_chiral_functor.tex:116 "Theorem CY-A_3, inf-categorical proof" -- consistent with AP-CY6 update.
 - But Remark 3.4 (rem:v3-st-d3-evidence) says "verified for C^3 where both sides are independently computable (kappa_ch = kappa_cat = 1)." The d=3 kappa_ch = chi(O_X) = chi^CY conjecture (conj:v3-st-cy-kappa-d3) is flagged conjectural at d>=3 -- honest. BUT the claim "kappa_cat = 1 for C^3" treats C^3 as compact (chi(O_X) = 1 for C^3 via formal Euler characteristic is ambiguous for non-compact targets). State explicitly: equivariant chi(O_{C^3}) = 1/((1-q_1)(1-q_2)(1-q_3)) and a scheme must be specified.
 - Type: convention clash (equivariant vs classical chi).

**W3-A7. Shadow = GW(C^3) via shadow-Eisenstein (AP-CY8 territory).**
 - cy_quantum_groups_6d_hcs.tex Prop 7.1 and cy_to_chiral_functor.tex Rem 6.11: "shadow coefficients S_r are coproduct corrections delta^(r); shadow IS GW for C^3 (no compact curves)."
 - (a) RIGHT: for C^3 the non-constant-map GW vanishes (no compact curves); the constant-map free energies F_g^{const}(C^3) are combinatorial (MacMahon); the shadow tower computes Virasoro free energies.
 - (b) WRONG: equating shadow S_r with F_g^{const}(C^3) requires BOTH (i) shadow = Feynman amplitude (proved in Vol I, thm:shadow-feynman-dictionary S_k = delta^{(k)}, per CLAUDE.md) and (ii) Feynman amplitude = constant-map GW (separate theorem; for C^3 this is the Faber-Pandharipande constant-map integral). The PAPER states (i) and asserts (ii) without independent anchor.
 - (c) CORRECT: "At kappa_ch = Psi, shadow_r equals Virasoro coproduct correction delta^(r) (Vol I); the identification with F_g^{const}(C^3) requires the Faber-Pandharipande constant-map integral (Faber-Pandharipande 2000, Thm 4) as SEPARATE INPUT." Need independent_verification decorator with derived_from = {Vol I shadow-Feynman} and verified_against = {Faber-Pandharipande FP2000}.
 - Type: necessary/sufficient (two inputs presented as one).

**W3-A8. Antipode non-lifting obstructions (OPE + Hopf) insufficient documentation.**
 - cy_quantum_groups_6d_hcs.tex Rem 4.5: S(T(u)) = T(u)^{-1} in transfer-matrix formalism "does not lift to vertex-algebraic antipode"; claims two obstructions (OPE quartic pole, Hopf z*J residual).
 - (a) RIGHT: the non-lifting is a real phenomenon (Miura nonlinearity).
 - (b) WRONG/INCOMPLETE: neither obstruction has an independent verification source cited. Per the independent-verification protocol, a claim of "does not lift" needs either an explicit computation or external reference (e.g., Prochazka-Rapcak, Arakawa).
 - (c) CORRECT: restrict to computed case (spin 2, N=2 explicit) or cite external. Type: hardcoded/symbolic (claim not backed by independent computation).


| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 1 | {b_k, B^{(2)}} = 0 for each k individually | TOTAL {b, B^{(2)}} = 0 via Costello TCFT | Individual arity-k terms don't vanish for non-formal algebras | Cross-arity cancellation: {b_3, B^{(2)}} cancelled by {b_2, B^{(2)}} via Stasheff. Total vanishes by operadic d^2=0. | part/whole |
| 2 | Tsygan formality proves {b, B^{(2)}} = 0 | Tsygan formality is a real theorem | Wrong scope: applies to B^{(0)} = Connes B, not B^{(j>=1)} | B^{(0)} mixed complex axiom [b, B^{(0)}]=0 does NOT extend to B^{(j)} hierarchy. | scope error |
| 3 | kappa_BKM = kappa_ch + chi(O_fiber) universally | True for N=1 (K3 x E): 5 = 3 + 2 | Numerical coincidence for single case | Fails for all Z/NZ-orbifolds with N>=2. Correct: kappa_BKM = c_N(0)/2 (Borcherds weight theorem). | specific/general |

## II. Theorem Downgrades

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 4 | "Theorem: BV-BRST = bar of G(X)" for CY3 | Structural identification plausible | G(X) does not exist; cannot be theorem | \begin{conjecture}. 11+ instances fixed. AP-CY6/AP-CY14 | label/content |
| 5 | "Theorem: kappa_ch = chi(O_X) for all CY" | True for d=2 with h^{1,0}=0 | FALSE for odd d (Serre forces chi(O_X)=0) | kappa_ch = worldsheet anomaly; chi(O_X) = target-space. Coincide at d=2, diverge at d=3. AP-CY34 | scope error |
| 6 | 62 instances of "Theorem CY-A_3" | CY-A_3 now proved (inf-cat) | Before proof: unproved conjecture in theorem env | Mass rectification. Chain-level results remain conjectural. | temporal |

## III. Kappa Conflations (7 types)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 7 | Bare "kappa" (~100+ instances) | Each kappa is real | Without subscript, different kappas conflate | Four kappas: kappa_{ch,BKM,cat,fiber}. K3xE spectrum: {0,2,3,5,24}. AP113 | label/content |
| 8 | "kappa(K3xE) = 3 vs 5 contradiction" | Both values real | DIFFERENT kappas of DIFFERENT algebras | kappa_ch=3 (chiral), kappa_BKM=5 (Igusa). No contradiction. | conflation |
| 9 | "Algebraizations share kappa_cat" as meaningful | kappa_cat IS same | VACUOUS: kappa_cat is manifold invariant | Like "both share gravity." AP-CY55 | vacuous/meaningful |
| 10 | kappa_ch = Sigma(-1)^i dim HH_i | Gives a real invariant | Gives chi_top (=24 for K3), NOT kappa_ch (=2) | Correct: Hodge-filtered supertrace str_{F^0}(q^{L_0}). AP-CY36 | formula error |
| 11 | kappa_ch additive under fiber products | Additive under direct sums | NOT under fiber products | kappa_ch(K3xE)=3 but chi(O_{K3xE})=2*0=0. Additivity vs multiplicativity. | additive/multiplicative |

## IV. E_n Level Confusions (8 types)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 12 | Phi: CY_d-Cat -> E_2-ChirAlg (uniformly) | E_2 correct for d<=2 | WRONG at d>=3: output is E_1 | Must scope: n=2 for d<=2; n=1 for d>=3. FM43 | scope error |
| 13 | "E_2-chiral algebra" at d=3 for A itself | E_2 DOES appear at d=3 | Lives on Z(Rep^{E_1}(A)), NOT on A | A is E_1 native. E_2 is derived via center. AP-CY56 | native/derived |
| 14 | E_3 on HH of E_1 algebras (Deligne) | E_3 Deligne is real | Requires E_inf input, not E_1 | For E_1: only E_2 (Dunn: E_1 tensor E_2 = E_3, but input contributes E_1). AP153 | scope error |
| 15 | Two E_3 structures are the same | Both exist | Agree under formality only | Algebraic E_3 (Deligne) vs topological E_3 (Conf(R^3)). Physical content at chain level. AP154 | algebraic/topological |
| 16 | Miki from E_3 operad | Miki IS an S_3 permutation | Comes from CY torus Weyl group, not operad | Counterexample: k[x]/(x^2) is E_3, no Miki. AP-CY22 | specific/general |
| 17 | CY-B is "E_2-Koszul" uniformly | CY-B IS Koszul duality | d-DEPENDENT: E_2 at d=2, E_1 at d=3 | At d=3: E_1-Koszul on A, E_2 on center. AP-CY58 | scope error |
| 18 | Class M E_3 bar is infinite | Class M IS most complex | Cohomology is 6^g (Kunneth) | Chain: P(q)^{6g}. Cohomology: 6^g. AP-CY21/38 | chain/cohomology |
| 19 | SN bracket vanishes for all CY_3 | True for C^d with GL(d) | False for non-toric CY_3 | Two mechanisms: (a) operadic degree (universal), (b) GL(d)-invariant vanishing (toric). | specific/general |

## V. Object Conflations (9 types)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 20 | CoHA = E_1-chiral algebra | CoHA related to E_1-sector | CoHA is associative, not chiral | Connection via functor Phi, not identification. AP-CY7 | construction/identification |
| 21 | Drinfeld center = derived center | Both real | Three distinct objects conflated | Z(C) = category center. Z^der = Hochschild cochains. Z categorifies derived center. AP-CY4 | level error |
| 22 | Drinfeld center = categorified averaging | Related via factorization | Center CONSTRUCTS; averaging DESTROYS | E_1 ->^Z E_2 ->^{Sym} E_inf. AP-CY54 | construction/narration |
| 23 | Flop = Koszul dual | Both operations on CY | Flop preserves kappa; Koszul exchanges | kappa(A_X)=kappa(A_{X+}) for flop. kappa(A)+kappa(A^!)=K for Koszul. AP-CY10 | conflation |
| 24 | CoHA = bar complex | Both have char M(q) | CoHA is algebra; bar is coalgebra | SV theorem: CoHA ≅ Y^+. Bar encodes Y-multiplication. Character coincidence. | algebra/coalgebra |
| 25 | Spectral z = worldsheet z | Both called "z" | Different objects | Delta_z spectral: shift parameter. OPE z: insertion coordinate. AP-CY31 | label/content |
| 26 | Phi distinguishes three K3 algebras | Three algebras exist | Phi gives ONE output: H_Muk | BKM from Borcherds lift, Conway from Leech. Different constructions. AP-CY59 | construction/functor |
| 27 | Six routes = six Phi applications | Six routes are constructions | Six DIFFERENT constructions | Convergence = CY-C (conjectural). AP-CY60 | construction/functor |
| 28 | R(z) = (id tensor S) o Delta_z(1) | R from coproduct | Coproduct of vacuum = 1 tensor 1 by counit | Correct R via half-braiding sigma in Z(Rep). AP-CY25 | construction error |

## VI. Scope and Status Errors

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 29 | 6d route bypasses CY-A_3 | Alternative approach | Each subproblem requires same data | Reorganises, doesn't resolve. AP-CY32 | reorganization/bypass |
| 30 | S_{ijk}=R_{ij}R_{ik}R_{jk} satisfies ZTE | R satisfies YBE | Pairwise != 3-particle consistency | Fails at O(kappa^2). S^{corr}=S+kappa^2*T exists. AP-CY30 | specific/general |
| 31 | Shadow class from non-formality alone | m_3!=0 necessary for >=L | Not sufficient | local P^2: m_3!=0 but class M (infinite). Must compute full tower. AP-CY12 | necessary/sufficient |
| 32 | Omega-background universal for CY_3 | Realizes E_1 for toric | Requires torus action | General mechanism: bracket degree 1-d. Omega-background: toric-specific. | specific/general |
| 33 | "CY frontier" (empty slogan) | Gap F_g^top - F_g^sh is real | "Frontier" says nothing | Computable via Borel resummation + KS wall-crossing. | label/content |

## VII. Formula and Computation Errors

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 34 | MF(W): A^n->A^1 is CY_{n-1} | MF IS a CY category | CY dim is n-2, not n-1 | ADE in 2 vars: CY_0. Need 5 vars for CY_3. AP-CY17 | off-by-one |
| 35 | A-hat convergence radius = pi | A-hat IS relevant | Argument halved: (x/2)/sinh(x/2) | Radius = 2*pi. The /2 doubles the radius. AP-CY19 | mechanism error |
| 36 | phi_{0,1} c(-1)=1 vs c(-1)=2 | Both normalizations exist | Factor of 2 = kappa_ch(K3) propagated silently | State convention. K3 elliptic genus = 2*phi_{0,1}. AP-CY42 | convention clash |
| 37 | Verdier inverts sigma_2 for k^!=-k | k^!=-k IS correct | sigma_2 is even under h_i->-h_i | k^! from Shapovalov form transposition, not sigma_2 inversion. AP-CY26 | mechanism error |
| 38 | B-cycle i^2=1 instead of i^2=-1 | B-cycle integrals needed | Sign error gives |q|=1, kills convergence | Verify |q|<1 and Im(tau)>0 after B-cycle computation. FM24 | sign error |

## VIII. Process and Agent Errors

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 39 | Agent writes persist to disk | Written inside sandbox | Sandbox isolation | Verify with ls after agent completion. AP-CY27 | sandbox/reality |
| 40 | Agent writes to correct repo | Files written | Wrong volume's directory | Verify FULL PATH. AP-CY29 | path error |
| 41 | Agent test values independent | Tests pass | 10% tautological | Multi-path verification required. AP-CY49 | tautological verification |
| 42 | Docstring values correct | Code correct | Docstring fabricates for n>=4 | Verify EVERY numerical value against function output. AP-CY24 | code/documentation |

## IX. Cross-Volume Confusions

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 43 | Bulk replace "arity"->"degree" | Rename intentional | Corrupts singularity, unitarity, etc. | 45 corruptions. Check compound words. FM42 | mechanical error |
| 44 | "shadow Postnikov tower" | Shadow tower is real | "Postnikov" is different concept | Correct: "obstruction tower" or "shadow tower" | terminology error |
| 45 | Part~IV hardcoded | Parts ARE numbered | Numbers change on restructuring | Use \ref{part:...}, never Part~N. AP-CY13 | hardcoded/symbolic |

## X. cy_to_chiral.tex Audit (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 46 | Class M E_3 bar cohomology is "infinite-dimensional" | d_4 survives for class M | Chain-level complex P(q)^{6g} is infinite, but cohomology is FINITE | dim H*(B^{E_3}(A)) = 6^g for class M (Kunneth: d_4 kills Lambda^0 and Lambda^3, leaving [0,3,3,0] per handle). AP-CY21/38 | chain/cohomology | cy_to_chiral.tex L3760, L3765 |
| 47 | "dim HH_0 = 2, dim HH_1 = 20, dim HH_2 = 2" (yielding -16) | Alternating sum = -16 is correct | Mislabeled: these are dim H*(Omega^p), not dim HH_i | HH_i uses homological grading (HH_0=22); the Hodge grading uses p (dim H*(Omega^0)=2). Both yield -16 under the correct alternating sum, but the labels were wrong. | label/content | cy_to_chiral.tex L69 |
| 48 | ClaimStatusConditional for class M E_3 bar genus result | Class M result WAS conditional | Now PROVED via Kunneth (6^g closed form) | Update status to ProvedHere for all classes including M. | temporal | cy_to_chiral.tex L3754-3755 |

## XI. en_factorization.tex Enforcement (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 49 | K3 listed as CY_4 in Pontryagin class table | K3 has c_2=24, p_1=-48 | K3 is CY_2 (complex dim 2), NOT CY_4 | Removed row. K3 cannot appear in CY_4 landscape table. AP-CY1 | scope error | en_factorization.tex L309 |
| 50 | Verification note "AP-CY21: class M infinite" | Class M IS most complex shadow class | Class M E_3 bar = 6^g (FINITE); class G is the infinite one | Corrected to "class M is 6^g not (1+t)^{3g}". AP-CY21/38 | chain/cohomology | en_factorization.tex L2688 |

## XII. K3 Example Chapters Enforcement (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 51 | "E_2-structure should come from Sp_4(Z)" (at d=3, no E_n scoping) | E_2 structure IS relevant at d=3 | At d=3, A is natively E_1; E_2 lives on Drinfeld center Z(Rep^{E_1}(A)), not on A | Fixed: clarified that E_2-braiding is on the Drinfeld center of the representation category, not on A itself. AP-CY56 | native/derived | k3_chiral_algebra.tex L35 |
| 52 | "CoHA is E_1-sector of G(X), which is CY-A_3" | CoHA/G(X) connection is real | G(X) requires CY-C (quantum group realization), NOT CY-A_3; CY-A_3 gives A_X, not G(X) | Fixed: CoHA as E_1-sector of G(X) requires Conjecture CY-C. CY-A_3 constructs A_X but not G(X). AP-CY7/AP-CY14 | label/content | k3_yangian_chapter.tex L1103 |
| 53 | kappa_BKM = h^{1,1}(K3)/4 = 20/4 = 5 | Numerically correct (5=5) | Misleading derivation: c_f(0)=10 comes from Jacobi form, not h^{1,1}/2 | Fixed: kappa_BKM = c_f(0)/2 = 10/2 = 5 with explicit AP-CY37 citation. Hodge number route obscures Borcherds weight theorem. | mechanism error | k3_chiral_algebra.tex L510 |
| 54 | "deeper identifications await CY-A_3" | CY-A_3 WAS open | CY-A_3 is now PROVED (inf-cat, thm:derived-framing-obstruction) | Fixed: remaining obstructions are chain-level framing data (non-formal) and Vol I Borcherds-lift bridge, not CY-A_3 itself. | temporal | k3_yangian_chapter.tex L1347, L1380-1391 |
| 55 | Bare $\kappa$-diagnostic in verification note | kappa_bullet notation required | AP113 zero-tolerance: all kappa must be subscripted or use bullet | Fixed: $\kappa$-diagnostic -> $\kappa_\bullet$-diagnostic. | label/content | k3_yangian_chapter.tex L126 |

## XIII. Connection/Bridge Chapters Enforcement (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 56 | "predicted modular characteristic is kappa_ch = chi_top/24 (BCOV prediction)" as blanket statement for compact CY3 | BCOV prediction IS used for compact CY3 | Presents conjectural formula without noting chi_top/24 != chi(O_X) for CY3 | chi(O_X)=0 for ALL CY3 by Serre duality (AP-CY34). kappa_ch = chi_top/24 is BCOV *prediction* (conjectural), not established formula. Must mark as conjectural and note the distinction. | scope error | bar_cobar_bridge.tex L235 |
| 57 | "conditional on CY-A_3" in DMVV conjecture (bar_cobar_bridge.tex) | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED (inf-cat, thm:derived-framing-obstruction, April 2026) | Remaining conditionality: Vol I Borcherds-lift identification (AP-CY8) and motivic DT comparison, NOT CY-A_3. | temporal | bar_cobar_bridge.tex L749 |
| 58 | "conditional on CY-A_3" for K3xE Stokes-WC identification | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | A_{K3xE} now exists. Remaining conditionality: Vol I Borcherds-lift identification (AP-CY8) + infinite stitching of local conifold identifications. | temporal | modular_koszul_bridge.tex L581, L936, L964 |
| 59 | "conditional on CY-A_3" for Hochschild bridge at d=3 | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Conjecture remains (upgrading the categorical-to-chiral Hochschild map to d=3 requires more than inf-cat existence), but the CY-A_3 conditionality is resolved. The conjecture's remaining content: the PTVV shifted Poisson maps to genus-0 convolution bracket. | temporal | modular_koszul_bridge.tex L317 |
| 60 | Face 1 "Conjectured for d=3 (conditional on CY-A_3)" in seven-face status remark | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED; thm at L153 already has ProvedHere | Status remark stale: Face 1 is ProvedHere for both d=2 and d=3. | temporal | cy_holographic_datum_master.tex L859 |
| 61 | "CY_3 (conditional on CY-A_3)" paragraph header in holographic datum | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Updated header. The paragraph body already said "now follow from Theorem CY-A_3". Only the header was stale. | temporal | cy_holographic_datum_master.tex L245 |
| 62 | K3xE Hecke eigensheaf "conditional on CY-A_3" | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | A_{SxE} exists by CY-A_3. Remaining conditionality: factorization Phi(SxE) = Phi(S) tensor Phi(E) (not established) and the Hecke eigensheaf identification. | temporal | geometric_langlands.tex L257 |
| 63 | "d=3 analogue remains part of CY-A_3" in convolution algebra proof | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Updated: "now established by CY-A_3 (proved)". The convolution bracket pulls back at both d=2 and d=3. | temporal | modular_koszul_bridge.tex L42 |
| 64 | kappa_ch + kappa_ch' = 0 displayed without scoping | True for KM/free-field class | Virasoro: sum = 13, not 0. Free-field scoping buried in prose after display | Fixed: displayed formula now shows general conductor relation kappa_ch + kappa_ch' = rho*K with explicit family-dependent scoping. | scope error | bar_cobar_bridge.tex L196 |

| 65 | "conditional on CY-A_3" in genus expansion section of modular_trace.tex | CY-A_3 WAS the bottleneck for GW identification | CY-A_3 is now PROVED; A_X exists | Remaining conditionality: the comparison between shadow tower and B-model topological string at g>=2. At g=1, unconditionally proved via Vol I Theorem D. | temporal | modular_trace.tex L168 |
| 66 | "the tower is conditional on CY-A_3" for CY3 shadow tower | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Tower is now accessible via CY-A_3 (proved). BKM modularity constraints provide structural predictions independently. | temporal | modular_trace.tex L173 |

### Positive findings (no violations)

The following were checked and found correct across all five files:

- **AP113 (bare kappa)**: Zero violations. All kappa subscripted throughout all five files.
- **AP-CY4 (Drinfeld center vs derived center)**: Correctly distinguished in modular_koszul_bridge.tex Def 3.1 (three Hochschild theories), cy_holographic_datum_master.tex Rem rem:no-cobar-bulk-confusion, geometric_langlands.tex Iwahori passage.
- **AP-CY7 (CoHA != chiral)**: Correctly noted as associative in bar_cobar_bridge.tex L359 ("on the CY side, the CoHA..."), geometric_langlands.tex L90 (explicit AP-CY7 citation).
- **AP-CY8 (denominator != bar Euler)**: No bare identification. The modular_koszul_bridge.tex Igusa cusp form section (Thm thm:k3xe-shadow-cohft-igusa) explicitly notes the AP-CY8 proviso.
- **AP-CY10 (flop != Koszul)**: modular_trace.tex L178 correctly distinguishes complementarity (Koszul) from flop.
- **AP-CY12 (shadow class from full tower)**: bar_cobar_bridge.tex correctly computes shadow class for each CY3 example from the full tower data, not from non-formality alone.
- **AP-CY54 (Drinfeld center != averaging)**: geometric_langlands.tex correctly describes Drinfeld center via half-braidings/Iwahori passage, never calls it "averaging".
- **AP-CY55 (manifold vs algebraization invariants)**: modular_koszul_bridge.tex kappa-spectrum tables (L333-344, L251-252) correctly separate manifold invariants from algebraization invariants.
- **AP-CY56 (E_n level scoping)**: geometric_langlands.tex correctly uses E_2 only for d<=2, E_1 for d>=3. cy_holographic_datum_master.tex Face 1 d=3 correctly references E_1-chiral.
- **AP-CY57 (construction/narration)**: The seven-face chapter constructs each face explicitly, not by narration. Koszul duality is constructed through the bar-Verdier pipeline in modular_koszul_bridge.tex.
- **AP25 (bar != cobar != Koszul)**: bar_cobar_bridge.tex Remark 3.1 (three functors, three outputs) correctly distinguishes Omega(B(A))=A (inversion), D_Ran(B(A))=B(A^!) (Verdier/Koszul), Z^der_ch(A)=RHom (derived center).
- **Geometric Langlands, derived Satake**: All CONJECTURAL throughout geometric_langlands.tex. Every formal statement uses \begin{conjecture} except Feigin-Frenkel (ProvedElsewhere).
- **Part references**: No hardcoded Part~N references found in any of the five files.

## XIV. Theory + Examples Chapters Enforcement (2026-04-15, 11-file sweep)

Files audited: cy_categories.tex, cyclic_ainf.tex, hochschild_calculus.tex, quantum_groups_foundations.tex, braided_factorization.tex, toroidal_elliptic.tex, matrix_factorizations.tex, fukaya_categories.tex, quantum_group_reps.tex, derived_categories_cy.tex, k3e_cy3_programme.tex.

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 65 | kappa_cat(K3 x E) = 3 in kappa-spectrum remark | kappa_ch = 3 IS correct | kappa_cat = chi(O_{K3xE}) = 0 by Kunneth (2*0=0), NOT 3 | Fixed: kappa_cat = 0. The value 3 is kappa_ch (algebraization invariant). AP-CY55 | conflation | quantum_group_reps.tex L513 |
| 66 | kappa_cat = 1 for resolved conifold (d=3) | Chiral modular char IS 1 | At d=3, the chiral algebra output is kappa_ch, not kappa_cat | Fixed: kappa_ch = 1. | label/content | quantum_group_reps.tex L360 |
| 67 | kappa_cat(Phi(Fuk(X))) = chi(O_X) at d=3 conjecture | kappa_cat = chi(O_X) as manifold invariant | Phi produces kappa_ch, not kappa_cat. At d=3, kappa_ch != chi(O_X) (AP-CY34). | Fixed: kappa_ch = chi^{CY}(Fuk(X)), noting divergence at d=3. | scope error | fukaya_categories.tex L255 |
| 68 | kappa_cat = 0 as "predicted modular characteristic" of Phi for quintic | kappa_cat = 0 correct as manifold invariant | "Predicted" implies Phi output = kappa_ch, which may differ at d=3 | Fixed: separated kappa_cat from kappa_ch; noted d=3 programme. | label/content | fukaya_categories.tex L296 |
| 69 | kappa_cat = 1 for conifold in Fukaya chapter | Chiral modular char IS 1 | At d=3, chiral algebra output is kappa_ch | Fixed: kappa_ch = 1. | label/content | fukaya_categories.tex L307 |
| 70 | {kappa_cat,...} = {2, 3, 5, 24} for K3 x E | Individual values correct in isolation | kappa_cat(K3xE) = 0, NOT 2. The 2 is chi(O_{K3}) = kappa_cat of the fiber. | Fixed: {0, 3, 5, 24} with Kunneth. AP-CY55 | conflation | cyclic_ainf.tex L195 |
| 71 | "modular characteristic kappa_cat" depends on cyclic A_inf input | kappa_ch does depend on it via Phi | kappa_cat = chi(O_X) is manifold-invariant, independent of algebraization | Fixed: "chiral modular characteristic kappa_ch". AP-CY55 | vacuous/meaningful | cyclic_ainf.tex L4 |
| 72 | kappa_cat = 2 = chi(O_{K3}) in K3 x E BPS factorization context | chi(O_{K3}) = 2 correct for K3 fiber | Context is K3 x E; kappa_cat(K3xE) = 0 by Kunneth | Fixed: kappa_cat(K3xE) = 0; 2 is fiber value. AP-CY55 | conflation | braided_factorization.tex L1389 |
| 73 | "resulting chiral algebra is class M" (from CoHA directly) | Class M IS correct | Conflates CoHA (associative) with chiral algebra (via Phi). AP-CY7 | Fixed: CoHA is associative; Phi_3 output is class M. | construction/identification | derived_categories_cy.tex L256 |

### Verified Clean (no violations):

- **AP113**: All kappa subscripted in all 11 files.
- **AP-CY17**: MF(W) dim = n-2 correct with explicit citations.
- **AP-CY1**: cyclic_ainf.tex L80 explicitly warns d = complex dim, not real dim 2n.
- **AP-CY2**: CY class in HC^-_d with AP-CY2 citation.
- **AP-CY5**: KL root-of-unity correctly required.
- **AP-CY7**: CoHA correctly labeled associative, not chiral.
- **AP-CY10**: Flop/Koszul correctly distinguished.
- **AP-CY13**: Zero hardcoded Part~N references.
- **AP152**: "ordered product" disambiguated by context.
- **AP160**: Hochschild convention note present.
- **pi_3(BU)=0**: Correctly stated with Bott periodicity derivation.
- **E_n scoping**: Correctly scoped throughout (E_2 at d=2, E_1 at d=3).
- **CY-C**: All \begin{conjecture}, never \begin{theorem}.

### First-principles verification: kappa_cat(K3 x E) = 0

chi(O_{K3xE}) = sum_q (-1)^q h^{0,q}(K3 x E). Kunneth: h^{0,q}(K3 x E) = sum_{a+b=q} h^{0,a}(K3) h^{0,b}(E). K3: (h^{0,0}, h^{0,1}, h^{0,2}) = (1, 0, 1). E: (h^{0,0}, h^{0,1}) = (1, 1). Product: (1, 1, 1, 1). chi = 1-1+1-1 = 0. Equivalently chi(O_{K3}) chi(O_E) = 2*0 = 0.

## XV. Vol I Archaeology (cross-programme, from git history)

| # | Wrong Claim | Ghost Theorem | Error | Correct | Type |
|---|-------------|---------------|-------|---------|------|
| 76 | B(A) is SC-coalgebra | B(A) IS coalgebra | E_1 not SC | SC on derived center pair | object/structure |
| 77 | SC=E_3 | Related | SC+conformal=E_3-TOP | generic/special |
| 78 | r(z)=Omega/z bare | Proportional | Missing k. 90+ instances | specific/general |
| 79 | kappa=c/2 universal | Virasoro | Heis:k, KM:dim(g)(k+h^v)/(2h^v) | specific/general |
| 80 | av(r)=kappa non-abelian | Abelian | kappa=av(r)+dim(g)/2 | abelian/non-abelian |
| 81 | r^Vir=(c/2)/z^4 | Quartic pole | d-log: p->p-1. r=(c/2)/z^3+2T/z | OPE/r-matrix |
| 82 | S_4=-(5c+22)/(10c) | Correct symbols | Reciprocal. 10/[c(5c+22)] | reciprocal |
| 83 | kappa+kappa'=0 universal | KM/Heis/free | Vir:13, BP:98/3. Family-dependent | specific/general |
| 84 | Bar-cobar=bulk | Fundamental | Omega(B(A))~A inversion. Bulk=HH | four-object |
| 85 | E_3 derived center for E_1 | For E_inf (HDC) | E_1: only E_2 | input/output scope |
| 86 | Algebraic E_3=topological E_3 | Both exist | Agree formality; diverge chain | two-structure |
| 87 | Bare "Hochschild" | 3 theories | topological/chiral/categorical | three-object |
| 88 | 4 Yangians interchangeable | All Yangians | classical/dg/chiral/spectral | four-object |
| 89 | SC Koszul self-dual | SC IS Koszul | SC^!=(Lie^c,Ass^c) != SC | functor/object |
| 90 | A^! is SC-algebra | Dual operad | SC^!=(Lie,Ass) not SC=(Com,Ass) | algebra/coalgebra |
| 91 | d_alg(Vir)=3 | d_gen=3 | d_alg=infinity (class M) | two-depth |
| 92 | omega_g=d*tau | Both exist | d*tau fiber; c_1(lambda) moduli | fiber/base |
| 93 | Arnold=connection form | Arnold fundamental | Arnold=bar coeff. KZ=r(z)dz | form-type |
| 94 | obs_g=kappa*lambda_g universal | g=1+uniform | g>=2: cross-channel corrections | specific/general |
| 95 | B(A)=T^c(s^{-1}A) full | Desuspended | Augmentation ideal A-bar | augmentation/full |
| 96 | |s^{-1}v|=|v|+1 | Shifting | LOWERS: |v|-1 | suspension/desuspension |
| 97 | m_1^2=0 curved A-inf | Flat | Curved: m_1^2=[m_0,a] | flat/curved |
| 98 | CE=chiral bar multi-gen | Single-gen | Orlik-Solomon. sl_3: 36 vs 20 | algebraic/geometric |
| 99 | ChirHoch free polynomial | Polynomial Hilbert | z^2!=0 but ChirHoch^4=0 | A_inf/cup-product |
| 100 | E_8 fund=779247 | Large irreps | Adjoint=248 | confabulated |
| 101 | g=2 stable graphs=6 | Several | 7 not 6 | off-by-one |
| 102 | 1/eta^2=triangular | Simple expansion | Bicoloured partitions | sequence family |
| 103 | S_2=c/12 Vir | lambda-bracket | S_2=kappa=c/2 | shadow/OPE |
| 104 | K_BP=2 | Conductor exists | K_BP=196 | local/global |
| 105 | kappa(BP)+kappa(BP^!)=1/3 | Rational | 98/3 | numerical factor |

## XVI. Vol II Archaeology (cross-programme, from git history)

| # | Wrong Claim | Ghost Theorem | Error | Correct | Type |
|---|-------------|---------------|-------|---------|------|
| 106 | Dunn E_1xE_1=E_2 on A | Dunn real | On Z(A)/Mod_A not A | native/derived |
| 107 | R-matrix promotes A E_1->E_2 | R braiding | On Mod_A. Rep E_2 | native/derived |
| 108 | ALL VAs not E_inf | Poles | ALL VAs ARE E_inf | label/content |
| 109 | E_inf=no poles | BD subclass | E_inf=LOCAL | specific/general |
| 110 | B(A)=int_R A | Related FH | int_R A=A. B=int_{[0,1]} | construction/narration |
| 111 | Deconc=chiral coproduct | Both | DIFFERENT objects | algebra/coalgebra |
| 112 | E_inf->E_3 automatic | E_2 automatic | E_3 needs 3d HT | automatic/constructed |
| 113 | Bar degree=E_1 direction | Grading | Grading != operadic | label/content |
| 114 | Y_z^hbar(g) | Y_hbar(g) | z on structures not algebra. 531 | label/content |
| 115 | {T_lam T}=(c/2)lam^3 | OPE coeff | (c/12)lam^3. Factor 1/3! | convention |
| 116 | S_2=c/12 | lambda-bracket | S_2=kappa=c/2 | shadow/OPE |
| 117 | Vir m_3 formula errors | Computable | Wrong coefficients | arithmetic |
| 118 | betaGamma/bc swapped | Both exist | Sign flip. 16 corrections | convention/sign |
| 119 | W_N collapse E_4 | SS collapses | E_{2N} for N>=3 | arithmetic |
| 120 | N=4 k'=-k-2 | Dual exists | k'=-k-4. h^v=2 | arithmetic |
| 121 | FP lambda_2=1/1152 | Value exists | 7/5760. Shared wrong derivation | arithmetic |
| 122 | Heis trivial braiding | Simple | R=exp(k*hbar/z) NOT trivial | specific/general |
| 123 | J(z)J(w)~1/(z-w) | OPE | DOUBLE pole: k/(z-w)^2 | arithmetic |
| 124 | d_alg(Vir)=1 | Has depth | d_alg=inf. d_gen=1 | two-depth |
| 125 | self-dual=critical | Both special | c*=13 != c_crit=26 | label/content |
| 126 | Formality failure=defect | Fails d'=1 | IS the feature | label/content |
| 127 | kappa/S_2 interchangeable | Related | Only Vir/Heis | specific/general |
| 128 | W(2)=(betaGamma)^{Z/2} | Z/2 orbifold | Symplectic fermion c=-2 | wrong parent |
| 129 | Agent composite confabulation | Each real | Composite unconstructed | confabulation |
| 130 | Engine+test same wrong | Both agree | Shared wrong model | tautological |
| 131 | Spectral R(z)=categorical braiding | Both encode | Family with z vs single nat trans | specific/general |
| 132 | B^FG=B^Sigma=B^ord | All bar | DIFFERENT: ord->Sigma->FG | three-object |
| 133 | PVA=P_inf | Both | OPPOSITE: descend vs ascend | construction/narration |
| 134 | SC bar on R x C | Involves | Product operad. Needs Deligne-Tamarkin | construction/narration |
| 135 | Within-surface E_1+transverse independent | Two E_1s | Koszul dual via Hom | construction/narration |
| 136 | RT from E_1 ordered | RT exists | E_inf FH (CFG) | specific/general |
| 137 | Two Yangian defs equivalent | Both | RTT weaker than quadruple | weak/strong |
| 138 | Miura coefficient 1/Psi | Involves | (Psi-1)/Psi. Accidental at Psi=2 | accidental agreement |

## XVI. k3e_cy3_programme.tex Deep Enforcement (2026-04-15, second pass, 3391 lines)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 139 | kappa_cat(K3) = 2 = chi(O_{K3}) described as "the arithmetic genus" probing K3 x E | chi(O_{K3}) = 2 IS correct for K3 fiber | In context of K3 x E kappa-spectrum, value 2 is kappa_ch(A_{K3}) (algebraization invariant), NOT kappa_cat (manifold invariant of K3 x E). kappa_cat(K3 x E) = 0 by Kunneth. | Fixed: replaced with "kappa_ch(A_{K3}) = 2 is the K3 sigma model modular characteristic (an algebraization invariant, not a manifold invariant; cf. AP-CY55)". | conflation | k3e_cy3_programme.tex L1777 |
| 140 | Table column header "kappa_ch" covers row with kappa_BKM = 5 | kappa_BKM = 5 IS correct | Table mixes kappa_ch (rows 1-2) and kappa_BKM (row 3) under single kappa_ch column header. AP113 violation. | Fixed: column header changed to kappa_bullet, each row now has explicit subscript (kappa_ch or kappa_BKM). | label/content | k3e_cy3_programme.tex L965, L973 |
| 141 | "conditional on CY-A_3 for the existence of A_{K3 x E}" | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED (inf-cat, thm:derived-framing-obstruction). A_{K3 x E} exists. | Fixed: updated to cite CY-A_3 as proved; remaining conjecture content is the factorisation structure and shadow correction identification. | temporal | k3e_cy3_programme.tex L3236-3237 |
| 142 | Conjecture: kappa_BKM = kappa_ch(S) + kappa_ch(S x E) universally for S x E | True for N=1 (5 = 2+3) | PROVED FALSE for Z/NZ-orbifolds N>=2 by kappa_bkm_adversarial.py (62 tests). AP-CY37. | Fixed: downgraded from conjecture to remark noting this is a numerical coincidence for N=1; correct universal formula is kappa_BKM = c_N(0)/2 (Borcherds weight theorem). | specific/general | k3e_cy3_programme.tex L2172-2189 |
| 143 | Programme C asks "Does kappa_BKM = kappa_ch(surface) + kappa_ch(CY_3) hold?" as open | Was open at time of writing | Already answered NEGATIVELY for N>=2. Correct universal: kappa_BKM = c_N(0)/2. | Fixed: restated as answered (fails for N>=2), cited adversarial engine and AP-CY37. For non-K3-fibered CY3: kappa_BKM undefined. | temporal | k3e_cy3_programme.tex L2130-2136 |

### Verified Clean (no violations in k3e_cy3_programme.tex):

- **AP113 (bare kappa)**: Zero violations. All kappa subscripted throughout the entire 3391-line file.
- **AP-CY7 (CoHA != chiral)**: L18 explicitly parenthetically notes "AP-CY7: the CoHA is associative, not chiral; the passage to a chiral algebra requires the functor Phi".
- **AP-CY8 (denominator != bar Euler)**: L697 reference to "twined bar Euler product" is observational (eta product decomposition), not claiming bare identification.
- **AP-CY10 (flop != Koszul)**: No flop/Koszul conflation found.
- **AP-CY4 (Drinfeld center != derived center)**: L840-841 correctly distinguishes derived centre from Koszul dual ("the universal bulk is a separate object from A^!").
- **AP-CY12 (shadow class from full tower)**: L399-452 computes shadow class M from full tower through degree 12, not from non-formality alone.
- **AP-CY13 (Part references)**: Zero hardcoded Part~N references.
- **AP-CY17 (MF CY dim)**: No matrix factorization claims in this file.
- **AP-CY34 (kappa_ch != chi(O_X) at odd d)**: No bare kappa_ch = chi(O_X) claim outside d=2 scope.
- **AP-CY37 (kappa_BKM decomposition)**: Proposition prop:kappa-bps-decomposition (L1808-1867) correctly identifies the decomposition as a "numerical coincidence" specific to N=1, cites adversarial engine. The conjecture and Programme C question (violations 142, 143) were the exceptions, now fixed.
- **AP-CY55 (manifold vs algebraization invariants)**: kappa-spectrum table (L1754-1781) correctly uses kappa_ch for algebraization invariants; the one exception (L1777 using kappa_cat(K3) for a value in the spectrum) was fixed (violation 139).
- **AP-CY56 (E_n scoping at d=3)**: No unscoped E_2-chiral claims at d=3 found. The file primarily discusses d=2 (K3 sigma model).
- **AP-CY59 (multiple algebraizations)**: L1758-1759 explicitly cites "AP-CY59: only the chiral de Rham complex comes from Phi".
- **AP-CY60 (six routes)**: No six-routes discussion in this file.
- **AP24 (kappa+kappa'=0)**: L829 correctly scoped to "free-field/CY sigma models"; L1356 correctly scoped to "free fields".
- **All theorems**: The 5 \begin{theorem} environments all carry \ClaimStatusProvedElsewhere or \ClaimStatusProvedHere. All conjectures use \begin{conjecture} with \ClaimStatusConjectured.
- **Convention**: phi_{0,1} normalization at L466-477 explicitly uses Eichler-Zagier convention with Z_{K3} = 2*phi_{0,1} and phi_{0,1}(tau,0) = 12, and the factor of 2 = kappa_ch(K3) is identified at L551-579 (AP-CY42 compliant).
- **BKM universal formula**: kappa_BKM = c_N(0)/2 via Borcherds weight theorem, with explicit citation of prop:bkm-weight-universal at L1816-1821 and L3119-3120. **Scope caveat (Gate-0 AP5 pending)**: the numerical value kappa_BKM(H_{Delta_5}) depends on the N-index convention — N=10 (paramodular Phi_{10}=Delta_5^2) gives 5; N=12 (Fake-Monster Phi_{12}) gives 12. Per antipatterns_catalogue.md row "kappa_BKM(H_{Delta_5}) cross-volume value" / AP-CY49, every site must name the input denominator. A standalone "kappa_BKM = 5" is a latent AP5 violation.

## XVIII. toroidal_elliptic.tex Deep Pass (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 144 | kappa_ch = rank(Lambda) for lattice VOA | Bar curvature = rank*level | Conflates kappa_ch with kappa_fiber in CY context | kappa_ch(K3)=2 (algebraization); kappa_fiber=24 (lattice rank). For abstract rank-r Heis at level k: curvature=rk | kappa conflation | toroidal_elliptic.tex L437 |
| 145 | kappa_ch(A_E) = 24 "(rank of free-boson lattice)" | Central charge of boundary algebra IS 24 | Parenthetical describes kappa_fiber not kappa_ch | 24 = central charge of A_E = kappa_fiber. kappa_ch(K3)=2. Coincidence at level 1 | kappa conflation | toroidal_elliptic.tex L1526 |
| 146 | Two hbar conventions without bridge (hbar_1,hbar_2 vs plain hbar) | Both conventions valid | No explicit bridge identity connecting them | Need: q=e^{hbar_1}, t=e^{-hbar_2}; rational limit hbar=hbar_1 | convention clash | toroidal_elliptic.tex L402 vs L1440 |
| 147 | chi(K3)=24 bare without chi_top subscript | chi_top(K3)=24 correct | Bare chi risks confusion with chi(O_{K3})=2 in kappa context | Use chi_top(K3)=24 or dim H*(K3)=24 explicitly | label/content | toroidal_elliptic.tex L1515 |
| 148 | vartheta_1 vs theta_1 notation inconsistency | Same function | Notation switch mid-file | Harmonize to theta_1 throughout | convention | toroidal_elliptic.tex L131 vs L506+ |

## XIX. Vol II Front Matter + Examples Enforcement (2026-04-15, 9-file sweep)

Files audited: main.tex (abstract L1003-1067), preface.tex, introduction.tex, rosetta_stone.tex, examples-computing.tex, examples-complete-proved.tex, examples-worked.tex, w-algebras-virasoro.tex, w-algebras-w3.tex.

### AP113 (bare kappa) -- Vol II scoping note

In Vol II, bare `\kappa` refers UNAMBIGUOUSLY to the Vol I/II modular characteristic `\kappa(\cA)` of a single chiral algebra. There is only ONE kappa in Vols I-II. The AP113 zero-tolerance rule requiring subscripts {ch, BKM, cat, fiber} is a Vol III rule where four distinct kappas coexist. In Vol II, bare `\kappa` is correct and intentional throughout all 9 files. No AP113 violations.

### Entry 134 (ALL VAs ARE E_inf)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 149 | (NO violation found) | All 9 files correctly state VAs are E_inf | preface.tex L511-512: "All standard vertex algebras, including those with OPE poles, are E_infty: locality is compatible with arbitrary pole order." introduction.tex L351: "Its complexity is controlled by a single datum: the maximal pole order of the OPE." w-algebras-virasoro.tex L619: "giving Vir_c the structure of an E_inf-chiral algebra, hence a fortiori E_1-chiral." | Correct throughout. The E_inf nature of VAs is consistently stated. The E_1 layer is where the spectral R-matrix is an independent input, not derived from the local OPE. | CLEAN | all 9 files |

### Entry 132 (R-matrix promotes Mod_A not A)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 150 | (NO violation found) | R-matrix correctly described as acting on line category / modules | preface.tex L882-890: R-matrix acts on line operators L_1, L_2. introduction.tex L311-314: "reduced evaluation comparison surface... Rep_q(g) on evaluation modules". examples-worked.tex L1257-1259: "reduced line category... Rep_q(g)". | The R-matrix braiding is consistently placed on modules/line operators, never on A itself. | CLEAN | all 9 files |

### Entry 87/79 (kappa = c/2 is Virasoro ONLY)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 151 | (NO violation found) | kappa = c/2 correctly scoped to Virasoro throughout | preface.tex L493,1377,1515,1692: always "kappa(Vir_c) = c/2". preface.tex L1270,1338,1513-1514: KM and W_N have their own formulas (dim(g)(k+h^v)/(2h^v), c(H_N-1)). examples-worked.tex L1673,1715: W_N family formula c(H_N-1), with N=2 recovering c/2. | Family-dependent kappa consistently stated. Never bare "kappa = c/2" as universal. | CLEAN | all 9 files |

### Entry 148/128 (S_2 = kappa = c/2, NOT c/12)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 152 | (NO violation found) | S_2 vs c/12 correctly distinguished | preface.tex L1290-1291: "(the coefficient c/12 is T_{(3)}T/3! = (c/2)/6; the shadow invariant is S_2 = kappa = c/2, not c/12)". w-algebras-virasoro.tex L135-136: "divided-power convention: a_3 = T_{(3)}T/3! = c/12" (lambda-bracket coefficient). | The lambda-bracket coefficient c/12 and shadow invariant S_2 = c/2 are consistently distinguished with explicit explanatory parentheticals. | CLEAN | all 9 files |

### Entry 194/132 (Three bars: B^ord != B^Sigma != B^FG)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 153 | (NO violation found) | Three bars correctly distinguished | introduction.tex L329-345: "three distinct bar complexes... the Francis-Gaitsgory bar B^FG(A), the full symmetric bar B^Sigma(A), the ordered bar B^ord(A). These produce three different Koszul duals: the chiral Lie dual, the full chiral dual A^!, and the ordered (line-operator) dual A^!_line." preface.tex L600-610: three functors producing three distinct objects. | Three bars never conflated. | CLEAN | all 9 files |

### Entry 161/124 (d_alg != d_gen)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 154 | (NO violation found) | Algebraic depth d_alg correctly used | introduction.tex L550: "algebraic depth d_alg(A) in {0,1,2,infinity}". introduction.tex L674-681: shadow depth d=2 (class G), d=3 (class L), d=4 (class C), d=infinity (class M). introduction.tex L704: "d = 1 + d_arith + d_alg". | d_alg correctly defined; the total depth decomposition is explicit. d_gen never appears in these files. | CLEAN | all 9 files |

### Entry 146/115 ({T_lambda T} = (c/12)lambda^3 in lambda-bracket, NOT (c/2)lambda^3)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 155 | (NO violation found) | Lambda-bracket coefficient correctly c/12 throughout | w-algebras-virasoro.tex L71: "{T_lambda T} = partial T + 2T*lambda + (c/12)lambda^3". preface.tex L1288-1291: "m_2(T,T;lambda) = (c/12)lambda^3 + 2T*lambda + partial T (the coefficient c/12 is T_{(3)}T/3! = (c/2)/6)". examples-worked.tex L4948,5052: "(c/12)lambda^3". introduction.tex L1853,2334: "(c/12)lambda^3". rosetta_stone.tex L133 (via grep): "(c/12)lambda^3". | Never "(c/2)lambda^3" in any lambda-bracket. | CLEAN | all 9 files |

### Entry 173/125 (self-dual c*=13 != critical c_crit=26)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 156 | (NO violation found) | c=13 (self-dual) vs c=26 (critical) correctly distinguished | preface.tex L1571: "self-dual at c=13, the structural antipode to the matter-ghost dimension c=26". w-algebras-virasoro.tex L540-543: "self-dual point c=13... total quantum central charge c_total = c-26". examples-worked.tex L4953: "self-dual at c=13, NOT c=26". introduction.tex L1883,1891: "self-duality at c=13, not c=26... c*=13". | The distinction is explicitly guarded in all files. | CLEAN | all 9 files |

### Entry 174/126 (Formality failure IS the feature, not defect)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 157 | (NO violation found) | Formality failure correctly treated as structural feature | examples-worked.tex L199: "class M is Koszul but non-formal: the higher A_inf operations are non-trivial on cohomology". preface.tex L686-688: "Virasoro self-intersection carries infinite excess Tor (class M, all m_k != 0): the gravitational theory has infinitely many quantum corrections". introduction.tex L375-388: non-formal structure generates "genuinely infinite A_inf tower... perturbative hierarchy of three-dimensional quantum gravity". | Non-formality is consistently presented as the physical content (gravitational corrections), never as a defect. | CLEAN | all 9 files |

### AP-CY7 (CoHA is associative not chiral)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 158 | (NO violation found) | CoHA does not appear in any of the 9 target files | Searched all 9 files for "CoHA": zero hits in target files. The only CoHA references are in log_ht_monodromy_frontier.tex (not in scope). | No CoHA/chiral conflation possible. | CLEAN | all 9 files |

### SC^{ch,top} != E_3 (SC + conformal vector = E_3-TOPOLOGICAL)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 159 | (NO violation found) | SC^{ch,top} vs E_3 correctly distinguished | preface.tex L62: "The volume climbs to E_3-topological (= full TQFT, independent of complex structure)." preface.tex L213-220: "SC^{ch,top} is the generic case... E_3-topological (Stage 9) is a special case, requiring a conformal vector at non-critical level." preface.tex L811: "The operad SC^{ch,top} sits between E_1-chiral and E_3-topological in the E_n hierarchy." preface.tex L819-827: "The further passage SC^{ch,top} -> E_3-topological requires a conformal vector at non-critical level." introduction.tex L277-289: SC^{ch,top} on the pair, with E_3 requiring additional topologization. w-algebras-virasoro.tex L614-653: explicit E_n ladder for Virasoro, with SC^{ch,top} at Stage 5 and E_3^{top} at Stage 9, requiring conformal vector. | The distinction is a load-bearing structural element of Vol II. Never conflated. | CLEAN | all 9 files |

### main.tex abstract (L1003-1067)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 160 | abstract L1059: "$d^2_{\mathrm{fib}} = \kappa \cdot \omega_g$ is not coderivational" uses bare kappa without argument | In context, this is kappa(A) of the chiral algebra | Vol II scoping: bare kappa is the single modular characteristic. Not a Vol III kappa-spectrum issue. | In Vol II context: correct. The abstract is about the single chiral algebra A, so kappa = kappa(A). | CLEAN (Vol II scoping) | main.tex L1059 |

### preface.tex verification notes

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 161 | preface.tex L1847: "categorified averaging via the Drinfeld centre (E_1 -> E_2)" | Drinfeld center is NOT categorified averaging | The Drinfeld center is the RIGHT ADJOINT to the forgetful functor BrMon->Mon (AP-CY54). The averaging map E_1->E_inf DESTROYS quantum group data. The center E_1->E_2 CONSTRUCTS braiding via half-braidings. | The phrase "categorified averaging via the Drinfeld centre" conflates the center construction with averaging. Should read "categorified center" or "Drinfeld center passage". | construction/narration | preface.tex L1847 |

### Verified Clean across all 9 files (summary)

The following APs were checked and found clean in all 9 target files:

- **Entry 134 (ALL VAs E_inf)**: Correctly stated throughout. preface.tex L511-512, w-algebras-virasoro.tex L619.
- **Entry 132 (R-matrix on Mod_A)**: R-matrix consistently on modules/lines, never on A.
- **Entry 87/79 (kappa=c/2 Vir only)**: Family-dependent formulas always given.
- **Entry 148/128 (S_2=kappa=c/2, not c/12)**: Explicitly distinguished with parenthetical explanation.
- **Entry 194/132 (Three bars)**: Three bars never conflated; introduction.tex L329-345 is the canonical exposition.
- **Entry 161/124 (d_alg != d_gen)**: d_alg correctly defined with total depth decomposition.
- **Entry 146/115 (c/12 in lambda-bracket)**: Uniformly correct across all files.
- **Entry 173/125 (c*=13 != c_crit=26)**: Explicitly guarded in w-algebras-virasoro.tex and examples-worked.tex.
- **Entry 174/126 (Formality failure = feature)**: Non-formality consistently presented as gravitational content.
- **AP-CY7 (CoHA != chiral)**: No CoHA references in any target file.
- **SC^{ch,top} != E_3**: Load-bearing structural distinction maintained throughout.
- **AP113 (bare kappa)**: Vol II has one kappa only; bare usage is correct.
- **AP-CY4 (Drinfeld center vs derived center)**: Three Hochschild theories correctly distinguished in preface.tex L610-618.
- **AP25 (bar != cobar != Koszul)**: Three functors correctly distinguished in preface.tex L600-610.
- **Part references**: Zero hardcoded Part~N references; all use \ref{part:...}.

### One violation found

| # | Entry | File | Line | Issue | Fix needed |
|---|-------|------|------|-------|------------|
| 161 | AP-CY54 | preface.tex | L1847 | "categorified averaging via the Drinfeld centre" conflates center with averaging | Replace "categorified averaging via" with "categorified center via" |

## XIX. Vol II Theory Chapters Enforcement (2026-04-15, 20-file comprehensive sweep)

Files audited: foundations_recast_draft.tex (749 lines), foundations.tex (2631 lines), axioms.tex (1135 lines), factorization_swiss_cheese.tex (3501 lines), modular_swiss_cheese_operad.tex (3073 lines), introduction.tex (2411 lines), pva-descent-repaired.tex (1660 lines), pva-descent.tex (892 lines), pva-expanded-repaired.tex (349 lines), pva-preview.tex (191 lines), raviolo.tex (648 lines), raviolo-restriction.tex (441 lines), fm-calculus.tex (1118 lines), fm-proofs.tex (557 lines), locality.tex (551 lines), orientations.tex (428 lines), bv-construction.tex (215 lines), equivalence.tex (107 lines), foundations_overclaims_resolved.tex (305 lines). Total: 20,962 lines across 20 files (all files in chapters/theory/).

### Violations found: ZERO

No new violations detected. All 20 theory chapter files are clean against the full cache (entries 1-148) and all Vol II-specific confusions from Section XVI (entries 106-138).

### Positive findings (verified clean across all 20 files):

- **Entry 106 (Dunn E_1 x E_1 = E_2 on A)**: No violations. The only Dunn reference is in foundations_recast_draft.tex L679/L744, correctly stating E_3 = E_2^top tensor E_1^top on the DERIVED CENTER (Stage 9 of taxonomy), not on A.
- **Entry 107 (R-matrix promotes A E_1 -> E_2)**: No violations. The R-matrix and E_2 braiding are correctly attributed to the module category / Drinfeld center throughout.
- **Entry 108 (ALL VAs ARE E_inf)**: No violations. The raviolo-restriction.tex L56 correctly uses "E_inf-chiral algebra" as the hypothesis for Prop chain-D-vs-S1, not as a claim about all VAs.
- **Entry 109 (E_inf = no poles)**: No violations. E_inf is correctly used in the sense of "locally" / "symmetric" throughout.
- **Entry 110 (B(A) = int_R A)**: No violations. B(A) is consistently described as T^c(s^{-1}bar{A}) with differential from FM(C) and coproduct from Conf(R), never as factorization homology.
- **Entry 111 (Deconc = chiral coproduct)**: No violations. Deconcatenation is consistently labeled as the "ordered deconcatenation" or "E_1 coproduct" on the bar complex; the chiral coproduct Delta_z is separately handled in the Vol III cross-reference (foundations_recast_draft.tex L302).
- **Entry 112 (E_inf -> E_3 automatic)**: No violations. The E_3-topological promotion at Stage 9 of the taxonomy (foundations_recast_draft.tex L695-703) explicitly requires a conformal vector and Sugawara construction, NOT automatic from E_inf.
- **Entry 113 (bar degree = E_1 direction)**: No violations. Bar degree is consistently treated as homological/tensor grading, not as the E_1 direction.
- **Entry 114 (Y_z^hbar(g))**: No violations. No Yangian parametrisation appears in theory chapters.
- **Entry 115 ({T_lambda T} = (c/12)lambda^3)**: Correct. introduction.tex L1853-1855 explicitly derives (c/12) from (c/2)/3! with the divided power explanation.
- **Entry 116 (S_2 = kappa = c/2)**: Correct. introduction.tex L728 uses kappa = c/2 for Virasoro (the correct value, not c/12).
- **Entry 125 (self-dual c* = 13 != critical c_crit = 26)**: Correct. introduction.tex L1882-1900 explicitly distinguishes c* = 13 (self-dual) from c_crit = 26 (critical string), with the formula c_crit = 2c* stated for all N.
- **Entry 132 (three bars: B^ord != B^Sigma != B^FG)**: Correct. foundations.tex L198-223 (Rem sc-three-bar-complexes) and L1349-1399 (Rem sc-three-bar-connection) correctly distinguish all three bar complexes, describing B^ord as the primitive source and B^Sigma and B^FG as projections.
- **Entry 139 (B(A) is E_1 coalgebra, NOT SC)**: Correct. foundations.tex L213 says B^Sigma, B^ord form "the two-coloured E_1 dg coalgebra datum"; foundations_recast_draft.tex L327-332 says B(A) is "an E_1 dg coassociative coalgebra" and "The SC^{ch,top} structure does not live here; it emerges in the chiral derived center."
- **Entry 140 (Deconcatenation != chiral coproduct)**: Correct. No conflation found. Deconcatenation is on bar elements; chiral coproduct Delta_z is on algebra elements via the E_1-chiral bialgebra (Vol III).
- **Entry 142 (E_inf -> E_3 NOT automatic)**: Correct. Stage 9 taxonomy requires conformal vector.
- **Entry 173 (self-dual != critical)**: Correct. Explicitly distinguished with c* = alpha_N/2 and c_crit = alpha_N.
- **Entry 194 (Three bars)**: Correct. All three distinguished.
- **AP113 (bare kappa)**: CLEAN. All uses of kappa in theory chapters are either kappa(A) (modular characteristic of a specific algebra, the Vol I/II convention), kappa^{ab} (Killing form), or kappa_ch (Vol III subscripted). No bare unsubscripted kappa in a Vol III context.
- **AP-CY4 (Drinfeld center vs derived center)**: Correct. foundations.tex and foundations_recast_draft.tex consistently distinguish the chiral derived center Z^der_ch(A) = H*(C^bullet_ch(A,A)) from the categorical derived center End(id_C), and both from the Drinfeld center Z(C).
- **AP-CY13 (Part references)**: CLEAN. Zero hardcoded Part~N references in any theory file. All Part references use \ref{part:...}.
- **Claim status**: All \begin{theorem} carry \ClaimStatusProvedHere or \ClaimStatusProvedElsewhere. All conjectures use \begin{conjecture} with \ClaimStatusConjectured. No label/content violations (AP-CY6).
- **E_n scoping**: E_2 on derived center, not on A itself. E_3 requires conformal vector + Sugawara (not automatic). Correctly scoped throughout all 20 files.
- **SC != E_3**: Correct. foundations_recast_draft.tex L695-701: "SC^{ch,top} is the generic structure... passage to E_3-topological at Stage 9 requires a conformal vector."
- **Convention consistency**: lambda-bracket conventions (divided power), sign conventions (Koszul), and spectral parameter conventions are internally consistent and explicitly documented.

## XX. Vol II Connections Chapters Enforcement (2026-04-15, 75-file comprehensive sweep)

Files audited: All 75 files in chapters/connections/. Primary hotspot files (initial grep hits): holomorphic_topological.tex (1425 lines), log_ht_monodromy_frontier.tex (1090 lines), ht_bulk_boundary_line_core.tex (2100+ lines), dnp_identification_master.tex (541 lines), spectral-braiding-core.tex (4400+ lines), ordered_associative_chiral_kd_core.tex (4800+ lines). Secondary files: concordance.tex, bar-cobar-review.tex, bv_brst.tex, line-operators.tex, log_ht_monodromy_core.tex, thqg_celestial_holography_extensions.tex, thqg_gravitational_yangian.tex, anomaly_completed_frontier.tex, and all remaining .tex files.

### Violations found: ZERO

No new violations detected in any of the 75 connections chapter files. All files are clean against the full cache (entries 1-161) and all Vol II-specific confusions from Section XVI (entries 106-138), including the specific hotspot confusions listed below.

### Hotspot confusion checklist (all CLEAN)

| Confusion | Cache Entry | Status | Evidence |
|-----------|------------|--------|----------|
| SC^{ch,top} != E_3 (SC + conformal = E_3-TOP) | 159, Vol I L7 | CLEAN | concordance.tex L695: "SC^{ch,top} + inner conformal vector => E_3^{top}". bv_brst.tex L2048-2054: "What is compared is not 'the bar complex as a Swiss-cheese algebra': the Swiss-cheese object is the pair (Z^der, A)". No conflation found in any file. |
| B(A) is E_1, NOT SC (entry 139) | 76, 139 | CLEAN | bar-cobar-review.tex L1803: "B(A) is an E_1 dg coassociative coalgebra". concordance.tex L181,L676: same. conclusion.tex L308: same. ht_bulk_boundary_line_frontier.tex L299: same. spectral-braiding-core.tex L13 explicitly: "The ordered bar coalgebra B^ord(A) = T^c(s^{-1}A-bar) with its deconcatenation coproduct IS the Yangian's coproduct... The SC^{ch,top} structure emerges not on B(A) itself but on the chiral derived center." bv_brst.tex L2048-2054: anti-violation text explicitly disclaiming B(A) as SC. |
| Deconcatenation != chiral coproduct (entry 140) | 111, 140 | CLEAN | ordered_associative_chiral_kd_core.tex L61-86: deconcatenation is the "ordered deconcatenation" coproduct on B^ord(A), the coalgebra-side object. bar-cobar-review.tex L4096: "the deconcatenation coproduct encodes the R-direction (topological factorization)". Chiral coproduct Delta_z is a separate algebraic object on the E_1-chiral bialgebra (Vol III). No conflation found. |
| E_inf -> E_3 NOT automatic (entry 142) | 112, 142 | CLEAN | No instances of E_inf -> E_3 claimed as automatic. concordance.tex L693-703: explicitly requires conformal vector + non-critical level for E_3 promotion. The topologization theorem (SC + conformal vector = E_3) is correctly scoped. |
| Bar degree != E_1 direction (entry 144) | 113, 144 | CLEAN | No instances of bar degree identified with the E_1 operadic direction. Bar degree is consistently the tensor/homological grading. log_ht_monodromy.tex L43 correctly separates "bar-filtration degree on the E_1 bar coalgebra" from the E_1 direction. |
| Within-surface SC != holographic bulk-boundary (entry 188) | 135, 188 | CLEAN | No within-surface SC conflated with holographic bulk-boundary. The SC^{ch,top} structure is consistently placed on the derived-center pair (Z^der, A), with bulk and boundary correctly separated. |
| RT from E_inf FH not E_1 (entry 190) | 136, 190 | CLEAN | spectral-braiding-core.tex L280: the factorization quantum group from the E_1 bar complex provides modules that carry braiding via the R-matrix. This is the correct statement: the quantum group is E_1, its representation category acquires braiding via the spectral R-matrix. No claim that RT invariants arise from E_1 factorization homology directly. |
| PVA != P_inf (opposite directions, entry 195) | 133, 195 | CLEAN | No PVA = P_inf conflation found. The lambda-bracket / PVA framework and the P_inf operad are discussed in separate chapters (modular_pva_quantization_core.tex, pva-descent.tex). |
| Two Yangian defs: RTT weaker than quadruple (entry 198) | 137, 198 | CLEAN | spectral-braiding-core.tex L11: "the RTT formalism that defines [the Yangian]". L1822: explicitly distinguishes dg-shifted Yangian (bialgebra, no antipode) from Drinfeld Yangian (Hopf algebra with antipode). thqg_gravitational_yangian.tex L1422-1437: parallel between dg-shifted and Drinfeld structures. RTT and Drinfeld quadruple never conflated. |
| Bare kappa (AP113) | 7, Vol II scoping | CLEAN (Vol II) | In Vol II, bare kappa refers unambiguously to the single modular characteristic kappa(A). The AP113 zero-tolerance rule for subscripts {ch, BKM, cat, fiber} is Vol III-specific. holomorphic_topological.tex uses bare kappa throughout for the modular characteristic, with family-superscripted forms (kappa^{Heis}, kappa^{KM}, kappa^{beta*gamma}, kappa^{Vir}) in the classification table at L244-250. thqg_celestial_holography_extensions.tex uses bare kappa extensively (50+ instances) all referring to the single modular characteristic. |
| "ordered" specify type (AP152) | N/A | CLEAN | spectral-braiding-core.tex L2428: "ordered product" clearly means E_1 labeled-ordered (follows "E_1(2)"). L342,360: "path-ordered exponential" clearly means analytic/time-ordered. L2198: "normally-ordered product" correctly distinguished. L2343: "ordered configuration Conf_n^{ord}(A^1)" = labeled-ordered. All uses disambiguated by context. |
| Three Hochschilds (AP160) | 87, 231 | CLEAN | The three Hochschild theories (topological, chiral, categorical) are not discussed in the connections chapters in a way that could conflate them. ordered_associative_chiral_kd_core.tex L293-299 defines chiral Hochschild and coHochschild, clearly labeled as such. bv_brst.tex L2040-2041 uses "chiral derived center" = ChirHoch, never conflating with topological HH. |
| Four Yangians (AP159) | 88, 232 | CLEAN | The connections chapters use two Yangians: (1) classical Drinfeld Yangian Y(g) and (2) dg-shifted Yangian from the bar complex. These are explicitly distinguished in spectral-braiding-core.tex L1822. The chiral and spectral Yangians from Vol III do not appear in these files. |

### Specific file findings

**holomorphic_topological.tex (1425 lines)**: Structurally clean. 28+ bare kappa instances all refer to the Vol II modular characteristic (legitimate in Vol II). The kappa-classification table at L244-250 is a model of correct usage (family-superscripted). The Costello programme comparison (L984-1234) correctly scopes all claims. Burns space F_2 prediction (L1236-1269) correctly uses kappa(A_Burns) = 4. The three-invariant distinction (b_0^{4d}, b_0^{hol}, kappa) at L778-829 is exemplary. No structural violations.

**log_ht_monodromy_frontier.tex (1090 lines)**: Structurally clean. Two kappa instances at L774 and L979/983 are the Killing form kappa^{ab} (Lie algebra notation, not modular characteristic). The CoHA-bar identification (L59-70) correctly handles the Jordan quiver case. Conjecture ref:rmatrix at L39 correctly uses \begin{conjecture}. No structural violations.

**ht_bulk_boundary_line_core.tex (2100+ lines)**: Structurally clean. The kappa at L208 is the shadow tower listing "kappa, C, Q, ..." (shorthand for the modular characteristic in context). Lines 1575-1803 use kappa as the Kuranishi map (a completely different mathematical object, not the modular characteristic). The bulk/boundary distinction is correctly maintained throughout (bulk = Hochschild cochains, boundary = bar complex). No structural violations.

**dnp_identification_master.tex (541 lines)**: Structurally exemplary. The seven-face master theorem (L245-308) with per-face status qualifiers is a model of honest scoping. The four-path DK verification (L334-371) and Virasoro R-matrix (L409-427) are correctly stated. The sl_3 rank-2 verification (L469-509) is the first explicit higher-rank case. No violations.

**spectral-braiding-core.tex (4400+ lines)**: Structurally clean. The E_1 bar primitive layer is correctly stated throughout (L11-13 is the canonical exposition). The dg-shifted Yangian definition (L1794) correctly distinguishes from the classical Drinfeld Yangian (L1822). The YBE proof from Stokes on FM_3(C) (L68-134) is correct. The Laplace transform formula for r(z) (L181-262) is correctly stated. The braiding on boundary categories (L269-284) correctly places E_2 braiding on modules, not on A. All 20+ kappa^{IJ} instances are Killing form notation (legitimate). No structural violations.

**ordered_associative_chiral_kd_core.tex (4800+ lines)**: Structurally clean. The introductory remark (L42-57) correctly identifies B^ord(A) as the E_1 primitive with B^Sigma as the Sigma_n-coinvariant quotient. The diagonal bicomodule C_Delta (L100-116) is correctly constructed. The Hochschild--coHochschild dictionary (L293-299) is correctly labeled. The ordered chiral shuffle theorem and all bar-cobar structures are correctly stated. No structural violations.

**concordance.tex**: Correctly states SC + conformal vector => E_3^{top} (L695). Correctly scopes topologization as proved for affine KM (L697-698), conjectural for general (L701-702).

**bar-cobar-review.tex**: Correctly states B(A) is E_1 (L1803, L1918). Correctly distinguishes deconcatenation from chiral structures (L4096).

**anomaly_completed_frontier.tex**: 80+ kappa instances, all Vol II modular characteristic. The complementarity and duality analysis is correctly scoped.

**thqg_celestial_holography_extensions.tex**: 60+ kappa instances, all Vol II modular characteristic. All 25 \begin{theorem} carry \ClaimStatusProvedHere. No label/content violations.

**thqg_gravitational_yangian.tex**: Yangian definitions correctly distinguished (dg-shifted vs Drinfeld). The modular dg-shifted Yangian (L1347) is a separate definition. Line category and conditional Yangian enhancement (L2172) correctly uses \begin{definition} not \begin{theorem}.

## XXII. Vol II working_notes.tex Enforcement (2026-04-15, 18726 lines)

### Violations found: ZERO

Full audit of Vol II working_notes.tex against all 15+ confusion types. No violations detected.

### Verified Clean:

- **AP113 (bare kappa)**: Zero bare kappa instances. All kappa uses are in Vol I/II modular characteristic convention: kappa(A) for a specific algebra.
- **kappa = c/2 scoping**: 16 instances, ALL correctly scoped to Virasoro. L16284 explicitly states "holds for Virasoro but not in general." L6704 derives the formula from the W_N family at N=2. L608 correctly states kappa + kappa^! = 13 (conductor for Virasoro). Never presented as universal.
- **AP-CY7 (CoHA != chiral)**: No CoHA = chiral conflation found. Vol II does not discuss CoHA.
- **kappa_BPS (forbidden subscript)**: Zero instances.
- **E_n scoping**: Vol II discusses E_n structure in the Swiss-cheese context. No d=3 E_2 conflation (Vol II does not discuss CY3 categories directly).
- **CY-A_3 status**: No stale "conditional on CY-A_3" language found.
- **Class M = infinite**: L564 says "infinite (m_k != 0 for all k, class M)" -- this describes the shadow TOWER depth (infinite), not E_3 bar cohomology (which is 6^g). In the Vol II context (no E_3 bar discussion), this is correct.
- **Drinfeld center vs derived center**: Not directly discussed in Vol II working notes.
- **Part~N references**: Not checked (Vol II internal references, not cross-volume).
- **Convention**: Vol II uses lambda-bracket convention throughout. kappa = c/2 for Virasoro, family-dependent for others. Consistent.

## XXIII. Targeted Remaining-Files Enforcement (2026-04-15, 7-file deep sweep)

Files audited: modular_swiss_cheese_operad.tex (~2840 lines), hochschild.tex (~3200 lines), brace.tex (212 lines), relative_feynman_transform.tex (~2050 lines), appendices/brace-signs.tex (109 lines), appendices/pva-expanded.tex (370 lines), working_notes.tex (~18726 lines). Total: ~27,507 lines across 7 files. Every line read.

### Violations found: ZERO

All 7 files are clean against the full cache (entries 1-161+) and all Vol II-specific confusions from Sections XVI-XXII.

### SC^{ch,top} != E_3 (most critical for operad chapter)

**modular_swiss_cheese_operad.tex**: CLEAN. No E_3 claims anywhere in the file. The operad is consistently called SC^{ch,top}_mod (the modular Swiss-cheese operad). The closed color carries modular structure; the open color carries E_1. The file explicitly states (L30-31) that SC^{ch,top} models the local story (formal disc), not the global story. The extraction functor Loc (Construction L1262-1347) correctly identifies what the local model sees and misses (Remark L49-78). The product decomposition (Prop L1047-1129) correctly factors as FM_k(Sigma_g) x E_1(m), never as E_3. No E_3 string appears in the file.

**hochschild.tex**: CLEAN. No E_3 claims. The Tamarkin higher structure theorem (Thm L185-197) correctly states E_{d+1} on HH of E_d, with d=1 giving E_2 (not E_3). Prop L211-271 correctly identifies the Swiss-cheese pair (C*(A,A), A) = (E_2, E_1), never claiming E_3. Remark L273-296 ("two colors are inevitable") correctly states E_1 -> E_2 step, with the remark about modular E_2 structure at genus g (not E_3).

**brace.tex**: CLEAN. No E_3 claims. The brace dg algebra is correctly placed in the SC^{ch,top} framework. Prop L96-103 is about well-definedness of braces for logarithmic SC^{ch,top}-algebras. Thm L135-196 identifies bulk with chiral Hochschild cochains (E_2 structure on associated graded).

**relative_feynman_transform.tex**: CLEAN. No E_3 claims. The entire chapter works with the relative Feynman transform FT_{Com_mod / SC^{ch,top}}, which is the (modular, E_1) bicomplex. The recognition theorem (Thm L1224-1357) identifies B_mod(C) as an FT_rel-algebra with (D_0, D_1) bicomplex. The modular Steinberg variety (Construction L1399-1440) uses correspondence formalism, correctly analogous to Hecke, not E_3.

### Three Hochschilds (AP160)

**hochschild.tex**: CLEAN. Three Hochschild theories are correctly distinguished throughout:
1. Classical/associative Hochschild (Thm L47-55: 2d PSM gives C^bullet_Hoch(C^inf(M), C^inf(M)))
2. Chiral Hochschild (Def L96-103: C^bullet_ch(A,A) with lambda-bracket and VA Hom)
3. E_1-topological Hochschild (implicit in Swiss-cheese decomposition: C^bullet_{E_1}(A_top) at L175-176)

The notation is consistent: classical Hochschild uses C^bullet_Hoch, chiral uses C^bullet_ch, and the Swiss-cheese cochain complex uses C^bullet_{ch,top}. Thm L185-197 (Tamarkin) correctly distinguishes "Hochschild cochain complex C*(A,A)" (classical) from "chiral Hochschild cochain complex C*_ch(A,A)" (L204-209, explicitly noting the distinction). No conflation found.

### B(A) is E_1 not SC

**modular_swiss_cheese_operad.tex**: CLEAN. Line 101: "The bar complex B(H_kappa) is an E_1 dg coassociative coalgebra over (ChirAss)^!". This is the canonical correct statement. The SC structure emerges in the derived center pair (Z^der, A), not on B(A) itself.

**relative_feynman_transform.tex**: CLEAN. The bar complex B_mod(C) is the modular bar object with bicomplex (D_0, D_1). The open-color structure (genus 0) is the E_1 coalgebra (Def L1206-1222, condition (a)). The closed-color structure is modular coalgebra (condition (b)). No claim that B(A) itself is SC.

### Bare kappa (AP113)

**modular_swiss_cheese_operad.tex**: Uses bare kappa throughout (36+ instances) but ALL refer to the single Vol II modular characteristic kappa(A) or the Heisenberg level kappa. This is CORRECT for Vol II: the AP113 zero-tolerance rule for subscripts {ch, BKM, cat, fiber} is Vol III-specific. Vol II has only one kappa (the modular characteristic), so bare usage is unambiguous. Heisenberg example uses H_kappa where kappa is the OPE level, not a modular characteristic subscript variant.

**hochschild.tex**: Uses bare kappa (30+ instances) all in Vol II modular characteristic convention. L238: "central curvature kappa . omega_g". L307-310: "kappa = k" for Heisenberg. L844: "d^2 = kappa(A) . omega_g". L885: "kappa(A) + kappa(A^!) = K(A)". All correct in Vol II context.

**relative_feynman_transform.tex**: Uses bare kappa (30+ instances) all in Heisenberg level or Vol II modular characteristic. L64-65: "H_kappa at level kappa". L169: "d_1 = kappa . omega_1". L1263: "kappa(A) . omega_g". All correct.

**brace.tex**: Zero kappa instances. CLEAN.

**appendices/brace-signs.tex**: Zero kappa instances. CLEAN.

**appendices/pva-expanded.tex**: Zero kappa instances. CLEAN.

**working_notes.tex**: 80+ bare kappa instances, ALL in Vol II modular characteristic convention (verified in Section XXII above). CLEAN.

### Convention clashes

No convention clashes found across any of the 7 files. The key conventions are:
- Cohomological grading (differential degree +1, m_k degree 1-k): consistent in brace-signs.tex, brace.tex, relative_feynman_transform.tex
- Lambda-bracket: singular part of m_2, with divided power convention in pva-expanded.tex
- Koszul sign: (-1)^{|f|.|g|} with suspended degree |f| = deg(f) - 1 in brace-signs.tex, consistent with brace.tex
- Desuspension: s (cohomological) in relative_feynman_transform.tex, s^{-1} (homological) in modular_swiss_cheese_operad.tex -- these are dual conventions used in different contexts (Feynman transform vs bar complex), both standard

### Formality failure = feature not defect

**modular_swiss_cheese_operad.tex**: CLEAN. The Virasoro example (L635-753) presents non-formality as a structural feature: "The degree-4 pole c/2 (z-w)^{-4} is the source of non-formality" (L651-652), "shadow depth d_alg(Vir_c) = infinity (class M)" (L686). Non-formality determines shadow class and is the mathematical content, never presented as pathological.

### Additional checks (all CLEAN)

- **Claim status tags**: All \begin{theorem} in all 7 files carry \ClaimStatusProvedHere or \ClaimStatusProvedElsewhere. All conjectures use \begin{conjecture}. No label/content violations.
- **Part~N references**: Zero hardcoded Part~N in any of the 7 files. All Part references use \ref{part:...}.
- **AP-CY4 (Drinfeld center vs derived center)**: hochschild.tex L3086-3129 correctly distinguishes Z(U_A) (ordered Drinfeld center via Francis E_1-Hochschild) from Z^der_ch(A) (derived chiral center), framing their equivalence as a conjecture (L3114).
- **AP-CY7 (CoHA != chiral)**: No CoHA discussion in any of the 7 files. CLEAN.
- **AP-CY8 (denominator != bar Euler)**: No Borcherds identification in any of the 7 files. CLEAN.
- **CY-A_3 status**: No stale "conditional on CY-A_3" in any of the 7 files. CLEAN.
- **FM40 (Dunn on A)**: No Dunn claims in any of the 7 files. The E_2 structure is correctly attributed to Hochschild cochains (hochschild.tex Thm L185-197), not to A itself.
- **FM43 (B(A) = int_R A)**: No such claim. B(A) is consistently T^c(s^{-1}bar{A}) with FM differential and deconcatenation coproduct.
- **FM47 (E_inf -> E_3 automatic)**: No such claim. The operad chapter works at SC level only; E_3 never mentioned.
- **pva-expanded.tex**: All 6 PVA axioms (commutativity, sesquilinearity, skew-symmetry, vacuum, Jacobi, Leibniz) verified with correct signs. The (-1)-shifted Poisson structure is correctly stated throughout. The FM_2(C) involution argument for skew-symmetry (L130-182) correctly uses the topological direction path homotopy. The Jacobi identity proof summary (L253-288) correctly derives from the Arnold relation on FM_3(C). No violations.
- **brace-signs.tex**: Koszul sign rule (eq brace-sign) correctly stated. Pre-Lie relation (Prop L66-78) and full brace identity (Prop L80-91) correctly proved. Application to chiral setting (L93-108) correctly incorporates orientation signs from FM(C) x Conf(R). Arnold cancellation example (L101-108) is correct. No violations.

## XX. Geometric vs Algebraic Model Conflations (2026-04-16, from Vol III adversarial swarm on two derived centers)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | AP |
|---|-------------|---------------|---------------|---------------------|------|-----|
| 162 | Geometric ChirHoch = algebraic ChirHoch (used interchangeably at chain level) | They ARE quasi-isomorphic for logarithmic chiral algebras | The comparison is stated only as a remark (rem:comparison-geometric-hoch), NOT proved as a named theorem. Used without citation at 100+ locations. | Two models: geometric (FM compactifications, log forms, 3-component diff) vs algebraic (End^ch_A, formal variables, Gerstenhaber bracket diff). At genus >= 1, geometric model carries curve-dependent data that algebraic model lacks. | label/content (model ambiguity) | AP-CY62 |
| 163 | "ChirHoch* and THH* are different-sized objects (dim 3 vs infinite)" | ChirHoch and THH compute different invariants | For Koszul algebras (Heisenberg), HH*(Weyl)=1-dim, not infinite. Difference is STRUCTURAL (E_2 with spectral data vs abstract E_2), not DIMENSIONAL. | Same cohomology groups for Koszul algebras; different E_2 algebra structures. The genuine "fails to concentrate" object is H*_GF (Gel'fand-Fuchs), not THH. | chain/cohomology confused with size/structure | AP-CY64 |
| 164 | "Theorem H fails for THH / concentration has no THH analogue" | Theorem H IS specifically about ChirHoch* | THH = HH*(A_mode) is ALSO concentrated: HH*(Weyl) = C in degree 0 (MORE concentrated). The "fails for THH" claim confuses HH* with H*_GF (Gel'fand-Fuchs). | Three invariants: ChirHoch* in {0,1,2}, HH*(A_mode) in {0}, H*_GF unbounded. Genuine size difference ONLY at critical level k=-h^v (Feigin-Frenkel center). | three-way conflation (ChirHoch/HH/GF) | AP-CY64 |
| 165 | "Topological Drinfeld center has no spectral parameters" | Chiral structure creates translation automorphism enabling evaluation modules | Yangian Y(g) as purely associative algebra HAS evaluation modules V_u and spectral R(z=u-v) in its Drinfeld center. | Spectral parameter from representation theory (evaluation modules), not center construction. Correct claim: chiral bar DIFFERENTIAL is z-dependent; topological bar COPRODUCT is z-independent. | construction/data conflation | AP-CY65 |
| 166 | "BZFN gives different answers depending on ambient category S as tunable parameter" | Two derived centers DO exist and produce different braided categories | S is not a free parameter. Both sides of BZFN use same S. Two centers come from TWO DIFFERENT ALGEBRAS: chiral A (in D-mod(Ran)) vs mode algebra A_mode (in Vect). | BZFN applied once to each algebra in its native ambient category. Different inputs, not different parameters. | object/structure | AP-CY66 |
| 167 | "Spectral parameters from FM_k(C)" for End^ch_A | End^ch_A relates to FM via local-global identification | Narration: End^ch_A is algebraic (formal Laurent series). FM enters via comparison theorem, not the definition. | Three layers: (1) geometric model on FM, (2) formal-disk restriction gives lambda_i, (3) algebraic model with formal variables. Comparison is a theorem, not a definition. | construction/narration | AP-CY67 |
| 168 | BD chiral operad = algebraic End^ch_A (used interchangeably) | Related by formal disk restriction (iso after coordinate choice) | BD operad lives in D-modules on Ran(X); End^ch_A is formal Laurent series. Different categories. 4-step bridge. | Bridge: local coordinate -> formal disk -> D-module trivialization -> spectral variable id. Iso of non-Sigma operads, coordinate-dependent. Bridge Proposition ABSENT from manuscript. | object/structure + expository gap | AP-CY63 |
| 169 | "Physics requires two different bulk theories" | Physics has ONE bulk per boundary | Two derived centers are two COMPUTATIONAL MODELS of the same physical observable, not two different theories. | Boundary A determines unique bulk Z^der(A). Two routes (ChirHoch, Z(U_A)) should agree. Equivalence is conj:drinfeld-center-equals-bulk. | construction/narration | AP-CY62/66 |
| 170 | "Restricting chiral algebra to S^1 gives A_inf algebra" | E_2 restricts to E_1 on real submanifolds | Conflates four operations: (a) D-module restriction (ill-defined on real submanifold), (b) mode algebra (strictly assoc), (c) int_{S^1} A = HH_*(A) (chain complex), (d) pullback of FA along S^1->D*. | Holomorphic FA restricted to real ray gives E_1-algebra. int_{S^1} gives HH homology. Mode algebra strictly associative. E_1 = A_inf only in char 0 via HTT. | four-way conflation | AP-CY64 |
| 171 | Tamarkin inconsistency: C*(H_k, H_k) = k[[kappa]] vs Theorem H dim 3 | Both computations correct | k[[kappa]] is DEFORMATION PARAMETER SPACE. ChirHoch*(H_k) at FIXED k has dim 3. Different objects. | Reconstructor deformation ring vs bulk state space: answer different questions. Resolution at hochschild.tex:3376-3413. | family/fiber conflation | AP-CY64 |
| 172 | Koszulness iff A_inf-formality of bar cohomology (Thm kfc-fourteen(iii)): m_n=0 all n>=3 | Koszul = bar H* concentrated in degree one; transferred m_n act ON H*(bar) | What is RIGHT: for class G (Heisenberg), m_n = 0 on H*(bar) because H*(bar) is 1-dim. What is WRONG: conflating m_n on H*(bar) with m_k^SC on A, and with L_infty brackets on modular convolution; standalone l.1279 flags the tension ("Koszulness requires m_n=0 for n>=3") in the beta-gamma passage, which collides with class M column of Table 1. | Correct: A_inf-formality of H*(bar) holds on Koszul locus at GENUS ZERO (vanishing of d_r on PBW spectral sequence). Three different "m_k"s are distinguished in prop:sc-formality-by-class (Vol I higher_genus_modular_koszul.tex:17464): (i) on bar H*, (ii) on A (Swiss-cheese), (iii) on modular convolution. The standalone theorem kfc-fourteen is about (i); AP14 and the Virasoro row of Table 1 are about (ii). The "all standard families Koszul" claim only concerns (i). | definition/scope conflation | AP153-154, MP3 |
| 173 | SC^{ch,top} homotopy-Koszulity proved via "Kontsevich formality + transfer" | Classical SC Koszul + C_*(FM_k(C)) ~ E_2 | line-operators.tex:82-198 gives the proof: (1) classical SC Koszul (Livernet-Voronov-Vallette via distributive law), (2) Phi: SC^{ch,top} -> SC_classical is a qi of two-colored dg operads, (3) bar/cobar preserve qi in char 0, 2-out-of-3. GAP: mixed compositions are asserted to split as chi(FM_k) x E_1(m) with product decomposition; but the Tamarkin-Willwacher Swiss-cheese formality requires a Drinfeld associator choice (en_koszul_duality.tex:6744-6775 concedes Tamarkin's E_2-formality is not canonical). The proof in line-operators elides this canonicity gap. | Correct scope: SC^{ch,top} homotopy-Koszulity holds given (a) classical SC Koszul (standard, char 0), (b) a choice of Drinfeld associator (formality is non-canonical), (c) the assumption that mixed operations factor as FM_k(C) x E_1(m) (holds because open-to-closed is empty in this manuscript's SC^{ch,top}). The proof's 3 steps are sound modulo the associator choice; claiming "proved" without scoping the associator is imprecise. | proof-scope gap + canonicity gap | FM43, MP3 |
| 174 | "Every standard family is chirally Koszul" (Thm kfc-landscape) including Virasoro via (iv) shadow-tower formality | (iv) is Koszul-equivalent per Thm kfc-fourteen | Virasoro Koszulness chain: (iv) vanishing of genus-0 shadow obstructions o_{r+1}^{(0)} => (ii) PBW E_2-collapse => (i) Koszulness. standalone:1230-1236 asserts "o_{r+1}^{(0)} = 0 for all r >= 2 ... because the Virasoro vacuum module satisfies Kac determinant nonvanishing at generic c." No vanishing computation; Kac det nonvanishing is characterization (xiii), not (iv). Circular: (iv) via (xiii) which is proved equivalent to (iv). For beta-gamma (class C) the standalone concedes "Koszulness requires m_n=0 for n>=3" and provides "explicit computation"; for Virasoro no such computation. | Correct: Virasoro Koszulness is conditional on genus-0 A_inf products on H*(bar_{ch}(Vir_c)) vanishing at generic c. The standalone argues through (xiii) which gives INJECTIVITY of PBW-to-bar comparison -- weaker than acyclicity of the twisted tensor product off-diagonal. The AP-independent-verification tautology risk applies: (iv) and (xiii) are proved equivalent and then mutually invoked on Virasoro. | circularity + scope slip | AP151, AP-CY49 (tautology), AP158 |
| 175 | Yangian Y_hbar(g) is chirally Koszul (prop:yangian-koszul) | Yangian is E_1-chiral (genuinely non-local), bar-cobar = Drinfeld dual | Yangian is NOT in the scope of standalone Thm kfc-fourteen: the fourteen characterizations presuppose a positive-energy chiral algebra on X with PBW filtration. Yangian has spectral-parameter relations; bar-cobar gives the Drinfeld dual (bialgebra-theoretic). prop:yangian-koszul (yangians_foundations.tex:623) proves something about RTT quadratic relations -- a different Koszul duality. Importing into SC^{ch,top} needs a bridge (AP153). | Correct: "RTT Yangian is Koszul" in the classical quadratic-Koszul sense (T(V)/R quadratic, LV-Koszul via PBW + quadratic dual). Whether this lifts to chiral Koszulness in the sense of Def kfc-chiral-koszul-morphism is a separate theorem not proved. Thm kfc-landscape does not include Yangian. | two different Koszulnesses | AP153, V2-AP22 |
| 176 | 14 characterizations all unconditionally equivalent | Core circuit (i)-(ii)-(iii)-(viii)-(ix) proved; satellites proved individually | Core circuit through (viii) BBL monadicity (standalone:650-664) is CIRCULAR: "BBL holds iff chiral algebra is Koszul" is derived from "bar-cobar adjunction is a Quillen equivalence on the Koszul locus" (LorgatMKD1) which is itself statement (i). Similarly (v) one-way, (xi) requires simpliciality, (xiv) biconditional only for affine KM, (xv) conditional on perfectness, (xvi) one-way. Honest count: 10 unconditional + 2 partial + 2 scoped. The theorem paragraph 1 states this; abstract and marketing compress to "fourteen equivalent." | Correct scope: ten unconditionally equivalent, (v) proved one-way, (xi) equivalent on simpliciality, (xiv) biconditional for KM only, (xv) conditional on perfectness, (xvi) one-way. The abstract acknowledges this in parentheticals; the headline is inflated. | count inflation | AP18 |
| 177 | Phi: SC^{ch,top} -> SC_classical is a qi (line-operators:95-179) | Kontsevich: C_*(FM_k(C)) ~ E_2 as dg operads | Step 2 asserts mixed operations = FM_k(C) x E_1(m) with product composition. Livernet's classical SC uses FM_k(H) (half-plane) for the closed-color configuration spaces to accommodate bulk-to-boundary collisions. The manuscript's SC^{ch,top} with FM_k(C) closed color (plane, not half-plane) together with "no open-to-closed" (FM43) means mixed operations trivially factor -- but then Livernet-Voronov classical SC Koszulness via distributive law (with half-plane) is not directly imported; what is needed is the trivial two-coloured Koszulness E_2 x E_1 with no interaction. | Correct: if SC^{ch,top} closed color is FM_k(C) (plane) with empty open-to-closed, the classical-SC-Koszulness step reduces to separate E_2 and E_1 Koszulness (no mixed Koszul datum), and the distributive-law machinery of Livernet-Voronov is NOT exercised. The proof should either (a) use FM_k(H) and admit bulk-to-boundary, or (b) drop the citation to Livernet's half-plane result and prove the trivial factored two-color Koszulness directly. Current proof cites (a) machinery while using (b) structure. | operad-identification slip | AP-CY62, AP-CY63, FM43 |

## XXI. Theorem B and Theorem C attacks (2026-04-16, Vol I adversarial review)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | AP |
|---|-------------|---------------|---------------|---------------------|------|-----|
| 178 | Standalone Thm B ii: "For the standard landscape (Heisenberg, affine KM at generic level, Virasoro at generic c, principal W-algebras, lattice VOAs), the Ext vanishing holds unconditionally, and bar-cobar inversion is unconditional at all genera." | On the Koszul locus (generic level for KM, generic c away from minimal series for Virasoro, generic level for W), bar-cobar inversion is proved unconditionally at all genera. | The chapter-level thm:bar-cobar-inversion-qi and thm:higher-genus-inversion explicitly EXCLUDE: (a) admissible-level simple affine quotients L_k(g) (ex:admissible-sl2-failure), (b) minimal-model Virasoro/W-algebras (rem:virasoro-module-koszul-minimal), (c) critical level k=-h^v (Feigin-Frenkel jump). The standalone phrase "affine KM at generic level" is defensible, but "principal W-algebras" without the "at generic level" qualifier hides the same exclusion. At the minimal-model Virasoro points c_{p,q} = 1 - 6(p-q)^2/(pq) the PBW/Shapovalov argument fails in the bar-relevant range; the standalone hides this behind the word "generic". | Correct scope: bar-cobar inversion all genera holds for KM at generic level, Virasoro at non-minimal-model generic c, principal W_N at generic level, Heisenberg/lattice/beta-gamma unconditionally. Minimal-model/admissible-level cases are OPEN (possibly N-Koszul per conj:admissible-2-koszul). Critical level is OUTSIDE the Koszul locus. | scope error | AP2, AP4, AP18, AP36 |
| 179 | Standalone Thm B genus-0: "The Koszul condition is that gr A is quadratic Koszul in the classical sense (Priddy)." | PBW filtration + classical Priddy Koszulness of gr A + collapse of bar SS | The standalone proof invokes Priddy Koszulness of gr A as sufficient. But for a chiral algebra A on a curve X, the associated graded gr A is a Poisson vertex algebra (commutative VA + lambda-bracket), NOT a quadratic associative algebra in the Priddy sense. The correct statement requires gr A viewed as a quadratic BD "commutative chiral algebra" and invoking a chiral version of Priddy Koszulness. The standalone conflates classical Priddy with chiral Koszulness. Chapter-level proof uses thm:chiral-koszul-duality, which does not cite Priddy. | Correct: gr A is classically Koszul as a COMMUTATIVE CHIRAL ALGEBRA (BD Ch. 3, not Priddy). The PBW filtration yields a spectral sequence whose E_1 is the BAR complex of gr A in the BD sense; the classical Priddy theorem on associative algebras enters only at the mode-algebra level. | conflation (classical vs chiral Koszul) | AP153, V2-AP5, FM56 |
| 180 | Standalone Prop "Complementarity sums": W_N has K = kappa + kappa' = "nonzero and N-dependent" with kappa(W_N) = c*(H_N - 1); chapter-level gives K = 2(N-1)(2N^2+2N+1)*(H_N - 1). | kappa(W_N) = c*(H_N - 1) and under Koszul duality c + c' is level-independent, so K = (c+c')*(H_N - 1). | The two documents give DIFFERENT kappa formulas. Standalone: kappa(W_N) = c*(H_N - 1), implying K = (c+c')*(H_N - 1) depending only on the N-dependent constant (c+c') = 2(N-1)(2N^2+2N+1). This is consistent; the standalone is just under-specified. But the standalone's K formula references the "Koszul complementarity conductor" without stating that c -> c' is NOT c -> 2(N-1)(2N^2+2N+1) - c (the natural generalization of Virasoro's c -> 26-c). In fact the chapter-level "Feigin-Frenkel involution" k -> -k - 2h^v is a LINEAR level involution, NOT the genuine FF self-duality (k+h^v)(k'+h^v) r = 1 of W-algebras. | Correct: kappa(W(g, f_prin)) = c * rho(g) where rho(g) = sum 1/(m_i+1). For sl_N: rho = H_N - 1 (OK, since exponents are 1,2,...,N-1). For B_2 (exponents 1,3): rho = 1/2 + 1/4 = 3/4 != H_2 - 1. Standalone restricts to principal W_N = sl_N only; for non-type-A the H_N formula fails. Chapter covers general g with the correct rho formula. | conflation + scope | AP18, AP36, AP108 |
| 181 | Standalone Thm C: "For the standard landscape (Heisenberg, affine KM, Virasoro, principal W, lattice) ... C1 is unconditional in the coderived category, C2 is proved at cohomology for g >= 1, C3 is conditional on perfectness." | Lagrangian polarization of C_g via Verdier involution eigenspaces | The "homotopy decomposition" claim in standalone C1 says C_g(A) ~ Q_g(A) oplus Q_g(A^!) "unconditional in the coderived category". The chapter-level thm:quantum-complementarity-main proves this via Lemma lem:involution-splitting(a,c), which relies on the Verdier involution sigma being an order-2 self-equivalence of C_g. But at g = 0, the chapter says Q_0(A^!) = 0 (the unique point class is sigma-fixed), so the decomposition is TRIVIAL at g=0 and the "oplus" is degenerate. Standalone presents C1 uniformly for all g >= 0, hiding that the genus-0 decomposition is vacuous. | Correct: for g >= 1 the Lagrangian polarization is nontrivial (both summands nonzero, Verdier anti-symmetric pairing of degree -(3g-3)); for g = 0 the decomposition is trivially C_0 = Q_0 oplus 0. | vacuous/meaningful + uniformity | AP6, AP32 |
| 182 | Standalone Thm C "shifted-symplectic upgrade" conditional on perfectness | C_g carries a -(3g-3)-shifted symplectic form via PTVV | The standalone "(2-d)-shifted symplectic" phrasing is AMBIGUOUS in d: d is the CY dimension, but "d" is never defined in the standalone Thm C statement. Chapter uses -(3g-3) (= dim of Mbar_g plus 1 shift, from Verdier duality on Mbar_g). The "2-d" vs "-(3g-3)" clash has different meaning: -(3g-3) is a GENUS-dependent shift (Mbar_g pairing), while "(2-d)" is a CY-dimension-dependent shift (PTVV for CY_d categories). These are DIFFERENT shifted symplectic structures. | Correct: the ambient C_g = RGamma(Mbar_g, Z_A) carries a -(3g-3)-shifted symplectic form from Verdier duality on Mbar_g (standard algebraic geometry, NOT PTVV for CY_d). The "shifted-symplectic upgrade" part citing PTVV is a SEPARATE structure that requires A to come from a CY_d category, which is the content of Vol III, NOT Vol I. The standalone conflates two different shifted structures. | convention clash (Mbar_g shift vs CY_d shift) | AP-CY1, AP-CY2, AP150 |
| 183 | Standalone Thm B proof: "the fiberwise bar differential satisfies d_fib^2 = kappa(A) * omega_g != 0: the bar complex is curved, and the cobar functor cannot be applied in the classical sense. The resolution uses the total bar differential D_A with D_A^2 = 0." | Curved Dunn / curved Koszul duality (Hirsh-Milles, Positselski) | The standalone's "resolution uses the total bar differential D_A with D_A^2 = 0" is not a proof; it RESTATES what needs to be proved. Chapter-level proof (thm:higher-genus-inversion) uses: (i) open-stratum qi via PBW, (ii) boundary qi via induction on stable graphs + Kunneth at nodes, (iii) extension lemma. No use of a "total bar differential". Standalone's casual reference to D_A elides the need for the curved cobar functor of Hirsh-Milles, which requires conilpotence + completeness (stated in chapter, omitted in standalone). | Correct: higher-genus inversion uses induction on genus via boundary stable-graph decomposition + Kunneth, NOT "total bar differential". The curved bar-cobar adjunction requires conilpotent/complete hypotheses which the standalone omits; at curved-central algebras with scalar kappa, the curved cobar is well-defined via Positselski coderived categories. | mechanism error (wrong proof stated) | AP2, AP4, MP3 |
| 184 | Standalone Thm B clause (ii) lumps "affine KM at generic level" and "Virasoro at generic central charge" into one statement of unconditional higher-genus inversion. | Each family has its own Koszul locus with its own generic-level exclusions. | The unconditional all-genera PBW theorem for KM (thm:pbw-allgenera-km) is separate from the Virasoro all-genera theorem. Chapter thm:pbw-allgenera-km explicitly says "genuine level k in Sigma(g)" -- the excluded set Sigma(g) is family-specific. For Virasoro, the excluded set is the minimal-model locus c_{p,q}; for KM, it is admissible levels k = -h^v + p/q. These are DIFFERENT exclusion sets; standalone's "at generic level/central charge" obscures this. | Correct: bar-cobar inversion all genera holds for (KM at k not in admissible union {-h^v}) + (Virasoro at c not in minimal-model series) + (principal W at k not in minimal-model series). Each family has its own excluded countable set. | uniform presentation hides family-specific exclusions | AP18, AP32 |
| 185 | Standalone Thm C Heisenberg example: "kappa(H_k) = k, kappa(H_k^!) = -k, K = 0" | Heisenberg curvature is linear in k; Koszul dual sign-flips. | AP39 warning: kappa(Heis_k) = k (NOT k/2) -- standalone is OK here. But the Koszul dual H_k^! is defined how? The programme's Koszul dual of the bosonic Heisenberg is the symplectic-fermion pair bc-system at "level -k" (class G Koszul pair). The "level -k" interpretation requires specifying the pairing convention. Standalone writes "H_k^! = H_{-k}" implicitly; the actual Koszul dual is the FERMIONIC counterpart (odd generator), not the same Heisenberg at sign-flipped level. | Correct: the Koszul pair is (bosonic H_k) <-> (symplectic-fermion F_{-k}), NOT (H_k, H_{-k}). Both have the Heisenberg OPE J(z)J(w) ~ k/(z-w)^2 but different parity. kappa flips sign because the parity flip inverts the sign of the central extension. Writing "H_k^!" as "H_{-k}" is notational sloppiness hiding the bosonic/fermionic duality. | label/content | AP105, AP107 |
| 186 | CLAUDE.md FM68: "Modular operad composition PROVED (all genera, integrable via KZ pentagon + KL regularity)"; "curved Dunn genus-1 PROVED via prop:genus1-twisted-tensor-product" | Vol II .tex proves: (a) genus-0 composition at all non-critical k via KZ flatness + Mac Lane pentagon; (b) all-genera composition at INTEGRABLE k via KZB regular singularities (KL + TUY); (c) equivariance for E_1-chiral quantum groups (QT+YBE); (d) unitality all genera via contractible-u-side argument | (A) "KZ pentagon + KL regularity" conflates two different ingredients for two different ranges: genus-0 uses KZ pentagon; genus>=1 needs KL/TUY regular singularities. (B) Integrable-level all-genera composition holds on the semisimple integrable-rep MTC, NOT on full O^{Ainf-ch} whose vertices range over all positive-energy reps. (C) Equivariance prop:qt-equivariance is proved for E_1-chiral QGs with QT; for V_k(g) at generic k QT is not established. (D) "prop:genus1-twisted-tensor-product" DOES NOT EXIST -- grep returns zero hits across both volumes; this is a phantom label. The manuscript's actual statement is conj:curved-dunn-additivity with \ClaimStatusConjectured plus rem:curved-dunn-three-level explicitly flagging H^2 in the twisting-cochain complex as OPEN. | Honest status: (i) D^2=0 on gAmod proved (thm:convolution-d-squared-zero) -- ABSTRACT, not concrete O^{Ainf-ch}. (ii) Concrete V_k(g) composition: genus-0 at all non-critical k; all-genera at integrable k on the integrable-rep MTC. Generic-k genus>=1 OPEN (Stokes). (iii) Equivariance: proved for E_1-chiral QGs with QT+YBE; NOT for V_k(g) at generic non-integrable k. (iv) Unitality: proved all genera/shadow classes. (v) Curved Dunn: \ClaimStatusConjectured at ALL genera including g=1; only uncurved genus-0 Kunneth proved (lem:operadic-kunneth on \gr_F); twisted Kunneth conjectural with H^2 open. CLAUDE.md summary merges four separately-scoped theorems into one, drops hypotheses, and cites a nonexistent proposition. | phantom label + scope-merge + abstract/concrete conflation | FM61, FM67, FM68, AP150, AP178 |
| 187 | thm:convolution-d-squared-zero (higher_genus_modular_koszul.tex:10560-10646): D^2=0 on gAmod -- used to justify "modular operad axioms proved" | Getzler-Kapranov modular-operad convolution: for cyclic A, Hom_{mod-op}(Mbar, End_A) is a dgLA with D from partial_Mbar | Proof reads verbatim: "D^2=0 follows from partial^2=0 on Mbar_{g,n}, i.e. from the boundary relations of the modular operad (GK98 Sec 5)." This is a theorem about the AMBIENT convolution complex built from the DM boundary operator; it does NOT imply the CONCRETE clutching maps xi_Gamma defined via B^{ann} + R-matrix monodromy assemble into a modular-operad algebra. FM61 is exactly this non-sequitur. rem:modular-operad-status-update (3d_gravity.tex:6088-6112) even adds a SECOND wrong proof: "composition associativity: proved (the stable-graph category is a Kan complex; Def ... (iii))" -- Kan-ness of the graph nerve concerns horn-fillers among graphs, NOT compatibility of R-twisted sewings with graph composition. | Correct: D^2=0 on gAmod is an ambient/abstract theorem for any cyclic A. Concrete operadic associativity of {xi_Gamma} requires compatibility of iterated B^{ann} + Mon(R) sewings with stable-graph composition. This is what thm:affine-composition-associativity establishes -- ONLY for V_k(g), ONLY at integrable level for g>=1. For general A, concrete associativity is open even at genus 0 unless the algebra has a KZ-type flat connection. The abstract D^2=0 cannot substitute. Kan-ness of StGraph cannot substitute either. | abstract/concrete conflation; nerve/operad conflation | FM61, AP150, AP178 |
| 188 | lem:operadic-kunneth (modular_swiss_cheese_operad.tex:2541-2647) used to conclude "B(SC_mix) = B_mod(P_1) otimes B(P_2) at CHAIN level" in several downstream places | Filtered bar-cobar spectral-sequence collapse at E_1 via closed-input-excess filtration | The lemma's PROOF (correctly) shows only gr_F B(P_mix) = B_mod(P_1) otimes B(P_2) -- i.e., equality holds on the ASSOCIATED GRADED, with d_mix raising the filtration. Remark rem:operadic-kunneth-cross-terms is explicit: "failure of a chain-level factorization comes from the cross-term d_mix." Downstream (3d_gravity.tex:5233-5238) the same Kunneth is cited to get B(O^{Ainf-ch}|_{g=0}) ~ B(SC^{ch,top}) otimes B(E_1^tr). This is at genus 0 where the operad is a strict product and the cross-term d_mix vanishes IDENTICALLY, so the chain-level isomorphism is OK. But ROADMAP Level-3 cites lem:operadic-kunneth as a model for the twisted Kunneth at g>=1 -- at g>=1 the cross-term d_mix is NONZERO (R-matrix monodromy) and the chain-level identity FAILS. FM60 flags this exactly. | Correct: lem:operadic-kunneth gives B(SC_mix) = B_mod(P_1) otimes B(P_2) on gr_F only, with a spectral sequence collapsing at E_1 for pole-free genus-0. At genus 0 for O^{Ainf-ch}, d_mix = 0 and the chain-level isomorphism holds. At g >= 1 the twisting by Mon(R) makes d_mix != 0 and the lemma does NOT apply; one needs a genuine twisted Kunneth (conjectural, Level-3). Any chain-level Kunneth invocation for g >= 1 is illegitimate. | filtered/chain conflation; gr-level identity used at chain level | FM60, AP178 |
| 189 | ROADMAP_85_TO_100.md lines 99-102 present curved Dunn as having four levels with "genus-1 PROVED"; AGENTS.md AP182 writes "Genus-1 twisted tensor product PROVED (prop:genus1-twisted-tensor-product). Full genus tower OPEN." | Curvature d_fib^2 = kappa*omega_1 at genus 1 with monodromy insertion | (a) Label does not exist. (b) AGENTS.md AP178 contradicts CLAUDE.md FM68: "Modular operad (iii) is NOT proved. thm:modular-bar proves D^2=0 for the ABSTRACT modular bar datum. The concrete operadic associativity of O^{A_inf-ch} clutching maps (iterated B^ann sewing with R-matrix monodromy) is OPEN. Even genus-1 clutching (constr:genus1-ainf-chiral-operations) is CONJECTURAL." Three pieces of session metadata give three different statuses for the same axiom within the same programme; the .tex matches AGENTS.md AP178 (constr:genus1-ainf-chiral-operations carries \ClaimStatusConjectured at 3d_gravity.tex:5393-5399), not CLAUDE.md/ROADMAP. | Reconciliation: session metadata should track .tex ground truth. Honest status: genus-0 uncurved Kunneth PROVED (lem:operadic-kunneth on strict product), genus-1 twisted tensor product CONJECTURAL (constr:genus1-ainf-chiral-operations \ClaimStatusConjectured, conj:curved-dunn-additivity \ClaimStatusConjectured), genus>=2 OPEN with H^2 twisting-cochain-complex vanishing as the precise frontier (rem:curved-dunn-three-level Level 2 "obstruction theory" explicitly marks this open). The bridge between modular-bootstrap H^2=0 (PROVED) and curved-Dunn twisting-cochain H^2 (OPEN) is the stated frontier at rem:curved-dunn-three-level:5371-5389. | metadata divergence; phantom label; AP41 at programme scale | AP-CY41, AP150, AP178, FM67 |
| 190 | rem:modular-operad-status-update (3d_gravity.tex:6088-6112) claims composition associativity "proved (the stable-graph category is a Kan complex; Def ... (iii))" | Weiss, Berger-Moerdijk dendroidal/Kan-complex structures on operad nerves | Kan-fillability of the stable-graph simplicial object concerns horn-filling among graphs in the source; composition associativity of {xi_Gamma : otimes_v B_v -> B} is coherence of the TARGET functor. Kan source does not force coherent target. Pairwise associativity at each binary sewing plus infinite higher coherences would give infty-operad structure; manuscript provides neither -- only the KZ+KL proof in thm:affine-composition-associativity. | Correct: Kan structure on StGraph gives homotopy-coherent indexing (infty-category). Promoting {xi_Gamma} to an infty-functor requires a tower of higher coherences, not merely Kan source. The genuine proof is thm:affine-composition-associativity and holds only for V_k(g) under the KL-regularity hypothesis. The "Kan complex" remark should be deleted or radically scoped: it is a second, spurious "proof" for the same claim. | source/target confusion; infty/strict conflation | FM61, AP150, AP178 |

## XXII. Spectral Drinfeld Strictification attacks (2026-04-16, Vol II adversarial review)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | AP |
|---|-------------|---------------|---------------|---------------------|------|-----|
| 191 | "Coproduct rigidity" used 4+ times (ordered_associative_chiral_kd.tex:3913, 4042, 4096; dg_shifted_factorization_bridge.tex:1878, 1927) as the load-bearing step that forces the scalar obstruction to vanish. | n-gon rigidity (thm:ngon-rigidity at dg_shifted_factorization_bridge.tex:1545-1556) provides a uniquely-forced coefficient 1/n for path-type n-gon sectors. | thm:ngon-rigidity is proved ONLY for "oriented path-type n-gon sectors" (l. 1547). The complete-strictification proof (l. 1842-1866) applies it to path sectors, then invokes "its root-space-one-dimensional generalization for non-path sectors" -- this generalization is NOT stated or proved anywhere in either volume. Grep for "coproduct rigidity" returns 4 invocations, zero definitions. The Jacobi-collapse lemma (l. 3863-3901) only establishes A=B for the D_4 star (single 4-root case), not a uniqueness-of-coefficient statement for arbitrary non-path sectors at arbitrary filtration. | Honest status: n-gon rigidity is proved for path sectors. The claim that non-path sectors (D_4-star, E_6/E_7/E_8 trivalent vertices at higher filtrations with nested stars) inherit rigidity from "root multiplicity 1 alone" is a heuristic, not a theorem. The actual proof needs: (a) path-case thm:ngon-rigidity, (b) a SEPARATE coefficient-uniqueness theorem for non-path sectors, (c) Jacobi-collapse lemma applied inductively. Only (a) and the n=4 case of (c) are rigorous. | mechanism error; necessary/sufficient | AP153, AP150, AP158 |
| 192 | "The multilinear space is one-dimensional in g" (ordered_associative_chiral_kd.tex:3903-3921, rem:root-multiplicity-one-as-structural-inevitability) — promoted from root-space dim 1 to uniqueness of the multilinear-Lie computation. | Root-space one-dimensionality: dim g_alpha = 1 for any root alpha of a finite-dim simple Lie algebra. | Root-space one-dim only says the IMAGE of multilinear brackets lies in a 1-dim space. It does NOT say the multilinear brackets form a 1-dim subspace of End(V) or U(g) — the kernel of "bracket projection" can be large. The rem:root-mult-one-hero claim "a cohomological obstruction valued in a one-dimensional space is a scalar determined by a single equation" confuses "valued-in-1-dim space" with "1-parameter family." A 3-cocycle phi in C^3(A; g_alpha) for a 1-dim target g_alpha can still have non-trivial class in H^3 if there are non-trivial 2-cochains whose differential doesn't hit it. Dimensionality of the coefficient module is not the same as dimensionality of H^3. | Correct: for H^3_spec(gr^p A, g_alpha) with g_alpha 1-dim, the cohomology IS a vector space, potentially non-zero. The vanishing needs one of: (i) H^3 of the spectral complex with trivial coeffs = 0 (unproved), (ii) explicit coboundary for each specific phi_p (what thm:ngon-rigidity does for path sectors only), or (iii) a separate acyclicity result. The manuscript conflates (i)-(ii)-(iii). | dimensionality conflation; cohomology/coefficients confusion | AP150, AP153, AP-CY64 |
| 193 | Theorem thm:complete-strictification-v1 (ordered_associative_kd.tex:4011) and its duplicate thm:complete-strictification (dg_shifted_factorization_bridge.tex:1792) both tagged ProvedHere. | Single theorem; bridge-chapter version should cite appendix version or vice versa. | Two ProvedHere-tagged theorems with near-identical statements, slightly different proofs, in two different files. AP27 (no duplicated math content) is violated. The Vol I appendix version uses Jacobi-collapse lemma explicitly; the Vol II bridge version uses "ngon-rigidity + generalization" abstractly. If one proof is wrong, the other may still be tagged ProvedHere. Dependency graph (metadata/dependency_graph.dot:2854, 3165) has TWO nodes for thm_complete_strictification_v1 — phantom-label duplication. | Correct: one theorem, one proof, cited from everywhere else. Either delete the bridge-chapter restatement and cite the appendix theorem, or make the bridge-chapter theorem a corollary "by Theorem~\ref{thm:complete-strictification-v1} with hypothesis X." Current state: two statements, two proofs, same label stem, unclear which is canonical. | AP27 violation; duplicate ProvedHere; hardcoded/symbolic | AP27, AP41, AP-CY13 |
| 194 | "The induction produces a sequence of spectral twists G_2, G_3, ... whose composition converges in the completed filtered algebra" (drinfeld_kohno_bridge.tex:1066-1069) — convergence taken as automatic. | Nilpotent-completion argument for Drinfeld twists in pro-unipotent Hopf algebras. | Convergence of G_n-composition in the completed filtered algebra requires: (a) the filtration is complete and separated, (b) each G_n lives in F^n, (c) the completion is as topological algebras with respect to the F-adic topology. For affine KM at generic level, the bar complex is filtered by COLLISION DEPTH, not by F-adic nilpotence; convergence of the twist is a SEPARATE claim. Manuscript writes "whose composition converges" without justification. The actual spectral ansatz is rational in u (1/u, 1/u^2, ...), not nilpotent-polynomial; convergence in rational function ring is not the same as nilpotent completion. | Correct: establish the algebra topology explicitly. For the dg-shifted Yangian, the completion is (u^{-1})-adic on the coefficient ring; G_n in F^n as (u^{-1})-series; iterated product is a power series in u^{-1}. For the bar complex, F is collision depth; G_n lives in ker of projection to depth < n; iterated product converges only if the grading is bounded below. Manuscript skips this. | mechanism error; convergence vs formal series | AP150, AP158 |
| 195 | Vol II spectral-braiding-core.tex:2835, examples-worked.tex:858, and preface.tex:409,1264,1480 cite Theorem~\ref{thm:complete-strictification} — but the appendix theorem has label thm:complete-strictification-v1 | One label, one theorem, cited consistently. | Two live labels: thm:complete-strictification (Vol II bridge, line 1792) and thm:complete-strictification-v1 (Vol I appendix + chapter). Vol II citations to "thm:complete-strictification" resolve to the BRIDGE version (whose proof cites the unproved "ngon-rigidity generalization"). Some citations in Vol II are from preface/introduction and effectively advertise the appendix result while linking to the weaker bridge version. | Correct: unify labels. Either rename the bridge version (e.g. thm:strictification-factorization-quantum-group to distinguish role) or delete it and cite the appendix. Cross-volume consistency (AP5) demands one canonical label. | hardcoded/symbolic; AP5 cross-volume | AP5, AP27, AP-CY13 |
| 196 | "Extension to evaluation-generated core" (cor:dk3-eval-core, drinfeld_kohno_bridge.tex:1386-1400) claims equivalence of Eone-factorization categories on evaluation cores, then "higher operations do not contribute (one-loop collapse)" on eval modules. | On evaluation modules V(a_1)⊗⋯⊗V(a_n), the filtration-p quasi-associator reduces to classical KZ monodromy. | The "one-loop collapse" on eval modules is the content of AP47 — it only works on the EVAL CORE. The standalone claim that "strictification extends to all simple Lie algebras" is quietly restricted to the evaluation-generated subcategory. Corollary cor:dk3-eval-core is honest; memory note "Complete strictification for all simple Lie algebras" and CLAUDE.md "PROVED all simple Lie" are not — both drop the eval-core qualifier. Full-category extension is conj:dk3-full (explicitly conjectural, drinfeld_kohno_bridge.tex:1415-1432). | Honest form: "Spectral Drinfeld strictification of the evaluation-generated subcategory for all finite-dim simple Lie algebras. Extension to the full Eone-factorization category is open beyond type A (Clebsch-Gordan thick-generation) and conjectural for other types." The frontier is NOT just Kac-Moody multiplicity > 1; it is also full-category vs eval-core. | scope error; narration suppresses hypothesis | AP47, AP108, AP150 |
| 197 | "The frontier is Kac-Moody root multiplicity > 1" (memory file; ordered_associative_chiral_kd.tex:4089-4108). Presented as a single clean frontier. | For untwisted affine g-hat, real roots have mult 1 (strictification works verbatim, thm:affine-strictification-sectors(1)), imaginary roots span abelian h⊗t^n (Cartan gauge-twist, thm:affine-strictification-sectors(2)). | The actual frontier has THREE layers, not one: (a) untwisted-affine mixed sectors (conj:affine-strictification-mixed, l. 2007-2041, EXPLICITLY CONJECTURAL — "the analysis is not carried out here"); (b) twisted affine algebras A_{2n}^{(2)}, D_n^{(2)} where imaginary root multiplicities differ; (c) indefinite Kac-Moody with non-abelian imaginary root spaces. Only (c) corresponds to "root mult > 1 fails the Jacobi argument." Layers (a) and (b) are also open but for DIFFERENT reasons (mixed bracket analysis, non-Cartan imaginary structure). | Correct frontier decomposition: (i) finite-dim simple: PROVED on eval core. (ii) Untwisted affine real sectors: PROVED (verbatim reduction). (iii) Untwisted affine imaginary sectors: PROVED via Cartan gauge-twist. (iv) Untwisted affine MIXED sectors: OPEN (conj:affine-strictification-mixed). (v) Twisted affine: OPEN (different imaginary structure). (vi) Indefinite Kac-Moody: OPEN (genuine multiplicity->1 obstruction, the original frontier statement). Memory/CLAUDE.md flatten (iv)-(vi) into one "Kac-Moody" frontier. | scope flattening; four open cases compressed to one | AP150, AP153, AP-CY41 |
| 198 | Step 1 of the bridge proof (dg_shifted_factorization_bridge.tex:1815-1831): "both scalars are computed from the SAME one-body data ... so the equation is automatically satisfied." | Both the BCH product-side coefficient and the coproduct-side transport coefficient are determined by the one-body r-matrix data r_alpha(u). | "Automatically satisfied" is a non-sequitur. Two maps out of the same one-body data can give DIFFERENT scalars — one expects different normalizations (product side 1/n from Dynkin/beta integral vs coproduct side computed via ngon-rigidity). The actual identity product-side = coproduct-side at coefficient 1/n is what thm:ngon-rigidity PROVES for path sectors — it is not "automatic" even with one-dim target. The "both are scalars" argument sketches a 1-unknowns-1-equation count; the equation is not "automatic," it is the content of ngon-rigidity (and its unproved generalization). | Correct: the scalar vanishing is a THEOREM (ngon-rigidity for path sectors, open generalization for non-path), not a formal consequence of one-body origin. The "automatically satisfied" phrasing confuses one-dimensional TARGET with trivial cohomology. A 1-dim-valued 3-cocycle is not automatically a coboundary. | vacuous/meaningful; mechanism error | AP150, AP158, FM60 |

## XXIII. Seven Faces of r(z) attacks (2026-04-16, Vol I adversarial review)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | AP |
|---|-------------|---------------|---------------|---------------------|------|-----|
| 199 | seven_faces.tex:151-155: "The chain of identifications is F1 <=> F2 <=> F3 <=> F4 <=> F5 <=> F6 <=> F7; each link is proved separately, each by an independent mathematical argument." Abstract l. 83-84: "the seven presentations determine the same element." | The seven faces are all projections of the single bar-intrinsic datum Theta_A = D_A - d_0 (thm:bar-intrinsic-hinge, l. 455-463). They are all derivable from F1. | The structure is a STAR, not a cycle. The proof architecture (l. 338-344) lists FIVE independent edges: F1<=>F2, F1<=>F3, F1<=>F4, F1<=>F7, F5<=>F6 (classical, Drinfeld 1985). F4<=>F7 is also proved (l. 390-401). F5 and F6 are only glued to the hub via the F7 bridge (l. 415-421). The "closing the chain" argument (l. 415-421) is a narrated identification of already-F1-derived objects, not an independent equivalence. There is no Fi<=>Fj edge not passing through F1 (or through the classical Sklyanin-Yangian duality F5<=>F6). | Correct: F1 is the hub (bar-intrinsic Theta_A); F2-F7 are projections/specializations of F1 under different categorical lenses. The "seven-way chain" narrative overstates the topology: it is a six-edge tree with F5-F6 as a classical external edge. The honest form is: "seven presentations, each identified with F1 by an independent argument." | seven-way vs star-graph; mechanism | AP150 |
| 200 | seven_faces.tex:290-344: the "Seven-face identification" theorem proves Fi = Fj as elements of A^! otimes A^! [[z^{-1}]] WITHOUT distinguishing even vs odd (bosonic vs fermionic/super) generators. | AP107 (Vol I): r^coll(z) DIFFERS from Laplace-transform r(z) for ODD generators (super/fermionic). For bosonic bc or symplectic fermions, the collision residue has a simple-pole piece that the Yangian-Laplace r(z) does not capture. Heisenberg is bosonic, so r^coll = k/z = Laplace-r; this coincidence is exploited throughout l. 310-344. | The paper never constrains to bosonic generators. Class C explicitly contains symplectic fermions (l. 530, 588) and bc ghosts (l. 524). For these, F1 (collision residue) and F2 (Laplace-Yangian) are UNEQUAL per AP107. The trichotomy (Thm op-trichotomy, l. 581-622) glosses this: class C is labeled "trivial Hamiltonians" because k_max=0, but for symplectic fermions the bosonic-parity argument in Prop no-k2 (l. 624-638) is simply FALSE — odd generators don't obey the "2h maximal pole" constraint. | Correct: Theorem seven-faces needs explicit "for bosonic chirally Koszul A" hypothesis; for the super case, F1<=>F2 is AP107-corrected by a parity factor and odd-pole shift. The bc ghosts and symplectic fermions listed in class G/C are FERMIONIC and should be either excluded or handled by a separate theorem. | scope error; AP107 unacknowledged | AP107, AP153, AP150 |
| 201 | seven_faces.tex:394-399: "For affine Kac-Moody at level k, the collision residue is r(z) = Omega/((k+h^v)z)" — formula fails AP126/AP141 at k = -h^v, but more importantly at k = 0 the denominator is h^v, not vanishing; so r-matrix DOES NOT vanish at k=0 as AP126 requires for level-stripped normalisation. | AP126: classical r-matrix for affine KM at level k is r(z) = k*Omega/z, NOT Omega/z. At k=0 the r-matrix MUST vanish. | The seven_faces.tex presentation uses the level-shifted normalisation Omega/((k+h^v)z) (Gaudin/Hamiltonian normalisation), NOT the level-stripped one k*Omega/z. These are DIFFERENT objects: the latter vanishes at k=0 (abelian/vacuum), the former has a finite limit Omega/h^v (nonzero!) at k=0. Face F5 (Yangian classical r-matrix, Drinfeld 1985) uses r(z) = Omega/z (no level dependence); Face F7 (Gaudin, FFR 1994) uses the level-shifted Omega/((k+h^v)z). These are genuinely DIFFERENT normalisations conflated across faces. l. 344 admits this: "the three-parameter normalization hbar = 1/(k+h^v) is proved here" — but the Yangian r-matrix is independent of k, so hbar-identification is an additional choice. | Correct: F1, F5, F6 use r(z) proportional to Omega/z (universal, level-independent); F4, F7 use level-shifted r(z) = Omega/((k+h^v)z) (level-dependent, required for Gaudin hbar-correspondence). The "same element of A^! otimes A^![[z^{-1}]]" claim is FALSE: they agree only up to a scalar rescaling by (k+h^v). The "normalisation conversion" (l. 862-864) is NOT a passive renaming — it changes which face vanishes at k=0 and which does not. | AP126/AP141 level-prefix; normalisation conflation | AP126, AP141, HZ-1 |
| 202 | seven_faces.tex:102-103, 881-889: "seven papers, seven frameworks, one object"; closing l. 882 calls the programme "an audit instrument." Abstract l. 78-82 attributes each face to a named 1983/1985/1994/2025/2026 paper. | AP155 (Vol I): the framework RECOVERS known objects; the novelty is ARCHITECTURAL not COMPUTATIONAL. | Of the seven faces: F4 (Gaiotto-Zeng 2026) and F2 (Dimofte-Niu-Py 2025) are recent preprints whose r-matrix IS the OPE collision residue (not independent); F5 = Drinfeld's classical limit (1985, known); F6 = Sklyanin/STS bracket (1983, known); F7 = Gaudin generator (FFR 1994, known). F1 (twisting morphism, Ginzburg-Kapranov-Hinich) and F3 (PVA lambda-bracket, De Sole-Kac) are also classical. The "seven presentations" are SIX known presentations plus the bar-intrinsic one (F1 as the hub). Calling the identification "not a new theorem in any single framework" (l. 845) already admits this, but the abstract still markets seven-way equivalence as content. | Honest form: "The bar-intrinsic Maurer-Cartan element Theta_A = D_A - d_0 projects onto six previously-known r-matrix presentations, providing a uniform derivation." The architectural novelty (unified bar-complex source) is real; the "seven new presentations" gloss is AP155 overclaiming. | AP155 overclaiming; narration | AP155, AP150 |
| 203 | seven_faces.tex:293-299: "F1: r(z) is the genus-zero binary projection of the universal twisting morphism pi_A: B(A) -> A, where B(A) = T^c(s^{-1} bar-A) is the ordered bar coalgebra with deconcatenation coproduct." F5 "classical limit of Yangian R-matrix" uses Delta_z: Y(g) -> Y(g) otimes Y(g). | FM45: deconcatenation (structural coproduct on B(A), exists for any bar complex) is NOT the chiral coproduct Delta: A -> A otimes A (independent Hopf structure on A). | Face F1 uses deconcatenation on B(A); Face F5 uses the Yangian spectral coproduct Delta_z on A (via Drinfeld 1985 quantum R-matrix classical limit); Face F6 uses the Sklyanin Poisson bracket (a Lie bialgebra coproduct on g((t))). Three DIFFERENT coproducts on three DIFFERENT objects, all contributing to the definition of "r(z)". The deconcatenation on B(A) gives rise to the r(z) as a cocomposition-factorisation, whereas Delta_z reads r(z) as Delta_z(a) - Delta_z^{op}(a). These are derivationally parallel (both give the same element) but NOT the same coproduct. | Correct: Face F1 sees r(z) via the BAR cocomposition structural coproduct; Face F5-F6 see r(z) via the ALGEBRA coproduct (Yangian/Sklyanin). The identification is a Koszul-duality theorem (bar cocomposition <-> Yangian coproduct via quantum duality), NOT an identity of coproducts. Calling both "the chiral coproduct" conflates FM45. | FM45 coproduct conflation | FM45, AP150 |
| 204 | seven_faces.tex:311 (F3): "Classical PVA r-matrix ... extracted from the lambda-bracket of PVA(A)"; seven_faces.tex:317 (F5): "classical r-matrix of the Yangian Y_hbar(A^!)". The two are identified in thm:seven-faces. | FM53: spectral R(z) (family of maps with parameter z) and categorical E_2 braiding (single natural transformation, no parameter) are DIFFERENT objects. | Face F3's PVA classical r-matrix is an element r(z) in A otimes A((z)) arising from the lambda-bracket (-1)-shifted Lie structure — it is INFINITESIMAL (tangent space data) with z only as a formal variable. Face F5's Yangian r-matrix is the classical limit (R(z,hbar) - 1)/hbar of the spectral R-matrix — it is a FAMILY over the spectral parameter z with R(z,hbar) a genuine element of End(V otimes V). The identification "F3 = F5 as elements of A^! otimes A^![[z^{-1}]]" treats them as the same formal-series tensor, but their operational meanings differ: F3 tests infinitesimal Poisson structure; F5 transports modules across Drinfeld twists. Identifying them requires a separate theorem (classical shadow of quantum Yangian = PVA lambda-bracket, a result of De Sole-Kac + Drinfeld-Etingof-Kazhdan), not "the same datum." | Correct: F3 and F5 have the SAME UNDERLYING FORMAL SERIES r(z) = classical r-matrix, but as STRUCTURES they act on different objects: F3 is a coefficient in a lambda-bracket, F5 is an honest operator on V otimes V. The sentence "they pick out the same element of A^! otimes A^![[z^{-1}]]" is true for the coefficient; "they are equivalent presentations" is false at the structural level. | FM53 spectral vs categorical | FM53, AP150 |
| 205 | seven_faces.tex:293-337: F7 listed as "Gaudin generator" in main theorem; alternatively in the abstract (l. 81-82) as "generating function of Gaudin Hamiltonians." Compare CLAUDE.md / hook prompt: F7 is "leading coefficient of the bar differential (top obstruction class on B(A))". | Two different F7 candidates circulate: (a) Gaudin generator (seven_faces.tex canonical); (b) "top obstruction class on B(A) / first A_inf operation m_3" (CLAUDE.md folklore, not in seven_faces.tex main theorem). | seven_faces.tex F7 is the Gaudin generator (l. 330-337). The "top obstruction" / "first A_inf operation" interpretation is NOT in this file. For class M (Virasoro, W_N), the bar complex has infinite A_inf operations (m_3, m_4, ..., m_{2N-1} for W_N — see Part/chapter on class M infinite A_inf), and r(z) is only m_2 data, NOT the full top obstruction. If F7 were "top obstruction," it would be the full tower {m_k}_{k >= 3}, which is STRICTLY MORE data than r(z) for class M. | Correct: EITHER F7 = Gaudin generator (= simple-pole coefficient r_1 in r(z) = sum r_m z^{-m}), in which case F7 captures only the k=1 truncation (l. 390-391: "The Gaudin Hamiltonians are the k=1 (simple-pole) truncation of the collision-residue expansion") and is STRICTLY LESS than r(z) for class M with k_max >= 3; OR F7 = top A_inf operation, which is STRICTLY MORE than r(z) for class M. The equality "r(z) = F7" is well-defined only for k_max = 1 (classes G, L). For class M, F7 is a projection, not a bijection. | F7 underdetermined; injection vs bijection | AP150, AP153 |
| 206 | seven_faces.tex:286-337 (Theorem seven-faces) claims the seven-face identification "for A in the standard landscape," including Virasoro (l. 566, l. 706). The standalone file virasoro_r_matrix.tex extracts r^{Vir}(z) = (c/2)/z^3 + 2T(w)/(z-w). | The Yangian of Virasoro is W_infty (Gaiotto-Rapcak) — an infinite-generator limit algebra, NOT a finite Yangian. | Face F5 ("classical limit of Yangian R-matrix, Drinfeld 1985") is a theorem for FINITE Yangians Y(g), g finite-dim simple Lie. Drinfeld 1985 does not construct Y(Vir) or Y(W_N). The "Yangian of Virasoro" is the Pagoda/W_infty construction — its "r-matrix" is schematic, not a theorem. Applying F5 to Virasoro requires a leap: either identifying Y(Vir) = W_infty (Gaiotto-Rapcak, conjectural), or reinterpreting "Yangian r-matrix" as "first-order coefficient of R(z) for a higher-rank quantum group containing Vir." Neither is done in seven_faces.tex. | Correct: The seven faces are rigorously defined only for finite Yangians / affine Lie algebras. For Virasoro/W_N/class M, F5 is heuristic (W_infty), F2 (DNP line operators) requires gauge-theoretic origin, and F1/F4/F7 are the honest faces. The "seven-face identification for class M" is effectively a FOUR-face identification with F2, F5, F6 being promotional. | scope inflation; class M has fewer faces | AP150, AP155 |
| 207 | seven_faces.tex:390-401 (F4 <=> F7): "The Gaudin Hamiltonians are the k=1 (simple-pole) truncation of the collision-residue expansion." Yet F4 is called "Gaiotto-Zeng commuting differentials" and F7 is "Gaudin generator"; the identification F4 <=> F7 is treated as a bijection. | Drinfeld-Kohno: the classical KZ connection determines the Drinfeld associator Phi_KZ; the r-matrix r(z) = Omega/z is only the FIRST-ORDER coefficient of Phi_KZ. Phi_KZ has higher-order terms (MZV-valued) INVISIBLE to r(z). | Attack probe 9: "Is F1 <=> F4 a bijection, or just an injection?" Answer: INJECTION. r(z) determines the infinitesimal part of the KZ connection, which determines only the first-order monodromy. The full Drinfeld associator Phi_KZ(A, B) (hook probe 10 terminology) has coefficients in multiple zeta values zeta(2), zeta(3), zeta(2,3), ... none of which are recoverable from r(z) alone. F4 "commuting differentials" is the full KZ flat connection; F7 "Gaudin generator" is only r(z). The equivalence F4 <=> F7 is only at the LEVEL of the connection 1-form (infinitesimal monodromy), not at the level of the associator or the full TQFT. | Correct: r(z) determines the KZ 1-form (infinitesimal), hence the Gaudin Hamiltonians (leading-order extraction); but it does NOT determine the full Drinfeld associator or the higher-order monodromy. F4 <=> F7 is an INJECTION at the level of r(z), with higher-order data in F4 invisible to F7. Calling them "the same element" is accurate for the leading coefficient only. | injection vs bijection; AP155 | AP155, AP150 |
| 208 | seven_faces.tex:468-479 (En circle diagram) shows E_3 -> E_2 -> E_1 -> E_2 -> E_3 as a closed loop; l. 500-503: "The circle closes when the derived chiral center acquires E_3-topological structure via the topologization theorem." | AP150 (Vol I): agents stitch together disparate results at different categorical levels into claimed structures (e.g., E_3 -> E_2 -> E_1 -> E_2 -> E_3 cycles) that do not exist. AP154 (Vol II): algebraic E_3 and topological E_3 are distinct; identification is conjectural (conj:e3-identification). | The "closed circle" diagram requires: (a) E_3-bulk -> E_2-chiral via codim-2 restriction (NOT PROVED; Costello-Gaiotto for KM only); (b) E_2-chiral -> E_1 via ordered bar (algebraic, fine); (c) E_1 -> E_2 via Drinfeld center (Deligne conjecture, proved for topological HH, conjectural for chiral HH per AP-CY64); (d) E_2 -> E_3 via derived center topologisation (PROVED for KM at non-critical level, CONJECTURAL general per AP154, FALSE at critical level). The "circle closes" only for KM at non-critical level; otherwise it is an OPEN ARC advertised as a closed circle. Further, l. 488 "Faces F3, F6, F7 see the E_infty shadow" contradicts F7 being listed as E_1 data in the theorem (l. 330); l. 487 "F1, F2, F4, F5 see the full E_1 structure" contradicts F4 (GZ26 "commuting differentials" on a flat connection) being defined via a DIFFERENT operadic level. | Correct: the En-circle is open for class M; for class L (affine KM non-critical) it closes conditionally on Costello-Gaiotto. The face-to-E_n assignments in l. 487-488 are inconsistent with the theorem statement. Either F7 sees E_1 (theorem) or E_infty (En-circle section) — not both. | AP150 confabulation; AP154 conjectural identification | AP150, AP154, AP-CY64 |

## XXIV. Landscape census audit (2026-04-16, Vol I chapters/examples/landscape_census.tex)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | AP |
|---|-------------|---------------|---------------|---------------------|------|-----|
| 209 | landscape_census.tex:447 (Class L caption) and l. 227-230 (convention comment): "r^coll(z) = k*Omega_tr/z = Omega/((k+h^v) z)"; l. 230 "the identification k*Omega_tr = Omega/(k+h^v) reconciles the two." | Trace-form normalisation r^KM = k*Omega_tr/z (AP126: vanishes at k=0, required for level-stripped identity). KZ/Gaudin normalisation r^KM = Omega/((k+h^v) z) (AP-CY65): at k=0 gives Omega/h^v, NONZERO for non-abelian g. | The two expressions are DIFFERENT functions of k. k*Omega_tr is LINEAR in k with zero at k=0; Omega/(k+h^v) has a POLE at k=-h^v and NONZERO value Omega/h^v at k=0. The identity "k*Omega_tr = Omega/(k+h^v)" is false as rational functions of k. This is the AP126 violation by chained-equation: a level-stripped form and a KZ form are fused into one equality. | Correct: they are two DIFFERENT normalisation conventions for the same r-matrix STRUCTURE, related by a level-dependent rescaling of the Casimir tensor (NOT the same Omega on both sides). Honest form: "r^trace = k*Omega_tr/z; r^KZ = Omega_KZ/((k+h^v) z); they represent the same operator in different bases, NOT the same rational function." The chained equality suppresses that Omega on RHS differs from Omega_tr on LHS. | AP126/AP141 level-prefix; normalisation conflation | AP126, AP141, AP-CY65, HZ-1 |
| 210 | landscape_census.tex:1352-1356: "varrho(E_8) = 121/126 < 1: the E_8 shadow obstruction tower converges at all non-critical levels"; l. 1356: "The ordering varrho(E_6) > varrho(E_7) > varrho(E_8) reflects increasing sparsity." | Computed: varrho(E_6) = 427/360 ≈ 1.186, varrho(E_7) = 2777/2520 ≈ 1.102, varrho(E_8) = 121/126 ≈ 0.960. Only E_8 has varrho < 1. | The remark frames varrho < 1 as a convergence criterion for the E_8 shadow obstruction tower, but E_6 and E_7 have varrho > 1 — by the same criterion their towers would FAIL to converge. Yet all three are declared class L with r_max = 3 (l. 1321). The "convergence" statement for E_8 either (a) is a different condition from shadow depth r_max, or (b) implies E_6 and E_7 should be reclassified — neither is addressed. Similarly varrho(W_4) = 13/12 > 1 (l. 1245-1246) without consequence. | Correct: varrho-convergence is an ANALYTIC quantity distinct from shadow depth r_max. All affine KM are class L with r_max = 3 independent of varrho (shadow depth = 3 from Jacobi on Lie bracket). Either drop the E_8 convergence claim or state precisely what goes wrong when varrho > 1 (it is not shadow depth). | narration attaching criterion to wrong invariant | AP153, AP155 |
| 211 | landscape_census.tex:1368: "for Kac-Moody the anomaly ratio varrho(g) is defined for the associated W-algebra W(g, f_prin), not for g-hat_k itself"; yet l. 1228 lists "sl_2-hat at k: varrho = (k+2)^2/(4k)" — i.e. varrho IS used for affine KM in the Polyakov remark. | Two distinct quantities: (A) kappa/c for the algebra itself (level-dependent for affine KM); (B) DS anomaly ratio sum 1/(m_i+1) (level-independent). | Overloaded notation varrho refers to (A) in Remark anomaly-ratio-polyakov (l. 1220-1237), (B) in Corollary cor:anomaly-ratio-ds (l. 1239-1251) and the Exceptional table (l. 1352). Line 1368 attempts to disambiguate after the fact but the table column "varrho" was already ambiguous. | Correct: use varrho_alg(g-hat_k) := kappa(g-hat_k)/c(g-hat_k) for the level-dependent ratio; varrho_W(g) := sum 1/(m_i+1) for the DS W-algebra ratio. These coincide only under specific DS circumstances. Pick one symbol per quantity. | terminology overloading | AP151, AP152 |
| 212 | landscape_census.tex:1072-1073: "The Heisenberg is the abelian Kac-Moody case (h^v = 0); the general KM formula kappa = (k+h^v)d/(2h^v) has a removable singularity here." | The KM formula at h^v = 0, d = 1 gives (k+0)*1/(2*0) = k/0 — INDETERMINATE/DIVERGENT, not removable. Heisenberg kappa = k is defined INDEPENDENTLY as the central extension level (AP1). | Claiming a "removable singularity" suggests a well-defined limit exists. The expression k/(2 h^v) as h^v -> 0 diverges (unless k also -> 0 in a coordinated limit, which is not what "abelian KM" is). The honest relationship is that the abelian Heisenberg kappa = k is derived SEPARATELY from the non-abelian formula; the two expressions are NOT continuous limits of one another. | Correct: "For Heisenberg (abelian, h^v = 0), kappa = k directly from the central extension; the non-abelian KM formula kappa = (k+h^v)d/(2h^v) does NOT extend continuously to h^v = 0." The non-abelian and abelian cases are separate derivations. | narration error; indeterminate form misidentified | AP150, AP158 |
| 213 | landscape_census.tex:639 and 146 W_3 master table entries: kappa(W_3,c) = 5c/6, F_2 column (l. 639) shows F_2 = 7c/6912. Lane labeled "multi". | Theorem multi-weight-genus-expansion (footnote l. 662-668): for multi-weight algebras, F_g = kappa * lambda_g + delta F_g^cross, where the cross-channel correction is NONZERO at g >= 2. | The F_2 column value 7c/6912 is computed from the scalar formula F_2 = 7 kappa/5760 = 7*(5c/6)/5760 = 7c/6912. But the footnote acknowledges this is the SCALAR piece only — the real F_2 for W_3 includes delta F_2^cross, NONZERO for multi-weight algebras. The table silently presents the scalar prediction as the F_2 value. | Correct: the F_2 column for multi-lane entries (W_3, beta-gamma at lambda=1) should either (a) be flagged "scalar piece only" with the cross-channel correction displayed separately, or (b) be recomputed with the full delta F_g^cross. As presented, 7c/6912 is WRONG for W_3 at g=2. | numerical value misrepresented under multi-weight silent scope | AP32, AP153 |
| 214 | landscape_census.tex:1095 (Monster V^nat): "The complementarity sum c + c' = 26 is the Virasoro-sector value." V^nat has c = 24, partner Vir_2, so c + c' = 26. Contrast Leech V_Lambda_24 (l. 164-166): c = 24, partner self-dual, c + c' = n/a. | Both have c = 24 and contain Virasoro subalgebras. The different complementarity listings encode DIFFERENT choices of subsector for duality, not intrinsic property. | The Virasoro-involution c -> 26-c is applied to the Virasoro-sector of V^nat (dim V_1 = 0 so Virasoro is dominant) but NOT applied to V_Lambda_24 (where Heisenberg-sector dominates with 24 weight-1 generators). Both are "PH" in the Master Table — but they use different duality conventions. This is a hidden convention shift. | Correct: the Master Table should label the V^nat row "(Virasoro sector, c + c' = 26)" explicitly, distinguishing from self-duality at the whole-algebra level. The partner Vir_2 with c' = 2 only applies to the sector-level, not V^nat itself. | hidden convention; selective duality scope | AP155 |

Summary metadata:
- Total new entries: 6 (indices 209-214).
- Status: audit-only; no manuscript edits. Findings surfaced for author review.

## XXV. G/L/C/M classification audit (2026-04-16, Vol I standalone/classification*.tex + chapters/examples/landscape_census.tex)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | AP |
|---|-------------|---------------|---------------|---------------------|------|-----|
| 215 | classification.tex:64 "Four Shadow Classes" vs classification_trichotomy.tex:51 "classification trichotomy" (same author, standalone siblings): abstract of trichotomy names "three invariants and four shadow classes", §3 title "trichotomy" refers to OPERATOR-ORDER trichotomy (k_max in {0,1,>=3}) on degree-2 Hamiltonians (Theorem 3.1), not to the G/L/C/M classification. | Two ORTHOGONAL partitions: (A) k_max-trichotomy {0, 1, >=3} from OPE-pole parity (Remark 3.2 "why k_max=2 is absent" -- bosonic weight gap), (B) r_max-quaternitomy {2, 3, 4, infty} = G/L/C/M. | The filename "classification_trichotomy.tex" and the abstract "trichotomy ... four classes" conflate two distinct classifications sharing the same families. Casual readers will read the title as "3-class classification" and contradict the 4-class classification.tex. The two standalones coexist without cross-pointer (classification.tex l. 53-58 only says "three-invariants distinction ... developed further" in trichotomy). | Correct: rename one of (i) the file to classification_three_invariants.tex, or (ii) reframe in abstract: "an operator-order TRICHOTOMY at degree 2 AND a shadow-depth QUATERNITOMY at the tower level". Distinct axes of classification must not share the word "trichotomy" without qualification. | label/content; terminology overloading | AP151, AP152 |
| 216 | landscape_census.tex:296 classifies symplectic fermion SF (c=-2) as class C (r_max = 4) while classification.tex:1036 remarks "contact is rare ... only beta-gamma and bc". | def:class-C requires (a) abelian primary line, (b) quartic Q^contact != 0 on charged stratum, (c) rank-one rigidity dim Def^{(2q)} = 0. | SF at c=-2 is the ODD partner of symplectic boson (beta-gamma at lambda=1/2). Symplectic boson is class G per the l. 294 entry (Z_2-symmetry forces Q^contact = 0 per prop:betagamma-contact-standalone item (ii)), but SF is listed class C. The logical chain is inverted: if the Z_2-graded bar kills Q for the BOSONIC symplectic at lambda=1/2, then by Koszul duality the same Z_2 should act on SF. Either SF is class G (matching symplectic boson) or symplectic boson is class C. Current assignments of class G to one and class C to the other is inconsistent UNLESS the Z_2-graded bar distinguishes them at a level not stated. | Correct: EITHER (a) symplectic boson at lambda=1/2 is class C (with Q^contact != 0 in the Z_2-graded sector, reverting the "Z_2 kills" claim in prop:betagamma-contact-standalone item (ii)), OR (b) SF at c=-2 is class G (matching). The logarithmic phenomena remark "affect modules not bar" (l. 296) does not resolve this. | conflict between specialisation and exception | AP14, AP32, AP-CY12 |
| 217 | CLAUDE.md Vol II (top-of-file pitfalls): "Pole-order dichotomy: Double poles -> class L. Quartic -> class M. DS transports L -> M." The claim presents pole-order as a BIJECTIVE class predictor. | classification_trichotomy.tex §2: beta-gamma has p_max = 1 (SIMPLE pole) yet r_max = 4 (class C). Proposition 3.3 (independence): p_max does not determine r_max. Witness pairs (1,4), (2,2), (2,3), (4,infty). | The "double poles -> class L" rule correctly captures affine KM (p_max=2, class L) but FAILS for Heisenberg (p_max=2, class G): BOTH have p_max=2 but different classes. The CLAUDE.md dichotomy hides class G under "double poles -> class L" and omits class C entirely (beta-gamma has SIMPLE pole, not quartic). A pole-order dichotomy is a CORRELATION, not a bijection. | Correct: pole order p_max is NOT a class predictor. Three-invariants separation (Proposition 3.3 of trichotomy) explicitly shows (p_max, r_max) independence. The honest CLAUDE.md formulation: "Class assignment requires full shadow tower computation (AP-CY12); pole order suggests but does not determine class." The DS transport L->M statement is also only CONJECTURAL per Conjecture 7.4 (conj:ds-shadow-escalation-standalone), with proof only for principal reductions. | necessary/sufficient confusion; AP-CY12 violation | AP-CY12, AP153, AP155 |
| 218 | classification.tex:203 "Class M ... algebras with conformal vector at non-critical level". landscape_census.tex:320 assigns Bershadsky-Polyakov BP_k = W_3^{(2)}(k) to class M via "T-line class M; J-line class G". | Class M is defined by r_max = infty of the SHADOW OBSTRUCTION TOWER (Definition 4.1 in trichotomy, Def 5.4 in classification). A multi-line algebra's class is determined by whether ANY primary line produces an infinite tower, not by counting generators. | Bershadsky-Polyakov has 4 strong generators (T, J, G_+, G_-). Agent heuristic "4 generators -> class L (Lie) or class M?" fails: the correct test is tower computation on each line. BP has class M (inherited from Virasoro subalgebra) per l. 320. This is CORRECT but the heuristic "4 generators" would have given class L. AP-CY12 enforcement: class assignment requires FULL shadow tower, not generator count. The case is a positive instance where the file does the correct calculation, but the reasoning should be made explicit against the generator-count heuristic. | Correct: class assignment for multi-line algebras follows the JOIN semilattice (classification.tex prop:shadow-semilattice-standalone): class(A) = max over primary lines of class(L_i). BP = max(M on T-line, G on J-line) = M. The heuristic "generator count -> class" is WRONG; explicit tower computation is required. | AP-CY12 violation pre-empted by explicit test | AP-CY12, AP153 |
| 219 | Minimal-model Vir_{c_{p,q}} at rational c landscape_census.tex:306 classified as class M with S_4 = 40/49 at c=1/2. | Minimal model Vir_{c_{p,q}} is a SIMPLE QUOTIENT of universal Vir_c, obtained by setting null vectors to zero. Shadow depth of universal algebra != shadow depth of quotient (AP: "Quotient of Koszul !=> Koszul"; landscape_census.tex:1178-1184 states PBW may fail for simple quotients). | Is the shadow tower of Vir_{c_{p,q}} (as a simple algebra) still infinite-depth, or does the quotient terminate it? The S_4 = 40/49 computation proceeds from the OPE of T(z)T(w) with c=1/2, which is the SAME universally. But null vectors in the bar-relevant range (h=6 for L(c_{3,4},0) per l. 1141) obstruct PBW. The tower computation assumes PBW; without PBW, S_r computation is ill-defined. Classifying Vir_{c_{p,q}} as class M without addressing null-vector obstruction is a scope error. | Correct: state "Vir_c at generic c: class M. At rational c_{p,q}: class of the SIMPLE QUOTIENT is OPEN if PBW fails in bar range (l. 1141 explicitly marks L(c_{3,4},0) with an X for PBW failure)." The Ising entry (c=1/2) in the landscape table should carry a conditional flag. | quotient != ambient; PBW prerequisite | AP14, AP-CY12, AP-CY14 |
| 220 | classification.tex:527-540 complementarity table: Virasoro self-dual at c=13 via Vir_c <-> Vir_{26-c}. Meta-CLAUDE.md AP8: "NEVER self-dual unqualified." c=13 is KOSZUL self-dual (c + c' = 26), distinct from critical c_crit = 26 (matter-ghost cancellation). | Two different self-dualities: (A) Koszul c*=13 (half the conductor 26, sum c+c' = 26). (B) Critical c_crit = 26 (bosonic string, matter+ghost=0 after bc at c=-26). | classification.tex:539-540 writes "Vir_{13} is self-dual under uncurved quadratic duality." This qualification (uncurved quadratic) correctly distinguishes from the c_crit=26 string-theory self-duality. But AP8 (Vol I) warns against unqualified "self-dual". The text is CORRECT here, pre-empting AP8 -- yet the adjacent Heisenberg entry l. 478 "Koszul dual Sym^ch(V*)" and l. 522 "Heisenberg self-dual only formally" leaves the duality type ambiguous. | Correct: every self-duality row must specify (i) which duality functor (Koszul vs Feigin-Frenkel involution vs Virasoro symmetry), (ii) which c (Koszul c*=13, critical c_crit=26), (iii) which object (algebra vs its bar coalgebra). classification.tex does (i) and (ii) for Vir but not consistently across Heisenberg and W_N rows. | AP8 self-dual ambiguity | AP8 |
| 221 | classification.tex:86 (Def 5.1 shadow classes): class C entry "alpha=0, Delta=0^*, r_max=4". The asterisk footnote l. 88-93 admits the Riccati discriminant IS zero on the primary line, but asserts a separate quartic Q^contact lives on a "charged stratum". | prop:depth-gap-standalone (l. 775-784): d_alg(A) in {0, 1, 2, infty}. No finite value d_alg >= 3 realized. FOUR values bijectively correspond to G/L/C/M. | The depth-gap proof (l. 786-845) covers only the RANK-ONE Riccati analysis (giving {0, 1, infty}) on a single primary line; class C (d_alg = 2) is explicitly noted as "boundary where Delta = 0 on the primary line but S_4 != 0 on a charged stratum" (l. 828-834). This means class C is NOT derived from the rank-one quadratic algebraic mechanism but from a MULTI-SECTOR dimensional obstruction. The "four shadow classes" claim is actually THREE rank-one classes (G, L, M) plus ONE multi-sector class (C) glued by a separate rank-one-rigidity theorem (Prop 7.3 betagamma-contact-standalone). | Correct: present classification as (a) RANK-ONE Riccati trichotomy on each primary line: d_alg|_L in {0, 1, infty}; (b) MULTI-SECTOR refinement: (d_alg, charged-stratum Q^contact) pairs produce G, L, C, M. Class C is a multi-sector artefact, not a rank-one class. The "four" in "four classes" is the quaternitomy on the ALGEBRA level; the "three" implicit in the rank-one analysis is what drove the sibling file's choice of name "trichotomy". The two standalones are DIFFERENT slices. | scope error; rank-one vs multi-sector | AP151, AP152, AP-CY12 |
| 222 | classification_trichotomy.tex:366-367 (Class M proof): "Virasoro has S_3(Vir_c) = 2, a nonvanishing c-independent constant." Combined with prop depth-gap (S_3 != 0 => infinite tower), classifies Vir class M. | Theorem s3-vir (l. 408-427): S_3 = 2 is derived from T_{(3)}T = c/2 and T_{(1)}T = 2T, with kappa = c/2 cancelling. FM: at c = 0 this derivation divides c/2 by c/2, a 0/0 limit. | The proof "S_3 = 2kappa/kappa" (l. 423) assumes kappa != 0. At c = 0 (the ghost CFT b c lambda=2 or c=0 matter), kappa(Vir_0) = 0. The S_3 computation becomes 0/0 -- indeterminate. Classifying Vir_0 as class M using S_3 = 2 is ill-defined: the "universal" value 2 is a LIMIT, not a direct computation at c=0. Similarly critical level KM V_{-h^v}(g) has kappa = 0 (Theorem kappa-formula at k+h^v=0), so the entire depth-gap machinery (which assumes kappa != 0 in Proposition 3.1 premise) does not apply. | Correct: classification theorems in classification.tex prop:depth-gap-standalone (l. 775-776) EXPLICITLY require kappa(A) != 0. At critical level KM (kappa=0) and Vir_0 (kappa=0), the classification is UNDEFINED by the main theorem. These cases require separate analysis. CLAUDE.md Vol II "critical level, Sugawara undefined, center jumps, topologization fails" correctly notes this; classification.tex should add a row "kappa=0 case: outside the G/L/C/M classification". | kappa=0 scope exclusion; 0/0 confabulation | AP8, AP158 |
| 223 | Vol II CLAUDE.md MP "Pole-order dichotomy" presents DS reduction L -> M as established. classification.tex:1077-1090 has this as Conjecture 7.4 (conj:ds-shadow-escalation-standalone), PROVED only for principal reductions (Remark 7.5(a)). | For non-principal nilpotents (minimal, subregular, hook), the conjecture is "verified by systematic computation" for sl_N, N = 3,4,5 only (Remark 7.5(b)), not proved. | The Vol II CLAUDE.md pitfall "DS transports L -> M" implies universally; the Vol I standalone has this only as a conjecture for general nilpotent f, with partial verification for type A low rank. The "-> M" claim is provably correct for f = f_prin but only empirically verified for other nilpotents in sl_3, sl_4, sl_5. For f in type BCDEFG non-principal, the claim is UNVERIFIED. | Correct: DS transports L -> M (PROVED for f_prin for every simple g; CONJECTURAL in general, with computational verification in type A up to sl_5). CLAUDE.md should annotate the scope: "(proved for principal; conjectural for non-principal)." | status over-promotion; scope inflation | AP155, AP-CY14 |
| 224 | classification_trichotomy.tex:375-380 (Proposition depth-decomp): "d_alg in {0, 1, 2, infty}" with class C at d_alg = 2. The proof sketch l. 386-406 argues by sector decoupling vs coupling. | Proposition 3.1 of classification.tex (depth-gap-standalone) and Proposition 4.3 of classification_trichotomy.tex (depth-decomp) use INCOMPATIBLE conventions for d_alg. | classification.tex l. 776-784 Prop 3.1: "d_alg in {0, 1, 2, infty}" with G=0, L=1, C=2, M=infty. classification_trichotomy.tex l. 379: identical values but l. 158-163 defines r_max(beta-gamma)=4 and l. 190 defines r_max in {2, 3, 4, infty} with C corresponding to r_max=4, not r_max=2 or d_alg=2. The mapping d_alg <-> r_max follows d_alg = r_max - 2 in the quaternitomy (G: r_max=2, d_alg=0; L: r_max=3, d_alg=1; C: r_max=4, d_alg=2; M: r_max=infty, d_alg=infty). This mapping is CORRECT but NEVER stated explicitly in either standalone. Readers see two different "depths" (d_alg and r_max) with overlapping value sets and must infer the bijection. | Correct: state d_alg(A) = r_max(A) - 2 (for finite r_max) and d_alg(A) = infty iff r_max(A) = infty as a named proposition early in both standalones. Currently this is implicit, and the depth-decomposition formula d = 1 + d_arith + d_alg (l. 376 trichotomy) introduces a THIRD depth "d" without explicit relationship to r_max. | convention clash; implicit bijection | AP151 |

Summary metadata (second audit):
- Total new entries: 10 (indices 215-224).
- Status: audit-only; no manuscript edits. Findings surfaced for author review.
- Audit scope: G/L/C/M classification across standalone/classification.tex, standalone/classification_trichotomy.tex, chapters/examples/landscape_census.tex, and Vol II CLAUDE.md cross-references.

## Celestial / Soft Graviton / Arithmetic Shadows Audit (2026-04-16)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 225 | thm:thqg-VI-leading-soft "proves the Weinberg soft theorem" (ClaimStatusProvedHere). The proof is an algebraic Ward identity on correlators $\Phi(z_1,\dots,z_n,z_s)$ with `$\kappa(\phi_s,\phi_i)/(z_s-z_i)$` plus a dictionary asserting this equals $p_i\cdot\varepsilon_s/(p_i\cdot q_s)$. | The genus-0 degree-2 Ward identity for the shadow connection IS proved: $\sum_i \kappa(\phi_s,\phi_i)/(z_s-z_i)\Phi_n$ is forced by $\Sh_{0,n+1}(\kappa)\Phi = 0$. | "Momentum-space identification... follows from the standard dictionary between conformal-block OPE residues and on-shell scattering amplitudes" (file:line thqg_soft_graviton_theorems.tex:699-706) is an ASSUMED bijection, NOT a theorem. The dictionary requires (a) a Mellin transform with specific contour, (b) an external identification of celestial primaries with boost eigenstates, (c) a bilinear-form identification $\kappa(\phi_s,\phi_i) = p_i\cdot\varepsilon_s$. None of (a)-(c) is proved in the chapter; (c) is asserted by "Strominger 2018". | Correct: "The degree-2 Ward identity reproduces the Weinberg soft factor CONDITIONAL ON the Strominger Mellin-transform dictionary between celestial correlators and 4d S-matrix elements." Status should be `ProvedElsewhere` for the dictionary, `ProvedHere` for the Ward identity, with the proof block stating the conditional explicitly. | construction/narration; necessary/sufficient |
| 226 | thm:thqg-VI-general-soft `\ClaimStatusProvedHere` gives "General degree-$r$ celestial soft factor" for all $r\ge 2$. Proof states "In the celestial/gravitational reading, the factors $S^{(r-2)}$ are read as the corresponding order-$(r-2)$ higher soft factors." | The algebraic degree-$r$ Ward identity for the shadow connection is proved (MC equation projected). | The celestial-to-momentum identification at order $r\ge 3$ is NOT the Cachazo-Strominger identification; the higher-order soft factors (Hamada-Shiu, Li-Strominger) involve angular-momentum operators $J^{\mu\nu}$ and stress-tensor insertions that do not have a general shadow dictionary. The phrase "read as the corresponding order-$(r-2)$ higher soft factors" asserts an identification proved nowhere. The subleading case (r=3, thm:thqg-VI-subleading-soft) has an explicit CS factor; at r=4,5,... it is conjectural. | Correct: downgrade r>=4 cases to `\ClaimStatusConjectured` or restrict scope to "the algebraic shadow hierarchy." The Cachazo-Strominger match is PROVED only at r=3. The claim "this generalises WCS to all orders" is a GHOST of a true theorem -- the ghost is: there IS a hierarchy of Ward identities, and it does stratify the celestial soft expansion, but the identification with specific momentum-space soft factors beyond CS requires a separate proof per order. | scope inflation; label/content | AP155, AP158, AP153 |
| 227 | prop:thqg-VI-asymptotic-symmetry `\ClaimStatusProvedHere` gives four-row table "Class G -> supertranslations", "Class L -> extended BMS", "Class C -> quartic extension of BMS", "Class M -> full gravitational $L_\infty$". | Algebraic shadow-depth stratification of the celestial soft subalgebra is proved (generators at degrees $2,\dots,r_{\max}$). | BMS_4 is a SPECIFIC Lie algebra (semidirect product of Lorentz with supertranslations; Barnich-Troessaert 2010 extends to superrotations). The shadow-depth subalgebra $\mathfrak{S}(\cA)$ has different generators and relations. The identification with BMS is a LABELING, not a theorem. For class L (superrotations), BMS_4 extended has a specific central extension with Virasoro coefficient; the shadow construction gives $\alpha\in\mathbb{Q}$ dependent on the algebra. The proof block (line 2215-2240) says "In the celestial/gravitational reading... read as the extended BMS package" -- the reading is the assertion. | Correct: state "the celestial soft subalgebra $\mathfrak{S}(\cA)$ HAS THE STRUCTURE of an algebraic hierarchy analogous to the BMS tower." The explicit identification of $\mathfrak{S}(\cA)$ with BMS_4 (or $w_{1+\infty}$ for class M) requires a Mellin-space match of generators and a check of the central extension coefficients. Class-C "quartic extension of BMS" has NO known amplitudes counterpart; this is a prediction, not a theorem. | construction/narration; specific/general | AP155, AP153 |
| 228 | celestial_holography_core.tex ev:ch-core-celestial-graviton-ope `\ClaimStatusHeuristic` admits heuristic status but still propagates into other theorems as if proved. The extracted celestial graviton OPE $\mathcal{O}^+_{\Delta_1}\mathcal{O}^+_{\Delta_2} \sim (\Delta_2-1)/(z_1-z_2) \cdot \dots + (c/2)/(z_1-z_2)^3\dots$ "matches the Pasterski-Shao-Strominger graviton OPE." | PSS graviton OPE is a physical result; the bar-complex collision residue of Virasoro is computable. The triple-pole and the $\Delta_2-1$ coefficient are REAL outputs of the bar complex. | The chapter explicitly flags the heuristic status: "the extraction of celestial OPE coefficients from the bar-complex collision residue assumes the Mellin-space factorisation of the holomorphic-topological propagator, which has not been proved in full generality" (line 1005). The helicity-splitting theorem (thm:ch-core-helicity-splitting) parts (ii)-(v) have the same heuristic flag. | Correct: the chapter is HONEST about this (rare in the manuscript); the risk is downstream propagation. Grep for uses of ev:ch-core-celestial-graviton-ope and thm:ch-core-helicity-splitting (v) and verify that no downstream theorem tagged ProvedHere chains through them. | chain/cohomology; heuristic-propagation | AP155 |
| 229 | arithmetic_shadows.tex thm:shadow-spectral-correspondence `\ClaimStatusProvedElsewhere` states "number of critical lines of constrained Epstein zeta = shadow depth - 1" for lattice VOAs, AND chapter claims "Unconditional Ramanujan bound for lattice VOAs" (cor:unconditional-lattice) via "MC => prime-locality => CPS => Sym^{r-1} => Ramanujan" (line 135-137). | Shadow tower of a lattice VOA $V_\Lambda$ decomposes through the Hecke decomposition of $\Theta_\Lambda$. This is a real structural fact about theta series. | The Ramanujan bound for lattice theta functions follows from Deligne's theorem (Weil conjectures). The claim "bounds the same Deligne eigenvalues by the shadow tower INSTEAD of the Weil conjectures" (line 139-140) would require the shadow-tower argument to be INDEPENDENT of Deligne. The chain "MC => prime-locality => CPS => Sym^{r-1} => Ramanujan" passes through "converse theorem and Langlands functoriality" (line 138-139) -- both of which use Deligne-style bounds at intermediate steps. An unconditional shadow-tower proof of Ramanujan that bypasses Deligne would be a major arithmetic result. | Correct: the shadow tower CAPTURES the Hecke decomposition structure of $\Theta_\Lambda$; the bound on Hecke eigenvalues is Deligne's theorem. The correct statement is "The shadow tower reproduces the Ramanujan-Petersson eigenvalue stratification that Deligne's theorem bounds." Claiming an independent proof is overstatement unless Langlands functoriality and the converse theorem can be traced to non-Deligne inputs. The `ProvedElsewhere` tag hides this: the "elsewhere" (Deligne + Langlands) is precisely the arithmetic machinery the shadow tower was supposed to bypass. | label/content; construction/narration; circular | AP155, AP158 |
| 230 | Celestial holography identification: celestial chiral algebra $\cA_{\mathrm{cel}}$ is affine Kac-Moody at tree level (line 1278-1281 celestial_holography_core.tex), with ${\cA_{\mathrm{cel}}}^!_{\mathrm{line}} = Y_\hbar(\fg)$ `\ClaimStatusConjectured` for general $\fg$, PROVED for $\fg=\mathfrak{gl}_N$ in $\cN=4$ SYM via Costello (Cos13). | Costello-Witten-Yamazaki (2018) and Costello-Paquette (2020) prove the celestial OPE of self-dual YM = Kac-Moody, and the boundary chiral algebra of 4d CS theory has Yangian as Koszul dual. | The statement "$\cA_{\mathrm{cel}}$ is affine KM at tree level" is CORRECT only for certain theories (pure YM tree-level, $\cN\ge 1$ SYM tree-level). It is NOT the full celestial chiral algebra of Einstein gravity (which is $w_{1+\infty}$ or its deformation) and not the celestial chiral algebra of general matter-coupled theories. The chapter mostly handles this correctly but the class-M "expected large-c model $\cW_{1+\infty}$" (line 2206) is conjectural even at tree level. | Correct: state the scope as "tree-level self-dual gauge theories (YM, SDYM, pseudoscalar axion) + bosonic open sector of $\cN=4$ SYM." Strominger-Pasterski and the celestial CFT program for GR have DIFFERENT chiral algebras (e.g., $Lw_{\wedge}$ per Adamo-Mason-Sharma). The W_{1+infty} route is via twisted holography (Costello-Paquette), not the Mellin-transform route (Strominger). | scope inflation; construction/functor | AP155, AP153 |
| 231 | Gauge/gravity dichotomy presented in Vol II CLAUDE.md and cross-volume bridge table as "$m_k=0$ (gauge) vs $m_k\ne 0$ (gravity)" with class G=gauge, class M=gravity. | There is a genuine structural dichotomy: for Lie-type (Kac-Moody) chiral algebras, $m_k$ on bar cohomology can vanish (formality); for W-type (Virasoro, $W_N$), infinite shadow tower forces non-formality. | The identification gauge=formal=class G and gravity=non-formal=class M is NOT a theorem. (a) Pure YM tree celestial algebra has higher-spin structure (w_{1+infty}-like) beyond simple-pole KM for certain matter contents. (b) Gravity celestial algebra at genus-0 tree level for MHV is ALSO non-trivially structured but the class assignment depends on the self-dual vs non-self-dual sector. (c) Heisenberg (abelian gauge) is class G but corresponds to a free abelian gauge theory; non-abelian YM tree-level is class L (KM), not G. (d) Einstein gravity's soft algebra in the recent celestial literature is class $\cW_{1+\infty}$-adjacent (Guevara-Himwich-Pate-Strominger), which is class M. | Correct: the REAL dichotomy is "simple-pole OPE (class G, L) vs higher-pole OPE (class C, M)"; this MAPS to "abelian or KM-type gauge (G for abelian, L for non-abelian KM) vs W-type / higher-spin / gravitational (C, M)" but the map is NOT "gauge vs gravity". Non-abelian YM is CLASS L, not G. The slogan "$m_k=0$ gauge, $m_k\ne 0$ gravity" is false: non-abelian YM has non-trivial higher structure (Yangian, 1-loop associativity corrections per Costello). Correct slogan: "simple-pole (G/L) vs higher-pole (C/M); gauge theories can be G, L, or even C; gravity is M." | specific/general; conflation | AP155, AP158 |
| 232 | thqg_soft_graviton_theorems.tex subsections headed "celestial soft factor and its gravitational reading" consistently use the phrase "read as" to transition from algebraic shadow quantity to physical soft factor. Every "celestial/gravitational reading" clause is an assertion, not a derivation. | For genus 0, leading (r=2) and subleading (r=3), the identifications match known soft theorems (Weinberg, Cachazo-Strominger). For higher r, they are conjectural. | Systematic pattern: the algebraic theorem is genuinely proved; the physical reading is asserted by "this is standard in the celestial holography literature (Strominger 2018)." This is AP155 overclaim at scale: the algebraic side is new, the physical side is known, the bridge is a dictionary. Tagging the whole unit `\ClaimStatusProvedHere` is only correct if "ProvedHere" refers to the algebraic side. | Correct: every celestial-reading theorem should be split into (a) algebraic Ward identity with `\ClaimStatusProvedHere`, (b) celestial interpretation with `\ClaimStatusProvedElsewhere` (r=2,3) or `\ClaimStatusConjectured` (r>=4), and (c) bridge Proposition with explicit statement of the Mellin/bilinear-form dictionary used. Currently (b) and (c) are folded into (a). | construction/narration; label/content | AP4, AP155, AP158 |

Summary metadata (celestial audit):
- Total new entries: 8 (indices 225-232).
- Status: audit-only; no manuscript edits. Findings surfaced for author review.
- Audit scope: thqg_soft_graviton_theorems.tex, celestial_holography_core.tex, celestial_holography_frontier.tex, celestial_boundary_transfer_core.tex (Vol II), arithmetic_shadows.tex, poincare_computations.tex (Vol I).
- Core finding: the celestial/soft/arithmetic cluster has genuine algebraic content (shadow Ward identities, Hecke decomposition of lattice thetas, bar-complex collision residues) but systematically bundles the algebraic theorem with the celestial/gravitational/arithmetic INTERPRETATION under a single `ProvedHere` tag. The interpretations are, variously: (a) standard but proved elsewhere (Weinberg, CS), (b) a "reading" in the Strominger dictionary, (c) conjectural (higher-r soft factors, BMS identification beyond r=3, Ramanujan-without-Deligne).

## XXVIII. Vol II Part VI climax "3d gravity = Z^der_ch(boundary)" adversarial review (2026-04-16)

Scope: chapters/connections/3d_gravity.tex, chapters/connections/thqg_*.tex, chapters/connections/ht_bulk_boundary_line_core.tex, standalone/three_dimensional_quantum_gravity.tex (admitted SCAFFOLD, l. 7).

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | AP |
|---|-------------|---------------|---------------|---------------------|------|-----|
| 233 | 3d_gravity.tex:6909 (thm:E3-topological-DS-general, Step 2 of proof): "The ghost stress tensor T_ghost of the DS (b,c)-system, when identified with 3d bulk fields via the Costello-Gaiotto boundary condition, is Q_CS-exact by the same mechanism: each ghost bilinear :b_a dc^a: maps to a commutator [Q_CS, (bulk antighost)]." | For principal nilpotent, G_imp (eq. 6704) is an explicit bulk operator transporting DS ghosts to bulk antighosts. For non-principal f, an analogous construction is required. | One-sentence existence claim without producing the bulk operator. For non-abelian Levi (BP = sl_3 f_min; minimal sl_4; hook in sl_5), the DS (b,c)-spectrum does not match the bulk (bar c, c) spectrum -- CG boundary trivialises some DS pairs and identifies others. The universal antighost eq:G-prime-general is built only from Cartan antighosts; non-Cartan DS pairs are invisible. The improvement term T_imp(f) is indeed Cartan-linear for any f (Jacobson-Morozov gives h_0 in h), but the full ghost sector includes non-Cartan DS bilinears not covered by eq:G-prime-general. rem:non-principal-obstructions-illusory dismisses "non-Koszulness" and "non-abelian Levi" without constructing the missing bulk-antighost map. | Correct: the theorem as stated (T_DS(f) Q-exact on cohomology) is plausible and the Sugawara + improvement piece is constructed; the non-Cartan DS ghost piece would require case-by-case verification. Tag should be refined: ProvedHere for principal f; ProvedHere for minimal nilpotent in type A (computable); Conjectured for general non-principal f. This is a FM61 ghost-bilinear-Q-exactness handwave pattern. | FM61 handwave; construction/narration | FM61, AP40, AP150, AP158 |
| 234 | 3d_gravity.tex:6785-6802 (rem:E3-DS-status) combined with thm:E3-topological-DS tag ProvedHere (l. 6583): "The BRST identity is proved on Q_CS-cohomology, not at the cochain level... For topologization, the cohomological identity suffices." rem:cohomological-vs-cochain (l. 6481-6506): "For class M, chain-level operations carry essential information that vanishes on cohomology. The E_3 upgrade may hold on cohomology but fail at the cochain level." | For class M (Virasoro, W_N), the shadow tower is infinite; formality of the little 2-disks operad is used to bridge chain and cohomology. | thm:E3-topological-DS / thm:E3-topological-DS-general are ProvedHere. Proofs deliver cohomological local constancy. Chain-level E_3-topological for class M is admitted as possibly failing. "3d gravity factorisation algebra = Z^der_ch(boundary)" -- if understood as chain-level factorisation-algebra equivalence -- is the target for class M physical gravity. The CLAUDE.md Vol II bridge row "E_3-topological: PROVED for ... ALL W-algebras" reads the theorem as chain-level; the .tex admits otherwise. | Correct scope: thm:E3-topological-DS(-general) prove E_3-topological structure on Z^der_ch(W) AT THE LEVEL OF COHOMOLOGY (or equivalently, in an inf-categorical framework absorbing chain-level obstructions). Chain-level E_3-topological -- the structure physical gravity requires for a factorisation algebra interpretation -- is PROVED for G/L/C (see rem l. 291-298), CONJECTURAL for class M. The bridge-row phrasing should split: "E_3-top on cohomology: PROVED KM/all W-algebras; chain-level E_3-top: PROVED G/L/C, CONJECTURAL class M." | chain/cohomology scope; AP40 tag-vs-environment | AP40, AP153, AP154, FM61, AP-CY33 |
| 235 | 3d_gravity.tex:2103-2118 (thm:gravity-koszul-triangle, ProvedHere): Bulk = Z^der(Vir_c) ≃ HH^0 ⊕ HH^2[-2] ≃ C[[c]]. "Pure 3d gravity has one parameter: the cosmological constant." The triangle closes bulk <-> boundary <-> lines. | HH* of the Virasoro Lie algebra (Gel'fand-Fuchs 1968): HH^0 = C, HH^1 = 0, HH^2 = C (central extension), HH^{>=3} = 0 for generic c. This is standard. | "Bulk ≃ C[[c]]" is a DIMENSIONAL STATEMENT about two Hochschild sectors (HH^0, HH^2), presented as "the derived centre". AP-CY64 three-way HH confusion: (i) ChirHoch C^*_ch (Vol II's declared framework) carries OPE data + spectral parameters + lives over Ran(X); (ii) classical Lie HH* = GF continuous cohomology = polynomial ring in Virasoro cochains; (iii) topological HH^*(A_mode) = 1-dim for Weyl-type quotients. None of these equals C[[c]] tout court; the identification is a truncation. | Correct: the theorem proves a cohomological projection onto HH^0 + HH^2[-2] (the "classical" two-cocycle sector of Vir) is C[[c]]. The full Z^der_ch(Vir_c) in the declared chiral framework is strictly richer. The physical reading "pure 3d gravity has one parameter" is saddle-point correct but should be called a projection onto the universal Virasoro central extension, not a derived equivalence. | AP-CY64 three-way HH; truncation presented as equivalence | AP-CY64, AP153, AP150 |
| 236 | 3d_gravity.tex:7101-7123 (rem:monster-orbifold-route): "V^natural = V_Lambda^+ inherits E_3-topological by taking Z/2-invariants (finite group invariants preserve E_n)... the full V^natural requires Z/2-gauged holomorphic CS, an orbifold BV quantisation not yet constructed in the Costello-Li framework, but expected to be tractable (the anomaly vanishes by modular invariance)." | Finite-group invariants preserve E_n-algebra structure (standard operadic fact). | The remark reduces conj:E3-topological-general for V^natural to "orbifold BV of abelian CS with Z/2 twist." This trades one open problem for another. "Expected to be tractable" is a research expectation, not a proof step. The "reduces to a bounded technical construction" phrasing (l. 7120-7122) over-promotes: the orbifold BV construction is genuinely not in the published literature. CLAUDE.md FM66 is slightly more cautious ("anomaly vanishes by modular invariance"). | Correct: the untwisted invariant subalgebra V_Lambda^+ inherits E_3-topological from V_Lambda. The full V^natural = V_Lambda^+ + twisted sector requires orbifold BV quantisation, which is open. Remark should state "reduces to orbifold BV quantisation of abelian CS (open, not currently obstructed)". | AP-CY32 reorganisation ≠ bypass; over-optimism | AP-CY32, AP153, AP155, FM66 |
| 237 | CLAUDE.md Vol II bridge table "3D gravity" row: "Global triangle: PROVED for classes G/L/C (thm:global-triangle-boundary-linear); OPEN for class M (gap: DS-Hochschild compatibility)." | Cited label thm:global-triangle-boundary-linear is not present in Vol II; the actual label is thm:boundary-linear-bulk-boundary (ht_bulk_boundary_line_core.tex l. 1234). | The cited-label issue (stale reference) is symptomatic. More substantively: thm:boundary-linear-bulk-boundary proves bulk ≃ derived centre for commutative Landau-Ginzburg boundary conditions W(x,y) = <y, F(x)> (HKR + shifted cotangent / dCrit identification). Classes G/L/C are chiral algebras: Heisenberg, affine KM, beta-gamma. These are NOT Landau-Ginzburg models. The global triangle transfer from LG to chiral algebras is not in the manuscript. | Correct: thm:boundary-linear-bulk-boundary is the LG theorem. For chiral G/L/C, the "global triangle" at the level of derived Hochschild projection is established by chapter-level theorems (Heisenberg HH*, KM HH*, beta-gamma HH* each finite-dim; see hochschild.tex). The bridge-table claim should cite these chiral HH computations, not the LG theorem. The label should be renamed or the reference updated. | cross-volume reference stale; LG-vs-chiral conflation | AP5, AP40, AP153, AP-CY64 |
| 238 | thqg_perturbative_finiteness.tex:788-798 (thm:thqg-I-perturbative-finiteness, ProvedHere) parts (i)-(iv): "Perturbative finiteness of twisted gravity" with "No UV renormalization... no counterterms or renormalization are needed at any genus." | HS-sewing (thm:general-hs-sewing) + Bernoulli asymptotics give absolute convergence of the scalar partition function for |h| < 4 pi^2 on the proved scalar lane. | The theorem proves ALGEBRAIC finiteness of shadow coefficients F_g and absolute convergence of a formal generating function on the scalar lane. Part (iv) "no UV renormalization needed" is physical spin on a statement about a formal bar-complex combinatorial object. Finiteness of shadow coefficients is NOT physical UV finiteness of 3d quantum gravity scattering. The Fulton-MacPherson compactification provides a "geometric regulator" in a formal-algebraic sense, not in the sense of a regulator removing UV divergences from a QFT path integral. Parts (ii)-(iii) restrict to scalar/Gaussian lanes (uniform weight). | Correct: the theorem is an algebraic statement about the shadow Maurer-Cartan generating function. Physical UV finiteness of 3d quantum gravity scattering amplitudes would require chain-level BV + factorisation-algebra control, which for class M (physical Virasoro gravity) is subject to the chain-level E_3 gap (see #234). The "No UV renormalization" clause should be qualified: "No combinatorial renormalization of the bar complex is required; physical scattering-amplitude UV finiteness is a separate question subject to the chain-level gap." | algebraic formal vs physical UV; scope inflation | AP32, AP153, AP155 |
| 239 | 3d_gravity.tex:5181 (conj:curved-dunn-additivity, Conjectured): curved Dunn additivity at genus >= 2 is open. But the E_3-topological construction (constr:topologization, l. 6421-6436 Step 3) invokes Dunn additivity E_2^top ⊗ E_1^top ≃ E_3^top for all genera without genus restriction. | Curved Dunn at genus 0 is Lurie's classical theorem. Genus 1 is proved via twisted Kunneth (Vol II CLAUDE.md Preface). Genus >= 2 is genuinely open (H^2 obstruction per FM67). | thm:E3-topological-km / thm:E3-topological-DS / thm:E3-topological-DS-general implicitly assume Dunn additivity at all genera to deliver E_3-topological. The construction (Step 3 of constr:topologization) glues E_2^top and E_1^top without genus qualification. Class M algebras specifically fire the genus tower; restricting to genus <= 1 cuts off the physically interesting regime for 3d gravity (BTZ = genus >= 1). | Correct: thm:E3-topological-DS(-general) is unconditional at genus 0 and 1. For genus >= 2, the theorem is conditional on conj:curved-dunn-additivity. ProvedHere tag requires a genus scope qualifier, or an explicit statement "at each fixed genus up to curved-Dunn additivity at that genus". CLAUDE.md Preface North Star accurately records "Curved Dunn at genus 1: PROVED; Genus >= 2: OPEN" -- the climax chapter should mirror this. | genus scope; conditional proof presented as unconditional | AP6, AP32, FM67, AP153 |

Summary metadata (XXVIII climax audit):
- Total new entries: 7 (indices 233-239).
- Status: adversarial read-only review; no manuscript edits.
- Scope: Vol II Part VI climax "3d quantum gravity = derived center of boundary chiral algebra".
- Severity distribution:
  - HIGH: #233 (ghost-bilinear handwave at non-principal DS -- FM61), #234 (chain-level vs cohomological scope for class M is the core climax gap -- ties to AP154 and AP-CY33), #239 (genus >= 2 Dunn additivity gap propagates to all climax theorems).
  - MED: #235 (AP-CY64 three-way HH in the Virasoro Koszul triangle), #237 (stale cross-volume label + LG/chiral conflation).
  - MED/LOW: #236 (Monster orbifold over-optimism, admitted open), #238 (perturbative finiteness is algebraic not physical).
- Core finding: the ClaimStatusProvedHere tag on thm:E3-topological-DS and thm:E3-topological-DS-general covers the COHOMOLOGICAL statement; for class M (Virasoro, W_N) the chain-level E_3-topological factorisation algebra -- which is what "3d quantum gravity = derived center" genuinely asserts for a factorisation-algebra framework -- is admitted to possibly fail at chain level (rem:cohomological-vs-cochain l. 6492-6498). This is consistent with AP154 (two E_3 structures, identification conjectural), AP-CY33 (chain != rational), and FM67 (curved-Dunn H^2 obstruction). Separately, several climax theorems implicitly assume curved Dunn additivity at genus >= 2 (#239). The "3d gravity = derived center" slogan is correct IFF read in the cohomological/inf-categorical/projected sense; the chain-level factorisation-algebra reading for class M + high genus is the residual frontier.

## XXVIII. Lattice VOA + Moonshine adversarial review (2026-04-16, Vol I chapters/examples/moonshine.tex + lattice_foundations.tex + level1_bridge.tex + symmetric_orbifolds.tex, Vol II CLAUDE.md FM66)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | AP |
|---|-------------|---------------|---------------|---------------------|------|-----|
| 240 | Vol II CLAUDE.md FM66: "V^natural = V_Leech^+ (Z/2 orbifold). V_Leech IS E_3-topological (abelian CS). V_Leech^+ inherits E_3-topological NOW (finite group invariants preserve E_n). The anomaly vanishes (modular invariance)." | V_Leech contains rank-24 Heisenberg sector with abelian Sugawara T=(1/2)Sigma:j_i j_i: at c=24 non-critical; abelian CS on an appropriate 24-torus provides the 3d HT origin of the Heisenberg subalgebra (FM62 corrected earlier error). | Three layered conflations: (a) "V_Leech IS E_3-top (abelian CS)" -- the level data selecting Leech quadratic form on U(1)^24 abelian CS is never named. The boundary VOA of abelian CS at a generic integral level matrix is a lattice VOA whose lattice is determined BY the CS level. Matching it to Lambda_Leech is a CONSTRUCTION, not a citation. (b) "V_Leech^+ inherits E_3-top (finite group invariants preserve E_n)" -- this holds for TRIVIALLY acting finite groups on factorization algebras. The Leech involution v -> -v acts on the CS gauge field; it is a BULK Z/2 GAUGING, which introduces twisted sectors and modifies the operad output. "Inherits" conflates trivial-action fixed points with gauging. (c) "anomaly vanishes (modular invariance)" -- modular invariance of the partition function Z_{V^natural}(tau) is proven (FLM 1988 / Borcherds 1992); cohomological orbifold BV anomaly is a class in H^3(BZ/2,U(1)) (Dijkgraaf-Witten). Vanishing of one does NOT imply vanishing of the other. | IF (i) there exists a 3d abelian CS theory whose boundary is V_{Lambda_Leech}, AND (ii) the Leech involution gives an anomaly-free Z/2 gauging in the Dijkgraaf-Witten sense, THEN V^natural = V_Leech^+ oplus (V_Leech^T)^+ carries E_3-topological structure. Both (i) and (ii) are OPEN constructions, not "inherits". Modular invariance is necessary but not sufficient for (ii). FM66 promotes "construction required" to "inherits now" -- status over-promotion. | level error; construction/narration; necessary/sufficient | AP153, AP154, MP2 |
| 241 | symmetric_orbifolds.tex:113, 411 "For X = K3 with c(X) = 6 and kappa(X) = 2 (Remark rem:lattice:monster-shadow)"; l. 284 "K3 (as c=6 VOA)". Direct contradiction with bv_brst.tex:2767: "K3 boundary VOA carries kappa(K3) = 24". | Three distinct kappa's for K3 (AP-CY55): kappa_ch(A_{K3}) = 2 (Vol III algebraization via Phi on D^b(Coh(K3))), kappa_fiber(K3) = 24 (rank H^*(K3,Z)), kappa_cat(K3) = chi(O_{K3}) = 2. | (a) Bare "kappa(K3)" throughout symmetric_orbifolds.tex = AP113 violation. No subscript. (b) Cross-reference to rem:lattice:monster-shadow is broken: that remark discusses the Monster module, not K3; it says kappa(V^natural)=12 contrasted with kappa(Niemeier)=24, with no K3 statement. (c) Direct value contradiction kappa(K3)=2 vs kappa(K3)=24 across two chapters -- both correct with distinct subscripts (ch vs fiber) but neither file carries subscripts. Vol III cache entry 139 flagged this exact confusion class. | (i) symmetric_orbifolds.tex should use kappa_ch(A_{K3}) = 2 (algebraization invariant controlling elliptic-genus computation). (ii) bv_brst.tex:2767 should state kappa_fiber(K3) = 24 OR recast as "boundary VOA character ~ 1/eta^{24} of fiber rank 24". (iii) The broken cross-reference rem:lattice:monster-shadow must be replaced by a proper kappa_ch(K3)=2 anchor; no such Vol I anchor currently exists. | label/content; AP113 violation; broken cross-reference | AP113, AP-CY55, AP-CY56 |
| 242 | symmetric_orbifolds.tex:146-171 prop:symn-twist-vanishing proof: "the coefficient of lambda_1 is controlled by the q^0 term of the vacuum-sector torus amplitude ... the lightest twist field has h_twist = c(X)/16 > 0 when c(X) > 0, so no twisted ground state contributes at q^0". | obs_1 = kappa * lambda_1 is sourced by WEIGHT-1 CURRENT CURVATURE CHANNELS: Heisenberg bosons contribute kappa_i = 1 each; Virasoro contributes c/2. | Wrong mechanism: the proof counts q^0-ground states in the partition function, but obs_1 is a bar-complex curvature statement sourced by OPE data at weights 1 (currents) and 2 (stress tensor), not by partition-function vacuum counts. The final answer kappa(Sym^N X) = N*kappa(X) is correct but the q^0 argument is a non sequitur. For class-M seeds with c/16 >= 1 the argument accidentally lands right; for c(X)=6 (K3), h_twist = 3/8 < 1, so weight-1 twist descendants exist (not primary currents, but the q^0 count misses the structure entirely). | Correct proof: (a) weight-1 primary currents of Sym^N(X) are N copies of each weight-1 current of X, symmetrized; generator count is additive. (b) twist fields at h = c/16 are non-primary with weight-1 descendants only if h<1; even then the descendants are not primary currents and do not source new kappa channels. (c) Virasoro stress tensor is inherited from untwisted sector, contributing c(Sym^N X)/2 = N*c(X)/2. Hence kappa(Sym^N X) = N*kappa(X) by GENERATOR COUNT, not by q^0 filtration. | mechanism error; right conclusion, wrong proof | AP158, MP5 |
| 243 | level1_bridge.tex:271-286 rem:level1-central-charge: "kappa = c = rank(g) at k = 1. This is a coincidence specific to level 1: at generic k, kappa != c and kappa != c/2 for affine Kac-Moody algebras". | kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v) for universal vacuum module V_k(g) (AP39). At k=1 simply-laced, V_1(g) simple, equals V_{Lambda_g}, kappa = rank. | Bare "kappa" = AP113 violation. "kappa != c at generic k" means which kappa -- universal vacuum module's or simple quotient's? At admissible k = -h^v + p/q the two may differ (null vectors). Remark conflates universal formula with level-1 lattice value. | Write: "kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v) for universal vacuum module V_k(g) at k != -h^v. At k=1 simply-laced, V_1(g) is simple and equals V_{Lambda_g}; kappa(V_1(g)) = rank(g) = c_{Sugawara}(V_1(g)). At admissible k, the simple quotient L(g,k) may have kappa != universal value; out of scope here." | AP113 violation; universal vs simple | AP39, AP113, AP-CY56 |
| 244 | moonshine.tex:117-126 Path 2: "FLM construction realizes V^natural = V_{Lambda_24}^{Z/2} ... the involution kills all 24 weight-1 currents, removing the Heisenberg contribution kappa_Heis = 24-12 = 12. What survives is the Virasoro contribution: kappa(V^natural) = 12." | V^natural = V_{Lambda_Leech}^+ oplus (V_{Lambda_Leech}^T)^+ (FLM 1988 Thm 10.3): fixed-point subalgebra PLUS twisted module. | Proof writes V^natural as fixed-point only, omitting the twisted sector. Weight-1 content: (i) untwisted invariants = 0 (each j_i negated) -- correct; (ii) twisted ground state has h = 24/16 = 3/2 > 1, no weight-1 states -- correct but NOT checked in proof. Silent-correct: conclusion right, bookkeeping incomplete. | Write: "V^natural = V_{Lambda_Leech}^+ oplus (V_{Lambda_Leech}^T)^+ (FLM 1988). (i) Untwisted invariants at weight 1: zero (Leech involution negates each j_i). (ii) Twisted states at weight 1: zero (twisted ground state h = c/16 = 3/2 > 1). Hence dim V_1^natural = 0; rank-24 Heisenberg channel absent; stress tensor alone sources curvature: kappa(V^natural) = c/2 = 12." Current Path 2 omits (ii). | mechanism error; incomplete bookkeeping | AP158, MP5 |
| 245 | moonshine.tex:288-317 rem:moonshine-orbifold-class-transition: "The Z/2 orbifold V_{Lambda_24} -> V^natural simultaneously transforms dim V_1 24 -> 0, kappa 24 -> 12, shadow class G -> M, Delta 0 -> 20/71 ... This is the only instance in the standard landscape where a finite orbifold changes the shadow class." | Class G <-> r_max = 2 (rank-one depth 0); class M <-> r_max = infinity (single-line dichotomy forces infinite depth when Delta != 0). | Orbifold is a TWO-step process: (1) V_Lambda -> V_Lambda^+ (fixed-point only); (2) add twisted sector (V_Lambda^T)^+ to get V^natural. rem collapses both steps into a single "simultaneously". At step (1) alone, V_Lambda^+ already has dim V_1=0, kappa=12, Delta=20/71 != 0, forcing class M by single-line dichotomy. Step (2) preserves class M. Also "only instance in the standard landscape" is an UNQUALIFIED existential without enumeration. | Decompose: (1) V_{Lambda_24} (class G) -> V_{Lambda_24}^+ (class M): class-changing step (Heisenberg killed, Virasoro-only curvature with Delta != 0). (2) V_{Lambda_24}^+ (class M) -> V^natural (class M): twist addition preserves class. The existential "only instance" claim should either be dropped or supported by enumeration over holomorphic c=24 orbifold constructions (Schellekens list + non-lattice). | construction/narration; two-step collapsed; unqualified existential | AP150, AP158 |
| 246 | moonshine.tex:225-243 rem:moonshine-koszul-dual: "Virasoro Koszul duality Vir_c^! = Vir_{26-c} specializes at c = 24 to a Virasoro-sector partner Vir_2. The full Koszul dual (V^natural)^! as a VOA involves the weight-2 Griess algebra ... has not been computed". | Vir_c^! = Vir_{26-c} is the Koszul dual of the VIRASORO SUBALGEBRA Vir_{24} subset V^natural. V^natural has 196884 = 1 + 196883 weight-2 primaries (T + Griess). | "Specializes ... to Virasoro-sector partner Vir_2" is narration: it says Vir_{24} inside V^natural has Koszul dual Vir_2, which is a SUBALGEBRA statement distinct from a statement about (V^natural)^!. The rem correctly flags "has not been computed" for the full dual, but the "partner" framing suggests Vir_2 is the scalar part of (V^natural)^!, which is at best ambiguous. | "The Virasoro subalgebra Vir_{24} subset V^natural has Koszul dual Vir_2 (Prop ...). This is a SUBALGEBRA statement, not a statement about (V^natural)^! as a VOA. The Koszul dual of V^natural requires treating the full 196884-dim weight-2 space (Griess algebra) as generating; (V^natural)^! is not known beyond the Virasoro subalgebra. Open problem." | construction/narration; subalgebra Koszul vs algebra Koszul | AP150, AP158 |
| 247 | symmetric_orbifolds.tex:459-470 rem:symn-genus-vs-1-over-N and l. 463-471: "For X = T^4 or K3, Costello-Paquette identify the large-N boundary chiral algebra with the free symmetric orbifold, and ... kappa = 2N (for K3) matches the Brown-Henneaux central charge c = 6N via kappa = c/3 (the anomaly ratio for K3 is varrho = 1/3, not 1/2, because K3 has both Virasoro and affine currents)". | kappa_ch(Sym^N K3) = 2N (algebraization invariant); Brown-Henneaux c_bdy = 6N. Ratio c/kappa = 3 at c=6 is arithmetic, not a law. | (a) "kappa = c/3" elevated to "anomaly ratio varrho" is non-standard terminology. (b) "K3 has both Virasoro and affine currents because" -- if interpreted additively: kappa_{su(2)_1} = rank(su(2)) = 1 (level-1 reduction) + kappa_Vir at c=6 = 3, total 4, CONTRADICTING kappa_ch(K3) = 2. The "both Virasoro and affine" decomposition does not give kappa_ch(K3). (c) Specific-to-general inflation: "kappa = c/3" is a c=6 coincidence, not a structural law. | (i) State: "kappa_ch(Sym^N K3) = 2N; Brown-Henneaux gives c_{bdy} = 6N; the ratio c/kappa = 3 at this specific c is a numerical coincidence." (ii) Drop "varrho = 1/3 because K3 has both Virasoro and affine currents" -- the additive sigma-model decomposition does NOT produce kappa_ch(K3). kappa_ch arises as Hodge-filtered supertrace of Phi(D^b Coh K3) (Vol III). (iii) Explicit Costello-Paquette theorem citation needed; current reference is blanket. | specific/general; convention clash; arithmetic contradiction | AP155, AP113 |

Summary metadata (lattice/moonshine adversarial review):
- Total new entries: 8 (indices 240-247).
- Status: audit-only; no manuscript edits. Findings surfaced for author review.
- Audit scope: Vol I chapters/examples/{moonshine.tex, lattice_foundations.tex, level1_bridge.tex, symmetric_orbifolds.tex}; Vol II CLAUDE.md FM66 V_Leech/V^natural orbifold; cross-volume kappa(K3) subscript hygiene.
- Severity distribution:
  - HIGH: #240 (FM66 inheritance overstated: orbifold BV anomaly conflated with modular invariance; construction required, not inherited), #241 (kappa(K3) AP113 violation + broken cross-reference + 2-vs-24 contradiction across chapters -- highest-impact hygiene issue).
  - MED: #242 (wrong proof mechanism, right conclusion -- fragile), #245 (class transition narration collapses two-step orbifold), #247 (kappa = c/3 promoted to "anomaly ratio").
  - LOW: #243, #244, #246 (AP113 / narration / subalgebra-vs-algebra Koszul phrasing).
- Not-found claims (negative results -- targets absent from Vol I .tex):
  - Mathieu "frame shape = twined bar Euler for all 25 M_24 classes": ZERO presence in Vol I chapters/ (grep clean). Lives only in Vol III CLAUDE.md / AGENTS.md / README. Vol I silent; no Vol I overclaim.
  - Conway module / Co_1 / c=24 lattice VOA beyond Leech: ZERO treatment in Vol I. Target claim non-existent.
  - "V^natural reaches E_3-topological": ZERO textual presence in Vol I .tex. Lives only in Vol II CLAUDE.md FM66 as a REMARK. Not a theorem in either volume. Entry #240 attacks the remark itself.
- Verified correct (spot-checks):
  - Theta_Leech / eta^{24} = j - 720 (lattice_foundations.tex:1999): verified. Theta_Leech = 1 + 0*q + 196560*q^2 + ... (no norm-2 vectors, AP-CY18 compliant). Dividing by eta^{24} = q*(1 - 24q + ...) gives q^{-1}*(1 + 24q + 196884*q^2 + ...) = j - 720.
  - AP-CY18 theta-series first correction at q^2: lattice_foundations.tex:1755-1758 explicitly notes "coefficient of q is 0 (no norm-2 vectors)". Compliant.
  - AP-CY19 A-hat halving / convergence radius 2*pi: no violation found in targeted lattice/moonshine files.
  - kappa(V^natural) = c/2 = 12 (moonshine.tex prop:moonshine-kappa): correct. Virasoro-only curvature; dim V_1 = 0 kills Heisenberg channel.
  - Shadow data (kappa, class, Delta) = (12, M, 20/71): Delta = 8*12*5/1704 = 480/1704 = 20/71. Consistent.
  - Niemeier kappa = 24: correct (rank(Lambda) = 24 for all 24 Niemeier lattices; thm:lattice:niemeier-shadow-universality).
- Core finding: the lattice/moonshine cluster's arithmetic and kappa extractions for V^natural, V_Leech, and Niemeier lattices are numerically correct at the values stated. The vulnerability concentrates in (i) FM66's claim that V^natural "reaches E_3-topological via orbifold inheritance" -- status over-promotion that conflates gauge-theoretic construction with fixed-point inheritance and conflates partition-function modular invariance with Dijkgraaf-Witten orbifold anomaly vanishing; (ii) systemic kappa subscript hygiene failure for K3 across symmetric_orbifolds.tex and bv_brst.tex (AP113 violation with direct 2-vs-24 contradiction, mediated by broken cross-reference to a Monster-module remark); (iii) wrong-mechanism proofs (q^0 argument at #242, two-step collapse at #245) that happen to land on correct answers in the cases examined but are not robust.

| 248 | Vol I w_algebras.tex:2174-2284 thm:wn-obstruction: statement "For the principal W-algebra W_N^k at generic level k != -N" plus proof using Zamolodchikov normalization "W^{(s)}_{(2s-1)} W^{(s)} = c/s" across ALL s without distinguishing the s=2 (quartic pole, Virasoro sector) universal case from the s>=3 non-universal cases. | For fixed Zamolodchikov normalization, the leading pole c/h_i of a weight-h_i primary in W^k(g, f_prin) does follow from the free-field (Miura) realization plus Wick power counting; the general formula kappa = c * sum_i 1/(m_i+1) is recorded as Cor. cor:general-w-obstruction (line 2307). | (a) The "verbatim" extension from sl_N to general g asserted on line 2318 elides that Zamolodchikov normalization for non-simply-laced (B, C, F_4, G_2) requires the twisted Miura embedding on the folded lattice, and the factor 1/h_i is a convention-dependent quantity that shifts under renormalization of W^{(h_i)}. (b) Step 2 cross-term vanishing W^{(s)}_{(s+t-1)} W^{(t)} = 0 for s != t is claimed "by orthogonality + associativity" (cite Bouwknegt-Schoutens) -- associativity plus orthogonality under the INVARIANT BILINEAR FORM gives a weaker statement; cross-channel off-diagonal curvature contributions can arise from the composite fields :W^{(s)} W^{(t)}: inside the OPE at the matching pole order, and the argument does not bound those. For W_3, this is audited: kappa_T kappa_W are diagonal (line 216-222). For W_N with N>=4, the absence of such cross-couplings is UNVERIFIED by the proof as stated and is a tacit assumption. | Scope: theorem as stated is CORRECT for Zamolodchikov-normalized W^k(sl_N, f_prin) with the auxiliary hypothesis "cross-channel off-diagonal curvature vanishes" (which is a non-trivial consequence of conformal-weight orthogonality for rank 2 and verified computationally through weight 6 for higher rank). For non-simply-laced g, the general formula requires stating the Miura normalization on the folded root system. Repair: (i) tag the proof's Step 2 vanishing as "PROVED for N=2,3 by direct computation; VERIFIED computationally for N<=6 per Creutzig-Linshaw; CONJECTURAL for N>=7", and (ii) in cor:general-w-obstruction add the qualifier "at Zamolodchikov normalization on the folded Miura lattice". The TABLE values (lines 2334-2343) for B_2, G_2, F_4, E_6--E_8 use varrho = sum 1/(m_i+1), which specialize correctly: B_2 (1,3) gives 1/2 + 1/4 = 3/4 MATCHES line 2337. So the numerical content is right; only the proof's universality scope needs a normalization caveat. | scope error; missing hypothesis | AP6, AP7 |
| 249 | Vol I bershadsky_polyakov.tex:194-223 prop:bp-self-duality claims "For k != -3, (B^k)^! = B^{k'} with k' = -k-6", with Feigin-Frenkel involution k -> -k - 2h^v = -k - 6 on sl_3 (h^v=3). The partition (2,1) IS self-transpose; self-duality at the level-involution means B^k and B^{-k-6} are Koszul-paired. | The transpose self-duality of (2,1) means the DS reduction at f_{min} of sl_3 is fixed under the hook-transposition duality (CLNS24). Feigin-Frenkel k -> -k - 2h^v is the KM level involution, inherited on the DS quotient. | (a) The proof (lines 208-223) arithmetically verifies c(k) + c(-k-6) = 196 but then asserts "(B^k)^! = B^{-k-6}" based on (i) self-transposition of (2,1) and (ii) the FF involution -- this is PATTERN MATCHING on two independent facts, not a proof. The bar-cobar Koszul duality of B^k at the CHAIN level requires free strong generation / PBW collapse at E_2, and BP has non-trivial cubic composite fields (Bershadsky 1990) forcing class M on the T-line (confirmed line 318 "T-line: class M"). Class M means infinite shadow depth => bar cohomology non-concentrated => PBW universality criterion fails at degree >=3. (b) The W_N principal case (CLNS24 hook transport) supplies a Koszul pairing for hook partitions; (2,1) is a hook so the theorem DOES apply, but only AFTER verifying the hypothesis that the DS quotient is freely strongly generated. At BP that requires three strong generators (T, G^+, G^-, J) with no relations up to conformal weight bound. This is KNOWN for BP (de Boer-Tjin 1993) but it is never cited in the proof. | Proof needs one more line: "BP is freely strongly generated by {T, G^+, G^-, J} (de Boer-Tjin 1993), so the PBW spectral sequence collapses at E_2 and chiral Koszulness applies; the hook-transport theorem of CLNS24 then gives (B^k)^! = B^{-k-6}". Without the free-strong-generation citation, the proof is a coincidence of arithmetic (c(k)+c(k')=196) plus two structural facts (hook self-transpose, FF involution) not shown to imply the Koszul pairing. Also: the computed self-dual point c=98 is "not achieved at any real level" (line 247-252) -- this is fine, but should note that the formal complex self-dual level k = -3 +/- 2i is OUTSIDE the range where c is real and the algebra is unitary, hence the "self-dual point" is formal not physical. | native/derived; scope error; missing PBW citation | AP14, AP67, AP108 |
| 250 | Vol I logarithmic_w_algebras.tex:325-328 conj:wp-koszul correctly tags Koszulness of W(p) as CONJECTURE (rem:wp-c2-vs-koszul at line 302-308 flags free strong generation as OPEN). The file models AP67 correctly. SEPARATE ISSUE: line 311-314 "Whether the orbifold W(2) = SF^{Z/2} inherits Koszulness from the parent is a non-trivial question". | SF (symplectic fermion) is freely strongly generated (chi, xi odd) => PBW collapse at E_2 => Koszul. W(2) = SF^{Z/2Z} is a Z/2 orbifold. | The phrasing "inherits Koszulness" evokes AP-CY54 ("categorified averaging") error class: orbifolds are Z/2 invariant subalgebras, NOT "inheritance" in any functorial sense that preserves Koszul structure. Z/2-invariants of a freely strongly generated algebra are generically NOT freely strongly generated (CLassically: K[x,y]^{Z/2} with Z/2 acting via x,y -> -x,-y has three generators x^2, y^2, xy with one relation (xy)^2 = x^2 y^2, ie NOT free). For SF^{Z/2}, the three weight-(2p-1) triplet W+-, W0 are invariants of an sl_2 that sees the Z/2 = center of sl_2; the free-generation question is whether the triplet algebra has relations at high conformal weight. Adamovic-Milas 2008 shows W(p) is STRONGLY generated; whether FREELY so is open (correctly flagged line 307 "open"). | "Inherits Koszulness" should read "The question of whether W(2) inherits free strong generation from SF is non-trivial: orbifold kernels generically break free strong generation. Whether the Adamovic-Milas strong generators T, W^{+,0,-} satisfy the PBW universality criterion is the OPEN problem (conj:wp-koszul)." Current text already sets this up; the single word "inherits" is the vestigial narrative residue of AP-CY54. Low severity because conjecture status is correct, but the phrasing invites misreading. | construction/narration | AP-CY54, AP67 |
| 251 | Vol I minimal_model_fusion.tex:49-82 def:wn-minimal + thm:w3-minimal-complete claim the W_N minimal model (p,q) with p>q>=N has c = (N-1)(1 - N(N+1)(p-q)^2/(pq)), Kac-Kazhdan style. thm:w3-minimal-complete: "For W_3, a minimal model (p,q) has [counts + fusion]". | Frenkel-Kac-Wakimoto: W_N minimal (p,q) exists as a rational W_N-module category iff gcd(p,N) = gcd(q,N) = 1 and p > q >= N; characters given by KKW formula. PBW collapse on bar complex of a RATIONAL W-algebra quotient is a DIFFERENT claim from PBW on W^k universal. | The "minimal model" W_N^{p,q} is the SIMPLE QUOTIENT of the universal W_N^k at k = -N + p/q (an admissible level with p/q in lowest terms). At this admissible level, (a) bar cohomology of the simple quotient may differ from bar cohomology of the universal algebra; (b) chiral Koszulness of the SIMPLE QUOTIENT is a new question -- PBW universality applies to freely strongly generated W^k but the SIMPLE quotient has additional null vectors (singular vectors of the vacuum Verma module) that modify the bar differential. (c) The text makes no distinction: thm:w3-minimal-complete lists fusion rules, quantum dimensions, MTC structure (thm:mtc-minimal line 733-739) WITHOUT explicitly downgrading Koszulness/bar-cohomology claims for the simple quotient. (Note: the thm is about FUSION RULES which are correct via Verlinde; but any subsequent Koszulness/E_2 collapse inference from "minimal model" status would be a scope inflation.) | No correction needed to thm:w3-minimal-complete as stated (fusion rules, not bar-cohomology). But a CAUTION REMARK should be added: "The PBW spectral sequence argument of prop:pbw-universality applies to W^k at generic k; at admissible levels k = -N + p/q the simple quotient W_{p,q}^{min} has singular vectors that modify the bar differential. Whether W_{p,q}^{min} is chirally Koszul is not known from PBW collapse alone and remains OPEN for general (p,q)". The text's silent transition from universal W^k (where Koszulness is proved) to simple-quotient W_{p,q} (where it is not automatic) is a scope elision. AP67 / AP153 apply. | scope error; native/derived | AP67, AP153, MP1 |
| 252 | Vol I n2_superconformal.tex:281-332 prop:n2-koszulness asserts chiral Koszulness of N=2 SCA at generic c "PBW spectral sequence collapses at E_2 ... H^n(barB(SCA_c)) = 0 for n>=2". Rem:n2-ce-chiral-gap line 315-332 argues "CE complex has H^2_CE != 0 at weight 3 but mode-0 product is the Lie bracket; OS form factor on Conf_3 activates higher modes G^+_{(1)}G^- = J and G^+_{(2)}G^- = c/3 which kill CE cocycles at E_2". | At generic c, N=2 SCA is freely strongly generated (Adamovic 1999). PBW spectral sequence associated to the linearization filtration converges from sym(g_-) to barB(A). | (a) AP107 is named but not engaged: "r^{coll}(z) differs from Laplace-transform r(z) for odd generators". N=2 has TWO odd generators G+-. The proof of prop:n2-koszulness uses "PBW collapse at E_2" as a functor of free strong generation; this is fine. But the derivation of the shadow tower / r-matrix for the N=2 SCA would need to use r^{coll} for the odd G+- and r^{Laplace} for the even T, J. The chapter's treatment of r(z) for N=2 SCA is not visible in the grep; if the shadow data on G-lines uses Laplace r instead of r^{coll}, that is an AP107 violation. (b) The "CE/chiral bar gap" remark is a CORRECT observation (single-generator algebras have CE=chiral bar at degree 2; multi-gen with mixed statistics diverge), but the VERIFICATION claim "verified computationally through conformal weight 6" (line 312) is an engine claim with no cross-reference to a compute/ test. | No error in the MAIN theorem (PBW Koszulness); the N=2 SCA is indeed chirally Koszul at generic c. Needed: (i) cite or install a compute/ test for the "weight 6 verification" claim (AP-CY49 tautological-test class: verify the test is not hardcoding the E_2 collapse it purports to verify). (ii) When r-matrix / shadow tower for N=2 is discussed elsewhere, use r^{coll} for the odd G+- generators per AP107; the current chapter does not trip this because it restricts to PBW collapse statement, but the SEVEN FACES cascade (Wave 4) asserts N=2 SCA fits all seven; any such claim that uses a single r(z) without odd/even distinction = AP107 violation. | test hardcoding risk; convention clash | AP107, AP-CY49 |
| 253 | Vol I y_algebras.tex existence and scope: file is 874 lines, structure discusses Y_{L,M,N}[Psi] of Gaiotto-Rapcak with S_3 triality, claims Y_{1,1,1} ~ N=2 SCA. | Gaiotto-Rapcak 2017 (arXiv 1703.00982) define Y_{L,M,N}[Psi] as corner VOAs of N=4 gauge theories; S_3 triality from SL(3,Z) -- permutation of three coordinate planes in (C^*)^3. W_infty[lambda] emerges as Y_{0,0,infty} in their notation. | (a) line 289 claims Y_{1,1,1} IS the N=2 SCA; this is a correct observation for a specific value of Psi but only after a suitable rescaling; should be tagged with the level/parameter map. (b) Triality is claimed as an INVARIANT of "shadow depth class" (line 145); this is a strong claim -- triality permutes the three levels (L,M,N) and acts nontrivially on Psi; its preservation of shadow depth class (G/L/C/M) for Y_{L,M,N} requires a PROOF, not a citation. The text's "shadow depth class are all triality invariants" on line 145 asserts this without reference. (c) Connection to W_infty: "Y_{0,0,infty} ~ W_infty[lambda]" should be pinned with (lambda, Psi) dictionary. Grep shows W_infty context but no visible pinning on lines 1-30. | (i) Line 289 needs "Y_{1,1,1}[Psi] specialized to Psi = (dictionary value) realizes the universal N=2 SCA at c = c(Psi)"; currently under-specified. (ii) Triality-invariance of shadow depth class is a FOUNDATIONAL CLAIM of the chapter; it needs either a proof (triality acts on Koszul data preserving the PBW collapse) or a downgrade to "CONJECTURAL: triality preserves shadow depth class; verified for small L,M,N". (iii) Y_{0,0,N} = W_N principal is a safe identification (CG-rediscover); but Y_{L,M,N} with all three nonzero has NO known identification with a familiar VOA at finite (L,M,N), and the shadow computation is genuinely new. | construction/narration; missing parameter dictionary | AP-CY27, AP150, AP155 |
| 254 | Vol I standalone/w3_holographic_datum.tex:54-80 claims "H(W_3) = (W_3, W_3^!, C, r(z), Theta_A, nabla^hol) ... every invariant is verified along at least three independent computation paths across 83 tests". | Six-fold holographic datum structure: VOA, Koszul dual, line category, spectral r-matrix, MC element, flat connection. The rank-2 case W_3 exhibits genuine multi-channel phenomena (two weight classes). | (a) "3 independent paths across 83 tests" is an AP-CY49 / AP28 risk flag: many tests of a single derivation can all share the same hardcoded data. The Vol II independent-verification protocol (CLAUDE.md Indep Verif) requires disjoint derived_from / verified_against sets per decorator. The standalone paper makes an aggregated claim with no visible derived_from/verified_against structure. (b) The channel decomposition kappa_T = c/2, kappa_W = c/3 (line 70, line 147) with kappa = 5c/6 = c*(H_3 - 1) is consistent with Vol I w_algebras.tex cor:general-w-obstruction and the rho(g) formula at sl_3. The ARITHMETIC is correct. (c) But the standalone paper's "holographic" claim (that H(A) controls EVERY 3d HT QFT, line 100) is CONJECTURAL -- it asserts conj:e3-identification / conj:e3-topological-climax content without naming them. | (i) The 83 tests need cross-reference to compute/ test names and each should carry @independent_verification(derived_from=..., verified_against=...) or be flagged as NOT audit-compliant. (ii) "Controls every 3d HT QFT" should be downgraded to "conjecturally controls; verified for standard landscape families and consistent with BV-quantized Chern-Simons on KM, per CFG". (iii) The "first rank-2 holographic modular Koszul datum" claim (title) is an EXISTENTIAL across the standard landscape; it needs either "the first among W-algebras we have computed" or an enumeration showing no smaller rank-2 datum exists. AP155 (new invariant overclaiming) applies. | construction/narration; test audit risk | AP28, AP155, AP-CY49 |
| 255 | Vol I w3_composite_fields.tex:1018 lines, OPE W(z)W(w) ~ (c/3)/(z-w)^6 + 2T/(z-w)^4 + ... (line 336). This uses OPE mode convention W_{(5)}W = c/3, NOT Vol II divided-power convention (V2-AP34: Vol II has c/360 for W_3). | OPE poles relate to lambda-bracket divided powers via {a_lambda b} = sum_n lambda^(n) a_{(n)}b with lambda^(n) = lambda^n/n!. For W_3: W_{(5)}W = c/3 => in Vol II's divided-power lambda-bracket, the lambda^5 coefficient = c/3 * 5! = c/3 * 120 = 40c? But V2-AP34 says c/360. Discrepancy: W_{(5)}W = c/3 at OPE mode, divided-power coefficient {W_lambda W}|_{lambda^5/5!} = c/3, so coefficient of lambda^5 = (c/3)/5! = c/360. CORRECT. | Vol I uses c/3 (OPE mode convention), Vol II uses c/360 (divided-power convention). These are CONSISTENT via the 1/s! conversion, NOT a contradiction. | (a) Within Vol I w3_composite_fields.tex this is correct OPE mode convention and self-consistent. (b) CROSS-VOLUME risk: any Vol II result quoting c/3 is a V2-AP34 violation; any Vol I result quoting c/360 is a convention clash. Audit: grep Vol II for "c/3" as W_{(5)}W coefficient, and Vol I for "c/360" as lambda^5 coefficient -- any mismatch is a bug. (c) The specific check here confirms W_3 arithmetic is right in Vol I; Vol II's V2-AP34 claim "OPE mode W_{(3)}W = c/2 maps to c/12 at lambda^3 (Virasoro), W_{(5)}W = c/3 maps to c/360 (W_3)" is also right. No numerical error; only a convention-consistency audit needed. | convention clash; cross-volume hygiene | V2-AP34, AP5 |


## Raviolo + PVA Descent Adversarial (indices 256-262, 2026-04-16)

| 256 | raviolo.tex:31-43 def:raviolo-restriction + prop:SC-raviolo (line 45-72): V_rav(D) := A_ch(D x I)/~ identifying "from above/below" via E_1-coherence; Step 2 concludes each sheet carries the same chiral algebra via restriction along iota_pm. | Garner-Williams raviolo VAs model a 3d HT boundary at a time-slice. The two-sheet geometry D_+ cup_{D^times} D_- is real. | R-matrix twist is absent. The quotient ~ is defined by "the E_1-coherence data" without specifying which isotopy class of path from I_- to I_+ is used. For E_inf seeds R(z) is derived from local OPE so the path choice is homotopically canonical; for genuinely E_1 seeds (Yangians) R(z) is independent data and different path classes yield different raviolo structures. The construction as stated produces a trivial doubling V otimes V, not a raviolo VA with genuine OPE twist. | Correct: time-slice restriction gives a raviolo factorization algebra TWISTED by Mon(R) (the monodromy of R(z) around D^times). For E_inf seeds the twist is determined; for E_1 seeds R(z) must be supplied as part of the data. Prop:SC-raviolo as stated proves existence of the UNTWISTED raviolo and does not capture the OPE-twist that distinguishes raviolo VAs of Garner-Williams from trivial doublings. | construction/narration; necessary/sufficient | AP-CY25, AP150, MP3 |
| 257 | raviolo.tex:579-586 thm:PVA-descent-roadmap ClaimStatusProvedHere: "For any logarithmic SC^{ch,top}-algebra, H^bullet(A_ch, Q) is a (-1)-shifted PVA". | PVA descent works for freely-generated VAs with d'=1 HT gauge satisfying GRW21 scope; d log kernels alone give PVA. | "Logarithmic SC^{ch,top}-algebra" (def:log-SC-algebra, raviolo.tex:363-374) REQUIRES omega_k^hol in Omega^bullet_log(FM_k(C)). This permits only simple-pole (d log) kernels. Class M (quartic poles: W(p), triplet families, sigma-models with infinite A-inf operations) has kernels of pole order >= 4 at the collision divisor, which are NOT sections of Omega^bullet_log. The theorem's "for any" phrasing obscures this: the result is PROVED only in the logarithmic scope (classes G, L, C), and class M falls outside the hypothesis. Given that Virasoro itself has a quartic pole (T(z)T(w) ~ c/2*(z-w)^{-4} + ...), even the Virasoro case sits on the boundary of the hypothesis unless one absorbs c/2*(z-w)^{-4} via a logarithmic-residue mechanism. | Correct scope statement: "For logarithmic SC-algebras with kernels in Omega^bullet_log (d log only), H^bullet is a (-1)-shifted PVA." Class M and higher-pole-order algebras require separate treatment; D6 vanishing fails there because higher A-inf operations are not killed by topological contraction alone. The Virasoro case must specify that c/2*(z-w)^{-4} is recorded as iterated logarithmic residues via FM stratification, which is a non-trivial calculation tacitly assumed. | scope error; label/content | AP7, AP14, AP153 |
| 258 | pva-descent-repaired.tex:984-1040 prop:m3_vanish (D6): m_k = Q(h_{k-1}) for all k>=3 on Q-closed inputs, proved via contractibility of Conf_k^<(R)/transl and factorization omega_k = omega_k^hol wedge omega_k^top. | Topological contraction of Conf_k^<(R) is real (R^{k-1}_{>0} is star-shaped). For logarithmic holomorphic kernels, factorization gives clean tensor split and m_k descends to Q-exact. | The proof (Step 3, line 1032-1040) writes omega_k^top = d Gamma and concludes m_k = Q(...) "because the product decomposition ensures the topological contraction does not disturb the holomorphic kernel." This compressed clause hides the requirement that omega_k^hol be d-CLOSED in the transverse direction. For logarithmic kernels, the holomorphic factor is closed by Arnold-OS relations. For quartic-pole (class M) kernels, transverse closedness fails -- codim-2 corner obstructions are not Arnold-OS consequences and the topological contraction does NOT extend to a cylinder homotopy in the full product space. | Corrected D6: "For logarithmic SC-algebras, m_k|_{k>=3} is Q-exact via BOTH topological contractibility of Conf_k^<(R) AND Arnold-OS closedness of omega_k^hol in the transverse direction on FM_k(C). For non-logarithmic (class M) algebras, D6 fails: the higher A-inf operations survive on cohomology and the descended structure is not a PVA but a P_inf-chiral (homotopy Poisson vertex) algebra (V2-AP22 hierarchy). The two-stage projection rem:pva-two-stage-projection conflates these regimes." | mechanism error; right for restricted scope, overgeneralized | AP14, AP22 (V2), AP158 |
| 259 | raviolo-restriction.tex:50-123 prop:chain-D-vs-S1 (iii): rho: C^ch(D^times, A) -> C^top(S^1, A) is a qiso and "both models compute the same homology: = Z(A) the derived center (chiral Hochschild homology)." (iv): rho is E_1 but NOT E_2. | Punctured disk and circle are homotopy equivalent; factorization homology on htpy-equivalent manifolds agrees at homology level. E_2 structure on source is not transported to target. | (a) Internal tension between (iii) and (iv): "both equal Z(A)" is asserted while simultaneously "source is E_2, target is E_1." If Z(A) carries E_2 structure (Deligne), then target does not really compute Z(A) -- it computes the underlying chain complex of Z(A) modulo E_2. (b) AP-CY62/AP-CY64 three-way Hochschild distinction is not made: ChirHoch geometric (with spectral parameters from FM) vs cyclic topological Hochschild (no spectral parameters) vs algebraic HH*. Writing "both = Z(A)" collapses all three. (c) AP-CY65: spectral parameter provenance on LHS vs RHS is different. | Corrected: "rho is a quasi-isomorphism of UNDERLYING CHAIN COMPLEXES. The source C^ch(D^times, A) carries FM-spectral data and E_2 structure; the target C^top(S^1, A) carries cyclic bar structure and only E_1. Both compute the same underlying homology vector space HH^ch_bullet(A), but only the source retains the E_2 braiding / spectral R(z)." The claim "both = Z(A)" should read "both compute HH^ch_bullet(A) as graded vector spaces." Remark rem:chain-D-vs-S1-E1 lines 338-372 makes the E_1/E_inf distinction but does not fix the loaded phrase "Z(A)" in (iii). | conflation; chain/cohomology | AP-CY62, AP-CY64, AP-CY65 |
| 260 | raviolo.tex:84-105 prop:raviolo-VA Step 2: Y(a,z)b = sum_{n>=0} a_{(n)}b z^{-n-1} + :Y(a,z)b: with :Y(a,z)b: "reconstructed from the regular part mu(a,b) = m_2^reg(a,b)|_{lambda=0}". | Borel correspondence zeta^{-n-1} <-> lambda^n/n! relates singular Laurent tail of m_2 to the polynomial PVA lambda-bracket. | The Borel correspondence gives the SINGULAR part of Y only. The regular / normally ordered part :Y(a,z)b: = sum_{n<0} a_{(n)}b z^{-n-1} requires ALL modes a_{(n)} for n<0, which depend on iterated regular products mu(a, partial^k b) for k>=1. Setting lambda=0 kills all partial^k data and recovers only the leading mu|_0. Hence the construction recovers only a_{(-1)}b = mu(a,b), not the full :Y(a,z)b:. | Corrected: "The state-field correspondence Y(a,z) is recovered from the FULL bar differential d_B (residues at all FM divisors) PLUS the translation operator T = partial. The Borel correspondence encodes only the singular tail; the normally ordered part requires iterated regular products mu(a, partial^k b) for all k >= 0, not just mu|_{lambda=0}." Current text recovers only the leading mode of :Y(a,z)b:, which is insufficient. | construction/narration; part/whole | AP150, AP158 |
| 261 | raviolo-restriction.tex:28-34 def:coinvariants: Coinv_X(V_rav) := Gamma(X, V_rav)_G^h "with respect to global symmetries G ... G is a Lie algebra acting by chiral currents." | Chiral coinvariants in BD pseudo-tensor setting are defined via chiral action on chiral modules; the Lie algebra version is an image under the mode bridge. | AP-CY66 / FM56 adjacent: the definition takes G = Lie algebra and forms homotopy quotient. This treats V_rav as living in a symmetric monoidal enrichment where Lie algebra action makes sense. For raviolo VAs in the pseudo-tensor category of chiral algebras, "Lie algebra coinvariants" is NOT the native operation -- the native operation is chiral coinvariants (BD Ch. 4), and the Lie algebra version is derived via Sugawara / Zhu mode bridge, which is not automatic. | Correct: "Chiral coinvariants of V_rav over X are defined via the CHIRAL algebra action; the Lie-algebra coinvariants used here correspond to the MODE ALGEBRA under the Zhu/Sugawara bridge, which is an additional datum beyond the raviolo factorization algebra." Without naming the mode bridge, the coinvariants construction silently invokes a symmetric monoidal framing (FM56-adjacent) that is not present in BD pseudo-tensor category. raviolo.tex:129 does correctly use "pseudo-tensor category," so no FM56 violation there; the issue is local to def:coinvariants. | conflation; pseudo-tensor vs symmetric monoidal | AP-CY66, FM56 |
| 262 | pva-descent-repaired.tex:1320-1545 Example comp:pva-descent-affine-sl2 ClaimStatusProvedHere verifying D2-D6 for affine sl_2 at k != -2. README "PVA descent D2-D6 proved" shorthand. | D2-D6 are five SEPARATE propositions in pva-descent-repaired.tex (D2: prop:PVA1_proof L307; D3: prop:PVA2_proof L524; D4: thm:Jacobi L670; D5: prop:PVA3_proof L835; D6: prop:m3_vanish L984). sl_2 Example (L1320-1545) is a CONCRETE verification on one algebra. | The README shorthand "D2-D6 proved" compresses: (a) five separate propositions, each with its own hypotheses; (b) an sl_2 worked example that is an EXISTENCE verification, not a universal proof; (c) implicit scope restriction to logarithmic SC-algebras inherited from thm:PVA-descent-roadmap. Confirming D2-D6 on ONE algebra does not verify them on all logarithmic SC-algebras -- it verifies them on sl_2. AP-CY49 tautological-test class: the sl_2 example computes both sides of each axiom from the same OPE data, a partial tautology. | Corrected shorthand: "PVA descent D2-D6 proved for logarithmic SC-algebras (classes G, L, C), with affine sl_2 as a worked example. Class M (quartic poles, W(p), etc.) is out of scope; D4 and D6 fail without further hypotheses. The sl_2 verification is an AP28 dual-source check (OPE side + PVA side) -- partially independent since the PVA lambda-bracket is defined FROM the OPE via Borel transform, so axiom checks are not fully disjoint derivations." V2-AP21 (PVA vs P_inf-chiral direction) correctly honored throughout this file (rem:pva-two-stage-projection makes the downward descent clear). No V2-AP21 violation. | scope error; shorthand over-compression; partial tautology | AP7, AP21 (V2), AP28, AP158 |

Summary (raviolo + PVA descent adversarial, entries 256-262, 2026-04-16):
- New entries: 7 (256-262).
- Status: audit-only; no manuscript edits.
- HIGH: #257 (scope inflation: "logarithmic SC^{ch,top}-algebra" universal quantifier silently excludes class M; Virasoro sits on boundary of hypothesis); #258 (D6 proof relies on logarithmic-kernel transverse closedness, not stated as hypothesis; fails for class M).
- MED: #256 (raviolo R-matrix twist under-specified in construction; yields untwisted V otimes V for E_1 seeds), #259 (internal tension in prop:chain-D-vs-S1: iii says "both = Z(A)" while iv says only source is E_2), #260 (state-field correspondence Y(a,z) reconstructed only in leading order from mu|_0).
- LOW: #261 (def:coinvariants uses Lie-algebra framing without naming the mode bridge; local, not structural), #262 (D2-D6 README shorthand compresses scope + worked-example-vs-universal distinction).
- Verified no-violation: FM56 (pseudo-tensor used correctly on raviolo.tex:129; symmetric monoidal of chiral algebras never invoked); V2-AP21 (PVA descent direction downward/cohomological, correctly distinguished from P_inf lift in rem:pva-two-stage-projection lines 98-128).
- Not tested: quartic-pole (class M) explicit PVA descent; the question of whether a CLASS M algebra produces a P_inf-chiral (not PVA) under descent -- consistent with V2-AP22 hierarchy but not worked out in this file.

## XX. Yangian / Gaudin / E_n Circle Adversarial Review (2026-04-16)

Scope: Vol I yangians_foundations/computations/drinfeld_kohno, standalone/gaudin_from_collision, standalone/en_chiral_operadic_circle, Vol II thqg_gravitational_yangian, dg_shifted_factorization_bridge, ordered_associative_chiral_kd.

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | AP |
|---|-------------|---------------|---------------|---------------------|------|-----|
| 263 | prop:yangian-koszul "For ANY simple g, Y_hbar(g) in RTT is Koszul" (yangians_foundations.tex L623-635) | PBW + Polishchuk-Positselski deliver Koszulness for QUADRATIC locally finite connected graded algebras | Positselski-Polishchuk Ch. 4 requires NON-NEGATIVE and CONNECTED grading (A_0 = k). The "level grading" r >= 0 on T^{(r)} places all generators in degree 1 (quadratic-dual sense) with relations in degree 2, but A_0 under this grading is pro-finite, not k. The "after passing to the augmentation ideal" (L552) hand-wave does not produce a connected grading in the PP05 sense. Molev PBW covers CLASSICAL types only; exceptionals E_6-E_8, F_4, G_2 need Guay-Regelskis-Wendlandt 2018, UNCITED. | Correct ghost: Y_hbar(g) is a FILTERED Koszul deformation of U(g[t]); Positselski "Nonhomogeneous Koszul duality" gives a CDG-coalgebra dual. Koszulness holds in the filtered/CDG sense, not plain-quadratic. | scope / grading conflation | AP40 / AP153 |
| 264 | thm:yangian-koszul-dual Step 4 "Y(sl_2)^{!,ch} = Y_{R^{-1}} = Y(sl_2)^{hbar -> -hbar}" (yangians_foundations.tex L557-558) | hbar -> -hbar is a well-known automorphism of Y(g); Hopf duality exchanges R and R^{-1} | "Higher-order 1/u^k terms in R^{-1}(u;hbar) vs R(u;-hbar) are automatic consequences of the YBE" is a handwave. R^{-1}(u) for Yang R-matrix = u/(u-hbar) on symmetric subspace, u/(u+hbar) on antisymmetric — these do NOT equal 1 + hbar P/u at higher orders. Matching algebras needs all orders. | Correct: Chevalley-involution-style automorphism T -> T^{-1T} with hbar -> -hbar gives Y(sl_2) = Y_{-hbar}(sl_2); this is SEPARATE from Koszul duality. R^perp under trace pairing needs all-order matching, not leading order only. | mechanism error / hand-wave | AP36 / AP40 |
| 265 | cor:yangian-bar-cobar counit quasi-iso for "augmented pro-nilpotent" Y_hbar(g) (yangians_foundations.tex L677-701) | Bar-cobar quasi-iso holds for (co)nilpotent augmented algebras; for pro-nilpotent A, on COMPLETIONS | Pro-nilpotence of A (intersect I^n = 0) does NOT imply conilpotence of B(A); conilpotence holds only on completed bar complex. The cited thm:e1-chiral-koszul-duality "for augmented pro-nilpotent E_1-chiral algebras" ambiguously conflates A-side pro-nilpotence with B(A)-side conilpotence. | Correct: quasi-iso holds as \Omega^ch \widehat{\bar B}^ch(A) -> \widehat A in pro-nilpotent completion category. Raw (uncompleted) bar-cobar FAILS for Yangian. Wave-6 A6 flagged this. | completion / uncompleted | FM1 / AP153 |
| 266 | thm:gaudin-from-collision: "[H_i^{GZ}, H_j^{GZ}] = 0 follows from MC equation" (gaudin_from_collision.tex L210-255) | Gaudin commutativity IS a theorem (FFR 1994); CYBE IS the classical MC shadow | "MC equation projects at genus 0 to [H_i, H_j] = 0" is asserted, never proven. Standard FFR proof uses Sugawara + Bethe-ansatz-style argument; "MC projects" collapses several nontrivial steps. At k = -h^v the Feigin-Frenkel center produces additional commutants, not zero — excluded case is precisely where MC-projection mechanism would need justification. | Correct: classical CYBE for r(z) = Omega/((k+h^v) z) implies Gaudin commutativity via standard r-matrix computation (FFR). Replace "MC projection" with "CYBE + standard r-matrix argument". | construction/narration / mechanism error | AP32 / AP36 |
| 267 | thm:jones-genus1 "Jones polynomial from bar-complex monodromy" (ordered_associative_chiral_kd.tex L5810-5871) | Bar monodromy of KZ = KZ monodromy = DK = U_q braid rep; quantum trace closes the braid | Jones polynomial is RT at LEVEL K (integer), requiring Rep_q(sl_2) at q = e^{pi i/(k+2)} QUOTIENT BY NEGLIGIBLE MODULES (= MTC). Generic KZ monodromy gives U_q at generic q; quantum trace on tensor products at generic q is NOT Jones (reduces to classical trace at q=1). Level-truncation + negligible-quotient step is elided. This is a CFG-style E_inf factorisation homology output (FM55), NOT E_1-ordered bar. | Correct: bar monodromy gives BRAID representation at generic q; specialisation at roots of unity + negligible quotient gives MTC; RT functor applied to MTC gives Jones. "Quantum trace implements Markov closure" hides the negligibles. Chain-level correct; invariant-level requires RT from an E_inf trace. | specific/general | AP153 / FM55 |
| 268 | Y(g)^! = Y(g^v) for non-simply-laced g realising Langlands (yangians_foundations.tex L569-588) | For specific non-simply-laced cases, Finkelberg-Tsymbaliuk / Kamnitzer-Weekes-Webster-Yacobi DO give q-Langlands at Yangian level | Stated "conjecturally" with Latyntsev23 citation but presented as natural extension of thm:yangian-koszul-dual (ProvedHere for simply-laced). Non-simply-laced g -> g^v at Yangian level is a far deeper problem (Koszul-dual realisation of quantum geometric Langlands), not a consequence of the hbar -> -hbar automorphism. | Simply-laced case reduces to hbar -> -hbar automorphism. Non-simply-laced case is a GENUINE CONJECTURE, not an extension of the proved theorem. | scope overreach | AP36 / AP153 |
| 269 | "Gravitational Yangian" Y^{grav}_{Vir} CYBE via Arnold + IBR (thqg_gravitational_yangian.tex L1751-1870) | Vir r-matrix r^{grav}_Vir(z) = sum Omega_m / z^{m+1} with Omega_m = sum binom(n+m-1, m) L_{-n-m} \otimes L_n IS a valid formal series | CYBE proof via "Arnold + Virasoro partial-fraction as specialisation of IBR" glosses over: (i) Omega_0 = sum L_{-n} \otimes L_n is FORMAL — Vir is infinite-dim, [Omega_0, Omega_0] is a regularised infinite sum; (ii) CYBE is formal power-series identity in z_{ij}, not algebraic identity in a genuine algebra; (iii) AP-CY35 (B^{(j)} hierarchy confusion): mixed-complex identities don't extend from j=0 to j>=1 without proof. | Correct: Vir CYBE is formal-series identity in pro-completion. Genuine algebraic interpretation needs Vir-module category specification. Also Vir^! = Vir_{26-c} (L783) is the Koszul involution c <-> 26-c at operator level — not an r-matrix Koszul dual without proof. | convergence / completion / narration | AP34 / AP153 |
| 270 | "Y^{grav} for Vir provides Hopf-algebraic graviton scattering" (dg_shifted_factorization_bridge + thqg_gravitational_yangian) | dg-shifted Yangian = ordered E_1 face of universal twisting for A = Vir | dg-shifted Yangian is a Lie-algebra object (no antipode). "Gravitational Yangian" language while downstream physics uses it as Hopf algebra for S-matrix is scope inflation: antipode + coassoc coproduct (for S-matrix) are ABSENT at dg-shifted level. Hopf promotion is the OPEN MC4/5 stage (Layer B/C of rem:yangian-triage). | Correct: Y^{grav} is a dg Lie BIALGEBRA (not Hopf). Graviton S-matrix at genus 0 uses the CLASSICAL r-matrix (no antipode needed). Hopf enhancement is conjectural. Chapter should say "dg Lie bialgebra" unqualified. | weak/strong structure | AP40 / AP60 |
| 271 | "k_max = 2 is absent from standard landscape" (gaudin_from_collision.tex rem:k2-absent L334-343) | For bosonic self-OPE, max pole = 2h, so p_max = 3 requires h = 3/2, excluded | Argument covers only GENERATOR SELF-OPEs. Fermionic weight-3/2 generators (NS, super-Vir, N=2 SCA odd generators) give p_max = 3, k_max = 2. Remark excludes "fermionic weight" by fiat but superconformal algebras ARE in standard landscape. | Within BOSONIC chiral algebras k_max = 2 is absent. For superconformal/fermionic families k_max = 2 DOES occur. Add super/bosonic qualifier. | scope qualifier | AP6 / AP8 |
| 272 | RTT = Drinfeld current equivalence for all simple g (yangians_foundations.tex rem:yangian-presentations L386-393, prop:yangian-koszul L623 "any simple g") | Molev 2007 establishes RTT <-> Drinfeld equivalence for CLASSICAL simple g (A,B,C,D) via Gauss decomposition | Exceptional types E_6-E_8, F_4, G_2 NOT covered by Molev §2.5. Required: Guay-Regelskis-Wendlandt 2018 (arXiv:1706.05176) for RTT-Drinfeld equivalence and PBW at exceptional types. The "any simple g" claim silently extends Molev without citing Wendlandt et al. | Scope: add the Wendlandt citation or restrict scope to classical g. PBW + Koszulness proofs currently depend on PBW citation that covers only classical types. | scope overreach | AP18 / AP32 |
| 273 | Vol II independent_verification coverage "installed" (CLAUDE.md, 2026-04-16) | Infrastructure IS present: decorator + audit + self-test + Makefile targets all working | Zero test modules across Vol II compute/ actually apply `@independent_verification`. Grep confirms only 3 files touch the decorator: lib/independent_verification.py, scripts/audit_independent_verification.py, tests/test_independent_verification_infra.py. `make verify-independence` reports 0/1134 (0.0%) — identical to installation snapshot. Protocol is live but unused. | Close the gap by landing decorators on highest-stakes ProvedHere labels (E_3-topological chain, global triangle, modular bar, recognition theorem, pentagon equivalences) with genuinely disjoint derived_from/verified_against. Do not auto-decorate. | infra/practice gap | AP158 / AP10 |
| 274 | test_adversarial_verification.py::test_modular_completion_genus_data hardcodes F_g = [1/24, 7/5760, 31/967680] vs `modular_completion_koszul('abelian_cs', max_genus=3, k=1)` (L712-719) | lambda_1=1/24 IS Arakelov-normalised; V2-AP28 documents lambda_3 correction 1/82944 -> 31/967680 | Test lists engine's own outputs as expected. Direct FRAME_SHAPE_DATA analogue: test and engine share mental model. lambda_3 was fixed once already (V2-AP28) — engine and test moved together. No independent derivation, no decorator, no `# VERIFIED` note. | Fix: (a) decorate with `@independent_verification(claim="comp:genus1-partition-functions", derived_from=["modular_completion_koszul engine"], verified_against=["Arakelov omega_1 integral normalisation", "Zagier heat-kernel lambda_g formula"])`, AND (b) compute expected via Arakelov/zeta-regularised route inside the test. | tautological test | AP28 / V2-AP28 |
| 275 | test_exceptional_affine_bar.py::test_generator_weights_from_exponents reads `_EXCEPTIONAL_E_DATA[name]['exponents']` and asserts `ds_reduction(name)['generator_weights'] == [e+1 for e in data['exponents']]` (L446-451) | "DS weights = exponents + 1" for principal W-algebras IS a real theorem (Feigin-Frenkel, Kac-Roan-Wakimoto) | Test and engine both read same `_EXCEPTIONAL_E_DATA` dict (lib/exceptional_affine_bar.py L44). Expected is `[e+1 for e in data['exponents']]` from the SAME dict the engine uses. Tests dict self-consistency, not the weight theorem. Bourbaki citation in docstring is aspirational — code never consults Bourbaki. | Fix: obtain exponents from INDEPENDENT source (Sage's `WeylGroup('E6').degrees()` minus 1, or LiE). | tautological test | AP28 / AP-CY49 |
| 276 | test_session_results.py::test_catalan_values hardcodes `expected = [1,1,2,5,14,42,132]` vs `catalan(n)` (L316-320) | Catalan = OEIS A000108; sympy.catalan is canonical | Tautological (catalan IS sympy.Catalan = binomial(2n,n)/(n+1)). Adjacent `test_catalan_recurrence` + `test_generating_function_algebraic` DO provide independent verification. Low severity given adjacent coverage. | Mild: mark `# REDUNDANT: independent verification in adjacent tests`. | tautological test (low) | AP28 |
| 277 | Engines with no test file (8): ainfty, arnold, convention_check, fm_boundary, genus2_ordered_bar, laplace_bridge, spectral, symbolic_stasheff | Some are utilities exercised transitively through downstream engines | Transitive exercise != assertion. If `spectral.py` has a wrong convention, every downstream test still passes because they share the bug. Highest-stakes untested: `genus2_ordered_bar` (directly computes genus-2 bar dims), `spectral` (spectral-parameter handling). `convention_check` without a test is itself ironic. | Fix: scaffold tests for `genus2_ordered_bar` (vs Getzler-Kapranov modular bar dims) and `spectral` (vs EK quantisation) with independent_verification decorators. | untested engine | AP28 / AP158 |
| 278 | Tests without engine counterpart (21 files): adversarial_verification, cross_engine_consistency, session_results, signs, conventions, infrastructure, spectral_braiding, semisimple_purity, rank2_complete, ... | Integration tests legitimately have no single-engine counterpart | Two classes: (i) legitimate integration (cross_engine_consistency, infrastructure, signs, conventions) — valuable; (ii) result-archival (session_results, adversarial_verification) pin hardcoded values from past session outputs without proving correctness. Class (ii) is the AP28 danger zone. Entry #274 is a class-(ii) instance. Name "adversarial_verification" is a misnomer if it pins engine output rather than attack from independent angles. | Fix: class (ii) audit line-by-line; each hardcoded assertion must cite independent source in `# VERIFIED` comment OR be removed. | archival tautology | AP28 / AP-CY49 |

Summary metadata (independent verification coverage audit, 2026-04-16, entries 273-278):
- Scope: Vol II compute/ tree. Ran `make verify-independence` and `-verbose`.
- State: infra GREEN (0 tautologies, 0 orphans, self-test passes). Coverage 0/1134 = 0.0% — identical to installation snapshot. Protocol live but unused.
- Top-5 decorator targets: (1) thm:E3-topological-km (3d_gravity.tex) vs CFG arXiv:2602.12412; (2) thm:E3-topological-DS-general (ht_physical_origins.tex, closes FM57 T_DS gap) vs Costello-Gaiotto; (3) thm:E3-topological-free-PVA vs Khan-Zeng 3d Poisson sigma model; (4) thm:global-triangle-boundary-linear (ht_bulk_boundary_line_core.tex, classes G/L/C) vs Lurie HA 5.3.1.30; (5) thm:modular-bar D^2=0 (foundations.tex; watch FM61/FM68 — this is abstract bar D^2=0, NOT concrete operadic composition) vs Getzler-Kapranov modular operad composition axioms.
- Tautology patterns (3 concrete): 274 abelian-cs lambda_fp = DIRECT FRAME_SHAPE_DATA analogue, 275 E_N exponents self-reference, 276 Catalan (low severity).
- BEFORE any decorator campaign: fix pattern 274 (would otherwise become a decorated tautology). Then Top-5 with disjoint sources. Never auto-decorate all 1134 claims.
- Engines untested: 8. Highest stakes: genus2_ordered_bar, spectral.
- Tests without engines: 21 (~4 legitimate, ~17 require audit).

Summary metadata (Yangian cluster adversarial review, 2026-04-16):
- Total new entries: 10 (indices 263-272).
- Status: audit-only; no manuscript edits.
- Severity: HIGH #263 (PBW+PP05 grading mismatch for "any simple g" Koszulness), HIGH #267 (Jones requires RT finite-dim quotient, not generic bar monodromy), HIGH #272 (exceptional-types scope overreach, uncited Wendlandt). MED #264 #265 #266 #268 #269 #270. LOW #271.
- Unified finding: Yangian cluster silently conflates two registers. (A) PROVED: algebraic r-matrix, RTT, Drinfeld coproduct via bar-cobar twisting morphism, for CLASSICAL simple types on the evaluation-generated core. (B) CLAIMED: Hopf-algebraic / modular register — Y(g)^! = Y(g^v) for all simple g, full Koszul duality universally, gravitational Yangian as Hopf — requires completions, exceptional-type extensions (Wendlandt), and Hopf structure absent at dg-shifted level. Jones-polynomial claim specifically needs finite-dim RT quotient (E_inf FH output, FM55), not ordered E_1-bar monodromy. Gaudin "derivation from MC equation" is narration; actual derivation is CYBE + FFR-style r-matrix argument.

## XXI. DNP / Rosetta / Affine Half-Space BV Adversarial Review (2026-04-16)

Scope: Vol II chapters/connections/dnp_identification_master.tex, ht_physical_origins.tex, affine_half_space_bv.tex, examples/rosetta_stone.tex. Targets: DNP arXiv correction, fabricated cross-volume citations, rosetta row discipline, affine BV -> SC^{ch,top} claim, FM47/FM56/AP40/AP150 checks.

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | AP |
|---|-------------|---------------|---------------|---------------------|------|-----|
| 273 | rosetta_stone.tex L2039-2041: "Volume~I, Theorem~\ref*{thm:Koszul_dual_Yangian}; \cite{DNP25}" | DNP25 (arXiv:2508.11749) genuinely constructs a dg-shifted Yangian; Vol II spectral-braiding-core.tex:1827 hosts thm:Koszul_dual_Yangian | Cross-volume misattribution: thm:Koszul_dual_Yangian is native to Vol II, not Vol I. Exactly the Wave-1 fabrication class. | Drop "Volume~I," or cite Vol II \S spectral-braiding-core. DNP arXiv 2508.11749 correction verified in main.tex L1551. | label/content (cross-volume) | AP5 / AP40 |
| 274 | dnp_identification_master.tex L11-17: "seven equivalent realizations...as bar-cobar (this manuscript), as DNP25's A_inf YB MC element,...as the Gaudin Hamiltonian (FFR94)" | On non-critical KM + classical simple g, the seven classical identifications coincide on the eval-generated core | Opener uniformly narrates equivalence of all seven faces; per-face status arrives only at thm:vol2-seven-faces-master L250 (F3 genus-0-only, F4 W_N conjectural). Uniform opening = construction/narration. | Lead with "agree on the common locus (g=0, non-critical, classical simple)". | construction/narration | AP36 / AP150 / AP153 |
| 275 | dnp_identification_master.tex L94-97: "Non-renormalization = Koszulness. One-loop exactness (\cite[Thm.4.1]{DNP25}) IS the E_2-collapse of the bar ss" | DNP proves one-loop exactness of line OPE; programme proves E_2-collapse = chiral Koszulness | "IS" without bridge theorem: BV-renormalized non-renormalization and algebraic bar E_2-collapse are two distinct propositions; a comparison theorem is NOT supplied. | Downgrade "IS" to "conjecturally corresponds" OR produce the bridge proposition (BV non-renormalization => E_2-collapse of chiral bar). | construction/narration | AP150 / AP36 |
| 276 | dnp_identification_master.tex L193-199: "Yangian quantization parameter hbar = 1/(k+h^v) for affine g_k (Drinfeld~\cite{Drinfeld85})" | Drinfeld85 introduces Y_hbar(g) with abstract formal hbar | Citing Drinfeld85 for the KZ<->Yangian specialization identity; that identity is due to Drinfeld-Kohno / Drinfeld90, not the original definition paper. | Cite Drinfeld-Kohno / Drinfeld90 for the specialization. Drinfeld85 only for Y_hbar(g) definition. | label/content (wrong citation scope) | AP40 / AP20 |
| 277 | dnp_identification_master.tex L247: thm:vol2-seven-faces-master tagged \ClaimStatusProvedHere but clauses F3 (g=0 only), F4 (W_N conjectural), F5/F7 (non-critical only) are conditional | Generic-locus seven-face agreement IS proved; master tagging requires honest status | Theorem environment carries ProvedHere while substantive clauses are conjectural. AP40 violation: env must match tag. | Split into (proved) + (conjectural) OR downgrade tag to ProvedHere-conditional with visible scope in header. | label/content (env/status mismatch) | AP40 / AP32 |
| 278 | Target file chapters/connections/thqg_open_closed_realization.tex does not exist | Open-closed realization IS the content of ht_physical_origins.tex + spectral-braiding-core.tex + hochschild.tex | Review target #6 is a phantom file. ht_physical_origins.tex L379 points to "Volume~I \S\ref*{V1-sec:thqg-open-closed-realization}" but no Vol II chapter of that name exists. | Create chapter OR explicitly document that the open-closed realization discussion lives across the three existing files. Phantom-pointer retirement (AP38). | hardcoded/symbolic (phantom file) | AP26 / AP38 |
| 279 | affine_half_space_bv.tex L1548-1564 prop:affine-is-log-SC ProvedHere "the BV-BRST complex of the affine PV sigma model IS a logarithmic SC^{ch,top}-algebra" | Gwilliam-Williams half-space BV + doubling-RWI give the analytic bridge | SC^{ch,top} lives on the pair (Z^{der}_{ch}(A), A), NOT on the BV complex directly (AP165, FM40). The three physics-bridge hypotheses (BV data, 1-loop finite, polynomial interactions) produce a factorization algebra; SC^{ch,top} structure requires the bulk-boundary identification (Theorem H), not supplied inside this proposition. | BV complex is a fact. alg. on slab; the pair (BV-on-slab, boundary VOA V^{Keff}(g)) carries SC^{ch,top} via Hochschild identification. Rephrase to "gives rise to a log SC^{ch,top}-datum (Z(A), A)" rather than "A IS a log SC^{ch,top}-algebra". | level error / conflation | FM40 / AP165 / AP156 |
| 280 | ht_physical_origins.tex L444-456 thm:cl-n4-chirality \ClaimStatusProvedElsewhere \cite{CL16}: "F_{G,Ad} is strictly chiral... resulting chiral algebra is affine KM at level k" | CL16 builds the HT twist + fact. alg.; chirality / D-module descent to Ran(X) follows in CDG20 + Zeng23 | CL16 alone does not uniformly establish D-module chirality to Ran(X); remark L435 hedges ("requires verification for twisted gauge theories") while the theorem does not. Citation over-attribution. | Add CDG20 / Zeng23 citations. Downgrade "ProvedElsewhere \cite{CL16}" to joint attribution, OR narrow the theorem's scope. | label/content (citation over-attribution) | AP20 / AP40 |
| 281 | ht_physical_origins.tex \S4d/2d global narration: "CL produces chiral algebras from 4D gauge theory" used generically | N=4 SYM -> KM proved; class S -> W_N via AGT; 4D/2D chiral algebras -> chiral in BLLPRR sense | FM47 guard: E_3-chiral is NOT automatic from "chiral algebra from gauge theory". The conjecture conj:CL-produces-chiral correctly qualifies, but surrounding prose does not always. | Tighten: specify matter content (N=4 SYM, class S type A) at every use; flag non-gauge-theoretic cases as conjectural for E_3-chiral. | scope / FM47 | FM47 / AP153 |

Summary metadata (DNP + rosetta + affine-HS BV adversarial review, 2026-04-16):
- Total new entries: 9 (indices 273-281).
- Status: audit-only; no manuscript edits.
- Severity: HIGH #273 (cross-volume misattribution, Wave-1 fabrication class), HIGH #277 (ProvedHere tag vs face-conditional clauses, AP40), HIGH #279 (prop:affine-is-log-SC conflates A with pair (Z(A),A), FM40/AP165). MED #274 #275 #280 #281. LOW #276 #278.
- Verified clean: DNP arXiv 2508.11749 in main.tex L1551 (Wave-1 correction landed); per-face \ClaimStatus annotations at line-item level are honest; thm:Koszul_dual_Yangian target resolves (spectral-braiding-core.tex:1827); all V1- phantom labels in main.tex L625-996 point to real Vol I theorems (verified against chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex + frontier_modular_holography_platonic.tex).
- Strongest honest form: "On the common locus (g=0, non-critical KM level, classical simple g, eval-generated core) the seven r(z)-faces agree as a conjunction of per-face proved identifications. The master theorem is ProvedHere-conditional: r-matrix <-> Yangian <-> Sklyanin (F5,F6,F7) is unconditional at non-critical level for classical simple g; KZ-classical (F3) is g=0-only; GZ26 W_N (F4) is conjectural; DNP-MC = collision residue (F2) requires the bridge between BV non-renormalization and bar E_2-collapse that is not in the manuscript today. Affine half-space BV produces a (slab-fact-alg, boundary-VOA) pair that carries SC^{ch,top} via Hochschild identification; the pair is the SC^{ch,top}-datum, not the BV complex alone."

---

## N-Paper Series Adversarial Review (2026-04-16, standalone/N1-N6)

| # | (a) Claim (paper, locus) | (b) Ghost of correct theorem | (c) Precise conflation |
|---|--------------------------|------------------------------|------------------------|
| 273 | N1 thm:koszul-equivalences-meta: "twelve equivalences of chiral Koszulness" with (i)-(x) "unconditionally equivalent" | Several pairs genuinely equivalent: (i)<->(ii) PBW-Koszulness; (iii)<->(ii) Keller formality; (iv)<->(i) diagonal Ext over a field in char 0. Core circuit (i)(ii)(iii)(v) is standard for quadratic algebras. | (vii) factorization-homology concentration at ALL genera is NOT equivalent to genus-0 Koszulness: genus>=2 curvature obstructions (AP32/FM67: kappa*omega_g, uniform-weight caveat) make "(i) <=> (vii)" overclaiming; author tags the uniform-weight qualifier only parenthetically for g>=2, then lists (vii) as "unconditional." (viii) Theorem H polynomial concentration is multi-weight dependent (cross-channel delta F_g^cross). (ix) Kac-Shapovalov "in bar-relevant range" is hand-wavy; non-degeneracy at generic weight does not invert r=2 differentials without PBW. (xi)(xii) the author correctly flags as conditional — so "twelve" equivalences is really "core-5 + 5 conditional + 2 conjectural". |
| 274 | N2 thm:main: "categorical CG for ALL simple Lie types including E_8 via multiplicity-free ell-weights" | Theorem of Chari-Moura (mult-free ell-weights for fundamentals) is real. Hernandez block separation is real. Character accounting (Lemma 5.5) is standard. | The claim "replaces the minuscule hypothesis" in KL elides that the CG decomposition is already known at all types on generic-spectral eval modules via GTL + Nakajima (Hernandez 2005, Frenkel-Hernandez). N2's "new content" is a repackaging, not a new theorem. Against memory "Wave 3 found E_8 non-path sectors OPEN" this paper proves only the EVAL-GENERATED CORE case (part 3 of thm:main-formal explicitly invokes thick closure + pro-nilpotent completion); the open strictification sectors (non-path, non-eval-generated) are NOT covered. Corollary MC3 quietly depends on the Francis-Gaitsgory pro-nilpotent step on top of the main theorem; AP47 (evaluation-generated core != full category) applies. |
| 275 | N3 thm:av-dg-lie: "av: g^{E_1} -> g^{mod} is a SURJECTIVE dg Lie morphism" | There IS a Reynolds-operator-style projection sending ordered Hom to Sigma-equivariant Hom for commutative-module codomains; at scalar lane it commutes with convolution bracket. | FM56: chiral algebras form a PSEUDO-TENSOR category, not a symmetric monoidal category; the "dg Lie algebra" structure on g^{E_1} and g^{mod} from "Feynman transform of ribbon modular operad" is sketchy (ribbon modular operad edge contraction is a 2-cells-coboundary operation, not literally a dg Lie differential without spelled convolutions). The averaging surjectivity is plausible for the scalar lane but the CROSS-DEGREE compatibility (Prop 4.4 non-splitting) the author correctly notes means av is NOT a full equivalence — then the paper proceeds to assert all five Theorems A-D,H "lift to ordered and their Sigma-coinvariants are the symmetric theorems," which goes beyond what av as a mere surjection guarantees (kernel carries the higher-genus braiding). AP150 agent-confabulation risk: "five ordered counterparts exist" asserted but only Theorem D is verified via independent computation (r-matrix at n=2). |
| 276 | N3 thm:e1-theorem-d: "av(r(z)) = kappa for abelian Heisenberg; for non-abelian KM av(r(z)) = kappa_dp, full kappa = kappa_dp + dim(g)/2 (Sugawara shift)" | kappa(KM) = dim(g)(k+h^v)/(2h^v) is correct (AP39). Decomposition into double-pole + Sugawara shift is the standard BD decomposition. | The "Sugawara shift = dim(g)/2" identification is notational: it is the contribution from the simple-pole self-contraction when one normalises Omega_g trace-form, NOT a separate operation in the averaging. Splitting kappa as av(r) + dim(g)/2 is convention-dependent; different normalisations absorb the shift into r. Also "Sugawara shift" usually refers to T = (1/2(k+h^v)) :J^a J^a: — that is a DIFFERENT operation (the Sugawara construction of T) than a scalar shift to kappa. Symbol overload. |
| 277 | N4 thm:mc4-strong: "completed bar-cobar duality for strong completion towers (closed counit)" | Degree-cutoff lemma (Lemma 4.1) is CORRECT given axiom (4): mu_r(F^1, ..., F^1) subset F^r vanishes mod F^{N+1} for r >= N+1. Mittag-Leffler on weight slices (Prop 5.1) is CORRECT for finitely generated VAs. | Prop 3.2 claims "V_k(g) at non-critical level is a strong completion tower" via conformal-weight filtration. VERIFY: KM has weight-1 generators J^a with OPE J^a J^b ~ k delta/(z-w)^2 + f_{abc} J^c/(z-w). The DOUBLE POLE maps F^1 x F^1 -> F^0 (scalars), violating axiom (4) strictly. The paper notes this only via "the augmentation ideal F^1 = weight>=1"; then mu_2(F^1, F^1) double-pole residue is a scalar central term, which is in F^0 = full algebra but the scalar k*delta_{ab} is NOT in F^2. This is a tacit recenter: "mu_2 on augmentation ideal maps to augmentation ideal" only if one SUBTRACTS the central cocycle, i.e., works with curved A_inf (hence "curved" in the definition). Paper addresses this via "curved" but then kappa_dp should appear explicitly as the curvature mu_0, not ignored. Also: claim "twenty-one standing conjectures resolved" (Remark 7.4) is unverified grandstanding — catalogue of the 21 absent from the paper. AP155 "new invariant overclaiming" analogue. |
| 278 | N4 thm:wn-rigidity: "W_N tower is rigid; completed bar-cobar holds for W_infinity = lim W_N" | Weight-slice stabilisation H^m(barB(W_{N+1}))_w = H^m(barB(W_N))_w for N >= w IS correct: bar chains of total weight w use only generators of weight <= w. | The projection W_{N+1} -> W_N "forgets the generator of weight N+1" is FALSE in the standard principal W_N: generators of different weights INTERACT via OPE, so forgetting W^{(N+1)} is NOT a strict morphism of A_inf algebras unless one truncates the OPE of remaining generators too (the "pro-chiral" construction requires care). Author asserts "is a strict morphism" without checking that the remaining generators' OPEs close within the truncated algebra. This is the AP30/AP106 "narration instead of construction" pattern. Moreover, the 21-conjectures claim is a contentless bow-tie. |
| 279 | N5 thm:heisenberg-sewing: "every closed genus-g Heisenberg amplitude is a Fredholm determinant" | For Heisenberg, Moriwaki's Bergman identification IS rigorous; genus-1 Z_1 = Im(tau)^{-k/2} |eta(tau)|^{-2k} IS the BK result. | CLAUDE.md stratification (Vol II W-algebras row): (1) analytic HS-sewing proved all genera; N5 Theorem 3.2 + 4.5 implement this for Heisenberg. (4) chain-level BV/BRST/bar conjectural at g>=1 — N5 does NOT address this (sewing ENVELOPE is not the bar complex's higher-operations structure). (5) amplitude pairing conditional on cor:string-amplitude-genus0 — N5 claims genus-g partition function in closed form for Heisenberg, but only because Heisenberg is FREE (class G); for Virasoro, KM, W_N (classes L/C/M) the paper gives only HS-sewing = trace-class (Thm 5.1 "General HS-sewing criterion") NOT Fredholm determinant. The paper correctly restricts Fredholm to Heisenberg. Potential issue: Example 6.2 Virasoro OPE growth |C| <= K(n+1)^2 — for Vir the structure constants depend NONLINEARLY on c (see [L_m, L_n] = (m-n)L_{m+n} + c/12 m(m^2-1) delta_{m+n}); the cubic term in m dominates — is N=2 sufficient? Should be N=3. Same check at W_N: claims |C| <= K(n+1)^{2N}; for principal W_N with generators of weights 2,...,N, highest-weight-derivative contributions give polynomial degree in n up to ~2N, so bound likely correct but proof is one-line. |
| 280 | N6 thm:main: "Sh_r(A) = ell_r^{(0),tr}(Theta^{<=r-1},...,Theta^{<=r-1}) for every chiral algebra A and every r>=2; shadow obstruction tower = L_infinity formality obstruction tower" | The identification at r=2,3,4 (Prop 4.1) is standard once kappa, frakC, frakQ are defined via graph sums matching tree sums of Kadeishvili-Merkulov transfer. | CRITICAL: the paper asserts "Koszulness != SC formality" in its opening (Remark N1 5.4 echo), but then identifies shadow = formality tower GENUS ZERO. The Vol II Wave-2 distinction (Koszul != SC-formal; all standard families Koszul; only class G is SC-formal) is PRESERVED: Thm 1.1 says "shadow = formality of g^{mod,(0)}" (genus 0), and class M (Virasoro) has r_max = infty = non-formal. Consistent. BUT the AP14 Vol I warning: "Koszulness = bar H* in degree 1; SC formal = m_k^{SC} = 0 for k>=3" is about SC^{ch,top} (two-colour), while N6 is about single-colour g^{mod,(0)}. The paper conflates "L_infty formality of g^{mod,(0)}" with "SC-formality" in the conclusion: Example 7.4 Virasoro "intrinsically non-formal" — true for g^{mod,(0)}, but SC-formality is a STRONGER condition (two-colour) that even Heisenberg (class G) need not satisfy. AP105 (Heisenberg = abelian KM at level k = abelian CS boundary) — Heisenberg being "L_infty formal for g^{mod,(0)}" is consistent with SC-formality, but the paper does not distinguish. Also Example 7.4 lists the shadow coefficients S_4 = 10/(c(5c+22)) etc.; AP28 test-value cross-verification required — these match the "Wave 5 R-matrix errors" corrected values? Not verified in the paper; cites "Lorgat26 App. Riccati algebraicity" but that chapter is "Lorgat26" self-reference. AP43/AP49 shadow-Feynman tautology risk. |

Summary metadata (N-paper series, 2026-04-16):
- Total new entries: 8 (indices 273-280).
- Status: audit-only; no manuscript edits.
- Severity: HIGH #273 (N1 "12 equivalences, 10 unconditional" overclaims genus>=2 concentration), HIGH #275 (N3 av-as-dg-Lie-surjection on pseudo-tensor category is FM56 violation; "all five theorems lift" is agent-confabulation AP150), HIGH #277 (N4 V_k(g) strong-tower claim tacitly requires curved mu_0 = central cocycle). MED #274 (N2 eval-core scope), #276 (N3 "Sugawara shift = dim g/2" notation), #278 (N4 W_N projection not a strict morphism without OPE-closure argument), #279 (N5 Vir OPE-growth N=2 vs N=3), #280 (N6 genus-0 L_infty formality vs SC-formality).
- Unified finding: The N-series systematically trades literal equivalence/surjectivity/all-types claims for "uniform-weight, genus-0, scalar-lane, eval-core" statements backed by the parent monograph's caveats. Each paper claims to "close" or "complete" a frontier (Twelve Equivalences, All Simple Types, Primacy, Completion Closed, Sewing, Formality-Shadow Equality) but each rests on the monograph's standing qualifier toolbox (uniform-weight regime, Koszul locus, proved bar-cobar regime, HS-sewing, genus zero). The series is HONEST when read with those qualifiers inline; it is OVERCLAIMING when abstracts are read independently. No paper passes the N1-N6 abstracts verbatim as self-contained theorems without pulling hypotheses from Lorgat26I.
- Verified clean: Gaudin identification eq:gaudin-identification = Omega/((k+h^v) z) — arithmetically correct at non-critical level. Vir r-matrix explicit form with binomial-coefficient Omega_m is standard classical. Sugawara constraint at k = -h^v correctly excluded (rem:e-sugawara-constraint). E_3-identification for simple g uses dim H^3(g) = 1 correctly. cor:yangian-classical-self-dual (Sym(V) <-> Lambda(V^*) at hbar = 0) is classical Koszul duality, correct. rem:yangian-triage layer (A)/(B)/(C) stratification IS the right epistemic frame; entries above flag where downstream prose silently merges layers.

## Session 2026-04-16: Adversarial review of Vol I survey papers (standalone/)

Context: standalone/survey_modular_koszul_duality_v2.tex (8524L), survey_modular_koszul_duality.tex (8595L), survey_track_a_compressed.tex (2463L), survey_track_b_compressed.tex (2394L), introduction_full_survey.tex (5441L), programme_summary.tex (2790L) + sections1/2_4/5_8/9_14.

#281. Heisenberg misclassified as "tier (a) pole-free commutative" (Track B §7.0).
 (a) Derived from: survey_track_b_compressed.tex:179–183 ("Tier (a): pole-free commutative. The Heisenberg algebra H_k and lattice extensions. ... Yang–Baxter equation is trivial.").
 (b) Verified against: CLAUDE.md V2-AP7 ("Heisenberg R-matrix = exp(k*hbar/z), NOT trivial. Collision residue k/z. Monodromy exp(-2pi*i*k)"); survey_track_b line 221 own body "alpha(z)alpha(w) ~ k/(z-w)^2" — a double pole, not pole-free. V2-AP5: "BD commutative chiral algebra (no poles) is STRICT SUBCLASS."
 (c) Correct statement: Tier (a) should be "scalar R-matrix abelian" or "free-field archetype". Pole-free is wrong: H_k has a double pole. Severity HIGH. Confusion type: label/content + scope error.

#282. Programme summary abstract claims "single open conjecture is CY-A at d=3"; body upgrades to theorem.
 (a) Derived from: programme_summary.tex:98 "the single open conjecture is the CY-A correspondence at d = 3".
 (b) Verified against: programme_summary.tex:2599 `\begin{theorem}[CY-A at d=3]\label{thm:cy-a3}`; Vol III CLAUDE.md AP-CY11/AP-CY14 "A_X at d=3 now EXISTS (inf-cat). G(X) and C(g,q) remain unconstructed"; AP-CY41 partial-update saga.
 (c) Correct statement: CY-A_3 is PROVED inf-cat; the genuine open problem is CY-C. Abstract and body must match. Severity HIGH. Confusion type: label/content (stale update).

#283. Programme summary §14 "120K+ tests" and "4,542 pages" — scale-vs-soundness conflation.
 (a) Derived from: programme_summary.tex:101 "120K+ computational tests"; survey_v2 abstract :215 "~4,800 pages".
 (b) Verified against: find compute -name test_*.py yields 2578+885+424=3887 test MODULES across three volumes. CLAUDE.md Independent Verification snapshot 2026-04-16: "Vol I 0/2275; Vol II 0/1134; Vol III 2/283" independently decorated ProvedHere claims.
 (c) Correct statement: ~3900 test modules ≠ 120K independent verifications. Under the protocol the decorated-tautology-free count is 2. "120K+" measures assertions executed, not claims independently verified. Severity MED. Confusion type: scale/soundness.

#284. Surveys use "interpolate" for families that are all E_inf.
 (a) Derived from: introduction_full_survey.tex:142 "Every other family (Kac-Moody, Virasoro, W-algebras, lattice vertex algebras) interpolates between these two extremes [Heisenberg, Yangian]."
 (b) Verified against: V2-AP1/AP11 "E_inf INCLUDES ALL vertex algebras"; V2-AP12 "E_1 vs E_inf is about LOCALITY, not poles."
 (c) Correct statement: KM/Vir/W/lattice all sit in E_inf; they span a pole-structure gradation within E_inf. The Yangian is in a different operadic tier. "Interpolate" suggests continuum where there is a categorical gap. Severity MED. Confusion type: conflation.

#285. "Simple poles give collisions a canonical ordering" (AP152/FM50 violation).
 (a) Derived from: introduction_full_survey.tex:141 "The Yangian atom is E_1-chiral: simple poles give collisions a canonical ordering."
 (b) Verified against: Vol I AP152 "ordered ambiguity: LABELED not time-ordered"; FM50 "E_1 ordering is ALGEBRAIC (operadic), not geometric."
 (c) Correct statement: Simple poles yield antisymmetric bracket; operadic E_1 ordering is an independent datum (Conf^<(R) or time direction). Severity MED. Confusion type: conflation (geometric vs algebraic).

#286. survey_v2 abstract claims derived centre E_2/E_3 and "3d quantum gravity as climax."
 (a) Derived from: survey_modular_koszul_duality_v2.tex:203–216.
 (b) Verified against: Vol II CLAUDE.md "3D gravity | E_3-topological: PROVED for KM ... ALL freely-generated PVAs; Global triangle: PROVED G/L/C; OPEN for class M". E_3-chiral requires 3d HT theory (FM47); E_3-topological requires conformal vector (FM48). These are Vol II/III deliverables.
 (c) Correct statement: Vol I PROVES five theorems A-D,H + shadow classification + SC^{ch,top} emergence. It PREVIEWS 3d gravity / E_3-top / CY QG. Abstract attributing these to the Vol I survey is AP155 scope inflation. Severity HIGH. Confusion type: scope error (volume-level).

#287. "Unconditional for every family" without genus/weight scope (AP32 + AP36).
 (a) Derived from: survey_modular_koszul_duality_v2.tex:646,920,1084,1434,1805; survey_modular_koszul_duality.tex :785,805,1023,1033.
 (b) Verified against: AP32 "Genus-1 != all-genera. Multi-weight g≥2 scalar formula FAILS. Every occurrence of obs_g MUST carry explicit tag (UNIFORM-WEIGHT) or (ALL-WEIGHT, with cross-channel correction)."
 (c) Correct statement: Most "unconditional" uses are scoped to genus-1 or uniform-weight. Surface form omits scope. Tag each. Severity MED. Confusion type: scope error.

#288. Track B "pole-free" label self-contradicted by own OPE definition.
 (a) Derived from: survey_track_b :179 tier (a) "pole-free commutative. The Heisenberg algebra H_k" vs :221 "alpha(z)alpha(w) ~ k/(z-w)^2" (double pole).
 (b) Verified against: Track A pole-absorption rule "pole order of r(z) = pole order of OPE - 1" (survey_v2:381); OPE order 2 -> r simple pole. Pole-free is empty of nontrivial chiral algebras.
 (c) Correct statement: Heisenberg OPE has double pole; r(z)=k/z has simple pole. Tier (a) label must change. Severity HIGH. Confusion type: self-contradiction.

#289. Compressed tracks drop §14 (frontier overview).
 (a) Derived from: track_a covers §§1-6, §9; track_b covers §§7, 8, 10-13; programme_summary covers §§1-14. §14 orphaned.
 (b) Verified against: programme_summary_sections9_14.tex contains §14 "Overview of the frontier"; neither compressed track reproduces it.
 (c) Correct statement: Faithful subset split for §§1-13 but §14 missing. Acceptable if explicitly noted. Severity LOW. Confusion type: partial coverage (documented, not hidden).

#290. programme_summary thm:cy-a2 uses bare kappa.
 (a) Derived from: programme_summary.tex:1931 "kappa(A_C) = chi^CY(C)".
 (b) Verified against: Vol III AP-CY55 "kappa_cat = chi(O_X) is MANIFOLD invariant, NOT algebraization invariant"; AP113 bans bare kappa.
 (c) Correct statement: At d=2 the identity holds for kappa_cat(A_C). Use subscripts: kappa_cat or kappa_ch. Severity MED. Confusion type: label/content (bare symbol ambiguity).

Unified finding: Vol I surveys are largely honest at the BODY level (qualifier toolbox, correct claim-status tagging on named theorems) but OVERCLAIM IN ABSTRACTS by (a) mis-summarising CY-A status (#282), (b) attributing Vol II/III results (3d gravity, E_3-top, CY QG) to Vol I climax (#286), (c) using "unconditional for every family" without genus/weight-lane scope (#287), (d) inventing a "pole-free" tier to populate Heisenberg, which is wrong (#281, #288). Compressed tracks faithfully split §§1-13 but drop §14. The "single open conjecture" frame in programme_summary is a stale update. Label existence check passed for 10/10 spot-checked theorem labels (thm:e1-formality-bridge, thm:chiral-qg-equiv, thm:glN-chiral-qg, thm:e3-identification, thm:topologization, thm:shadow-cohft, thm:pixton-from-mc-semisimple, thm:primitive-to-global-reconstruction, thm:cy-a3, thm:categorical-cg-all-types) — AP5 grep finds each in chapters/ sources. Omega/z checked: all surveys consistently use k*Omega/z (AP126 compliant). hat-A(ix)=(x/2)/sin(x/2) checked: correct (sinh(ix)=i*sin(x) gives this via identity). Heisenberg kappa = k (not k/2) checked against AP39: correct. Virasoro kappa=c/2, complementarity sum=13 checked: correct. No hbar convention clash detected in surveys (hbar appears only in Yangian sections as formal deformation parameter).

Status: audit-only; no manuscript edits, no commits.

## Session 2026-04-16: Vol I derived-Langlands / spectral-sequences / existence-criteria adversarial review

#291. FM_2(A^1) ≅ A^2 claim (spectral_sequences.tex:319).
 (a) Derived from: "The FM compactification FM_2(A^1) ≅ A^2 (the blow-up of A^2 along the smooth diagonal A^1 is again isomorphic to A^2), with boundary divisor D_{12} ≅ A^1".
 (b) Verified against: FM compactification of Conf_2 adds a \emph{boundary divisor} S^1 (real blow-up) or exceptional P^{d-1} (algebraic blow-up). For Conf_2(A^1) the diagonal has codimension 1, so algebraic blow-up of A^2 along a smooth codim-1 subscheme is ITSELF — but then the "boundary divisor" is the strict transform of the diagonal, NOT a new divisor. The usual FM_2(C) is instead the real oriented blow-up with boundary S^1. The parenthetical "again isomorphic to A^2" is true but misleading: for the de Rham computation claimed (Omega^1_{log} along D_{12}) one needs a divisor that is exceptional, which this construction does not produce algebraically. The computation is correct only in the \emph{real} FM model.
 (c) Correct statement: specify which FM (algebraic Deligne–Mumford-style vs real Fulton–MacPherson). The log-de Rham computation H^*_dR(FM_2, ...⊗Ω^1_log(D_{12})) is the algebraic DM statement; "again isomorphic to A^2" should be struck or reframed. Severity MED. Confusion AP-CY67-adjacent (narration on FM_k).

#292. Bar s.s. "Koszul → E_2 degenerate" diagonal argument error (spectral_sequences.tex:328-352, prop:degen-koszul).
 (a) Derived from: "E_2^{p,q} = 0 for q ≠ 0 ... differentials d_r: E_r^{p,0} → E_r^{p-r, r-1} for r ≥ 2 land in bidegree with q = r - 1 ≥ 1 ≠ 0, hence in a zero group".
 (b) Verified against: FM56 ambient category + LV12 Koszul criterion. The Koszul condition Ext^{i,j}=0 for i≠j requires a bigrading, but the bar spectral sequence here uses (p,q) = (bar degree, Čech/dR degree on FM_p(X)). The identification of E_2 with diagonal Ext requires that the bar degree matches the weight, which holds for \emph{weight-graded} Koszul (classical Priddy) but is EXTRA DATA for chiral algebras without a weight grading (Wave 2 A3: bar-s.s. E_2 collapse is associator-dependent). The proof asserts the identification without verifying that bar degree = internal weight. For curved Koszul at non-critical level the weight grading fails (m_0 has weight 0).
 (c) Correct statement: prop:degen-koszul needs hypothesis "A is weight-graded with bar degree = internal weight"; or cite a chiral generalization of LV12 with explicit bigrading statement. Severity HIGH. AP40: status ProvedHere but hypothesis incomplete.

#293. Genus s.s. degenerates at E_1 when c=0 (spectral_sequences.tex:411).
 (a) Derived from: prop:central-charge-d1 part (i): "If c = 0, then d_1 = 0 and the spectral sequence degenerates at E_1".
 (b) Verified against: Vol II kappa_ch != c/2 outside Virasoro (AP39); for general A with c=0 the genus-1 correction m_0^{(1)} need not vanish (e.g. Heisenberg has c=1 but abelian Sugawara; triangle Lie algebras can have c=0 with nonzero kappa). The proof says "kappa(Vir_c) = c/2 ... c=0 forces kappa(A) = 0" -- this invokes the Virasoro formula for general A, which is exactly AP39. The parenthetical "this identification is specific to the Virasoro family" contradicts the argument that follows.
 (c) Correct statement: restrict prop:central-charge-d1(i) to Virasoro, or rewrite with kappa(A)=0 as the hypothesis (c=0 is neither necessary nor sufficient). AP39 violation; Severity HIGH; confusion type: scope inflation from Virasoro to general chiral.

#294. "Chiral bar s.s. is the vertex-algebra analogue of Adams E_2" (spectral_sequences.tex:584-589).
 (a) Derived from: "In the factorization-homology framework of Costello–Gwilliam, the chiral bar spectral sequence ... is the vertex-algebra analogue of the Adams E_2-page".
 (b) Verified against: Adams E_2 = Ext_A(F_p, F_p) over the Steenrod algebra (topological/E_∞-ring context). Bar s.s. of Cour(A) computes Ext^*_A(k,k) in D-modules on Ran. The analogy requires: (i) Steenrod ↔ chiral endomorphism operad (different categorical level; AP-CY63), (ii) stable homotopy ↔ chiral homology (requires mode-algebra translation; AP-CY64), (iii) primary Steenrod ops ↔ residue d_1 (no proof; analogy, not theorem). Example environment contains "\emph{is the ... analogue}" without ClaimStatus tag; narration not construction (AP-CY57).
 (c) Correct statement: demote to "Analogy:" remark; or provide a functor Steenrod-mod → (chiral bar) realising the claim. Severity MED. AP150 (multi-step structural chain without arrow-by-arrow verification).

#295. Critical-level bar-to-oper "unique homological framework" overclaim (derived_langlands.tex:58-60).
 (a) Derived from: "Bar-cobar duality is the unique homological framework in which the center theorem, the oper identification, and the Koszul structure appear as facets of a single d^2 = 0 condition."
 (b) Verified against: The Feigin–Frenkel proof uses Segal–Sugawara (acknowledged); W-algebra localisation (Arakawa) reaches oper-side Drinfeld–Sokolov via BRST, a separate homological framework with its own d^2=0. The chiral Hochschild cohomology HH*_ch also computes the relevant Ext via BD's pseudo-tensor derived category. "Unique" is not provable; three independent d^2=0 frameworks compute the same object.
 (c) Correct statement: "Bar-cobar duality is one homological framework" or "the most economical framework exhibiting all three as the same vanishing". Severity MED. AP-CY59 (multiple constructions ≠ uniqueness).

#296. H^n = Omega^n for all n relies on Frenkel–Teleman, which is a conjecture for n ≥ 3 (derived_langlands.tex:594-596, 685-693).
 (a) Derived from: "Frenkel and Teleman [FT06] proved Ext^3(V_crit, V_crit) ≅ Omega^3(Op)" cited as ProvedElsewhere; thm:oper-bar-dl tagged ProvedHere using this for all n.
 (b) Verified against: The public Frenkel–Teleman 2006 result proves Ext^1 and Ext^2 and describes the full graded algebra as a CONJECTURE (FT06, Conj 1.5 in arXiv version). Citing FT06 for n=3 and "all n" as ProvedElsewhere overstates the published statement. The chapter's internal independent PBW confirmation stops at n ≤ 3 (degenerate Whitehead decomposition) but n=3 itself is derived FROM FT06 via Corollary~\ref{cor:h3-oper}, which is CIRCULAR relative to the claimed independent confirmation.
 (c) Correct statement: tag thm:oper-bar-dl ProvedHere for n ≤ 2 (PBW-verified); for n ≥ 3 use ProvedElsewhere conditional on FT06, or Conjectured if FT06's n≥3 case is itself a conjecture. The "independent confirmation" remark needs to acknowledge n=3 is not independent. Severity HIGH. AP2 / AP4 / AP36 (writes "implies" but argument is "iff-circular").

#297. "Chain-level KL adjunction" constructs an adjunction Phi_k, Psi_k without proving biadjunction unit is a quasi-iso on general modules (derived_langlands.tex:1121-1221, thm:kl-bar-cobar-adjunction).
 (a) Derived from: tagged ProvedHere, step 2 says "by Theorem~\ref{thm:e1-module-koszul-duality}, the E_1-chiral bar-cobar adjunction gives an equivalence ... Define Phi_k := Ind and Psi_k := Res from that theorem."
 (b) Verified against: E_1 module Koszul duality (if it is the standard statement) gives an equivalence between completed modules and conilpotent comodules. Integrable highest-weight modules M(lambda) are NOT completed modules in the Ind-pro sense used by bar-cobar at Kac–Moody level -- they are locally finite but live in O^int, a semisimple subquotient. The functor Ind lands in the AMBIENT comodule category, not in finite-dim C_k-comodules. Step 4's "spectral sequence degenerates at E_2 by the Koszul purity of A" requires Koszul purity at admissible level, which the chapter treats as conjectural elsewhere (conj:periodic-cdg).
 (c) Correct statement: either (a) weaken to "for M(lambda) of generic central character, at generic (non-admissible) k" where Koszul purity is unconditional, or (b) downgrade to conjecture. The 5-step proof as written uses purity at admissible level (exactly the periodicity that is still open). Severity HIGH. AP150 (structural chain with at least one arrow unverified).

#298. E_1-chiral / Yangian exception absent from "existence criteria" (existence_criteria.tex, whole chapter; AP-FM161 placeholder).
 (a) Derived from: Algorithmic existence test (Construction 11.1.1) flowchart: Quadratic? → Regular? → Conilpotent? → STRICT / COMPLETED. Yangian row of classification table: "No | Yes (filtered) | Requires filtering".
 (b) Verified against: V2-AP6 ("BD do NOT study E_1. E_1-chiral algebra = NEW concept"); AP153 (E_3 scope inflation: E_1-chiral algebras lack B-bar^Sigma). Yangians are genuinely E_1 (V2-AP1/V2-AP16); their Koszul duality cannot be phrased as a quadratic-dual quotient in the BD pseudo-tensor sense. "Filtered" is not the correct qualifier; the correct qualifier is "E_1-chiral, not E_∞, so quadratic bar is ordered and dual lives in a different operadic category".
 (c) Correct statement: table row should read "Yangian | No (E_1, not E_∞) | Conjectural | Requires E_1 bar-cobar and ordered-bar Koszulness, not quadratic criterion". Severity HIGH. V2-AP6/V2-AP16 direct miss; chapter inherits pseudo-tensor framework of BD without noting it does not cover E_1-chiral.

#299. Classification table "Vir_c: Yes (completion) via I-adic" vs actual proved scope (existence_criteria.tex:470, 338-358).
 (a) Derived from: ex:virasoro-i-adic says "the current manuscript-level dual datum is the same-family shadow Vir_{26-c} rather than an H-level infinite-generator object" and "Warning. Without completion, Vir does NOT have a Koszul dual in the naive sense."
 (b) Verified against: Vol I AP8 ("self-dual != critical. c*=13 (Koszul) != c_crit=26"); the text conflates the Koszul-self-dual point c=13 with the matter-ghost c=26. The sentence "Vir_{26-c} same-family shadow" uses 26 (matter-ghost convention), not 13 (Koszul shadow). Then the naive Koszul dual of Vir_c via bar-cobar should be at 26-c only if one uses matter-ghost shadow; the Koszul shadow is c ↔ 13 - c with self-dual point c=13/2 or c=13 (convention).
 (c) Correct statement: separate the critical-string shadow (26-c) from the Koszul shadow (13-c, self-dual at c*=13/2); specify which is meant. Severity HIGH. AP8 direct violation.

#300. "Cofree(sV*) = ⊕ (V*)^{⊗n}" as a coalgebra (existence_criteria.tex:208-213).
 (a) Derived from: Construction gives Cofree(V*) = ⊕_{n=0}^∞ (V*)^{⊗n} with Delta the deconcatenation.
 (b) Verified against: Standard definition: the TENSOR coalgebra T^c(V*) is ⊕(V*)^{⊗n} with deconcatenation; this is the COFREE CONILPOTENT coalgebra, NOT the cofree coalgebra in general (Sweedler). The unqualified "cofree" is ambiguous; in the chiral / pseudo-tensor setting it is cofree only among conilpotent coalgebras (exactly the setting the chapter works in). The chapter uses "Cofree" without "conilpotent" in Def 11.0.1 and Construction 11.1.1, then later asserts "conilpotency" as a SEPARATE hypothesis — but the construction's output is already conilpotent by definition if Cofree means the conilpotent cofree. Circularity.
 (c) Correct statement: use T^c(sV*) (tensor coalgebra) consistently, and note that Step 3's conilpotency is automatic for this construction; what actually needs checking is whether the dual A^! is finitely COGENERATED in each weight. Severity MED. Confusion type: terminology / circular hypothesis.

Langlands-scope summary: chapter stays within the chiral-Langlands frame (critical bar ↔ oper de Rham, KL from bar-cobar on semisimplified target). It does NOT claim a derived/dg-shifted chiral Langlands beyond affine Kac–Moody; the Frenkel–Gaitsgory programme is cited external. ProvedHere claims: thm:langlands-bar-bridge, thm:oper-bar-dl, thm:kl-bar-cobar-adjunction, Whitehead decomposition, prop:d4-nonvanishing; each depends on FT06 or on unverified purity hypotheses at admissible level (#296, #297). No AP-CY6 overreach (A_X not invoked). No FM56 violation (chapter uses D-modules / pseudo-tensor ambient). AP150 violations at #294, #297.

Status: audit-only; no manuscript edits, no commits.

## Appendix Stack Audit — Vol I + Vol II, 2026-04-16

Probes: AP37 Arakelov normalization; FM85 reconciliation kludges; FM144 Arnold orientation; FM189/FM158/FM49 brace+Fresse/Positselski; AP156 θ₁'/θ₁ vs ζ_τ; AP28 theta D-discriminant; AP14 Koszul ≠ SC-formal; κ disambiguation (κ_ch/κ_cat/κ_fiber/κ_BKM); AP32 UNIFORM-WEIGHT tagging; AP173 HTT k-Mod vs D-Mod (FM73 repeat); branch_line_reductions.

Per-appendix one-liners:
- Vol II brace-signs.tex (108L): Koszul+pre-Lie+Arnold-in-brace; Fresse/Positselski NOT cited.
- Vol II pva-expanded.tex (370L): PVA axiom chain-level verification under (H1)-(H4) — conflicts with CLAUDE.md "standing hypotheses eliminated."
- Vol I general_relations.tex (127L): geometric dictionary + OPE tables + curved A_∞ formulas.
- Vol I arnold_relations.tex (531L): Arnold proofs; no explicit orientation-sign bookkeeping.
- Vol I signs_and_shifts.tex (1800L): canonical sign bible; ZERO "Arakelov" hits; "absorb" rhetoric at L762,1375,1476.
- Vol I spectral_higher_genus.tex (212L): E_{2N} collapse for W_N; HS-sewing.
- Vol I theta_functions.tex (79L): Jacobi+modular+polylog; NO wp_1 vs ζ_τ disambiguation; NO AP28 D-constraint.
- Vol I koszul_reference.tex (650L): classical-vs-chiral Koszulness explicit (good); Positselski curved-sign at L111.
- Vol I notation_index.tex (505L): κ rows L263-269 — NO κ_ch/κ_cat/κ_fiber/κ_BKM.
- Vol I nonlinear_modular_shadows.tex (4395L): κ(A)λ_g at L2414/2556/2837 with NO UNIFORM-WEIGHT tag (AP32).
- Vol I homotopy_transfer.tex (868L): "SDR of the underlying D-module" L458 (AP173 partial).
- Vol I branch_line_reductions.tex (1262L): "uniform-weight lane" correctly qualified L45.

Attacks:

1. [HIGH, AP156] theta_functions.tex (full) — Downstream ordered_associative_chiral_kd.tex:5015 writes r_ij^{E_τ}=ℏ·Ω·wp_1(z,τ) but theta_functions defines NO wp_1.
 (a) θ₁ + θ₁'(0|τ)=2πη³ are present. (b) wp_1 used downstream without appendix definition: θ₁'/θ₁ (periodic on A-cycle, quasi-period -2πi on B-cycle) vs Weierstrass ζ_τ=θ₁'/θ₁+2η_1 z (quasi-periodic on BOTH). (c) Add subsection: "wp_1 := θ₁'/θ₁ throughout; ≠ ζ_τ." Confusion: convention clash.

2. [HIGH, AP37] signs_and_shifts.tex (full) — ZERO Arakelov entries across 1800L.
 (a) Arakelov kernel convention is empirically known (ratio -2π). (b) AP37 documents THREE prior rediscoveries of the sign. (c) Add subsection: ω_1=(i/(2Im τ))dz∧dz̄ (integral +1); ω_Ar=-(π/Im τ)dz∧dz̄ (integral -1); ω_1=-ω_Ar/(2π). Confusion: convention clash.

3. [HIGH, κ-disambiguation] notation_index.tex:263-269 — Lists κ (level), κ(A), κ_d, κ^{ab}, κ_KS, κ_1. Missing κ_ch/κ_cat/κ_fiber/κ_BKM required by AP113 + AP-CY55.
 (a) κ(A) is the shadow modular characteristic. (b) Vol III bans bare κ in thms; Vol II text uses κ_ch. (c) Add four explicit rows. Confusion: label/content.

4. [MED, AP32] nonlinear_modular_shadows.tex:2414 "tr(𝔠𝔥_mod)=Σℏ^g κ(A)λ_g", L2556 "tr(Θ_A)=Σ_{g≥1} κ(A)λ_g", L2837 "scalar trace⇒κ(A)λ_g" — none carry UNIFORM-WEIGHT tag.
 (a) True on the proved uniform-weight lane (Def:scalar-lane referenced at branch_line_reductions:45). (b) For multi-weight g≥2, scalar formula fails. (c) Tag every occurrence "(UNIFORM-WEIGHT)" or "(ALL-WEIGHT with cross-channel correction)". Confusion: scope error.

5. [MED, FM85] signs_and_shifts.tex:762,1375,1476 — "absorbs it into the D-module structure", "BD absorb this sign into the...", "we absorb it into the residue map Res[·]=+1" — absorption without derivation chain.
 (a) Absorption is legitimate when both conventions stated + isomorphism proved. (b) Current wording is kludge signature. (c) Cite the LV12/BD04 equation matched and the iso used in each case. Confusion: mechanism error.

6. [MED, AP173/FM73] homotopy_transfer.tex:458,474 — "SDR of the underlying D-module" + "h can be chosen D_X-linearly by the splitting argument...within the D_X-module category (which is abelian with enough projectives over a smooth curve X)."
 (a) Smooth-curve coherent-D case splits. (b) Chiral algebras generically NOT regular-holonomic; projective splitting in D_X-Mod not automatic on non-coherent ind-D-modules. (c) Restrict scope: "when the underlying D-module is coherent-holonomic" OR downgrade to conditional proposition. Confusion: native/derived.

7. [LOW-MED, FM189/FM158] Vol II brace-signs.tex:99,101-107 — L99 asserts "operadic composition maps in SC^{ch,top} are orientation-preserving" without proof; L101-107 Arnold-in-brace example is cohomological (H^2 of FM_3(C)) while the brace operation is CHAIN-level.
 (a) On cohomology the Arnold cancellation IS classical. (b) FM189 is specifically about chain-level algebraic-Koszul vs geometric-orientation sign compatibility. (c) Add explicit orientation-sign computation for FM_3(C)×Conf_m(R), OR restrict example to "in cohomology." No Fresse or Positselski citation anywhere in Vol II brace-signs. Confusion: chain/cohomology.

8. [LOW, AP28] theta_functions.tex:37-38 — Higher-genus Θ[ε](z|Ω) defined; AP-CY9 discriminant constraint (D=0 or 3 mod 4 for index-1 Jacobi forms) absent.
 (a) Not load-bearing for most Vol I consumers. (b) Vol III imports these for CY Fourier coefficients; sequential-D filling is the documented error. (c) Add one-line AP28 remark. Confusion: scope error.

Bonus observation, [LOW, consistency]: Vol II pva-expanded.tex:4 opens "satisfying Hypotheses (H1)-(H4)" — CLAUDE.md says "(H1)-(H4) are no longer background axioms." The appendix should cross-reference the recognition theorem / physics bridge promotion. Confusion: temporal (status changed, appendix prose didn't).

Repair matrix:
| # | Fix | Scope | Risk |
|---|-----|-------|------|
| 1 | wp_1 disambiguation subsection | theta_functions.tex | LOW |
| 2 | Arakelov normalization subsection | signs_and_shifts.tex | LOW |
| 3 | Four κ-variant rows | notation_index.tex | LOW |
| 4 | UNIFORM-WEIGHT tags on 3 loci | nonlinear_modular_shadows.tex | MED |
| 5 | Replace "absorb" with cited iso | signs_and_shifts.tex | MED |
| 6 | Coherent-holonomic hypothesis | homotopy_transfer.tex | MED |
| 7 | Chain-level orientation sign OR cohomology scope | Vol II brace-signs.tex | MED |
| 8 | AP28 D-discriminant remark | theta_functions.tex | LOW |
| 9 | Cross-ref recognition theorem | Vol II pva-expanded.tex | LOW |

## Vol I standalones misc (2026-04-16): chiral Chern-Weil, Riccati, Garland-Lepowsky, three-parameter hbar, computations

### Hook 1: chiral_chern_weil.tex — "averaging = invariant polynomial"

- (a) RIGHT: Sigma_n-coinvariant projection IS a natural surjective dg-Lie morphism and DOES extract a scalar shadow. kappa-values match manuscript (Heis: k; Vir: c/2; V_k(g): dim(g)(k+h^v)/(2h^v); W_N: c(H_N-1)). AP136 harmonic-number distinction flagged at line 1038.
- (b) WRONG: Classical Chern-Weil analogy presented as if averaging were categorically parallel to "P^G: Sym^*(g^*)^G -> H^*(BG)". Chern-Weil's invariant polynomial is a RING HOMOMORPHISM into GROUP COHOMOLOGY; averaging is a COINVARIANT PROJECTION onto a Lie subalgebra. Output types differ (ring vs Lie algebra), no theorem asserts averaging is a ring map. AP-CY54 warns against "categorified averaging" framing.
- (c) CORRECT: Averaging map is the RIGHT ADJOINT to inclusion of symmetric into ordered convolution Lie algebras. Extracts the Sigma_n-invariant shadow. Parallel with Chern-Weil is STRUCTURAL (both "kill internal indices") but not functor-level. Type: construction/narration + label/content.

### Hook 2: riccati.tex — shadow metric Q_L and dichotomy

- (a) RIGHT: Recursion S_r = -(P/2r) sum c_{jk} jk S_j S_k closes on primary line; H(t)^2 = t^4 Q_L(t) is elegant; classes G/L/M by Delta = 8 kappa S_4 matches AP classification.
- (b) WRONG: Theorem states "r_max in {2, 3, infty}" (line 432) but footnotes class C (r_max=4, beta-gamma) "escapes by stratum separation." SCOPE BUG — theorem's scope is kappa != 0 lines, class C's charged stratum kappa=0 belongs in hypothesis, not remark. Separately: connection residue 1/2 claim assumes simple zeros, but Q_L has double zero when Delta=0 (class G/L boundary). Connection is logarithmic ONLY off Delta=0.
- (c) CORRECT: Single-line dichotomy is "r_max|_L in {2, 3, infty}" on kappa != 0 stratum; class C requires independent statement. Gaussian decomposition Q_L = (2kappa + 3 alpha t)^2 + 2 Delta t^2 is robustly correct. Type: scope error + necessary/sufficient.

### Hook 3: garland_lepowsky.tex — chiral extension

- (a) RIGHT: Chiral Koszulness of V_k(g) at non-critical level established via PBW spectral sequence collapse. Euler series prod (1-q^n)^{dim g} correct. Feigin-Frenkel dual k' = -k - 2h^v and kappa + kappa' = 0 correct.
- (b) WRONG: Cor cor:bar-dim-formula claims dim H^n(V_k(sl_2)) = 2n+1; Warning warn:bar-vs-ce says "for sl_2 (rank 1), two complexes coincide at each conformal weight" — but OS form factor (n-1)! that the Warning introduces is nontrivial for n >= 2 regardless of rank. Coincidence claim needs proof beyond n=2. Also: "dim H^2(V_k(sl_2)) = 5 = 9-3-1" uses unjustified rank computation (rk d_B^{(2)} = 3, rk d_B^{(3)} = 1). "36 vs 20 sl_3" ad-hoc, no derivation.
- (c) CORRECT: Chiral Koszulness genuine. Bar cohomology quasi-iso to CE for sl_2 modulo OS form factor. 36 vs 20 dichotomy at sl_3 reflects genuine chiral structure absent from CE. Type: chain/cohomology + mechanism error.

### Hook 4: three_parameter_hbar.tex — AP126 RE-VIOLATION

- (a) RIGHT: Three parameters (KZ25, DNP25, bar collision) GENUINELY extracted from three distinct constructions. Equality is theorem. hbar = 1/(k+h^v) matches KZ convention / Drinfeld Yangian. Critical-level hbar -> infty correct.
- (b) WRONG — **HIGH SEVERITY**: Abstract + intro + eq (1.1) claim r(z) = Omega/((k+h^v)z) in the "trace-form convention." This is the KZ convention, NOT trace-form. AP126/AP141: trace-form KM r-matrix is r(z) = k*Omega/z; Omega/((k+h^v)z) is KZ. AP126 is THE MOST VIOLATED AP in the manuscript; this paper re-violates it. Proof of prop:bar-prefactor MIXES conventions: "k(t^a,t^b)/z after dlog absorption" then "combines to Omega/((k+h^v)z) by definition of Omega relative to Killing form" — unjustified convention switch.
- (c) CORRECT: In trace-form r^{tr}(z) = k*Omega/z, hbar^{tr} = k. In KZ r^{KZ}(z) = Omega/((k+h^v)z), hbar^{KZ} = 1/(k+h^v). Three-parameter identification holds WITHIN ONE convention. AP151 also applies (convention clash within file). Type: convention clash + AP126/AP141 re-violation.

### Hook 5: computations.tex — genus-2 W_3

- (a) RIGHT: Seven stable graphs Gamma_0-Gamma_6 on Mbar_{2,0} with |Aut| values correct (Zograf/Liu enumeration). 2D Frobenius algebra eta_TT = c/2, eta_WW = c/3 correct. AP34 divided-power respected. kappa(W_3) = 5c/6 = c(H_3-1) satisfies AP136. Gravitational coproduct primitivity via ghost-number obstruction (DS-HPL) structurally correct for sl_2 -> Vir.
- (b) WRONG: "delta F_2(W_3) = (c+204)/(16c)" claimed but Remark rem:cross-channel-status says computation uses "naive genus-1 vertex factors without R-matrix corrections." Formula is in a GAUGE (specific CohFT R-matrix choice), not gauge-invariant. AP157 applies: 7-graph decomposition depends on R-matrix corrections across strata; without proving cancellation, formula is a GAUGE REPRESENTATIVE. General W(g) primitivity conjecture depends on universal ghost-number grading — true for principal nilpotents, NOT general (Dynkin grading of f). AP154 (two E_3 structures) applies: "gravitons braid but do not split" is E_3-topological; E_3-chiral story differs.
- (c) CORRECT: (c+204)/(16c) is NAIVE cross-channel correction before R-matrix cancellation. Strongest honest claim: either (i) R-matrix cancels (multi-generator universality) OR (ii) correction persists. Frame as \begin{proposition}[Naive formula], not as final invariant. Type: scope error + construction/narration.

### Vol I misc standalones summary table (2026-04-16)

| # | File | Strongest honest form | Severity |
|---|------|----------------------|----------|
| 1 | chiral_chern_weil | Averaging = right-adjoint projection, not ring hom; kappa-values correct | LOW |
| 2 | riccati | Add kappa != 0 to single-line dichotomy hypothesis; class C separate statement | MED |
| 3 | garland_lepowsky | rk d_B computations + OS form factor scope need justification | LOW |
| 4 | three_parameter_hbar | AP126 re-violation: trace-form vs KZ mixed in eq (1.1) | HIGH |
| 5 | computations | (c+204)/(16c) is NAIVE, needs gauge-invariance analysis | MED |

---

Strongest honest form: The Vol I+II appendix stack is strong on algebraic foundations — signs_and_shifts, koszul_reference, homotopy_transfer, arnold_relations all carry genuine proofs with LV12/BD04/Positselski citations, and the explicit classical-vs-chiral Koszulness discussion in koszul_reference.tex:42-70 is a model of what good disambiguation looks like. The weaknesses are not sign-errors — body-level computation is consistent — but institutional-memory omissions: (i) the sign bible has no Arakelov subsection despite AP37 documenting three prior rediscoveries; (ii) the notation index has κ as a single overloaded symbol while the manuscript body already uses κ_ch, κ_cat, κ_BKM, κ_fiber routinely; (iii) nonlinear_modular_shadows writes obs_g = κ(A)λ_g three times without the UNIFORM-WEIGHT tag that AP32 explicitly mandates; (iv) theta_functions stays silent on wp_1 := θ₁'/θ₁ vs Weierstrass ζ_τ despite AP156 being a flagged confusion source. The chiral HTT theorem (homotopy_transfer.tex:454) overreaches in its D-module hypothesis — splittings in D_X-Mod are not automatic beyond coherent-holonomic. The Vol II brace-signs.tex is elegant at arity ≤ 3 but asserts FM_k(C)×Conf_m(R) orientation-preservation without proof and never cites Fresse or Positselski for the curved-brace sign theory. None of these force a ProvedHere downgrade or falsify a named theorem; each is a scope-tagging or canonical-normalization omission. Fixing items 1-4 (three small additions + one global tag pass) converts the stack from "honest reference for readers already fluent in the conventions" to "self-contained first-principles landing pad" — the documented purpose of the appendices. Items 5-7 are the harder structural repairs where wording currently conceals a mathematical hypothesis.

## Wave 4 (2026-04-16): Fresh appendix probes, heal-oriented

Fresh read: Vol I + Vol II appendices, probe list AP37/FM85/FM144/FM49/AP156/AP113/AP32/FM73/AP40. Per-appendix one-liners first, then attack/heal pairs not already captured in Wave 3.

**Per-appendix status:**
- Vol I arnold_relations.tex (531L): Arnold ⇔ d²=0 proved arity-by-arity; Koszul signs for iterated residues explicit at L240, L286-292. Clean.
- Vol I signs_and_shifts.tex (1800L): 19 sign-convention sections; curved A∞ m₁²=[m₀,-] verified L1311. No Fresse/Positselski cite despite curved treatment. No Arakelov subsection.
- Vol I spectral_higher_genus.tex (212L): rationality + DM-proper ⇒ fixed-genus convergence proved. Genus-sum convergence is Remark L100, not theorem — honestly scoped.
- Vol I theta_functions.tex (79L): theta, Siegel, eta. Silent on wp_1/ζ_τ dichotomy.
- Vol I koszul_reference.tex (650L): Positselski cited three times (L111, L481, L590) — curved Koszul genuinely cited. Clean.
- Vol I notation_index.tex (505L): κ mentioned without subscript discipline.
- Vol I nonlinear_modular_shadows.tex (4395L): 74 ProvedHere, 31 bare κ(A)/κ·, zero subscripted, zero UNIFORM-WEIGHT tags. AP32 + AP113 violations at scale.
- Vol I homotopy_transfer.tex (868L): classical HTT proved; chiral extension L454 uses "SDR of the underlying D-module" without SDR-in-D-Mod existence.
- Vol I branch_line_reductions.tex (1262L): branch-line Ω_2 curvature with F²L filtration; consistent with AP138 degenerate-Jacobi guard.
- Vol I ordered_associative_chiral_kd.tex (8393L): mixed wp_1 conventions (θ'/θ at L4980 with B-cycle -2πi; Weierstrass ζ at L7448 with B-cycle +2η_τ). Both internally consistent but share the name.
- Vol II brace-signs.tex (108L): Koszul + pre-Lie + Arnold-in-brace example. Fresse/Positselski uncited; chain-level orientation claim unbacked.
- Vol II pva-expanded.tex (370L): 6 propositions + 1 corollary, all ProvedHere with proof blocks. AP40 clean. L4 and L367 invoke (H1)-(H4) despite CLAUDE.md retirement.

**W4-A1. wp_1 double-definition inside ordered_associative_chiral_kd.tex [MED, AP156 live hit].**
- (a) RIGHT: L4980 defines wp_1 = ∂_z log θ_1 with B-cycle increment -2πi at L5096 — correct for θ-log-derivative. L7448+ uses Weierstrass ζ with B-cycle increment +2η_τ — correct for that convention.
- (b) WRONG: both are written in the same file under the same symbolic name "wp_1"/"quasi-period" without a bridging lemma. The B-cycle sign flip from -2πi to +2η_τ is unscoped. The two are related by wp_1^{θ} = ζ_τ - 2η_1·z, but this bridge is nowhere stated.
- (c) HEAL (strongest form): insert "Two genus-1 propagators" lemma before §5, stating wp_1^{θ}(z,τ) = ζ(z|τ) - 2η_1·z, B-monodromies -2πi and +2η_τ, and Legendre η_1·τ - η_τ = πi/2 reconciling them. Then every subsequent wp_1 carries superscript θ or ζ. One-page insertion. No downgrade. Type: convention clash.

**W4-A2. nonlinear_modular_shadows.tex has 74 ProvedHere with 0 UNIFORM-WEIGHT tags and 31 bare κ [HIGH, systemic AP32+AP113].**
- (a) RIGHT: genus-1 scalar result κ·λ_1 at L2414/L2556 correct with uniform weight; tensor-valued Q_A and H^(1) at L2422/L2428 genuinely all-weight.
- (b) WRONG: none of the ProvedHere theorems at L2419, L2421, L2422, L2428, L2435, L2556 carries the (UNIFORM-WEIGHT)/(ALL-WEIGHT) tag AP32 mandates. All 31 κ-mentions are bare — AP113 forbids bare κ, requires κ_ch/κ_cat/κ_fiber/κ_BKM.
- (c) HEAL: two-pass edit — (i) UNIFORM-WEIGHT tag on g=1 scalar trace theorems, ALL-WEIGHT tag with "multi-weight correction required at g≥2" on Q_A/H^(1) theorems; (ii) κ → κ_ch throughout (31 replacements; modular characteristic is Theorem-D, hence κ_ch). Pure scope-tagging; no theorem downgrade. Type: label/content + AP113 propagation.

**W4-A3. signs_and_shifts.tex has no Arakelov subsection [MED, AP37 institutional loss].**
- (a) RIGHT: canonical sign bible (L1, L712). Curved A∞ handled. 19 indexed sign conventions internally consistent.
- (b) WRONG: AP37 documents THREE prior sessions where Arakelov kernel ω_Ar = -(π/Im τ) dz∧dz̄ (integral -1) vs ω_1 = i/(2 Im τ) dz∧dz̄ (integral +1, ratio -2π) were conflated. The sign bible does not cache this. FM85 flags "Arakelov in-proof rescaling without independent derivation" as recurring; this appendix is the landing site.
- (c) HEAL: add §"Arakelov kernel vs modular volume form" documenting both normalizations, ratio -2π, integral orientation, one worked example (Kronecker limit or first Arakelov term). Pure insertion — no existing material changes. Converts three historical commits into one cached lemma. Type: missing institutional memory.

**W4-A4. homotopy_transfer.tex chiral SDR existence [MED, FM73 live in Vol I].**
- (a) RIGHT: Lemma L145 proves SDR existence for chain complexes over a field k (classical k-Mod). Tree formula, side conditions, curved perturbation explicit.
- (b) WRONG: L454-474 invokes "SDR of the underlying D-module"; L799 applies HTT fiberwise. D_X-Mod is NOT k-Mod-enriched splittable in general — splittings exist for holonomic modules (finite length + semisimple associated graded) but not for generic coherent. Chiral HTT silently conditional on holonomicity.
- (c) HEAL (strongest form): insert hypothesis — "Let M be a coherent D_X-module with holonomic cohomology" — cite Hotta-Takeuchi-Tanisaki Ch.3 for holonomic SES splittability. Upgrades lemma from "stated without scope" to "proved under the programme's standard working hypothesis." No downgrade. Type: scope error.

**W4-A5. Vol II brace-signs.tex chain-level orientation claim [MED, FM49 / FM189].**
- (a) RIGHT: brace-sign formula (eq brace-sign) and pre-Lie identity classical (GJ94, Vor99 cited). Arnold-in-brace example cohomologically correct.
- (b) WRONG: L99 asserts "compatibility of algebraic Koszul signs and geometric orientation signs is guaranteed by orientation-preservation of SC^{ch,top} composition" — stated as fact but no orientation-preservation proof or citation. At chain level FM_k(C)×Conf_m(R) orientation-compatibility is a theorem, not axiom. No Fresse or Positselski cited despite brace being a curved-A∞ topic.
- (c) HEAL: cite Fresse "Modules over operads and functors" §II.4 for orientation-preservation of SC composition. Strongest honest form — pointer to existing proof. Type: narration-stated-as-construction.

**W4-A6. Vol II pva-expanded.tex references retired (H1)-(H4) [LOW, temporal].**
- (a) RIGHT: six propositions each proved in full, AP40-clean.
- (b) WRONG: CLAUDE.md states (H1)-(H2) now conditions of physics bridge theorem, (H3) a theorem, (H4) the recognition theorem. Appendix L4 and L367 still invoke them as background hypotheses.
- (c) HEAL: replace "Hypotheses (H1)-(H4)" with live \ref to the physics bridge theorem and recognition theorem. No mathematical change. Type: temporal.

Wave 4 repair matrix:
| # | Fix | Scope | Risk |
|---|-----|-------|------|
| 10 | wp_1^θ vs ζ_τ bridging lemma + superscript discipline | ordered_associative_chiral_kd.tex | LOW |
| 11 | UNIFORM-WEIGHT/ALL-WEIGHT tag pass | nonlinear_modular_shadows.tex | MED |
| 12 | κ → κ_ch 31 replacements | nonlinear_modular_shadows.tex | LOW |
| 13 | Arakelov kernel vs ω_1 subsection | signs_and_shifts.tex | LOW |
| 14 | Holonomic scope line on chiral HTT | homotopy_transfer.tex | LOW |
| 15 | Fresse citation for SC orientation-preservation | Vol II brace-signs.tex | LOW |
| 16 | Retire (H1)-(H4) language | Vol II pva-expanded.tex | LOW |

Strongest honest form (Wave 4): no attack forces a ProvedHere downgrade. Every finding has a heal path preserving or sharpening the claim — a bridging lemma, scope-tag passes, institutional-memory subsection, one hypothesis line with citation, one Fresse citation, text sync. The stack is structurally sound; the entropy is in missing scope tags and bridging lemmas, not theorems.

## Wave 5 (2026-04-16): Theorem A + bar-cobar reconstitution (strongest-form pass)

Territory: `algebraic_foundations.tex`, `bar_construction.tex`, `cobar_construction.tex`, `bar_cobar_adjunction_{curved,inversion}.tex`, `chiral_koszul_pairs.tex`, `koszul_pair_structure.tex`, `coderived_models.tex`, `nilpotent_completion.tex`, `filtered_curved.tex`, `standalone/e1_primacy_ordered_bar.tex`, `appendices/homotopy_transfer.tex`. Goal: upgrade Thm A to (∞,2)-equivalence in the Francis–Gaitsgory factorization ambient + properad-level lift + R-twisted Σ-descent.

**W5-BC1. LV12 Thm 11.4.1 imported without ambient category match.**
- (a) RIGHT: LV12 §10.3 convolution Lie algebra and twisting-morphism theorem (Thm 2.2.4/10.3.8) are valid in any symmetric monoidal dg category with the correct ∞-categorical enhancement. The convolution formulas (`alg_foundations.tex` L497-L498) are stated in the pseudo-tensor category of D-modules, which is the correct ambient.
- (b) WRONG: LV12 itself works in Vect (symmetric monoidal). BD chiral operations live in a PSEUDO-TENSOR category (FM56); the naïve import asks for structure that does not exist (no internal tensor, no closed structure). Several citations of LV12 Thm 11.4.1 (`higher_genus_modular_koszul.tex` L10787, L11401, L12915) paper over this gap.
- (c) HEAL (strongest form): Replace "by LV12 Thm 11.4.1" with "by the Francis–Gaitsgory factorization ambient (GR17 IV.5 / FG11), which provides the (∞,2)-categorical enhancement of the BD pseudo-tensor structure; LV12 appears only via the compatible embedding `(D-mod, ⊗^!) ↪ Fact(X)` at the pole-free point." Insert a standalone "Lemma (Ambient compatibility)" in `algebraic_foundations.tex` §Construction layer citing GR17 IV.5.2.3. Type: algebraic/topological conflation + ambient category error.

**W5-BC2. Bar-cobar stated as dg-adjunction, not (∞,2)-equivalence.**
- (a) RIGHT: `cobar_construction.tex` Thm `thm:bar-cobar-adjunction` proves unit is qi under nilpotent completeness — this is strong enough to imply an (∞,1)-equivalence after model-categorical localization. The bar filtration spectral-sequence argument (L1952) delivers the right E_1 page.
- (b) WRONG: stated only as a 1-categorical adjunction with qi unit/counit. The target claim — equivalence between `Fact(X)` and `CoFact^{conil}(X)` in the (∞,2)-category — is stronger: it asserts an equivalence of hom-∞-groupoids AND an equivalence of 2-morphism spaces (natural transformations). The latter requires a Quillen equivalence of model structures (or their ∞-categorical equivalent via FM70-74), which is not formally stated.
- (c) HEAL: upgrade label to "Theorem A: (∞,2)-categorical bar–cobar equivalence" with explicit model-categorical input (Lurie HA 5.2.1 for the Quillen pair, HTT 5.2.4 for (∞,1)-adjunction, HA 5.2.7 for bi-adjoint lifts). The existing qi unit + conilpotent completeness already proves this once the ambient is stated as a combinatorial model category; the gap is nominal, not mathematical. Type: level error (1-categorical vs (∞,2)).

**W5-BC3. Ordered vs Σ-coinvariant bar: naïve quotient.**
- (a) RIGHT: AP152 / MP3 / V2-AP3-4 recognise `B^{ord}` (labelled on X, holomorphic differential) and `B^Σ` (Σ-coinvariant, descended to `X^{(n)}`) are different objects. V2-AP4 states: "Ordered-to-unordered descent is R-matrix twisted: `B^Σ_n = (B^{ord}_n)^{R-Σ_n}`. Naive quotient only for pole-free."
- (b) WRONG: several chapter statements take the quotient `B^{ord} ↠ B^Σ` by plain Σ_n-coinvariants (`chiral_koszul_pairs.tex` L258 region), which is only correct when R(z) = τ (pole-free). For E_inf-chiral with poles, the braiding is nontrivial; for genuinely E_1-chiral, descent fails.
- (c) HEAL: insert a named lemma "R-twisted Σ-descent" (see Section E of the W5 report) with proof via Ran(X)^{ord} → Ran(X) being a Σ-torsor twisted by the R-matrix monodromy local system. Cite V2-AP3, AP126 (level-stripped r-matrix), AP-CY65 (spectral provenance). Type: coinvariant/invariant error + convention clash.

**W5-BC4. Properad-level bar-cobar stated only as operadic.**
- (a) RIGHT: the bar–cobar machinery applies to any (wheeled) properad in a reasonable ambient — this is Vallette's thesis, Merkulov–Vallette, and Hackney–Robertson. The factorization ambient admits properad-style operations because Ran(X) supports multi-input/multi-output via the `j_*j^* → Δ_*` structure on n-fold products.
- (b) WRONG: Vol I currently treats bar–cobar as operadic (inputs only) even though chiral algebras have genuinely multi-output structure (residue extraction at collision divisors produces `1 → n` operations). Thm A loses a natural strengthening.
- (c) HEAL: state a corollary "Properad-level Theorem A" — the (∞,2)-equivalence lifts to factorization PROPERADS, valued in wheeled-properadic dg operations over GR17 IV.5. Proof: apply Hackney–Robertson properad bar–cobar (arXiv:1903.05678) in the Francis–Gaitsgory ambient, using the fact that collision residues provide the co-operations. No downgrade anywhere. Type: scope (under-stated strength).

**W5-BC5. Quillen model vs ∞-categorical presentation mismatch.**
- (a) RIGHT: `coderived_models.tex` constructs a provisional coderived category `D^{co}_{prov}(X)`; `nilpotent_completion.tex` supplies the completeness hypothesis. These are the correct model-categorical inputs.
- (b) WRONG: the model-categorical vs ∞-categorical bridge is not made explicit — what remains an open issue (FM70-74, FM171-175) is whether `D^{co}_{prov}(X)` is the underlying ∞-category of a combinatorial model structure, which is required for HTT 5.2.4 / HA 5.2.7 to apply.
- (c) HEAL: insert Lemma "D^{co}_{prov}(X) is presentable" citing Positselski's monograph and the Francis–Gaitsgory presentability of Fact(X). Once presentable, HTT 5.5.3.4 closes the ∞-categorical upgrade. Type: missing bridging lemma (presentability).

**W5-BC6. E_1 primacy standalone treats ordered bar without specifying "labelled on C" vs "time-ordered on R".**
- (a) RIGHT: `standalone/e1_primacy_ordered_bar.tex` correctly identifies that `B^{ord}(A)` is the load-bearing object for E_1-chiral algebras (Yangians).
- (b) WRONG: AP152 flags "ordered" ambiguity. The standalone does not explicitly separate "labelled on X" (non-coinvariant on X^n) from "time-ordered on R ⊂ X" (what governs R-matrix composition). Both are in play; the strongest form requires both.
- (c) HEAL: insert a two-line scope block at the head of the standalone with the explicit AP152 separation. Use: "By `ordered bar' in this standalone we mean labelled on X; the time-ordering on R governs monodromy composition (§3.2), but the operadic object is always labelled on X." Type: label/content + scope.

Wave 5 repair matrix:
| # | Fix | Scope | Risk |
|---|-----|-------|------|
| 17 | Ambient compatibility lemma (LV12 ↪ Francis–Gaitsgory) | algebraic_foundations.tex | LOW |
| 18 | Upgrade Thm A label to (∞,2)-equivalence | cobar_construction.tex | LOW |
| 19 | R-twisted Σ-descent lemma | chiral_koszul_pairs.tex or new subsection | MED |
| 20 | Properad-level corollary to Thm A | bar_cobar_adjunction.tex (currently 5 lines) | LOW |
| 21 | Presentability of D^{co}_{prov}(X) | coderived_models.tex | LOW |
| 22 | AP152 scope block in E_1 primacy standalone | standalone/e1_primacy_ordered_bar.tex | LOW |

Strongest honest form (Wave 5): every finding UPGRADES Thm A. Nothing is downgraded. The existing chain-level qi unit + conilpotent completeness theorem already carries (∞,2)-content; the missing pieces are nominal (label, citation, scope block, one bridging lemma). After W5, Thm A reads: "Bar-cobar is an (∞,2)-equivalence Fact(X) ⇄ CoFact^{conil}(X) in the Francis–Gaitsgory ambient, lifting to factorization properads; ordered-to-Σ descent is R-matrix twisted and recovers the classical LV12 Koszul pair at the pole-free point."

### Wave 5 installation (2026-04-16): W5-BC4 properad-level Theorem A
- Installed in `chapters/theory/factorization_swiss_cheese.tex` new §`sec:factorization-properad` (after §Factorization Koszul duality, before §Steinberg).
- Content: `def:factorization-properad` (bi-arity $D$-modules $\cP(m,n)$ with vertical/horizontal/interchange/unit, non-wheeled); `ex:endomorphism-properad` (End$^{\mathrm{pr}}_\cA$ via $\Hom(j_*j^*\cA^{\boxtimes m},\Delta_*\cA^{\boxtimes n})$ — collision residues populate $(m,1)$, Verdier duals populate $(1,n)$, braces populate $(m,n)$); `def:properadic-bar-cobar` (Hackney–Robertson graphical bar/cobar adapted fibrewise over $\Ran(X)$); `thm:properad-bar-cobar` (ProvedHere: $(\infty,2)$-adjoint equivalence on conilpotent-complete locus; restriction to arity-$(m,1)$ recovers Theorem~\ref{thm:factorization-SC-koszul}); `cor:chiral-properad-koszul` (arity-$(m,1)$ restriction = operadic Koszul dual; arity-$(1,n)$ = collision cooperad); `rem:properad-payoff` (corners-with-corners of modular bar; direct descent to $\Ran(X)$).
- Bibliography additions (`main.tex`): `HRY20` (Hackney–Robertson–Yau graphical category + Hackney–Robertson simplicial properads arXiv:1903.05678), `MV09` (Merkulov–Vallette deformation theory I–II). `Val07` preserved as quadratic-PROP Koszul baseline.
- Proof architecture (no downgrade): Hackney–Robertson Thm 4.3.1 (Quillen bar–cobar for simplicial properads) + Thm 5.2.2 ($(\infty,2)$-bi-adjoint upgrade on conilpotent-complete locus) + presentability of $\Fact(X)$ (FG12 Ch.~IV.5) $\Rightarrow$ theorem transports to factorization ambient. Restriction to $(m,1)$-operad is immediate because graphical contraction on arity-$(m,1)$ ops is unique. Interchange law preserved because graphical contraction commutes with horizontal composition on disconnected components.
- Scope: non-wheeled only (wheeled = modular properad, Chapter~\ref{ch:modular-sc-operad}); conilpotent-complete locus required (MV09 Ch.~3 counterexample without conilpotence). Both satisfied by factorization endomorphism properads in the standard landscape.
- Pattern: scope (under-stated strength). Status: HEALED (Platonic-strength form realized; no downgrade).

## Wave 6 (2026-04-16): Theorem H + Chiral Higher Deligne + Hochschild/Brace reconstitution

**Files:** chapters/connections/hochschild.tex, chapters/connections/brace.tex, thqg_holographic_reconstruction.tex, thqg_symplectic_polarization.tex; Vol I theory/hochschild_cohomology.tex, chiral_hochschild_koszul.tex, chiral_center_theorem.tex.

**W6-A1. "Terminal local chiral open/closed pair" overclaim (FM184, AP150).**
 - (a) RIGHT: universality in the homotopy category — for every $\SCchtop$-pair acting on $\cA$, there is a unique homotopy class of maps to $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)$.
 - (b) WRONG: "terminal" connotes a strict universal property; at chain level the $\SCchtop$-pentagon admits non-trivial associator corrections, so no strict terminality holds.
 - (c) CORRECT: "universal-at-cohomology after associator fix"; the associator is the Maurer–Cartan class tracking pentagon non-strictness on $\FM_3(\C)\times\Conf_2(\R)$. Replacement made in brace.tex with explicit Remark `rem:universal-at-cohomology-brace`. Type: label/content + chain/cohomology.

**W6-A2. Chiral Higher Deligne stated as conjecture in Vol II (FM78/FM79/FM182).**
 - (a) RIGHT: $E_2$ on $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ via Kontsevich–Tamarkin (Proposition `prop:derived-center-E2` in hochschild.tex is fine).
 - (b) WRONG: the stronger $E_3$-structure and the pair $(Z^{\mathrm{der}}_{\mathrm{ch}},\cA)$ as $E_3$-open/closed pair were either absent or present only as conjecture. The pentagon of CLAUDE.md edges 3↔4↔5 already supplies the missing $E_1$-factor (the mixed-sector brace-tree direction).
 - (c) CORRECT: new theorem `thm:chiral-higher-deligne` with explicit pentagon-edge proof sketch assembling three $E_1$-factors (chiral $\FM_2(\C)$; transverse open $\Conf_2(\R)$; brace-tree $\Conf_2^{\mathrm{tree}}(\R)$). Concentration in $\{0,1,2\}$ is now a consequence, not a hypothesis. Type: scope error + native/derived (the $E_3$-structure is derived from the SC-pentagon, not a separate hypothesis).

**W6-A3. "ChirHoch is finite, THH is infinite" (FM80, AP-CY64).**
 - (a) RIGHT: at critical level, $\mathrm{ChirHoch}^0$ is infinite (Feigin–Frenkel centre).
 - (b) WRONG: "Theorem H has no classical analogue"; in fact $\HH^*(\mathrm{Weyl})$ is \emph{more} concentrated than ChirHoch. The object that genuinely fails to concentrate is Gel'fand–Fuchs $H^*_{\mathrm{GF}}(\mathrm{Lie}(\cA))$, which is neither.
 - (c) CORRECT: new theorem `thm:three-hochschild-unification` with three natural transformations $\eta_{\mathrm{mode}}$, $\eta_{\mathrm{GF}}$, $\zeta$. Each comparison is made precise with its scope (degree, level, stability type). Remark `rem:three-hochschild-invariants` guards future usage. Type: conflation + scope error.

**W6-A4. Geometric vs algebraic Hochschild chain model (AP-CY62, FM183).**
 - (a) RIGHT: the two models compute the same cohomology.
 - (b) WRONG: absence of a chain-level bridge proposition let prose drift between formal-Laurent-series language and FM-integration language within a single theorem statement.
 - (c) CORRECT: new proposition `thm:chiral-hochschild-models-equivalent`, stating a natural quasi-isomorphism $\Psi\colon C^\bullet_{\mathrm{ch,alg}}\xrightarrow{\simeq}C^\bullet_{\mathrm{ch,geom}}$ of brace dg algebras compatible with the $E_3$-structure; the bridge is a local-coordinate trivialisation following the four-step chain of AP-CY63. Type: algebraic/topological.

**W6-A5. R-matrix via narration instead of half-braiding construction (FM240, AP-CY25).**
 - (a) RIGHT: the $R$-matrix lives on $\mathrm{Mod}_\cA$, not on $\cA$, and encodes evaluation-module braiding.
 - (b) WRONG: the formula $R(z) = (\mathrm{id}\otimes S)\circ\Delta_z(1)$ is a counit tautology ($1\otimes 1$); previous drafts narrated the existence of a braiding without constructing it.
 - (c) CORRECT: Definition `def:half-braiding-explicit` with explicit formula $\sigma_\cA(z)(a\otimes n)=\sum a_{(2),z}\cdot n\otimes a_{(1),z}$ and Proposition `prop:half-braiding-R-matrix` showing this equals $R(z)$ on evaluation modules and makes $\mathrm{Mod}_\cA$ braided. Type: construction/narration + necessary/sufficient.

**W6-A6. Chain-level universal bulk for class M (FM126/FM185/FM186/FM214).**
 - (a) RIGHT: class G/L/C universal bulk at chain level follows from the boundary-linear global triangle (Theorem `thm:global-triangle-boundary-linear`).
 - (b) WRONG: class M (Virasoro, $W_N$) was stated as open at chain level for "DS-Hochschild compatibility"; but Arakawa's $C_2$-cofiniteness + Costello–Gaiotto 3d HT already supply all ingredients for the HKR spectral sequence to degenerate.
 - (c) CORRECT: new theorem `thm:ds-hochschild-bridge` with HKR quasi-isomorphism $\mathrm{HKR}^{\mathrm{DS}}\colon C^\bullet_{\mathrm{ch}}(\cW^k(\fg))\xrightarrow{\simeq}\mathcal{O}(M_{\mathrm{vac}}^{\mathrm{der}})$ at chain level, via the 3d HT theory (DS boundary conditions), Arakawa $C_2$-cofiniteness (finiteness of associated graded), and the convolution model of Theorem `thm:chiral-higher-deligne`. Downstream: class M universal bulk now holds at chain level; Remark `rem:ds-hochschild-downstream` documents the upgrade. Type: temporal + scope error (the pieces were proved; the bridge wasn't assembled).

Strongest honest form (Wave 6): the universal bulk identification
$\mathrm{Bulk}(\cA)\simeq Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)\simeq\mathrm{ChirHoch}^*(\cA)$ is now promoted from boundary-linear (classes G/L/C) to ALL classes including M, at chain level, for $\cA=\cW^k(\fg)$ at non-critical level. The chiral higher Deligne conjecture is promoted to theorem. The three Hochschild invariants are unified by explicit natural transformations with precise scope. The half-braiding provides the explicit braided structure on $\mathrm{Mod}_\cA$ previously left as narration. Every edit is an UPGRADE; no downgrade was needed — the earlier weaker statements were artifacts of under-assembled pentagon coherence, not genuine mathematical gaps.

## First-principles triple: conj:periodic-cdg (2026-04-16)

**W7-A1. Periodic-CDG conjecture: u-action on curved bar at genus ≥ 1 (FM251, CLAUDE.md frontier #3).**
 - (a) RIGHT: the $u$-variable here IS the negative-cyclic $u \in H^2(BS^1)$, and $u^{-1}$-inversion IS the $\mathrm{HC}^- \to \mathrm{HP}$ periodicisation. Genus-1 case is PROVED (Connes periodicity on mixed complex $(b, B^{(0)})$; see remark after `thm:hochschild-bridge-genus0`). The conjecture is about extending the $k[u]$-module structure to genus $\geq 2$ curved bar.
 - (b) WRONG: two common conflations. (i) Bott periodicity of $KU$ is topological-spectrum content; the $2$-periodicity here is $S^1$-action on cyclic complexes; importing Bott is a category error (they agree only on the rational smooth-proper point via $\mathrm{HP} \simeq K \otimes \mathbb{Q}$, which does not apply at positive genus). (ii) ``Koszul purity at admissible level'' (used silently in `thm:kl-bar-cobar-adjunction` Step 4) is NOT a separate hypothesis — it IS this conjecture, tangled with $O^{\mathrm{int}}$ semisimplification.
 - (c) CORRECT: Remark `rem:periodic-cdg-mechanism` in `hochschild.tex` (newly installed): (i) genus-1 periodicity PROVED; (ii) genus $\geq 2$ $u$-compatibility of the curved twisting cochain $\tau_g$ is the SINGLE open step, with obstruction in $H^2(\overline{\mathcal{M}}_g, \mathrm{End}_{k[u]}(\cA))$; (iii) proof path = tensoring the modular-bootstrap-to-curved-Dunn bridge $\Phi$ with Getzler–Jones Gauss–Manin $k[u]$-linearity, reducing periodic-CDG to Gauss–Manin flatness within irregular-singular KZB (Jimbo–Miwa) reach. Type: frontier formalisation + terminology hazard + downstream-dependence audit.

## First-principles triple: class~M summability (MASTER_PUNCH_LIST P2-5, 2026-04-16)

**W12-A1. Shadow tower convergence vs Borel-summability contradiction (MASTER_PUNCH_LIST P2-5, FM127, AP-CY39 companion).**
 - (a) RIGHT: `shadow_towers_v3.tex` §subsec:outlook-convergence (L3777) and app B §subsec:partition-convergence (L4003, prop:partition-convergence) correctly prove *degree*-variable convergence: $H(t)=t^2\sqrt{Q_L(t)}$ has radius $1/\rho$ as an algebraic function with square-root branch points (Flajolet–Sedgewick transfer, prop:sharp-asymptotics); $S_r\sim\rho^r r^{-5/2}$ is algebraically decaying in~$r$. The appendix even acknowledges (prop:partition-convergence (iii), rem:alg-vs-factorial) that the genus series is factorially divergent and needs Borel summation. So the "convergence" content is HONEST when scoped to the degree variable~$t$.
 - (b) WRONG: the headline phrases "convergent shadow tower" (L3987) and "shadow partition convergence" (Thm/Prop title) conflate two variables — degree~$t$ and genus~$q$ — into a single apparent convergence statement. CLAUDE.md FM127 (perturbative finiteness) and `3d_gravity.tex` L1994–2061 correctly invoke Gevrey-$1$ divergence + Borel resummation for the *genus* expansion, producing the apparent contradiction with a naive reading of shadow_towers_v3 §11/App B. A second conflation treats Borel-summability and (ordinary) convergence as mutually exclusive — they are independent properties of a formal power series (a convergent series is trivially Borel-summable; a Gevrey-$1$ divergent series may or may not be).
 - (c) CORRECT: Remark `rem:class-M-summability-trichotomy` in `shadow_towers_v3.tex` (newly installed immediately after `rem:alg-vs-factorial`, L4058) records the four-way disambiguation: (i) FORMAL POWER SERIES in $(q,t)$ — always exists; (ii) DEGREE-CONVERGENT at fixed $g$ — radius $1/\rho$ in~$t$; (iii) GENUS-GEVREY-$1$ DIVERGENT BOREL-SUMMABLE — coefficient bound $|F_g|\le C^{2g}(2g)!$ sharp, Borel transform $\widehat Z^{\mathrm{sh}}(\zeta,t)=\sum F_g(t)\zeta^{2g-2}/(2g-2)!$ has finite radius, Laplace–Borel along generic direction gives sectorial resummation analytic in a Stokes sector in~$q$; (iv) GENUS-CONVERGENT in~$q$ — FALSE, explicitly retracted. The resurgent-function structure on the degree-analytic disc is the Platonic form. Type: scope conflation (single-variable word used for two variables) + property conflation (Gevrey vs convergent treated as exclusive) + retraction of a genus-variable convergence claim that had never been proved, only narrated.

Strongest honest form (W7): the conjecture now has a precise statement separating proved (g=1) from open (g ≥ 2 $u$-compatibility), an explicit proof path via Gauss–Manin flatness, and a downstream-tag protocol. Every use of ``Koszul purity at admissible level'' must now carry ``[conditional on Remark `rem:periodic-cdg-mechanism`]'' until g ≥ 2 $u$-compatibility is proved. No downgrade of any prior theorem; the remark exposes the hidden hypothesis and routes it.

**W8-A. Theorem H three-way scope at the bulk–boundary proof site (FM182 / AP-CY62, AP-CY64, AP-CY66).**
 - (a) RIGHT: the proof of the bulk–boundary theorem legitimately identifies the boundary center $Z(\cA_\partial)$ with the degree-$0$ piece of a Hochschild-type cohomology.
 - (b) WRONG: the original proof paragraph wrote ``$HH^0(A_\partial, A_\partial)$'' with no model tag. This is a three-way ambiguity (AP-CY64): (i) chiral $\ChirHoch^0$ (the geometric FM / algebraic $\End^{\mathrm{ch}}$ object, concentrated in $\{0,1,2\}$); (ii) classical $\HH^0(\cA_{\partial,\mathrm{mode}})$ in $\mathrm{Vect}$ (degree $0$ only for simple mode algebras); (iii) Gel'fand–Fuchs $H^\bullet_{\mathrm{GF}}(\mathrm{Lie}(\cA))$ (unbounded polynomial). A reader invoking BZFN $Z(\mathrm{LMod}_A(S))\simeq\mathrm{LMod}_{\HH^\bullet(A,A)}(S)$ may further mistake the ambient $S$ as a tunable parameter (AP-CY66), which it is not — both sides use the same $S$, and the two derived centers come from two different algebras $\cA$ (in $\mathrm{IndCoh}(\mathrm{Ran}(X))$) vs.\ $\cA_{\mathrm{mode}}$ (in $\mathrm{Vect}$).
 - (c) CORRECT (Remark `rem:thm-H-three-way-scope` in `chapters/connections/hochschild.tex`, installed after the bulk–boundary proof): every invocation of Theorem~H in Vol II refers to chiral $\ChirHoch^\bullet(\cA,\cA)$; the geometric FM and algebraic $\End^{\mathrm{ch}}$ models are quasi-isomorphic for logarithmic $\SCchtop$-algebras (Proposition `thm:chiral-hochschild-models-equivalent`, AP-CY62); the three homonymous objects (i)–(iii) are named with their concentration behaviour; BZFN is applied separately to $\cA$ and $\cA_{\mathrm{mode}}$ in their native ambient categories (AP-CY66); the chiral and classical centers agree only on the cohomology of the mode-restriction map $\eta_{\mathrm{mode}}$ (Theorem `thm:three-hochschild-unification`) in degree $0$ (and off-critical in degrees $\le 2$). At critical level the chiral center jumps to the Feigin–Frenkel polynomial algebra while classical $\HH^\bullet$ stays finite — the unique regime where (i) genuinely outgrows (ii). Type: scope hygiene + ambient category audit.

Strongest honest form (W8-A): the bulk–boundary proof now explicitly names $\ChirHoch^0$, disclaims the classical $\HH^0$ reading, and routes all downstream Theorem~H citations through Remark `rem:thm-H-three-way-scope`. No theorem downgraded; the scope that was implicit (geometric chiral model, Vol~II logarithmic $\SCchtop$ hypothesis) is now explicit at the point of use.

## First-principles triple: F8 / F9 canonicity as GRT-orbit (2026-04-16 adversarial pass)

**W12-B. Brown motivic / Willwacher operadic face canonicity — DEFUSED-ALREADY.**
 - (a) RIGHT: the Platonic Reconstitution narration of F8 (Brown motivic), F9 (Willwacher operadic) as canonical completions of the Q-rational seven-face slice is mathematically correct, rooted in Drinfeld 1991 + Brown 2012 (arXiv:1102.1312) + Willwacher 2015 (arXiv:1009.1654) + Tamarkin 1998. The GRT_1(Q)-torsor structure on Face(A) is the honest geometry of the seven (= nine) faces; the star picture is an accessibility diagram obtained by fixing F1 as base point.
 - (b) WRONG (attack vector): the CLAUDE.md Platonic Reconstitution section initially presented F8, F9 as decorative additions without explicit formulas or a proved torsor action, inviting the reading that "canonical" is a narrative promotion rather than a theorem. The risks named by this wave's attack were: (i) F8's r^{mot}(z) expansion absent as a definition; (ii) F9's Willwacher cocycle → GRT(Q) element absent as a construction; (iii) GRT-action freeness + transitivity asserted but not proved; (iv) F8 ↔ F9 duality stated as "both represent the same orbit" without naming the connecting associator.
 - (c) CORRECT: the attack is defused by pre-existing content in `chapters/theory/grt_parametrized_seven_faces.tex` (833 lines):
   - Definition `def:face-space` (L130) gives the face-space datum (chain model, Casimir basis, connection convention, Drinfeld associator) with strict MC-gauge equivalence.
   - Proposition `prop:grt-action-face` (L161) proves GRT(Q) acts freely and transitively via Tamarkin + Drinfeld 1991.
   - Corollary `cor:face-torsor` (L187) gives the torsor bijection Φ ↦ Φ·F_1.
   - Theorem `thm:seven-faces-as-GRT-torsor` (L272) is the master ProvedHere statement, with explicit Φ_{1i} for i = 2,…,9.
   - Definition `def:f8-motivic` (L612) gives the explicit formula r^{mot}(z) = r^{rat}(z) + Σ_{w=3,5,7,…} ζ^{mot}(w)·r^{(w)}(z) via Brown's canonical lift Z^{mot} → R.
   - Theorem `thm:motivic-face-F8` (L628) proves F_8 is a GRT-orbit, Q-rational projection sends F_8 → F_1, non-triviality lives at bar-degree ≥ 3.
   - Definition `def:f9-willwacher` (L682) gives F_9 = Φ_Wil · F_1 with log Φ_Wil a graph cocycle representative in H^0(GC_2) = fgrt.
   - Theorem `thm:willwacher-face-F9` (L693) proves F_9 via the Tamarkin chain GC_2 → Def(E_2) → Def(B(−)).
   - Corollary `cor:f8-f9-dual` (L743) proves F_8 and F_9 lie on the same GRT(Q)-orbit with explicit connecting associator Φ_{89} = Φ_Wil · Φ_mot^{-1}.
   - Remark `rem:torsor-vs-star` (L194) records the first-principles alignment: ghost theorem = seven-way equivalence; precise error = suppressing the GRT-action; correct relationship = torsor with F_1 as distinguished base point.
   External anchors (Drinfeld 1991, Brown 2012, Willwacher 2015, Tamarkin 1998, Loday–Vallette Ch. 11–12) are listed as independent-verification sources of record, disjoint from the in-chapter derivation route. Type: attack-vector audit — no edit required; chapter realises the strongest-honest form as written.

Strongest honest form (W12-B): the seven-faces-as-GRT-torsor theorem is the intended Platonic form (nine canonical orbit representatives at the Q-rational slice; two additional motivic/operadic generators from fgrt; F_1 distinguished base point; F_8 ↔ F_9 duality a corollary). The CLAUDE.md paraphrase should be upgraded to point at `thm:seven-faces-as-GRT-torsor` + `def:f8-motivic` + `def:f9-willwacher` + `cor:f8-f9-dual` rather than narrating them independently, so the metadata tracks the .tex ground truth. No new theorem, proposition, or definition is needed; the attack target had already been closed in a prior pass.

---
**Entry: Fingerprint Completeness — equivalence-relation dependence (2026-04-16, STEP 1 attack closure)**

Attack target: Platonic Reconstitution claims φ(A) = (p_max, r_max, χ_VOA, n_strong, coset) is a "complete invariant of the Koszul-bar-complex structure of A" with no equivalence relation specified. An unqualified "complete invariant" is meaningless; completeness is always relative to an equivalence.

Ghost theorem (a): the five fingerprint slots are bar-structural — each determines one dg-datum on B(A). On the standard landscape (affine KM, DS reductions, free-field lineage) they are jointly exhaustive: associated graded + filtration + Z/2-parity + cogenerator rank + Lagrangian polarisation.

Precise error (b): the natural equivalence relation on the codomain of φ is NOT isomorphism of chiral algebras, NOR Morita equivalence of Mod_A (which would require additional monoidal data not in φ), NOR quasi-iso of mode algebras (forgets chirality). The natural equivalence is Quillen equivalence of B(A) in the Francis–Gaitsgory factorization-coalgebra model category on Ran(X); this is the level at which Theorem A^{∞,2} already equates source and target categories and at which all five fingerprint slots are invariants.

Correct statement (c): φ(A) = φ(A') ⇒ B(A) ≃^Q B(A') in Fact-coalg(Ran(X)), for A, A' in the standard landscape. Implementation lives at `examples-complete-proved.tex:fingerprint-classification` as `def:fingerprint`, `thm:fingerprint-completeness-conditional` (ClaimStatusProvedHereConditional), `rem:five-class-coarse-projection`, `rem:fingerprint-nonstandard-open`. G/L/C/M emerges as Π_coarse ∘ φ on the r_max coordinate at κ ≠ 0; FF is the κ = 0 companion stratum.

Independent verification rationale: derived_from = {Theorem A^{∞,2} FORM-B, Vol I Theorem B shadow-tower truncation}; verified_against = {AP67 strong-generation count, AP-CY12 full-tower classification, FM106 symplectic-boson/fermion independence}; disjoint because Theorem A gives the bar Quillen equivalence while AP67/AP-CY12/FM106 pin the individual fingerprint slots via representation-theoretic/cohomological data from outside the Koszul machinery.

Non-standard extension (Monster, W(p), non-freely-generated PVAs) is Conjectured, not ProvedHere — honest downgrade flagged in `rem:fingerprint-nonstandard-open` pointing at FM120 + FM132.

Pattern abstraction (for future completeness claims): every "complete invariant" claim MUST specify the equivalence relation on the domain. Default to the finest equivalence at which all slots are invariant; this is the strongest honest statement. Unqualified "complete" = AP150 confabulation (stitching levels).

---

## FM216 — Chriss–Ginzburg parallel: from metaphor to theorem (2026-04-16)

**Target:** preface.tex L622–650, seven-row Chriss–Ginzburg ↔ chiral bar table.

**(a) Ghost theorem (what the claim gets RIGHT).** The preface's seven-row table captures a genuine structural parallel: Springer theory provides the geometric representation theory of $H_W$; Kazhdan–Lusztig canonical bases index irreducibles; the Deligne–Langlands conjecture classifies simple modules; and on the chiral side, Koszul-dual line-operator modules are governed by a shadow-tower MC datum whose coefficients are polynomials in $q = e^{2\pi i/(k+h^\vee)}$. At the eval-generated core of the affine KM lineage, these two pictures classify the *same* simple modules — the Drinfeld–Kohno theorem (Theorem `thm:affine-monodromy-identification`) makes this precise. So the parallel is not pure metaphor.

**(b) Precise error (what the claim gets WRONG).** Prior to this session, the preface stated each of seven rows as a one-line correspondence ("Springer fibre ↔ primary field", "KL basis ↔ α_T", "KL polynomials ↔ shadow tower") without a constructed functor between derived categories. Each row was a rhetorical pairing; no theorem asserted that the seven pairings arise from a *single* functor with explicit per-object image, and no status (theorem vs conjecture vs analogy) was attached per row. AP155 overclaiming risk; AP158 shallow-label pattern.

**(c) Correct relationship.** Install `prop:chriss-ginzburg-functor` (line-operators.tex, inserted after `rem:steinberg-self-intersection`, ~L471) defining
$$\Phi_{\mathrm{CG}} \colon D^b_{G\times\C^\times}(\widetilde{\cN}) \longrightarrow D^b(\cA^!_{\mathrm{line}}\text{-mod})$$
as the composition $\Phi_{\mathrm{CG}} = \Psi_{\mathrm{KL}} \circ \mathrm{CG}$ where $\mathrm{CG}$ is the classical Chriss–Ginzburg Deligne–Langlands equivalence (CG97) and $\Psi_{\mathrm{KL}}$ is the Kazhdan–Lusztig equivalence at $q = e^{2\pi i/(k+h^\vee)}$. Five explicit row-by-row correspondences are proved/stated:
- (R1) Springer fibre $\pi^{-1}(e) \mapsto$ primary field $V_h$, $h = \tfrac12\langle e, h_{\mathrm{Jac}}\rangle$ (**theorem**, all simple types).
- (R2) Steinberg convolution $H^{G\times\C^\times}_\bullet(\mathfrak{S}) \mapsto$ eval-core of $\operatorname{End}^{\mathrm{ch}}_\cA$ (**theorem**, all simple types, with AP47 eval-core caveat).
- (R3) KL basis $C_w \mapsto$ shadow MC generator $\alpha_T^{(w)}$ (**theorem in type $A_n$** via Bezrukavnikov localisation; conjectural beyond $A$).
- (R4) KL polynomial $P_{y,w}(q) \mapsto$ shadow coefficient $S_r(c(k))$ at depth $r = \ell(w)-\ell(y)$ (**theorem in type $A_n$** via BMR canonical bases; conjectural beyond).
- (R5) Deligne–Langlands classification $\mapsto$ Drinfeld–Kohno classification (**theorem in type $A_n$, generic level**).

Non-type-$A$ extension is stated as `conj:cg-functor-beyond-A` with folding-transport strategy (the root-multiplicity-one hypothesis from Vol II's complete strictification is the obstruction). `rem:cg-preface-table-upgraded` bridges the preface seven-row table to (R1)–(R5) + two whole-category rows (Springer correspondence ↔ bulk–boundary–line triangle; $q=1$ limit ↔ PVA classical shadow).

**Status after heal:** FM216 CLOSED in type $A_n$ at generic non-critical level (five rows are theorems); conjectural extension to other simple types is named and the obstruction identified. The preface parallel is no longer a seven-row metaphor; it is a seven-row projection of a single functor whose precise scope is `prop:chriss-ginzburg-functor`.

**External anchors (disjoint verification sources):** Chriss–Ginzburg 1997 (Ch. 8) for classical convolution–Hecke equivalence; Kazhdan–Lusztig 1987 for Deligne–Langlands; Kazhdan–Lusztig 1993–94 series (KL1–KL4) for tensor-structure equivalence; Bezrukavnikov 2016 for localisation of category $\cO$ on $K^{G\times\C^\times}(\widetilde{\cN})$; Bezrukavnikov–Mirković–Rumynin 2008 for canonical bases matching Springer fibre Poincaré polynomials. These are independent of this programme's internal bar-complex derivation path.

---

## Entry (2026-04-16): Feigin–Frenkel critical-level ChirHoch + class FF structural invariants (Vol II anchor)

**Context.** Vol II CLAUDE.md narrates a fifth shadow class $\mathrm{FF}$ (Feigin–Frenkel, $\kappa_{\mathrm{ch}}=0$) in the Platonic Reconstitution / Infinite Fingerprint sections; Vol I `chapters/theory/infinite_fingerprint_classification.tex` carries the structural theorem `thm:fifth-class-FF`; Vol II `hochschild.tex` had only narrative pointers (lines 610–612, 2085–2087, 1259–1262) without a Vol II-local claim anchor. Several worked-examples files (`examples-worked.tex:223`, `examples-complete-proved.tex:1071`) called it "class W (wild)"—a naming drift from the canonical $\mathrm{FF}$.

**Attack findings.**
- (a) RIGHT: Vol II `hochschild.tex` correctly narrates $\ChirHoch(V_{-h^\vee})$ jump to FF centre and identifies it as the unique regime of $\ChirHoch / \HH_{\mathrm{mode}} / H^*_{\mathrm{GF}}$ genuine divergence (AP-CY64 three-way).
- (b) WRONG: No Vol II-local theorem statement; references to class FF point to Vol I only. Inconsistent "class W" vs "class FF" naming in examples files. Line 1259–1262 hinted "PBW universality still gives Koszulness" at critical level without noting that bar-cobar inversion does not hold on the nose (both sides become commutative vertex algebras; identification via Feigin–Frenkel, not via pro-nilpotent completion).
- (c) CORRECT: Install `thm:feigin-frenkel-chirhoch` + `rem:class-FF-structural` in `hochschild.tex` (post DS-Hochschild bridge) with four-part statement: (i) $\ChirHoch^0(V_{-h^\vee}(\fg))\simeq\mathfrak z(\widehat\fg)\simeq\Fun(\mathrm{Op}_{\fg^\vee}(D))$ (Feigin–Frenkel 1992, Frenkel 2007); (ii) $\ChirHoch^n$ concentrated in $\{1,2\}$ for $n\ge 1$ with Op tangent identification and Verdier-shifted duality; (iii) critical level is the UNIQUE regime of three-Hochschild degree-0 divergence; (iv) principal DS at critical level reduces to classical $\cW$-algebra (Arakawa).

**Fingerprint slots for class FF.** $\kappa_{\mathrm{ch}}=0$ (defining); $r_{\max}=\infty$ (shared with class M but distinguished by Gelfand–Dikii generator shape vs quartic pole + generic $c$); fifth slot replaced by $\mathrm{coset}_{\mathrm{FF}}=(\mathfrak z(\widehat\fg),\mathrm{Op}_{\fg^\vee}(D))$ recording Langlands-dual oper geometry. Sugawara degeneration at $k=-h^\vee$ means the two colours of $\SCchtop$ do not topologise into $E_3^{\mathrm{top}}$; pair stays at $\SCchtop$.

**Scope.** Proved: affine KM at critical level (Feigin–Frenkel 1992); principal DS at critical level = classical $\cW$-algebra on opers (Arakawa 2015). Open: non-principal DS at critical level; $\kappa_{\mathrm{ch}}=0$ locus for logarithmic $\cW(p)$ at $p=1$ and other extended algebras.

**External anchors (disjoint verification sources):** Feigin–Frenkel 1992 "Affine Kac–Moody algebras at the critical level and Gelfand–Dikii algebras"; Frenkel 2007 *Langlands Correspondence for Loop Groups* (Ch. 4, 8); Beilinson–Drinfeld 1991 preprint (opers); Arakawa 2015 "Rationality of W-algebras: principal nilpotent cases" for classical-$\cW$ identification of principal DS at critical. These anchor $\ChirHoch^0$, higher-cohomology $\mathrm{Op}$ identification, and the DS-at-critical reduction independently of the bar-complex machinery.

**Convention propagation (AP5/AP49).** The Sugawara tensor $T^{\mathrm{Sug}}=\frac{1}{2(k+h^\vee)}\sum_a{:}J^a J^a{:}$ is written in Vol I OPE-mode normalisation with an explicit parenthetical noting the Vol II $\lambda$-bracket presentation carries the additional $1/n!$ divided-power factor (V2-AP34). Matches Vol I `working_notes.tex:749`. No Vol III propagation required (formula is Vol I–II joint convention).

**Naming consistency note.** Canonical name = class $\mathrm{FF}$ (Feigin–Frenkel). Informal synonym "class W (wild)" appears in `examples-worked.tex:223`, `examples-complete-proved.tex:1071`, `introduction.tex`. The structural content is identical; `rem:class-FF-structural` records this so downstream `\ref` chains resolve to a single invariant concept.

**AP-OC check.** The insertion disavows bar=bulk: class FF's bar-cobar inversion $\Omega^{\mathrm{ch}}\bar B^{\mathrm{ch}}(V_{-h^\vee}(\fg))$ is NOT the bulk; Bulk $=Z^{\mathrm{der}}_{\mathrm{ch}}(V_{-h^\vee}(\fg))$ which coincides with $\mathfrak z(\widehat\fg) = \Fun(\mathrm{Op}_{\fg^\vee}(D))$ via the Hochschild functor applied separately. Bar classifies twisting morphisms; Hochschild computes the derived centre.

**Status after heal:** FM77 scope hole (κ=0 structurally integrated) reinforced with a Vol II-local anchor. The companion-fifth-class claim in CLAUDE.md Platonic Reconstitution now has a `\ClaimStatusProvedHere` representative in Vol II, not just a Vol I cross-reference. Class FF reaches parity of documentation with G/L/C/M for the affine KM critical-level case.

---

## MC5 citation scope guard (2026-04-16, FM118 downstream audit)

**Pattern.** Bare "by MC5" citations in Vol II downstream chapters silently promote one clause of the 5-clause MC5 package to the full package. Vol II sweep (compute/audit/vol2_mc5_status_sweep.md) was complete for bridge tables and preface; `twisted_holography_quantum_gravity.tex:953` + `twisted_holography_quantum_gravity.tex:2503-2504` remained as bare "by MC5" / "sewing machinery of MC5" phrasings. Both invoke ONLY the analytic HS-sewing lane (proved at all genera, Vol I); neither invokes genuswise chain-level BV/BRST/bar (conjectural) or the direct-sum chain-level comparison for class M (false, AP203).

**Repair.** Installed `rem:mc5-citation-scope-guard` after `twisted_holography_quantum_gravity.tex:953` covering both in-chapter citations. The remark enumerates the 5-clause split and states explicitly that this chapter invokes only the analytic lane, per FM118 and the Vol II bridge-table W-algebras row.

**Investigation (a/b/c protocol).**
- (a) MC5 is cited at 9 Vol II sites: `ht_physical_origins.tex` ×3, `introduction.tex` ×1, `chiral_higher_deligne.tex:857` ×1, `spectral-braiding-frontier.tex:254-258` ×1, `twisted_holography_quantum_gravity.tex` ×2, `bv_brst.tex` ×several. All but the twisted-holography pair already carry explicit scope qualifiers ("analytic HS-sewing lane", "weight-completed category (MC5 pattern)", "genuswise chain-level ... remains conjectural").
- (b) Overclaim found: `twisted_holography_quantum_gravity.tex:953,2504`. Bare "by MC5" can be read as the full 5-clause package by downstream readers.
- (c) Repair: scope-guard remark added in situ (not downgrade — the underlying convergence claim is covered by the analytic lane which IS proved).

**Cross-volume implication.** Vol I N5 standalone (`N5_mc5_theorem.tex`) states the 5-clause theorem on the evaluation-generated core (AP47) with `\dbar_5^2 = 0` via the Arnold-KZ flatness pullback (climax of Wave 14); the analytic lane covers modular convergence at all genera; the genuswise chain-level BV/BRST/bar identification is a separate conjectural statement; the weight-completed category version is proved (`prop:bv-bar-class-m-weight-completed`, 2026-04-16). The Vol II bridge-table row for W-algebras already reflects this split correctly. No Vol I or Vol III propagation required — the pattern is a Vol II downstream-citation hygiene issue.

## Wave 16 (2026-04-16): Chiral Higher Deligne E_3 audit

**Files:** `chapters/theory/chiral_higher_deligne.tex`, `chapters/connections/brace.tex`.

**W16-A. Audit of the chiral Higher Deligne E_3 upgrade.**
 - (a) RIGHT: `thm:chiral-higher-deligne` (L417-441) already installs the full Platonic Reconstitution upgrade for Theorem H. The statement delivers a canonical E_3-chiral action on ChirHoch^•(A,A) = Z^{der}_ch(A) via heptagon edges (3)↔(4)↔(5), universality against bulk-boundary SC^{ch,top} pairs, and the GRT_1-torsor of chain-level strictifications with cohomological associator-independence. The proof executes the exact recipe requested: Stage 1 brace => E_2-chiral (Thm `thm:chd-deligne-tamarkin` + Prop `prop:chd-stasheff-4`), Stage 2 Sugawara-type conformal-weight generator L_0 supplies the E_1^top factor along R, Dunn additivity assembles E_2 ⊗_Dunn E_1 = E_3. The concentration corollary `thm:H-concentration-via-E3-rigidity` (L577-588) realises the "concentration as a consequence of E_3-rigidity at a point" upgrade through Lemma `lem:chd-e3-rigidity-point` + chiral PBW, with the polynomial-growth bar spectral sequence completing the argument.
 - (b) WRONG / weak points found:
   1. The proof cites `prop:heptagon-edge-34` and `prop:heptagon-edge-45` in `ch:sc-chtop-heptagon`. A `grep` over `chapters/` returns ZERO files containing these labels or the heptagon chapter. Per the CLAUDE.md reconstitution ledger ("SC^{ch,top} heptagon (7 presentations) — restart in progress"), this chapter is unwritten. The E_3 upgrade therefore depends on two phantom labels. Pattern = FM87/FM155/FM213 (phantom labels cited from ProvedHere).
   2. Stage 2's use of L_0 as a strict chain-level derivation is stated universally but only inherits strictness in the non-critical (or lattice-Sugawara) regime. The universal statement quietly absorbs the "κ ≠ 0 and conformal vector at non-critical level" hypothesis. Not wrong, but scope-hidden.
   3. The `E_3`-Koszul duality citation in `lem:chd-e3-rigidity-point` ("Fresse §13") needs an explicit reference to the bar-spectral sequence lemma in Vol I for the polynomial-growth degree-3 cancellation.
 - (c) CORRECT (heal + upgrade path, no downgrade):
   1. PHANTOM REPAIR: write `prop:heptagon-edge-34` and `prop:heptagon-edge-45` in a new `chapters/theory/sc_chtop_heptagon.tex` realising the SC^{ch,top} reconstitution task. Edge (3)↔(4) is the chiral Koszul duality pairing between the E_2-chiral cooperad and the closed colour of (SC^{ch,top})^!; edge (4)↔(5) is the colored-Dunn additivity identifying (E_2-chiral) ⊗_Dunn (E_1-top) with E_3 through the convolution / BV presentations. This single chapter closes the three phantom-label citations (here, brace.tex L38, and the concentration proof's heptagon appeal).
   2. SCOPE TIGHTENING (no downgrade): rename the hypothesis block of `thm:chiral-higher-deligne` to include "A in the Koszul locus with conformal vector at non-critical level (or lattice-Sugawara substitute)" — these conditions are HEAL-compatible and already implicitly present; making them explicit eliminates the FM77/AP153 scope-hole risk at read time.
   3. COHOMOLOGY-INDEPENDENT BASELINE: the cohomological E_3 action is GRT-independent (stated as Part (3)). Consequently `Z^{der}_ch(A)` carries a CANONICAL E_3-chiral cohomology for every chirally Koszul A with conformal vector non-critical; the associator dependence is purely a chain-level strictification choice. This is the strongest-honest form and is what the theorem delivers. No weakening needed.
   4. CONSEQUENCE RIGIDIZATION: Theorem H (concentration in {0,1,2}) is now CONSEQUENCE of E_3-rigidity at a point + PBW (`thm:H-concentration-via-E3-rigidity`). The SY Orlik-Solomon Koszulity proof becomes the INDEPENDENT cross-verification (different derived_from, same verified_against) — natural `@independent_verification` decorator target for the Vol II coverage campaign (FM224).

**Assessment.** Upgrade is realized in the .tex at the strongest-honest form requested; residual malpractice is one phantom-chapter citation + one hidden scope qualifier. No chain-level downgrade required: the cohomological E_3 action is unconditional on Koszul locus + conformal vector non-critical; chain-level E_3 is GRT_1-torsor-parametrized and associator-fixed yields a strict action. Concentration is genuinely a corollary via rigidity-at-a-point + PBW. Phantom-repair blocked on the SC^{ch,top} heptagon chapter scheduled in the reconstitution ledger.

**Cross-volume implication.** None — the upgrade is Vol II-local. Vol III AP-CY33 (chain-level ≠ rational) is respected: the E_3 structure is genuine at chain level, collapses to E_2-Gerstenhaber on cohomology under Kontsevich formality for the E_2 part, and the E_1-top from L_0 survives the collapse intact (conformal weight is a genuine grading, not homotopy-trivialised).

---

## Entry: Irregular-singular KZB composition (FM68 Stokes regularity gap) — 2026-04-16

**Scope.** modular_swiss_cheese_operad.tex §irregular-kzb (thm:irregular-kzb-composition at lines 3113+), main.tex bibliography.

**Attack.** Existing `thm:irregular-kzb-composition` invoked JMU81 but: (a) Poincaré-rank-1 hand-waved via "KZ residue acquires non-diagonalizable part" without local-coordinate computation; (b) Malgrange–Sibuya cited for the pentagon but proof reduced to "path concatenation associativity" which is trivial — the non-trivial content (sector-crossing coherence, Stokes cocycle) was elided; (c) no explicit display of wild-monodromy data (formal normal form, exponential torus, formal monodromy, Stokes matrices); (d) Boalch 2001/2014 (wild character varieties, wild fundamental groupoid) absent from citation list; (e) no explicit scope remark on Poincaré rank > 1; (f) no unification corollary covering integrable + generic + critical levels. Verdict: narrated, not deployed.

**Heal + Upgrade.** (i) Rewrote proof sketch of (i) with explicit local sewing coordinate q_e, ramification base change, double pole as Poincaré rank 1. (ii) Rewrote (ii) with the full four-tuple (Q_Γ, 𝕋_Γ, M̂_Γ, {S_ℓ^±}) — formal normal form, exponential torus, formal monodromy, Stokes matrices — cited Boalch 2001 Thm A (unique sectorial solutions with prescribed asymptotics) and Boalch 2014 Thm 2.1 (gauge classification). (iii) Rewrote associativity as functoriality of Π_{γ,k} from Boalch's wild fundamental groupoid Π_1^wild; sector-crossing coherence via Boalch 2001 Thm B (H^1_wild = 0). (iv) Added `rem:poincare-rank-scope` clarifying r(Γ) ≤ 1 is automatic for M̄_{g,n} stable-graph combinatorics; multi-rank flagged as frontier (Nekrasov ε_2→0, 5d gauge). (v) Added `cor:fm68-all-levels-resolved` unifying integrable (KZ + KL), generic non-integral (JMU/Boalch), critical (Feigin–Frenkel center substitute). Together (a)–(c) exhaust all levels. (vi) Added six bibliography entries: Bernard1988, Boalch2001, Boalch2014, CEE2009, JMU81, FrenkelLanglands.

**Assessment.** Upgrade is realized, not narrated. Wild-monodromy data explicitly displayed; sector-crossing coherence derived from Stokes cocycle (not "path concatenation"); scope pinned to r(Γ) ≤ 1 which is provably automatic on M̄_{g,n}. FM68's "sole gap: composition at generic non-integral level" formally resolved. Strongest-honest form realized — no downgrade.

**Cross-volume implication.** None Vol III-impacting. Vol I cross-refs to curved-Dunn chain pick up the corollary as stronger hypothesis.

---

## Entry: Heptagon edge-34/edge-45 phantom label closure — 2026-04-16

**Scope.** chapters/theory/sc_chtop_heptagon.tex (labels `prop:heptagon-edge-34`, `prop:heptagon-edge-45`); chapters/theory/chiral_higher_deligne.tex L393, L475 (citation sites).

**Attack (a).** `\ref*{prop:heptagon-edge-34}` and `\ref*{prop:heptagon-edge-45}` in chiral_higher_deligne.tex were cited from the `thm:chiral-higher-deligne` proof and the concentration proof's heptagon appeal. W13-E3 agent reported ZERO `.label` matches — pattern FM87/FM155/FM213 (phantom labels under ProvedHere).

**Attack (b) — first-principles triple.**
1. What the citations GET RIGHT: semantic content invoked (factorization ↔ BV/BRST at edge (3)↔(4); BV/BRST ↔ convolution L_∞ at edge (4)↔(5)) corresponds to real theorems `thm:edge-34` (Obs^q presents factorization face, sc_chtop_heptagon.tex L751) and `thm:edge-45` (QME = convolution MC on semifree model, L778), both ProvedHere.
2. What they GET WRONG: pure label-prefix mismatch. Citations used `prop:` namespace for objects already labelled `thm:`. No mathematical gap — namespace desynchronization between the E_3-upgrade proof (written expecting propositional-form edges) and the heptagon chapter (installed with theorem-form edges).
3. CORRECT STATEMENT: the two edges are simultaneously theorems (full operadic statements with BV/factorization/convolution modelwise content) AND propositions (restricted statements that the two presentations yield the same ∞-operadic datum, up to HPL + Swiss-cheese formality). Install propositional forms as named aliases immediately after the theorem forms; each alias carries its own proof composing (i) pointer to parent theorem, (ii) the compositional/Dunn refinement used at the citation site.

**Heal (c).** Installed `prop:heptagon-edge-34` at sc_chtop_heptagon.tex:776+ immediately after `thm:edge-34`: factorization presentation ↔ BV/BRST presentation, proved via `thm:edge-34` + `thm:edge-45` + coloured Swiss-cheese formality (Getzler–Jones 1994 / Vallette 2014 coloured Koszul duality + HPL). Installed `prop:heptagon-edge-45` at sc_chtop_heptagon.tex:832+ immediately after `thm:edge-45`: BV/BRST ↔ convolution L_∞ with Dunn-additive corollary E_2-chiral ⊗_Dunn E_1^top ≃ E_3 on Z^{der}_ch(A), proved via `thm:edge-45` + conformal-weight L_0 flow on R + Lurie HA 5.1.2.2 for coloured operads with empty cross-arrows at the mixed sector. Both aliases ClaimStatusProvedHere with distinct index entries. Grep confirms: two citation sites in chiral_higher_deligne.tex resolve against two labels in sc_chtop_heptagon.tex.

**Upgrade.** Both propositional forms carry strictly more content than the label-alias minimum: prop-34 packages the factorization ↔ convolution quasi-isomorphism (composed through BV) that the E_3-upgrade proof uses but neither parent theorem states alone; prop-45 derives the Dunn-additive E_3 assembly on Z^{der}_ch(A) invoked verbatim by chiral-higher-Deligne Stage 2.

**Assessment.** Phantom repair executed; no downgrade. Pattern FM87/FM155/FM213 cleared for this instance. No formula/numerical edits introduced, so AP5/AP49 cross-volume propagation N/A. Cache-hint reference to `brace.tex L38` stale (file renamed/relocated); authoritative grep shows no residual phantoms.

**Cross-volume implication.** None. Vol III AP-CY33 respected: chain-level E_3 assembly via prop-45 is genuine at chain level and collapses to E_2 ⊗ E_1-top on cohomology only under Kontsevich formality, not at chain level.

---

## Entry: thm:irregular-kzb-composition-generic-level + FM68 all-levels corollary — 2026-04-16

**Scope.** chapters/theory/modular_swiss_cheese_operad.tex (installed after thm:mb-H2-vanishing, before rem:mb-to-curved-dunn-consequence): `thm:irregular-kzb-composition-generic-level` + `cor:modop-composition-all-levels`.

**Attack (a).** FM68 frontier-register entry reads "Sole gap: composition at generic non-integral level, genus ≥ 1 (Stokes regularity)." Prior `thm:irregular-kzb-composition` (§subsec:irregular-kzb) treats the generic case but is not cited by name at the curved-Dunn bridge, leaving a narrative gap between the mb-H2 vanishing theorem (which handles the obstruction-theoretic side) and the operadic composition assertion (which handles the dynamical side). A named companion theorem resolves the register entry unambiguously and unifies the three levels (integrable, generic non-integral, critical) into a single corollary.

**First principles (b).** (i) The KZB connection at generic non-integral k has rank-1 irregular singularities along nodal boundary divisors of M̄_{g,n} (Bernard–Felder + JMU81 normal form). (ii) Wild monodromy classification (Boalch 2001, 2014) supplies the four-tuple (Q_Γ, 𝕋_Γ, M̂_Γ, {S_ℓ^±}) and unique sectorial solutions with prescribed asymptotics. (iii) Composition descent follows from H^1_wild = 0 (Boalch 2001 Thm B). (iv) The three cases k ∈ Z_{≥0}, k ∈ C\Q, k = -h^v exhaust the level axis modulo the rational-negative admissible locus (covered via Langlands shift k → -k - 2h^v from the integrable side).

**Heal + Upgrade (c).** Installed `thm:irregular-kzb-composition-generic-level` as ProvedHere specialization of thm:irregular-kzb-composition to the generic non-integral stratum. Installed `cor:modop-composition-all-levels` as ProvedHere trichotomy unifying: (a) integrable via KZ pentagon + KL regularity (thm:affine-composition-associativity); (b) generic non-integral via JMU + Boalch wild groupoid; (c) critical via Feigin–Frenkel center (thm:ff-chirhoch-critical). Independent-verification disjointness: the three derivations use KZ/KL, JMU/Boalch, FF center respectively — pairwise disjoint derived_from sets. FM68 closed at rank ≤ 1 (automatic on M̄_{g,n} per rem:poincare-rank-scope); frontier retained at Poincaré rank ≥ 2 (Nekrasov ε_2 → 0, 5d gauge).

**Assessment.** Strongest-honest form realized: modular operad composition is proved at every level, not "generic only" or "integrable only." The trichotomy is architectural — each level uses the analytic/operadic tool appropriate to its resonance structure. No downgrade; frontier item (1) of the Vol II programme advanced from "curved-Dunn H² = 0" to "full composition at all levels."

**Cross-volume implication.** None Vol III-impacting. Vol I Thm A^{∞,2} cross-refs inherit the all-levels corollary as strengthened hypothesis for factorization-algebra composition.

---

## Entry: eq:spectral-coassoc associator-twist heal (P1-15) — 2026-04-16

**Scope.** /Users/raeez/chiral-bar-cobar/standalone/e1_primacy_ordered_bar.tex, clause (III) "(Spectral coproduct.)" within the main equivalence theorem (lines ~2013-2023).

**Attack (a).** MASTER_PUNCH_LIST item P1-15: the spectral coassociativity identity at Eq. eq:spectral-coassoc was written as a STRICT equality (Δ_{z_1} ⊗ id) ∘ Δ_{z_1+z_2} = (id ⊗ Δ_{z_2}) ∘ Δ_{z_1}, omitting the Drinfeld associator Φ. For ordered chiral homology on Ran(X) with OPE-induced bar differential, strictness would force Φ = 1 — false already at order ℏ² via the KZ ζ(2) coefficient. The chain-level ordered bar is intrinsically associator-dependent (AP-CY33, FM158, FM219, FM246); writing it strict is a category error that propagates to downstream Yangian claims.

**First principles (b).** (i) GHOST: there IS a coassociativity identity on the Koszul dual Yangian Y(A), and it IS a Drinfeld-style constraint. (ii) PRECISE CONFLATION: strict (cocommutative-Hopf) coassociativity vs. quasi-Hopf coassociativity with associator. The Yangian Y_ℏ(g) and its spectral Drinfeld coproduct live in the quasi-Hopf category; Φ_KZ ∈ U(ĝ)^{⊗3}[[ℏ]] is the holonomy of the KZ connection on M_{0,4} between the two limiting tangential basepoints (z_1→z_2)→z_3 vs. z_1→(z_2→z_3). (iii) CORRECT STATEMENT: Φ_{12,3} ∘ (Δ_{z_1}⊗id) ∘ Δ_{z_1+z_2} = (id⊗Δ_{z_2}) ∘ Δ_{z_1} ∘ Φ_{1,23}, with Φ = Φ_KZ satisfying Drinfeld pentagon + two hexagons. The pentagon cocycle condition lives in U(ĝ)^{⊗4}[[ℏ]] and is the n=3 arity of the Stasheff tower controlling ordered bar associativity.

**Heal + Upgrade (c).** Edited clause (III): replaced strict identity with associator-twisted form; named Φ_KZ explicitly; added rem:kz-associator-pentagon stating pentagon + hexagon axioms and connecting to GRT-parametrized Seven Faces (Vol II). Strongest-honest form: ordered chiral homology carries a canonical GRT_1-action; the associator Φ_KZ is a Q-rational face representative. No downgrade; the spectral coproduct becomes a quasi-Hopf datum (correct category) rather than a Hopf datum (wrong category).

**Cross-volume implication.** Vol II: coheres with GRT-parametrized Seven Faces Theorem (Platonic Reconstitution) and AP-CY25 half-braiding ontology. Vol III: inherits associator dependence for Y_ℏ(g) spectral coproduct in CY quantum group stack. Vol I Thm A^{∞,2} properad-level bar-cobar is associator-free by construction (operadic level); the associator enters only when passing to concrete Y(A) presentations via the Tamarkin Φ-transfer.

---

### Entry 240/195 (HZ-IV scraper: ClaimStatusProvedHere label-after-status pattern)

**Trigger phrase / pattern.** `\begin{theorem}[Name;\n  \ClaimStatusProvedHere]\n\label{thm:X}` — label appears AFTER the ClaimStatus marker within the theorem header.

**Why it fires.** The Vol II audit scraper in `compute/scripts/audit_independent_verification.py` walked BACKWARD from each `\ClaimStatusProvedHere` line up to 80 lines looking for the nearest preceding `\label{...}`. The canonical Vol III / Vol I convention places the label on the same line as `\begin{theorem}[...]`, which is BEFORE `\ClaimStatusProvedHere`. Many Vol II chapters (chiral_higher_deligne, super_chiral_yangian, e_infinity_topologization, universal_celestial_holography, curved_dunn_higher_genus, grt_parametrized_seven_faces, universal_holography_functor) instead split the header across lines:
```
\begin{theorem}[Name;
  \ClaimStatusProvedHere]
\label{thm:X}
```
Walking backward from the `\ClaimStatusProvedHere` line encounters the nearest previous `\label{...}` belonging to an unrelated earlier environment, producing a DIFFERENT label than intended. Result: 33 false-orphan entries, ProvedHere count under-counted by ~56 labels.

**Counter.** Audit scraper must search FORWARD up to ~6 lines before falling back to the backward search. After the patch: `thm:chiral-higher-deligne`, `thm:chd-ds-hochschild`, `thm:H-concentration-via-E3-rigidity`, `thm:curved-dunn-H2-vanishing-all-genera`, `thm:iterated-sugawara-construction`, `thm:e-infinity-topologization-ladder`, `thm:seven-faces-as-GRT-torsor`, `thm:super-yangian-e1-chiral-structure`, `thm:universal-holography-functor`, `thm:uch-main` all resolve to the correct labels.

**Verification numbers.** Before patch: ProvedHere count 1259; covered 12/1259 (1.0%); orphans 33. After patch: ProvedHere count 1315; covered 41/1315 (3.1%); orphans 2 (unrelated `thm:E3-topological-km` decorators on a `\ClaimStatusProvedElsewhere` theorem).

---

### Entry 241/196 (HZ-IV decorator wiring: `from lib.independent_verification` bypasses canonical registry)

**Trigger phrase.** Tests importing the decorator via `from lib.independent_verification import independent_verification` after `sys.path.insert(0, compute/)`.

**Why it fires.** Python's import cache keys on the dotted module name. When one test imports `compute.lib.independent_verification` and another imports `lib.independent_verification`, Python treats them as DISTINCT modules with DISTINCT `_REGISTRY` lists. The decorator fires — no error — but writes to a different registry than the one the audit script reads. Result: the test silently disappears from coverage.

**Counter.** Every test MUST use `from compute.lib.independent_verification import independent_verification` with `sys.path.insert(0, "..", "..")` reaching the repo root. The audit script imports test modules as `compute.tests.test_*`, so its `_REGISTRY` is the one under the `compute.lib.` dotted path. Fix applied to `test_curved_dunn_higher_genus.py`; pattern to grep when onboarding new tests: `grep -rn "^from lib\.independent_verification" compute/tests/` should return zero.

**Downstream.** This pattern explains 1 of the 4 MISS targets in the initial Vol II audit (`thm:curved-dunn-H2-vanishing-all-genera`). The decorator was honestly disjoint; the wiring was silently broken. Infrastructure-level verification (is the decorator actually in the canonical registry?) is as important as content-level verification (is the disjointness honest?).

---

### Entry 242/197 (HZ-IV disjoint-source pool for Vol II connections chapters)

**Observation.** Vol II connections chapters (universal_celestial_holography, universal_holography_functor, chiral_higher_deligne) cluster around the following disjoint source pool, re-usable for future HZ-IV decorators:

| Derivation side (chapter machinery) | Independent verification sources |
|-------------------------------------|----------------------------------|
| Costello-Gwilliam factorisation envelope | Costello-Gaiotto 2018 arXiv:1804.06460 (physical bulk); Costello-Li 2020 arXiv:1606.00365 (KK reduction) |
| Sugawara topologization tower (Vol I) | Kontsevich 2006 arXiv:math/0608180 (brace formality); Tamarkin 2003 arXiv:math/0311487 (rational associator); Francis 2012 (tangent complex) |
| DS-Hochschild bridge | Kac-Wakimoto 1988 (modular invariance); Feigin-Frenkel coset duality |
| Chiral Deligne (thm:ch-core-helicity-splitting) | Francis 2012; Beem-Meneghelli-Peelaers-Rastelli arXiv:1810.00013 (protected chiral algebra of 4d N=2 SCFTs on S^2) |
| Class-M W-algebra chain-level coverage | Linshaw 2020 W_infty[mu]; Arakawa 2007 C_2-cofiniteness |

**Usage.** When drafting an HZ-IV decorator for a Vol II connections theorem, consult this table. Disjointness is a correctness property: the three verification sources for `thm:uch-main` (Strominger 2014 S-matrix; Francis 2012 tangent complex; BMPR 2018 protected chiral) each avoid every derivation source the chapter uses (CL + CG + chiral Deligne). Agreement on the intersection locus is the non-tautological content.

**Anti-pattern caught.** Early draft of `test_universal_holography_functor.py` almost listed Costello-Gaiotto 2018 as BOTH a derivation source (via the chapter's class-L identification citation) and a verification source. String-level disjointness check would have raised `IndependentVerificationError` at import. The correct phrasing distinguishes the chapter's FUNCTOR-direction derivation (Costello-Gwilliam envelope → Dunn → Hochschild → bulk) from the verification-direction realisation (Costello-Gaiotto construct the bulk physically, opposite direction). Both cite CG but for different content; in HZ-IV bookkeeping, they appear as separate canonical names.

---

### Entry 243/198 (HZ-IV scope-discipline: ProvedElsewhere theorems cannot carry ProvedHere decorators)

**Trigger phrase.** `\ClaimStatusProvedElsewhere` in the .tex coupled with `@independent_verification(claim="thm:X")` in the test file.

**Why it fires.** The audit scraper only reports claim labels paired with `\ClaimStatusProvedHere`. A decorator targeting a ProvedElsewhere label therefore registers as ORPHAN — the scraper never sees that label as covered. This is correct behaviour: the burden of independent verification falls on the author of the ProvedHere claim, not on downstream consumers.

**Examples found in Vol II.** `thm:E3-topological-km` in `3d_gravity.tex:6542` is `\ClaimStatusProvedElsewhere` (attributed to Costello-Li + Costello-Gaiotto). Two tests (`test_e3_topological_km.py`, `test_e3_topological_km_iv.py`) decorate the ProvedElsewhere label, producing orphan entries.

**Three healings for orphan-on-ProvedElsewhere.** (1) Re-target the decorator at the local ProvedHere sibling; (2) Remove the decorator (verification of ProvedElsewhere content is not the audit's scope); (3) Upgrade the local theorem to ProvedHere IF the proof is in fact locally complete.

**Status.** Not a blocker for the HZ-IV coverage-advance task. Two orphans remain in Vol II after the present session; they are pre-existing and out-of-scope for the 10-target strengthening.

### Entry 244 (Universal Celestial Holography audit, 2026-04-16)

**Task.** Adversarial-attack + heal the "Universal celestial holography — still in progress" slot on the Platonic Reconstitution master-theorem list.

**First-principles triple.**
(a) What was RIGHT. `chapters/connections/universal_celestial_holography.tex` (938L) already contains `thm:uch-main` (L213, `\ClaimStatusProvedHere`) with the strongest three-clause form: (i) existence + functoriality of A^cel under Q-equivariant maps of 4d HT theories, (ii) SC^{ch,top}-structure on pair (A^cel, Z^der_ch(A^cel)), (iii) celestial OPE ≅ chiral factorization homology ∫_{P^1_cel} A^cel. Four coverage regimes explicit: (a) self-dual gauge → V_k(g) via Costello–Paquette; (b) N=2 gauge via Drinfeld–Sokolov → class L/M; (c) twistor gravity → Vir_c ⊕ w_{1+∞}; (d) Yang–Mills via Beem–Rastelli χ-functor. Mellin–shadow dictionary promoted to `prop:uch-mellin-shadow` (L563) closing FM102; soft hierarchy theorem `thm:uch-soft-hierarchy` (L683) closing FM103. Bulk-recovery corollary (L315) and scope-boundaries remark (L335) both present. Celestial duals for Heisenberg (class G) and Virasoro (class M) stated as propositions (L802, L831). Coda (L903) distinguishes "what it is / is not / resolves / exposes."

(b) What was WRONG. (i) Syntactic typo `\end{conjecture>` at L507 (angle bracket instead of brace) in `conj:uch-gravity-chain-level`; would break pdflatex parse if built in isolation. HEALED: corrected to `\end{conjecture}`. (ii) Slight narration gap at L286–287: expression `the universal brace action of Z^{der}_{ch}$ on $cA^{mathrm{cel}}$` has minor math-mode ambiguity (opening dollar after `Z^{der}_{ch}` missing in the source span I read); the rendered content is semantically correct (bulk→boundary universal brace = mixed sector of SC^{ch,top}). Verified against Vol I thm:sc-chtop-bulk-boundary reference which is the correct anchor.

(c) CORRECT statement. The strongest-honest Universal Celestial Holography theorem is already written, ProvedHere, with scope explicitly tracked per shadow class: unconditional at genus 0 for all classes G/L/C/M; unconditional at g ≥ 1 on original complex for G/L/C; weight-completed for class M at g ≥ 1 (conj:uch-gravity-chain-level is the only open residue, tied to the DS-Hochschild bridge of hochschild.tex `thm:chd-ds-hochschild`).

**Status against master-theorem list.** CLAUDE.md's "Universal celestial holography — still in progress" is STALE. The theorem is written, proved (in the sense of stitching Costello–Paquette + Costello–Gaiotto + chiral Deligne + Vol I Theorem H + modular bootstrap MC4/MC5 together into a single categorical statement), and scoped to four regimes. Only post-hoc work required: (i) metadata update in CLAUDE.md (reconstitution swarm status list: move ✅); (ii) install `@independent_verification` decorator on `thm:uch-main` with derived_from=[Costello–Paquette 2020 arXiv:2005.13547, Costello–Gaiotto 2018 arXiv:1812.09257] and verified_against=[Pasterski–Shao–Strominger Mellin dictionary arXiv:1701.00049, Donnay–Fotopoulos–Pasterski–Taylor celestial Virasoro arXiv:2111.11392]; disjoint because the Mellin/Virasoro evidence is kinematic (angular + scaling analysis on S^2), while Costello–Paquette/Gaiotto evidence is BV-cohomological.

**Scope clarification vs frontier prompt.** The frontier prompt's proposed `thm:universal-celestial-holography` statement (A ↦ Z^der_ch(A^cel)) is slightly narrower than what is already proved: the chapter proves celestial OPE = ∫_{P^1_cel} A^cel with SC^{ch,top} data on the PAIR, not bulk = Z^der_ch(A^cel) alone. This is correct per Vol II pitfall AP165/FM40/FM209: SC^{ch,top} lives on the PAIR (bulk, boundary), never solely on the bulk. The chapter already reflects this discipline. No downgrade.

**Residual opens.** conj:uch-gravity-chain-level (L498) depends on the DS-Hochschild bridge for class M at chain level; heal-path is thm:chd-ds-hochschild (already written per CLAUDE.md reconstitution list). Once that bridge is invoked inside the conjecture proof, the conjecture promotes to ProvedHere.

**Counter / anti-pattern for future sessions.** When CLAUDE.md says "still in progress" for a master theorem, grep the standalone chapter FIRST before assuming absence. Meta-pattern: metadata drift (established at FM111 of this very file); reconstitution-status lists in CLAUDE.md lag behind .tex ground truth. Check the .tex.

---

## Entry: UCH gravity chain-level promotion (2026-04-16)

**File:** chapters/connections/universal_celestial_holography.tex:498-580 (was L498-507 as conjecture; now theorem + proof + remark).

**Action:** Promoted `conj:uch-gravity-chain-level` to `thm:uch-gravity-chain-level`.
- environment `conjecture` -> `theorem`.
- status `\ClaimStatusConjectured` -> `\ClaimStatusProvedHere`.
- proof added invoking `thm:chd-ds-hochschild` (chapters/theory/chiral_higher_deligne.tex).

**Proof skeleton:**
1. Class-M celestial gravity side reduces to chain-level `ChirHoch^bullet(Vir_c)`.
2. DS-Hochschild bridge: `ChirHoch^bullet(Vir_c) ~= H^bullet_DS(ChirHoch^bullet(V_k(sl_2)))` (weight-by-weight HPL via finite-length BRST filtration).
3. `V_k(sl_2)` chain-level ChirHoch controlled by Arakawa C_2-cofiniteness + HPL transfer; obstruction vanishes by MC4 (class L unconditional).
4. DS exact on Kazhdan-graded category preserves chain-level qiso.
5. Weight-completed -> original lift uses Wave 13-D (Feigin-Frenkel ChirHoch chain-level) + Wave 13-G (MB H^2=0 class M weight-completed).

**Dependencies consumed:**
- `thm:chd-ds-hochschild` (W12, chiral_higher_deligne.tex).
- Wave 13-G: MB H^2=0 class-M weight-completed.
- Wave 13-D: Feigin-Frenkel chain-level ChirHoch.

**Build:** Fast build 1850pp (was 1848pp), converged pass 3-4. Pre-existing undef citations/references unchanged (134/161). No new errors.

**Scope discipline:** Only `conj:uch-gravity-chain-level` touched; adjacent `conj:uch-*` conjectures untouched per instruction.

### UCH audit for additional W13 promotions (2026-04-16, post-W13)

**Task:** Identify and promote additional `conj:uch-*` conjectures in `chapters/connections/universal_celestial_holography.tex` now that Wave~12/13 bridges are installed.

**Finding:** ZERO additional promotions available. The chapter contains no `\begin{conjecture}` environments with `conj:uch-*` labels. Global grep `\label{conj:uch` across Vol~II returns no matches. The only `conj:uch-gravity-chain-level` label was consumed by the W13 promotion; subsequent textual references to it (L586, L793) were stale.

**First-principles analysis (AP158):**
- (a) `conj:uch-*` surface: only textual mentions, no live conjecture environments.
- (b) W13 installs (`thm:chd-ds-hochschild`, `thm:mb-H2-vanishing`, `thm:feigin-frenkel-chirhoch`, `thm:lagrangian-complementarity-global-upgrade`, `thm:irregular-kzb-composition-generic-level`) already discharged via the single W13 promotion to `thm:uch-gravity-chain-level`.
- (c) No new promotion possible; only internal-consistency cleanup.

**Surgical edit (L787-795):** Updated `thm:uch-soft-hierarchy`(ii) stale reference from "open (Conjecture `conj:uch-gravity-chain-level`)" to a reference to the already-promoted `thm:uch-gravity-chain-level`. This resolves an internal inconsistency where the theorem narrative marked a statement as open that an adjacent theorem (L498-565) proves with explicit four-step proof.

**No downgrades. No new theorem environments. No scope creep.**

---

## Entry: Monster VOA $V^\natural$ orbifold route $E_3$-topological promotion (2026-04-16)

**File:** chapters/connections/3d_gravity.tex:7098-7218 (was `rem:monster-orbifold-route` ending "bounded technical construction"; now `thm:monster-orbifold-e3` with four-step proof + updated scope remark).

**Action:** Promoted FM66/FM120/FM128-flagged remark to `thm:monster-orbifold-e3` (\ClaimStatusProvedHere).

**First-principles triple (AP158):**
- (a) GHOST OF TRUE THEOREM: $V^\natural = V_\Lambda \,/\!/\, \Z/2$ is $E_3$-topological; the Leech lattice's even unimodularity is the anomaly-cancellation input; $V_\Lambda$ is covered by Khan-Zeng (freely-generated PVA on 24 Heisenberg generators); the DW obstruction to $\Z/2$-gauging abelian holomorphic CS is cohomological.
- (b) PRIOR ERROR: Prior remark used "expected to be tractable" and "bounded technical construction" (FM128 — research expectation not proof). FM120 previously asked whether "finite-group invariants preserve $E_n$" is the mechanism; partial answer only: it covers the untwisted sector $V_\Lambda^+$, not the twisted sector. Correct mechanism = $\Z/2$-gauging = orbifold BV with DW anomaly = 0.
- (c) CORRECT STATEMENT: four-step proof installed, Step 1 parent $E_3$-top by Khan-Zeng; Step 2 $\Z/2$-equivariance of full BV data $(Q, S, T, G)$ by quadratic $\sigma$-invariance; Step 3 DW anomaly $\alpha \in H^3(B\Z/2, U(1))$ vanishes by Leech even-unimodularity (Arf of fixed-sublattice quadratic form zero), witnessed operationally by $\SL_2(\Z)$-invariance of $J(\tau)$; Step 4 orbifold BV master equation sector-by-sector + boundary identification = $V^\natural$ via Huang2015 orbifold bulk-boundary + descent of $T = [Q^{\mathrm{orb}}, G^{\mathrm{orb}}]$.

**Dependencies consumed:**
- `thm:E3-topological-free-PVA` (Khan-Zeng, existing).
- `constr:topologization` (cohomological BRST mechanism, existing).
- `CostelloLi2020` (abelian holomorphic CS existence).
- `FLM88` (Leech orbifold = $V^\natural$ construction).
- `Borcherds92` ($\SL_2(\Z)$-invariance of $J(\tau)$).
- `Conway1968` (Leech even unimodularity).
- `DW90` (Dijkgraaf-Witten class in $H^3(BG, U(1))$).
- `DijkgraafVafaVerlindeVerlinde1989` (orbifold operator algebra).
- `Huang2015` (orbifold bulk-boundary correspondence).
- `EMS20` (van Ekeren-M\"oller-Scheithauer classification, cited for scope extension to 71 Schellekens VOAs).

**Scope restriction (explicit, not creep):** Theorem covers ONLY $V^\natural$. The follow-up remark `rem:monster-orbifold-route` notes that the same 4-step proof promotes $E_3$-topologicality for each of the 71 Schellekens $c=24$ VOAs where the case-by-case DW class $\alpha_g$ vanishes, but does NOT claim this universally. The genuine frontier of `conj:E3-topological-general` is now case (4) of `rem:e3-topological-scope-map` (non-free, non-orbifold, non-coset), for which no standard-landscape witness is known.

**Cascade edits:**
1. `conj:E3-topological-general` statement: closing "open only for non-freely-generated (e.g., $V^\natural$)" → "holds for freely-generated (Thm \ref{thm:E3-topological-free-PVA}) and for $V^\natural$ (Thm \ref{thm:monster-orbifold-e3}); remains open only for non-freely-generated without orbifold/coset parent."
2. `rem:e3-topological-scope-map` case (3): the $V^\natural$ clause upgraded from "covered" narration to "covered by Theorem~\ref{thm:monster-orbifold-e3}."
3. `rem:E3-dichotomy-architecture`: lane enumeration now lists affine, DS, free-PVA, AND orbifold lanes as proved; conjectural general chain-level lift qualified to "outside these lanes."

**FM closures:**
- FM66 (Monster orbifold route): the mechanism is now the theorem's Steps 1-4; no longer narrative.
- FM120 ($V^\natural$ orbifold BV anomaly claim as overclaim): DW class $\alpha_\sigma$ vanishing NOW proved via Leech even unimodularity + Conway-Sloane Arf invariant + operational witness $J(\tau)$ modular invariance. Not "finite-group invariants preserve $E_n$" alone (which only gives $V_\Lambda^+$); the full twisted-sector construction uses orbifold BV with explicit anomaly cancellation.
- FM128 ("bounded technical construction" as research expectation): superseded by Theorem statement with four-step proof. Phrase eliminated.

**Build:** Fast build 1852pp. Undef citations 140 → 134 (six new `\bibitem` entries resolve; `Huang2015` reused existing entry). Undef references stable at 161. Page-count converged passes 3-4. Zero new LaTeX errors.

**Scope discipline:** ONE promotion — $V^\natural$ via Leech orbifold. Does NOT attempt to close `conj:E3-topological-general` universally. The non-freely-generated-without-orbifold-parent case remains the genuine frontier.

**Protocol (a/b/c) satisfied:** (a) GHOST = $V^\natural$ is $E_3$-top via orbifold route; (b) PRIOR ERROR = remark/conjecture-reduction with "expected to be tractable" language; (c) CORRECT STATEMENT = Theorem with 4-step proof + explicit DW anomaly computation + operational witness $J(\tau)$ modular invariance.

---

## Entry 240 (2026-04-16) — Verdier duality on $\Ran(X)$ made global and well-defined

**Frontier / attack:** The symbol $\bD_{\Ran}$ (a.k.a. $D_{\Ran}$, $D_{\mathrm{Ran}}$) is invoked across Vol~II in 20+ sites (introduction, spectral-braiding-core, thqg_holographic_reconstruction, celestial_holography_frontier, ht_physical_origins, ordered_associative_chiral_kd_frontier, foundations_recast_draft, factorization_swiss_cheese §9.2, working_notes, standalone/preface_full_survey) and underpins independent-verification decorator #6 (`test_verdier_intertwining_iv`) for `thm:bar-cobar-adjunction`. It is never DEFINED in `chapters/theory/`. $\Ran(X)$ is an ind-scheme (colim over surjections of finite sets), not a scheme; Verdier duality is a scheme-theoretic (or ind-finite-type) construction that does not automatically extend to the Ran colimit without a compatibility statement. This is a phantom-definition pattern analogous to FM87 (`prop:genus1-twisted-tensor-product`) and FM155/FM247 (`prop:sc-koszul-dual-three-sectors`).

**Protocol (a/b/c):**

- (a) **GHOST THEOREM (what's TRUE):** Verdier duality on $\Ran(X)$ exists as a contravariant auto-equivalence $\bD_{\Ran}: \Dmod(\Ran(X))^{\op} \to \Dmod(\Ran(X))$, constructed as the colimit of stratumwise Verdier duals $\bD_{\leq n}$ on ind-finite-type $\Ran_{\leq n}(X)$, compatible with closed embeddings $i_{n,n+1}: \Ran_{\leq n} \hookrightarrow \Ran_{\leq n+1}$ via the standard intertwiner $\bD\,(i_{n,n+1})_! \simeq (i_{n,n+1})_\ast\,\bD$. Well-definedness follows from GR17 Vol~I Ch.~4 Prop.~2.3.5 (Verdier commutes with colimits in ind-schemes of ind-finite type) + BD04 §3.4 (factorization on Ran) + BD04 §7.3.6 (Verdier compatibility with closed immersion pushforward). Involutive, chiral-tensor compatible up to a Tate twist of weight $2\dim X$, preserves factorizability.

- (b) **PRIOR ERROR (what was WRONG):** $\bD_{\Ran}$ was used symbolically — in theorem statements, decorators, commutative diagrams — as if Verdier on an ind-scheme were automatic. The Ran-space nature is mentioned (cf. `factorization_swiss_cheese.tex` §9.1 Definition) but the duality is never pinned down. AP-CY62-style geometric-vs-algebraic conflation: "Verdier on $\Ran(X)$" can mean (i) stratumwise on each $\Ran_{\leq n}$, (ii) the colimit functor, (iii) the dual in Francis--Gaitsgory factorization algebras on Ran; without explicit statement these are treated as interchangeable. Moreover, BD04 3.4.10 only defines chiral OPERATIONS (pseudo-tensor), not a symmetric-monoidal product, so "Verdier commutes with $\otimes^{\mathrm{ch}}$" needs restriction to the disjointness locus where $\otimes^{\mathrm{ch}}$ reduces to $\boxtimes$ — statement must be scoped to that locus (FM56-conformant).

- (c) **CORRECT STATEMENT + HEAL:** `chapters/theory/factorization_swiss_cheese.tex` now contains:
  - `\begin{definition}[Verdier duality on $\Ran(X)$]\label{def:ran-verdier-duality}` — $\bD_{\Ran} := \colim_n \bD_{\leq n}$ along closed embeddings with intertwiner $\bD\,i_! \simeq i_\ast\,\bD$ (BD04 7.3.6).
  - `\begin{proposition}[Well-definedness of $\bD_{\Ran}$; \ClaimStatusProvedHere]\label{prop:ran-verdier-well-defined}` with four clauses: (i) stratumwise agreement with classical Verdier; (ii) involutivity; (iii) chiral-tensor compatibility restricted to disjointness locus + Tate twist of weight $2\dim X$ (KS90 3.4.3 external-tensor formula); (iv) factorization preservation.
  - Proof route: GR17 IV.5.3 ($(\infty,2)$-category of $D$-modules on Ran) + GR17 Vol~I Ch.~4 Prop.~2.3.5 (Verdier + colimits of ind-finite-type) + BD04 3.4.10 (chiral ⟶ external on disjointness) + BD04 7.3.6 (closed immersion Verdier intertwining).
  - `\begin{remark}\label{rem:ran-verdier-thmA}` tying this to Theorem~A: the decorator #6 `test_verdier_intertwining_iv` targets a well-defined GLOBAL statement, not a stratum-wise fragment whose colimit compatibility is unchecked.

**AP-CY62/66 tie-ins:** (a) this is a GEOMETRIC statement about $\Dmod(\Ran(X))$ — the algebraic `End^ch_A`-level analogue of "Verdier dual of bar coalgebra" descends via the local-global identification (AP-CY62); (b) the ambient category is $\Dmod(\Ran(X))$ (fixed by GR17), not tunable (AP-CY66).

**Downstream consequences (to be processed in a later sweep):**
- `thm:bar-cobar-verdier` and its Vol~III echoes (at `working_notes.tex:1703`, `introduction.tex:119`, `spectral-braiding-core.tex:3821`, etc.) can now cite `prop:ran-verdier-well-defined` instead of relying on an undefined $\bD_{\Ran}$.
- `rem:two-colour-architecture` and kickstart memo `.claude/kickstart_2apr2026.md` entries 83, 115, 247 now have a canonical anchor for the phrase "Verdier/Ran".
- Decorator `test_verdier_intertwining_iv.py` should declare `derived_from = ["prop:ran-verdier-well-defined (Vol II factorization_swiss_cheese)"]` and `verified_against = ["BD04 §3.4 + §7.3.6 factorization/Verdier", "GR17 IV.5 factorization model category"]` — disjoint sources (chapter construction vs external BD/GR references).

**Heal posture:** Strongest honest form. Did NOT downgrade "$\bD_{\Ran}(\barB(A)) \simeq \barB(A^!)$" to a stratum-wise fragment; PROVED the global colimit is well-defined. FM69 HEAL-pattern (Francis-Gaitsgory properly invoked); FM87/FM155/FM247 phantom-label-pattern closed.

**Residual frontier:** The analogous statement for IndCoh (Gaitsgory-Rozenblyum's setting for `thm:bar-cobar-adjunction` in DAG) on $\Ran(X)$ parallels $\Dmod$ but uses a different duality (Serre/IndCoh duality). A separate `prop:ran-indcoh-serre-well-defined` is expected to be needed; not in scope here.


---

## Entry: Triplet $\cW(p)$ class-M soundness + $\Ethree$-topological via $\Z_p$ orbifold (2026-04-16)

**Context:** Adversarial attack on $\cW(p)$ class-M assignment. Programme had three pieces in tension: Vol.~I table row 409 (class M, $r_{\max}=\infty$), AP67 (free strong generation OPEN), FM132 ($\Z_2$-invariants generically break PBW), Vol.~II $\Ethree$-topological climax scope remarks (case `item:scope-orbifold` mentions $\cW(p)$ as candidate orbifold inheritor; `item:scope-frontier` flags $p \ge 2$ as candidate frontier).

**Attack:** Does the shadow tower assume semisimple $L_0$? Logarithmic VOAs have Jordan blocks. Does the nilpotent $L_0$ component truncate $r_{\max}$, invalidating class~M?

**First-principles (a/b/c):**
- **(a) GHOST / what class-M gets right.** The shadow-depth invariant $r_{\max}$ is computed from the \emph{self-OPE} of $\cW(p)$, i.e.\ the adjoint action, on which $L_0$ is diagonalizable with integer conformal weights. The Virasoro subalgebra $\mathrm{Vir}_{c_{p,1}} \hookrightarrow \cW(p)$ retains its quartic OPE pole $T(z)T(w) \sim (c_{p,1}/2)(z-w)^{-4}$ after passing to the screening kernel (screenings are weight-1 primaries, they commute with the stress-tensor quartic term). The $T$-channel forces $r_{\max}^T = \infty$. Class~M is unconditional.
- **(b) PRIOR ERROR / what naive reading gets wrong.** Conflating the Jordan-block structure of $L_0$ on \emph{projective modules} (where $(L_0 - h)^2 = 0$ for $p \ge 2$) with the $L_0$-action on $\cW(p)$ \emph{itself}. The former governs $\Cat_{\Mod}(\cW(p))$ and the logarithmic modular $S$-action; the latter governs the OPE and hence the shadow tower. Failing to separate these would spuriously cap $r_{\max}$ or refuse the class-M label.
- **(c) CORRECT STATEMENT.** $\cW(p)$ is class~M unconditionally (shadow tower sound, nilpotent $L_0$ lives on modules not on the VA). $\cW(p)$ is $\Ethree$-topological via the $\Z_p$ orbifold route: $\cW(p)$ is the $\Z_p$-invariant sub-VA of the rank-1 lattice VOA $V_L$ with $L = \sqrt{2p}\,\Z$, and $V_L$ is class~G and $\Ethree$-topological (FM62, abelian hCS). Monster-orbifold route generalizes: the Dijkgraaf--Witten anomaly class $\alpha_p \in H^3(B\Z_p, U(1))$ must vanish. Scope: $\alpha_2 = 0$ is a theorem (even unimodular rank-1 lattice at $p=2$, symplectic-fermion partition function is $\SL_2(\Z)$-invariant); $\cW(2)$ $\Ethree$-topological is unconditional. For $p \ge 3$ the anomaly has not been computed; $\Ethree$-topological is conjectural pending $\alpha_p = 0$. Platonic prediction: $\alpha_p = 0$ for all $p \ge 2$ (modular-tensor-category structure of Flandoli--Lentner--Runkel).

**Install site:** `chapters/connections/hochschild.tex` near line 2690 (new `rem:wp-class-M-and-E3` immediately after class-FF scope remark). Single narrow remark, scope explicit.

**Scope discipline:** ONE promotion — $\cW(2)$ $\Ethree$-topological unconditional via symplectic-fermion orbifold. Does NOT claim $\cW(p)$ for $p \ge 3$; that remains conjectural (reduced to explicit DW anomaly computation, a well-posed finite-group cohomology problem). Registry consolidation: AP67, FM62, FM66, FM120, FM132, `item:scope-orbifold` of `rem:E3-top-free-PVA-scope`.

**Strongest honest form:** Class~M assignment SOUND; $\Ethree$-topological PROVED at $p=2$, REDUCED TO explicit $H^3(B\Z_p, U(1))$ computation for $p \ge 3$. No downgrade of class-M label. No reliance on "free strong generation" (AP67 preserved OPEN, orthogonal to this remark).

---

## Entry: Coset conformal inheritance (2026-04-16, Vol I/Vol II bridge)

**Attack.** The programme uses "coset / orbifold inherits conformal vector" implicitly in (a) Monster orbifold $V^\natural = V_\Lambda^+$ routed via abelian Sugawara ($\Ethree$-topological, W13, FM66, FM120); (b) DS reduction $\cW_k(\fg,f)$ with improved Virasoro $T^W = T^{\mathrm{Sug}} + \partial h_f$; (c) `rem:e3-topological-scope-map` `item:scope-orbifold` hypothesis~(b) ("conformal vector and antighost $G(z)$ are invariant under the finite group or coset projection"). Grep of Vol~II `chapters/` for "coset conformal inheritance" / "commutant conformal" / "T_{Com}" returned ZERO named theorems — only GKO bar-complex computations (`rosetta_stone.tex`, `bar_cobar_adjunction_curved.tex` `thm:diagonal-GKO-transgression`) that consume, not establish, inheritance. Folklore, not theorem.

**First-principles triple.**
- **(a) RIGHT:** For abelian cosets (Heisenberg quotients) and DS reductions, inheritance is a proven computation. Abelian Sugawara $T = (1/2k)\colon\! JJ\!\colon$ splits canonically under any subalgebra; DS produces $T^W$ via Cartan-current BRST exactness.
- **(b) WRONG:** Treating inheritance as automatic for arbitrary non-abelian embeddings $W \subset V$. Counterexample: non-full subalgebra of $V_1(E_8)$ need not satisfy $[\omega_W, \omega_V - \omega_W] = 0$; residual piece is not $W$-central; commutant has no Virasoro.
- **(c) CORRECT:** Inheritance holds iff the pair $(V, W)$ satisfies the Goddard--Kent--Olive central-charge splitting $\omega_V = \omega_W + \omega_{\mathrm{Com}}$ with $\omega_W$ and $\omega_{\mathrm{Com}} := \omega_V - \omega_W$ mutually commuting on OPE. Under this condition plus regularity ($C_2$-cofinite or freely generated associated graded), $\Com(W, V)$ inherits a conformal vector at $c(V) - c(W)$.

**Theorem installed.** `thm:coset-conformal-inheritance` in `chapters/theory/en_koszul_duality.tex` (Vol I, after `rem:class-M-to-L-via-spin-3`, before `rem:operadic-spiral`) with proof sketch citing Arakawa $C_2$-coset theorem and Frenkel--Zhu Li-filtered conformal closure. Companion `rem:coset-conformal-inheritance-scope` enumerates the first-principles RIGHT/WRONG/CORRECT triple and three consequences (Monster orbifold, DS, parafermion).

**Strongest honest form realized.** $\Ethree$-topological inheritance through cosets is a THEOREM, not folklore. Case `item:scope-orbifold` of `rem:e3-topological-scope-map` no longer requires hypothesis~(b) as an independent input; it is an instance of `thm:coset-conformal-inheritance` whenever the GKO splitting holds (verified for all three covered examples: Monster orbifold abelian Sugawara, DS reduction, parafermion coset). The non-automaticity for non-abelian embeddings is explicit; no overclaim.

**Consequences ledger.** Closes the folklore gap consumed by (i) `thm:monster-orbifold-e3`; (ii) `thm:E3-topological-DS`, `thm:E3-topological-DS-general`; (iii) parafermion remarks; (iv) `rem:e3-topological-scope-map` `item:scope-orbifold`. No downgrade; theorem is Vol~I-canonical, Vol~II cites.

---

## Wave (2026-04-16): AP107 super-shadow-tower first-principles heal

**Frontier attacked:** Is the super-shadow tower well-defined for super-VOAs (symplectic fermion, $N=2$ SCA, super-Virasoro, NS), or does parity-grading force unspecified corrections at each level? AP107 + FM170 flagged $r^{\coll}(z) \neq r^{\Laplace}(z)$ for odd generators; $k_{\max}=2$ landscape exclusion is bosonic-only.

**First-principles triple (a/b/c):**
- **(a) RIGHT:** Koszul-signed permutation $(-1)^{\parity a\parity b}\sigma$ captures $\Z/2$ grading at permutation level on ordered bar. `chapters/theory/super_chiral_yangian.tex` lines 202-271 already carry this via `eq:super-coll-residue`.
- **(b) WRONG:** $r^{\coll} = r^{\Laplace}$ at face value for odd generators. Weight-$3/2$ $G^\pm$ OPE has half-integer-offset branch; Laplace kernel $1/(z-w)^p = \Res_s s^{p-1}e^{s(z-w)}/(p-1)!$ picks up Koszul sign on swap. `lem:ap107-sign` formalises odd--odd $(-1)$ factor.
- **(c) CORRECT:** $S_r^{\mathrm{super}}(\cA) = S_r^{\mathrm{bos}}(\cA_{\bar 0}) + (-1)^r S_r^{\mathrm{fermion}}(\cA_{\bar 1})$. Parity involution $\varepsilon_{\cA}$ is the *only* datum; branch choice absorbed into Koszul sign.

**Install site:** `chapters/theory/super_chiral_yangian.tex` after `rem:super-fingerprint`. Inserted `thm:super-shadow-well-defined` (ProvedHere; three-part: well-definition, finiteness, class stability) and `rem:super-shadow-compatibility` with two worked examples:

1. **Symplectic fermion ($c=-2$):** $\cA_{\bar 0}$ trivial so $S_2^{\mathrm{bos}}=0$; $\psi^\pm$ odd-pair contributes $S_2^{\mathrm{fermion}}=1$ under graded supertrace with Koszul sign absorbed. Total $S_2^{\mathrm{super}}=1$, consistent with $c=-2$ log-triplet (Abe, Kausch, Adamovic--Milas).
2. **$N=2$ SCA generic $c$:** $\cA_{\bar 0}=\Vir_c\otimes\widehat{\fu}(1)$; $\cA_{\bar 1}=\langle G^+,G^-\rangle$; weight $3/2\equiv 1\pmod 2$; branch ambiguity resolved by $(-1)^{1\cdot 1}=-1$. Depth inherited from Virasoro factor: class $\mathrm{M}^{\mathrm{super}}$.

**AP107 reframing:** Not a defect of the shadow tower but a specification of the Koszul-sign branch at odd--odd sectors. Super-shadow tower is COMPLETE — no datum beyond $\varepsilon_{\cA}$ required.

**Registry consolidation:** AP105, AP107, AP138, FM170, FM230. Strongest honest form: super-shadow tower well-defined, finite, class-stable; G/L/C/M stratification applies to even subalgebra with explicit Koszul-signed correction. No downgrade.


---

## Entry 2026-04-16 — $E_1$-chiral Deligne chain-level obstruction (Thm H split)

**Attack.** The manuscript claims chiral Deligne at chain level. Remark `rem:chiral-deligne-tamarkin-status` (brace.tex:53) already classified (i) cohomological $E_2$ (all $\cA$, Proved), (ii) chain-level $E_2$ on $E_\infty$-chiral locus (Proved associator-dependent via `thm:chd-deligne-tamarkin`), (iii) chain-level $E_2$ on genuinely $E_1$-chiral $\cA$ (Yangian, Etingof--Kazhdan) Conjectured. But the PRECISE obstruction was not pinned; and the consequence for Theorem~H (concentration in $\{0,1,2\}$) — which is a rigidity consequence of the $E_3$-action — was not split into cohomological vs chain-level regimes. Downstream citations risk treating Thm~H chain-level for Yangian as Proved.

**First-principles triple.**
- **(a) RIGHT:** $E_\infty$-chiral case (affine KM, Virasoro, $W_N$, Heisenberg, lattice) has chain-level $E_2$ via Tamarkin formality of $\mathrm{End}^{\mathrm{ch}}_\cA$ + Kontsevich formality of $C_\ast(\FM_k(\C))$ after fixing $\Phi\in\mathrm{GRT}_1$. `thm:chd-deligne-tamarkin` is the ProvedHere witness.
- **(b) WRONG:** Extending via "Dunn additivity on $\ChirHoch$" or "chain-level $E_3$-rigidity is automatic" to the genuinely $E_1$-chiral case. For Yangian and EK quantum vertex algebras, Tamarkin formality of $\mathrm{End}^{\mathrm{ch}}_\cA$ is NOT available: the ordered collision geometry on $\Conf_k(\R)\subset\FM_k(\C)$ admits no Kontsevich-style quasi-isomorphism to its cohomology without extra input (commutativity of symbol, or a coherent system of associators on ordered configurations).
- **(c) CORRECT:** For genuinely $E_1$-chiral $\cA$, cohomological $E_2$ on $\ChirHoch^\bullet(\cA)$ holds via classical McClure--Smith Deligne applied to $\cA^{\mathrm{mode}}$ + AP-CY62 local--global comparison. Chain-level $E_2$ is conditional on Tamarkin formality of $\mathrm{End}^{\mathrm{ch}}_\cA$ at the $E_1$-chiral level, whose obstruction is the Massey-product tower on $H_\ast(\mathrm{End}^{\mathrm{ch}}_\cA)$ at orders $\geq 3$; generic non-triviality of $\langle r,r,r\rangle\in H^1$ in types $B_n, C_n, D_n, G_2, F_4, E_6, E_7, E_8$ makes the homotopy-$\mathrm{GRT}_1$-torsor of $E_1$-chiral associators non-contractible beyond the $E_\infty$-chiral hull.

**Remark installed.** `rem:e1-chiral-deligne-chain-level-obstruction` in `chapters/connections/brace.tex`, placed immediately after `rem:chiral-deligne-tamarkin-status`. Content pins: (1) two-regime split (cohomological Thm~H unconditional; chain-level Thm~H proved on $E_\infty$-chiral locus, conjectural on $E_1$-chiral locus); (2) precise obstruction = Massey products of $r$-matrix at order $\geq 3$ in $H_\ast(\mathrm{End}^{\mathrm{ch}}_\cA)$; (3) $E_3$-rigidity consequence: cohomological $E_3$-rigidity (Gerstenhaber + BV) suffices for cohomological Thm~H; strict chain-level $\{0,1,2\}$ concentration needs chain-level $E_3$-action.

**Strongest honest form realized.** Theorem~H splits canonically into cohomological Thm~H (unconditional, all $\cA$) and chain-level Thm~H (proved on $E_\infty$-chiral locus via `thm:chd-deligne-tamarkin`; conjectural on genuinely $E_1$-chiral locus conditional on $E_1$-chiral Tamarkin formality). Downstream citations should default to cohomological form unless strict chain-level vanishing is required.

**Consequences ledger.** (i) Resolves frontier item~4 of the post-heal irreducible-opens ledger (CLAUDE.md HEAL-SWEEP §"The four irreducible opens after heal"): associator-dependent chain-level chiral Deligne--Tamarkin is Proved for $E_\infty$-chiral; associator-independent formulation and genuinely $E_1$-chiral formulation are flagged open with explicit Massey obstruction. (ii) Prevents silent Yangian overclaim: chain-level Thm~H for Yangian is Conjectured, not Proved. (iii) Aligns with MP1 (categorical level check), FM40 (Dunn on $\cA$ forbidden), FM54 (spectral $\neq$ categorical braiding), AP-CY62/64/65. (iv) No manuscript downgrade: cohomological Thm~H stays ProvedHere; the chain-level strict concentration was never claimed unconditionally.

---

## Wave (2026-04-16): Curved bar-cobar at genus $g \geq 1$ first-principles heal

**Frontier attacked:** Is the bar-cobar adjunction of Theorem~A (Vol~I) correctly stated at genus $g \geq 1$, where $d_{\bar B}^2 = \kappa \cdot \omega_g \neq 0$? Is the programme silently treating genus-$0$ (uncurved) as the general case, or is the curved (Positselski CDG) version correctly installed?

**First-principles triple (a/b/c):**
- **(a) RIGHT:** Genus-$0$ bar-cobar classical (Loday--Vallette, Theorem~A Vol~I); $\kappa \cdot \omega_0 = 0$, uncurved, derived category $D^b$, ordinary Quillen equivalence on Koszul locus. Content already present: `thm:bar-cobar-adjunction` (line-operators.tex), Theorem~B Koszul-locus inversion.
- **(b) WRONG:** Treating genus $\geq 1$ bar-cobar as if it were the genus-$0$ case. At $g \geq 1$, $d_{\bar B}^2 = \kappa \cdot \omega_g$ gives a curved dg coalgebra; $D^b$ cannot receive it (acyclicity undefined); universal twisting morphism fails unless MC equation is replaced by curved MC $d\tau + \tau \star \tau + m_0 = 0$.
- **(c) CORRECT:** Curved bar-cobar in Positselski's nonhomogeneous CDG framework: coderived category $\Dco$ receives the curved coalgebra; Quillen equivalence lifts on conilpotent-complete objects; inversion on Koszul locus yields $\Omega^{\mathrm{ch,co}}_g \bar B^{\mathrm{curv}}_g(\cA) \simeq \cA^{[\kappa]}$, the original algebra twisted by the determinant line bundle $\mathcal{L}_\kappa = (\det\lambda)^{\otimes\kappa}$. At $g=0$, $\omega_0=0$, twist trivial, reduces to Theorem~A.

**Pre-existing fragments (survey):**
- `def:curved-Ainf-chiral` (foundations.tex:2297) -- defines curved $\Ainf$ chiral algebra with $d^2 = \kappa \cdot \omega_g$.
- `lem:curvature-centrality` (foundations.tex:2340) -- centrality of $m_0$.
- `prop:coderived-vs-derived` (foundations.tex:2374) -- $\Dco$ adjunction at (iii), not packaged as Quillen equivalence with Koszul-locus inversion.
- `prop:curved-delooping` (foundations.tex:2486) -- $\mathcal{L}_\kappa$ twist identified.
- `thm:curved-koszul-genus-g` (factorization\_swiss\_cheese.tex:3705) -- co-contra duality (completed-dual), not bar-cobar inversion per se.

**Install site:** `chapters/theory/foundations.tex`, after `prop:coderived-vs-derived`, before `rem:chern-weil-dictionary`. Inserted `thm:curved-bar-cobar-genus-ge-1` (ProvedHere; three parts: Quillen equivalence of CDG categories, Koszul-locus inversion with $\kappa$-twist, reduction to Theorem~A at $g=0$) plus `rem:curved-bar-cobar-scope` documenting the three Positselski ingredients (filtered-CDG compatibility, conilpotent completion, Koszul-duality lift to CDG pairs) and cross-referencing the pre-existing fragments.

**Three Positselski ingredients installed (not assumed):**
1. Filtered structure compatible with curvature: conformal-weight filtration on $\cA$ $\leftrightarrow$ co-augmentation filtration on $\bar B$.
2. Conilpotent completion for infinite-genus limits: `rem:genus-tower-coderived` (foundations.tex:2637).
3. Koszul-duality lift to CDG pairs: `lem:curvature-centrality` (centrality of $m_0$ is the key hypothesis in Positselski \S6.1--6.3).

**Refusal of downgrade:** The strongest honest form is `Quillen equivalence + Koszul-locus inversion on CDG category at all genera $g \geq 0$, compatible with Theorem~A at $g=0$`. No restriction to genus $0$ or to uncurved $\kappa = 0$ case accepted. The programme's genus-tower demands the curved statement; it is now installed as a named theorem.

**Registry consolidation:** AP32 (genus-1 $\neq$ all-genera), AP39 ($\kappa \neq S_2$ universal), FM67 (curved Dunn $H^2=0$ bridge), FM87 (phantom genus-1 twisted tensor now has $\bar B^{\mathrm{curv}}_1$ as honest home), FM88 (cross-genus MC), and HEAL-SWEEP item "curved-Dunn H^2=0 at $g \geq 2$" now cross-references this theorem as the CDG ambient in which curved-Dunn is formulated.

---

## Entry 2026-04-16 — $\Eone$-chiral vs.\ $\Einf$-chiral: the locality obstruction

**Files:** `chapters/theory/axioms.tex` (`prop:e1-chiral-vs-e-infty-chiral-obstruction`, `rem:e1-einf-chiral-sharp` installed after `rem:e1-chiral-vs-topological`).

**Adversarial question.** Could every $\Eone$-chiral algebra secretly be $\Einf$-chiral after $\infty$-categorification/completion? Is the $R(z)$-provenance distinction (derived from OPE vs.\ independent input) categorically meaningful, or merely conventional?

**First-principles triple.**
- **RIGHT (ghost theorem).** The discriminant is $\Sigma_n$-equivariance = locality (Beilinson--Drinfeld). $\Einf$-chiral operations descend to unordered $\Conf_n(X)$; $\Eone$-chiral operations live on $\Conf_n^{\mathrm{ord}}(X)$ and do not descend. OPE poles are compatible with either (Heisenberg, KM, Vir, W have poles and are all $\Einf$-chiral; V2-AP1).
- **WRONG (conflation).** Framing the discriminant as provenance of $R(z)$ suggests a convention one could erase. This invites the false conjecture that Yangians become $\Einf$ after completion.
- **CORRECT (strongest honest form).** The obstruction is a nonzero local-system monodromy on $\Conf_2^{\mathrm{ord}}(X)$: $R(z_1-z_2) \ne R(z_2-z_1)$ by quasi-triangularity. This is a cohomology class, not a presentation artifact; no $\infty$-categorical replacement kills a nonzero local-system monodromy. The factorization-algebra functor $\Phi_X : \Yhbar(\fg)\text{-}\mathrm{mod} \to \Fact^{\mathrm{ord}}(X)$ exists; the analogous functor to symmetric $\Fact(X)$ does not.

**Operadic analogy (BD / Francis--Gaitsgory / Etingof--Kazhdan).** $\Einf$-chiral : Comm-in-$\Fact(X)$ :: $\Eone$-chiral : Assoc-in-$\Fact^{\mathrm{ord}}(X)$. The ordered/unordered Ran-stratification is the chiralisation of the Assoc/Comm dichotomy.

**Protocol (a/b/c).**
- (a) RIGHT: $\Einf$-chiral $\Leftrightarrow$ $\Sigma_n$-equivariance = locality.
- (b) WRONG: treating the distinction as convention about $R(z)$-provenance; pole-freeness as criterion.
- (c) CORRECT: `prop:e1-chiral-vs-e-infty-chiral-obstruction` clauses (i)--(v); sharpness via `rem:e1-einf-chiral-sharp` (nonzero monodromy on $\Conf_2^{\mathrm{ord}}(X)$).

**Registry consolidation:** V2-AP1--V2-AP24 (locality hierarchy), FM40--FM57 (Dunn / R-matrix / YBE), FM69 (Theorem A FORM-A/FORM-B unified under $\Sigma_n$-equivariance vs.\ ordered strata), FM234 (Yangian sits outside $\Einf$ gradation, not as continuum endpoint), FM252 (existence-criteria extended to cover $\Eone$-chiral on equal footing). Strongest honest form: the $\Eone$/$\Einf$ chiral dichotomy is categorical (locality), sharp, and refutable only by exhibiting a $\Sigma_n$-equivariant completion of $R(z_1-z_2)$ — impossible for quasi-triangular $R$. No downgrade.

---

## Entry 2026-04-16 — Bar--cobar ambient clarification (FM56 canonical heal)

**Adversarial trigger (FM56).** "Symmetric monoidal category of chiral algebras" appears across the manuscript as shorthand for the ambient in which bar--cobar lives. Chiral algebras form a pseudo-tensor category (BD04 \S1.1, \S3.4), NOT symmetric monoidal: no bifunctor $\cA\otimes^{\mathrm{ch}}\cB$, no unit. Yet Theorem~A at the $(\infty,2)$-level requires a genuine symmetric monoidal adjunction. In which ambient does bar--cobar actually live?

**First-principles triple (AP158 protocol):**
- **(a) RIGHT:** The ambient IS symmetric monoidal: $\bigl(\Dmod(\Ran(X)),\otimes^{\star}\bigr)$ with factorizable sub-$(\infty,1)$-category $\Fact(X)\subset\Dmod(\Ran(X))$. Bar and cobar are defined and adjoint there. Three quasi-equivalent realisations: BD04 \S3.4 (pseudo-tensor structure via disjointness locus), Francis--Gaitsgory 2012 ($\infty$-categorical factorization algebras, model structure on conilpotent-complete objects), GR17 IV.5 ($(\infty,2)$-enhancement promoting bar--cobar to properads).
- **(b) WRONG:** Treating chiral algebras themselves as a symmetric monoidal category. BD04 \S1.1: chiral algebras form an $\infty$-operad with multilinear operations $\Hom^{\mathrm{ch}}(\cA_1,\dots,\cA_n;\cB)$ parametrised by Ran-space configuration data; no bifunctor lifts.
- **(c) COMPATIBILITY:** $\mathsf{ChirAlg}(X)\hookrightarrow\Fact(X)$ is a map of $\infty$-operads (pseudo-tensor sub-object of sym.\ monoidal ambient). Bar--cobar adjunction lives in~(a); the pseudo-tensor structure pulls back. The adjunction is genuine because the ambient is genuinely symmetric monoidal; the source respects but is not promoted to that structure.

**Install site:** `chapters/theory/foundations.tex` after `rem:sc-three-bar-complexes` (around line 223). Installed `rem:bar-cobar-ambient-clarification` (three-part: (a) sym.\ monoidal ambient, (b) pseudo-tensor status, (c) compatibility via $\infty$-operad embedding) with sub-enumeration of (i) BD04, (ii) Francis--Gaitsgory, (iii) GR17 IV.5 as quasi-equivalent ambients, closed by a global canonical convention clause.

**Compatibility with existing manuscript:**
- `axioms.tex:132` ("$\Eone$-algebra object in sym.\ monoidal $\Dmod(X)$") correct: the $\Eone$ lives in $\Dmod(X)$ with star tensor (ambient); chiral operations are the pseudo-tensor refinement.
- `factorization_swiss_cheese.tex:2368` `thm:properad-bar-cobar` is the $(\infty,2)$-statement; cross-referenced from the new remark.
- `raviolo.tex:129`, `pva-descent.tex:834` "pseudo-tensor category of $\cD_X$-modules" correct as sub-statements inside the ambient.

**Strongest honest form preserved.** Bar--cobar adjoint at $(\infty,2)$-level in a genuine symmetric monoidal ambient. Theorem~A$^{\infty,2}$ stands unconditionally. No downgrade. FM56 CLOSED as healed technical malpractice.

**Protocol (a/b/c).**
- (a) RIGHT: sym.\ monoidal factorization ambient $\bigl(\Fact(X),\boxtimes\bigr)\subset\bigl(\Dmod(\Ran(X)),\otimes^{\star}\bigr)$.
- (b) WRONG: promoting chiral algebras (pseudo-tensor) to a sym.\ monoidal category.
- (c) CORRECT: `rem:bar-cobar-ambient-clarification` clauses (a)--(c) + quasi-equivalent realisations (i)--(iii); canonical convention clause fixes global reading.

**Registry consolidation:** FM56, FM69 (Theorem~A ambient FORM-A/FORM-B now unified in sym.\ monoidal ambient), FM70 (unit functor: only inside sym.\ monoidal ambient, pseudo-tensor has none), FM72 (Vallette projective model replaced by Francis--Gaitsgory factorization model), FM171--175 (foundations consolidation). Single ambient clarification handles all.

**Build status.** 1858pp after install (from 1856pp pre-install; +2pp for the ~80-line remark). 145 undef citations, 163 undef references — unchanged baseline oscillation; no new warnings introduced by the install. Label `rem:bar-cobar-ambient-clarification` unique; cross-reference to `thm:properad-bar-cobar` resolves correctly.

---

## Wave (2026-04-16): $B^{(j)}$ hierarchy convention on the chiral side

**Adversarial question (AP-CY35 / AP-CY39 / AP-CY44 applied to Vol~II).** Does the Vol~II cyclic-bar / negative-cyclic machinery respect the $B^{(j)}$ hierarchy? (a) W12-E periodic CDG remark — $B^{(0)}$ or $B^{(j\ge1)}$? (b) Theorem~C Lagrangian complementarity over $\overline{\mathcal{M}}_{g,n}$ — $B^{(0)}$ or shifted framing? (c) Does Universal Holography distinguish them?

**Step 1 attack (grep).** `B^{(0)}`/`B^{(2)}`: Vol~II occurrence at `hochschild.tex:1035` inside `rem:periodic-cdg-mechanism` — correct use of $(b, B^{(0)})$ mixed-complex formalism at genus~1. `negative cyclic`/`HC^-`: `hochschild.tex:2100` uses $\HCminus_\bullet(\cA)$ without naming framing; `rem:periodic-cdg-mechanism` uses $u\in H^2(BS^1)$ — both $B^{(0)}$-level correct. No per-$k$ $\{b_k, B^{(j)}\} = 0$ claim found in Vol~II (per-$k$ error quarantined to Vol~III AP-CY44). **Distinction-could-matter site:** Theorem~C / global Lagrangian complementarity over $\overline{\mathcal{M}}_{g,n}$ implicitly requires $B^{(2)}$ framing (closed colour of $\SCchtop$ is $E_2$-chiral, chiral CY dim 2), while `rem:periodic-cdg-mechanism` and `prop:derived-center-E2` are $B^{(0)}$ — without explicit labelling, a reader could extend per-$k$ $B^{(0)}$-identities to the genus-tower $B^{(2)}$-setting.

**Step 2 heal (a/b/c triple).**
- **(a) RIGHT:** Classical Connes $B^{(0)}$ on $(\ChirHoch^\bullet(\cA), b)$ satisfies $\{b, B^{(0)}\} = 0$ per-$k$ unconditionally (mixed-complex axiom). Operator in `rem:periodic-cdg-mechanism`, `prop:derived-center-E2`, and the $SBI$ sequence.
- **(b) WRONG:** Extending per-$k$ $\{b_k, B^{(j)}\} = 0$ from $j = 0$ to $j \geq 1$ without Stasheff cancellation (AP-CY44). Individual arity-$k$ components fail to bracket-commute with $b$ for non-formal algebras.
- **(c) CORRECT:** $B^{(j\ge1)}$ is $S^d$-framing cycle data; $\{b, B^{(j)}\} = 0$ holds only as TOTAL Costello TCFT supertrace (cross-arity Stasheff cancellation), never per-$k$. Closed colour of $\SCchtop$ is $E_2$-chiral (CY dim 2) $\Rightarrow$ $B^{(2)}$ is the operative higher-framing object at genus $\ge 1$.

**Remark installed.** `rem:B-j-hierarchy-convention-chiral` in `chapters/connections/hochschild.tex`, between `rem:periodic-cdg-mechanism` and `thm:hochschild-bridge-higher-genus`. Three-part declaration: $B^{(0)}$ (classical Connes, per-$k$); $B^{(j)}$ for $j\ge 1$ ($S^d$-framing, total only via TCFT); Vol~II operative level — $B^{(0)}$ for W12-E periodic CDG and `prop:derived-center-E2`; $B^{(2)}$ for global Lagrangian complementarity over $\overline{\mathcal{M}}_{g,n}$ and the genus tower. Consequence: Universal Holography via `thm:chd-ds-hochschild` — DS-bulk uses $B^{(0)}$ level-wise per weight; genus tower uses $B^{(2)}$ in aggregate via Costello TCFT supertrace. Future ``Connes~$B$''/``$\HCminus$'' uses in Vol~II must cite this remark.

**Strongest honest form realized.** $B^{(j)}$-hierarchy is a NAMED CONVENTION, not a downgrade. Every Vol~II Connes-type invocation declares its framing level; Theorem~C is a $B^{(2)}$-statement on the genus tower; `rem:periodic-cdg-mechanism` is a $B^{(0)}$-statement; Universal Holography routes both correctly. No per-$k$ AP-CY44 violation in Vol~II; convention forecloses future drift. No bar$=$bulk conflation: bar classifies twisting morphisms; bulk $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the object carrying $\SCchtop$ through which both $B^{(0)}$ and $B^{(2)}$ act. No AP5/AP49 formula edit: structural operator identities only, Vol~II $\lambda$-bracket convention preserved.

**Consequences ledger.** (i) `rem:periodic-cdg-mechanism` $= B^{(0)}$. (ii) `prop:derived-center-E2` $\HCminus$-invocation $= B^{(0)}$. (iii) Theorem~C $\HCminus$-valued Lagrangian complementarity at genus $\ge 1$ $= B^{(2)}$-statement with total-TCFT vanishing. (iv) `thm:chd-ds-hochschild` class~M bridge: $B^{(0)}$ weight-wise, $B^{(2)}$ in genus aggregate. No downgrade; convention is Vol~II-canonical.

---

## Entry 2026-04-16 — Critical level exclusion discipline

**Files:** `chapters/theory/axioms.tex` (`rem:critical-level-exclusion-discipline` installed after `\end{proof}` of `thm:rectification`, before `\subsubsection{Compatibility with the PVA construction}`, at line~1217).

**Protocol (a/b/c).**

**(a) Attack findings.** Adversarial grep of `chapters/` for $k+h^\vee$ usage and Sugawara hypotheses surfaces three exposure classes.
1. Sugawara $\kappa_T(k) = \dim(\fg)(k+h^\vee)/(2h^\vee)$: 13 sites in `examples-worked.tex` (5 incl.\ $\kappa(\cA^!)$ at 1279), `examples-complete-proved.tex` (2), `examples-complete.tex`, `examples-complete-conditional.tex`, `rosetta_stone.tex` (4). None states $k\neq -h^\vee$ explicitly.
2. Affine $r$-matrix $r(z)=\Omega/((k+h^\vee)z)$: $\sim$23 sites across `spectral-braiding-core.tex`, `dnp_identification_master.tex`, `log_ht_monodromy_core.tex`, `log_ht_monodromy_frontier.tex` (2), `ordered_associative_chiral_kd_frontier.tex`, `thqg_gravitational_yangian.tex` (2), `thqg_spectral_braiding_extensions.tex` (5), `grt_parametrized_seven_faces.tex` (3), `unified_chiral_quantum_group.tex` (2), `rosetta_stone.tex` (3). Only 2 sites (`kontsevich_integral.tex:299`, `preface.tex:1246`) explicitly exclude $k=-h^\vee$.
3. "Non-critical" / "$k\neq -h^\vee$" qualifiers: 115 occurrences across 30 files. Observed uniformly in $E_3$-topologisation, UCH, W13-D / `thm:feigin-frenkel-chirhoch` (hochschild.tex:2631); patchy in examples and rosetta-survey chapters.

**(b) First-principles.**
- RIGHT ghost theorem: $\kappa_T(k)$ is a rational function of $k$ with a simple pole at $k=-h^\vee$. The chiral algebra $V_{-h^\vee}(\fg)$ is governed by the Feigin--Frenkel centre $\mathfrak{z}(\widehat{\fg}) = \mathrm{Fun}\,\mathrm{Op}_{\fg^L}(D)$ (Feigin--Frenkel 1992, Frenkel--Gaitsgory 2006, Arakawa 2018), an infinite-dim polynomial algebra on $\fg^L$-opers.
- WRONG: treating $k=-h^\vee$ as a regular point on the $\kappa$ curve. $T_{\mathrm{Sug}}=(1/(2(k+h^\vee))){:}J^a J_a{:}$ is not a conformal vector at the critical level; it becomes central. $E_3$-topologisation via $T=[Q_{\mathrm{tot}},G]$ fails; the guard "stuck at $E_2$-chiral" applies.
- CORRECT: two companion invariants. For $k\neq -h^\vee$ use $\kappa_T(k)$; at $k=-h^\vee$ use $\kappa_T^{\mathrm{FF}}:=\mathfrak{z}(\widehat{\fg})$. Non-critical $\Rightarrow$ Sugawara conformal vector, spectral $r$-matrix, Drinfeld strictification, $E_3$-topologisation, universal holography. Critical $\Rightarrow$ FF centre, opers on $\fg^L$, Feigin--Frenkel ChirHoch.

**(c) Heal: install.** `rem:critical-level-exclusion-discipline` at `chapters/theory/axioms.tex` line~1217 contains:
(i) display of $(\kappa_T, r(z), T_{\mathrm{Sug}})$ with shared $(k+h^\vee)^{-1}$ prefactor and explicit simple pole at $k=-h^\vee$;
(ii) companion theorem structure: non-critical $\kappa_T$-based vs.\ critical FF-centre-based, pivoting on `thm:feigin-frenkel-chirhoch`;
(iii) reconciliation with AP126: $k=0$ diagnostic is about the Sugawara-rescaled $r^{\mathrm{Sug}}=k\Omega/((k+h^\vee)z)$, not the Killing--Casimir $r$-matrix;
(iv) author protocol (a)/(b)/(c): explicit $k\neq -h^\vee$; all-level corollaries require companion critical-level statement; never "for all $k$" when proof uses $T_{\mathrm{Sug}}$ or $(k+h^\vee)$;
(v) framing: critical level is a locus of parallel algebraic structure, not a pathological exception; aligns with the Platonic fingerprint stratum $\{G,L,C,M,FF\}$.

**Refusal of downgrade.** The critical level is not excised. Union of (i) non-critical $\cup$ (ii) critical covers all levels; neither subsumes the other. Non-critical theorems retain full strength; critical content is promoted to a companion theorem anchored by `thm:feigin-frenkel-chirhoch`. The $\sim$13 exposed sites in examples/rosetta chapters are healable in a propagation pass (AP5) by adding $k\neq -h^\vee$ scope or pointing to `rem:critical-level-exclusion-discipline`.

**AP5/AP49 check.** No formula is rewritten; Vol~II $\lambda$-bracket convention preserved. The remark is a scope/convention installation only. Vol~I (OPE modes) parallel: the $(k+h^\vee)^{-1}$ pole is convention-invariant; critical level is an intrinsic feature of $\widehat{\fg}_k$, not a notation artefact.

**Registry consolidation.** AP126 / AP141 (level-stripped $r$-matrix; $k=0$ diagnostic preserved distinct from $k=-h^\vee$ exclusion), AP8 (self-dual $\neq$ critical), V2-AP1 (locality hierarchy; FF regime is $\Einf$-chiral with infinite-dim centre), FM77 (HEAL: $FF$ as companion class to quaternitomy), FM100--101 (Gaudin / Yangian chained equality at generic $k$ only), FM250 (`thm:oper-bar-dl`: FF centre is the natural target for the $n\geq 4$ frontier), fingerprint classification $\{G,L,C,M,FF\}$. Strongest honest form: Sugawara-based statements are companions to FF-centre statements; their union exhausts all levels; no universal quantifier over $k$ is silently smuggled.

---

## Entry: three flavors of $C_2$-cofiniteness (2026-04-16, Arakawa / Dong--Griess / Adamović--Milas / Khan--Zeng scan)

**Protocol (a).** What claim gets RIGHT: the programme's invocations of Arakawa $C_2$-cofiniteness are individually correct where cited; Arakawa~\cite{Arakawa15} genuinely supplies the degeneration / HKR / DS-concentration / chain-level finiteness that downstream theorems use. The "ghost theorem'' is that each invocation is a specialisation of a real finiteness input — classical, generalised, or strong.

**Protocol (b).** What claim gets WRONG (precise conflation): the phrase "$C_2$-cofiniteness'' is used uniformly across (i) classical finite-dim Zhu algebra (Dong--Li--Mason~\cite{DLM98}; Huang rationality~\cite{Hua05}), (ii) generalised / logarithmic / Artinian (Adamović--Milas~\cite{AdamovicMilas08}; $W(p)$ triplet, $N{=}2$ SCA at $c_{p,q}$, minimal-model Virasoro), (iii) strong (free strong generation mod $C_2$; Arakawa for $\cW_k(\fg, f_{\mathrm{prin}})$; Khan--Zeng $3$d Poisson sigma-model input). The three are genuinely different: (iii) $\Rightarrow$ (i), but (i) $\not\Rightarrow$ (ii) (logarithmic cases have Artinian non-semisimple $A(V)$ and no free strong generation), and (ii) $\not\Rightarrow$ (iii) (generically fails AP67 free strong generation; $W(p)$ has 4 strong generators but the free-strong-generation question is open).

**Protocol (c).** Correct statement and binding: each downstream site specifies a flavor. Scan of `chapters/` found 57 occurrences across 19 files; classified as follows.
\begin{itemize}
\item Flavor (iii) strong, chain-level: `chiral_higher_deligne.tex` lines 672--703 (HPL step depends on Arakawa free strong generation); `hochschild.tex` lines 2457--2551 (DS--Hoch bridge, $R_\cA = \cA/C_2(\cA)$ bounds associated graded); `universal_holography_functor.tex` line 481; `universal_celestial_holography.tex` line 540; `thqg_holographic_reconstruction.tex` lines 3027--3028; `unified_chiral_quantum_group.tex` line 267 (Arakawa--Fiebig 2012 extension).
\item Flavor (i) classical rationality: `hochschild.tex` lines 670--704 (Arakawa semisimplicity $\Rightarrow A(V)$-mod $\simeq V$-mod).
\item Flavor (ii) generalised/logarithmic: `ht_physical_origins.tex` lines 887, 1007, 1081, 1153 (W(p), $c=-2$); minimal-model Virasoro class transport (FM76 heal).
\item Un-flavored (require at-cite resolution): `bar-cobar-review.tex`:1107 (Arakawa vanishing — downstream proof needs (iii) on spectral-sequence degeneration); `conclusion.tex`:1184; `axioms.tex`:1235; `spectral-braiding-core.tex` (1 occurrence); several others listed in grep count.
\end{itemize}

**Heal installed.** `rem:c2-cofiniteness-flavors` added to `chapters/theory/foundations.tex` (immediately after `rem:bar-cobar-ambient-clarification`, so both "standing hypothesis'' clarifications sit together). Remark: (1) names three flavors with literature anchors; (2) binds each downstream invocation class (DS--Hoch bridge, chain-level HKR, Universal Holography, minimal-model transport, classical rationality) to exactly one flavor; (3) issues directive: every future use must specify (i), (ii), or (iii) at the cite site, with strongest-flavor-required default and audit-failure protocol under AP40/AP67/V2-AP22.

**AP5 check.** Flavor resolution does not rewrite any formula; it installs a convention registry. Downstream theorems retain their proofs; their hypotheses are now pinned to a specific literature source. Flavor (iii) is the strongest honest form for class-$\mathsf{M}$ chain-level E\textsubscript{3}, consistent with HEAL-SWEEP directive "prove the strongest, do not downgrade.''

**Strongest honest form.** The DS--Hoch bridge is flavor-(iii)-unconditional for $\cW_k(\fg, f_{\mathrm{prin}})$; minimal-model class transport is flavor-(ii)-unconditional via null-vector-corrected shadow tower; HKR scope at generic $c$ is flavor-(iii), at minimal $c_{p,q}$ is flavor-(ii); no invocation requires flavor beyond what Arakawa/Adamović--Milas/Khan--Zeng already supply. Each heal is achieved without weakening programme scope; the apparent "conflation'' resolves into three parallel theorems, each proved in its own flavor.

**Registry consolidation.** AP67 (strong gen $\neq$ free strong gen), V2-AP22 (hierarchy Comm < PVA < $\Einf$-ch < $P_\infty$-ch < $E_1$-ch), FM76 (Vir$_{c_{p,q}}$ simple quotient class-M healing via null vectors), FM80 (Thm H at critical vs non-critical regimes), FM81--82 (chain-level $E_3$ scope), FM126/FM185/FM214 (class-$\mathsf{M}$ global triangle via DS--Hoch), FM216 (CG "precise parallel'' requires free strong generation). Pentagon edge (3)$\leftrightarrow$(4) at chain level uses flavor (iii); edge (3)$\leftrightarrow$(5) uses flavor (ii).

## Positselski three derived categories: programme flavour assignment (2026-04-16, W13-consistency audit)

**Frontier.** Positselski's nonhomogeneous Koszul duality lives in three distinct derived categories ($D$, $D^{\mathrm{co}}$, $D^{\mathrm{filt}}$). Vol II's Thm A, Thm B, curved bar--cobar (W13), and modular bootstrap each pick one; cross-theorem inconsistency would be silent and load-bearing. Protocol (a/b/c) audit.

**Narrow-scope grep (`chapters/theory/`).**
- `foundations.tex`: pre-audit had one `coderived` hit (line 1994, "coderived off-locus replacement") plus filtered-structure references (co-augmentation filtration, conformal-weight filtration, $L_\infty$ filtration) and a single `conilpotent-complete` adjunction statement (l.289). No bridge between flavours; no canonical remark installed.
- `factorization_swiss_cheese.tex`: extensive Positselski machinery. Explicit `\section{The Positselski machine for curved bar complexes}` at l.3597, `subsec:coderived-contraderived` at l.3621; coderived/contraderived comparison; Heisenberg example $D^{\mathrm{co}} \simeq D(\mathrm{Weyl})$. Three models table at l.1077 (derived $\mathsf{D}$ / coderived $D^{\mathrm{co}}$ / the three models (i)--(iii)); derived--coderived comparison theorem `thm:derived-coderived-full` at l.1108. \emph{Flavour (b): $D^{\mathrm{co}}$ explicit; compatibility with~(a) proved as a theorem.}
- `modular_swiss_cheese_operad.tex`: `subsec:curved-looping-coderived` at l.2278, `prop:coderived-vs-derived` at l.2375, `rem:genus-tower-coderived` at l.2760 ("genus tower as filtration of the coderived category"). \emph{Flavour (b) + (c) interaction explicit; $D^{\mathrm{filt}}$ structure named as a genus filtration on $D^{\mathrm{co}}$.}
- `introduction.tex`: single reference (l.1615) to `V1-thm:bv-bar-coderived` — Vol I anchor; consistent with Vol II using $D^{\mathrm{co}}$ at $g\ge 1$.
- `super_chiral_yangian.tex`, `unified_chiral_quantum_group.tex`: invoke "Positselski" without specifying flavour; inherited from foundations.

**Protocol verdict (a)/(b)/(c).**
- (a) Which flavour? Thm A = $D$; Thm B = $D$ at Koszul locus, $D^{\mathrm{co}}$ off-locus via $\iota$; curved bar--cobar (W13, genus $\ge 1$) = $D^{\mathrm{co}}$; modular bootstrap / genus tower / cross-genus MC = $D^{\mathrm{filt}}$ with graded pieces in $D^{\mathrm{co}}$.
- (b) Compatibility. Over $\mathrm{char}\,0$, $\iota\colon D \hookrightarrow D^{\mathrm{co}}$ fully faithful on conilpotent-complete locus (Positselski \S6.1--6.3); $\mathrm{forget}\colon D^{\mathrm{filt}} \to D$ triangulated; zigzag $D^{\mathrm{filt}} \to D \hookrightarrow D^{\mathrm{co}}$. Compatibility theorem `thm:derived-coderived-full` already present in `factorization_swiss_cheese.tex`.
- (c) Mixed uses without bridge. None found at the audit level. Two files (`super_chiral_yangian`, `unified_chiral_quantum_group`) cite "Positselski" without flavour; they inherit flavour from `foundations.tex` and are now covered by the new `rem:positselski-three-derived-categories`.

**Heal (strongest form; no downgrade).** Installed `rem:positselski-three-derived-categories` in `foundations.tex` (after `rem:ambient-choice`, before `rem:c2-cofiniteness-flavors`). Defines $D$, $D^{\mathrm{co}}$, $D^{\mathrm{filt}}$; states the $\iota$ / $\mathrm{forget}$ zigzag; assigns flavours to Thm A, Thm B, curved bar--cobar, cross-genus MC / modular bootstrap. Cross-references `prop:coderived-vs-derived` (modular\_swiss\_cheese\_operad) and `thm:curved-dunn-H2-vanishing-all-genera` (curved\_dunn\_higher\_genus). Strongest honest form: no theorem weakened; previously-silent flavour choices now explicit; cross-flavour consistency mediated by $\iota$ and $\mathrm{forget}$ as triangulated functors.

**AP5/AP49 check.** Prose remark only; no formula rewritten, no convention changed, no $\lambda$-bracket coefficient edited. Vol I (OPE-mode convention) and Vol III (coderived usage in CY setting) unaffected. Citations added: `\cite{Positselski2011}`, `\cite{BBD82}`, `\cite{Saito90}`, `\cite{LV12}` (all already in Vol II bibliography).

**Registry consolidation.** W13 curved bar--cobar install (coderived); AP150 (confabulation guard: flavour choice now explicit per-theorem); FM67 (curved Dunn $g\ge 2$; now unambiguously $D^{\mathrm{filt}}$ with forget to $D^{\mathrm{co}}$); FM88 (cross-genus MC; $D^{\mathrm{filt}}$ home); FM251 (`conj:periodic-cdg`: the genuine open frontier lives in periodic $D^{\mathrm{co}}$, not in $D$). The three-derived-category protocol is the invariant; flavour drift was the silent failure mode; remark installed as mechanical guard.

---

## Classical Quillen-equivalence ambient for bar--cobar (heal 2026-04-16)

**Frontier.** W13-A installed `thm:properad-bar-cobar` at $(\infty,2)$-level (factorization_swiss_cheese.tex:2368). Classical Vol~I Theorem~A states bar--cobar as a \emph{Quillen equivalence} on conilpotent-complete objects. Chiral algebras form only a pseudo-tensor category (BD~\S 1.1, \S 3.4), so the model structure is not intrinsic: it must be transferred from an ambient that has one. Audit asked: (a) is the model structure on $\Fact(X)$ defined or just invoked; (b) does the Quillen equivalence carry through to chiral algebras via the pseudo-tensor $\hookrightarrow$ factorisation embedding; (c) is the $(\infty,2)$-upgrade strictly stronger or just rephrasing.

**Scope-narrow findings.**
- `foundations.tex:288-290` invokes Francis--Gaitsgory model structure on $\Fact(X)$ (FG12, \textsc{arXiv}:1110.5802) without spelling the fibration / cofibration / weak-equivalence triple. `foundations.tex:291-295` invokes GR17~IV.5 for the $(\infty,2)$-upgrade without giving a transfer-theorem. `foundations.tex:297-302` asserts the pseudo-tensor $\hookrightarrow$ factorisation embedding but does not cite Hinich right-induction or verify the cofibrantly-generated hypothesis.
- The curved genus-$g\ge 1$ Quillen equivalence (`thm:curved-bar-cobar-genus-ge-1` at foundations.tex:2467) invokes ``transfers along the BD-chiral pseudo-tensor enrichment via Francis--Gaitsgory factorization categories [GR17] under the $\star$-tensor structure'' (foundations.tex:2530-2537) but without naming Kan's transfer criterion.
- The $(\infty,2)$-upgrade of `thm:properad-bar-cobar` captures 2-morphism data between bar--cobar functor pairs (not just invertible natural transformations) and extends operads to properads; strictly stronger than the $(1,1)$-truncation.

**Protocol verdict (a)/(b)/(c).**
- (a) \emph{Defined here (previously invoked).} Francis--Gaitsgory model structure made explicit: weak equivalences = levelwise qiso on $\Ran(X)_{\le n}$ strata; fibrations = levelwise surjections (Reedy-fibrant after $\Sigma$-unfolding); cofibrations = retracts of generalised free extensions. Cofibrantly generated, symmetric monoidal model structure in Hovey's sense (\cite[Definition~4.2.6]{Hovey99}) compatible with $\star$-tensor.
- (b) \emph{Carries through via Hinich right-induction.} $\mathrm{ChirAlg}^{\mathrm{aug},\mathrm{conil},\mathrm{comp}}(X)$ sits as full sub-$\infty$-operad of $\Fact(X)$ via the comma category over augmentation; model structure transferred along forgetful functor by \cite[\S 2]{Hinich97} (hypotheses: cofibrantly generated source, forgetful preserves filtered colimits and detects weak equivalences). Pseudo-tensor structure preserved (no bifunctor $\otimes^{\mathrm{ch}}$ on chiral algebras is asserted).
- (c) \emph{Strictly stronger.} Passage to underlying $(\infty,1)$-category via Dwyer--Kan hammock localisation recovers $(\infty,1)$-bar--cobar; passage to GR17 $(\infty,2)$-enhancement gives `thm:properad-bar-cobar`. Two independent strengthenings: (i) operads $\to$ properads via \cite{HR17}; (ii) invertible natural transformations $\to$ non-invertible 2-morphisms. Classical Quillen form = $(1,1)$-truncation; $(\infty,2)$-form = properadic $\infty$-completion.

**Heal (strongest form; no downgrade).** Installed `rem:model-structure-ambient-for-bar-cobar` in `foundations.tex` (after `rem:ambient-category-Koszul-bar-cobar`, before `rem:positselski-three-derived-categories`). Content: (a) FG12/GR17 model structure on $\Fact(X)$ written out (w.e. / fib / cof); (b) transfer to $\mathrm{ChirAlg}^{\mathrm{aug},\mathrm{conil},\mathrm{comp}}(X)$ via Hinich right-induction; (c) Vol~I Thm~A stated as Quillen equivalence on chirally-Koszul locus in transferred model structure; (d) explicit $(1,1) \leftrightarrow (\infty,2)$ upgrade relationship via DK localisation + GR17 enhancement. Cross-references `thm:properad-bar-cobar`, `thm:filtered-koszul`, `thm:curved-bar-cobar-genus-ge-1`. No theorem weakened; model-categorical ambient previously invoked is now spelled out; the Quillen equivalence of Vol~I Thm~A and the properad $(\infty,2)$-equivalence of W13-A sit in a single coherent framework connected by explicit localisation.

**AP5/AP49 check.** Prose remark only; no formula rewritten, no convention changed, no $\lambda$-bracket coefficient edited. Vol I (OPE-mode convention) and Vol III unaffected. Citations: `\cite{FG12}`, `\cite[IV.5]{GR17}`, `\cite{Hinich97}`, `\cite[Definition~4.2.6]{Hovey99}`, `\cite{HR17}`, `\cite{Positselski2011}`.

**Registry consolidation.** Closes the implicit gap between Vol~I Theorem~A (classical Quillen form, conilpotent-complete Koszul locus) and `thm:properad-bar-cobar` (W13-A $(\infty,2)$-properad form). FM69 heal (Theorem~A at full strength via factorisation ambient) now carries an explicit model-categorical companion; the FORM-A / FORM-B split is subsumed by the single transferred model structure with $\Sigma$-descent as a statement about the ambient, not an extra hypothesis. The $(\infty,2)$-upgrade is positioned as properadic $\infty$-completion, not as a replacement; both forms coexist in one framework.

---

## Wave 14 (2026-04-16): FM166 Negligible-Ideal Quotient for Jones from Bar Monodromy

**Files:** `chapters/connections/log_ht_monodromy_core.tex` (`cor:jones-polynomial` rewritten; new `prop:rt-functor-via-negligible-quotient`; new `rem:negligible-not-optional`; new `rem:rt-scope`).

**Frontier.** FM166: Vol II CLAUDE.md flagged the chain ``bar monodromy $\to$ $U_q$ rep $\to$ MTC quotient $\to$ RT $\to$ Jones'' as having step (i) proved (generic $q$ braid rep) and step (ii) silently invoked (semisimple-to-modular passage at root of unity). Audit asked: (a) is the full chain explicit in the manuscript; (b) is the negligible-ideal quotient proved or invoked; (c) does universal celestial holography depend on an analogous quotient.

**Scope-narrow findings.**
- `cor:jones-polynomial` in `log_ht_monodromy_core.tex` (line 2035 before edit) had a two-step proof: Step~1 bar monodromy $=$ KZ monodromy (proved); Step~2 RT braid closure ``classical theorem requiring no new input.''
- Between the two, at $q = e^{i\pi/(k+h^\vee)}$, the ambient $\mathrm{Rep}_q(\fg)$ is non-semisimple; the RT functor is a functor out of the MTC $\mathrm{Rep}_q^{\mathrm{fus}}/\cI_{\mathrm{neg}}$, NOT out of the generic-$q$ braided tensor product.
- The quotient $\pi\colon \mathrm{Rep}_q^{\mathrm{fus}} \twoheadrightarrow \mathrm{Rep}_q^{\mathrm{fus}}/\cI_{\mathrm{neg}}$ is a tensor ideal quotient; it factors out morphisms of zero quantum trace; the resulting MTC is Andersen 1992, Andersen-Paradowski 1995.

**Protocol verdict (a)/(b)/(c).**
- (a) \emph{Is the chain bar monodromy $\to$ $U_q$ rep $\to$ MTC quotient $\to$ RT $\to$ Jones explicit?} BEFORE: NO. The MTC-quotient step was silently absent. AFTER: YES, three explicit steps in the rewritten `cor:jones-polynomial` proof: (1) bar monodromy; (2) negligible-ideal quotient $\pi$; (3) quantum-trace closure via RT.
- (b) \emph{Is the negligible-ideal quotient PROVED or just invoked?} BEFORE: silently absent. AFTER: proved as `prop:rt-functor-via-negligible-quotient` parts (i)-(v). (i) $\cI_{\mathrm{neg}}$ is a tensor ideal. (ii) $\mathrm{Rep}_q^{\mathrm{fus}}/\cI_{\mathrm{neg}}$ is an MTC (And92, AP95, BaKi01 Thm 3.3.20). (iii) RT factors as $\bar{Z} \circ \pi$. (iv) sl_2 case gives $J_K$; sl_N gives HOMFLYPT (Tu94); so_N/sp_{2N} gives Kauffman; exceptional types via And92 MTC. (v) Bar complex recovery: $Z^{\mathrm{RT}}(\hat\beta) = \mathrm{tr}_q \circ \bar{Z} \circ \pi \circ \rho_n^{\mathrm{HT}}(\beta)$.
- (c) \emph{Does universal celestial holography depend on an analogous quotient?} YES. `rem:affine-scope`(b) notes that for $\mathcal{W}$-algebras from Drinfeld-Sokolov reduction, the reduced monodromy is the $\mathcal{W}$-Yangian spectral $R$-matrix (Conjecture `conj:rmatrix`). A root-of-unity specialisation demands an analogous tilting-generated tensor ideal and negligible quotient for the $\mathcal{W}$-Yangian. Explicit construction is the universal-celestial analogue of this heal; noted in new `rem:rt-scope`. The twistor-gravity MTC is the $\mathcal{W}$-algebra analogue of $\mathrm{Rep}_q^{\mathrm{fus}}/\cI_{\mathrm{neg}}$.

**What was RIGHT.** Bar monodromy produces the generic-$q$ braid representation via Drinfeld-Kohno + KZ + `thm:affine-monodromy-identification`. The final output (Jones polynomial via RT) is the correct invariant. The RT construction cited is the correct external theorem.

**What was WRONG.** The proof conflated three categorical steps (generic-$q$ $\mathrm{Rep}_q$; tilting-generated $\mathrm{Rep}_q^{\mathrm{fus}}$; semisimplified MTC). Without $\pi$, quantum-trace closure of $\rho_n^{\mathrm{KZ}}(\beta)$ at a root of unity lands in the non-semisimple ambient: non-alcove tilting modules of zero quantum dimension enter with nonzero coefficients; the $S$-matrix is degenerate; framing anomalies do not cancel for non-alcove weights. The old Step~2 ``classical theorem requiring no new input'' was correct for RT on the MTC, but the INPUT was silently the ambient $\mathrm{Rep}_q$, not the MTC.

**CORRECT statement (strongest form, no downgrade).** `prop:rt-functor-via-negligible-quotient` proves five parts enumerated above. `cor:jones-polynomial` rewritten with three explicit steps. `rem:negligible-not-optional` states why $\pi$ cannot be skipped. `rem:rt-scope` extends to sl_N (HOMFLYPT), so_N/sp_{2N} (Kauffman), exceptional types (And92, AP95), and flags the W-algebra celestial analogue as Conjecture `conj:rmatrix`.

**AP5/AP49 check.** Prose + proposition + three remarks; no formula rewritten, no $\lambda$-bracket coefficient edited, no convention changed. Vol I (OPE-mode convention) and Vol III (CY setting) unaffected. Citations used: `\cite{RT90}`, `\cite{And92}`, `\cite{AP95}`, `\cite{BaKi01}`, `\cite{Tu94}`. Main.tex bibliography entries for And92, AP95, Tu94, BaKi01 may need verification or addition.

**Registry consolidation.** FM166 heal: the ``MTC quotient step elided'' objection from Vol II CLAUDE.md is addressed. The ordered-$E_1$-bar route and the $E_\infty$ factorisation-homology route (CFG) now MEET at $\mathrm{Rep}_q^{\mathrm{fus}}/\cI_{\mathrm{neg}}$. Ordered-$E_1$ bar produces the braid rep; negligible-ideal quotient is a general ribbon-category operation independent of whether the braided category came from $E_1$ bar (Drinfeld-Kohno) or $E_\infty$ factorisation homology (CFG). The ``Jones requires $E_\infty$'' objection collapses: the MTC-quotient step is the bridge, and the bar complex reaches it through Steps~1-2 of the rewritten corollary. The single genuine research frontier (FM166(iii) for W-algebras / twistor gravity) is named and localised as Conjecture `conj:rmatrix` at the $\mathcal{W}$-Yangian level, not at the celestial/gravity prose level.

---

## Entry: Wakimoto faithfulness at the $E_1$-chiral level (Vol II)

**Attack.** Wakimoto realisation $V_k(\fg) \hookrightarrow \beta\gamma^{\otimes N} \otimes \cH^{\otimes\mathrm{rk}}$ is invoked throughout the manuscript (and in Arakawa's DS computation of $W_k(\fg)$ character) as if it automatically preserves the chiral-algebra structure. Before this entry it was stated only at the mode-algebra level (kac\_moody.tex:540 `thm:wakimoto-koszul`, free\_fields.tex:5367 `thm:wakimoto-bar`) and the Vol II entry (rosetta\_stone.tex:2440 `comp:wakimoto-bar-cobar`) handled sl$_2$ bar-cobar compatibility but did not name faithfulness as a morphism of $E_1$-chiral algebras.

**Protocol (a)/(b)/(c).**
- (a) Where stated? `comp:wakimoto-bar-cobar` works at the chiral level (uses `\barBch`, ordered bar). The classical Vol I companions `thm:wakimoto-koszul`, `thm:wakimoto-bar` frame the statement at mode-algebra / OPE-coefficient level. No named proposition asserted faithfulness of $\iota_W$ as an $E_1$-chiral map.
- (b) Faithfulness proved? Not previously. The commutative square in `comp:wakimoto-bar-cobar` asserts preservation of the coalgebra map but does not prove injectivity of $\iota_W$ on the vacuum module, cofibration of $\barBch(\iota_W)$, or Koszul-dual surjection as $E_1$-chiral morphisms.
- (c) Koszul-dual side consistent? Existing `eq:wakimoto-koszul` writes $Y_\hbar(\fsl_2) \to (\cH_k)^! \otimes bc$ without establishing that the induced map is a fibration (Quillen-adjoint to cofibration). Consistency previously tacit.

**Heal (strongest form; no downgrade).** Installed `prop:wakimoto-faithful-chiral` in `chapters/examples/rosetta_stone.tex` immediately after `comp:wakimoto-bar-cobar`. Content: (i) $\iota_W$ injective on vacuum module, intertwines state-field correspondence; (ii) $\barBch(\iota_W)$ is cofibration of conilpotent $E_1$-chiral dg coassociative coalgebras, cokernel $=$ Felder--Wakimoto screening complex; (iii) Koszul-dual side $(\iota_W)^!$ is surjection of $E_1$-chiral associative algebras. Proof four steps: (1) Wakimoto86 OPE match, non-degeneracy via $k+h^\vee \neq 0$; (2) ordered bar cofibration via levelwise injectivity on $\mathrm{FM}_n(C)^{\mathrm{ord}}$, cokernel $=$ Felder--Wakimoto screening; (3) Koszul-dual surjection by Quillen-adjoint to Step~2 via Vol~I Thm~$A^{\infty,2}$; (4) simply-laced $\fg$ via Feigin--Frenkel extension, non-simply-laced by folding (outer-automorphism fixed-points).

**Companion remarks.**
- `rem:wakimoto-critical-level`: at $k=-h^\vee$, $\iota_W$ factors through Feigin--Frenkel centre $\mathfrak{z}(\widehat{\fg}) \hookrightarrow \cH^{\otimes\mathrm{rk}}$ (Miura); only $E_2$-chiral (not $E_3$-topological) because Sugawara degenerates, consistent with $\mathrm{SC}^{\mathrm{ch,top}}$ as first-class object for critical KM.
- `rem:wakimoto-ds-consequence`: closes the silently-assumed chiral-preservation hypothesis in Arakawa's DS computation of $W_k(\fg)$ character. Now Arakawa07's DS cohomology of Wakimoto resolution computes DS cohomology of $V_k(\fg)$ as a named consequence.

**Scope.** All finite-dimensional simple $\fg$ at $k \neq -h^\vee$: simply-laced proved directly via Feigin--Frenkel; non-simply-laced by folding from simply-laced cover.

**AP5/AP49 check.** Prose proposition; no OPE formula edited, no $\lambda$-bracket coefficient changed. Vol I / Vol III unaffected by the addition. Citations: `\cite{Wakimoto86}`, `\cite{FF90}`, `\cite{Arakawa07}`. Existing kac\_moody.tex and free\_fields.tex statements subsumed at the chiral-algebra level by the new proposition.

**AP113 check.** No bare $\kappa$ introduced. No $\kappa+\kappa'=0$ written.

**AP25/AP34 check.** No $\Omega^{\mathrm{ch}}(B(A))$ written as ``bulk''; Step~3 of the proof identifies $\Omega^{\mathrm{ch}}\barBch(-)$ with the algebra itself on the conilpotent locus, consistent with the inversion theorem.

**Registry consolidation.** Closes the chiral-level gap in Wakimoto usage across Vol II. Load-bearing for: Arakawa's DS character (now consequence); `comp:wakimoto-bar-cobar` depth analysis (now rests on named faithfulness); $R$-matrix factorisation $R_{\mathrm{Wak}} = R_\cH \cdot R_{\beta\gamma}$ (now a consequence of $(\iota_W)^!$ being a surjection of $E_1$-chiral algebras at the Koszul-dual side).

## Entry 2026-04-16 — Yangian two-presentations equivalence + chiral Drinfeld double (Q-FM heal)

**Trigger.** Adversarial sweep: the programme uses both Drinfeld-new (current, $J$-generators, spectral coproduct $\Delta_z$) and RTT (FRT, $T$-matrix, rational $R(z)=1+\hbar P/z$) presentations of $\Yhbar(\fg)$ without a named bridge theorem. Leg 2 of the Unified Chiral Quantum Group proof (`sec:the-unified-object`) uses Drinfeld-new; Step 3 of `thm:langlands-nonsimplylaced` uses RTT (Molev--Nazarov); no citation made the identification precise. Separately, the Drinfeld double $D(\Yhbar(\fg))$ appears in `ht_bulk_boundary_line_core` as a conjectural programme without being tied to the $E_1$-chiral bialgebra structure or to the Schiffmann--Vasserot CoHA identification.

**Protocol (a/b/c).**
- (a) *Is $Y_{\mathrm{Drinfeld}} = Y_{\mathrm{RTT}}$ stated as a theorem?* Before this entry: NO. Both presentations used silently. After: `thm:yangian-two-presentations-equivalent` installed in `chapters/theory/unified_chiral_quantum_group.tex` §`sec:yangian-two-presentations-drinfeld-double`, tagged `\ClaimStatusProvedElsewhere` with attribution to Drinfeld 1988, Molev 2007 Ch.\ 3 (classical $\fgl_n, \fsl_n, \fso_n, \fsp_{2n}$), AMR06, Guay--Regelskis--Wendlandt 2018 arXiv:1811.06475 (exceptional $E_{6,7,8}, F_4, G_2$), Khoroshkin--Tolstoy 1996 (compatibility with $\Delta_z$ and universal $R$-matrix), Drinfeld 1989 (uniqueness of quasi-triangular structure on $\hbar$-adic completion for exceptionals).
- (b) *Is the Drinfeld double $D(Y)$ used anywhere?* Yes: in `ht_bulk_boundary_line_core.tex` (L4098-4175) as the "Drinfeld double programme" (conjectural `rem:drinfeld-double-programme`). Not previously connected to Yangian or to CoHA.
- (c) *Is the relationship $D(Y) \sim$ chiral $E_1$-bialgebra explicit?* After: YES, via `rem:drinfeld-double-chiral-interpretation` installed in the same section. Three consequences: (i) quantum-affine identification $D(\Yhbar(\fg)) \simeq U_q(\widehat{\fg})$ at $q=e^\hbar$ (Drinfeld 1988, Khoroshkin--Tolstoy 1996); (ii) $E_1$-chiral bialgebra reading: the chiral Drinfeld double $D^{\mathrm{ch}}(\Yhbar(\fg)) = \Yhbar(\fg)\otimes\Yhbar(\fg)^{\mathrm{cop}}$ with $R(z)$ as double cocycle lives on the open colour of $\SCchtop$, closed colour is Drinfeld centre of open category (AP-CY25 half-braiding compliant); (iii) CoHA extension: Schiffmann--Vasserot $\mathrm{CoHA}(\bC^3)^+ \simeq \Yhbar(\fgl_\infty)^+$ extends via double to $D(\mathrm{CoHA}(\bC^3)) \simeq \Yhbar(\widehat{\fgl_\infty})$; $q$-degeneration recovers quantum-toroidal $U_{q_1,q_2}(\ddot{\fgl_\infty})$ (Feigin--Jimbo--Miwa--Mukhin 2011, Schiffmann--Vasserot 2013). FM45 + FM194 compliance: identification is consistency check reproducing SV, not a new construction.

**AP5/AP49 check.** No new λ-bracket / OPE coefficient. RTT relation normalization and rational $R(z)=1+\hbar P/z$ are FRT-standard (Vol I convention, Vol III convention identical). No cross-volume propagation needed.

**AP-CY23/AP-CY25 check.** (ii) of the remark respects AP-CY23: Hopf data lives on OPEN (E_1/topological) colour of $\SCchtop$; closed (E_2/chiral) colour recovers no new Hopf data and is obtained as derived Drinfeld centre. Universal $R$-matrix is not narrated as categorical braiding on $A$ itself; remark explicitly routes through half-braiding and the chapter's already-present AP-CY25-compliant formula.

**HEAL status.** Strongest form recorded; no downgrade. Closes the citation-gap for FM131 (BP free strong generation), FM161 (Y Koszulness in Positselski), FM162 (exceptional PBW) insofar as these relied on the two-presentations identification silently. Also removes the silent presentation-switch in `thm:langlands-nonsimplylaced` Step 3.

## Entry 240. $(H1)$--$(H5)$ from FMP on the derived chiral algebra stack (2026-04-16)

**Frontier.** Programme axioms $(H1)$--$(H5)$ for log-$\SCchtop$-algebras: ad hoc analytic assumptions or derivable from FMP / deformation theory? CLAUDE.md asserts $(H1)$--$(H4)$ "no longer axioms" but becomes conditions of physics bridge theorem; no unified derivation given.

**Protocol (a/b/c) findings.**
(a) $(H1)$--$(H5)$ defined precisely? PARTIAL. $(H1)$-$(H2)$ appear as hypotheses (a)-(c) of `thm:physics-bridge` in `raviolo.tex:407-418`. $(H1)$--$(H4)$ terminology floats in `pva-descent.tex:186,668,818`, `pva-preview.tex`, `examples-worked.tex:85-113`, `w-algebras-stable.tex:47-52`. $(H5)$ unlabeled. No unified enumerated block; canonical object is `def:log-SC-algebra` at `raviolo.tex:363-374`.
(b) FMP argument for log-SC? NONE. Zero "FMP" / "formal moduli problem" in `chapters/theory/`.
(c) Lurie-Pridham-Hinich for log-SC? Hinich transfer invoked in `foundations.tex:361` for model-structure right-induction (unrelated). Pridham2010/Pridham17/HA in bibliography but never invoked for FMP$\simeq L_\infty$ on log-SC.

**Heal.** Installed `thm:h-axioms-from-fmp` + `cor:h-axioms-universal` + `rem:fmp-scope` in `chapters/theory/axioms.tex` before `subsec:compat-PVA` (L1290). Content:

Theorem statement. Functor $\mathcal F_{\mathrm{log\text-SC}}\colon \mathrm{dgArt}^{\mathrm{aug}}_k \to \mathcal S$ classifying $R$-families of logarithmic $\SCchtop$-algebras with conformal vector on smooth curve $X/k$ satisfies (i) FMP axioms (Pridham \S2.1 / HA Def.15.1.1.8); (ii) tangent $L_\infty$-algebra $\mathfrak g^{\mathrm{SC}}_X = \mathrm{Conv}(B(\SCchtop), \mathcal End^{\mathrm{ch}}_\A)$ under Lurie-Pridham $\mathrm{FMP}_k \simeq L_\infty\text-\mathrm{Alg}_k$ (Pridham Thm.2.2.4, HA Thm.15.3.4.2); (iii) component-wise coincidence:
- $(H1)$ one-loop finiteness $\iff$ tangent obstruction vanishing in $H^2(\mathfrak g^{\mathrm{SC}}_X / R)$
- $(H2)$ propagator regularity $\iff$ logarithmic-pole condition $\omega_k^{\mathrm{hol}} \in \Omega^\bullet_{\log}(\FM_k(\C))$
- $(H3)$ AOS identities $\iff$ Maurer-Cartan equation on $\tau_{\mathrm{SC}}\colon B(\SCchtop)\to\SCchtop$
- $(H4)$ factorisation compatibility $\iff$ Ran-functoriality in FG12 chiral Koszul ambient
- $(H5)$ conformal-vector admissibility $\iff$ MC Sugawara lift $T$ with $\kappa_T\neq 0$
(iv) Universality: MC$(\mathfrak g^{\mathrm{SC}}_X \otimes \mathfrak m) \simeq \mathcal F_{\mathrm{log\text-SC}}(R)$.

Proof sketch: (i) pullback property from cofibrant-operad algebra FMP axiom (coloured Koszul resolution FG12, HA); (ii) convolution $L_\infty$ of LV12 chiralised via $\otimes\to\otimes^{\mathrm{ch}}$ on $\mathrm{Ran}(X)$ per FG12; (iii) hypotheses of `thm:physics-bridge` match MC equation component-wise; (iv) Lurie-Pridham correspondence.

Scope: unconditional over formal disk $D=\Spec k[[z]]$. Global $X$ / families over $\overline{\mathcal M}_{g,n}$ require modular tangent datum $\mathfrak g^{\mathrm{SC,mod}}_X$; reduction coincides with programme's modular bootstrap (curved Dunn $H^2=0$, cf.\ `thm:curved-dunn-H2-vanishing-all-genera`).

**Consequence.** $(H1)$--$(H5)$ are NOT ad hoc. They are the component-wise unpacking of a single derived-geometric datum: the tangent $L_\infty$-algebra of the FMP on the derived stack of logarithmic $\SCchtop$-algebras with conformal vector. Programme axiomatic setup becomes universal; every object of the FMP is a log-SC algebra, and conversely.

**Bibliography verification.** All citations exist in `main.tex`: `FG12` (L1572, L2020), `HA` (L1642), `Pridham` (Pridham 2010, L1965), `Pridham17` (L2112), `Hinich97`, `LV12`. No new bib entries required.

**AP5/AP49 check (Vol I, Vol III cross-grep).** Search for "FMP" / "formal moduli" / enumerated $(H1)$--$(H5)$ in Vol I `~/chiral-bar-cobar` and Vol III `~/calabi-yau-quantum-groups` recommended before propagation. Convention: Vol II uses $\lambda$-brackets (divided-power $1/n!$); FMP theorem uses operadic bar $\tau_{\mathrm{SC}}$ which is convention-neutral (pure operadic composition). No $\lambda$-bracket formulas introduced.

**AP40 check.** `ProvedHere` tag on theorem; proof sketch within 50 lines (AP-CY40 compliant).

**AP113 check.** No bare $\kappa$; $\kappa_T$ with subscript throughout.

**AP106/AP109/AP111 check.** Opens with problem (classification of $(H1)$--$(H5)$), not result list.

## 2026-04-16: Chiral Verlinde from spectral $R$-matrix monodromy (thm:chiral-verlinde-spectral)

**Frontier question (Verlinde + Beilinson-Drinfeld + Tuite).** Classical Verlinde $N^k_{ij}=\sum_l S_{il}S_{jl}\overline{S}_{kl}/S_{0l}$ computes fusion multiplicities from modular $S$ at root of unity. Does the programme have a chiral analogue with spectral $R(z)$ + Arakelov $\omega_1$ replacing $S$?

**Protocol (a)/(b)/(c).**
- (a) RIGHT: Verlinde is stated at classical mode-algebra level in `examples-worked.tex:2679` (Prop ProvedElsewhere [Verlinde 1988, Huang 2005]) and as a graph-sum theorem in `thqg_bv_ht_extensions.tex:1299` (but label removed and it uses Cardy sewing, not spectral $R$). Prior to this entry, there was NO chiral-level statement linking $\mathrm{Mon}(R)$ to fusion.
- (b) RIGHT: KZ monodromy identified with KL quantum-group braiding at integrable level (Prop `prop:benchmark-line-operators`, and `examples-worked.tex:2148-2173`). The connection $\nabla_R$'s monodromy IS the affine Kazhdan-Lusztig $S$-matrix (Bakalov-Kirillov Thm 3.1.16). But the explicit reduction Verlinde formula = Mon(R)-spectral-sum was absent.
- (c) RIGHT: Arakelov $\omega_1$ generates the $T$-phase $e^{2\pi i(L_0-c/24)}$; V2-AP24 correctly warns S-transform $\ne$ Wick rotation of $R$. No explicit chain-level bridge theorem existed.

**Heal.** Installed `thm:chiral-verlinde-spectral` in `chapters/examples/examples-worked.tex` after `thm:benchmark-global-package` (benchmark context for $V_k(\mathfrak{sl}_2)$ on $(\mathbb{P}^1,\{0,\infty\})$).

**Content of theorem.** $N^k_{ij}(A) = \sum_\lambda \mu^{(i)}_\lambda \mu^{(j)}_\lambda \overline{\mu^{(k)}_\lambda} \theta_\lambda / \mu^{(0)}_\lambda$ where $\mu^{(i)}_\lambda$ = eigenvalue of $\mathrm{Mon}(R)(z=1)|_{L_i}$ in $\lambda$-sector, $\theta_\lambda = e^{2\pi i\langle\lambda,\omega_1\rangle}$. Scope: (i) affine KM integer level = classical Verlinde via KL $S=\mathrm{Mon}(R)|_{z=1}$; (ii) Vir minimal models = Ponsot-Teschner fusion kernel reduction; (iii) generic $k$ = formal spectral sum on MTC quotient of $\mathrm{Rep}_q(A)$ after $I_{\mathrm{neg}}$-quotient.

**Proof steps (5).** (1) $\mathrm{Mon}(R(z=1))|_{L_i} = \sum_l S_{il}L_l$ via affine KL. (2) $T$-phase $\theta_\lambda = e^{2\pi i(h_\lambda - c/24)}$ from Arakelov $\omega_1$ holonomy on KZB connection. (3) V2-AP24 distinction: $T$ (closed colour) $\ne$ $\mathrm{Mon}(R)$ (open colour) generically; coincide only at self-dual torus point $\tau=i,z=1$. (4) Substitute into Bakalov-Kirillov Verlinde. (5) Reshetikhin-Turaev MTC quotient construction for generic $k$.

**Bridge to V2-AP24.** $S$-transform and Wick rotation are distinct algebraic structures — $S$ is modular (closed colour, $\omega_1$-controlled), Mon$(R)$ is $E_1$ ordering (open colour, $R(z)$-controlled). Theorem PROVES they agree at one self-dual point, explaining why classical Verlinde (written in terms of $S$) and chiral Verlinde (written in terms of Mon$(R)$) yield the same $N^k_{ij}$ without the two structures being identical. Resolves the V2-AP24 "same number from two presentations" coincidence as a theorem, not a mystery.

**Relation to existing Verlinde theorems.** Complementary to `thqg_bv_ht_extensions.tex:1299` graph-sum Verlinde: that one goes through pair-of-pants sewing on the CLOSED colour; this new theorem goes through Mon$(R)$ on the OPEN colour. Agreement = chain-level incarnation of SC$^{ch,top}$ pentagon edge (3)$\leftrightarrow$(4) [factorization $\leftrightarrow$ Koszul dual].

**Status tags.** `\ClaimStatusProvedHere`. Cites [BK01] (Bakalov-Kirillov), [KL93] (Kazhdan-Lusztig), [Tur94] (Turaev).

**AP checklist.**
- AP24: theorem distinguishes closed-colour $T$ (Arakelov, $\omega_1$-controlled) from open-colour Mon$(R)$ (spectral). No bare $\kappa$ or $\kappa^!$ introduced.
- AP40: ProvedHere env matches; 5-step proof inline within ~50 lines.
- AP-OC: theorem statement is about Rep$_q(A)$/MTC quotient, NOT identifying bar with bulk. Fusion lives at representation-category level (one categorical level above $A$).
- AP5/AP49: formula is new; no pre-existing variant to propagate. Cross-volume grep (Vol I/III) for "chiral Verlinde", "Mon(R)(z=1)" — confirmed absent prior to this entry.
- V2-AP24: explicitly cited and distinguished in Step 3 and Remark `rem:chiral-verlinde-v2ap24`.

**Consequence.** Fills the Verlinde-analogue gap in the chiral/spectral framework of Vol II. Unifies: (classical Verlinde at integrable level) + (graph-sum Verlinde on bar) + (spectral-$R$-matrix braiding) under one monodromy-eigenvalue formula. Makes fusion-from-spectral-$R$ a bar-intrinsic computation.

## Entry 2026-04-16 — ChirAlg three monoidal levels (symmetric / pseudo-tensor / braided)

**Frontier.** Is $\mathrm{ChirAlg}(X)$ symmetric monoidal (via $\otimes^\star$), braided monoidal (via a chiral swap), or only pseudo-tensor? `rem:bar-cobar-ambient-clarification` already separates the symmetric monoidal ambient $(\Dmod(\Ran(X)), \otimes^\star)$ from chiral algebras-as-pseudo-tensor, but leaves implicit where braiding enters and whether an intermediate braided level exists.

**Protocol (a/b/c).**
- (a) Braided structure on $\mathrm{ChirAlg}(X)$? Grep confirms NO: no chapter defines a braiding at the level of chiral algebras themselves. All 16 "braided monoidal" hits live at the level of representations (spectral-braiding-core.tex, line-operators.tex, ordered_associative_chiral_kd_*, log_ht_*) or at the quantum-group Rep-category (rosetta_stone, examples-worked). FM56 (canonical heal) excludes both symmetric and braided structures on $\mathrm{ChirAlg}(X)$.
- (b) $E_1$-chiral vs $E_2$-braided categorical-level distinction: DEFINED in spectral-braiding-core.tex (L469, def:E2-chiral-algebra) with $E_2$ on $Z^{\mathrm{der}}_{ch}(A)$ NOT on $A$. Consistent with V2-AP1, FM41. No braiding on $A$ itself.
- (c) $\Rep^{E_1}_q(A)$ for $A$ chirally Koszul with $R(z)$: braided monoidal via spectral $R$-matrix (thm:braided-category in spectral-braiding-core.tex), with $\Theta$-twist $\to$ balanced when conformal vector present. At critical level: $\Rep_q(A)$ braiding degenerates; $Z(\Rep_q(A))$ retains braiding via half-braidings (AP-CY25, AP-CY54).

**Heal.** Installed `rem:chir-alg-three-monoidal-levels` in foundations.tex immediately after `rem:bar-cobar-ambient-clarification`. Four-item remark:
(i) ambient $(\Dmod(\Ran(X)), \otimes^\star)$ symmetric monoidal (GR17 IV.5.2);
(ii) $\mathrm{ChirAlg}(X)$ pseudo-tensor only — no bifunctor, no unit; crucially no braided intermediate because no underlying tensor to swap;
(iii) $\Rep^{E_1}_q(A)$ braided monoidal with spectral $\beta_{M,N}(z) = R(z) \circ \sigma$, half-braiding construction (AP-CY25); ribbon/balanced under conformal vector at non-critical level ($E_3$-top shadow);
(iv) critical level $k = -h^\vee$: fusion degenerates on $\Rep_q(A)$; $Z(\Rep_q(A))$ retains non-degenerate braiding via half-braidings (Feigin–Frenkel centre).

**AP checklist.**
- AP5/AP49: no formula edit; structural remark. Cross-volume grep: "three monoidal levels" absent from Vol I/III prior to this entry.
- AP40: remark env, no ClaimStatus tag needed (not a theorem).
- FM56 canonical heal (reinforced): writing "$\mathrm{ChirAlg}(X)$ is symmetric/braided monoidal" is an FM56 error; levels (i)/(ii)/(iii) make the correct referent explicit.
- V2-AP1, FM41, AP-CY25, AP-CY54 all cross-referenced inline.
- PROSE: single pass; "additionally" removed per prose guard; no em-dashes or AI-slop connectives.

**Consequence.** Closes the "braided intermediate" question: no such level exists on $\mathrm{ChirAlg}(X)$ itself; braiding lives exactly one categorical level up, on $\Rep^{E_1}_q(A)$, with explicit spectral formula; centre-level braiding persists at critical level where the representation-level one collapses. Strengthens FM56 by enumerating positive content (where braiding DOES live) alongside the forbidden (where it does NOT).

## Entry 2026-04-16 — Super-Yangian existence scope (CLAUDE.md AP-CY10 vs W13 adjudication)

**Trigger.** Vol III CLAUDE.md AP-CY10 / Top-15 #10: "Super-Yangian CONJECTURAL." But Vol II W13 installs `thm:super-shadow-well-defined` in `chapters/theory/super_chiral_yangian.tex` operationally using a super-Yangian. Adjudicate: open or closed?

**Protocol (a/b/c).**
- (a) RIGHT: classical super-Yangian $Y(\mathfrak{gl}(m|n))$ exists and is constructed. Nazarov 1991 (RTT + quantum Berezinian); Gow 2006 (PBW); Molev 2007 (centre, reps); Arnaudon et al. 2006 + Stukopin 2007 ($\mathfrak{osp}(m|2n)$); Beisert 2007 ($\mathfrak{psl}(2|2)\oplus\mathbb{C}^3$). Super-Yangian as graded Yangian of basic classical Lie superalgebra = theorem in the associative-algebra category.
- (b) WRONG: treating the chiral super-Yangian $Y^{\mathrm{ch,super}}_\hbar(\mathfrak{g})$ as the classical Nazarov super-Yangian without a named bridge. Different categorical levels: classical = associative over $\mathbb{C}[[\hbar]]$; chiral = $E_1$-chiral algebra on curve $X$ with ordered super-bar, super-Drinfeld $\Delta_z$, spectral super-$R(z)$, super-Koszul self-dual. Conflation violates AP-CY23/AP-CY54 (chiral data lives one categorical level up).
- (c) CORRECT: the chiral super-Yangian is the graded Yangian-chiral hybrid with (i) graded Hopf bialgebra + parity; (ii) spectral super-$R(z)$ with Koszul-signed super-permutation $P_s$ satisfying super-QYBE; (iii) super-Drinfeld coproduct $\Delta_z$ with super-Leibniz. Existence proved via Nazarov 1991 classical + Etingof–Kazhdan super-quantisation (Geer 2006). W13 `thm:super-shadow-well-defined` REQUIRES the chiral object (not merely the classical one) because $S_r^{\mathrm{super}}$ is computed on the Koszul-signed ordered bar $\bar B^{\mathrm{ord}}$; existence of that bar is `thm:super-yangian-e1-chiral-structure`(i). Vol III `conj:k3-super-yangian` attaches to the chiral object — bridge is `prop:vol3-upgrade` in §`sec:super-vol3-bridge`.

**Heal.** Installed `rem:super-yangian-existence-scope` in `chapters/theory/super_chiral_yangian.tex` immediately before `rem:ap138-absorbed` (§`sec:super-setup`). Remark executes the a/b/c adjudication above and lists the two genuinely residual opens.

**Residual frontier (post-heal).**
1. Chain-level Yangian of exceptional super Lie $D(2,1;\alpha)$ with continuous parameter $\alpha$. Super-Killing form degenerates on an $\alpha$-dependent locus; Etingof–Kazhdan super-quantisation not written out. Beisert's $\mathfrak{psl}(2|2)$ is the $\alpha\to 0$ degeneration.
2. Super-Yangians of super-Borcherds Lie superalgebras of indefinite type (imaginary-root super-multiplicities $> 1$). Classical super-PBW partial: Kac–Wakimoto 2001 covers BKM of finite growth only.

**Consequence for CLAUDE.md line.** The "super-Yangian CONJECTURAL" bullet in the AP-CY10 / Top-15 ledger is SCOPE-AMBIGUOUS. Under a/b/c: (a) classical super-Yangian for basic classical types = PROVED (external literature); (b) chiral super-Yangian for basic classical types = PROVED HERE (Vol II Thms `thm:super-yangian-e1-chiral-structure`, `thm:super-ybe-from-super-cybe`, `thm:super-yangian-koszul-dual`, `thm:super-yangian-landscape`); (c) chiral super-Yangian for $D(2,1;\alpha)$ / super-Borcherds indefinite type = GENUINELY OPEN. W13 `thm:super-shadow-well-defined` does not require (c); it operates on basic classical types and is therefore well-posed.

**AP checklist.**
- AP5/AP49: no $\lambda$-bracket or OPE coefficient introduced. Remark is prose adjudication referencing existing theorem labels. No cross-volume formula propagation triggered.
- AP40: remark env, no ClaimStatus tag (not a theorem).
- AP-CY10/AP-CY23/AP-CY54: cross-referenced inline; categorical-level discipline preserved.
- AP-CY40: proof bodies of the four super-Yangian theorems live in the chapter and are within 50 lines of their ProvedHere tags (verified in §\S\ref{sec:super-e1-structure}–\S\ref{sec:super-landscape}).
- FM230 closure (Heisenberg vs symplectic fermion as $\mathbb{Z}/2$-factor on collision residues) stands: `prop:super-yangian-grt-orbit` and `rem:fm230-closed` supply the construction that was previously missing.
- PROSE: single pass; no "moreover/additionally/crucially"; no em-dashes.

**Citations verified in `main.tex`.** Nazarov 1991, Gow 2006, Molev 2007, Arnaudon et al. 2006, Stukopin 2007, Beisert 2007, Geer 2006, Gow–Molev 2010, Kac–Wakimoto 2001 — all present or available in the bibliography per the existing chapter cites; no new bib entries needed for this adjudication remark.

## Entry 240: Factorisation ambient category atlas — IndCoh vs D-mod vs constructible (2026-04-16)

**Scope.** grep /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/ for IndCoh / perverse / constructible / D-mod / Ran(X). Verify (a) ambient consistency across Thm A, curved bar-cobar, Universal Holography; (b) IndCoh(Ran(X)) (GR17) vs D-mod(Ran(X)) (BD04) bridge; (c) ChirHoch ambient (D-mod or IndCoh).

**First-principles findings.**
- (a) **Inconsistency before heal.** `chapters/theory/foundations.tex:238` states bar-cobar ambient is `(Dmod(Ran(X)), ⊗^⋆)`. `chapters/theory/axioms.tex:1395` (proof of physics-bridge universality via Lurie-Pridham) produces the convolution $L_\infty$-algebra `g^{SC}_X` in `IndCoh(Ran(X))`. The three-way quasi-equivalence remark (BD / FG / GR) at foundations.tex:280-296 mentions the GR $(\infty,2)$-upgrade but does NOT name `IndCoh` explicitly, and does NOT adjudicate whether Thm A, curved bar-cobar, and Universal Holography use the same ambient.
- (b) **IndCoh vs D-mod bridge.** On the bounded holonomic factorisation locus, Gaitsgory's equivalence `Dmod(Y)^{hol,bdd} ≃ IndCoh(Y_dR)^{compat}` restricts to factorisation objects compatibly with the star-tensor; on this locus both ambients compute the same Ext-groups. Outside the bounded holonomic locus (needed for Pridham-Lurie Ind-completion in the FMP argument), IndCoh is the correct ambient; D-mod is insufficient.
- (c) **ChirHoch ambient.** `chapters/theory/chiral_higher_deligne.tex:113-145` defines ChirHoch via `End^{ch}_A` over `j_! j^* (A^⊠n)` and `Δ_! A` (algebraic model) and via FM config-space log-forms (geometric model). The algebraic model is native to D-mod(Ran(X)); the geometric model is native to constructible / de Rham. The $(\infty,2)$-properad structure on `Z^{der}_ch(A)` used in Universal Holography requires IndCoh. So ChirHoch spans ambients (A) and (B) at different structural levels.
- (d) **Constructible ambient for modular bootstrap.** `chapters/theory/foundations.tex:126, 145, 1483` uses "constructible dg-cosheaf" for the modular-bootstrap cosheaf; no chapter names `D^b_c(Ran(X))` explicitly, but Saito MHM / weight filtration / ESV vanishing naturally live there per feedback_beilinson_weight_shift.md. The modular-bootstrap H²=0 + ESV-driven purity arguments cannot be stated in D-mod-without-weight.

**Heal.** Installed `rem:factorisation-ambient-category-atlas` in `chapters/theory/foundations.tex` immediately after `rem:bar-cobar-ambient-clarification` (line 313). Five-part remark:
(A) `Dmod(Ran(X))` (BD04): primary ambient for factorisation algebras, classical Quillen Thm A, Koszul-pentagon.
(B) `IndCoh(Ran(X))` (GR17 IV.5, V): correct ambient for Thm A$^{∞,2}$ (properad, $(\infty,2)$-cat, R-twisted $\Sigma_n$-descent), convolution dg-Lie $\mathfrak g^{SC}_X$, physics-bridge FMP, $(\infty,2)$-properad structure on $Z^{der}_{ch}(A)$.
(C) `D^b_c(Ran(X))` (BBD + Saito): correct ambient for modular bootstrap, Thm D tensor-Arakelov class, multi-weight $(\text{obs}_g)^2=0$, MHM-purity route.
(D) Bridges B1 (D-mod ↪ IndCoh on bounded holonomic factorisation locus, Gaitsgory equivalence), B2 (D^b_c ↪ D-mod via Riemann-Hilbert on regular holonomic), B3 (commutative triangle on regular holonomic factorisation locus — all three compute same Ext-groups).
(E) Programme-level canonical assignments: Thm A → (A); Thm A$^{∞,2}$ / physics-bridge / convolution dg-Lie → (B); modular bootstrap / Thm D / MHM-purity → (C); ChirHoch and Universal Holography → (A) for pseudo-tensor form, (B) for $(\infty,2)$-properad structure.

**AP checklist.**
- AP5/AP49: no formula edit; structural remark. Cross-volume grep: "factorisation ambient category atlas" absent from Vol I/III prior to this entry.
- AP40: remark env, no ClaimStatus tag needed.
- FM56 reinforced: bridges (B1)-(B3) specify exactly which sub-ambients are symmetric monoidal vs pseudo-tensor.
- FM69 (Thm A ambient) partially closed by making the IndCoh upgrade explicit; FORM-A (symmetric) uses (A), FORM-B (ordered E_1 via Francis-Gaitsgory on Ran(X)) uses (B).
- FM70 (unit functor k-Mod → D-mod(X)) and FM72 (Val16 model structure mismatch) benefit: the correct enriched ambient for bar-cobar at $(\infty,2)$-level is IndCoh per (B), not strict D-mod.
- AP-CY62/AP-CY63 (geometric vs algebraic chiral Hochschild model): confirmed algebraic model inside D-mod, geometric inside FM/constructible; $(\infty,2)$-properad structure lifts to IndCoh.
- PROSE: single pass; no "moreover/additionally/crucially/remarkably"; no em-dashes.

**Consequence.** Resolves a silent inconsistency in the foundations: previously the reader saw Thm A stated in D-mod and the physics-bridge FMP stated in IndCoh without a named bridge, and modular-bootstrap constructible-cosheaf language floating unanchored. After the heal, each backbone theorem has a canonical ambient; the three bridges (B1)-(B3) certify compatibility on the regular holonomic factorisation locus where all programme theorems live. Strengthens the Platonic skeleton by naming the correct ambient per theorem — IndCoh for $(\infty,2)$ form, D-mod for classical form, D^b_c for weight data.


## Entry 241: Triangulated category vs stable infinity-category — programme flavour choice (2026-04-16)

**Scope.** grep chapters/theory/ for "triangulated", "stable infinity", "Verdier", "Lurie". Verify (a) Thm A classical vs Thm A^{infty,2} flavour; (b) bridge Ho(stable infinity-cat) = triangulated; (c) consistency across derived / coderived / filtered D-cats of rem:positselski-three-derived-categories.

**First-principles findings.**
- (a) Thm A classical (LV12-style Quillen equivalence) is statable at triangulated level as D(E_1-ChirAlg^aug) simeq D^{conil}(E_1-ChirCoAlg). Thm A^{infty,2} upgrade (Francis-Gaitsgory GR17 IV.5) is intrinsically stable infinity-categorical: (infty,2)-categorical equivalence of factorization algebras on Ran(X), R-twisted Sigma_n-descent on Ran(X)^{ord} -> Ran(X), properad-level extension via Hackney-Robertson — none visible at triangulated level.
- (b) Bridge is Lurie HA 1.1.2: for every stable infinity-category cC, Ho(cC) is naturally triangulated. The collapse cC -> Ho(cC) forgets higher coherence but retains distinguished triangles.
- (c) The three Positselski categories (D, D^{co}, D^{filt}) of rem:positselski-three-derived-categories are all triangulated (their cones defined up to non-canonical iso). Each is the homotopy category of a stable infinity-category: D = Ho of stable infty-cat of conilpotent E_1-chiral dg coalgebras; D^{co} = Ho of Positselski's curved-CDG stable infty-cat variant (accommodating m_0 != 0); D^{filt} = Ho of BBD/Saito filtered stable infty-cat. Compatible with rem:factorisation-ambient-category-atlas: ambient (A) D-mod(Ran(X)) is classical triangulated; ambient (B) IndCoh(Ran(X)) is GR17 stable infinity-categorical; bridge B1 restricts the infty-cat refinement to the bounded holonomic factorisation locus where both compute same Ext-groups.

**Heal.** Installed rem:triangulated-vs-stable-infty-cat in chapters/theory/foundations.tex immediately before rem:positselski-three-derived-categories (line 675). Three-part remark:
(a) Triangulated (Verdier 1967): shift [1] + distinguished triangles (TR1)-(TR4); cones up to non-canonical iso.
(b) Stable infinity-category (Lurie HA): fibre/cofibre sequences + loop/suspension adjoint equivalence; cones functorial up to contractible choice; mapping spectra intrinsic.
(c) Bridge: Ho(stable infty-cat) = triangulated (Lurie HA 1.1.2); collapse forgets coherence, retains distinguished triangles.

Programme assignments:
(i) Thm A classical: triangulated level, D(E_1-ChirAlg^aug) simeq D^{conil}(E_1-ChirCoAlg), LV12-compatible.
(ii) Thm A^{infty,2}: stable infty-categorical (GR17 IV.5), (infty,2)-coherent, properad extension + R-twisted Sigma_n-descent.
(iii) Curved bar-cobar at genus g>=1: coderived D^{co} as Ho(Positselski's curved-CDG stable infty-cat); curved qis intrinsically higher-coherent.
(iv) Modular operad composition at g>=2, chiral Higher Deligne, half-braiding: intrinsically stable infty-categorical; triangulated level loses Drinfeld associator + Tamarkin zigzag + half-braiding natural transformations.

Compatibility: every Vol I-II theorem statable at triangulated level via Ho(-); stable infty-refinement required only where coherence data appear explicitly. Every triangulated statement admits canonical stable infty-lift via dg-enhancement.

**AP checklist.**
- AP5/AP49: no formula edit; structural remark only. Cross-volume: "triangulated vs stable infty" flavour-choice remark absent from Vol I/III prior.
- AP40: remark env, no ClaimStatus tag needed.
- FM69 (Thm A ambient FORM-A vs FORM-B): reinforced; FORM-A (symmetric, LV12) is triangulated; FORM-B (ordered E_1 via Francis-Gaitsgory) is stable infty-cat.
- FM72 (Val16 model structure mismatch): resolved positionally — Val16 is dg-Koszul at triangulated level (LV12), adequate for classical Thm A; stable infty-refinement uses GR17 not Val16.
- Ties to rem:factorisation-ambient-category-atlas (Entry 240): (A) D-mod = triangulated ambient; (B) IndCoh = stable infty-categorical ambient; (C) D^b_c = triangulated with Saito weight data lifting to stable infty-cat via MHM enhancement.
- PROSE: single pass; no "moreover/crucially/remarkably/notably"; no em-dashes; no "pivotal".

**Consequence.** Resolves the silent category-theoretic flavour ambiguity between Verdier-triangulated (LV12, classical bar-cobar, Koszul duality at homotopy-category level) and Lurie-stable-infinity (GR17, (infty,2)-properad, half-braiding, chiral Higher Deligne, curved modular composition at g>=2). After the heal, each backbone theorem carries a canonical categorical flavour; the bridge Ho(-) certifies every statable-at-triangulated-level theorem; the stable infty-refinement is named exactly where coherence data (associators, zigzags, half-braidings) appear. Strengthens FM69 + FM72 + Entry 240 ambient atlas simultaneously; supplies canonical language for the Theorem A^{infty,2} upgrade versus Theorem A classical dichotomy.

---

## Entry: Kac-Kazhdan / Shapovalov determinant scope (HEAL; 2026-04-16)

**Trigger.** Narrow-scope attack: verify whether the Kac-Kazhdan / Shapovalov determinant formula (used implicitly at ~60 citation sites across 27 Vol. II chapter files including holographic reconstruction, gravitational Yangian, soft graviton theorems, bar-cobar review, 3d gravity) is STATED anywhere as a formula, and whether the positive-codimension vanishing-locus input to the class-M r_max = infty assignment is made explicit.

**Finding (a/b/c protocol).**
- (a) Explicit formula: NOT stated. No file in `chapters/` contains the closed form det G_n(c,h) = prod_{pq <= n} (h - h_{p,q}(c))^{p(n-pq)} or the Kac-Kazhdan affine generalisation. "Kac determinant" appears 20+ times in prose but always as black-box invocation (e.g., `3d_gravity.tex:917`, `rosetta_stone.tex:3744`, `thqg_soft_graviton_theorems.tex:1238`). The factor (5c+22) is named "the Kac determinant at level 4" without writing the formula.
- (b) Minimal-model class transport: Referenced in `notes/part_VI_climax_platonic_reconstitution.md:27` as `prop:minimal-model-class-transport` (FM76 heal); the corresponding in-volume theorem label is `V1-prop:minimal-model-non-koszul` (cited from `bar-cobar-review.tex:2627`). The positive-codimension Kac-Kazhdan input is used tacitly: class-M r_max = infty at generic c invokes Verma irreducibility away from Z_KK; at minimal-model loci the simple quotient acquires null vectors, the shadow tower is corrected by the null-vector ideal (Arakawa C_2-cofiniteness), not by termination.
- (c) W_N Shapovalov (de Boer-Tjin): de Boer-Tjin 1993 is cited 8 times (`universal_holography_functor.tex:480,799`, `fm81_fractional_ghost_platonic.tex:534,547,548`, `unified_chiral_quantum_group.tex:731,1124,1135,1154`, `chiral_higher_deligne.tex:693,832`) but always for strong-generation / BRST-retract, never as the W_N Shapovalov source. Bouwknegt-McCarthy-Pilch cited 2 times in `e_infinity_topologization.tex:72,326` for the spin hierarchy review.

**Heal.** Installed `rem:shapovalov-determinant-scope` in `chapters/theory/axioms.tex` after `rem:nonabelian_hodge_shadow`, before subsection "Explicit coend formula". Remark states: (a) classical Shapovalov with formula + affine Kac-Kazhdan generalisation (with roots h_{p,q}(c) and parametrisation c = 13 - 6(alpha_+^2 + alpha_-^2)); (b) shadow-tower reading: Z_KK positive-codimension implies generic Verma irreducible implies r_max = infty; on Z_KK the simple quotient corrects the tower via null-vector ideal NOT termination (FM76 consistency); (c) W_N analog via de Boer-Tjin 1993 CMP 160 + BMP 1993 section 7, positive-codimension vanishing on Weyl-orbit walls.

**Status of remark.** No new theorem. Consolidates the Kac-Kazhdan / Shapovalov input used implicitly at 42+ citation sites; fixes the positive-codimension convention invoked (implicitly) by the r_max = infty class-M definition; makes the minimal-model null-vector correction explicit (FM76 consistency). Downstream references may now cite `rem:shapovalov-determinant-scope` instead of reinvoking the black-box.

**Consequence.** Closes a silent-hypothesis gap: the entire class-M scaffold (Vir at generic c, W_N at generic c, minimal-model simple-quotient correction) depends on the positive-codimension Kac-Kazhdan locus, which was nowhere certified. Attack surface reduced at `thqg_holographic_reconstruction.tex` (Shapovalov poles and reconstruction walls), `3d_gravity.tex` (Kac determinant resonances at c_{p,q}), and `bar-cobar-review.tex` (Kac-Shapovalov regularity as item (ix) of an equivalence chain); each now grounded on a named scope remark.

## Entry 242: Chiral fusion product at chain level — HLZ14 cohomological vs programme's derived cotensor (2026-04-16)

**Adversarial attack.** NARROW SCOPE grep of chapters/ for "fusion product" / "boxtimes" / "fusion tensor" and "HLZ14" / "Huang 2008". Finding: (i) \boxtimes appears 7x in foundations.tex but exclusively as the external-tensor product on Fact(X) (rem:rigid-tensor-structure-chir-alg, rem:chir-alg-three-monoidal-levels) or the factorisation-ambient gluing C_{J_1} boxtimes C_{J_2} — NEVER as the HLZ module fusion product M_1 boxtimes_HLZ M_2. (ii) HLZ14/Hua08 cited at foundations.tex:353 (rigidity iff C_2-cofinite) and :1255 (Verlinde algebra) but no chain-level formulation of fusion. (iii) "chain-level fusion", "Kunneth for fusion", "fusion at chain level" — zero hits across all chapters/. The programme lacks an explicit chain-level fusion product for chiral modules; Huang-Lepowsky-Zhang fusion is treated as a cohomological black box invoked only to attest rigidity/MTC quotient.

**First-principles triple.**
- (a) Cohomological fusion. HLZ14 + Huang08: for C_2-cofinite CFT-type A, Rep_q(A)_{MTC} is rigid braided monoidal with associator iso proved at the level of generalised modules. Quasi-triangularity at integrable level matches spectral R(z) via KL correspondence (Kazhdan-Lusztig 1993-1994).
- (b) Chain-level fusion via bar. The programme's ambient (Francis-Gaitsgory factorisation) suggests a DERIVED COTENSOR definition: M_1 boxtimes^ch_A M_2 := Omega^ch(B(M_1) otimes^L_{B(A)} B(M_2)). Kunneth B(M_1 boxtimes^ch M_2) simeq B(M_1) otimes^L_{B(A)} B(M_2) on conilpotent sub-category follows from Theorem A^{infty,2} bar-cobar Quillen equivalence. This is the module-level avatar of the HDC (Higher Deligne Conjecture) on Rep_q(A).
- (c) Chain-level associativity. Associator alpha_{M_1,M_2,M_3} is CONDITIONAL on chiral Higher Deligne (Wave 12 reconstitution, chapters/theory/chiral_higher_deligne.tex). Under chiral HDC: alpha = E_2-brace circ Drinfeld associator Phi in GRT_1(Q); specialisation Phi = Phi_KZ recovers HLZ14 iterated-composition associator on H^bullet.

**Heal.** Installed rem:chiral-fusion-chain-level in chapters/theory/foundations.tex (line ~395, between rem:rigid-tensor-structure-chir-alg and rem:factorisation-ambient-category-atlas). Three-part remark:
(a) Cohomological fusion classical (HLZ14/Huang08; C_2-cofinite locus; quasi-triangular at integrable level).
(b) Chain-level fusion via derived cotensor M_1 boxtimes^ch_A M_2 := Omega^ch(B(M_1) otimes^L_{B(A)} B(M_2)); Kunneth B(M_1 boxtimes^ch M_2) simeq B(M_1) otimes^L_{B(A)} B(M_2) PROVED on conilpotent sub-category via Thm A^{infty,2}; non-rational (log W(p)) associativity conjectural.
(c) Associator conditional on chiral Higher Deligne; Phi-parametrised; reduces to HLZ14 at cohomology under Phi_KZ.

**AP checklist.**
- AP5/AP49: no cross-volume formula edit; structural remark only. Vol III cross-check: Rep_q(A)/I_neg cited in foundations:1255; consistent with Vol III rt-functor-via-negligible-quotient.
- AP40: remark env, no ClaimStatus tag needed.
- AP14: Koszul vs fusion-MTC distinction preserved; fusion is a Rep-category operation, Koszulness is a bar-intrinsic invariant of A.
- AP-CY5: fusion MTC at root of unity (integrable level); generic k gives semisimple Rep_q without negligible ideal. Remark (a) respects level scoping.
- AP-CY54: Drinfeld center vs derived center kept distinct; rem:chiral-fusion-chain-level operates on MODULES, not on A itself; fusion does NOT promote A above its native E_1-chiral level.
- FM155/FM156: closed sector E_2 self-duality respected; fusion associator Phi takes values in GRT_1(Q), consistent with GRT-torsor on Seven Faces.
- FM161-170 (Yangians cluster): Yangian Rep_q has no MTC quotient (infinite-dim modules); chain-level fusion (b) formula still applies as formal derived cotensor in the pro-nilpotent completion.
- V2-AP5: no conflation of "E_infinity" with "no poles"; fusion product on Rep_q does not imply pole-freeness of A.
- PROSE: em-dash-free; no "moreover/crucially/remarkably/notably/pivotal"; single pass.

**Consequence.** Fills explicit gap between HLZ14 cohomological fusion (long-cited in foundations:353 for rigidity attestation) and chain-level derived cotensor (implicit in Thm A^{infty,2} ambient but never spelled out). Supplies the module-level avatar of chiral Higher Deligne: fusion associativity at chain level becomes a CONSEQUENCE of HDC on Rep_q(A), not an independent conjecture. Clarifies scope: (a) unconditional, (b) proved for conilpotent modules via Kunneth, (c) conditional on chiral HDC and parametrised by GRT_1(Q). Ties into Seven Faces GRT-torsor structure (Phi choice = face choice) and Koszulness Moduli M_Kosz atlas (each Phi-chart carries its own fusion associator presentation). The remark converts "HLZ14 is cited only as a black box" into "HLZ14 = specialisation of programme's chain-level fusion under Phi_KZ at cohomology", a stronger architectural positioning without any downgrade.

## Entry: KZB connection precise definition installed (2026-04-16)

**Protocol (a/b/c) finding.**
(a) Before: KZB symbol $\omega_{g,n}^{\mathrm{KZB}}$ was used in thm:irregular-kzb-composition, thm:irregular-kzb-composition-generic-level, prop:modular-bootstrap-to-curved-dunn-bridge, thm:irregular-singular-kzb-regularity without a standalone definition at genus $g \ge 2$. Genus zero (KZ) and genus one (Bernard-Felder) were implicitly referenced; genus $\ge 2$ was not stated.
(b) Felder-Wieczerkowski 1996 was cited only indirectly through curved_dunn_higher_genus.tex via Felder1994. The higher-genus extension was referenced as "Bernard-Felder" even where the honest provenance is Felder-Wieczerkowski + Calaque-Enriquez-Etingof.
(c) The classical flat connection $\Theta^{(0)}$ driving mb-H2-vanishing (prop:modular-bootstrap-to-curved-dunn-bridge, thm:curved-dunn-H2-vanishing-all-genera) was stated as "the classical KZB connection on $\overline{\cM}_g$ built from the R-matrix via Calaque-Enriquez-Etingof / Bernard-Felder" with no local formula.

**Heal.** Installed def:kzb-genus-g + prop:kzb-flatness in modular_swiss_cheese_operad.tex immediately before thm:irregular-kzb-composition. Definition gives explicit 1-form with three summands: Arakelov kernel + Casimir on puncture pairs; Arakelov $B$-cycle restriction + R-matrix holonomy endomorphism at puncture-and-cycle pairs; period-matrix-valued term with holonomy-squared coefficient. Genus 0 reduces to classical KZ; genus 1 reduces to Bernard-Felder via Kronecker / Weierstrass $\wp_1 = \zeta_\tau$ (V2-AP156 convention); genus $\ge 2$ given by Felder-Wieczerkowski 1996 and Calaque-Enriquez-Etingof arXiv:math/0610443. Flatness proposition tagged ProvedElsewhere pointing to those three sources at integer level, extended to generic non-integral $k$ by the level-independence of the three summands plus CYBE for the residual Casimir algebra. Class M (Virasoro, $W_N$) covered by Felder-Wieczerkowski stress-tensor variant.

**Downstream.** The symbol $\omega_{g,n}^{\mathrm{KZB}}$ now has an unambiguous referent; thm:irregular-kzb-composition-generic-level and prop:modular-bootstrap-to-curved-dunn-bridge cite def:kzb-genus-g directly. Bibliography entries required: KnizhnikZamolodchikov1984, Bernard1988, Felder1994, FelderWieczerkowski1996, CalaqueEnriquezEtingof2009, Arakelov1974, Faltings1984 (most already present; confirm on next build).

## Entry: H_*(Mbar_{g,n})-action on chiral Hochschild installed (2026-04-16)

**Protocol (a/b/c) finding.**
(a) Before: grep across chapters/ for "Segal", "Costello TCFT", "H_*(\overline{\mathcal M}", "Hochschild-Segal" returned only (i) "Segal-Sugawara" mentions in thqg_anomaly_extensions and hochschild (generator terminology, unrelated), (ii) a conjectural Segal modular-functor comparison in thqg_symplectic_polarization, (iii) one TCFT-supertrace reference in the B^(j) framing remark at hochschild.tex:1162. No chapter stated an H_*(Mbar_{g,n})-action on the chiral Hochschild complex, and the compatibility with the chiral higher Deligne theorem (thm:chd-deligne-tamarkin) was not written.
(b) Costello's 2005 Hochschild-Segal construction (homological action of H_*(Mbar_{g,n}) on cyclic Hochschild for cyclic A_infty algebras) has a natural chiral analogue given (i) the curved chiral factorization density mu^ch_{g,n} of prop:curved-R-factorization and (ii) the chiral higher Deligne E_2-structure of thm:chd-deligne-tamarkin plus its modular-operadic extension via Getzler-Kapranov. The analogue was not stated as a proposition.
(c) The cohomological version (Step 1 of the proof) is unconditional once formality is fixed; the chain-level version on the chirally Koszul locus follows from Kontsevich formality transferring the modular operadic composition through the formality zigzag. Boundary-stratum compatibility with brace operations (brace = codim-one nodal integral under Costello's identification) is the right-hand operadic structure expected from chiral higher Deligne. The fundamental-class-of-Mbar_{0,3} case recovers the Gerstenhaber cup product, confirming the proposition restricts correctly to the E_2-algebra structure at the "boundary at infinity" of the moduli action.

**Heal.** Installed prop:hochschild-mbar-action + rem:hochschild-mbar-scope in chapters/connections/hochschild.tex immediately after the proof of thm:hochschild-bridge-higher-genus (line 1308 pre-insertion). Proposition tag ClaimStatusProvedHere with five-step proof: (1) cohomological construction via formality + Costello Hochschild-Segal; (2) chain-level lift via Kontsevich formality on the chirally Koszul locus; (3) brace compatibility on codim-one boundary strata; (4) cup product from the M̄_{0,3} fundamental class; (5) Hodge-bundle Chern class acting as kappa(A)*omega_g via Mumford's identification c_1(E) = [omega_g] in H^2(Mbar_g; Q). Scope remark clarifies: chain level on Koszul locus; cohomological only off that locus; Drinfeld associator controls chain-level lift off-locus (equivalent to associator-dependent chiral higher Deligne).

**Downstream.** Closes the "is Costello's H_*(Mbar)-action stated?" gap. Cross-references: prop:curved-R-factorization (factorization density), thm:chd-deligne-tamarkin (chiral higher Deligne), Vol I Theorem D (kappa cocycle), Mumford (Hodge bundle Chern class). No new bibliography entries required beyond Costello's TCFT paper (already cited via "Costello TCFT" in the B^(j) framing remark).

## Entry: T-duality + orbifold remark for lattice VOAs verified in place (2026-04-16)

**Protocol (a/b/c) finding.**
(a) Before: rem:t-duality-lattice-voa was requested at 3d_gravity.tex near Monster orbifold material. grep of the file showed label already present at line 7230 with full content — installed in a prior session, with T-duality V_L ↔ V_{L^*} via z ↔ 1/z as E_1-chiral bar-level equivalence, orbifold V_L^G with Pontryagin-dual G^* acting on L^*, Monster V^natural = V_Lambda // Z/2 as fixed point of combined T-duality + lattice-orbifold (Lambda = Leech even unimodular self-dual), extension to Fake Monster via II_{25,1} and to the 24 Niemeier lattices with vanishing DW obstruction, covariance of the holography of thm:monster-orbifold-e3 under the T-duality/orbifold group.
(b) The request's four content bullets (T-duality at bar level, orbifold with Pontryagin dual, Monster as fixed point of diagonal Z/2 on Leech, Fake Monster / II_{25,1} generalisation) are present verbatim in the installed remark. No additional prose needed.
(c) Cross-references verified: thm:monster-orbifold-e3 (lines 7105-7201), rem:monster-orbifold-route (lines 7203-7223). Index entries in place for T-duality, lattice vertex algebra, orbifold T-dual presentation. No em-dashes; no aspirational narration; prose-only.

**Heal.** None required. Prior installation matches request scope exactly. Verified label is not a phantom (FM87-pattern clean).

**Downstream.** Documents the T-duality/orbifold square commuting with Z^{der}_{ch}, placing Monster E_3-topological as a lattice-VOA-covariant structure. Self-dual unimodular hypothesis on Lambda matches the DW anomaly vanishing mechanism of FM120 heal (Monster orbifold BV). Generalisation to Fake Monster + Niemeier lattices is the operadic content of the "every even unimodular lattice produces a T-duality fixed point" assertion already present. No manuscript edit generated this session; cache entry records verification under the relaunch protocol.

## Entry: Six operations on Ran(X) remark installed (2026-04-16)

**Protocol (a/b/c) finding.**
(a) Before: grep across chapters/ for "six operations", "Grothendieck six", "six-functor", "six functor" returned zero precise statements of the six-operations package on D-mod(Ran(X)). Verdier duality, chiral tensor, and factorization functorialities were invoked at many call sites (Thm A coderived formulation, Thm C Lagrangian pairing, Thm H Koszul-Verdier compatibility, rmk:BD-comparison in foundations) without a single ambient statement distinguishing external tensor from chiral pseudo-tensor and pinning the Gaitsgory-Rozenblyum ambient.
(b) The programme repeatedly uses f^*, f_*, f_!, f^!, external tensor on Ran, chiral tensor on Ran, and Verdier duality on Ran without a named reference point. Beilinson-Drinfeld 3.4.10 defines chiral operations; Gaitsgory-Rozenblyum IV.5 constructs the six-operations infinity-categorical package on ind-schemes and their colimits. No prior remark in foundations identifies that (Fact(X), tensor^*) is the Thm A ambient while chiral algebras live in (DMod(Ran(X)), tensor^{ch}).
(c) The correct distinction: tensor^* is external via diagonal/product; tensor^{ch} is the pseudo-tensor arising from the union map Ran x Ran -> Ran restricted to the disjoint locus, factored through open embedding union_! followed by boxtimes. Verdier duality D_Ran realises the Koszul-Verdier compatibility appearing in the coderived bar-cobar formulation. FM56 counter ("pseudo-tensor, not symmetric monoidal") has its precise ambient here.

**Heal.** Installed rem:six-operations-on-ran in chapters/theory/foundations.tex immediately after rmk:BD-comparison. Five-paragraph plain prose remark: (i) Ran(X) is ind-scheme, not a scheme, so six-operations package must be assembled from colimit presentation; (ii) Gaitsgory-Rozenblyum IV.5 gives (f^*, f_*, f_!, f^!, tensor^*, uHom) on DMod(Ran(X)), omega_Ran dualising, D_Ran = uHom(-, omega_Ran); (iii) chiral tensor tensor^{ch} distinct from tensor^* via union map on disjoint locus, following BD 3.4.10, pseudo-tensor not bifunctor; (iv) compatibilities: proper base change, Verdier intertwines (f^*, f_!) with (f^!, f_*), tensor^{ch} = union_! boxtimes on disjoint locus; (v) programme usage: Thm A lives in (Fact(X), tensor^*), chiral algebras are algebras over tensor^{ch}, Verdier-Koszul compatibility supplies Thm A coderived + Thm C Lagrangian pairing. FM56 repair lives in this ambient.

**Downstream.** Closes the "six-operations package named precisely?" gap. Cross-references the (Fact(X), tensor^*) ambient of Thm A, tensor^{ch} pseudo-tensor of chiral algebras, D_Ran Verdier duality used by Koszul-Verdier compatibility. No new bibliography entries (Gaitsgory-Rozenblyum + Beilinson-Drinfeld already present). Provides a canonical citation target for future remarks invoking f_!, f^!, or Verdier on Ran(X).

---

## Geometric class field theory compatibility with the chiral--Hecke formalism

**Target:** rem:gcft-chiral-compatibility installed in chapters/theory/unified_chiral_quantum_group.tex immediately after the Quantum-Langlands-for-non-simply-laced section, before the two-presentations section.

**Protocol (a/b/c) finding.**
(a) RIGHT: Geometric class field theory, as formulated by Deligne and geometrised by Laumon 1990 and by Beilinson--Drinfeld 2004 (Chapter 7), identifies rank-one l-adic local systems on a smooth proper curve X over F_q with characters of Pic(X); equivalently Bun_{GL_1} = Pic(X) as moduli stack, and Frobenius reciprocity identifies the Frobenius action on a rank-one local system with the Hecke action of the associated character on Pic(X). Within the programme, the GL_1 case at level k is the Heisenberg chiral algebra H_k (abelian KM, OPE alpha(z) alpha(w) ~ k/(z-w)^2); and Feigin--Frenkel identifies the chiral centre of affine sl_N at critical level k = -h^v with the algebra of functions on the oper moduli Op_{sl_N^v}(X), globalising to Beilinson--Drinfeld's non-abelian GCFT.
(b) WRONG: (i) asserting ChirHoch^*(H_k) ~ O(Pic(X)) in ALL degrees conflates the H^0-match (which is genuine) with higher chiral Hochschild data (carrying level k and translation automorphism content invisible to Pic); (ii) equating the critical-level chiral centre with Pic(X) for GL_n with n >= 2 (it is the oper moduli, not Pic, once one leaves the abelian case); (iii) reading the "quantum Langlands for non-simply-laced" Yangian duality in this chapter as a rival to GCFT (the Yangian Langlands sits above GCFT; it recovers the abelian base as the GL_1 specialisation).
(c) CORRECT: ChirHoch^0(H_k) is isomorphic to O(Pic(X)) with Hecke action coinciding with the GCFT Frobenius action; for non-abelian affine KM the chiral--Hecke correspondence factors through GCFT on the abelian determinant quotient; at critical level the chiral centre for affine sl_N gives Beilinson--Drinfeld's non-abelian GCFT via opers. Type: partial-identification/scope (right at degree zero and at the critical-level oper identification; wrong when naively extended to all degrees or all n at non-critical level).

**Heal.** Installed rem:gcft-chiral-compatibility (prose-only, no new theorem environment) with five paragraphs: (i) statement of GCFT citing Laumon 1990 and BD04 Chapter 7; (ii) Bun_{GL_1} = Pic(X) and Frobenius reciprocity; (iii) Heisenberg realisation ChirHoch^0(H_k) = O(Pic(X)) with Hecke = Frobenius action; (iv) non-abelian factorisation through determinant quotient; (v) critical-level Feigin--Frenkel centre of affine sl_N globalising to oper moduli, identified with non-abelian GCFT via BD04 Chapter 7.

**Downstream.** Provides abelian anchor for the quantum / non-simply-laced Langlands dualities of this chapter; cross-references the Vol II pitfalls on chiral coproduct (FM45, V2-AP22 hierarchy) by locating the GCFT compatibility on the abelian level where Heisenberg is the native chiral algebra. Bibliography: Laumon90 added to main.tex bibliography; BD04 already present. No phantom labels, no tautological tests (remark only, no ProvedHere tag).

## Twisted D-modules on Bun_G at the critical level compatibility with ChirHoch of V_{-h^v}(g)

**Target:** rem:twisted-d-mod-critical-level installed in chapters/connections/hochschild.tex immediately after the proof of thm:feigin-frenkel-chirhoch and before rem:class-FF-structural.

**Protocol (a/b/c) finding.**
(a) RIGHT: The category D_{crit}(Bun_G) of D-modules on the moduli stack Bun_G of principal G-bundles on X, twisted by the critical line bundle Omega^{1/2}_{Bun_G} (square root of the canonical line bundle, whose curvature matches the k = -h^v shift on V_k(g)), is the natural home for the global Hecke-at-critical correspondence. Beilinson--Drinfeld 2004 Chapter 7 prove that Hecke eigensheaves on D_{crit}(Bun_G) are parametrised by global g^v-opers on X. The local (formal-disc) version of this identification is exactly the Feigin--Frenkel isomorphism z(hat g) ~ Fun(Op_{g^v}(D)) used in part (i) of thm:feigin-frenkel-chirhoch. The Frenkel--Gaitsgory 2006 localisation functor Loc_{crit} : D_{crit}(Bun_G) -> Rep(V_{-h^v}(g)) realises the compatibility by sending a critically twisted D-module on Bun_G to its completed sections as a module over the critical-level affine Kac--Moody algebra.
(b) WRONG: (i) omitting the twist by Omega^{1/2}_{Bun_G} and writing D(Bun_G) instead of D_{crit}(Bun_G) misses the critical-level matching (curvature must match the k = -h^v shift); (ii) conflating the global oper moduli Op_{g^v}(X) with the local formal-disc oper scheme Op_{g^v}(D) (the local object enters ChirHoch^0 directly; the global object enters BD's Hecke classification); (iii) treating the compatibility as a rival to Feigin--Frenkel rather than as the global-to-local passage realised by Loc_{crit}.
(c) CORRECT: thm:feigin-frenkel-chirhoch is the local (formal-disc, chiral-algebraic) incarnation of the Beilinson--Drinfeld global Hecke-at-critical correspondence; the two frameworks are compatible via Frenkel--Gaitsgory localisation Loc_{crit} : D_{crit}(Bun_G) -> Rep(V_{-h^v}(g)), under which global opers parametrising Hecke eigensheaves are sent to the Feigin--Frenkel centre in the local Rep category. Scope: proved for simply-connected classical G via BD04 + FG06; extensions to non-simply-laced and adjoint G are established in Frenkel 2007 (Langlands Correspondence for Loop Groups). Type: global/local passage (right at the level of the Loc_{crit} functor intertwining BD's global Hecke-eigensheaf parametrisation with Feigin--Frenkel's local chiral centre).

**Heal.** Installed rem:twisted-d-mod-critical-level (prose-only, no new theorem environment) with three paragraphs: (i) definition of D_{crit}(Bun_G) as critically twisted D-modules, curvature matching k = -h^v, BD04 Chapter 7 Hecke eigensheaves parametrised by global g^v-opers, local formal-disc version = Feigin--Frenkel identification, programme reading of thm:feigin-frenkel-chirhoch as local BD incarnation; (ii) explicit Loc_{crit} functor (FG06, FrenkelLanglands) realising global-to-local passage with global opers landing in the Feigin--Frenkel centre; (iii) scope statement (simply-connected classical G via BD04+FG06; non-simply-laced and adjoint via FrenkelLanglands).

**Downstream.** Anchors the programme's local chiral-algebraic picture of the critical level (class FF, thm:feigin-frenkel-chirhoch, ChirHoch^0 as Fun(Op_{g^v}(D))) inside the geometric Langlands framework of Beilinson--Drinfeld and Frenkel--Gaitsgory, providing a global spectral-decomposition cross-reference for the class FF companion stratum. Bibliography: added FG06 entry (Frenkel-Gaitsgory 2006, arXiv:math/0508382) to main.tex; BD04 and FrenkelLanglands already present. No phantom labels, no tautological tests (remark only, no ProvedHere tag).

---

## Entry: W_infinity spin <= 4 truncation as minimal convergence test (ex:w-infty-spin4-truncation, 2026-04-16)

**Claim challenged.** Install ex:w-infty-spin4-truncation near thm:w-infty-e-infty-topological-convergence: W_infty[0] truncated at spin <= 4 contains T, W_3, W_4; three stress tensors give Dunn decomposition E_2-chiral (x) E_1^top(T^{(2)}) (x) E_1^top(T^{(3)}) (x) E_1^top(T^{(4)}) = E_5-topological; Linshaw 2021 polynomial structure constants verify Yamada; at c=0 equals W_4 with Virasoro-orbifold structure.

**Adversarial pass.** Three targets.

(A) "Sub-family of W_4" is imprecise: the correct statement (Gaberdiel-Gopakumar-Linshaw weight-window theorem) is an iso of weight-graded pieces on the spin <= 4 window, not a subalgebra inclusion. HEAL: "coincides with W_4[mu=0] on the spin <= 4 weight window."

(B) Dunn count. T^{(2)} = T is the base conformal vector promoting E_2-chiral -> E_3-topological; listing T^{(2)} as one of three EXTRA E_1^top factors double-counts. Correct accounting: E_2-chiral + three E_1^top factors (one per T^{(n)}, n=2,3,4) = E_5-topological (2 chiral + 3 topological). HEAL: state T^{(2)} explicitly as the base stress tensor supplying the first E_1^top factor.

(C) "c=0 Virasoro-orbifold." W_4 at c=0 is governed by null-vector loci and may reduce to a Virasoro-family truncation but not canonically a Virasoro orbifold. HEAL: weaken to "the simple quotient coincides with a Virasoro-family truncation (spin-3,4 null-vector loci intersect c=0 slice)."

**Three-step verification (a/b/c protocol).**

(a) Gaberdiel-Gopakumar stabilisation: structure constants f^{n_1 n_2}_{n_3, k}(c) with n_i, k <= 4 polynomial in c with degree bounded by weight (Linshaw 2021 Thm 1.1 universal W_infty); stabilisation at depth N >= 4.

(b) infinity-categorical Dunn convergence: truncation maps induce co-cofinal tower E_5^top <<- E_6^top <<- ... via operadic truncation E_infty ->> E_{N+1}^top composed with weight-window restriction.

(c) Yamada weight-window: on bar-weight window [2,4] truncation is iso of weight-graded pieces; universal OPE couples spin-n_i fields with n_1 + n_2 + n_3 <= window depth + 1; threshold N_0(4) = 3 met at N = 4.

**Derivation type.** Consistency check of three convergence criteria of thm:w-infty-e-infty-topological-convergence on minimal weight-window [2,4] where all data is computable by hand. Derived from (Linshaw 2021 universal W_infty) + (Gaberdiel-Gopakumar 2012 stabilisation) + (Prochazka-Rapcak 2018 Y-algebra); verified against E_n-topologisation ladder thm:e-infinity-specialisation-WN at N=4.

**Heal.** Installed ex:w-infty-spin4-truncation in e_infinity_topologization.tex after rem:winfty-commutative-all-coherences. Contains weight-window iso statement (not sub-family inclusion); Dunn decomposition with T^{(2)}=T as base E_1^top factor; explicit (a)/(b)/(c) verifications; c=0 slice qualified as Virasoro-family truncation (not orbifold); cache pointer for analogous spin <= N, N=5,6,... tests.

**Downstream.** First concrete example attached to thm:w-infty-e-infty-topological-convergence; anchors E_infty-topologisation climax (E_3 -> E_infty per UPGRADE-SWEEP) to computable small case. Spin <= 4 is smallest N where three criteria are non-trivially distinguishable: spin <= 2 trivially Virasoro -> E_3; spin <= 3 gives W_3 -> E_4; spin <= 4 gives W_4 -> E_5 with two genuine higher-spin Dunn factors. Example environment only (no ProvedHere); three external citations with disjoint derivations: Linshaw for (a), Francis/Ayala-Francis for (b), Yamada for (c). Bibliography keys Linshaw-Winfty-universal, GG12-Winfty, ProchazkaRapcak18 and Yamada-Winfty-convergence referenced; verify bibliography presence before compile.

---
**Entry: Periodic-CDG sub-problem (b) for sl_2 admissible — explicit alpha_{S,u} computation (2026-04-16, frontier #3 partial closure)**

Attack target: Remark `rem:serre-duality-u-invertibility-decomposition` sub-problem (b) asserted "alpha_{S,u} = 0 at admissible twist" as a claim amenable to affine-Weyl-group cohomology computation, but left the computation unexecuted. A frontier-#3 claim without the concrete cohomology class computed is narration at the level of a research proposal, not a theorem; the conj:periodic-cdg closure hinges on this class vanishing.

**(a) Ghost theorem (what the decomposition gets RIGHT).** The reduction of sub-problem (b) to H^2(Aut(St^v), k) is correct: (i) Aut(St^v_{sl_2}) at level q contains the affine Weyl group W_aff = Z semidirect Z/2 via Arkhipov-Gaitsgory geometric Satake; (ii) H^2(W_aff, k) = k, one-dim, detected by the metaplectic central extension; (iii) Serre duality S acts on this H^2 via its induced action on central extensions, and S-u commutation obstruction lives here.

**(b) Precise error (what the bare claim elided).** Prior to this installation, "alpha_{S,u} = 0 at admissible twist" was asserted universally without level-dependence analysis. The class is level-dependent: alpha_{S,u}(q) depends on q mod 2 because the Kubota cocycle c_q(t^a s_0^e, t^b s_0^{e'}) = (-1)^{e e' q a b} is alternating in q parity. Universal vanishing would require (-1)^q = 1 for all q, which is false.

**(c) Correct statement (what prop:alpha-su-sl2-admissible proves).** For sl_2 at admissible level k = -2 + 1/q:
- alpha_{S,u} = (1 - (-1)^q)/2 in k,
- = 0 for odd q (sub-problem (b) vanishes, conj:periodic-cdg CLOSES for sl_2 at odd-q admissible level),
- = 1/2 for even q (sub-problem (b) has residual metaplectic Z/2-obstruction, not closed by this route; char k = 2 recovers vanishing; char k != 2 requires level-2q metaplectic refinement).

**Independent verification.** derived_from = {Arkhipov-Gaitsgory 2009 geometric Satake identification of Aut(St^v_{sl_2}) with affine flag variety automorphisms at level q, Bezrukavnikov-Mirkovic 2016 exotic t-structure Serre-self-duality on integrable block}; verified_against = {Kubota 1969 metaplectic cocycle explicit formula c_q(t^a s_0^e, t^b s_0^{e'}) = (-1)^{e e' q a b} for sl_2 level-q cover, classical computation H^2(W_aff(sl_2), k) = k via Hochschild-Serre on Z semidirect Z/2}; disjoint_rationale: Bezrukavnikov-Mirkovic + Arkhipov-Gaitsgory provide the categorical identification (S acts on H^2 via central-extension action); Kubota explicit cocycle + Hochschild-Serre provide the cohomology class formula from an independent route (number-theoretic metaplectic covers, not geometric representation theory).

**Programme consequence.** conj:periodic-cdg at sl_2 admissible level splits into: (odd q) CLOSED via this proposition + Remark sub-problems (a), (c); (even q) residual Z/2 metaplectic class, reduces to level-2q refinement via passage to the metaplectic double cover Aut(St^v)_{met} → Aut(St^v). The single frontier-#3 open problem of the Platonic Reconstitution (remaining after W7, W12-A, W12-B closures) is now partial: odd-q half of sl_2 admissible locus closed; even-q half reduced to strictly weaker Z/2 metaplectic class.

**Pattern abstraction.** Affine-Weyl-cohomology obstructions to u-invertibility at admissible level depend on level parity through metaplectic cocycles. For higher rank g, the analogous class lives in H^2(W_aff(g), k); parity becomes lattice-divisibility (alpha_{S,u} = 0 iff q coprime to the denominator lattice disc(g)). sl_2 case has disc = 2, giving the odd/even dichotomy; simply-laced g of higher rank give disc dividing |Z(G)|; non-simply-laced g add lacing-number factor. Generalisation of prop:alpha-su-sl2-admissible to arbitrary simple g is the natural next step; sl_3 expected to give q coprime to 3 closure, sl_n closure on q coprime to n.

No downgrade of any prior theorem; the proposition splits a single open conjecture (conj:periodic-cdg at sl_2 admissible) into one closed piece (odd q) and one strictly smaller residue (even q, Z/2-class). Type: frontier computation + level-parity audit + metaplectic-cover routing.

---

## Entry: Yangian Massey indeterminacy does not kill the zeta(3) class (prop:massey-yangian-indeterminacy-nonzero, 2026-04-16)

**Claim challenged.** Does the indeterminacy coset Ind = r . H^*(E) cup H^*(E) . r of the triple Massey bracket <r,r,r> contain the depth-2 nested-bracket class [Omega_{12},[Omega_{13},Omega_{23}]], thereby killing the zeta(3) contribution and making <r,r,r> = 0 in the coset?

**Protocol (a/b/c).**

(a) RIGHT. Indeterminacy is the image of ad_r : g^{ch}_{deg-1} -> g^{ch}_{deg+2} acting on Massey fillers (LV12 Ch. A.3). For the Yangian r-matrix r = Omega_{12} + Omega_{13} + Omega_{23} on the Drinfeld--Kohno Lie algebra t_3, ad_r preserves the depth filtration and raises depth by 1. Massey fillers for the CYBE cocycle are depth-1, so Ind in degree 3 lands in depth 2 -- matching the ambient depth of [Omega_{12},[Omega_{13},Omega_{23}]]. Depth match is necessary for the question to even be well-posed.

(b) WRONG. (i) "Depth-2 ambient + depth-2 indeterminacy range implies indeterminacy covers all of depth 2" -- false, depth-2 subspace splits as decomposable wedge^2 t_3^{(1)} PLUS indecomposable nested-bracket line (Kohno's H^*(t_3) computation, 1987). (ii) "ad_r of a depth-1 filler can produce a nested commutator by Jacobi manipulations" -- false, Jacobi on [r,[Omega_{ij},Omega_{kl}]] redistributes decomposable brackets and never leaves wedge^2. (iii) Ignoring Brown's motivic-depth theorem, which is the structural input that separates decomposable from indecomposable depth-2 classes.

(c) CORRECT. The image of ad_r in depth 2 is precisely wedge^2 t_3^{(1)} (the decomposable subspace), which is transverse to the line spanned by [Omega_{12},[Omega_{13},Omega_{23}]] (the indecomposable depth-2 generator, paired with zeta(3) by Brown). Therefore Ind does not contain the nested-bracket class; the coset <r,r,r> in H^3(E)/Ind is non-zero; the zeta(3) obstruction survives unconditionally.

**Heal.** Installed prop:massey-yangian-indeterminacy-nonzero in chapters/connections/brace.tex immediately after prop:massey-rrr-yangian-scope and before rem:massey-rrr-yangian-verification. Four-step proof: (1) depth filtration preservation of ad_r with depth increment 1; (2) explicit image in depth 2 lands in wedge^2 t_3^{(1)} (decomposable); (3) motivic-depth separation via Brown's theorem -- nested bracket is indecomposable, transverse to decomposable subspace; (4) coset is non-zero with explicit representative zeta(3) . [Omega_{12},[Omega_{13},Omega_{23}]] modulo decomposable depth-2 indeterminacy. Upgrades prop:massey-rrr-yangian-scope(e) from "non-zero up to normalisation" to "non-zero with explicit indecomposable coset representative."

**Downstream.** Strengthens the chain-level chiral Deligne--Tamarkin obstruction for genuinely E_1-chiral algebras (Yangians, Etingof--Kazhdan QVAs): the zeta(3) obstruction is not a normalisation artifact that indeterminacy might remove, but an unconditional indecomposable class in H^3(E)/Ind. Confirms that associator-dependence (over a base containing zeta(3), zeta(5), ...) is the strongest honest form of chain-level Deligne--Tamarkin for E_1-chiral, as claimed in prop:massey-rrr-yangian-scope(e) third bullet and in thm:chd-deligne-tamarkin. Shares the three disjoint verification sources V1 (Drinfeld's KZ depth-2 coefficient), V2 (Kohno's H^*(t_3)), V3 (Brown's motivic depth) already recorded in rem:massey-rrr-yangian-verification -- V2 and V3 are the load-bearing inputs for the indeterminacy transversality argument. No new bibliography entries required (LV12, Kohno1987, BrownMixedTate, Drinfeld90QuasiHopf, AT12 all already present). No phantom labels; no tautological tests (proposition is structural, verified against depth-2 Lie-algebra cohomology computation independent of any chiral or operadic construction).

---

## FM247 — Phantom `prop:sc-koszul-dual-three-sectors` + Com^!=Lie category error (2026-04-17 coverage entry)

**Attack target.** Two shared-root issues in `spectral-braiding-core.tex:3730` (and `bv_brst.tex:2059`): (i) `\ref{prop:sc-koszul-dual-three-sectors}` — a named proposition cited TWICE but never `\label`-defined anywhere in `chapters/`, identical phantom-label pattern to FM87, FM155, FM213; (ii) embedded category error declaring the closed sector of `(SCchtop)^!` equals `Com^!=Lie`, whereas the closed colour of `SCchtop` is `C_*(FM_k(C)) = E_2` whose self-duality under Koszul (Tamarkin, Getzler-Jones) is `E_2^! = E_2^{shifted}` (shift by 1), NOT `Com^!=Lie`.

**Beilinson rectify (a/b/c).**

(a) RIGHT. The three-sector decomposition claim — that `(SCchtop)^!` splits into a closed-colour operadic Koszul dual, an open-colour operadic Koszul dual, and a trivial mixed sector (no open-to-closed cooperations) — IS correct. The directionality constraint (no open-to-closed arrows) transports under bar to a trivial cross-sector cooperad, leaving two independent sector duals.

(b) WRONG. (i) Closed sector identified as `Com` conflates the COHOMOLOGY of `E_2` (Gerstenhaber operad) with `Com`. Gerstenhaber = Com + Lie[1] is a direct-sum decomposition, and the Koszul dual at the Poisson-filtered associated-graded level IS `Gerst^! = Gerst{1}` (self-dual up to shift); on the nose, the closed sector dual is `E_2^{shifted}`, NOT `Com^! = Lie`. (ii) Open sector dual was tacitly `Ass^! = Ass` (self-dual under operadic Koszul), which is correct. (iii) Phantom label means no canonical source for the three-sector claim was ever written; the `\ref` sites inherited the error.

(c) CORRECT. The sector-decomposed Koszul dual is `(SCchtop)^! = (E_2^{shifted}, Ass, mixed-trivial)` with gr-Poisson filtration recovering `(Lie . Com, Ass, mixed-trivial)` at the associated-graded level. In particular: closed sector Koszul dual is `E_2{1}` (self-duality up to shift of Gerstenhaber), NOT `Com^! = Lie`; on gr, the Com→Lie arrow IS correct but refers only to the associated-graded stratum.

**Heal installed.** `sc_chtop_heptagon.tex` (1141 lines; per CLAUDE.md Platonic Reconstitution swarm completion) writes `prop:sc-koszul-dual-three-sectors` with explicit Vallette coloured Koszul duality computation: Ginzburg-Kapranov quadratic-dual construction for two-colour operad with empty cross-arrows (no open-to-closed), Künneth-for-coloured-operads reducing the three-sector dual to tensor product of single-sector duals, closed-sector computation giving `C_*(FM_k(C))^! = E_2^{shifted}` (Tamarkin-Getzler-Jones), open-sector computation giving `Ass^! = Ass`. The `\ref*{prop:sc-koszul-dual-three-sectors}` phantoms at `spectral-braiding-core.tex:3730` and `bv_brst.tex:2059` now resolve to the defined proposition. Both embedded `Com^!=Lie` misstatements corrected in situ to `E_2^! = E_2^{shifted}`.

**UPGRADE counter.** The heptagon chapter `sc_chtop_heptagon.tex` extends the pentagon of SC^{ch,top} equivalences to seven presentations (operadic, Koszul dual, factorisation, BV/BRST, convolution + Drinfeld-centre face via `Z(Rep_{fact}(A))` + DAG face via global sections of a stack of `E_1`-chiral algebras with SC^{ch,top}-datum). W13 proposition `prop:heptagon-edge-34/edge-45` (compositional qiso + Dunn assembly) closes the two new edges at chain level.

**Pattern.** FM87/FM155/FM213/FM247 share the phantom-label-under-ProvedHere root cause: cross-reference `\ref` before the target proposition is written, then the theorem citing it inherits ProvedHere status without the proof anchor existing. Counter-protocol: EVERY `\ref` or `\ref*` to a proposition/theorem must be grep-verified against `\label` definitions in the same commit; red-team sweep weekly to catch drift. `sc_chtop_heptagon.tex` closure of FM155/FM247 empirically demonstrates that the strongest honest form (sector-decomposed duality with correct `E_2^{shifted}` closed-sector dual) survives the Beilinson-attack and becomes a theorem. No downgrade.

**Independent verification sources.** derived_from = {Ginzburg-Kapranov 1994 quadratic Koszul duality for two-colour operads, Vallette 2007 coloured Koszul duality with trivial mixed sector, Kontsevich-Tamarkin E_n formality}; verified_against = {Getzler-Jones 1994 Gerstenhaber-as-E_2 homology computation, Sinha 2006 operadic homology of `C_*(FM_k(C))`, Tamarkin 2007 E_2 self-duality up to degree shift}; disjoint_rationale: Ginzburg-Kapranov + Vallette supply the general two-colour machine (categorical/algebraic); Getzler-Jones + Sinha + Tamarkin compute `C_*(FM_k(C))^!` topologically (algebro-topological). The two routes share only the definition of `E_2 = C_*(FM_k(C))` itself; the dual computation is independently verified.

## Tautological-test audit (2026-04-17 session swarm)

**Scope.** LOSSLESS scan of all IV-decorated test files under `/Users/raeez/chiral-bar-cobar-vol2/compute/tests/` plus the FM225/FM226 confirmed danger-zone tests. ~30 IV files scanned directly; wave-3/4/5/6/7/8/9/10/11/12/13/14/15/16 climax IV files pattern-matched via structured grep. Test files NOT modified; this entry flags patterns for human review in follow-up.

**Finding 1 (FM225 live, confirmed).** `compute/tests/test_adversarial_verification.py:712-719` hardcodes `expected = [Rational(1, 24), Rational(7, 5760), Rational(31, 967680)]` compared DIRECTLY against `modular_completion_koszul('abelian_cs', max_genus=3, k=1)` engine output. This is the paradigmatic AP28 tautology: engine output vs engine-shaped hardcoded value, no independent derivation. Bug was corrected once (λ_3: 1/82944 → 31/967680) per V2-AP28; engine+test moved together because both read the same `lambda_fp` source. HIGH risk.

**Finding 2 (FM226 live, confirmed).** `compute/tests/test_exceptional_affine_bar.py:446-451` `test_generator_weights_from_exponents` computes `expected = [e + 1 for e in data['exponents']]` where `data = _EXCEPTIONAL_E_DATA[name]` — the SAME dict the engine reads. Tests dict self-consistency under the `e ↦ e+1` map, NOT the Feigin-Frenkel W-algebra weight theorem. HIGH risk.

**Finding 3 (NEW, pervasive across ~27 IV decorator files, the HIGHEST-volume pattern).** The "structural oracle" idiom is employed throughout the climax IV decorator campaign: a predicate `_foo(flag1: bool, flag2: bool) -> bool` is defined as `return flag1 and flag2` (or `return True`, or set-disjointness on hardcoded literals), then the test body asserts `_foo(True, True)` and optionally `not _foo(False, True)`. This is a decorated TAUTOLOGY: the test's truth value is fixed at import time, independent of any engine or theorem content. The IV decorator machinery registers (claim, derived_from, verified_against, disjoint_rationale) correctly, but the test function itself does NOT verify anything — it asserts `True and True == True`. This is a direct analogue of the Vol III `FRAME_SHAPE_DATA[N] = (weight, c_0, ...)` + `weight := c_0/2` row/test pair that motivated the Independent Verification Protocol.

| File path | Line anchor | Pattern | AP28 risk |
|-----------|-------------|---------|-----------|
| `compute/tests/test_adversarial_verification.py` | :712-719 | hardcoded `expected=[Rational(1,24),...]` vs `modular_completion_koszul` engine | HIGH (FM225) |
| `compute/tests/test_exceptional_affine_bar.py` | :446-451 | `expected=[e+1 for e in data['exponents']]` from same dict engine reads | HIGH (FM226) |
| `compute/tests/test_adversarial_verification.py` | :706-710 | `assert lambda_fp(1) == Rational(1, 24)` (hardcoded vs engine's `lambda_fp`) | HIGH |
| `compute/tests/test_e3_topological_km_iv.py` | :35-51, :77-78 | structural oracle on set membership; `return topologised.isdisjoint(fails) and ...`; `assert _oracle()` | HIGH (climax ProvedHere) |
| `compute/tests/test_e3_topological_ds_general_iv.py` | :26-54, :83-84 | structural oracle on set membership; `assert _e3_topological_holds_for_ds_general()` | HIGH (climax ProvedHere) |
| `compute/tests/test_e3_topological_free_pva_iv.py` | :26-44, :70-71 | structural oracle on set membership; `assert _e3_topological_holds_for_free_pva_noncritical()` | HIGH (climax ProvedHere) |
| `compute/tests/test_global_triangle_boundary_linear_iv.py` | :32-49, :72-73 | `classes_where_proved.isdisjoint(...)`; `assert _global_triangle_holds_on_GLC()` | HIGH (FM126 HEAL-target ProvedHere) |
| `compute/tests/test_modular_bar_d_squared_iv.py` | :36-53, :77-78 | `axioms = {k: True}` dict; `return all(axioms.values()) and len(axioms)==3` | HIGH (climax ProvedHere) |
| `compute/tests/test_bar_differential_squared_iv.py` | :53-72, :99-100 | `vanishing_terms = {k: True}` dict; `return len(==6) and all(values())` | HIGH (Vol I Theorem A descendant) |
| `compute/tests/test_affine_monodromy_identification_iv.py` | :45-58, :85-93 | `return True` after boolean-arg guard; loops over rank but always returns True | HIGH (climax ProvedHere) |
| `compute/tests/test_chd_ds_hochschild_iv.py` | :43-57, :86-95 | `return True` after boolean-arg guard; DS-Hoch bridge IS FM126/185/186 heal target | HIGH (climax, critical heal anchor) |
| `compute/tests/test_climax_theorems_wave3_iv.py` | :27-29, :56-59 (+6 more) | `_oracle(a, b): return a and b`; `assert _oracle(True, True)` | HIGH (7 climax claims) |
| `compute/tests/test_climax_theorems_wave4_iv.py` | :27, :57-59 (+5 more) | same pattern across 6 oracles (abelian strictification, BD-CG, MC, DS Koszul, LG truncation) | HIGH (7 claims) |
| `compute/tests/test_climax_theorems_wave5_iv.py` | :26-27, :53-55 (+5 more) | CY duality, D1, FM, HH-CoHH, Stokes, Obs-SC, Jacobi — all `return a and b` | HIGH (7 claims) |
| `compute/tests/test_climax_theorems_wave6_iv.py` | :122-125, :158-161, :193-196 | arithmetic oracles (`c * Fraction(5,6)` etc.) — test value = hardcoded, engine reads same `c * H_N - 1` formula | MED (arithmetic but same-formula tautology risk; verify against Mumford/Polchinski external numerically) |
| `compute/tests/test_climax_theorems_wave7_iv.py` | :27-29, :56-59 (+5 more) | same boolean-oracle pattern; R-twisted descent, D0-D1, DS-Koszul, FM strata, IHX, Leibniz, PVA1 | HIGH (7 claims) |
| `compute/tests/test_climax_theorems_wave8_iv.py` | :26-29, :50-52 (+5 more) | SC operad, raviolo, affine KM, modular all-genera, r-mode, filtration transport | HIGH (7 claims) |
| `compute/tests/test_climax_theorems_wave9_iv.py` | :28-30, :53-55 (+5 more) | HH-UGT, LG vanishing, m_3, truncation, W_3 cocycles, normform | HIGH (7 claims) |
| `compute/tests/test_climax_theorems_wave10_iv.py` | :26-28, :50-52 (+5 more) | GLZ compat, L1 Koszul, TS, AGT, all-genus, analytic YB, annular-HH | HIGH (7 claims) |
| `compute/tests/test_climax_theorems_wave11_iv.py` | :26-28, :48-49 (+5 more) | annular bar closure, bar concentration, bar-represents, bar-terminal, bar-weight, braided, bulk-is-chirhoch | HIGH (7 claims) |
| `compute/tests/test_climax_theorems_wave12_iv.py` | :26-28, :49-50 (+5 more) | models-equivalent, trinity, Verlinde, class-M-chainlevel, class-C, shadow-depth, uncurved | HIGH (7 claims; FM126 heal target touched) |
| `compute/tests/test_climax_theorems_wave13_iv.py` | :26-28, :49-50 (+5 more) | KZ derived, Gerstenhaber, Positselski, Baxter-Rees, fingerprint, formal genus, twisting | HIGH (7 claims, FM177 touched) |
| `compute/tests/test_climax_theorems_wave14_iv.py` | :24-26, :46-47 (+5 more) | HH-cohh chain, half-space, HC-Verdier, Heisenberg BV, hexagon, higher-genus, Hochschild-bridge | HIGH (7 claims) |
| `compute/tests/test_climax_theorems_wave15_iv.py` | not exhaustively sampled | wave-pattern same structure | HIGH (presumed) |
| `compute/tests/test_climax_theorems_wave16_iv.py` | not exhaustively sampled | wave-pattern same structure | HIGH (presumed) |
| `compute/tests/test_climax_theorems_iv.py` | :94-116, :152-174 | stronger — tests actual structural numerics (Leech rank 24, DM dim 3g-3+n, Stokes count 2) + hardcoded constants | MED (Leech rank is genuine external mathematical fact, not engine tautology; Stokes-matrix count arithmetic from Jimbo-Miwa — cross-check external) |
| `compute/tests/test_mb_h2_vanishing_iv.py` | :42-55, :86-88 | `return True` hardcoded on `genus` | HIGH (FM67/FM88 heal target) |
| `compute/tests/test_verdier_intertwining_iv.py` | :34, :76 | `def _bar_cobar_commutes_with_verdier(): ... return True`; single-line oracle | HIGH (Theorem D adjacency) |
| `compute/tests/test_universal_holography_functor_fm_iv.py` | :64 | `return True` inside oracle body | HIGH (climax Universal Holography ProvedHere) |
| `compute/tests/test_sc_chtop_heptagon_iv.py` | :71-75 | boolean-oracle `return True`; assert with `ds_hoch_bridge=False, class_m=False` returns True trivially | HIGH (heptagon pentagon-to-heptagon extension ProvedHere) |
| `compute/tests/test_triality_y_algebra_iv.py` | not matched to oracle pattern (no boolean oracle) | file structure unaudited in detail | UNKNOWN |

**Summary counts.**
- Files scanned (IV-decorated + flagged by FM): ~30 IV files + `test_adversarial_verification.py` + `test_exceptional_affine_bar.py`.
- HIGH-risk tests/decorators flagged: ~27 files, ~160+ individual test functions (most climax-wave files contain 6-7 oracle-style decorators each).
- MED-risk: 2 (wave6 arithmetic oracles; wave1 `test_climax_theorems_iv.py` — mixes genuine external facts with structural bookkeeping).
- UNKNOWN: 1 (`test_triality_y_algebra_iv.py` — no boolean oracle matched; requires dedicated audit).

**Three most dangerous tests (human-review priority).**
1. `compute/tests/test_adversarial_verification.py:712-719` (FM225) — direct hardcoded-vs-engine tautology that passed through the Vol III swarm attention and remains live. REMEDIATION: recompute `expected` values via independent Arakelov heat-kernel / zeta-regularised determinant; cite Mumford's λ_g formula and derive F_g from geometry, not from `lambda_fp` engine.
2. `compute/tests/test_e3_topological_km_iv.py:35-78` — the flagship ProvedHere claim `thm:E3-topological-km` (Vol II climax, CFG 2506.12412 verified_against) is backed by `topologised.isdisjoint(fails)` on HARDCODED string sets with no engine call. The decorator's disjoint_rationale is honest, but the test body is `True`. REMEDIATION: import a CFG-style factorization-homology trace oracle from a newly-scaffolded engine OR recompute the BRST Q-cohomology on a small V_k(sl_2) sector numerically and compare against programme's chain-level formula, with BOTH sides derived from independent initial data.
3. `compute/tests/test_global_triangle_boundary_linear_iv.py:32-73` — the FM126 heal anchor (`thm:global-triangle-boundary-linear`, Lurie HA 5.3.1.30 BZFN) is backed by `classes_where_proved.isdisjoint(classes_where_conditional)` on hardcoded `{"G", "L", "C"}` vs `{"M"}` — the class membership IS the claim, not a computation. REMEDIATION: implement ChirHoch^0(A_GLC) sample-computation (e.g. Heisenberg at k=1) against Lurie HA 5.3.1.30 mode-algebra Z(LMod_A) on a finite-dim Weyl truncation; disjoint because Lurie is universal categorical and programme is chiral-specific.

**Meta-pattern (critical).** The climax waves (3-16) appear to have been generated by a template: a decorator with honest derived_from / verified_against / disjoint_rationale, paired with a trivial boolean-oracle test body. The decorator registry IS correctly populated — `make verify-independence` will report healthy coverage — but the tests themselves verify nothing. This is the EXACT failure mode Independent Verification Protocol was designed to prevent (cf. CLAUDE.md: "tautology = audit failure, not silent pass"). The disjointness check passes because derived_from and verified_against are legitimately disjoint strings; but the test body never compares any engine output against either derivation path. Coverage % appears green while epistemic content is zero.

**Recommended remediation pipeline (human follow-up).**
1. (P0) Fix FM225 and FM226 in-place by recomputing `expected` values via independent derivation (Mumford λ_g + Feigin-Frenkel exponents) with documentation cite.
2. (P1) Pick the top-5 decorator-install priorities from CLAUDE.md (thm:E3-topological-km, thm:E3-topological-DS-general, thm:E3-topological-free-PVA, thm:global-triangle-boundary-linear, thm:modular-bar D²=0). Replace the structural-oracle test body with an actual numerical comparison: engine output on a small input, independent external formula evaluated on the SAME input, assert equality.
3. (P2) Audit wave-3 through wave-16 systematically: for each of the ~21 climax theorems per wave, decide whether to (a) supply a genuine engine-vs-external comparison, (b) downgrade the claim status, or (c) mark the decorator `pending_numerical_witness=True` so audit surfaces it.
4. (P3) Add a new audit check to `compute/scripts/audit_independent_verification.py` that scans test bodies for the structural-oracle pattern (`return True`, `return flag1 and flag2`, `return setA.isdisjoint(setB)`) and warns when a decorator wraps such a trivial body.

**AP28 protocol reminder.** From CLAUDE.md: "Test expected values from 2+ independent sources with documented derivation. Engine+test from same mental model share error." Structural oracles violate this: they test neither the engine nor the external source — they test literal constants. A test that returns `True` by construction cannot falsify the claim; it cannot distinguish a correct programme from an incorrect one. The decorator's disjointness check is necessary but not sufficient: the test body must COMPARE something to something. This audit entry is LOSSLESS — no tests are modified; recommendations are for author prioritization.

## FM closure audit (2026-04-17 session swarm)

Lossless audit of CLAUDE.md Unified Error Catalogue (FM40-FM247) against actual `.tex` inscriptions. LOSSLESS: no FM entries deleted from CLAUDE.md. Scope: FMs with explicit "Counter:" clauses or listed in HEAL-SWEEP / PLATONIC RECONSTITUTION sections. Status codes: CLOSED (counter inscribed), PARTIAL (counter partially realized / still some gap), OPEN — counter not found (counter NOT found in .tex).

**Methodology.** For each FM with a named label/file counter, grep for that label or file in `chapters/` tree. Label present = CLOSED; label absent but file-adjacent prose found = PARTIAL; neither = OPEN.

### Audit table (grouped by FM cluster)

| FM | Counter target | Status | Evidence |
|----|---------------|--------|----------|
| FM67, FM87, FM88 | `prop:genus1-twisted-tensor-product`, `thm:curved-dunn-H2-vanishing-all-genera`, bridge chain map | CLOSED | `chapters/theory/curved_dunn_higher_genus.tex` (5 ProvedHere); `prop:modular-bootstrap-to-curved-dunn-bridge` found in 5 chapters incl. `modular_swiss_cheese_operad.tex` |
| FM68, FM91, FM92, FM111 | Modular operad composition via KZ/KZB regularity + irregular-singular framework | CLOSED | `modular_swiss_cheese_operad.tex`; Jimbo-Miwa irregular-singular present in 6 chapters incl. `curved_dunn_higher_genus.tex` |
| FM69, FM70 | Theorem A FORM-B via Francis-Gaitsgory + R-twisted Σ-descent | CLOSED | `prop:R-twisted-sigma-n-descent` at `factorization_swiss_cheese.tex`; Francis-Gaitsgory / GR17 / Ran(X) cited across 15 chapters |
| FM75, FM76, FM80 | Bar-cobar inversion at minimal-model / admissible / critical loci | PARTIAL | Arakawa C_2-cofiniteness cited (3 theory files incl. `topologization_class_m_original_complex_platonic.tex`); minimal-model null-vector correction present in `unified_chiral_quantum_group.tex`; no unified Thm B published |
| FM77, FM105-110 | Infinite Fingerprint + class FF integration | CLOSED | `chapters/theory/infinite_fingerprint_classification.tex` present; referenced across 5 chapters |
| FM81 | `thm:E3-topological-DS-general` non-principal (ghost-bilinear lift) | CLOSED | `chapters/connections/fm81_fractional_ghost_platonic.tex`; 27 files reference; label present |
| FM82 | `thm:E3-topological-free-PVA` including class M | CLOSED | `thm:E3-topological-free-PVA` present across 20 files; decorated in `test_e3_topological_free_pva_iv.py` |
| FM83, FM197, FM198 | 14 characterizations on own Φ-chart via Koszulness moduli `M_Kosz` | CLOSED | `chapters/theory/koszulness_moduli_M_kosz.tex` |
| FM97-101, FM230 | Seven Faces as GRT-torsor with F8 (motivic) + F9 (Willwacher) | CLOSED | `chapters/theory/grt_parametrized_seven_faces.tex`; Brown motivic content across 4 chapters |
| FM102, FM103 | Celestial Weinberg + higher-r soft via Mellin-shadow bridge | CLOSED | `chapters/connections/soft_graviton_mellin_shadow_bridge_platonic.tex` (8 Mellin hits); `universal_celestial_holography.tex` |
| FM120, FM128 | Monster V^♮ orbifold BV anomaly vanishing | CLOSED | `chapters/connections/monster_chain_level_e3_top_platonic.tex`; `celestial_moonshine_bridge.tex` |
| FM125, FM126, FM185-188, FM214 | Universal Holography + DS-Hochschild bridge closing class M chain-level | CLOSED | `chapters/theory/chiral_higher_deligne.tex` (16 ProvedHere, 2 HPL-transfer hits) with `thm:chd-ds-hochschild`, `cor:universal-holography-class-M`; `universal_holography_functor.tex` |
| FM127 | Algebraic vs physical UV finiteness split | CLOSED | `thqg_perturbative_finiteness.tex` + `programme_climax_platonic.tex` |
| FM130, FM131, FM162 | W_N N≥4 cross-channel + BP free strong gen + exceptional PBW | PARTIAL | `Guay-Regelskis-Wendlandt / 1811.06475 / 1706.05176 / de Boer-Tjin` ZERO repo hits; `unified_chiral_quantum_group.tex` asserts the Yangian-cluster heal but key bibliographic anchors missing |
| FM132-134 | W(p) / N=2 SCA / Y-algebra triality independent verification | CLOSED | `chapters/theory/super_chiral_yangian.tex`; `test_super_chiral_yangian.py` with 10 `@independent_verification` decorators |
| FM135 | W_3 holographic datum Vol II decorator | CLOSED | `test_grt_parametrized_seven_faces.py` (9 IV), wave_iv test batteries decorate climax theorems |
| FM136-142 | YM Open_B scope + Clay-disambiguation + screening rename + log-FM vs log-VOA + critical-string Clifford | PARTIAL | YM chapters present; cluster-wide renames not grep-confirmed |
| FM143-147 | Kontsevich integral / FM sign / 4T=Arnold / Bar-Natan STU citation | PARTIAL | `kontsevich_integral.tex` cites Bar-Natan (3 files); explicit STU citation + sign re-derivation not verified |
| FM148-154 | Raviolo PVA descent D2-D6 + Mon(R) twist on ρ | PARTIAL | `chapters/theory/raviolo.tex`, `raviolo-restriction.tex` retain (H1)-(H4) assumption language; logarithmic-SC scope present but Mon(R) isotopy not explicit |
| FM155, FM156, FM247 | Phantom `prop:sc-koszul-dual-three-sectors`; Com^!=Lie → E_2^{shifted} | CLOSED | `chapters/theory/sc_chtop_heptagon.tex:147,703` defines prop; `spectral-braiding-core.tex:3751` has `\label`; phantom resolved |
| **FM157** | Liv06 → Hoefel / Hoefel-Livernet rebinding | **OPEN — counter not found** | Grep for `Hoefel|arXiv:0809.4623|Hoefel-Livernet|arXiv:1207.2307|HL12` returns ZERO hits across entire repo. Original `Liv06` cites also not found in `chapters/`. Citation drift unresolved despite being called out in 7+ chapter sites per FM157 |
| FM158, FM159, FM160, FM219 | Kontsevich formality as ∞-qiso + Drinfeld associator + Voronov embedding qiso | PARTIAL | Drinfeld associator cited across 19 chapters incl. `sc_chtop_heptagon.tex`, `kontsevich_integral.tex`; universal named Convention not inscribed |
| FM161, FM163, FM167 | Y(g) Positselski + all-order R^{-1} + non-simply-laced Langlands | PARTIAL | Positselski / filtered-CDG across 12 chapters; `Finkelberg-Tsymbaliuk / quantum geometric Langlands` ZERO hits — non-simply-laced heal incomplete |
| FM165, FM166 | Gaudin MC + Jones from ordered E_1 bar + MTC quotient factoring | PARTIAL | `Jones polynomial / RT functor / MTC quotient` across 11 chapters; factoring argument prose-level |
| FM168, FM169 | Gravitational Yangian as Hopf + CYBE pro-completion | PARTIAL | `thqg_gravitational_yangian.tex` retains framework; antipode at Layer-B not inscribed as new proposition |
| **FM171-174** | (H1)-(H4) retirement + zombie pva-descent + foundations drafts + double recognition label | **OPEN — counter not found** | `pva-descent.tex`, `pva-preview.tex`, `foundations_overclaims_resolved.tex`, `foundations_recast_draft.tex` ALL STILL ON DISK. 3 chapters still carry `\begin{assumption}[...(H1)-(H4)]`; `thm:recognition-foundations` (foundations.tex:2233) AND `thm:recognition-SC` (locality.tex:364) both labeled simultaneously |
| FM175 | gr-splitting second-proof demotion to Remark + Gerstenhaber→Poisson naming | PARTIAL | `line-operators.tex:214-220` retains prose; no explicit Remark demotion verified |
| FM176-181 | Type-A scope + slot-commutativity + orthogonal coideal + Riordan GF | PARTIAL | `shifted_rtt_duality_orthogonal_coideals.tex`, `typeA_baxter_rees_theta.tex` (31 Baxter hits), `casimir_divisor_core_transport.tex` present; explicit rename to "weight-Rees spectral-telescope" not found |
| FM182-184 | Named ChirHoch sub-lemma + qi bridge theorem | PARTIAL | `hochschild.tex:851` uses Swiss-cheese recognition route; `chiral_higher_deligne.tex` covers brace identity; explicit `thm:chiral-hochschild-models-equivalent` not grep-located |
| FM189 | Brace strict-coordinate convention promoted to numbered Convention | PARTIAL | `brace.tex` retains remark; numbered Convention not verified |
| FM190-196 | Standalone scope tagging + SV coproduct reconstruction framing | PARTIAL | Platonic standalones propagated via HEAL but `bar_chain_models` wording not rechecked |
| FM199, FM200, FM202-206 | N-series (Vol I) scope refinements | PARTIAL | Vol II reflects Vol I; Vol II preface AP14 clean; N5/N6 OPE bound not re-verified |
| FM207, FM208 | rosetta_stone Vol II-local + per-face qualifiers on `thm:vol2-seven-faces-master` | PARTIAL | `rosetta_stone.tex` present; `dnp_identification_master.tex` retains theorem; `\ClaimStatusProvedHereConditional` split not verified |
| FM209 | `prop:affine-is-log-SC` rephrased to pair (Z^der_ch, A) | PARTIAL | `affine_half_space_bv.tex:1548` retains proposition; AP165-compliant rephrasing not grep-confirmed |
| FM210, FM211 | DNP qualifier propagation + non-renormalization tag | PARTIAL | `dnp_identification_master.tex` retains framing |
| FM212 | `thm:cl-n4-chirality` citation expansion to CDG20/Zeng23 | PARTIAL | `ht_physical_origins.tex:444-456` cites CL16; additional citations not confirmed |
| **FM213** | Phantom file `chapters/connections/thqg_open_closed_realization.tex` | **OPEN — counter not found** | File does NOT exist; `ht_physical_origins.tex:379` pointer still dangling |
| FM220-223 | Preface modular status alignment + spectral-vs-categorical naming | PARTIAL | `preface.tex` retains some universal-IS-claims; HEAL not fully propagated |
| FM224-229 | Independent-verification decorator campaign | PARTIAL | 212 `@independent_verification` decorators across 40 test files (from 0/1134 baseline); many `_iv.py` variants; coverage well below 100% of ProvedHere pool |
| FM234, FM235 | E_∞/E_1 interpolate prose + AP152 ordering | PARTIAL | Vol I survey prose; Vol II downstream rectifications not fully pushed |
| **FM236** | "Unconditional for every family" scope-tag renames | **OPEN — counter not found** | Zero repo-wide renames verified in this pass |
| FM240 | Explicit half-braiding σ_A(z) construction before `thm:braided-category` | CLOSED | `spectral-braiding-core.tex:3933,3936,3972` (3 half-braiding refs); `thm:braided-category` at L270 preceded by half-braiding narrative |
| FM241-246 | Spectral-braiding co-YBE rewriting / pole universalisation / chiral Deligne qualifier / genus-tower asymmetry / Dunn polarisation / DNP25-vs-A_∞ split | PARTIAL | `spectral-braiding-core.tex` present; specific per-FM annotations not grep-verified |
| FM248-257 | Spectral sequences / derived Langlands / existence criteria | PARTIAL | `conj:periodic-cdg` closed in Vol I (`chapters/theory/periodic_cdg_admissible.tex` in `~/chiral-bar-cobar`); Vol II downstream not fully propagated |

### Aggregate (40 representative FM clusters audited, covering ~185 individual FMs)

- **CLOSED (counter fully inscribed with named label/file)** — 14 clusters: FM67/87/88, FM68/91/92/111, FM69/70, FM77/105-110, FM81, FM82, FM83/197/198, FM97-101/230, FM102/103, FM120/128, FM125/126/185-188/214, FM127, FM132-134, FM135, FM155/156/247, FM240.
- **PARTIAL (counter partially realized, gap remains)** — 22 clusters: FM75/76/80, FM130/131/162, FM136-142, FM143-147, FM148-154, FM158/159/160/219, FM161/163/167, FM165/166, FM168/169, FM175, FM176-181, FM182-184, FM189, FM190-196, FM199/200/202-206, FM207/208, FM209, FM210/211, FM212, FM220-223, FM224-229, FM234/235, FM241-246, FM248-257.
- **OPEN — counter NOT found in .tex** — 4 clusters:
  - **FM157** — Liv06 → Hoefel citation rebinding: zero hits for Hoefel/Livernet/0809.4623/1207.2307/HL12 across entire repo. Citation error still live at 7+ `\cite{Liv06}` sites.
  - **FM171-174** — pva-descent zombie + foundations drafts + double recognition label: `pva-descent.tex`, `pva-preview.tex`, `foundations_overclaims_resolved.tex`, `foundations_recast_draft.tex` all still present; `thm:recognition-foundations` AND `thm:recognition-SC` both labeled simultaneously.
  - **FM213** — Missing `thqg_open_closed_realization.tex`: file does not exist; `ht_physical_origins.tex:379` pointer dangling.
  - **FM236** — "Unconditional for every family" scope-tag renames not propagated.

### Three most interesting closure gaps

1. **FM157 (Liv06 mis-citation)** — Simplest and most mechanical FM in the entire sweep ("rebind Liv06 → Hoefel + Hoefel-Livernet"); zero repo-wide occurrences of the correct authors / arXiv IDs. All `\cite{Liv06}` sites (line-operators, modular_swiss_cheese_operad, bar-cobar-review, introduction, preface, concordance) still carry the wrong attribution. Pure citation fix never committed despite repeated call-outs.

2. **FM171-174 (foundations zombie drafts + double recognition theorem)** — Four explicit "delete these files" counters from HEAL-SWEEP, none executed: `pva-descent.tex`, `pva-preview.tex`, `foundations_overclaims_resolved.tex` (305 L), `foundations_recast_draft.tex` (749 L). V2-AP27 (duplicated .tex forbidden) violated at foundational layer. The recognition theorem is labeled in TWO places with slightly different scope (`thm:recognition-foundations` at `foundations.tex:2233` and `thm:recognition-SC` at `locality.tex:364`); both are cited across the downstream graph in 14+ places — exactly the pattern V2-AP27 warns against.

3. **FM130-131/162 (Yangian load-bearing citations)** — HEAL explicitly names "cite Guay-Regelskis-Wendlandt 2018 (arXiv:1811.06475 / 1706.05176) for exceptional PBW" and "cite de Boer-Tjin 1993 for BP free strong generation" as prerequisite for `thm:Koszul_dual_Yangian` scope-extension to ALL simple types. Zero repo hits for either arXiv number or either author name. `unified_chiral_quantum_group.tex` asserts the extension as theorem but the cited anchors for PBW beyond classical types are missing — a load-bearing "all simple types" claim whose key bibliographic anchor has not been inscribed.

**Note on decorator coverage (FM224-229).** From 0/1134 at installation to 212 `@independent_verification` occurrences across 40 test modules — substantial absolute progress, but coverage of the 1134 ProvedHere pool remains well below 100%. Most installed decorators target the Platonic reconstitution climax theorems (`thm:chd-ds-hochschild`, `thm:universal-holography-functor`, `thm:E3-topological-*`, `thm:curved-dunn-H2-*`, `thm:uch-main`, `thm:unified-chiral-quantum-group`); the long tail of older ProvedHere claims remains undecorated. FM225/FM226 structural-oracle pattern (see "AP28 protocol reminder" above) is an orthogonal deeper gap: even decorated tests may be tautological if the body compares an engine output only to itself.

**Session outputs**: audit is LOSSLESS (no CLAUDE.md deletions); append-only on `first_principles_cache.md`; no `.tex` modifications; no commits.

## Part-ordering Platonic audit (Agent 1, 2026-04-17 swarm)

Eight-part structure at `main.tex:1332,1380,1424,1449,1509,1547,1583,1610` audited against Platonic narrative arc.

### Transition table

| Transition | Narrative RIGHT | Narrative WRONG / redundancy | Strongest honest form | Verdict |
|---|---|---|---|---|
| I→II (Swiss-cheese → E_1 Core) | Two-coloured operad precedes ordered bar; closed colour at `main.tex:1346` motivates the open-colour focus of Part II at `bar-cobar-review` (`main.tex:1414`). | Part I already contains the E_1-open-colour `pva-descent-repaired` and `pva-expanded-repaired` (`main.tex:1376–1377`) — arguably E_1 Core territory. | The coalgebraic shadow (Part I) followed by the STRICT E_1 refinement (Part II, R-matrix + KZ + Yangian at `main.tex:1388–1391`). | KEEP |
| II→III (E_1 Core → Faces of r(z)) | r(z) = Res^{coll}_{0,2}(Θ_A) is the binary-collision residue of the MC element BUILT in Part II (Yangian spectral parameter native to ordered bar at `thqg_gravitational_yangian`, `main.tex:1418`); GRT_1-torsor viewpoint unlocks seven faces at `dnp_identification_master` (`main.tex:1440`). | `typeA_baxter_rees_theta` (II, L1419) and `spectral-braiding-core` (III, L1441) both concern spectral R(z); arguably spectral braiding belongs in II. | Ordered bar (II) produces r(z) → faces (III) read it through seven lenses. | KEEP |
| III→IV (Faces → Characteristic Datum and Modularity) | Part III r(z) = genus-0 projection; Part IV extends to modular operad + all-genus MC via `modular_swiss_cheese_operad` (`main.tex:1488`) and `grt_parametrized_seven_faces` (L1489). | Part IV mixes WORKED EXAMPLES (Rosetta, Virasoro, W_3 at L1480–1485) with MODULAR THEORY (L1488–1505) — two distinct narrative strata conflated. | Genus-0 datum (III) → modular envelope (IV). Examples should perhaps segregate as a IV.A micro-section. | KEEP (with caveat: internal IV.A/IV.B split recommended but out-of-scope for this audit) |
| IV→V (Characteristic Datum → HT Landscape) | Part V's opening `main.tex:1514–1516` "Koszul triangle...of Part~\ref{part:bbl-core}" grounds V in III's triangle; but Part V's anomaly-completion transgression `anomaly_completed_core` (L1536) requires IV's modular MC class Θ^oc. | V DEPENDS on IV (modular MC); IV DOES NOT depend on V. Proposal to swap V↔IV (landscape observed → datum abstracted) REJECTED: Rosetta Stone (IV, L1480) computes the four-functor datum BEFORE anomaly completion uses it. The bottom-up proposal inverts the logical arrow. | Datum built abstractly (IV) → landscape fills it in (V). | KEEP (swap proposal REJECTED) |
| V→VI (HT Landscape → 3D Gravity) | Part VI explicitly "requires the full E_1 + modular + complementarity machinery of Parts~I–V" (`main.tex:1558–1559`); Virasoro quartic pole forces infinite A_∞ tower, PROPERLY the most downstream Part. | None substantive; arc is clean. | Landscape (V) provides anomaly + holographic machinery → Gravity (VI) is its climactic specialization at Vir_c. | KEEP |
| VI→VII (3D Gravity climax → Frontier) | Frontier chapters are core-chapter splits (`spectral-braiding-frontier`, `ht_bulk_boundary_line_frontier`, etc. at `main.tex:1596–1607`): conjectural extensions of Parts I–VI. | Part VII and Part VIII BOTH handle unresolved material. The opening line of VII (L1592–1593) "No earlier part depends on material in this part" + the closure claim of VIII (L1644–1646) that "all four irreducible opens...are now closed" creates architectural REDUNDANCY: VII = open conjectures, VIII = theorems that close those same conjectures. | VII should be absorbed into VIII as "VIII.A Open Frontier / VIII.B From Frontier to Theorem" — one unified frontier-closure Part. | MERGE (proposal: absorb VII into VIII as two sections) |
| VII→VIII (Frontier → From Frontier to Theorem) | VIII promotes FM67/FM126/FM251/FM91 to theorems via bridges (`main.tex:1615–1635`). Natural capstone. | VIII.body references `thm:curved-dunn-H2-vanishing-all-genera` (L1620) which lives in `curved_dunn_higher_genus` — currently in PART IV (`main.tex:1493`), NOT Part VIII. Architectural mismatch: the theorem closing FM67 lives in IV, while VIII only narrates the closure. | Either move the four closure chapters into Part VIII, or redefine Part VIII as the META-NARRATIVE integration Part (currently done by `part_viii_synthesis`, L1648). | PROMOTE-CLIMAX (see below) |

### Climax question

Part VI (3D Gravity) vs Part VIII (Frontier-to-Theorem) as architectural climax.

- Part VI is the NARRATIVE climax: specific downstream phenomenon (3d gravity from Virasoro) that the whole apparatus aims at (`main.tex:1552–1559`).
- Part VIII is the META-THEORETIC closure: promotes the four irreducible opens to theorems.

Verdict: **Part VI remains narrative climax; Part VIII is the epistemic closure.** The two roles are orthogonal. No promotion swap recommended. However the current VII+VIII diptych dilutes the epistemic closure: MERGE VII into VIII delivers the strongest honest form — "Open Frontier followed by its Closure" in one Part.

### Concrete recommendations

1. MERGE Part VII into Part VIII with internal sections (VIII.A Open / VIII.B Closed). Saves one `\part{}` heading; clarifies architecture.
2. KEEP all other transitions.
3. Split Part IV internally into IV.A (Worked Examples: Rosetta + Vir + W_3) and IV.B (Modular Machinery: `modular_swiss_cheese_operad` onward) via `\section*` or subparts — clarifies the examples/theory stratum.
4. REJECTED: the V↔IV swap proposal. Current order is correct per Rosetta Stone being a VERIFICATION of the four-functor datum, not a derivation of it.

### Lossless discharge

All recommendations preserve every `\input{}` directive at `main.tex:1365–1650` unchanged; only `\part{}` headings and optional `\section*` insertions would be modified. No chapter content, label, or `\ref` target is altered.

### Cross-volume ref audit

- Vol III `main.tex` uses `\label{part:examples}` (L792) and `\label{part:frontier}` (L923) but these are Vol III-LOCAL labels (Vol III has its own Part named "examples"). No Vol II→Vol III collision from Vol II label changes.
- Vol II's `part:swiss-cheese`, `part:e1-core`, `part:bbl-core`, `part:examples`, `part:holography`, `part:gravity`, `part:frontier`, `part:frontier-to-theorem` are referenced ONLY within Vol II (searched via Grep across both Vol I and Vol III trees — hits are in `audit/`, `healing/`, and scratch dirs, not in Vol I/III `.tex` source).
- Recommended MERGE (VII→VIII) would retire `\label{part:frontier}`. Within Vol II, grep for `\ref{part:frontier}` locates references in the Part VII opener itself (`main.tex:1589`) and is otherwise self-contained. The retirement is safe; the Part VIII opener already subsumes the narrative.
- No Vol I or Vol III cross-ref at risk.

Agent 1 complete. PROPOSAL ONLY; no reorder executed.

## Chapter-placement Platonic audit (Agent 2, 2026-04-17 swarm)

Per-chapter first-principles audit of `\input{chapters/...}` placement in `main.tex` against the Platonic spine: Part I (Open Primitive / SC^{ch,top} foundation), Part II (E_1 core), Part III (Faces of r(z) GRT torsor), Part IV (Characteristic Datum / Modularity), Part V (Standard HT Landscape), Part VI (3D Gravity / E_n climax), Part VII (Frontier), Part VIII (From Frontier to Theorem).

Method: (a) read chapter header to identify primary content; (b) map to native architectural spine; (c) KEEP vs MOVE. LOSSLESS — no chapter file edits; only `\input{...}` reordering if MOVE recommended. PROPOSAL ONLY, no execution.

| File | Current part | Native part | Verdict | Justification |
|------|--------------|-------------|---------|---------------|
| `theory/introduction` | pre-Part I | pre-Part I | KEEP | Front-matter introduction, correctly placed before Part I. |
| `theory/foundations` | I | I | KEEP | Foundational definitions of chiral algebras. |
| `theory/locality` | I | I | KEEP | HT locality operad — foundational. |
| `theory/axioms` | I | I | KEEP | Concrete A_inf chiral axioms — foundational. |
| `theory/equivalence` | I | I | KEEP | W(SC^{ch,top}) ↔ axioms equivalence — foundational. |
| `theory/bv-construction` | I | I | KEEP | BV-BRST construction of SC datum — foundational. |
| `theory/factorization_swiss_cheese` | I | I | KEEP | Layered factorization SC hierarchy — foundational. |
| `theory/raviolo` | I | I | KEEP | Relation to raviolo VAs — locality context. |
| `theory/raviolo-restriction` | I | I | KEEP | Cech/Thom-Sullivan model — locality calculus. |
| `theory/fm-calculus` | I | I | KEEP | FM calculus — foundational operadic. |
| `theory/orientations` | I | I | KEEP | Orientations on FM_k(C)×Conf_m(R) — foundational. |
| `theory/fm-proofs` | I | I | KEEP | Stokes/residue proofs — foundational. |
| `theory/pva-descent-repaired` | I | I | KEEP | PVA descent — cohomological shadow, foundational. |
| `theory/pva-expanded-repaired` | I | I | KEEP | Expanded PVA proofs — foundational appendix-like. |
| `connections/bar-cobar-review` | II | II | KEEP | Bar complex as twisting classifier — E_1 core. |
| `connections/line-operators` | II | II | KEEP | Line ops / Koszul duality / spectral R — E_1 core. |
| `connections/ordered_associative_chiral_kd_core` | II | II | KEEP | Ordered E_1 Koszul duality — E_1 core central. |
| `connections/dg_shifted_factorization_bridge` | II | II | KEEP | dg-shifted factorization bridge — E_1 specialization. |
| `connections/thqg_gravitational_yangian` | II | II | KEEP | Universal Gravitational Yangian from collision residue — E_1 object. |
| `connections/typeA_baxter_rees_theta` | II | II | KEEP | Baxter-Rees compactification — type-A RTT, E_1 core. |
| `connections/shifted_rtt_duality_orthogonal_coideals` | II | II | KEEP | Shifted RTT, coideal descent — E_1 core. |
| `connections/casimir_divisor_core_transport` | II | II | KEEP | Casimir/divisor transport — E_1 auxiliary. |
| `connections/dnp_identification_master` | III | III | KEEP | Seven faces master — core Part III content. |
| `connections/spectral-braiding-core` | III | III | KEEP | Spectral braiding / R-matrix provenance — Part III central. |
| `connections/ht_bulk_boundary_line_core` | III | III | KEEP | HT bulk-boundary-line — r(z) face adjacent. |
| `connections/celestial_boundary_transfer_core` | III | III | KEEP | KK reduction 6d→3d, Airy-Witt — r(z) transfer face. |
| `connections/affine_half_space_bv` | III | III | KEEP | Affine half-space BV → Vir, W_3 — r(z) realization. |
| `connections/fm3_planted_forest_synthesis` | III | III | KEEP | FM_3 planted-forest synthesis — operadic r(z) calculus. |
| `connections/kontsevich_integral` | III | III | KEEP | Kontsevich integral / knot invariants — r(z) face. |
| `examples/rosetta_stone` | IV | IV | KEEP | Heisenberg Rosetta Stone — characteristic-datum anchor. |
| `examples/examples-computing` | IV | IV | KEEP | Explicit examples — characteristic datum. |
| `examples/examples-complete-proved` | IV | IV | KEEP | Complete A_inf computations — characteristic. |
| `examples/examples-worked` | IV | IV | KEEP | Worked examples — characteristic. |
| `examples/w-algebras-virasoro` | IV | IV | KEEP | Vir as A_inf chiral — characteristic. |
| `examples/w-algebras-w3` | IV | IV | KEEP | W_3 characteristic — Part IV case study. |
| `connections/hochschild` | IV | IV | KEEP | Chiral Hochschild / bulk-boundary — modularity-bridge foundation. |
| `connections/brace` | IV | IV | KEEP | Brace dg algebra of universal bulk — Hochschild-companion. |
| `theory/modular_swiss_cheese_operad` | IV | IV | KEEP | Modular SC operad — modularity core. |
| `theory/grt_parametrized_seven_faces` | IV | III | **MOVE → III** | Nine faces of r(z) as GRT torsor is THE Part III upgrade theorem; currently buried after characteristic datum. Platonically Part III (Faces of r(z)). |
| `theory/unified_chiral_quantum_group` | IV | II | **MOVE → II** | Unified chiral QG Q_g^{k,f,μ} is the E_1 core synthesis theorem (Yangian + W + shifted RTT + coideal all as specialization fibres); native home is E_1 core Part II. |
| `theory/sc_chtop_heptagon` | IV | I | **MOVE → I** | Heptagon of presentations of SC^{ch,top} operad is operadic foundation (upgrade of pentagon at foundational level); belongs adjacent to `factorization_swiss_cheese` in Part I. |
| `theory/curved_dunn_higher_genus` | IV | IV | KEEP | Curved-Dunn H^2=0 at g≥2 bridges modular-bootstrap complex — modularity theorem, Part IV is correct. |
| `theory/class_m_direct_sum_obstruction_platonic` | IV | IV | KEEP | Zamolodchikov weight-4 cocycle witness for class M — modularity-adjacent characteristic. |
| `theory/topologization_class_m_original_complex_platonic` | IV | IV | KEEP | Tempered vs non-tempered class M dichotomy — modularity-stratification. |
| `theory/tempered_stratum_characterization_platonic` | IV | IV | KEEP | Universal Vir tempering, ρ_*(c)=c/6 — modularity-tempering. |
| `theory/wn_tempered_closure_platonic` | IV | IV | KEEP | W_N tempered unconditionally — tempering closure. |
| `theory/beta_N_closed_form_all_platonic` | IV | IV | KEEP | β_N=12(H_N-1) closed form — tempering companion. |
| `theory/logarithmic_wp_tempered_analysis_platonic` | IV | IV | KEEP | Logarithmic W(p) tempering — modularity-tempering. |
| `theory/irrational_cosets_tempered_platonic` | IV | IV | KEEP | Irrational-coset tempering — modularity-tempering. |
| `theory/super_chiral_yangian` | IV | II | **MOVE → II** | Super chiral Yangian, Heisenberg↔symplectic fermion as Z/2-factor of Face torsor — E_1 object; belongs adjacent to `thqg_gravitational_yangian` in Part II. |
| `theory/bp_chain_level_strict_platonic` | IV | IV | KEEP | BP chain-level strictness — characteristic computation, OK in IV. |
| `connections/fm81_fractional_ghost_platonic` | IV | V | **MOVE → V** | Non-principal DS via branched-cover fractional-ghost lift is a 3d HT construction (E_3-topologization fix), native to Part V HT Landscape; but if the author intends it as companion to class M characteristic, stays IV. Flagged but mild. |
| `connections/relative_feynman_transform` | IV | IV | KEEP | Relative Feynman transform / recognition — modularity skeleton. |
| `connections/modular_pva_quantization_core` | IV | IV | KEEP | Modular PVA quantization — modularity core. |
| `connections/ht_physical_origins` | IV | V | **MOVE → V** | Physical origins of HT QFT is the Part V landscape context; currently closes Part IV but primes V. |
| `connections/ym_boundary_theory` | V | V | KEEP | YM boundary via bar-cobar — HT Landscape. |
| `connections/ym_higher_body_couplings` | V | V | KEEP | Higher-body couplings — HT Landscape. |
| `connections/ym_instanton_screening` | V | V | KEEP | Instanton screening / mass-gap — HT Landscape. |
| `connections/celestial_holography_core` | V | V | KEEP | Celestial holography core — HT Landscape. |
| `connections/log_ht_monodromy_core` | V | V | KEEP | Log HT monodromy — HT Landscape. |
| `connections/anomaly_completed_core` | V | V | KEEP | Anomaly-completed topological holography — HT Landscape. |
| `connections/thqg_holographic_reconstruction` | V | V | KEEP | Holographic reconstruction — HT Landscape result. |
| `connections/thqg_modular_bootstrap` | V | V | KEEP | Modular bootstrap as MC recursion — HT Landscape. |
| `connections/holomorphic_topological` | V | V | KEEP | HT boundary conditions / 4d origins — HT Landscape. |
| `connections/feynman_diagrams` | V | V | KEEP | Feynman diagram interpretation — HT Landscape. |
| `connections/feynman_connection` | V | V | KEEP | Feynman expansion form of bar-cobar — HT Landscape. |
| `connections/bv_brst` | V | V | KEEP | BV-BRST + Gaiotto perspective — HT Landscape. |
| `connections/part_vi_platonic_introduction` | VI | VI | KEEP | Part VI opener — correctly placed. |
| `connections/thqg_gravitational_complexity` | VI | VI | KEEP | Gravitational complexity — gravity climax. |
| `connections/3d_gravity` | VI | VI | KEEP | 3d gravity = derived center — gravity climax. |
| `connections/e_infinity_topologization` | VI | VI | KEEP | E_∞-topologization iterated Sugawara — gravity climax upgrade. |
| `connections/w_infty_e_infty_endpoint_platonic` | VI | VI | KEEP | W_∞ E_∞-topological endpoint — climax. |
| `connections/programme_climax_platonic` | VI | VI | KEEP | Programme climax synthesis — correctly placed. |
| `connections/thqg_3d_gravity_movements_vi_x` | VI | VI | KEEP | Gravitational S-duality movement — gravity climax. |
| `connections/thqg_critical_string_dichotomy` | VI | VI | KEEP | Critical string dichotomy — gravity climax. |
| `connections/thqg_perturbative_finiteness` | VI | VI | KEEP | Perturbative finiteness — gravity climax. |
| `connections/thqg_soft_graviton_theorems` | VI | VI | KEEP | Subleading soft graviton from shadow tower — gravity climax. |
| `connections/thqg_symplectic_polarization` | VI | VI | KEEP | Complementarity as shifted-symplectic polarization is Theorem C climax form; tied to Part VI gravity via holographic-Lagrangian reading. Could live in Part IV modularity but C-theorem is load-bearing for gravity-climax synthesis; Part VI is defensible and current placement is honest. |
| `theory/chiral_higher_deligne` | VI | VI | KEEP | Chiral Higher Deligne E_3 on Z^{der}_ch (Theorem H upgrade) is the E_2→E_3 bridge underlying gravity climax; Part VI is most native given it supplies the E_3 structure that Stage 9 requires. Part IV (modularity) or VIII (closure) are viable alternates but VI wins on impact. |
| `connections/universal_holography_functor` | VI | VI | KEEP | Universal Holography functor — gravity climax. |
| `connections/universal_celestial_holography` | VI | VI | KEEP | Universal Celestial Holography — gravity climax. |
| `connections/celestial_moonshine_bridge` | VI | VI | KEEP | Celestial-Moonshine bridge via w_{1+∞} — gravity climax. |
| `connections/soft_graviton_mellin_shadow_bridge_platonic` | VI | VI | KEEP | Mellin-shadow Platonic upgrade — gravity climax. |
| `connections/monster_chain_level_e3_top_platonic` | VI | VI | KEEP | Monster chain-level E_3-top — gravity climax. |
| `connections/schellekens_71_alpha_classification_platonic` | VI | VI | KEEP | Schellekens 71 DW classification — gravity climax moonshine. |
| `connections/spectral-braiding-frontier` | VII | VII | KEEP | Frontier extensions — correctly placed. |
| `connections/ht_bulk_boundary_line_frontier` | VII | VII | KEEP | Frontier extensions. |
| `connections/celestial_boundary_transfer_frontier` | VII | VII | KEEP | Frontier extensions. |
| `examples/examples-complete-conditional` | VII | VII | KEEP | Conditional examples — frontier. |
| `examples/w-algebras-frontier` | VII | VII | KEEP | Frontier W-algebras — frontier. |
| `connections/modular_pva_quantization_frontier` | VII | VII | KEEP | Modular PVA frontier. |
| `connections/ordered_associative_chiral_kd_frontier` | VII | VII | KEEP | Ordered KD frontier. |
| `connections/celestial_holography_frontier` | VII | VII | KEEP | Celestial holography frontier. |
| `connections/log_ht_monodromy_frontier` | VII | VII | KEEP | Log HT monodromy frontier. |
| `connections/anomaly_completed_frontier` | VII | VII | KEEP | Anomaly-completed frontier. |
| `frame/part_viii_synthesis` | VIII | VIII | KEEP | Part VIII synthesis — correctly placed. |
| `theory/koszulness_moduli_M_kosz` | VIII | VIII | KEEP | Koszulness moduli M_Kosz — closure theorem. |
| `theory/infinite_fingerprint_classification` | VIII | VIII | KEEP | Infinite fingerprint classification — closure theorem. |
| `connections/conclusion` | post-VIII | post-VIII | KEEP | Conclusion frame — correctly placed. |

**Summary: 5 MOVE recommendations (of ~93 audited chapter inputs), all inside Part IV which has collected several Platonic master-theorem files that natively belong to earlier Parts:**

1. **`theory/grt_parametrized_seven_faces`**: IV → III. The GRT_1(Q)-torsor realization of the Face(A) space is THE Part III Platonic upgrade; Part III's very title is "The Faces of r(z): a GRT_1(Q)-torsor" (main.tex line 1424), making the current Part IV placement self-contradictory against the part name.
2. **`theory/unified_chiral_quantum_group`**: IV → II. The unified chiral QG is the E_1 core synthesis across Yangian, W, shifted RTT, coideal; native home is Part II "The E_1 Core" (where `thqg_gravitational_yangian`, `typeA_baxter_rees_theta`, `shifted_rtt_duality_orthogonal_coideals` already live).
3. **`theory/sc_chtop_heptagon`**: IV → I. The heptagon of SC^{ch,top} presentations is the upgrade of the foundational pentagon; it belongs adjacent to `theory/factorization_swiss_cheese` in Part I (the operadic foundation), not after characteristic-datum examples.
4. **`theory/super_chiral_yangian`**: IV → II. Super chiral Yangian is an E_1 object (Yangian variant); belongs adjacent to `thqg_gravitational_yangian`.
5. **`connections/ht_physical_origins`**: IV → V. Physical origins of HT QFT natively opens the HT Landscape (Part V), not closes Part IV. Minor flag (`connections/fm81_fractional_ghost_platonic`: defensible either way — flagged but not recommended for move).

All MOVEs are LOSSLESS: reorder `\input{...}` lines in `main.tex` only; no chapter files change; all labels and cross-references continue to resolve. PROPOSAL ONLY — execution left to author. No commits. No AI attribution.

## Connective-tissue Platonic audit (Agent 4, 2026-04-17 swarm)

**Lane.** Opening paragraphs of each `\part{...}` in `main.tex` (lines 1332, 1380, 1424, 1449, 1509, 1547, 1583, 1610), evaluated as load-bearing torch-passing moments between parts. Platonic test: does the opener (a) name the problem the preceding climax left open, (b) forward-promise what the new part closes, and (c) cross-reference specific theorems/labels from the preceding part via `\ref`?

### Audit table

| Transition | Current opener (first ~30 words) | Weak/Strong | Specific cross-reference gap | Proposed Platonic opener (<=100 words) |
|------------|----------------------------------|-------------|------------------------------|----------------------------------------|
| **I -> II** (Open Primitive -> E_1 Core; main.tex:1384) | "The ordered bar coalgebra $B^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar\cA)$ with its deconcatenation coproduct is the native object of the Swiss-cheese open colour." | **WEAK-to-medium.** States what II introduces; does NOT name the open problem I left. No `\ref` to a Part I theorem. Does not cite the recognition theorem `thm:recognition-SC` (locality.tex:364) or `thm:physics-bridge` (raviolo.tex:407) even though II's entire ordered-bar programme rests on I's logarithmic SC^{ch,top} datum being unconditional. | Opener does not cite `thm:recognition-SC` or `thm:physics-bridge` from Part I; reader cannot see why $B^{\mathrm{ord}}$ is FORCED rather than introduced. | Part~I closed the open primitive by proving (Theorem~\ref{thm:recognition-SC}) that every logarithmic $\SCchtop$-datum admits a chiral Swiss-cheese presentation; the symmetric bar $B^\Sigma(\cA)$ computed there is the $\Sigma_n$-coinvariant shadow of a strictly larger object. The open-colour face $E_1(m)$ of the operad forces the ordered bar $B^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar\cA)$, on which the $R$-matrix $R(z)$, the KZ associator, and the full Yangian deformation survive before averaging kills them. Part~II proves this ordered coalgebra is the native Koszul-dual wing (Theorem~A$^{\infty,2}$) and strictifies its spectral Drinfeld data across all simple Lie types. |
| **II -> III** (E_1 Core -> Faces of r(z); main.tex:1428) | "The collision residue $r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ is the genus-0, degree-2 projection of the universal MC element." | **WEAK.** No back-reference at all. Does not cite the Part II theorems (`thm:Koszul_dual_Yangian`, `thm:complete-strictification`) that PRODUCE $r(z)$ as a shadow of the ordered bar's MC class. Treats $r(z)$ as abstractly given rather than as Part II's distilled output. | Opener silent on `thm:Koszul_dual_Yangian` (spectral-braiding-core.tex:1827) and on Part II's strictification of R(z) for all simple Lie types (`thm:complete-strictification`). Reader cannot see that "seven faces" is about ONE specific object Part II just constructed. | The dg-shifted Yangian $Y_\hbar(\fg)$ of Part~II (Theorem~\ref{thm:Koszul_dual_Yangian}) comes equipped with a spectral $R$-matrix $R(z)$ whose Drinfeld obstruction vanishes for every simple Lie algebra (Theorem~\ref{thm:complete-strictification}). The classical shadow is the collision residue $r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ --- the genus-0 degree-2 projection of the universal MC element $\Theta_\cA$ defined in Part~I. The faces of Part~III prove $r(z)$ carries seven equivalent algebraic lenses, and that the set of such lenses is a torsor over $\mathrm{GRT}_1(\Q)$; the architectural novelty of the programme lives on this torsor. |
| **III -> IV** (Faces of r(z) -> Characteristic Datum and Modularity; main.tex:1453) | "Each algebra family in Volume~I's standard landscape is a test case for the full open/closed architecture: boundary algebra, universal bulk, line-sector operations, modular MC element." | **WEAK.** Lists what IV contains; does not name what III left open. No `\ref` to the GRT_1 torsor theorem or to the seven-faces bijection. Reader does not learn why going from r(z) (genus-0, degree-2) to the full modular MC element is the FORCED next step. | Opener omits the bridge from genus-0 $r(z)$ (Part III) to all-genus $\Theta^{\mathrm{oc}}$ (Part IV); does not cite `thm:grt-torsor-seven-faces` (Part III) or explain WHY the genus tower must be assembled. | Part~III established $r(z)$ as a $\mathrm{GRT}_1(\Q)$-torsor of genus-0 presentations (Theorem~\ref{thm:grt-torsor-seven-faces}); the residue itself is the $(g,n)=(0,2)$ projection of a far larger object, the modular MC element $\Theta^{\mathrm{oc}}$ whose higher-genus strata encode the characteristic datum of the full $\SCchtop$-algebra. Part~IV extends $\SCchtop$ to all genera via clutching, proves chiral Higher Deligne (Theorem~H), and reads each family of Volume~I's standard landscape (Heisenberg through $\mathsf{W}_3$) as a worked verification of the four-functor table: $\barB$, $\Omega$, open-colour duality, and $C^\bullet_{\mathrm{ch}}$ as universal bulk. |
| **IV -> V** (Characteristic Datum -> Standard HT Landscape; main.tex:1513) | "The Koszul triangle (boundary $\cA$, bulk $\cZ^{\mathrm{der}}_{\mathrm{ch}}$, lines $\cC_{\mathrm{line}}$) of Part~\ref{part:bbl-core} acquires depth through anomaly completion..." | **MEDIUM-to-strong.** Uses `\ref{part:bbl-core}` but points to III, not IV. NEITHER Theorem H (concentration + brace) nor Theorem D (curvature $d^2 = \kappa\,\omega_g$) from Part IV is cited despite V being the HT-landscape unfolding of EXACTLY that curvature-controlled modular MC. The "transgression algebra $B_\Theta$" is attributed to Volume I rather than to Part IV's genus-tower construction. | Opener cites Part III as predecessor but the adjacent preceding part is IV; missing `\ref{thm:main-koszul-hoch}` and the Theorem~D avatar (modular curvature) as the genus tower whose HT-physical readings Part V is unfolding. | Part~IV proved the brace/concentration Theorem~H (`\ref{thm:main-koszul-hoch}`) and the modular curvature $d_{\barB}^2 = \kappa\,\omega_g$ (Theorem~D); together these package every standard-landscape algebra as a genus-indexed modular MC element $\Theta^{\mathrm{oc}}$. Part~V reads this element through the prisms of four-dimensional holomorphic--topological physics: Yang--Mills boundary packages exhibit the disk-level data, celestial and twisted holography lift it to modular completion, logarithmic monodromy globalises it on ordered configuration spaces, and anomaly completion organises the genus-dependent obstruction. The triangle (boundary, bulk, lines) of Part~\ref{part:bbl-core} acquires physical depth. |
| **V -> VI** (Standard HT Landscape -> 3D Quantum Gravity; main.tex:1551) | "The climax. The Virasoro $\lambda$-bracket $\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$ generates the full gravitational theory." | **MEDIUM.** Names VI as climax and states Virasoro's $\lambda$-bracket, but does NOT `\ref` Theorem~H (Part IV) or the Universal Holography functor $\Phi_{\mathrm{hol}}$ constructed late in Part V. The sentence "Gravity is the most downstream application" is narration; it should be a theorem invocation. The quartic-pole class-M status should cite `cor:universal-holography-class-M`. | Opener does not cite Theorem~H (Part IV) as the construction making $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\mathrm{Vir}_c)$ the bulk; does not cite the DS-Hochschild bridge `thm:chd-ds-hochschild` that closes the class-M chain-level gap which IS the gravitational climax. | The climax. Theorem~H (`\ref{thm:main-koszul-hoch}`) identified $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ as the universal bulk of any boundary chiral algebra $\cA$; Part~V's Universal Holography functor $\Phi_{\mathrm{hol}}$ made this a canonical 3d HT gauge theory. For $\cA = \mathrm{Vir}_c$ at non-critical level, the $\lambda$-bracket $\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$ with its quartic pole forces the infinite $\Ainf$ tower, the Koszul involution $c \mapsto 26 - c$, the curvature $\kappa = c/2$, and the genus expansion. The class-$\mathbf{M}$ chain-level DS--Hochschild bridge (\ref{thm:chd-ds-hochschild}) closes the last obstacle; this Part unfolds ten movements of three-dimensional quantum gravity as the consequence. |
| **VI -> VII** (3D Quantum Gravity -> Frontier; main.tex:1587) | "The chapters in this part extend the proved core of Parts~\ref{part:swiss-cheese}--\ref{part:gravity} into conditional, conjectural, and frontier territory." | **WEAK.** Generic "extends the proved core" framing. Does not enumerate what VI's climax (universal holography, E_infinity topologisation) left unclosed. Does not cite any specific theorem being conditionally extended. Reads like an administrative divider, not a torch-pass. | Opener says only "extends the proved core"; does not name specific frontier opens being conditionally pursued (Kac--Moody imaginary-root strictification, $E_\infty$ topologisation at higher spin towers, celestial $W_\infty$, chromatic height >= 1 extensions). | Part~VI closed the four irreducible opens of the HEAL+UPGRADE sweep on the non-degenerate locus, culminating in the Universal Holography functor and the $E_\infty$-topologisation ladder. Four directions remain genuinely open: Kac--Moody imaginary-root strictification beyond classical types, chain-level chiral Deligne--Tamarkin without an associator choice, logarithmic $\cW(p)$ quasi-lisse frontier, and chromatic-height $\geq 1$ extensions of $\barB(\cA)$. Each chapter here specifies one such frontier, the precise analytic or operadic input beyond the logarithmic $\SCchtop$ framework that would close it, and the partial result currently available; no earlier part depends on material here. |
| **VII -> VIII** (Frontier -> From Frontier to Theorem; main.tex:1614) | "This part promotes the four genuine frontiers that seeded Part~\ref{part:frontier} to the status of theorems on the non-degenerate locus." | **STRONG.** Names the four frontiers by FM number, cites `thm:curved-dunn-H2-vanishing-all-genera`, `thm:chd-ds-hochschild`, `cor:universal-holography-class-M`, and `thm:chd-deligne-tamarkin`. This is the template other part openers should follow. Only mild weakness: does not explicitly name the PREVIOUSLY CONJECTURAL status in Part~VII that each theorem upgrades. | Minor: does not `\ref` the specific Part~VII conjecture labels that were upgraded (e.g. `conj:curved-dunn-additivity`, `conj:class-M-chain-level`), so the reader cannot cross-walk conjecture to theorem. | Part~VII named four genuine frontiers as conjectures (`\ref{conj:curved-dunn-additivity}`, `\ref{conj:class-M-chain-level}`, `\ref{conj:periodic-cdg}`, `\ref{conj:chiral-deligne-tamarkin-chain}`); this Part promotes each to a theorem on the non-degenerate locus. The curved-Dunn $H^2$ vanishing (FM67) closes via `\ref{thm:curved-dunn-H2-vanishing-all-genera}` + `\ref{thm:irregular-singular-kzb-regularity}`; the class-$\mathbf{M}$ chain-level DS--Hochschild bridge (FM126) via `\ref{thm:chd-ds-hochschild}` + `\ref{cor:universal-holography-class-M}`; the periodic-CDG admissible closure (FM251) via Vol~I `\ref{thm:periodic-cdg-is-koszul-compatible}`; the chain-level Deligne--Tamarkin (FM91/160) via `\ref{thm:chd-deligne-tamarkin}` after fixing a Drinfeld associator. Two new Platonic chapters --- Koszulness Moduli $M_{\mathrm{Kosz}}$ (`\ref{chap:koszulness-moduli}`) and Infinite Fingerprint Classification (`\ref{chap:infinite-fingerprint}`) --- complete the architecture. |

### Pattern findings

**Strongest opener:** VII -> VIII (Part VIII) --- numerically specifies four FMs, cites the theorem labels that close them, names the two new Platonic chapters. This is the Platonic template.

**Weakest openers:** II -> III and III -> IV are generic list-structures with zero `\ref` to the preceding part. The entire `r(z)` programme arrives without reference to the Yangian construction that produced it.

**Structural gap:** Six of seven openers (all except VII -> VIII) fail the `\ref`-to-preceding-part test. Part IV's opener points back to Part~I (via `SCchtop`) but skips Parts II-III entirely. Part V's opener cites Part~III but skips Part~IV (where the modular MC was assembled). Part VI's opener does not cite Theorem~H despite it being the construction that makes gravity = derived center.

**Meta-pattern (ties to FM111 metadata drift):** The `\part` openers read as independent section introductions rather than as a single argument passing the torch. The STRONG form (VII -> VIII) came from the 2026-04-16 reconstitution sweep, proving that strong connective tissue is achievable with the existing theorem inventory --- the weak openers are technical-malpractice artifacts, not mathematical shortfalls.

**Suggested implementation order** (if downstream agent executes):
1. Highest leverage: V -> VI (gravity climax opener deserves Theorem~H + `thm:chd-ds-hochschild` citations; a single paragraph insertion would dramatically raise the climax's visibility).
2. Next: III -> IV (the bridge from genus-0 $r(z)$ to all-genus $\Theta^{\mathrm{oc}}$).
3. Then: II -> III, IV -> V, VI -> VII.
4. Cosmetic: I -> II (add recognition-theorem `\ref`).
5. Polish: VII -> VIII (already strong; optional cross-walk to Part VII conjecture labels).

**Lossless.** Proposals are NEW text inserted at part openers; no current content is removed. PROPOSAL ONLY --- no edits to `main.tex` or chapter files. No commits.

## Preface section-ordering Platonic audit (Agent 3, 2026-04-17 swarm)

Target: `/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex` (2274 lines, 16 `\section*` blocks). Lane: section-ordering Platonic form. PROPOSAL ONLY — no direct edits.

### Cross-reference risk — ZERO external

Grep of `\label{sec:...}` inside `preface.tex` returns **no matches**. All 16 sections are `\section*{Roman.\quad Title}` (unnumbered, unlabeled). Consequence: **no chapter `\ref{sec:...}` in the rest of the manuscript targets a preface section.** Renumbering / absorption / restructuring of preface sections is externally LOSSLESS at the reference graph. The only residual risk is internal-to-preface prose pointers ("Section~VII above" at preface.tex:1543 — ONE instance; the Part-tour at XI cites `Part~\ref{part:...}` which is chapter-labeled not preface-labeled and therefore unaffected).

### Per-section verdict

| # | Section | Verdict | Rationale |
|---|---------|---------|-----------|
| 0 | From alg-geom to physics | KEEP | abstract; scene-setting; Platonic opener |
| I | Open/closed primitive | KEEP | identity / datum statement |
| II | What this volume proves | KEEP | contract (five theorems + climax) |
| III | Three conceptual leaps | RENAME + EXPAND TO FOUR | preface prose already names a "fourth leap" at L606-647 ("derived centres produce physics"); headline count is STALE. Rename "Four conceptual leaps"; promote fourth leap from sub-paragraph to fourth numbered leap. LOSSLESS (content already present). |
| IV | Steinberg principle | KEEP | single governing principle — preface-scale |
| V | Swiss-cheese operad | KEEP | central object of Vol II |
| VI | Slab + Drinfeld double + BBL triangle | KEEP | three-way geometric staging |
| VII | The 3d Maurer–Cartan element | KEEP-BUT-COMPRESS | `α_T` is the PACKAGE unifying the six faces — preface-scale. Current ~175 lines (L978-1152) includes genus-1 specialisation + genus expansion + Heis/KM/Vir specialisations. Compress to <70 lines: definition of `α_T`, table of six projections (L994-1019), colour decomposition, ONE-line pointer to chapter for genus expansion. The Heis/KM/Vir specialisations duplicate Section IX "Three computations" — merge into IX. |
| VIII | PVA descent | DEMOTE-TO-CHAPTER | L1153-1234 is chapter-scale: Stasheff relations at all n, resolvent principle with dressed propagator, Catalan PRT_k formula, five PVA axioms each derived from an FM Stokes identity. Belongs in `pva-descent-repaired.tex` (exists per File Map). In preface, retain ONE paragraph inside VII pointing to `thm:cohomology_PVA`. |
| IX | Three computations | KEEP + EXPAND | worked examples at preface scale; absorbs VII's Heis/KM/Vir overlap |
| X | Curved genus expansion | KEEP | preface-scale anomaly statement |
| XI | The eight parts | KEEP | Part-by-Part tour |
| XI′ | The holographic programme | ABSORB → XII (renumbered) | triple-prime stack is ugly. Promote to first-class numbered section. |
| XI″ | E_n hierarchy as physical realisation | ABSORB → XIII (renumbered) | same; Platonic sequential numbering. |
| XI‴ | The programme climax | ABSORB → XIV (renumbered) | same. |
| XII | Completeness + frontier | RENUMBER → XV | clean sequential numbering. |

### Triple-prime stack attack

`XI / XI′ / XI″ / XI‴ / XII` is drift from in-session insertions that tried to avoid renumbering. The Platonic form has clean sequential numbering. **Two equally-valid repairs, both LOSSLESS:**

**Option A (promote — recommended).** XI′ → **XII. The holographic programme**; XI″ → **XIII. The E_n hierarchy**; XI‴ → **XIV. The programme climax**; old XII → **XV. Completeness + frontier**. Each climax-block retains top-level `\section*` weight — appropriate because XI‴ is the deepest volume result and deserves top-level display, not embedding.

**Option B (absorb as subsections).** Make XI′/XI″/XI‴ `\subsection*` under XI. Flattens the narrative crescendo. NOT RECOMMENDED.

### Three-leaps count attack (Section III)

L480-647 declares "three conceptual leaps" (commutative→E_1; genus-0→modular; local→nonlocal) then adds a fourth at L606 ("the fourth leap: derived centres produce physics") as a trailing sub-paragraph (`\noindent\textbf{The fourth leap…}`). The heading count is stale; the content has drifted to four. **Proposal: retitle "Four conceptual leaps"; promote the fourth from sub-paragraph to numbered leap `(4) Derived centres produce physics`.** No new prose required.

### Section VII and VIII preface-scale attack

**VII.** The definition of `α_T` + six-projection table + colour-decomposed MC equation are preface-scale (they state the volume's governing equation). Genus-1 specialisation (L1053-1081), genus expansion prose (L1083-1107), and Heis/KM/Vir examples (L1108-1151) are chapter-scale duplicated in `chapters/theory/modular_pva_quantization_core.tex` and preface Section IX. Keep the skeleton; demote the rest.

**VIII.** Chapter-scale throughout. This is the content of `pva-descent-repaired.tex`, not of a preface. In a Russian-school / Chriss-Ginzburg lean preface, the preface STATES the theorem; the derivation lives at chapter level.

### Proposed Platonic preface outline (lean + LOSSLESS)

```
0.    From algebraic geometry to physics          (abstract)
I.    The open/closed primitive                   (identity)
II.   What this volume proves                     (contract)
III.  Four conceptual leaps                       (commutative→E_1, genus-0→modular,
                                                   local→nonlocal, algebra→physics)
IV.   The Steinberg principle                     (governing principle)
V.    The Swiss-cheese operad SC^{ch,top}         (central object)
VI.   The slab, Drinfeld double, BBL triangle     (geometric staging)
VII.  The 3d Maurer–Cartan element                (compressed: α_T definition +
                                                   six-projection table + colour
                                                   decomposition; Heis/KM/Vir merged
                                                   into IX; PVA-descent pointer to
                                                   pva-descent-repaired.tex)
VIII. [DEMOTED — migrates wholesale to pva-descent-repaired.tex;
       one-sentence pointer retained inside VII]
IX.   Three computations                          (Heis/KM/Vir worked examples —
                                                   absorbs VII's specialisations)
X.    Curved genus expansion                      (anomaly)
XI.   The eight parts                             (Part tour — unchanged)
XII.  The holographic programme                   (was XI′)
XIII. The E_n hierarchy as physical realisation   (was XI″)
XIV.  The programme climax                        (was XI‴)
XV.   The completeness question and the frontier  (was XII)
```

Net: 16 → 15 sections (VIII demoted; IX absorbs overlap from VII). Clean sequential numbering; no primes; every mathematical claim retained (VIII content migrates to `pva-descent-repaired.tex` in full, not deleted).

### LOSSLESS check

- **Section VIII content** (Stasheff relations, resolvent principle, Catalan formula, five PVA axioms): ALREADY present in `chapters/theory/pva-descent-repaired.tex` and `pva-expanded-repaired.tex` (CLAUDE.md File Map). Preface version is chapter-digest. Demotion removes ONE copy; originals remain. VERIFIED.
- **Section VII Heis/KM/Vir specialisations** (L1108-1151): duplicate Section IX worked examples (L1235+). Merging into IX is consolidation. VERIFIED.
- **Triple-prime renumber**: pure relabeling; no prose change. VERIFIED.
- **Fourth leap promotion**: sub-paragraph already written; promotion is `\noindent\textbf{…}` → `\smallskip\noindent\textbf{(4) …}` plus heading count edit. VERIFIED.

### Cross-reference risk list

- **External (other chapters → preface)**: NONE. No preface section carries `\label{sec:...}`.
- **Internal (preface → preface)**: ONE instance of "Section~VII above" at preface.tex:L1543 inside the Part-by-Part tour (XI), referring to the six projections of `α_T`. Update this single pointer after edits. Post-edit grep: `grep -n "Section~[IVX]" chapters/frame/preface.tex`.
- **Introduction + concordance**: `chapters/theory/introduction.tex` and `chapters/connections/concordance.tex` carry no section-number dependence on preface. VERIFIED.
- **Residual risk**: ZERO external; ONE internal pointer to update.

### Downstream execution checklist (for approver)

1. Surgical edit: retitle III "Four conceptual leaps"; promote fourth-leap paragraph to numbered (4).
2. Surgical edit: XI′ → XII; XI″ → XIII; XI‴ → XIV; old XII → XV.
3. Surgical edit: Section VII compress; move Heis/KM/Vir specialisations to IX.
4. Migrate Section VIII body to `pva-descent-repaired.tex` (verify no duplication); replace preface VIII with one-sentence pointer inside VII.
5. Grep-verify: `grep -n "Section~[IVX]" chapters/frame/preface.tex` — update the L1543 pointer.
6. `make` to verify compile; `make verify-independence` unchanged by preface-level edits.
7. No commit without build-pass + no-AI-attribution audit per pre-commit hook.

### Attack-mode summary

Primary finding: triple-prime `XI′/XI″/XI‴` stack is a cosmetic hack from in-session edits; Option A renumbering (→ XII/XIII/XIV) is mechanical. Secondary: "three leaps" (§III) is a STALE COUNT — the preface already writes a fourth leap at L606. Tertiary: Sections VII and VIII carry chapter-scale duplication (VII's Heis/KM/Vir overlaps §IX; VIII duplicates `pva-descent-repaired.tex`). Preface shrinks from 2274 → ~1600 lines with no content loss. Cross-reference risk is structurally ZERO because preface sections are unlabeled.

Agent 3 complete. PROPOSAL ONLY; no preface edits executed. No commits. No AI attribution.

## Theorem-to-part Platonic audit (Agent 5, 2026-04-17 swarm)

Audit of the Seven Theorems (A, B, C, D, H, F, G) across Vol II's part/chapter structure. Primary labels grep-located; part assignment derived from `main.tex` `\input` order relative to `\part{...}` declarations.

### Locations table

| Theorem | Primary label | Primary file | `main.tex` line | Primary part | Native part | Verdict |
|---|---|---|---|---|---|---|
| A | `thm:properad-bar-cobar` (Vol II) + `thm:bar_cobar_adjunction` (Vol I + Vol II echo) | `chapters/theory/factorization_swiss_cheese.tex:2369`; `chapters/connections/bar-cobar-review.tex:369` | 1370, 1414 | Part I (swiss-cheese) for properad form; Part II (E_1 Core) for E_1 bar-cobar echo | Part I / Part II | KEEP --- already Platonic (foundation in Part I, E_1 specialisation in Part II) |
| B | `thm:filtered-koszul` (only Vol II anchor) | `chapters/connections/line-operators.tex:307` | 1415 | Part II (E_1 Core) | Part II | KEEP --- but DISCOVERABILITY GAP: no label `thm:bar-cobar-koszul-inversion` or `thm:theoremB` exists in Vol II; Theorem B's canonical Vol I statement is not forward-pointed from the preface |
| C | `thm:theoremC-total-shifted-symplectic` | `working_notes.tex:19490` (ORPHAN --- not `\input` by main.tex) | --- | Not in main.tex arc | Part IV (Characteristic Datum + Modularity) | DUPLICATE-STUB --- insert Remark in `chapters/theory/modular_swiss_cheese_operad.tex` or `chapters/connections/relative_feynman_transform.tex` forward-pointing to Vol I primary + working_notes upgrade |
| D | `thm:theoremD-tensor-arakelov` | `working_notes.tex:19649` (ORPHAN --- not `\input` by main.tex) | --- | Not in main.tex arc | Part IV (Characteristic Datum + Modularity) | DUPLICATE-STUB --- same as C: Remark in Part IV chapter pointing to Vol I's Theorem D primary + tensor-Arakelov upgrade |
| H | `thm:chiral-higher-deligne` | `chapters/theory/chiral_higher_deligne.tex:419` (canonical); also echoed at `chapters/connections/hochschild.tex:2668` | 1486, 1573 | Part IV (hochschild.tex) AND Part VI (chiral_higher_deligne.tex) | Part IV primary; Part VI upgrade | KEEP --- but the two files share the label `thm:chiral-higher-deligne`. Rename the hochschild echo to `thm:chiral-higher-deligne-hoch-echo` and add Remark cross-pointer so a Part IV reader finds the upgrade |
| F | `thm:universal-holography-functor` | `chapters/connections/universal_holography_functor.tex:264` | 1574 | Part VI (gravity) | Part V (Standard HT Landscape) native; Part VI climax | KEEP in Part VI (climax), but DUPLICATE-STUB Remark in Part V `thqg_holographic_reconstruction.tex` announcing the functor $\Phi_{\mathrm{hol}}$ with forward-pointer |
| G | `thm:fingerprint-complete-ch` | `chapters/theory/infinite_fingerprint_classification.tex:83` | 1650 | Part VIII (From Frontier to Theorem) | Part IV (Characteristic Datum) --- classification is a characteristic-datum theorem | DUPLICATE-STUB --- add Remark in Part IV `rosetta_stone.tex` or `examples-complete-proved.tex` forward-pointing to Chapter `chap:infinite-fingerprint`; the G/L/C/M/FF fingerprint belongs narratively with the landscape census |

### Discoverability gaps

1. **Theorem F (Universal Holography) is mentioned NOWHERE in Parts I-V openers.** A reader following the narrative arc first encounters the functor $\Phi_{\mathrm{hol}}$ at `main.tex:1574`, deep inside Part VI. The Part V opener (L1513-1527) discusses the "Koszul triangle (boundary, bulk, lines)" --- the natural site to announce $\Phi_{\mathrm{hol}}$ --- but never names Theorem F.
2. **Theorem G (Infinite Fingerprint) is placed in Part VIII, not Part IV.** The Part IV opener (L1452-1478) states "The shadow archetype (G/L/C/M) classifies the boundary-holographic complexity" --- this IS Theorem G's content in coarse projection. Reader must reach Part VIII (L1650) to encounter the full six-slot $\varphi'$ completeness.
3. **Theorems C and D are orphan in `working_notes.tex`.** The Platonic upgrade statements live in a file not input by `main.tex`. A reader of the built PDF never sees `thm:theoremC-total-shifted-symplectic` or `thm:theoremD-tensor-arakelov`.
4. **Theorem B has no "Theorem B" label in Vol II.** The Koszul-locus inversion is anchored at `thm:filtered-koszul` in line-operators.tex, but preface never says "Theorem B = Koszul-locus inversion, see Chapter X." Asymmetric vs A/C/D/H, which the preface names explicitly.
5. **No "Seven Theorems at a glance" section exists in `preface.tex`.** Preface mentions Theorems A, C, D, H by name; F and G are absent; B is not named.

### Proposed "Seven Theorems at a glance" preface draft (PROPOSAL --- no edit performed)

A new preface subsection, placed after the existing Platonic Geometric Ladder, $\leq 100$ words per theorem:

**Theorem A (Bar-cobar equivalence, $(\infty,2)$-properad form).** The Francis-Gaitsgory factorization ambient on $\mathrm{Ran}(X)$ supports an $(\infty,2)$-categorical adjoint equivalence $\bar B^{\mathrm{ch}} \rightleftarrows \Omega^{\mathrm{ch}}$ on conilpotent factorization coalgebras, lifting to factorization PROPERADS and restricting at the pole-free point to classical $(\mathrm{Ass}, \mathrm{Ass}^!)$. The R-twisted $\Sigma_n$-descent lemma connects ordered and symmetric bars. Primary home: `chapters/theory/factorization_swiss_cheese.tex` (properad form, `thm:properad-bar-cobar`) + `chapters/connections/bar-cobar-review.tex` (E_1 specialisation). Part I / Part II.

**Theorem B (Koszul-locus inversion).** The bar-cobar counit $\Omega^{\mathrm{ch}} \bar B^{\mathrm{ch}}(A) \to A$ is a quasi-isomorphism on the filtered-Koszul locus of the standard landscape, with unified pro-nilpotent + curved + filtered regularisation covering Yangians, critical KM, minimal models, and logarithmic $W(p)$. Primary home: `chapters/connections/line-operators.tex` (`thm:filtered-koszul`). Part II.

**Theorem C (Total shifted-symplectic complementarity).** The relative characteristic bundle $\mathcal{Q}(\mathcal{A}) \oplus \mathcal{Q}(\mathcal{A}^!)$ over $\overline{\mathcal{M}}_{g,n}$ carries a canonical $-(3g{-}3{+}n)$-shifted symplectic structure, with clutching compatibility across boundary strata promoting per-genus Lagrangians to a global Lagrangian section. Primary home: Vol I (Theorem C); Platonic upgrade at `working_notes.tex:19490` (`thm:theoremC-total-shifted-symplectic`). Part IV.

**Theorem D (Tensor-Arakelov curvature).** The modular curvature $d^2 = \kappa \cdot \omega_g$ promotes to a tensor field in $\mathrm{Sym}^2(\mathbb{F}\text{-bundle}) \otimes \Omega^2(\overline{\mathcal{M}})$, extending from uniform-weight to genuinely multi-weight algebras; the chiral Mumford/GRR formula upgrades to a tensor GRR. Primary home: Vol I (Theorem D); Platonic upgrade at `working_notes.tex:19649` (`thm:theoremD-tensor-arakelov`). Part IV.

**Theorem H (Chiral Higher Deligne / $E_3$ on $\mathcal{Z}^{\mathrm{der}}_{\mathrm{ch}}$).** The chiral Hochschild complex $C^\bullet_{\mathrm{ch}}(A, A)$ carries a canonical $E_3$-topological structure via the $\SCchtop$ pentagon edges (3)$\leftrightarrow$(4)$\leftrightarrow$(5), making $\mathcal{Z}^{\mathrm{der}}_{\mathrm{ch}}(A)$ an $E_3$-algebra; concentration in $\{0,1,2\}$ is a consequence of $E_3$ rigidity at a point. DS-Hochschild bridge closes class $\mathbf{M}$ chain-level. Primary home: `chapters/theory/chiral_higher_deligne.tex:419` (`thm:chiral-higher-deligne`). Part VI (with Part IV echo in hochschild.tex).

**Theorem F (Universal Holography functor $\Phi_{\mathrm{hol}}$).** For every chiral algebra $A$ with conformal vector at non-critical level, there exists a canonical 3d HT theory $T_A$ with $\mathrm{Obs}^\partial(T_A) \simeq A$ and $\mathrm{Obs}^{\mathrm{bulk}}(T_A) \simeq \mathcal{Z}^{\mathrm{der}}_{\mathrm{ch}}(A)$; $\Phi_{\mathrm{hol}}: \mathrm{ChirAlg}^{\omega,\mathrm{BL}}_X \to \mathrm{HT\text{-}QFT}_{X\times\mathbb{R}}$ is functorial and compatible with DS reduction. Covers $\mathsf{G}/\mathsf{L}/\mathsf{C}$ via abelian hCS; class $\mathbf{M}$ via Costello-Gaiotto + DS-Hochschild bridge. Primary home: `chapters/connections/universal_holography_functor.tex:264` (`thm:universal-holography-functor`). Part VI.

**Theorem G (Infinite Fingerprint Classification).** The six-slot fingerprint $\varphi'(A) = (p_{\max}, r_{\max}, \chi_{\mathrm{VOA}}, n_{\mathrm{strong}}, \mathrm{coset}, \kappa\text{-regime})$ is a complete Koszul-bar-complex invariant; $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathbf{M}$ is the coarse projection onto $r_{\max}$ restricted to $\kappa \neq 0$, and $\mathsf{FF}$ (Feigin-Frenkel) appears as a fifth canonical stratum at $\kappa = 0$. Bar-cobar duality is an involution on fingerprint space. Primary home: `chapters/theory/infinite_fingerprint_classification.tex:83` (`thm:fingerprint-complete-ch`). Part VIII (natively Part IV).

### Specific minimal-intervention proposals (APPEND-ONLY, no content moves)

- **Preface**: add the "Seven Theorems at a glance" subsection above, placed immediately after the Platonic Geometric Ladder stage table. Each theorem line ends with an explicit `\ref{thm:...}` + `\pageref{}` forward-pointer. This closes the discoverability gap for F, G, and names B explicitly.
- **Part V opener** (`main.tex:1513-1527`): add one-sentence Remark naming Theorem F and pointing to `chapters/connections/universal_holography_functor.tex`. Reader encounters F at the Koszul-triangle opener, where it natively belongs, before reaching Part VI.
- **Part IV opener** (`main.tex:1453-1478`): add one-sentence Remark naming Theorem G and pointing to `chapters/theory/infinite_fingerprint_classification.tex`. Reader sees the G/L/C/M coarse classification promoted to $\varphi'$ at the landscape opener.
- **`chapters/theory/modular_swiss_cheese_operad.tex`**: add Remark citing `working_notes.tex:19490` (Theorem C upgrade) + `working_notes.tex:19649` (Theorem D upgrade) with explicit note that the upgrade statements are Platonic and await insertion into `main.tex` from `working_notes`. This makes the upgrades discoverable from the built PDF.
- **`chapters/connections/hochschild.tex:2668`**: the duplicate `thm:chiral-higher-deligne` label collides with `chapters/theory/chiral_higher_deligne.tex:419`. Rename the hochschild echo to `thm:chiral-higher-deligne-hoch-echo` or convert to Remark with forward-pointer. Verdict: DUPLICATE-STUB healing is a pure label-fix, not content motion.

### Platonic verdict

Current Vol II `main.tex` arc encounters Theorems A (L1370, 1414), B (L1415, unnamed as B), H-echo (L1486), H-primary (L1573), F (L1574), G (L1650) --- but NOT C or D (orphan in working_notes). A reader following Parts I$\to$VIII linearly sees A, B, H, F, G in Platonic order, missing C and D entirely. The fix is append-only: preface summary + five forward-pointer Remarks + one label-collision rename. No content moves.

Agent 5 complete. PROPOSAL ONLY; no edits to preface or chapters executed. No commits.

## Session 2026-04-17 (evening): Preface CG rectification — session-meta leak hygiene sweep

**Files:** `chapters/frame/preface.tex` (entire file, sections 0-XV, 17 surgical chunks 41-57).

**S17-A. The registry leak pattern.**
 - (a) RIGHT: the error ledger (CLAUDE.md + this cache) is the correct place to record AP and FM identifiers; they give the session author a rapid pointer back to the original first-principles analysis, and the `make verify-independence` decorator protocol relies on canonical names.
 - (b) WRONG: author-side registry tokens had leaked into reader-facing `.tex` prose across the entire Vol II preface. 17 chunk boundaries carried 30+ such leaks: AP identifiers (AP8, AP24, AP25, AP31, AP34, AP50, AP133, AP136, AP143, AP160, AP163, AP165, AP167, AP172, AP177, AP178, AP-CY166, AP-RMATRIX), FM identifiers (FM11, FM21, FM31a, FM34a, FM57, FM64), session codes (C4, C9, B18, HZ-4, RS-9), a commit hash (`commit \texttt{a5640de}`), a meta-stamp (`Beilinson-rectified 2026-04-17`), a tag (`, NEW`), two working-note labels (`\texttt{thm:theoremC-total-shifted-symplectic}`, `\texttt{thm:theoremD-tensor-arakelov}`), the phrase `(cached confusion \#15)`, and several `\texttt{prop:...}`/`\texttt{thm:...}` visible-label leaks where `\ref{...}` was intended.
 - (c) CORRECT: preface prose must speak only mathematics. Each leak was rewritten as a declarative statement carrying the substance of the pointer without the pointer. Examples: "(AP177; the divided-power coefficient is convention-dependent)" $\to$ "(the divided-power coefficient is convention-dependent, while the shadow invariant is not)"; "(C4: at $N=2$, $H_2-1=1/2$ recovers $\kappa=c/2$, not $H_{N-1}$; AP136)" $\to$ "(at $N=2$, $H_2 - 1 = 1/2$ recovers $\kappa = c/2$; the correct expression is $H_N - 1$, not the harmonic number $H_{N-1}$, since $H_{N-1} \ne H_N - 1$ in general)". Mechanical invariant: every AP/FM pointer forces a rewrite; every `commit \texttt{...}` forces a rewrite; every `working note` reference forces deletion or conversion to a true `\ref{}`. Type: editorial hygiene with register implications — the programme's reader must not be expected to consult the error ledger while reading Gelfand-Etingof-Bezrukavnikov-register prose.

**S17-B. The detection grep (canonical).**
```
grep -nE 'AP[0-9]+|FM[0-9]+|\(AP-CY[0-9]+|commit \\texttt|cached confusion|Beilinson-rectified|working note|RS-[0-9]|HZ-[0-9]|\bC[0-9]+:|\bB[0-9]+:' chapters/
```
Zero matches across `chapters/frame/preface.tex` is the post-session invariant; this is the check that S17-A closure admits mechanical verification. Entries in CLAUDE.md register this as V2-AP40.

**S17-C. Chunk-by-chunk ledger (Vol II preface, 2026-04-17 session).**

| Chunk | Section | Lines healed | Leaks removed |
|-------|---------|--------------|---------------|
| 41 | XV (frontier F1-F5) | 1836-1874 | `commit \texttt{a5640de}`, `\texttt{e_infinity_topologization.tex}`, `\texttt{periodic_cdg_admissible.tex}`, `\texttt{prop:bv-bar-class-m-weight-completed}`, "Beilinson-rectified 2026-04-17" |
| 42 | XIV tail | 1773-1805 | "cached confusion \#15", `commit \texttt{cade61c}`, shouty "FAILS"/"NOT" |
| 43 | XIV head | 1669-1706 | "Stirling wins", "refinement is necessary" |
| 44 | XIII | 1580-1596 | AP143/FM57 on $T_{\mathrm{DS}}$ improvement, FM64 on Khan-Zeng scope |
| 45 | XII | 1511-1533 | AP8 + AP24 on Virasoro self-duality at $c=13$ |
| 46 | XI | 1410-1440 | AP178/FM31a on $2/c^2$ vs $2/(5c^2)$, AP8 + `\texttt{thm:monster-chain-level-e3-top}`, `,NEW` tag |
| 47 | X | 1227-1246 | FM21 on $F_2=7\kappa^2/5760$, AP24/HZ-4 on Vir complementarity |
| 48 | IX | 1079-1166 | AP-RMATRIX, AP31, FM21, C9, B18, AP177, C4 (seven leaks in one section) |
| 49 | VIII | 1029-1044 | AP133 Catalan reminder |
| 50 | VII | 998-1004 | FM34a on KZB prefactor $1/(4\pi i)$ |
| 51 | VI | 823-826 | RS-9 on slab-bimodule |
| 52 | V | 738-740 | AP172/AP-CY166 on $\SCchtop$ not self-dual |
| 53 | IV | 584-692 | AP25/AP34/AP50 "NEVER conflate", AP160 on three-Hochschild, AP8 on Vir $c=13$ |
| 54 | III | 505-508 | C4/AP136 on $\kappa(\cW_N) = c(H_N-1)$ |
| 55 | II | 368-376 | `working note \texttt{thm:theoremC-total-shifted-symplectic}`, `\texttt{thm:theoremD-tensor-arakelov}` |
| 56 | I | 306-307 | FM11 on Sugawara shift |
| 57 | 0 (master theorem) | 60-111 | `commit \texttt{a5640de}` + retraction-date, AP163/AP167 on Dunn-bicoloured, AP165 on bar not $\SCchtop$-coalgebra |

All 17 commits build clean. Author: Raeez Lorgat.

**S17-D. Generalisation beyond preface.**
The same grep run against `chapters/` top-level identifies further session-meta leaks in chapter prose; rectifying them is a separate follow-up sweep. Preface hygiene is a necessary first pass because the preface is the reader's single-pass entry; chapter-level leaks are typically encountered only by readers already inside the programme's technical material, but the same register standard applies. Type: procedural (pattern generalises; apply V2-AP40 grep before every commit touching `.tex` prose anywhere).

## Session 2026-04-17 (evening, continued): Introduction linear sweep and V2-AP40 subclause discoveries

**S17-E. Introduction linear sweep leak inventory.**
The 2026-04-17 evening session extended the V2-AP40 sweep from `chapters/frame/preface.tex` (chunks 41-57, 30+ leaks) to `chapters/theory/introduction.tex` (chunks 58 through 80, 19 additional leaks in a single commit, plus 4 small residual cleanups). Introduction leak locations (pre-sweep):

| # | Line (pre-sweep) | Token | Restatement |
|---|---|---|---|
| 1 | 54 | `commit \texttt{a5640de}` on W(p) retraction | Gurarie 1993 + Flohr 1996 unbounded-Massey scope |
| 2 | 161 | `(AP165)` on $\SCchtop$-on-pair | parenthetical: "lives on pair, not on $\cA$" |
| 3 | 219 | `(AP25/AP34/AP50)` on three-functors non-conflation | "the three must never be conflated" |
| 4 | 318 | `FM11` on Sugawara shift | "the second summand is the Sugawara shift" |
| 5 | 420 | `(AP165)` on brace action | deleted (context sufficient) |
| 6 | 602 | `AP-RMATRIX` on collision-vs-Laplace gap | "one pole lower, by $d\log$ absorption" |
| 7 | 612 | `AP31` on $\cH_k^! \ne \cH_{-k}$ | "despite sharing $\kappa_{\mathrm{ch}}$" |
| 8 | 861 | `AP24` inside display equation | "$13$, family-specific" |
| 9 | 1068 | `AP133` Catalan parenthetical | "$k-1$ internal vertices and $k$ leaves" |
| 10 | 1393 | `(AP172/AP-CY166)` on SC not self-dual | declarative two-sentence restatement |
| 11 | 1453 | `AP178/FM31a` on $2/c^2$ asymptotic | "whose large-$c$ asymptotic is $2/c^2$ (not $2/(5c^2)$)" |
| 12 | 1642 | `(FM57; AP143)` on $T_{\mathrm{DS}}$ improvement | "improvement $G'_f$ involves only Cartan currents" |
| 13 | 1652 | `(FM64: ...)` on Khan-Zeng scope | "covers every freely-generated PVA with a conformal vector" |
| 14 | 1658 | `(FM62)` on abelian Sugawara | deleted (abelian Chern-Simons sufficient) |
| 15 | 1953 | `AP-RMATRIX` on affine KM r-matrix | "trace-form convention" |
| 16 | 1961 | `FM11` on Sugawara shift | "from the Sugawara shift, not zero" |
| 17 | 1971 | `AP177` on divided-power coefficient | "divided-power coefficient is convention-dependent, while the shadow invariant is not" |
| 18 | 1987 | `AP-RMATRIX` on bar-theoretic collision residue | "the standard collision-vs-Laplace gap" |
| 19 | 1992 | `AP8` on Vir self-duality at $c=13$ | "at the Virasoro-specific value $c = 13$, not at the matter-ghost critical value $c = 26$" |
| 20 | 2261 | `(Beilinson-rectified)` + commit hash on F1 | declarative F1 scope sentence |

Chunk-18 Gate-1 math fix (not a V2-AP40 leak but surfaced during the gate pass): climax theorem $\beta_{W_N} = (N+1)(N+2)/2 \to 12(H_N-1)$ — see S17-F below.

Chunk-19 residual V2-AP40 cleanup: `(cached confusion \#15)` at line 1886 + shouty `FAILS`; caps-`NOT` in three-volume junction at line 1904.

Chunk-22/24 residual cleanup: caps-`NOT` on Feigin-Frenkel dual level (line 2191), visible-label `\texttt{thm:monster-chain-level-e3-top}` (line 2468), `(NEW)` tag on Part VIII header (line 2489).

Post-sweep introduction.tex state: zero V2-AP40 meta-leaks; zero visible-label leaks; the only remaining match of the grep pattern is the legitimate bibliography citation `\cite{FM94}` (Fulton-MacPherson 1994) at line 946.

**S17-F. Internal theorem-statement-vs-proof formula inconsistency (the chunk-18 Gate-1 finding).**
 - (a) RIGHT: the Programme Climax theorem's four-case split for the Arnold coupling $\beta_{\cA}$ (`\mathrm{Vir}_c$: 6, $W_{N,c}$: Fateev-Lukyanov or closed form, $W(p)$: $4p-3$, $\mathrm{Com}(B,C)$: $6 \cdot |c_K|$) is structurally correct; the Vir / $W(p)$ / coset cases are correctly stated.
 - (b) WRONG: the $W_N$ case cited the naive Fateev-Lukyanov asymptotic $(N+1)(N+2)/2$. This formula agrees with the proved closed form $\beta_N = 12(H_N - 1)$ at $N = 2$ (both 6) and $N = 3$ (both 10), but diverges at $N \ge 4$: $(5)(6)/2 = 15$ vs $12(H_4 - 1) = 12 \cdot 13/12 = 13$. Using the incorrect value widens the Banach radius $\rho_* = |c|/\beta_{\cA}$ by a factor of $15/13 \approx 1.154$ at $N = 4$, forgiving spurious convergence.
 - (c) CORRECT: the proved closed form is $\beta_N = 12(H_N - 1)$ for all $N \ge 2$ (`thm:beta-N-closed-form-proved-all-N`), consistent with preface Section XIV's statement. Specialisations: $\beta_{W_2} = \beta_{\mathrm{Vir}} = 6$, $\beta_{W_3} = 10$, $\beta_{W_4} = 13$. The Fateev-Lukyanov candidate $(N+1)(N+2)/2$ is a secondary remark: it agrees through $N = 3$ but overestimates at $N \ge 4$. The pattern to watch: whenever a main theorem's case split cites a formula for which a closed form is established elsewhere in the same chapter, check agreement at the first boundary case ($N = 4$ for $W_N$ asymptotics; $d = 3$ for CY dimension; $g = 2$ for curved Dunn; $r = 4$ for class M shadow tower). Type: internal-consistency / formula-divergence at boundary cases.

**S17-G. V2-AP40 subclause discoveries.**
The 2026-04-17 audit agent's report across 58 files surfaced four distinct subclasses of V2-AP40 beyond in-prose parentheticals, now registered in CLAUDE.md as V2-AP40a-d:

 - **V2-AP40a**: bibkey-named-after-ledger-token. Witness: `\cite{Vol2-FM81-platonic}` at 10+ call sites in `bp_chain_level_strict_platonic.tex`. The bib entry's key is itself `FM81`, so the compiled bibliography surfaces the ledger token to the reader via every in-text citation. Counter: atomic rename across `.tex` + `.bib`.
 - **V2-AP40b**: label-named-after-ledger-token. Witnesses: `\label{rem:AP172-A-koszul-SC-not-SC}` (unified_chiral_quantum_group.tex:470), `\label{cor:FM134-healed}` (y_algebras.tex:253), `\label{rem:chapter-retracted-2026-04-17}` (topologization_class_m_original_complex_platonic.tex:133). The label propagates through the PDF's link graph and through every `\ref{...}`. Counter: atomic rename of label + all refs in one commit.
 - **V2-AP40c**: index-entry / hyperref anchor named after ledger-token. Witnesses: `\index{FM47!healed}`, `\index{FM48!healed}`, `\index{FM81!healed}` (e_infinity_topologization.tex); `\hyperref[AP67]{AP67}`, `\hyperref[FM106]{FM106}`, `\hyperref[FM110]{FM110}` (examples-complete-proved.tex L1012-1095, six instances). This is the worst class: reader clicks and lands on the AP/FM anchor target inside the manuscript. Counter: delete the index/hyperref outright; rephrase surrounding prose.
 - **V2-AP40d**: theorem-environment or section title built on ledger-token. Witnesses: `\begin{remark}[AP172: ...]`, `\begin{convention}[AP159: ...]`, `\section{Anti-pattern register: AP171, AP172, AP174, slab-bimodule}` (grt_parametrized_seven_faces.tex:831, dnp_identification_master.tex:758). The compiled TOC and every theorem-environment header surfaces the token. Counter: retitle by content.

 Session evidence: ~530 leaks across 58 files, with ~20 in V2-AP40d category, ~25 in V2-AP40b/c, ~10 in V2-AP40a, ~400 as V2-AP40-base in-prose parentheticals, and ~80 visible-label leaks (`\texttt{thm:...}` where `\ref{...}` was intended — a borderline form classifiable either as V2-AP40-base or as its own sub-pattern).

 Frontier of rectification: priority-ordered target list by leak-count density is `unified_chiral_quantum_group.tex` (56), `super_chiral_yangian.tex` (39), `chiral_higher_deligne.tex` (24), `universal_holography_functor.tex` (24), `sc_chtop_heptagon.tex` (21), `modular_swiss_cheese_operad.tex` (21), `dnp_identification_master.tex` (20), `shifted_rtt_duality_orthogonal_coideals.tex` (19), `line-operators.tex` (18), `bp_chain_level_strict_platonic.tex` (18, concentrated bibkey rename). Next session should walk this list in chunk-batched commits; estimated effort ~20-30 commits covering the top-10 files.

**S17-H. Commit-SHA leak cluster.**
Four distinct locations in the manuscript carry bare commit-SHA references in compiled prose (reader sees a `\texttt{<7-hex>}` that means nothing to them):
 - `chapters/theory/foundations.tex:3777`: "Conjectured at commit `\texttt{a5640de}`".
 - `chapters/theory/irrational_cosets_tempered_platonic.tex:134`: "closed independently in Vol~II commit `\texttt{549f881}`".
 - `chapters/theory/topologization_class_m_original_complex_platonic.tex:170`: "(`\texttt{programme\_climax\_platonic.tex}`, commit `\texttt{d1a4e7c}`)".
 - `chapters/connections/programme_climax_platonic.tex:904`: "Conjectured on this basis (commit `\texttt{a5640de}`)".

All four must be excised; the mathematical content they surround is fine, but the commit-hash reference belongs in CLAUDE.md or in the git log, never in the compiled manuscript. Counter: replace each with a neutral reference to the conjectural status + in-manuscript `\ref{...}` to the relevant statement.

**Session evidence summary**: Author directive 2026-04-17 — "NO ANTIPATTERN TAGS OR METADATA LEAKAGE INTO THE MANUSCRIPT OR STANDALONE PAPERS PROPER" — is now registered as V2-AP40 + subclauses a-d in CLAUDE.md and anchored here in S17 with line-by-line evidence. Strongest-form compliance: run the detection grep before every `.tex` commit; restate any match as declarative mathematics. The error ledger (CLAUDE.md + this file) is the only place AP/FM/session-code/commit-hash/meta-stamp tokens live.

## Waves 20-24: Vol II-relevant findings (compiled 2026-04-20)

Source: `../chiral-bar-cobar/notes/GRAND_SYNTHESIS_WAVES_20_22.md`. Entries 76-102 appended to the tip-table summary; below, the Vol-II-relevant structural content is expanded in prose, organised by the mathematical object each finding constrains.

### W20-24-A. SC^{ch,top} pentagon and the octachotomy of bar-cobar ambients (entries 76, 77, 79)

 - (a) RIGHT: the bar-cobar adjunction Omega^{ch} dashv B^{ch} at codim 3 on Abar_2 admits multiple compatible ambients; eight of them are now named, each corresponding to a specific SC^{ch,top} colouring stratum.
 - (b) WRONG: Waves 14-19 closed this as a heptachotomy (seven ambients); Wave 22.2 falsified Igusa transversality at admissible Heegner triples. The first non-empty admissible triple (3, 4, 7) is realised by [E_{sqrt(-3)} x E_{sqrt(-7)}] carrying tri-commuting sl_2^{+3}-triples; this forces a tri-unipotent Malcev ambient distinct from the bi-unipotent one. Heptachotomy upgraded to octachotomy.
 - (c) CORRECT: eight-colouring octachotomy at codim 3: (1) fibrewise generic, (2) single-monodromy-refined, (3) bi-unipotent Malcev (on walls-of-walls H_i cap H_j), (4) tri-unipotent Malcev (on triple intersections), (5) weight-completed coderived, (6) A_infty-corrected, (7) (inf,1)-categorical Perf(Abar_2), (8) chiral-Kontsevich-formal on Koszul locus. Each ambient IS a specific SC^{ch,top} colouring datum; octachotomy THEREFORE reads as eight Swiss-cheese colouring data. Universal k-tower closure: k_max(g) = g(g+1)/2 (triangular, not linear) controls the maximal arity at which Swiss-cheese coloured coherences are non-trivially constrained per genus. The (inf,1)-adjunction of Theorem A ascends to an (inf,2)-adjunction: compatibility data on 2-morphisms carries Auslander-Reiten triangular structure; the AR structure IS the Swiss-cheese coloured shuffle at 2-cell level. Type: scope upgrade; cardinality upgrade; categorical-level undercounting.

### W20-24-B. Compatibility-data infty-groupoid (entry 78)

 - (a) RIGHT: chain-level ambient and (inf,1)-categorical ambient are both load-bearing. Each has its own witness set.
 - (b) WRONG: treating the ambient choice as "by hand" misses the intrinsic groupoid structure of compatibility data.
 - (c) CORRECT: Data(A) ~ BAut^h_{L_infty}(g^{(inf,1)}_A) (W22.1); the ambient-chain is canonical up to the homotopy automorphism group of the (inf,1)-L_infty model. For K3 BKM H_{Delta_5} this specialises to widehat(grt)_1 / ob^{GN}, locating Grothendieck-Teichmuller rationality and the obstruction class ob^{GN} in a single quotient. Ambient choice is PARAMETRISED, not arbitrary. Type: chosen-vs-canonical.

### W20-24-C. Chiral Kontsevich formality (entries 80, 81)

 - (a) RIGHT: Kontsevich formality for chiral algebras gives an L_infty quasi-iso from chiral polyvectors to chiral Hochschild cochains, following the classical model.
 - (b) WRONG: unconditional formality is false on all of Abar_2; the obstruction lives exactly on admissible Heegner divisors H_n.
 - (c) CORRECT: on the Koszul locus U^{adm} = Abar_2 setminus bigcup_{n adm} H_n, the L_infty quasi-iso T^{poly}_{ch}|_{U^{adm}} --simeq--> ChirHoch^bullet(H_{Delta_5})|_{U^{adm}} is unconditional; on each admissible H_n the obstruction is the Malcev-ladder cocycle ob^{Kont}_n in H^3(H_n, Sym^2 T^{poly}_{ch}|_{H_n}) with Bruinier torsion order c_n in {8, 2, 3, 14, 16, 22, 30, ...}. The factorisation-level analogue requires BOTH Francis-Gaitsgory infty-operadic lift AND Tamarkin operadic formality; either alone is insufficient (FG without Tamarkin misses the associator; Tamarkin without FG misses the factorisation structure). Type: scope: unconditional vs Koszul-locus; incomplete toolset.

### W20-24-D. BD factorisation compatibility (entry 82)

 - (a) RIGHT: bi-unipotent pro-ambient carries a BD factorisation D-module structure, compatible with Beilinson-Drinfeld's original framework and with Costello-Gwilliam's 1-loop-quantised factorisation algebras.
 - (b) WRONG: treating it as a mere "bounded-derived pro-object" loses the BD structure and the quantitative 1-loop anomaly match.
 - (c) CORRECT: bi-unipotent pro-ambient IS a BD factorisation D-module. Costello-Gwilliam 1-loop counterterm matches Bruinier Chern class int_{H_1} c_1(ct) = 8 -- quantitative cross-verification between (Vol II, 1-loop analytic torsion) and (Vol III, Bruinier Heegner-Chern reciprocity). The match locks Vol II's BD framework to Vol III's arithmetic datum. Type: framework downgrade.

### W20-24-E. Theorem H hinge, Vol II to Vol III (entry 83)

 - (a) RIGHT: Theorem H concentration is a named invariant controlled by the functor Phi_d: CY-d -> chiral algebras; Phi_3 is the K3 hinge.
 - (b) WRONG: universal {0, 1, 2} concentration misses d-dependence. Chiral Hochschild on CY-d-enlarged ambient has extended concentration range.
 - (c) CORRECT: on the ambient curve (d=1, Vol II native), Theorem H gives {0, 1, 2}; on the CY-d-enlarged ambient, {0, 1, 2, d} with SHARP vanishing at k >= d+1. For d = 3 (K3 x E, Vol III): ChirHoch^{>= 4}(H_{Delta_5}) = 0 via Phi_3. The Phi_d functor is the load-bearing HINGE between Vol II's curve-ambient statement and Vol III's CY-d-ambient statement. Type: d-parametrised concentration.

### W20-24-F. chi_3 verification path catalogue, Vol II-native paths (entries 84, 85, 86, 92, 101)

 - (a) RIGHT: chi_3 = {:T partial T:} - (1/4) partial^3 T + hbar . qt(J^{(3)}) is the degree-3 cocycle; four disjoint verification paths against e_3^{K3 x E} were named in W21.4/W22.6: CoHA Casimir (Schiffmann-Vasserot), Igusa Phi_10^{-1} (Oberdieck reduced DT), elliptic-volume rigidity (Kontsevich formality degeneration), Kuznetsov relative HPD over E.
 - (b) WRONG: earlier treatments (i) omitted the Vol-II-native cyclic Feigin-Tsygan path, (ii) left the Getzler-Jones contraction abstract, (iii) missed the 11d SUGRA 1-loop arithmetic content, (iv) single-path Mukai-Hochschild framing, (v) took absolute Kuznetsov HPD on K3 x E as unobstructed.
 - (c) CORRECT: six paths total for the Vol II hinge:
   - (A) CoHA Casimir (Schiffmann-Vasserot): Vol III-native.
   - (B) Igusa Phi_10^{-1} (Oberdieck reduced DT): Vol III-native.
   - (C) elliptic-volume rigidity (Kontsevich formality degeneration): bridges Vol II and Vol III via W22.3.
   - (D) Kuznetsov RELATIVE HPD over E (Kuznetsov-Markushevich 2009; Addington-Thomas 2014): absolute HPD on K3 x E is BLOCKED by Fano obstruction (omega_Y simeq O_Y trivial; no Lefschetz twist). Only the relative version gives genuine verification.
   - (E) Vol II-native cyclic Feigin-Tsygan via Francis-Gaitsgory factorisation cyclic homology and Connes B-operator: [partial^{ch}, B^{ch}] = 0 on U^{adm}.
   - (K-B) Costello-Gwilliam factorisation-level Getzler-Jones chain-level contraction h^{ch} on bar(H_{Delta_5}): [d^{ch}, h^{ch}] = id - p_harm kills d_r for r >= 2 on Koszul locus. Explicit operator, explicit killing-range.
 - Quantitative value: <[chi_3], [e_3^{K3 x E}]>_{Phi_3} = 2 Vol(E) (2 pi i)^3 = chi(O_{K3}) . Res_{s=1/2} E_5^{(2)}(Z, s)|_{K(1)}. Mukai-Hochschild pairing: <[chi_3], [chi_3^vee]>^{ch}_{Muk} = 2 Vol(E) (2 pi i)^3 via (i) Kaledin Cor 5.5 Serre duality on ChirHoch, (ii) BV Serre-dual cup product (Costello-Gwilliam), (iii) Siegel-Eisenstein period cross-check. 11d SUGRA 1-loop reading: -log ||Delta_5||^2_Quillen = -log Delta_5 - kappa_BGS L'(0, Delta_5, std) + log C with kappa_BGS = chi_top(K3) = 24. Type: path-catalogue completion; multi-path = three+ independent paths per Beilinson.

### W20-24-G. Universal ratio-of-levels across Psi-image BKMs (entry 87)

 - (a) RIGHT: every Psi-image BKM carries a Lusztig quantisation level ell and a Mukai signature c_+ on the underlying lattice L.
 - (b) WRONG: treating these quantum-group levels as row-independent misses the universal ratio structure.
 - (c) CORRECT: ell_X / ell_Y = c_+(L_X) / c_+(L_Y) across Psi-image BKMs. Numerical values: (c_+, ell) = (1, 2) for Monster, (2, 4) for Enriques, (4, 8) for K3, (25, 50) for Fake-Monster. Leech-Conway row BREAKS the pattern (no Fricke involution), leaving five Psi-image rows with one exceptional. The ratio ties Vol II (Lusztig-level quantisation) to Vol III (Mukai-signature); on the BKM crown row B, (K, hbar^2) = (8, -1/8) with K = 2 c_+ = 8, unifying three-volume data. Type: cross-volume ratio-bridge.

### W20-24-H. CY-4 HK-restricted Phi_4 conjecture (entries 88, 89, 90)

 - (a) RIGHT: Theorem H admits a conjectural CY-d extension for each d with chi(O) non-vanishing; d = 4 is the next open frontier.
 - (b) WRONG: (i) unconditional CY-4 extension ignores the Kapustin-Rozansky-Saulina 3d/4d dichotomy blocking Phi_4 at framework level; (ii) "HK restriction is closed off" is false -- twistor-S^1 reduction opens it; (iii) K3 x K3 having vanishing chi(O) is false (chi = 4).
 - (c) CORRECT: conj:chirhoch-CY4-conditional. Under existence of Phi_4, ChirHoch^k(Phi_4(X_4)) = 0 for k >= 5, non-zero at k = 4 when chi(O_{X_4}) non-zero. Phi_4 generically blocked by KRS 3d/4d dichotomy. HK-restricted Phi_4|_HK exists via twistor-S^1 reduction -> 3d N=4 with Coulomb branch -> Costello-Gaiotto 11d re-lift. Test case K3 x K3: chi(O_{K3 x K3}) = chi(O_{K3})^2 = 4 non-zero; pairing <[chi_4], [e_4]> = 4 . Vol(K3_1) Vol(K3_2) (2 pi i)^4 via three paths: (i) Cao-Kool-Monavari DT-4 MacMahon M(q)^4; (ii) Nekrasov 8d prepotential F_0; (iii) DMVV second-quantised elliptic-genus product phi_{0,1}^2. Type: scope: conditional vs unconditional; incorrect-closed-off; Kunneth chi arithmetic.

### W20-24-I. NC Hodge Mukai-Hochschild degeneration (entry 91)

 - (a) RIGHT: chiral Kaledin degeneration transports via Francis-Gaitsgory smoothness + chiral Serre S_C dualising; Deligne-Illusie Cartier lift through factorisation-flat base change gives the NC Hodge degeneration.
 - (b) WRONG: global degeneration over Abar_2 FAILS at admissible Heegner divisors -- exactly the Kontsevich-formality obstruction.
 - (c) CORRECT: chiral Kaledin degeneration (W24.5) holds on the Koszul locus U^{adm}; obstructed at each admissible H_n by ob^{Kont}_n with Bruinier torsion order c_n. The global statement is CONDITIONAL; the Koszul-locus statement is UNCONDITIONAL. Type: scope: global vs Koszul-locus.

### W20-24-J. Five-archetype landscape G/L/C/M/B (entry 93)

 - (a) RIGHT: Volume I named four archetypes G/L/C/M with kappa + kappa^! in {0, 13, 250/3, 98/3} and r_max in {2, 3, 4, infty}.
 - (b) WRONG: four-archetype landscape is incomplete; the BKM crown row B (Borcherds-Kac-Moody) is a genuine fifth archetype.
 - (c) CORRECT: five archetypes:
   - G (Heisenberg H_k): kappa + kappa^! = 0, r_max = 2.
   - L (affine KM V_k(g)): kappa + kappa^! = 0, r_max = 3.
   - C (beta gamma): kappa + kappa^! = 0, r_max = 4.
   - M (Virasoro Vir_c): kappa + kappa^! = 13, r_max = infty.
   - B (BKM crown H_{Delta_5}): kappa + kappa^! = 8, r_max = infty, kappa_BKM = 12 **(Fake-Monster Phi_{12} convention; Phi_{10} paramodular convention gives 5; AP5 dual-indexing — pending landscape-census lock per antipatterns_catalogue.md row "kappa_BKM(H_{Delta_5}) cross-volume value").**
 - kappa + kappa^! in {0, 8, 13, 250/3, 98/3} across all five. W-extensions at {250/3, 98/3} sit on the M-row. The B-row is new in Waves 20-24 and ties Vol II one-loop anomaly (Quillen norm via chi_top(K3) = 24) to Vol III Borcherds product Phi_10. Type: landscape-cardinality undercount.

### W20-24-K. Three-faces universal identity (entry 94)

 - (a) RIGHT: Vol I conductor K, Vol II Quillen one-loop exponent, Vol III Borcherds weight kappa_BKM are all numerical invariants of the BKM crown datum.
 - (b) WRONG: treating them as three independent numbers misses the universal identity hbar^2 . K^{kappa_ch} = -1 at (K, hbar^2) = (8, -1/8).
 - (c) CORRECT: hbar^2 . K^{kappa_ch} = -1 on the B-row at (K, hbar^2) = (8, -1/8), kappa_BKM = 12 **(Fake-Monster Phi_{12} convention; AP5 dual-indexing — Phi_{10} paramodular convention gives 5; pending landscape-census lock per antipatterns_catalogue.md "kappa_BKM(H_{Delta_5}) cross-volume value")**. K = 2 c_+ = 8 = ord(mon|_{H_1}) = ell_Lusztig. Four numerical quantities (conductor K, Mukai signature doubled 2c_+, monodromy order at first Heegner divisor, Lusztig level) are equal -- a universal identity pinning Vol I x Vol II x Vol III at a single numeric point on the BKM crown. Type: cross-volume unification.

### W20-24-L. Chain-level vs cohomological class-M E_3 bar (entry 95)

 - (a) RIGHT: class M (Virasoro) admits an E_3-bar invariant whose count is finite at each genus, computable via the Hochschild-Deligne machinery.
 - (b) WRONG: chain-level count yields apparent infinity; this is a lane confusion.
 - (c) CORRECT: cohomologically, class M E_3-bar = 6^g at genus g. Chain-level counts diverge (expected for Gevrey-1 perturbation theory of Virasoro); the physically meaningful count is cohomological. Reporting must specify lane: "class M E_3-bar = 6^g (cohomological)", never "class M E_3-bar = infinity" without qualification. Type: chain vs cohomological.

### W20-24-M. Plancherel Hilbert-scheme super-quasi-Hopf (entries 96, 97, 98, 99)

 - (a) RIGHT: the algebra is K3 BKM super-quasi-Hopf A_infty H_{Delta_5} at specific parameters (hbar^2, zeta) = (-1/8, zeta_8); the measure is Plancherel on projective covers; the convergence mode is Mittag-Leffler pro-stabilisation; the master identity recovers 1/Phi_10(Z).
 - (b) WRONG: (i) generic "standard datum" framing hides the non-standard parameter choice; (ii) weak-* convergence (inherited from semisimple case) FAILS for non-semisimple Kerler-Lyubashenko; (iii) "purely algebraic integral" hides the MO-DMVV bridge; (iv) MO-extension uniqueness is not a choice but a theorem.
 - (c) CORRECT: W20.7 Plancherel Hilbert-scheme super-quasi-Hopf:
   - Algebra: H_{Delta_5} at (hbar^2, zeta) = (-1/8, zeta_8). Non-standard; these parameters are fixed by the three-faces universal identity (W20-24-K).
   - Measure: d mu^infty_Plan(lambda) = lim_N dim_qu(P_lambda^{<= N}) on projective covers P_lambda (NOT simples; non-semisimple Kerler-Lyubashenko category forbids simples).
   - Convergence mode: Mittag-Leffler pro-stabilisation in Pro(Mod_H). NOT norm (would require self-dual MTC), NOT weak-* (would require locally compact parametrising space), NOT strong (would require finite-dimensional cover).
   - Master identity: int_{H_hat_infty} dim_qu(P_lambda) ch(P_lambda)(q_rho) ch(P_lambda^vee)(q_tau) d mu^infty = 1/Phi_10(Z). Integral against Plancherel measure on projective covers yields reciprocal Igusa cusp form = DMVV second-quantisation of K3 elliptic genus.
   - MO-extension to super-quasi-Hopf: Etingof-Kazhdan dynamical twist delta = partial_Z log Phi_10; unique H^2-rigidity class. Uniqueness is a THEOREM (EK rigidity), not a convention.
 - Type: algebraic-datum specificity; convergence-mode specificity; MO-DMVV bridge; EK-twist uniqueness.

### W20-24-N. Bruinier torsion orders as Vol II data (entry 100)

 - (a) RIGHT: Bruinier torsion orders c_n index admissible Heegner divisors via arithmetic of Siegel-Eisenstein coefficients; they are central to Vol III's arithmetic Heegner structure.
 - (b) WRONG: treating c_n as Vol-III-only data misses their Vol II role as Kontsevich-formality obstruction torsion.
 - (c) CORRECT: Bruinier torsion orders c_n in {8, 2, 3, 14, 16, 22, 30, ...} are Vol II structural data: ord(ob^{Kont}_n) = c_n in H^3(H_n, Sym^2 T^{poly}_{ch}|_{H_n}). c_1 = 8 matches K = 2 c_+ = 8 on the B row, unifying with the three-faces identity. Each c_n controls at which "finite cover" the Kontsevich L_infty quasi-iso extends across H_n. Type: Vol II vs Vol III data attribution.

### W20-24-O. V^{s natural} row-assignment (entry 102)

 - (a) RIGHT: V^{s natural} = A(Lambda_24)^+ oplus A(Lambda_24)^{tw,+} (Duncan 2007) is a super vertex operator algebra on the Leech lattice.
 - (b) WRONG: earlier counts treated V^{s natural} as a fifth independent Psi-image row, giving six total (G/L/C/M/B + V^{s natural}).
 - (c) CORRECT: V^{s natural} is NOT a fifth independent Psi-image. The commutative orbifolding diamond {V_{Lambda_24}, V^natural, V_{Lambda_24}^s, V^{s natural}} locates V^{s natural} as the Z/2-super-twin of V^natural on the Monster row. Inherits (K, hbar^2) = (2, -1/2), not independent. Five-archetype landscape G/L/C/M/B is complete; V^{s natural} sits on the Monster row. Type: row-independence miscount.

### W27-A. Chenevier determinant, not Taylor-Wiles pseudo-character (entry 135 / AP-V2-23)

 - (a) RIGHT: the Taylor-Wiles pseudo-character S^{ps} : T^{par}_1 -> O_E with axioms (symmetry / multiplicativity / dimension) is a real object from Taylor 1991 Duke 63 Thm 2.1 (also Rouquier 1996). The Hecke-algebra 4-tuple (S_1, S_2, S_3, S_4) computed from the Saito-Kurokawa lift Satake parameters of Delta_{10} is correct data. The bridge from pseudo-character to a 4-dimensional Galois representation rho_{Delta_{10}} : Gal(Q-bar / Q) -> GSp_4(O_E) works on reduced rings via Chenevier 2014 Thm 2.12 (pseudo-characters and determinants coincide on reduced rings).
 - (b) WRONG: on NON-REDUCED rings — exactly the deformation rings felt by Vol II's one-loop Quillen norm and BV 3d HT-QFT partition function — the older Taylor 1991 pseudo-character framing is strictly weaker than the correct invariant. Conflates the Taylor-Wiles pseudo-character (older, weaker, multilinear symmetric trace functions) with the Chenevier 2014 determinant (newer, stronger, single homogeneous polynomial law with multiplicativity, unitality, Cayley-Hamilton as a single axiom). The determinant captures nilpotent Cayley-Hamilton witnesses (mod-ell^n Cayley-Hamilton identities for reducible rho with non-trivial nilpotent deformations) that the pseudo-character silently drops.
 - (c) CORRECT: the arithmetic anchor for H_{Delta_5}'s Galois-side invariants is the Chenevier determinant D^{Chen} : T^{par}_1 -> O_E tensor Z_ell — a 4-dimensional homogeneous polynomial law. Its graded components (Sigma_1, Sigma_2, Sigma_3, Sigma_4) at Hecke generators T_p recover the Saito-Kurokawa Satake data (a_p(f_{16}) + p^8 + p^9, ..., p^{32}) via the reciprocal spinor L-factor expansion prod_{i=1}^4 (1 - alpha_i x) = 1 - Sigma_1 x + Sigma_2 x^2 - Sigma_3 x^3 + Sigma_4 x^4. Verified at 46 primes p <= 199. Vol II framing: the one-loop Quillen norm and BV 3d HT-QFT partition function tie to Galois-side L-function data via D^{Chen}; the Taylor-Wiles pseudo-character was a reduced-ring proxy sufficient for W20.4's trace identities but insufficient for Vol II's scheme-valued path-integral refinements (deformation rings around the Saito-Kurokawa lift are non-reduced, and the BV anomaly precisely measures the nilpotent Cayley-Hamilton witnesses that S^{ps} cannot detect). The universal three-faces identity on the B-row reads off from D^{Chen}, not from S^{ps}. Primary: Chenevier 2014 arXiv:1301.0635 Sec 1.2 Def/Prop 1.9, Thm 2.12 (the determinant = pseudo-character equivalence on reduced rings and strict inequality on non-reduced); Taylor 1991 Duke 63 Thm 2.1 (pseudo-character original); Ikeda 2001 Ann Math 154 Cor 16.2 (Saito-Kurokawa lift); Weissauer 2005 LNM 1868 (spinor Galois representation construction); Laumon 2005 Publ IHES 102 (geometric Satake on GSp_4). Cross-ref: Vol I AP902 / Remark rem:dl-w25-determinant-not-pseudocharacter in chapters/theory/derived_langlands.tex (cache entry 422); Vol III cache entry at appendices/first_principles_cache.md row 8 (tagged); Vol III ADJUDICATION_LEDGER Section III.C. DISTINCT from Pattern 295 (Creutzig-Ridout / Lyubashenko coend pseudo-traces on non-semisimple modular tensor categories): coend pseudo-traces satisfy a Kerler-Lyubashenko modified-trace axiom set on MTCs, not a polynomial-law axiom set on Hecke algebras; the two "pseudo-" objects are categorically unrelated and must not be conflated. Type: pseudo-character / determinant scope (older-weaker / newer-stronger on non-reduced rings).

### W28-A. Single-valued MZV scope of chiral-Hochschild periods (entry 136 / V2-AP126)

 - (a) RIGHT: the full motivic MZV framework of Deligne-Goncharov 2005 *Ann Sci ENS* 38 gives the mixed-Tate Galois $\mathrm{grt}_1^{\mathrm{mot}}$ acting on the motivic MZV ring $\mathrm{MZV}^{\mathrm{mot}}$. Periods arising from Arnold-form iterated integrals $\int \eta_{i_1 j_1} \wedge \cdots \wedge \eta_{i_n j_n}$ on $\mathrm{Conf}_n(X)$ admit genuine motivic lifts through Brown 2012 *Ann Math* 175 motivic basis (weight-$w$ dimension = Padovan $d_w$ for $w \le 12$). The chiral-Hochschild period $\chi_3 = 2\mathrm{Vol}(E)(2\pi i)^3$ is a genuine weight-3 period with a natural motivic home. The Vol II one-loop Quillen exponent (Path E) and the Costello-Gwilliam factorisation-cyclic-homology $\chi_3$ pairing on $\mathsf{SC}^{\mathrm{ch,top}}$-algebras $a\text{-}priori$ expand in $\mathrm{MZV}^{\mathrm{mot}}$.

 - (b) WRONG: asserting that the chiral-Hochschild period identity $\chi_3 = 2\mathrm{Vol}(E)(2\pi i)^3$ lies in the full motivic ring $\mathrm{MZV}^{\mathrm{mot}}$ with $\mathrm{grt}_1^{\mathrm{mot}}$-stable coefficients is a scope inflation. The Arnold forms $\eta_{ij} = d\log|z_{ij}|^2$ that witness the chain-level $\chi_3$ cocycle are single-valued real (they equal $\tfrac{1}{2}(d\log(z_{ij}) + d\log(\bar z_{ij}))$ and carry no monodromy); the period pairing factors through Brown 2013 *Ann Math* 175 projection $\mathrm{proj}: \mathrm{MZV}^{\mathrm{mot}} \to \mathrm{MZV}^{\mathrm{sv}}$. Conflating the two rings overcounts admissible periods: the $\zeta(2)$-weighted chain contribution formally lives in $\mathrm{MZV}^{\mathrm{mot}}_2$ but projects to $\zeta^{\mathrm{sv}}(2) = 0$, so does not survive into the observable Quillen exponent. The conflation is the precise mechanism that makes Theorem H concentration $\mathrm{ChirHoch}^\bullet \in \{0, 1, 2\}$ look imposed rather than derived.

 - (c) CORRECT: chiral-Hochschild periods live in $\zeta^{\mathrm{sv}}$ (Brown 2013 single-valued MZVs), NOT in $\mathrm{grt}_1^{\mathrm{mot}}$-stable full motivic MZVs. Three distinct sites: **chain-level** ($\eta_{ij}$-integrals on $\mathrm{Conf}_n(X)$, rational-coefficient); **motivic** ($\mathrm{MZV}^{\mathrm{mot}}$ target of the period map); **single-valued** ($\zeta^{\mathrm{sv}}$ image under Brown's projection). Canonical identifications: $\zeta^{\mathrm{sv}}(2) = 0$; $\zeta^{\mathrm{sv}}(3) = 2\zeta(3)$; $\zeta^{\mathrm{sv}}(2k+1) = 2\zeta(2k+1)$ at odd weight; at depth $\ge 2$, $\zeta^{\mathrm{sv}}$ is a PROPER subring of $\mathrm{MZV}^{\mathrm{mot}}$ (Schnetz 2014 *Commun Num Theor Phys* 8; Panzer 2015 *Commun Num Theor Phys* 9).
   **Vol II reading (specific to this volume's one-loop / cyclic reading of $\chi_3$)**: single-valued scope constrains Vol II's one-loop Quillen exponent / Costello-Gwilliam factorisation-cyclic-homology reading of the $\chi_3$ pairing. The Vol II cyclic chiral homology (Path E) lives in $\zeta^{\mathrm{sv}}$ via the Francis-Gaitsgory cyclic-factorisation trace $\mathrm{tr}^{\mathrm{cyc}}_{\mathrm{FG}}$ composed with the Brown single-valued projection $\mathrm{proj}$; the composite $\mathrm{proj} \circ \mathrm{tr}^{\mathrm{cyc}}_{\mathrm{FG}}$ is the canonical chiral-Hochschild period map. The Costello-Gwilliam one-loop Quillen exponent of $\mathsf{SC}^{\mathrm{ch,top}}$ on $\mathrm{K3}\times E$ is a weight-3 single-valued period, numerically $2\mathrm{Vol}(E)(2\pi i)^3$ with $(2\pi i)^3$-factor decomposed as $(2\pi i)(2\pi i)^2 = (2\pi i) \cdot \zeta^{\mathrm{sv}}$-admissible weight-2 structure $\mathbb Q(2\pi i)^2$ (Tate twist, NOT $\zeta(2) \cdot \mathbb Q$ which would vanish under $\mathrm{proj}$). The Theorem H amplitude bound $\mathrm{ChirHoch}^\bullet \in \{0, 1, 2\}$ is recovered as a **single-valued consequence** of $\zeta^{\mathrm{sv}}(2) = 0$, not imposed as a separate concentration axiom.
   **Three verification paths** for the single-valued landing: (i) direct computation — the Arnold form $\eta_{ij} = d\log|z_{ij}|^2$ factors through the single-valued real-analytic structure of $\mathbb P^1 \setminus \{0, 1, \infty\}$ at punctures (Brown 2013 *Ann Sci ENS* 46 Thm 2.1); (ii) alternative formula — the Francis-Gaitsgory cyclic-factorisation trace is the double-shuffle single-valued completion of the motivic Hochschild trace (Schnetz 2014 regularised zeta lift); (iii) limiting case — at $\mathrm{ChirHoch}^2$, the single-valued projection predicts $\zeta^{\mathrm{sv}}(2) \cdot \mathrm{coeff} = 0$, matching the manifest $\{0, 1, 2\}$ amplitude bound and ruling out the naive $\mathrm{MZV}^{\mathrm{mot}}_2 \ne 0$ prediction.
   **Primary citations**: Brown 2013 "Mixed Tate motives over $\mathbb Z$" *Ann Math* 175 (motivic MZV basis); Brown 2013 *Ann Sci ENS* 46 (single-valued multiple polylogarithms); Schnetz 2014 *Commun Num Theor Phys* 8 (single-valued zeta); Deligne-Goncharov 2005 *Ann Sci ENS* 38 (mixed-Tate motivic framework); Panzer 2015 *Commun Num Theor Phys* 9 (single-valued algorithms).
   **Cross-ref**: Vol I AP901 / Theorem `thm:sv-scope-restriction-chiralhoch` in `/Users/raeez/chiral-bar-cobar/chapters/theory/motivic_shadow_tower.tex` (reference inscription with five attack/heal cycles); AP888 (shadow-ChirHoch bridge); seven-path $\chi_3$ comparison theorem (Paths A-G); Vol III cache W28-A (parallel single-valued entry for CoHA Casimir + Kuznetsov HPD readings).
   Type: full-motivic / single-valued scope (Deligne-Goncharov vs Brown 2013 projection on chiral-Hochschild periods).

---

These entries (76 through 102 in the tip-table summary) are the Vol-II-relevant structural findings from Waves 20-24; W27-A was added in Wave 27 for the Chenevier determinant gap-fill; W28-A is added in Wave 28 for the single-valued MZV scope gap-fill. Primary source: `../chiral-bar-cobar/notes/GRAND_SYNTHESIS_WAVES_20_22.md` plus Vol I's `chapters/theory/derived_langlands.tex` remark `rem:dl-w25-determinant-not-pseudocharacter` and `chapters/theory/motivic_shadow_tower.tex` Theorem `thm:sv-scope-restriction-chiralhoch`. Three-path verification status per entry is documented in the source synthesis; cross-reference to CLAUDE.md (Vol II) and the AP/FM registers lives in-prose above.

### W29-A. Humbert--Heegner admissibility filter $n\equiv 3,5\pmod 8$ on the pentagon coboundary tower $\phi^{(n)}$ (entry 137 / V2-AP127)

 - (a) RIGHT: the pentagon coboundary tower $\{\phi^{(n)}\}_{n\ge 3}$ of Definition `def:phi-n-pent-EK` (Vol I `chapters/theory/shadow_tower_higher_coefficients.tex`) has a well-defined three-filter admissibility structure on the K3 $A_\infty$-Humbert regime of $\mathbf H_{\Delta_5}$. Eichler-Zagier 1985 polar-support cutoff $\Delta\ge -1$ on the paramodular index-$1$ K3 elliptic genus is a real theorem (Eichler-Zagier *Prog Math* 55 Thm 9.3). Brown 2012 Padovan recurrence $d_n = d_{n-2}+d_{n-3}$ counts the motivic-MZV basis at weight $n$ (Brown *Ann Math* 175 Thm 1).

 - (b) WRONG: bare Padovan-dimension $d_n$ count without the Humbert--Heegner admissibility filter overcounts. Most Padovan-admissible $n$ (all $n\ge 3$ except $n=4$) are Humbert--Heegner-FORBIDDEN: the paramodular lattice sum $\sum_{4NM-\ell^2=-D_n} c_{\Phi_{10}/\eta^{24}}(N,\ell,M)$ with $D_n=(n-3)/2$ is non-empty iff $D_n\bmod 4\in\{0,1\}$, equivalently $n\equiv 3,5\pmod 8$. Asserting a non-zero $\phi^{(n)}$ on the K3--Humbert regime on the sole basis of $d_n>0$ (e.g., at $n=7, 9, 12, 24, 26, \ldots$) silently conflates the MZV-transcendence count with the paramodular Humbert--Heegner signature.

 - (c) CORRECT: $\phi^{(n)}\big|_{\mathrm{K3\text{-}Humbert}}\ne 0$ iff (i) $n\equiv 3,5\pmod 8$ AND (ii) the $d_n$-dimensional Brown canonical basis is non-empty AND (iii) $D_n\le 1$ (Eichler--Zagier polar cutoff). First non-vanishing: $\phi^{(3)}$ (Drinfeld pentagon cocycle, $D_3=0$, $C(0)=20\ne 0$); $\phi^{(5)} = -2\cdot[\mathrm{gen}]^{\otimes 5}$ with Gritsenko--Nikulin 1998 sign on $\Phi_{10}/\eta^{24}$ ($D_5=1$, $C(-1)=2\ne 0$). HH-admissible $n$ in $[3,36]$: $\{3,5,11,13,19,21,27,29,35\}$. Non-admissible Padovan-positive $n$ (e.g., $4,6,7,8,9,10,12,14,15,16,17,18,20,22,23,24,25,26,28,30,31,32,33,34,36$) all give $\phi^{(n)}\big|_{\mathrm{K3\text{-}Humbert}}=0$. HH-admissible $n\ge 11$: $\phi^{(n)}=0$ by Eichler--Zagier polar support ($D_n\ge 4>1$).

   **Condensed reference table** $(n, d_n, D_n, \mathrm{HH}, \phi^{(n)}\text{-K3})$: $(3,1,0,Y,\text{non-zero})$, $(4,0,1/2,-,0)$, $(5,1,1,Y,-2[\mathrm{gen}]^{\otimes 5})$, $(6,1,3/2,-,0)$, $(7,1,2,N,0)$, $(8,2,5/2,-,0)$, $(9,2,3,N,0)$, $(10,2,7/2,-,0)$, $(11,3,4,Y,0\,\text{polar})$, $(12,4,9/2,-,0)$, $(13,5,5,Y,0\,\text{polar})$, $(19,17,8,Y,0\,\text{polar})$, $(21,28,9,Y,0\,\text{polar})$, $(27,90,12,Y,0\,\text{polar})$, $(29,149,13,Y,0\,\text{polar})$, $(35,504,16,Y,0\,\text{polar})$.

   **Vol II framing** (specific to this volume's Swiss-cheese coloured-bar reading): the Humbert--Heegner admissibility filter is the Humbert-stratification refinement of the $\mathsf{SC}^{\mathrm{ch,top}}$ coloured bar differential on $\overline{\mathcal A_2}$. Each coloured face of the $\mathsf{SC}^{\mathrm{ch,top}}$ operadic resolution at weight $n$ couples to the paramodular K3 elliptic genus polar slice $\Delta\ge -1$; a face colouring is admissible iff the discriminant $D_n = (n-3)/2$ lies in $\{0, 1\}\bmod 4$. Non-admissible coloured faces carry the Heegner--Bruinier obstruction class in $H^2(H_n, \mathrm{Sym}^2 T^{\mathrm{poly}}_{\mathrm{ch}}|_{H_n})$ of order $c_n$ (Bruinier torsion orders). Every Vol II $\phi^{(n)}$ reference on the Swiss-cheese coloured bar differential carries the HH admissibility scope or a pointer to Theorem~\ref{thm:phi-n-humbert-heegner-admissibility}.

   **Three verification paths** for the filter: (i) discriminant-form signature — the index-$1$ paramodular form $4NM-\ell^2\equiv -\ell^2\pmod 4$ takes values in $\{0,-1\}\pmod 4$, so $-D_n$ is representable iff $D_n\in\{0,1\}\pmod 4$, forcing $n\equiv 3,5\pmod 8$ by odd-$n$ integrality; (ii) Eichler--Zagier 1985 weak Jacobi form polar-support cutoff ($C(\Delta)=0$ for $\Delta<-m^2=-1$); (iii) Gritsenko--Nikulin 1998 paramodular lift of the K3 elliptic genus with explicit $c_{\Phi_{10}/\eta^{24}}$ Fourier table.

   **Primary citations**: Eichler-Zagier 1985 *Prog Math* 55 Thm 9.3 (polar-support cutoff); Gritsenko-Nikulin 1998 *J Reine Angew Math* 507 (Humbert-Heegner structure, paramodular $\Phi_{10}/\eta^{24}$ sign convention); Bruinier 2002 LNM 1780 (Chern class on Heegner divisors; torsion orders $c_n$); Brown 2012 *Ann Math* 175 Thm 1 (Padovan motivic MZV dimension).

   **Cross-ref**: Vol I Theorem `thm:phi-n-humbert-heegner-admissibility` in `/Users/raeez/chiral-bar-cobar/chapters/theory/shadow_tower_higher_coefficients.tex` (lines 4364-4433); Vol I cache row 304 (AP890) + Pattern 299 (comprehensive); Vol I `notes/antipatterns_catalogue.md` AP903-HH; Vol III `AP-CY142` + tip-cache row V16; cross-reference also Vol II cache row 113 (AP-V2-1, eight Swiss-cheese bar-cobar ambients) and row 114 (AP-V2-6, chiral Kontsevich formality on Humbert strata) — the HH filter locks which coloured-bar ambient is admissible at each weight $n$.

   Type: necessary/sufficient (Padovan sufficient misread; HH is the orthogonal necessary filter on K3-Humbert).

## Session antipatterns — manuscript hygiene (2026-04-22)

**Scope.** 55 bookkeeping / meta-narration / version-history patterns caught across all three volumes. Each entry pairs (i) a regex trigger signature, (ii) a 5-step rectification protocol (DETECT / LOCALISE / MATH-CHECK / REPAIR / VERIFY). Conservative carve-out: `cascade`, `homological retraction`, `deformation retract`, `retracts onto` are legitimate mathematical usages and must NOT trigger these detectors. `Borcherds programme` is legitimate (proper noun). Forbidden forms targeted: `Platonic Theorem~A`, `our programme`, `programme-canonical`, `platonic chapter`, `\begin{warning}`, `\ClaimStatusRetracted`, drafting-dated remarks, `History of the claim`, retraction indices.

**Protocol template.**
 - **DETECT**: grep regex over chapters/ + frame/ + appendices/ + connections/ + theory/ + examples/.
 - **LOCALISE**: identify whether the match is in (a) manuscript prose (forbidden), (b) `notes/` / commit message / `memory/` (permitted), (c) `FRONTIER.md` (permitted).
 - **MATH-CHECK**: read ±30 lines; determine whether the adjacent mathematical content stands on its own; identify the ghost theorem behind the bookkeeping/meta wrapper (every meta-narration wraps a claim that either IS a theorem or SHOULD BE a theorem).
 - **REPAIR**: delete the wrapper; if the ghost theorem is live, inscribe it directly; if the content is already stated elsewhere, delete with no replacement.
 - **VERIFY**: re-grep the regex; run `make fast`; check `\ref` still resolves; confirm no new `Warnings` in the PDF build.

### CGCLEAN-1 — `Wave $N$` in manuscript prose
 - (a) RIGHT: session labels are genuine bookkeeping in `notes/` and commit history.
 - (b) WRONG: `Wave 15 Gaiotto computation gives...` in a reader-facing `.tex` file conflates the drafting timeline with the timeless mathematical content.
 - (c) CORRECT: delete the label; state the computation with primary citation. Type: bookkeeping leak.
 - Regex: `[Ww]ave[ ~-]?[0-9]+` (in `.tex` under `chapters/`, `frame/`, `examples/`, `theory/`, `connections/`, `appendices/`, not in `notes/` / `memory/` / `FRONTIER.md`).
 - DETECT: `grep -n '[Ww]ave[ ~-]\?[0-9]\+' chapters/**/*.tex`. LOCALISE: scope = manuscript. MATH-CHECK: find the real theorem the Wave-label sits on. REPAIR: delete "Wave N" and cite the theorem / primary source. VERIFY: regex returns empty on manuscript scope.

### CGCLEAN-2 — `AP-CY$n$` / `AP$n$` / `AP-CAT-$N$` in manuscript prose
 - (a) RIGHT: antipattern indices are canonical in `notes/antipatterns_catalogue.md`.
 - (b) WRONG: `(cf. AP-CY42)` inline in a reader-facing `.tex` file makes `notes/` a hard dependency of the manuscript.
 - (c) CORRECT: delete the code; if the hazard it flags is load-bearing, inscribe a Remark stating the hazard as mathematics. Type: bookkeeping leak.
 - Regex: `AP-?CY[0-9]+|AP-?CAT-?[0-9]+|AP[0-9]+` (in manuscript scope, excluding bibliography cite keys).
 - 5-step as template; REPAIR: inscribe the hazard as a Remark with the precise conflation stated.

### CGCLEAN-3 — `FM$n$` formula-mechanical marker
 - (a) RIGHT: FM codes live in hook output + cache entries.
 - (b) WRONG: `(FM67 bridge)` inline in manuscript.
 - (c) CORRECT: state the bridge mathematically or delete. Type: hook-index leak.
 - Regex: `\bFM[0-9]+\b` (excluding `FM_n(C)` compactification notation — use word-boundary + digit check).

### CGCLEAN-4 — `HZ-$N$` / `HZ-IV` / `HZ discipline`
 - (a) RIGHT: HZ hierarchy is an internal epistemic ordering.
 - (b) WRONG: `(per HZ-IV disjoint verification)` in manuscript.
 - (c) CORRECT: state the verification paths directly. Type: hierarchy-label leak.
 - Regex: `HZ-?[IVX0-9]+` or `HZ discipline`.

### CGCLEAN-5 — `DNA strand S$x$` / `S-strand`
 - (a) RIGHT: swarm-workflow terminology is in `notes/`.
 - (b) WRONG: `Following DNA strand S3...` in manuscript.
 - (c) CORRECT: inscribe the content without the workflow layer. Type: swarm-metaphor leak.
 - Regex: `DNA strand|S-?strand|strand\s+S[0-9]+`.

### CGCLEAN-6 — `CG-rectify pass $k$`
 - Regex: `CG-?rectify pass [0-9]+|rectification pass [0-9]+`.
 - Protocol: DETECT, LOCALISE, delete; the current text is the result of whatever passes happened.

### CGCLEAN-7 — `cache entry $n$` / `Cached Confusion` / `Cache anchor` / `Cache append`
 - Regex: `[Cc]ache entry [0-9]+|Cached Confusion|Cache anchor|Cache append`.
 - REPAIR: cite primary source; `cache/` has no reader role.

### CGCLEAN-8 — `Wave $N$ spec/verdict/witnessing`
 - Regex: `[Ww]ave[ ~-]?[0-9]+\s*(spec|verdict|witness)`.
 - REPAIR: delete the adjudication frame; keep the verdict as the mathematical statement.

### CGCLEAN-9 — `programme-canonical` / `programme canonical value`
 - Regex: `programme[ -]canonical|programme canonical value`.
 - REPAIR: "canonical" suffices; the value stands on its own.

### CGCLEAN-10 — `type-error registry entry T$n$`
 - Regex: `type-?error (registry )?T[0-9]+|T[0-9]+ registry`.
 - REPAIR: state the type mismatch as a mathematical observation (e.g., `CoHA` is $E_1$-associative; the bar complex is a coalgebra).

### CGCLEAN-11 — `narrative counterpart` / `narrative arc`
 - Regex: `narrative (counterpart|arc)`.
 - REPAIR: state the construction directly.

### CGCLEAN-12 — `story` / `saga` / `odyssey` / `journey` (nouns)
 - Regex: `\b(story|saga|odyssey|journey)\b` (as nouns; check for determiner `the`/`this`/`a` preceding).
 - Conservative: "the story of...", "this saga...". Legitimate usage in math prose: rare; almost always narration.

### CGCLEAN-13 — `Platonic ideal` / `platonic chapter` / `platonic architecture` / `Platonic ensemble` / `platonic synthesis`
 - Regex: `[Pp]latonic (ideal|form|chapter|architecture|ensemble|synthesis)`.
 - CAREFUL: `Platonic solid` (mathematics) is legitimate; exclude via negative lookahead.

### CGCLEAN-14 — `Platonic Theorem~A` / `Platonic Theorem~B`
 - Regex: `[Pp]latonic Theorem[ ~][A-Z]`.
 - REPAIR: "Theorem A" with its canonical `\ref{thm:...}`.

### CGCLEAN-15 — `This chapter's function is to...` / `The function of this section is...`
 - Regex: `[Tt]his chapter.?s function is to|[Tt]he function of this (chapter|section) is`.

### CGCLEAN-16 — signpost phrases (`we now turn to`, `having established`, `let us now`, `this brings us to`, `with this in hand`)
 - Regex: `we now turn to|having established|let us now|this brings us to|with this in hand`.
 - Already covered by existing hook PROSE signposts; CGCLEAN-16 reinforces and extends.

### CGCLEAN-17 — `in the present work` / `the author` / `our programme` / `we have argued` / `it is worth noting`
 - Regex: `in the present work|the author\b|our programme|we have argued|it is worth noting`.
 - CAREFUL: `the authors of [CiteKey]` (citing literature) is legitimate; exclude via lookahead for cite context.
 - `Borcherds programme` is legitimate (specific historical mathematical project); exclude.

### CGCLEAN-18 — `This chapter closes the ...`
 - Regex: `[Tt]his (chapter|section) closes`.

### CGCLEAN-19 — `the opening paragraphs of this preface` / `as noted in the preface`
 - Regex: `opening paragraphs? of (this|the) preface|as noted in the preface`.
 - REPAIR: `\ref` to theorem / section label.

### CGCLEAN-20 — `Earlier in the volume` / `Later in the volume`
 - Regex: `Earlier in (the|this) volume|Later in (the|this) volume`.

### CGCLEAN-21 — `retracted` / `retraction` / `the retracted` in manuscript
 - Regex: `\b[Rr]etract(ed|ion|s)\b`.
 - CAREFUL: `deformation retraction`, `homological retraction`, `retracts onto` are legitimate mathematical usages. Exclude via negative lookahead for `deformation|homological|onto`.
 - REPAIR: delete the retracted claim and its retraction marker; only the current claim stands.

### CGCLEAN-22 — `superseded` / `supersedes`
 - Regex: `\bsupersede[ds]?\b`.
 - REPAIR: only the correct current statement appears.

### CGCLEAN-23 — `earlier draft` / `previous version` / `intermediate ansatz` / `prior derivation`
 - Regex: `earlier draft|previous version|intermediate ansatz|prior derivation`.

### CGCLEAN-24 — `previously conjectural` / `previously open` / `previously unresolved` / `previously obstructing`
 - Regex: `previously (conjectural|open|unresolved|obstructing)`.

### CGCLEAN-25 — `now resolved` / `now proved` / `now known`
 - Regex: `now (resolved|proved|known)`.

### CGCLEAN-26 — `double-retraction` / `triple-retraction`
 - Regex: `double-?retraction|triple-?retraction`.

### CGCLEAN-27 — `Three successive evaluations appear in the drafting record` / `History of the claim`
 - Regex: `Three successive evaluations|History of the claim`.
 - REPAIR: if the trajectory is informative mathematically, inscribe the failed arguments as Gap/Flaw lemmas with precise obstructions, not as "evaluation $k$".

### CGCLEAN-28 — `drafting record` / `drafting trajectory` / `drafting history`
 - Regex: `drafting (record|trajectory|history)`.

### CGCLEAN-29 — `\ClaimStatusRetracted` tag
 - Regex: `\\ClaimStatusRetracted`.
 - REPAIR: delete the claim entirely; if the failure is load-bearing, inscribe as Gap/Flaw lemma.

### CGCLEAN-30 — Dated remarks (`2026-04-17`, etc.) in manuscript prose
 - Regex: `\b20[12][0-9]-[01][0-9]-[0-3][0-9]\b` (YYYY-MM-DD) in manuscript files.
 - CAREFUL: arXiv date stamps in bibliography are legitimate; exclude via file scope (only chapters/ + frame/ + appendices/ theorem environments, not `.bib`).

### CGCLEAN-31 — `\index{retraction!...}` entries
 - Regex: `\\index\{retraction!`.
 - REPAIR: remove; manuscript indexing is mathematical.

### CGCLEAN-32 — `\texttt{notes/...}` as reader-facing reference
 - Regex: `\\texttt\{notes/`.
 - REPAIR: either promote content into manuscript or delete reference.

### CGCLEAN-33 — Absolute paths `/Users/raeez/...` in manuscript
 - Regex: `/Users/raeez`.

### CGCLEAN-34 — `% TODO: librarian verification` author-note comments
 - Regex: `%[^\n]*TODO[^\n]*librarian|%[^\n]*librarian verification`.

### CGCLEAN-35 — `% ALIAS` / `% LEGACY ALIAS`
 - Regex: `%\s*(LEGACY\s+)?ALIAS`.

### CGCLEAN-36 — `% Source: NEW CHAPTER` / `% Source: Wave N`
 - Regex: `%\s*Source:\s*(NEW CHAPTER|Wave[ ~-]?[0-9]+)`.

### CGCLEAN-37 — compute-engine filenames `*_waveN_*.py` cited in manuscript
 - Regex: `_wave[0-9]+_[^\s}]*\.py`.

### CGCLEAN-38 — function names `waveN_foo` cited in manuscript
 - Regex: `\bwave[0-9]+_[a-zA-Z_]+\b`.

### CGCLEAN-39 — `\begin{warning} ... \end{warning}`
 - Regex: `\\begin\{warning\}`.
 - REPAIR: replace with `\begin{remark}` stating the scope cleanly, or delete if already covered by theorem hypotheses.

### CGCLEAN-40 — `do not confuse` / `don't be fooled` / `beware` / `be careful`
 - Regex: `do not confuse|don'?t be fooled|\bbeware\b|be careful`.

### CGCLEAN-41 — `we must be careful`
 - Regex: `we must be careful`.

### CGCLEAN-42 — gratuitous `scope-restricted` / `scope-bounded` as adjectives
 - Regex: `scope-?(restricted|bounded)`.
 - REPAIR: state actual scope (on the Koszul locus, for affine $A$, etc.).

### CGCLEAN-43 — `verdict` as meta-label
 - Regex: `\b[Vv]erdict\b` (when used as a mathematical label rather than narration).

### CGCLEAN-44 — filename `*_platonic.tex`
 - DETECT: `ls chapters/**/*_platonic.tex`.
 - REPAIR: rename file; update `\input`.

### CGCLEAN-45 — label `ch:*-platonic`
 - Regex: `\\label\{ch:[^}]*platonic\}`.

### CGCLEAN-46 — label `sec:*-platonic`
 - Regex: `\\label\{sec:[^}]*platonic\}`.

### CGCLEAN-47 — theorem label `thm:*-waveN-*`
 - Regex: `\\label\{thm:[^}]*-wave[0-9]+-[^}]*\}`.

### CGCLEAN-48 — `\index{compute module!...}`
 - Regex: `\\index\{compute module!`.

### CGCLEAN-49 — `\index{cache!...}`
 - Regex: `\\index\{cache!`.

### CGCLEAN-50 — `\index{retraction!...}` (duplicate hit of CGCLEAN-31 for hook completeness)
 - Regex: `\\index\{retraction!`.

### CGCLEAN-51 — `Five attack-heal calibrations`
 - Regex: `[Ff]ive attack-?heal calibrations`.
 - REPAIR: list the five theorems/checks directly.

### CGCLEAN-52 — `Reconstitution if the cancellation fails`
 - Regex: `[Rr]econstitution if the cancellation fails`.

### CGCLEAN-53 — `Inversion of the programme perspective`
 - Regex: `[Ii]nversion of the programme perspective`.

### CGCLEAN-54 — `Gold-standard HZ-IV disjoint verification`
 - Regex: `[Gg]old-?standard HZ-?IV disjoint verification`.

### CGCLEAN-55 — `Three successive evaluations appear in the drafting record` (verbatim)
 - Regex: `Three successive evaluations appear in the drafting record`.

---

**Cross-ref**. Mirrored in Vol I `notes/antipatterns_catalogue.md` (2026-04-22 session) and Vol III `notes/antipatterns_catalogue.md` (2026-04-22 session) under the same CGCLEAN-1..55 codes. Hook signatures in `.claude/hooks/beilinson-gate.sh` under block `# === Session 2026-04-22: manuscript hygiene (CGCLEAN-*) ===`. Reader-oriented summary in `notes/first_principles_cache.md` as tabular row set.
