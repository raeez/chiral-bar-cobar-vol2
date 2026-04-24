# Agent 11 - Vol III CY-to-Chiral / Kappa Stratification Examiner

Date: 2026-04-24.
Owned surface: `compute/audit/architecture_swarm_20260424/agent11_vol3_kappa_bridge.md` only.
Shared TeX edited: no.
Commits/pushes: no.

## Surfaces Read

- Vol II instructions: `CLAUDE.md`, `AGENTS.md`.
- Vol II required surfaces: `chapters/frame/preface.tex`,
  `chapters/theory/introduction.tex`,
  `chapters/connections/concordance.tex`,
  `chapters/frame/part_viii_synthesis.tex`, and active input graph
  anchors in `main.tex`.
- Vol III instructions and canonical anchors:
  `/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md`,
  `/Users/raeez/calabi-yau-quantum-groups/main.tex`,
  `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex`,
  `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex`.
- Focused grep targets: `kappa-stratification`, `CY-to-chiral`,
  `Phi_d`, two-stage factorisation, BKM, Borcherds/Gritsenko,
  K3/K3 x E, Mukai, `Y^+`, Drinfeld double, six routes.

## Executive Verdict

The Vol II bridge mostly knows the Vol III doctrine, but it still needs
scope hardening. The most serious defects are: unqualified/bare
`\kappa` in a cross-volume status ledger; full-vs-sparse Theorem H
concentration drift; singular "the Vol III functor" language where
Vol III now treats `{\Phi_d}` as a per-d family; a "same chain complex"
claim that outruns Vol III's CY-C conjectural status; and one-loop
Quillen normalisation missing the Vol III constant term.

The Vol II universal trace identity is directionally correct:
`\kappa_{\mathrm{BKM}} = c_N(0)/2` is not
`\kappa_{\mathrm{ch}} + \chi(\mathcal O_{\mathrm{fiber}})`.
Do not weaken that. The integration risk is the opposite: importing
Vol III's current internal drift back into Vol II. Vol III itself has
inconsistent eight-form tables in `cy_d_kappa_stratification.tex`; until
that is reconciled, Vol II should state only the five-CHL/twined slice
or cite the full eight-form catalogue without duplicating its numerical
table.

## Control Constants

- K3 x E spectrum:
  `{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}^{\mathrm{Heis}},
  \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}} = {0, 3, 5, 24}`.
  Anchors: Vol III `main.tex:828-840`, `main.tex:1444-1467`,
  `cy_d_kappa_stratification.tex:131-153`.
- Total-space K3 x E Hodge supertrace:
  `\kappa_{\mathrm{cat}}(K3 x E)=\kappa_{\mathrm{ch}}(A_{K3 x E})=0`;
  the K3 fibre value `2` is separate.
  Anchors: Vol III `main.tex:1357-1362`,
  `cy_d_kappa_stratification.tex:147-153`.
- Borcherds weight:
  `\kappa_{\mathrm{BKM}}(\Delta_5)=5` in the default denominator
  normalisation; Igusa square `\Phi_{10}=\Delta_5^2` has weight `10`.
  Anchor: Vol III `cy_to_chiral.tex:10616-10624`,
  `cy_to_chiral.tex:10636-10638`.
- Two-stage factorisation:
  `\Phi_d = \SpCh_{\Sigma_{d-1},C}\circ\PhiFA_d`; stage 1 is the
  canonical `E_d` holomorphic factorisation algebra, stage 2 is a
  specialisation, not an inverse.
  Anchors: Vol III `main.tex:604-632`, `main.tex:1352-1370`.
- At `d >= 3`, the output is `E_1`-chiral; `E_2` lives on the Drinfeld
  centre of the `E_1` representation category.
  Anchor: Vol III `main.tex:631-632`.

## ATTACK -> HEAL Cycles

### Cycle 1 - Bare `\kappa` in the Cross-Volume Ledger

ATTACK.

`chapters/connections/concordance.tex:154`,
`252-263`, `337-357`, and `679` use bare
`\kappa(\cA)` for the genus-1 curvature/modular characteristic. In a
Vol I-only paragraph this could be read as the old modular scalar. In
the current cross-volume ledger it is hazardous: Vol III hard-splits
`\kappa_{\mathrm{ch}}`, `\kappa_{\mathrm{cat}}`,
`\kappa_{\mathrm{BKM}}`, and `\kappa_{\mathrm{fiber}}`
(`/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md`, "Four
`\kappa`-invariants"). The required Vol II preface already uses
`\kappa_{\mathrm{ch}}(\cA)` for the same curvature scalar at
`chapters/frame/preface.tex:565-603`.

HEAL.

At `chapters/connections/concordance.tex:154`, `252-263`, `337-357`,
and `679`, replace the bare symbol by
`\kappa_{\mathrm{ch}}(\cA)` if the intended invariant is the chiral
modular characteristic. If a Vol I-specific scalar is intended instead,
define it on first use as `\kappa_{\mathrm{mod}}^{\mathrm{V1}}(\cA)`
and state its comparison with `\kappa_{\mathrm{ch}}`. Do not let this
ledger introduce a fifth un-subscripted kappa.

Status recommendation: moderate; notation can silently create a false
K3 x E equality.

### Cycle 2 - The Five-Archetype Table Mixes `K^\kappa` and `\kappa_{\mathrm{ch}}`

ATTACK.

`chapters/theory/introduction.tex:1897-1942` labels the functional as
bare `\kappa + \kappa^!`, then inserts the B-row ceiling
`K^\kappa=8`, while the same paragraph correctly says
`\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3\times E)=3` is separate
(`1930-1933`). Vol III's K3 x E doctrine requires four distinct
constructions, not one kappa scale:
`{0,3,5,24}` at Vol III `main.tex:828-840` and
`cy_d_kappa_stratification.tex:131-153`.

HEAL.

At `chapters/theory/introduction.tex:1902-1908`, name the table
"Theorem-C conductor/complementarity functional" rather than bare
`\kappa + \kappa^!`. In the table body, write
`\kappa_{\mathrm{ch}}+\kappa_{\mathrm{ch}}^!` for G/L/C/M rows, and
`K^\kappa=8` for the B row. Add one sentence after `1930-1933`:
`The B-row value is neither \kappa_{\mathrm{BKM}}=5 nor
\kappa_{\mathrm{ch}}^{\mathrm{Heis}}=3 nor
\kappa_{\mathrm{cat}}=0; it is the Mukai conductor
K^\kappa=2c_+(\mathrm{II}_{4,20}).`

Status recommendation: moderate; conceptually important but locally
healable.

### Cycle 3 - Universal Trace Identity Scope: Five CHL vs Eight-Form Catalogue

ATTACK.

Vol II states the trace identity on the CHL index set:
`chapters/frame/preface.tex:1973-1991` and
`chapters/theory/introduction.tex:2047-2085`. The introduction then
correctly distinguishes additive CHL weights `(5,4,3,2,1)` from twined
Borcherds weights `(5,2,1,1,1)` at `2060-2070`. The preface, however,
describes the scope as "the eight diagonal orbifolds and the STU model"
at `1983-1985` while the displayed formula uses only
`N in {1,2,3,4,6}`. Vol III separates these:
five CHL frame shapes in `cy_d_kappa_stratification.tex:2013-2029`,
and a full eight-form catalogue at `main.tex:565-579`.

There is an additional source caveat: the current Vol III
`cy_d_kappa_stratification.tex` contains mutually inconsistent
eight-form numerical tables (`155-169`, `2117-2200`, and `2394-2414`).
Vol II should not duplicate that table until Vol III is reconciled.

HEAL.

At `chapters/frame/preface.tex:1983-1985`, replace the scope phrase by:
`Scope: the five CHL/BKM-denominator frame shapes
N in {1,2,3,4,6}; the full Gritsenko-Clery eight-form catalogue,
including the non-CHL N in {5,7,8} hosts and cover assignments, is a
Vol III extension and is not used in this identity.`

At `chapters/theory/introduction.tex:2060-2070`, keep the two-family
distinction, but label the used family as "five-CHL twined Borcherds
slice" rather than "the" Vol III Borcherds catalogue.

Status recommendation: moderate. The formula is not wrong; the scope
language is too broad.

### Cycle 4 - Additive Split: Vol II Is Correct and Should Not Be Weakened

ATTACK.

`chapters/frame/preface.tex:1988-1991` and
`chapters/theory/introduction.tex:2081-2085` say
`\kappa_{\mathrm{BKM}}` does not decompose as
`\kappa_{\mathrm{ch}}+\chi(\mathcal O_{\mathrm{fiber}})` and that the
split fails at every `N in {1,2,3,4,6}`. This is the correct Vol III
doctrine in `/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md` and in
`cy_d_kappa_stratification.tex:172-185`: at `N=1`, the left side is
`5`, while the total-space right side is `0+0=0`.

Vol III `main.tex:849-852` currently says the naive decomposition is
an `N=1` numerical coincidence and fails for `N>=2`; that line is
weaker than Vol III's own CLAUDE and `cy_d_kappa_stratification.tex`.

HEAL.

Do not edit Vol II toward Vol III `main.tex:849-852`. Preserve the
strong Vol II wording. If integration touches Vol III, the correction
anchor is Vol III `main.tex:849-852`: replace "is the N=1 numerical
coincidence; it FAILS for all N >= 2" by the stronger doctrine from
`cy_d_kappa_stratification.tex:172-185`.

Status recommendation: no Vol II defect; protect this bridge.

### Cycle 5 - Theorem H CY-d Enlargement: Full Window vs Sparse Window

ATTACK.

The required Vol II surfaces disagree. The preface says
`\ChirHoch^k(\cA)=0` for `k >= d+1` and describes an enlarged window
`{0,1,...,d}` at `chapters/frame/preface.tex:438-447`. The introduction
states the sharper sparse range `{0,1,2,d}` at
`chapters/theory/introduction.tex:2280-2317`, with zero skipped degrees
`3,...,d-1`. Vol III's current summary is not strong enough to justify
the full window: `cy_to_chiral.tex:10687-10689` says the `d=3`
assignment is under H1--H4 and arbitrary CY3 morphism functoriality
remains outside the theorem; `cy_to_chiral.tex:10695-10700` only gives
output scope by dimension, not full Hochschild occupancy.

HEAL.

At `chapters/frame/preface.tex:438-447`, replace `{0,1,\ldots,d}` by
the introduction's sparse range `{0,1,2,d}` and add:
`At d=3 this is {0,1,2,3}; at d=4 it is {0,1,2,4}, not a claim that
degree 3 is occupied.` Keep `k >= d+1` as a vanishing statement only.
The status should be conditional on the Vol III H1--H4/fixed
specialisation hypotheses unless the target theorem is located and
proved in Vol III.

Status recommendation: high. The preface currently overstates the
middle-degree content.

### Cycle 6 - `{\Phi_d}` Is a Per-d Family, Not a Single Global Functor

ATTACK.

Several Vol II phrases use unqualified singular language: "the Volume
III functor `\Phi`" at `chapters/frame/preface.tex:1980-1982`,
"the Vol III functor `\Phi` extends from CY-3 to ... CY-4" at
`2281-2306`, and "Vol III CY-to-chiral functor `\Phi`" at
`2452-2482`. Vol III `main.tex:604-607` says the correspondence is a
per-d family of symmetric-monoidal assignments rather than a single
category-theoretic functor. At `d >= 3`, the output is `E_1`-chiral and
the `E_2` braiding lives on the Drinfeld centre (`main.tex:631-632`).

HEAL.

At the cited Vol II anchors, write `the family {\Phi_d}` or fix the
dimension explicitly: `\Phi_3` for `K3 x E`, `\Phi_2` for K3, and the
HK-restricted candidate `\Phi_4^{\mathrm{HK}}` for the CY4 paragraph.
Do not state "extends" at `chapters/frame/preface.tex:2281-2306`;
write "admits a conjectural HK-restricted candidate extending the
programme" to match `chapters/theory/introduction.tex:2319-2348` and
Vol III `cy_to_chiral.tex:10695-10700`.

Status recommendation: moderate/high; otherwise the text reintroduces
the single-`\Phi` antipattern Vol III explicitly removed.

### Cycle 7 - "Same Chain Complex" Outruns CY-C and Six-Route Status

ATTACK.

`chapters/theory/introduction.tex:2253-2278` says the three Vol I/II/III
descriptions "agree on the same chain complex." Vol III is more cautious:
`main.tex:712-721` marks the quantum vertex chiral group `G(X)` as
unconstructed in general, says the K3 x E six routes are six distinct
constructions producing the same `\Phi_3` output, and emphasizes they
are not six applications of `\Phi_3`. Vol III `main.tex:1470-1497`
labels the six-output isomorphism as CY-C conjectural.

HEAL.

Replace `chapters/theory/introduction.tex:2272` by:
`On the constructed K3 x E stage-2 target, the three descriptions are
compared by specified quasi-isomorphisms; the assertion that all six
routes produce the same quantum vertex chiral group is the CY-C
conjectural package of Vol III, not a theorem of the present paragraph.`

At `chapters/frame/preface.tex:2344-2346`, keep the generator-rank
stratification `\rho^{R_i}` distinct from `\kappa_{\mathrm{ch}}`, but
add `CY-C conjectural` to the six-routes clause.

Status recommendation: high. This is a status-tag defect, not a
notation issue.

### Cycle 8 - Quillen Norm Normalisation Drops the Constant

ATTACK.

Vol II writes
`\log Z^{(1)} = -\log\|\Delta_5\|_Q^2 = -\log\Delta_5 -
24 L'(0,\Delta_5,\mathrm{std})`
at `chapters/frame/preface.tex:2043-2049` and
`chapters/frame/part_viii_synthesis.tex:410-416`. Vol III's matching
normalisation includes a multiplicative constant:
`-\log\|\Delta_5\|^2_{\mathrm{Quillen}} = -\log\Delta_5
- \kappa_{\mathrm{BGS}} L'(0,\Delta_5,\mathrm{std}) + \log C`,
with `\kappa_{\mathrm{BGS}}=24`, at Vol III `main.tex:906-914`.

HEAL.

At both Vol II anchors, either add `+\log C` or state explicitly that
the Quillen metric has been normalised so that `C=1`. Prefer:
`\;-\;\kappa_{\mathrm{BGS}}L'(0,\Delta_5,\mathrm{std})+\log C,\quad
\kappa_{\mathrm{BGS}}=\chi_{\mathrm{top}}(K3)=24,`
because it keeps the BGS coefficient named and prevents accidental
identification with `\kappa_{\mathrm{BKM}}=5`.

Status recommendation: moderate. This is an exact normalisation
mismatch.

### Cycle 9 - `\Delta_5` vs `\Phi_{10}` Must Stay Normalised

ATTACK.

Vol II often moves between the Siegel character `1/\Phi_{10}` and the
default BKM weight `\Delta_5`: see `chapters/frame/preface.tex:882-887`,
`2270-2278`, `2545-2548`, and `chapters/theory/introduction.tex:2217-2220`,
`2243-2245`. These passages are mostly safe, but the integration rule
must be explicit: Vol III `cy_to_chiral.tex:10616-10624` says
`\kappa_{\mathrm{BKM}}(\Delta_5)=5`, while the Igusa-square
normalisation `\Phi_{10}=\Delta_5^2` has weight `10` and is not the
default `\kappa_{\mathrm{BKM}}` value.

HEAL.

Near the first `1/\Phi_{10}=1/\Delta_5^2` occurrence in
`chapters/frame/preface.tex:887`, add a parenthetical:
`the BKM weight used below is the default denominator normalisation
\Delta_5 of weight 5; \Phi_{10} is the square normalisation of weight
10.` Do not write `\kappa_{\mathrm{BKM}}(\Phi_{10})=5` anywhere; if
`\Phi_{10}` is named, either use weight `10` or immediately translate
back to the `\Delta_5` denominator normalisation.

Status recommendation: moderate. This prevents an exact factor-of-two
normalisation error.

### Cycle 10 - K3 AGT / Maulik--Okounkov Identification Needs Status

ATTACK.

`chapters/theory/introduction.tex:2233-2251` states that the chiral
quantum group undergirding the BKM/Siegel pair is identified with
`Y^{MO}_\hbar(\mathrm{Hilb}(K3))` at `\hbar^2=-1/8`. Vol III's current
status is weaker: `main.tex:798-818` separates the abelian
Mukai-Heisenberg presentation from a conjectural non-abelian K3 Yangian
envelope, and `cy_to_chiral.tex:10687-10689` says each `r_CY` face is a
specific construction whose invariant match must be verified per face.

HEAL.

At `chapters/theory/introduction.tex:2233-2251`, change the opening
verb from "is identified with" to:
`is conjecturally compared, on the K3 x E / Hilb(K3) constructed
stratum, with the Maulik--Okounkov quantum group...`
Then split the verified content:
`stable-envelope R-matrix comparison` / `Borcherds product character`
/ `Humbert monodromy order` should each cite the exact Vol III theorem
or be marked conjectural. Do not let this paragraph prove a global
non-abelian K3 Yangian.

Status recommendation: high. This is the main K3/Mukai status risk.

## Vol III Source Conflicts Observed

These are not Vol II edits, but they affect integration:

- Vol III `CLAUDE.md` and Vol III `main.tex:565-579` describe the
  Gritsenko-Clery eight-form spread with non-CHL `N in {5,7,8}` and
  cover assignments. Vol III `cy_d_kappa_stratification.tex` has at
  least three incompatible numerical presentations:
  `155-169`, `2117-2200`, and `2394-2414`.
- Vol III `main.tex:849-852` weakens the additive-split refutation to
  "fails for all N >= 2", while Vol III `CLAUDE.md` and
  `cy_d_kappa_stratification.tex:172-185` say it fails also at `N=1`
  under the total-space convention.
- Vol III `cy_to_chiral.tex:10653` says
  `\kch(A_2)=24`, but `cy_to_chiral.tex:10687` and
  `cy_d_kappa_stratification.tex:1016-1019` say the K3
  `\kappa_{\mathrm{ch}}` value is `2`; `24` is the Mukai-lattice rank
  / `\kappa_{\mathrm{fiber}}`, not `\kappa_{\mathrm{ch}}`.

Integration rule: for Vol II, prefer the subscripted four-invariant
discipline and avoid duplicating Vol III's conflicting tables until
Vol III is reconciled.

## Tests / Commands Run

No builds or pytest runs were performed. This task was a cross-volume
source audit. Commands used were targeted `rg`, `sed`, `nl -ba`, `wc -l`,
and `git status --short` over the assigned Vol II and Vol III surfaces.

## Residual Open Questions

- Which Vol III eight-form table is canonical for publication:
  the CLAUDE/main spread, the `cy_d_kappa_stratification.tex:2117`
  catalogue, or the `2394` corollary? Vol II should not decide this.
- Is the K3 AGT / MO comparison intended as a theorem on a constructed
  stratum, or as a conjectural bridge? The current Vol II introduction
  reads theorem-level.
- Does Vol III have a proved theorem for CY-d chiral Hochschild sparse
  concentration `{0,1,2,d}` beyond the `d=3` H1--H4 specialisation? If
  not, Vol II should keep the CY-d enlargement conditional.
