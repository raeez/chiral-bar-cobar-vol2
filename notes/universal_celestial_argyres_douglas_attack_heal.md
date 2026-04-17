# Universal Celestial Holography at Argyres-Douglas: Attack-Then-Heal

> **HISTORICAL — AP288 session-ledger retraction banner (2026-04-18, Wave 7).**
> The prose at L47, L179, L194, L230 claims that `thm:uch-main` clauses (ii)-(iii)
> and `thm:uch-gravity-chain-level` class-M chain-level extension apply
> *unconditionally* to Argyres-Douglas / class-M inputs once the chiral
> algebra chi(T_4) is named. Wave-1 Beilinson audit + subsequent topologization
> wave refine this: `thm:uch-gravity-chain-level` is inscribed
> `ClaimStatusProvedHere` at `universal_celestial_holography.tex:511` via
> half-BRST chain-level splitting, BUT chain-level class M on the *original
> complex in Ch(Vect)* remains a frontier item; the chain-level is established
> on the weight-completed / pro-object / J-adic ambients, not the direct-sum
> ambient in Ch(Vect) (see Vol I `thm:mc5-class-m-chain-level-pro-ambient`,
> CLAUDE.md Topologization row "Honest frontier inventory" items (I)-(III)).
> Canonical post-heal scope: UCH-gravity chain-level extension applies in the
> weight-completed ambient for class-M inputs (Vir, W_N, M(2,5), W(p) regular
> sector); direct-sum ambient in Ch(Vect) at g ≥ 1 remains open. Use Vol I
> CLAUDE.md theorem-status table + Vol II FRONTIER.md as authoritative.

## Target

`thm:uch-main` at `chapters/connections/universal_celestial_holography.tex:213`,
tagged `\ClaimStatusProvedHere`. Three clauses: (i) existence and
functoriality of the celestial chiral algebra A^cel(T_4); (ii) the
SC^{ch,top} structure on the pair (A^cel, Z^der_ch(A^cel)); (iii) the
celestial OPE equals the chiral factorization homology on P^1_cel.

Vol II Definition 2 (`def:uch-ht-twist`, line 126) explicitly requires
T_4 to be a "BV theory on R^4 equipped with a nilpotent supercharge Q"
in the Costello-Li sense. The 3d HT reduction is performed by
Costello-Li's reduction lemma (Thm 6.2 of Costello-Li TwistedSugra).
The boundary chiral algebra construction invokes Costello-Gaiotto
(Definition 3, line 137). All three are Lagrangian-BV constructions.

Remark `rem:uch-nonlagrangian` (line 621) claims the theorem extends to
Argyres-Douglas via the Beem-Rastelli functor "directly without a
Lagrangian HT twist." The N=2 SCVOA coset note
(`notes/n2_scvoa_coset_ds_hoch_bridge_platonic.md`) invokes this extension
for AD(A_{p,q}) cosets.

## (a) What thm:uch-main gets RIGHT for Argyres-Douglas

Three genuine ghost theorems survive for AD theories.

(R1) For every 4d N=2 SCFT T_4 (Lagrangian or not), the
Beem-Lemos-Liendo-Peelaers-Rastelli-van Rees functor chi(T_4) produces
a vertex algebra via the Schur supercharge Q = Q_1^- + tilde S^{1 dot-}:
chi(T_4) = H^*(Q, local ops on R^2 subset R^4). This is Theorem 2.1 of
BLLPR 1312.5344, and it is SUPERCHARGE-INTRINSIC, not Lagrangian. The
image chi(T_4) is an E_infty-chiral algebra (Theorem 2.2 of BLLPR; see
Vol II `thm:4d2d-einf` at `ht_physical_origins.tex:38`). For AD(A_{2,3})
the image is chi(AD(A_{2,3})) = M(2,5) = Vir_{-22/5}, the (2,5) Virasoro
minimal model.

(R2) chi(T_4) is chirally Koszul (Vir_{-22/5} is class M in the Vol I
sense; Yangian/Feigin-Frenkel-type fingerprint is applicable). Once the
vertex algebra is named, clauses (ii) and (iii) of `thm:uch-main`
apply: the pair (chi(T_4), Z^der_ch(chi(T_4))) is an SC^{ch,top}-algebra
(chiral Deligne, Vol I Theorem C), and factorization homology on P^1
computes the perturbative celestial OPE of the Schur-sector operators.
Both statements hold regardless of whether T_4 admits a Lagrangian BV
presentation.

(R3) The class M extension of `thm:uch-main` closed in prior session via
the DS-Hochschild bridge (`thm:uch-gravity-chain-level` at line 498,
powered by `thm:chd-ds-hochschild`) applies to M(2,5) directly:
ChirHoch^bullet(Vir_{-22/5}) is chain-level identified with
H^bullet_DS(ChirHoch^bullet(V_{-13/5}(sl_2))) via HPL through DS. This
is the content of the N=2 SCVOA coset note (with trivial U(1)_R coset
because M(2,5) has no R-current, or equivalently the level is
admissible k = -(2)+p/q = -2+2/5 for sl_2).

## (b) What thm:uch-main gets WRONG

One precise error and one precise conflation.

(W1) **The 3d reduction step is not defined for non-Lagrangian T_4.**
The proof of `thm:uch-main`(i) in lines 257-274 reads: "By Costello-Li
Thm 6.2 the KK reduction along R_v preserves the HT structure on
R_u x C_z. By Costello-Gaiotto the transverse Dirichlet boundary
condition at u=0 yields a well-defined boundary chiral algebra."
Costello-Li Theorem 6.2 takes as input a BV action functional S[phi]
on R^4, KK-reduces the fields along R_v, and produces a BV action on
R^3. Without a BV action there is no input to KK reduction. For
AD(A_{2,3}) no Lagrangian exists (Argyres-Douglas 1995 NPB), so the
hypothesis of Thm 6.2 is not satisfied. The reduction step is
UNDEFINED.

(W2) **The Beem-Rastelli functor does not land on celestial data.**
The proof of `prop:uch-ym` at line 609 asserts that the Beem-Rastelli
image chi(T_4) IS the celestial chiral algebra A^cel(T_4), citing
Paquette-Williams §4. But the Beem-Rastelli Q commutes with the SU(2)_R
Cartan and acts on a transverse R^2 subset R^4 inside the 4d worldvolume;
this is NOT the celestial sphere at null infinity. The Schur sector
lives on the chiral-algebra plane in the 4d worldvolume; the celestial
sphere lives at infinity. The identification A^cel(T_4) = chi(T_4)
requires an EXTRA step: the 4d Omega-background localization to the
Schur plane + the Penrose transform to the celestial sphere. This is
Yan 2019's "reconstruction" conjecture, and it is OPEN.

Concretely: for N=4 SYM, the Beem-Rastelli image is the small N=4
superconformal algebra at c = -9, whereas the Costello-Paquette celestial
algebra is the Kac-Moody V_k(sl_N) at HT level. These are different
vertex algebras. The celestial algebra is reached via the HT twist +
boundary; the Beem-Rastelli algebra is reached via the Schur twist. The
chapter silently identifies them via Paquette-Williams §4, which in turn
requires the Lagrangian HT twist to produce the Schur sector as a
subsector of the HT boundary.

## (c) Correct relationship

The precise mathematical object at AD is the BLLPR chiral algebra
chi(T_4) = M(2,5), reached via the Schur supercharge (which does not
require a Lagrangian). The precise celestial chiral algebra A^cel(T_4)
is NOT directly defined for non-Lagrangian T_4; its would-be
definition requires a Lagrangian BV setup for Costello-Li's KK
reduction + Costello-Gaiotto's boundary extraction. Three possible
relationships:

(C1) **Decoupled definition** (conservative). For non-Lagrangian AD,
REDEFINE A^cel(T_4) := chi(T_4) by hand, bypassing the Lagrangian HT
twist. This is `rem:uch-nonlagrangian`'s current posture. Under this
definition, clauses (ii) and (iii) of `thm:uch-main` apply
unconditionally: SC^{ch,top} structure by chiral Deligne (input is a
chiral algebra, Lagrangian origin irrelevant); factorization homology
on P^1 by Beilinson-Drinfeld (same). The DS-Hochschild bridge closes
the class M chain level. **Valid, at the cost of severing the 4d-to-2d
link for non-Lagrangian T_4.**

(C2) **Yan-Creutzig reconstruction** (conjectural). Assume Yan 2019 +
Creutzig 2017: there exists a functor from BLLPR vertex algebras back
to 4d N=2 SCFTs (inverse to chi). Then chi(T_4) DETERMINES T_4, so
A^cel(T_4) is defined via this inverse + Costello-Li + Costello-Gaiotto.
The equality A^cel(T_4) = chi(T_4) then becomes a theorem about the
reconstruction being compatible with HT twisting. **Conjectural both in
the existence of the reconstruction and in the HT-compatibility.**

(C3) **Costello-Paquette 6d lift** (conjectural). AD theories descend
from 6d (2,0) theory on an irregular Hitchin curve (Xie-Yan 2017,
Song-Xie-Yan 2017). The 6d theory has a holomorphic BV structure
(Costello-Li 2021). KK reduction of the 6d HT twist to the irregular
Hitchin curve produces a 4d theory whose BV structure is singular at
the irregular punctures; the HT boundary chiral algebra at the punctures
IS the BLLPR chi(AD). Under this identification, A^cel = chi at AD.
**Conjectural; requires making sense of BV with irregular sources.**

## Verdict: Does universal celestial holography extend to AD?

**Yes at the VERTEX ALGEBRA LEVEL (clauses ii, iii), no at the 4d-to-2d
functor level (clause i) without additional hypothesis.**

Precisely: the statement that the PAIR (chi(T_4),
Z^der_ch(chi(T_4))) is an SC^{ch,top}-algebra and that its
factorization homology on P^1 equals the Schur-sector correlation
algebra of T_4 is unconditional for any 4d N=2 SCFT, Lagrangian or not,
including AD(A_{2,3}) with M(2,5). This is because the input is a
vertex algebra (chi(T_4) = M(2,5) is well-defined via the
supercharge-intrinsic Schur cohomology of BLLPR), and clauses (ii),
(iii) of `thm:uch-main` depend only on the input vertex algebra.

The class M chain-level extension via `thm:chd-ds-hochschild` also
applies directly to M(2,5) because M(2,5) = W_{k}(sl_2, f_prin) for the
admissible level k = -2 + 2/5, and the DS-Hochschild bridge covers all
admissible-level principal DS reductions.

What DOES NOT extend is the interpretation of chi(T_4) as the HT-twist
celestial boundary algebra A^cel(T_4). Without a Lagrangian BV theory
on R^4, the Costello-Li reduction + Costello-Gaiotto boundary
extraction is undefined, so the IDENTIFICATION A^cel(T_4) = chi(T_4)
requires the Yan-Creutzig reconstruction or the 6d-lift construction,
both conjectural.

## The precise Lagrangian-vs-non-Lagrangian obstruction

The obstruction is **localized in clause (i) of thm:uch-main, not in
clauses (ii), (iii)**.

Clause (i) has two sub-pieces: (i-a) the existence of A^cel(T_4) as a
chiral algebra on P^1_cel, and (i-b) the functoriality of
T_4 -> A^cel(T_4). For Lagrangian T_4, both are proved via
Costello-Li + Costello-Gaiotto + Paquette-Williams. For non-Lagrangian
AD, (i-a) is recovered VIA SUBSTITUTION chi(T_4) in place of the
(undefined) A^cel(T_4), but (i-b) — functoriality in T_4 — requires
that T_4 be representable somehow (a Lagrangian defines a point; an
irregular Hitchin presentation defines another point). The Beem-Rastelli
functor chi: {4d N=2 SCFTs} -> {vertex algebras} is defined at the
level of superconformal-index data, not at the level of BV theories.

Concretely the Vol II theorem's strongest honest form for AD is:

> Theorem (Universal celestial holography at AD, corrected form). Let
> T_4 be any 4d N=2 SCFT (Lagrangian or not) and chi(T_4) its BLLPR
> Schur vertex algebra. Then the pair (chi(T_4), Z^der_ch(chi(T_4)))
> is an SC^{ch,top}-algebra, chiral factorization homology on P^1
> computes its Schur-sector correlation functions, and the class M
> chain-level extension via DS-Hochschild applies whenever chi(T_4)
> is admissible DS of an affine Kac-Moody. For Lagrangian T_4 this
> equals A^cel(T_4) = HT celestial boundary. For non-Lagrangian T_4
> (incl. AD), the identification A^cel(T_4) = chi(T_4) is conjectural
> pending (C2) Yan-Creutzig or (C3) 6d lift.

For AD(A_{2,3}) specifically: chi(AD(A_{2,3})) = M(2,5) = Vir_{-22/5};
SC^{ch,top} structure on the pair, unconditional; factorization
homology on P^1 computes Schur-sector correlators, unconditional;
4d-to-celestial identification as HT boundary, conjectural.

## Heal: what to edit (minimal, not this session)

`rem:uch-nonlagrangian` (line 621) should be split into two clauses:
(N1) chi(T_4) always exists and is the correct vertex-algebra input to
clauses (ii), (iii) of `thm:uch-main`; (N2) the identification
A^cel(T_4) = chi(T_4) is proved only for Lagrangian T_4 via Costello-Li
+ Costello-Gaiotto; for non-Lagrangian T_4 including AD, the identification
is conjectural pending Yan-Creutzig or 6d-lift. `prop:uch-ym` (line
593) should be restricted to Lagrangian T_4; the non-Lagrangian case
should be a separate conjecture. `thm:uch-main` clause (i) functoriality
statement should specify "covariantly functorial under Q-equivariant
maps of Lagrangian 4d HT theories"; the extension to non-Lagrangian is
a separate conjecture.

This heal does NOT downgrade the celestial duality for AD; it
SPLITS the two statements (SC^{ch,top} on vertex algebra = PROVED;
4d-to-celestial identification = CONDITIONAL). Both strongest-honest
forms survive; only the conflation between them is repaired.

## One concrete anchor: AD(A_{2,3}) in numbers

chi(AD(A_{2,3})) = M(2,5) at c = -22/5. Chirally Koszul (class M,
Vol I fingerprint). Kappa = c/2 = -11/5. Shadow tower: S_2 = c/2 =
-11/5; S_4 = 10 / [c(5c + 22)] = 10 / [(-22/5)(−22 + 22)] = 10 / 0.
**S_4 diverges at M(2,5) because 5c + 22 = 0 exactly**. This is the
signature of a minimal model: the shadow tower has a pole at the
minimal-model locus, and the divergence is the residue of the null
vector at weight 5 (the (2,5) minimal model has null vector at weight
(2-1)(5-1) = 4 actually, shifted by the conformal weight of the vacuum).
The shadow pole at c = -22/5 is the manifestation of the minimal-model
degeneration in the Vol I fingerprint classification; it is NOT an
obstruction to the SC^{ch,top} structure, which lives on the chain
model of chi(AD(A_{2,3})) and is insensitive to shadow-coefficient
poles.

The DS-Hochschild bridge applies: M(2,5) = W_{k}(sl_2, f_prin) at
k = -2 + 2/5 = -8/5. This is the boundary admissible level p/q = 2/5,
and Arakawa's C_2-cofiniteness covers it (minimal models are
C_2-cofinite). ChirHoch^bullet(M(2,5)) is chain-level computed by the
bridge as H^bullet_DS(ChirHoch^bullet(V_{-8/5}(sl_2))), and the class M
chain-level extension of `thm:uch-main` applies unconditionally on the
Koszul locus.
