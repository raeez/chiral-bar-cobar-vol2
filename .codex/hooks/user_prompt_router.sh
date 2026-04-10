#!/bin/bash

INPUT=$(cat)
PROMPT=$(printf '%s' "$INPUT" | jq -r '.prompt // ""')
PROMPT_LC=$(printf '%s' "$PROMPT" | tr '[:upper:]' '[:lower:]')

CONTEXT=""

if [[ "$PROMPT_LC" =~ audit|rectif|fortif|beilinson|prove|proof|theorem|lemma|claim|formula|verify|propagat|consisten|make[[:space:]]+fast|pytest|build ]]; then
  CONTEXT="RECTIFICATION_SESSION_ACTIVE"$'\n'
fi

if [[ "$PROMPT_LC" =~ audit|review|red-team|redteam|pressure-test|pressure[[:space:]-]?test|falsif ]]; then
  CONTEXT+="Prefer the repo skill \`vol2-deep-audit\` for a findings-first pass. Read the live surface before editing, prioritize mathematical bugs and status drift, and anchor findings to exact files or labels."$'\n'
fi

if [[ "$PROMPT_LC" =~ audit|rectif|fortif|beilinson ]]; then
  CONTEXT+="Prefer the repo skill \`vol2-beilinson-rectification\`. Register substantial work in update_plan, read the live surface before editing, log findings in compute/audit/linear_read_notes.md, and do not stop until the session is marked CONVERGED or BLOCKED."$'\n'
fi

if [[ "$PROMPT_LC" =~ formula|coefficient|invariant|table|spectral[[:space:]-]?sequence|lambda|ope|normaliz|eta|kappa|r-matrix|rmatrix|verify ]]; then
  CONTEXT+="Prefer the repo skill \`vol2-formula-verification\`. Use at least three independent verification paths when feasible, and convert OPE-mode versus lambda-bracket conventions explicitly before comparing across volumes."$'\n'
fi

if [[ "$PROMPT_LC" =~ propagat|cross-volume|cross[[:space:]-]?volume|vol[[:space:]]*i|vol[[:space:]]*ii|vol[[:space:]]*iii|all[[:space:]]+files ]]; then
  CONTEXT+="Prefer the repo skill \`vol2-cross-volume-propagation\`. After any mathematical correction, search active chapters, superseded splits, Vol I, Vol III, and compute/tests before declaring success."$'\n'
fi

if [[ "$PROMPT_LC" =~ make|pdflatex|latex|build|pytest|test[[:space:]]|tests[[:space:]]|warnings|log ]]; then
  CONTEXT+="Prefer the repo skill \`vol2-build-surface\`. Stabilize the build surface before trusting warning counts, and classify whether failures are mathematical, conventional, or artifact noise."$'\n'
fi

if [[ "$PROMPT_LC" =~ frontier|research|programme|program|synthesis|new[[:space:]]+theorem|conjecture|architecture ]]; then
  CONTEXT+="Prefer the repo skill \`vol2-frontier-research\`. Separate proved core, conditional bridge, conjectural extension, and heuristic picture. Keep the work local unless the user explicitly authorizes delegation."$'\n'
fi

if [[ "$PROMPT_LC" =~ compute[[:space:]-]?engine|new[[:space:]]+engine|scaffold[[:space:]]+engine|compute[[:space:]]+module|test[[:space:]]+engine|engine[[:space:]]+test ]]; then
  CONTEXT+="Prefer the repo skill \`vol2-compute-engine\`. Read nearby compute patterns first, lock conventions before coding, and derive expected values independently of the engine output."$'\n'
fi

if [[ "$PROMPT_LC" =~ swarm|sub-agent|subagent|parallel[[:space:]]+agent|delegate|delegation ]]; then
  CONTEXT+="If and only if the user has explicitly authorized delegation, prefer the repo skill \`vol2-research-swarm\`. Keep the critical-path task local, split only independent sidecar tasks, and integrate only after local verification."$'\n'
fi

if [[ "$PROMPT_LC" =~ factorization[[:space:]-]?swiss|modular[[:space:]-]?swiss|relative[[:space:]-]?feynman|route[[:space:]]+[abc]|six-layer|local[[:space:]-]?global[[:space:]-]?tension ]]; then
  CONTEXT+="Prefer the repo skill \`vol2-six-layer-architecture\`. Read `.claude/specs/master.md` and the relevant Route A/B/C spec before treating any architectural statement as live truth."$'\n'
fi

if [[ -n "$CONTEXT" ]]; then
  jq -n --arg ctx "$CONTEXT" '{
    "hookSpecificOutput": {
      "hookEventName": "UserPromptSubmit",
      "additionalContext": $ctx
    }
  }'
fi
