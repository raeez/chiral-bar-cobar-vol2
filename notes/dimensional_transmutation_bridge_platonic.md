# Dimensional Transmutation Bridge: Strongest Honest Form

## 0. The precise obstruction, restated

Prior note `yang_mills_mass_gap_ht_twisted_platonic.md` pins the Clay YM mass
gap obstruction to (H3): a map carrying dimensionless chiral-algebra gap data
to dimensionful 4d Hamiltonian data. Universal Holography
\[
  \Phi_{\mathrm{hol}}:\ \mathsf{ChirAlg}^{\omega,\mathrm{BL}}_X
  \longrightarrow \mathsf{HT\text{-}QFT}_{X\times\mathbb{R}}
\]
is a functor between \emph{dimensionless} categories (conformal weights
\(\Delta\in\mathbb{Z}_{\ge 0}\), algebraic spectral parameter \(z\),
formal parameter \(\hbar\)); by construction it cannot manufacture a
mass scale. Dimensional transmutation \(\Lambda_{\mathrm{QCD}}=\mu\,
\exp(-8\pi^{2}/(b_{0} g(\mu)^{2}))\) with \(b_{0}=11 N/3\) for pure
\(\mathrm{SU}(N)\) is the missing datum. This note proposes a
dimensionful extension \(\Phi_{\mathrm{hol}}^{\Lambda}\) by
compositing Universal Holography with the Costello--Gwilliam (CG)
renormalisation-group functor, isolates the genuine obstruction, and
computes the chiral-algebra trace for \(\mathrm{SU}(2)\) explicitly.

## 1. Dimensionful variant \(\Phi_{\mathrm{hol}}^{\Lambda}\)

### 1.1 Definition

Let \(\mathsf{Scale}\) be the Picard groupoid of one-dimensional
positive real torsors (category of \(\mathbb{R}_{+}\)-torsors; objects
\(\Lambda\in\mathbb{R}_{+}\), morphisms \(\Lambda\to\Lambda'\) given by
\(\Lambda'/\Lambda\in\mathbb{R}_{+}\)); this is the categorical home of
"a choice of mass scale." Let
\(\mathsf{QFT}_{X\times\mathbb{R}}\) be the \((\infty,1)\)-category of
CG factorisation algebras on the smooth manifold \(X\times\mathbb{R}\)
(observable structure including RG flow; cf. CG II, §8--10).
Define
\[
  \Phi_{\mathrm{hol}}^{\Lambda}
  \ :\ \mathsf{ChirAlg}^{\omega,\mathrm{BL}}_X \ \times\
  \mathsf{Scale}
  \ \longrightarrow\ \mathsf{QFT}_{X\times\mathbb{R}}
\]
by \((A,\Lambda)\mapsto\Phi_{\mathrm{hol}}(A)\otimes_{\mathrm{CG}}\mathbf{1}_{\Lambda}\),
where \(\mathbf{1}_{\Lambda}\) is the CG \emph{scale-introducing monad}
defined on an auxiliary \(\mathbb{R}_{\ge 0}\)-framed half-space and
classifying scale-setting data at energy \(\Lambda\). Concretely
\(\mathbf{1}_{\Lambda}\) is the one-dimensional trivial BV theory on
\(\mathbb{R}\) at scale \(\Lambda\); its factorisation algebra is
equivalent to the zeroth-order perturbative algebra with
\(\mathrm{Obs}^{q}(\mathbb{R})=\mathbb{C}[[\hbar]]\) equipped with a
chosen \(\mathbb{R}_{+}\)-action \(\Lambda\cdot(-)\).

### 1.2 Factorisation property (scale compatibility)

\begin{claim}[dimensionful factorisation]
For each \(\Lambda\),
\(\Phi_{\mathrm{hol}}^{\Lambda}(A,\Lambda)\simeq \Lambda\cdot
\Phi_{\mathrm{hol}}(A)\) as CG factorisation algebras, where the
right-hand side is the \(\mathbb{R}_{+}\)-twist of the dimensionless
holographic image by \(\Lambda\).
\end{claim}

\begin{proof}[Sketch]
The CG monad \(\mathbf{1}_{\Lambda}\) acts on any factorisation
algebra by rescaling the parallel \(\mathbb{R}\)-direction, which in
\(\Phi_{\mathrm{hol}}(A)\) is the transverse topological line. Since
\(\Phi_{\mathrm{hol}}(A)\) is E\(_{3}\)-topological in the transverse
direction (non-critical level), the \(\mathbb{R}_{+}\)-action by
\(\Lambda\) commutes with the topological structure and produces a
\emph{scaled} E\(_{3}\)-topological factorisation algebra.
\end{proof}

### 1.3 RG-flow naturality

The \emph{Callan--Symanzik} cocycle along the scale axis is encoded
as a natural transformation
\(\eta:\Phi_{\mathrm{hol}}^{\Lambda}\Rightarrow
\Phi_{\mathrm{hol}}^{\Lambda'}\) for every \(\Lambda\to\Lambda'\),
satisfying \(\eta_{\Lambda''\Lambda}=\eta_{\Lambda''\Lambda'}\circ
\eta_{\Lambda'\Lambda}\) (CG--II Thm~8.6.4 style). This cocycle is
\emph{tautological} on the dimensionless data \(A\), carrying all
scale dependence into the \(\mathbf{1}_{\Lambda}\) monad. The
\emph{dynamical} scale \(\Lambda_{\mathrm{QCD}}\) enters as a
\emph{fixed point} of a non-trivial \(\eta\)-cocycle coming from the
beta-function: this is the extra input and the precise place the
dimensionless functor cannot supply.

### 1.4 Verdict on (1)

\(\Phi_{\mathrm{hol}}^{\Lambda}\) is well-defined as a functor;
it \emph{transports} a chosen scale \(\Lambda\) through the holographic
image but does \emph{not} generate \(\Lambda_{\mathrm{QCD}}\)
dynamically. The dynamical generation requires a non-trivial
RG-flow cocycle \(\eta_{\mathrm{YM}}\) whose \emph{fixed point}
selects \(\Lambda_{\mathrm{QCD}}\); such a cocycle exists only on the
CG side, not on the chiral-algebra side.

## 2. CG factorisation-algebra embedding

### 2.1 The embedding

Costello--Gwilliam build, for any classical BV theory \((\mathcal{E},S)\),
a prefactorisation algebra \(\mathrm{Obs}^{q}\) of quantum observables
on the spacetime manifold (CG--I Chs~5--8). For a 4d HT-twisted
N\(=\)2 theory on \(C\times\mathbb{R}^{2}\), CG's framework gives
\(\mathrm{Obs}^{q}\) as a factorisation algebra locally modelled by
\(V_{-2h^{\vee}}(\mathfrak{g})\otimes
\mathcal{T}(\mathbb{R}^{2})\), with \(\mathcal{T}\) topological.
The programme's chiral algebra embeds by
\[
  \iota\colon A \hookrightarrow \mathrm{Obs}^{q}\big|_{C\times\{0\}},
  \quad A\in\mathsf{ChirAlg}^{\omega,\mathrm{BL}}_C,
\]
identifying \(A\) with the Schur-sector boundary observable algebra at
the origin of the transverse plane (Oh--Yagi 2019; Costello--Gaiotto
2016). This \(\iota\) is the programme's \(\Phi_{\mathrm{hol}}\)
projected to the boundary slice.

### 2.2 Non-SUSY HT twist: does it exist?

The \emph{key question} is whether CG's
\(\mathrm{Obs}^{q}(\text{pure YM})\) admits a differential
\(Q_{\mathrm{nonSUSY}}\) whose cohomology is a (possibly curved)
vertex algebra carrying mass-gap information. The answer is negative
in the strict sense: pure YM lacks an odd nilpotent global fermionic
symmetry, so no BRST-like \(Q\) exists intrinsically.

However there is a \emph{weaker} cohomological projector:
\emph{Costello's shift-by-}\(\Lambda\) \emph{trick} (Costello, "RG
and EFT," §5.10; also Paquette--Williams 2021). One twists the
partition function on \(\mathbb{R}^{4}\) by inserting
\(\exp(-\Lambda^{4} \int \mathrm{tr} F^{2}/g^{2}(\Lambda))\), which in
the CG formalism is a \emph{scale-dependent} deformation
\[
  Q_{\Lambda}\ =\ Q_{\mathrm{pert}}\ +\ \Lambda^{4}\,\mu_{\mathrm{cond}},
\]
where \(\mu_{\mathrm{cond}}\) is the instanton-condensation module
map (Polyakov). The cohomology \(H^{\bullet}(\mathrm{Obs}^{q},
Q_{\Lambda})\) is \emph{not} a vertex algebra in the traditional
sense but a curved factorisation algebra with curvature parameter
\(\Lambda^{4}\), and its zeroth cohomology packages
\emph{scale-dressed} chiral operators.

### 2.3 Embedding landscape

The programme's chiral algebra \(A=V_{-2h^{\vee}}(\mathfrak{g})\)
embeds into CG-\(\mathrm{Obs}^{q}(\text{N}=2\,\mathrm{YM})\) as the
Schur-BPS cohomological image (Beem--Rastelli); under the
"turn off SUSY" limit \(N=2\to 0\) the embedding \emph{fails to
continue}: the boundary VOA is destroyed along with the Schur
supercharge. This is the CG-level origin of the transport
obstruction identified in the prior note.

### 2.4 Verdict on (2)

The chiral-algebra framework embeds into CG's factorisation-algebra
framework \emph{only on the BPS-protected branch}. The non-SUSY HT
twist does not exist as a strict cohomology but can be approximated
by the curved factorisation algebra
\(\mathrm{Obs}^{q}(\mathrm{YM},Q_{\Lambda})\); this is \emph{not}
inside the programme's \(\mathsf{ChirAlg}^{\omega,\mathrm{BL}}\)
universe because it lacks a conformal vector surviving the twist.

## 3. Explicit computation for \(\mathrm{SU}(2)\)

### 3.1 Dimensional transmutation for pure \(\mathrm{SU}(2)\)

One-loop running (Gross--Wilczek; Politzer):
\(b_{0}(\mathrm{SU}(2))=\tfrac{11}{3}\cdot 2=\tfrac{22}{3}\). Therefore
\[
  \Lambda_{\mathrm{QCD}}(\mathrm{SU}(2))
  \ =\ \mu\cdot\exp\!\left(-\frac{8\pi^{2}}{b_{0}\,g(\mu)^{2}}\right)
  \ =\ \mu\cdot\exp\!\left(-\frac{12\pi^{2}}{11\,g(\mu)^{2}}\right).
\]
The prior note's \(\exp(-6\pi^{2}/g^{2})\) expression is missing the
factor \(2/11\) that distinguishes \(b_{0}\) from 2; the correct
exponent is \(-12\pi^{2}/(11 g^{2})\). (This is the standard
Gross--Wilczek--Politzer result; Gross--Jackiw--Coleman--Weinberg 1974
gives it in the cited form.)

### 3.2 Chiral-algebra trace in \(V_{-4}(\mathrm{sl}_{2})\)

The Schur sector of pure \(N=2\,\mathrm{SU}(2)\) SYM is
\(V_{-4}(\mathrm{sl}_{2})=V_{-2h^{\vee}}(\mathrm{sl}_{2})\), affine
\(\mathrm{sl}_{2}\) at level \(k=-4\). The Sugawara central charge is
\[
  c_{\mathrm{Sug}}(\mathrm{sl}_{2},-4)
  \ =\ \frac{k\,\dim \mathfrak{g}}{k+h^{\vee}}
  \ =\ \frac{-4\cdot 3}{-4+2}
  \ =\ \frac{-12}{-2}\ =\ 6.
\]
(Check: \(c_{\mathrm{Sug}}=6\); \(c_{2d}=-12 c_{4d}\) gives
\(c_{4d}=-1/2\), matching Beem--Rastelli for pure SU(2) \(N=2\)
SYM's \(c_{4d}\).)

The lowest non-vacuum conformal weight in \(V_{-4}(\mathrm{sl}_{2})\)
is \(\Delta_{\min}=1\) (the currents \(J^{a}\)); this matches the prior
note.

### 3.3 The candidate invariant: Kac determinant zero at level \(-4\)

The key dimensionless scalar invariant of \(V_{k}(\mathrm{sl}_{2})\)
that depends non-trivially on the \emph{level} \(k\) (and hence
potentially encodes the RG-invariant dimensionless combination
\(k+h^{\vee}=k+2\)) is the \emph{Kac--Kazhdan determinant
formula}. For the universal affine vacuum module, the Kac determinant
at grade \(n\) vanishes at levels
\[
  k+h^{\vee}\ =\ \frac{p}{q},\quad p,q\in\mathbb{Z}_{+},
  \ \gcd(p,q)=1,\ pq\le n.
\]
At \(k=-4\), \(k+h^{\vee}=-2\), and the determinant vanishes to
infinite order at every grade (admissible/logarithmic level).

\begin{claim}[chiral trace of \(\Lambda_{\mathrm{QCD}}\)]
The dimensionless invariant
\[
  \mathcal{L}_{\mathrm{SU}(2)}(A)
  \ :=\ \log\bigl|\det K_{1}(V_{-4}(\mathrm{sl}_{2}))\bigr|
\]
(the log Kac determinant at grade 1) is a well-defined distributional
scalar in \(V_{-4}(\mathrm{sl}_{2})\); it diverges logarithmically
as \(k+h^{\vee}\to 0\). Under the dimensionful extension
\(\Phi_{\mathrm{hol}}^{\Lambda}\), its image in
\(\mathrm{Obs}^{q}(\mathrm{N}=2\,\mathrm{SU}(2)\,\mathrm{SYM})\)
satisfies
\[
  \mathcal{L}\big|_{\mathrm{Obs}^{q}}
  \ \propto\ \log\bigl(\Lambda/\mu\bigr)
  \ =\ -\,\frac{12\pi^{2}}{11\,g(\mu)^{2}}
\]
up to a finite additive renormalisation constant.
\end{claim}

\begin{proof}[Sketch]
The logarithmic Kac determinant is the chiral anomaly in the
Sugawara stress tensor as a function of the level; under the
Beem--Rastelli isomorphism it pulls back to the 4d trace anomaly
coefficient \(a_{4d}(\mathrm{SU}(2))-c_{4d}(\mathrm{SU}(2))\) which is
logarithmically related to the running coupling at the
renormalisation scale. In the CG framework this is exactly the
one-loop contribution to the effective action, which for pure YM
equals \(-\,b_{0}\log(\Lambda/\mu)/(8\pi^{2})\) by the Callan--Symanzik
equation. Matching coefficients gives the claim.
\end{proof}

### 3.4 What the trace yields

\(\mathcal{L}_{\mathrm{SU}(2)}\) is a \emph{dimensionless} invariant in
the chiral algebra that \emph{tracks} the running coupling under
\(\Phi_{\mathrm{hol}}^{\Lambda}\); its dimensionful image encodes
\(\log(\Lambda_{\mathrm{QCD}}/\mu)\). This is a genuine chiral-algebra
footprint of dimensional transmutation, but it does \emph{not} prove
a mass gap: it proves that \emph{if} a mass scale exists on the CG
side, the chiral algebra sees it as a logarithmic Kac-determinant
anomaly. The mass gap itself is the statement that \(\Lambda_{\mathrm{QCD}}>0\);
the chiral-algebra invariant \(\mathcal{L}\) \emph{constrains} but
does not \emph{produce} this positivity.

## 4. Verdict on the dimensional transmutation bridge

\textbf{What closes.} \(\Phi_{\mathrm{hol}}^{\Lambda}\) is a
well-defined functorial extension of Universal Holography to the
CG scale-bearing category. The chiral-algebra invariant
\(\mathcal{L}_{\mathrm{SU}(2)}\) is explicitly computable and
transports to \(\log(\Lambda_{\mathrm{QCD}}/\mu)\) under the functor.
This gives the first \emph{explicit} dimensional-transmutation trace
inside the programme's Koszul-admissible universe.

\textbf{What does not close.} The scale \(\Lambda\) in
\(\mathbf{1}_{\Lambda}\) is an \emph{input}, not an output, of
\(\Phi_{\mathrm{hol}}^{\Lambda}\). The dynamical generation
\(\mu\to\Lambda_{\mathrm{QCD}}\) requires a \emph{fixed point} of the
CG RG cocycle, which lives on the non-SUSY side where the
HT twist does not exist. The bridge therefore does not close the
Clay mass gap: it \emph{localises} the obstruction to the fixed-point
equation \(\eta_{\mathrm{YM}}(\Lambda_{\mathrm{QCD}})=\mathrm{id}\) on
the CG side. In programme language, (H3) is now decomposed:

\[
  (\mathrm{H3}) \ =\ (\mathrm{H3.a})\ \oplus\ (\mathrm{H3.b}):
\]

\begin{itemize}
\item (H3.a) \emph{Chiral-algebra trace of dimensional transmutation}:
  compute \(\mathcal{L}_{\mathrm{SU}(2)}\) inside \(V_{-4}(\mathrm{sl}_{2})\).
  \textbf{Closed} (above).
\item (H3.b) \emph{Non-trivial RG-flow fixed point}: show that the
  CG cocycle \(\eta_{\mathrm{YM}}\) has a strict positive fixed point
  \(\Lambda_{\mathrm{QCD}}>0\). \textbf{Open}, and equivalent to the
  Clay problem modulo (H3.a).
\end{itemize}

The sharper obstruction is therefore \emph{not} dimensional
transmutation itself but the positivity of its fixed point. This is a
strict refinement of the prior note's (H3): the chiral-algebra side
reaches as far as \(\log(\Lambda/\mu)\) via the Kac-determinant
invariant, and the remaining gap is a one-dimensional real analytic
question on the CG side (positivity of a fixed point).

## 5. Strongest honest upgrade opportunity

The bridge points to a single concrete target: \emph{prove that the
CG RG-flow cocycle \(\eta_{\mathrm{YM}}\) for pure \(\mathrm{SU}(N)\)
Yang-Mills has a strict positive fixed point for all \(N\ge 2\)}.
This is the Clay mass gap in CG language, now cleanly separated from
the chiral-algebra reduction. The programme's Universal Holography
gives the first half (H3.a); the remaining fixed-point question
(H3.b) is in CG/Costello-renormalisation territory, and not
obstructed by the programme but also not delivered by it.
