"""挑战 12 自动验收。运行：python verify.py"""

import sys
import numpy as np

sys.path.insert(0, ".")
from solar import simulate_solar, total_energy, orbital_period, PLANETS

passed, failed = [], []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


DT = 0.001

print("=== S12.1 接口 ===")
pos, vel, masses = simulate_solar(dt=DT, years=1.0)
check("返回 (pos_hist, vel_hist, masses)，9 个天体",
      pos.shape == (1001, 9, 2) and vel.shape == (1001, 9, 2)
      and len(masses) == 9 and masses[0] == 1.0)

print("=== S12.2 轨道稳定（10 年无逃逸/无撞太阳） ===")
pos10, vel10, _ = simulate_solar(dt=DT, years=10.0)
r = np.linalg.norm(pos10[:, 1:, :], axis=2)   # 8 行星到太阳距离
check(f"半径范围 {r.min():.2f} ~ {r.max():.2f} AU（全部在轨）",
      r.min() > 0.1 and r.max() < 40.0)

print("=== S12.3 能量守恒 ===")
e = total_energy(pos10, vel10, masses)
drift = abs(e[-1] - e[0]) / abs(e[0])
check(f"10 年能量漂移 {drift:.3%} < 1%", drift < 0.01)

print("=== S12.4 开普勒第三定律 ===")
# 内行星（水星~火星）周期 < 10 年，能在模拟窗口内转满一圈；
# 外行星（木星 11.9 年、海王星 165 年）周期远超窗口，无法在此验证
inner = PLANETS[:4]
ok = True
for i, (name, a, m, phi) in enumerate(inner, start=1):
    T = orbital_period(pos10[:, i, 0], pos10[:, i, 1], DT)
    if T is None or abs(T**2 / a**3 - 1) > 0.02:
        ok = False
        print(f"  ✗ {name}: T={T}")
check(f"内行星（{', '.join(p[0] for p in inner)}）T²/a³ ≈ 1（误差 < 2%）", ok)

print("=== S12.5 收敛性（dt 减半结果一致） ===")
p1, _, _ = simulate_solar(dt=DT, years=1.0)
p2, _, _ = simulate_solar(dt=DT / 2, years=1.0)
diff = np.linalg.norm(p1[-1, 3, :] - p2[-1, 3, :])   # 地球 1 年后位置
check(f"地球 1 年后位置差异 {diff:.4f} AU < 0.05（收敛）", diff < 0.05)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！你毕业了！")
