---
name: vol2-build-surface
description: Use when the task depends on LaTeX builds, build logs, warning classification, targeted pytest runs, or deciding whether a manuscript change is actually verified. Do not use for purely conceptual work with no executable verification surface.
---

# Vol II Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- `make`
- targeted `python3 -m pytest ...`
- direct log inspection

## Classification rules

- Fatal LaTeX error: actionable immediately.
- Undefined Vol I cross-reference: expected unless the local file claims otherwise.
- Pass-1 warnings: not yet findings until they persist on a stable rerun.
- Interrupted build with corrupted aux surface: clean/restart before trusting any counts.
- Test oracle mismatch: treat as either a mathematics bug or a convention bug until proved otherwise.

## Workflow

1. Stabilize the build surface.
2. Run the narrowest falsifying build/test command.
3. Classify failures into:
   - manuscript error
   - compute error
   - convention mismatch
   - stale aux/log artifact
   - expected external cross-volume warning
4. Fix or quarantine only after classification.

## Reporting standard

- Quote the decisive failure signature in paraphrase.
- Distinguish persistent warnings from transient pass-1 noise.
- If concurrency or external workers make the logs race-prone, say so explicitly.
