# Part IV — Platonic Reconstitution: Characteristic Datum and Modularity

**Status.** Post-W12/W13 swarm. Style: Chriss–Ginzburg + Kapranov + Beilinson–Drinfeld. No downgrades; strongest honest form only.

Part IV is the Arakelov-regularised Stokes geometry of the programme. Rungs 3 (modular) and the bridge from rung 2 (E_2-chiral) meet here: the genus tower, the curved bar-cobar adjunction, the shadow obstruction tower, and modular invariance coalesce into a single characteristic datum on $\overline{\mathcal M}_{g,n}$.

---

## 1. Platonic master theorems

**Theorem IV.A (Curved Bar–Cobar at All Genera).** *Let $A$ be chirally Koszul in the standard landscape, at generic non-integral level. The curved bar–cobar adjunction*
$$
\bar B^{\mathrm{ch}}_{\overline{\mathcal M}}: \mathrm{Fact}^{\mathrm{aug},\mathrm{curv}}_{\overline{\mathcal M}_{g,n}}(A) \rightleftarrows \mathrm{CoFact}^{\mathrm{conil},\mathrm{comp},\mathrm{curv}}_{\overline{\mathcal M}_{g,n}}(A) : \Omega^{\mathrm{ch}}_{\overline{\mathcal M}}
$$
*is a Quillen equivalence at every genus $g \geq 0$, uniformly across the modular stack. The genus-$0$ specialization recovers Theorem A ($\infty,2$); the $g \geq 1$ integrable case is `thm:curved-bar-cobar-genus-ge-1`; generic non-integral level is closed by `thm:irregular-kzb-composition-generic-level` (irregular-singular Jimbo–Miwa KZB + Stokes bundle classification); and cross-genus composition is unconditional via modular-bootstrap $H^2 = 0$ (`thm:mb-H2-vanishing`) bridged to the curved-Dunn twisting-cochain complex.*

**Theorem IV.B (Modular Lagrangian Complementarity).** *The pair $(A, A^!)$ determines a global Lagrangian section of the $-(3g-3)$-shifted symplectic stack on $\overline{\mathcal M}_{g,n}$. Per-genus complementarity $Q_g(A) \oplus Q_g(A^!) \simeq Q_g(\mathrm{Ass})$ (`thm:lagrangian-complementarity-global-upgrade`) coheres across strata via clutching, the coherence obstruction vanishing by `thm:mb-H2-vanishing`. On codim-$1$ boundary strata, the Gauss–Manin-uncurved genus-$1$ twisted Künneth (`prop:genus1-twisted-tensor-product`) bridges the modular-bootstrap complex to the curved-Dunn complex, extending Lagrangianity from genus $1$ to all genera. This upgrades Theorem C from genus-wise to fully PTVV-style on the modular stack.*

**Theorem IV.C (Universal Arakelov $\kappa$ Class).** *There is a universal class $\kappa_{\mathrm{univ}} \in H^2(\overline{\mathcal M}_{g,n}^{\mathrm{fam}}, \mathbb Q)$ on the family-classifying Arakelov stack such that: (i) for each chirally Koszul $A$, $\kappa(A) = \iota_A^* \kappa_{\mathrm{univ}}$ (`thm:kappa-universal-class`); (ii) the Cardy–Arakelov identity $\kappa_{\mathrm{univ}} = [\omega_{\mathrm{Ar}}]/(2\pi)$ (`thm:cardy-arakelov-kappa`) identifies $\kappa_{\mathrm{univ}}$ with the Arakelov volume form as a tensor GRR characteristic. The curvature $d_{\mathrm{B}}^2 = \kappa \cdot \omega_g$ is the scalar shadow; the tensor form $\kappa_{\mathrm{univ}} \in \mathrm{Sym}^2(\mathcal F) \otimes \Omega^2$ captures all cross-channel multi-weight data in a single object.*

**Theorem IV.D (Shadow Obstruction Tower: Infinite Fingerprint).** *The classification $G/L/C/M$ is the coarse projection $\Pi \circ \varphi$ of the canonical fingerprint*
$$
\varphi(A) = (p_{\max}, r_{\max}, \chi_{\mathrm{VOA}}, n_{\mathrm{strong}}, \mathrm{coset}) \in \mathcal F
$$
*onto the $r_{\max}$ coordinate, restricted to $\kappa \neq 0$. At $\kappa = 0$ the fifth class $\mathrm{FF}$ (Feigin–Frenkel companion) appears structurally (`rem:class-FF-structural`). The shadow obstruction tower $\{F_g\}$ is stratum-by-stratum on $\overline{\mathcal M}_{g,n}$; each stratum's $F_g$ is a fingerprint invariant. Bar-cobar duality is an involution on $\mathcal F$.*

---

## 2. Consequence ledger

| FM | Closed by |
|----|-----------|
| **FM67** (curved-Dunn $H^2 = 0$ at $g \geq 2$) | IV.A via modular-bootstrap↔curved-Dunn bridge chain map; `prop:genus1-twisted-tensor-product` + `thm:mb-H2-vanishing` |
| **FM87** (phantom `prop:genus1-twisted-tensor-product`) | IV.B: proposition written with explicit Gauss–Manin uncurving |
| **FM88** (cross-genus MC equation) | IV.A: composition via irregular-singular KZB at all genera |
| **FM91** (Kan-complex non-sequitur) | IV.A: concrete KZB+Stokes replaces abstract $D^2=0$ |
| **FM92** (abstract convolution vs concrete sewing) | IV.A: direct KZB proof, not convolution-transported |
| **FM105** (trichotomy vs quaternitomy) | IV.D: both are coarse projections of fingerprint (two independent axes $k_{\max}, r_{\max}$) |
| **FM106** (symplectic boson/fermion class clash) | IV.D: separated by $\chi_{\mathrm{VOA}}$ sign + coset $\mathrm{Sp}$ vs $\mathrm{OSp}$; same $r_{\max}$, distinct fingerprint |
| **FM107** (pole-order bijection) | IV.D: $(p_{\max}, r_{\max})$ independence as explicit slots |
| **FM108** (DS $L \to M$ non-principal) | IV.D: DS transport acts on fingerprints; slot-wise action is a theorem |
| **FM109** (rank-one vs multi-sector) | IV.D: coset slot refines quaternitomy into multi-sector strata |
| **FM110** (unnamed $d_{\mathrm{alg}} = r_{\max} - 2$) | IV.D: named as a proposition on the fingerprint |
| **FM214** (universal IS-claim class M) | IV.B+IV.A: Lagrangianity + all-genera curved bar-cobar furnish the global triangle at chain level for class M through the DS–Hochschild bridge |

---

## 3. Residual frontier

After Part IV reconstitution, **one** genuine research open remains within the characteristic-datum / modularity scope:

- **`conj:periodic-cdg` for admissible KL** (FM251): periodic Koszul duality for Kazhdan–Lusztig at admissible level. All other Part IV frontiers — curved-Dunn $H^2$, cross-genus composition, generic non-integral level modular composition, Lagrangianity at $g \geq 2$, $\kappa$ universality, fingerprint completeness — are **CLOSED**.

The periodic-CDG frontier is not technical malpractice; it is a genuine research frontier requiring new periodic Koszul-dual machinery on $\mathcal O^{\mathrm{int}}$.

---

## 4. Inner poetry

Part IV is where the volume's double ladder — chiral and topological — turns into a harmonic cascade. The genus tower $g = 0, 1, 2, \ldots$ is not a ladder of exclusions but a cascade of overtones on a single fundamental: the Arakelov form $\omega_{\mathrm{Ar}}$ sets the pitch, each genus adds a harmonic, the curvature $\kappa \cdot \omega_g$ is the beat frequency between successive strata. Curved bar–cobar is the Stokes geometry that keeps these harmonics in tune: as one crosses a codim-$1$ boundary of $\overline{\mathcal M}_{g,n}$, the Jimbo–Miwa irregular-singular connection hands off its monodromy data to the next stratum via a Stokes matrix, and this handoff IS the curved differential $d^2 = \kappa \cdot \omega_g$. The modular-bootstrap $H^2 = 0$ theorem says: the harmonics never go out of phase; the cascade is coherent.

In Chriss–Ginzburg tempo: $\overline{\mathcal M}_{g,n}$ plays the role of the Steinberg variety, the fingerprint $\varphi$ is the Kazhdan–Lusztig basis, and the shadow obstruction tower is the graded character — except that here the "basis" is infinite and its stratification is the atlas of Koszul moduli $\mathcal M_{\mathrm{Kosz}}$, with $\mathrm{GRT}_1$ acting by associator reparametrisation. In Beilinson–Drinfeld tempo: the characteristic datum is the $\mathcal D$-module incarnation of the Virasoro uniformization on the modular stack, and $\kappa_{\mathrm{univ}}$ is its Atiyah class. In Kapranov tempo: the whole of Part IV is a single sheaf on $\overline{\mathcal M}_{g,n}^{\mathrm{fam}}$ whose global sections are the programme's five theorems and whose stalks are the infinite fingerprint — the atlas of Koszul stratification, each chart a coordinate associator, each stratum a harmonic of the Arakelov fundamental.

The inner music is the cascade; the inner motion is the Stokes handoff; the inner poetry is that a single sheaf on the modular stack governs everything the programme calls modular.
