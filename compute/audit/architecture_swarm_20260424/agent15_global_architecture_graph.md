# Agent 15 -- Global Architecture/Input Graph Audit

Date: 2026-04-24

Scope: active `main.tex` ordering, `.claude/specs/*`, Vol I master synthesis
in `/Users/raeez/chiral-bar-cobar`, Vol II body proper, and the
seven-part/five-theorem architecture. This was a read-only audit except for
this report. No shared TeX/source/metadata was edited. A final grep sanity
check accidentally invoked `make` through shell command substitution in the
grep pattern; no running build process or recent standard LaTeX artifacts were
found afterward.

## Executive verdict

The current architecture is not coherent as written. The active manuscript is
an eight-part graph, while the repo-local manifesto still declares a seven-part
volume. The route specs demand a six-layer foundation ordered as
Factorization Swiss-Cheese -> Modular Swiss-Cheese -> Relative Feynman
Transform, but the active graph splits those inputs across Part I and Part IV.
The body has already repaired several mathematical claims locally, especially
AP165's "bar is not an SC coalgebra" correction, yet stale echoes in `main.tex`,
`introduction.tex`, and `line-operators.tex` still advertise the old stronger
statements.

The smallest coherent replacement is:

1. Keep seven numbered parts as the canonical architecture.
2. Convert `From Frontier to Theorem` into an unnumbered synthesis/epilogue, or
   explicitly revise every manifesto and introduction to an eight-part volume.
   The first option is smaller and preserves the seven-part doctrine.
3. Treat the six-layer route triad as a gated logical dependency:
   Route B/factorization gives the global truth; Route A/modular SC gives the
   local formal-disc model; Route C/relative FT gives the flat algebraic
   skeleton. No all-genus curved derived-coderived statement may depend on
   Route A/C alone.
4. Split Theorem C vocabulary into two distinct objects: the six-row
   cross-volume taxonomy
   `G/L/C/M/M^{ext}/B`, and the five landmark values
   `{0,8,13,250/3,98/3}`. The Vol II `G/L/C/M/FF` fingerprint is a local
   critical-level projection, not the cross-volume theorem taxonomy.
5. Regenerate metadata after source status tags are reconciled; current
   metadata records conditional relative-FT results as `ProvedHere`.

## Attack -> Heal cycles

### Cycle 1 -- Seven parts attacked by active eight-part graph

ATTACK. The repo manifesto declares seven parts:
`CLAUDE.md:48-55`. The active `main.tex` has eight numbered `\part` entries:
Part I at `main.tex:1774`, Part VII at `main.tex:2098`, and Part VIII
`From Frontier to Theorem` at `main.tex:2147`. The body also says "The volume
has eight parts" in `chapters/theory/introduction.tex:2725-2728`, and the part
summary includes Part VIII at `chapters/theory/introduction.tex:2929-2998`.

Failure. The architecture cannot simultaneously be "seven parts" and an
eight-part active input graph. This matters because the seven-part shape is
not decorative: Part VI is named as the climax and Part VII as the frontier in
`CLAUDE.md:52-55`, while Part VIII claims closure of frontiers and "Platonic
form realised" in `main.tex:2152-2183`.

HEAL. The smallest coherent heal is to keep seven numbered parts and make the
current Part VIII an unnumbered synthesis after Part VII:
`\part*{Synthesis: From Frontier to Theorem}`. Then update
`chapters/theory/introduction.tex:2725-2728` and the summary at
`chapters/theory/introduction.tex:2975-2998` to say "seven parts plus a
synthesis". If the programme intentionally wants eight parts, then
`CLAUDE.md:48-55` and every seven-part statement must be revised. The
seven-plus-synthesis option is lower churn and better preserves the stated
Vol II doctrine.

Patch priority: P0.

Status recommendation: Part VIII closure statements should remain scoped to
the non-degenerate locus. Cross-volume "Platonic form realised" language
should be `Conditional` unless the Vol I residual frontier register is also
closed.

### Cycle 2 -- Six-layer route specs attacked by active input order

ATTACK. The master route spec states the six-layer hierarchy at
`.claude/specs/master.md:9-34`, then orders the chapters as Route B primary
`factorization_swiss_cheese` at `.claude/specs/master.md:40-48`, Route A local
approximation `modular_swiss_cheese_operad` immediately after Route B at
`.claude/specs/master.md:51-60`, and Route C `relative_feynman_transform` as
the algebraic skeleton at `.claude/specs/master.md:62-65`. Route A explicitly
says to add `modular_swiss_cheese_operad` after `factorization_swiss_cheese`
at `.claude/specs/route-a-modular-sc.md:124-128`. Route C says to add
`relative_feynman_transform` after line 909/Part V at
`.claude/specs/route-c-relative-ft.md:150-157`.

Active `main.tex` does not implement that order. Route B is loaded in Part I:
`main.tex:1813`. The heptagon follows at `main.tex:1814`. Route A is not loaded
until Part IV: `main.tex:1972`. Route C is also in Part IV:
`main.tex:1984`, and it appears before `modular_pva_quantization_core` at
`main.tex:1985`, even though its proof invokes `thm:modular-bar`,
`prop:D0D1`, and `thm:genus-completion` in
`chapters/connections/relative_feynman_transform.tex:1241-1268`.

Failure. The six-layer foundation is split across Part I and Part IV, while
earlier Parts II-III can be read before the local/global scope guards supplied
by Route A/C. The relative-FT chapter is also logically downstream of modular
PVA data but appears one input before the chapter that supplies that data.
LaTeX references may resolve, but the mathematical reading order is inverted.

HEAL. The least invasive coherent architecture is to state a two-gate design:
Part I contains the HT/factorization foundation and the heptagon; Part IV opens
the modular/global gate by loading modular SC, relative FT, and modular PVA.
That requires revising `.claude/specs/master.md:40-65`,
`.claude/specs/route-a-modular-sc.md:124-128`, and
`.claude/specs/route-c-relative-ft.md:150-157` so they match the active graph.

The stronger mathematical heal is to move the route triad into logical order
before any all-genus bar-cobar claim:

```
factorization_swiss_cheese
modular_swiss_cheese_operad
modular_pva_quantization_core
relative_feynman_transform
sc_chtop_heptagon
```

This is cleaner but touches shared source order and should be coordinated with
the main thread.

Patch priority: P0 for spec/body consistency; P1 for physical reordering if
chosen.

Status recommendation: until this is fixed, all claims using Route A/C to
support curved all-genus derived-coderived equivalence should be
`Conditional`.

### Cycle 3 -- AP165 repair attacked by stale bar-as-SC echoes

ATTACK. Correct AP165 language is present in the active manuscript:
`main.tex:1259-1279` says the bar complex is an `E_1` dg coassociative
coalgebra and "the bar itself is not an `\SCchtop`-coalgebra"; the SC datum is
the derived-centre pair. `chapters/theory/foundations.tex:2335-2363` repeats
the same correction.

Stale echoes remain:

- `main.tex:1659-1665` says Vol II "reinterprets the bar complex as an algebra
  over the Swiss-cheese operad".
- `chapters/examples/rosetta_stone.tex:8-10` says the chapter proves the bar
  complex is a Swiss-cheese algebra, although the theorem below it has been
  repaired at `chapters/examples/rosetta_stone.tex:124-142`.
- `chapters/theory/introduction.tex:1419-1430` states the recognition theorem
  for a logarithmic `\SCchtop`-algebra and then identifies the bar differential
  with holomorphic factorisation and bar coproduct with topological
  factorisation without the derived-centre pair qualification.

Failure. The manuscript now contains both the correction and the old error.
This creates duplicated theorem echoes: readers can cite the older statement
from `main.tex` or `introduction.tex` against the corrected AP165 surface.

HEAL. Replace all bar-as-SC phrasing with the local AP165 form:

```
The bar complex is an E_1 chiral coassociative coalgebra. The
\SCchtop datum is the derived chiral-centre pair
(C^\bullet_ch(A,A), A); the bar is a resolution used to compute it.
```

Patch priority: P0.

Status recommendation: `thm:intro-recognition` at
`chapters/theory/introduction.tex:1419-1430` can stay `ProvedHere` only after
being rewritten as a local-shadow/derived-centre recognition theorem. If left
as a bare statement about `A` carrying the full `W(\SCchtop)` structure with
bar differential/coproduct as the two colours, downgrade to `Conditional`.

### Cycle 4 -- Homotopy-Koszul local theorem attacked by global overuse

ATTACK. The route specs are explicit that homotopy-Koszulity of
`\SCchtop` is local/formal-disc data, not the all-genus curved global theorem:
`.claude/specs/master.md:33-34`, `.claude/specs/route-a-modular-sc.md:63-80`,
and `.claude/specs/route-c-relative-ft.md:67-79`. The active factorization and
modular chapters also carry this correction locally.

Stale global overuse remains:

- `chapters/connections/line-operators.tex:64-79` states homotopy-Koszulity
  for `\SCchtop` and says the bar-cobar unit/counit for
  `\SCchtop`-algebras are weak equivalences without a local-model qualifier.
- `chapters/connections/line-operators.tex:231-254` says the bar-cobar and
  filtered bar-cobar adjunctions hold unconditionally for any logarithmic
  `\SCchtop`-algebra.
- `main.tex:1720-1732` repeats those results as unconditional for any
  logarithmic `\SCchtop`-algebra.
- `chapters/theory/introduction.tex:1439-1462` states the same bar-cobar
  Quillen equivalence after the local operadic homotopy-Koszul theorem.

Failure. The local operadic theorem is being used as if it proves the global
curved factorization theorem. This violates the central distinction in
`.claude/specs/master.md:3-7`: the local operad misses D-module monodromy,
periods, and the curvature `d_fib^2 = kappa omega_g`.

HEAL. Keep `thm:homotopy-Koszul` as `ProvedHere` for the formal-disc/local
operadic model. Rewrite every unconditional bar-cobar echo to one of:

- local flat model: `ProvedHere`;
- chirally Koszul locus: `ProvedHere` if the local hypotheses are explicit;
- curved all-genus derived-coderived model: `Conditional`, dependent on
  factorization Koszul duality and the chiral Riemann-Hilbert/Positselski
  comparison.

Patch priority: P0.

### Cycle 5 -- Status graph attacked by active conditional tags

ATTACK. The active `relative_feynman_transform.tex` has already been
downgraded:

- `thm:relative-ft-involutive` is `\ClaimStatusConditional` at
  `chapters/connections/relative_feynman_transform.tex:1456-1480`.
- `thm:derived-coderived-full` is `\ClaimStatusConditional` at
  `chapters/connections/relative_feynman_transform.tex:1549-1572`.
- `thm:three-routes-equivalence` is `\ClaimStatusConditional` at
  `chapters/connections/relative_feynman_transform.tex:2909-2942`.

Metadata disagrees:

- `metadata/claims.jsonl:1241` records `thm:relative-ft-involutive` as
  `ProvedHere`.
- `metadata/claims.jsonl:1242` records `thm:derived-coderived-full` as
  `ProvedHere`.
- `metadata/claims.jsonl:1252` records `thm:three-routes-equivalence` as
  `ProvedHere`.
- `metadata/theorem_registry.md:3-12` is a 2026-04-24 snapshot with
  `2351` `ProvedHere` claims and therefore inherits stale counts.

Failure. The status register lies about three central architecture theorems.
Any generated dependency graph or proof-status table built from it will
overstate the live theorem surface.

HEAL. Regenerate `metadata/claims.jsonl`, `metadata/theorem_registry.md`, and
any derived dependency graph after source tags settle. If regeneration is not
available, patch the three JSONL rows manually only after coordination, because
metadata is outside this audit's write scope.

Patch priority: P0.

Status recommendation: keep all three relative-FT comparison theorems
`Conditional`. `thm:recognition-relative-ft` may remain `ProvedHere` only for
recognition of the flat skeleton as a bigraded/filtered complex, not as a
curved derived-coderived equivalence.

### Cycle 6 -- Five-theorem taxonomy attacked by Vol I master synthesis

ATTACK. Vol II `CLAUDE.md:57-65` still describes Theorem C as a
five-archetype `G/L/C/M/B` landmark ceiling with values
`{0,8,13,250/3,98/3}`. The newer Vol I master synthesis distinguishes this
from the true taxonomy:

- `/Users/raeez/chiral-bar-cobar/notes/MASTER_PLATONIC_IDEAL_CROSS_VOLUME_BATTLE_HARDENED_2026_04_22.md:57-76`
  gives the six-row spine `G/L/C/M/M^{ext}/B`.
- The same file at lines `363-383` says the five values are landmarks, not a
  closed value classification; the six rows exhaust archetypes, while
  `W_{N>=4}` gives dense values inside the `M` row.

Vol II body introduces a different five-class projection:

- `main.tex:2177-2178` says Infinite Fingerprint uses `G/L/C/M/FF`.
- `chapters/frame/part_viii_synthesis.tex:365-391` presents `FF` as a fifth
  class at `kappa=0`.
- `chapters/theory/infinite_fingerprint_classification.tex:90-112` proves
  completeness by cases on `G/L/C/M/FF`.

Failure. Three different objects are being named as if they were the same
architecture: five theorem values, six archetype rows, and a five-class
fingerprint projection with critical-level `FF`. This is a cross-volume
master-synthesis/body inconsistency.

HEAL. Adopt the following vocabulary everywhere:

- Cross-volume Theorem C taxonomy: six rows `G/L/C/M/M^{ext}/B`.
- Landmark values: `{0,8,13,250/3,98/3}`.
- Vol II fingerprint projection: `G/L/C/M/FF`, a local critical-level
  projection on the standard `C_2`-cofinite landscape, not the taxonomy.

Patch priority: P0 for `CLAUDE.md`/introduction/body statements that identify
the fingerprint projection with Theorem C; P1 for local chapter wording once
the global statement is fixed.

Status recommendation: `thm:fingerprint-complete-ch` can be `ProvedHere` only
on its stated standard-landscape domain. Any claim that it closes the
cross-volume Theorem C taxonomy should be `Conditional` until it incorporates
the `M^{ext}` and `B` rows or explicitly factors through them.

### Cycle 7 -- Universal trace ladder attacked by scope collision

ATTACK. Active `main.tex:1519-1538` uses the programme-family universal trace
identity with weights `(5,4,3,2,1)` and `c_N(0)=(10,8,6,4,2)`.
Vol I master synthesis confirms this as programme-canonical at
`/Users/raeez/chiral-bar-cobar/notes/MASTER_PLATONIC_IDEAL_CROSS_VOLUME_BATTLE_HARDENED_2026_04_22.md:257-260`.

But Vol II `CLAUDE.md:494-508` names an eight-form Gritsenko--Clery spread as
"universal" and says the modular PVA chapters use
`kappa_BKM(Phi_N)=c_N(0)/2` with the eight-form cover assignment. The Vol I
master synthesis at lines `257-260` separates four ladders: programme,
singly-twined, physical CHL, and Clery-Gritsenko eight-form. It says the
programme ladder is canonical for all three volume climaxes.

Failure. The word "universal" is overloaded. The programme UTI ladder and the
Clery-Gritsenko eight-form atlas are both legitimate, but they are different
families. Treating the eight-form atlas as the universal trace identity changes
the value set used by the climax.

HEAL. Use two explicit scope labels:

- "programme-canonical UTI ladder": `(5,4,3,2,1)` at
  `N in {1,2,3,4,6}`, with `c_N(0)=(10,8,6,4,2)`;
- "Clery-Gritsenko eight-form atlas": weights
  `{5,2,1,1,1/2,1,1/4,0}`, with cover assignment.

Patch priority: P1.

Status recommendation: programme UTI can stay as currently scoped in
`main.tex:1519-1538`; statements making the eight-form atlas universal for
all three volume climaxes should be `Conditional` or rephrased as an atlas
parallel to the programme ladder.

## Dependency failures

1. `main.tex:1813`, `main.tex:1972`, and `main.tex:1984-1985` violate the
   route-spec dependency order in `.claude/specs/master.md:40-65`.
2. `chapters/connections/relative_feynman_transform.tex:1241-1268` invokes
   modular PVA inputs that are loaded one line later in `main.tex:1985`.
3. `main.tex:1659-1665` contradicts the AP165 correction in
   `main.tex:1259-1279` and `chapters/theory/foundations.tex:2335-2363`.
4. `chapters/connections/line-operators.tex:231-254`,
   `main.tex:1720-1732`, and `chapters/theory/introduction.tex:1439-1462`
   globalize local homotopy-Koszulity beyond the route specs' scope.
5. `metadata/claims.jsonl:1241-1242` and `metadata/claims.jsonl:1252`
   contradict active source tags in `relative_feynman_transform.tex`.
6. `CLAUDE.md:57-65` and the current fingerprint chapters conflate the
   six-row taxonomy, five landmark values, and local `G/L/C/M/FF` projection.
7. `CLAUDE.md:494-508` and `main.tex:1519-1538` use different "universal"
   Borcherds ladders unless the scope labels are made explicit.

## Duplicated or stale theorem echoes

| Echo | Current anchor | Conflict | Recommendation |
|---|---|---|---|
| Bar complex as SC algebra | `main.tex:1659-1665`; `chapters/examples/rosetta_stone.tex:8-10` | Correct AP165 guard at `main.tex:1259-1279` and `foundations.tex:2335-2363` | Rewrite to `E_1` coalgebra + derived-centre pair |
| Unqualified recognition | `chapters/theory/introduction.tex:1419-1430` | Bar differential/coproduct phrasing lacks derived-centre pair qualification | Rewrite or downgrade |
| Global bar-cobar Quillen equivalence from local HK | `line-operators.tex:64-79`, `line-operators.tex:231-254`, `main.tex:1720-1732`, `introduction.tex:1439-1462` | Route specs require local/global separation | Scope to local flat model; curved comparison conditional |
| Five-archetype Theorem C | `CLAUDE.md:57-65` | Vol I master six-row taxonomy at lines `57-76` and `363-383` | Split six rows from five landmark values |
| Part VIII closure | `main.tex:2147-2196`, `chapters/theory/introduction.tex:2725-2728` | Seven-part manifesto at `CLAUDE.md:48-55`; Vol I residual frontiers at master lines `257-277` | Make unnumbered synthesis or revise manifesto globally |
| Metadata `ProvedHere` statuses | `metadata/claims.jsonl:1241-1242`, `metadata/claims.jsonl:1252` | Active source says `Conditional` | Regenerate metadata |

## Patch priority

P0:

- Resolve seven-part vs eight-part architecture.
- Reconcile route specs with active input order, or reorder the route inputs.
- Remove bar-as-SC stale echoes.
- Scope homotopy-Koszul/bar-cobar claims to local flat vs curved global.
- Fix metadata status drift for relative FT.
- Split Theorem C six-row taxonomy from five landmark values and the Vol II
  `G/L/C/M/FF` projection.

P1:

- Scope programme UTI ladder vs Clery-Gritsenko eight-form atlas.
- Repair `introduction.tex` part summary and reading-path text after deciding
  seven-plus-synthesis vs eight numbered parts.
- Add a short route-order note at the opening of Part IV if modular SC and
  relative FT remain physically located there.

P2:

- Regenerate derived diagrams and tables after P0/P1 changes.
- Align legacy comments and source-only headers that do not enter the PDF but
  mislead future grep-driven audits.

## Status-tag recommendations

| Label/surface | Recommended status | Reason |
|---|---|---|
| `thm:homotopy-Koszul` | `ProvedHere`, explicitly local/formal-disc | Operadic statement is local; global curvature invisible to it |
| `thm:bar-cobar-adjunction` | `ProvedHere` only for local flat/logarithmic operadic model; otherwise `Conditional` | Current echoes overstate the global curved case |
| `thm:filtered-koszul` | Same as above | Depends on the same local/global distinction |
| `thm:intro-recognition` | `ProvedHere` after rewrite; otherwise `Conditional` | Needs derived-centre pair qualification |
| `thm:relative-ft-involutive` | `Conditional` | Active source already has this at `relative_feynman_transform.tex:1456-1480` |
| `thm:derived-coderived-full` | `Conditional` | Active source already has this at `relative_feynman_transform.tex:1549-1572` |
| `thm:three-routes-equivalence` | `Conditional` | Active source already has this at `relative_feynman_transform.tex:2909-2942` |
| `thm:fingerprint-complete-ch` | `ProvedHere` for standard `C_2`-cofinite landscape only | Not the cross-volume Theorem C taxonomy |
| Part VIII "Platonic form realised" | `Conditional` outside the non-degenerate Vol II locus | Vol I master still records residual frontiers |

## Greps and read-only checks run

No intentional build or test suite was run. During the final sanity check, a
grep pattern containing backticks around `make` triggered shell command
substitution. Follow-up checks found no running build process and no recent
standard LaTeX artifacts under the top two directory levels:

```bash
pgrep -af 'pdflatex|latexmk|tectonic|make' || true
find . -maxdepth 2 -type f \( -name '*.aux' -o -name '*.log' -o -name '*.toc' -o -name '*.out' -o -name '*.fls' -o -name '*.fdb_latexmk' \) -mmin -2 -print
```

Representative read-only commands:

```bash
sed -n '1,240p' CLAUDE.md
git status --short
rg -n -F '\part{' main.tex
rg -n -F '\input{' main.tex
rg --files .claude/specs
nl -ba .claude/specs/master.md | sed -n '1,120p'
nl -ba .claude/specs/route-a-modular-sc.md | sed -n '1,140p'
nl -ba .claude/specs/route-b-fact-sc.md | sed -n '1,140p'
nl -ba .claude/specs/route-c-relative-ft.md | sed -n '1,160p'
nl -ba main.tex | sed -n '1248,1284p'
nl -ba main.tex | sed -n '1648,1736p'
nl -ba main.tex | sed -n '1768,1822p'
nl -ba main.tex | sed -n '1960,1990p'
nl -ba main.tex | sed -n '2090,2200p'
nl -ba chapters/theory/foundations.tex | sed -n '2334,2368p'
nl -ba chapters/theory/introduction.tex | sed -n '1416,1466p'
nl -ba chapters/theory/introduction.tex | sed -n '2718,2735p;2924,3000p'
nl -ba chapters/connections/line-operators.tex | sed -n '36,84p;228,258p'
nl -ba chapters/connections/relative_feynman_transform.tex | sed -n '1236,1268p;1452,1484p;1546,1572p;2906,2942p'
nl -ba metadata/claims.jsonl | sed -n '1236,1256p'
nl -ba metadata/theorem_registry.md | sed -n '1,18p'
rg -n 'relative-ft-involutive|derived-coderived-full|three-routes-equivalence|ClaimStatusConditional|ClaimStatusProvedHere' chapters/connections/relative_feynman_transform.tex metadata/claims.jsonl metadata/theorem_registry.md
nl -ba /Users/raeez/chiral-bar-cobar/notes/MASTER_PLATONIC_IDEAL_CROSS_VOLUME_BATTLE_HARDENED_2026_04_22.md | sed -n '50,85p'
nl -ba /Users/raeez/chiral-bar-cobar/notes/MASTER_PLATONIC_IDEAL_CROSS_VOLUME_BATTLE_HARDENED_2026_04_22.md | sed -n '250,282p'
nl -ba /Users/raeez/chiral-bar-cobar/notes/MASTER_PLATONIC_IDEAL_CROSS_VOLUME_BATTLE_HARDENED_2026_04_22.md | sed -n '355,390p'
```

## Final architecture replacement

Use this as the stable replacement graph:

```text
Seven numbered parts:
I   Open Primitive: HT/factorization foundation; local SC shadow; AP165 guard.
II  E_1 Core: ordered bar and line operators, scoped to local/chirally Koszul input.
III Seven Faces of r(z): GRT torsor and spectral-braiding faces.
IV  Characteristic Datum and Modularity: modular SC, modular PVA, relative FT.
V   HT Landscape: examples and physical families.
VI  3D Quantum Gravity: climax, programme-canonical UTI ladder.
VII Frontier: conditional and scope-boundary items.

Unnumbered synthesis after VII:
From Frontier to Theorem: closed non-degenerate-locus frontiers,
Koszulness moduli, and Infinite Fingerprint, explicitly not a replacement
for the seven-part spine.
```

The theorem spine then reads:

```text
A: bar-cobar, local/flat unless factorization hypotheses are present.
B: chiral Positselski, coderived when curvature is present.
C: six-row taxonomy G/L/C/M/M^{ext}/B plus five landmark values.
D: obstruction-tower universality, scoped to the admissible comparison locus.
H: Hochschild concentration, excluding critical/FF unless separately proved.
```

This replacement preserves the active mathematical repairs, removes the
part-count contradiction, and prevents the local operadic theorem from being
used as a proof of the global curved factorization theorem.
