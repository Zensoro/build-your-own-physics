**简体中文** | [**English**](README.en.md)

# Challenge 02 · Pendulum

> **当欧拉法开始撒谎：单摆教你认识数值误差。**
> 需要：挑战 01 的经验 + 三角函数直觉（math.sin 就是"转圈"，见数学补给站）。

## Why This Challenge

挑战 01 的欧拉法"够用就好"。但单摆会暴露它的致命弱点——**能量会漂移**。你会看到摆越摆越高（能量凭空增加），这是数值方法的错，不是物理的错。

理解这一点，是你从"会用欧拉法"到"懂得选积分器"的分水岭。

> 🎓 需要 AI 导师吗？复制 [ai/tutor.md](ai/tutor.md)（挑战 01 的模板稍作修改即可）给你的 AI 助手。

## Physics Background

### 运动方程

无摩擦单摆（小角度近似 $\sin\theta \approx \theta$ 之前）：

$$ \frac{d^2\theta}{dt^2} = -\frac{g}{L}\sin\theta $$

写成两个一阶方程：

$$ \frac{d\omega}{dt} = -\frac{g}{L}\sin\theta, \quad \frac{d\theta}{dt} = \omega $$

其中 $\theta$ 是摆角，$\omega$ 是角速度。

### 能量

$$ E = \frac{1}{2}mL^2\omega^2 + mgL(1 - \cos\theta) $$

在无摩擦系统中，$E$ 应该**永远守恒**。这是你检验数值方法最好的标尺。

## Your Task

1. 用**欧拉法**模拟单摆，观察能量随时间的变化——它会"漂移"
2. 换成**欧拉-克罗默法（Euler-Cromer，又称半隐式欧拉）**，观察能量是否守恒
3. 绘制 $(\theta, \omega)$ 相空间图，观察轨迹形状

### Starter Code

```python
# challenges/02-pendulum/starter/pendulum.py
import math
import matplotlib.pyplot as plt

G = 9.81

def simulate_euler(L, theta0, omega0=0.0, dt=0.01, t_max=20.0):
    """欧拉法模拟单摆。"""
    theta, omega = theta0, omega0
    times, thetas, omegas = [0.0], [theta], [omega]
    t = 0.0
    while t < t_max:
        # TODO: 欧拉法更新
        # omega = omega + (-G / L * math.sin(theta)) * dt
        # theta = theta + omega * dt
        t += dt
        times.append(t)
        thetas.append(theta)
        omegas.append(omega)
    return times, thetas, omegas

def simulate_euler_cromer(L, theta0, omega0=0.0, dt=0.01, t_max=20.0):
    """欧拉-克罗默法模拟单摆。"""
    theta, omega = theta0, omega0
    times, thetas, omegas = [0.0], [theta], [omega]
    t = 0.0
    while t < t_max:
        # TODO: 欧拉-克罗默法更新
        # 注意：更新 omega 时用的是新的 theta 还是旧的？
        # omega_new = omega + (-G / L * math.sin(theta_old)) * dt
        # theta_new = theta + omega_new * dt
        t += dt
        times.append(t)
        thetas.append(theta)
        omegas.append(omega)
    return times, thetas, omegas

if __name__ == "__main__":
    L, theta0 = 1.0, math.radians(30.0)
    t_e, th_e, om_e = simulate_euler(L, theta0)
    t_c, th_c, om_c = simulate_euler_cromer(L, theta0)
    
    # 画相空间
    plt.plot(th_e, om_e, label="Euler")
    plt.plot(th_c, om_c, label="Euler-Cromer")
    plt.xlabel("theta (rad)")
    plt.ylabel("omega (rad/s)")
    plt.legend()
    plt.show()
```

### 完成后的检查

- [ ] 欧拉法的相空间轨迹是**向外扩散的螺旋**（能量增长）
- [ ] 欧拉-克罗默法的相空间轨迹是**闭合的圆**（能量守恒）
- [ ] 对比两种方法在相同参数下的能量-时间图
- [ ] 回答：为什么欧拉法会让摆越摆越高？

## Hints

<details>
<summary>展开查看提示</summary>

- 欧拉-克罗默法的关键：**用新的 $\omega$ 去更新 $\theta$**，即 $\theta_{n+1} = \theta_n + \omega_{n+1}\Delta t$
- 相空间中，守恒系统表现为闭合曲线；耗散系统表现为向内螺旋
- 试试把初始角度设为 $170°$（接近倒立），看看大角度下小角度近似的失效
- 能量单位可以归一化，只看相对变化 $\Delta E / E_0$
</details>

## Next Steps

你已经见识了数值方法的陷阱。挑战 03（轨道）将引入**蛙跳法**——一个既简单又神奇地保持能量守恒的方法，并带你验证开普勒定律。

→ [前往挑战 03：Orbit](../03-orbit/README.md)
