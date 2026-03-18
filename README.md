<div align="center">

<br>

# Modular Homotopy Theory for Factorization Algebras on Curves

### Volume 2: A&infin; Chiral Algebras and 3D Holomorphic&ndash;Topological QFT

<br>

*The bar differential is holomorphic factorization.*
*The coproduct is topological factorization.*
*Together they make a Swiss-cheese algebra on* FM<sub>k</sub>(&Copf;) &times; Conf<sub>k</sub>(&Ropf;).

<br>

![Pages](https://img.shields.io/badge/pages-501+-a371f7?style=for-the-badge&labelColor=0d1117)
![Claims](https://img.shields.io/badge/tagged%20claims-500+-3fb950?style=for-the-badge&labelColor=0d1117)
![Build](https://img.shields.io/badge/build-passing-3fb950?style=for-the-badge&labelColor=0d1117)

<br>

</div>

---

<br>

## Overview

This volume applies the algebraic engine of Volume&nbsp;I to three-dimensional holomorphic&ndash;topological quantum field theory. The bar complex of a chiral algebra carries a differential from &Copf;-direction factorization and a coproduct from &Ropf;-direction factorization; together they make the bar complex an algebra over the holomorphic&ndash;topological Swiss-cheese operad SC<sup>ch,top</sup> on &Copf;&ensp;&times;&ensp;&Ropf;. The A<sub>&infin;</sub> chiral algebra structure is the twisting morphism &alpha;&ensp;&isin;&ensp;MC(Hom(B&#x0304;<sup>ch</sup>(A),&ensp;End<sub>A</sub>)), and the Maurer&ndash;Cartan equation &part;&alpha;&ensp;+&ensp;&alpha;&ensp;&star;&ensp;&alpha;&ensp;=&ensp;0 is the spectral Stasheff identity.

The stable-graph modular bar coalgebra in log-FM coordinates carries the five-component differential D<sup>log</sup><sub>mod</sub>&ensp;=&ensp;d<sub>&#x010C;</sub>&ensp;+&ensp;d<sub>Ch<sub>&infin;</sub></sub>&ensp;+&ensp;d<sub>coll</sub>&ensp;+&ensp;d<sub>sew</sub>&ensp;+&ensp;d<sub>loop</sub>, with boundary operators as residue correspondences on log-FM strata. The one-edge principle governs the theory: **trees govern chirality; loops govern modularity**. A deformation theory that only remembers trees cannot see modular obstructions.

<br>

## Six Main Theorems

| &ensp; | Theorem | Statement |
|:---:|---------|-----------|
| **F** | **Homotopy-Koszulity** | SC<sup>ch,top</sup> is homotopy-Koszul; bar-cobar on SC<sup>ch,top</sup>-algebras is a Quillen equivalence. |
| **G** | **PVA Descent** | On H<sup>&bullet;</sup>(A,Q): regular part of m<sub>2</sub> is commutative product, singular part is &lambda;-bracket; the pair is a (&minus;1)-shifted Poisson vertex algebra. Jacobi from Arnold on FM<sub>3</sub>(&Copf;); Leibniz from three-face Stokes. |
| **J** | **Bulk-Boundary-Line** | A<sub>bulk</sub>&ensp;&simeq;&ensp;Z<sub>der</sub>(B<sub>&part;</sub>)&ensp;&simeq;&ensp;ChirHoch<sup>&bullet;</sup>(A<sup>!</sup>); line operators&ensp;=&ensp;A<sup>!</sup>-mod; spectral R-matrix satisfies YBE. |
| **K** | **Curved Swiss-Cheese** | At genus g&ensp;&geq;&ensp;1: curved bar complex with d<sub>fib</sub><sup>2</sup>&ensp;=&ensp;&kappa;(A)&ensp;&middot;&ensp;&omega;<sub>g</sub> is a curved SC<sup>ch,top</sup>-algebra. |
| **L** | **Deformation Brace** | Chiral Hochschild cochains carry a brace algebra governing deformations of the SC<sup>ch,top</sup>-algebra. |
| **M** | **Modular PVA Quantization** | Stable-graph modular bar coalgebra + genus-raising operator = universal obstruction recursion for PVA-to-VA quantization. |

<br>

## Connection to Volume I

| Volume I concept | Volume II incarnation |
|-----------------|----------------------|
| Bar differential d<sub>B</sub> | &Copf;-direction factorization |
| Bar coproduct &Delta; | &Ropf;-direction factorization |
| Modular convolution L<sub>&infin;</sub> | Colored modular deformation object (bulk + boundary + line) |
| &Theta;<sub>A</sub> graph-sum | Modular effective action S<sup>mod</sup><sub>HT</sub> |
| Shadow Postnikov tower | PVA coordinate spectral sequence |
| Koszul dual A<sup>!</sup> | dg-shifted Yangian (line operator category) |
| Complementarity | Bulk-boundary-line triangle |
| Genus-two shells | Loop&compfn;loop + sep&compfn;loop + planted-forest channels |

<br>

## Architecture

```
Volume II
├── Part I    Swiss-Cheese Algebra                 Bar complex → SC^{ch,top}-algebra
├── Part II   Descent Calculus                     PVA descent (D2-D6), axioms ⟹ operad
├── Part III  Dualities and Bulk-Boundary-Line     Theorem J, dg-shifted Yangians, R-matrices
├── Part IV   Standard Landscape                   Heisenberg, LG, Chern-Simons, W₃
└── Part V    Quantization and Holography          Modular PVA quantization, holographic targets
```

<br>

## Building

```bash
cd ~/chiral-bar-cobar-vol2 && make          # Build Vol II PDF
```

> **Requirements**: TeX Live 2024+ with `pdflatex`. Same package requirements as Volume I.

<br>

## Key Results

- **SC<sup>ch,top</sup> is homotopy-Koszul**: Kontsevich formality + transfer from classical Swiss-cheese (Koszul by Livernet, Voronov, GK94)
- **PVA descent D2&ndash;D6 all proved**: Exchange cylinder + three-face Stokes on FM<sub>3</sub>(&Copf;)
- **Recognition theorem proved**: Weiss cosheaf descent (lem:product-weiss-descent)
- **Zero conjectural algebraic inputs**: Only the standing physical axioms (H1)&ndash;(H4)
- **W<sub>3</sub> quartic quasi-primary**: &Lambda;&ensp;=&ensp;:TT:&ensp;&minus;&ensp;(3/10)&part;<sup>2</sup>T with coefficient 16/(22+5c)
- **Genus-two shell decomposition**: First level where all three geometry types interact

<br>

---

<div align="center">

<sub>501+ pages &ensp;&middot;&ensp; 41+ active files &ensp;&middot;&ensp; 500+ tagged claims &ensp;&middot;&ensp; 100% claim-tag coverage</sub>

</div>
