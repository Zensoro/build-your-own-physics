"""挑战 01 自动验收。运行：python verify.py"""

import math
import sys

sys.path.insert(0, ".")
from projectile import simulate

G = 9.81

passed, failed = [], []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


V0, THETA = 50.0, 45.0

print("=== S1.1 接口 ===")
times, xs, ys = simulate(V0, THETA)
check("返回三个列表且长度相等", len(times) == len(xs) == len(ys) > 0)
check("从原点出发", abs(xs[0]) < 1e-12 and abs(ys[0]) < 1e-12)
check("时间从 0 开始", abs(times[0]) < 1e-12)

print("=== S1.2 轨迹形状 ===")
check("y 除最后一步外 >= 0（落地即停）", min(ys[:-1]) >= -1e-9)
check("y 有上升段和下降段（抛物线）",
      max(ys) > 10.0 and ys[0] < max(ys) and ys[-1] < max(ys))

print("=== S1.3 射程精度（收敛性检验） ===")
R_theory = V0**2 * math.sin(2 * math.radians(THETA)) / G

def range_of(dt):
    _, xs_dt, _ = simulate(V0, THETA, dt=dt)
    return xs_dt[-1]

R_fine = range_of(0.001)
err_fine = abs(R_fine - R_theory) / R_theory
check(f"dt=0.001 射程 {R_fine:.1f}m vs 理论 {R_theory:.1f}m, 误差 {err_fine:.2%} < 2%",
      err_fine < 0.02)

# 收敛性：固定 t=1s 比较 y 值（避开"落地跨步"和"步长对齐"干扰）
# 欧拉法是一阶精度 → 步长减半，误差约减半（误差 = g*t*dt/2）
def y_at(t_target, dt):
    """用线性插值取精确 t_target 时刻的 y（避免最后一步越过 t_target）。"""
    times_t, _, ys_t = simulate(V0, THETA, dt=dt, t_max=t_target + dt)  # 多跑一步
    for i in range(1, len(times_t)):
        if times_t[i] >= t_target:
            t0, t1 = times_t[i - 1], times_t[i]
            f = (t_target - t0) / (t1 - t0)
            return ys_t[i - 1] + f * (ys_t[i] - ys_t[i - 1])
    return ys_t[-1]

y_theory = V0 * math.sin(math.radians(THETA)) * 1.0 - 0.5 * G * 1.0**2
err_d1 = abs(y_at(1.0, 0.2) - y_theory)
err_d2 = abs(y_at(1.0, 0.1) - y_theory)
check(f"收敛性: dt=0.2 误差 {err_d1:.3f}m ≈ 2× dt=0.1 误差 {err_d2:.3f}m",
      err_d1 > 0.01 and abs(err_d1 / max(err_d2, 1e-9) - 2.0) < 0.4)

print("=== S1.4 最高点精度 ===")
H_theory = (V0 * math.sin(math.radians(THETA)))**2 / (2 * G)
H_sim = max(ys)
err_h = abs(H_sim - H_theory) / H_theory
check(f"最高点 {H_sim:.1f}m vs 理论 {H_theory:.1f}m, 误差 {err_h:.2%} < 2%", err_h < 0.02)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 02 吧！")
