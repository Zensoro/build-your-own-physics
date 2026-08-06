**English** | [**简体中文**](README.md)

# Challenge 01 · Projectile Motion

> **Build a projectile from scratch and watch it really fly.**
> All you need: the Python basics from Challenge 00 plus an AI assistant. No calculus, no college physics.

## Why This Challenge

Projectile motion is the first piece of "physics code" you'll ever write. It's simple enough to need just one law, yet it already contains the core pattern of every challenge that follows: **read the law → write the code → run it → see the phenomenon**.

Finish this one and you'll have the rhythm of the whole repository.

## What You Need

| You need | Notes |
|--------|------|
| The Python basics from Challenge 00 | Variables, loops, lists, functions, plotting |
| An AI assistant | ChatGPT / Claude / Doubao / DeepSeek |
| Arithmetic + the Pythagorean theorem | That's genuinely all |

**Don't be scared of the math**: the "differential equation" and "numerical integration" in this section can stay a black box for now — copy the code pattern, run it, watch the parabola appear, and *then* ask your AI to build the intuition for you.

## 🎓 Is There an AI Tutor?

**Yes.** Every challenge ships with AI collaboration prompts: [ai/tutor.en.md](ai/tutor.en.md). Paste those prompts into your AI assistant and it will:
- Walk you through writing the code step by step (never handing you the full answer)
- Ask questions to help you debug when you're stuck
- Quiz you at the end to make sure you really understood it

## Physics Background

### There Is Only One Law

$$ \vec{F} = m\vec{a} $$

Substitute gravity and you get the equations of motion:

$$ \frac{d\vec{v}}{dt} = \vec{g}, \quad \frac{d\vec{x}}{dt} = \vec{v} $$

where $\vec{g} = (0, -9.81) \text{ m/s}^2$ (taking $y$ as up).

### The Intuitive Version: What Is a "Differential Equation"?

Don't let the name scare you. It's really just one sentence:

```
Gravity is changing the velocity at every instant (downward, 9.81 m/s²).
The position follows the velocity at every instant.
```

That's it. Everything else is just "translating that sentence into code."

### Key Idea: From Differential Equation to Numerical Integration

We don't know an analytic expression for the position $x(t)$ — and that's fine. We can just **push it forward one small step at a time**:

```
For each small step Δt:
    v_new = v + g * Δt          # gravity changes the velocity
    x_new = x + v * Δt          # velocity changes the position
```

This is the **Euler method** — the simplest and most important numerical integration scheme there is. It isn't accurate, but it's accurate enough to show you the phenomenon, and inaccurate enough that in Challenge 02 you'll feel exactly why it isn't good enough.

## Your Task

In the language you're comfortable with, write a projectile simulation from scratch:

1. Given an initial speed $v_0$ and a launch angle $\theta$, simulate the projectile's trajectory
2. Use the Euler method, with an adjustable time step $\Delta t$
3. Print or plot the trajectory

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

### Checklist After Completion

- [ ] Launched at 45°, the trajectory is a nice clean parabola
- [ ] The range (the landing x coordinate) is close to the theoretical value $R = v_0^2 \sin(2\theta) / g$
- [ ] The peak height is close to the theoretical value $H = v_0^2 \sin^2\theta / (2g)$
- [ ] As you shrink $\Delta t$, the range gets closer and closer to the theoretical value

## Hints

<details>
<summary>Click to reveal the hints</summary>

- Euler method update order: **update the velocity first, then the position**
- The vertical acceleration is $-g$ (downward); the horizontal acceleration is $0$
- Theoretical range: $R = \frac{v_0^2 \sin(2\theta)}{g}$, which is about 255 m for $v_0 = 50, \theta = 45°$
- Try $\theta = 45°$ and $\theta = 30°$ and see which one flies farther
</details>

## Next Steps

Now that you've finished Challenge 01, you know how to "push a particle along." Challenge 02 (the pendulum) will show you the limits of the Euler method and introduce a smarter integrator.

→ [Go to Challenge 02: Pendulum](../02-pendulum/README.en.md)
