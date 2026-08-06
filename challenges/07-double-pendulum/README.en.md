**English** | [**简体中文**](README.md)

# Challenge 07 · Double Pendulum

> **The unpredictability of deterministic systems: welcome to chaos.**

> Prerequisites: experience from Challenge 02 + intuition for calculus (math supply station). Differential equations can be derived with AI's help.
> 🎓 AI tutor available: [ai/tutor.en.md](ai/tutor.en.md)

## Why This Challenge

The double pendulum has only 4 state variables, and its equations of motion are completely determined — yet its trajectory is **unpredictable**. This is the entry point to chaos theory, and your first serious use of **RK4** (Runge–Kutta).

## Physics Background

### Equations of motion (Lagrangian mechanics)

The double pendulum's equations of motion can be written as a $4 \times 4$ first-order ODE system. Derive them with Lagrangian mechanics (this is your first time "starting from energy"):

$$ L = T - V $$

Applying the Euler–Lagrange equations gives two coupled second-order equations; reducing their order yields four first-order equations.

### RK4 (classic fourth-order Runge–Kutta)

For $\frac{dy}{dt} = f(t, y)$, RK4 takes a weighted average of four slopes:

$$ y_{n+1} = y_n + \frac{\Delta t}{6}(k_1 + 2k_2 + 2k_3 + k_4) $$

Its accuracy is a **fourth-power** improvement over a second-order method (global error $O(\Delta t^4)$).

### Key signature of chaos: the Lyapunov exponent

Two nearly identical initial conditions have a trajectory separation $d(t)$ that grows exponentially:

$$ d(t) \approx d_0 e^{\lambda t} $$

$\lambda > 0$ indicates a chaotic system.

## Your Task

1. Derive the double pendulum's equations of motion (using Lagrangian mechanics).
2. Implement an RK4 solver.
3. Simulate the double pendulum and plot the trajectories of both arms.
4. (Advanced) Compute the Lyapunov exponent: run two simulations whose initial conditions differ by $10^{-8}$, plot $\log d(t)$ vs $t$, and measure the slope.

### Checklist after completion

- [ ] Small-angle initial condition: motion close to the two normal modes (predictable).
- [ ] Large-angle initial condition: trajectory clearly chaotic (unpredictable).
- [ ] Energy conservation (RK4's error is tiny over short simulations).
- [ ] Lyapunov exponent $\lambda > 0$ (quantitative evidence of chaos).
- [ ] Compare the trajectory difference between the Euler method and RK4 at the same parameters.

## Hints

<details>
<summary>Show hints</summary>

- Deriving the double pendulum equations is tedious, but every step builds physical intuition — don't skip them.
- Numerically, write the equations as a `dydt(y, t)` function, and RK4 becomes generic code.
- Lyapunov exponent: do a linear fit over the part with $t > t_{transient}$.
- Trajectory plotting: draw the tip of the arm over 10,000 steps; a chaotic system fills the space "messily."
- Reference: the small oscillations chapter of Landau's *Mechanics*, or Feynman Lectures Vol. I Ch. 9.
</details>

## Next Steps

Move from point masses to continuum media. Challenge 08 simulates fluids with the **Lattice Boltzmann Method** — a modern numerical approach to fluid mechanics.

→ [Go to Challenge 08: Fluid](../08-fluid/README.en.md)
