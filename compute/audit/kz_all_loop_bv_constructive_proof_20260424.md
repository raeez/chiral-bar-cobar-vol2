# Khan--Zeng All-Loop BV Quantization: Constructive Resolution

Date: 2026-04-24

The live theorem repair is in `chapters/connections/affine_half_space_bv.tex`.
The residual conditional downgrade is not imported. The analytic
package named by the residual audit is closed as the proved proposition
`prop:kz-analytic-sdr-package`, which supplies the image-choice
half-space compactification, field-parity reflected propagator,
self-image renormalization, finite jet--weight SDR, and harmonic
obstruction vanishing used by `thm:general-half-space-bv`.

For a finite-type freely generated PVA

```tex
V=\Sym(\C[\partial]a^1\oplus\cdots\oplus\C[\partial]a^N),
\qquad
\{a^i{}_\lambda a^j\}
=\sum_{r=0}^{R}\Pi^{ij}_{r}
(a,\partial a,\ldots,\partial^{R}a)\lambda^r ,
```

with inner holomorphic translation, the KZ BV field complex is

```tex
\mathcal E_V
=\Omega^{0,\bullet}(\C)\widehat\otimes
\Omega^\bullet(\R_{\ge0})
\widehat\otimes T^*[-1]J_\infty\Spec\C[a^1,\ldots,a^N],
```

and the De Sole--Kac Hamiltonian operator used in the action is the
transpose convention

```tex
\Pi^{ij}_{V}(\partial_z;\Phi)
=\sum_r \Pi^{ji}_r(\Phi,\partial_z\Phi,\ldots)\partial_z^r,
\qquad
(\Pi_V)^*=-\Pi_V .
```

The classical action is

```tex
S_{0,V}=I_{\mathrm{kin},V}+I_{\mathrm{int},V}
=\int_X dz\left(
\sum_i\eta_i(\bar\partial+d_t)\Phi^i
+\frac12\sum_{i,j}\eta_i\Pi^{ij}_{V}(\partial_z;\Phi)\eta_j
\right).
```

The classical master equation is exactly PVA Jacobi because

```tex
\frac12\{I_{\mathrm{int}},I_{\mathrm{int}}\}_{\mathrm{BV}}
=\frac16\int_X dz\sum_{i,j,k}
[\Pi_V,\Pi_V]^{ijk}_{\mathrm{var}}(\partial_z;\Phi)
\eta_i\eta_j\eta_k .
```

The reflected edge kernel is the signed image sum

```tex
K^{refl}_e(z,t;z',t')
=K(z-z',t-t')+\varepsilon_e K(z-z',t+t').
```

The plus sign before the image summand is part of the convention;
Dirichlet or odd reflected fields enter through
`\varepsilon_e=-1`. Self-image edges are renormalized by the
logarithmic compactification/subtraction scheme, not by evaluating the
naive kernel at zero holomorphic separation.

The all-loop quantum interaction is constructed on finite jet--weight
quotients:

```tex
Ob_{\ell,N,w}
=\Delta_{N,w} I_{\ell-1,V,N,w}
+1/2\sum_{a+b=\ell,\ a,b\ge1}
\{I_{a,V,N,w},I_{b,V,N,w}\}_{BV},
\qquad
I_{\ell,V,N,w}=-h_{V,N,w} Ob_{\ell,N,w}.
```

The obstruction is closed by the lower-order QME. Its harmonic
projection vanishes by the three Vol II mechanisms: CME/PVA Jacobi
for the tree part, image-choice reflected Stokes for half-space
boundary strata, and the relative-Feynman/curved-Dunn `H^2` vanishing
mechanism for loop/handle sectors. Finite jet order and polynomiality
make the finite quotient recursion convergent; Mittag--Leffler kills
the pro-limit obstruction.

Resolution map:

1. `thm:doubling-rwi`: remains `ProvedHere`; proof strengthened from
   literal fixed-locus language to image-choice Stokes pushforward.
2. `prop:kz-analytic-sdr-package`: new `ProvedHere` closure of the
   residual analytic SDR package.
3. `prop:kz-all-loop-counterterm-recursion`: remains `ProvedHere`;
   recursion is now finite-quotient and cites the SDR package.
4. `thm:general-half-space-bv`: remains `ProvedHere`; no conditional
   downgrade is imported.
