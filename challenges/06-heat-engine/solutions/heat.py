"""挑战 06 · Heat Engine — 参考实现（FTCS 热扩散 + 热机效率）。

一维热扩散：∂T/∂t = α·∂²T/∂x²
显式 FTCS：T^{n+1}_i = T^n_i + (α·dt/dx²)(T^n_{i+1} - 2T^n_i + T^n_{i-1})
稳定条件：α·dt/dx² ≤ 1/2
依赖 numpy。被 verify.py import 时无第三方绘图依赖。
"""

import numpy as np


def simulate_diffusion(T0, alpha=1.0, dx=0.01, dt=5e-5, n_steps=20000):
    """FTCS 显式格式模拟一维热扩散（Dirichlet 固定边界：端点不变）。

    Args:
        T0:      初始温度分布 (nx,)（端点值会被视为固定边界）
        alpha:   热扩散系数
        dx, dt:  空间/时间步长
        n_steps: 步数
    Returns:
        (T_hist, x): T_hist 形状 (n_steps + 1, nx)，x 形状 (nx,)
    """
    T = np.asarray(T0, dtype=float).copy()
    nx = len(T)
    r = alpha * dt / dx**2

    hist = [T.copy()]
    for _ in range(n_steps):
        lap = np.zeros_like(T)
        lap[1:-1] = T[2:] - 2 * T[1:-1] + T[:-2]
        T = T + r * lap
        # 固定边界（Dirichlet）：端点保持初值
        T[0] = T0[0]
        T[-1] = T0[-1]
        hist.append(T.copy())

    x = np.arange(nx) * dx
    return np.array(hist), x


def carnot_efficiency(T_hot, T_cold):
    """卡诺效率（热力学第二定律给出的理论上限）。"""
    return 1.0 - T_cold / T_hot


def engine_efficiency(T_hot, T_cold, r=1.5, gamma=1.4):
    """一个真实（非卡诺）热机——矩形循环的效率。

    矩形循环：等压膨胀 → 等容降压 → 等压压缩 → 等容升压。
    最高温度 T_hot、最低温度 T_cold；压缩比 r = V2/V1。
    理想气体，nR = 1。

    Returns:
        实际效率（应严格低于同温度区间下的卡诺效率）
    """
    V1, V2 = 1.0, r
    nR = 1.0
    P1 = nR * T_hot / V2   # 等压膨胀压力（B 点）
    P2 = nR * T_cold / V1  # 等容降压压力（C 点）
    if P1 <= P2:
        raise ValueError("需 T_hot/T_cold > r 才能构成正向循环")

    w_net = (V2 - V1) * (P1 - P2)          # 循环净功 = P-V 图围成面积
    # 吸热：等压膨胀段（C_p = γR/(γ-1)）+ 等容升压段（C_v = R/(γ-1)）
    q_in = (gamma / (gamma - 1)) * P1 * (V2 - V1) \
         + (1.0 / (gamma - 1)) * V1 * (P1 - P2)
    return w_net / q_in


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    nx = 100
    x = np.linspace(0, 1, nx)
    T0 = np.where(x < 0.5, 1.0, 0.0)   # 左热右冷的阶梯
    hist, x = simulate_diffusion(T0, alpha=1.0, dx=x[1] - x[0],
                                 dt=5e-5, n_steps=20000)

    plt.imshow(hist[::200].T, aspect="auto", cmap="hot",
               extent=[0, 20000 * 5e-5, 0, 1])
    plt.colorbar(label="T")
    plt.xlabel("t")
    plt.ylabel("x")
    plt.title("Heat diffusion: step profile relaxes to linear")

    print(f"卡诺效率 (600K, 300K) = {carnot_efficiency(600, 300):.3%}")
    print(f"矩形循环实际效率     = {engine_efficiency(600, 300):.3%}")
    plt.show()
