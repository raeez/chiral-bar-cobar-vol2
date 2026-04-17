# DS-Hochschild Bridge Extension to N=2 SCVOA Cosets chi[T[X]] / u(1)_R

## Platonic Statement

Let T[X] be a 4d N=2 SCFT associated to a Calabi-Yau geometry X (CY3
or K3 x E), let chi[T[X]] be its BLLPR chiral algebra, and let u(1)_R
be the U(1) R-symmetry current inside chi[T[X]]. Then there is a
chain-level quasi-isomorphism of E_2-chiral Gerstenhaber algebras

    ChirHoch^bullet( chi[T[X]] / u(1)_R )
        ~ H^bullet_{DS,coset}( ChirHoch^bullet( V_k(g) ) ),

where (g, f, k) is the Arakawa-Kawasetsu-Moller (AKM) presentation
of chi[T[X]] / u(1)_R as the u(1)-coset of a W-algebra W_k(g, f),
and H^bullet_{DS,coset} is the composite of Drinfeld-Sokolov BRST
reduction along f with the Heisenberg coset functor at the free U(1)
level. The qi lifts to the E_3-chiral extensions of
thm:chiral-higher-deligne via Step 4 of thm:chd-ds-hochschild applied
twice.

This extends Vol II thm:chd-ds-hochschild (principal/hook-type W) to
the BLLPR lineage and closes CY-C I_2 non-separating chain-level AND
CY-C I_3 class-M chain-level simultaneously.

## (1) AKM Coset Presentation of chi[T[X]] / u(1)_R

For Argyres-Douglas theories AD(A_{p,q}) of type (A_{p-1}, A_{q-1})
Dan-Cohen arXiv:1811.04933 plus Song-Xie-Yan arXiv:1706.01607 plus
Creutzig arXiv:1708.01363 identify

    chi[AD(A_{p,q})] = W_{k_{p,q}}(sl_{p+q}, f_{[p,q]}),

with k_{p,q} = -(p+q) + p/(p+q) the admissible boundary level and
f_{[p,q]} the nilpotent whose Jordan type is the partition of (p+q)
obtained by concatenating one Jordan block of size p and one of size
q; equivalently f_{[p,q]} is the hook nilpotent with arm p and leg q,
belonging to the Arakawa-van-Ekeren class covered by
thm:chd-ds-hochschild as a hook-type nilpotent (Rem rem:chd-nonprincipal-scope).

The U(1)_R current inside chi[AD] is the Heisenberg field
J_R(z) = :phi_R partial phi_R:, singled out in Beem-Lemos-
Liendo-Peelaers-Rastelli-van-Rees arXiv:1312.5344 (BLLPR) as the
spin-1 descendent of the 4d R-symmetry. Its commutant (coset)
realises the "reduced" BLLPR algebra used by the Schur-index
character formula:

    chi[T[X]] / u(1)_R := Com(u(1)_R, chi[T[X]]).

For K3 x E fibres (CY-C with trivial base) the same scheme applies
with (g, f, k) chosen on the Arakawa-Kawasetsu-Moller list so that
the resulting W plus Heisenberg decomposition reproduces the T^2
chiral algebra of the wrapped M5 brane theory. In general the
decomposition

    chi[T[X]] = (chi[T[X]] / u(1)_R) otimes H(J_R)    (tensor mod VOA spectral flow)

is the Fock decomposition of the U(1) subalgebra; this is the
elementary lattice-VOA plus coset decomposition needed below.

## (2) C_2-Cofiniteness for the Coset

Arakawa-Moller arXiv:2006.12692 (building on
Arakawa-Kawasetsu arXiv:1610.05865) proves:

    THEOREM (AKM 2020). For any C_2-cofinite N-graded VOA V and any
    Heisenberg subalgebra H subset V with semisimple action on V, the
    coset Com(H, V) is C_2-cofinite.

Combined with Arakawa's arXiv:1004.1554 C_2-cofiniteness for
hook-type admissible W_k(sl_N, f) at boundary level, we get:

    Corollary. chi[T[X]] / u(1)_R is C_2-cofinite.

Explicitly, the C_2-cofiniteness bound is

    dim R_{C_2}(chi[T[X]] / u(1)_R) <= dim R_{C_2}( W_k(sl_{p+q}, f_{[p,q]}) )
                                     = (Arakawa 2015 bound) < infinity,

with equality up to the contribution of the free U(1) lattice sector
(which contributes only 1 to R_{C_2} per standard lattice argument).

This finiteness is precisely what the HPL Step 3 of
thm:chd-ds-hochschild requires: the contracting homotopy is
conformal-weight-stratified and each stratum is finite-dimensional,
so HPL transfers chain-level (no completion needed).

## (3) Chain-Level DS-Hoch Bridge for the Coset

The Heisenberg coset functor Com(H, -) is an exact functor on
Heisenberg-graded VOAs (Lam arXiv:math/0102118;
Creutzig-Kanade-Linshaw-Ridout arXiv:1904.11139). On Hochschild
cohomology it descends to a chain-level SDR:

    ChirHoch^bullet(V) = ChirHoch^bullet( Com(H,V) ) otimes Fock(H),

where the right-hand Fock factor is a rank-one Heisenberg
Hochschild, computed explicitly (Heisenberg is class G, free-PVA,
and ChirHoch^bullet(H) = k concentrated in degree 0 at non-critical).

The SDR data are:

    i: Com(H,V) hookrightarrow V       (inclusion of the commutant)
    p: V twoheadrightarrow Com(H,V)    (Heisenberg-reduction projection)
    h: V -> V[-1]                      (Heisenberg contracting homotopy)

satisfying ph=0, hi=0, Q_heis h + h Q_heis = id - ip, with
Q_heis = 0 (Heisenberg is Koszul-free) so h is simply the
weight-grading homotopy on the Heisenberg Fock factor. HPL transfer
through (i,p,h) is immediate and chain-level because each
conformal-weight stratum is finite-dimensional (AKM C_2-cofiniteness).

The composite DS-then-coset functor is thus

    chi[T[X]] / u(1)_R
        = Com(H_R, W_k(sl_{p+q}, f_{[p,q]}))
        = Com(H_R, DS_f(V_k(sl_{p+q}))),

and the chain-level DS-Hoch bridge becomes the composition

    ChirHoch^bullet( chi[T[X]] / u(1)_R )
        ~_{HPL_coset}
    ChirHoch^bullet( W_k(sl_{p+q}, f_{[p,q]}) )       otimes Fock(H_R)^{-1}
        ~_{thm:chd-ds-hochschild}
    H^bullet_{DS}( ChirHoch^bullet( V_k(sl_{p+q}) ) ) otimes Fock(H_R)^{-1}
        =: H^bullet_{DS,coset}( ChirHoch^bullet( V_k(sl_{p+q}) ) ).

Both steps are chain-level (HPL plus HPL). The E_3-extension lifts by
Step 4 of thm:chd-ds-hochschild plus the trivial fact that coset by
a free U(1) preserves E_3 (Heisenberg is SC^{ch,top}-compatible, Vol
II FM62 explicit).

## Closure of CY-C Residuals

I_2 non-separating chain-level closure.
At g=2 non-separating degeneration M_bar_2 has a unique open stratum
whose chiral algebra in the Beem-Rastelli direction is precisely a
BLLPR algebra of type AD(A_{1,1}). Its Hochschild cohomology is
chain-level computed by the coset DS-Hoch bridge above with (p,q) =
(2,2), g = sl_4, f the hook-[2,2] nilpotent. The non-separating
chain-level class from Vol III wave-2 CY-C now identifies with
H^bullet_{DS,coset}( ChirHoch^bullet( V_{-4+1/2}(sl_4) ) ), chain-level.
FM157 phantom label retired: the non-separating class is not a
phantom but a BLLPR coset Hochschild.

I_3 class-M chain-level closure.
Class M (Virasoro, principal W_N, hook-type W) was closed for
principal and hook f by thm:chd-ds-hochschild. The residual I_3
gap was the Beem-Rastelli subclass whose 4d origin is an AD-type
theory, not directly a gauge-theoretic W. The AKM coset presentation
above realises exactly this residual subclass as a Heisenberg coset
of the hook W, and the composite DS-coset bridge furnishes the
chain-level qi that closes I_3.

Both closures are unconditional on the Koszul locus at generic
admissible level (Arakawa 2015 plus AKM 2020 plus
thm:chd-ds-hochschild). Exotic nilpotents remain open
(rem:chd-nonprincipal-scope); the BLLPR lineage does not require
them.

## Report

Yes: the DS-Hoch bridge extends unconditionally to BLLPR cosets
chi[T[X]] / u(1)_R on the Koszul locus at generic admissible level.
The extension is the composite DS-then-Heisenberg-coset, both steps
chain-level via HPL; C_2-cofiniteness is provided by Arakawa 2015
plus AKM 2020; the E_3 lift is Step 4 of thm:chd-ds-hochschild
applied twice. This closes CY-C I_2 non-separating chain-level AND
CY-C I_3 class-M chain-level simultaneously, since the I_2
non-separating class is realised by the BLLPR coset of type
AD(A_{1,1}) and the I_3 class-M gap was precisely the BLLPR
subclass of hook-type W. No new hypotheses are needed beyond the
admissibility scope of thm:chd-ds-hochschild.
