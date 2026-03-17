# RESEARCH PROGRAMMES — Volume II Frontier

**Purpose**: Complete inventory of every research front emerging from Volume II,
organized by maturity and dependency. Where Volume I's PROGRAMMES.md tracks the
algebraic frontier *after* the monograph, this document tracks what Volume II
must accomplish, what it points toward, and how the two volumes converge.

**Audience**: Future sessions, referees assessing the programme's coherence,
the author planning attack strategies.

**Governing principle (Dual Imperative)**: Precision enables ambition. Every
front below must be honest about what is sketch, what is proof, and what is
aspiration. The physics voice must remain primary — these are physical results
that happen to produce mathematics, not the reverse.

**Last updated**: March 17, 2026 (post-foundational closure campaign)

**Relationship to other files**:
- `PROOF_ATLAS.md` — Proof-by-proof strategy (the micro view; this file is the macro)
- `SESSION_PROMPT.md` — Execution engine and priority stack
- `autonomous_state.md` — Session-level state
- `COMPUTE_ROADMAP.md` — Detailed compute infrastructure plan
- `~/chiral-bar-cobar/notes/PROGRAMMES.md` — Vol I programme companion

---

## The Two-Volume Programme

Volume I proved modular Koszul duality algebraically. Volume II derives it physically.
The convergence is not metaphorical — each volume proves theorems the other needs.

The **four irreducible pieces** of the unified programme:

| Piece | Vol I face | Vol II face | Status |
|-------|-----------|-------------|--------|
| Configuration space coherence | Arnold relations on FM_n(C) | AOS cancellations in Feynman integrals | Classical (both) |
| Bar-cobar exchange | Verdier duality on Ran(X) (Thm A) | BV-BRST gives SC^{ch,top}-algebra structure | Proved (I) / Conditional (II) |
| Genus-1 curvature | d² = κ·ω₁ (Thm B) | Formality obstruction from higher A∞ | Proved (I) / Conjectured (II) |
| Modular compatibility | Clutching on M̄_g (Thm C/D) | Higher-genus A∞ from string worldsheet | Proved (I) / Open (II) |

The **convergence programme** has five precise bridges (BR1–BR5 in PROOF_ATLAS.md).
None are currently formalized as labeled conjectures with precise hypotheses.
This is the highest-value structural work after the PVA descent proofs.

---

## Status at a Glance (updated 2026-03-17)

| Status | Count | Description |
|--------|-------|-------------|
| ProvedHere | ~35 | ALL foundational items (F3-F5, FM1, D1-D6), homotopy-Koszulity, PVA descent, Hochschild, spectral, examples, cross-volume bridges |
| ProvedElsewhere | ~7 | CG/Lurie (closed ≃ BD), Arnold (AOS), CDG/KZ (abelian CS) |
| Conditional | ~4 | Chain-level A∞ (on H1-H4), Virasoro/W_3 truncation bounds (on H1-H4) |
| Conjectured | ~2 | Higher-genus extension (g≥2), general (H1)-(H4) functor |
| **Total** | **~48** | |

**ALL 18 former NeedsVerification claims are now PROVED.** The paper's core is ~42 secure
claims (35 PH + 7 PE). The remaining frontier is the standing physical axioms
(H1)-(H4) and the higher-genus extension.

### Key closures (2026-03-17 session):
- **D6**: H3(a) factorization + topological contractibility → compatible contractions are CONSEQUENCES
- **F3**: Weiss cosheaf descent lemma (product structure + CG17 + AF15 + Künneth)
- **F5**: Bar-cobar rectification via homotopy-Koszulity (4-step proof)
- **FM1**: 8-step Stokes proof with explicit k=2,3 and AOS corner cancellation
- **D2-D5**: Repaired geometric proofs (exchange cylinder + three-face Stokes on FM_3(C))

---

## Front I: PVA Descent — FULLY CLOSED

### Vision
A∞ chiral algebra on chain level descends to a (−1)-shifted Poisson vertex algebra
on Q-cohomology. This is the central theorem of the paper — everything else is
infrastructure for this or consequences of it.

### ALL axioms proved (2026-03-17)

| Axiom | PROOF_ATLAS | Status | Mechanism |
|-------|------------|--------|-----------|
| Commutativity | D2 | **PROVED** | Exchange cylinder in Conf_2(R×C) |
| Skew-symmetry | D3 | **PROVED** | Exchange cylinder singular + Borel transform ζ→λ |
| Leibniz | D4 | **PROVED** | Mixed regular-singular three-face Stokes on FM_3(C) |
| **Jacobi** | **D5** | **PROVED** | Full three-face singular Stokes + AOS corners |
| Higher vanishing | D6 | **PROVED** | H3(a) factorization + topological contractibility |

### What closed D6 (the breakthrough)
The factorization hypothesis H3(a) — ω_k = ω_k^hol ∧ ω_k^top — means the
topological contraction of Conf_k^<(R) ≅ R^{k-1}_{>0} acts purely in the R-fibre
and cannot create holomorphic singularities. The "compatible higher contraction
homotopies K_k" are CONSEQUENCES of H3(a), not extra hypotheses.

### Gap between aspiration and achievement: CLOSED
The paper now proves the complete PVA descent theorem (D2-D6) via explicit
geometric constructions. Two model studies (free theory, abelian current algebra)
make the dictionary concrete.

---

## Front II: Operadic Equivalence — FULLY CLOSED

### Vision
The A∞ chiral axioms (m_k with sesquilinearity and spectral substitution) are
equivalent to algebra structure over C_*(W(SC^{ch,top})).

### All three directions proved (2026-03-17)

**Forward (F4: operad ⟹ axioms)**: PROVED in axioms.tex. 4-part verification:
unitality, sesquilinearity (translation equivariance), A∞ relations (boundary
stratification + spectral substitution), degree (operadic suspension).

**Reverse (F5: axioms ⟹ operad)**: PROVED in axioms.tex. 4-step bar-cobar
rectification: construct coalgebra C_A over B(SC^{ch,top}), apply cobar functor,
verify agreement on fundamental chains, uniqueness via Quillen equivalence from
homotopy-Koszulity (thm:homotopy-Koszul).

**Recognition (F3)**: PROVED in locality.tex. Weiss cosheaf descent lemma
(lem:product-weiss-descent) closes the gap: product Weiss covers factor,
holomorphic descent (CG17), topological descent (AF15), Künneth assembly.

### Why this matters
Without operadic equivalence, the paper's results are stated twice in incompatible
languages. The equivalence theorem is what makes the two formulations (operadic and
axiomatic) genuinely the same subject.

---

## Front III: Examples — Computational Verification

### Vision
Every claim about a specific physical theory (free multiplet, LG, CS, Virasoro, W₃)
must have either a mathematical proof or a computational verification. Currently,
the examples chapter makes claims backed by stubs.

### Example inventory

| Example | m₁ | m₂ | m₃ | m_{≥4} | H• | Compute % | Critical gap |
|---------|-----|-----|-----|---------|------|-----------|-------------|
| Free multiplet | ✓ (Q²=0) | ✓ (product) | 0 (trivial) | 0 | C | 100% | H⁰ contradiction |
| LG cubic | stub | stub | stub | "=0" (unproved) | C (claimed) | 0% | ALL stubs |
| Abelian CS | ✓ | ✓ (k·λ) | 0 | 0 | J's | ~80% | Trivial abelian |
| Virasoro | N/A | ✓ (OPE→λ-bracket) | unknown | "m₇ trunc" | T,∂T,... | ~30% | Jacobi = S.Zero |
| W₃ | N/A | ✓ (known OPE) | unknown | unknown | T,W,Λ,... | 0% | Not started |

### Attack plan

**Tier 1** (Critical — blocks paper credibility):
1. **Fix free multiplet H⁰ contradiction**: examples-computing.tex says C; examples-complete.tex says C[F_n]. Resolve which is correct and make consistent.
2. **Implement LG cubic m₁/m₂/m₃**: The ALL-stubs state is indefensible. The paper's second worked example has zero computation behind it.
3. **Implement real Virasoro Jacobi**: The `return S.Zero` in `check_virasoro_jacobi` tests NOTHING. Implement the actual Lie conformal algebra Jacobi check.

**Tier 2** (High value — strengthens examples chapter):
4. **LG truncation proof**: Ghost number budget for m₄ = 0. This needs the explicit degree counting with holomorphic/topological split.
5. **Virasoro truncation analysis**: Power counting for m₇ = 0. The OPE has poles up to order 4; how does this constrain higher m_k?
6. **Abelian CS R-matrix computation**: The normalization r(z) = Laplace of λ-bracket needs verification with explicit constants.

**Tier 3** (Expansion — new examples):
7. **Nonabelian CS at level k**: The first genuinely nontrivial R-matrix. SU(2)_k boundary → ĝ_k current algebra. Would verify H4 in a nonabelian setting.
8. **W₃ operations**: m₃(T,T,T), m₃(T,T,W), etc. from Feynman diagrams. Computationally intensive but finite.
9. **Free fermion**: The bc system as an A∞ chiral algebra. Should exhibit F^! = βγ duality.

### What computation would prove
The most powerful computational result would be: implement Virasoro m₂ with REAL
λ-bracket verification (not hardcoded), then show Jacobi holds COMPUTATIONALLY.
This provides independent evidence for D5 (the hardest theorem) before the full
sign-intensive proof is written.

---

## Front IV: Hochschild and Brace Infrastructure

### Vision
The bulk operators of the 3D HT QFT are identified with chiral Hochschild cochains.
This is the physical origin of the monograph's Theorem H complex.

### What needs to exist

| Claim | PROOF_ATLAS | Current state | What's needed |
|-------|------------|---------------|---------------|
| Brace algebra on HC cochains | H1 | Sketched | FM(C) × Conf(R) fiber product construction |
| Gerstenhaber bracket | H1 (derived) | Sketched | Derivation from brace |
| MC ↔ formal deformations | H1 (derived) | Claimed | Standard operadic argument (spell out) |
| Bulk ≃ HC_ch | H2 | Claimed | Quasi-iso via Hochschild universality |

### Gap analysis
The Hochschild section (§13) is one of the weakest parts of the paper. The claims
are stated as if they follow from general operadic principles, but:
- The FM(C) × Conf(R) fiber product is not computed explicitly
- The brace operations are not defined on elements
- The bulk ≃ HC quasi-iso is asserted without proof density

**Strategy**: Write the brace operations explicitly for the free multiplet (where
everything is linear). Then extend to LG by perturbation. The Gerstenhaber bracket
and MC deformation story follow from the brace structure by standard (published)
results.

---

## Front V: Spectral Braiding and R-matrices

### Vision
The bulk-boundary composition in the 3D HT QFT produces a spectral R(z) satisfying
the Yang-Baxter equation. Its classical limit is the Laplace transform of the
λ-bracket kernel.

### The chain of results

```
Bulk-boundary composition → R(z) meromorphic → YBE from FM₃ Stokes → r(z) = Laplace({·_λ ·})
                                                                       ↓
                                                              DK-0 shadow in Vol I
```

### Attack plan
1. **Prove R(z) construction (H3)**: Define R(z) as path-ordered exponential of
   boundary-to-boundary propagator. Show meromorphicity from (H2).
2. **Prove YBE (H3 continued)**: Apply Stokes on FM₃(C) — SAME technique as D5 (Jacobi).
   This is not a coincidence: Jacobi for the λ-bracket and YBE for R(z) are both
   consequences of the FM₃ boundary structure. A unified proof would be ideal.
3. **Prove classical limit (H4)**: r(z) = Res_{λ=0} e^{−λz} {a_λ b}. Verify for
   abelian CS: {J_λ J} = kλ gives r(z) = k/z² (up to normalization).
4. **Connect to Vol I DK (BR3)**: The evaluation-locus R-matrix in Vol I is computed
   algebraically. The Vol II R-matrix is computed physically. Show they agree.

### Relationship to Front I
D5 (Jacobi) and H3 (YBE) share the same proof technology: Stokes on FM₃ + AOS.
The sign computations are different but the geometric content is identical.
Proving one strongly informs the other.

---

## Front VI: Cross-Volume Bridge Formalization

### Vision
The five bridges between Vol I and Vol II must be formalized as labeled conjectures
(or theorems where provable) with precise hypotheses.

### Current state
All five bridges exist as prose descriptions in concordance.tex §34.3. None are
formalized with:
- Explicit hypotheses (which of H1–H4 are needed)
- Precise conclusion (exact statement of what specializes to what)
- Convention reconciliation (Vol I uses LV signs; Vol II uses Koszul signs)
- Dependency chain (which results in each volume are prerequisites)

### The five bridges in detail

**BR1: Bar-cobar bridge** (§15 ↔ Vol I Thm A)
- Claim: SC^{ch,top} bar-cobar on C×R specializes Vol I's bar-cobar on X.
- Precise version: When X = C and the topological direction is R:
  B_{SC}(A) should be quasi-isomorphic to B_{BD}(A_ch) where A_ch is the
  chiral algebra obtained by restricting the closed color of SC^{ch,top}.
- Requires: F5 (axioms ⟹ operad), Vol I Thm A.
- Convention check: Bar desuspension s^{-1} in both volumes. ✓
  Sign convention: LV (-1)^{rs+t} vs Koszul (-1)^{(j-1)(|a₁|+...+|a_s|)}.
  These are the SAME convention written in different notation (Vol I uses
  the (r,s,t) partition, Vol II uses the (s,j) pair with r = s, s = j, t implicit).
  **VERIFY THIS CLAIM.** If wrong, every sign comparison fails.

**BR2: Hochschild bridge** (§13 ↔ Vol I Thm H)
- Claim: Dimensional reduction C×R → C sends Vol II's bulk=HC_ch to Vol I's Thm H.
- Precise version: The E₁ coinvariant of the SC^{ch,top} Hochschild complex
  should be the BD chiral Hochschild complex of Vol I.
- Requires: H2 (bulk ≃ HC_ch), Vol I Thm H.
- Key gap: The "integrate out R" step is physically obvious but mathematically
  it's a functor from SC^{ch,top}-modules to BD^{ch}-modules. Define this functor.

**BR3: DK/YBE bridge** (§18 ↔ Vol I DK-0)
- Claim: r(z) = Laplace of λ-bracket recovers the evaluation-locus R-matrix of Vol I.
- Precise version: For A = ĝ_k (affine KM), the R-matrix R(z) constructed
  physically (bulk-boundary composition with propagator K) should equal the
  algebraic R-matrix R^{KZ}(z) from the KZ connection.
- Requires: H3, H4, Vol I DK-0.
- This would be the most concrete bridge — verifiable for SU(2)_k.

**BR4: W-algebra bridge** (§20 ↔ Vol I MC5)
- Claim: Feynman-diagrammatic m_k for W-algebras matches Vol I's bar differential.
- Precise version: For A = W_N obtained by DS reduction, the m_k from Feynman
  diagrams on C×R should equal the components d_k of the bar differential
  d = d_CE + d_{curvature} computed algebraically in Vol I.
- Requires: E4/E5, Vol I MC5 (BV/BRST = bar).
- MC5 itself is downstream of MC3/MC4 in Vol I. This bridge is therefore
  DEEPLY conjectural — it requires unproved results in both volumes.

**BR5: (H1)–(H4) functor bridge** (§6 ↔ Vol I Programme VI)
- Claim: (H1)–(H4) define a functor HT-QFT → A∞-chirAl.
- This is programme-level, not a single theorem.
- What would make it precise: a theorem saying "every perturbative 3D HT QFT
  with polynomial interaction satisfies (H1)–(H4)" (a massive analytic result).
- Current status: checked for free, LG cubic, abelian CS (all Gaussian/cubic).

### Priority ordering
BR3 (DK/YBE) is the most concrete — can be verified for abelian CS today.
BR1 (bar-cobar) is the most structurally important — connects the core theorems.
BR2 (Hochschild) is the deepest — requires the dimensional reduction functor.
BR4 (W-algebra) is the most ambitious — requires MC5 in Vol I.
BR5 (functor) is programme-level — not formalizable as a single conjecture.

---

## Front VII: Higher-Genus Extension

### Vision
Volume II works on C × R (genus 0 in the holomorphic direction). The monograph's
genus tower should lift to A∞ with spectral parameters on Σ_g × R.

### What this would require
1. **Replace C with Σ_g**: The propagator K(t,z) on C×R becomes K_g(t,z,w)
   on Σ_g×R, involving the prime form E(z,w) and higher-genus Green's function.
2. **FM_n(Σ_g)**: The configuration space compactification on a genus-g surface.
   The Arnold relations are replaced by higher-genus relations involving the
   period matrix.
3. **Curved A∞**: On Σ_g, the A∞ structure should be curved: m₁² ≠ 0.
   The curvature m₀ should be related to Vol I's κ(A)·ω_g.
4. **Formality obstruction**: The higher-genus A∞ algebra should NOT be formal
   (the PVA descent fails). The obstruction classes in H²(M̄_g) should be
   the genus-g quantum corrections of Vol I.

### Current state
Completely open. The paper mentions this as "Research Signal 3" in concordance.tex.
The mathematical content would be:
- A curved A∞ chiral algebra on Σ_g × R from BV-BRST
- Its curvature m₀ = κ(A) · ω_g (connecting to Vol I Theorem B)
- The tower {m_0^(g), m_1^(g), m_2^(g), ...} indexed by genus
- The full tower assembles into a modular A∞ structure

### Why this is the ultimate bridge
If the higher-genus A∞ structure can be constructed, then Vol II literally
*is* the physics of Vol I. The four main theorems of the monograph would have
physical derivations, not just algebraic proofs.

---

## Front VIII: Formality and Koszulness from Physics

### Vision
(H1)–(H4) + BV-BRST should imply chiral Koszulness for the resulting algebras.
This would give a physical *explanation* of chiral Koszulness — currently an
algebraic property without a known physical reason.

### Why this is hard
The monograph explicitly warns: chiral Koszulness ≠ classical Koszulness.
The chiral bar complex uses all OPE poles (Borcherds), not just the leading pole.
A classical Koszul algebra (like U(g) for reductive g) need not be chiral Koszul.

### What physics could contribute
If the BV-BRST construction produces A∞ chiral algebras that are *automatically*
formal on cohomology (Front I, D6), then the formality theorem would imply:
- The bar complex B(A) computes the "correct" Koszul dual
- Chiral Koszulness follows from formality + PVA structure
- The monograph's MC1 (PBW concentration) has a physical proof

### Current state
Research signal 2 in concordance.tex. No formalization.

---

## Maturity Assessment

### Fully baked (ready to write)
- D2 (commutativity): standard Borcherds argument
- D3 (λ-bracket): standard Borcherds/Kac argument
- Free multiplet H⁰ fix: just resolve the contradiction

### Half baked (strategy clear, execution needed)
- D4 (Leibniz): A∞(n=3) decomposition — the strategy is explicit but the
  spectral substitution → integral step needs computation
- F4 (operad ⟹ axioms): CG template exists, adaptation to SC^{ch,top} needed
- E2 (LG truncation): ghost number budget partially worked out in PROOF_ATLAS
- LG compute implementation: m₁ is just Q, m₂ has known structure, m₃ from cubic vertex

### Quarter baked (direction clear, significant work)
- D5 (Jacobi): the proof outline exists (FM₃ + AOS) but sign bookkeeping is formidable
- F5 (rectification): approach (b) via bar-cobar is cleaner but requires §15
- D6 (higher vanishing): needs explicit homotopy or degree argument per example
- Virasoro real Jacobi: the λ-bracket is known, the n-product formulation is known,
  but implementing the actual Lie conformal algebra Jacobi computation in code

### Prebaked (conception exists, major work to begin)
- BR1–BR4 bridge formalization: precise hypotheses, convention reconciliation
- Hochschild infrastructure (H1–H2): fiber product construction, quasi-iso
- R(z) construction (H3): path-ordered exponential, meromorphicity
- W₃ operations (E5): Feynman diagram enumeration for 2-generator system

### Raw (programme-level, nothing written)
- Higher-genus A∞ (Front VII): would be the ultimate bridge
- Koszulness from physics (Front VIII): research signal, not a theorem
- BR5 functor bridge: requires general (H1)–(H4) verification
- Nonabelian CS (beyond abelian): first nontrivial R-matrix computation

---

## Dependency Ordering for Sessions

```
SESSION N (any session):
  1. If P0 items exist → fix them (contradictions, broken refs)
  2. Pick from the appropriate phase:

PHASE A (current priority):
  D2, D3 → D4 → D5      [PVA descent, the critical path]
  LG compute → E2         [examples credibility]
  Vir real Jacobi          [computational evidence for D5]

PHASE B (after PVA descent):
  F4, F5                   [operadic equivalence]
  BR1, BR3 formalization   [most concrete bridges]

PHASE C (after equivalence):
  H1, H2                   [Hochschild infrastructure]
  H3, H4                   [spectral braiding]
  BR2, BR4                 [deeper bridges]

PHASE D (research frontier):
  Front VII (higher genus)
  Front VIII (Koszulness)
  BR5 (functor)
```

### Estimated page counts for each front

| Front | Current pages | Pages needed | Notes |
|-------|--------------|-------------|-------|
| I (PVA descent) | ~15 (sketches) | ~25 (rigorous) | +10 pages of careful proof |
| II (Operadic equiv) | ~8 | ~15 | +7 pages |
| III (Examples) | ~20 | ~30 | +10 pages of computation |
| IV (Hochschild) | ~10 | ~18 | +8 pages |
| V (Spectral) | ~8 | ~15 | +7 pages |
| VI (Bridges) | ~3 | ~10 | +7 pages (new §) |
| VII (Higher genus) | 0 | ~20 | New chapter |
| VIII (Koszulness) | 0 | ~5 | New section |
| **Total** | **~64** | **~138** | From 111pp → ~185pp |

The paper can reasonably grow from 111pp to ~185pp with all fronts executed.
This is comparable in ambition to the monograph's growth from ~200pp initial
to ~1742pp final — scaled appropriately for a companion paper.

---

## Cross-Volume Convention Reconciliation

### Sign conventions
- Vol I (LV): Σ_{r+s+t=n} (−1)^{rs+t} m_{r+1+t}(id^r ⊗ m_s ⊗ id^t) = 0
- Vol II (Koszul): Σ_{i+j=n+1} Σ_{s=0}^{n−j} (−1)^{ε(s,j)} m_i(a₁,...,a_s,m_j(...),a_{s+j+1},...,a_n) = 0
  where ε(s,j) = (j−1)(|a₁|+...+|a_s|)

**Claimed equivalence**: With the identification r = s, s = j, t = n−j−s:
  rs + t = sj + n − j − s = (j−1)s + (n−j) = (j−1)|total before| + (correction)
  This needs EXPLICIT verification on elements of definite degree.

### Grading
- Both volumes use COHOMOLOGICAL grading with |d| = +1. ✓
- Both volumes use bar DESUSPENSION B(A) = T^c(s^{-1}Ā, d). ✓
- Both volumes: m_k has degree 1−k. ✓

### Central charges and levels
- Sugawara: T = (1/2(k+h^∨)) Σ :J^a J^a:, c = k·dim(g)/(k+h^∨). ✓ in both.
- Feigin-Frenkel: k ↔ −k−2h^∨. ✓ in both.
- Virasoro DS formula: ✓ in both.

### Propagator conventions
- Vol II: K(t,z) = Θ(t)/(2πz). This is specific to C×R.
- Vol I: Does not use propagators (algebraic, not physical).
- The bridge between propagator-defined m_k (Vol II) and algebraically-defined
  bar differential (Vol I) is exactly MC5.

---

## The Endgame

When all eight fronts are advanced:
- The paper proves that 3D HT QFT produces (−1)-shifted PVAs on Q-cohomology (Front I)
- The operadic and axiomatic formulations are equivalent (Front II)
- Every example is computed and verified (Front III)
- The Hochschild and spectral infrastructure exists (Fronts IV–V)
- The five bridges to Vol I are formalized with precise hypotheses (Front VI)
- The higher-genus extension is articulated as a programme (Front VII)
- The Koszulness-from-physics insight is captured (Front VIII)

At that point, the two-volume programme is genuinely a unified subject:
**modular homotopy theory for factorization algebras on curves**, with an algebraic
face (proved in Vol I) and a physical face (derived in Vol II), connected by five
precise bridges.
