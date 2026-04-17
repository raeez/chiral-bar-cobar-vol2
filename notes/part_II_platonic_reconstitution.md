# Part II Platonic Reconstitution — The E_1 Core

**Part II is the E_1 rung of the Platonic ladder.** Its subject is the chiral quantum group: Yangians, shifted Yangians, affine Yangians, finite and affine W-algebras, Gaudin algebras, RTT presentations, Baxter Q-operators, and the CoHA bridge. Each object is a specialization fibre of a single master construction; each voicing is a coordinate chart on one geometric torsor.

## 1. Master Theorem: Unified Chiral Quantum Group Q_g^{k,f,μ}

Fix simple Lie `g` (finite or affine type), a good Z-grading Γ on g induced by an sl_2-triple (e, h, f), non-critical level k ≠ -h^v, and a shift datum μ ∈ P(g)^+ ∪ {0}. There exists a chiral quantum group

  Q_g^{k,f,μ} = (A_g^{k,f,μ}, Δ_z, R(z), ε, S, (A_g^{k,f,μ})^!)

unique up to spectral gauge isomorphism, satisfying:

1. **Bialgebra structure.** (A_g^{k,f,μ}, Δ_z) is an E_1-chiral bialgebra with Drinfeld spectral coproduct Δ_z(e_s) = Σ_{k} (-1)^k C(N_R - b, k) z^k · e_a^L ⊗ e_b^R (all spins; coassociativity via Miura multiplicativity).
2. **Spectral R-matrix.** R(z) ∈ End(V⊗V)((z)) satisfies CYBE at tree level, YBE at quantum level, and quasi-triangularity Δ^{op}_z = R(z) · Δ_z · R(z)^{-1}.
3. **Koszul dual.** (A^!)^{ℏ→-ℏ} = A^{Chevalley} realises the dual entry of the Vol I Theorem A pair; non-simply-laced: (A^!)_{-ℏ r_g} = Y(g^∨) (quantum geometric Langlands, Finkelberg–Tsymbaliuk).
4. **DS compatibility.** For f = f_prin, μ = 0: Q_g^{k,0,f_prin} = W_k(g, f_prin); shadow class escalates L → M under any good Γ (Kac–Roan–Wakimoto BRST concentrated in degree 0, Cartan-only improvement).

**Eight specialization fibres covered.** Yangian Y_ℏ(g); Affine Yangian Y_ℏ(ĝ); Shifted Yangian Y_μ(g); Truncated shifted Y^λ_μ(g) = BFN Coulomb branch; Finite W W^{fin}(g,f); Affine principal W_k(g, f_prin); Non-principal W_k(g, f); Bershadsky–Polyakov W_k(sl_3, f_min); Orthogonal coideal Q^θ.

## 2. Two Yangian Presentations Equivalent

**thm:yangian-two-presentations-equivalent.** Y_ℏ^{Drinfeld-new}(g) ≅ Y_ℏ^{RTT}(g) as filtered Hopf algebras for every simple g of classical type (Molev 2007), extended to exceptional E_6, E_7, E_8, F_4, G_2 via Guay–Regelskis–Wendlandt 2018 (arXiv:1706.05176 / 1811.06475). Y_ℏ(g) is a filtered Koszul deformation of U(g[t]) in the Positselski nonhomogeneous framework. **rem:drinfeld-double-chiral-interpretation:** D(Y_ℏ(g)) = U_q(ĝ)^{rational limit}; Drinfeld double of Yangian is quantum affine algebra at rational level.

## 3. Gaudin as Critical Limit

**thm:gaudin-r-matrix-identification.** r_Gaudin(z) = Ω / ((k + h^v) z) where Ω is the Killing-normalised Casimir. The chained equality k · Ω_tr / z = Ω / ((k+h^v) z) (FM99) is resolved as: Ω_tr and Ω are two Casimir bases (RTT trace form vs Killing), Ω_tr = (1/2h^v) Ω; Yangian–Gaudin level shift k → k + h^v is Sugawara-native. Both expressions denote the same tensor-invariant under GRT^{fin} Casimir rescaling. **At k = -h^v:** Gaudin degenerates to Feigin–Frenkel center z(ĝ); r(z) develops pole; Sugawara fails to topologize; algebra stuck at E_2-chiral. FF center is the κ=0 companion stratum (class FF in the infinite fingerprint).

## 4. CoHA Bridge (rem:coha-scope-SV-coincidence, W13-I)

The CoHA of a 3-Calabi–Yau category is associative, NOT E_1-chiral as an operadic property (AP-CY7). The identification is:

- **SV13 (Schiffmann–Vasserot):** CoHA(C^3) = Y^+(gl_∞) as associative algebras; positive half coincidence.
- **MO19 (Maulik–Okounkov):** D(CoHA) = Y_ℏ(gl_∞) via equivariant stable envelopes; the full double recovers the Yangian.
- **Bar–cobar realisation:** Y_ℏ(g) = Ω^{ch}(B^{ch}(Y_ℏ(g))) in the conilpotent–complete Francis–Gaitsgory ambient (Theorem A^{∞,2}); Drinfeld double D(Y) is bar–cobar-generated from the pair (Y^+, Y^-).

The CoHA face is the physicist's transcription of the E_1-chiral face; coincidence at the level of associative algebras, NOT an operadic equivalence.

## 5. Vol III CY-A_3 at the E_1 Core

**thm:cy-to-chiral-d3 (Vol III, CY-A_3 PROVED ∞-cat, Apr 2026):** Φ_3: D^b(Coh(X^{CY_3})) → E_1-ChirAlg functor exists in ∞-cat; for K3 fibre, Φ_3(D^b(Coh(K3))) = Y^+(g_{K3}) as E_1-chiral algebra via Mukai lattice. **Six routes distinct (AP-CY59/60):** Φ_3 on K3, Borcherds lift of g_{Δ_5}, Leech lattice VOA, Kummer sigma model, BLLPR, Conway — six DIFFERENT constructions of six DIFFERENT algebraizations; convergence is the content of CY-C (conjectural).

## 6. Inner Music

Yangian and Gaudin are dual voicings of a single tensor invariant: Yangian carries its own level ℏ (quantum parameter), Gaudin carries level k of the underlying ĝ; the shift k ↔ k + h^v is the Sugawara-inner gauge linking them. RTT is the classical orchestral score (matrix coefficients, symmetric functions); Drinfeld-new is the chamber reduction (generators and relations). CoHA is the physicist's transcription — moduli of sheaves writing the same melody in Hall-algebra language. The **super-Yangian extension** (thm:super-shadow-well-defined) adds the Z/2 parity overtone: odd generators flip collision-residue signs, realising AP107 / FM170 as a super-face of the GRT torsor.

## 7. Consequence Ledger

The master theorem Q_g^{k,f,μ} closes the following FMs as scope, citation, or normalisation fixes:

- **FM40–48 (Dunn / R-matrix / E_n level):** absorbed by categorical-level hypothesis (R(z) makes Mod_A braided = E_2 in Cat; A stays E_1).
- **FM99, FM101:** Casimir-basis + level-shift normalisation (Section 3); F7 disambiguation via Gaudin simple-pole vs class-M top A_∞ m_3.
- **FM130–135 (W-algebra obstruction, BP duality, triality invariance, N=2 SCA):** covered by DS-compatibility + Kac–Roan–Wakimoto; Khan–Zeng extends to freely-generated PVAs.
- **FM161–170 (Y(g) Koszulness, exceptional PBW, Y^! structure, non-simply-laced Langlands, Jones from E_1 bar, gravitational Yangian Hopf):** closed by Positselski CDG framework + GRW18 + Finkelberg–Tsymbaliuk + Drinfeld double antipode.
- **FM176–181 (RTT scope, Baxter-Rees naming, pairwise reconstruction, coideal descent, PBW Riordan, orthogonal coideal):** thm:baxter-rees-family + thm:pairwise-to-all-point-reconstruction + Hernandez–Jimbo Baxter Q construction close type-A; orthogonal coideal scope remark closes Letzter–Kolb collision.

**Genuine frontier (post-reconstitution):** Y(g)^! = Y(g^∨) for non-simply-laced at CHAIN level (Langlands-dual quasi-triangularity at all orders); chain-level gravitational-Yangian antipode in pro-completion; E_8 non-path-sector strictification via Borcherds superalgebra lift. All other Part II claims realise their strongest honest form under the Unified Chiral Quantum Group master theorem.
