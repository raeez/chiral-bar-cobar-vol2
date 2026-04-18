# Deeper prescriptions for `theorem_A_infinity_2.tex`

Date: `2026-04-18`

Target read-only source:
`/Users/raeez/chiral-bar-cobar/chapters/theory/theorem_A_infinity_2.tex`

Writable output:
`/Users/raeez/chiral-bar-cobar-vol2/compute/audit/theorem_A_infinity_2_deeper_prescriptions.md`

This pass treats the six prescriptions already recorded in
`/Users/raeez/chiral-bar-cobar-vol2/compute/audit/vol1_theorem_A_infinity_2_attack_heal_2026_04_18.md`
as baseline and selects the first deeper convergent target in the user-supplied priority order.

## Convergent target

`Target 1` is the first convergent deeper target:
explicit chain-level unit/counit and their triangle identities.

Prompt-local tags: `AP269`, `AP293`, `AP306`.

Local on-disk witnesses already exist outside the target file:

- `/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1967-2049` defines the canonical counit `\psi_\cA`, the unit `\eta_\cC`, and the Hom-bijection implementing `\Omega^{\mathrm{ch}} \dashv \bar B^{\mathrm{ch}}`.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/theorem_B_scope_platonic.tex:663-678` fixes the canonical direction of the chain-level adjunction.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/theorem_B_scope_platonic.tex:766-771` already invokes one triangle identity.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/theorem_B_scope_platonic.tex:783-846` gives the explicit coalgebra-side unit map.

Those witnesses are not imported into `theorem_A_infinity_2.tex`, and that omission creates the deeper second-order gap below.

## Findings

1. `HIGH` -- no triangle-identity witness is imported into `thm:A-infinity-2`.

Anchors:
`/Users/raeez/chiral-bar-cobar/chapters/theory/theorem_A_infinity_2.tex:746-763`,
`:819-899`.

The theorem states an `(\infty,2)`-categorical adjoint equivalence, names a unit and counit, and the proof sketches free/cofree constructions plus quasi-isomorphism arguments, but nowhere records:

- the canonical chain-level unit `\eta_\cC\colon \cC \to \bar B^{\mathrm{ch}}\Omega^{\mathrm{ch}}(\cC)`,
- the canonical chain-level counit `\psi_\cA\colon \Omega^{\mathrm{ch}}\bar B^{\mathrm{ch}}(\cA) \to \cA`,
- the two triangle composites
  `\psi_{\Omega(\cC)} \circ \Omega(\eta_\cC)` and
  `\bar B(\psi_\cA) \circ \eta_{\bar B(\cA)}`,
- the ambient qualification that these identities are strict only after passage to the homotopy/localized factorization ambient.

Step 1 (`:826-845`) only says the adjunction follows from the universal property; Step 2 (`:846-866`) proves equivalence-type statements for the two maps; Step 4 (`:886-899`) immediately turns to restrictions. The missing witness is therefore not the existence of the adjunction, but the mate-identification proving that the claimed unit/counit really exhibit an adjoint equivalence in the correct ambient.

2. `HIGH` -- the downstream descent list still reuses the wrong algebra-side mate because the triangle witness was never inscribed locally.

Anchors:
`/Users/raeez/chiral-bar-cobar/chapters/theory/theorem_A_infinity_2.tex:1364-1372`.

Item `(D2)` says the first sentence of `thm:A-infinity-2` descends directly to the chain-level bar-cobar adjunction. Item `(D3)` then identifies the relevant map as the "unit of the adjunction" `\id \to \Omegach_X \Bbarch_X` and says that at a point it becomes the identity on `\cA`. That is too strong for the canonical chain-level lane already isolated elsewhere in Vol I: on the algebra side the strict adjunction map is the counit `\psi_\cA`, while the arrow `\cA \to \Omegach_X\Bbarch_X(\cA)` is only the inverse of `\psi_\cA` on the Koszul/coderived loci. Without the triangle proposition, `D2`/`D3` overstate what has actually descended.

## Prescription

Prerequisite: treat the prior agent's chain-level adjunction insertion as the baseline. If the proposition
`prop:ainf2-chain-level-adjunction`
from the earlier prescription has not been inscribed, do that first; the deeper patch below assumes it exists and then supplies the missing witness.

### A. AP293-positive deliverable

Insert immediately after the prior chain-level adjunction proposition and before current line `732`:

```tex
\begin{proposition}[Triangle identities for the chain-level chiral bar--cobar adjunction;
\ClaimStatusProvedHere]
\label{prop:ainf2-chain-triangle-identities}
Assume the notation of Proposition~\ref{prop:ainf2-chain-level-adjunction}.
For every conilpotent-complete factorization coalgebra $\cC$ and
augmented factorization algebra $\cA$, let
\[
\eta_\cC \colon \cC \longrightarrow \Bbarch_X\Omegach_X(\cC),
\qquad
\psi_\cA \colon \Omegach_X\Bbarch_X(\cA) \longrightarrow \cA
\]
be the chain-level unit and counit corresponding, under the canonical
twisting-morphism bijection, to
$\id_{\Omegach_X(\cC)}$ and $\id_{\Bbarch_X(\cA)}$ respectively.
Then the triangle composites
\[
\Omegach_X(\cC)
\xrightarrow{\Omegach_X(\eta_\cC)}
\Omegach_X\Bbarch_X\Omegach_X(\cC)
\xrightarrow{\psi_{\Omegach_X(\cC)}}
\Omegach_X(\cC)
\]
and
\[
\Bbarch_X(\cA)
\xrightarrow{\eta_{\Bbarch_X(\cA)}}
\Bbarch_X\Omegach_X\Bbarch_X(\cA)
\xrightarrow{\Bbarch_X(\psi_\cA)}
\Bbarch_X(\cA)
\]
represent the identity endomorphisms in the homotopy category of the dg
factorization model underlying Definition~\ref{def:fg-ambient}. On the
Koszul/conilpotent loci these representatives are chain-level
quasi-isomorphisms; away from those loci they become equivalences only
after passage to the coderived localisation used in
Theorem~\ref{thm:koszul-reflection}.
\end{proposition}

\begin{proof}
Theorem~\ref{thm:bar-cobar-adjunction} furnishes the canonical
Hom-bijection
\[
\Hom\bigl(\Omegach_X(\cC),\cA\bigr)
\;\cong\;
\Tw^{\mathrm{ch}}(\cC,\cA)
\;\cong\;
\Hom\bigl(\cC,\Bbarch_X(\cA)\bigr),
\]
and Proposition~\ref{prop:ainf2-chain-level-adjunction} is precisely its
factorization-level restatement. By construction, $\eta_\cC$ is the mate
of $\id_{\Omegach_X(\cC)}$, while $\psi_\cA$ is the mate of
$\id_{\Bbarch_X(\cA)}$. Applying the same bijection once more to the two
composites
\[
\psi_{\Omegach_X(\cC)}\circ \Omegach_X(\eta_\cC),
\qquad
\Bbarch_X(\psi_\cA)\circ \eta_{\Bbarch_X(\cA)}
\]
shows that they have the same mates as the respective identity
endomorphisms. Hence they equal the identity in the homotopy category:
this is exactly the triangle-identity statement for the strict
chain-level adjunction.

On the conilpotent/Koszul loci, the same natural transformations are
chain-level quasi-isomorphisms by
Theorem~\ref{thm:thm-B-coalgebra-side-unit-qi} and
Theorem~\ref{thm:bar-cobar-inversion-qi}. Off those loci,
Theorem~\ref{thm:koszul-reflection}\ref{KR-iii} is the correct ambient:
the unit and counit are not asserted as strict chain-level inverses
there, but as equivalences after passage to the coderived localisation.
\end{proof}
```

Why this is the right AP293-positive block:

- it is a genuinely new proposition with a proof body, not a scope-only rewrite;
- it upgrades the prior chain-level adjunction proposition from declaration to witnessed adjunction data;
- it localises the "strict vs homotopy/localized" issue exactly where `thm:A-infinity-2` currently blurs it.

### B. Add the ambient qualifier to `thm:A-infinity-2`

After the displayed unit/counit line at current `:758-762`, insert:

```tex
The underlying strict chain-level adjunction is the one of
Proposition~\ref{prop:ainf2-chain-level-adjunction}, and its triangle
identities are recorded in
Proposition~\ref{prop:ainf2-chain-triangle-identities}. In particular,
the equalities are claimed on the nose only after passage to the
homotopy / coderived factorization ambient named there.
```

This keeps the theorem honest without reopening the already-prescribed
adjunction-direction split.

### C. Rewrite downstream items `(D2)` and `(D3)`

Replace current lines `1364-1372` with:

```tex
\item \label{D2} Bar--cobar adjunction:
\textup{Theorem~\ref{thm:bar-cobar-adjunction}} together with
Proposition~\ref{prop:ainf2-chain-triangle-identities}. Descent:
restrict the chain-level adjunction package underlying
Theorem~\ref{thm:A-infinity-2} and then pass to cohomological
truncation.
\item \label{D3} Algebra-side counit in geometric form:
\textup{Theorem~\textup{\ref{thm:geom-unit}}}. Descent:
apply \ref{A2-ii} to the counit
\[
\psi_\cA\colon \Omegach_X\Bbarch_X(\cA)\longrightarrow\cA
\]
of the canonical chain-level adjunction. On the Koszul locus its inverse
produces the map $\cA\to\Omegach_X\Bbarch_X(\cA)$, but that inverse is
not itself a strict unit.
```

The key repair is local: stop calling the algebra-side inverse map a
unit, and make the descent depend on the new triangle-identity witness.

## AP306 convergence check for this pass

Stated scope of this pass: `Target 1` only.

- `(a)` materially stronger than baseline: yes; the file receives a new proposition giving the missing witness rather than another ambient annotation.
- `(b)` no unresolved obstruction in stated scope: yes, for the triangle-identity issue. Targets `2`-`4` remain outside this pass by prompt ordering.
- `(c)` proof hostile-reviewer robust: yes, because it imports already-inscribed unit/counit and canonical-direction witnesses instead of inventing a new mechanism.
- `(d)` numerical verification: not applicable; this patch carries no numerical claim.
- `(e)` scope qualifiers paired with boundary obstruction: yes; "strict chain level" versus "homotopy/coderived localisation" is named explicitly.
- `(f)` strongest honest form: yes; the prescription does not downgrade to vague `(\infty,2)` language when a sharper chain-level mate statement already exists on disk.
- `(g)` AP293-negative satisfied: yes; the new proposition
  `prop:ainf2-chain-triangle-identities`
  is the positive deliverable with proof body.

## Deliverable name

AP293-positive deliverable:
`prop:ainf2-chain-triangle-identities`

