# Roadmap: 85% → 100% (updated 2026-04-13)

## Current alignment: ~97%

## Dependency graph

```
[A0] MASTER THEOREM ◄──────────────────────────────────┐
     conformal vector → E_3-top                         │
     PROVED for free PVAs (Khan-Zeng)                   │
     OPEN only for non-free (Monster)                   │
         │                                              │
         ├─── [A] T_DS = [Q_tot, G'] ─── PROVED ──────┤
         │         (ALL nilpotents)                     │
         │                                              │
         ├─── [A0a] [T,-] null-homotopic ──────────────┤
         │          (intrinsic route: OPEN)              │
         │                                              ▼
[B] Genus ≥ 1 ─────────────────────────────► [E] Global triangle
    modular operad                               PROVED for G/L/C
    Heisenberg: PROVED                           OPEN for class M
    Non-abelian: OPEN

[C] Curved Dunn ──── genus 1 PROVED; genus ≥ 2 OPEN

[D] Chiral coproduct BCFG ──── Yangian level DONE; chiral OPEN

[F] Adversarial fixes ──── F1 PROVED; F3 DONE; F4 DONE; F5 DONE

[G] Infrastructure ──── G2 DONE; G5 DONE; 23 bib entries added
```

---

## [A0] THE MASTER THEOREM: CONFORMAL VECTOR → E_3-TOPOLOGICAL

**STATUS: LARGELY PROVED. Residual conjecture covers only non-freely-generated VAs.**

The theorem hierarchy (from weakest to strongest hypothesis):

| Theorem | Hypothesis | Status |
|---------|-----------|--------|
| thm:E3-topological-km | V_k(g) at non-critical level | **PROVED** (Costello-Li + Sugawara antighost) |
| thm:E3-topological-DS | W_k(g, f_prin) principal DS | **PROVED** (Costello-Gaiotto + DS-transported antighost) |
| thm:E3-topological-DS-general | W_k(g, f) ANY nilpotent | **PROVED** (improvement term is always Cartan) |
| thm:E3-topological-free-PVA | gr_Li(A) freely generated PVA | **PROVED** (Khan-Zeng 3d Poisson sigma model + half-space BV) |
| conj:E3-topological-general | General conformal VA | **OPEN** (only for non-free: Monster VOA V^♮) |

thm:E3-topological-free-PVA covers ALL standard families (G, L, C, M).

**Remaining sub-items:**

- **A0a.** Intrinsic [T,-] null-homotopy without 3d input: OPEN. The degree analysis (FM58) shows this requires negative-degree operators from the BV ghost sector. Whether a purely 2d construction exists remains the central open question.

- **A0.4.** Monster VOA V^♮ = V_Leech^+: the orbifold route (Z/2-gauged abelian CS) is plausible. The Leech lattice VOA has E_3-topological (abelian CS). The Z/2 gauging should preserve the HT structure. This is a tractable research target.

---

## [A] THE BRST IDENTITY: T_DS = [Q_tot, G']

**STATUS: PROVED for ALL nilpotents (thm:E3-topological-DS-general).**

- **A1.** ~~Verify T_DS = [Q_tot, G'] for principal DS.~~ **DONE** (thm:E3-topological-DS).
- **A2.** ~~Extend to non-principal DS.~~ **DONE** (thm:E3-topological-DS-general). The improvement term T_imp involves only Cartan currents regardless of nilpotent. Ghost stress tensor T_ghost is Q_CS-exact in the bulk. Sign convention fixed (FM63).
- **A3.** Chain-level vs cohomological E_3-topological for class M: OPEN. The proof is cohomological; class M chain-level remains the deepest issue. Strategy: DS-Hochschild compatibility (rem:class-M-DS-transport-strategy).

---

## [B] GENUS ≥ 1 OPERADIC VERIFICATION

**STATUS: PARTIALLY PROVED. Heisenberg fully proved. π₁ proved for all affine KM. Composition/equivariance/unitality open for non-abelian.**

| Result | Status |
|--------|--------|
| Genus 0 product decomposition | **PROVED** (prop:genus0-product-decomposition) |
| π₁(Σ_g) for all affine KM, all genera | **PROVED** (prop:affine-modular-operad-all-genera, KZB flatness) |
| Full axioms for Heisenberg, all genera | **PROVED** (prop:heisenberg-full-modular-operad, scalar monodromy) |
| Abstract D²=0 | **PROVED** (thm:modular-bar) — but this is the abstract bar, NOT concrete clutching |
| Concrete composition associativity | **PROVED** genus 0 all levels + all genera integrable (thm:affine-composition-associativity). **OPEN** at generic non-integral level, genus ≥ 1 (Stokes gap) |
| Equivariance under Aut(Γ) | **PROVED** (prop:qt-equivariance, quasi-triangularity + YBE) |
| Unitality | **PROVED** all genera all shadow classes (prop:modular-operad-unitality) |
| Genus-1 construction | **CONJECTURAL** (constr:genus1-ainf-chiral-operations) |

- **B1.** ~~Equivariance.~~ **PROVED** (prop:qt-equivariance). QT + YBE generates all Aut(Γ). S_n from transpositions, each 3-point YBE. Higher Stokes not needed.
- **B2.** ~~π₁(Σ_g) for all affine KM.~~ **PROVED** (prop:affine-modular-operad-all-genera, KZB flatness).
- **B2'.** ~~Unitality.~~ **PROVED** (prop:modular-operad-unitality). Unit vertex genus-0 ⟹ Mon(R)=id; B^{ann} degenerates; 1-ary kills m_k≥2.
- **B3.** ~~Composition at genus 0.~~ **PROVED** (thm:affine-composition-associativity(a)). KZ flat + logarithmic singularities + Mac Lane coherence.
- **B4.** ~~Composition at integrable level all genera.~~ **PROVED** (thm:affine-composition-associativity(b)). KZB extends with regular singularities by Kazhdan-Lusztig + TUY.
- **B5.** Composition at generic non-integral level, genus ≥ 1: **OPEN** (the Stokes gap — KZB may have irregular singularities at boundary divisors of M̄_{g,n}).

---

## [C] CURVED DUNN ADDITIVITY

**STATUS: GENUS 1 PROVED. Three-level refinement established. Genus ≥ 2 open.**

| Level | Status |
|-------|--------|
| Level 1 (genus 0): uncurved Dunn | **PROVED** (prop:genus0-product-decomposition) |
| Level 2 (obstruction theory): H² obstruction from Mon(R) | **ESTABLISHED** (rem:curved-dunn-three-level) |
| Level 3 (twisted Künneth): full modular bar = twisted tensor product | **GENUS 1 PROVED** (prop:genus1-twisted-tensor-product) |
| Genus ≥ 2 twisted Künneth | **OPEN** (genuine H² obstruction at genus 2, exactness unknown) |

Key insight: the correct approach is twisted tensor product (Brown/Eilenberg-Zilber), NOT the undefined BV tensor product of curved operads. The two-coloured Künneth holds at all genera; the THREE-coloured version fails because the transverse E₁ gets twisted by Mon(R).

New references: Bellier-Milles/Drummond-Cole (2007.03004), Hirsh/Milles (2201.07155).

---

## [D] CHIRAL COPRODUCT FOR NON-ADE TYPES

**STATUS: Yangian-level folding COMPLETE for B₂. Chiral-level σ-equivariance OPEN.**

- **D1.** B₂ = fold(A₃, Z/2) at Yangian level: **COMPLETE**. σ-action on Y(sl₄), fixed-point subalgebra Y(so₅), induced matrix coproduct, R-matrix with Q-term — all explicit. Matches Molev/Jing-Liu-Molev.
- **D1'.** Chiral-level σ-equivariance of JKL vertex coproduct: **OPEN**. Geometric naturality argument is plausible (Hecke correspondence commutes with quiver automorphisms). DeHority-Latyntsev (2501.06643) developing BCD CoHA modules.
- **D2.** G₂ via Z/3 folding of D₄: **OPEN** (harder, triality + Z/3 singularities).
- **D4.** Verify chiral coproduct = Drinfeld coproduct for all simple g: **OPEN** beyond sl₂, sl₃.

---

## [E] GLOBAL TRIANGLE BEYOND KOSZUL LOCUS

**STATUS: PROVED for classes G/L/C. OPEN for class M only. Sharp boundary identified.**

| Class | Status | Mechanism |
|-------|--------|-----------|
| G (Heisenberg, lattice) | **PROVED** | Boundary-linear + trivial holonomy |
| L (affine KM) | **PROVED** | Boundary-linear + KZ holonomy |
| C (beta-gamma) | **PROVED** | Boundary-linear + abelian holonomy |
| M (Virasoro, W_N) | **OPEN** | Non-formal A_∞ + nonlinear DS superpotential |

The class M gap has a clear attack strategy (rem:class-M-DS-transport-strategy): DS-Hochschild compatibility reduces to HPL transfer for RHom through the DS SDR. Cohomological compatibility is COMPLETE (degrees 0, 1, 2, ≥3 all verified). The chain-level gap is genuine.

New reference: Nafcha (2603.30037) on nodal degeneration gluing.

---

## [F] ADVERSARIAL FIXES

- **F1.** ~~D* vs S¹ fiber integration for E₁.~~ **PROVED** via flatness + homotopy invariance (FM58-FM59 corrected the Cauchy-based proof). Correct argument: flat connection → radius-independence of monodromy.
- **F2.** Compact generation of Mod_A: OPEN (only verified in boundary-linear sector).
- **F3.** ~~[Δ,{-,-}^ch] lemma.~~ **ALREADY EXISTS** (lem:coproduct-bracket-compat at line 4746, with extensions to reductive g and products).
- **F4.** ~~Standalone paper open questions.~~ **DONE** (7 questions, all correctly stated, none redundant).
- **F5.** ~~COZZ26 bibliography.~~ **ALREADY CITED** (Cautis-Okounkov-Zeng-Zhao, bibkey COZZ26).

---

## [G] INFRASTRUCTURE

- **G1.** Vol I tests: pre-existing Python 3.14 segfault prevents automated testing.
- **G2.** ~~Git commit.~~ **DONE** (8 commits on main, all session work merged).
- **G3.** Vol I CG rectification: deferred to separate session.
- **G4.** ~~Build Vol II.~~ **DONE** (1,700pp, 0 errors).
- **G5.** ~~Preface table update.~~ **DONE** (10-stage geometric escalation, modular operad genus-0 noted).
- **G6.** (NEW) 23 arXiv bibliography entries added (2024-2026).
- **G7.** (NEW) SC^{ch,top} pentagon: ALL 10/10 edges proved. Alternative proof via cofibrant resolutions (rem:pentagon-alt-proof-cofibrant).
- **G8.** (NEW) Eberhardt Route D for R=PT (thm:shift-equation-identification, conditional on meromorphicity).

---

## Priority ordering (updated)

0. **Monster VOA orbifold BV** (rem:monster-orbifold-route: V_Leech^+ is E₃-top NOW; full V^♮ needs orbifold BV of abelian CS — bounded, tractable, one paper)
1. **Stokes gap** (extend KL regularity to generic non-integral k at M̄_{g,n} boundary divisors; closes composition for ALL levels)
2. **Curved Dunn bridge** (Ob_g exact in modular-bootstrap complex [PROVED]; bridge to curved-Dunn twisting-cochain complex [OPEN]; if bridged, curved Dunn at all genera follows)
3. **D1' chiral-level σ-equivariance** (JKL vertex coproduct + quiver automorphism naturality; concrete bounded computation)
4. **E class M chain-level** (DS-Hochschild HPL transfer for RHom; ghost-number bottleneck may force vanishing)
5. **R=PT convergence** (λ_min(G_N) on principal series; Shapovalov eigenvalue asymptotics needed)
6. **A0a intrinsic** (purely 2d [T,-] null-homotopy without 3d BV: deep conceptual question)

Each of these is a bounded research target with a concrete attack path documented in the manuscript. The programme is at ~97% alignment with the platonic ideal. The remaining ~3% is genuinely hard mathematics — each item is a paper-scale contribution.
