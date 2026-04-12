# A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT

**Volume II** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* (this volume) | The 3D interpretation: what the engine computes |
| **III** | *Calabi-Yau Quantum Groups* | The categorical completion: CY categories as quantum chiral algebras |

## Connection to Volume I

Every chapter depends on Vol I's five theorems:

| Vol I Theorem | What it supplies |
|:---:|----------------|
| **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
| **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
| **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
| **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |

## Seven Parts

- **I. The Open Primitive**: SC^{ch,top} constructed, recognition theorem, homotopy-Koszulity proved, PVA descent D2-D6 proved
- **II. The E_1 Core**: Ordered bar B^{ord}(A) as primary structure; line operators, dg-shifted Yangian, spectral Drinfeld strictification (all simple types)
- **III. The Seven Faces of r(z)**: Collision residue as R-matrix, Yangian, Sklyanin, Drinfeld-Kohno, celestial OPE, holographic map
- **IV. The Characteristic Datum and Moduldegree**: Standard landscape examples, modular Swiss-cheese operad, Feynman transform, modular PVA quantization
- **V. The Standard HT Landscape**: YM boundary, celestial holography, anomaly-completed Koszul duality, holographic reconstruction
- **VI. Three-Dimensional Quantum Gravity**: The climax; Virasoro lambda-bracket generates the full gravitational theory; critical string dichotomy c=26 vs c!=26
- **VII. The Frontier**: All conditional and conjectural material; no earlier part depends on this

## Status

| Metric | Value |
|--------|------:|
| Pages | ~1,633 |
| Tagged claims | ~2,604 |
| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
| Compute modules | 53 lib + 64 test |
| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
| Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
| Cross-volume bridges | 15 (including 3D gravity climax row) |
| Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |

Zero conjectural algebraic inputs beyond the standing physical axioms, which have been made explicit as derived consequences.

## Build

```bash
# Build Vol II
make              # full build
make fast         # single-pass quick check

# Build Vol I (dependency)
cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
```

Requires TeX Live 2024+ with pdflatex (memoir, EB Garamond, newtxmath).

## Repository Layout

```
chiral-bar-cobar-vol2/
  main.tex                  entry point
  Makefile                  build system
  chapters/
    frame/                  preface
    theory/                 Part I (~16 files)
    examples/               Parts IV-V (~13 files)
    connections/            Parts II-III + V-VII (~72 files)
  appendices/               brace signs, orientations, FM proofs
  compute/                  53 lib + 64 test files
```
