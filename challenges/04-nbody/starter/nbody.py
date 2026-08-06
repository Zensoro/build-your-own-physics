"""N 体引力模拟：直接求和 + 蛙跳法。

任务：补全 TODO 部分，让 simulate 能正确运行并通过 verify.py 验收。
单位：G = 1 自然单位。依赖 numpy。
运行：python verify.py（验收）或 python nbody.py（画图看现象）
"""

import numpy as np

G_DEFAULT = 1.0


def accelerations(positions, masses, G=1.0, soft=1e-3):
    """计算所有粒子受到的加速度（直接求和）。

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
        # TODO: 计算粒子 i 受到其他所有粒子的引力加速度
        # 提示：
        #   r = 其他粒子位置 - positions[i]            # (N-1, 2)
        #   dist = sqrt(r 的平方和 + soft**2)            # (N-1,)
        #   加速度 = G * sum( masses[其他] * r / dist**3, axis=0 )
        #   牛顿万有引力：a_i = G * Σ_j m_j (r_j - r_i) / |r_j - r_i|^3
        pass
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
    Returns:
        (pos_hist, vel_hist): 形状均为 (n_steps + 1, N, 2)
    """
    pos = np.array(positions, dtype=float)
    vel = np.array(velocities, dtype=float)
    masses = np.array(masses, dtype=float)

    pos_hist = [pos.copy()]
    vel_hist = [vel.copy()]
    for _ in range(n_steps):
        # TODO: 蛙跳法（Velocity Verlet）三步
        # 1. 半步推进速度：vel = vel + a * dt/2
        # 2. 整步推进位置：pos = pos + vel * dt
        # 3. 用新位置重算加速度，再半步推进速度：
        #    a_new = accelerations(pos, masses, G, soft)
        #    vel = vel + a_new * dt/2
        a = accelerations(pos, masses, G, soft)
        pass  # ← 用上面的三步替换这一行

        pos_hist.append(pos.copy())
        vel_hist.append(vel.copy())
    return np.array(pos_hist), np.array(vel_hist)


def total_energy(pos_hist, vel_hist, masses, G=1.0, soft=1e-3):
    """计算每一时刻的总机械能 E = KE + PE。"""
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
