#!/bin/bash
# ==========================================================================
# CGCLEAN-1..55 hook snippet (Session 2026-04-22: manuscript hygiene)
# ==========================================================================
# This snippet is the append block requested for .claude/hooks/beilinson-
# gate.sh. Writes under .claude/hooks/ were sandboxed off during the 2026-
# 04-22 inscription session; the snippet lives here in notes/ awaiting
# manual install. To install: splice this block into beilinson-gate.sh
# immediately BEFORE the `# SECTION 4 ... PROPAGATION` closing `fi` on
# line 356, ahead of the `CONTEXT=""` block that begins the OUTPUT
# section. The block uses the same ISSUES / WARNINGS accumulators and
# output JSON structure already present in the hook.
#
# Cross-references.
#  - notes/antipatterns_catalogue.md  (Session 2026-04-22 section)
#  - notes/first_principles_cache_comprehensive.md  (per-pattern cache)
#  - notes/first_principles_cache.md  (reader-oriented row set)
#
# Scope discipline. Conservative carve-outs: `cascade`, `homological
# retraction`, `deformation retract`, `retracts onto` are legitimate math
# and are excluded via negative filters. `Borcherds programme`, `Langlands
# programme`, `minimal model programme`, `Platonic solid` remain
# legitimate. Forbidden forms targeted: `Platonic Theorem~A`, `our
# programme`, `programme-canonical`, `platonic chapter`, `\begin{warning}`,
# `\ClaimStatusRetracted`, drafting-dated remarks, `History of the claim`,
# retraction indices.
#
# Standing principle (from CLAUDE.md of all three volumes): the manuscript
# is self-complete, self-coherent, self-consistent; the current version
# stands for itself and only itself. No references to previous versions,
# intermediate ansätze, earlier drafts, retracted values, superseded
# formulas, or drafting-history commentary. Bookkeeping, meta-narration,
# and version-history apparatus belong in `notes/`, `FRONTIER.md`, commit
# messages, and `memory/` — never in the manuscript.
# ==========================================================================

# === Session 2026-04-22: manuscript hygiene (CGCLEAN-1..55) ===
if [[ "$FILE_PATH" == *.tex ]]; then
  case "$FILE_PATH" in
    */chapters/*|*/frame/*|*/examples/*|*/theory/*|*/connections/*|*/appendices/*) CG_SCOPE=1 ;;
    *) CG_SCOPE=0 ;;
  esac
  if [ "$CG_SCOPE" -eq 1 ]; then
    # CGCLEAN-1: Wave $N$ session label in manuscript
    LINE=$(grep -En '\b[Ww]ave[ ~-]?[0-9]+' "$FILE_PATH" 2>/dev/null | grep -v '^[[:space:]]*%' | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-1: 'Wave N' session label in manuscript. Delete; cite theorem / primary source. Line: ${LINE}\n"
    # CGCLEAN-2: AP registry codes (AP-CY, AP-CAT, APn)
    LINE=$(grep -En '\b(AP-?CY[0-9]+|AP-?CAT-?[0-9]+|AP[0-9]+)\b' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-2: AP registry code in manuscript. Inscribe hazard as Remark. Line: ${LINE}\n"
    # CGCLEAN-3: FM hook-index marker (exclude FM_n compactification notation)
    LINE=$(grep -En '\bFM[0-9]+\b' "$FILE_PATH" 2>/dev/null | grep -vE 'FM_[0-9{]|\\FM|Fulton' | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-3: FM hook-index marker in manuscript. State bridge mathematically. Line: ${LINE}\n"
    # CGCLEAN-4: HZ hierarchy label
    LINE=$(grep -En 'HZ-?[IVX0-9]+|HZ discipline|HZ[- ]hierarchy' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-4: HZ hierarchy label. State verification paths directly. Line: ${LINE}\n"
    # CGCLEAN-5: DNA strand / S-strand
    LINE=$(grep -En 'DNA strand|S-?strand|strand\s+S[0-9]+' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-5: DNA strand (swarm metaphor) in manuscript. Inscribe content directly. Line: ${LINE}\n"
    # CGCLEAN-6: CG-rectify pass / rectification pass
    LINE=$(grep -En '[Cc][Gg]-?rectify pass [0-9]+|rectification pass [0-9]+' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-6: CG-rectify pass number in manuscript. Delete. Line: ${LINE}\n"
    # CGCLEAN-7: cache entry / Cached Confusion / Cache anchor / Cache append
    LINE=$(grep -En '[Cc]ache entry [0-9]+|Cached Confusion|Cache anchor|Cache append' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-7: Cache-registry reference in manuscript. Cite primary source. Line: ${LINE}\n"
    # CGCLEAN-8: Wave N spec/verdict/witness
    LINE=$(grep -En '[Ww]ave[ ~-]?[0-9]+\s*(spec|verdict|witness)' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-8: Wave adjudication frame. State result as theorem/remark. Line: ${LINE}\n"
    # CGCLEAN-9: programme-canonical
    LINE=$(grep -En 'programme[ -]canonical|programme canonical value' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-9: 'programme-canonical' (meta-adjective). Use 'canonical' or delete. Line: ${LINE}\n"
    # CGCLEAN-10: type-error registry T-code
    LINE=$(grep -En 'type-?error (registry )?T[0-9]+|\bT[0-9]+ registry' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-10: Type-error registry code. State as mathematical type mismatch. Line: ${LINE}\n"
    # CGCLEAN-11: narrative counterpart/arc
    LINE=$(grep -En 'narrative (counterpart|arc)' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-11: 'narrative counterpart/arc'. State construction directly. Line: ${LINE}\n"
    # CGCLEAN-12: narrative nouns (story, saga, odyssey, journey) as preceding-determiner nouns
    LINE=$(grep -En '\b(the|this|a|our) (story|saga|odyssey|journey)\b' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-12: Narrative noun (story/saga/odyssey/journey). Delete; state theorem. Line: ${LINE}\n"
    # CGCLEAN-13: Platonic meta-adjective (Platonic solid exempt)
    LINE=$(grep -En '[Pp]latonic (ideal|form|chapter|architecture|ensemble|synthesis)' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-13: 'Platonic' meta-adjective (Platonic solid exempt). Delete. Line: ${LINE}\n"
    # CGCLEAN-14: Platonic Theorem~X
    LINE=$(grep -En '[Pp]latonic Theorem[ ~][A-Z]' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-14: 'Platonic Theorem~X'. Use 'Theorem X' with \\ref{thm:...}. Line: ${LINE}\n"
    # CGCLEAN-15: This chapter's function is to...
    LINE=$(grep -Eni "[Tt]his (chapter|section)('s| is)? function is to|[Tt]he function of this (chapter|section) is" "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-15: Authorial-intent narration. Delete; chapter performs by being read. Line: ${LINE}\n"
    # CGCLEAN-16: signpost phrases (reinforces existing PROSE block)
    for PHRASE in "we now turn to" "having established" "let us now" "this brings us to" "with this in hand"; do
      if grep -qi "$PHRASE" "$FILE_PATH" 2>/dev/null; then
        LINE=$(grep -n -i "$PHRASE" "$FILE_PATH" | head -1)
        ISSUES="${ISSUES}CGCLEAN-16: Signpost '${PHRASE}'. Replace with direct mathematical transition. Line: ${LINE}\n"
      fi
    done
    # CGCLEAN-17: self-referential voice (Borcherds/Langlands programme exempt)
    for PHRASE in "in the present work" "our programme" "we have argued" "it is worth noting"; do
      if grep -qi "$PHRASE" "$FILE_PATH" 2>/dev/null; then
        LINE=$(grep -n -i "$PHRASE" "$FILE_PATH" | grep -v 'Borcherds programme\|Langlands programme\|Manin.*programme\|minimal model programme\|LMP\|langlands' | head -1)
        [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-17: Self-referential voice '${PHRASE}'. Delete. Line: ${LINE}\n"
      fi
    done
    LINE=$(grep -En '\bthe author\b' "$FILE_PATH" 2>/dev/null | grep -v 'the authors' | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-17: 'the author' self-reference. Delete. Line: ${LINE}\n"
    # CGCLEAN-18: chapter-closing meta-paragraph
    LINE=$(grep -En '[Tt]his (chapter|section) closes' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-18: Chapter-closing meta-paragraph. Delete. Line: ${LINE}\n"
    # CGCLEAN-19: preface self-reference
    LINE=$(grep -En 'opening paragraphs? of (this|the) preface|as noted in the preface' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-19: Preface self-reference. Use \\ref{thm:...}. Line: ${LINE}\n"
    # CGCLEAN-20: Earlier/Later in the volume
    LINE=$(grep -En '(Earlier|Later) in (the|this) volume' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-20: Drafting-order navigation. Use \\ref label. Line: ${LINE}\n"
    # CGCLEAN-21: retracted/retraction (deformation/homological retraction exempt)
    LINE=$(grep -En '\b[Rr]etract(ed|ion|s)\b' "$FILE_PATH" 2>/dev/null | grep -vE 'deformation retract|homological retract|retracts onto|strong deformation|chain retraction|strong retract' | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-21: 'retracted/retraction' (drafting). Delete retracted claim and its marker. Line: ${LINE}\n"
    # CGCLEAN-22: superseded
    LINE=$(grep -En '\bsupersede[ds]?\b' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-22: 'superseded/supersedes' (drafting). Line: ${LINE}\n"
    # CGCLEAN-23: drafting-history phrases
    LINE=$(grep -En 'earlier draft|previous version|intermediate ansatz|prior derivation' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-23: Drafting-history phrase. State current derivation only. Line: ${LINE}\n"
    # CGCLEAN-24: previously conjectural/open/unresolved/obstructing
    LINE=$(grep -En 'previously (conjectural|open|unresolved|obstructing)' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-24: 'previously X' temporal status. Line: ${LINE}\n"
    # CGCLEAN-25: now resolved/proved/known
    LINE=$(grep -En '\bnow (resolved|proved|known)\b' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-25: 'now resolved/proved/known' temporal qualifier. Line: ${LINE}\n"
    # CGCLEAN-26: double/triple-retraction
    LINE=$(grep -En 'double-?retraction|triple-?retraction' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-26: Double/triple-retraction. Delete. Line: ${LINE}\n"
    # CGCLEAN-27: Three successive evaluations / History of the claim
    LINE=$(grep -En 'Three successive evaluations|History of the claim' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-27: Drafting-record callout. Inscribe failed arguments as Gap/Flaw lemmas. Line: ${LINE}\n"
    # CGCLEAN-28: drafting record/trajectory/history
    LINE=$(grep -En 'drafting (record|trajectory|history)' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-28: 'drafting X' self-narration. Delete. Line: ${LINE}\n"
    # CGCLEAN-29: \ClaimStatusRetracted
    LINE=$(grep -En '\\ClaimStatusRetracted' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-29: \\ClaimStatusRetracted tag. Delete claim or inscribe as Gap/Flaw lemma. Line: ${LINE}\n"
    # CGCLEAN-30: dated remarks (exclude .bib)
    case "$FILE_PATH" in
      *.bib) ;;
      *)
        LINE=$(grep -En '\b20[12][0-9]-[01][0-9]-[0-3][0-9]\b' "$FILE_PATH" 2>/dev/null | head -1)
        [ -n "$LINE" ] && WARNINGS="${WARNINGS}CGCLEAN-30: Dated YYYY-MM-DD remark. Delete date; inscription is timeless. Line: ${LINE}\n"
        ;;
    esac
    # CGCLEAN-31: \index{retraction!...}
    LINE=$(grep -En '\\index\{retraction!' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-31: \\index{retraction!...} entry. Remove. Line: ${LINE}\n"
    # CGCLEAN-32: \texttt{notes/...}
    LINE=$(grep -En '\\texttt\{notes/' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-32: \\texttt{notes/...} reader-facing reference. Promote or delete. Line: ${LINE}\n"
    # CGCLEAN-33: /Users/raeez paths
    LINE=$(grep -En '/Users/raeez' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-33: Absolute home path in manuscript. Replace with \\ref or delete. Line: ${LINE}\n"
    # CGCLEAN-34: % TODO librarian verification
    LINE=$(grep -En '%[^\n]*TODO[^\n]*librarian|%[^\n]*librarian verification' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && WARNINGS="${WARNINGS}CGCLEAN-34: % TODO librarian verification comment. Verify or delete. Line: ${LINE}\n"
    # CGCLEAN-35: % ALIAS / % LEGACY ALIAS
    LINE=$(grep -En '%\s*(LEGACY\s+)?ALIAS\b' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && WARNINGS="${WARNINGS}CGCLEAN-35: % ALIAS / LEGACY ALIAS comment. Rename label; delete comment. Line: ${LINE}\n"
    # CGCLEAN-36: % Source provenance
    LINE=$(grep -En '%\s*Source:\s*(NEW CHAPTER|[Ww]ave[ ~-]?[0-9]+)' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && WARNINGS="${WARNINGS}CGCLEAN-36: % Source provenance comment. Delete. Line: ${LINE}\n"
    # CGCLEAN-37: waveN engine filename
    LINE=$(grep -En '_wave[0-9]+_[A-Za-z0-9_]*\.py' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-37: Compute-engine filename with waveN index. Rename; cite canonical. Line: ${LINE}\n"
    # CGCLEAN-38: waveN_foo function name
    LINE=$(grep -En '\bwave[0-9]+_[A-Za-z_]+\b' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-38: Function name waveN_foo. Rename. Line: ${LINE}\n"
    # CGCLEAN-39: \begin{warning}
    LINE=$(grep -En '\\begin\{warning\}' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-39: \\begin{warning} environment. Replace with \\begin{remark} or delete. Line: ${LINE}\n"
    # CGCLEAN-40: hedging phrases
    LINE=$(grep -Eni '\bdo not confuse\b|\bdon.t be fooled\b|\bbeware\b|\bbe careful\b' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-40: Hedging phrase (do not confuse / beware / be careful). Delete; state precisely. Line: ${LINE}\n"
    # CGCLEAN-41: we must be careful
    LINE=$(grep -Eni '\bwe must be careful\b' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-41: 'we must be careful' self-hedge. Delete; state scope. Line: ${LINE}\n"
    # CGCLEAN-42: scope-restricted/bounded
    LINE=$(grep -En 'scope-?(restricted|bounded)' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && WARNINGS="${WARNINGS}CGCLEAN-42: 'scope-restricted/bounded' meta-adjective. Name actual scope. Line: ${LINE}\n"
    # CGCLEAN-43: 'Verdict:' as meta-label
    LINE=$(grep -En '^\s*\\?[Vv]erdict:' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-43: 'Verdict:' meta-label. Use Theorem/Proposition/Lemma/Corollary/Remark. Line: ${LINE}\n"
    # CGCLEAN-44: filename *_platonic.tex
    case "$FILE_PATH" in
      *_platonic.tex|*platonic*.tex) ISSUES="${ISSUES}CGCLEAN-44: Filename contains 'platonic' meta-tag: ${FILE_PATH}. Rename.\n" ;;
    esac
    # CGCLEAN-45: label ch:*-platonic
    LINE=$(grep -En '\\label\{ch:[^}]*platonic\}' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-45: Chapter label ch:*-platonic. Rename; update \\ref. Line: ${LINE}\n"
    # CGCLEAN-46: label sec:*-platonic
    LINE=$(grep -En '\\label\{sec:[^}]*platonic\}' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-46: Section label sec:*-platonic. Rename; update \\ref. Line: ${LINE}\n"
    # CGCLEAN-47: thm:*-waveN-*
    LINE=$(grep -En '\\label\{thm:[^}]*-wave[0-9]+-[^}]*\}' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-47: Theorem label carries waveN index. Rename to canonical content. Line: ${LINE}\n"
    # CGCLEAN-48: \index{compute module!...}
    LINE=$(grep -En '\\index\{compute module!' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-48: \\index{compute module!...} entry. Remove. Line: ${LINE}\n"
    # CGCLEAN-49: \index{cache!...}
    LINE=$(grep -En '\\index\{cache!' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-49: \\index{cache!...} entry. Remove. Line: ${LINE}\n"
    # CGCLEAN-50: \index{retraction!...} — duplicate of CGCLEAN-31 for hook-completeness.
    # CGCLEAN-51: Five attack-heal calibrations
    LINE=$(grep -En '[Ff]ive attack-?heal calibrations' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-51: 'Five attack-heal calibrations'. List the five theorems/checks. Line: ${LINE}\n"
    # CGCLEAN-52: Reconstitution if cancellation fails
    LINE=$(grep -En '[Rr]econstitution if the cancellation fails' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-52: 'Reconstitution if cancellation fails'. State cancellation theorem or obstruction lemma. Line: ${LINE}\n"
    # CGCLEAN-53: Inversion of the programme perspective
    LINE=$(grep -En '[Ii]nversion of the programme perspective' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-53: 'Inversion of the programme perspective'. State dual construction. Line: ${LINE}\n"
    # CGCLEAN-54: Gold-standard HZ-IV disjoint verification
    LINE=$(grep -En '[Gg]old-?standard HZ-?IV disjoint verification' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-54: 'Gold-standard HZ-IV disjoint verification'. List concrete paths. Line: ${LINE}\n"
    # CGCLEAN-55: Three successive evaluations (verbatim)
    LINE=$(grep -En 'Three successive evaluations appear in the drafting record' "$FILE_PATH" 2>/dev/null | head -1)
    [ -n "$LINE" ] && ISSUES="${ISSUES}CGCLEAN-55: Drafting-record callout (verbatim). Inscribe three Gap/Flaw lemmas. Line: ${LINE}\n"
  fi
fi
# === end CGCLEAN block ===
