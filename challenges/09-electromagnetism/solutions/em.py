"""挑战 09 · Electromagnetism — 参考实现（一维 FDTD / Yee 网格）。

一维无源麦克斯韦方程（Ez, Hy 偏振）：
    ∂Ez/∂t = -(1/ε) ∂Hy/∂z
    ∂Hy/∂t = -(1/μ) ∂Ez/∂z
Yee 网格：Ez 在整数格点、整数时间；Hy 在半格点、半时间。
稳定条件（CFL）：c·Δt/Δz ≤ 1，其中 c = 1/√(εμ)。
依赖 numpy。被 verify.py import 时无第三方绘图依赖。
"""

import numpy as np

C0 = 3.0e8  # 真空光速 (m/s)
MU0 = 4.0 * np.pi * 1e-7
EPS0 = 1.0 / (MU0 * C0**2)


def fdtd_1d(nz=400, dz=1e-3, dt=None, n_steps=1000, source="gauss",
            eps_r_profile=None, source_idx=None, f_source=2e9):
    """一维 FDTD 模拟高斯/正弦脉冲传播。

    Args:
        nz:           格点数
        dz:           空间步长 (m)
        dt:           时间步长 (s)，默认取 CFL=0.95 的最优值
        n_steps:      时间步数
        source:       "gauss"（高斯脉冲）或 "sine"（连续正弦波）
        eps_r_profile: 介电常数分布 (nz,)，None = 真空
        source_idx:   源位置（默认 1/4 处）
        f_source:     正弦源频率 (Hz)
    Returns:
        (ez_hist, hy_hist, z):
            ez_hist 形状 (n_steps, nz)；hy_hist 形状 (n_steps, nz)（Hy 定义在半格点，
            为方便存储取同样长度，Hy[k] 对应 z = (k+0.5)·dz）
    """
    if dt is None:
        dt = 0.95 * dz / C0   # CFL = c·dt/dz = 0.95

    eps_r = np.ones(nz) if eps_r_profile is None else np.asarray(eps_r_profile)
    eps = eps_r * EPS0

    ez = np.zeros(nz)
    hy = np.zeros(nz)
    z = np.arange(nz) * dz

    if source_idx is None:
        source_idx = nz // 4
    n_src = source_idx

    # 一阶 Mur 吸收边界系数（吸收出射波，抑制边界反射）
    mur_coef = (C0 * dt - dz) / (C0 * dt + dz)

    ez_hist = []
    hy_hist = []
    for n in range(n_steps):
        ez_old = ez.copy()
        # Hy 更新（Ez 差分在半格点）
        hy[:-1] = hy[:-1] - (dt / MU0 / dz) * (ez[1:] - ez[:-1])
        # Ez 更新（Hy 差分在半格点）
        ez[1:] = ez[1:] - (dt / eps[1:] / dz) * (hy[1:] - hy[:-1])
        # 一阶 Mur 吸收边界（左右两端）
        ez[0] = ez_old[1] + mur_coef * (ez[1] - ez_old[0])
        ez[-1] = ez_old[-2] + mur_coef * (ez[-2] - ez_old[-1])
        # 源注入
        if source == "sine":
            ez[n_src] += dt * np.sin(2 * np.pi * f_source * n * dt)
        else:  # gauss
            ez[n_src] += np.exp(-0.5 * ((n - n_steps / 4) / (n_steps / 12)) ** 2) * 0.5

        ez_hist.append(ez.copy())
        hy_hist.append(hy.copy())

    return np.array(ez_hist), np.array(hy_hist), z


def reflectance(eps_r1, eps_r2):
    """两种介质界面上的功率反射系数 R = ((Z1-Z2)/(Z1+Z2))²。"""
    Z1 = np.sqrt(MU0 / (eps_r1 * EPS0))
    Z2 = np.sqrt(MU0 / (eps_r2 * EPS0))
    return ((Z1 - Z2) / (Z1 + Z2)) ** 2


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    ez, hy, z = fdtd_1d(nz=400, n_steps=400)
    dz = z[1] - z[0]
    dt = 0.95 * dz / C0
    plt.plot(z * 1e3, ez[200], label=f"t={200*dt*1e9:.2f} ns")
    plt.plot(z * 1e3, ez[300], label=f"t={300*dt*1e9:.2f} ns")
    plt.xlabel("z (mm)")
    plt.ylabel("Ez (V/m)")
    plt.legend()
    plt.title("FDTD: a Gaussian pulse propagates at c")
    plt.show()
