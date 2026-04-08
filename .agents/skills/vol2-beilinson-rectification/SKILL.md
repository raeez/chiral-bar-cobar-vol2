---
name: vol2-beilinson-rectification
description: Use when the user asks to audit, rectify, fortify, fix, tighten, or converge a Vol II chapter, theorem, proof, introduction, appendix, or the live manuscript surface. Do not use for purely local copyedits with no mathematical or structural truth conditions.
---

# Vol II Beilinson Rectification

Run the full local rectification loop on the live surface.

## Inputs

- exact target file or theorem if given
- otherwise the smallest live surface implied by the user prompt

## Mandatory loop

1. Start with a short progress update naming the target and first verification step.
2. Register a nontrivial task in `update_plan`.
3. Read before editing:
   - target file
   - local context
   - active `\input` graph from `main.tex`
   - current dirty diff
   - relevant compute/tests or build logs
4. Run three hostile passes:
   - `RED`: logic, hypotheses, signs, formulas, scope
   - `BLUE`: consistency, labels, status tags, duplicate formulations, build/test collisions
   - `GREEN`: missing definitions, dangling references, structural gaps, statements that should be weakened or split
5. Record actionable findings in `compute/audit/linear_read_notes.md` with:
   - date
   - target
   - severity
   - class
   - exact location
   - issue
   - fix
   - status
6. Fix in dependency order:
   - `CRITICAL`
   - `SERIOUS`
   - `MODERATE`
7. After each substantive mathematical correction:
   - grep the active Vol II surface
   - grep superseded split files if they still sell the same claim
   - grep `~/chiral-bar-cobar`
   - grep `~/calabi-yau-quantum-groups` if the claim is truly cross-volume
8. Run the narrowest verification that can falsify the change:
   - targeted `pytest`
   - targeted grep
   - log inspection
   - `make fast` for load-bearing theorem/proof rewrites
9. Re-audit the modified surface.
10. Finish only with:
   - `CONVERGED`
   - `BLOCKED: <specific blocker>`

## Non-negotiables

- Never patch before reading.
- Never accept a slogan when the proof scope is narrower.
- Never propagate an unverified correction across multiple files.
- Never upgrade a statement to proved-here in the same pass as its first unchecked proof draft.
- Never let theorem environment, claim-status tag, and surrounding prose disagree.

## Tool discipline

- Use `multi_tool_use.parallel` for independent reads, greps, log checks, and targeted tests.
- Use `apply_patch` for manual edits.
- Use `exec_command` for `git diff`, `pytest`, `make fast`, and focused shell inspection.
- Keep the work local unless the user explicitly asks for delegation or swarm behavior.
