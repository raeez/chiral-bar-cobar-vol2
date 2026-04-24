#!/bin/bash
exit 0

INPUT=$(cat)
CMD=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // ""')
RESP=$(printf '%s' "$INPUT" | jq -r '.tool_response // ""')
CMD_LC=$(printf '%s' "$CMD" | tr '[:upper:]' '[:lower:]')
RESP_LC=$(printf '%s' "$RESP" | tr '[:upper:]' '[:lower:]')

BLOCK_REASON=""
CONTEXT=""

if [[ "$CMD_LC" =~ make|pdflatex|pytest|python3[[:space:]]+-m[[:space:]]+pytest ]]; then
  if [[ "$RESP_LC" =~ failed|fatal[[:space:]]error|traceback|undefined[[:space:]]control[[:space:]]sequence|make:[[:space:]]\*\*\*|error:|assertionerror|no[[:space:]]output[[:space:]]pdf[[:space:]]file[[:space:]]produced ]]; then
    BLOCK_REASON="Verification surfaced failures or fatal warnings. Classify the output, fix what is in scope, or report a specific blocker before stopping."
    CONTEXT="Build/test output indicates the verification surface is not yet clean."
  fi
fi

if [[ "$CMD_LC" =~ git[[:space:]]+diff|git[[:space:]]+status|make|pytest|python3[[:space:]]+-m[[:space:]]+pytest ]]; then
  DIRTY_RELEVANT=$(git status --short 2>/dev/null | grep -E '\.(tex|py)$' | head -20)
  if [[ -n "$DIRTY_RELEVANT" ]]; then
    EXTRA="Beilinson gate: dirty .tex/.py files exist. Re-check claim status, theorem-environment/tag alignment, propagation, nearby therefore/hence/it-follows drift, and standalone-document artifacts before declaring success."
    if [[ -n "$CONTEXT" ]]; then
      CONTEXT="${CONTEXT}"$'\n'"${EXTRA}"
    else
      CONTEXT="${EXTRA}"
    fi
  fi
fi

if [[ -n "$BLOCK_REASON" ]]; then
  jq -n --arg reason "$BLOCK_REASON" --arg ctx "$CONTEXT" '{
    "decision": "block",
    "reason": $reason,
    "hookSpecificOutput": {
      "hookEventName": "PostToolUse",
      "additionalContext": $ctx
    }
  }'
  exit 0
fi

if [[ -n "$CONTEXT" ]]; then
  jq -n --arg ctx "$CONTEXT" '{
    "hookSpecificOutput": {
      "hookEventName": "PostToolUse",
      "additionalContext": $ctx
    }
  }'
fi
