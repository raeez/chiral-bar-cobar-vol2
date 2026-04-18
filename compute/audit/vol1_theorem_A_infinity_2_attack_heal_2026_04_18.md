# Vol I Theorem A^{\infty,2} Properad Attack-Heal

Date: `2026-04-18`

Target: `/Users/raeez/chiral-bar-cobar/chapters/theory/theorem_A_infinity_2.tex`

Status: `BLOCKED FOR DIRECT INSCRIPTION IN THIS SESSION`

Reason: the sibling Vol I file is readable but not writable from the current sandbox (`test -w /Users/raeez/chiral-bar-cobar/chapters/theory/theorem_A_infinity_2.tex` returned `not_writable`). The repair below is therefore packaged as a ready-to-inscribe delta rather than applied in place.

## Localized gap

The neighborhoods that were under inspection in the prior wave are:

- `1128-1178`: alternative-proof-lane scoping plus `cor:classical-A-from-A-infinity-2`.
- `1784-1828`: HZ-IV independent-verification sources, especially the Lurie `(\infty,1)` lane.

These two neighborhoods point to the same structural gap:

1. the chapter's load-bearing theorem `thm:A-infinity-2` is stated only in the `(\infty,2)`-properad lane;
2. the proof, corollaries, and HZ-IV decorators already use strict chain-level and `(\infty,1)`-categorical lanes;
3. Verdier intertwining is used downstream but never stated in `thm:A-infinity-2`.

The result is an AP269/AP25 compound: strict adjunction data, ambient equivalence, and Verdier duality are all present in the chapter, but not separated into named theorem clauses with the correct ambient qualifiers.

## Findings

1. `HIGH` at `theorem_A_infinity_2.tex:732-817`, `:840-899`, `:1792-1797`

`thm:A-infinity-2` is only the `(\infty,2)` theorem. The strict chain-level adjunction lives only inside Step 1 of the proof, while the HZ-IV remark explicitly calls out an independent `(\infty,1)`-categorical verification path from Lurie HA 5.5. Pattern 269 requires both lanes to be stated as theorem-level mathematics, not left implicit.

2. `HIGH` at `theorem_A_infinity_2.tex:192-195`, `:252`, `:758-762`

The file silently swaps adjunction orientations. The classical twisting-morphism bijection is `\Omega \dashv B` at strict chain level; the theorem statement displays `\Bbarch_X \dashv \Omegach_X` with no convention sentence. That is acceptable only after explaining that the ambient `(\infty,2)` equivalence is biadjoint, while the strict chain-level adjunction keeps the classical orientation.

3. `HIGH` at `theorem_A_infinity_2.tex:1166-1185`, `:1373-1377`, and by absence from `:732-817`

Verdier intertwining is not a theorem clause. The corollary proof currently invokes "Verdier-biequivariance of `\Bbarch_X`" but the theorem statement contains no `\mathbb D_{\operatorname{Ran}}` and no `\cA^!_\infty`.

4. `MODERATE` at `theorem_A_infinity_2.tex:47-50`

The slogan "`the chiral bar is its own Koszul dual`" violates AP25. The chapter needs the standard three-functor display already used elsewhere in Vol I:

` \Omega(\barB(\cA)) \simeq \cA ` = inversion

` \mathbb D_{\Ran}\barB(\cA) \simeq \cA^!_\infty ` = Verdier lane

` (H^*(\barB(\cA)))^\vee = \cA^! ` = linear duality

5. `MODERATE` at `theorem_A_infinity_2.tex:92-94`, `:1746-1748`

"Standard landscape" is used as if self-explanatory. The theorem needs an explicit scope remark naming the hypothesis class and excluding the known non-standard/logarithmic families.

6. `MODERATE` at `theorem_A_infinity_2.tex:795-808` vs `:1217-1249`

The theorem-level `R`-twisted descent item is still too narrative. The explicit `\Sigma_n`-action is only stated later in the lemma.

## Proposed inscription

### A. Insert before `thm:A-infinity-2` (after current line 730)

```tex
\begin{proposition}[Chain-level twisting-morphism adjunction underlying Theorem~$A^{\infty,2}$;
\ClaimStatusProvedHere]
\label{prop:ainf2-chain-level-adjunction}
Let $X$ be a smooth curve over a field of characteristic~$0$,
$\cA\in\Fact^{\aug}(X)$, and
$\cC\in\CoFact^{\conil,\comp}(X)$. On the dg enhancement underlying the
Francis--Gaitsgory factorization ambient there are natural bijections
\[
\Hom_{\Fact^{\aug}(X)}\!\bigl(\Omegach_X(\cC),\cA\bigr)
\;\simeq\;
\Tw_X(\cC,\cA)
\;\simeq\;
\Hom_{\CoFact^{\conil,\comp}(X)}\!\bigl(\cC,\Bbarch_X(\cA)\bigr).
\]
Thus the strict chain-level adjunction is
\[
\Omegach_X \dashv \Bbarch_X.
\]
Its unit
$\eta^{\mathrm{str}}_\cC\colon \cC\to\Bbarch_X\Omegach_X(\cC)$
and counit
$\varepsilon^{\mathrm{str}}_\cA\colon \Omegach_X\Bbarch_X(\cA)\to\cA$
are the chain maps corresponding to the identity twisting morphisms.
On the Koszul locus these maps are quasi-isomorphisms; under
\textup{(H1)}--\textup{(H3)} they become coderived equivalences on the
full conilpotent-complete locus.
\end{proposition}

\begin{proof}
The displayed bijection is the Loday--Vallette twisting-morphism
adjunction \cite[Theorem~2.2.9]{LV12}, specialised to the chiral operad
and to the Francis--Gaitsgory $\star$-monoidal factorization ambient by
\cite[Proposition~3.1]{Francis2012}. Step~1 of the proof of
Theorem~\ref{thm:A-infinity-2} constructs the cofree bar coalgebra
$\Bbarch_X(\cA)$ and the free cobar algebra $\Omegach_X(\cC)$ with the
standard bar and cobar differentials, so the universal twisting
morphism produces the two Hom-sets exactly as in the classical case.
The strict unit and counit are the chain maps corresponding to the
identity morphisms under this bijection. On the Koszul locus,
Corollaries~\ref{cor:eight-cor-counit-qi} and
\ref{cor:eight-cor-unit-weq} identify these maps as chain-level
quasi-isomorphisms. Off the Koszul locus, Theorem~\ref{thm:koszul-reflection}
\ref{KR-iii} together with Positselski's coderived continuation
\cite[Theorem~9.1]{Positselski2018} upgrades the same maps to coderived
equivalences on the conilpotent-complete locus.
\end{proof}
```

Why this block is load-bearing:

- it resolves Pattern 269 directly;
- it explains the later Lurie `(\infty,1)` verification sentence;
- it distinguishes the strict chain-level adjunction from the ambient equivalence.

### B. Rewrite the opening of `thm:A-infinity-2`

Replace the theorem's first paragraph beginning at current line `746` with:

```tex
Let $X$ be a smooth curve over a field of characteristic~$0$. The
strict chain-level twisting-morphism adjunction underlying
Theorem~$A^{\infty,2}$ is Proposition~\ref{prop:ainf2-chain-level-adjunction}.
After passage to the Francis--Gaitsgory factorization ambient
$\Fact(X)$ \textup{(}Definition~\ref{def:fg-ambient}\textup{)} and
localisation to the conilpotent-complete locus, the same bar and cobar
functors become biadjoint; we record one orientation of the resulting
\textup{($\infty,2$)}-categorical adjoint equivalence:
```

Then change:

- "`The equivalence satisfies three additional properties:`" to "`The equivalence satisfies four additional properties:`"

### C. Add a new theorem item `(iv)` after current item `(iii)`

```tex
\item \label{A2-iv} \emph{Verdier intertwining.}
Write $\cA^!_\infty$ for the homotopy Koszul-dual factorization algebra
of Theorem~\ref{thm:bar-cobar-verdier}; equivalently,
\[
\mathbb{D}_{\operatorname{Ran}(X)}\Bbarch_X(\cA)
\;\simeq\;
\cA^!_\infty.
\]
On the Koszul locus, $H^*(\cA^!_\infty)$ recovers the strict dual
$\cA^! = (H^*(\Bbarch_X(\cA)))^\vee$. This Verdier lane is distinct from
the inversion statement $\Omegach_X\Bbarch_X(\cA)\simeq\cA$.
```

This wording follows the canonical Vol I theorem
`thm:bar-cobar-verdier` at
`chapters/theory/cobar_construction.tex:1342-1391`, which uses
` \mathbb D_{\operatorname{Ran}}(\bar B^{\mathrm{ch}}(\mathcal A))
\simeq (\mathcal A)^!_\infty ` as the chapter-level notation choice.

### D. Strengthen item `(iii)` with the explicit `R`-twist

At current lines `806-808`, replace the last sentence with:

```tex
where $L_R$ is the $\Sigma_n$-equivariant local system on
$\Ran^{\ord}(X)$ whose elementary transposition on the top stratum
$\Conf^{\ord}_n(X)$ acts by
$R(z_i-z_{i+1})\cdot\tau_{i,i+1}$
\textup{(}Lemma~\ref{lem:R-twisted-descent}, hypotheses~\ref{R1}+\ref{R2}\textup{)}.
```

### E. Add a proof step for the Verdier lane

After current Step~4 in the proof of `thm:A-infinity-2`, add:

```tex
\emph{Step 5: Verdier intertwining.}
Theorem~\ref{thm:bar-cobar-verdier} identifies the Verdier dual of the
bar coalgebra with the homotopy Koszul-dual factorization algebra:
\[
\mathbb{D}_{\operatorname{Ran}(X)}\Bbarch_X(\cA)\simeq \cA^!_\infty.
\]
This is the Verdier lane of Theorem~A. It is not the bar--cobar
inversion statement of Step~2 and does not pass through the graded
linear dual $(H^*(\Bbarch_X(\cA)))^\vee$.
```

### F. Insert an AP25 remark near the setup (best after current line 94)

```tex
\begin{remark}[Scope of the standard landscape in this chapter]
\label{rem:ainf2-standard-landscape-scope}
In this chapter, the phrase \emph{standard landscape} means finitely
strongly generated Koszul $\Eone$-chiral algebras on a smooth curve,
equipped with a conformal vector and finite-dimensional conformal-weight
pieces satisfying \textup{(H1)}--\textup{(H3)}. The proved families used
below are Heisenberg / free-fermion / generic-rank lattice theories
\textup{(}class~$\mathsf{G}$\textup{)}, affine Kac--Moody algebras at
generic non-critical level \textup{(}class~$\mathsf{L}$\textup{)}, and
Virasoro plus principal $\mathcal{W}_N$ at the generic parameters and
ambient stated each time \textup{(}class~$\mathsf{M}$\textup{)}. This
phrase does \emph{not} silently include parafermion $Z_k$, general
coset VOAs, non-unimodular or indefinite lattice VOAs, triplet or
symplectic-fermion logarithmic theories, or other non-semisimple
logarithmic examples unless they are named explicitly.
\end{remark}
```

### G. Replace the AP25-violating slogan at current lines `47-50`

Suggested replacement:

```tex
on the Koszul locus $\Kosz(X)\subset\Alg^{\fact,\aug,\comp}_X$ and up
to the canonical coderived correction off $\Kosz(X)$. The guiding
formula is not that ``the chiral bar is its own Koszul dual'' but that
bar--cobar inversion, Verdier duality, and graded linear duality are
three distinct operations on $\Bbarch_X(\cA)$.
```

Optionally insert immediately after this a short remark:

```tex
\begin{remark}[Three outputs of the bar coalgebra]
\label{rem:ainf2-three-functors}
For emphasis,
\[
\Omega^{\mathrm{ch}}_X\Bbarch_X(\cA)\simeq \cA,\qquad
\mathbb D_{\operatorname{Ran}(X)}\Bbarch_X(\cA)\simeq \cA^!_\infty,\qquad
\bigl(H^*(\Bbarch_X(\cA))\bigr)^\vee=\cA^!.
\]
The first is bar--cobar inversion, the second Verdier duality, and the
third graded linear duality. None implies either of the others.
\end{remark}
```

### H. Rewrite `cor:classical-A-from-A-infinity-2` proof at current lines `1173-1185`

Suggested replacement:

```tex
\begin{proof}
Apply Theorem~\ref{thm:A-infinity-2}\ref{A2-ii} and take
cohomological~$H^0$ of the resulting ambient equivalence. The
conilpotent-complete locus contains all chirally Koszul algebras by
Definition~\ref{def:chiral-koszul-pair} and
Proposition~\ref{prop:conilpotent-koszul}, so the cohomological
equivalence is on the full Koszul locus. Verdier-duality intertwining is
the pullback of Theorem~\ref{thm:A-infinity-2}\ref{A2-iv}; on the
Koszul locus this agrees with the chapter-level Verdier theorem
Theorem~\ref{thm:bar-cobar-verdier}.
\end{proof}
```

### I. Tighten the HZ-IV remark at current lines `1792-1797`

Suggested replacement:

```tex
\item \textbf{(b) Lurie HA Chapter~5.5 factorization algebras}
\cite[\S5.5]{HA}: independent $(\infty,1)$-categorical construction
of factorization algebras via the little-discs operad and
factorization envelopes. This verifies the ambient
$(\infty,1)$-categorical lane of Theorem~\ref{thm:A-infinity-2}; via
Proposition~\ref{prop:ainf2-chain-level-adjunction} and the pole-free
restriction \ref{A2-ii}, it reads back to the classical LV12
chain-level adjunction without invoking GR17 or Francis 2012's
$\star$-product.
```

## Open obstructions after this patch

1. Direct application remains blocked by sandbox permissions in the current session.

2. The adjunction-direction convention should be propagated across Vol I after inscription. This target file currently uses the ambient orientation `\Bbarch_X \dashv \Omegach_X`, while `chapters/theory/cobar_construction.tex:1973-1975` explicitly uses the strict chain-level orientation `\Omega^{\mathrm{ch}} \dashv \bar B^{\mathrm{ch}}`. The proposed proposition/theorem split makes the local distinction honest, but a follow-up grep across Vol I is still needed.

3. No build or pytest pass was run after the draft because the target repo was not writable and the request explicitly targets the manuscript source rather than the current Vol II workspace.

## AP293-positive witness

The proposed new block `prop:ainf2-chain-level-adjunction` is a genuine new proposition with proof body. It sharpens the theorem architecture by:

- separating strict chain-level adjunction from ambient `(\infty,2)` equivalence;
- preventing AP269 adjunction-strictness drift;
- unlocking a non-circular Verdier clause in `thm:A-infinity-2`.
