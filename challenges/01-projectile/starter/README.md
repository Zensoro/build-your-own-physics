# Challenge 01 · Projectile Motion — Starter Code

> 这是挑战 01 的起步代码。**你的任务是把 `TODO` 补全。**
> 运行环境：Python 3.8+，只需 `math`（画图需 Matplotlib）。

## 文件结构

```
starter/
├── projectile.py     # 你的实现（补全 TODO）
└── verify.py         # 自动验收（跑这个检查你过没过关）
```

## projectile.py

```python
"""抛体运动模拟：欧拉法。

任务：补全 TODO 部分，让 simulate 能正确运行并通过 verify.py 验收。
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
```

## verify.py

```python
"""挑战 01 自动验收。运行：python verify.py"""

import math
import sys

sys.path.insert(0, ".")
from projectile import simulate

G = 9.81

passed, failed = [], []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


V0, THETA = 50.0, 45.0

print("=== S1.1 接口 ===")
times, xs, ys = simulate(V0, THETA)
check("返回三个列表且长度相等", len(times) == len(xs) == len(ys) > 0)
check("从原点出发", abs(xs[0]) < 1e-12 and abs(ys[0]) < 1e-12)
check("时间从 0 开始", abs(times[0]) < 1e-12)

print("=== S1.2 轨迹形状 ===")
check("y 始终 >= 0（落地即停）", min(ys) >= -1e-9)
check("y 有上升段和下降段（抛物线）",
      max(ys) > 10.0 and ys[0] < max(ys) and ys[-1] < max(ys))

print("=== S1.3 射程精度（收敛性检验） ===")
R_theory = V0**2 * math.sin(2 * math.radians(THETA)) / G

def range_of(dt):
    _, xs_dt, _ = simulate(V0, THETA, dt=dt)
    return xs_dt[-1]

R_fine = range_of(0.001)
err_fine = abs(R_fine - R_theory) / R_theory
check(f"dt=0.001 射程 {R_fine:.1f}m vs 理论 {R_theory:.1f}m, 误差 {err_fine:.2%} < 2%",
      err_fine < 0.02)

# 收敛性：dt 减半，误差应约减半（欧拉法一阶精度）
R_coarse = range_of(0.002)
err_coarse = abs(R_coarse - R_theory) / R_theory
check(f"收敛性: dt=0.002 误差 {err_coarse:.2%} ≈ 2× dt=0.001 误差 {err_fine:.2%}",
      abs(err_coarse / max(err_fine, 1e-9) - 2.0) < 0.5)

print("=== S1.4 最高点精度 ===")
H_theory = (V0 * math.sin(math.radians(THETA)))**2 / (2 * G)
H_sim = max(ys)
err_h = abs(H_sim - H_theory) / H_theory
check(f"最高点 {H_sim:.1f}m vs 理论 {H_theory:.1f}m, 误差 {err_h:.2%} < 2%", err_h < 0.02)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 02 吧！")
```

## 使用方法

```bash
cd challenges/01-projectile/starter
python verify.py     # 验收
python projectile.py # 画图看现象
```

## 完成后的检查（对照）

- [ ] 45° 发射，轨迹是漂亮的抛物线
- [ ] 射程接近理论值 254.8 m
- [ ] 减小 dt，射程越来越接近理论值
- [ ] `verify.py` 全部通过

## 如果卡住了

1. 先看 README 的 Hints（展开）
2. 问 AI 导师（`../ai/tutor.md`）
3. 实在不行再看 `../solutions/`
