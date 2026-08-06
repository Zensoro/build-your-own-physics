"""挑战 06 自动验收。运行：python verify.py"""

import sys
import numpy as np

sys.path.insert(0, ".")
from heat import simulate_diffusion, carnot_efficiency, engine_efficiency

passed, failed = [], []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


print("=== S6.1 接口 ===")
nx = 100
x = np.linspace(0, 1, nx)
dx = x[1] - x[0]
T0 = np.where(x < 0.5, 1.0, 0.0)
hist, xr = simulate_diffusion(T0, alpha=1.0, dx=dx, dt=5e-5, n_steps=20000)
check("返回 (T_hist, x) 且帧数 = n_steps+1",
      hist.ndim == 2 and hist.shape == (20001, nx) and len(xr) == nx)

print("=== S6.2 热平衡：阶梯 → 线性 ===")
linear = 1.0 - xr / (nx - 1) / dx   # 固定端点 T(0)=1, T(L)=0 的稳态
dev = np.max(np.abs(hist[-1] - linear))
check(f"最终分布与线性稳态最大偏差 {dev:.4f} < 0.05", dev < 0.05)

print("=== S6.3 热流方向（第二定律） ===")
# 初始单调不增（阶梯）→ 稳定格式下始终单调不增：热永远从高温流向低温
max_up = np.max(np.diff(hist, axis=1))
check(f"任意时刻温度沿 x 单调不增 (上翻 {max_up:.2e} ≤ 1e-6)",
      max_up <= 1e-6)

print("=== S6.4 显式格式稳定性 ===")
# α·dt/dx² = 1·0.0001/0.0001 = 1 > 1/2 → 数值不稳定
hbad, _ = simulate_diffusion(T0, alpha=1.0, dx=dx, dt=1e-4, n_steps=500)
check(f"αdt/dx²>1/2 时温度发散 (max|T|={np.abs(hbad).max():.2e} > 2)",
      np.abs(hbad).max() > 2)

print("=== S6.5 热机效率 ≤ 卡诺效率 ===")
eta_c = carnot_efficiency(600, 300)
check(f"卡诺效率(600K,300K) = {eta_c:.3%} = 50%", abs(eta_c - 0.5) < 1e-12)
eta_e = engine_efficiency(600, 300)
check(f"矩形循环实际效率 {eta_e:.3%} < 卡诺 {eta_c:.3%}",
      0 < eta_e < eta_c)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 07 吧！")
