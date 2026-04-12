# Roadmap: 85% → 100%

## Dependency graph

```
[A0] MASTER THEOREM ◄──────────────────────────────────┐
     conformal vector → E_3-top                         │
     (THE theorem the volume must prove)                │
         │                                              │
         ├─── [A] T_DS = [Q_tot, G'] ──────────────────┤
         │         (Virasoro via DS, one route)         │
         │                                              │
         ├─── [A0a] Direct algebraic proof ─────────────┤
         │          (T ∈ im(d_HH) on C*(A,A))          │
         │                                              ▼
[B] Genus ≥ 2 ─────────────────────────────► [E] Global triangle
    operadic                                     beyond Koszul
    verification

[C] Curved Dunn ──── (independent)

[D] Chiral coproduct BCFG ──── (independent)

[F] Adversarial fixes ──── (independent, can be done now)

[G] Infrastructure ──── (independent, can be done now)
```

---

## [A0] THE MASTER THEOREM: CONFORMAL VECTOR → E_3-TOPOLOGICAL

**Goal:** Prove that ANY chiral algebra with a conformal vector at non-critical level has E_3-topological bulk observables. This is THE theorem the volume must prove. As simple as that.

**Statement (target):**

> **Theorem.** Let A be a chiral algebra on X carrying a conformal vector T(z) at non-critical level (i.e., T generates a Virasoro subalgebra Vir_c ⊂ A with c ≠ c_crit). Assume [MINIMAL HYPOTHESES]. Then the derived chiral center Z^{der}_{ch}(A) carries an E_3-topological algebra structure, independent of the complex structure of X.

**What "minimal hypotheses" means:** The conformal vector alone gives:
- E_2 on Z(A) (Deligne conjecture, automatic, no hypothesis)
- T(z) generates translations on A (part of the VA axioms)
- Non-critical level ensures the Sugawara denominator doesn't vanish

The question is: what ADDITIONAL hypothesis (if any) is needed to promote E_2 → E_3-topological?

**Two proof strategies:**

**A0a. Direct algebraic route (preferred, no physics input).**
The conformal vector T ∈ A acts on the Hochschild cochain complex C*(A,A) via the A-bimodule structure. The claim is that T is in the image of the Hochschild differential d_HH on C*(A,A):
$$T = d_{\mathrm{HH}}(G) \quad \text{for some } G \in C^{*-1}(A,A).$$
If this holds, then:
- Step 1: The translation operator ∂_z = [T, -] is d_HH-exact on C*(A,A).
- Step 2: The factorisation algebra Z(A) on X is locally constant in Hochschild cohomology (translations are exact → z-dependence is cohomologically trivial).
- Step 3: Lurie/Ayala-Francis recognition: locally constant factorisation algebra on X = E_2-topological algebra.
- Step 4: Dunn with existing E_1^{top} (transverse) → E_3-topological.

This is purely algebraic — no 3d HT theory, no gauge theory, no BV-BRST needed. The hypothesis is just: T ∈ im(d_HH).

**Key question for A0a:** Is T ∈ im(d_HH) automatic for any conformal vector at non-critical level? Or is it an additional hypothesis?

For KM at non-critical: T_Sug = (1/(2(k+h∨))) Σ_a :J^a J_a:. The Sugawara construction shows T_Sug IS a cup product of currents (it's in the image of the multiplication map μ: A⊗A → A, which is related to d_HH). Whether this means T_Sug ∈ im(d_HH) on the Hochschild complex requires checking.

For general VA with conformal vector: T is an element of weight 2 in A. It may or may not be in im(d_HH). This is the content of the theorem.

**A0b. Physical route (via 3d HT theory).**
If A arises as the boundary of a 3d HT theory (gauge-theoretic or not), and T = [Q, G] in the BRST complex of that 3d theory, then Construction constr:topologization gives E_3-topological. This is the route through items A and A1-A3 below.

**Sub-items for A0:**

- **A0.1.** Determine whether T ∈ im(d_HH) is automatic for conformal vectors at non-critical level, or whether it requires an additional hypothesis (e.g., T comes from Sugawara, or A is chirally Koszul, or A has finite shadow depth).

- **A0.2.** If T ∈ im(d_HH) is automatic: write the proof as a Theorem in 3d_gravity.tex, replacing Conjecture conj:E3-topological-climax.

- **A0.3.** If T ∈ im(d_HH) requires a hypothesis: identify the minimal hypothesis, add it to the theorem statement, and verify it for all standard families (KM, Virasoro, W_N, Heisenberg, lattice VOAs).

- **A0.4.** Verify: does this direct algebraic proof agree with the physical route (Construction constr:topologization) on the overlap (KM at non-critical level)?

**This is the HIGHEST PRIORITY item in the roadmap.** If A0a succeeds, it closes the climax for ALL conformal vertex algebras at non-critical level, without case-by-case gauge-theory input.

---

## [A] THE BRST IDENTITY: T_DS = [Q_tot, G']

**Goal:** Prove E_3-topological for Virasoro (and all W-algebras via DS).

**Current status:** E_3-topological PROVED for KM at non-critical level (Costello-Li). For Virasoro: the Costello-Gaiotto theorem provides the 3d HT theory (holomorphic CS with DS boundary conditions). Construction constr:topologization proves: IF T=[Q,G] THEN E_3-topological. The gap is the specific BRST identity in the DS-modified complex.

**Sub-items:**

- **A1.** Verify that the DS reduction of the Sugawara antighost G_Sug gives a field G' in the DS-modified BV complex satisfying T_DS = [Q_tot, G']. The improvement term (1/2)dJ^h in T_DS should be Q_tot-exact.
  - *Difficulty:* Medium. The ingredients exist (Sugawara proved in Vol I, DS transport proved).
  - *Depends on:* Nothing external. Internal to the manuscript.
  - *Would resolve:* The climax conjecture for Virasoro and all principal W-algebras.

- **A2.** Extend A1 to non-principal DS reductions (subregular, hook-type).
  - *Difficulty:* Hard. Non-principal DS has different BRST structure.
  - *Depends on:* A1.

- **A3.** Determine whether the chain-level E_3-topological structure holds for class M (infinite shadow tower), or only at the cohomological level.
  - *Difficulty:* Hard. Class M chain-level vs cohomological distinction is the deepest issue.
  - *Depends on:* A1.

---

## [B] GENUS ≥ 2 OPERADIC VERIFICATION

**Goal:** Verify the modular operad axioms for O^{A_∞-ch} at genus ≥ 2.

**Current status:** Definition def:modular-operad-ainf-chiral. Genus 0: proved (SC × E_1^tr). Genus 1: explicit operations (R-matrix clutching formula). Composition associativity: proved (stable graph category is Kan). Missing: equivariance and unitality at genus ≥ 2.

**Sub-items:**

- **B1.** Verify equivariance of clutching maps under Aut(Γ) for genus-2 stable graphs.
  - *Key question:* Does quasi-triangularity R·Δ = Δ^op·R provide the equivariance? Or is the operad genuinely non-symmetric (ordered modular operad)?
  - *Difficulty:* Medium-Hard.
  - *Depends on:* Nothing. Can be done now.

- **B2.** Verify that the R-matrix monodromy composition at multi-node curves satisfies π_1(Σ_g) relations: [a_1,b_1]···[a_g,b_g] = 1.
  - *Difficulty:* Medium. For Heisenberg (scalar monodromy): straightforward. For sl_2 (matrix monodromy): non-trivial.
  - *Depends on:* Nothing. Can be done now.

- **B3.** Compute F_2 for Heisenberg via operadic stratum-sum and verify agreement with shadow tower.
  - *Difficulty:* Low-Medium (Heisenberg is scalar, should simplify).
  - *Depends on:* B2.

- **B4.** Compute F_2 for sl_2 via operadic stratum-sum.
  - *Difficulty:* Medium (matrix monodromy, 7 stable graphs).
  - *Depends on:* B2, B3.

- **B5.** Formulate and prove the general statement: for all g ≥ 0, the operadic curvature matches the shadow tower F_g = κ · λ_g^FP.
  - *Difficulty:* Hard (requires understanding all genera simultaneously).
  - *Depends on:* B3, B4.

---

## [C] CURVED DUNN ADDITIVITY

**Goal:** Prove that curved E_2 decomposes as curved E_1 in curved E_1, with curvature as obstruction.

**Current status:** Conjecture conj:curved-dunn-additivity, refined to 3 levels of precision. No precedent in the literature. The BV tensor product of curved operads has not been defined.

**Sub-items:**

- **C1.** Define the curved E_n operad as a modular completion of the genus-0 E_n operad with clutching controlled by the Hodge class λ_1.
  - *Difficulty:* Medium. Bellier-Milles/Drummond-Cole provide model category structure on curved operads.
  - *Depends on:* Nothing.

- **C2.** Define the Boardman-Vogt tensor product of curved operads.
  - *Difficulty:* Hard. No precedent. Would be a novel contribution to operadic algebra.
  - *Depends on:* C1.

- **C3.** Prove the curved Dunn decomposition: curved E_2^{curv} = E_1^{curv} ∘_BV E_1^{curv}.
  - *Difficulty:* Very hard.
  - *Depends on:* C1, C2.

- **C4.** Verify that the curvature decomposition matches the Arakelov entanglement: κ·ω_g decomposes into contributions from the two E_1 factors entangled by the dbar-defect.
  - *Difficulty:* Medium (once C3 exists).
  - *Depends on:* C3.

---

## [D] CHIRAL COPRODUCT FOR NON-ADE TYPES

**Goal:** Construct the chiral coproduct on V_k(g) for all simple g.

**Current status:** ADE: constructed (JKL via CoHA). Type A: constructed (GRZ via M2-M5). BCFG: open.

**Sub-items:**

- **D1.** Extend JKL vertex coproduct to B_n, C_n, F_4 via Z/2 folding of the corresponding ADE quiver CoHA.
  - *Difficulty:* Medium. Requires checking Z/2-equivariance of the vertex coproduct.
  - *Depends on:* Nothing external. Requires understanding JKL construction.

- **D2.** Extend JKL to G_2 via Z/3 folding of D_4 (triality).
  - *Difficulty:* Hard. Genuine technical obstruction from third roots of unity in spectral parameter.
  - *Depends on:* D1 (for the folding framework).

- **D3.** Alternatively, extend GRZ to BCD via orientifold planes in the M2-M5 system.
  - *Difficulty:* Hard. Requires orientifold M-theory technology.
  - *Depends on:* Nothing (independent approach).

- **D4.** Verify the chiral coproduct agrees with the Drinfeld coproduct on Y_\hbar(g) for all simple g (not just sl_2, sl_3).
  - *Difficulty:* Medium. Strictification theorem covers the algebraic side; the chiral lift needs checking.
  - *Depends on:* D1 or D3.

---

## [E] GLOBAL TRIANGLE BEYOND KOSZUL LOCUS

**Goal:** Close the global triangle boundary → bulk → boundary for non-formal (class M) algebras.

**Current status:** Proved at boundary-linear level. Three algebraic + one geometric obstruction identified (hochschild.tex:2016-2058).

**Sub-items:**

- **E1.** Construct a homotopy-coherent Hochschild/bar-cobar compatibility theorem for chiral algebras with non-formal A_∞ structure.
  - *Difficulty:* Very hard. This is the deepest remaining theoretical problem.
  - *Depends on:* A3 (understanding class M chain-level structure).

- **E2.** Prove factorization descent for the Verdier dual: pointwise centres assemble into a factorization algebra on Ran(C).
  - *Difficulty:* Hard.
  - *Depends on:* E1.

- **E3.** Trivialize defect holonomy: prove the shadow connection's holonomy around defect loops is trivializable for standard families.
  - *Difficulty:* Medium-Hard.
  - *Depends on:* E2.

---

## [F] ADVERSARIAL FIXES (can be done NOW)

- **F1.** D* vs S^1 proof: construct the fiber integration for the E_1 case (currently E_∞ only).
  - *Difficulty:* Medium. The fiber integral of the OPE coefficient system over radial fibers.

- **F2.** Categorical level shift: verify compact generation of Mod_A for specific non-Yangian examples (e.g., Virasoro modules, W_3 modules).
  - *Difficulty:* Low-Medium.

- **F3.** [Δ,{-,-}^ch] lemma: extend from simple g to reductive g (gl_n) and to products of simple factors.
  - *Difficulty:* Low (H^3(gl_n) = C, same argument applies).

- **F4.** Standalone paper: verify all 8 open questions are correctly stated and non-redundant after session edits.
  - *Difficulty:* Low.

- **F5.** Add Cao-Okounkov-Zhou-Zhou (stable envelopes for critical loci) to bibliography and cite in the chiral coproduct discussion.
  - *Difficulty:* Low.

---

## [G] INFRASTRUCTURE (can be done NOW)

- **G1.** Run `make test` on Vol I to verify all 5000+ compute tests pass after session changes.

- **G2.** Git commit all session changes with a descriptive commit message.

- **G3.** Vol I standalone: execute CG rectification Phases 3-5 (chunk-by-chunk 5-gate sweep of 7800 lines).

- **G4.** Build all three volumes with full converging multi-pass builds (not single-pass).

- **G5.** Update the preface Section 0 table to reflect the modular operad Definition (no longer "conjectural" at genus 0).

---

## Priority ordering

0. **A0** (THE MASTER THEOREM: conformal vector → E_3-topological. If the direct algebraic route A0a works, it closes the climax for ALL conformal VAs at once. This is the single highest-value target.)
1. **F1-F5** (immediate, no dependencies, clean up adversarial findings)
2. **G1-G5** (immediate, infrastructure)
3. **A1** (medium difficulty, would close the climax for Virasoro via DS — a backup if A0a fails)
4. **B1-B3** (medium difficulty, would validate the modular operad)
5. **D1** (medium difficulty, extends coproduct to BCD)
6. **A2, B4-B5** (harder extensions)
7. **C1-C2** (novel operadic algebra, independent research contribution)
8. **E1-E3, D2, C3-C4** (the hardest items, likely multi-paper programme)
