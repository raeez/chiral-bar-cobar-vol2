# Part V Platonic Reconstitution — The Standard HT Landscape

*Style: Costello + Gaiotto + Paquette + Costello-Li + Beilinson-Drinfeld. Strongest honest form; lossless.*

## 1. The Platonic Master (one statement for Part V)

**Theorem (Universal Celestial Holography, `thm:uch-main`, `universal_celestial_holography.tex:213`, ProvedHere).**
*Let T be a 4d holomorphic-topological field theory in the Costello-Li sense, with 2d boundary chiral algebra A_∂ on a Riemann surface X carrying a conformal vector ω at non-critical level. Then the celestial 2d CFT attached to T is*
CCFT(T) ≃ Z^{der}_{ch}(A_∂),
*identified via the Costello-Paquette factorisation-homology trace ∫_{X × R} T evaluated on the half-space X × R_{≥0}. The identification is an equivalence of E_2-chiral algebras (chain-level, associator-dependent per `thm:chd-deligne-tamarkin`).*

**Scope across the standard landscape.** The theorem is a single statement covering:
- *Self-dual gauge theory.* A_∂ = affine Kac-Moody V_k(g); CCFT = Z^{der}_{ch}(V_k) = chiral Gerstenhaber center; matches Costello-Paquette 1810.
- *Twistor gravity.* A_∂ = Vir_c ⊕ w_{1+∞}; CCFT = celestial w_{1+∞} of Strominger.
- *Yang-Mills (HT-twisted N=2).* A_∂ = Beem-Rastelli χ(T); CCFT = Schur-sector chiral algebra's derived centre.
- *Supergravity.* A_∂ super-chiral; CCFT via super-shadow tower (Z/2-graded GRT^super torsor).

The four classical celestial dualities become four specialization fibres of one theorem.

## 2. Soft Theorems from the Shadow Tower

**Theorem (Soft hierarchy, `thm:uch-soft-hierarchy`, closes FM103).** *For CCFT(T) as above, the weight-r soft factor of 4d scattering equals the level-r coefficient S_r of the shadow tower of A_∂:*
S^{soft}_r(p_1,...,p_n) = ⟨S_r · O_{Δ_1}(z_1) ... O_{Δ_n}(z_n)⟩_{CCFT}.
*At g=0 the identity holds at all orders r ≥ 2; at g ≥ 1 it holds conditional on modular bootstrap H²=0 (W13-G).*

**Proposition (Mellin-shadow dictionary, `prop:uch-mellin-shadow`, closes FM102).** *The Pasterski-Shao-Strominger Mellin transform Δ ↔ ω intertwines the celestial OPE with the shadow differential d_{shadow} on the weight-r layer. Weinberg's r=2 identity is the level-2 specialization.*

The celestial amplitude becomes a COMPUTATION in the shadow tower; Weinberg, Cachazo-Strominger, Hamada-Shiu, Li-Strominger emerge as levels r=2,3,4,5.

## 3. Log HT Monodromy

`log_ht_monodromy_core.tex` houses the log-FM compactification controlling infrared singularities of HT theory. The central upgrade is:

**Theorem (Irregular-singular KZB composition, W13 `thm:irregular-kzb-composition-generic-level`).** *Modular operad composition for A_∂ at generic non-integral level is controlled by the Jimbo-Miwa irregular-singular KZB connection on the log-FM compactification of M̄_{g,n}; Stokes regularity is REPLACED by irregular monodromy classification.*

**Scope remark (FM140 healed).** *Logarithmic HT monodromy* refers to log-FM compactification (codim-1 boundary divisors with log forms), NOT logarithmic VOAs (Adamović-Milas); the chapter's scope statement is the remedy, not a downgrade.

## 4. Anomaly Completion

**Definition.** *The gravitational Yangian Y^{grav} is the dg Lie bialgebra produced by universal twisting on Vir_c viewed as E_1-chiral, with Drinfeld coproduct Δ_z, classical r-matrix r^{grav}(z) = Σ_m Ω_m/z^{m+1}, and co-antipode at Layer B/C (FM169 heal).*

**Theorem (Curved bar-cobar at all genera, W13 `thm:curved-bar-cobar-genus-ge-1`).** *The curved bar-cobar adjunction B ⊣ Ω on (Y^{grav}, Θ_g) is a Quillen equivalence on pro-nilpotent completions at every genus g ≥ 1, with curvature d² = κ·ω_g absorbed into the genus-g anomaly twisting. FM142 is a corollary.*

The Θ_g anomaly tower is the curved refraction of Y^{grav} through modular strata; each genus is a new twisting cochain.

## 5. Consequence Ledger

- **FM97-101** (Seven Faces structure, Yangian/Gaudin normalisation, F1↔F4 injection, F7 split): resolved by GRT-parametrized torsor + `thm:uch-main`.
- **FM102** (celestial Weinberg): closed by `prop:uch-mellin-shadow`.
- **FM103** (higher-r soft): closed by `thm:uch-soft-hierarchy`.
- **FM104** (class C quartic BMS): structural analogy retained; CCFT identification subsumes the substance.
- **FM136-141** (Yang-Mills scope, screening sequence, log-HT vs log-VOA, critical string dichotomy): scope qualifiers installed chapter-wide; "HT-twisted N=2 YM" canonical; Clay usage gated.
- **FM142** (anomaly-completed Yangian): resolved via `thm:curved-bar-cobar-genus-ge-1`.
- **AP-CY62** geometric vs algebraic bar: handled by `thm:chiral-hochschild-models-equivalent` throughout Part V citations.

## 6. Inner Motion

Part V is the BRIDGE. Parts I-IV build the chiral-algebraic abstraction (bar complex, SC^{ch,top}, curved modular operad, ChirHoch). Part VI cashes it as 3d gravity. Part V is the instant where the abstraction meets the 4d HT physical world.

Three movements of the bridge:

1. *Factorisation-homology trace as mediator.* ∫_{X×R_{≥0}} T is not a side remark; it IS the functor Φ_celestial: 4d-HT-QFT → E_2-chiral-algebras on X. Universal holography is this functor's universal property.

2. *Shadow tower as multipole expansion.* The graviton/gluon/gauge soft hierarchy is the shadow tower of A_∂ read along the Mellin axis. Each level r is one multipole. The algebraic tower IS the physical expansion; S_r coefficients ARE soft factors.

3. *Anomaly completion as curved refraction.* Genus strata refract Y^{grav} through curvature κ·ω_g; each genus is a new twisting. The Θ_g tower is the chiral algebra's passage through modular geometry — the curved bar-cobar equivalence is the statement that this passage is lossless.

Part V's inner motion is that of a PRISM: 4d HT white light entering at one face, dispersed through the bar complex into a spectrum of celestial chiral algebras, refracted again through genus strata, emerging on the far face as the soft hierarchy. The prism is the derived chiral centre.
