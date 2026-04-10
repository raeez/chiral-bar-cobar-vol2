---
name: vol2-compute-engine
description: Use when the user asks to scaffold, add, extend, or repair a Vol II compute engine or its test surface. Do not use for pure manuscript prose tasks with no compute artifact.
---

# Vol II Compute Engine

New compute engines are part of the mathematical verification surface, not sidecars.

## Inputs

- engine topic or theorem family
- target formulas, invariants, or checks
- expected file names if given

## Workflow

1. State the mathematical claim the engine is meant to test.
2. Read nearby `compute/lib/` and `compute/tests/` patterns before creating anything.
3. Lock conventions first:
   - OPE mode versus lambda-bracket
   - divided-power factors
   - level normalization
   - genus and arity scope
4. Implement the library and the test surface together.
5. Derive expected values independently of the engine output.
6. Run the narrowest targeted `pytest` slice that can falsify the new logic.
7. Propagate any shared normalization or expected-value corrections into the manuscript or notes if needed.

## Verification standard

- Prefer at least three verification paths per load-bearing formula when feasible.
- For a new standalone engine, aim for a meaningful test surface rather than a token smoke test.
- Never update tests from the engine output alone.
- Every hardcoded expected value should have a traceable source or invariant.

## Vol II traps

- `AP128` / `V2-AP28`: engine and test sharing the same wrong derivation is not independent verification.
- `V2-AP34`: lambda-bracket coefficients use divided powers.
- `AP126`: affine `r`-matrix level factors survive.
- `AP49`: cross-volume comparisons require convention conversion.
