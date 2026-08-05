# Challenge 01 · Projectile Motion

> **从零模拟一个抛体，看到它真的飞起来。**
> 只需要：挑战 00 的 Python 基础 + 一个 AI 助手。不需要微积分、不需要大学物理。

## Why This Challenge

抛体运动是你写下的第一段"物理代码"。它简单到只用一条定律，却包含了所有后续挑战的核心模式：**读定律 → 写代码 → 跑起来 → 看到现象**。

完成它，你就掌握了这个仓库的节奏。

## 你需要什么

| 你需要 | 说明 |
|--------|------|
| 挑战 00 的 Python 基础 | 变量、循环、列表、函数、画图 |
| 一个 AI 助手 | ChatGPT / Claude / 豆包 / DeepSeek |
| 四则运算 + 勾股定理 | 就这些，真的 |

**数学不用怕**：本节用到的"微分方程"和"数值积分"，你可以先当作"黑盒"——照着代码模式抄，跑起来看到抛物线后，再让 AI 给你讲直觉。

## 🎓 有 AI 导师吗？

**有。** 每个挑战都配有 AI 协作提示词：[ai/tutor.md](ai/tutor.md)。复制里面的提示词给你的 AI 助手，它就会：
- 引导你一步步写代码（不给完整答案）
- 你卡住时用提问帮你 debug
- 完成后考你，确保你真懂了

## Physics Background

### 定律只有一个

$$ \vec{F} = m\vec{a} $$

把重力代进去，得到运动方程：

$$ \frac{d\vec{v}}{dt} = \vec{g}, \quad \frac{d\vec{x}}{dt} = \vec{v} $$

其中 $\vec{g} = (0, -9.81) \text{ m/s}^2$（取 $y$ 向上）。

### 直觉版：什么是"微分方程"？

不需要害怕这个名字。它就是一句话：

```
速度每时每刻都在被重力改变（向下 9.81 m/s²）。
位置每时每刻都在跟着速度走。
```

就这么简单。剩下的全是"把这句话翻译成代码"。

### 关键概念：从微分方程到数值积分

我们不知道位置 $x(t)$ 的解析表达式——但没关系。我们可以**一小步一小步地推**：

```
每一小步 Δt：
    v_new = v + g * Δt          # 速度被重力改变
    x_new = x + v * Δt          # 位置被速度改变
```

这就是 **欧拉法（Euler method）**——最简单也最重要的数值积分方法。它不精确，但足够让你看到现象，也足够让你在挑战 02 中体会到它为什么不够好。

## Your Task

用你熟悉的语言，从零写出抛体模拟：

1. 给定初速度 $v_0$ 和发射角 $\theta$，模拟抛体轨迹
2. 使用欧拉法，时间步长 $\Delta t$ 可调
3. 输出或绘制轨迹

### Starter Code

```python
# challenges/01-projectile/starter/projectile.py
import math
import matplotlib.pyplot as plt

G = 9.81  # m/s^2

def simulate(v0, theta_deg, dt=0.01, t_max=10.0):
    """欧拉法模拟抛体运动。
    
    Args:
        v0: 初速度 (m/s)
        theta_deg: 发射角 (度)
        dt: 时间步长 (s)
        t_max: 模拟总时长 (s)
    
    Returns:
        (times, xs, ys): 三个列表，分别为时间、x 坐标、y 坐标
    """
    theta = math.radians(theta_deg)
    vx, vy = v0 * math.cos(theta), v0 * math.sin(theta)
    x, y = 0.0, 0.0
    
    times, xs, ys = [0.0], [x], [y]
    t = 0.0
    while t < t_max and y >= 0:
        # TODO: 更新速度 (欧拉法)
        # vx = ...
        # vy = ...
        # TODO: 更新位置
        # x = ...
        # y = ...
        
        t += dt
        times.append(t)
        xs.append(x)
        ys.append(y)
    
    return times, xs, ys

if __name__ == "__main__":
    times, xs, ys = simulate(v0=50.0, theta_deg=45.0)
    plt.plot(xs, ys)
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Projectile Motion")
    plt.axis("equal")
    plt.show()
```

### 完成后的检查

- [ ] 45° 角发射，轨迹是一条漂亮的抛物线
- [ ] 射程（落点 x 坐标）接近理论值 $R = v_0^2 \sin(2\theta) / g$
- [ ] 最高点接近理论值 $H = v_0^2 \sin^2\theta / (2g)$
- [ ] 减小 $\Delta t$，射程越来越接近理论值

## Hints

<details>
<summary>展开查看提示</summary>

- 欧拉法更新顺序：**先更新速度，再更新位置**
- 竖直方向加速度是 $-g$（向下），水平方向是 $0$
- 理论射程：$R = \frac{v_0^2 \sin(2\theta)}{g}$，$v_0 = 50, \theta = 45°$ 时约 255 m
- 尝试 $\theta = 45°$ 和 $\theta = 30°$，看看哪个飞得更远
</details>

## Next Steps

完成挑战 01 后，你已经会"推着粒子走"了。挑战 02（单摆）将展示欧拉法的局限，并引入更聪明的积分方法。

→ [前往挑战 02：Pendulum](../02-pendulum/README.md)
