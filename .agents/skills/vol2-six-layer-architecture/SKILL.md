---
name: vol2-six-layer-architecture
description: Use when the task is a chapter-scale architectural rewrite or analysis touching the factorization-versus-operadic hierarchy, especially `factorization_swiss_cheese`, `modular_swiss_cheese_operad`, `relative_feynman_transform`, or the Route A/B/C local-global split encoded in `.claude/specs/`.
---

# Vol II Six-Layer Architecture

This skill surfaces the Claude-side master/route specs for Codex.

## Trigger surface

Use this skill when the task mentions any of:

- factorization Swiss-cheese
- modular Swiss-cheese operad
- relative Feynman transform
- Route A / Route B / Route C
- the local-versus-global tension
- the six-layer framework

## Read order

1. `.claude/specs/master.md`
2. Then the relevant route spec:
   - `.claude/specs/route-a-modular-sc.md`
   - `.claude/specs/route-b-fact-sc.md`
   - `.claude/specs/route-c-relative-ft.md`
3. Then the target live chapter(s) in this repo.
4. Then the cited Vol I dependencies named in the spec.

## Operating rule

- Treat the route specs as design constraints and dependency maps, not as proof.
- The live `.tex` still wins over the spec if the repo has moved.
- If the spec and live surface diverge, state the divergence explicitly before patching.

## Output standard

- Name the route being used.
- Keep the local/global distinction explicit.
- Distinguish factorization truth, operadic local shadow, and relative-Feynman algebraic skeleton.
