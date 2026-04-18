# Vol I `chiral_koszul_pairs.tex` Audit Prescriptions

Read-only input audited: `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex`

Mandatory writable output: `/Users/raeez/chiral-bar-cobar-vol2/compute/audit/chiral_koszul_pairs_prescriptions.md`

Vol I was not edited.

## Summary

- Findings count: 5
- Highest-severity defect: the admissible `\mathfrak{sl}_2` paragraph in `chiral_koszul_pairs.tex:1914-1921` contradicts the off-locus bar-cobar failure already inscribed for `L_{-1/2}(\mathfrak{sl}_2)` in `bar_cobar_adjunction_inversion.tex:1948-2017`.
- AP293-positive deliverable: restate the PBW criterion at its true strength, inscribe the star-shaped implication graph, promote generic affine Kac--Moody purity to an explicit scoped 13th characterization, separate the three Positselski ambients, and add the concrete `L_{-1/2}(\mathfrak{sl}_2)`/`\eta_4` witness.

## Convergence (AP306)

- (a) `thm:pbw-koszulness-criterion` checked at `chiral_koszul_pairs.tex:1082-1152`.
- (b) The meta-theorem implication web checked at `chiral_koszul_pairs.tex:2666-3170`.
- (c) D-module-purity directionality checked at `chiral_koszul_pairs.tex:2647-2650`, `2687-2690`, `3755-3931`, `3288-3290`.
- (d) Positselski/off-locus ambient language checked at `chiral_koszul_pairs.tex:293-299`, `346-347`, `454-467`, `643-644`, `2555-2569`.
- (e) Admissible `\mathfrak{sl}_2` witness checked against `chiral_koszul_pairs.tex:1902-1924`, `2048-2054`, `bar_cobar_adjunction_inversion.tex:1948-2017`, `holographic_datum_master.tex:1624-1628`, `1794-1799`, and `kac_moody.tex:2975-3019`.
- (f) Every target below includes a verbatim `old_string` / `new_string` pair suitable for later Vol I application.
- (g) Positive additions, not only removals, are listed in the final section.

## 1. `thm:pbw-koszulness-criterion` (`chiral_koszul_pairs.tex:1082-1152`)

### Current excerpt

Anchor: `chiral_koszul_pairs.tex:1082-1152`

```tex
\begin{theorem}[PBW criterion for chiral Koszulness; \ClaimStatusProvedHere]
\label{thm:pbw-koszulness-criterion}
\index{Koszul property!PBW criterion|textbf}
\textup{[Regime: filtered-complete
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\cA$ be a chiral algebra with PBW filtration
$F_0 \subset F_1 \subset \cdots \subset \cA$
such that the associated graded
$\operatorname{gr}_F \cA$ is a commutative chiral algebra
(equivalently, a vertex Poisson algebra).
Suppose:
\begin{enumerate}
\item\label{item:pbw-flat} The filtration is \emph{flat}: each $F_p/F_{p-1}$ is a free
 $\cO_X$-module of finite rank in each conformal weight.
\item\label{item:pbw-classical-koszul} The associated graded $\operatorname{gr}_F \cA$
 is classically Koszul: the Koszul complex
 $\barBgeom(\operatorname{gr}_F \cA) \otimes_\tau \operatorname{gr}_F \cA$
 is acyclic in positive degrees.
\item\label{item:pbw-bounded} For each bar degree $n$ and conformal weight $h$, the
 chain group $\barBgeom^n_h(\cA)$ is finite-dimensional.
\end{enumerate}
Then $\cA$ is chiral Koszul: the Koszul complex
$\barBgeom(\cA) \otimes_\tau \cA$ is acyclic in positive degrees.
\end{theorem}

\begin{proof}
Equip the Koszul complex $K = \barBgeom(\cA) \otimes_\tau \cA$ with
the filtration induced by $F$:
\[
F_p K^n = \sum_{i+j = n} F_i \barBgeom(\cA) \otimes_\tau F_j \cA.
\]
This is a bounded-below, exhaustive filtration compatible with the
differential (the bar differential and the twisting morphism $\tau$
both respect $F$ since they are defined by the OPE, which respects
conformal weight). The resulting spectral sequence has:
\[
E_0^{p,q} = \operatorname{gr}^p_F K^{p+q},
\qquad
d_0 = \operatorname{gr}_F(d_K).
\]
By flatness~\ref{item:pbw-flat}, the associated graded of $K$ is
the Koszul complex of $\operatorname{gr}_F \cA$:
\[
\operatorname{gr}_F K \cong
\barBgeom(\operatorname{gr}_F \cA) \otimes_\tau \operatorname{gr}_F \cA.
\]
(This uses that the bar construction commutes with taking associated
graded for flat filtrations: the residue differential of the associated
graded sees only the leading-order OPE terms, i.e., the vertex Poisson
bracket.)

By hypothesis~\ref{item:pbw-classical-koszul}, the $E_1$ page
is concentrated in degree $0$:
\[
E_1^{p,q} = H^{p+q}(\operatorname{gr}^p K) =
\begin{cases}
\bC & p = q = 0, \\
0 & p + q > 0.
\end{cases}
\]
All higher differentials $d_r$ for $r \geq 1$ are therefore zero
(they map between zero groups), so the spectral sequence collapses
at $E_1$.

By completeness of the filtration and the bounded-below hypothesis,
the spectral sequence converges:
$E_\infty = \operatorname{gr} H^*(K)$.
Since $E_\infty$ is concentrated in degree~$0$,
we conclude $H^n(K) = 0$ for $n > 0$.
\end{proof}
```

### Defect diagnosis

- The label is correct, but the theorem currently proves acyclicity of the twisted Koszul complex, not collapse of the PBW spectral sequence on `\barBgeom(\cA)` later attributed to it at `chiral_koszul_pairs.tex:2697-2699`, `2775-2779`, `2895-2897`, and `2350-2352`.
- The proof uses an undefined twisting morphism `\tau` in the statement and proof (`chiral_koszul_pairs.tex:1099-1105`, `1109-1116`) rather than the universal twisting morphism.
- The proof invokes completeness at `chiral_koszul_pairs.tex:1147-1149`, but completeness/Hausdorff convergence is not stated among the hypotheses; hypothesis `(3)` only gives finite-dimensionality.
- AP7/AP32: this should be stated as a filtered-complete PBW/Koszul-locus theorem, not as a bare acyclicity lemma whose downstream citations silently upgrade it to `E_2`-collapse.

### Edit pair

```tex
old_string:
\begin{theorem}[PBW criterion for chiral Koszulness; \ClaimStatusProvedHere]
\label{thm:pbw-koszulness-criterion}
\index{Koszul property!PBW criterion|textbf}
\textup{[Regime: filtered-complete
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\cA$ be a chiral algebra with PBW filtration
$F_0 \subset F_1 \subset \cdots \subset \cA$
such that the associated graded
$\operatorname{gr}_F \cA$ is a commutative chiral algebra
(equivalently, a vertex Poisson algebra).
Suppose:
\begin{enumerate}
\item\label{item:pbw-flat} The filtration is \emph{flat}: each $F_p/F_{p-1}$ is a free
 $\cO_X$-module of finite rank in each conformal weight.
\item\label{item:pbw-classical-koszul} The associated graded $\operatorname{gr}_F \cA$
 is classically Koszul: the Koszul complex
 $\barBgeom(\operatorname{gr}_F \cA) \otimes_\tau \operatorname{gr}_F \cA$
 is acyclic in positive degrees.
\item\label{item:pbw-bounded} For each bar degree $n$ and conformal weight $h$, the
 chain group $\barBgeom^n_h(\cA)$ is finite-dimensional.
\end{enumerate}
Then $\cA$ is chiral Koszul: the Koszul complex
$\barBgeom(\cA) \otimes_\tau \cA$ is acyclic in positive degrees.
\end{theorem}

\begin{proof}
Equip the Koszul complex $K = \barBgeom(\cA) \otimes_\tau \cA$ with
the filtration induced by $F$:
\[
F_p K^n = \sum_{i+j = n} F_i \barBgeom(\cA) \otimes_\tau F_j \cA.
\]
This is a bounded-below, exhaustive filtration compatible with the
differential (the bar differential and the twisting morphism $\tau$
both respect $F$ since they are defined by the OPE, which respects
conformal weight). The resulting spectral sequence has:
\[
E_0^{p,q} = \operatorname{gr}^p_F K^{p+q},
\qquad
d_0 = \operatorname{gr}_F(d_K).
\]
By flatness~\ref{item:pbw-flat}, the associated graded of $K$ is
the Koszul complex of $\operatorname{gr}_F \cA$:
\[
\operatorname{gr}_F K \cong
\barBgeom(\operatorname{gr}_F \cA) \otimes_\tau \operatorname{gr}_F \cA.
\]
(This uses that the bar construction commutes with taking associated
graded for flat filtrations: the residue differential of the associated
graded sees only the leading-order OPE terms, i.e., the vertex Poisson
bracket.)

By hypothesis~\ref{item:pbw-classical-koszul}, the $E_1$ page
is concentrated in degree $0$:
\[
E_1^{p,q} = H^{p+q}(\operatorname{gr}^p K) =
\begin{cases}
\bC & p = q = 0, \\
0 & p + q > 0.
\end{cases}
\]
All higher differentials $d_r$ for $r \geq 1$ are therefore zero
(they map between zero groups), so the spectral sequence collapses
at $E_1$.

By completeness of the filtration and the bounded-below hypothesis,
the spectral sequence converges:
$E_\infty = \operatorname{gr} H^*(K)$.
Since $E_\infty$ is concentrated in degree~$0$,
we conclude $H^n(K) = 0$ for $n > 0$.
\end{proof}

new_string:
\begin{theorem}[PBW criterion for chiral Koszulness; \ClaimStatusProvedHere]
\label{thm:pbw-koszulness-criterion}
\index{Koszul property!PBW criterion|textbf}
\textup{[Regime: filtered-complete
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\cA$ be a chiral algebra equipped with an exhaustive,
Hausdorff, complete PBW filtration
$F_0 \subset F_1 \subset \cdots \subset \cA$
such that the associated graded
$\operatorname{gr}_F \cA$ is a commutative chiral algebra
\textup{(}equivalently, a vertex Poisson algebra\textup{)}.
Suppose:
\begin{enumerate}
\item\label{item:pbw-flat} each $F_p/F_{p-1}$ is a free
 $\cO_X$-module of finite rank in each conformal weight;
\item\label{item:pbw-classical-koszul} the associated graded
 $\operatorname{gr}_F \cA$ is classically Koszul, so its bar
 cohomology is concentrated on the Koszul diagonal;
\item\label{item:pbw-bounded} for each bar degree $n$ and
 conformal weight $h$, the chain group
 $\barBgeom^n_h(\cA)$ is finite-dimensional.
\end{enumerate}
Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item the PBW spectral sequence on $\barBgeom(\cA)$ collapses at $E_2$;
\item the twisted Koszul complex
 $\barBgeom(\cA)\otimes_{\tau_{\mathrm{univ}}}\cA$
 is acyclic in positive degrees.
\end{enumerate}
In particular, $\cA$ is chirally Koszul.
\end{theorem}

\begin{proof}
Filter both $\barBgeom(\cA)$ and
$K=\barBgeom(\cA)\otimes_{\tau_{\mathrm{univ}}}\cA$ by the induced
PBW degree. Because the filtration is exhaustive, Hausdorff, complete,
and bounded below on each conformal-weight piece, and because the
weight pieces are finite-dimensional by
\textup{\ref{item:pbw-bounded}}, both spectral sequences converge
strongly weight by weight.

For the bar complex, flatness identifies
$\operatorname{gr}_F\barBgeom(\cA)$ with
$\barBgeom(\operatorname{gr}_F\cA)$. Classical Koszulness of
$\operatorname{gr}_F\cA$ implies that the associated-graded bar
cohomology is concentrated on the diagonal, so the $E_1$ page of the
PBW spectral sequence on $\barBgeom(\cA)$ is concentrated in the row
$q=0$. Hence every differential $d_r$ with $r\ge 2$ vanishes, and the
PBW spectral sequence collapses at $E_2$.

For the twisted Koszul complex, the same flatness gives
\[
\operatorname{gr}_F K \cong
\barBgeom(\operatorname{gr}_F\cA)\otimes_{\tau_{\mathrm{univ}}}
\operatorname{gr}_F\cA.
\]
By \textup{\ref{item:pbw-classical-koszul}} this associated-graded
complex is acyclic in positive degrees, so the $E_1$ page of the
spectral sequence for $K$ is concentrated in total degree~$0$.
Strong convergence therefore gives $H^n(K)=0$ for $n>0$.

Statement \textup{(ii)} is the defining acyclicity condition for the
universal twisting datum, and together with
\textup{(i)} it places $\cA$ on the PBW/Koszul locus.
\end{proof}
```

### AP anchor

- AP7/AP32: missing Koszul-locus/filtered-complete scope.
- AP284: downstream equivalence arrows currently cite this theorem for a stronger statement than it proves.

## 2. N-equivalent implication structure (`chiral_koszul_pairs.tex:2666-3170`)

### Current excerpt

Anchors: `chiral_koszul_pairs.tex:2666-2690`, `2769-3140`, `3142-3170`

```tex
\begin{theorem}[Equivalences and consequences of chiral Koszulness; \ClaimStatusProvedHere]
\label{thm:koszul-equivalences-meta}
\index{Koszul property!equivalences of characterizations|textbf}

Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
with PBW filtration $F_\bullet$.
Conditions \textup{(i)--(v)}, \textup{(ix)--(x)}, and the
genus-$0$ clause of condition~\textup{(vii)} below are eight
genuinely independent bidirectional equivalences; condition~\textup{(vi)}
(Barr--Beck--Lurie comparison) is a proved consequence of
condition~\textup{(v)} rather than an independent route, and is listed
for completeness.
...
\begin{remark}[Proof web redundancy]
\label{rem:koszul-proof-web-redundancy}
The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
single chain.
Its unconditional core already has several proof lanes that do not
route through the same intermediate condition:
\[
\textup{(i)} \Longleftrightarrow \textup{(v)}
\quad\text{(universal twisting morphism and bar filtration),}\qquad
\textup{(i)} \Longleftrightarrow \textup{(iii)}
\quad\text{($A_\infty$ transfer and Keller classicality),}
\]
\[
\textup{(i)} \Longleftrightarrow \textup{(iv)}
\quad\text{(Ext diagonal vanishing),}\qquad
\textup{(i)} \Longleftrightarrow \textup{(vii)}
\quad\text{(the genus-$0$ clause of factorization homology concentration),}
\]
\[
\textup{(i)} \Longleftrightarrow \textup{(ix)}
\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
\textup{(i)} \Longleftrightarrow \textup{(x)}
\quad\text{(FM boundary acyclicity),}
\]
and on the monadic side
\[
\textup{(i)} \Longleftrightarrow \textup{(vi)}
\quad\text{(Barr--Beck--Lurie monadicity).}
\]
```

### Defect diagnosis

- The proof is written as a star-shaped web around `(i)` with a smaller core circuit `(i) <-> (ii) <-> (iii) <-> (v)`, but the theorem never inscribes that graph explicitly; it presents the reader with a naked "N characterizations" headline (`chiral_koszul_pairs.tex:2666-2690`) and a long proof that only later reveals the topology (`chiral_koszul_pairs.tex:2769-3140`, `3142-3170`).
- No item-level proof anchors are inscribed in the theorem statement itself, so the reader cannot tell which implications are direct, which factor through `(i)`, and which are conditional or one-way.
- AP284 therefore bites exactly here: the proof is star-shaped, not cyclic, and each arrow needs to be named where the theorem is stated.

### Edit pair

```tex
old_string:
\begin{remark}[Proof web redundancy]
\label{rem:koszul-proof-web-redundancy}
The proof of Theorem~\ref{thm:koszul-equivalences-meta} is not a
single chain.
Its unconditional core already has several proof lanes that do not
route through the same intermediate condition:
\[
\textup{(i)} \Longleftrightarrow \textup{(v)}
\quad\text{(universal twisting morphism and bar filtration),}\qquad
\textup{(i)} \Longleftrightarrow \textup{(iii)}
\quad\text{($A_\infty$ transfer and Keller classicality),}
\]
\[
\textup{(i)} \Longleftrightarrow \textup{(iv)}
\quad\text{(Ext diagonal vanishing),}\qquad
\textup{(i)} \Longleftrightarrow \textup{(vii)}
\quad\text{(the genus-$0$ clause of factorization homology concentration),}
\]
\[
\textup{(i)} \Longleftrightarrow \textup{(ix)}
\quad\text{(Kac--Shapovalov non-degeneracy),}\qquad
\textup{(i)} \Longleftrightarrow \textup{(x)}
\quad\text{(FM boundary acyclicity),}
\]
and on the monadic side
\[
\textup{(i)} \Longleftrightarrow \textup{(vi)}
\quad\text{(Barr--Beck--Lurie monadicity).}
\]

Three direct cross-links are the load-bearing redundancy.

\smallskip\noindent
\textup{(v)}$\Rightarrow$\textup{(i)} is the shortest loop.

new_string:
\begin{remark}[Implication graph for
Theorem~\ref{thm:koszul-equivalences-meta}]
\label{rem:koszul-proof-web-redundancy}
The implication structure is \emph{star-shaped about
\textup{(i)}}, not cyclic.

\smallskip\noindent
\emph{Core circuit.}
\[
\textup{(i)}
\Longleftrightarrow
\textup{(ii)}
\Longleftrightarrow
\textup{(iii)}
\Longleftrightarrow
\textup{(v)}
\Longleftrightarrow
\textup{(i)}
\]
with anchors:
\textup{(i)}$\Leftrightarrow$\textup{(ii)}
by Theorem~\ref{thm:pbw-koszulness-criterion},
\textup{(ii)}$\Leftrightarrow$\textup{(iii)}
by Proposition~\ref{prop:ainfty-formality-implies-koszul} and
Theorem~\ref{thm:ainfty-koszul-characterization},
\textup{(ii)}$\Rightarrow$\textup{(v)}
by Theorem~\ref{thm:bar-concentration} plus
Theorem~\ref{thm:bar-cobar-inversion-qi},
and \textup{(v)}$\Rightarrow$\textup{(i)}
by Theorem~\ref{thm:fundamental-twisting-morphisms}.

\smallskip\noindent
\emph{Direct spokes from \textup{(i)}.}
\[
\textup{(i)} \Longleftrightarrow \textup{(iv)}
\qquad
\textup{(i)} \Longleftrightarrow \textup{(vii)}
\qquad
\textup{(i)} \Longleftrightarrow \textup{(ix)}
\qquad
\textup{(i)} \Longleftrightarrow \textup{(x)}
\]
where the anchors are, respectively,
Theorem~\ref{thm:ext-diagonal-vanishing},
Proposition~\ref{prop:bar-fh} together with
Theorem~\ref{thm:pbw-koszulness-criterion},
Theorem~\ref{thm:kac-shapovalov-koszulness},
and the proof paragraphs headed
\emph{FM boundary acyclicity} in
Theorem~\ref{thm:koszul-equivalences-meta}.

\smallskip\noindent
\emph{Monadic spoke.}
\[
\textup{(v)} \Longleftrightarrow \textup{(vi)}
\]
by the Barr--Beck--Lurie argument in the proof of
Theorem~\ref{thm:koszul-equivalences-meta}, using
Theorem~\ref{thm:quillen-equivalence-chiral}.

\smallskip\noindent
\emph{One-way and conditional spokes.}
\[
\textup{(v)} \Rightarrow \textup{(viii)},
\qquad
\textup{(xii)} \Rightarrow \textup{(x)},
\qquad
\textup{(i)} \Longleftrightarrow \textup{(xi)}
\ \text{under perfectness/non-degeneracy.}
\]
The anchors are Theorem~H together with
Theorem~\ref{thm:main-koszul-hoch},
Remark~\ref{rem:d-module-purity-content},
and the \emph{Lagrangian criterion} paragraphs in the proof of
Theorem~\ref{thm:koszul-equivalences-meta}.

This explicit star diagram is the theorem-level record of the proof
web. Any future enlargement to twelve-plus-one or thirteen
characterizations should be added by adjoining a new spoke with its own
named arrow, not by silently changing the headline count.
```

### AP anchor

- AP284: inscribe the star-shaped implication graph and anchor every arrow.

## 3. D-module purity scope and two-way status (`chiral_koszul_pairs.tex:2647-2650`, `3288-3290`, `3818-3931`)

### Current excerpt

Anchors: `chiral_koszul_pairs.tex:2647-2650`, `3288-3290`, `3852-3931`

```tex
Item~\textup{(xii)} ($\mathcal{D}$-module purity) is a one-directional
implication~\textup{(xii)}$\Rightarrow$\textup{(x)}; the converse
is proved for affine Kac--Moody at non-critical level
(Remark~\ref{rem:d-module-purity-content}) but open for Virasoro
and $\mathcal{W}$ algebras.
```

```tex
The converse of~\textup{(xii)} is proved for the affine
Kac--Moody lineage
(Proposition~\ref{prop:d-module-purity-km}); the non-affine
case (Virasoro, $\cW$-algebras) remains open.
```

```tex
\begin{proposition}[Kac--Moody equivalence via
Saito--Kashiwara weight filtration;
\ClaimStatusProvedHere]
\label{prop:d-module-purity-km-equivalence}
...
The implications \textup{(a)}$\Leftrightarrow$\textup{(b)}
are part of the core circuit
\textup{(i)}$\Leftrightarrow$\textup{(ii)} of
Theorem~\ref{thm:koszul-equivalences-meta}.
The implication \textup{(c)}$\Rightarrow$\textup{(b)}
is the one-directional part of the meta-theorem
(\textup{(xii)}$\Rightarrow$\textup{(x)}): purity
of~$\barBgeom_n$ forces Saito strictness on the weight
filtration, and Saito strictness gives FM stratum
acyclicity, which in turn forces PBW strictness by the
Kac--Shapovalov implication
\textup{(ix)}$\Rightarrow$\textup{(ii)}.

The new content is the converse \textup{(b)}$\Rightarrow$\textup{(c)}.
```

### Defect diagnosis

- The file already proves a scoped two-way result for generic affine Kac--Moody algebras at `chiral_koszul_pairs.tex:3852-3931`, but the theorem-level summary still leaves that positive result hidden behind a general one-way slogan at `2647-2650`.
- The citation at `3288-3290` points to `prop:d-module-purity-km`, which proves only the forward affine implication (`3818-3843`), not the converse. The converse is proved by `prop:d-module-purity-km-equivalence` (`3852-3931`).
- AP284 and the user's target require the two directions to be stated as genuinely proved where they are genuinely proved. The manuscript should therefore keep the general theorem one-way, but add an explicit scoped upgrade: on the generic affine Kac--Moody locus, D-module purity is the thirteenth equivalent characterization.

### Edit pairs

```tex
old_string:
Item~\textup{(xii)} ($\mathcal{D}$-module purity) is a one-directional
implication~\textup{(xii)}$\Rightarrow$\textup{(x)}; the converse
is proved for affine Kac--Moody at non-critical level
(Remark~\ref{rem:d-module-purity-content}) but open for Virasoro
and $\mathcal{W}$ algebras.

new_string:
Item~\textup{(xii)} ($\mathcal{D}$-module purity) is one-directional
in general:
\textup{(xii)}$\Rightarrow$\textup{(x)}.
On the generic affine Kac--Moody locus, however, the converse is
proved by Proposition~\ref{prop:d-module-purity-km-equivalence}, so
$\mathcal{D}$-module purity becomes a genuine additional
characterization there. For Virasoro and $\mathcal{W}$ algebras the
converse remains open.
```

```tex
old_string:
The converse of~\textup{(xii)} is proved for the affine
Kac--Moody lineage
(Proposition~\ref{prop:d-module-purity-km}); the non-affine
case (Virasoro, $\cW$-algebras) remains open.

new_string:
The converse of~\textup{(xii)} is proved for the generic affine
Kac--Moody lineage
\textup{(}Proposition~\ref{prop:d-module-purity-km-equivalence}\textup{)};
there $\mathcal{D}$-module purity is a thirteenth equivalent
characterization. The non-affine case
\textup{(}Virasoro, $\cW$-algebras\textup{)} remains open.
```

```tex
old_string:
\end{proof}

\begin{remark}[Family dependence of the
$\cD$-module purity equivalence]

new_string:
\end{proof}

\begin{corollary}[Generic affine Kac--Moody:
$\cD$-module purity as a thirteenth characterization;
\ClaimStatusProvedHere]
\label{cor:d-module-purity-km-thirteenth}
For $\cA = V_k(\fg)$ at generic non-critical level, condition
\textup{(xii)} of Theorem~\ref{thm:koszul-equivalences-meta} is
equivalent to the unconditional core
\textup{(i)}--\textup{(vii)}, \textup{(ix)}--\textup{(x)}.
Equivalently, on this locus $\mathcal{D}$-module purity is the
thirteenth characterization of chiral Koszulness.
\end{corollary}

\begin{proof}
This is exactly Proposition~\ref{prop:d-module-purity-km-equivalence},
rewritten in the numbering of
Theorem~\ref{thm:koszul-equivalences-meta}.
\end{proof}

\begin{remark}[Family dependence of the
$\cD$-module purity equivalence]
```

### AP anchor

- AP284: additional characterizations need both directions separately proved and separately scoped.
- AP293: the positive theorem already exists locally; it needs promotion, not suppression.

## 4. Positselski three-ambient split (`chiral_koszul_pairs.tex:293-299`, `346-347`, `454-467`, `643-644`, `2555-2569`)

### Current excerpt

Anchors: `chiral_koszul_pairs.tex:293-299`, `346-347`, `454-467`, `643-644`, `2555-2569`

```tex
Off the Koszul locus, the bar-cobar object persists in the
provisional coderived category
$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
(Appendix~\ref{sec:coderived-models}),
not in the ordinary derived category.
```

```tex
The unified
\emph{Koszul Reflection} of
Theorem~\ref{thm:koszul-reflection}, $K = \Bbarch_X$ with inverse
$K^{-1} = \Omegach_X$, is a symmetric-monoidal adjoint equivalence
of $(\infty,1)$-categories
\[
   K\;\colon\;\Alg^{\fact,\aug,\comp}_X
   \;\rightleftarrows\;\CoAlg^{\fact,\conil,\co}_X\;\colon\;K^{-1},
\]
satisfying $K^{2}\simeq\mathrm{id}$ on the Koszul locus
$\Kosz(X)\subset\Alg^{\fact,\aug,\comp}_X$ (chain-level
quasi-isomorphism for both unit and counit) and
$K^{2}\simeq\mathrm{id}$ in $D^{\co}(\Bbarch\text{-}\CoFact)$ off
$\Kosz(X)$ (coderived equivalence under the covariantly-weighted
Positselski package).
```

### Defect diagnosis

- The target file uses all three off-locus Positselski surfaces, but only piecemeal: the pro-object completion appears at `346-347` and `454-467`, the coderived category at `293-299` and `643-644`, and the weight-completed/covariantly weighted lane only as the bundled phrase "Positselski package" at `2555-2569`.
- The sentence at `2555-2569` also conflates chain-level strict inversion on the Koszul locus with `(\infty,1)`-categorical/coderived involutivity off the locus.
- AP269 and AP289 therefore both fire here: the manuscript needs one explicit three-ambient scope declaration and one explicit lane split between strict chain-level and coderived/weight-completed statements.

### Edit pair

```tex
old_string:
The unified
\emph{Koszul Reflection} of
Theorem~\ref{thm:koszul-reflection}, $K = \Bbarch_X$ with inverse
$K^{-1} = \Omegach_X$, is a symmetric-monoidal adjoint equivalence
of $(\infty,1)$-categories
\[
   K\;\colon\;\Alg^{\fact,\aug,\comp}_X
   \;\rightleftarrows\;\CoAlg^{\fact,\conil,\co}_X\;\colon\;K^{-1},
\]
satisfying $K^{2}\simeq\mathrm{id}$ on the Koszul locus
$\Kosz(X)\subset\Alg^{\fact,\aug,\comp}_X$ (chain-level
quasi-isomorphism for both unit and counit) and
$K^{2}\simeq\mathrm{id}$ in $D^{\co}(\Bbarch\text{-}\CoFact)$ off
$\Kosz(X)$ (coderived equivalence under the covariantly-weighted
Positselski package).

new_string:
The unified
\emph{Koszul Reflection} of
Theorem~\ref{thm:koszul-reflection}, $K = \Bbarch_X$ with inverse
$K^{-1} = \Omegach_X$, should be read in two distinct lanes.

\smallskip\noindent
\emph{Strict chain-level lane.}
On the Koszul locus
$\Kosz(X)\subset\Alg^{\fact,\aug,\comp}_X$, the unit and counit are
chain-level quasi-isomorphisms on the original complexes, so
$K^2\simeq\mathrm{id}$ holds strictly there.

\smallskip\noindent
\emph{Off-locus Positselski lane.}
Away from $\Kosz(X)$, three ambients must be separated:
\begin{enumerate}[label=\textup{(\roman*)}]
\item the pro-object completion underlying the completed tensor product
 $\widehat{\otimes} = \varprojlim_n(-/F^n)$;
\item the weight-completed factorization companion
 $\cA^!_\infty$, obtained before strict rectification;
\item the coderived category
 $D^{\co}(\Bbarch\text{-}\CoFact)$ in which the counit is inverted.
\end{enumerate}
The derived bar-cobar adjunction is an adjoint equivalence of
$(\infty,1)$-categories in this Positselski ambient, but off the
Koszul locus the manuscript asserts only the coderived equivalence
$K^2\simeq\mathrm{id}$ there, not a chain-level quasi-isomorphism on
the original complexes.
```

### AP anchor

- AP269: strict chain-level quasi-isomorphism is not the same statement as `(\infty,1)`-categorical adjoint equivalence.
- AP289: separate pro-object, weight-completed, and coderived ambients explicitly.

## 5. `L_{-1/2}(\mathfrak{sl}_2)` and the `\eta_4` off-locus witness (`chiral_koszul_pairs.tex:1902-1924`, `2048-2054`)

### Current excerpt

Anchors: `chiral_koszul_pairs.tex:1902-1924`, `2048-2054`

```tex
For $\fg = \mathfrak{sl}_2$, admissible Koszulness is settled:
the simple quotient $L_k(\mathfrak{sl}_2)$ is chirally Koszul at
\emph{every} admissible level $k = -2 + p/q$ ($p \geq 2$,
$q \geq 1$, $\gcd(p,q) = 1$). The argument is structural:
the null-vector ideal $I_k$ is generated in a single conformal
weight, the bar complex of $L_k$ is the quotient bar complex
$\barB(V_k)/\barB(I_k)$, and the quotient bar spectral sequence
degenerates at~$E_2$ by the Kac--Wakimoto character formula.
```

```tex
The rank $\geq 2$ threshold is genuine: for
$\mathfrak{sl}_2$, the single Cartan class $[H]$ at
$E_1^{2, h_\alpha}$ co-resonates with a root target at
$E_1^{1, h_\alpha + 1}$ via the Poisson bracket $[H, F] = -2F$,
and $d_r$ cancellation through that channel restores Koszulness
(consistent with the sharp $L_k(\mathfrak{sl}_2)$ result at all
admissible levels recalled above).
```

### Defect diagnosis

- These sentences assert a blanket admissible `\mathfrak{sl}_2` Koszul theorem that the manuscript's other Vol I surfaces explicitly deny. `bar_cobar_adjunction_inversion.tex:1952-2017` gives `L_{-1/2}(\mathfrak{sl}_2)` as an admissible-level failure of strict bar-cobar inversion; `kac_moody.tex:2975-3019` says the finite-page degeneration at `k=-1/2` is not promoted there to chirally Koszulness; `holographic_datum_master.tex:1624-1628` and `1794-1799` name the surviving off-diagonal class `\eta_4` as the concrete witness.
- The current paragraph at `1902-1924` only supports finite-page control of ordinary-character and Li--bar calculations, not strict bar-cobar inversion or Ext-diagonal purity. That limitation is already built into `chiral_koszul_pairs.tex:1896-1912` and into the reducedness warning of `chiral_koszul_pairs.tex:2311-2438`.
- AP275 requires the concrete boundary-obstruction pairing to be stated. The admissible `\eta_4` class should be named, not hidden under a blanket "restores Koszulness" sentence.

### Edit pairs

```tex
old_string:
For $\fg = \mathfrak{sl}_2$, admissible Koszulness is settled:
the simple quotient $L_k(\mathfrak{sl}_2)$ is chirally Koszul at
\emph{every} admissible level $k = -2 + p/q$ ($p \geq 2$,
$q \geq 1$, $\gcd(p,q) = 1$). The argument is structural:
the null-vector ideal $I_k$ is generated in a single conformal
weight, the bar complex of $L_k$ is the quotient bar complex
$\barB(V_k)/\barB(I_k)$, and the quotient bar spectral sequence
degenerates at~$E_2$ by the Kac--Wakimoto character formula.

new_string:
For $\fg = \mathfrak{sl}_2$, the admissible simple-quotient story is
not a blanket strict-Koszul theorem in this chapter. What is proved
here is the finite-page bar/Li--bar control recorded above
\textup{(}Theorem~\ref{thm:kw-bar-spectral} and
Proposition~\ref{prop:bar-admissible}\textup{)}.
The concrete off-locus witness is the non-degenerate admissible point
$k=-1/2$: the weight-$4$ singular vector produces an off-diagonal bar
class, denoted $\eta_4$ elsewhere in Vol~I, so the worked
Kac--Wakimoto degeneration does not upgrade here to strict bar-cobar
inversion or Ext-diagonal purity for $L_{-1/2}(\mathfrak{sl}_2)$.
```

```tex
old_string:
The rank $\geq 2$ threshold is genuine: for
$\mathfrak{sl}_2$, the single Cartan class $[H]$ at
$E_1^{2, h_\alpha}$ co-resonates with a root target at
$E_1^{1, h_\alpha + 1}$ via the Poisson bracket $[H, F] = -2F$,
and $d_r$ cancellation through that channel restores Koszulness
(consistent with the sharp $L_k(\mathfrak{sl}_2)$ result at all
admissible levels recalled above).

new_string:
The rank $\geq 2$ threshold is genuine, but the rank-$1$ case is not a
strict-Koszul shortcut. For $\mathfrak{sl}_2$, the same co-resonance
explains why the reduced Li--bar obstruction is subtler than in
$\mathfrak{sl}_3$; it does \emph{not} by itself prove strict bar-cobar
inversion for the simple quotient. The worked admissible point
$L_{-1/2}(\mathfrak{sl}_2)$ remains the concrete witness: the
weight-$4$ singular vector yields the off-diagonal class $\eta_4$,
which survives on the original complex and obstructs the strict lane.
```

### AP anchor

- AP275: boundary-obstruction pairing via the admissible class `\eta_4`.
- AP7/AP32: do not silently promote finite-page admissible spectral-sequence control to strict-Koszulness.

## AP293-positive deliverable

What gets added if the prescriptions are applied:

- A theorem-level PBW statement whose label now matches its downstream use: explicit `E_2`-collapse plus acyclicity, with the universal twisting morphism and complete-filtration hypotheses stated.
- An inscribed star-shaped implication graph for the twelve-condition theorem, with the core circuit and each direct spoke named.
- A new scoped corollary making generic affine Kac--Moody `\mathcal{D}`-module purity the thirteenth characterization.
- A single explicit three-ambient Positselski declaration: pro-object completion, weight-completed factorization companion, coderived equivalence.
- A concrete admissible off-locus witness paragraph naming `L_{-1/2}(\mathfrak{sl}_2)` and `\eta_4`, so the strict lane is falsified by a named class rather than by vague admissible caution.
