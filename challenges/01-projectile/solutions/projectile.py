"""挑战 01 · 抛体运动 — 参考实现（欧拉法）。

放在 solutions 分支。强烈建议先自己写，卡住再看。
运行：python projectile.py
（被 verify.py import 时无任何第三方依赖）
"""

import math

G = 9.81  # m/s^2


def simulate(v0, theta_deg, dt=0.01, t_max=10.0):
    """欧拉法模拟抛体运动（无空气阻力）。"""
    theta = math.radians(theta_deg)
    vx = v0 * math.cos(theta)
    vy = v0 * math.sin(theta)
    x, y = 0.0, 0.0

    times, xs, ys = [0.0], [x], [y]
    t = 0.0
    while t < t_max and y >= 0:
        vy -= G * dt          # 重力只影响竖直速度
        x += vx * dt          # 水平匀速
        y += vy * dt          # 位置跟着速度走
        t += dt
        times.append(t)
        xs.append(x)
        ys.append(y)

    return times, xs, ys


def verify(v0=50.0, theta_deg=45.0, dt=0.001):
    """验证：模拟结果 vs 理论值。"""
    times, xs, ys = simulate(v0, theta_deg, dt=dt)

    R_theory = v0**2 * math.sin(2 * math.radians(theta_deg)) / G
    R_sim = xs[-1]
    print(f"射程: 模拟 {R_sim:.1f} m vs 理论 {R_theory:.1f} m, "
          f"误差 {abs(R_sim - R_theory) / R_theory * 100:.2f}%")

    H_theory = (v0 * math.sin(math.radians(theta_deg)))**2 / (2 * G)
    H_sim = max(ys)
    print(f"最高点: 模拟 {H_sim:.1f} m vs 理论 {H_theory:.1f} m, "
          f"误差 {abs(H_sim - H_theory) / H_theory * 100:.2f}%")


if __name__ == "__main__":
    verify()
    import matplotlib.pyplot as plt
    times, xs, ys = simulate(50.0, 45.0)
    plt.plot(xs, ys)
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Projectile Motion (Euler, v0=50, 45°)")
    plt.axis("equal")
    plt.show()
