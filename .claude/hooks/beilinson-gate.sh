#!/bin/bash
# ==========================================================================
# BEILINSON GATE — Vol II PostToolUse hook for Edit|Write
# ==========================================================================
# Comprehensive enforcement: shared AP checks (from Vol I) + Vol II-specific
# (AP-OC, E_infinity/E_1 hierarchy). All fixes from RED audit applied.
# ==========================================================================

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

case "$FILE_PATH" in
  *.tex|*.py) ;;
  *) exit 0 ;;
esac

ISSUES=""
WARNINGS=""

if [[ "$FILE_PATH" == *.tex ]]; then

  # === SHARED CHECKS (same as Vol I, propagated to prevent drift) ===

  # --- AP24: Unqualified kappa+kappa'=0 ---
  if grep -q 'kappa.*+.*kappa.*=.*0' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n 'kappa.*+.*kappa.*=.*0' "$FILE_PATH" | grep -v 'Kac--Moody\|Kac-Moody\|free.field\|self-contragredient\|lattice\|principal\|Heisenberg\|affine' | head -3)
    if [ -n "$MATCHES" ]; then
      ISSUES="${ISSUES}AP24: Possibly unqualified kappa+kappa'=0. For Virasoro: =13, NOT 0. Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP8: Self-dual Virasoro/Vir without c=13 ---
  if grep -qi 'self.dual.*virasoro\|virasoro.*self.dual\|self.dual.*Vir\|Vir.*self.dual' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'self.dual.*virasoro\|virasoro.*self.dual\|self.dual.*Vir[^a-z]\|Vir[^a-z].*self.dual' "$FILE_PATH" | grep -v 'c=13\|c = 13\|c\*=13' | head -3)
    if [ -n "$MATCHES" ]; then
      ISSUES="${ISSUES}AP8: Self-dual Virasoro without c=13. Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP25/AP34: bar != Verdier != cobar ---
  if grep -qi 'bar.cobar.*produces.*bulk\|bar.cobar.*open.to.closed\|cobar.*Koszul dual' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'bar.cobar.*produces.*bulk\|bar.cobar.*open.to.closed\|cobar.*Koszul dual' "$FILE_PATH" | head -3)
    if [ -n "$MATCHES" ]; then
      ISSUES="${ISSUES}AP25/AP34: Omega(B(A))=A (inversion), NOT bulk. D_Ran(B(A))=B(A!) (Verdier). Lines: ${MATCHES}\n"
    fi
  fi

  # --- AP40: Environment/tag mismatch (uses printf, not echo, to avoid \b mangling) ---
  if grep -q 'ClaimStatusConjectured' "$FILE_PATH" 2>/dev/null; then
    CONJ_LINES=$(grep -n 'ClaimStatusConjectured' "$FILE_PATH" | cut -d: -f1)
    for LINE in $CONJ_LINES; do
      START=$((LINE - 10))
      [ $START -lt 1 ] && START=1
      CONTEXT=$(sed -n "${START},${LINE}p" "$FILE_PATH")
      if printf '%s\n' "$CONTEXT" | grep -q 'begin{theorem}\|begin{proposition}\|begin{lemma}\|begin{corollary}'; then
        ISSUES="${ISSUES}AP40: ClaimStatusConjectured in proof-bearing environment near line ${LINE}.\n"
        break
      fi
    done
  fi

  # === VOL II-SPECIFIC CHECKS ===

  # --- AP-OC: Bar = bulk conflation (Vol II critical) ---
  if grep -qi 'bar complex.*bulk\|bar.*produces.*bulk\|B(A).*bulk observ' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'bar complex.*bulk\|bar.*produces.*bulk\|B(A).*bulk observ' "$FILE_PATH" | head -3)
    if [ -n "$MATCHES" ]; then
      ISSUES="${ISSUES}AP-OC: Bar=bulk conflation. Bar classifies TWISTING MORPHISMS. Bulk = Z^der_ch(A). Lines: ${MATCHES}\n"
    fi
  fi

  # --- Vol II AP43: "not E_infty" for vertex algebras ---
  if grep -qi 'not E_\\infty\|is not.*E.*infty\|not.*E_\\infty' "$FILE_PATH" 2>/dev/null; then
    MATCHES=$(grep -n -i 'not E_\\infty\|is not.*E.*infty\|not.*E_\\infty' "$FILE_PATH" | head -3)
    if [ -n "$MATCHES" ]; then
      ISSUES="${ISSUES}AP43(Vol II): ALL vertex algebras ARE E_infty-chiral. OPE poles do NOT break E_infty. Lines: ${MATCHES}\n"
    fi
  fi

  # --- PROSE ---
  for WORD in notably crucially remarkably interestingly importantly furthermore moreover additionally delve leverage utilize underscore facilitate pivotal nuanced intricate streamline tapestry multifaceted cornerstone; do
    if grep -qi "\\b${WORD}\\b" "$FILE_PATH" 2>/dev/null; then
      LINE=$(grep -n -i "\\b${WORD}\\b" "$FILE_PATH" | head -1)
      ISSUES="${ISSUES}PROSE: '${WORD}'. Line: ${LINE}\n"
    fi
  done

  for PHRASE in "it is worth noting" "having established" "we now turn to" "in this section we" "as we shall see" "let us now" "we proceed to" "the key insight is" "it turns out that" "this brings us to" "with this in hand"; do
    if grep -qi "$PHRASE" "$FILE_PATH" 2>/dev/null; then
      LINE=$(grep -n -i "$PHRASE" "$FILE_PATH" | head -1)
      ISSUES="${ISSUES}PROSE: Signpost '${PHRASE}'. Line: ${LINE}\n"
    fi
  done
  # --- AP158/AP-CY61: Shallow correction detection ---
  OLD_STR=$(echo "$INPUT" | jq -r '.tool_input.old_string // empty' 2>/dev/null)
  NEW_STR=$(echo "$INPUT" | jq -r '.tool_input.new_string // empty' 2>/dev/null)
  if [ -n "$OLD_STR" ] && [ -n "$NEW_STR" ]; then
    OLD_LEN=${#OLD_STR}
    NEW_LEN=${#NEW_STR}
    if [ $OLD_LEN -gt 40 ] && [ $NEW_LEN -gt 0 ]; then
      RATIO=$((NEW_LEN * 100 / OLD_LEN))
      if [ $RATIO -ge 70 ] && [ $RATIO -le 150 ]; then
        HAS_MATH_CLAIM=$(echo "$NEW_STR" | grep -ci 'is the\|equals\|gives\|produces\|categorif\|corresponds to\|is equivalent' 2>/dev/null)
        HAS_SUBSTANCE=$(echo "$NEW_STR" | grep -ci 'begin{remark}\|begin{proof}\|factori[sz]\|adjoint\|adjunction\|construct\|\\xrightarrow\|\\simeq\|\\cong' 2>/dev/null)
        if [ "$HAS_MATH_CLAIM" -gt 0 ] && [ "$HAS_SUBSTANCE" -lt 1 ]; then
          WARNINGS="${WARNINGS}AP158: Possible shallow correction (term swap without mathematical content). Investigate from first principles before replacing a claim. Invoke /investigate if unsure.\n"
        fi
      fi
    fi
  fi

fi

# ---------------------------------------------------------------------------
# SECTION 2: COMPUTE LAYER CHECKS (for .py files)
# ---------------------------------------------------------------------------
if [[ "$FILE_PATH" == *.py ]]; then
  if grep -q 'assert.*==' "$FILE_PATH" 2>/dev/null; then
    HARDCODED=$(grep -c 'assert.*==.*[0-9]' "$FILE_PATH" 2>/dev/null)
    CROSSCHECK=$(grep -c 'assert.*approx\|assert.*close\|verify_.*path\|cross_check\|independent' "$FILE_PATH" 2>/dev/null)
    if [ "$HARDCODED" -gt 5 ] && [ "$CROSSCHECK" -lt 2 ]; then
      WARNINGS="${WARNINGS}AP10: ${HARDCODED} hardcoded assertions but only ${CROSSCHECK} cross-checks. Add multi-path verification.\n"
    fi
  fi
fi

# ---------------------------------------------------------------------------
# SECTION 3: BUILD DISCIPLINE
# ---------------------------------------------------------------------------
COUNTER_FILE="/tmp/claude_beilinson_edit_count_vol2"
COUNT=$(cat "$COUNTER_FILE" 2>/dev/null || echo 0)
COUNT=$((COUNT + 1))
echo "$COUNT" > "$COUNTER_FILE"

BUILD_REMINDER=""
if (( COUNT % 5 == 0 )); then
  BUILD_REMINDER="BUILD CHECK: ${COUNT} edits. Run: pkill -9 -f pdflatex; sleep 2; cd ~/chiral-bar-cobar-vol2 && make fast"
fi

# ---------------------------------------------------------------------------
# SECTION 4: CROSS-VOLUME PROPAGATION
# ---------------------------------------------------------------------------
PROPAGATION=""
if [[ "$FILE_PATH" == *.tex ]]; then
  NEW_CONTENT=$(echo "$INPUT" | jq -r '(.tool_input.new_string // .tool_input.content) // empty' 2>/dev/null)
  if echo "$NEW_CONTENT" | grep -q '\\kappa\|\\Theta\|\\lambda_g\|SC.*ch.*top\|E_\\infty\|E_1\|\\frac{c}' 2>/dev/null; then
    PROPAGATION="AP5/AP49: Formula edit. Grep ALL THREE volumes. Convention: Vol I=OPE modes, Vol II=lambda-brackets (1/n! factor)."
  fi
fi

# ---------------------------------------------------------------------------
# OUTPUT
# ---------------------------------------------------------------------------
CONTEXT=""
[ -n "$ISSUES" ] && CONTEXT="${CONTEXT}VIOLATIONS:\n${ISSUES}\n"
[ -n "$WARNINGS" ] && CONTEXT="${CONTEXT}WARNINGS:\n${WARNINGS}\n"
[ -n "$BUILD_REMINDER" ] && CONTEXT="${CONTEXT}${BUILD_REMINDER}\n"
[ -n "$PROPAGATION" ] && CONTEXT="${CONTEXT}${PROPAGATION}\n"

if [ -n "$CONTEXT" ]; then
  jq -n --arg ctx "$CONTEXT" '{
    "hookSpecificOutput": {
      "hookEventName": "PostToolUse",
      "additionalContext": $ctx
    }
  }'
fi

exit 0
