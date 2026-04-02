"""Timing test: T_k(1,...,1) for k=2,...,25 WITHOUT clearing cache."""
import sys, os, time, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 1)

from compute.m7_m10_depth_frontier import StasheffEngine

def catalan(n):
    if n < 0: return 0
    return math.comb(2*n, n) // (n+1)

engine = StasheffEngine(1.0)
t_total = time.time()

for k in range(2, 26):
    lams = tuple(1.0 for _ in range(k-1))
    t0 = time.time()
    result = engine.mk(lams)
    dt = time.time() - t0
    T = result.get(0, 0.0)
    S = result.get(-1, 0.0)
    P = S * 12.0

    if k % 2 == 1 and k >= 3:
        r = (k-1)//2
        T_cat = (-1)**(r+1) * k * catalan(r-1) * math.factorial(2*r)
        err = abs(T - T_cat) / max(1, abs(T_cat))
        print(f"k={k:>2} r={r:>2}  T={T:>25.1f}  T_cat={T_cat:>25.0f}  err={err:.2e}  P={P:>25.1f}  dt={dt:.3f}s  cache={len(engine._cache)}")
    else:
        print(f"k={k:>2}       T={T:>25.6f}  (even, should be 0)  P={P:>25.1f}  dt={dt:.3f}s  cache={len(engine._cache)}")

print(f"\nTotal time: {time.time() - t_total:.1f}s")
