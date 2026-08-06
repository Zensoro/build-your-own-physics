"""挑战 08 自动验收。运行：python verify.py"""

import sys
import numpy as np

sys.path.insert(0, ".")
from fluid import simulate_lid_driven

passed, failed = [], []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


NX, NY, TAU, U, STEPS = 32, 32, 0.6, 0.1, 5000
rho, ux, uy = simulate_lid_driven(nx=NX, ny=NY, tau=TAU, U_wall=U,
                                  n_steps=STEPS)

print("=== S8.1 接口 ===")
check(f"返回 (rho, ux, uy) 形状 (ny,nx) = ({NY},{NX})",
      rho.shape == (NY, NX) and ux.shape == (NY, NX) and uy.shape == (NY, NX))

print("=== S8.2 质量守恒 ===")
mass0 = NX * NY
mass_rel = abs(rho.sum() - mass0) / mass0
check(f"Σρ 相对偏差 {mass_rel:.2%} < 2%", mass_rel < 0.02)

print("=== S8.3 中心主涡（回流） ===")
cx_, cy_ = NX // 2, NY // 2
check(f"中心 ux = {ux[cy_, cx_]:.4f} < 0（顶层向右 → 中心回流）",
      ux[cy_, cx_] < 0)

print("=== S8.4 顶盖速度 ===")
lid_ux = ux[-1, :].mean()
check(f"顶盖行平均 ux = {lid_ux:.4f} > 0.8·U = {0.8 * U}",
      lid_ux > 0.8 * U)

print("=== S8.5 速度场连续（无棋盘振荡） ===")
# 避开边界层（顶盖附近物理梯度大），检查内部区域的高频振荡
inner = ux[4:-4, 4:-4]
d = np.max(np.abs(np.diff(inner, axis=1)))
check(f"内部区域 ux 最大相邻差分 {d:.4f} < 0.02（光滑，无棋盘模式）", d < 0.02)

print("=== S8.6 两个角涡（反向旋转） ===")
c_l, c_r = 2, NX - 3
check(f"左下角 uy = {uy[2, c_l]:.4f} < 0 且 右下角 uy = {uy[2, c_r]:.4f} > 0",
      uy[2, c_l] < 0 and uy[2, c_r] > 0)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 09 吧！")
