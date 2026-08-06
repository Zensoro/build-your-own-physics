"""双摆模拟：RK4 龙格-库塔法。

任务：补全 TODO 部分，让 simulate 能正确运行并通过 verify.py 验收。
依赖 numpy。运动方程已在 derivs 里给出，你只需实现积分器。
运行：python verify.py（验收）或 python double_pendulum.py（画图看现象）
"""

import numpy as np


def derivs(state, m1=1.0, m2=1.0, L1=1.0, L2=1.0, g=9.81):
    """返回 [ω1', ω2', α1, α2]（一阶 ODE 右端，已由拉格朗日力学推出）。"""
    th1, th2, w1, w2 = state
    d = th1 - th2
    denom = 2 * m1 + m2 - m2 * np.cos(2 * d)
    a1 = (-g * (2 * m1 + m2) * np.sin(th1)
          - m2 * g * np.sin(th1 - 2 * th2)
          - 2 * np.sin(d) * m2 * (w2**2 * L2 + w1**2 * L1 * np.cos(d))) \
         / (L1 * denom)
    a2 = (2 * np.sin(d)
          * (w1**2 * L1 * (m1 + m2) + g * (m1 + m2) * np.cos(th1)
             + w2**2 * L2 * m2 * np.cos(d))) / (L2 * denom)
    return np.array([w1, w2, a1, a2])


def rk4_step(f, y, t, dt):
    """经典四阶龙格-库塔单步。

    Args:
        f: 右端函数 f(y, t) -> dy/dt
        y: 当前状态（向量）
        t: 当前时刻
        dt: 步长
    Returns:
        y 在 t+dt 处的新值
    """
    # TODO: 实现 RK4 四步
    # k1 = f(y, t)
    # k2 = f(y + dt/2·k1, t + dt/2)
    # k3 = f(y + dt/2·k2, t + dt/2)
    # k4 = f(y + dt·k3, t + dt)
    # 返回 y + dt/6·(k1 + 2k2 + 2k3 + k4)
    pass  # ← 替换这一行


def simulate(theta1_0, theta2_0, omega1_0=0.0, omega2_0=0.0,
             dt=0.005, t_max=20.0, m1=1.0, m2=1.0, L1=1.0, L2=1.0,
             g=9.81):
    """RK4 模拟双摆。返回 (times, states)，states 形状 (n, 4)。"""
    y = np.array([theta1_0, theta2_0, omega1_0, omega2_0])
    f = lambda yy, tt: derivs(yy, m1, m2, L1, L2, g)

    n = int(t_max / dt) + 1
    times = np.linspace(0.0, t_max, n)
    states = np.empty((n, 4))
    states[0] = y
    for i in range(1, n):
        y = rk4_step(f, y, times[i - 1], dt)
        states[i] = y
    return times, states


def simulate_euler(theta1_0, theta2_0, omega1_0=0.0, omega2_0=0.0,
                   dt=0.005, t_max=20.0, m1=1.0, m2=1.0, L1=1.0, L2=1.0,
                   g=9.81):
    """显式欧拉法（对比用：能量会明显漂移）。"""
    y = np.array([theta1_0, theta2_0, omega1_0, omega2_0])
    f = lambda yy, tt: derivs(yy, m1, m2, L1, L2, g)

    n = int(t_max / dt) + 1
    times = np.linspace(0.0, t_max, n)
    states = np.empty((n, 4))
    states[0] = y
    for i in range(1, n):
        y = y + dt * f(y, times[i - 1])
        states[i] = y
    return times, states


def energy(states, m1=1.0, m2=1.0, L1=1.0, L2=1.0, g=9.81):
    """总机械能（势能零点取两摆最低点）。"""
    th1 = states[:, 0]
    th2 = states[:, 1]
    w1 = states[:, 2]
    w2 = states[:, 3]
    ke = (0.5 * m1 * L1**2 * w1**2
          + 0.5 * m2 * (L1**2 * w1**2 + L2**2 * w2**2
                        + 2 * L1 * L2 * w1 * w2 * np.cos(th1 - th2)))
    pe = ((m1 + m2) * g * L1 * (1 - np.cos(th1))
          + m2 * g * L2 * (1 - np.cos(th2)))
    return ke + pe


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    t, s = simulate(np.radians(120), np.radians(90), dt=0.005, t_max=30)
    x2 = np.sin(s[:, 0]) + np.sin(s[:, 1])
    y2 = -np.cos(s[:, 0]) - np.cos(s[:, 1])

    plt.plot(x2, y2, lw=0.5, color="tab:blue")
    plt.gca().set_aspect("equal")
    plt.title("Double pendulum: chaotic end-point trajectory")
    plt.xlabel("x2")
    plt.ylabel("y2")
    plt.show()
