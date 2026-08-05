"""抛体运动模拟：欧拉法。

任务：补全 TODO 部分，让 simulate 能正确运行并通过 verify.py 验收。
运行：python verify.py（验收）或 python projectile.py（画图看现象）
"""

import math

G = 9.81  # m/s^2


def simulate(v0, theta_deg, dt=0.01, t_max=10.0):
    """欧拉法模拟抛体运动（无空气阻力）。

    Args:
        v0: 初速度 (m/s)
        theta_deg: 发射角 (度)
        dt: 时间步长 (s)
        t_max: 模拟总时长 (s)

    Returns:
        (times, xs, ys): 时间、x 坐标、y 坐标三个列表
    """
    theta = math.radians(theta_deg)
    vx = v0 * math.cos(theta)   # 水平初速度
    vy = v0 * math.sin(theta)   # 竖直初速度
    x, y = 0.0, 0.0

    times, xs, ys = [0.0], [x], [y]
    t = 0.0

    while t < t_max and y >= 0:
        # TODO 1: 欧拉法更新（挑战 00 学过的顺序）
        # 提示：
        #   重力只影响竖直速度：vy = vy - G * dt   （向下加速）
        #   水平速度不变：vx 不用动
        #   位置跟着速度走：x = x + vx * dt
        #                    y = y + vy * dt

        t += dt
        times.append(t)
        xs.append(x)
        ys.append(y)

    return times, xs, ys


if __name__ == "__main__":
    # 手动测试：画 45° 的抛物线
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("未安装 matplotlib，跳过画图。")
        raise SystemExit

    times, xs, ys = simulate(50.0, 45.0)
    plt.plot(xs, ys)
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Projectile Motion (Euler, v0=50, 45°)")
    plt.axis("equal")
    plt.show()
