**English** | [**简体中文**](README.md)

# Challenge 06 · Heat Engine

> **From the diffusion equation to the Carnot cycle: a code-based proof of the second law of thermodynamics.**

> Prerequisites: array operations + experience from Challenge 05.
> 🎓 AI tutor available: [ai/tutor.en.md](ai/tutor.en.md)

## Why This Challenge

The heat diffusion equation is another pillar of physical simulation. You'll watch "heat flows from hot to cold" happen naturally on a grid — then upgrade it into a real **heat engine** and run a Carnot cycle.

## Physics Background

### Heat Diffusion Equation

$$ \frac{\partial T}{\partial t} = \alpha \nabla^2 T $$

where $\alpha$ is the thermal diffusivity. This is a **parabolic** equation (the wave equation is hyperbolic), so the numerical scheme and its requirements are completely different.

### Explicit FTCS

$$ T_i^{n+1} = T_i^n + \frac{\alpha \Delta t}{\Delta x^2} (T_{i+1}^n - 2T_i^n + T_{i-1}^n) $$

Stability condition: $\frac{\alpha \Delta t}{\Delta x^2} \le \frac{1}{2}$.

### Heat Engine and the Carnot Cycle

A heat engine operates between a hot reservoir at $T_H$ and a cold reservoir at $T_C$; its maximum efficiency is the Carnot efficiency:

$$ \eta = 1 - \frac{T_C}{T_H} $$

## Your Task

1. Implement a 1D heat diffusion simulation (FTCS scheme).
2. Verify: start from a step temperature profile; over time it smooths into a straight line (thermal equilibrium).
3. Plot the temperature-vs-time evolution and observe the direction of heat flow (a manifestation of the second law).
4. (Advanced) 2D heat diffusion — simulate a "heat source + heat sink" and compute the steady-state temperature field.
5. (Challenge) Simulate a simple heat-engine cycle (isothermal + adiabatic) and measure its efficiency against the Carnot efficiency.

### Checklist after completion

- [ ] Initial step profile → final linear profile (thermal equilibrium)
- [ ] Heat always flows from hot to cold (second law)
- [ ] The explicit scheme becomes numerically unstable when $\alpha\Delta t/\Delta x^2 > 0.5$
- [ ] Engine efficiency ≤ Carnot efficiency

## Hints

<details>
<summary>Show hints</summary>

- Note: the diffusion equation's stability condition is $\alpha\Delta t/\Delta x^2 \le 1/2$, different from the wave's CFL condition.
- After thermal equilibrium the temperature gradient is linear (1D) and satisfies Laplace's equation (2D).
- The implicit scheme (Crank–Nicolson) is unconditionally stable but requires solving a linear system — an advanced challenge.
- For the Carnot cycle, use Boyle's law for the isothermal process and Poisson's relation for the adiabatic process.
</details>

## Next Steps

After thermodynamics, we return to dynamics — but this time, to **chaos**. Challenge 07's double pendulum is the classic demonstration of "unpredictability in a deterministic system."

→ [Go to Challenge 07: Double Pendulum](../07-double-pendulum/README.en.md)
