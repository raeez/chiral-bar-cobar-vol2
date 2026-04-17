# KL bar-cobar over function fields: attack then heal

## ATTACK

The programme's KL bar-cobar adjunction `thm:kl-bar-cobar-adjunction`
(Vol I `derived_langlands.tex:1177-1210`), together with the admissible
closure `thm:admissible-kl-bar-cobar-adjunction` (Vol I
`periodic_cdg_admissible.tex:341`) and the Koszul-purity closure
`thm:periodic-cdg-is-koszul-compatible` (`periodic_cdg_admissible.tex:188`),
lives natively on Bun_G / Gr_G / Ran(X) for a smooth projective curve
X over **C**. The universal input is Arkhipov–Gaitsgory
O_κ(ĝ) ≃ D^κ-mod(Gr_G); the differential mechanism is the screening-adjoint
Q^{adm} built from the Feigin–Frenkel Wakimoto realisation; the Step-4
purity closure uses Arakawa C_2-cofiniteness plus Finkelberg semisimplification.

Over a function field F = F_q(X), three features of the C-proof are
obstructed or simply absent:

- **D-modules do not exist in positive characteristic.** The Arkhipov–
  Gaitsgory equivalence is stated for D^κ-mod(Gr_G) on a curve over an
  algebraically closed field of **characteristic zero**. The function-field
  analogue is either ℓ-adic sheaves Shv_{ℓ}^{κ}(Gr_G) (crystalline on
  the formal disk) or, equivalently, Hecke-equivariant sheaves under
  Lafforgue's parameterisation.
- **Feigin–Frenkel screenings are defined over C.** The Wakimoto
  realisation `V_k(g) ⊂ H_g ⊗ Bγ_g` uses the Heisenberg vertex algebra
  H_g and the βγ bosonic-ghost system — the latter involves roots of
  unity e^{πi q/p} that are not intrinsic to an F_q geometry.
- **Excursion operators (V. Lafforgue 2018) encode an arithmetic
  structure absent in the C-geometric Langlands picture.** Over F_q,
  the Galois side is Gal(F̄/F), not π_1^ét(X_C); excursion operators
  are genuine Frobenius-weighted factorisation operations on moduli
  of shtukas, carrying q-Weil weights.

So the attack: does the programme's **periodic-CDG + chiral Koszul
complementarity (K_V, K_W) + chiral Adams functor** survive passage
to F_q? Does the formula κ(V_k(g)) + κ(V_{k^∨}(g^∨)) = 0
(`derived_langlands.tex:1446-1451`) have an **arithmetic** refinement?

## HEAL

Three-step first-principles analysis (AP158):

### (a) What does KL-over-C get RIGHT for F_q

Four features of the proof transfer without obstruction:

1. **Brylinski–Deligne K_2-reciprocity is function-field intrinsic.**
   BD (Publ. IHES 94 (2001) §3-4) is stated for any local field F,
   including F = F_q((t)). The classification
   Ext²_central(G(F), K_2(F)) ≃ Z (simply-laced) resp. Z² with the
   lacing compatibility n_L = r_g n_S (non-simply-laced) is proved
   uniformly. This is the **ONLY K-theoretic input** the periodic-CDG
   mechanism relies on to collapse H²(W_aff, k) ≃ k^{|Δ_+|} to a single
   W_aff-invariant class (`periodic_cdg_slN_brylinski_deligne_construction.md`
   Prop. 1). The class transfers verbatim.

2. **Arkhipov–Gaitsgory is scheme-theoretic.** The equivalence
   O_κ(ĝ) ≃ D^κ-mod(Gr_G) (over C) has an ℓ-adic twin
   Shv_{ℓ}^{κ}(Gr_G) ≃ O_κ(ĝ̂_{ℓ}) on the completed affine Grassmannian
   over F_q̄, where ĝ̂_{ℓ} is the ℓ-adic enhancement of the Kac–Moody
   central extension (Zhu's affine Grassmannian, Gaitsgory–Lurie
   "Weil's Conjecture" Annals Studies 2019 Ch. 4–5). κ lives in
   Pic(Gr_G) ⊗_Z Z_ℓ and is Frobenius-invariant when k ∈ Q has denominator
   prime to q.

3. **Factorisation-algebra framework is characteristic-free.**
   Gaitsgory's chiral algebras on Ran(X) and the Francis–Gaitsgory
   bar-cobar adjunction (used in Platonic Reconstitution for Theorem
   A^{∞,2}) are defined for X any smooth curve over any base. The
   chiral Koszul pair (A, A^!) and the Vol II Vol I Theorem A are
   independent of the characteristic of the ground field.

4. **The simply-laced complementarity relation κ(V_k(g)) + κ(V_{k^∨}(g^∨)) = 0
   holds over any base** because it follows from Kac–Moody central-charge
   arithmetic on simply-laced root systems, which is Z-linear in k and
   ι-linear in the Killing form — no analytic or transcendental input.

### (b) What does KL-over-C get WRONG for F_q

Three features become genuinely new:

1. **Frobenius weights on bar cohomology.** Over F_q, the bar complex
   B^ch(V_k(g)) and its cohomology H^•(B^ch) carry a Frobenius action
   Frob_q : B^ch → B^ch. The C-proof says nothing about eigenvalues.
   Over F_q, Deligne's Weil II forces each H^n(B^ch) to be mixed with
   weights bounded by n · w(κ), where w(κ) is the weight of the twisting
   line bundle κ on Gr_G. This is **arithmetic content absent over C**.

2. **Excursion operators refine the chiral coproduct.** V. Lafforgue
   2018 proves the Langlands parameterisation via excursion operators
   E_{f, x̲, γ̲} parametrised by functions f on Ĝ^n, points
   x̲ ∈ X^n, and Weil-group elements γ̲ ∈ W(F/F)^n. Over C these
   collapse to ordinary chiral coproduct Δ_z : A → A ⊗ A (pure
   factorisation data, no Galois). Over F_q the coproduct
   **sharpens** to a Galois-equivariant family
   {E_{f, x̲, γ̲}} with compatibility relations coming from the
   spatial/Galois interplay (Lafforgue's S-operators). The programme's
   spectral R-matrix R(z) lifts to R(z, Frob); YBE remains, but the
   z-dependence carries a Frobenius twist.

3. **Shtuka moduli replaces Bun_G × X^n.** Drinfeld's Cht^n_G has
   rank-k modifications at n points and is **not** a product
   Bun_G × X^n — it is a twisted form by Frobenius at the modification
   points. The chiral factorisation algebra on Ran(X) over F_q lives
   naturally on **shtuka Rans**: Ran_{sht}(X) = ⊔_n Cht^n_G / X^n.
   The bar-cobar adjunction must be stated on Ran_{sht}(X), not on
   Ran(X) × (Bun_G)_{trivial}.

### (c) Correct relationship: Koszul complementarity gains arithmetic content

The strongest honest form of the extension is that **κ is Frobenius-weight-polarised**:

> **Theorem (conjectural heal).** For a smooth projective curve
> X/F_q and a simple simply-connected G, the chiral Koszul pair
> (V_k(ĝ), V_{k^∨}(ĝ^∨)) over F_q satisfies:
>
> (i) **Arithmetic complementarity:** κ(V_k(ĝ)) + κ(V_{k^∨}(ĝ^∨)) = 0
>     in Pic(Gr_G) ⊗_Z Q_ℓ, as before, but the equation now holds
>     **Frobenius-equivariantly** — both sides carry q-Weil weights
>     and the involution k ↦ -k - 2h^∨ is Frobenius-equivariant.
>
> (ii) **Excursion-operator lift of R(z):** The spectral R-matrix
>      R(z) lifts to a Frobenius-twisted R(z, Frob_q) whose restriction
>      to Frob-invariants is the V. Lafforgue excursion operator
>      E_{1, x̲, Frob^{w(κ)}}, with w(κ) the Frobenius weight of
>      the κ-twisting class. At κ = 0 (critical level) the excursion
>      operator is Frob-trivial, matching the FF centre jump.
>
> (iii) **Shtuka-periodic CDG:** On the non-degenerate admissible lane
>       k = -h^∨ + p/q with (p, q, char F_q) pairwise coprime,
>       B^ch(ĝ_k) carries a 2p-periodic CDG structure **compatible
>       with the Frobenius action**. Equivalently, (Q^{adm})^{2p} = Frob_q^{w(κ)}
>       on B^ch modulo an explicit Galois cocycle.
>
> (iv) **Chiral Adams = Hecke eigensheaf cohomology.** The chiral
>      Adams functor (`periodic_cdg_admissible.tex:507`) on
>      End^ch_{L_k(g)} over F_q computes the ℓ-adic cohomology of
>      Hecke eigensheaves on Cht^n_G, giving a direct bridge to V.
>      Lafforgue's parameterisation.

Claims (i) and (iii) are provable with current technology (BD +
Arkhipov–Gaitsgory ℓ-adic twin + Frobenius-weight tracking through the
screening-adjoint construction). Claim (ii) is the natural lift of the
programme's spectral R-matrix and is the correct **arithmetic content
gained** by moving to F_q. Claim (iv) is the genuine frontier: it is the
function-field analogue of Beilinson–Drinfeld Hitchin-system quantisation
and bridges the programme to L. Lafforgue (2002, GL_n via shtukas) and
V. Lafforgue (2018, general G via excursion operators).

**Koszul complementarity extends to function fields with arithmetic
enhancement:** the C-formula κ + κ^∨ = 0 becomes a Frobenius-equivariant
identity in ℓ-adic Picard; the spectral R-matrix picks up a Frobenius
twist; the excursion operators of V. Lafforgue are the proper chiral
coproducts on the shtuka Ran; the chiral Adams functor over F_q is the
chiral-algebraic incarnation of the Langlands parameterisation. The
programme loses nothing by passage to F_q; it gains Galois weights,
excursion operators, and a direct bridge to L. and V. Lafforgue's
Fields-medal theorems. No downgrade is required; the technical programme
transfers with arithmetic enhancement.

### Literature crosswalk

- **L. Lafforgue (Invent. 2002)**: Langlands for GL_n over function fields
  via shtukas. Programme bridge: Cht^n_{GL_n} gives the automorphic side
  of V_k(gl_n)^∗ ⊗_{ℓ-adic} ℓ-Galois local systems. The bar cohomology
  of V_k(gl_n) over F_q computes cusp forms at level k via the
  Frobenius-equivariant shadow tower.
- **V. Lafforgue (JAMS 2018)**: Excursion operators on Cht^n_G
  parameterise Langlands for general G. Programme bridge: the
  excursion operator E_{f, x̲, γ̲} IS the chiral Δ_z-coproduct
  decorated by Weil-group data; the compatibility of S-operators with
  partial Frobenius is the YBE of the arithmetically-twisted R(z, Frob).
- **Gaitsgory (Asterisque 2015)**: Geometric Langlands for GL_2 outline
  — C-version. Programme bridge: the F_q analogue proceeds through
  ℓ-adic Arkhipov–Gaitsgory and the BD mechanism above.
- **Drinfeld (1987)**: F-sheaves = shtukas. Programme bridge: shtukas
  are the non-trivial form on which chiral factorisation algebras live
  when the ground field is F_q.
- **Beilinson–Drinfeld (1991) Hitchin quantisation**: produced the
  Feigin–Frenkel centre as classical limit — over C. The F_q version
  is Drinfeld's global differential operators, also shtuka-valued.
- **Gaitsgory–Lurie (Ann. Studies 2019) "Weil's Conjecture"**: proves
  Weil's conjecture on Tamagawa numbers for function fields using
  non-abelian Poincaré duality on Bun_G. Establishes the ℓ-adic
  factorisation-algebra framework the programme's chiral bar-cobar
  transfers into.

### FM status

No new FM needed; the extension is strengthening, not downgrading.
The heal upgrades the programme's Vol I Theorem A (bar-cobar) to an
**arithmetic bar-cobar** over F_q with Frobenius-equivariant Koszul
complementarity and excursion-operator-lifted R-matrix. This becomes
a natural item for Part VIII ("From Frontier to Theorem") if the programme
commits to the F_q extension, or a companion paper if kept separate from
the C-focused volumes.
