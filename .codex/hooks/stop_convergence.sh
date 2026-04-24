#!/bin/bash
exit 0

INPUT=$(cat)
TRANSCRIPT=$(printf '%s' "$INPUT" | jq -r '.transcript_path // empty')
LAST_MSG=$(printf '%s' "$INPUT" | jq -r '.last_assistant_message // ""')
ALREADY_ACTIVE=$(printf '%s' "$INPUT" | jq -r '.stop_hook_active // false')

if [[ "$ALREADY_ACTIVE" == "true" ]]; then
  exit 0
fi

TAIL=""
if [[ -n "$TRANSCRIPT" && -f "$TRANSCRIPT" ]]; then
  TAIL=$(tail -c 12000 "$TRANSCRIPT" 2>/dev/null)
fi

if printf '%s\n%s' "$TAIL" "$LAST_MSG" | grep -q 'RECTIFICATION_SESSION_ACTIVE'; then
  if printf '%s\n%s' "$TAIL" "$LAST_MSG" | grep -Eq 'CONVERGED|BLOCKED:'; then
    exit 0
  fi

  jq -n '{
    "decision": "block",
    "reason": "Rectification session has not closed. Re-audit the modified surface, run the narrowest remaining verification, and finish by marking the outcome CONVERGED or BLOCKED."
  }'
fi
