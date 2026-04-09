# CLAUDE.md -- Volume II: A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT

**Canonical reference for all shared content: ~/chiral-bar-cobar/CLAUDE.md. This file contains ONLY Vol II-specific material.**

## Identity

The Swiss-cheese operad SC^{ch,top} is the natural home of the bar complex: differential = holomorphic factorization on C, deconcatenation coproduct = topological factorization on R. The five Vol I theorems are the modular invariants surviving Sigma_n-coinvariance. The bar complex presents SC^{ch,top} as the Steinberg variety presents the Hecke algebra. Physics IS the homotopy type.

~1,500pp, this repo. Seven parts: I(The Open Primitive) II(The E_1 Core) III(Seven Faces of r(z)) IV(Characteristic Datum and Modularity) V(Standard HT Landscape) VI(Three-Dimensional Quantum Gravity = CLIMAX) VII(Frontier).

## Standing Hypotheses

The algebraic framework is unconditional. Former (H1)-(H4) are no longer background axioms: (H1)-(H2) conditions of physics bridge theorem, (H3) theorem of configuration space geometry, (H4) recognition theorem (proved). Homotopy-Koszulity of SC^{ch,top}: PROVED (Kontsevich formality + transfer). All formerly conditional results now unconditional.

## Vol II-Specific Pitfalls

- SC directionality: Open-to-closed is EMPTY. Bulk -> boundary only.
- PVA is (-1)-shifted: lambda-bracket on H*(A,Q) has shifted parity.
- R-matrix provenance: R(z) from bulk-boundary composition, NOT universal R-matrix (agree on eval locus = DK-0).
- Formality failure at d'=1: NOT a defect. Non-vanishing A-inf operations IS curved bar d^2=kappa*omega_1.
- Bulk = derived CENTER of boundary. NOT bulk = boundary. Proved boundary-linear; global triangle conjectural.
- Spectral Drinfeld strictification: PROVED all simple Lie. Frontier: Kac-Moody root mult > 1.
- Self-dual != critical: c*=13 (Koszul) != c_crit=26 (matter-ghost). For W_N: c*=alpha_N/2, c_crit=alpha_N. NEVER conflate.
- Pole-order dichotomy: Double poles -> class L (formal SC). Quartic -> class M (infinite A-inf). DS transports L -> M.

## The E_1/E_inf Locality Hierarchy (V2-AP1 through V2-AP24)

These arose from a catastrophic session (2026-04-02) where E_1/E_inf terminology was corrupted across multiple files. V2-AP numbering avoids collision with Vol I.

### The Three-Tier Picture
(i) Pole-free: R=tau. (ii) VA with poles: R!=tau but DERIVED from local OPE. (iii) Genuinely E_1: R!=tau, independent input. Tiers (i)+(ii) are BOTH E_inf. Tier (iii) is E_1. E_inf = LOCAL = Sigma_n-equivariant. E_1 = NONLOCAL. OPE poles are compatible with E_inf.

### Critical V2-APs
V2-AP1: E_inf INCLUDES ALL vertex algebras. KM, Virasoro, Heisenberg are ALL E_inf. NEVER "VAs are not E_inf."
V2-AP3: Three bars: B^FG (zeroth pole only) != B^Sigma (all poles + coinvariants) != B^ord (all poles + ordering). Maps: B^ord -> B^Sigma (coinvariants), gr(B^Sigma) -> B^FG (filtration).
V2-AP4: Ordered-to-unordered descent is R-matrix twisted: B^Sigma_n = (B^ord_n)^{R-Sigma_n}. Naive quotient only for pole-free.
V2-AP5: NEVER equate E_inf with "no OPE poles." BD "commutative chiral algebra" (no poles) is STRICT SUBCLASS.
V2-AP6: BD do NOT study E_1. E_1-chiral algebra = NEW concept from THIS manuscript.
V2-AP7: Heisenberg R-matrix = exp(k*hbar/z), NOT trivial. Collision residue k/z. Monodromy exp(-2pi*i*k).
V2-AP8: NEVER add restrictive parenthetical glosses. "E_inf (= BD commutative = no poles)" NARROWS the term.
V2-AP11: NEVER conflate E_inf with BD "commutative." BD Chapter 4 "commutative" = pole-free = strict subclass.
V2-AP12: E_1 vs E_inf is about LOCALITY, not poles.
V2-AP13: NEVER trust agent claim "VAs are not E_inf." This exact error caused cascading damage.
V2-AP14: NEVER oscillate between conventions in single session.
V2-AP15: NEVER edit E_1/E_inf language without author confirmation.
V2-AP17: NEVER revert file based on false premise. Surgical removal only.
V2-AP18: Author's explicit statements override agent literature searches.
V2-AP19: NEVER batch-propagate unverified corrections. ONE edit, verify, THEN propagate.
V2-AP20: NEVER add "in the sense of [reference]" without verification.
V2-AP21: PVA != P_inf-chiral. PVA = classical shadow (descend to cohomology). P_inf = homotopy intermediate. Opposite directions.
V2-AP22: Full hierarchy: Comm assoc < PVA < E_inf-chiral < P_inf-chiral < E_1-chiral. Bar/Koszul at E_inf and E_1 levels.
V2-AP23: Chromatic: classical theory is height 0. L_{K(n)}(B(A))=0 for n>=1. Pole order != chromatic height.
V2-AP24: S-transform (closed, complex structure) != Wick rotation of R (open, E_1 ordering). Different algebraic data.

## Cross-Volume Bridges

| Bridge | Vol II claim | Vol I anchor | Status |
|--------|-------------|--------------|--------|
| Bar-cobar | SC^{ch,top} specializes Thm A | Theorem A | Proved |
| DS-bar | Bar-cobar commutes with DS | ds-koszul-intertwine | Proved |
| Hochschild | BV-BRST origin of Thm H | Theorem H | Proved |
| DK/YBE | r(z) via Laplace provides DK-0 | MC3 | Proved |
| PVA-Coisson | PVA descent recovers Coisson | Deformation theory | Proved |
| W-algebras | Feynman-diag m_k matches bar diff | MC5 | Proved g=0; conj g>=1 |
| Affine monodromy | C_line^red = Rep_q(g) on eval modules | Thm A + DK | Proved |
| Soft theorems | Shadow tower controls soft graviton hierarchy | Thm H | Proved g=0 |
| Two-colour | ordered -> A^!_line, symmetric -> A^!_ch | two-color-master | Proved |

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make    # Vol II
cd ~/chiral-bar-cobar && make fast                           # Vol I
cd ~/chiral-bar-cobar && make test                           # Tests
```

## File Map

**Theory** (chapters/theory/): foundations, locality, axioms, equivalence, bv-construction, raviolo, raviolo-restriction, fm-calculus, orientations, fm-proofs, pva-descent-repaired, pva-expanded-repaired, factorization_swiss_cheese, modular_swiss_cheese_operad, introduction.

**Examples** (chapters/examples/): rosetta_stone, examples-computing, examples-worked, examples-complete-proved, examples-complete-conditional, w-algebras-virasoro, w-algebras-w3.

**Core Parts II-VI**: bar-cobar-review, line-operators, ordered_associative_chiral_kd_core, dg_shifted_factorization_bridge, thqg_gravitational_yangian (II); dnp_identification_master, spectral-braiding-core, ht_bulk_boundary_line_core, celestial_boundary_transfer_core, affine_half_space_bv, fm3_planted_forest_synthesis (III); hochschild, brace, relative_feynman_transform, modular_pva_quantization_core, ht_physical_origins (IV); ym_synthesis_core, celestial_holography_core, log_ht_monodromy_core, anomaly_completed_core, thqg_holographic_reconstruction, thqg_modular_bootstrap (V); thqg_gravitational_complexity, 3d_gravity, thqg_3d_gravity_movements_vi_x, thqg_critical_string_dichotomy, thqg_perturbative_finiteness, thqg_soft_graviton_theorems, thqg_symplectic_polarization (VI).

## Git

All commits authored by Raeez Lorgat. NEVER credit an LLM. git stash FORBIDDEN.
