TEX = pdflatex
TEXFLAGS = -interaction=nonstopmode -halt-on-error
MAIN = main
STAMP = .build_stamp

.PHONY: all fast clean veryclean test

all: $(STAMP)

$(STAMP): $(MAIN).tex $(wildcard chapters/*/*.tex) $(wildcard appendices/*.tex)
	@for pass in 1 2 3; do \
		echo "=== Pass $$pass ==="; \
		$(TEX) $(TEXFLAGS) $(MAIN).tex || exit 1; \
	done
	@touch $(STAMP)
	@echo "=== Build complete ==="

fast:
	$(TEX) $(TEXFLAGS) $(MAIN).tex

clean:
	rm -f $(MAIN).aux $(MAIN).log $(MAIN).out $(MAIN).toc $(MAIN).bbl $(MAIN).blg
	rm -f $(MAIN).idx $(MAIN).ind $(MAIN).ilg $(MAIN).lof $(MAIN).lot
	rm -f chapters/*/*.aux appendices/*.aux

veryclean: clean
	rm -f $(STAMP) $(MAIN).pdf

test:
	cd compute && .venv/bin/python -m pytest tests/ -q --timeout=120
