#!/bin/bash

INPUT=$(cat)
CMD=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // ""')
RESP=$(printf '%s' "$INPUT" | jq -r '.tool_response // ""')
CMD_LC=$(printf '%s' "$CMD" | tr '[:upper:]' '[:lower:]')
RESP_LC=$(printf '%s' "$RESP" | tr '[:upper:]' '[:lower:]')

if [[ "$CMD_LC" =~ make|pdflatex|pytest|python3[[:space:]]+-m[[:space:]]+pytest ]]; then
  if [[ "$RESP_LC" =~ failed|fatal[[:space:]]error|traceback|undefined[[:space:]]control[[:space:]]sequence|make:[[:space:]]\*\*\*|error:|assertionerror|no[[:space:]]output[[:space:]]pdf[[:space:]]file[[:space:]]produced ]]; then
    jq -n '{
      "decision": "block",
      "reason": "Verification surfaced failures or fatal warnings. Classify the output, fix what is in scope, or report a specific blocker before stopping.",
      "hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": "Build/test output indicates the verification surface is not yet clean."
      }
    }'
  fi
fi
