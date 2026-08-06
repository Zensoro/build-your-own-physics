"""太阳系模拟（毕业项目）：太阳 + 八大行星 N 体。

任务：补全 TODO 部分，让 simulate_solar 能正确运行并通过 verify.py 验收。
AU-年单位制（GM_☉ = 4π²，地球轨道周期恰为 1 年）。
依赖 numpy。挑战 03（蛙跳）+ 挑战 04（N 体）的集大成。
运行：python verify.py（验收）或 python solar.py（画图看现象）
"""

import numpy as np

MU_SUN = 4.0 * np.pi**2   # GM_☉，AU³/yr²

# 行星: (名称, 半长轴 a/AU, 质量 m/M_☉, 初始角度/rad)
PLANETS = [
    ("Mercury", 0.3871, 1.660e-7, 0.0),
    ("Venus",   0.7233, 2.447e-6, 1.0),
    ("Earth",   1.0000, 3.003e-6, 2.0),
    ("Mars",    1.5237, 3.227e-7, 3.0),
    ("Jupiter", 5.2026, 9.547e-4, 4.0),
    ("Saturn",  9.5549, 2.858e-4, 5.0),
    ("Uranus",  19.218, 4.366e-5, 6.0),
    ("Neptune", 30.110, 5.151e-5, 7.0),
]


def initial_state():
    """返回 (positions, velocities, masses)。

    - positions: (9, 2)，第 0 行是太阳（原点静止）
    - velocities: (9, 2)
    - masses: (9,)，第 0 个是太阳（质量 1）
    """
    pos = np.zeros((len(PLANETS) + 1, 2))
    vel = np.zeros((len(PLANETS) + 1, 2))
    masses = np.ones(len(PLANETS) + 1)
    for i, (name, a, m, phi) in enumerate(PLANETS, start=1):
        # TODO: 圆轨道初始条件
        # v_c = 2*pi/sqrt(a)（AU/yr，让轨道近似圆）
        # pos[i] = (a*cos(phi), a*sin(phi))
        # vel[i] = (-v_c*sin(phi), v_c*cos(phi))
        pass  # ← 替换这一行
        masses[i] = m
    return pos, vel, masses


def accelerations(positions, masses, soft=1e-6):
    """所有粒子的引力加速度（直接求和 O(N²)）。G = MU_SUN。"""
    positions = np.asarray(positions, dtype=float)
    masses = np.asarray(masses, dtype=float)
    N = len(masses)
    acc = np.zeros_like(positions)
    idx = np.arange(N)
    for i in range(N):
        # TODO: 粒子 i 的引力加速度（复用挑战 04 的思路）
        # r = 其他粒子位置 - positions[i]
        # dist = sqrt(r 平方和 + soft**2)
        # acc[i] = MU_SUN * sum(masses[其他]*r/dist**3, axis=0)
        pass  # ← 替换这一行
    return acc


def simulate_solar(dt=0.001, years=10.0, soft=1e-6):
    """蛙跳法（Velocity Verlet）模拟太阳 + 八大行星。

    Returns:
        (pos_hist, vel_hist, masses):
            pos_hist 形状 (n_steps+1, 9, 2)；vel_hist 同
    """
    pos, vel, masses = initial_state()
    n_steps = int(years / dt)

    pos_hist = [pos.copy()]
    vel_hist = [vel.copy()]
    for _ in range(n_steps):
        # TODO: 蛙跳三步（挑战 03/04 的老朋友）
        # 1. a = accelerations(pos, masses, soft); vel += a*dt/2
        # 2. pos += vel*dt
        # 3. a_new = accelerations(pos, masses, soft); vel += a_new*dt/2
        pass  # ← 替换这一行

        pos_hist.append(pos.copy())
        vel_hist.append(vel.copy())
    return np.array(pos_hist), np.array(vel_hist), masses


def total_energy(pos_hist, vel_hist, masses, soft=1e-6):
    """每时刻总机械能 E = KE + PE（G = MU_SUN）。"""
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
            pe += MU_SUN * masses[i] * np.sum(masses[idx != i] / dist)
        pe *= 0.5
        energies.append(ke + pe)
    return np.array(energies)


def orbital_period(xs, ys, dt):
    """从位置序列测量公转周期：极角累计到 2π 的时刻（线性插值）。"""
    theta = np.arctan2(ys, xs)
    dtheta = np.diff(theta)
    dtheta[dtheta > np.pi] -= 2 * np.pi
    dtheta[dtheta < -np.pi] += 2 * np.pi
    cum = np.cumsum(dtheta)
    hit = np.where(cum >= 2 * np.pi)[0]
    if len(hit) == 0:
        return None
    k = hit[0]
    f = (2 * np.pi - cum[k - 1]) / (cum[k] - cum[k - 1])
    return (k + f) * dt


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    pos, vel, masses = simulate_solar(dt=0.002, years=10.0)
    plt.figure(figsize=(7, 7))
    for i in range(1, 9):
        plt.plot(pos[:, i, 0], pos[:, i, 1], lw=0.8,
                 label=PLANETS[i - 1][0])
    plt.scatter([0], [0], color="orange", s=120, label="Sun")
    plt.axis("equal")
    plt.legend(loc="upper right", fontsize=8)
    plt.title("Solar System: 8 planets, leapfrog, 10 years")
    plt.tight_layout()
    plt.show()
