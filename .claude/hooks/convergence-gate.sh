#!/bin/bash
# ==========================================================================
# CONVERGENCE GATE — Vol II Stop hook
# ==========================================================================
# Same logic as Vol I. Only activates on SKILL INVOCATIONS, not loose word
# matches. Prevents false positives when discussing rectification.
# ==========================================================================

INPUT=$(cat)
TRANSCRIPT=$(echo "$INPUT" | jq -r '.transcript_path // empty')

if [ -n "$TRANSCRIPT" ] && [ -f "$TRANSCRIPT" ]; then
  TAIL=$(tail -c 8000 "$TRANSCRIPT" 2>/dev/null)

  IS_RECTIFICATION=false

  # Pattern 1: Skill invocation markers
  if echo "$TAIL" | grep -q '<command-name>rectify\|<command-name>audit\|<command-name>chriss-ginzburg\|<command-name>rectify-all\|<command-name>beilinson'; then
    IS_RECTIFICATION=true
  fi

  # Pattern 2: Explicit convergence gate marker
  if echo "$TAIL" | grep -q 'RECTIFICATION_SESSION_ACTIVE'; then
    IS_RECTIFICATION=true
  fi

  # Pattern 3: User slash command invocation
  if echo "$TAIL" | grep -q '"content":"/rectify \|"content":"/audit \|"content":"/chriss-ginzburg-rectify\|"content":"/rectify-all\|"content":"/beilinson-rectify'; then
    IS_RECTIFICATION=true
  fi

  if [ "$IS_RECTIFICATION" = true ]; then
    if echo "$TAIL" | grep -q "CONVERGED"; then
      exit 0
    fi
    if echo "$TAIL" | grep -qi "BLOCKED\|STUCK\|cannot proceed\|rate.limited"; then
      exit 0
    fi
    jq -n '{"decision":"block","reason":"CONVERGENCE GATE: Rectification loop has not converged. Declare CONVERGED or BLOCKED."}'
    exit 0
  fi
fi

exit 0
