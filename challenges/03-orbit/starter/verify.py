"""挑战 03 自动验收。运行：python verify.py"""

import math
import sys

sys.path.insert(0, ".")
from orbit import simulate, MU

DT = 0.001   # 年
N = 1000     # 一年

passed, failed = [], []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


def energy_series(xs, ys, mu, dt):
    """从前向差分恢复速度，计算每个时刻的能量 E = 1/2 v^2 - mu/r。

    蛙跳法中，速度 v(n+1/2) = (x[n+1] - x[n]) / dt 可精确恢复。
    用位置 x[n+1] 计算势能，得到能量序列。
    """
    es = []
    for i in range(len(xs) - 1):
        vx = (xs[i + 1] - xs[i]) / dt
        vy = (ys[i + 1] - ys[i]) / dt
        es.append(0.5 * (vx**2 + vy**2) - mu / math.hypot(xs[i + 1], ys[i + 1]))
    return es


print("=== S3.1 接口 ===")
xs, ys = simulate(MU, 1.0, 0.0, 0.0, 2 * math.pi, DT, N)
check("返回列表长度 = n_steps + 1", len(xs) == N + 1 and len(ys) == N + 1)
check("初始位置正确", abs(xs[0] - 1.0) < 1e-12 and abs(ys[0]) < 1e-12)

print("=== S3.2 圆轨道稳定 ===")
r_vals = [math.hypot(x, y) for x, y in zip(xs, ys)]
check("轨道半径在 0.95~1.05 AU", 0.95 < min(r_vals) and max(r_vals) < 1.05)
check("一年后回到起点 (闭合)", math.hypot(xs[-1] - 1.0, ys[-1]) < 0.05)

print("=== S3.3 椭圆轨道 (0.8 v_c) ===")
xs_e, ys_e = simulate(MU, 1.0, 0.0, 0.0, 0.8 * 2 * math.pi, DT, N)
r_e = [math.hypot(x, y) for x, y in zip(xs_e, ys_e)]
check("椭圆：0.3 < min(r) < max(r) < 1.6", 0.3 < min(r_e) < max(r_e) < 1.6)

print("=== S3.4 能量守恒（蛙跳法核心优势） ===")
es = energy_series(xs, ys, MU, DT)
drift = abs(es[-1] - es[0]) / abs(es[0])
check(f"圆轨道 1000 步能量漂移 {drift:.4%} < 0.1%", drift < 0.001)

# 椭圆轨道：能量振荡有界（跑 5 年幅度不增长 = 辛积分器）
def osc_amp(xs, ys, mu, dt):
    es = energy_series(xs, ys, mu, dt)
    return (max(es) - min(es)) / abs(es[0])

amp_1y = osc_amp(xs_e, ys_e, MU, DT)
xs_e5, ys_e5 = simulate(MU, 1.0, 0.0, 0.0, 0.8 * 2 * math.pi, DT, 5 * N)
amp_5y = osc_amp(xs_e5, ys_e5, MU, DT)
check(f"椭圆能量振荡有界: 1年 {amp_1y:.3%} vs 5年 {amp_5y:.3%} (5年不显著增长)",
      amp_5y < amp_1y * 1.5)
print(f"  （辛积分器特征：振荡幅度不随时间增长；欧拉法则线性漂移）")

print("=== S3.6 逃逸速度 ===")
xs_p, ys_p = simulate(MU, 1.0, 0.0, 0.0, math.sqrt(2) * 2 * math.pi, DT, N)
r_p = math.hypot(xs_p[-1], ys_p[-1])
check(f"sqrt(2)*v_c 一年后 r={r_p:.2f} > 2 AU (逃逸)", r_p > 2.0)
xs_h, ys_h = simulate(MU, 1.0, 0.0, 0.0, 1.5 * 2 * math.pi, DT, N)
r_h = math.hypot(xs_h[-1], ys_h[-1])
check(f"1.5*v_c 一年后 r={r_h:.2f} > 3 AU (更快逃逸)", r_h > 3.0)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 04 吧！")
