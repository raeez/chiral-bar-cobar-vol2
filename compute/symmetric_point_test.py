"""Quick test: T_k(1,...,1) for k=2,...,12 with timing."""
import sys, os, time, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 1)  # line-buffered

from compute.m7_m10_depth_frontier import StasheffEngine

engine = StasheffEngine(1.0)

for k in range(2, 13):
    engine._cache.clear()
    lams = tuple(1.0 for _ in range(k - 1))
    t0 = time.time()
    result = engine.mk(lams)
    dt = time.time() - t0
    T_coeff = result.get(0, 0.0)
    scalar = result.get(-1, 0.0)
    P_k = scalar / (1.0 / 12.0) if abs(scalar) > 1e-300 else 0.0
    print(f"k={k:>2}  T={T_coeff:>20.6f}  P={P_k:>20.1f}  time={dt:.3f}s  cache_size={len(engine._cache)}")
