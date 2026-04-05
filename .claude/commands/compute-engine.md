---
description: "Scaffold a new Vol II compute engine"
---

# New Compute Engine — Vol II

**Engine name/topic**: $ARGUMENTS

Same protocol as Vol I `/compute-engine`. Vol II compute modules live at `~/chiral-bar-cobar-vol2/compute/`.

### Vol II-specific engine patterns

- Swiss-cheese operation computations (m_k^{SC} at higher arity)
- PVA descent verification (D2-D6 axiom checks)
- Bulk-boundary-line triangle consistency
- E_1/E_infinity R-matrix computations
- Spectral braiding at specific parameter values
- Lambda-bracket computations (remember AP44: 1/n! conversion)

### Test standard
```bash
cd ~/chiral-bar-cobar-vol2 && python3 -m pytest compute/tests/test_{name}_engine.py -v
```

Minimum 30 tests, 3 verification paths per formula.
