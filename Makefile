# ============================================================================
#  Makefile — A∞ Chiral Algebras and 3D Holomorphic-Topological QFT (Vol II)
# ============================================================================
#
#  Usage:
#    make            Full build (3 passes, stamp-based idempotent)
#    make fast       Single-pass build for quick iteration
#    make clean      Remove all LaTeX build artifacts
#    make veryclean  Remove artifacts AND compiled PDFs
#    make check      Halt-on-error validation
#    make count      Manuscript statistics
#    make test       Run compute test suite
#    make help       Show available targets
#
# ============================================================================

# --- Configuration -----------------------------------------------------------

MAIN      := main
TEX       := pdflatex
TEXFLAGS  := -interaction=nonstopmode -file-line-error -synctex=0
LOG_DIR   := .build_logs
PASSES    := 3
FAST_PASSES := 1

# Source files
SOURCES   := $(wildcard *.tex) \
             $(wildcard chapters/theory/*.tex) \
             $(wildcard chapters/examples/*.tex) \
             $(wildcard chapters/connections/*.tex) \
             $(wildcard appendices/*.tex)

# Output
PDF       := $(MAIN).pdf
STAMP     := .build_stamp

# If PDF was externally deleted but stamp remains, force a rebuild.
ifeq (,$(wildcard $(PDF)))
  $(shell rm -f $(STAMP))
endif

# LaTeX intermediate extensions
AUX_EXTS  := aux log out toc synctex.gz fdb_latexmk fls bbl blg \
             nav snm vrb idx ilg ind lof lot

# ============================================================================
#  Targets
# ============================================================================

.PHONY: all fast clean veryclean count check test help

## all: Full build with convergence detection.
all: $(STAMP)

$(STAMP): $(SOURCES)
	@echo "══════════════════════════════════════════════════════════"
	@echo "  Building: $(MAIN).tex  →  $(PDF)"
	@echo "  Engine:   $(TEX) (up to $(PASSES) passes)"
	@echo "══════════════════════════════════════════════════════════"
	@mkdir -p $(LOG_DIR)
	@converged=0; \
	for pass in $$(seq 1 $(PASSES)); do \
		echo "── Pass $$pass / $(PASSES) ──"; \
		$(TEX) $(TEXFLAGS) $(MAIN).tex >$(LOG_DIR)/pass$$pass.log 2>&1; \
		rc=$$?; \
		if [ $$rc -ne 0 ]; then \
			echo "  ✗  Pass $$pass failed."; \
			grep -aE '^\! |Emergency stop|Fatal error|Undefined control sequence' $(LOG_DIR)/pass$$pass.log | head -n 10; \
			exit $$rc; \
		fi; \
		pages=$$(strings $(PDF) 2>/dev/null | grep -c '/Type /Page' || echo '?'); \
		undef_cit=$$(grep -c 'Citation.*undefined' $(MAIN).log 2>/dev/null | tr -d ' \n' || echo 0); \
		undef_ref=$$(grep -c 'Reference.*undefined' $(MAIN).log 2>/dev/null | tr -d ' \n' || echo 0); \
		overfull=$$(grep -c 'Overfull \\\\hbox' $(MAIN).log 2>/dev/null | tr -d ' \n' || echo 0); \
		underfull=$$(grep -c 'Underfull \\\\hbox' $(MAIN).log 2>/dev/null | tr -d ' \n' || echo 0); \
		rerun=$$(grep -c 'Rerun to get' $(MAIN).log 2>/dev/null | tr -d ' \n' || echo 0); \
		echo "   $${pages}pp, $$undef_cit undef citations, $$undef_ref undef references, $$rerun rerun requests, $$overfull overfull, $$underfull underfull"; \
		if [ "$$rerun" = "0" ] && [ "$$undef_cit" = "0" ] && [ "$$undef_ref" = "0" ]; then \
			echo "✓ Converged after $$pass passes."; \
			converged=1; \
			break; \
		fi; \
	done; \
	if [ "$$converged" = "0" ]; then \
		echo "⚠ Did not fully converge after $(PASSES) passes (Cit=$$undef_cit, Ref=$$undef_ref, Rerun=$$rerun)."; \
	fi
	@touch $(STAMP)
	@echo "     Logs: $(LOG_DIR)/ and $(MAIN).log"

## fast: Single-pass quick build.
fast:
	@echo "  ── Fast build ($(FAST_PASSES) pass) ──"
	@mkdir -p $(LOG_DIR)
	@$(TEX) $(TEXFLAGS) $(MAIN).tex >$(LOG_DIR)/fast.log 2>&1 || { \
		echo "  ✗  Build failed."; \
		grep -aE '^\! |Emergency stop|Fatal error|Undefined control sequence' $(LOG_DIR)/fast.log | head -n 10; \
		exit 1; \
	}
	@echo "  ✓  Fast build complete."

## check: Halt on first error.
check:
	@echo "  ── Error check (halt-on-error) ──"
	@mkdir -p $(LOG_DIR)
	@$(TEX) -interaction=nonstopmode -halt-on-error $(MAIN).tex >$(LOG_DIR)/check.log 2>&1 || { \
		echo "  ✗  Check failed. See $(LOG_DIR)/check.log"; \
		grep -aE '^\! |Emergency stop|Fatal error|Undefined control sequence' $(LOG_DIR)/check.log | head -n 10; \
		exit 1; \
	}
	@echo "  ✓  No fatal errors."

## clean: Remove build debris but preserve the stamp.
clean:
	@echo "  Cleaning build artifacts..."
	@for ext in $(AUX_EXTS); do \
		rm -f $(MAIN).$$ext; \
	done
	@find chapters appendices -name '*.aux' -delete 2>/dev/null || true
	@rm -rf $(LOG_DIR)
	@rm -f texput.log
	@echo "  ✓  Clean (stamp preserved)."

## veryclean: Remove everything including PDF and stamp.
veryclean: clean
	@rm -f $(PDF) $(STAMP)
	@echo "  ✓  Stamp and PDF removed — next make will rebuild."

## count: Manuscript statistics.
count:
	@echo ""
	@echo "  ── Vol II Statistics ──"
	@printf "  Source files:   %s .tex files\n" "$$(find . -name '*.tex' -not -path './.build_logs/*' | wc -l | tr -d ' ')"
	@printf "  Total lines:   %s\n" "$$(find . -name '*.tex' -not -path './.build_logs/*' -exec cat {} + | wc -l | tr -d ' ')"
	@if [ -f $(PDF) ]; then \
		PAGES=$$(strings $(PDF) | grep -c '/Type /Page' 2>/dev/null || echo '?'); \
		printf "  PDF pages:     %s\n" "$$PAGES"; \
		printf "  PDF size:      %s\n" "$$(du -h $(PDF) | cut -f1)"; \
	else \
		echo "  PDF:           (not yet built — run 'make')"; \
	fi
	@echo ""

## test: Run compute test suite.
test:
	@if [ -d compute/tests ]; then \
		cd compute && .venv/bin/python -m pytest tests/ -q --timeout=120; \
	else \
		echo "  (no compute tests found)"; \
	fi

## help: Show available targets.
help:
	@echo ""
	@echo "  Vol II — Build System"
	@echo "  ─────────────────────"
	@echo ""
	@echo "  make            Full build ($(PASSES) passes, stamp-based)"
	@echo "  make fast       Quick single-pass build"
	@echo "  make check      Halt-on-error validation"
	@echo "  make clean      Remove build debris (preserves stamp)"
	@echo "  make veryclean  Remove everything (forces rebuild)"
	@echo "  make count      Manuscript statistics"
	@echo "  make test       Run compute tests"
	@echo "  make help       This message"
	@echo ""
