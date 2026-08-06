"""挑战 11 · Quantum — 参考实现（分裂算符法解含时薛定谔方程）。

一维含时薛定谔方程（ħ=1, m=1 自然单位）：
    i·∂ψ/∂t = -(1/2)∂²ψ/∂x² + V(x)·ψ
分裂算符法（二阶对称分裂，O(Δt³)）：
    ψ(t+Δt) ≈ e^{-iVΔt/2} · e^{-iTΔt} · e^{-iVΔt/2} ψ(t)
    - 坐标空间作用 e^{-iVΔt/2}
    - FFT 到动量空间作用 e^{-i(k²/2)Δt}（动能 T = k²/2）
    - IFFT 回坐标空间再作用 e^{-iVΔt/2}
依赖 numpy。被 verify.py import 时无第三方绘图依赖。
"""

import numpy as np


def gaussian_wavepacket(x, x0=0.0, k0=0.0, sigma=1.0):
    """归一化高斯波包：ψ = (2πσ²)^(-1/4) e^{ik0x} e^{-(x-x0)²/(4σ²)}。"""
    psi = (2 * np.pi * sigma**2) ** (-0.25) \
        * np.exp(1j * k0 * x) \
        * np.exp(-(x - x0) ** 2 / (4 * sigma**2))
    return psi


def evolve(psi, V, dx, dt, n_steps):
    """分裂算符法演化 n_steps 步。

    Args:
        psi:  初始波函数 (nx,) 复数组
        V:    势能 (nx,)
        dx:   空间步长
        dt:   时间步长
        n_steps: 步数
    Returns:
        psi_final: 演化后的波函数
    """
    nx = len(psi)
    psi = psi.copy()

    # 动量空间波数（FFT 约定：k = 2π·freq / (nx·dx)）
    k = 2 * np.pi * np.fft.fftfreq(nx, d=dx)
    kin = np.exp(-1j * (k**2 / 2.0) * dt)     # e^{-iTΔt}，T = k²/2 (m=1)
    halfV = np.exp(-1j * V * dt / 2.0)         # e^{-iVΔt/2}

    for _ in range(n_steps):
        psi = psi * halfV                       # 半个势能步
        psi = np.fft.ifft(np.fft.fft(psi) * kin)  # 动能步（动量空间）
        psi = psi * halfV                       # 半个势能步
    return psi


def expectation_energy(psi, V, dx):
    """能量期望 ⟨E⟩ = ∫ψ* H ψ dx（H = -1/2∂²/∂x² + V）。"""
    psi = np.asarray(psi)
    lap = np.zeros_like(psi)
    lap[1:-1] = (psi[2:] - 2 * psi[1:-1] + psi[:-2]) / dx**2
    lap[0] = lap[1]
    lap[-1] = lap[-2]
    Hpsi = -0.5 * lap + V * psi
    return np.real(np.sum(np.conj(psi) * Hpsi) * dx)


def transmission_probability(psi, x, barrier_right):
    """势垒右侧的总概率（透射部分）。"""
    mask = x > barrier_right
    return np.sum(np.abs(psi[mask]) ** 2) * (x[1] - x[0])


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    nx = 1024
    L = 200.0
    x = np.linspace(-L / 2, L / 2, nx)
    dx = x[1] - x[0]
    dt = 0.1

    # 自由波包展宽
    psi0 = gaussian_wavepacket(x, x0=-40.0, k0=0.5, sigma=3.0)
    psi_f = evolve(psi0, np.zeros(nx), dx, dt, 2000)

    plt.plot(x, np.abs(psi0) ** 2, label="t=0")
    plt.plot(x, np.abs(psi_f) ** 2, label="t=200")
    plt.xlabel("x")
    plt.ylabel("|ψ|²")
    plt.legend()
    plt.title("Quantum: free wavepacket spreads")
    plt.show()
