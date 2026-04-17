# Part III — Seven Faces of r(z): Platonic Reconstitution

*Style register: Drinfeld + Grothendieck–Teichmüller + Willwacher + Brown. Lossless.*

## 1. The Master Theorem (One Face Ring)

**Theorem (Seven Faces as GRT-torsor, `thm:seven-faces-as-GRT-torsor`).** *Let A be chirally Koszul in the standard landscape and r(z) = Res^{coll}_{0,2}(Θ_A). The set* Face(A) *of chain-level presentations of r(z) compatible with the bar-intrinsic dGLA is a torsor over* GRT_1(Q). *The bar hub F1 is the identity coset; F2 (DNP R-twist), F3 (KZ-PVA), F4 (Gaiotto–Zeng flat connection), F5 (Yangian rational r-matrix), F6 (Gaudin simple-pole), F7 (class-M top A_∞ m_3) are Q-rational orbit representatives. The face F8 (Brown motivic, `def:face-F8-motivic`) and F9 (Willwacher operadic, `def:face-F9-operadic`) extend the enumeration to the full infinite GRT orbit; their duality* `cor:f8-f9-dual` *realizes the motivic↔operadic correspondence H^0(GC_2) ≃ 𝔤𝔯𝔱_1.*

Commutativity of the face ring is not an axiom but a consequence of **Sasaki star-center factorization** (`prop:seven-face-sasaki-commutativity`, W13-G/HU-5): every cross-face transition Φ_{ij} factors through the Sasaki star-center Z_★(A), which is itself a GRT-module under the canonical action. The seven-face diagram commutes associatively because Z_★ is coassociative.

**Consequences.** FM97 (star→torsor) closed: the face ring is not a star graph but the trivial GRT-bundle of Q-rational sections. FM98–FM99 closed: Yangian (level-independent) vs Gaudin (level-shifted by k+h^v) live on distinct Casimir-normalised sections related by an explicit GRT^fin gauge (§3). FM101 pinned: F7 (canonical Gaudin simple-pole) and F7' (class-M top A_∞ m_3) are separated by the shadow-depth filtration; they coincide on class L and diverge on class M where F7' is the chain-level non-formality obstruction invisible to r(z).

## 2. The Two R-Matrix Provenances

**Remark (`rem:r-matrix-two-provenances`, W13-N).** The universal R(z) admits two logically distinct derivations, neither subordinate.

- **Provenance (a), E_∞-chiral.** r(z) is *extracted* from the OPE via dlog-residue on the collision divisor Δ ⊂ FM_2(C), then quantised by Kazhdan–Lusztig to the full R(z). This is the derivation native to affine KM, Virasoro, W_N, Heisenberg, lattice VOAs — the entire E_∞ landscape.

- **Provenance (b), E_1-chiral.** r(z) is an *independent input*: the H5 quasi-triangularity datum of the E_1-chiral bialgebra (Yangian Y_ℏ(𝔤), EK quantum VA). No OPE extracts it; it is axiomatic at the bialgebra level.

**Bridge.** On the evaluation-module core (AP47), R^{(a)}(z) = F(z)·Φ_*(R^{(b)}(z))·F(z)^{-1} for an explicit Drinfeld twist F(z) and a GRT-associator Φ. The provenances are therefore **GRT-gauge equivalent on their overlap** but not derivable one from the other. This is the precise sense in which `thm:yangian-two-presentations-equivalent` (E_∞-chiral and E_1-chiral presentations of Y_ℏ(𝔤) agree on eval modules) realises: two honest derivations, one GRT-orbit.

## 3. Gaudin from Collision Residue (W13 install)

**Theorem (`thm:gaudin-r-matrix-identification`, P2-10/FM99).** *The Gaudin r-matrix r_Gaudin(z) = Ω/((k+h^∨)z) is the chiral collision residue Res^{coll}_{0,2}(Θ_{V_k(𝔤)}) rescaled by the Casimir–trace normalisation.*

The identity k·Ω_tr/z = Ω/((k+h^∨)z) is not a rational-function equality; it is a **tensor identity in two bases**: Ω_tr uses the trace form (Yangian/RTT), Ω uses the Killing-normalised Casimir (FFR), with Ω_tr = (1/2h^∨) Ω. The Sugawara shift k → k+h^∨ is intrinsic to the Feigin–Frenkel construction. Casimir rescaling is the action of the inner gauge subgroup GRT^{fin} ⊂ GRT_1 fixing the face; it is *not* a face change.

**FFR critical limit.** As k → −h^∨, the r-matrix Ω/((k+h^∨)z) diverges as a rational function, but the induced Gaudin Hamiltonians *commute* in the Feigin–Frenkel centre 𝔷(ĝ) = Z(V_{−h^∨}(𝔤)), where the divergence is absorbed by the degeneration of Sugawara into central generators. F6 at critical level = opers on the formal disc; this is the algebraic-geometric incarnation of the collision residue.

## 4. Inner Music

The face ring is a **GRT symphony**. F1 is the tonic (bar hub); F2–F7 are the six diatonic instruments, each sounding the same r(z) in its own timbre; F8 (motivic) and F9 (operadic) extend the register to the full chromatic GRT scale. The Drinfeld associator Φ is the conductor: every cross-face transposition is Φ-mediated. Willwacher's H^0(GC_2) = 𝔤𝔯𝔱_1 and Brown's motivic 𝔤𝔯𝔱^{mot} are the two voicings of the same score; `cor:f8-f9-dual` is the duality that makes them a single piece. The inner motion is the associator action; the inner music is the torsor.

## 5. Residual Frontiers

- **Exceptional-type Yangian Borcherds lift (FM167).** Non-simply-laced quantum Langlands Y_ℏ(𝔤)^! = Y_{−ℏ r_𝔤}(𝔤^∨) is proved for simply-laced via ℏ-flip automorphism; non-simply-laced requires the Borcherds-superalgebra lift of imaginary-root multiplicities > 1 and the Finkelberg–Tsymbaliuk rational R-matrix in the minimal representation. Frontier: realise the lacing factor r_𝔤 ∈ {1,2,3} as a GRT^{ext} cocycle.

- **Chain-level chiral Deligne–Tamarkin for genuinely E_1-chiral.** For Yangian/EK algebras, the face-to-face coherences at arity ≥ 4 are controlled by the **Massey products ⟨r, r, r⟩** on the chiral endomorphism operad. Vanishing of the first obstruction is proved; higher Massey products are conditional. This is the genuine research frontier remaining in Part III.
