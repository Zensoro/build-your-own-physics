**English** | [**简体中文**](README.md)

# Challenge 02 · Pendulum — Starter Code

> This is the starter code for Challenge 02. **Your job is to fill in the `TODO`s.**
> Environment: Python 3.8+, only `math` is required (Matplotlib if you want plots).

## File structure

```
starter/
├── pendulum.py        # 你的实现（补全 TODO）
└── verify.py          # 自动验收（跑这个检查你过没过关）
```

## pendulum.py

```python
"""单摆模拟：欧拉法 vs 欧拉-克罗默法。

任务：补全 TODO 部分，让两个函数都能运行并通过 verify.py 验收。
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
        #   角加速度 alpha = -G / L * sin(theta)   （重力造成的）
        #   先更新角速度：omega = omega + alpha * dt
        #   再更新角度：  theta = theta + omega * dt
        #   （先速度后位置——挑战 01 学过的顺序）

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
        #   角加速度 alpha = -G / L * sin(theta)
        #   先更新角速度：omega_new = omega + alpha * dt
        #   再更新角度：  theta = theta + omega_new * dt   ← 用新的 omega！
        #   注意：这个函数里，变量 omega 可以先等于新值，再用于角度更新。

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
```

## verify.py

```python
"""挑战 02 自动验收。运行：python verify.py"""

import math
import sys

sys.path.insert(0, ".")
from pendulum import simulate_euler, simulate_euler_cromer, energy

G = 9.81
L, theta0, omega0, dt, t_max = 1.0, math.radians(30.0), 0.0, 0.01, 20.0

passed = []
failed = []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


print("=== S2.1 接口 ===")
t_e, th_e, om_e = simulate_euler(L, theta0, omega0, dt, t_max)
t_c, th_c, om_c = simulate_euler_cromer(L, theta0, omega0, dt, t_max)
check("返回长度相等 (欧拉)", len(t_e) == len(th_e) == len(om_e) > 0)
check("返回长度相等 (欧拉-克罗默)", len(t_c) == len(th_c) == len(om_c) > 0)
check("初始条件正确", abs(th_e[0] - theta0) < 1e-12 and abs(om_e[0]) < 1e-12)

print("=== S2.2 运动范围（小角度不发散） ===")
check("欧拉法摆角未爆掉", max(abs(a) for a in th_e) < 10.0)
check("欧拉-克罗默摆角未爆掉", max(abs(a) for a in th_c) < 10.0)

print("=== S2.3 小角度周期 ===")
t5, th5, _ = simulate_euler_cromer(L, math.radians(5.0), 0.0, 0.001, 10.0)
zero_crossings = sum(1 for i in range(1, len(th5)) if th5[i - 1] * th5[i] < 0)
T_sim = 10.0 / max(zero_crossings / 2, 1) if zero_crossings >= 2 else 0.0
T_theory = 2 * math.pi * math.sqrt(L / G)
check(f"小角度周期 {T_sim:.3f}s ≈ 理论 {T_theory:.3f}s (误差<2%)",
      abs(T_sim - T_theory) / T_theory < 0.02)

print("=== S2.4 能量行为 ===")
E0 = energy(L, [theta0], [0.0])[0]
Ee = energy(L, th_e, om_e)
Ec = energy(L, th_c, om_c)
drift_e = (Ee[-1] - E0) / E0
drift_c = (Ec[-1] - E0) / E0
check(f"欧拉法能量漂移 {drift_e:+.2%} > +5% (确实在撒谎)",
      drift_e > 0.05)
check(f"欧拉-克罗默能量漂移 {drift_c:+.2%} < 1% (守恒)",
      abs(drift_c) < 0.01)
check("欧拉法漂移方向是增长 (E 增加)", drift_e > 0)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 03 吧！")
```

## How to run it

```bash
cd challenges/02-pendulum/starter
python verify.py     # 验收
python pendulum.py   # 画图看现象
```

## Checklist after completion (compare against these)

- [ ] The Euler phase space is an **outward spiral** (energy growing)
- [ ] The Euler–Cromer phase space is a **closed curve** (energy conserved)
- [ ] Energy plot: the Euler curve clearly rises, the Euler–Cromer curve stays essentially flat
- [ ] `verify.py` passes everything

## If you get stuck

1. Start with the Hints in the README (expand them)
2. Ask your AI tutor (`../ai/tutor.en.md`)
3. Only if nothing works, look at `../solutions/`
