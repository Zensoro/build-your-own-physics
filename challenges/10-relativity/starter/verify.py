"""挑战 10 自动验收。运行：python verify.py"""

import math
import sys
import random

sys.path.insert(0, ".")
from relativity import gamma, lorentz, inverse_lorentz, spacetime_interval
from relativity import time_dilation, length_contraction

passed, failed = [], []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


print("=== S10.1 γ 因子 ===")
check(f"γ(0.6c) = {gamma(0.6):.4f} = 1.25", abs(gamma(0.6) - 1.25) < 1e-9)
check("γ(0) = 1", abs(gamma(0.0) - 1.0) < 1e-12)

print("=== S10.2 时空间隔不变 ===")
random.seed(42)
ok = True
for _ in range(1000):
    e = (random.uniform(-10, 10), random.uniform(-10, 10),
         random.uniform(-10, 10), random.uniform(-10, 10))
    v = random.uniform(0.0, 0.9)
    e_p = lorentz(e, v)
    s2 = spacetime_interval(e, (0, 0, 0, 0))
    s2_p = spacetime_interval(e_p, (0, 0, 0, 0))
    if abs(s2 - s2_p) > 1e-9:
        ok = False
        break
check("1000 个随机事件：s² 变换前后不变 (<1e-9)", ok)

print("=== S10.3 光速不变 ===")
ct, x = 3.0, 3.0   # 光信号 (c=1)
ok = True
for v in [0.1, 0.5, 0.9]:
    ct_p, x_p, _, _ = lorentz((ct, x, 0.0, 0.0), v)
    if abs(x_p / ct_p - 1.0) > 1e-9:
        ok = False
check("任意 v 下光信号速度 = c", ok)

print("=== S10.4 逆变换 ===")
e = (4.0, 2.0, 1.0, 3.0)
e_back = inverse_lorentz(lorentz(e, 0.6), 0.6)
ok = all(abs(a - b) < 1e-9 for a, b in zip(e, e_back))
check("S→S'→S 往返后恢复原事件", ok)

print("=== S10.5 尺缩与钟慢 ===")
check(f"钟慢：Δτ=1s → Δt={time_dilation(1.0, 0.6):.4f}s = γ·1s",
      abs(time_dilation(1.0, 0.6) - 1.25) < 1e-9)
check(f"尺缩：L0=1m → L={length_contraction(1.0, 0.6):.4f}m = 1/γ",
      abs(length_contraction(1.0, 0.6) - 0.8) < 1e-9)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 11 吧！")
