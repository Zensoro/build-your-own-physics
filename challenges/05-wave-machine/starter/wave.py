"""一维波动方程模拟：FTCS / 蛙跳格式。

任务：补全 TODO 部分，让 simulate 能正确运行并通过 verify.py 验收。
依赖 numpy。
运行：python verify.py（验收）或 python wave.py（画图看现象）
"""

import numpy as np


def simulate(u0, c=1.0, dx=0.01, dt=0.005, n_steps=2000, bc="fixed"):
    """模拟一维波动方程 ∂²u/∂t² = c²·∂²u/∂x²。

    Args:
        u0:      初始位移 (nx,)（初始速度设为零）
        c:       波速
        dx, dt:  空间/时间步长
        n_steps: 步数
        bc:      "fixed"（固定端，u=0）或 "free"（自由端，∂u/∂x=0）
    Returns:
        (u_hist, x):
            u_hist 形状 (n_steps + 1, nx)，第 0 帧为 u0
            x       形状 (nx,)
    """
    u0 = np.asarray(u0, dtype=float)
    nx = len(u0)
    C2 = (c * dt / dx) ** 2

    # 初始速度为零 → 由泰勒展开 u¹ = u⁰ + 0.5·C²·∇²u⁰
    lap0 = np.zeros_like(u0)
    lap0[1:-1] = u0[2:] - 2 * u0[1:-1] + u0[:-2]
    u_prev = u0.copy()
    u_cur = u0 + 0.5 * C2 * lap0

    hist = [u_prev.copy(), u_cur.copy()]

    for _ in range(n_steps - 1):
        # TODO: 蛙跳格式更新 u_next
        # 提示：
        #   C2 = (c*dt/dx)**2 （已在上面算好）
        #   1. 内部点更新：
        #      u_next[1:-1] = 2*u_cur[1:-1] - u_prev[1:-1]
        #                    + C2*(u_cur[2:] - 2*u_cur[1:-1] + u_cur[:-2])
        #   2. 边界条件：
        #      bc="fixed": u_next[0] = u_next[-1] = 0
        #      bc="free" : u_next[0] = u_next[1]; u_next[-1] = u_next[-2]
        u_next = np.zeros_like(u_cur)
        pass  # ← 用上面的更新公式替换这一行

        u_prev, u_cur = u_cur, u_next
        hist.append(u_cur.copy())

    x = np.arange(nx) * dx
    return np.array(hist), x


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    nx = 400
    x = np.linspace(0, 4, nx)
    u0 = np.exp(-((x - 2.0) / 0.15) ** 2)   # 中心高斯波包
    hist, x = simulate(u0, c=1.0, dx=x[1] - x[0], dt=0.005, n_steps=600)

    plt.imshow(hist.T, aspect="auto", cmap="RdBu_r",
               vmin=-1, vmax=1, extent=[0, 600 * 0.005, 0, 4])
    plt.colorbar(label="u")
    plt.xlabel("t")
    plt.ylabel("x")
    plt.title("Wave: a Gaussian packet splits and propagates")
    plt.show()
