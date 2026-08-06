"""挑战 04 · N-Body — 参考实现（直接求和 + 蛙跳法）。

单位：G = 1 自然单位。依赖 numpy。
被 verify.py import 时无任何第三方绘图依赖（matplotlib 仅在 __main__ 内导入）。
"""

import numpy as np

G_DEFAULT = 1.0


def accelerations(positions, masses, G=1.0, soft=1e-3):
    """计算所有粒子受到的加速度（直接求和 O(N^2)，含引力软化 soft）。

    Args:
        positions: (N, 2) 各粒子位置
        masses:    (N,)   各粒子质量
        G:         引力常数
        soft:      软化参数，防止两粒子极近时力发散
    Returns:
        (N, 2) 加速度数组
    """
    positions = np.asarray(positions, dtype=float)
    masses = np.asarray(masses, dtype=float)
    N = len(masses)
    acc = np.zeros_like(positions)
    idx = np.arange(N)
    for i in range(N):
        r = positions[idx != i] - positions[i]          # (N-1, 2)
        dist = np.sqrt(np.sum(r**2, axis=1) + soft**2)   # (N-1,)
        acc[i] = G * np.sum(
            masses[idx != i, None] * r / dist[:, None]**3, axis=0)
    return acc


def simulate(positions, velocities, masses, dt, n_steps,
             G=1.0, soft=1e-3):
    """蛙跳法（Velocity Verlet）模拟 N 体系统。

    Args:
        positions: (N, 2) 初始位置
        velocities: (N, 2) 初始速度
        masses:    (N,)   质量
        dt:        时间步长
        n_steps:   步数
        G, soft:   见 accelerations
    Returns:
        (pos_hist, vel_hist): 形状均为 (n_steps + 1, N, 2)
    """
    pos = np.array(positions, dtype=float)
    vel = np.array(velocities, dtype=float)
    masses = np.array(masses, dtype=float)

    pos_hist = [pos.copy()]
    vel_hist = [vel.copy()]
    for _ in range(n_steps):
        a = accelerations(pos, masses, G, soft)
        vel = vel + a * dt / 2.0          # 半步速度
        pos = pos + vel * dt              # 整步位置
        a_new = accelerations(pos, masses, G, soft)
        vel = vel + a_new * dt / 2.0      # 半步速度
        pos_hist.append(pos.copy())
        vel_hist.append(vel.copy())
    return np.array(pos_hist), np.array(vel_hist)


def total_energy(pos_hist, vel_hist, masses, G=1.0, soft=1e-3):
    """计算每一时刻的总机械能 E = KE + PE（应使用辛积分器保持守恒）。"""
    pos_hist = np.asarray(pos_hist, dtype=float)
    vel_hist = np.asarray(vel_hist, dtype=float)
    masses = np.asarray(masses, dtype=float)
    N = len(masses)
    idx = np.arange(N)
    energies = []
    for pos, vel in zip(pos_hist, vel_hist):
        ke = 0.5 * np.sum(masses[:, None] * vel**2)
        pe = 0.0
        for i in range(N):
            r = pos[idx != i] - pos[i]
            dist = np.sqrt(np.sum(r**2, axis=1) + soft**2)
            pe += G * masses[i] * np.sum(masses[idx != i] / dist)
        pe *= 0.5
        energies.append(ke + pe)
    return np.array(energies)


def center_of_mass(pos_hist, masses):
    """计算每一时刻的质心位置，返回 (n_steps + 1, 2)。"""
    pos_hist = np.asarray(pos_hist, dtype=float)
    masses = np.asarray(masses, dtype=float)
    return np.sum(masses[:, None] * pos_hist, axis=1) / np.sum(masses)


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # 对称二体圆轨道演示
    p0 = np.array([[-0.5, 0.0], [0.5, 0.0]])
    v0 = np.array([[0.0, np.sqrt(0.5)], [0.0, -np.sqrt(0.5)]])
    m = np.array([1.0, 1.0])
    pos, vel = simulate(p0, v0, m, 0.001, 4000, soft=0.0)

    plt.plot(pos[:, 0, 0], pos[:, 0, 1], label="body 1")
    plt.plot(pos[:, 1, 0], pos[:, 1, 1], label="body 2")
    plt.gca().set_aspect("equal")
    plt.legend()
    plt.title("N-Body: symmetric 2-body orbit")
    plt.show()
