---
description: "Cross-volume AP5 propagation check from Vol II"
---

# Cross-Volume Propagation Check (AP5) — Vol II

**Pattern**: $ARGUMENTS

Same protocol as Vol I `/propagate`. Extra Vol II nuance:

**AP49 Convention Alert**: Vol II uses lambda-brackets (divided powers). Vol I uses OPE modes. The coefficient at order n differs by 1/n!. When grepping for a Vol II formula in Vol I, apply the conversion BEFORE comparing.

```bash
grep -rn "$ARGUMENTS" ~/chiral-bar-cobar/chapters/ ~/chiral-bar-cobar/appendices/ 2>/dev/null
grep -rn "$ARGUMENTS" ~/chiral-bar-cobar-vol2/chapters/ ~/chiral-bar-cobar-vol2/appendices/ 2>/dev/null
grep -rn "$ARGUMENTS" ~/calabi-yau-quantum-groups/chapters/ ~/calabi-yau-quantum-groups/notes/ 2>/dev/null
```

Also check compute layers across all three volumes.
