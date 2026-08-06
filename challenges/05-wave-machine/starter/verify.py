"""挑战 05 自动验收。运行：python verify.py"""

import sys
import numpy as np

sys.path.insert(0, ".")
from wave import simulate

passed, failed = [], []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


def gaussian(x, x0, w):
    return np.exp(-((x - x0) / w) ** 2)


print("=== S5.1 接口 ===")
nx = 400
x = np.linspace(0, 4, nx)
dx = x[1] - x[0]
u0 = gaussian(x, 2.0, 0.15)
hist, xr = simulate(u0, c=1.0, dx=dx, dt=0.005, n_steps=150)
check("返回 (u_hist, x) 且帧数 = n_steps+1",
      hist.ndim == 2 and hist.shape == (151, nx) and len(xr) == nx)

print("=== S5.2 高斯波包分裂传播 ===")
peak0 = u0.max()
center_val = abs(hist[-1, nx // 2])
right_peak = abs(hist[-1, nx // 2:]).max()
left_peak = abs(hist[-1, :nx // 2]).max()
check(f"中心衰减 {center_val:.2f} < 0.4·{peak0:.2f}（能量分到两侧）",
      center_val < 0.4 * peak0)
check("两侧均出现波峰（分裂成两个）",
      right_peak > 0.3 * peak0 and left_peak > 0.3 * peak0)

print("=== S5.3 波速 = c ===")
# 右行波峰应在 x0 + c·t = 2.0 + 1·0.75 = 2.75 附近
t = 150 * 0.005
x_peak_right = xr[nx // 2 + np.argmax(hist[-1, nx // 2:])]
theory = 2.0 + 1.0 * t
check(f"右行波峰 x={x_peak_right:.2f} ≈ 理论 {theory:.2f} (误差<15%)",
      abs(x_peak_right - theory) < 0.15 * theory)

print("=== S5.4 边界反射相位 ===")
# 波包靠近右边界向右传播（t 足够到达边界并反射）
x2 = np.linspace(0, 4, nx)
u1 = gaussian(x2, 3.4, 0.12)
hf = simulate(u1, c=1.0, dx=dx, dt=0.005, n_steps=200, bc="fixed")[0]
hfree = simulate(u1, c=1.0, dx=dx, dt=0.005, n_steps=200, bc="free")[0]
inner = nx - 10  # 右边界内侧点
check("固定端边界恒为 0", np.allclose(hf[:, 0], 0) and np.allclose(hf[:, -1], 0))
check("自由端边界 ∂u/∂x=0（u[-1]=u[-2]）",
      np.allclose(hfree[:, -1], hfree[:, -2]))
# 固定端：撞击后内侧点出现负峰（相位反转）；自由端：保持同相（不出现明显负）
check("固定端反射相位反转（内侧出现谷，min<0）", hf[:, inner].min() < -0.1)
check("自由端反射同相（内侧不出现明显负，min>-0.05）",
      hfree[:, inner].min() > -0.05)

print("=== S5.5 CFL 条件（数值爆炸） ===")
xc = np.linspace(0, 4, nx)
uc = gaussian(xc, 2.0, 0.15)
# c·dt/dx = 1·0.03/0.01 = 3 > 1 → 不稳定
hbad = simulate(uc, c=1.0, dx=dx, dt=0.03, n_steps=200, bc="fixed")[0]
check(f"CFL 破坏时 |u| 数值发散 (max={hbad.max():.2e} > 5)", hbad.max() > 5)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 06 吧！")
