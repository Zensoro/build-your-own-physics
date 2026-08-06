"""一维 FDTD（时域有限差分，Yee 网格）：电磁波传播。

任务：补全 TODO 部分，让 fdtd_1d 能正确运行并通过 verify.py 验收。
依赖 numpy。
运行：python verify.py（验收）或 python em.py（画图看现象）
"""

import numpy as np

C0 = 3.0e8  # 真空光速 (m/s)
MU0 = 4.0 * np.pi * 1e-7
EPS0 = 1.0 / (MU0 * C0**2)


def fdtd_1d(nz=400, dz=1e-3, dt=None, n_steps=1000, source="gauss",
            eps_r_profile=None, source_idx=None, f_source=2e9):
    """一维 FDTD 模拟高斯/正弦脉冲传播。

    Yee 网格：Ez 在整数格点、整数时间；Hy 在半格点、半时间。
    更新方程（一维无源）：
        Hy[k]   ← Hy[k]   - (Δt/μ/Δz)·(Ez[k+1] - Ez[k])
        Ez[k+1] ← Ez[k+1] - (Δt/ε/Δz)·(Hy[k+1] - Hy[k])

    Args:
        nz:           格点数
        dz:           空间步长 (m)
        dt:           时间步长 (s)，默认 CFL=0.95
        n_steps:      时间步数
        source:       "gauss" 或 "sine"
        eps_r_profile: 介电常数分布 (nz,)，None = 真空
        source_idx:   源位置（默认 1/4 处）
        f_source:     正弦源频率 (Hz)
    Returns:
        (ez_hist, hy_hist, z)
    """
    if dt is None:
        dt = 0.95 * dz / C0

    eps_r = np.ones(nz) if eps_r_profile is None else np.asarray(eps_r_profile)
    eps = eps_r * EPS0

    ez = np.zeros(nz)
    hy = np.zeros(nz)
    z = np.arange(nz) * dz

    if source_idx is None:
        source_idx = nz // 4
    n_src = source_idx

    mur_coef = (C0 * dt - dz) / (C0 * dt + dz)   # 一阶 Mur 吸收边界系数

    ez_hist = []
    hy_hist = []
    for n in range(n_steps):
        ez_old = ez.copy()

        # TODO 1: 更新 Hy（在 Ez 格点之间取差分）
        # hy[:-1] = hy[:-1] - (dt / MU0 / dz) * (ez[1:] - ez[:-1])
        pass  # ← 替换这一行

        # TODO 2: 更新 Ez（在 Hy 格点之间取差分）
        # ez[1:] = ez[1:] - (dt / eps[1:] / dz) * (hy[1:] - hy[:-1])
        pass  # ← 替换这一行

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


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    ez, hy, z = fdtd_1d(nz=400, n_steps=400)
    plt.plot(z * 1e3, ez[200], label=f"t={200*0.95*1e-3/C0*1e9:.2f} ns")
    plt.plot(z * 1e3, ez[300], label=f"t={300*0.95*1e-3/C0*1e9:.2f} ns")
    plt.xlabel("z (mm)")
    plt.ylabel("Ez (V/m)")
    plt.legend()
    plt.title("FDTD: a Gaussian pulse propagates at c")
    plt.show()
