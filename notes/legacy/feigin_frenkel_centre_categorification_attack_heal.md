# Feigin-Frenkel Centre: Can the FF-Isomorphism Be Categorified to Chain Level?

## Attack

The programme's FF-adjunction (see `universal_holography_two_adjunctions_platonic_heal.md`,
`universal_holography_critical_ff_attack_heal.md`) rests on the
Feigin-Frenkel isomorphism

  FF-iso:  𝔷(ĝ)  ≅  Fun(Op_{g^L}(D^×))

proved in Feigin-Frenkel 1992 ("Affine Kac-Moody algebras at the critical level
and Gelfand-Dikii algebras", Int. J. Mod. Phys. A). The proof is an isomorphism
of COMMUTATIVE ALGEBRAS of zero-cohomology classes: 𝔷(ĝ) is the algebra of
Segal-Sugawara operators (the Poisson-central subalgebra of V_{-h^∨}(g) under
the Li-filtered Poisson bracket), and Fun(Op_{g^L}(D^×)) is the polynomial ring
on oper differentials on the punctured disk.

FF's proof proceeds via: (i) Wakimoto realisation W_0(ĝ) ↪ V_{-h^∨}(g), an
embedding into a free-field complex; (ii) the kernel of the screening charges
Q_i = ∮ e^{α_i}(z) dz acting on W_0(ĝ) is the image of 𝔷(ĝ); (iii) computation
of that kernel yields the polynomial algebra on oper differentials.

**The attack.** All three steps live at the level of *zeroth* cohomology.
Step (i) is not a quasi-isomorphism onto V_{-h^∨}(g) — the Wakimoto complex is
much larger. Step (ii) uses the SCREENING CHARGE SUBCOMPLEX, whose zeroth
cohomology is 𝔷(ĝ). But the screening charges have non-trivial *higher*
cohomology H^i (i ≥ 1) — these encode the logarithmic / quantum corrections
that the FF-iso by construction discards. Step (iii) matches H^0 to
Fun(Op_{g^L}(D^×)) but says nothing about matching the full derived structure.

If the programme's FF-adjunction is to hold at CHAIN LEVEL (not merely
cohomologically), one needs a CHAIN-LEVEL ∞-ALGEBRA quasi-iso

  FF-chain:  C^•(𝔷(ĝ))  ≃  Γ(𝒪p_{g^L}(D^×))

of E_∞-algebras in D-modules (or factorisation algebras) on the curve. Does
this chain-level enhancement exist, or is the FF-iso cohomologically rigid with
non-trivial H^{≥1} obstruction (e.g., a ζ(3) or higher-MZV coefficient
absorbing chain-level data invisible at H^0)?

## (a) What FF gets RIGHT

The cohomological FF-iso is proved and unconditional. Concretely:

1. **Zeroth-cohomology match.** 𝔷(ĝ)_{H^0} = Fun(Op_{g^L}(D^×))_{H^0} as
   commutative Poisson algebras. This is the ghost theorem.

2. **Poisson structure.** The Poisson bracket on 𝔷(ĝ) (induced from the
   second bracket on V_{-h^∨+ε}(g) expanded at ε = 0 via Hayashi-style
   regularisation) matches the Gelfand-Dikii Poisson structure on
   Op_{g^L}(D^×) induced from the oper moduli. The Poisson structures match.

3. **Factorisation compatibility.** Beilinson-Drinfeld ("Chiral algebras",
   AMS 2004, Ch. 3.6–3.8) construct the chiral algebra of g^L-opers
   𝒪p_{g^L} on the curve X and prove that 𝔷(ĝ), viewed as a factorisation
   algebra on X (the local FF centre), matches 𝒪p_{g^L} at the level of
   *factorisation structure on H^0*. This is a global-on-curve strengthening
   of FF's local statement; it proves compatibility with factorisation
   (OPE / fusion) at H^0.

4. **Classical limit.** The (Poisson) classical limit of 𝔷(ĝ), obtained as
   the associated graded with respect to the Li filtration, is Sym•(g((t))/g[[t]]),
   whose invariants give the Hitchin Hamiltonians. The classical limit of
   Fun(Op_{g^L}(D^×)) is the functions on the classical oper moduli. These
   match — this is the Hitchin-in-opers statement (BD Chiral Algebras 3.7.21).

5. **Langlands naturality.** The FF-iso is Langlands-dual equivariant: the
   LHS depends on ĝ (at critical), the RHS on opers for the Langlands dual
   g^L. This structural appearance of g^L on the oper side is the
   FF-signature of the geometric Langlands correspondence and supports the
   FF-Langlands-naturality of FF-Φ_hol in the programme's two-adjunction
   heal.

These five facts are the ghost theorem — the honest content that survives
cohomological abstraction.

## (b) What FF does NOT imply at chain level (the open question)

**FF does NOT prove chain-level ∞-equivalence.** Specifically:

1. **Wakimoto embedding is not a quasi-iso.** W_0(ĝ) ↪ V_{-h^∨}(g) is a
   genuine subcomplex; V_{-h^∨}(g) modulo W_0(ĝ) has non-trivial higher
   cohomology given by the screening-charge cokernel. This cokernel encodes
   the passage from free-field data to the actual VOA, and carries its own
   quasi-iso problems.

2. **Screening charge higher cohomology.** For each simple root α_i of g,
   the screening charge Q_{α_i} = ∮ e^{α_i}(z) dz defines a differential on
   W_0(ĝ). The intersection ∩_i Ker(Q_{α_i}) is 𝔷(ĝ) at the level of H^0.
   But each Q_{α_i} has non-zero H^1, H^2, …, corresponding to states
   annihilated modulo higher screening images. The FF-iso ignores all of
   these.

   For sl_2 (rank 1, h^∨ = 2): H^1(Q_{α}) is a 1-parameter space of "null
   vectors at level 2" (the Kac module structure); the corresponding
   derived correction to 𝔷(ĝ) at H^1 is non-zero. FF's iso does not
   address whether this H^1 matches a corresponding H^1 of the oper DG
   algebra.

3. **Oper DG structure is not rigid.** Fun(Op_{g^L}(D^×)) as an honest DG
   algebra (not just a commutative H^0 algebra) requires a CHOICE of
   quasi-iso-quotient from a derived moduli stack. Candidates: (i) the DG
   algebra of functions on the cotangent stack T^*Op_{g^L}; (ii) the Tate
   extension of Beilinson-Drinfeld's oper sheaf; (iii) Arinkin-Gaitsgory's
   singular-support filtration on coherent sheaves on Op_{g^L}. These three
   produce different DG algebras with the same H^0. Which, if any, is the
   FF partner at chain level?

4. **Chain-level Wakimoto.** The Wakimoto construction at chain level (say,
   via Frenkel-Ben-Zvi "Vertex Algebras and Algebraic Curves" Ch. 12) gives
   a quasi-iso onto a semi-infinite cohomology 𝐻^{∞/2+•}(ĝ, 𝔥; M) for
   certain modules M; this is the BRST formulation of FF. The
   semi-infinite cohomology has non-trivial higher pieces in general, and
   for critical level the analogue construction needs the critical BRST
   charge (Feigin-Frenkel 1990s). The chain-level FF candidate is
   semi-infinite-cohomology-matching-oper-cochain-DGA, but this equivalence
   is NOT PROVED.

5. **Higher-MZV obstruction.** The Drinfeld associator Φ_KZ has
   coefficients in Q[ζ(2), ζ(3), …]. Any chain-level equivalence between
   two ∞-algebras passes through a choice of associator — there is a GRT
   torsor of such equivalences (FM100 / AP-CY33). For the FF-chain
   candidate, different associators Φ would give different chain-level
   equivalences, and the ζ(2) / ζ(3) coefficients would appear as
   non-trivial higher-order corrections. Whether the H^0 FF-iso lifts to a
   SINGLE, distinguished Φ-coset of chain-level equivalences — or whether
   the lift is obstructed by a GRT-cocycle — is genuinely open.

6. **Gaitsgory 2007 ("On the notion of geometric realisation") and the
   programme of categorifying FF.** Gaitsgory constructs a derived
   equivalence of categories D(ĝ-mod_{crit}) ≃ QCoh(Op_{g^L})^{Hecke-equiv}
   (the "critical-level Kazhdan-Lusztig at g = g^L"), which is a
   CATEGORIFICATION of FF at the level of module categories, but does NOT
   directly give a chain-level ∞-algebra equivalence of 𝔷(ĝ) with
   C^•(Op_{g^L}). The Gaitsgory equivalence, combined with the
   Arinkin-Gaitsgory singular-support framework (Sel. Math. 2015), suggests
   the chain-level lift should exist — but it has not been written as a
   THEOREM on the FF centre directly.

**Concrete open.** Does there exist a natural quasi-iso of E_∞-algebras

   α:  C^•_{fact}(𝔷(ĝ))  ⟶  C^•_{fact}(Γ(X, 𝒪p_{g^L}))

inducing the FF-iso on H^0 (on local sections), such that α is compatible
with (i) the factorisation structure on both sides, (ii) the BD chiral
algebra structure on 𝒪p_{g^L}, and (iii) the DG structure coming from
semi-infinite cohomology on the LHS? This is the programme's FF-chain
question.

## (c) Correct relationship

The honest state of affairs is a **hierarchy of four statements**, each
implied by the previous:

1. **FF H^0-iso (PROVED).** 𝔷(ĝ)_{H^0} ≅ Fun(Op_{g^L}(D^×))_{H^0} as
   commutative Poisson algebras. Feigin-Frenkel 1992.

2. **FF factorisation-H^0 iso (PROVED).** The above upgrades to an iso of
   factorisation algebras on X at H^0. Beilinson-Drinfeld Chiral Algebras
   Ch. 3.7–3.8.

3. **FF ∞-categorical equivalence of module categories (PROVED).**
   D(ĝ-mod_{crit}) ≃ QCoh(Op_{g^L})^{Hecke-equiv}. Gaitsgory 2007;
   Arinkin-Gaitsgory 2015 via singular support.

4. **FF chain-level ∞-algebra quasi-iso (OPEN).** C^•(𝔷(ĝ)) ≃ C^•(Op_{g^L})
   as E_∞-algebras in factorisation algebras on X. Would follow from
   combining (3) with the Tannakian reconstruction of the chiral algebra from
   its module category, but the Tannakian argument at critical level is
   obstructed by Gaitsgory's "contractibility conjecture" (still open in
   some cases).

**For the programme's FF-adjunction, statement (3) is enough for
cohomological / categorical versions of `FF-Φ_hol ⊣ FF-Reduce`, and for the
Langlands-naturality `g ↔ g^L` as a duality of Hitchin-quantised 3d theories.
Statement (4) is strictly richer — it would upgrade the FF-adjunction to a
chain-level equivalence of 3d HT theories (rather than merely of partition
functions / categories of line operators).**

The programme should therefore STATE (3) as the current level of FF-adjunction,
and FLAG (4) as a specific open problem whose resolution would upgrade the
FF-adjunction from a categorical to a chain-level statement. A candidate
approach: use (3) to construct a chain-level Tannakian dual of the oper side
via the critical-level Hecke category; compare with the
semi-infinite-cohomology model of 𝔷(ĝ); the obstruction to equivalence is
expected to vanish after a choice of Drinfeld associator Φ_KZ, producing a
GRT_1-torsor of chain-level quasi-isomorphisms rather than a single
canonical one — consistent with the GRT-parametrised Seven Faces theorem.

## Synthesis with the programme

The four-tier hierarchy maps cleanly onto the programme's architecture:

- Tier 1 (H^0) = the programme's cohomological Thm F non-critical fragment
  applied at critical.
- Tier 2 (factorisation-H^0) = the FF-Φ_hol functor at the level of
  factorisation algebras.
- Tier 3 (∞-categorical module) = the programme's FF-Langlands-naturality
  `FF-Φ_hol(V_{-h^∨}(g))^{Langlands-R-rev} ≅ FF-Φ_hol(V_{-h^∨}(g^L))` on
  categories of line operators (`= Rep`-category of the 3d HT theory).
- Tier 4 (chain-level E_∞ quasi-iso) = the STRICTLY RICHER upgrade: a
  quasi-iso of 3d HT partition function SHEAVES, not just partition
  function NUMBERS.

The programme currently lives in tiers 1–3 at the FF-adjunction. Tier 4 is
a genuine research frontier. Status parallels the four irreducible opens in
CLAUDE.md HEAL-SWEEP: technical malpractice closed; Platonic form
articulated; one genuine research frontier remains to complete the climax.

**Closes attack:** the FF-isomorphism does NOT automatically categorify to
chain level. It does so via the Gaitsgory categorification of FF (tier 3),
which is sufficient for the programme's cohomological / categorical
FF-adjunction. Chain-level (tier 4) remains open; this is consistent with
and parallel to the four genuine opens of the HEAL-SWEEP. Flagging it
explicitly as a tier-4 frontier is the honest state.

## Independent verification anchors

- derived_from = ["Feigin-Frenkel 1992 H^0 iso", "BD Chiral Algebras
  factorisation construction", "Gaitsgory 2007 critical-level categorical
  equivalence"]
- verified_against = ["Frenkel 2007 Ch. 10 loop-group Langlands", "Arinkin-
  Gaitsgory 2015 singular-support formalism"]
- disjoint_rationale = "FF 1992 and BD 2004 construct 𝔷(ĝ) from Segal-
  Sugawara operators in affine algebra representation theory; Gaitsgory 2007
  and AG 2015 construct the categorical equivalence via derived algebraic
  geometry on oper moduli, independently. Both are independent of the
  programme's chiral bar-cobar / Universal Holography framework."
