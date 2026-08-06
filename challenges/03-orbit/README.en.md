**English** | [**简体中文**](README.md)

# Challenge 03 · Orbit

> **Write down the law of gravity, set a planet in orbit — then verify Kepler.**

> You'll need: what you learned in Challenges 01-02 + squares and square roots.
> 🎓 There's an AI tutor: [ai/tutor.en.md](ai/tutor.en.md)

## Why This Challenge

This is the first "wow" moment in the whole repository: starting from a single law, $\vec{F} = G m_1 m_2 / r^2$, you'll watch **elliptical orbits emerge on their own**. Better still, you can use your own simulation data to verify all three of Kepler's laws — that's the power of rebuilding things from scratch.

## Physics Background

### Universal gravitation

$$ \vec{F} = -\frac{G M m}{r^2}\hat{r} $$

For a planet (mass $m$) orbiting the Sun (mass $M$):

$$ \frac{d^2\vec{r}}{dt^2} = -\frac{GM}{r^2}\hat{r} $$

### The leapfrog method (Leapfrog / Velocity Verlet)

Challenge 02 showed us that the Euler method breaks energy conservation. The leapfrog method uses a trick — **staggered half steps** — to keep energy stable over long simulations:

```
1. 半步推进速度：v(t + Δt/2) = v(t) + a(t) * Δt/2
2. 整步推进位置：x(t + Δt)   = x(t) + v(t + Δt/2) * Δt
3. 计算新加速度：a(t + Δt) = F(x(t + Δt)) / m
4. 半步推进速度：v(t + Δt)   = v(t + Δt/2) + a(t + Δt) * Δt/2
```

It's a **symplectic integrator** — its long-term energy drift stays bounded, which is exactly what orbital simulation needs.

## Your Task

1. Use the leapfrog method to simulate a planet orbiting the Sun (with the Sun held fixed)
2. Verify that the orbit is an ellipse (with the Sun at one focus)
3. Use your simulation data to verify **Kepler's three laws**:
   - **First law**: the orbit is an ellipse with the Sun at a focus
   - **Second law**: equal areas are swept in equal times (constant areal velocity)
   - **Third law**: $T^2 \propto a^3$ (run several simulations with different initial conditions to check)

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

### Checklist after completion

- [ ] The orbit closes (after one year the planet returns near its starting point)
- [ ] With an initial speed of $0.8 \times v_0$, the orbit becomes a clearly visible ellipse
- [ ] With $1.2 \times v_0$, the orbit is still an ellipse (not escaping yet)
- [ ] With $\sqrt{2} \times v_0$, the orbit becomes a parabola (escape velocity!)
- [ ] The areal velocity stays constant (second law)
- [ ] The energy drifts by $< 0.1\%$ after 10,000 steps (the power of the leapfrog method)

## Hints

<details>
<summary>Expand for hints</summary>

- The gravitational parameter is $\mu = GM$; using $\mu$ instead of $G \times M$ saves a bit of computation
- Verifying the second law: compute the area swept by the Sun–planet line in each time step — it should stay constant
- Verifying the third law: vary the orbital radius $a$, measure the period $T$, and plot $\log T$ vs $\log a$; the slope should be $3/2$
- Units matter: use AU and years and the numbers become much friendlier
</details>

## Next Steps

You now have a stable, energy-conserving integrator. Challenge 04 upgrades a single star into a many-body system — the N-body problem — and introduces the Barnes-Hut acceleration algorithm.

→ [Go to Challenge 04: N-Body](../04-nbody/README.en.md)
