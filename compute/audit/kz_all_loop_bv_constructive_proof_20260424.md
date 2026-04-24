# Khan--Zeng BV Quantization: Surviving Core and Conditional All-Loop Package

Date: 2026-04-24

The live theorem repair is in `chapters/connections/affine_half_space_bv.tex`.
The proved core is the shifted-cotangent KZ BV action and the
identification of its classical master equation with the Poisson-vertex
Hamiltonian condition. The nonlinear all-loop theorem is not proved
from finite type and finite jet order alone. Its all-loop extension is a
finite-quotient homological-perturbation recursion conditional on the
analytic SDR package named by `assum:kz-analytic-sdr-package`.

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

The all-loop recursion is valid on finite jet--weight quotients once
the renormalized half-space BV algebra, reflected image-choice Stokes
theorem, quotient-compatible SDR, and harmonic obstruction-vanishing
data are supplied:

```tex
Ob_{\ell,N,w}
=\Delta_{N,w} I_{\ell-1,V,N,w}
+1/2\sum_{a+b=\ell,\ a,b\ge1}
\{I_{a,V,N,w},I_{b,V,N,w}\}_{BV},
\qquad
I_{\ell,V,N,w}=-h_{V,N,w} Ob_{\ell,N,w}.
```

The algebraic proof then uses

```tex
Q^2=0,\quad [Q,\Delta]=0,\quad
\Delta\{F,G\}=\{\Delta F,G\}\pm\{F,\Delta G\},
\quad
\mathrm{id}-H=dh+hd,
\quad
H(Ob_{\ell,N,w})=0.
```

The proof obligation is precisely the analytic package which supplies
the reflected image-choice Stokes theorem, quotient-compatible SDR,
self-image renormalization, and harmonic obstruction vanishing.

Resolution map:

1. `lem:kz-cme-pva-jacobi`: `ProvedHere`; the classical KZ BV action
   satisfies CME exactly when the PVA Hamiltonian operator satisfies
   skew-symmetry and Jacobi.
2. `thm:doubling-rwi`: conditional on the image-choice half-space
   compactification, field-parity signs, self-image renormalization,
   and orientation-compatible Stokes pushforward.
3. `prop:kz-all-loop-counterterm-recursion`: conditional finite-quotient
   HPL recursion under `assum:kz-analytic-sdr-package`.
4. `thm:general-half-space-bv`: conditional under the same KZ analytic
   SDR package.
5. The affine lane remains `ProvedHere` by the mixed BF/Chern--Simons
   one-loop-exact calculation; the nonlinear finite-jet PVA lane stays
   fenced until the analytic SDR package is proved.
