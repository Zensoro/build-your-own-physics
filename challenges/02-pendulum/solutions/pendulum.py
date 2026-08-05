"""挑战 02 · 单摆 — 参考实现（欧拉法 vs 欧拉-克罗默法）。

放在 solutions 分支。强烈建议先自己写，卡住再看。
运行：python pendulum.py
（被 verify.py import 时无任何第三方依赖）
"""

import math

G = 9.81


def simulate_euler(L, theta0, omega0=0.0, dt=0.01, t_max=20.0):
    """欧拉法（显式）模拟单摆。

    注意：先保存旧 omega，用旧 omega 更新 theta —— 这是显式欧拉的关键。
    如果直接 omega=omega+alpha*dt 后再用 omega 更新 theta，
    就变成欧拉-克罗默法了（能量守恒，无法展示"欧拉法能量漂移"）。
    """
    theta, omega = theta0, omega0
    times, thetas, omegas = [0.0], [theta], [omega]
    t = 0.0
    while t < t_max:
        alpha = -G / L * math.sin(theta)   # 角加速度
        omega_old = omega                  # ★ 保存旧角速度
        omega = omega + alpha * dt         # 更新角速度（新值）
        theta = theta + omega_old * dt     # 用旧角速度更新角度（显式）
        t += dt
        times.append(t)
        thetas.append(theta)
        omegas.append(omega)
    return times, thetas, omegas


def simulate_euler_cromer(L, theta0, omega0=0.0, dt=0.01, t_max=20.0):
    """欧拉-克罗默法（半隐式欧拉）模拟单摆。"""
    theta, omega = theta0, omega0
    times, thetas, omegas = [0.0], [theta], [omega]
    t = 0.0
    while t < t_max:
        alpha = -G / L * math.sin(theta)   # 角加速度
        omega = omega + alpha * dt          # 先更新角速度（新值）
        theta = theta + omega * dt          # 再更新角度（用新 omega！）
        t += dt
        times.append(t)
        thetas.append(theta)
        omegas.append(omega)
    return times, thetas, omegas


def energy(L, thetas, omegas, m=1.0):
    """总机械能 E = 1/2 m L^2 omega^2 + m g L (1 - cos(theta))。"""
    return [0.5 * m * L**2 * w**2 + m * G * L * (1 - math.cos(th))
            for th, w in zip(thetas, omegas)]


if __name__ == "__main__":
    L, theta0 = 1.0, math.radians(30.0)

    t_e, th_e, om_e = simulate_euler(L, theta0)
    t_c, th_c, om_c = simulate_euler_cromer(L, theta0)
    E0 = energy(L, [theta0], [0.0])[0]

    # 数值报告
    print("=== 能量漂移对比 (t=20s) ===")
    print(f"欧拉法:        {(energy(L, th_e, om_e)[-1] - E0) / E0:+.2%}")
    print(f"欧拉-克罗默法: {(energy(L, th_c, om_c)[-1] - E0) / E0:+.2%}")

    # 小角度周期验证
    t5, th5, _ = simulate_euler_cromer(L, math.radians(5.0), dt=0.001, t_max=10.0)
    crossings = sum(1 for i in range(1, len(th5)) if th5[i-1] * th5[i] < 0)
    T_sim = 10.0 / (crossings / 2)
    T_theory = 2 * math.pi * math.sqrt(L / G)
    print(f"\n=== 小角度周期 (theta0=5°) ===")
    print(f"模拟: {T_sim:.3f}s vs 理论: {T_theory:.3f}s, 误差 {abs(T_sim-T_theory)/T_theory:.2%}")

    # 可视化（惰性导入，被 verify.py import 时不加载）
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(13, 4))
    axes[0].plot(th_e, om_e, lw=0.8, label="Euler")
    axes[0].set_title("相空间：欧拉法（外扩螺旋=能量增长）")
    axes[0].set_xlabel("theta (rad)")
    axes[0].set_ylabel("omega (rad/s)")

    axes[1].plot(th_c, om_c, lw=0.8, label="Euler-Cromer", color="tab:green")
    axes[1].set_title("相空间：欧拉-克罗默法（闭合=能量守恒）")
    axes[1].set_xlabel("theta (rad)")
    axes[1].set_ylabel("omega (rad/s)")

    axes[2].plot(t_e, [e / E0 - 1 for e in energy(L, th_e, om_e)], lw=1, label="Euler")
    axes[2].plot(t_c, [e / E0 - 1 for e in energy(L, th_c, om_c)], lw=1,
                 label="Euler-Cromer", color="tab:green")
    axes[2].axhline(0, color="gray", lw=0.5, ls="--")
    axes[2].set_title("能量相对变化 (E-E0)/E0")
    axes[2].set_xlabel("t (s)")
    axes[2].legend()

    plt.tight_layout()
    plt.show()
