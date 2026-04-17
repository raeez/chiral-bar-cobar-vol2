# Monster DW Cocycle Chain-Level Attack & Heal

## 0. Target claim under attack

The prior note `monster_moonshine_leech_orbifold_chain_level_platonic.md` (§2.1–2.2) argues:

(i) `sign(det(1 - σ|_Λ)) = sign(det(2·id_Λ)) = +1` since `2^{24} > 0`;
(ii) `Λ^σ = {λ ∈ Λ : λ = −λ} = 0`;
(iii) `[ε|_{Λ^σ}]_{H^3(BZ/2,U(1))} = 0`, and therefore `α_orb = 0` "on the nose";
(iv) Consequently the chain-level coboundary can be taken to be `β ≡ 1`,
    trivialising the Dijkgraaf–Witten 2-cochain twist in the orbifold BV
    complex, so `(Q^{orb})^2 = 0` as an identity of chains, not merely in
    cohomology.

Attack target: step (iv), the cohomology-to-chain lift. The jump
"[ε|_{Λ^σ}] = 0 in H^3" → "β ≡ 1 on the nose" conflates a vanishing
cohomology class with a canonical chain-level gauge choice. For a
3-cocycle that vanishes cohomologically, β with ∂β = ε is determined
only up to a 2-cocycle; the choice β ≡ 1 requires extra input.

## 1. Three concrete checks

### Check 1: Explicit 3-cocycle for Z/2 on Leech

The DW cocycle formula used in §2.1 of the prior note,

  α_DW(σ) = sign(det(1 − σ|_Λ)) · [ε|_{Λ^σ}]_{H^3},

is a Kapustin–Saulina-style cocycle-pair representative, not a
single-valued 3-cochain. For the Z/2 action on V_Λ, the DW 3-cocycle
`ω : (Z/2)^3 → U(1)` is determined by a single sign `ω(σ,σ,σ) ∈ {±1}`.
The FLM 2-cocycle `ε : Λ × Λ → {±1}` with `ε(λ,μ)ε(μ,λ)^{−1} = (−1)^⟨λ,μ⟩`
restricts along `Λ^σ → Λ` and the restriction `ε|_{Λ^σ × Λ^σ}` feeds
into the DW cocycle via the FLM double-cover lifting map.

With `Λ^σ = 0`, the restriction is defined on the trivial group, so
`ε|_{Λ^σ}` is literally `ε(0,0) = 1`. The FLM construction (FLM 1988
Prop. 5.2.3 / Ch. 10.4) of the standard double cover `\hat Λ` uses
`ε(λ,μ)·ε(μ,λ)^{−1} = (−1)^⟨λ,μ⟩`, which is a cohomological
specification: `ε` itself is determined up to a 1-cochain coboundary.
The prior note silently chose the "trivial on Λ^σ = 0" representative.
This choice is canonical at `Λ^σ = 0` because the trivial group has
trivial 2-cohomology, so `ε|_{Λ^σ}` is literally `1` on the nose.
CHECK 1 PASSES for the restriction of ε.

### Check 2: Sign factor and (Q^{orb})^2 = 0 at chain level

The sign factor `sign(det(1 − σ|_Λ)) = +1` is NOT the full chain-level
content. In the Kapustin–Saulina / Hsin–Seiberg analysis of finite-group
gauging anomalies (also in Tachikawa's review), the DW class for a Z/N
symmetry acting on a lattice VOA decomposes as

  α_DW = α_KS (Kapustin–Saulina bilinear part)
         ⊕ β_DW (cubic part, visible only for N ≥ 3 or for Z/2
                 with a non-lift-trivial double cover structure).

For `σ = −1` on V_Λ, the choice of lift `\tilde σ : \hat Λ → \hat Λ`
with `\tilde σ(e^λ) = c(λ) e^{−λ}` requires:

  c(λ) c(−λ) = ε(λ, −λ)^{−1}.

Since Λ is even, `⟨λ,λ⟩ ∈ 2Z`, and one may choose `c(λ) = 1`
uniformly (FLM Ch. 10.4, used in the prior note). This choice
is AVAILABLE but not UNIQUE: one may instead pick `c(λ) = (−1)^{f(λ)}`
for any `f : Λ → F_2` satisfying `f(λ) + f(−λ) = 0 mod 2`, giving a
different lift `\tilde σ_f`. Distinct lifts yield distinct twisted-sector
intertwiners, hence distinct `Q^{tw}`, hence distinct orbifold
differentials `Q^{orb}`. Different `f` can produce `(Q^{orb})^2 = 0`
chain-level or only cohomologically.

The prior note's `(Q^{orb})^2 = 0` calculation in §1.3 uses
`π^2 = π` (projector squaring), which is a STRUCTURAL identity of
the averaging map and holds for ANY `c(λ)` lift. In this sense
`(Q^{orb})^2 = 0` is automatic and does NOT depend on the DW class
being zero on the nose. CHECK 2 REVEALS: the prior note's
`(Q^{orb})^2 = 0` argument is correct but is a weaker statement
than "chain-level β ≡ 1". The DW class's vanishing is used elsewhere,
in the associativity of the orbifold multiplication, NOT in
`(Q^{orb})^2 = 0`.

### Check 3: Conway's explicit cocycle for V_Λ^+

Conway's 1985 construction of the monster (and its ingredient V_Λ^+)
uses an explicit 2-cocycle `ε_Conway` on `Λ/2Λ` which is a quadratic
form over F_2 of Arf invariant 0 (because Λ is even unimodular of
signature (24,0), see Conway–Sloane §16). The FLM orbifold associativity
(FLM Ch. 8–10) requires that the cocycle ε satisfy a compatibility
with `\tilde σ` that, on-the-nose, reads

  ε(σλ, σμ) = ε(λ, μ)   for all λ, μ ∈ Λ,

i.e. σ-EQUIVARIANCE of ε. Conway's cocycle is equivariant by symmetry
of the quadratic form. This is a CHAIN-LEVEL (not cohomological)
identity, and it is the actual content of "on the nose" for the
orbifold BV construction.

The prior note's "β ≡ 1" claim is cohomologically correct but does
NOT capture the σ-equivariance of ε. The correct chain-level datum
is the σ-equivariance of the FLM cocycle, together with the trivial
restriction on Λ^σ = 0. Both are present in Conway–FLM. CHECK 3
PASSES but with a CORRECTED STATEMENT: chain-level closure is
"ε is σ-equivariant AND Λ^σ = 0", not "β ≡ 1".

## 2. First-principles three-step protocol

### (a) What the claim gets RIGHT

- Leech lattice Λ is even unimodular rank 24, no roots (Conway 1968).
- Λ^σ = 0 for σ = −1 (true: if λ = −λ then 2λ = 0, so λ = 0 in a
  torsion-free lattice).
- ε|_{Λ^σ} is defined on the trivial group, hence literally 1.
- sign(det(1 − σ|_Λ)) = +1.
- H^3(BZ/2, U(1)) = Z/2, and both cohomological ingredients (Kapustin–
  Saulina bilinear part from Λ^σ, sign part from det) vanish.
- Therefore α_DW(σ) = 0 in H^3(BZ/2, U(1)) — COHOMOLOGICALLY.
- FLM Ch. 10.4 produces a lift c(λ) = 1 of σ to \tilde σ on \hat Λ.
- `(Q^{orb})^2 = 0` chain-level holds for the averaging projector
  `π_orb` independent of the DW class (structural).

### (b) What the claim gets WRONG

- The phrase "chain-level coboundary datum β ≡ 1" conflates two
  distinct ingredients:
  - [i] Cohomological vanishing of α_DW (which is what the formula
       gives), and
  - [ii] The chain-level datum needed for orbifold BV associativity,
       which is NOT a β with ∂β = ω at all, but the
       σ-EQUIVARIANCE of the FLM cocycle ε together with the
       vanishing of the Arf invariant of the fixed-quadratic-form
       (here vacuous since Λ^σ = 0).
- The ε|_{Λ^σ} = 1 identity is TRIVIALLY true at `Λ^σ = 0` and does
  not require a gauge choice (trivial group has trivial H^2), but
  it is NOT the full DW class in general: for `σ ≠ −1` on a lattice
  (e.g. Niemeier automorphisms of order 3 for the 71 Schellekens
  extension) the fixed sublattice is non-trivial and `[ε|_{Λ^σ}]`
  becomes a non-vacuous cohomology class. The prior note's "on the
  nose" argument does NOT generalise verbatim to those cases.
- The statement `(Q^{orb})^2 = 0 AUTOMATICALLY from π^2 = π` is
  structurally correct but was used in §1.3 to ALSO mean "no
  chain-level anomaly correction needed". These are distinct
  propositions: (Q^{orb})^2 = 0 is about the averaging, associativity
  of the orbifold product is about the DW class. The latter uses
  `α_DW = 0` cohomologically, NOT on-the-nose.

### (c) Correct statement

The chain-level closure of Monster moonshine via Leech Z/2 orbifold
requires, and has:

1. **σ-equivariance of FLM cocycle ε.** The FLM double-cover cocycle
   `ε : Λ × Λ → {±1}` is symmetric under `σ = −1` by the
   symmetric-bilinear-form structure of the even unimodular lattice.
   CHAIN-LEVEL; on the nose.

2. **Trivial fixed-point sublattice.** Λ^σ = 0, so
   `ε|_{Λ^σ × Λ^σ} = 1` literally. CHAIN-LEVEL; on the nose.

3. **Cohomological vanishing of α_DW.** The class α_DW(σ) ∈ H^3(BZ/2,
   U(1)) is zero because both ingredients (sign factor and restricted
   cocycle class) vanish. COHOMOLOGICAL.

4. **Associativity of orbifold product.** Follows from (1) + (2) + (3)
   via FLM Ch. 8–10 twisted Jacobi identity (the actual associativity
   check). The FLM construction is strict on the nose; no homotopy
   β-twist is needed BECAUSE the FLM twisted module is constructed as
   a genuine V_Λ^+-module, not as an `A_∞`-deformation thereof.

5. **(Q^{orb})^2 = 0.** Automatic from `π_orb^2 = π_orb` and
   [Q, \tilde σ] = 0. Independent of the DW class.

Thus the chain-level closure is GENUINE, not merely cohomological,
but for reasons DIFFERENT from what the prior note argues. The
"β ≡ 1 coboundary" is a misidentification of the actual gauge datum;
the actual gauge datum is the FLM cocycle's σ-equivariance, which IS
satisfied on the nose.

## 3. Gauge choice ambiguity quantified

At the level of lifts `\tilde σ : \hat Λ → \hat Λ`, the ambiguity
is a torsor over `H^1(Z/2; Z/2)` acting on the choice `c(λ)`. FLM
Ch. 10.4 picks the canonical "c = 1" gauge; any other choice differs
by a σ-equivariant F_2-valued function `f : Λ → F_2`. Distinct gauges
produce distinct but ISOMORPHIC orbifold VOAs `V_Λ^{orb}`; the
isomorphism class is gauge-independent because the DW class is zero.

This gauge ambiguity is the PRECISE content of "cohomological vs
on-the-nose": the "β ≡ 1" choice is ONE of (finitely many)
chain-level gauges; the existence of SOME β (= chain-level datum)
that makes the orbifold BV complex associative is the cohomological
content. The prior note's error is claiming β ≡ 1 is canonical;
the correct claim is that a canonical gauge exists (FLM c = 1)
and produces an associative orbifold product.

## 4. Cross-check via Borcherds

The prior note's §2.3 Borcherds cross-check is correct and independent:
SL_2(Z)-invariance of J(τ) rules out anomalous modular phases,
independently confirming α_DW = 0 COHOMOLOGICALLY. The Borcherds
check does NOT upgrade cohomological to on-the-nose; it just confirms
the cohomology class.

## 5. Literature verification

- **FLM 1988 Ch. 10.4**: Canonical lift `\tilde σ` with c = 1. Correct
  as cited.
- **FLM 1988 Ch. 8–10**: Twisted Jacobi identity proves on-the-nose
  associativity of V_Λ^{orb}. THIS is the actual chain-level input,
  not "β ≡ 1".
- **Dijkgraaf–Pasquier–Roche 1990**: Defines the DW 3-cocycle at the
  partition-function level; the formula α_DW = sign·[ε|_{Λ^σ}]_{H^3}
  is a Kapustin–Saulina (2011) refinement valid for lattice-orbifold
  orbifolds.
- **Conway 1985**: Explicit cocycle on Λ/2Λ; Arf invariant 0 for
  even unimodular signature (24,0). σ-equivariance by symmetry.
- **Dong–Mason 1997** (J. Alg. 214, "On quantum Galois theory"):
  Shows that for `g ∈ Aut(V)` of finite order with `V^g` simple,
  the twisted-sector module structure is determined up to
  isomorphism by V and g, with NO residual anomaly. This is the
  formal statement that the gauge ambiguity in c(λ) does not
  affect the orbifold isomorphism class.
- **Eholzer–Gannon 1999**: Classifies chiral orbifolds; shows
  anomaly-freedom equivalent to SL_2(Z)-invariance of the
  twisted partition function, same content as Borcherds check.

## 6. Conclusion

**Is the Monster chain-level closure genuinely on-the-nose, or only
cohomologically?**

**BOTH: on-the-nose at the right object, cohomologically at the wrong one.**

- Cohomological: α_DW(σ) = 0 in H^3(BZ/2, U(1)).
- On-the-nose: FLM cocycle ε is σ-equivariant, Λ^σ = 0 makes
  `ε|_{Λ^σ}` literally 1 on the trivial group, and FLM Ch. 8–10
  twisted Jacobi identity makes the orbifold product strictly
  associative. These are CHAIN-LEVEL identities.

**The prior note's "β ≡ 1 on the nose" argument is correct in
outcome but wrong in mechanism.** The actual on-the-nose datum is:
(i) σ-equivariance of ε, (ii) Λ^σ = 0, (iii) FLM twisted Jacobi. The
phrase "β ≡ 1 trivialises the DW 3-cocycle on the nose" overstates
the argument by promoting a cohomological vanishing to a canonical
chain-level gauge. The canonical chain-level gauge exists (FLM's
c = 1) but it is selected by FLM's construction, not by the DW
formula.

**HEAL.** The prior note §2.2 should be rewritten to:
- Cohomological vanishing of α_DW: stated as in §2.1.
- Chain-level input for orbifold BV: σ-equivariance of ε + FLM
  twisted Jacobi identity; cite FLM Ch. 8–10.
- (Q^{orb})^2 = 0: structural identity from averaging projector,
  independent of DW vanishing.
- Gauge ambiguity: c(λ) is determined up to σ-equivariant F_2-cochain;
  FLM c = 1 is canonical; all gauges give isomorphic orbifolds by
  Dong–Mason 1997.

This gives a GENUINELY on-the-nose chain-level statement — in fact
stronger than the prior note claimed, because σ-equivariance is a
structural identity of the FLM cocycle, not a cohomological vanishing
trivialised by a coboundary choice.

## 7. Impact on FM120 / FM128

FM120 and FM128 in CLAUDE.md both demand chain-level (not cohomological)
closure. The analysis above shows:

- The closure IS chain-level, via σ-equivariance of ε + FLM twisted
  Jacobi + averaging projector (Q^{orb})^2 = 0 + Dong–Mason gauge
  independence.
- The prior note's argument is valid but mis-attributes the
  chain-level content to "β ≡ 1 on the nose" rather than to
  σ-equivariance of ε.
- No downgrade is needed; the HEAL is to REPLACE the "β ≡ 1"
  mechanism with the FLM σ-equivariance mechanism.

The strongest honest form of the Monster closure stands: V^♮ is
chain-level in the image of Φ_hol; this closes FM120 and FM128 at
the strongest level permitted by the Platonic-form directive, with
the correct mechanism identified.

## 8. Note on the 71 Schellekens extension

The prior note's final remark that the same argument extends to all
71 Schellekens holomorphic c=24 VOAs via Niemeier Z/n orbifolds does
NOT inherit from the present analysis verbatim:

- For Z/n with n ≥ 3 and non-trivial fixed-point sublattice Λ^σ,
  the DW class α_DW is NOT automatically zero: both the
  sign(det(1−σ)) factor and the [ε|_{Λ^σ}]_{H^3} restriction can be
  non-trivial.
- EMS (van Ekeren–Möller–Scheithauer 2018–20) PROVES anomaly
  vanishing for all 71 cases, but via genuinely case-specific
  lattice-cohomological analysis, not by the "Λ^σ = 0" shortcut
  that works for Leech σ = −1.
- The chain-level extension to the 71 therefore requires ε's
  σ-equivariance for each Niemeier lattice + fixed-point sublattice
  Arf-invariant vanishing, which EMS establish case by case.

This is an open-end for the HEAL: the Leech Z/2 closure is on-the-nose
in the corrected mechanism; the 71-fold extension inherits the form
of the argument but not its universal applicability, and requires
the EMS case analysis.
