# Beilinson Audit: Drinfeld Double Programme (Wave 6-6 / 6-7 / 6-8 / 6-9)

Target: four new sections installed by Waves 6-6 through 6-9 across four Vol II files.

- Wave 6-6 (Part a, construction): chapters/connections/ordered_associative_chiral_kd_frontier.tex L5787-6177, conj:drinfeld-double-e1-construction
- Wave 6-7 (Part b, antipode): chapters/connections/spectral-braiding-frontier.tex L2376-2717, conj:drinfeld-double-antipode, def:chiral-drinfeld-antipode, prop:orientation-verdier
- Wave 6-8 (Part c, Z(U) = Z^der_ch): chapters/connections/hochschild.tex L1495-1760, conj:drinfeld-center-equals-bulk, conj:drinfeld-center-amplitude, comp:drinfeld-center-heisenberg
- Wave 6-9 (Part d, hemisphere = cyclic pairing): chapters/connections/modular_pva_quantization_frontier.tex L1346-1754, conj:hemisphere-cyclic-pairing, def:cyclic-pairing-bar, comp:heisenberg-cyclic-pairing, comp:heisenberg-hemisphere-pairing, comp:heisenberg-bar-koszul-pairing

Mode: read-only, six hostile examiners plus cross-coherence and base-case uniformity.

---

## 1. Per-examiner finding counts

| Examiner | CRITICAL | MODERATE | MINOR | Total |
|---|---|---|---|---|
| Formalist | 1 | 3 | 2 | 6 |
| Topologist | 1 | 2 | 2 | 5 |
| Physicist | 0 | 2 | 2 | 4 |
| Number Theorist | 0 | 1 | 1 | 2 |
| Adversarial Chef | 1 | 2 | 1 | 4 |
| Editor | 0 | 3 | 2 | 5 |
| **Total** | **3** | **13** | **10** | **26** |

Cross-coherence: 2 MODERATE findings (dependency chain + convention sharing). Base-case uniformity: 1 MODERATE finding (normalisation tracking across four parts).

---

## 2. Formalist

### F-CRIT-1: Internal contradiction between comp:tamarkin-e2-heisenberg and Theorem H (amplitude bound)

At hochschild.tex:294-302, comp:tamarkin-e2-heisenberg computes `V_T = C^*(H_k, H_k) ≅ k[[κ]]` as a formal power series ring: INFINITE-dimensional as a graded vector space. At hochschild.tex:1691-1695, Part (c) invokes this exact computation then writes "truncated to the amplitude bound of Theorem H, the surviving piece is k<1,κ> with total dimension two." But Vol I Theorem H is a **theorem**, not a filter: it says `total_dim(ChirHoch*(A)) ≤ 4`, so if comp:tamarkin-e2-heisenberg is correct it already contradicts Theorem H, and the Drinfeld-center-equals-bulk base case (comp:drinfeld-center-heisenberg at 1685-1697) depends on this "truncation" to reach `Z(U_{H_k}) ≅ k<1, κ>` with dim 2. CLAUDE.md AP94-AP98 and the audit notes at compute/audit/complete_frontier_status_2026_04_08.md:290 already flag this exact inconsistency as a known issue ("polynomial" was corrected to "polynomial growth of Betti numbers, not a polynomial algebra"), but comp:tamarkin-e2-heisenberg was not updated in the sweep. Part (c) inherits the stale computation and papers over the contradiction by calling Theorem H a "truncation." Either comp:tamarkin-e2-heisenberg is wrong (it should be a finite complex of total dim ≤ 4), or Theorem H does not apply to H_k (class G), or the two objects are different. All three resolutions demand explicit statement; the current text contains a logical cycle.

### F-MOD-1: "Z_2-grading with degree-zero A and degree-one A^!" is nonstandard

conj:drinfeld-double-e1-construction D1-D4 impose a Z/2 grading on U(A) = A ⋈ A^!. Classical Drinfeld double D(H) = H^{*op} ⊗ H is Z/2-graded only in the super setting; the usual associative double is NOT Z/2-graded. The text offers no motivation for the grading, no compatibility with the ghost-number / bar-degree grading that Part (b)'s remark on u_A references, and no verification that the pointwise fibre in Part (c) step (1) respects it. Either drop the Z/2 claim or anchor it to the bar grading (which would then collide with Part (c)'s classical-fibre reduction).

### F-MOD-2: Items D2 and D3 are redundant, and possibly inconsistent at higher arity

D2 says the mixed product is "twisted by the classical r-matrix r(z_1 - z_2)"; D3 says the mixed sector is "controlled by the universal twisting morphism τ ∈ A^! ⊗ A, which at binary level reduces to the r-matrix." At binary level D2 and D3 are equivalent, but D2 quantifies over arity-2 configurations and D3 quantifies over all arity. The text never states the arity-n analogue of D2, so the arity-n mixed product is only pinned by D3. Recommend merging D2 into D3 or stating D2 as "at arity two" explicitly.

### F-MOD-3: "A^! = (bar-B(A))^v" at 5822-5823 is one of four candidates for the notation

The line `\cA^! = (\barB(\cA))^\vee` uses Verdier-dual-of-bar-coalgebra (which matches CLAUDE.md AP34's A^!_inf — the Verdier, chain-level dual). But then 5826-5828 says "cobar and Verdier dual are distinct functors (AP34). The Drinfeld double uses the Verdier-dual A^!, not the cobar Ω(B(A))." Good — the disambiguation is correct. But the FORMULA `(\barB(\cA))^\vee` still ambiguously resembles naive linear duality (the strict A^! of AP34). The reader cannot tell from this formula alone whether `^v` means D_Ran or Hom_k(-,k). Insert one sentence: "Here `^v` denotes the Verdier functor D_Ran on Ran(C), not linear duality."

### F-MIN-1: "def:chiral-drinfeld-antipode" uses `\begin{definition}` with `\ClaimStatusConjectured`

spectral-braiding-frontier.tex:2419. AP43 and V2-AP31 forbid `\begin{definition}` for conjectural objects: a "definition" must define something that exists. Correct environment is `\begin{conjecture}[Definition attempt]` or a `Construction` environment, with the conjectural status explicit. Matches V2-AP31 "AP4 at write time."

### F-MIN-2: Theorem-like environment `\begin{computation}` with `\ClaimStatusProvedHere` for heuristic computations

comp:heisenberg-hemisphere-pairing at modular_pva_quantization_frontier.tex:1584 is tagged `\ClaimStatusHeuristic` — correct. But comp:heisenberg-bar-koszul-pairing at 1613 is tagged `\ClaimStatusProvedHere` despite computing the "principal branch √(-k²) = -ik" and absorbing "factors of i into the normalisation." A computation that absorbs undetermined phases is not proved; downgrade to `\ClaimStatusHeuristic` or tighten the phase tracking.

---

## 3. Topologist

### T-CRIT-1: "Ordered Drinfeld centre" is not defined

conj:drinfeld-center-equals-bulk asserts `Z(U_A) ≃ ChirHoch*(A)` and specifies "the bar used throughout is the ordered bar B^ord (AP102); the equivalence is between the ordered Drinfeld centre and the chiral Hochschild complex computed by ordered configurations on C." But the "ordered Drinfeld centre" is not defined anywhere in the text — the ordinary Drinfeld centre Z(C) of a monoidal category C is the E_2-centre; its "ordered" version would be an E_1-centre (Hochschild on an A_inf-algebra, giving back the same object as the centre of the monoidal category of modules by Tamarkin). The text oscillates between "Drinfeld centre = centre of the monoidal category of modules" (classical) and "Drinfeld centre of an algebra = Hochschild cochains" (Tamarkin), and these coincide only after an E_n-shift that the ordered bar complex does not provide automatically. The "ordered Drinfeld centre" needs either a definition or a concrete model as ordered-HH^0 of a strict monoidal dg category.

### T-MOD-1: "Factorization coproduct on B^ord(A^!) is Verdier transform of deconcatenation (AP83)"

hochschild.tex:1616-1621. AP83 says factorization coproduct (Sym^c, coshuffle) != deconcatenation (T^c). The claim here is that "the factorization coproduct on B^ord(A^!) is the Verdier transform of the deconcatenation coproduct on B^ord(A)" — this conflates the two coproduct types in exactly the way AP83 warns against. The Verdier transform of deconcatenation is still deconcatenation (on the Verdier-dual object), NOT factorization / coshuffle. Either fix the language ("the deconcatenation coproduct on B^ord(A^!) is the Verdier transform of the deconcatenation coproduct on B^ord(A)") or produce a genuine factorization-vs-deconcatenation conversion.

### T-MOD-2: Cyclic pairing definition uses Z_n ⊂ Σ_n, but B^ord is not Σ_n-equivariant

def:cyclic-pairing-bar at modular_pva_quantization_frontier.tex:1438 sums over "the cyclic subgroup Z_n ⊂ Σ_n." rem:cyclic-not-full-symmetric correctly warns that only after passing to B^Σ(A) is the pairing Σ_n-equivariant. But B^ord does NOT carry an ambient Σ_n-action in the first place — it has the open/line-colour ordering. The cyclic action Z_n does act on the ordered configuration (as rotation), but there is no enveloping Σ_n on B^ord. Writing "Z_n ⊂ Σ_n" is therefore ambiguous: either (a) Z_n is acting on B^ord directly (in which case drop the Σ_n), or (b) the pairing is really defined on B^Σ and pulled back (in which case the Koszul-Hopf-pairing interpretation needs to travel through the R-twisted descent, V2-AP4). Pick one.

### T-MIN-1: "S^2 rotation symmetry" justifying Z_n-equivariance

rem:cyclic-not-full-symmetric:1471 — "the hemisphere pairing is naturally Z_n-equivariant at each bar level" by S^1-rotation symmetry of D^3. But the hemisphere D^3 has rotation symmetry SO(3) (or at least O(2), the stabiliser of the axis), which is much larger than Z_n. The choice of Z_n is a discrete subgroup selected by n marked points on the boundary; this is not rotation symmetry of D^3 per se. Rewrite as "Z_n is the automorphism group of the cyclically ordered boundary insertion pattern on the equatorial S^1 ⊂ ∂D^3."

### T-MIN-2: Antipode formula's "bar grading sign (-1)^{(|J|+1)^2}"

rem:antipode-heisenberg-sanity at spectral-braiding-frontier.tex:2461 computes the sign as "(-1)^{(|J|+1)^2} = -1 for a bosonic field with |J| = 0." For |J|=0: (0+1)^2 = 1, so (-1)^1 = -1. Correct. But the general formula should be (-1)^{|s^{-1}J|·||S||} or similar; writing (|J|+1)^2 instead of (|J|+1) without cohomological motivation is opaque. For |J|=0 these agree; for |J|=1 they diverge: (-1)^{(1+1)^2} = +1 vs (-1)^{1+1} = +1 (both +1 by accident); for |J|=2: (-1)^{9} = -1 vs (-1)^{3} = -1 (both -1). The formula happens to agree with (-1)^{|J|+1} on all parities, so writing (|J|+1)^2 is misleading but not wrong. Replace with (-1)^{|J|+1} for clarity.

---

## 4. Physicist

### P-MOD-1: DFPY16 citation does not compute Z_{D^3}

main.tex:1496: DFPY16 is Dedushenko-Fan-Pufu-Yacoby, "Sphere partition functions and Coulomb branch operators" (1609.04406). That paper computes S^3 partition functions (closed sphere), NOT hemisphere D^3 partition functions. The hemisphere / half-BPS boundary localisation was carried out by Yoshida-Sugiyama (1605.04822) and by Dimofte-Gaiotto in various lecture settings; DFPY16 is a weak citation for Z_{D^3}. Comp:heisenberg-hemisphere-pairing at :1599 hedges "see DFPY16 for the analogous computation in the Coulomb-branch sphere partition function," which is honest but makes the key formula `Z_{D^3}[U(1)_k] = c · k^{-1/2}` a derivation-by-analogy. Strengthen by citing Yoshida-Sugiyama or explicitly stating "no direct reference for Z_{D^3} in the literature; formula derived by reduction from S^3."

### P-MOD-2: Dimofte25 citation is a PIRSA lecture

main.tex:1498: `Dimofte25` is "Slab constructions and fiber functors in 3d holomorphic-topological QFT, lecture notes, Perimeter Institute, 2025; PIRSA:25110067." This is used in THREE of the four parts as the anchor for the slab-pairing / Hopf-pairing identification. AP11 (single-point external dependency) applies: any derivation that requires Dimofte's slab fiber functor is hostage to a single unpublished lecture. Flag this in the concordance with status/fallback, or reproduce the essential construction in an appendix. Part (d) in particular HINGES on Dimofte25 at stage (ii) of the three-stage identification, and the "slab fiber functor" citation at chapters/frame/preface.tex:241 shows this dependency is programme-wide.

### P-MIN-1: Omega-background parameter ε appearing without definition

modular_pva_quantization_frontier.tex:1411, 1527, 1708: `n(T; ε)` and "Omega-deformation parameter ε controlling the localisation" and "regularity at ε=0." The parameter ε is not defined, not related to an Omega-deformation of C or of R^2, and is not explicitly the one appearing in DFPY16 (where the Omega-deformation is on C_z with parameter ε, sometimes called ε_+ = ε_1 + ε_2). One sentence fixing ε to the Omega-deformation on the holomorphic direction would close the gap.

### P-MIN-2: "Collision residue k/z" for Heisenberg

V2-AP7 says the Heisenberg R-matrix is exp(k·ħ/z) with "collision residue k/z" — consistent with modular_pva_quantization_frontier.tex:1580-1582 and with Part (a)'s equation 5897-5900 r_{H_k}(z) = k/z. All four parts agree at the R-matrix level. Good. MINOR concern: the "k/z" in Part (a) is the r-matrix whereas the collision residue of V2-AP7 is a derivative of the R-matrix; at the binary level these coincide up to conventions, but the text never explicitly says this. One-line clarification suffices.

---

## 5. Number Theorist

### N-MOD-1: "Associator at spectral parameter z is the KZ associator ... with coefficients in the ring of multiple zeta values"

ordered_associative_chiral_kd_frontier.tex:6054-6065. The statement is that the bar-level associator in conj:drinfeld-double-e1-construction is the KZ associator Φ_KZ(a,b) of Drinfeld, whose coefficients are rational linear combinations of MZVs. This is CORRECT but the manuscript's phrasing "the associator at spectral parameter z is the KZ associator on three points" is backwards: the KZ associator is a constant in the universal enveloping algebra of the free Lie algebra on two generators; it does NOT depend on z. The z-dependence enters through the KZ connection on M_{0,n}, not through the associator itself. Rewrite: "The associator for the three-point ordered configuration is the monodromy of the KZ connection, which at the level of formal universal expressions is the Drinfeld KZ associator Φ_KZ ∈ U(t_3)[[MZV]], independent of the spectral parameter."

### N-MIN-1: "Transcendental" qualifier

Obstruction 3 at 6060 calls the associator "a transcendental power series in the coproduct variables with coefficients in the ring of multiple zeta values." The phrase "transcendental power series" is confused: the SERIES is formal, the COEFFICIENTS are conjecturally transcendental (not all MZVs are proven transcendental). Rewrite: "a formal series whose coefficients lie in the Z-algebra of multiple zeta values, whose transcendence properties are governed by the Zagier/Brown conjectures."

---

## 6. Adversarial Chef

### C-CRIT-1: sl_2 level-one base case is NOT a verification — it is a name-assignment

Part (a) §subsec:drinfeld-e1-base-cases at 6119-6153 claims "the putative Drinfeld double U(V_1(sl_2)) should be an affine quantum-group-like object ... We CONJECTURE that it is the affine Yangian Y(sl_2-hat) at level one, or a variant thereof." Then the paragraph ends: "the V_1(sl_2) case is the cleanest nontrivial test of the construction; resolving it is the first milestone." So sl_2 level 1 is NOT a verified base case — it is a guess at an expected answer, labelled as the "first milestone" of an open programme. The paragraph opens by calling this a "base case" but the content shows it is a target, not a check.

The only genuine base case across all four parts is Heisenberg (class G). A programme with a SINGLE base case is, in the Beilinson principle, one positive data point — insufficient to distinguish between several incompatible conjectures. An adversary can construct at least one alternative Hopf object matching the Heisenberg data: e.g., the trivial double U(H_k) = H_k ⊗ H_k (undeformed) with the antipode J(z) → -J(-z) and the cyclic pairing k·m·δ_{m+n,0} agrees with everything in the Heisenberg computations EXCEPT the R-matrix exp(kħ/z), which is a feature of H_k alone. The conjectures therefore do not pin down U(A) uniquely even at class G: they pin it down modulo the R-matrix.

Strong recommendation: either add the ∃-level computation as a genuine base case (not just "this is our target"), or demote the sl_2 paragraph from "base case" to "expected target" and honestly label Heisenberg as the ONLY verified locus.

### C-MOD-1: The conjunction of all four conjectures is too strong

Suppose all four hold. Then we have:
- U(A) a chiral Hopf object with Z/2-grading and r-matrix twist (Part a)
- S: U(A) → U(A) a chiral antipode with u_A-squared identity (Part b)
- Z(U(A)) ≃ ChirHoch*(A), bounded to dim ≤ 4 by Theorem H (Part c)
- <A, A^!>_hemi = n · <-,->_bar (Part d)

But Part (c)'s amplitude bound (`≤ 4`) combined with Part (d)'s cyclic pairing (which is NON-DEGENERATE on B^ord(A), hence infinite-rank for non-finite-dim A) is in tension: if the cyclic bar pairing is non-degenerate, then the "centre" computed as the kernel of an ideal with respect to that pairing has no obvious reason to be bounded. Part (d)'s Heisenberg computation produces an infinite-dim Gaussian sum; Part (c)'s Heisenberg computation produces total dim 2. Both cannot be "the" natural invariant of H_k without an explicit map between them. The programme should either (a) prove that cyclic-bar-pairing and derived-centre live on different complexes (likely), or (b) identify the map and show how dim-4 is extracted from the full Gaussian sum.

### C-MOD-2: Class C (betagamma) is "not cyclic"

Part (d) rem:hemisphere-cyclic-obstructions(iii) at 1698-1706 correctly notes that βγ (class C) is "not cyclic in the strict sense because the weight-zero generator prevents a non-degenerate invariant pairing." Good — this is honest. But then conj:hemisphere-cyclic-pairing is stated for a generic A "admitting a cyclic A_inf structure" — the scope is therefore class G + (part of) class L + class M, EXCLUDING class C. Meanwhile Part (a), Part (b), and Part (c) all claim to cover "class G, L, C, M" (e.g., spectral-braiding-frontier.tex:2503). Parts (a)-(c) and (d) have incompatible scopes: (a)-(c) assert class-C coverage, (d) excludes class C. This is a MODERATE contradiction in programme scope. Either Parts (a)-(c) should narrow to exclude class C, or Part (d) should describe how a shifted/degenerate cyclic structure extends the hemisphere-cyclic identification to class C.

### C-MIN-1: "The only invariants under the chiral adjoint action of U(H_k) are 1 and κ"

comp:drinfeld-center-heisenberg at hochschild.tex:1680-1684 asserts this "by direct inspection" and "pointwise freeness." No computation is shown; the hardcoded answer dim 2 is declared, and V2-AP28 (engine and test from same mental model) applies: this is exactly the kind of "declared-by-inspection" value that needs two independent derivation paths. Supply one more path: either (a) direct E_2-centre computation from comp:tamarkin-e2-heisenberg, or (b) Hochschild cochain computation, or (c) classical Heisenberg-double computation as an independent check.

---

## 7. Editor

### E-MOD-1: Duplicate content across ordered_associative_chiral_kd_frontier and hochschild

The phrase "U_A = A ⋈ A^! of Remark rem:drinfeld-double-programme" appears in Part (a) at 5805, Part (b) at 2380, Part (c) at 1501, and Part (d) implicitly via conj:hemisphere-cyclic-pairing. This is exactly V2-AP27 ("duplicated mathematical content across files FORBIDDEN"). The four parts should NOT each re-introduce U_A; instead, define U_A once in one canonical location (likely Part a as the CONSTRUCTION) and have Parts (b)-(d) reference it by \ref. Currently all four parts define or re-describe U_A. Risk: future edits will drift in four places.

### E-MOD-2: Cross-reference hygiene

Parts (a) through (d) all cite `rem:drinfeld-double-programme` in the core chapter ordered_associative_chiral_kd_core.tex. Verified present. But:
- Part (a) cites `Remark rem:dimofte-k-matrix` and `Remark rem:dimofte-double-bosonization` (both in core)
- Part (c) cites `Theorem thm:bulk-boundary-line-factorization` (in hochschild.tex:1357 — same file, OK)
- Part (c) cites `Theorem thm:bulk_hochschild` (cross-chapter)
- Part (d) cites `Remark rem:slab-fiber-functor` (verified in preface and modular_pva — but not in a theorem environment, so the "slab fiber functor identification" is a REMARK, not a theorem, and Part (d) treats it as the basis of stage (ii) of a conjecture chain)

The Remark-based anchoring is acceptable for a conjectural programme but should be called out: "stage (ii) depends on Remark rem:slab-fiber-functor, which is itself an expository summary of Dimofte25." Honesty.

### E-MOD-3: Status tagging is inconsistent across the four parts

- Part (a): conjecture D1-D4 as sub-items, all `\ClaimStatusConjectured`. Good.
- Part (b): Conjecture axioms (a)-(d) with PER-AXIOM verification status in remark — (a) "proved at bar level, conjectural at double level"; (c) "doubly conjectural"; (d) "verified on class G, open elsewhere." Good, detailed.
- Part (c): conj:drinfeld-center-equals-bulk is `\ClaimStatusConjectured`; conj:drinfeld-center-amplitude is conditional on (c); comp:drinfeld-center-heisenberg is `\ClaimStatusProvedHere`. GOOD, but the ProvedHere tag on comp:drinfeld-center-heisenberg is questionable (see C-MIN-1).
- Part (d): conj:hemisphere-cyclic-pairing is `\ClaimStatusConjectured`; comp:heisenberg-hemisphere-pairing is `\ClaimStatusHeuristic` (one-loop determinant); comp:heisenberg-bar-koszul-pairing is `\ClaimStatusProvedHere` (absorbs factors of i); comp:heisenberg-cyclic-pairing is `\ClaimStatusProvedHere` (definition-level). A reader cannot see a uniform "conjectural-with-base-case-verified" pattern; each part uses a different convention.

Recommend a single "Programme status table" inserted at a canonical location (e.g., end of Part (a)) summarising: which axiom/stage is proved at what level of bar / class / arity across all four parts. This would also catch the scope mismatch flagged in C-MOD-2.

### E-MIN-1: AP105 compliance — Heisenberg opening

Part (d) §subsec:heisenberg-base-case at :1574 opens "The simplest setting in which all three stages are under control is 3d abelian Chern-Simons at level k, whose boundary algebra is the Heisenberg vertex algebra..." This is the CG "unique survivor" move correctly deployed. Good.

Part (a) §subsec:drinfeld-e1-base-cases opens "We verify that the construction ... recovers the expected answer in the two base cases where a classical answer is available." This is the "list results before proving them" pattern (AP109). Rewrite as "The construction is tautological on class G; the sl_2 level-one case is the first nontrivial test."

### E-MIN-2: Prose hygiene

Grep for em dashes in the four new sections: hochschild.tex has em dash at 1707 ("the 'twist' between H_k and H_{-k} becomes trivial and"), no em dashes found in the four section ranges on direct inspection — the four waves inherited clean prose. Grep for AI slop (moreover / notably / crucially / remarkably): none found on direct inspection. Good. MINOR: "essentially tautological" at Part (a):6117 — "essentially" is a hedge; drop it.

---

## 8. Cross-coherence verdict

The four parts claim the dependency chain:
- Part (a) → constructs U_A
- Part (b) → antipode S_A on U_A assuming Part (a) — ACKNOWLEDGED as "doubly conjectural"
- Part (c) → Z(U_A) = Z^der_ch(A) assuming Part (a) + (b) — ACKNOWLEDGED
- Part (d) → hemisphere = cyclic pairing assuming U_A from (a) — ACKNOWLEDGED indirectly

**Dependency chain consistency: PARTIAL PASS.**

- Part (b) correctly tags axiom (c) as "doubly conjectural pending Part (a)."
- Part (c) correctly states it depends on the construction of U_A from Part (a).
- Part (c) rem:drinfeld-center-four-functors honestly states that "bar-cobar inversion and Verdier duality do NOT suffice to identify Z(U_A) with ChirHoch*(A); the Hochschild functor is a separate input."
- Part (d) does NOT explicitly depend on Parts (b) and (c); the pairing construction is independent, but the SCOPE statement that the bar side "is the pairing of the Drinfeld double" assumes Part (a)'s U_A exists. Part (d) should cite Part (a) at the line where "pairing of the Drinfeld double" appears (currently around 1561).

**Coproduct ↔ antipode compatibility:** Part (a) provides a "coproduct sketch" at subsec:drinfeld-e1-coproduct without actually defining Δ_U. Part (b)'s antipode axiom (c) is `(id ⊗ S) ∘ Δ = η ∘ ε`. Since Δ is a "sketch," the antipode axiom cannot be checked. Part (b) correctly labels this as "doubly conjectural." But nothing forces Part (a)'s eventual Δ to be compatible with Part (b)'s S beyond bar-level compatibility. A MODERATE coherence issue: the programme should state, as an explicit conjecture, "the Δ of Part (a) and the S of Part (b) satisfy the antipode axiom," rather than leaving this as an implicit expectation.

**Scope mismatch:** Parts (a), (b), (c) all cover classes G, L, C, M. Part (d) excludes class C. See C-MOD-2.

---

## 9. Heisenberg base case uniformity verdict

Asserted uniform Heisenberg data across all four parts:
- κ_ch = k: CONFIRMED. Part (a):5901 (`r_{H_k}(z)=k/z`); Part (b):2480 (`r(z)=k·Omega/z`, Kac-Moody, specialises to Heisenberg after reduction); Part (c):1682 (`κ^Heis = k, not k/2`, AP39 compliant); Part (d):1620-1635 (`k^! = -k`, free-field complementarity).
- R = exp(kħ/z): CONFIRMED in Part (d):1580, matches V2-AP7. NOT explicitly written in Parts (a)-(c); Part (a) gives the r-matrix k/z (which exponentiates to R).
- S(J(z)) = -J(-z): CONFIRMED in Part (b) eq:antipode-heisenberg (line 2447). Not referenced in Parts (a), (c), (d).
- Z(U_H) dim 2: CONFIRMED in Part (c) comp:drinfeld-center-heisenberg (generators 1, κ). Parts (a), (b), (d) do not compute Z(U_H).
- Hemisphere = c·k^{-1/2}: CONFIRMED in Part (d):1593.

**Base case uniformity: PASS** on all explicit data points that appear in multiple parts.

**MODERATE finding:** the Heisenberg data across the four parts is consistent but NOT CROSS-CHECKED. For example, Part (c)'s base case asserts Z(U_{H_k}) ≃ k<1, κ> without using the antipode S of Part (b) or the hemisphere pairing of Part (d) to verify. Part (d)'s base case computes a Gaussian exponential pairing k^{-1}·exp(-α²/k) that involves neither the centre nor the antipode. The four parts are consistent BECAUSE each computes an independent quantity; they do not produce an overdetermined system that would catch errors. Recommend: add a single table in one canonical location giving the Heisenberg values of the six objects (U, Δ, S, u, Z, <-,->) and verifying the antipode / pairing compatibility at k = 1 (say).

**Internal arithmetic check:** At Part (a):6124 the Feigin-Frenkel level for sl_2 at k=1 gives k' = -5. Verified: -k - 2h^v = -1 - 4 = -5 for h^v(sl_2) = 2. At k = -h^v = -2, k' = 2 - 4 = -2, consistent with self-dual critical level. Both arithmetic checks pass.

---

## 10. Top 5 CRITICAL / MODERATE findings

1. **F-CRIT-1:** `comp:tamarkin-e2-heisenberg` says `V_T ≅ k[[κ]]` (infinite-dim) but Theorem H says total dim ≤ 4. Part (c) "truncates" to dim 2; Theorem H is not a truncation but a theorem. Internal Vol II contradiction that the Drinfeld-center-equals-bulk Heisenberg base case depends on.

2. **T-CRIT-1:** "Ordered Drinfeld centre" Z(U_A) in conj:drinfeld-center-equals-bulk is not defined. The ordinary Drinfeld centre is E_2; the "ordered" version is an E_1-centre = Hochschild on an A_inf-algebra, but the text does not make this identification explicit.

3. **C-CRIT-1:** The sl_2 level-one "base case" in Part (a) is a guess at the expected answer ("affine Yangian ... or a variant thereof"), NOT a verification. Heisenberg is the ONLY genuine base case across all four parts, and it does not uniquely pin down U(A) — the construction is modulo R-matrix data.

4. **T-MOD-1:** Part (c) obstruction (2) refers to "the factorization coproduct on B^ord(A^!)," conflating AP83's distinction between factorization (Sym^c, coshuffle) and deconcatenation (T^c). The Verdier transform of a deconcatenation coproduct is still a deconcatenation coproduct on the Verdier dual; the "factorization coproduct" language is incorrect.

5. **C-MOD-2:** Class C (βγ) is explicitly excluded from Part (d)'s scope but included in Parts (a)-(c)'s scope. The four conjectures therefore cover different landscapes and cannot be composed on class C.

---

## 11. Overall programme health grade

**Grade: B+ (promising research programme, three issues to resolve before proof of concept)**

Strengths:
- The programme is HONESTLY CONJECTURAL throughout: no part claims more than it has.
- The "obstruction" discipline is excellent: each part lists its 3-4 programmatic obstructions explicitly.
- Four functors (AP34) are respected: Part (c)'s rem:drinfeld-center-four-functors is a model of correctness on the Bar-Cobar / Verdier / Hochschild / Drinfeld-centre distinction.
- Feigin-Frenkel level arithmetic is correct (k' = -k - 2h^v, not -k - h^v), matching VF031 and the CLAUDE.md directive.
- AP126 (level-prefixed r-matrix) verified on every r-matrix formula: 5899, 5921, 6131, 2480, 1678.
- AP132 (augmentation ideal in bar complex) verified: 5819, 2432, 1523, 1436.
- AP1 (kappa family-specific) verified: Part (c):1682 explicitly says κ^Heis = k, not k/2.
- Prose is clean: no em dashes or AI slop in the new material.
- Each part's Heisenberg base case is correctly computed under its own conventions.

Weaknesses:
- ONE base case (Heisenberg) is insufficient for a four-conjecture programme; the "second base case" (sl_2 level-1) is a target not a check.
- Internal contradictions with existing Vol II content (F-CRIT-1) not caught by the wave authors.
- Cross-coherence between parts relies on VERBAL acknowledgements rather than structural verification; no overdetermined compatibility checks.
- Single-citation dependencies on Dimofte25 (a PIRSA lecture) and DFPY16 (wrong partition function) are epistemic weak points.

---

## 12. Recommended conjecture demotions / restatements

1. **Part (a) conj:drinfeld-double-e1-construction D2 and D3**: merge or explicitly scope D2 to arity 2. Current formulation is redundant.

2. **Part (a) sl_2 level-one "base case" subsection**: rename from "Base cases" to "First milestone" or "Expected targets." Currently misleadingly labelled.

3. **Part (b) def:chiral-drinfeld-antipode**: downgrade from `\begin{definition}` to `\begin{conjecture}[Tentative definition]` or `\begin{construction}`. V2-AP31 / AP43 forbid `\begin{definition}` for conjectural objects.

4. **Part (c) conj:drinfeld-center-equals-bulk**: either (a) define "ordered Drinfeld centre" Z(U_A) or (b) replace "Z(U_A)" with the explicit model "HH^0(U_A-mod)" or "ordered-E_1-centre of U_A." The current notation is a floating symbol.

5. **Part (c) comp:drinfeld-center-heisenberg**: demote from `\ClaimStatusProvedHere` to `\ClaimStatusHeuristic` pending resolution of F-CRIT-1 (the contradiction between V_T = k[[κ]] and Theorem H amplitude bound).

6. **Part (d) conj:hemisphere-cyclic-pairing**: explicitly narrow scope to exclude class C, or extend via cyclic completion. Current scope is implicitly inconsistent with Parts (a)-(c).

7. **Programme-level**: add a single "Drinfeld double programme status table" (one table per class in {G, L, C, M}, one row per part (a)-(d), showing "proved / verified on base case / conjectural / excluded") in one canonical location. This would have caught C-MOD-2 before installation.

---

## 13. Files referenced

- /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex (Part a)
- /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex (Part b)
- /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex (Part c, comp:tamarkin-e2-heisenberg at 290)
- /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex (Part d)
- /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex (rem:drinfeld-double-programme, rem:dimofte-*)
- /Users/raeez/chiral-bar-cobar-vol2/main.tex (DFPY16 at 1496, Dimofte25 at 1498, Drinfeld85 at 1505, Majid95 at 1573, etingof1996quantization at 1913, Drinfeld90 at 2103)
- /Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md (V2-AP1-35)
- /Users/raeez/chiral-bar-cobar-vol2/compute/audit/complete_frontier_status_2026_04_08.md (prior flag of F-CRIT-1 pattern)
- /Users/raeez/chiral-bar-cobar/CLAUDE.md (AP34, AP83, AP94-98, AP102, AP105, AP109, AP126, AP132, AP134, AP141)

End of audit.
