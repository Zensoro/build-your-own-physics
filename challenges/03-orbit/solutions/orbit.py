"""挑战 03 · 轨道 — 参考实现（蛙跳法 / Velocity Verlet）。

放在 solutions 分支。强烈建议先自己写，卡住再看。
运行：python orbit.py
（被 verify.py import 时无任何第三方依赖）
"""

import math

MU = 4.0 * math.pi * math.pi  # AU^3/yr^2


def simulate(mu, x0, y0, vx0, vy0, dt, n_steps):
    """蛙跳法（Velocity Verlet）模拟二体轨道（太阳固定原点）。"""
    x, y = x0, y0
    vx, vy = vx0, vy0
    xs, ys = [x], [y]

    for _ in range(n_steps):
        r = math.hypot(x, y)
        ax = -mu * x / r**3
        ay = -mu * y / r**3

        # 1. 半步推进速度
        vx += ax * dt / 2
        vy += ay * dt / 2

        # 2. 整步推进位置
        x += vx * dt
        y += vy * dt

        # 3. 用新位置重算加速度，再半步推进速度
        r_new = math.hypot(x, y)
        ax_new = -mu * x / r_new**3
        ay_new = -mu * y / r_new**3
        vx += ax_new * dt / 2
        vy += ay_new * dt / 2

        xs.append(x)
        ys.append(y)

    return xs, ys


def energy_series(xs, ys, mu, dt):
    """从位置序列用中心差分估计速度，计算每个时刻的能量 E = 1/2 v^2 - mu/r。"""
    es = []
    for i in range(len(xs)):
        if i == 0:
            vx = (xs[1] - xs[0]) / dt
            vy = (ys[1] - ys[0]) / dt
        elif i == len(xs) - 1:
            vx = (xs[-1] - xs[-2]) / dt
            vy = (ys[-1] - ys[-2]) / dt
        else:
            vx = (xs[i + 1] - xs[i - 1]) / (2 * dt)
            vy = (ys[i + 1] - ys[i - 1]) / (2 * dt)
        es.append(0.5 * (vx**2 + vy**2) - mu / math.hypot(xs[i], ys[i]))
    return es


if __name__ == "__main__":
    DT, N = 0.001, 1000  # 一年

    print("=== 圆轨道（地球） ===")
    xs, ys = simulate(MU, 1.0, 0.0, 0.0, 2 * math.pi, DT, N)
    rs = [math.hypot(x, y) for x, y in zip(xs, ys)]
    print(f"半径范围: {min(rs):.4f} ~ {max(rs):.4f} AU")
    print(f"闭合误差: {math.hypot(xs[-1]-1, ys[-1]):.4f} AU")

    es = energy_series(xs, ys, MU, DT)
    print(f"能量漂移: {(es[-1]-es[0])/abs(es[0]):.4%}")

    print("=== 椭圆轨道（0.8 v_c） ===")
    xs_e, ys_e = simulate(MU, 1.0, 0.0, 0.0, 0.8 * 2 * math.pi, DT, N)
    r_e = [math.hypot(x, y) for x, y in zip(xs_e, ys_e)]
    print(f"近日点 {min(r_e):.4f} AU, 远日点 {max(r_e):.4f} AU")
    es_e = energy_series(xs_e, ys_e, MU, DT)
    print(f"能量漂移: {(es_e[-1]-es_e[0])/abs(es_e[0]):.4%}")

    print("=== 逃逸速度 ===")
    for factor, name in [(math.sqrt(2), "sqrt(2)*v_c"), (1.5, "1.5*v_c")]:
        xs_p, ys_p = simulate(MU, 1.0, 0.0, 0.0, factor * 2 * math.pi, DT, N)
        print(f"{name}: 一年后 r = {math.hypot(xs_p[-1], ys_p[-1]):.2f} AU")

    # 可视化（惰性导入，被 verify.py import 时不加载）
    import matplotlib.pyplot as plt
    plt.figure(figsize=(6, 6))
    plt.plot(xs, ys, lw=1.2, label="circular (v = v_c)")
    plt.plot(xs_e, ys_e, lw=1.2, label="elliptical (v = 0.8 v_c)")
    plt.scatter([0], [0], color="orange", s=80, label="Sun")
    plt.axis("equal")
    plt.xlabel("x (AU)")
    plt.ylabel("y (AU)")
    plt.legend()
    plt.title("Orbit: Leapfrog Method")
    plt.show()
