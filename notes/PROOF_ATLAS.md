# PROOF ATLAS — Volume II
# Every proof that needs to exist, with dependencies, strategies, and current status.
# March 2026 — Updated 2026-03-17 after foundational PVA repair and closure campaign.

> This document is the proof programme for Volume II. It maps every theorem that the
> paper aspires to prove, the dependencies between them, and concrete strategies for
> each. When a proof is completed, update the status here AND in concordance.tex.
>
> **Current state (2026-03-17)**: ALL foundational items (F3-F5, FM1, D2-D6) PROVED.
> Zero conjectural algebraic inputs remain; only standing physical axioms (H1)-(H4).

---

## I. OPERADIC FOUNDATIONS (§1-§3, §5)

### F1. Swiss-cheese operad well-definedness
- **Claim**: SC^{ch,top} with FM_k(C) × E_1(m) is a well-defined colored operad
- **Status**: ProvedHere ✓ CLOSED
- **File**: foundations.tex
- **Dependencies**: FM compactification (classical), E_1 operad (classical)

### F2. Closed color ≃ BD chiral operad
- **Claim**: The closed (ch) color of SC^{ch,top} recovers the BD chiral operad via zigzag
- **Status**: ProvedElsewhere ✓ CLOSED (CG, Lurie)
- **File**: foundations.tex

### F3. Recognition theorem
- **Claim**: Prefactorization algebras on C×R satisfying locality axioms ≃ C_*(W(SC^{ch,top}))-algebras
- **Status**: PROVED HERE ✓ CLOSED
- **File**: foundations.tex (thm:recognition), locality.tex (thm:recognition-SC, lem:product-weiss-descent)
- **Proof mechanism**: Weiss cosheaf descent lemma (4-step):
  1. Product decomposition of Weiss covers: covers of D×I project to Weiss covers of D and I
  2. Holomorphic descent along C: CG17 recognition for meromorphic prefactorization algebras
  3. Topological descent along R: AF15 recognition for locally constant prefactorization algebras
  4. Künneth assembly: C_*(FM_k(C)) ⊗ C_*(E_1(m)) ≃ C_*(FM_k(C) × E_1(m))
  Higher coherences from W-resolution product decomposition.

### F4. Operad ⟹ axioms direction
- **Claim**: A C_*(W(SC^{ch,top}))-algebra produces m_k satisfying A∞ chiral axioms
- **Status**: PROVED HERE ✓ CLOSED
- **File**: axioms.tex (prop:operad-implies-axioms)
- **Proof mechanism**: 4-part verification:
  (I) Unitality from operadic units
  (II) Sesquilinearity from C-translation equivariance
  (III) A∞ relations from boundary stratification of FM_k(C) + spectral substitution
  (IV) Degree from operadic suspension

### F5. Axioms ⟹ operad direction (rectification)
- **Claim**: Tame A∞ chiral data rectifies to C_*(W(SC^{ch,top}))-algebra
- **Status**: PROVED HERE ✓ CLOSED
- **File**: axioms.tex (thm:rectification)
- **Proof mechanism**: 4-step bar-cobar rectification:
  1. Construct conilpotent coalgebra C_A = T^c(s^{-1} bar{A}) over B(SC^{ch,top})
  2. Apply cobar functor; homotopy-Koszulity (thm:homotopy-Koszul) identifies Ω B ≃ W
  3. Verify agreement on fundamental chains: cogenerator projection recovers m_k
  4. Quillen equivalence gives uniqueness up to contractible ambiguity

---

## II. BV-BRST CONSTRUCTION (§6)

### B1. Chain-level A∞ structure from BV-BRST
- **Status**: CONDITIONAL on (H1)-(H4) ✓
- **File**: bv-construction.tex
- **Notes**: Physics input. Mathematical content is in F4.

### B2. Compatibility with W(SC^{ch,top})
- **Status**: CONDITIONAL on (H1)-(H4) ✓ (F3 now proved, so reduces to B1)
- **File**: bv-construction.tex

---

## III. PVA DESCENT (§7-§9) — ALL CLOSED

### D1. Regular/singular decomposition
- **Status**: ProvedHere ✓ CLOSED

### D2. Commutativity of product on H•
- **Status**: PROVED HERE ✓ CLOSED
- **File**: pva-descent-repaired.tex (prop:product-commutative)
- **Proof mechanism**: Exchange cylinder in Conf_2(R×C). Explicit path
  x_1(s) = (-cos(πs), re^{iπs}), x_2(s) = (cos(πs), -re^{iπs}).
  The holomorphic separation 2re^{iπs} ≠ 0 ensures the path avoids the diagonal.
  Stokes on the cylinder gives μ(a,b) - (-1)^{|a||b|}μ(b,a) = Q-exact.

### D3. Skew-symmetry of λ-bracket
- **Status**: PROVED HERE ✓ CLOSED
- **File**: pva-descent-repaired.tex (prop:PVA2_proof)
- **Proof mechanism**: Same exchange cylinder, singular sector.
  Degree-(-1) Koszul sign (-1)^{(|a|+1)(|b|+1)} + Borel transform ζ→λ.

### D4. Leibniz rule
- **Status**: PROVED HERE ✓ CLOSED
- **File**: pva-descent-repaired.tex (prop:PVA3_proof)
- **Proof mechanism**: Mixed regular-singular three-face Stokes on FM_3(C).
  Three divisors D_{12}, D_{23}, D_{13} contribute {a_λ b}·c, {a_λ(bc)}, b·{a_λ c}.
  Standard PVA Leibniz rule emerges — no Wick integral correction needed.

### D5. Jacobi identity
- **Status**: PROVED HERE ✓ CLOSED
- **File**: pva-descent-repaired.tex (thm:Jacobi)
- **Proof mechanism**: Full three-face singular-singular Stokes on FM_3(C).
  Key correction: D_{13} face is NOT discarded (non-consecutive ≠ vanishing).
  D_{13} produces the third Jacobi term with sign from ε_{13}=-1 and Koszul transposition.
  AOS cancellation at codimension-2 corners. Jacobiator is Q-exact → vanishes on cohomology.

### D6. Higher m_{k≥3} vanish on H•
- **Status**: PROVED HERE ✓ CLOSED
- **File**: pva-descent-repaired.tex (prop:m3_vanish, lem:topological-contraction)
- **Proof mechanism**: H3(a) factorization + topological contractibility.
  Key insight: H3(a) says ω_k = ω_k^hol ∧ ω_k^top, so the topological contraction
  (from Conf_k^<(R)/transl ≅ R^{k-1}_{>0}, contractible) acts purely in the R-fibre
  and cannot create holomorphic singularities. The "compatible K_k" are consequences
  of H3(a), NOT extra hypotheses.
  4-step proof: invoke H3(a) → construct bounding chain via contractibility →
  define homotopy h_{k-1} by integrating ω_k^hol over FM_k(C) × Γ_{k-1} →
  Stokes in topological fibre recovers m_k as Q-exact.

---

## IV. FM CALCULUS (§8) — CLOSED

### FM1. Stokes → A∞ relations
- **Status**: PROVED HERE ✓ CLOSED
- **File**: fm-calculus.tex (thm:stokes_arnold)
- **Proof mechanism**: 8-step proof:
  1. Stokes as master equation
  2. General residue-to-composition via inner/outer coordinate decomposition
  3. Explicit k=2 verification with Koszul sign (-1)^{|a|}
  4. Explicit k=3 verification: four boundary divisors, spectral substitution Λ_{12}=λ_1+λ_2
  5. Non-consecutive vanishing: time-ordering forces zero net winding
  6. General Koszul sign computation
  7. AOS cancellation at codimension-2 corners (sign flip + recursive Stokes)
  8. Assembly into A∞ identity

### FM2. AOS corner cancellations
- **Status**: ProvedElsewhere ✓ CLOSED (Arnold)

---

## V. HOCHSCHILD AND CONNECTIONS (§13-§18)

### H1. Chiral Hochschild cochain complex
- **Status**: ProvedHere ✓
- **File**: hochschild.tex, brace.tex

### H2. Bulk ≃ chiral Hochschild
- **Status**: ProvedHere ✓
- **File**: hochschild.tex (thm:bulk-CHC)
- **Proof**: Three-step argument (translation invariance + contractibility + filtration)

### H3. Spectral R(z) from bulk-boundary
- **Status**: ProvedHere ✓
- **File**: spectral-braiding.tex
- **Dependencies**: Conditional on (H1)-(H4)

### H4. Classical r(z) = Laplace of λ-bracket
- **Status**: ProvedHere ✓
- **File**: spectral-braiding.tex

### H5. Line operators ≃ A!-modules
- **Status**: ProvedHere ✓
- **File**: line-operators.tex (thm:lines_as_modules)
- **Dependencies**: Homotopy-Koszulity (thm:homotopy-Koszul, proved)

---

## VI. EXAMPLES (§11-§12, §19-§20)

### E1. Free multiplet: m_{k≥3} = 0
- **Status**: ProvedHere ✓ CLOSED

### E2. LG cubic: truncation at m₃
- **Status**: ProvedHere ✓
- **File**: examples-computing.tex

### E3. Abelian CS: boundary = û(1)_k
- **Status**: ProvedElsewhere ✓ CLOSED (CDG, KZ)

### E4. Virasoro: truncation at m₇
- **Status**: Conditional on (H1)-(H4)
- **File**: w-algebras.tex

### E5. W₃: higher operations
- **Status**: Conditional on (H1)-(H4)
- **File**: w-algebras.tex

---

## VII. CROSS-VOLUME BRIDGES (5 bridges)

### BR1. Bar-cobar bridge
- **Status**: ProvedHere ✓ (thm:mc5-genus-zero-bridge)

### BR2. Hochschild bridge
- **Status**: ProvedHere ✓ (thm:hochschild-bridge-genus0)

### BR3. DK/YBE bridge
- **Status**: ProvedHere ✓ (Laplace bridge)

### BR4. W-algebra bridge
- **Status**: ProvedHere ✓ (genus-0 bar = Feynman)

### BR5. PVA-Coisson bridge
- **Status**: ProvedHere ✓ (thm:pva-coisson-bridge; PVA at X=pt recovers Coisson)

---

## VIII. DEPENDENCY GRAPH (all resolved)

```
F1 (SC well-def) ─── ✓
  │
  ├── F2 (closed ≃ BD) ─── ✓
  │
  ├── F3 (recognition) ─── ✓ (Weiss descent)
  │
  ├── F4 (operad ⟹ axioms) ─── ✓
  │     │
  │     └── F5 (axioms ⟹ operad) ─── ✓ (homotopy-Koszulity)
  │
  └── D1 (reg/sing) ─── ✓
        │
        ├── D2 (commutativity) ─── ✓ (exchange cylinder)
        │
        ├── D3 (λ-bracket) ─── ✓ (exchange cylinder + Borel)
        │     │
        │     ├── D4 (Leibniz) ─── ✓ (mixed three-face Stokes)
        │     │
        │     ├── D5 (Jacobi) ─── ✓ (three-face singular Stokes + AOS)
        │     │     │
        │     │     └── D6 (higher vanish) ─── ✓ (H3(a) + contractibility)
        │     │
        │     └── H4 (r(z) = Laplace) ─── ✓
        │
        └── H3 (R(z) from bulk-boundary) ─── ✓

FM1 (Stokes → A∞) ─── ✓ (8-step proof)

B1 (chain-level A∞) ─── ✓ (conditional H1-H4)
  │
  └── H2 (bulk ≃ HC) ─── ✓
```

### Status summary: ALL foundational items PROVED.
The only remaining conditions are the standing physical axioms (H1)-(H4),
which are verified in the worked examples but not proved in general.
