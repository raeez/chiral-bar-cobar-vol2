---
description: "Beilinson rectification loop on a Vol II chapter"
model: opus
---

RECTIFICATION_SESSION_ACTIVE

# Beilinson Rectification Loop — Vol II

**Target**: $ARGUMENTS

Read CLAUDE.md (Vol II) before beginning. All Vol I anti-patterns AP1-AP50 apply. Vol II-specific: AP-OC (bar != bulk), AP35-AP58 (E_infinity/E_1 hierarchy), AP-CHR/AP-RED/AP-WICK.

The standard: Kac, Gelfand, Etingof, Beilinson, Drinfeld, Kazhdan, Bezrukavnikov, Polyakov, Nekrasov, Kapranov, Ginzburg, Chriss-Ginzburg.

## THE PROGRAMME

Same 4-phase structure as Vol I `/rectify`. Key Vol II differences:

### Build command
```bash
pkill -9 -f pdflatex; sleep 2; cd ~/chiral-bar-cobar-vol2 && make fast
```

### Vol II-specific audit checks
- **AP-OC**: Bar classifies twisting morphisms, NOT bulk observables. Bulk = Z^der_ch(A).
- **AP35-AP58**: E_infinity = ALL vertex algebras (including those with OPE poles). E_1 = nonlocal (quantum vertex algebras). NEVER say "vertex algebra is not E_infinity."
- **AP-CHR**: Pole order != chromatic height. Classical bar complex is height 0.
- **AP-WICK**: S-transform != Wick rotation of topological direction.
- **AP44**: lambda-bracket coefficient = a_{(n)}b/n!, NOT a_{(n)}b.
- **Three bar complexes**: FG bar (zeroth product only) != symmetric bar (Vol I Thm A) != ordered bar (Part VII).

### Cross-volume propagation
After ANY formula change, grep ALL THREE volumes:
```bash
grep -rn "PATTERN" ~/chiral-bar-cobar/chapters/ ~/chiral-bar-cobar-vol2/chapters/ ~/calabi-yau-quantum-groups/chapters/ 2>/dev/null
```

Convention check (AP49): Vol I uses OPE modes. Vol II uses lambda-brackets. The coefficient at order n differs by 1/n!.

### Phases 1-4
Same as Vol I `/rectify`. CONVERGE before stopping.
