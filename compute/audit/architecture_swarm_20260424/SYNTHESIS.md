# Architecture Attack-Heal Synthesis, 2026-04-24

## Scope

The swarm attacked the Vol II architecture/design surface, the Vol I
master-synthesis interface, and the coherence of that interface with the
Vol II body proper.  The run was executed in three batches: six, six,
then three readers.  Each reader returned a compact report in this
directory.

## Integration Rule

Broken proof is not manuscript decay.  The integration rule used here is:
repair the proof, isolate the true hypotheses, preserve the strongest
correct theorem, and remove only the false inference.  A status demotion
is not an acceptable substitute for a mathematical repair.

## Surviving Core

The surviving core is not the literal product
`Ran(Sigma_g) x Ran(R)`.  The correct geometric carrier is the mixed
open-closed holomorphic-topological Ran geometry
`Ran^{oc}_{HT}(Sigma_g,I)`, whose strata are indexed by closed bulk
collisions in the curve and ordered open boundary collisions in the
interval, with compatibility maps for mixed bulk-boundary approach.

The surviving algebraic core is the relative Feynman skeleton.  It is a
stable-graph bicomplex shared by the global factorization route and the
local operadic route.  It does not by itself remember global D-module
monodromy, Arakelov corrections, or the projective curvature class.

The surviving local-operadic core is associated-graded product geometry
plus mixed-face differential.  The product decomposition is a depth-zero
shadow; the full modular Swiss-cheese object has Type III mixed bubbling
faces.

The surviving topologisation core is conditional only in the mathematical
sense of named hypotheses.  Under the stated convergence, formality, or
Positselski criteria, the conclusions are proved implications.  The text
now avoids using unproved global equivalence as if it were an established
theorem.

## Main Repairs Inscribed

- `chapters/theory/factorization_swiss_cheese.tex`: inserted the mixed
  HT Ran geometry and repaired the bar construction, Koszul recovery,
  curved Riemann-Hilbert comparison, and colour-projection language.
- `chapters/theory/modular_swiss_cheese_operad.tex`: replaced the
  false product decomposition by an associated-graded statement plus
  mixed-face differential, and narrowed `Loc` to formal-collision
  extraction.
- `chapters/connections/relative_feynman_transform.tex`: changed the
  relative Feynman transform from an overclaimed global equivalence into
  the proved stable-graph skeleton, with explicit hypotheses for
  involutivity and derived/coderived comparison.
- `chapters/theory/sc_chtop_heptagon.tex`: separated the chiral bar
  resolution from the full two-coloured Swiss-cheese datum.
- `chapters/theory/chiral_higher_deligne.tex`,
  `chapters/connections/hochschild.tex`, and
  `chapters/connections/brace.tex`: separated proved brace/Hochschild
  actions from two-coloured strict refinements that require the named
  comparison hypotheses.
- Register and process-language repairs removed stale proof-status
  macros, stale UHF/FM labels, and draft-history language from the
  targeted active files.

## Verification

- `python3 scripts/generate_metadata.py`: regenerated the theorem
  registry and label metadata after the repairs.
- `compute/.venv/bin/python -m pytest
  compute/tests/test_universal_holography_functor_fm_iv.py
  compute/tests/test_fm81_fractional_ghost.py -q`: 15 passed.
- `python3 compute/scripts/audit_independent_verification.py --tex-root .
  --tests-dir compute/tests --show-orphans`: pass for tautologies and
  orphan registry entries; the audit still reports the global coverage
  gap of claims without independent verification.
- `git diff --check`: pass.

## Remaining Mathematical Obligations

- Prove the mixed-factorization duality theorem for
  `Ran^{oc}_{HT}(Sigma_g,I)` as a theorem in its own right, not as a
  mnemonic inherited from the product Ran space.
- Prove or cite the KZB/prime-form comparison needed for global genus
  formality beyond the local screen.
- Extend independent verification coverage beyond the current registry
  slice; the audit still reports many proved-here claims without a
  computational or independent-test anchor.
