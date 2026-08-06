"""挑战 07 自动验收。运行：python verify.py"""

import sys
import numpy as np

sys.path.insert(0, ".")
from double_pendulum import simulate, simulate_euler, energy, derivs

passed, failed = [], []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


print("=== S7.1 接口 ===")
t, s = simulate(0.1, 0.05, dt=0.005, t_max=20)
check("返回 (times, states) 且 states 形状 (n,4)",
      t.shape == s.shape[:1] == (4001,) and s.shape[1] == 4)

print("=== S7.2 小角度 · 有界振荡 ===")
th1 = s[:, 0]
check(f"|θ1| 有界 < 0.2 (实测 max={np.abs(th1).max():.3f})",
      np.abs(th1).max() < 0.2)
n_cross = int(np.sum(np.diff(np.sign(th1)) != 0))
check(f"θ1 过零 {n_cross} 次（在振荡，未停滞）", n_cross > 10)

print("=== S7.3 RK4 能量守恒 ===")
e = energy(s)
drift = abs(e[-1] - e[0]) / e[0]
check(f"20s 能量相对漂移 {drift:.3%} < 0.5%", drift < 0.005)

print("=== S7.4 混沌 · 初值敏感（李雅普诺夫） ===")
t1, s1 = simulate(2.0, 2.0, dt=0.005, t_max=6)
t2, s2 = simulate(2.0 + 1e-8, 2.0, dt=0.005, t_max=6)
d = np.linalg.norm(s1 - s2, axis=1)          # 轨迹间距 d(t)
i1, i4 = int(1.0 / 0.005), int(4.0 / 0.005)
lam = np.log(d[i4] / max(d[i1], 1e-300)) / 3.0   # λ ≈ ln(d4/d1)/(t4-t1)
check(f"估计李雅普诺夫指数 λ ≈ {lam:.2f} /s > 0.3 (指数发散)",
      lam > 0.3)

print("=== S7.5 欧拉 vs RK4 能量漂移对比 ===")
te, se = simulate_euler(0.1, 0.05, dt=0.005, t_max=20)
drift_e = abs(energy(se)[-1] - energy(se)[0]) / energy(se)[0]
check(f"欧拉漂移 {drift_e:.2%} > 10× RK4 漂移 {drift:.3%}",
      drift_e > 10 * drift)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 08 吧！")
