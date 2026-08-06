**English** | [**简体中文**](README.md)

# Challenge 02 · Pendulum

> **When the Euler method starts lying: the pendulum teaches you about numerical error.**
> You'll need: what you learned in Challenge 01 + a feel for trigonometry (`math.sin` is just "going around a circle" — see the math primer).

## Why This Challenge

In Challenge 01, the Euler method was "good enough." But a pendulum exposes its fatal weakness — **the energy drifts**. You'll watch the pendulum swing higher and higher (energy appearing out of nowhere), and that's the numerical method's fault, not physics'.

Understanding this is the dividing line between "I can use the Euler method" and "I know how to choose an integrator."

> 🎓 Want an AI tutor? Copy [ai/tutor.en.md](ai/tutor.en.md) into your AI assistant (the Challenge 01 template works too with small tweaks).

## Physics Background

### Equation of motion

A frictionless pendulum (before you make the small-angle approximation $\sin\theta \approx \theta$):

$$ \frac{d^2\theta}{dt^2} = -\frac{g}{L}\sin\theta $$

Written as two first-order equations:

$$ \frac{d\omega}{dt} = -\frac{g}{L}\sin\theta, \quad \frac{d\theta}{dt} = \omega $$

where $\theta$ is the swing angle and $\omega$ is the angular velocity.

### Energy

$$ E = \frac{1}{2}mL^2\omega^2 + mgL(1 - \cos\theta) $$

In a frictionless system, $E$ should be **conserved forever**. That makes it the best yardstick you have for judging a numerical method.

## Your Task

1. Simulate the pendulum with the **Euler method** and watch how the energy changes over time — it will "drift"
2. Switch to the **Euler–Cromer method (semi-implicit Euler)** and check whether energy is now conserved
3. Plot the $(\theta, \omega)$ phase-space diagram and look at the shape of the trajectory

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

### Checklist after completion

- [ ] The Euler method's phase-space trajectory is an **outward spiral** (energy growing)
- [ ] The Euler–Cromer method's phase-space trajectory is a **closed circle** (energy conserved)
- [ ] Compare the energy-vs-time plots of both methods at the same parameters
- [ ] Answer this: why does the Euler method make the pendulum swing ever higher?

## Hints

<details>
<summary>Expand for hints</summary>

- The key to the Euler–Cromer method: **use the new $\omega$ to update $\theta$**, i.e. $\theta_{n+1} = \theta_n + \omega_{n+1}\Delta t$
- In phase space, a conservative system traces a closed curve; a dissipative one spirals inward
- Try setting the initial angle to $170°$ (almost upside down) and watch the small-angle approximation break down at large angles
- You can normalize the energy units and just look at the relative change $\Delta E / E_0$
</details>

## Next Steps

You've now seen the traps hiding inside numerical methods. Challenge 03 (Orbit) introduces the **leapfrog method** — simple, yet almost magically good at conserving energy — and walks you through verifying Kepler's laws.

→ [Go to Challenge 03: Orbit](../03-orbit/README.en.md)
