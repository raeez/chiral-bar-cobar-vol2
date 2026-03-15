# CLAUDE.md — A-infinity Chiral Algebras in 3D HT QFT

## Identity

Research collaborator for Raeez Lorgat's paper on $A_\infty$ chiral algebras in 3D holomorphic-topological quantum field theory. This is the **physics face** of modular Koszul duality — Volume II of a unified research programme whose algebraic face is the monograph at `~/chiral-bar-cobar`. The two volumes share a common theorem graph, status discipline, and verification infrastructure.

**Title**: *$A_\infty$ Chiral Algebras and Chiral Hochschild Cohomology in 3D Holomorphic--Topological QFT*

**Relationship to the monograph**: The monograph (Volume I) starts from abstract Koszul duality and connects to physics. This paper (Volume II) starts from 3D HT physics and derives the algebraic structure. They are complementary faces of modular homotopy theory for factorization algebras on curves.

**The Dual Imperative**: Maximalist ambition (push for the most powerful theorems) synergizes with maximal truth-seeking (know exactly what is proved). Precision enables ambition. When claims outrun proofs, strengthen the proof first.

**Epistemic status**: This paper is a first pass. The ideas carry genuine insight, but the mathematics may only be approximately correct and the formulations may not have yet found their true form of expression. Do NOT assume correctness — every claim must be verified, not rubber-stamped. The restructuring should surface uncertainties and make them easier to resolve, not paper over them. The status audit must be genuinely critical: distinguish between the insight (real) and its current articulation (approximate).

---

## The Paper

**Core construction**: The Swiss-cheese operad $\mathsf{SC}^{\mathrm{ch,top}}$ with two colors (closed=holomorphic, open=topological). Its Boardman-Vogt resolution $W(\mathsf{SC}^{\mathrm{ch,top}})$ governs A-infinity chiral algebras — the algebraic structure on bulk local operators of 3D HT QFTs on $\mathbb{C} \times \mathbb{R}$.

**Two equivalent formulations**:
1. **Operadic**: Algebras over $C_*(W(\mathsf{SC}^{\mathrm{ch,top}}))$
2. **Axiomatic**: Higher operations $m_k: A^{\otimes k} \to A((\lambda_1))\cdots((\lambda_{k-1}))$ with spectral substitution

**Main results** (all conditional on (H1)-(H4) where indicated):
- Swiss-cheese recognition theorem (operadic ↔ prefactorization)
- Operad ↔ axioms equivalence
- PVA descent: $H^\bullet(A,Q)$ carries (-1)-shifted Poisson vertex algebra
- Bulk = chiral Hochschild cochains
- Bar-cobar adjunction for $\mathsf{SC}^{\mathrm{ch,top}}$
- Spectral braiding $R(z)$ solving Yang-Baxter equation
- Classical limit: $r(z) = \text{Laplace transform of } \lambda\text{-bracket kernel}$

**Examples**: Free chiral multiplet, Landau-Ginzburg cubic, abelian Chern-Simons, Virasoro, $W_3$.

---

## Build System

- `make` — Full build (multi-pass, stamp-based)
- `make fast` — Single pdflatex pass. **Primary iteration tool.**
- `make clean` — Remove build artifacts
- `make test` — Run computational tests (`cd compute && python -m pytest tests/ -q`)
- Build command: `pkill -9 -f pdflatex 2>/dev/null || true; sleep 1; make fast`

---

## Session Entry Protocol

1. Build: `make fast`
2. Tests: `cd compute && python -m pytest tests/ -q`
3. Read concordance.tex for status
4. Read relevant chapter files before editing
5. After each edit: verify `make fast` compiles
6. Never guess a formula — compute it or cite it

---

## Mathematical Invariants — CRITICAL PITFALLS

### Grading and Conventions (inherited from monograph)
- COHOMOLOGICAL grading: |d| = +1
- Bar uses DESUSPENSION: B(A) = T^c(s^{-1}A-bar, d)
- Suspension: sV = V[-1] under V[n]^k = V^{k+n}

### Swiss-Cheese Operad (paper-specific)
- Two colors: ch (closed, holomorphic) and top (open, topological)
- Operations: SC(ch,...,ch; ch) = FM_k(C); SC(ch,...,ch,top,...,top; top) = FM_k(C) x E_1(m)
- NO open-to-closed operations: SC(...,top,...; ch) = empty
- Chain operad: C_*(W(SC^{ch,top})) — the homotopy-coherent version
- Closed color restricts to BD chiral operad via zigzag of quasi-isomorphisms

### Spectral Parameters
- m_k: A^{otimes k} -> A((lambda_1))...((lambda_{k-1})), degree 1-k
- lambda_i are difference coordinates: lambda_i corresponds to z_i - z_k (relative to last slot)
- Sesquilinearity LEFT: m_k(..., partial a_i, ...) = -lambda_i * m_k(..., a_i, ...)
- Sesquilinearity RIGHT: m_k(..., partial a_k) = (sum lambda_j + partial) * m_k(...)
- Block fusion: inner block replaced by sum of parameters (spectral substitution principle)

### Regular/Singular Decomposition of m_2
- m_2(a,b) = m_2^{reg}(a,b) + m_2^{sing}(a,b)
- Regular part: A[[lambda]] — gives commutative product on cohomology
- Singular part: lambda^{-1}A[[lambda^{-1}]] — gives lambda-bracket on cohomology
- Product on H*: [a].[b] = Sym(m_2^{reg}(a,b)) — commutative, associative
- Bracket on H*: {a_lambda b} = ASym(m_2^{sing}(a,b)) — sesquilinear, skew, Jacobi, Leibniz

### The Four Analytic Hypotheses (H1)-(H4)
These are LOAD-BEARING. Never absorb them silently into other statements.
- (H1) BV Data and HT Gauge Fixing: consistent BV quantization, one-loop finiteness
- (H2) Propagator Regularity: meromorphic in C, exponential decay in R, simple pole near collision
- (H3) Configuration Space Renormalization: FM compactification, logarithmic forms, AOS relations
- (H4) Factorization Compatibility: cluster limits assemble to C_*(W(SC^{ch,top}))-algebra
- Verified in: free multiplet, LG cubic, abelian CS

### Cross-Reference to Monograph Pitfalls
The following invariants from ~/chiral-bar-cobar/CLAUDE.md apply here:
- Com^! = Lie (NOT coLie); Sym^! = Lambda
- Heisenberg NOT self-dual: H^! = Sym^ch(V*)
- CHIRAL KOSZULNESS != CLASSICAL KOSZULNESS (chiral bar uses all OPE poles via Borcherds)
- Bar differential: d_bracket^2 != 0; full d = d_bracket + d_curvature satisfies d^2 = 0
- Feigin-Frenkel involution: k <-> -k-2h^dual (NOT -k-h^dual)
- Sugawara UNDEFINED at critical level (not "diverges")
- W_3 composite: Lambda = :TT: - (3/10)partial^2 T (MINUS sign)
- FM compactification: C-bar_n(X) = Bl (blowup), NOT X^n \ Delta
- QME: hbar*Delta*S + (1/2){S,S} = 0 (factor 1/2)

### A-infinity Conventions
- Stasheff identity: Sum_{i+j=n+1} Sum_{s=0}^{n-j} (-1)^{epsilon(s,j)} m_i(..., m_j(...)|Lambda_block, ...) = 0
- Sign: epsilon(s,j) = (j-1)(|a_1|+...+|a_s|) — Koszul sign
- Curved: m_1^2(a) = m_2(m_0,a) - m_2(a,m_0) = [m_0,a] (COMMUTATOR, MINUS sign)

### Physics Formulas
- Free propagator: K(t-t',z-z') = Theta(t-t')/(2pi(z-z'))
- Virasoro lambda-bracket: {T_lambda T} = partial T + 2T lambda + (c/12)lambda^3
- Virasoro action: S_Vir = integral mu(d_t+dbar)T + T mu partial mu + (c/24) mu partial^3 mu
- CS boundary: J(z)J(w) ~ k/(z-w)^2 (affine KM at level k)
- Abelian CS R-matrix: R(z) = exp(hbar q_1 q_2 / z)

---

## H/M/S Semantic Levels (inherited from monograph)

- **H-level**: Homotopy-native (derived/infinity-categorical/formal-moduli)
- **M-level**: Model-level (dg/bar-complex/chain model/explicit formulas)
- **S-level**: Shadow (cohomological/numerical/generating-function)

---

## Status Tags (inherited from monograph)

- `\ClaimStatusProvedHere` — proved completely in this paper
- `\ClaimStatusProvedElsewhere` — proved in monograph or literature (cite source)
- `\ClaimStatusConjectured` — stated precisely but unproved
- `\ClaimStatusHeuristic` — physical identification without mathematical proof
- `\ClaimStatusOpen` — open problem

**Paper-specific status refinement**: Many results are conditional on (H1)-(H4). Use `\ClaimStatusProvedHere` with an explicit note "conditional on (H1)-(H4)" when the proof assumes the analytic hypotheses.

---

## Cross-Volume Bridges

Five precise bridges connect this paper to the monograph. Each should be stated as a theorem or conjecture with status tag.

1. **Bar-cobar bridge**: SC^{ch,top} bar-cobar (§9) specializes the monograph's Theorem A when the curve is C and the topological direction is R.
2. **Hochschild bridge**: This paper's bulk=Hochschild (§8) provides the BV-BRST origin of the monograph's Theorem H complex.
3. **Yang-Baxter/DK bridge**: Classical r(z) = Laplace of lambda-bracket (§11) provides physical origin for the monograph's DK-0 evaluation-locus shadow.
4. **W-algebra bridge**: Paper's Feynman-diagrammatic m_k (§13) should match monograph's bar differential at genus 0 via BRST=bar (MC5).
5. **(H1)-(H4) bridge**: The analytic hypotheses define the physics-to-algebra functor — conditions under which the BV construction lands in the monograph's algebraic framework.

---

## Known Internal Issues (from v41 audit, March 2026)

### CRITICAL
1. **Free multiplet H⁰ contradiction**: examples-computing.tex says H⁰(A,Q) = C; examples-complete.tex says H⁰ = C[F_n]. One is wrong. Resolve before any other examples work.
2. ~~LG cubic compute = ALL stubs~~ **RESOLVED**: m1_lg (Q^2=0), m2_lg (free product), m3_lg (2g cubic vertex), m_{k>=4}=0 (form degree counting). 14 tests.
3. ~~Virasoro Jacobi = `return S.Zero`~~ **RESOLVED**: Full symbolic Jacobi computation with sesquilinearity. Component-by-component verification. 10 tests.

### HIGH
4. ~~Sesquilinearity stubs~~ **RESOLVED**: verify_sesquilinearity_left/right implemented in ainfty.py. Tested on Virasoro (left+right) and abelian/su(2) (left).
5. **(H4) vaguely stated**: "tameness hypotheses" is not a mathematical definition. (H4) needs a precise formulation.
6. **PVA descent proved THREE times**: pva-preview.tex §7, fm-calculus.tex §8, pva-descent.tex §9 all contain overlapping PVA arguments. Consolidate to ONE authoritative location.

### MEDIUM
7. **Broken cross-references**: eq:sesqui_1, eq:sesqui_i are referenced but never defined as \label.
8. **Empty appendix stubs**: brace-signs.tex has 5 lines, orientations.tex has 6 lines.
9. **Virasoro truncation at m₇**: claimed without proof; needs explicit power counting with bidegree analysis.

---

## What NOT To Do

- Do not change mathematical content during restructuring — preserve exactly
- Do not add packages without checking preamble compatibility
- Do not create new .tex files when content belongs in existing chapter
- Do not duplicate definitions — reference from theory chapters
- Do not use \newcommand in chapter files (all macros in main.tex preamble)
- Do not absorb (H1)-(H4) silently into theorem statements
- Do not treat the cross-volume bridges as analogies — they must be precise theorems
- Do not lose the physics voice while importing algebraic formalism from the monograph
- Do not add TODO comments — track externally
- Do not blur the conditional-on-(H1)-(H4) status across chapters
- Do not implement Jacobi verification as `return S.Zero` — compute it or prove it
- Do not leave `pass` stubs as implementations — implement or remove honestly
- Do not claim "ProvedHere" for a result whose proof is a sketch or physical intuition

---

## Git Attribution — HARD RULE

All git commits are authored by Raeez Lorgat. Never credit an LLM. No "co-authored-by", no "generated by", no AI attribution anywhere in the repo.

---

## File Map

### Theory (chapters/theory/)
- `foundations.tex` — §1 Operadic model: SC^{ch,top}, FM, factorization on C×R
- `raviolo.tex` — §2 Raviolo vertex algebras from time-slice restriction
- `locality.tex` — §3 Holomorphic-topological locality
- `axioms.tex` — §4 Concrete axioms for A∞ chiral algebras (m_k, sesquilinearity, signs)
- `equivalence.tex` — §5 Operad ↔ axioms equivalence
- `bv-construction.tex` — §6 BV-BRST: from QFT to A∞ chiral algebras
- `pva-preview.tex` — §7 A∞ to PVA on cohomology (first pass)
- `fm-calculus.tex` — §8 Fulton-MacPherson calculus & proof of A∞ relations
- `pva-descent.tex` — §9 Cohomological descent: A∞ to Poisson vertex algebras (full)
- `raviolo-restriction.tex` — §10 Čech/Thom-Sullivan model and coinvariants

### Examples (chapters/examples/)
- `examples-computing.tex` — §11 Computing A∞ operations (free, LG, CS)
- `examples-complete.tex` — §12 Complete computations (extended)
- `examples-worked.tex` — §19 Worked examples (bar-cobar applications)
- `w-algebras.tex` — §20 W-algebras: Virasoro and W_3

### Connections (chapters/connections/)
- `hochschild.tex` — §13 Chiral Hochschild cohomology and bulk-boundary
- `brace.tex` — §14 Brace algebra on FM(C)×Conf(R)
- `bar-cobar-review.tex` — §15 Chiral bar-cobar and Koszul duality (review)
- `line-operators.tex` — §16-17 Line operators + bar-cobar for SC^{ch,top}
- `spectral-braiding.tex` — §18 Bulk-boundary functoriality and spectral R(z)
- `conclusion.tex` — §21 Conclusion and outlook
- `concordance.tex` — Constitutional status ledger (normative)

### Appendices (appendices/)
- `brace-signs.tex` — §A Brace signs and degree conventions
- `orientations.tex` — §B Orientations on FM_k(C)×Conf_m(R) and Stokes
- `fm-proofs.tex` — §C FM calculus: complete proofs
- `pva-expanded.tex` — §D A∞ chiral identities to vertex Poisson axioms

### Compute (compute/)
- `lib/` — verification modules (ainfty.py, pva.py, spectral.py)
- `lib/examples/` — worked example implementations (free_multiplet, lg_cubic, virasoro, abelian_cs)
- `tests/` — pytest test suite (test_examples.py, test_pva.py, test_signs.py)

### Planning (notes/)
- `SESSION_PROMPT.md` — Execution doctrine and priority stack
- `autonomous_state.md` — Session state, proof pipeline, compute status
- `PROOF_ATLAS.md` — Every proof that needs to exist, with dependencies and strategies
- `PROGRAMMES.md` — Research programme organized by front (8 fronts, maturity assessment)
- `COMPUTE_ROADMAP.md` — Detailed compute infrastructure plan with test specifications
