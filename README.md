# A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT

**Volume II** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* (this volume) | Derived centres interpreted physically as 3d HT gauge theories |
| **III** | *Calabi-Yau Quantum Groups* | Concrete CY quantum groups as examples of Vol I's abstract E_1-chiral quantum groups |

## Connection to Volume I

Every chapter depends on Vol I's five theorems:

| Vol I Theorem | What it supplies |
|:---:|----------------|
| **(A)** Bar-cobar adjunction | E_1 bar coalgebra; chiral derived center gives SC^{ch,top} datum |
| **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
| **(C)** Complementarity | Bulk-boundary-line triangle inherits (-1)-shifted symplectic structure |
| **(D)** Modular characteristic | The genus-1 curvature coefficient kappa(A); the higher-genus scalar continuation of d^2 = kappa(A) * omega_g is conditional |
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
| Pages | ~1,749 |
| Preface | 1,998 lines (expanded from 791 in the 2026-04-13 reconstitution) |
| Tagged claims | ~2,650+ |
| Source files | 19 theory + 13 examples + 75 connections = 107 chapter .tex + 2 appendices |
| Compute files | 61 lib + 63 test files |
| Collected tests | 3,571 |
| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP182 + AP158 + FM40-FM68 |
| First-principles cache | 620 lines, cross-programme enforcement verified clean |
| Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
| Cross-volume bridges | 15 (including 3D gravity climax row) |
| Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |

The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody algebras, all W-algebras, and more generally every non-critical conformal vertex algebra whose Li-graded PVA is freely generated, and remains conjectural only for non-freely-generated conformal VAs.

## Build

All compiled output goes to `out/`.

```bash
make fast                    # quick converging build → out/main.pdf
make                         # full build: manuscript + working notes → out/
make release                 # full rebuild → out/ + iCloud
make test                    # compute test suite
make clean-builds            # remove /tmp/mkd-* isolated build directories
```

Each build runs in its own `/tmp/mkd-chiral-bar-cobar-vol2-<NS>/`
directory, so parallel agents never clobber each other. Set
`MKD_BUILD_NS` for warm rebuilds across invocations:

```bash
export MKD_BUILD_NS="agent-$$"
make fast                         # warm on second call
```

Requires TeX Live 2024+ with pdflatex (memoir, EB Garamond, newtxmath).

## Repository Layout

```
chiral-bar-cobar-vol2/
  main.tex                  entry point
  Makefile                  build system
  chapters/
    frame/                  preface
    theory/                 Part I (~19 files)
    examples/               Parts IV-V (~13 files)
    connections/            Parts II-III + V-VII (~75 files)
  appendices/               brace signs, orientations, FM proofs
  compute/                  61 lib + 63 test files
```
