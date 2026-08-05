# Challenge 03 · Orbit

> **写下万有引力，让一颗行星绕起来——然后验证开普勒。**

> 需要：挑战 01-02 的经验 + 平方/开方运算。
> 🎓 有 AI 导师：[ai/tutor.md](ai/tutor.md)

## Why This Challenge

这是整个仓库第一个"哇"时刻：从一条定律 $\vec{F} = G m_1 m_2 / r^2$ 出发，你会亲眼看到**椭圆轨道自然涌现**。更妙的是，你还能用模拟数据验证开普勒三大定律——这就是"从零重构"的威力。

## Physics Background

### 万有引力

$$ \vec{F} = -\frac{G M m}{r^2}\hat{r} $$

对绕太阳（质量 $M$）运动的行星（质量 $m$）：

$$ \frac{d^2\vec{r}}{dt^2} = -\frac{GM}{r^2}\hat{r} $$

### 蛙跳法（Leapfrog / Velocity Verlet）

挑战 02 告诉我们欧拉法会破坏能量守恒。蛙跳法通过**交错半步**的技巧，让能量在长期模拟中保持稳定：

```
1. 半步推进速度：v(t + Δt/2) = v(t) + a(t) * Δt/2
2. 整步推进位置：x(t + Δt)   = x(t) + v(t + Δt/2) * Δt
3. 计算新加速度：a(t + Δt) = F(x(t + Δt)) / m
4. 半步推进速度：v(t + Δt)   = v(t + Δt/2) + a(t + Δt) * Δt/2
```

它是**辛积分器（symplectic integrator）**——长期能量漂移有界，这正是轨道模拟需要的。

## Your Task

1. 用蛙跳法模拟一颗行星绕太阳运动（太阳固定）
2. 验证轨道是椭圆（太阳在一个焦点上）
3. 用模拟数据验证**开普勒三大定律**：
   - **第一定律**：轨道是椭圆，太阳在焦点
   - **第二定律**：相同时间内扫过相同面积（面积速度恒定）
   - **第三定律**：$T^2 \propto a^3$（不同初始条件跑多次验证）

### Starter Code

```python
# challenges/03-orbit/starter/orbit.py
import math
import matplotlib.pyplot as plt

G = 6.674e-11
M_SUN = 1.989e30
AU = 1.496e11
YEAR = 3.156e7

def simulate(mu, x0, y0, vx0, vy0, dt, n_steps):
    """蛙跳法模拟二体轨道（太阳固定在原点）。
    
    mu = G * M 为引力参数。
    """
    x, y = x0, y0
    vx, vy = vx0, vy0
    xs, ys = [x], [y]
    
    for _ in range(n_steps):
        r = math.hypot(x, y)
        ax, ay = -mu * x / r**3, -mu * y / r**3
        # TODO: 蛙跳法三步
        # 1. 半步推进速度
        # 2. 整步推进位置
        # 3. 计算新加速度，再半步推进速度
        xs.append(x)
        ys.append(y)
    
    return xs, ys

if __name__ == "__main__":
    # 地球绕太阳，圆轨道近似（实际是椭圆）
    mu = G * M_SUN
    x0, y0 = 1.0 * AU, 0.0
    v0 = math.sqrt(mu / (1.0 * AU))  # 圆轨道速度
    vx0, vy0 = 0.0, v0
    dt = 3600.0  # 1 小时
    n_steps = int(365.0 * 24)  # 一年
    
    xs, ys = simulate(mu, x0, y0, vx0, vy0, dt, n_steps)
    plt.plot(xs, ys)
    plt.scatter([0], [0], color="orange", s=80, label="Sun")
    plt.axis("equal")
    plt.legend()
    plt.show()
```

### 完成后的检查

- [ ] 轨道闭合（一年后回到起点附近）
- [ ] 用 $0.8 \times v_0$ 的初速度，轨道变成明显的椭圆
- [ ] 用 $1.2 \times v_0$，轨道仍是椭圆（还没逃逸）
- [ ] 用 $\sqrt{2} \times v_0$，轨道变成抛物线（逃逸速度！）
- [ ] 面积速度恒定（第二定律）
- [ ] 能量在 1 万步后漂移 $< 0.1\%$（蛙跳法的威力）

## Hints

<details>
<summary>展开查看提示</summary>

- 引力参数 $\mu = GM$，用 $\mu$ 代替 $G \times M$ 可以减少计算量
- 第二定律验证：计算每个时间步内行星与太阳连线扫过的面积，应该恒定
- 第三定律验证：改变轨道半径 $a$，测周期 $T$，画 $\log T$ vs $\log a$，斜率应为 $3/2$
- 单位很重要：用 AU 和年做单位，数字会更友好
</details>

## Next Steps

你有了一个稳定、能量守恒的积分器。挑战 04 将把单星升级为多体系统——N 体问题，并引入 Barnes-Hut 加速算法。

→ [前往挑战 04：N-Body](../04-nbody/README.md)
