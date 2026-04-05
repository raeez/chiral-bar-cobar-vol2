---
description: "Multi-path formula verification for Vol II claims"
---

# Multi-Path Formula Verification — Vol II

**Claim**: $ARGUMENTS

Same 8-path taxonomy as Vol I `/verify`. Vol II-specific paths:

### Additional verification paths for Vol II

- **Swiss-cheese structure check**: Verify against the SC^{ch,top} operad directly
- **PVA descent check**: Does the claim descend correctly to the PVA shadow?
- **Bulk-boundary consistency**: Does the formula respect Z^der_ch(A) = universal bulk?
- **Convention bridge**: Verify the same formula in Vol I OPE-mode convention (AP49: divide lambda-bracket coefficients by n!)

### Vol II-specific AP traps
- AP44: lambda-bracket coefficient at order n is a_{(n)}b/n!
- AP-OC: bar classifies twisting morphisms, NOT bulk
- AP19: r-matrix poles one less than OPE (d log absorption)

Minimum 3 independent paths. Write tests. Cross-check across volumes.
