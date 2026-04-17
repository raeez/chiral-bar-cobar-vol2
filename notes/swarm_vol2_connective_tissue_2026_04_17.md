# Adversarial audit: Vol II connective tissue (swarm agent #4 of 5, 2026-04-17)

Target: `/Users/raeez/chiral-bar-cobar-vol2/`. Hard no-touch constraint honoured (read-only of `main.tex`, `preface.tex`, `part_viii_synthesis.tex`, etc.). Mandate: transitions, signposts, framing between chapters and Parts.

---

## 1. Part-introduction inventory

`main.tex` opens each `\part{...}` block with a `\noindent`-anchored prose paragraph that acts as an inlined Part preamble. A separate dedicated \*chapter\*-level introduction file exists for only two Parts (VI and VIII). The table classifies each.

| Part | Title | Inline `\noindent` preamble in `main.tex`? | Dedicated introduction CHAPTER file? | LOC | Quality |
|------|-------|-------------------------------------------|--------------------------------------|-----|---------|
| I | The Open Primitive | YES (main.tex 1336-1363, ~28 lines) | NO (prose delegated to `chapters/theory/foundations.tex` §1.1 "The primitive datum") | n/a | Adequate: preamble opens with a \*problem\* ("primitive datum of a 3d HT theory") |
| II | The $E_1$ Core | YES (main.tex 1385-1413, ~28 lines) | NO | n/a | Adequate: opens with ordered bar as the Swiss-cheese open-colour native object |
| III | Faces of $r(z)$: a $\mathrm{GRT}_1(\Q)$-torsor | YES (main.tex 1431-1442, ~12 lines) | NO (the FIRST chapter `dnp_identification_master.tex` is itself a master theorem, not an introduction) | n/a | UNDER-SIGNPOSTED. Preamble lists seven guises but never unpacks \*why\* the seven-face torsor is a GRT$_1(\Q)$-torsor. The headline ("a $\mathrm{GRT}_1(\Q)$-torsor") is dropped immediately. This is Part III's \*headline promise\*; it should get its own introductory chapter. |
| IV | Characteristic Datum and Modularity | YES (main.tex 1457-1482, ~25 lines) | NO | n/a | Adequate for modularity framing but does not situate the 19 chapter inputs; reader drops from 25 lines of framing into `rosetta_stone.tex` (a 1000+-line worked computation) with no bridge. |
| V | Standard HT Landscape | YES (main.tex 1512-1526, ~14 lines) | NO (the FIRST chapter `ht_physical_origins.tex` functions semi-introductorily but is a proper technical chapter opened with "4d/2d correspondence algebras") | n/a | MISSING. Part V is the most physically loaded ("Yang--Mills boundary packages, celestial and twisted holography, logarithmic monodromy") and the preamble tries to do all the work in 14 lines. No dedicated introduction. |
| VI | Three-Dimensional Quantum Gravity (CLIMAX) | YES (main.tex 1551-1581, ~30 lines) | **YES**: `chapters/connections/part_vi_platonic_introduction.tex` (586 lines) | 586 | STRONG. Platonic introduction opens with CG-deficiency ("Classical 3d QG recognizes ONE stress tensor"), unpacks E$_\infty$-ladder. Best-signposted Part. |
| VII | Frontier | YES (main.tex 1608-1614, ~7 lines) | NO | n/a | MINIMAL. Seven chapter inputs ride on a single paragraph stating "no earlier part depends on this." |
| VIII | From Frontier to Theorem | YES (main.tex 1635-1667, ~33 lines) | **YES**: `chapters/frame/part_viii_synthesis.tex` (483 lines, FIRST input) | 483 | STRONG (newly inscribed). Maps 4 closed frontiers to named theorems. |

**Finding F1.1:** Only Parts VI and VIII have chapter-length introductions. Parts I--V and VII rely entirely on 7--28 line `\noindent` preambles in `main.tex`.

**Finding F1.2 (critical, AP106 adjacent):** Part III's GRT$_1(\Q)$-torsor headline is the single most intellectually novel piece of architecture in Vol II and receives only a 12-line prose block.

**Finding F1.3:** Part V (26 chapter inputs — the largest) receives only a 14-line preamble.

---

## 2. Opening-paragraph typology (10 sampled chapters)

Classification: (a) problem opening (CG-valid), (b) definition opening, (c) "This chapter constructs..." (AP106 forbidden), (d) theorem-statement opening, (e) AI slop / HZ-10 violation.

| # | File | First substantive paragraph | Class | Evidence |
|---|------|------------------------------|-------|----------|
| 1 | `chapters/theory/foundations.tex` | "Vol~I worked pointwise... What is the correct primitive datum for the open sector of a 3d HT theory, and what is its operadic home?" | (a) problem | Ends with explicit question; CG-compliant |
| 2 | `chapters/connections/bar-cobar-review.tex` | "The bar complex $\barB(\cA)$ classifies \emph{twisting morphisms}..." | (b) definition | Opens with what the object IS, not what problem it solves |
| 3 | `chapters/connections/line-operators.tex` | "Line operators in 3d HT quantum field theories are identified with modules for..." | (d) theorem-statement | First sentence IS a theorem claim; no deficiency preamble |
| 4 | `chapters/connections/spectral-braiding-core.tex` | "The Yangian $Y(\fg)$ is the universal quantization of... Yet the RTT formalism that defines it treats the spectral parameter as a formal variable... None of these are explained." | (a) problem | Exemplary CG deficiency opening |
| 5 | `chapters/connections/dnp_identification_master.tex` | "The collision residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{\cA})$ of an $\SCchtop$-algebra $\cA$ has seven equivalent realizations..." | (b) definition + (d) theorem | Announces result in first sentence; no deficiency |
| 6 | `chapters/connections/hochschild.tex` | "Bulk observables admit a geometric interpretation via chiral Hochschild cohomology, developed here through..." | (c) **AP106 violation**: "developed here" = "This chapter constructs..." re-worded |
| 7 | `chapters/examples/rosetta_stone.tex` | "The Heisenberg algebra~$\cH_k$ has shadow depth $r_{\max} = 2$ (class~G), so $\Theta^{\mathrm{oc}}$ terminates at degree~2. Every projection is computed in closed form..." | (d) theorem-statement | Result-list opening; AP109 adjacent |
| 8 | `chapters/examples/w-algebras-virasoro.tex` | "W-algebras have shadow depth $r_{\max} = \infty$, so the $\Ainf$ tower $\{m_k\}$ is genuinely infinite..." | (d) theorem-statement | Same pattern as Rosetta |
| 9 | `chapters/connections/ht_physical_origins.tex` | "String amplitudes, gauge theory partition functions, and conformal blocks each produce bar-cobar structures..." | (b) definition + list | Directly lists 3 origins without framing the problem |
| 10 | `chapters/connections/3d_gravity.tex` | "\subsubsection*{The deficiency} Three-dimensional pure gravity with negative cosmological constant has no propagating degrees of freedom. The bulk is empty..." | (a) problem | EXEMPLARY: explicit deficiency subsection; gold standard |

**Scorecard:** (a) problem 3/10 — foundations, spectral-braiding, 3d_gravity. (b) definition 3/10. (c) AP106 violation 1/10 (hochschild.tex "developed here through dimensional descent" — soft violation but counts). (d) theorem-statement 4/10 — line-operators, dnp_identification_master, rosetta_stone, w-algebras-virasoro. (e) AI slop 0/10 (HZ-10 clean on openings; em dashes and hedging absent).

**Finding F2.1:** 3 chapters open with a genuine CG deficiency. 4 chapters open with a theorem/result-statement, which the Vol I CLAUDE.md flags as AP109 adjacent ("Never list results before proving"). The overall opening discipline is uneven.

**Finding F2.2:** `w-algebras-virasoro.tex` is a `\section` (not `\chapter`), suggesting it was never intended to stand alone; yet it is a direct `\input` in main.tex under Part IV. The section-vs-chapter distinction leaks through the architecture.

---

## 3. Missing transitions (chapter-to-chapter, Part-to-Part)

Between any two consecutive `\input{...}` lines in main.tex, I find **zero** transitional bridge prose across all eight Parts. Every inter-chapter join is atomic.

Examples within Part II (E$_1$ Core):
```
\input{chapters/connections/bar-cobar-review}         % ends with bar-cobar adjunction
\input{chapters/connections/line-operators}          % opens "Line operators in 3d HT QFT are..."
\input{chapters/connections/ordered_associative_chiral_kd_core}
\input{chapters/connections/dg_shifted_factorization_bridge}
```
The reader goes from bar--cobar adjunction (a general statement) directly to line operators (a specific interpretation) with no bridge sentence. The eight chapters of Part II have eight independent openings.

### Part-to-Part transitions (top 3 requested)

**Part III $\to$ Part IV** (Faces of $r(z)$ $\to$ Characteristic Datum): main.tex 1453-1482 has a `\noindent` preamble for Part IV that opens with "Each algebra family in Volume~I's standard landscape is a test case..." — this DOES mention the preceding Part but only implicitly, via the phrase "four-functor table" referencing the seven faces only in passing. The bridge is weak: no sentence of the form "Part III's $r(z)$ now specializes to each family; Part IV executes the specialization."

**Part IV $\to$ Part V** (Characteristic Datum $\to$ HT Landscape): main.tex 1508-1526 preamble for Part V opens with "The Koszul triangle (boundary $\cA$, bulk $\mathcal{Z}^{\mathrm{der}}_{\mathrm{ch}}$, lines $\mathcal{C}_{\mathrm{line}}$) of Part~\ref{part:bbl-core}..." — good reference to Part III but SKIPS Part IV entirely. The reader who just read the modularity sweep (Part IV) is thrown back to Part III. This is a structural skip.

**Part V $\to$ Part VI** (HT Landscape $\to$ 3D QG CLIMAX): main.tex 1547-1581 preamble is 30 lines, dense and well-formed; opens with the Brown--Henneaux specialization. GOOD BRIDGE. This is the only Part-to-Part transition with genuine connective tissue, and it exists because Part VI has a real introduction chapter backing it.

**Finding F3.1:** Zero inter-chapter bridge paragraphs across 2638 lines of main.tex. Every chapter is an atomic `\input`.

**Finding F3.2:** Part IV $\to$ V transition skips over Part IV, referencing only Part III's Koszul triangle; this is a CROSS-PART SKIP pattern.

---

## 4. Signposting failures (chapters that delay announcing their goal)

Forward-pointer audit: does each chapter say "We prove X, stated precisely in Theorem Y" in its opening paragraph?

- `foundations.tex`: the first subsection (§1.1) ends with a question ("What is the correct primitive datum...?") and does NOT point forward to a named theorem; the reader must parse §§1.1--1.4 before encountering `thm:recognition-foundations` at line 1462. DELAY: ~1400 lines of prose before the main result.
- `hochschild.tex`: opens with "Bulk observables admit a geometric interpretation..." — no pointer to the main `thm:bulk-chiral-hochschild` (which is the chapter's headline). Reader wanders.
- `celestial_holography_core.tex`: opens with a 6-line summary of Kaluza--Klein reduction; the "Problem, restated at its true level" subsection does not arrive until §2 (line ~50). Acceptable but the bullet list in §2 would benefit from earlier placement.
- `brace.tex`: opens with "The chiral Hochschild cochain complex ... carries operadic brace operations from the Swiss-cheese cooperad" — announces the result in sentence 1. GOOD.
- `spectral-braiding-core.tex`: opens with 3 deficiencies and the resolution in paragraph 2. GOOD.
- `3d_gravity.tex`: opens with a named "The deficiency" subsection. EXEMPLARY.

**Finding F4.1:** Chapters that cover general theory (foundations, hochschild, unified_chiral_quantum_group) tend to delay their main theorem pointer by thousands of lines. Chapters that have been Chriss-Ginzburg-rectified (3d_gravity, spectral-braiding-core, part_vi_platonic_introduction) announce within paragraph 1-2.

**Finding F4.2:** Delayed signposting correlates strongly with chapters NOT yet touched by the UPGRADE-SWEEP or CG-rectification waves.

---

## 5. Abstract-vs-Body discrepancies

Claimed (preface + introduction + CLAUDE.md headline):

- "The SC$^{\mathrm{ch,top}}$ pentagon has been upgraded to a HEPTAGON" (reconstitution claim)
- "Seven Theorems" (UPGRADE-SWEEP claim)
- "Eight Parts" (Part VIII inscribed)
- "E$_\infty$-topologization is the true climax, not E$_3$" (Part VI Platonic introduction)

Executed (main.tex actual input structure):

- Part III headline is "Faces of $r(z)$: a $\mathrm{GRT}_1(\Q)$-torsor" but the 12-line preamble only lists seven guises — never names the GRT$_1(\Q)$-torsor theorem or cites `grt_parametrized_seven_faces.tex`. The preamble promises torsor, the chapter inputs deliver nine guises (per the unified CLAUDE.md), but the reader never sees the torsor action explicitly in the preamble.
- Part V headline is "The Standard HT Landscape" but 14-line preamble. Nine chapter inputs (YM boundary, YM higher-body, YM instanton, celestial holography, log HT monodromy, anomaly-completed, thqg holographic reconstruction, thqg modular bootstrap, holomorphic-topological) — no orientation map between them.
- The preface advertises CLIMAX = E$_\infty$-topologization but the Part VI preamble (main.tex 1551-1581) still frames the climax as E$_3$-topological. The Platonic introduction chapter (`part_vi_platonic_introduction.tex`) upgrades the framing to E$_\infty$, but the reader of main.tex encounters the preamble FIRST and the Platonic introduction SECOND — the ladder has a confusing order.
- Part VIII inscription claims "the four irreducible opens are closed on the non-degenerate locus" but the Part VIII preamble (main.tex 1635-1667) fails to name the four opens until paragraph 2. The synthesis chapter names them in §1. Redundant claim-before-naming structure.

**Finding F5.1:** Preface's HEPTAGON / SEVEN-THEOREMS / EIGHT-PARTS / E$_\infty$-CLIMAX claims are technically honoured in main.tex but NOT echoed in the `\noindent` Part preambles. The architecture upgrade lives in individual chapters (`sc_chtop_heptagon.tex`, `part_vi_platonic_introduction.tex`, `part_viii_synthesis.tex`) but has not propagated into the main.tex scaffolding.

---

## 6. Concrete connective-tissue inscriptions proposed

For each deficit in §§1--5, propose a short framing paragraph ($\le$100 words) and location.

**C6.1 (F1.2, F5.1): Part III torsor introduction.** NEW chapter `chapters/connections/part_iii_platonic_introduction.tex` (~500 lines, modeled on `part_vi_platonic_introduction.tex`). Opening paragraph ($\le$100 words):
> The collision residue $r(z)$ has one identity and many guises. Part II constructed it as the degree-2 E$_1$ MC datum; Part III reads it through nine presentations — bar hub, DNP $R$-twist, KZ r-matrix, GZ Hamiltonians, Yangian r-matrix, Sklyanin bracket, Gaudin Hamiltonian, Brown motivic face, Willwacher operadic face. The nine are not independent: they form a single $\mathrm{GRT}_1(\Q)$-torsor, with every two presentations related by a Drinfeld-associator action $\Phi_{ij} \in \mathrm{GRT}_1(\Q)$. Part III constructs this torsor, identifies the orbit representatives, and proves the action is transitive on Q-rational faces.

Insert this chapter at main.tex line 1443 BEFORE `dnp_identification_master`.

**C6.2 (F1.2, F3.2): Part V orientation chapter.** NEW chapter `chapters/connections/part_v_platonic_introduction.tex`. Opening ($\le$100 words):
> The Koszul triangle of Part III — boundary $\cA$, bulk $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, lines $\cC_{\mathrm{line}}$ — acquires depth in Part V through the standard HT landscape: nine concrete chapter instantiations. Three Yang--Mills variants (boundary, higher-body, instanton) exhibit the triangle at affine Kac--Moody boundary; celestial and twisted holography lift the triangle to modular completion; logarithmic HT monodromy globalizes it on ordered configuration spaces; anomaly completion organizes the genus-dependent obstruction; thqg holographic reconstruction and modular bootstrap close the chain-level triangle on class M via the DS--Hochschild bridge.

Insert at main.tex line 1528 BEFORE `ht_physical_origins`.

**C6.3 (F3.1): Part II inter-chapter bridges.** Replace 8 atomic `\input` lines at main.tex 1415-1424 with 7 single-sentence `\noindent` bridges (one between each consecutive pair). Example: between `bar-cobar-review` (bar--cobar adjunction) and `line-operators` (modules for $\cA^!_{\mathrm{line}}$):
> \noindent With the bar--cobar adjunction in place, we turn to the objects it classifies: line operators, the first concrete incarnation of $E_1$ Koszul duality on the open colour.

Apply to all eight Parts — ~70 one-sentence bridges across main.tex, budgeting ~50 LOC total.

**C6.4 (F4.1): Chapter forward-pointer retrofits.** For foundations.tex, hochschild.tex, universal_holography_functor.tex: insert 2-sentence "What this chapter proves" signpost WITHOUT violating AP111 (the violation is "What this chapter proves" as a block header; a forward-pointer in prose is fine). Template ($\le$100 words per chapter):
> The main result, stated in Theorem~\ref{thm:X} and proved in §Y, is that Z. Before the proof we develop the ambient formalism in §§A--B, fix conventions in §C, and verify the Heisenberg special case in §D; the argument proper occupies §Y.

**C6.5 (F5.1): Part VI preamble upgrade.** Rewrite main.tex 1551-1581 preamble to OPEN with the E$_\infty$-topologization climax (matching `part_vi_platonic_introduction.tex`) rather than the Brown--Henneaux Virasoro specialization. Target: 30 lines restating the Platonic introduction's §0--§2 compressed:
> The climax of this volume is not E$_3$-topological but E$_\infty$-topological. Three-dimensional quantum gravity with asymptotic Virasoro symmetry is the $N=2$ rung of an infinite ladder; $\cW_N$ occupies rung $N-1$; $\cW_\infty$ occupies the Platonic endpoint. Each inner higher-spin stress tensor $T^{(n)}$ adds one $E_1$-topological factor via Dunn additivity; the full Bakas--Pope--Romans tower commutes them all into $E_\infty$-topological. Part VI proves the N=2 rung explicitly; the ladder to $\infty$ is stated as climax extension at chain level.

**C6.6 (F1.3): Part VII preamble.** Current 7-line preamble expand to ~20 lines naming the seven chapter inputs and their conditional status:
> The Frontier collects seven conditional theorems: three spectral-braiding frontier results (Yangian Koszul depth, celestial asymptotic braiding, modular-bootstrap H$^2$), the celestial boundary transfer beyond wedge, conditional examples of class M chain-level, non-tempered W(p) triplet, and two strictly-conjectural W-algebra extensions. Each depends on additional analytic input beyond the logarithmic $\SCchtop$ framework; each has a candidate proof-path identified in the HEAL-SWEEP; each is reviewed in the Beilinson-rectified open frontiers ledger (§"Open Frontiers" in CLAUDE.md).

---

## Campaign summary

The connective tissue of Vol II is strong at the \*chapter\* level (individual openings like 3d_gravity.tex, spectral-braiding-core.tex, part_vi_platonic_introduction.tex are exemplary CG-deficient openings) and very weak at the \*scaffolding\* level (Part preambles, inter-chapter bridges, cross-Part transitions). Two Parts have real introductions (VI, VIII, totalling 1069 LOC of dedicated framing); six Parts rely on 7--28 line `\noindent` preambles. Zero inter-chapter transitional paragraphs exist across 2638 lines of main.tex.

Six concrete inscriptions (C6.1--C6.6) would repair the principal deficits: two new Part-introduction chapters (III and V), ~70 one-sentence inter-chapter bridges, forward-pointer retrofits in three general-theory chapters, a Part VI preamble E$_\infty$ upgrade, and a Part VII preamble expansion. Total new LOC $\approx$ 1200 (comparable to `part_vi_platonic_introduction.tex` alone). The upgrade would bring scaffolding-level connective tissue into parity with chapter-level rectification already achieved.
