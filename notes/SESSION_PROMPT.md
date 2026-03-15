# SESSION PROMPT — Volume II: A∞ Chiral Algebras
# Launch: "Read notes/SESSION_PROMPT.md and execute it."
# Date: March 2026. References CLAUDE.md for invariants.

> **Epistemic calibration.** This paper is a first pass. The insight is real but the
> articulation is approximate. Every claim is a defendant. The goal of every session
> is to narrow the gap between aspiration and achievement: prove what can be proved,
> sharpen what can be stated, and be honest about what remains open.

---

## COGNITIVE CONTRACT

You are a research collaborator on Volume II of a two-volume research programme:

- **Volume I** (~1742pp, ~/chiral-bar-cobar): proved algebraic face (4 main theorems, MC1-2 resolved)
- **Volume II** (~111pp, ~/ainfinity-chiral-hochschild-cohomology-3d-qft): physics face (first pass)

Volume II starts from 3D holomorphic-topological physics and derives A∞ chiral algebras.
Volume I starts from abstract Koszul duality and connects to physics. They converge.

### The Cardinal Rule (inherited from Vol I audit)

**Every claim is a hypothesis about itself until you have traced the proof to ground.**
Vol II has ~18 "Needs Verification" claims and ~8 "ProvedHere" claims. Many of the
ProvedHere are trivial (free multiplet, Laurent decomposition). The genuinely hard
results (Jacobi from AOS, higher m_k vanishing, operad↔axioms equivalence) are ALL
marked Needs Verification. **This honesty is a feature.** The goal is to resolve
Needs Verification claims one by one, either upgrading to ProvedHere or downgrading
to Conjectured/Open.

### The Physics Voice

Vol II must sound like physics. It starts from Feynman diagrams, propagators, BV-BRST,
and derives algebraic structure. The monograph's formalism should appear as consequences,
not premises. When importing Vol I machinery, always show the physics first, then
connect to the algebra. A reader of Vol II should feel they are learning physics that
happens to produce beautiful mathematics, not mathematics wearing a physics costume.

---

## GROUND TRUTH

### Census (March 13, 2026)

| Status | Count | Notes |
|--------|-------|-------|
| ProvedHere | 8 | Mostly trivial (SC well-def, free example, Laurent, AOS corners) |
| ProvedElsewhere | 7 | CG/Lurie, CDG/KZ, Arnold, GLZ |
| Needs Verification | 18 | THE LIVE FRONTIER — every one is a potential theorem |
| Conditional on (H1)-(H4) | 2 | Chain-level A∞, SC compatibility |
| Definition | 2 | Sesquilinearity, A∞ relations |
| Conjectured | 4 | Research signals (formality obstruction, chiral Koszulness, higher genus, spectral beyond eval) |
| Open | 4 | Same research signals |
| **Total** | **~45** | |

### Build
- 111pp, compiles cleanly
- `pkill -9 -f pdflatex 2>/dev/null || true; sleep 1; make fast`

### Tests
- 38 tests, all passing
- ~30% genuine verification (Koszul signs, A∞ arity-4, Laurent arithmetic, OPE coefficients)
- ~70% scaffolding/degenerate (free = trivial, abelian = degenerate, Virasoro Jacobi = `return S.Zero`)
- ALL LG operations are stubs (`pass`)

### Git
- Single commit `cfff744` ("first pass", Nov 2025)
- Massive untracked restructure: main.tex gutted → \input chapter structure
- All chapters/, appendices/, compute/, CLAUDE.md, Makefile untracked

### Internal Issues (from v41 audit)
1. **CRITICAL**: Contradictory free multiplet H⁰ (C vs C[F_n]) across two files
2. **CRITICAL**: LG cubic compute = ALL stubs
3. **HIGH**: Sesquilinearity formula inconsistency within axioms.tex (line 35 vs line 219)
4. **HIGH**: (H4) never checked for any example; vaguely stated
5. **HIGH**: Virasoro Jacobi test = hardcoded `return S.Zero` (tests nothing)
6. **MEDIUM**: Two empty appendix stubs (brace-signs, orientations)
7. **MEDIUM**: Broken cross-references (eq:sesqui_1, eq:sesqui_i)
8. **MEDIUM**: PVA descent proved three times with overlapping notation

---

## ORIENT (first 10 minutes)

1. Build: `cd ~/ainfinity-chiral-hochschild-cohomology-3d-qft && make fast`
2. Tests: `cd ~/ainfinity-chiral-hochschild-cohomology-3d-qft/compute && .venv/bin/python -m pytest tests/ -q`
3. Read `chapters/connections/concordance.tex` — the constitution
4. Read `notes/autonomous_state.md` for recent session results
5. Read `notes/PROOF_ATLAS.md` for the proof programme
6. Read relevant chapter files BEFORE any edit
7. Record state in extended thinking. Then classify and select.

---

## CLASSIFY — Work Surfaces

| Surface | Description | Key files | Risk |
|---------|-------------|-----------|------|
| FOUNDATION | Operadic model, recognition, equivalence | foundations.tex, equivalence.tex | HIGH |
| AXIOM | A∞ axioms, signs, sesquilinearity | axioms.tex | HIGH (sign-intensive) |
| DESCENT | PVA descent, Jacobi, higher vanishing | pva-descent.tex, fm-calculus.tex | HIGHEST |
| EXAMPLE | Free, LG, CS, Virasoro, W₃ | examples-*.tex, w-algebras.tex | MEDIUM |
| CONNECTION | Hochschild, brace, bar-cobar, spectral | hochschild.tex, spectral-braiding.tex | HIGH |
| BRIDGE | Cross-volume bridges to Vol I | concordance.tex, bar-cobar-review.tex | HIGH |
| COMPUTE | Python verification | compute/lib/, compute/tests/ | LOW |
| APPENDIX | Extended proofs, signs | appendices/ | MEDIUM |
| CONTROL | Constitution, status | concordance.tex | HIGH |

---

## SELECT — Prioritization

```
Is there an internal contradiction?              → Fix it NOW (free multiplet H⁰, sesquilinearity)
Is there a Needs Verification → ProvedHere?      → Prove it (highest value work)
Is there a compute stub for a real example?       → Implement it (LG cubic, nonabelian CS)
Is there a cross-volume bridge to formalize?      → Formalize it
Is there a broken cross-reference?                → Fix it
Is there an appendix stub?                        → Fill it
Else                                              → Exposition or prose
```

### Priority Stack

**P0 — Critical (internal contradictions)**:
1. Resolve free multiplet H⁰ contradiction (C vs C[F_n])
2. Fix sesquilinearity formula inconsistency in axioms.tex
3. Fix Virasoro Jacobi — implement real computation, not `return S.Zero`

**P1 — High-value proofs (Needs Verification → ProvedHere)**:
4. PVA commutativity from m₂^reg (symmetry argument — should be provable)
5. λ-bracket from m₂^sing (antisymmetry argument — should be provable)
6. Leibniz rule (outer-reg/inner-sing projection — should be provable)
7. LG truncation at m₃ (degree counting — needs careful ghost number analysis)
8. Operad ⟹ axioms direction (Stokes residue — should be provable)

**P2 — Hard proofs (Needs Verification, requiring significant work)**:
9. Jacobi identity from AOS (the hardest step — FM₃ boundary + Arnold)
10. Higher m_{k≥3} vanish on H• (requires explicit homotopy contractions)
11. Recognition theorem (adapt CG to SC^{ch,top})
12. Axioms ⟹ operad (rectification — inverse direction)

**P3 — Compute infrastructure**:
13. Implement LG cubic m₁/m₂/m₃ + test m₄=0
14. Implement nonabelian Virasoro Jacobi (real computation, not hardcoded zero)
15. Build PVA axiom verifier for worked examples
16. Build FM boundary residue calculator

**P4 — Cross-volume bridges**:
17. Formalize bar-cobar bridge as labeled conjecture
18. Formalize Hochschild bridge as labeled conjecture
19. Formalize YBE/DK bridge as labeled conjecture
20. Formalize W-algebra/BRST bridge as labeled conjecture
21. Formalize (H1)-(H4) functor as programme statement

**P5 — Appendices and exposition**:
22. Fill brace-signs.tex (sign conventions appendix)
23. Fill orientations.tex (FM orientation appendix)
24. Expand fm-proofs.tex (complete FM boundary calculations)
25. Expand pva-expanded.tex (complete arity 2/3 translations)

---

## EXECUTE — Work Protocol

### DESCENT surface (highest risk, highest value)
1. Read fm-calculus.tex IN FULL before any edit
2. Read pva-descent.tex IN FULL
3. For Jacobi: trace the FM₃ boundary → 3 collision divisors → residue compositions → AOS cancellations at corners. Each step must be explicit.
4. For higher vanishing: construct the homotopy h explicitly. Do not assert "by a similar argument."
5. Check ALL signs against CLAUDE.md § A∞ Conventions
6. `make fast` after each theorem

### EXAMPLE surface
1. Read the example chapter AND the compute module simultaneously
2. Every claimed truncation (m_k=0 for k≥K) must have either:
   - A degree-counting proof with explicit ghost number budget, OR
   - A computational verification via compute/lib/examples/
3. Free multiplet: resolve H⁰ contradiction FIRST
4. LG cubic: implement m₁/m₂/m₃ BEFORE writing any new proofs about LG
5. Virasoro/W₃: truncation claims need power-counting proofs with explicit bidegree analysis

### BRIDGE surface
1. Read BOTH CLAUDE.md files before writing any bridge statement
2. Each bridge must be a labeled `\begin{conjecture}...\end{conjecture}` with:
   - Precise hypotheses (which (H1)-(H4) are needed)
   - Precise conclusion (which Vol I theorem is specialized/recovered)
   - Status tag
3. Check convention consistency: Vol I uses LV signs (-1)^{rs+t}; Vol II uses Koszul signs (-1)^{(j-1)(|a₁|+...+|a_s|)}. These are equivalent but look different.

### COMPUTE surface
1. Write tests FIRST, then implement
2. Every test must verify something MATHEMATICAL, not just "code runs"
3. Test tiers (from Vol I audit methodology):
   - Tier 1 (structural): d²=0, Jacobi, associativity — self-certifying
   - Tier 2 (published): known values from Kac, BPZ, etc.
   - Tier 3 (cross-check): two independent code paths agree
   - Tier 4 (regression): "whatever code produced" — AVOID
4. `return S.Zero` is NEVER an acceptable Jacobi verification
5. `pass` stubs must be replaced with implementations or removed

### All surfaces
- After each batch: `make fast` as gate
- At session end: update autonomous_state.md
- Never guess a formula — compute it or cite it
- Never absorb (H1)-(H4) silently

---

## VERIFY — After Each Work Unit

1. `make fast` compiles clean
2. No new undefined refs or multiply-defined labels
3. If claim status changed: update concordance.tex
4. If bridge formalized: check convention consistency with Vol I
5. If computation added: run `cd compute && .venv/bin/python -m pytest tests/ -q`
6. **Trace-to-ground**: for any upgraded claim, state in one sentence what each step depends on

---

## FAILURE MODES

| # | Mode | Signal | Prevention |
|---|------|--------|------------|
| F1 | Absorbing (H1)-(H4) | Theorem without conditional | Always state dependency |
| F2 | Physics-washing | Proof "by physical reasoning" | Physical intuition = evidence, not proof |
| F3 | Sign hand-waving | "Signs work out" | Explicit sign computation or citation |
| F4 | Stub acceptance | LG stubs remain stubs | Implement or mark honestly |
| F5 | Convention collision | Vol I sign ≠ Vol II sign | Check BOTH CLAUDE.md files |
| F6 | Jacobi shortcut | `return S.Zero` | Real computation or proof |
| F7 | Overclaiming | NeedsVerification → ProvedHere without proof | Trace every step |
| F8 | Bridge vagueness | "Should match" instead of precise conjecture | Labeled \begin{conjecture} |
| F9 | Scope creep | Working on Vol I from Vol II | Stay in Vol II; cross-ref Vol I |
| F10 | Duplicate proof | PVA descent proved in 3 places | Consolidate to ONE location |

---

## SESSION END PROTOCOL

1. Build: `cd ~/ainfinity-chiral-hochschild-cohomology-3d-qft && make fast`
2. Tests: `cd compute && .venv/bin/python -m pytest tests/ -q`
3. Update `notes/autonomous_state.md`
4. Update concordance.tex if any status changed
5. Do NOT update CLAUDE.md unless a new Critical Pitfall was found
