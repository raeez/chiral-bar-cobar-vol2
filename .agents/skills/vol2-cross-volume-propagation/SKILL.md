---
name: vol2-cross-volume-propagation
description: Use after any mathematical wording, status, or formula change that may appear elsewhere in Vol II, Vol I, Vol III, superseded split files, notes, or compute layers. Do not use for isolated edits that cannot plausibly propagate.
---

# Vol II Cross-Volume Propagation

This skill exists to stop local truth from coexisting with global drift.

## Search surface

After a load-bearing change, inspect:

- active Vol II chapter files
- active Vol II appendices
- superseded split files that still advertise the same claim
- `~/chiral-bar-cobar`
- `~/calabi-yau-quantum-groups` when the bridge is genuinely cross-volume
- `compute/` and `compute/tests/`

## Propagation checklist

1. Search exact phrase variants and symbolic variants.
2. Check theorem statements, summaries, examples, remarks, introductions, and appendices.
3. Check build-facing surfaces:
   - label names
   - references
   - citation claims
4. Check compute-facing surfaces:
   - function docstrings
   - tests
   - hardcoded expected values
5. Update all still-live advertisements of the old claim in the same session.

## Convention alert

- Vol I uses OPE modes.
- Vol II uses lambda-brackets with divided powers.
- Vol III may use motivic or categorical normalizations.

Never compare formulas across volumes without converting conventions first.

## Stop condition

Do not call the propagation done until:
- the active surface is consistent;
- stale superseded claims that still mislead future audits are either corrected or explicitly quarantined;
- tests or log checks no longer contradict the new statement.
