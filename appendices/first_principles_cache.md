# First-Principles Analysis Cache — Cross-Programme Reference

This file caches every first-principles investigation from the programme's git history.
For each wrong claim: what it gets RIGHT, what it gets WRONG, the correct relationship, and the confusion type.

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

## I. Retracted Proofs (3)

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
- **BKM universal formula**: kappa_BKM = c_0(0)/2 = 10/2 = 5 correctly stated at L1816-1821 and L3119-3120 via Borcherds weight theorem, with explicit citation of prop:bkm-weight-universal.

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
