---
description: "Build Vol II, run tests"
---

# Build Vol II

```bash
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2
cd ~/chiral-bar-cobar-vol2 && make
echo "=== Vol II build complete ==="
cd ~/chiral-bar-cobar-vol2 && python3 -m pytest compute/tests/ -x --tb=short -q 2>/dev/null || echo "No Vol II tests or test failure"
echo "=== Tests complete ==="
```
