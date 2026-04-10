# Vol II MC5 Status Sweep

Canonical truth (from Vol I `chapters/connections/editorial_constitution.tex:179`):

> MC5 is not fully proved. What is proved at all genera is the analytic
> HS-sewing package (Theorem thm:general-hs-sewing + Theorem
> thm:heisenberg-sewing). The remaining genuswise BV/BRST/bar
> identification is still conjectural; at genus 0 the algebraic BRST/bar
> comparison is proved (Theorem thm:algebraic-string-dictionary);
> tree-level amplitude pairing requires Corollary
> cor:string-amplitude-genus0.

## Files touched

1. `CLAUDE.md` (Vol II cross-volume bridge table).
2. `chapters/connections/thqg_line_operators_extensions.tex` (MC
   hierarchy list).
3. `chapters/connections/concordance.tex` (research signal 3 on
   higher-genus $A_\infty$ structure).

All other occurrences of "MC5" / "MC5 proved" in Vol II were already
qualified with the canonical wording ("analytic HS-sewing lane proved
at all genera; full genuswise BV/BRST/bar identification conjectural")
by earlier sessions.

## Diffs

### 1. `CLAUDE.md:83` (W-algebras bridge row)

Before:

    | W-algebras | Feynman-diag m_k matches bar diff | MC5 | Proved g=0; conj g>=1 |

After:

    | W-algebras | Feynman-diag m_k matches bar diff | MC5 | Analytic HS-sewing proved at all genera; genuswise BV/BRST/bar identification conjectural (g=0 algebraic BRST/bar comparison proved) |

### 2. `chapters/connections/thqg_line_operators_extensions.tex:1241-1242`

Before:

    \item MC5 (all-genera sewing): partition functions converge.
      \textbf{Proved} (Theorem~\ref*{thm:general-hs-sewing}).

After:

    \item MC5 (all-genera sewing): partition functions converge.
      \textbf{Analytic HS-sewing proved at all genera}
      (Theorem~\ref*{thm:general-hs-sewing});
      the full genuswise BV/BRST/bar identification remains
      conjectural.  At genus~$0$ the algebraic BRST/bar comparison
      is proved
      (Vol~I, Theorem~\ref*{V1-thm:algebraic-string-dictionary}),
      and the tree-level amplitude pairing is conditional on
      Vol~I, Corollary~\ref*{V1-cor:string-amplitude-genus0}.

### 3. `chapters/connections/concordance.tex:659` (research signal 3)

Before (relevant fragment):

    \emph{Status: Resolved at all genera} (Volume~I, MC5 proved).

After:

    \emph{Status: Analytic lane of MC5 proved at all genera; the
    full genuswise BV/BRST/bar identification remains conjectural.}
    ... subject to the conjectural genuswise BV/BRST/bar
    identification.

## Files audited but not touched (already canonical)

- `chapters/connections/concordance.tex`: cross-volume bridge row at
  lines 144-145 already says "analytic HS-sewing proved at all genera,
  ...; genuswise BV/BRST/bar identification conjectural". Prose at 392
  ("The analytic lane of MC5 is therefore proved at all genera; the
  full genuswise BV/BRST/bar identification remains conjectural"), 477
  ("MC5 is partially proved, with the analytic HS-sewing package ..."),
  and the MC status table at 506-524 ("Analytic part proved ...") all
  match canonical.
- `chapters/connections/ht_physical_origins.tex:439, 759, 807, 1203`:
  four prose instances already qualified with "analytic HS-sewing lane
  of MC5 is proved at all genera ... the full genuswise BV/BRST/bar
  identification remains conjectural".
- `chapters/theory/introduction.tex:1570`: "the analytic lane of MC5
  is proved at all genera, while the full genuswise BV/BRST/bar
  identification remains conjectural". Canonical.
- `chapters/connections/conclusion.tex:941-944`: MC5 row in the
  concrete-consequences table already reads "Proved ($g{=}0$);
  $D^{\mathrm{co}}$ ($g{\ge}1$)" with specific Vol I theorem anchors.
- `chapters/connections/spectral-braiding.tex:1915-1919` and
  `spectral-braiding-frontier.tex:254-258`: both already state
  "contingent on the genuswise BV/BRST/bar identification of MC5
  which remains conjectural in Volume~I beyond the analytic HS-sewing
  lane".
- `chapters/connections/twisted_holography_quantum_gravity.tex:953,
  2504`: both are analytic-sewing references ("MC5 (Volume I, Theorem
  inductive-genus-determination)", "sewing machinery of MC5
  (thm:general-hs-sewing)"), which match the analytic lane that is
  proved.
- `chapters/connections/bar-cobar-review.tex:3738-3865`: the genus-0
  and genus-1 MC5 bridge theorem/corollary are structurally correct
  (they state the curvature formula and the Feynman/bar match at
  g=0,1), no status overclaim.
- `chapters/connections/spectral-braiding-core.tex:3466-3770`: all
  MC5 references are to the genus-one-bridge corollary (label
  reference, not a status claim).
- `chapters/connections/ht_bulk_boundary_line.tex:1413` and
  `ht_bulk_boundary_line_frontier.tex:220`: "(Theorem~D, bridge
  MC5)" is a label/identifier, not a status claim.
- `chapters/connections/thqg_concordance_supplement.tex:54, 86`: the
  dependency matrix at 86 marks inputs with $\bullet$ and does not
  claim "proved". Line 54 lists G7's inputs "G1, G6, MC5" as
  dependencies, again not a status claim.
- `chapters/frame/preface.tex`: no MC5 references. Wave 4-1, Wave
  13-1 FIX 1, Wave 15-2 edits preserved (untouched).
- `chapters/connections/3d_gravity.tex`: no MC5 references. Wave
  15-10 edits preserved (untouched).

## Verification grep

Post-fix, every occurrence of "MC5 ... proved" (case-insensitive)
across Vol II is now qualified with "analytic", "analytic HS-sewing",
or "analytic lane", and every nearby claim carries an explicit
"genuswise BV/BRST/bar identification remains conjectural" rider.

Command run:

    grep -n "MC5.*[Pp]roved" /Users/raeez/chiral-bar-cobar-vol2/**/*.tex
    grep -n "MC5.*[Pp]roved" /Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md

All matches contain one of the qualifiers above. Zero unqualified
"MC5 PROVED" claims remain on the active Vol II surface.

## Scope compliance

- Vol I files: untouched (scope compliance).
- Vol III files: untouched.
- `editorial_constitution.tex`: no local Vol II copy exists
  (canonical is in Vol I); not touched.
- Wave 4-1, 13-1, 15-2, 15-10 modifications in
  `chapters/frame/preface.tex` and `chapters/connections/3d_gravity.tex`:
  preserved (files were audited via grep and contained no MC5 claims
  to correct).
