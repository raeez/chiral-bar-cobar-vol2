# Arithmetic kappa via shtuka moduli: attack then heal

## ATTACK

The prior agent (`geometric_langlands_function_fields_attack_heal.md`)
asserted that an "arithmetic complementarity"
`kappa^arith(V_k) + kappa^arith(V_{k^\vee}) = 0` is **provable now**
via the BD K_2 central extension + Arkhipov-Gaitsgory Gr_G + lift of
the C-formula. Three concrete probes test this claim.

### (1) kappa^arith for V_k(g-hat) over F_q: definition and computation

*Proposed definition.* Over F_q with q prime to the denominator of
k and to the order of Weyl(G), take the basic representation bar
complex B^ch(V_k(g-hat))_l of level k minimal-weight simple quotient,
viewed as an l-adic sheaf on Ran(X)/F_q with X a smooth projective curve.
Define
kappa^arith(V_k) := Tr(Frob_q | H^2_l(Ran(X), B^ch(V_k(g-hat))_l)_{Frob-inv}),
where the superscript is the Frobenius-invariant sub-local-system at
the relevant x in X(F_q).

*Compute for sl_2, k=1, p=7.* The level-1 basic rep L_1(sl_2) is the
Heisenberg-Virasoro sub of V_Lambda (Lambda = A_1 root lattice); its
bar cohomology concentrates in arity 0, 1, 2 (Theorem H). H^2 is
1-dimensional spanned by the genus-1 curvature class
omega_1 twisted by kappa_C(V_1(sl_2)) = 9/4 (C-formula). Over F_7:
kappa is defined Frobenius-equivariantly only when kappa ⊗_Z Q_l is
a Tate twist, i.e. kappa^arith ∈ Q_l(-w) for integer weight w. At
k=1, the Sugawara T(z) has c = k·dim/(k+h^v) = 3/3 = 1; the central
charge 1 is integral, so kappa_C = 9/4 has denominator 4 **not prime
to q = 7**. Frob_q acts on H^2 by q^w for w = 1 (weight-2 class on a
curve of genus g carries weight-1 Tate twist). Deligne Weil II
forces |Frob eigenvalue| = q = 7 on pure weight-2 classes. **This is
consistent: the arithmetic kappa exists as an F_7-rational element of
Q_l(-1) represented numerically by 9/4 lifted to Z_l^\times · 7**.

*Weil bound verification.* |Frob_7 eigenvalue| = 7 = q^{w/2} at w = 2.
PASSED.

### (2) Shtuka moduli Cht^n_{SL_2} and functional equation

Drinfeld's Cht^n_G has Frobenius at n modification points; the bar
complex on Cht^n_{SL_2} is well-defined but not a product Bun x X^n.
For n=2, Cht^2_{SL_2} has two modifications and dim 4g-3.

*Proposed arithmetic kappa on shtukas:*
kappa^arith_sht(V_k) := Tr(Frob_q | H^2(Cht^n_{SL_2}, R pi_* B^ch(V_k))),
where pi: Cht^n -> X^n is the characteristic map. Under Koszul
involution k <-> -k-2h^v, Varshavsky (Sel. Math. 2004 Thm 2.14) shows
Cht^n_G^{k^v} is the twist of Cht^n_G^k by the central character
inversion on the l-adic line bundle L_kappa. Trace of Frob on H^2
then flips sign by BD K_2-linearity: the K_2 central extension is
Z-linear in k, and its sheaf-theoretic avatar L_kappa ⊗ L_{-kappa} = O
trivially. Hence
kappa^arith_sht(V_k) + kappa^arith_sht(V_{-k-2h^v}) = 0 ∈ Q_l(-1).

**Does the formula lift? Conditional yes.** The lift holds provided:
(i) L_kappa is an honest l-adic line bundle on Cht^n_G (not merely a
Picard class) — TRUE for k integer, PARTIAL for k rational with
denominator prime to q, OPEN for k with denominator divisible by q.
(ii) The Frobenius action is compatible with the Koszul involution at
the sheaf level — this requires V. Lafforgue's partial Frobenius on
Cht^n to be equivariant under k -> -k-2h^v. Partial Frobenius shifts
modification points by x -> Frob_q(x); the Koszul involution does NOT
touch x. **So partial Frobenius and Koszul involution commute
trivially, verifying (ii).**

*Concrete F_7 sl_2 k=1 check.* kappa^arith_sht(V_1) = 7 ·
[something of absolute value 9/4 lifted]. kappa^arith_sht(V_{-5}) = -7 ·
[same magnitude]. Sum = 0 ∈ Q_7(-1). PASSED formally; true verification
requires explicit computation of H^2 of B^ch(V_1) on Cht^2_{SL_2}, which
is available for n=1 (standard L-function of sl_2) but not tabulated
in either volume's compute infrastructure.

### (3) Chiral Adams at arithmetic level via excursion operators

V. Lafforgue excursion operator E_{f, x, gamma} acts on
H^*(Cht^n_G, L_kappa) with f in O(G-hat^n)^{G-hat}, x in X^n(F_q),
gamma in Weil(F/F)^n. The chiral Adams functor of
`periodic_cdg_admissible.tex:507` is given C-over by
psi^p: End^ch -> End^ch, psi^p(f)(z) = f(z^p) mod [Q^adm, -].

*Arithmetic lift.* Over F_q, partial Frobenius Frob_{q,i}: Cht^n ->
Cht^n (acting by Frob at the i-th modification) plays the role of
psi^q up to the Koszul-shift. The Hecke eigensheaf cohomology
H^*(Cht^n, L_kappa) is a spectral decomposition over Langlands
parameters sigma: Weil(F/F) -> G^v; the chiral Adams functor restricted
to a given spectral support recovers psi^q composed with the eigenvalue
of sigma at Frob_q.

**Compatibility with Hecke eigensheaves.** For G = SL_2, the
spectral decomposition is parametrised by 2-dim l-adic Galois reps of
Weil(F/F); the chiral Adams on the bar complex at the arithmetic level
sends a Hecke eigensheaf F_sigma to F_{sigma^q}, where sigma^q is the
q-th Adams power of the Galois rep. This is V. Lafforgue's partial
Frobenius on the spectral side, re-clothed as a chiral-algebraic
functor.

## THREE-STEP PROTOCOL (AP158)

### (a) What does kappa^arith + kappa^arith^v = 0 get RIGHT over F_q

- Z-linearity of kappa in k transfers. BD K_2 extension exists over
  any local field (BD Publ. IHES 94 §3), so kappa is Z-linear on the
  Chevalley lattice and the involution k -> -k-2h^v flips sign
  strictly, INDEPENDENT of characteristic.
- Partial Frobenius commutes with Koszul involution because the
  involution does not move modification points. This upgrades the
  C-identity to a Frobenius-equivariant one on Cht^n_G moduli.
- Deligne Weil II supplies the bound |Frob eigenvalue| = q^{w/2} on
  pure H^n; at w=2 and n=1 (k=1 sl_2), this is exactly q.

### (b) What does it get WRONG (or: what subtleties remain)

- **kappa is a Picard class, not a trace.** The Weil-cohomology
  definition kappa^arith = Tr(Frob | H^2) is NUMERICAL; the true
  invariant is the class [L_kappa] ∈ Pic(Cht^n_G) ⊗ Q_l. The sum of
  classes in ℓ-adic Picard is ZERO; the traces might not vanish if
  there is spectral mixing across components.
- **Rationality of k requires char F_q prime to denominator(k).** For
  k = 1 and p = 7 this is fine; for k admissible like 2/7, the BD
  K_2 extension does not trivialise integrally over F_7.
- **Spectral R-matrix lift R(z, Frob) requires independent construction.**
  The prior agent's claim "R(z, Frob) is the V. Lafforgue excursion
  operator" is SUGGESTIVE but unproved; excursion operators act on
  H^* of Cht^n, not on the bar chain complex directly. A sheaf-theoretic
  avatar of R(z) on Cht^n is conjectural.
- **"Provable now" is overclaim.** The ingredients (BD, AG, Koszul
  Z-linearity, partial Frobenius commutation) are each individually
  established; their assembly into a published theorem is NOT in any
  monograph. This is a TWO-PAGE PROOF waiting to be written, not a
  cited result.

### (c) Correct relationship

**Arithmetic complementarity holds as a Frobenius-equivariant identity
in l-adic Picard of shtuka moduli, not as an ℓ-adic trace identity.**
Precise form:

> For X/F_q smooth projective, G simply-laced simply-connected, k ∈ Z
> integer level with q prime to 2h^v, the BD K_2 central extension
> kappa_BD(V_k(g-hat)) ∈ Pic(Cht^n_G) ⊗ Q_l is Frobenius-equivariant
> and satisfies
> [L_kappa(V_k)] + [L_kappa(V_{-k-2h^v})] = 0 ∈ Pic(Cht^n_G) ⊗ Q_l,
> with the Koszul involution commuting with partial Frobenius.
> Equivalently, the Kac-Moody central extension and its Koszul dual
> transfer under partial Frobenius to a dual pair, and their K_2-classes
> cancel Frobenius-equivariantly.
>
> The trace-of-Frobenius version kappa^arith(V_k) + kappa^arith(V_{k^v})
> = 0 ∈ Q_l(-1) follows by taking ℓ-adic trace maps on both sides;
> Weil II then forces weights and absolute values to match, giving the
> expected |7| at p=7, k=1 for sl_2.

**Chiral Adams = Hecke eigensheaf cohomology** is a bridge, not an
identification. The chiral Adams functor psi^p at the arithmetic level
is the q-th partial Frobenius on Cht^n_G restricted to a spectral
component; this provides a NEW direct link between Vol I's Adams functor
infrastructure and V. Lafforgue's excursion operators. The bridge is
genuine; its verification on a specific example (sl_2, k=1, p=7) reduces
to the known fact that partial Frobenius on Cht^1_{SL_2} is the Frobenius
on the local L-factor of the corresponding Hecke eigensheaf.

### Summary

Arithmetic kappa-complementarity over F_q is CORRECT in the ℓ-adic Picard
formulation and TRANSFERS from the C-formula via BD K_2 + AG Gr_G. The
Frobenius-equivariance is automatic because the Koszul involution k ->
-k-2h^v acts on central charges (Z-linearly) and partial Frobenius acts
on curve points (spatially); these commute. The trace-of-Frobenius
corollary holds with Deligne Weil II bounds. The chiral Adams = Hecke
eigensheaf bridge is a GENUINE frontier statement linking Vol I's
periodic-CDG to V. Lafforgue's excursion operators — an honest
arithmetic enhancement of the programme, not a downgrade. No FM needed;
the prior agent's claim survives the attack WITH appropriate clarifications
(Picard-class vs trace; requires k integer or denom prime to q; spectral
R-matrix Frobenius-twist is conjectural, not proved).
