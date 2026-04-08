# Full Mathematical Defect Catalogue — Volume II

Date: `2026-04-08`

Scope:
- live/active Volume II input graph from `main.tex` (`64` active inputs);
- mathematically load-bearing claims only;
- exposition/style omitted on purpose;
- includes active-surface defects plus the most dangerous stale propagation hazards still present in-repo.

Method:
- hostile reread of the foundational spine;
- exact-location scan for status/proof drift, scope inflation, and dependency contamination;
- dependency inventory keyed to the currently unstable theorem lanes.

This catalogue is best-current exhaustive relative to the detectable live surface and the scanned stale mirrors. It is not a proof that no further local mathematics bugs remain.

## I. Confirmed Direct Defects On The Current Live Surface

### 1. `thm:recognition-SC` is not proved at theorem strength

- Severity: `CRITICAL`
- Class: `P/S`
- Location: [chapters/theory/locality.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex#L378)
- Exact lines: `378–492`
- Defect:
  The proof of the HT prefactorization recognition theorem is not closed.
  Step `3a` begins from a `C_\ast(W(\SCchtop))`-algebra and immediately speaks of “evaluating the prefactorization algebra” before such an object has been constructed.
  Step `3b` applies one-color recognition theorems factor-by-factor and then asserts the mixed-color assembly via Kunneth/Boardman–Vogt language, but no genuine two-color comparison functor or universal-property proof is supplied.
  On hostile reread, this is a programme sketch, not a finished equivalence proof.
- Consequence:
  Every downstream claim using `thm:recognition-SC` or `thm:recognition-foundations` is mathematically contaminated until this theorem is repaired or downgraded.

### 2. `thm:physics-bridge` does not prove propagator factorization

- Severity: `CRITICAL`
- Class: `P/C`
- Location: [chapters/theory/raviolo.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex#L405)
- Exact lines: `405–449`
- Defect:
  Step `(i)` claims a factorized Green kernel for `Q = \dbar_z + d_t`, but the displayed computation produces
  `Q(K_C \otimes \delta_R) = \delta_C \otimes \delta_R + K_C \otimes \delta'_R`,
  and the unwanted term is discarded by fiat.
  More fundamentally, additive splitting of the operator is not itself a proof that the Green kernel is a pure tensor of separate Green kernels.
  The theorem therefore proves less than it claims under hypotheses `(a)`–`(c)`.
- Consequence:
  Every physical-realization lane using `thm:physics-bridge` inherits a proof-state defect, not merely a missing citation.

### 3. `main.tex` still lies about the recognition lane

- Severity: `SERIOUS`
- Class: `S/P`
- Location: [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex#L505)
- Exact lines: `505–520`, `562–565`
- Defect:
  The top-level live summary still says the operadic foundations, including the recognition theorem, “are proved without physical hypotheses,” and still says the former standing hypotheses `(H1)`–`(H4)` have been eliminated, with `(H4)` reduced to “the recognition theorem.”
  Given defect `I.1`, this summary is false on the current proof surface.

### 4. `concordance.tex` still classifies the recognition lane as proved

- Severity: `SERIOUS`
- Class: `S/P`
- Location: [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex#L25)
- Exact lines: `25–32`, `41–48`, `67–68`
- Defect:
  The normative status ledger still records:
  `H4` as `Proved`,
  “Recognition theorem” as `ProvedHere`,
  `SC \leftrightarrow HT prefactorization` as `ProvedHere`,
  and even says compatibility with `W(\mathsf{SC}^{\mathrm{ch,top}})` holds “via recognition ... now proved.”
  These are not conservative summaries of the actual proof surface after defect `I.1`.

### 5. `foundations.tex` still advertises the bulk/Hochschild theorem with the old false scope

- Severity: `SERIOUS`
- Class: `S`
- Location: [chapters/theory/foundations.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex#L516)
- Exact lines: `516–524`
- Defect:
  The proof still cites `Theorem~\ref{thm:bulk_hochschild}` as
  “unconditional for any logarithmic `\SCchtop`-algebra.”
  That statement is no longer true on the live surface; the theorem was tightened to HT prefactorization realizations in the scope of `thm:physics-bridge`.

### 6. `affine_half_space_bv.tex` overclaims completion

- Severity: `SERIOUS`
- Class: `S/P`
- Location: [chapters/connections/affine_half_space_bv.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/affine_half_space_bv.tex#L1724)
- Exact lines: `1724–1734`
- Defect:
  The synthesis section says:
  “The half-space programme is complete for any logarithmic `\SCchtop`-algebra,”
  and the displayed chain explicitly routes through “recognition.”
  Because the recognition theorem is not presently closed, this slogan outruns the checked proof surface.

## II. Active-Surface Dependency Contamination

Interpretation:
- the files below are not all independently false;
- they are mathematically at risk because they lean on the broken theorem lanes above;
- until `thm:recognition-SC` and `thm:physics-bridge` are repaired or downgraded, every claim in these files that depends on those lanes is unverified relative to the current manuscript proof surface.

### A. Active files depending on `thm:physics-bridge`

Reference counts are occurrences in the active input graph.

```text
7  chapters/theory/fm-calculus.tex
5  chapters/connections/affine_half_space_bv.tex
5  chapters/connections/hochschild.tex
5  chapters/connections/spectral-braiding-core.tex
5  chapters/examples/examples-complete-conditional.tex
5  chapters/examples/w-algebras-virasoro.tex
5  chapters/theory/axioms.tex
4  chapters/examples/examples-worked.tex
4  chapters/theory/bv-construction.tex
4  chapters/theory/raviolo.tex
3  chapters/connections/3d_gravity.tex
2  chapters/connections/anomaly_completed_core.tex
2  chapters/connections/ht_bulk_boundary_line_frontier.tex
2  chapters/connections/line-operators.tex
2  chapters/connections/log_ht_monodromy_frontier.tex
2  chapters/examples/examples-computing.tex
2  chapters/theory/introduction.tex
1  chapters/connections/bar-cobar-review.tex
1  chapters/connections/brace.tex
1  chapters/connections/dg_shifted_factorization_bridge.tex
1  chapters/connections/ht_bulk_boundary_line_core.tex
1  chapters/connections/log_ht_monodromy_core.tex
1  chapters/connections/modular_pva_quantization_frontier.tex
1  chapters/examples/examples-complete-proved.tex
1  chapters/frame/preface.tex
1  chapters/theory/factorization_swiss_cheese.tex
1  chapters/theory/foundations.tex
1  chapters/theory/pva-descent-repaired.tex
1  chapters/theory/raviolo-restriction.tex
```

Top-priority active files on this lane:
- [chapters/theory/fm-calculus.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex)
- [chapters/connections/affine_half_space_bv.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/affine_half_space_bv.tex)
- [chapters/connections/hochschild.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex)
- [chapters/connections/spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex)
- [chapters/examples/examples-complete-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex)
- [chapters/examples/w-algebras-virasoro.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex)
- [chapters/theory/axioms.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/axioms.tex)

### B. Active files depending on the recognition theorem lane

```text
2  chapters/connections/hochschild.tex
2  chapters/connections/ht_bulk_boundary_line_core.tex
1  chapters/connections/bar-cobar-review.tex
1  chapters/connections/brace.tex
1  chapters/connections/conclusion.tex
1  chapters/connections/relative_feynman_transform.tex
1  chapters/connections/thqg_3d_gravity_movements_vi_x.tex
1  chapters/theory/bv-construction.tex
1  chapters/theory/foundations.tex
1  chapters/theory/locality.tex
1  chapters/theory/raviolo.tex
```

Top-priority active files on this lane:
- [chapters/connections/hochschild.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex)
- [chapters/connections/ht_bulk_boundary_line_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex)
- [chapters/theory/bv-construction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/bv-construction.tex)
- [chapters/theory/raviolo.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex)
- [chapters/theory/foundations.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex)

### C. Active files still carrying the bulk/Hochschild lane

```text
9  chapters/connections/hochschild.tex
2  chapters/theory/foundations.tex
2  chapters/theory/raviolo.tex
1  chapters/connections/brace.tex
1  chapters/connections/ht_bulk_boundary_line_core.tex
1  chapters/connections/ht_bulk_boundary_line_frontier.tex
1  chapters/connections/line-operators.tex
1  chapters/examples/examples-computing.tex
```

Interpretation:
- this lane is no longer overstated in `hochschild.tex`, but all citations to it must respect its new scoped statement;
- every downstream text that still speaks as if the theorem were abstract/unconditional is a defect.

### D. Active files still carrying the boundary-linear exact-sector lane

```text
5  chapters/connections/ht_bulk_boundary_line_core.tex
5  chapters/connections/ht_bulk_boundary_line_frontier.tex
3  chapters/connections/hochschild.tex
3  chapters/examples/examples-worked.tex
2  chapters/theory/introduction.tex
1  chapters/connections/line-operators.tex
1  chapters/connections/relative_feynman_transform.tex
1  chapters/frame/preface.tex
1  chapters/theory/foundations.tex
```

Interpretation:
- any text in these files that globalizes the exact-sector theorem beyond its scoped hypotheses is suspect by default.

## III. Explicit Scope/Status Drift Still Present Outside The Core Fix

### 1. Recognition/H4 summary drift

- [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex#L505) still says the recognition theorem is proved without physical hypotheses.
- [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex#L562) still packages `(H4)` as if it had been cleanly discharged.
- [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex#L27) still marks `(H4)` as proved.
- [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex#L44) still marks the recognition theorem as `ProvedHere`.
- [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex#L48) still marks `SC \leftrightarrow HT prefactorization` as `ProvedHere`.
- [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex#L68) still says the compatibility result is obtained “via recognition ... now proved.”

### 2. Residual bulk/Hochschild scope drift

- [chapters/theory/foundations.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex#L518) still calls `thm:bulk_hochschild` unconditional.

### 3. Completion-language drift

- [chapters/connections/affine_half_space_bv.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/affine_half_space_bv.tex#L1726) still claims the half-space programme is complete for any logarithmic `\SCchtop`-algebra.

## IV. Inactive But Still Dangerous Propagation Hazards

These are not part of the active `main.tex` surface, but they still live in-repo and can mislead future rectification passes.

### 1. `w-algebras-conditional.tex` contains a direct contradiction in its opener

- Severity: `SERIOUS`
- Location: [chapters/examples/w-algebras-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex#L1)
- Exact lines: `1–11`
- Defect:
  The section title is “Conditional Extensions,” but line `7` says
  “All results hold unconditionally for any logarithmic `\mathrm{SC}^{\mathrm{ch,top}}`-algebra.”
  This is a literal status contradiction on the page.

### 2. `foundations_overclaims_resolved.tex` still carries the old bulk/Hochschild scope lie

- Severity: `MODERATE`
- Location: `chapters/theory/foundations_overclaims_resolved.tex:42`
- Defect:
  The stale mirror still calls `thm:bulk_hochschild` unconditional for any logarithmic `\SCchtop`-algebra.

### 3. Heavy inactive bridge-theorem contamination remains in the older W-algebra and examples surfaces

High-count inactive examples:
- `chapters/examples/w-algebras.tex` (`12` references to `physics-bridge`)
- `chapters/examples/examples-complete.tex` (multiple `ClaimStatusConditional` lanes and physical-realization material)

Interpretation:
- these stale files are not presently governing the live build,
- but they remain collision surfaces for future audits and propagation.

## V. Priority Order For Mathematical Repair

1. Repair or downgrade `thm:recognition-SC` in [locality.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/locality.tex#L378).
2. Repair or downgrade `thm:physics-bridge` in [raviolo.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex#L405).
3. Propagate those status changes into the live ledgers:
   [main.tex](/Users/raeez/chiral-bar-cobar-vol2/main.tex#L505) and [concordance.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex#L25).
4. Remove residual direct overclaims:
   [foundations.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex#L518) and [affine_half_space_bv.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/affine_half_space_bv.tex#L1726).
5. Re-audit the heaviest contaminated active files on the bridge lane:
   `fm-calculus`, `affine_half_space_bv`, `hochschild`, `spectral-braiding-core`, `w-algebras-virasoro`, `examples-complete-conditional`, `axioms`.

## VI. Current Verdict

The current live Volume II surface is not mathematically converged.

The deepest failures are not cosmetic:
- one foundational equivalence theorem is not actually proved as written;
- one foundational physical-to-algebra bridge does not establish its key analytic separation claim;
- the top-level status ledgers still advertise those lanes as solved;
- a broad downstream slice of the volume therefore remains mathematically contaminated.

Status:
- `BLOCKED` on foundational theorem repair.
