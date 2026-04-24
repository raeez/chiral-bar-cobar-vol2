# Agent 01 - Factorization Primary / BD-CG Examiner

Owned file: `compute/audit/architecture_swarm_20260424/agent01_factorization_primary.md`

## Verdict

The tested claim is true only after a substantial scope correction.

Corrected core:

1. The primary all-genus architecture should be a colored holomorphic-topological factorization object on the mixed open-closed Ran/configuration geometry, not literally on `Ran(Sigma_g) x Ran(R)`.
2. `SC^{ch,top}` is the formal-disc collision model extracted from that geometry. It is not the global governing object at higher genus, but it is not disposable: it is the exact local OPE/Wick/topologisation calculus.
3. The existing chapter overstates three bridges as proved: the global BD-CG mixed comparison, local-to-global recovery from the formal-disc shadow, and all-genus factorization Koszul recovery from Getzler-Kapranov involutivity. These should be `ClaimStatusConditional` or `ClaimStatusConjectured`.
4. Curvature must be separated from ordinary D-module flatness. The scalar lane `d_fib^2 = kappa(A) omega_g` is an anomaly/projective-family curvature statement, not the curvature of a BD D-module connection on the curve.

## Surfaces Read

Vol II:

- `CLAUDE.md`
- `AGENTS.md`
- `.claude/specs/master.md`
- `.claude/specs/route-b-fact-sc.md`
- `chapters/theory/factorization_swiss_cheese.tex`
- `chapters/theory/foundations.tex`
- `chapters/theory/introduction.tex`
- `chapters/theory/axioms.tex`
- `chapters/connections/line-operators.tex`
- `chapters/connections/dg_shifted_factorization_bridge.tex`
- `main.tex` input and bibliography region

Vol I Route B dependencies:

- `/Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex`
- `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex`

External primary/source anchors checked:

- Beilinson-Drinfeld, *Chiral Algebras*, AMS page: https://bookstore.ams.org/coll-51
- Francis-Gaitsgory, *Chiral Koszul duality*, arXiv:1103.5803: https://arxiv.org/abs/1103.5803
- Costello-Gwilliam, *Factorization Algebras in Quantum Field Theory*, Cambridge page: https://www.cambridge.org/core/books/factorization-algebras-in-quantum-field-theory/9597AFE8E8767F8F38A73C74B8F2501B
- Lurie, *Higher Algebra*: https://www.math.ias.edu/~lurie/papers/HA.pdf
- Positselski, *Two kinds of derived categories...*, arXiv:0905.2621: https://arxiv.org/abs/0905.2621
- Getzler-Kapranov, *Modular operads*, arXiv:dg-ga/9408003: https://arxiv.org/abs/dg-ga/9408003

## Finding Register

Fatal findings:

1. `Ran(Sigma_g) x Ran(R)` is not the correct global HT configuration object. A point of the product is a pair of finite subsets, not a finite set of product points or a colored open-closed configuration. It loses incidence data and boundary attachment.
2. The current BD-CG equivalence theorem claims a global equivalence with local model algebras over `C_*(FM_bullet(X))`. That cannot be right at `g >= 1`, where monodromy, periods, and global descent data are precisely the information not seen by the formal-disc operad.
3. The curvature language in the BD construction treats a D-module connection as if it could have `nabla_A^2 = kappa(A) omega_g`. A D-module connection is flat; the nonzero scalar class belongs to the family/anomaly/curved-bar lane, not to the ordinary BD connection on `X`.
4. The all-genus factorization Koszul theorem imports Getzler-Kapranov involutivity beyond its range. `FT^2 ~= id` for modular operads does not by itself prove global BD/CG factorization recovery, Positselski coderived convergence, or mixed HT descent.
5. The current Chiral Riemann-Hilbert chain-map statement from a square-zero dg object to a curved object is inconsistent unless the curvature acts trivially on the image. This should be a curved/coderived comparison, not an ordinary chain map.

Moderate findings:

1. Genus-zero local-to-global is overstated. It can be a theorem for translation/rational/formal-disc-determined objects under explicit hypotheses; it is not a theorem for arbitrary factorizable D-modules on `P^1` or `A^1`.
2. The phrase "only the local formal-disc shadow" should be retained only as a scope declaration. Repo doctrine gives equal status to chain-level and categorical lanes; the local shadow is the exact local theorem, not a lesser object.
3. `foundations.tex` already contains the healthier mixed open-closed geometry and global-descent conjecture; `factorization_swiss_cheese.tex` should import that structure instead of replacing it with `Ran(Sigma_g) x Ran(R)`.

## ATTACK -> HEAL Cycle 1: What BD Actually Gives

Claim attacked: A chiral algebra is simply a factorizable D-module on Ran, so the operadic object is only a local shadow.

Attack:

BD gives chiral algebras through D-modules on a curve with chiral operations, and the factorization reformulation is a theorem under the relevant unital/factorization hypotheses. Francis-Gaitsgory extends the chiral/factorization comparison in a homotopical setting. This does not imply that every global factorizable D-module is determined by its formal-disc operad, nor that the local operad is mathematically secondary.

Local anchors:

- `chapters/theory/factorization_swiss_cheese.tex:35-48`
- `chapters/theory/factorization_swiss_cheese.tex:219-248`
- `chapters/theory/factorization_swiss_cheese.tex:1725-1767`
- `chapters/theory/foundations.tex:265-320`
- `chapters/theory/foundations.tex:2436-2499`

Heal:

Replace the opening thesis at `chapters/theory/factorization_swiss_cheese.tex:35` with:

```tex
\noindent
The primary global object in this chapter is a coloured
holomorphic-topological factorisation datum on the mixed Ran geometry of
the curve and the topological line.  In the closed holomorphic direction
this is the Beilinson--Drinfeld/Francis--Gaitsgory factorisation
D-module formulation of chiral algebra; in the open topological
direction it is the locally constant factorisation-algebra formulation
of an $E_1$-algebra.  The two-coloured operad
$\SCchtop$ is the formal-disc collision model extracted from this
global object.  It is therefore local, not global; it is also exact at
the level where OPEs, Wick contractions, topologisation maps, and
Swiss-cheese boundary operations are computed.
```

Status recommendation:

- BD/FG closed chiral-factorization comparison: `ClaimStatusProvedElsewhere`.
- Local formal-disc extraction of `SC^{ch,top}`: `ClaimStatusProvedHere` only for product-formal local rectangle data.
- Global recovery from local shadow: `ClaimStatusConjectured` unless the chapter states extra descent and regularity hypotheses.

## ATTACK -> HEAL Cycle 2: `Ran(Sigma_g) x Ran(R)` Is the Wrong Space

Claim attacked: Factorization on `Ran(Sigma_g) x Ran(R)` is the primary architecture.

Attack:

The product of Ran spaces is not the Ran space of the product and is not the mixed open-closed configuration space. A point of `Ran(Sigma_g) x Ran(R)` is a pair `(S,T)`, which suggests all rectangular pairs `S x T`; it does not encode a finite set of points in `Sigma_g x R`, nor the boundary incidence relation of open points. BD D-modules also live in the algebraic/holomorphic direction; the real line is a Costello-Gwilliam/Lurie locally constant direction, not a BD D-module direction.

The better object already exists in Vol I and Vol II: open-closed configurations
`Conf^{oc}_{k,\vec m}(X,D,tau) = C_k(X \setminus D) x prod_j Conf^{ord}_{m_j}(I_{p_j})`
and the corresponding open-closed convolution differential
`D^{oc} = d_int + [tau,-] + d_sew + d_pf + hbar Delta + d_bdy + d_mix`.

Local anchors:

- `chapters/theory/factorization_swiss_cheese.tex:755-862`
- `chapters/theory/factorization_swiss_cheese.tex:2053-2066`
- `chapters/theory/foundations.tex:126-156`
- `chapters/theory/foundations.tex:1925-1965`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:2037-2077`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:2698-2760`

Heal:

Insert before `chapters/theory/factorization_swiss_cheese.tex:750`:

```tex
\begin{definition}[Mixed HT Ran geometry]
\label{def:mixed-ht-ran-geometry}
Let $\Sigma_g$ be the holomorphic curve and let $I \subset \mathbb R$
be the topological boundary interval.  The mixed
holomorphic-topological Ran geometry $\Ran^{\mathrm{oc}}_{\HT}(\Sigma_g,I)$
is the coloured Ran/configuration prestack whose $(k,m)$-stratum is
\[
  \Conf_k(\Sigma_g \setminus D)\times
  \Conf_m^{\mathrm{ord}}(I),
\]
with the evident variants for several boundary intervals.  Closed
collisions are governed by the Beilinson--Drinfeld Ran/factorisation
D-module structure on $\Sigma_g$; open collisions are governed by the
locally constant factorisation structure on $I$; mixed boundary
collisions are the module strata.  The notation
$\Ran(\Sigma_g)\times\Ran(\mathbb R)$ is used only as a mnemonic for
separate holomorphic and topological directions, not as the global
parameter space.
\end{definition}
```

Replace `chapters/theory/factorization_swiss_cheese.tex:2062-2066` with:

```tex
\item[\textup{(i)}] The bar construction forms a factorisation
coalgebra over the coloured mixed geometry
$\Ran^{\mathrm{oc}}_{\HT}(\Sigma_g,I)$, or equivalently over its
open-closed configuration strata
$\Conf_k(\Sigma_g\setminus D)\times\Conf_m^{\mathrm{ord}}(I)$ after
choosing the boundary interval.  No assertion is made that the global
object is a factorisation coalgebra on the literal product
$\Ran(\Sigma_g)\times\Ran(\mathbb R)$.
```

Status recommendation:

- Definition of mixed HT Ran/configuration geometry: `ClaimStatusProvedHere` as a definition aligned with Vol I.
- Global Weiss descent for arbitrary covers: `ClaimStatusConjectured`.

## ATTACK -> HEAL Cycle 3: Curvature Is Not D-Module Curvature

Claim attacked: Higher genus curvature is monodromy/curvature of the factorizable D-module connection.

Attack:

A D-module connection is flat. Nontrivial monodromy around cycles is compatible with flatness, but it is not curvature. The Vol I scalar lane says the curved bar/family differential has scalar projection
`d_fib^2 = kappa(A) omega_g` and, globally, `obs_g(A)=kappa(A) lambda_g` for uniform-weight scalar cases. Vol I also warns that this is the scalar projection of a full Maurer-Cartan/family datum, with cross-channel corrections in multi-weight examples. The current text repeatedly blurs three objects:

- the flat BD D-module connection on the curve;
- the Arakelov or propagator form on a fixed curve;
- the Hodge/moduli class `lambda_g` or `lambda_1` controlling scalar genus obstruction.

Local anchors:

- `chapters/theory/factorization_swiss_cheese.tex:43-48`
- `chapters/theory/factorization_swiss_cheese.tex:864-881`
- `chapters/theory/factorization_swiss_cheese.tex:1125-1167`
- `chapters/theory/factorization_swiss_cheese.tex:1340-1454`
- `chapters/theory/foundations.tex:3251-3259`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:194-247`
- `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:909-920`
- `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:4703-4712`

Exact formulas/constants from landscape:

- Scalar lane: `d_fib^2 = kappa(A) omega_g`.
- Cohomology class: `obs_g(A)=kappa(A) lambda_g`.
- Uniform-weight scalar coefficient: `F_g(A)=kappa(A) lambda_g^{FP}`.
- `lambda_g^{FP} = ((2^{2g-1}-1)/2^{2g-1}) |B_{2g}|/(2g)!`.
- `lambda_1^{FP}=1/24`, `lambda_2^{FP}=7/5760`.
- Multi-weight correction: `F_g = kappa lambda_g^{FP} + delta F_g^{cross}` for `g >= 2`.

Heal:

Replace `chapters/theory/factorization_swiss_cheese.tex:864-881` with:

```tex
\begin{remark}[Curvature lane]
\label{rem:factorization-curvature-lane}
The BD factorisation $D$-module on a fixed curve is flat in the
$D$-module sense.  The nonzero class used in the higher-genus bar
construction is not the curvature of that connection.  It is the
projective/family anomaly of the genus tower after the propagator
normalisation has been chosen.  On the proved scalar lane this anomaly
has projection
\[
  d_{\mathrm{fib}}^2=\kappa(\cA)\,\omega_g,
  \qquad
  \operatorname{obs}_g(\cA)=\kappa(\cA)\lambda_g,
\]
with the scalar numerical integral
$F_g(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}$ for uniform-weight
examples.  For multi-weight algebras the scalar term is only the first
projection; the cross-channel correction
$\delta F_g^{\mathrm{cross}}$ must be retained.
\end{remark}
```

Status recommendation:

- Genus-one scalar curvature for standard uniform-weight examples: `ClaimStatusProvedHere` where the computation is present.
- All-genus scalar lane for uniform-weight examples as imported from Vol I: `ClaimStatusProvedElsewhere`.
- Full multi-weight/global curvature reconstruction: `ClaimStatusConditional` or `ClaimStatusConjectured`, depending on whether the local computation has been supplied.

## ATTACK -> HEAL Cycle 4: BD-CG Mixed Equivalence Overclaim

Claim attacked: The chapter proves an equivalence between BD factorizable D-modules, CG holomorphic prefactorization algebras, and local `C_*(FM_bullet(X))` models.

Attack:

The theorem conflates three comparison levels:

1. BD/FG closed holomorphic chiral-factorization comparison.
2. CG/Lurie locally constant/topological factorization comparison.
3. The mixed holomorphic-topological boundary comparison.

The first two are external theorems under their own hypotheses. The third is not proved by applying Riemann-Hilbert on each `Ran_k(X)` and Kunneth. The local formal-disc model is a functor out of the global object; it is not globally equivalent at higher genus, exactly because periods, monodromy, and descent data survive.

Local anchors:

- `chapters/theory/factorization_swiss_cheese.tex:1725-1767`
- `chapters/theory/factorization_swiss_cheese.tex:1769-1864`
- `chapters/theory/foundations.tex:2436-2499`
- `chapters/theory/foundations.tex:1925-1965`
- Francis-Gaitsgory arXiv abstract: chiral/factorization equivalence in homotopical setting.
- Costello-Gwilliam book description: factorization algebras as local-to-global objects organizing field theory data.

Heal:

Replace theorem `thm:BD-CG-equivalence` at `chapters/theory/factorization_swiss_cheese.tex:1725` with:

```tex
\begin{theorem}[BD--CG comparison, scoped form;
\ClaimStatusConditional]\label{thm:BD-CG-equivalence-scoped}
Let $\Sigma_g$ be a smooth curve and let $I$ be the topological
boundary interval.
\begin{enumerate}[label=\textup{(\roman*)}]
\item The closed holomorphic sector is governed by the
Beilinson--Drinfeld/Francis--Gaitsgory chiral-factorisation
comparison for unital factorisation $D$-modules on $\Ran(\Sigma_g)$.
\item The open topological sector is governed by the
Costello--Gwilliam/Lurie/Ayala--Francis locally-constant
factorisation comparison on $I$, hence by $E_1$-algebras.
\item The mixed open-closed sector admits a local comparison after
formal completion along product-formal collision rectangles.  Under
this completion the extracted local operations are precisely the
$\SCchtop$ formal-disc operations.
\end{enumerate}
The theorem does not assert that arbitrary global mixed
BD-factorisation data are equivalent to their local
$\SCchtop$ shadows.  That stronger statement requires a coloured
Ran-space descent theorem for holomorphic-topological boundary
factorisation algebras and is recorded separately as conjectural.
\end{theorem}
```

Replace the proof opening at `chapters/theory/factorization_swiss_cheese.tex:1769` with:

```tex
\begin{proof}
Parts \textup{(i)} and \textup{(ii)} are imported comparison theorems,
with their hypotheses left explicit.  For \textup{(iii)}, restrict the
mixed factorisation datum to a product-formal rectangle
$D_z\times I_t$ and complete along the closed, open, and mixed
collision diagonals.  The closed completed collision strata identify
with the Fulton--MacPherson strata of the formal disc; the open strata
identify with ordered intervals; the mixed strata give the usual
Swiss-cheese module faces.  This produces a functor from the mixed
factorisation datum to a $W(\SCchtop)$-algebra.  The construction is
local and functorial.  Full faithfulness or essential surjectivity for
global objects is not used here and is not claimed.
\end{proof}
```

Status recommendation:

- Current `ClaimStatusProvedHere` should be replaced by `ClaimStatusConditional`.
- Add a separate conjecture for full mixed BD-CG descent with `ClaimStatusConjectured`.

## ATTACK -> HEAL Cycle 5: Factorization Koszul Duality Is Only Local Without Extra Hypotheses

Claim attacked: Factorization Koszul duality recovers the all-genus global object from `SC^{ch,top}` via Feynman transform involutivity.

Attack:

Getzler-Kapranov involutivity is a theorem about the Feynman transform of modular operads. Vol I supplies an algebraic modular-operad lane for the bar genus tower and a coderived Positselski lane. Neither theorem automatically proves global BD/CG factorization recovery for the mixed HT object. The present theorem also begins from the wrong base space (`Ran(Sigma_g) x Ran(R)`).

Local anchors:

- `chapters/theory/factorization_swiss_cheese.tex:2046-2096`
- `chapters/theory/factorization_swiss_cheese.tex:2119-2263`
- `chapters/connections/line-operators.tex:64-218`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex:6251-6299`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:8467-8515`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:581-617`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:1-120`

Heal:

Replace theorem opening at `chapters/theory/factorization_swiss_cheese.tex:2053` with:

```tex
\begin{theorem}[Local factorisation Koszul duality and global
obstructions; \ClaimStatusConditional]
\label{thm:factorization-koszul-scoped}
Let $\cA$ be a Koszul $A_\infty$ chiral algebra in the product-formal
scope of Theorem~\ref{thm:BD-CG-equivalence-scoped}.
\begin{enumerate}[label=\textup{(\roman*)}]
\item The formal-disc collision shadow of the mixed factorisation
datum is controlled by the homotopy Koszul dual of
$\SCchtop$; equivalently, the local bar-cobar construction is the
$\SCchtop$ collision calculus.
\item The genus tower carries the modular-operad/Feynman-transform
structure described in Vol.~I, with recovery on the Koszul locus in
the appropriate completed coderived category.
\item Recovering an arbitrary global mixed HT factorisation object
from its local $\SCchtop$ shadow is not a formal consequence of
\textup{(i)} or \textup{(ii)}.  It requires the coloured Ran descent
and mixed BD--CG comparison hypotheses.
\end{enumerate}
\end{theorem}
```

Status recommendation:

- Local homotopy-Koszulity of `SC^{ch,top}`: `ClaimStatusProvedHere` where the line-operator/local proof supplies it.
- Modular Feynman-transform involution: `ClaimStatusProvedElsewhere`.
- All-genus global recovery of mixed HT factorization data: `ClaimStatusConjectured` pending the descent theorem.

## ATTACK -> HEAL Cycle 6: "Only Local Shadow" Must Not Demote the Chain-Level Lane

Claim attacked: `SC^{ch,top}` is only a local formal-disc shadow.

Attack:

As a warning against global overreach this phrase is useful. As architecture it is too coarse. The repo doctrine says the chain-level and `(infty,1)`-categorical lanes are equal status. The local formal-disc operad is exactly where pole orders, OPE residues, Wick contractions, boundary associahedra, and topologisation maps are computed. The right distinction is global versus local, not real versus shadow.

Local anchors:

- `CLAUDE.md` chain-level/`(infty,1)` equal-status section
- `AGENTS.md` same doctrine
- `chapters/theory/factorization_swiss_cheese.tex:35-48`
- `chapters/theory/foundations.tex:1969-2397`
- `chapters/theory/foundations.tex:2436-2499`
- `chapters/theory/introduction.tex:407-435`
- `chapters/theory/axioms.tex:95-138`

Heal:

Insert before the end of the remark at `chapters/theory/axioms.tex:134`:

```tex
This operadic formulation is the local formal-disc formulation of the
theory.  It is not a replacement for the global Beilinson--Drinfeld or
Costello--Gwilliam factorisation object on the mixed Ran geometry, and
the global object is not recovered from the local one without descent
hypotheses.  Conversely, the local operad is not merely bookkeeping: it
is the exact chain-level collision calculus in which the
$A_\infty$ operations, OPE poles, boundary associahedra, and
topologisation maps are computed.
```

Status recommendation:

- Keep local operadic results as proved when the proof is local.
- Add "local formal-disc/product-formal scope" to theorem statements whose current wording reads globally.

## ATTACK -> HEAL Cycle 7: Curved Riemann-Hilbert Cannot Be an Ordinary Chain Map

Claim attacked: Chiral Riemann-Hilbert gives a quasi-isomorphism from an honest dg coalgebra to a curved dg coalgebra with nonzero curvature.

Attack:

If `D_0^2=0`, `D_g^2 = kappa omega_g`, and `Phi D_0 = D_g Phi`, then applying squares gives
`0 = D_g^2 Phi = kappa omega_g Phi`. Unless the curvature vanishes on the image, this is not an ordinary chain map in the category of dg complexes. It must be stated as a curved/coderived comparison, a twisting by a Maurer-Cartan element, or a comparison after passing to the determinant-line/projective connection package.

Local anchors:

- `chapters/theory/factorization_swiss_cheese.tex:3497-3541`
- `chapters/theory/factorization_swiss_cheese.tex:3607-3692`
- `chapters/theory/foundations.tex:3344-3540`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:1-120`
- Positselski source anchor above.

Heal:

Replace the chain-map sentence in `chapters/theory/factorization_swiss_cheese.tex:3510-3527` with:

```tex
There is a comparison in the curved coderived category between the
single-valued Arakelov-normalised model and the multivalued period
model.  Concretely, the comparison is represented by a twisting datum
$\Phi_g$ satisfying the curved intertwining equation in the
Positselski coderived sense; it is not an ordinary chain map from a
square-zero complex to a complex with nonzero curvature unless the
curvature class acts trivially on the image.
```

Status recommendation:

- Curved/coderived comparison: `ClaimStatusConditional`.
- Any ordinary quasi-isomorphism statement at nonzero `kappa omega_g`: downgrade or add the vanishing hypothesis.

## Replacement Core Theorem

Recommended chapter-level replacement for Route B, insertable after the opening definitions in `chapters/theory/factorization_swiss_cheese.tex`:

```tex
\begin{theorem}[Scoped factorisation architecture for Vol.~II;
\ClaimStatusConditional]
\label{thm:scoped-factorisation-architecture}
Let $\Sigma_g$ be a smooth curve and let $I$ be the topological
boundary interval.  A Vol.~II holomorphic-topological open-closed datum
is a coloured factorisation object on
$\Ran^{\mathrm{oc}}_{\HT}(\Sigma_g,I)$: a closed
Beilinson--Drinfeld factorisation $D$-module on $\Ran(\Sigma_g)$, an
open locally constant Costello--Gwilliam factorisation algebra on
$I$, and mixed boundary module structure on the open-closed collision
strata.  Formal completion along product-formal collision rectangles
extracts a $W(\SCchtop)$-algebra.  This extraction is the local
Swiss-cheese collision calculus.  It is not asserted to be globally
essentially surjective or fully faithful outside the stated
product-formal/descent hypotheses.

On the scalar curvature lane the genus-family bar differential obeys
$d_{\mathrm{fib}}^2=\kappa(\cA)\omega_g$ and
$\operatorname{obs}_g(\cA)=\kappa(\cA)\lambda_g$ in the scope proved
in Vol.~I.  This is a projective/family anomaly statement, not the
curvature of the flat BD $D$-module connection on the fixed curve.
\end{theorem}
```

## Exact Claim-Status Recommendations

- `factorization_swiss_cheese.tex:35-48`: retain thesis only with the scoped theorem above; global factorization primary is `ClaimStatusConditional`, not absolute.
- `factorization_swiss_cheese.tex:1725` (`thm:BD-CG-equivalence`): change from `ClaimStatusProvedHere` to `ClaimStatusConditional`; split external proved sectors from conjectural mixed descent.
- `factorization_swiss_cheese.tex:2053` (`Factorization Koszul duality...`): change to `ClaimStatusConditional`; all-genus global recovery should be `ClaimStatusConjectured`.
- `factorization_swiss_cheese.tex:3497` (`Chiral Riemann-Hilbert correspondence...`): change to `ClaimStatusConditional` and phrase in curved coderived category.
- `introduction.tex:1419-1437`: recognition theorem should match `foundations.tex` and be `ClaimStatusConditional` with product-formal local-shadow scope.
- `axioms.tex:95-138`: add local-shadow scope paragraph.
- `axioms.tex:938-1249`: keep operad-to-axioms and axioms-to-operad only for local formal-disc/product-formal `W(SC^{ch,top})` algebras.

## Constants and Formula Discipline

No new formula was invented. Exact formulas used above were read from Vol I/Vol II surfaces:

- `d_fib^2 = kappa(A) omega_g` from Vol II/Vol I scalar curved-bar lane.
- `obs_g(A)=kappa(A) lambda_g` from Vol I `landscape_census.tex:4703-4708`.
- `F_g(A)=kappa(A) lambda_g^{FP}` and multi-weight correction `delta F_g^{cross}` from `landscape_census.tex:909-920`.
- `lambda_g^{FP} = ((2^{2g-1}-1)/2^{2g-1}) |B_{2g}|/(2g)!` from `landscape_census.tex:4709-4712`.
- `lambda_1^{FP}=1/24`, `lambda_2^{FP}=7/5760` from `landscape_census.tex:4719-4725`.
- `kappa(Vir_c)=c/2`, `S_4=10/[c(5c+22)]`, `Delta=40/(5c+22)`, and Zamolodchikov norm `c(5c+22)/10` from `landscape_census.tex:461-489`.
- Affine universal vacuum formula `kappa(V_k(g)) = dim(g)(k+h^\vee)/(2h^\vee)` from `landscape_census.tex:875-877`.

## Commands Run

Representative command surface:

```bash
sed -n '1,240p' CLAUDE.md
sed -n '241,620p' CLAUDE.md
sed -n '1,330p' AGENTS.md
sed -n '1,260p' .claude/specs/master.md
sed -n '1,260p' .claude/specs/route-b-fact-sc.md
git status --short
git diff --stat
git diff -- chapters/theory/foundations.tex chapters/theory/introduction.tex main.tex | sed -n '1,260p'
wc -l chapters/theory/factorization_swiss_cheese.tex chapters/theory/foundations.tex chapters/theory/introduction.tex chapters/theory/axioms.tex
nl -ba chapters/theory/factorization_swiss_cheese.tex | sed -n '31,250p'
nl -ba chapters/theory/factorization_swiss_cheese.tex | sed -n '746,1490p'
nl -ba chapters/theory/factorization_swiss_cheese.tex | sed -n '1492,2315p'
nl -ba chapters/theory/factorization_swiss_cheese.tex | sed -n '3490,3545p'
nl -ba chapters/theory/foundations.tex | sed -n '87,320p'
nl -ba chapters/theory/foundations.tex | sed -n '1762,1965p'
nl -ba chapters/theory/foundations.tex | sed -n '2436,2689p'
nl -ba chapters/theory/foundations.tex | sed -n '3248,3765p'
nl -ba chapters/theory/introduction.tex | sed -n '100,176p'
nl -ba chapters/theory/introduction.tex | sed -n '407,435p'
nl -ba chapters/theory/introduction.tex | sed -n '1419,1570p'
nl -ba chapters/theory/axioms.tex | sed -n '41,138p'
nl -ba chapters/theory/axioms.tex | sed -n '919,1250p'
nl -ba chapters/connections/line-operators.tex | sed -n '1,225p'
nl -ba chapters/connections/dg_shifted_factorization_bridge.tex | sed -n '1,260p'
rg --files /Users/raeez/chiral-bar-cobar | rg 'configuration_spaces\\.tex$|landscape_census\\.tex$|higher_genus_foundations\\.tex$|bar_cobar_adjunction_curved\\.tex$'
nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex | sed -n '2030,2095p'
nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex | sed -n '2696,2768p'
nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex | sed -n '1,120p'
nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex | sed -n '194,258p'
nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex | sed -n '8460,8525p'
nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex | sed -n '560,750p'
nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '6240,6315p'
nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex | sed -n '461,489p'
nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex | sed -n '875,922p'
nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex | sed -n '4700,4728p'
rg -n '\\input\\{|factorization_swiss_cheese|foundations|introduction|axioms|dg_shifted_factorization_bridge|line-operators' main.tex chapters -g '*.tex'
```

External source checks were done for the primary anchors listed above.

No build was run; the prompt requested an audit report and forbade shared TeX edits.

## Files Changed

- Added `compute/audit/architecture_swarm_20260424/agent01_factorization_primary.md`.

No shared TeX file was edited.
