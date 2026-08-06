"""挑战 11 自动验收。运行：python verify.py"""

import sys
import numpy as np

sys.path.insert(0, ".")
from quantum import gaussian_wavepacket, evolve, expectation_energy
from quantum import transmission_probability

passed, failed = [], []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


NX, L = 1024, 200.0
x = np.linspace(-L / 2, L / 2, NX)
dx = x[1] - x[0]
dt = 0.1


def sigma_of(psi):
    """波包宽度 σ（中心化标准差）。"""
    p = np.abs(psi) ** 2 * dx
    n = p.sum()
    mx = (x * p).sum() / n
    return np.sqrt(((x - mx) ** 2 * p).sum() / n)


psi0 = gaussian_wavepacket(x, x0=-40.0, k0=0.5, sigma=3.0)

print("=== S11.1 接口 ===")
psif = evolve(psi0, np.zeros(NX), dx, dt, 1000)
check("evolve 返回形状正确的复数组",
      psif.shape == psi0.shape and np.iscomplexobj(psif))

print("=== S11.2 概率守恒 ===")
n0 = np.sum(np.abs(psi0) ** 2) * dx
n1 = np.sum(np.abs(psif) ** 2) * dx
check(f"∫|ψ|²dx 从 {n0:.6f} → {n1:.6f}（偏差 {abs(n1-n0):.2e} < 1e-9）",
      abs(n1 - n0) < 1e-9)

print("=== S11.3 能量守恒 ===")
E0 = expectation_energy(psi0, np.zeros(NX), dx)
E1 = expectation_energy(psif, np.zeros(NX), dx)
rel = abs(E1 - E0) / abs(E0)
check(f"⟨E⟩ 相对变化 {rel:.2e} < 1e-3", rel < 1e-3)

print("=== S11.4 自由波包展宽 ===")
psif2 = evolve(psi0, np.zeros(NX), dx, dt, 2000)
s0, sf = sigma_of(psi0), sigma_of(psif2)
check(f"σ: {s0:.2f} → {sf:.2f}（展宽 {sf/s0:.1f}× > 1.2，不确定性增长）",
      sf > 1.2 * s0)

print("=== S11.5 势垒隧穿 ===")
V = np.zeros(NX)
V[(x > 10) & (x < 20)] = 1.0   # 方势垒 V0=1，波包能量 E≈k0²/2=0.125 < V0
psi_tf = evolve(psi0, V, dx, dt, 2000)   # 2000 步：波包到达势垒区且未卷绕
P = transmission_probability(psi_tf, x, 20)
P0 = transmission_probability(evolve(psi0, np.zeros(NX), dx, dt, 2000),
                              x, 20)
check(f"势垒后透射概率 {P:.3f} > 0.01（经典应为 0，量子隧穿发生）", P > 0.01)
check(f"有势垒透射 {P:.3f} < 无势垒 {P0:.3f}（势垒确实阻挡）", P < P0)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 12 吧！")
