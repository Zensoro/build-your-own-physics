"""单摆模拟：欧拉法 vs 欧拉-克罗默法。

任务：补全 TODO 部分，让两个函数都能运行并通过 verify.py 验收。
运行：python verify.py（验收）或 python pendulum.py（画图看现象）
"""

import math

G = 9.81  # m/s^2


def simulate_euler(L, theta0, omega0=0.0, dt=0.01, t_max=20.0):
    """欧拉法模拟单摆。

    Args:
        L: 摆长 (m)
        theta0: 初始摆角 (rad)
        omega0: 初始角速度 (rad/s)
        dt: 时间步长 (s)
        t_max: 模拟总时长 (s)

    Returns:
        (times, thetas, omegas): 时间、摆角、角速度三个列表
    """
    theta, omega = theta0, omega0
    times, thetas, omegas = [0.0], [theta], [omega]
    t = 0.0

    while t < t_max:
        # TODO 1: 欧拉法更新
        # 提示：
        #   角加速度 alpha = -G / L * math.sin(theta)   （重力造成的）
        #   先更新角速度：omega = omega + alpha * dt
        #   再更新角度：  theta = theta + omega * dt
        #   注意：欧拉法更新角度时，必须用**旧的** omega！
        #   （先保存 omega_old = omega，再更新 omega，再用 omega_old 更新 theta）
        #   如果用新 omega，就变成欧拉-克罗默法了——两个函数就没区别了。

        t += dt
        times.append(t)
        thetas.append(theta)
        omegas.append(omega)

    return times, thetas, omegas


def simulate_euler_cromer(L, theta0, omega0=0.0, dt=0.01, t_max=20.0):
    """欧拉-克罗默法（半隐式欧拉）模拟单摆。

    和欧拉法唯一的区别：更新角度时用**新的**角速度。
    """
    theta, omega = theta0, omega0
    times, thetas, omegas = [0.0], [theta], [omega]
    t = 0.0

    while t < t_max:
        # TODO 2: 欧拉-克罗默法更新
        # 提示：
        #   角加速度 alpha = -G / L * math.sin(theta)
        #   先更新角速度：omega = omega + alpha * dt
        #   再更新角度：  theta = theta + omega * dt   ← 用更新后的 omega！
        #   注意：变量 omega 先赋新值，再用它更新 theta，顺序很重要。

        t += dt
        times.append(t)
        thetas.append(theta)
        omegas.append(omega)

    return times, thetas, omegas


def energy(L, thetas, omegas, m=1.0):
    """计算每个时刻的总机械能 E = 1/2 m L^2 omega^2 + m g L (1 - cos(theta))。

    返回能量列表。无摩擦系统中能量应该守恒——数值方法则会破坏它。
    """
    return [0.5 * m * L**2 * w**2 + m * G * L * (1 - math.cos(th))
            for th, w in zip(thetas, omegas)]


if __name__ == "__main__":
    # 手动测试：画相空间对比
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("未安装 matplotlib，跳过画图。")
        raise SystemExit

    L, theta0 = 1.0, math.radians(30.0)
    t_e, th_e, om_e = simulate_euler(L, theta0)
    t_c, th_c, om_c = simulate_euler_cromer(L, theta0)

    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.plot(th_e, om_e, label="Euler")
    plt.title("相空间：欧拉法（能量漂移→外扩螺旋）")
    plt.xlabel("theta (rad)")
    plt.ylabel("omega (rad/s)")

    plt.subplot(1, 3, 2)
    plt.plot(th_c, om_c, label="Euler-Cromer")
    plt.title("相空间：欧拉-克罗默法（闭合→能量守恒）")
    plt.xlabel("theta (rad)")
    plt.ylabel("omega (rad/s)")

    plt.subplot(1, 3, 3)
    E0 = energy(L, [theta0], [0.0])[0]
    plt.plot(t_e, [e / E0 - 1 for e in energy(L, th_e, om_e)], label="Euler")
    plt.plot(t_c, [e / E0 - 1 for e in energy(L, th_c, om_c)], label="Euler-Cromer")
    plt.title("能量相对变化 (E-E0)/E0")
    plt.xlabel("t (s)")
    plt.ylabel("(E-E0)/E0")
    plt.legend()

    plt.tight_layout()
    plt.show()
