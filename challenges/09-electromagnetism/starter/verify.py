"""挑战 09 自动验收。运行：python verify.py"""

import sys
import numpy as np

sys.path.insert(0, ".")
from em import fdtd_1d, C0

passed, failed = [], []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


NZ, DZ = 2000, 1e-3

print("=== S9.1 接口 ===")
ez, hy, z = fdtd_1d(nz=400, dz=DZ, n_steps=400)
check("返回 (ez_hist, hy_hist, z) 形状正确",
      ez.shape == (400, 400) and hy.shape == (400, 400) and len(z) == 400)

print("=== S9.2 真空波速 = c ===")
dt = 0.95 * DZ / C0
ezv, _, zv = fdtd_1d(nz=NZ, dz=DZ, n_steps=1000, source_idx=300)
right = zv >= 0.3   # 只测右侧行波（源向两侧发射，避免左右对称混淆）
peak_at = lambda fr: zv[right][np.argmax(np.abs(ezv[fr][right]))]
p0, p1 = peak_at(300), peak_at(700)
v = (p1 - p0) / ((700 - 300) * dt)
check(f"脉冲峰值速度 {v:.3e} m/s ≈ c ({v/C0:.3f}×)", abs(v / C0 - 1) < 0.02)

print("=== S9.3 介质界面 · 反射存在 + 相位反转 ===")
eps_r = np.ones(NZ)
eps_r[1200:] = 4.0   # 真空 → ε=4 介质
ezi, _, _ = fdtd_1d(nz=NZ, dz=DZ, n_steps=2600,
                    eps_r_profile=eps_r, source_idx=300)
s = ezi[:, 1000]     # 界面左侧观测点
E_inc = np.sum(s[1050:1450] ** 2)
E_ref = np.sum(s[1750:2150] ** 2)
# 无界面基准（同一窗口的能量应≈0）
ez0, _, _ = fdtd_1d(nz=NZ, dz=DZ, n_steps=2600, source_idx=300)
s0 = ez0[:, 1000]
E0 = np.sum(s0[1750:2150] ** 2)
check(f"反射能量 {E_ref/E_inc:.3f} > 3× 无界面基准 {E0/E_inc:.3f}（确实有反射）",
      E_ref > 3 * E0)
check(f"反射主峰 {s[1750:2150].min():.3f} < 0（ε 增大 → 相位反转）",
      s[1750:2150].min() < 0)

print("=== S9.4 介质中波速 = c/√εr ===")
t1400 = ezi[:, 1400]  # 界面后 200 格
k = t1400.argmax()
t_interface = 650 + 900 / 0.95     # 源中心 650 + 900 格以 0.95 格/步
v_med = 200 * DZ / ((k - t_interface) * dt)
check(f"介质波速 {v_med:.3e} ≈ c/2 ({v_med/(C0/2):.3f}×, 误差<12%)",
      abs(v_med / (C0 / 2) - 1) < 0.12)

print("=== S9.5 CFL 条件（数值爆炸） ===")
ezb, _, _ = fdtd_1d(nz=400, dz=DZ, dt=2 * DZ / C0, n_steps=300)  # CFL=2
exploded = np.isnan(ezb).any() or np.nanmax(np.abs(ezb)) > 10
check("CFL=2 时数值爆炸（NaN 或 |Ez| 巨大）", exploded)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 10 吧！")
