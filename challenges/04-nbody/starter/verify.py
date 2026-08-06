"""挑战 04 自动验收。运行：python verify.py"""

import sys
import numpy as np

sys.path.insert(0, ".")
from nbody import simulate, total_energy, center_of_mass

DT, N = 0.001, 4000

passed, failed = [], []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


print("=== S4.1 接口 ===")
p0 = np.array([[-0.5, 0.0], [0.5, 0.0]])
v0 = np.array([[0.0, np.sqrt(0.5)], [0.0, -np.sqrt(0.5)]])
m2 = np.array([1.0, 1.0])
pos2, vel2 = simulate(p0, v0, m2, DT, N, soft=0.0)
check("返回帧数 = n_steps + 1", pos2.shape == (N + 1, 2, 2))

print("=== S4.2 对称二体 · 能量守恒 ===")
# 圆轨道：每体质心半径 0.5，速度 sqrt(0.5)，理论 E = -0.5
es = total_energy(pos2, vel2, m2, soft=0.0)
drift = abs(es[-1] - es[0]) / abs(es[0])
check(f"能量漂移 {drift:.3%} < 0.5%", drift < 0.005)

print("=== S4.3 质心守恒（动量守恒） ===")
com = center_of_mass(pos2, m2)
com_drift = np.max(np.linalg.norm(com - com[0], axis=1))
check(f"质心漂移 {com_drift:.2e} < 1e-6", com_drift < 1e-6)

print("=== S4.4 轨道稳定（不发散） ===")
r = np.linalg.norm(pos2 - com[:, None, :], axis=2)  # (frames, 2)
check(f"轨道半径稳定在 0.45~0.55 (实测 {r.min():.3f}~{r.max():.3f})",
      0.45 < r.min() and r.max() < 0.55)

print("=== S4.5 三体 · 不发散 ===")
rng = np.random.default_rng(7)
p3 = rng.uniform(-1, 1, (3, 2))
v3 = rng.uniform(-0.5, 0.5, (3, 2))
m3 = rng.uniform(0.5, 1.5, 3)
pos3, _ = simulate(p3, v3, m3, 0.01, 800, soft=0.05)
maxr = np.max(np.linalg.norm(pos3, axis=2))
check(f"三体模拟后最大半径 {maxr:.2f} < 20 (未飞散)", maxr < 20)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 05 吧！")
