# Agent 03 Report: Relative Feynman Transform Route C

Scope owned: `compute/audit/architecture_swarm_20260424/agent03_relative_ft.md`.
No shared TeX was edited.

## Audit Surface

Route C target:
`chapters/connections/relative_feynman_transform.tex`.

Required local anchors read:

- `.claude/specs/master.md:62-65`: Route C is the algebraic skeleton between factorization and operadic routes.
- `.claude/specs/route-c-relative-ft.md:31-85`: requested definition, recognition, involutivity, derived-coderived comparison, three-routes unification.
- `chapters/connections/relative_feynman_transform.tex:971-1015`, `1224-1357`, `1539-1680`, `1717-1854`, `1929-2082`, `2454-2641`, `3292-3332`.
- `chapters/connections/modular_pva_quantization_core.tex:413-525`, `641-720`, `870-930`.
- `chapters/theory/factorization_swiss_cheese.tex:31-226`, `2042-2263`, `3478-3885`.
- `chapters/theory/modular_swiss_cheese_operad.tex:1-80`, `1249-1445`, `1478-1515`, `2783-3032`.
- `chapters/frame/preface.tex:1331-1395`, `1496-1515`.

Required Vol I anchors read:

- `/Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:2393-2443`: open-closed boundary strata and residue extraction.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex:6245-6315`: `thm:bar-modular-operad`, bar complex as `FCom`-algebra.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:194-251`: three differentials and scalar curvature projection.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:8462-8525`: Getzler-Kapranov Feynman involution, cited as proved elsewhere.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:580-617`: modular pre-Koszul datum and curved fiberwise differential.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:188-360`: provisional coderived category and Positselski filtered criterion.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/poincare_duality_quantum.tex:605-650`: Vol I definition of the Feynman transform.

## Executive Finding

Route C is true only after narrowing it to a formal algebraic skeleton over a
given modular bar datum. The current chapter repeatedly states stronger
claims: a universal recognition theorem, relative homotopy-involutivity, and
all-genus derived-coderived equivalence. Those claims are not consequences of
the cited Vol I Feynman transform, modular PVA bar construction, or
Positselski surface. They should be replaced by a minimal skeleton:

1. Input: a modular bar datum `C`.
2. Object: the completed stable-graph coalgebra `Bmod(C)`.
3. Operators: `D_0 = D_int + D_sep`, `D_1 = D_nsep`.
4. Formal theorem: `D_0^2 = D_1^2 = D_0 D_1 + D_1 D_0 = 0`.
5. Interpretation: this bicomplex is the common algebraic shadow of the local
   operadic route and the global factorization route.
6. Non-theorem: it does not determine global D-module monodromy, the Arakelov
   curved model, or derived-coderived comparison.

## ATTACK -> HEAL Cycle 1: Relative FT Definition

ATTACK.

Anchor: `relative_feynman_transform.tex:971-1015`.

The definition is circular. It defines
`\FT_{\cM\!od / \cP}(A)` as `\Bmod(A)`, then later proves that
`\Bmod(C)` is an algebra over `\FT_{\mathrm{rel}}`. Thus the object being
recognized is built into the definition.

The color data are also not coherent. At `relative_feynman_transform.tex:704-705`
the input is a modular operad and an operad `\cP`; at
`relative_feynman_transform.tex:852-864` the standard example takes
`\cP = \SCchtop`, but `\SCchtop` is already two-colored, with closed/open/mixed
operations. The formula `\SCchtop(J)` at line 860 treats it as a one-colored
open operad and loses the closed and mixed components.

Vol I support: `/Users/raeez/chiral-bar-cobar/chapters/theory/poincare_duality_quantum.tex:605-650`
defines the Feynman transform as a stable-graph sum with edge-contraction
differential. It does not identify the transform with an already-constructed
bar object of an algebra.

HEAL.

Replace the current definition by a "relative Feynman skeleton" over a modular
bar datum. Do not claim a universal quotient transform until the relative
two-colored modular-operad construction is actually built.

Exact replacement anchor:
`chapters/connections/relative_feynman_transform.tex:971-1015`.

Replacement text:

```tex
\begin{definition}[Relative Feynman skeleton]
\label{def:relative-feynman-transform}
\index{Feynman transform!relative skeleton|textbf}
Let $C$ be a modular bar datum in the sense of
Definition~\ref{def:modular-bar-datum}.  The \emph{relative
Feynman skeleton} attached to $C$ is the complete genus-filtered
stable-graph coalgebra
\[
  \FT_{\mathrm{rel}}(C)
  :=
  \prod_{[\Gamma]\in \StGraph^{\mathrm{conn}}}
  \bigl(\orline(\Gamma)\otimes
  \bigotimes_{v\in V(\Gamma)}s\,C(\mathrm{Fl}(v))\bigr)_{\Aut(\Gamma)}
\]
equipped with the two operators
\[
  D_0:=D_{\mathrm{int}}+D_{\mathrm{sep}},\qquad
  D_1:=D_{\mathrm{nsep}}.
\]
Here $D_0$ records the genus-preserving local
$\SCchtop$ bar operations, while $D_1$ records the
nonseparating modular self-sewing supplied by the
closed modular extension.  The notation
$\FT_{\Com_{\mathrm{mod}}/\SCchtop}$ means this
stable-graph skeleton, not a claim that the global
factorization algebra is recovered from the skeleton.
\end{definition}
```

Claim-status recommendation: no claim tag on the definition. The following
formal proposition can remain `\ClaimStatusProvedHere` only after it is stated
as the bicomplex identity for a given modular bar datum.

## ATTACK -> HEAL Cycle 2: Recognition Theorem

ATTACK.

Anchor: `relative_feynman_transform.tex:1224-1357`.

The theorem asserts a universal property:

- `relative_feynman_transform.tex:1231-1243`: `\FT_{\mathrm{rel}}` represents
  the functor of `\FT_{\mathrm{rel}}`-algebra structures on `\Bmod(A)`.
- `relative_feynman_transform.tex:1286-1299`: conversely, an
  `\FT_{\mathrm{rel}}`-algebra structure recovers a
  `(\Com_{\mathrm{mod}},\SCchtop)`-algebra structure on `A`.

This contradicts the chapter's own local/global warning at
`relative_feynman_transform.tex:54` and `1362-1383`: the relative skeleton
forgets D-module monodromy and period data at positive genus. Two global
factorization algebras can share the same `D_0,D_1` skeleton and differ in
global monodromy or Arakelov representative.

The proof also uses the bar-cobar adjunction at `1286-1297` as if
homotopy-Koszulity of the local operad recovered the positive-genus global
algebra. The modular operad chapter explicitly denies that implication at
`modular_swiss_cheese_operad.tex:2783-2812` and `3002-3032`.

HEAL.

Replace recognition by a formal identification theorem: given a modular bar
datum, the already constructed modular bar object carries the relative
skeleton. Do not state representability or equivalence of algebra structures.

Exact replacement anchor:
`chapters/connections/relative_feynman_transform.tex:1224-1268`.

Replacement text:

```tex
\begin{theorem}[Recognition of the relative Feynman skeleton;
\ClaimStatusProvedHere]
\label{thm:recognition-relative-ft}
Let $\cA$ be a logarithmic $\SCchtop$-algebra for which a modular
bar datum $C$ has been fixed.  Then the complete modular bar object
\[
  \Bmod(C)
\]
is canonically the relative Feynman skeleton
\[
  \FT_{\mathrm{rel}}(C)
\]
of Definition~\ref{def:relative-feynman-transform}.  Under this
identification
\[
  D_\cP=D_0=D_{\mathrm{int}}+D_{\mathrm{sep}},
  \qquad
  D_{\cM\!od}=D_1=D_{\mathrm{nsep}},
\]
and the genus filtration spectral sequence is the spectral sequence
of the bicomplex $(\Bmod(C),D_0,D_1)$.

This recognition theorem is formal.  It identifies the algebraic
skeleton carried by a chosen modular bar datum; it does not assert
that the skeleton determines the underlying factorization
$D$-module, its monodromy, or the curved Arakelov representative at
positive genus.
\end{theorem}
```

Replace the proof by a direct reference to `thm:modular-bar`,
`prop:D0D1`, and `thm:genus-completion`, ending with the warning that the
positive-genus converse is false without extra global data.

Claim-status recommendation: `\ClaimStatusProvedHere` survives only for this
formal identification. The current universal property should be removed or
restated as `\ClaimStatusConjectured` with explicit missing hypotheses.

## ATTACK -> HEAL Cycle 3: Relative Involutivity

ATTACK.

Anchor: `relative_feynman_transform.tex:1539-1680`.

The theorem claims unconditional homotopy-involutivity of
`\FT_{\Com_{\mathrm{mod}}/\SCchtop}`. The proof has three gaps.

First, separate color involutivity is not a theorem of relative mixed
involutivity. Vol I proves Getzler-Kapranov involutivity for a modular operad
at `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:8467-8480`.
It does not prove that a two-colored relative extension with directional
Swiss-cheese mixed operations is homotopy-involutive.

Second, `\FT_{\mathrm{rel}}(\FT_{\mathrm{rel}}(A))` is not defined by the
current definition. The first transform is a completed coalgebra/skeleton, not
again a `(\Com_{\mathrm{mod}},\SCchtop)`-algebra unless a cobar/dualization
functor and admissibility hypotheses are supplied.

Third, the Mittag-Leffler argument at `relative_feynman_transform.tex:1612-1634`
is invalid. Surjections of filtered complexes do not imply stabilization of
images on cohomology. The later quotients can change the image by connecting
morphisms unless one assumes finite-dimensionality, boundedness, or a
vanishing `\varprojlim^1` condition.

HEAL.

Downgrade involutivity to a conditional flat-model theorem, or move it to a
conjecture/proof obligation. The true local result is: on the conilpotent
finite-type flat locus, assuming modular homotopy-Koszulity of the full
relative two-colored extension and strong convergence of the genus filtration,
double bar-cobar/Feynman reconstruction recovers the flat algebraic object.

Exact replacement anchor:
`chapters/connections/relative_feynman_transform.tex:1539-1680`.

Replacement text:

```tex
\begin{theorem}[Conditional flat involutivity of the relative skeleton;
\ClaimStatusConditional]
\label{thm:relative-ft-involutive}
Let $\cA$ be a logarithmic $\SCchtop$-algebra with modular bar
datum $C$.  Assume:
\begin{enumerate}[label=\textup{(\roman*)}]
\item the relevant partially modular two-coloured extension is
homotopy-Koszul, including the mixed operations;
\item the completed genus filtration on $\Bmod(C)$ is separated,
complete, and satisfies the Mittag--Leffler condition on cohomology
equivalently $\varprojlim^{1}H^\ast(\Bmod(C)/F^g)=0$;
\item the second transform is interpreted through the completed
cobar/Feynman dual of the conilpotent coalgebra $\Bmod(C)$.
\end{enumerate}
Then the flat completed object satisfies
\[
  \FT_{\mathrm{rel}}^{\,2}(\cA)\simeq \cA
\]
in the derived category of complete genus-filtered flat objects.
This statement concerns the flat skeleton $(\Bmod(C),D_0+D_1)$ only.
It does not recover the curved fiberwise model
$(\barB^{(g)}(\cA),\dfib)$.
\end{theorem}
```

Claim-status recommendation: `\ClaimStatusConditional`, not
`\ClaimStatusProvedHere`, unless the mixed relative modular Koszul theorem and
the `\varprojlim^1` vanishing are proved in the chapter.

## ATTACK -> HEAL Cycle 4: Derived-Coderived Comparison

ATTACK.

Anchor: `relative_feynman_transform.tex:1717-1854` and duplicate
`relative_feynman_transform.tex:3292-3332`.

The theorem claims all-genus derived-coderived comparison for every
logarithmic `\SCchtop`-algebra. The cited support is narrower:

- Vol I `coderived_models.tex:188-360` defines a provisional coderived
  category for filtered curved factorization models with bounded-below
  filtration and specific coacyclicity criteria.
- The factorization chapter itself says the comparison is on the proved
  comparison surface, not a consequence of local homotopy-Koszulity:
  `factorization_swiss_cheese.tex:2253-2262`.
- The Route C proof admits at `relative_feynman_transform.tex:1817-1820`
  that explicit monodromy identification is proved only in genus 1.

The theorem also conflates existence of a curved object with equivalence to
the flat model. Existence of `(barB^{(g)}, dfib)` in a coderived category is
not enough to show the chiral exponential map is a coderived equivalence.

HEAL.

Replace the global theorem by a comparison principle with explicit hypotheses.
State genus 1 as the proved worked case if the local computation remains in
the chapter; state higher genus as conditional on the chiral Riemann-Hilbert
comparison and Positselski bounded-filtered criterion.

Exact replacement anchor:
`chapters/connections/relative_feynman_transform.tex:1717-1854`.

Replacement text:

```tex
\begin{theorem}[Flat-derived / curved-coderived comparison surface;
\ClaimStatusConditional]
\label{thm:derived-coderived-full}
Let $\cA$ be a logarithmic $\SCchtop$-algebra with modular bar
datum $C$.  Suppose that the factorization model on
$\Ran(\Sigma_g)\times\Ran(\R)$ is a filtered curved factorization
model in the sense of Volume~I's coderived framework, and suppose
that the chiral exponential map $\Phi_g$ has been constructed as a
filtered morphism whose associated graded is the identity.  If the
Positselski bounded-filtered criterion applies to its cone, then
\[
  \Phi_g\colon
  (\gr_F^g\Bmod(C),D_0)
  \longrightarrow
  (\barB^{(g)}(\cA),\dfib)
\]
is an isomorphism in the coderived category.  The source carries the
ordinary flat-derived invariant package; the target is its curved
coderived representative.

At genus $1$ this is the explicit Arakelov/Legendre computation.
For $g>1$ the statement depends on the higher-genus chiral
Riemann--Hilbert comparison and the bounded-filtered Positselski
hypotheses.  The relative Feynman skeleton supplies the flat
bicomplex; it does not by itself supply the curved comparison.
\end{theorem}
```

Claim-status recommendation: `\ClaimStatusConditional` globally; a separate
genus-1 proposition may be `\ClaimStatusProvedHere` if the computation is
kept and checked.

## ATTACK -> HEAL Cycle 5: Functorial Triangle and Faithfulness

ATTACK.

Anchor: `relative_feynman_transform.tex:1929-2082`.

The proposition claims:

- `Fact -> RelFT` is faithful at all genera (`1944-1949`).
- `Op -> RelFT` is faithful at all genera (`1950-1956`).

This is not compatible with the route's own premise. The functor
`Fact -> RelFT` forgets D-module connection/monodromy data (`1978-1980`).
A forgetful functor that discards monodromy is not faithful without a
rigidification assumption. The proof at `1982-1987` says `D_0,D_1` determine
all OPE and self-sewing data; that still does not determine morphisms of
factorization D-modules with nontrivial local-system or period data.

The operadic map `Op -> RelFT` also cannot be faithful as stated. Passing to
the bicomplex forgets higher homotopies and possible mixed-color coherence
data unless the operadic coalgebra is cofibrantly generated by precisely the
operations detected by `(D_0,D_1)`.

HEAL.

Replace the proposition by a comparison diagram on objects, with genus-0
equivalence and positive-genus non-full/non-faithful behavior unless extra
rigidifications are imposed.

Exact replacement anchor:
`chapters/connections/relative_feynman_transform.tex:1929-2082`.

Replacement text:

```tex
\begin{proposition}[Comparison maps to the relative skeleton;
\ClaimStatusProvedHere]
\label{prop:functorial-triangle}
There are natural assignments to the relative Feynman skeleton:
\[
  \mathbf{Fact}\longrightarrow \mathbf{RelFT},
  \qquad
  \mathbf{Op}\longrightarrow \mathbf{RelFT},
\]
defined by forgetting, respectively, the global factorization
$D$-module data and the higher local operadic presentation while
retaining the completed stable-graph bicomplex $(D_0,D_1)$.
At genus $0$ these assignments agree with the usual localization
equivalence between factorization on $\Ran(\C)$ and formal-disc
operadic data.  At genus $g\ge1$ they are comparison maps, not
equivalences in general: the factorization side contains monodromy
and period data invisible to the skeleton, while the operadic side
contains local coherence data not recorded by the pair $(D_0,D_1)$
unless a cofibrant rigid presentation has been fixed.
\end{proposition}
```

Claim-status recommendation: formal existence of comparison maps can be
`\ClaimStatusProvedHere`; faithfulness/fullness at positive genus should be
removed or made conditional on a rigidified subcategory.

## ATTACK -> HEAL Cycle 6: Chiral Exponential and Curvature Formula

ATTACK.

Anchor: `relative_feynman_transform.tex:2541-2641`, especially
`2552-2558` and `2594-2628`.

The conjugation formula
\[
  \Phi_g^{-1}\circ \dfib\circ \Phi_g
  = D_0 + D_1 + \kappa(\cA)\cdot\omega_g
\]
mixes a degree-1 differential with a degree-2 curvature term. In a curved
dg setting, the curvature belongs to the square of the differential or to the
curvature component `m_0`, not as an additive summand of the differential
unless a degree shift/suspension convention is explicitly supplied.

The proof then says the BCH series reorganizes as `D_0 + D_1 + kappa omega_g`
by the Legendre relation at genus 1 and higher-genus Riemann bilinear
relations (`2621-2628`). That is a proof of at most a worked genus-1
calculation plus a higher-genus program, not an all-genus `ProvedHere`
conjugation theorem.

HEAL.

State the comparison as a filtered map whose associated graded is the identity,
and put curvature in the square/curvature component. Reserve the stronger
formula for genus 1.

Exact replacement anchor:
`chapters/connections/relative_feynman_transform.tex:2541-2568`.

Replacement text:

```tex
\begin{proposition}[Properties of the chiral exponential map;
\ClaimStatusConditional]
\label{prop:chiral-exponential-properties}
Assume the chiral exponential map $\Phi_g$ is defined on the
completed filtered bar complex and preserves the pole-order
filtration.  Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\Phi_g$ is invertible as a filtered formal operator, with
associated graded equal to the identity.
\item If the cone of $\Phi_g$ satisfies the bounded-filtered
Positselski criterion, then $\Phi_g$ is an isomorphism in the
coderived category.
\item The curvature comparison is a statement about squares:
\[
  \bigl(\Phi_g^{-1}\dfib\Phi_g\bigr)^2
  =
  \kappa(\cA)\cdot\omega_g
\]
as the curvature component of the transported curved differential.
At genus $1$ the Legendre relation gives the explicit
$B$-cycle monodromy calculation.  For $g>1$ the corresponding
identification requires the higher-genus chiral Riemann--Hilbert
comparison.
\end{enumerate}
\end{proposition}
```

Claim-status recommendation: filtered invertibility can be `\ClaimStatusProvedHere`
if the operator is locally nilpotent on the completed filtration. The
coderived quasi-isomorphism and curvature identification are conditional
globally.

## Minimal True Route C Skeleton

The following is the strongest algebraic statement that survived all cycles.

```tex
\begin{theorem}[Relative Feynman skeleton of the modular bar complex;
\ClaimStatusProvedHere]
Let $C$ be a modular bar datum.  The completed stable-graph object
\[
  \Bmod(C)=
  \prod_{[\Gamma]\in\StGraph^{\mathrm{conn}}}
  \bigl(\orline(\Gamma)\otimes
  \bigotimes_{v\in V(\Gamma)}s\,C(\mathrm{Fl}(v))\bigr)_{\Aut(\Gamma)}
\]
carries two degree-one operators
\[
  D_0=D_{\mathrm{int}}+D_{\mathrm{sep}},
  \qquad
  D_1=D_{\mathrm{nsep}},
\]
with
\[
  D_0^2=0,\qquad D_1^2=0,\qquad D_0D_1+D_1D_0=0.
\]
The genus filtration is complete, $D_0$ preserves it, and $D_1$
raises it by one.  Its spectral sequence has
\[
  E_1^{p,q}=H^{p+q}(\gr_F^p\Bmod(C),D_0),
  \qquad d_1=[D_1].
\]
This bicomplex is the relative Feynman skeleton common to the
local operadic construction and the global factorization construction.
It records the stable-graph algebra and genus-raising obstruction
operator, but not the global $D$-module monodromy or the curved
Arakelov representative.
\end{theorem}
```

This theorem is exactly supported by:

- `modular_pva_quantization_core.tex:451-525`: `D^2=0` and the `D_0,D_1`
  split.
- `modular_pva_quantization_core.tex:641-720`: complete genus filtration
  and spectral sequence.
- Vol I `bar_cobar_adjunction_curved.tex:6245-6315`: bar complex as
  algebra over the Feynman transform of the commutative modular operad.

## Claim-Status Recommendations

- `def:relative-feynman-transform`: keep as a definition of skeleton, not a
  universal transform.
- `prop:rft-differential-identification`: keep `\ClaimStatusProvedHere` after
  narrowing to the modular bar datum.
- `thm:recognition-relative-ft`: keep `\ClaimStatusProvedHere` only for formal
  identification `Bmod(C)=FT_rel(C)` as bicomplex/skeleton; remove universal
  property.
- `thm:relative-ft-involutive`: downgrade to `\ClaimStatusConditional`.
- `thm:derived-coderived-full`: downgrade to `\ClaimStatusConditional`;
  split genus-1 proved case if desired.
- `prop:functorial-triangle`: keep only as comparison maps; remove
  positive-genus faithfulness/fullness unless rigidified.
- `prop:chiral-exponential-properties`: split filtered invertibility
  (`ProvedHere` if locally nilpotent) from coderived equivalence
  (`Conditional`).
- `thm:three-routes-equivalence`: downgrade to conditional comparison
  principle, or make it a remark summarizing the skeleton.

## Open Obligations

1. Build an actual relative two-colored modular Feynman transform for
   `(\Com_{\mathrm{mod}},\SCchtop)` rather than using `Bmod(C)` as the
   definition.
2. Prove mixed-color homotopy-Koszulity/involutivity, not just separate
   open and closed color involutivity.
3. Supply a valid strong-convergence proof for the completed genus filtration,
   including `\varprojlim^1` control.
4. Prove the chiral exponential comparison beyond genus 1, or explicitly
   restrict the theorem to genus 1 and known computed families.
5. Rigidify the factorization and operadic categories before claiming
   faithfulness of comparison functors to the relative skeleton.

## Tests and Commands

No build or test suite was run, in accordance with the session instruction not
to edit shared TeX and the repo rule against unnecessary builds. Verification
was by targeted `rg`, `nl`, `sed`, and `git status --short` reads across the
specified Route C, Route A/B, modular PVA, preface, and Vol I Feynman-transform
anchors.

## Files Changed

- `compute/audit/architecture_swarm_20260424/agent03_relative_ft.md`

