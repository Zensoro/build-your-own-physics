"""二体轨道模拟：蛙跳法（辛积分器）。

任务：补全 TODO 部分，让 simulate 能正确运行并通过 verify.py 验收。
单位：AU-年制（距离=AU，时间=年），mu = 4*pi^2 AU^3/yr^2。
运行：python verify.py（验收）或 python orbit.py（画图看现象）
"""

import math

MU = 4.0 * math.pi * math.pi  # 太阳引力参数 (AU^3/yr^2)


def simulate(mu, x0, y0, vx0, vy0, dt, n_steps):
    """蛙跳法（Velocity Verlet）模拟行星绕固定太阳的轨道。

    Args:
        mu: 引力参数 GM (AU^3/yr^2)
        x0, y0: 初始位置 (AU)
        vx0, vy0: 初始速度 (AU/yr)
        dt: 时间步长 (yr)
        n_steps: 步数

    Returns:
        (xs, ys): 位置列表，长度 n_steps + 1
    """
    x, y = x0, y0
    vx, vy = vx0, vy0
    xs, ys = [x], [y]

    for _ in range(n_steps):
        r = math.hypot(x, y)                 # 到太阳的距离
        ax = -mu * x / r**3                  # x 方向加速度
        ay = -mu * y / r**3                  # y 方向加速度

        # TODO: 蛙跳法（Velocity Verlet）三步
        # 1. 半步推进速度：vx += ax * dt/2,  vy += ay * dt/2
        # 2. 整步推进位置：x += vx * dt,     y += vy * dt
        # 3. 用新位置重算加速度，再半步推进速度：
        #    r_new = hypot(x, y)
        #    ax_new = -mu * x / r_new**3
        #    ay_new = -mu * y / r_new**3
        #    vx += ax_new * dt/2
        #    vy += ay_new * dt/2

        xs.append(x)
        ys.append(y)

    return xs, ys


def energy(mu, xs, ys, vx_list, vy_list):
    """计算总机械能 E = 1/2 v^2 - mu/r（单位质量）。

    注意：本函数需要速度序列。蛙跳法模拟中，速度定义在半时间步。
    更简单的方式：在 simulate 里同时记录速度，或用
    v = (x[n+1] - x[n-1]) / (2*dt) 从位置差分估计。
    """
    return [0.5 * (vx**2 + vy**2) - mu / math.hypot(x, y)
            for x, y, vx, vy in zip(xs, ys, vx_list, vy_list)]


if __name__ == "__main__":
    # 手动测试：画圆轨道和椭圆轨道
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("未安装 matplotlib，跳过画图。")
        raise SystemExit

    DT = 0.001   # 年
    N = 1000     # 一年

    # 圆轨道（地球）
    xs_c, ys_c = simulate(MU, 1.0, 0.0, 0.0, 2.0 * math.pi, DT, N)

    # 椭圆轨道（0.8 倍圆速度）
    xs_e, ys_e = simulate(MU, 1.0, 0.0, 0.0, 0.8 * 2.0 * math.pi, DT, N)

    plt.figure(figsize=(6, 6))
    plt.plot(xs_c, ys_c, label="circular (v = v_c)")
    plt.plot(xs_e, ys_e, label="elliptical (v = 0.8 v_c)")
    plt.scatter([0], [0], color="orange", s=80, label="Sun")
    plt.axis("equal")
    plt.legend()
    plt.show()
