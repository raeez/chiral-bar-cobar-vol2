# Khan--Zeng BV Quantization: Surviving Core and Open Analytic Package

Date: 2026-04-24

The adversarial repair converged to a smaller true theorem.  The
classical shifted-cotangent KZ BV action is constructed in
`chapters/connections/affine_half_space_bv.tex`, and its classical
master equation is equivalent to the PVA Hamiltonian condition.  The
nonlinear all-loop QME theorem is not proved from finite type and
finite jet order alone; it is a finite-quotient HPL recursion
conditional on the analytic SDR package now named
`assum:kz-analytic-sdr-package`.

For a finite-type freely generated PVA

```tex
V=\Sym(\C[\partial]a^1\oplus\cdots\oplus\C[\partial]a^N),
\qquad
\{a^i{}_\lambda a^j\}
=\sum_{r=0}^{R}\Pi^{ij}_{r}
(a,\partial a,\ldots,\partial^{R}a)\lambda^r ,
```

the De Sole--Kac Hamiltonian matrix convention used in the action is

```tex
\Pi^{ij}_{V}(\partial_z;\Phi)
=\sum_r \Pi^{ji}_r(\Phi,\partial_z\Phi,\ldots)\partial_z^r,
\qquad
(\Pi_V)^*=-\Pi_V .
```

The classical action is split as

```tex
S_{0,V}=I_{\mathrm{kin},V}+I_{\mathrm{int},V},
\qquad
Q=\{I_{\mathrm{kin},V},-\}_{BV}=\bar\partial+d_t .
```

The classical master equation is

```tex
\frac12\{S_{0,V},S_{0,V}\}_{BV}=0
```

and this is equivalent to PVA skew-symmetry and Jacobi because, in the
local-functional quotient by total derivatives,

```tex
\frac12\{I_{\mathrm{int},V},I_{\mathrm{int},V}\}_{BV}
=\frac16\int_X dz\sum_{i,j,k}
[\Pi_V,\Pi_V]^{ijk}_{\mathrm{var}}(\partial_z;\Phi)
\eta_i\eta_j\eta_k .
```

The all-loop recursion is valid on each finite quotient once the
renormalized half-space BV algebra, reflected image-choice Stokes
theorem, quotient-compatible SDR, and harmonic obstruction-vanishing
data are supplied:

```tex
Ob_{\ell,N,w}
=\Delta_{N,w} I_{\ell-1,N,w}
+1/2\sum_{a+b=\ell,\ a,b\ge1}
\{I_{a,N,w},I_{b,N,w}\}_{BV},
\qquad
I_{\ell,N,w}=-h_{V,N,w}Ob_{\ell,N,w}.
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

Thus the hidden structure is not an unconditional nonlinear all-loop
KZ theorem.  It is:

1. proved classical KZ BV/CME = PVA Jacobi;
2. proved finite-quotient HPL recursion under explicit SDR/anomaly
   hypotheses;
3. proved affine all-loop theorem by the mixed BF/Chern--Simons
   one-loop-exact calculation;
4. open nonlinear analytic package: field-parity reflected propagator,
   self-image renormalization, image-choice FM/raviolo compactification,
   reflected Stokes pushforward, and harmonic obstruction vanishing.
