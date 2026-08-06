"""挑战 07 · Double Pendulum — 参考实现（RK4 + 李雅普诺夫）。

双摆运动方程（拉格朗日力学，m1, m2, L1, L2 通用）：
    θ1'' = [-g(2m1+m2)sinθ1 - m2·g·sin(θ1-θ2)
            - 2sin(θ1-θ2)·m2·(ω2²L2 + ω1²L1·cos(θ1-θ2))] / [L1(2m1+m2-m2·cos(2θ1-2θ2))]
    θ2'' = [2sin(θ1-θ2)·(ω1²L1(m1+m2) + g(m1+m2)cosθ1 + ω2²L2·m2·cos(θ1-θ2))]
            / [L2(2m1+m2-m2·cos(2θ1-2θ2))]
依赖 numpy。被 verify.py import 时无第三方绘图依赖。
"""

import numpy as np


def derivs(state, m1=1.0, m2=1.0, L1=1.0, L2=1.0, g=9.81):
    """返回 [ω1', ω2', α1, α2]（一阶 ODE 右端）。"""
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
    """经典四阶龙格-库塔单步。"""
    k1 = f(y, t)
    k2 = f(y + 0.5 * dt * k1, t + 0.5 * dt)
    k3 = f(y + 0.5 * dt * k2, t + 0.5 * dt)
    k4 = f(y + dt * k3, t + dt)
    return y + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)


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

    # 大角度 → 混沌
    t, s = simulate(np.radians(120), np.radians(90), dt=0.005, t_max=30)
    x1 = np.sin(s[:, 0])
    y1 = -np.cos(s[:, 0])
    x2 = x1 + np.sin(s[:, 1])
    y2 = y1 - np.cos(s[:, 1])

    plt.plot(x2, y2, lw=0.5, color="tab:blue")
    plt.gca().set_aspect("equal")
    plt.title("Double pendulum: chaotic end-point trajectory")
    plt.xlabel("x2")
    plt.ylabel("y2")
    plt.show()
