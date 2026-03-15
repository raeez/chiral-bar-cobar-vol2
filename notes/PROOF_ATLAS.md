# PROOF ATLAS — Volume II
# Every proof that needs to exist, with dependencies, strategies, and current status.
# March 2026

> This document is the proof programme for Volume II. It maps every theorem that the
> paper aspires to prove, the dependencies between them, and concrete strategies for
> each. When a proof is completed, update the status here AND in concordance.tex.

---

## I. OPERADIC FOUNDATIONS (§1-§3, §5)

### F1. Swiss-cheese operad well-definedness
- **Claim**: SC^{ch,top} with FM_k(C) × E_1(m) is a well-defined colored operad
- **Status**: ProvedHere ✓
- **File**: foundations.tex
- **Dependencies**: FM compactification (classical), E_1 operad (classical)
- **Notes**: Straightforward from definitions. DONE.

### F2. Closed color ≃ BD chiral operad
- **Claim**: The closed (ch) color of SC^{ch,top} recovers the BD chiral operad via zigzag
- **Status**: ProvedElsewhere (CG, Lurie)
- **File**: foundations.tex
- **Dependencies**: [CG18] Prop 5.2.3, [Lurie-HA] Thm 5.4.5.3
- **Notes**: Zigzag stated. Verify the precise citations.

### F3. Recognition theorem ⚠️
- **Claim**: Prefactorization algebras on C×R satisfying locality axioms are equivalent to
  C_*(W(SC^{ch,top}))-algebras
- **Status**: NEEDS VERIFICATION
- **File**: foundations.tex (line 188-196)
- **Dependencies**: F1, [CG18] recognition theorem, [AF15] factorization homology
- **Strategy**: The CG recognition theorem works for the E_n operad. The adaptation to
  SC^{ch,top} requires:
  1. The Boardman-Vogt resolution W(SC^{ch,top}) is cofibrant (standard BV theory)
  2. The factorization algebra on C×R with HT locality satisfies Weiss cosheaf descent
  3. On each disk D²×I, the algebra restricts to an E_2×E_1 algebra (by the SC structure)
  4. Cosheaf descent + disk algebras ⟹ operadic algebra (CG recognition)
  The main gap is Step 2: showing HT locality implies Weiss cosheaf descent for the SC operad.
- **Estimated effort**: MODERATE (2-3 pages if the CG argument adapts cleanly)
- **Blocked by**: Nothing. This can be attacked now.

### F4. Operad ⟹ axioms direction ⚠️
- **Claim**: A C_*(W(SC^{ch,top}))-algebra produces operations m_k satisfying the concrete
  A∞ chiral axioms (sesquilinearity, spectral substitution, A∞ relations)
- **Status**: NEEDS VERIFICATION
- **File**: equivalence.tex (line 10-25)
- **Dependencies**: F1, fm-calculus.tex (Stokes integration)
- **Strategy**:
  1. The operadic structure maps C_*(FM_k(C)) ⊗ A^⊗k → A produce m_k
  2. Sesquilinearity: comes from the FM_k(C) structure — translating one point
     z_i → z_i + ε gives a boundary term in the operadic integral, which produces
     the -λ_i factor via residue
  3. Spectral substitution: comes from factorization — when FM_k(C) → FM_l(C) ×
     FM_{k-l+1}(C) by collapsing a subset, the spectral parameters add
  4. A∞ relations: comes from ∂(FM_k(C)) = ∪ FM_l × FM_{k-l+1} (boundary stratification)
     via Stokes' theorem
  Each step is a Stokes residue computation on FM_k(C).
- **Estimated effort**: MODERATE (3-4 pages; Step 2 is the most delicate)
- **Blocked by**: Nothing.

### F5. Axioms ⟹ operad direction (rectification) ⚠️
- **Claim**: Concrete axiom data (m_k with sesquilinearity and A∞ relations) can be
  promoted to a C_*(W(SC^{ch,top}))-algebra structure
- **Status**: NEEDS VERIFICATION
- **File**: equivalence.tex (line 33-40)
- **Dependencies**: F4, operadic rectification theory
- **Strategy**: This is the hard direction. Two approaches:
  (a) **Direct**: construct the operadic structure maps from the m_k by integration.
      The m_k produce forms on FM_k(C) via the spectral parameters; integrating over
      FM_k(C) gives the operadic action. The A∞ relations ensure compatibility.
  (b) **Abstract**: use the operadic bar-cobar adjunction. The m_k define a
      twisting morphism τ: B(SC^{ch,top}) → End(A), and rectification produces
      the operad algebra structure.
  Approach (b) is cleaner but requires the bar-cobar machinery for SC^{ch,top}.
  Approach (a) is more explicit and connects to the FM calculus.
- **Estimated effort**: HARD (4-6 pages; approach (b) requires §15 bar-cobar)
- **Blocked by**: F4 (forward direction should be proved first)

---

## II. BV-BRST CONSTRUCTION (§6)

### B1. Chain-level A∞ structure from BV-BRST
- **Claim**: The Feynman diagram expansion of time-ordered products produces m_k
  satisfying the A∞ chiral axioms
- **Status**: CONDITIONAL on (H1)-(H4)
- **File**: bv-construction.tex
- **Dependencies**: F4, (H1)-(H4)
- **Strategy**: Given (H1)-(H4), the BV data produces:
  - Propagator K(t,z) satisfying (H2) regularity
  - Time-ordered products T_k via Feynman diagrams on FM_k(C)
  - The Stokes theorem on FM_k(C) (via (H3)) produces A∞ relations
  The proof is essentially F4 applied to the specific propagator K.
- **Notes**: This is the PHYSICS INPUT. The mathematical content is in F4.

### B2. Compatibility with W(SC^{ch,top})
- **Claim**: The BV construction lands in the operadic framework (not just axioms)
- **Status**: CONDITIONAL on (H1)-(H4) + F3 (recognition)
- **Dependencies**: B1, F3
- **Notes**: This follows from B1 + F3 if both are proved.

---

## III. PVA DESCENT (§7-§9) — THE CRITICAL PATH

### D1. Regular/singular decomposition
- **Claim**: m₂(a,b;λ) = m₂^reg(a,b;λ) + m₂^sing(a,b;λ) with reg ∈ A[[λ]], sing ∈ λ⁻¹A[[λ⁻¹]]
- **Status**: ProvedHere ✓
- **File**: axioms.tex
- **Notes**: Laurent decomposition. DONE.

### D2. Commutativity of product on H• ⚠️
- **Claim**: The product [a]·[b] = evaluation of Sym(m₂^reg(a,b;0)) is commutative
- **Status**: NEEDS VERIFICATION
- **File**: pva-descent.tex
- **Dependencies**: D1
- **Strategy**:
  1. m₂^reg(a,b;λ) = m₂^reg(b,a;-λ-∂) by A∞ Stasheff + sesquilinearity
  2. At λ=0: m₂^reg(a,b;0) = m₂^reg(b,a;-∂) + (homotopy boundary terms)
  3. On cohomology (Q-closed elements): boundary terms vanish
  4. The ∂-correction terms are Q-exact (sesquilinearity of ∂-action)
  5. Therefore [a]·[b] = [b]·[a] on H•
  This is the Borcherds commutativity argument. The key step is (4): showing that
  the ∂-correction from (-λ-∂) evaluated at λ=0 is Q-exact.
- **Estimated effort**: LOW (1 page; standard argument from Borcherds/Kac)
- **Blocked by**: Nothing. ATTACK NOW.

### D3. λ-bracket from m₂^sing ⚠️
- **Claim**: {a_λ b} = m₂^sing(a,b;λ) defines a sesquilinear, skew-symmetric λ-bracket
- **Status**: NEEDS VERIFICATION
- **File**: pva-descent.tex
- **Dependencies**: D1
- **Strategy**:
  - Sesquilinearity: direct from A∞ sesquilinearity of m_k, projected to singular part
  - Skew-symmetry: from the Borcherds formula
    {a_λ b} = -Σ_n (-∂-λ)^n/n! · (b_n a)
    where b_n a are the n-products from OPE. The singular part captures exactly the
    positive-n modes (poles), and skew-symmetry is the classical Borcherds identity.
  - Proof: write m₂^sing in terms of n-products, apply Borcherds, verify signs.
  The Virasoro and abelian CS examples already verify this computationally.
- **Estimated effort**: LOW-MEDIUM (1-2 pages)
- **Blocked by**: Nothing. ATTACK NOW.

### D4. Leibniz rule ⚠️
- **Claim**: {a_λ bc} = {a_λ b}c + b{a_λ c} + ∫₀^λ {[a_μ b]_λ c} dμ
- **Status**: NEEDS VERIFICATION
- **File**: pva-descent.tex
- **Dependencies**: D1, D2, D3
- **Strategy**:
  The n=3 A∞ identity gives:
  m₁(m₂(a,m₂(b,c))) - m₂(m₁(a),m₂(b,c)) + ... = 0
  Project this identity: take a,b Q-closed, apply outer-reg/inner-sing decomposition.
  - Outer reg: gives the product structure
  - Inner sing: gives the λ-bracket
  - The A∞ sign (-1)^{rs+t} becomes the Leibniz compatibility sign
  Key technical point: the spectral substitution λ_block = λ₁+λ₂ in the A∞ identity
  becomes the λ-integral ∫₀^λ in the Leibniz rule.
- **Estimated effort**: MEDIUM (2-3 pages; spectral substitution → integration is subtle)
- **Blocked by**: D2, D3

### D5. Jacobi identity ⚠️⚠️⚠️ (THE HARDEST STEP)
- **Claim**: {a_λ {b_μ c}} - {b_μ {a_λ c}} = {{a_λ b}_{λ+μ} c}
- **Status**: NEEDS VERIFICATION
- **File**: pva-descent.tex (line 176-198)
- **Dependencies**: D3, fm-calculus.tex (Stokes + AOS)
- **Strategy**:
  The Jacobi identity comes from the n=3 A∞ identity projected to the sing-sing-sing
  component. The proof has three layers:

  **Layer 1**: The n=3 A∞ identity on FM₃(C).
  ∂(FM₃(C)) has 3 boundary divisors D_{12}, D_{23}, D_{13} corresponding to the
  three pairwise collisions. Stokes' theorem gives:
  0 = ∫_{FM₃} d(amplitude) = Σ_S ∫_{D_S} Res_S(amplitude)
  Each boundary integral computes a composition of m₂ operations.

  **Layer 2**: AOS cancellations at codimension-2 corners.
  Where two boundary divisors meet (e.g., D_{12} ∩ D_{23}), the Arnold-Orlik-Solomon
  relations cancel the contributions. This is classical: the Arnold relation
  ω_{12} ∧ ω_{23} + ω_{23} ∧ ω_{31} + ω_{31} ∧ ω_{12} = 0
  on configuration spaces.

  **Layer 3**: Projection to sing-sing component.
  The Stokes identity on FM₃ gives an identity involving m₂ ∘ m₂ compositions.
  Projecting to the singular parts in both spectral parameters λ, μ extracts the
  Jacobi identity for the λ-bracket.

  **Key difficulty**: The sign bookkeeping in Layer 3 is formidable. The projection
  from the A∞ identity (which uses Koszul signs with element degrees) to the PVA
  Jacobi identity (which uses λ-bracket conventions) involves tracking:
  - Koszul signs from the A∞ identity
  - The spectral substitution λ → λ+μ in the RHS
  - The orientation of the boundary divisors in FM₃(C)

  **Computational verification**: The abelian CS case is trivially satisfied (Jacobi = 0=0=0).
  The Virasoro case is known classically but the compute module returns `S.Zero` without
  computing. A genuine Virasoro Jacobi check would be the strongest evidence.

- **Estimated effort**: HARD (4-6 pages; the sign computation is the bottleneck)
- **Blocked by**: D3, fm-calculus.tex (Stokes integration must be solid first)

### D6. Higher m_{k≥3} vanish on H• ⚠️⚠️
- **Claim**: On Q-cohomology, m_k induces zero for k≥3 (so A∞ → PVA is exact, not A∞)
- **Status**: NEEDS VERIFICATION
- **File**: pva-descent.tex
- **Dependencies**: D1 through D5
- **Strategy**:
  This requires constructing explicit homotopy contractions h_k such that
  m_k(a₁,...,a_k) = Q(h_k(a₁,...,a_k)) + (lower terms)
  for Q-closed a_i.

  **Approach 1**: Degree counting. If m_k has degree 1-k, and the only degree-1
  operation is Q=m₁, then on the cohomological grading m_k for k≥3 must be
  Q-exact. This works for degree reasons UNLESS there are degree-preserving
  homotopies that obstruct the vanishing.

  **Approach 2**: Explicit homotopy. Construct h_k using the FM_k(C) Green's function.
  The idea: the A∞ operations m_k are integrals over FM_k(C), and the homotopy h_k
  is the integral over a "cone" in FM_k(C) that witnesses the contractibility of
  the FM₃,...,FM_k boundary strata.

  **Approach 3**: Homotopy transfer. Use the homological perturbation lemma (HPL)
  to transfer the A∞ structure from (A, m_k) to (H•(A,Q), transferred operations).
  The HPL guarantees that the transferred structure is A∞, and the transferred
  m_k^{tr} for k≥3 are the obstructions to formality. If the A∞ algebra is
  formal (which is the claim), these all vanish.

  **CRITICAL OBSERVATION**: The claim is NOT that the A∞ algebra is formal in general.
  The claim is that on cohomology, the induced structure is a PVA (product + bracket),
  which means m₃^{tr} = 0, m₄^{tr} = 0, etc. This is a specific formality claim.
  The LG example has m₃ ≠ 0 at the chain level, so the A∞ algebra is NOT formal.
  The vanishing is on COHOMOLOGY only.

  **For the free theory**: m_{k≥3} = 0 at chain level, so trivially 0 on cohomology. ✓
  **For LG cubic**: m₃ ≠ 0 at chain level, but H•(A,Q) = C, so there are no nontrivial
  cohomology classes to evaluate m₃ on. Vacuously true. ✓ (but not informative)
  **For Virasoro**: The interesting case. Need to show m₃^{tr} = 0 on H•.

- **Estimated effort**: HARD (3-5 pages; approach depends on the example)
- **Blocked by**: D5 (Jacobi first, then higher vanishing)

---

## IV. FM CALCULUS (§8)

### FM1. Stokes → A∞ relations ⚠️
- **Claim**: Integration over FM_k(C) boundaries produces A∞ identities via Stokes
- **Status**: NEEDS VERIFICATION
- **File**: fm-calculus.tex (586 lines, largest theory chapter)
- **Dependencies**: FM compactification (classical), AOS relations (classical)
- **Strategy**: The proof has 4 steps (outlined in file):
  1. Amplitudes as logarithmic forms on FM_k(C)
  2. Stokes' theorem: ∫_{FM_k} dω = Σ_S ∫_{D_S} ω
  3. Boundary integrals = operadic compositions (m_i ∘ m_j)
  4. Corner cancellations via AOS
  Steps 1-2 are standard. Step 3 requires explicit residue computation. Step 4 is
  classical (Arnold relations at codimension-2 corners of FM).
- **Estimated effort**: MEDIUM (already 586 lines; needs careful sign audit)
- **Blocked by**: Nothing (but D5 Jacobi depends on this)

### FM2. AOS corner cancellations
- **Claim**: At codimension-2 corners of FM_k(C), boundary contributions cancel pairwise
  by Arnold-Orlik-Solomon relations
- **Status**: ProvedElsewhere ✓ (Arnold)
- **File**: fm-calculus.tex, appendices/fm-proofs.tex
- **Notes**: Classical result. The adaptation to our specific FM compactification
  needs spelling out (currently in appendix stub).

---

## V. HOCHSCHILD AND CONNECTIONS (§13-§18)

### H1. Chiral Hochschild cochain complex
- **Claim**: HC•_ch(A,A) carries a brace algebra structure via FM(C) × Conf(R) fiber products
- **Status**: NEEDS VERIFICATION
- **File**: hochschild.tex, brace.tex
- **Dependencies**: F1 (SC operad structure)
- **Strategy**: The construction mirrors Gerstenhaber-Voronov but with FM(C) replacing Conf(R^n).

### H2. Bulk ≃ chiral Hochschild ⚠️
- **Claim**: The space of bulk local operators (from BV) is quasi-isomorphic to HC•_ch(A,A)
- **Status**: NEEDS VERIFICATION
- **File**: hochschild.tex (line 78)
- **Dependencies**: H1, B1
- **Strategy**: The bulk local operators are defined as the BV cohomology of observables
  supported on a point in R (the topological direction). The chiral Hochschild cochains
  are endomorphisms of A as an A∞ chiral module. The quasi-isomorphism should come from
  the universal property of Hochschild cochains as the "center" of the A∞ category.

### H3. Spectral R(z) from bulk-boundary ⚠️
- **Claim**: The bulk-boundary composition produces a meromorphic R(z) satisfying YBE
- **Status**: NEEDS VERIFICATION
- **File**: spectral-braiding.tex
- **Dependencies**: F4 (operad ⟹ axioms), (H1)-(H4)
- **Strategy**: Two independent arguments:
  (a) **Physical**: R(z) = path-ordered exponential of boundary-to-boundary propagator.
      YBE follows from factorization of 3-point functions.
  (b) **Mathematical**: R(z) is the image of the FM₂(C) fundamental class under the
      operadic structure map. YBE comes from the WDVV / Stokes identity on FM₃(C).
  Approach (b) connects to D5 (Jacobi) and would give a unified proof.

### H4. Classical r(z) = Laplace of λ-bracket ⚠️
- **Claim**: The classical limit of R(z) is the Laplace transform of the λ-bracket kernel
- **Status**: NEEDS VERIFICATION
- **File**: spectral-braiding.tex
- **Dependencies**: D3 (λ-bracket), H3
- **Strategy**: In the abelian CS example, {J_λ J} = kλ and r(z) = k/z² (up to normalization).
  The Laplace transform of λ → kλ/z² ... this needs the precise normalization.
  The key formula: r(z) = Res_{λ=0} e^{-λz} {a_λ b}.

### H5. Line operators ≃ A!-modules ⚠️
- **Claim**: C_line ≅ A!-mod (Koszul dual modules are line operators)
- **Status**: NEEDS VERIFICATION
- **File**: line-operators.tex
- **Dependencies**: F5 (rectification), bar-cobar-review.tex
- **Strategy**: This is the physical realization of the monograph's DK-0 (evaluation-locus
  module equivalence). The proof requires:
  1. Line operators as boundary-condition-changing operators
  2. The SC^{ch,top} bar construction produces the Koszul dual
  3. Module equivalence via the twisting morphism

---

## VI. EXAMPLES (§11-§12, §19-§20)

### E1. Free multiplet: m_{k≥3} = 0
- **Status**: ProvedHere ✓
- **Compute**: 100% implemented
- **Notes**: Trivial (no interaction vertices). FIX: resolve H⁰ contradiction.

### E2. LG cubic: truncation at m₃ ⚠️
- **Status**: NEEDS VERIFICATION
- **File**: examples-computing.tex
- **Compute**: 0% (ALL stubs)
- **Strategy**: Ghost number budget analysis:
  - Each cubic vertex W'''=2g: contributes 1 to ghost number
  - Each propagator K: contributes -1 to ghost number
  - Tree diagram with k external legs: V = k-2 vertices, E = (3V-k)/2 edges
  - For k=3: V=1, E=0, ghost = 1. Combined with form degree on C×R: total degree matches |m₃|=1-3=-2 ✓
  - For k=4: V=2, E=1, ghost = 2-1=1. Form degree gives |m₄| should be 1-4=-3, but ghost+form = ... NEEDS EXPLICIT CHECK
  The degree counting must account for:
  - Ghost number (from vertices and propagators)
  - Form degree on C (holomorphic, 0 or 1)
  - Form degree on R (topological, 0 or 1)
  - Internal integration over C×R for each propagator
- **Estimated effort**: MEDIUM (1-2 pages of explicit degree bookkeeping)
- **Priority**: Implement m₁/m₂/m₃ in compute FIRST, then prove truncation

### E3. Abelian CS: boundary = û(1)_k
- **Status**: ProvedElsewhere (CDG, KZ) ✓
- **Compute**: Complete (trivial abelian case)

### E4. Virasoro: truncation at m₇ ⚠️
- **Status**: NEEDS VERIFICATION
- **File**: w-algebras.tex
- **Compute**: Degenerate (Jacobi = `return S.Zero`)
- **Strategy**: Power counting on Virasoro Feynman diagrams. The T(z)T(w) OPE has
  poles up to order 4. Higher m_k require more propagators, which increase the
  pole order. The truncation at m₇ comes from the constraint that the total pole
  order cannot exceed... (needs explicit analysis).
- **Priority**: Implement REAL Virasoro Jacobi check first

### E5. W₃: higher operations ⚠️
- **Status**: NEEDS VERIFICATION
- **File**: w-algebras.tex (1185 lines — second largest file)
- **Strategy**: Feynman diagram enumeration for m₃(T,T,T), m₃(T,T,W), m₃(T,W,W), etc.
  The W₃ algebra has two generators T (weight 2) and W (weight 3), with OPE containing
  composite fields :TT: and :TW: and the Lambda composite.
  This is computationally intensive but finite.

---

## VII. CROSS-VOLUME BRIDGES (5 bridges)

### BR1. Bar-cobar bridge
- **Claim**: SC^{ch,top} bar-cobar specializes Vol I Theorem A when curve=C, top=R
- **Status**: Conjectured (should become labeled conjecture with precise hypotheses)
- **Dependencies**: F5 (rectification), Vol I Theorem A
- **What would a proof require**: Operadic comparison map SC^{ch,top} → BD^{ch}, inducing
  bar(SC^{ch,top})-algebra → bar(BD^{ch})-algebra, compatible with the twisting morphisms.

### BR2. Hochschild bridge
- **Claim**: BV-BRST → Vol I Theorem H complex
- **Status**: Conjectured
- **Dependencies**: H2 (bulk ≃ HC), Vol I Theorem H
- **What would a proof require**: Dimensional reduction C×R → C (integrate out R), showing
  the BV cochain complex dimensionally reduces to the chiral Hochschild complex of Vol I.

### BR3. DK/YBE bridge
- **Claim**: r(z) = Laplace of λ-bracket recovers DK-0 evaluation-locus shadow
- **Status**: Conjectured
- **Dependencies**: H3 (R(z) from bulk-boundary), H4 (classical limit), Vol I DK-0
- **What would a proof require**: Show the Stokes derivation of R(z) on FM₃(C) matches
  the operadic R-matrix construction in Vol I's DK square.

### BR4. W-algebra bridge
- **Claim**: Feynman-diagrammatic m_k matches Vol I bar differential at genus 0
- **Status**: Conjectured
- **Dependencies**: E4-E5, Vol I MC5 (BV/BRST = bar)
- **What would a proof require**: Show the Feynman diagram expansion of m_k for W-algebras
  reproduces the bar differential computed algebraically in Vol I.

### BR5. (H1)-(H4) functor bridge
- **Claim**: The analytic hypotheses define a functor from 3D HT QFTs to A∞ chiral algebras
- **Status**: Programme-level
- **What would a proof require**: General proof of (H1)-(H4) for a class of theories
  (e.g., all perturbative 3D HT theories with polynomial interaction).

---

## VIII. DEPENDENCY GRAPH

```
F1 (SC well-def) ─── DONE
  │
  ├── F2 (closed ≃ BD) ─── ProvedElsewhere
  │
  ├── F3 (recognition) ⚠️ ────────────────── blocks B2
  │
  ├── F4 (operad ⟹ axioms) ⚠️ ──────────── blocks F5, B1, H3
  │     │
  │     └── F5 (axioms ⟹ operad) ⚠️ ────── blocks BR1, H5
  │
  └── D1 (reg/sing) ─── DONE
        │
        ├── D2 (commutativity) ⚠️ ── LOW effort, ATTACK NOW
        │
        ├── D3 (λ-bracket) ⚠️ ────── LOW effort, ATTACK NOW
        │     │
        │     ├── D4 (Leibniz) ⚠️ ── MEDIUM effort
        │     │
        │     ├── D5 (Jacobi) ⚠️⚠️⚠️ ── HARD, depends on FM1
        │     │     │
        │     │     └── D6 (higher vanish) ⚠️⚠️ ── HARD
        │     │
        │     └── H4 (r(z) = Laplace) ⚠️
        │
        └── H3 (R(z) from bulk-boundary) ⚠️
              │
              └── BR3 (DK/YBE bridge)

FM1 (Stokes → A∞) ⚠️ ─── blocks D5

B1 (chain-level A∞) ── Conditional on (H1)-(H4)
  │
  └── H2 (bulk ≃ HC) ⚠️
        │
        └── BR2 (Hochschild bridge)
```

### Critical path: D2 → D3 → D4 → D5 → D6
The PVA descent sequence is the backbone. D2 and D3 can be attacked NOW.
D5 (Jacobi) is the hardest step and the most valuable theorem.

### Independent tracks:
- F3 (recognition) can proceed in parallel with PVA descent
- F4/F5 (equivalence) can proceed in parallel with D2/D3
- E2 (LG truncation) + compute implementation can proceed in parallel with everything
