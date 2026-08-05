# Challenge 03 · Orbit — Starter Code

> 这是挑战 03 的起步代码。**你的任务是把 `TODO` 补全。**
> 运行环境：Python 3.8+，只需 `math`（画图需 Matplotlib）。

## 文件结构

```
starter/
├── orbit.py          # 你的实现（补全 TODO）
└── verify.py         # 自动验收（跑这个检查你过没过关）
```

## 单位制说明（重要）

我们使用 **AU-年制**（推荐，数字友好）：
- 距离单位：AU（1 AU = 日地距离）
- 时间单位：年
- 引力参数 $\mu = GM = 4\pi^2$ AU³/yr²

在这个单位制下，地球的圆轨道速度恰好是 $v = 2\pi$ AU/yr，周期恰为 1 年。开普勒第三定律自动满足 $T^2 = a^3$（AU/年制）。

## orbit.py

```python
"""二体轨道模拟：蛙跳法（辛积分器）。

任务：补全 TODO 部分，让 simulate 能正确运行并通过 verify.py 验收。
单位：AU-年制（距离=AU，时间=年），mu = 4*pi^2 AU^3/yr^2。
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
```

## verify.py

```python
"""挑战 03 自动验收。运行：python verify.py"""

import math
import sys

sys.path.insert(0, ".")
from orbit import simulate, MU

DT = 0.001   # 年
N = 1000     # 一年

passed, failed = [], []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


def energy_series(xs, ys, mu, dt):
    """从位置序列用中心差分估计速度，计算每个时刻的能量。"""
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


print("=== S3.1 接口 ===")
xs, ys = simulate(MU, 1.0, 0.0, 0.0, 2 * math.pi, DT, N)
check("返回列表长度 = n_steps + 1", len(xs) == N + 1 and len(ys) == N + 1)
check("初始位置正确", abs(xs[0] - 1.0) < 1e-12 and abs(ys[0]) < 1e-12)

print("=== S3.2 圆轨道稳定 ===")
r_vals = [math.hypot(x, y) for x, y in zip(xs, ys)]
check("轨道半径在 0.95~1.05 AU", 0.95 < min(r_vals) and max(r_vals) < 1.05)
check("一年后回到起点 (闭合)", math.hypot(xs[-1] - 1.0, ys[-1]) < 0.05)

print("=== S3.3 椭圆轨道 (0.8 v_c) ===")
xs_e, ys_e = simulate(MU, 1.0, 0.0, 0.0, 0.8 * 2 * math.pi, DT, N)
r_e = [math.hypot(x, y) for x, y in zip(xs_e, ys_e)]
check("椭圆：0.3 < min(r) < max(r) < 1.6", 0.3 < min(r_e) < max(r_e) < 1.6)

print("=== S3.4 能量守恒（蛙跳法核心优势） ===")
es = energy_series(xs, ys, MU, DT)
drift = abs(es[-1] - es[0]) / abs(es[0])
check(f"圆轨道 1000 步能量漂移 {drift:.4%} < 0.1%", drift < 0.001)
es_e = energy_series(xs_e, ys_e, MU, DT)
drift_e = abs(es_e[-1] - es_e[0]) / abs(es_e[0])
check(f"椭圆轨道 1000 步能量漂移 {drift_e:.4%} < 0.1%", drift_e < 0.001)

print("=== S3.6 逃逸速度 ===")
xs_p, ys_p = simulate(MU, 1.0, 0.0, 0.0, math.sqrt(2) * 2 * math.pi, DT, N)
r_p = math.hypot(xs_p[-1], ys_p[-1])
check(f"sqrt(2)*v_c 一年后 r={r_p:.2f} > 2 AU (逃逸)", r_p > 2.0)
xs_h, ys_h = simulate(MU, 1.0, 0.0, 0.0, 1.5 * 2 * math.pi, DT, N)
r_h = math.hypot(xs_h[-1], ys_h[-1])
check(f"1.5*v_c 一年后 r={r_h:.2f} > 3 AU (更快逃逸)", r_h > 3.0)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 04 吧！")
```

## 使用方法

```bash
cd challenges/03-orbit/starter
python verify.py     # 验收
python orbit.py      # 画图看现象
```

## 完成后的检查（对照）

- [ ] 圆轨道：完美的圆，一年闭合
- [ ] 椭圆轨道（0.8 v）：太阳在椭圆一个焦点
- [ ] 能量图：几乎水平的直线（蛙跳法的魔法）
- [ ] `verify.py` 全部通过

## 如果卡住了

1. 先看 README 的 Hints（展开）
2. 问 AI 导师（`../ai/tutor.md`）
3. 实在不行再看 `../solutions/`
