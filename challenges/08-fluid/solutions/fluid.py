"""挑战 08 · Fluid — 参考实现（D2Q9 格子玻尔兹曼 + 顶盖驱动流）。

LBM 核心两步：
    碰撞：f_i ← f_i - (f_i - f_i^eq)/τ
    迁移：f_i(x + c_i·Δt, t+Δt) = f_i(x, t)
宏观量恢复：ρ = Σf_i,  ρu = Σf_i·c_i
稳定条件：τ > 1/2（黏度 ν = (τ-1/2)/3 必须为正）。
依赖 numpy。被 verify.py import 时无第三方绘图依赖。
"""

import numpy as np

# D2Q9 方向与权重
CX = np.array([0, 1, 0, -1, 0, 1, -1, -1, 1])
CY = np.array([0, 0, 1, 0, -1, 1, 1, -1, -1])
W = np.array([4 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 9,
              1 / 36, 1 / 36, 1 / 36, 1 / 36])


def equilibrium(i, rho, ux, uy):
    """方向 i 的平衡分布 f_i^eq。"""
    cu = CX[i] * ux + CY[i] * uy
    return W[i] * rho * (1 + 3 * cu + 4.5 * cu**2 - 1.5 * (ux**2 + uy**2))


def simulate_lid_driven(nx=32, ny=32, tau=0.6, U_wall=0.1,
                        n_steps=5000, rho0=1.0):
    """顶盖驱动流（lid-driven cavity）——最经典的 LBM 基准测试。

    顶盖（上边界）以速度 U_wall 向右移动；其余三壁无滑移（反弹边界）。

    Returns:
        (rho, ux, uy): 最终宏观场，形状均为 (ny, nx)
    """
    f = np.zeros((9, ny, nx))
    rho = np.full((ny, nx), rho0)
    ux = np.zeros((ny, nx))
    uy = np.zeros((ny, nx))

    # 初始化为平衡态（静止流体）
    for i in range(9):
        f[i] = equilibrium(i, rho, ux, uy)

    for _ in range(n_steps):
        # --- 宏观量 ---
        rho = f.sum(axis=0)
        ux = (CX[:, None, None] * f).sum(axis=0) / rho
        uy = (CY[:, None, None] * f).sum(axis=0) / rho

        # --- 碰撞 ---
        for i in range(9):
            f[i] = f[i] - (f[i] - equilibrium(i, rho, ux, uy)) / tau

        # --- 迁移 ---
        for i in range(9):
            f[i] = np.roll(f[i], CX[i], axis=1)
            f[i] = np.roll(f[i], CY[i], axis=0)

        # --- 边界（迁移后 bounce-back） ---
        # 左壁 x=0（静止）
        f[1, :, 0] = f[3, :, 0]
        f[5, :, 0] = f[7, :, 0]
        f[8, :, 0] = f[6, :, 0]
        # 右壁 x=nx-1（静止）
        f[3, :, -1] = f[1, :, -1]
        f[6, :, -1] = f[8, :, -1]
        f[7, :, -1] = f[5, :, -1]
        # 底部 y=0（静止）
        f[2, 0, :] = f[4, 0, :]
        f[5, 0, :] = f[7, 0, :]
        f[6, 0, :] = f[8, 0, :]
        # 顶盖 y=ny-1（向右移动 U_wall，modified bounce-back）
        f[4, -1, :] = f[2, -1, :]
        f[7, -1, :] = f[5, -1, :] - (1.0 / 6.0) * rho[-1, :] * U_wall
        f[8, -1, :] = f[6, -1, :] + (1.0 / 6.0) * rho[-1, :] * U_wall

    return rho, ux, uy


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    rho, ux, uy = simulate_lid_driven(nx=64, ny=64, n_steps=20000)

    # 涡度 ω = ∂uy/∂x - ∂ux/∂y
    wx = np.gradient(uy, axis=1)
    wy = np.gradient(ux, axis=0)
    vort = wx - wy

    plt.figure(figsize=(6, 5))
    plt.imshow(vort, cmap="RdBu_r", origin="lower")
    plt.colorbar(label="vorticity")
    plt.quiver(ux[::4, ::4], uy[::4, ::4], scale=30)
    plt.title("Lid-driven cavity: main vortex + corner vortices")
    plt.tight_layout()
    plt.show()
