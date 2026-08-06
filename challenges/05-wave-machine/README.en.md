**English** | [**简体中文**](README.md)

# Challenge 05 · Wave Machine

> **Let waves run across the lattice: from the wave equation to standing waves and interference.**

> Prerequisites: array operations (NumPy) + experience from Challenge 04.
> 🎓 AI tutor available: [ai/tutor.en.md](ai/tutor.en.md)

## Why This Challenge

Waves are everywhere — sound, light, water, earthquakes. Starting from the **wave equation**, you'll simulate the real propagation of waves on a lattice, and watch standing waves, interference, and boundary reflection with your own eyes.

## Physics Background

### One-dimensional wave equation

$$ \frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2} $$

where $u(x,t)$ is the displacement and $c$ is the wave speed.

### Discretization (FTCS scheme)

Discretize space into lattice points $x_i = i \Delta x$ and time into $t_n = n \Delta t$:

$$ u_i^{n+1} = 2u_i^n - u_i^{n-1} + \left(\frac{c\Delta t}{\Delta x}\right)^2 (u_{i+1}^n - 2u_i^n + u_{i-1}^n) $$

This scheme is called the **leapfrog scheme (leapfrog in time)**. The stability condition is $c\Delta t / \Delta x \le 1$ (the CFL condition).

## Your Task

1. Implement a 1-D wave equation simulation (FTCS scheme)
2. Give it a Gaussian wave packet as the initial condition, and watch it spread to both sides
3. Observe **boundary reflection** (fixed end vs. free end)
4. (Advanced) Double-slit interference: the interference pattern produced by two wave sources

### Checklist after completion

- [ ] The Gaussian wave packet splits into two wave packets, traveling left and right
- [ ] Wave speed = $c$ (measure peak travel distance / time)
- [ ] Reflection at a fixed end shows **phase reversal**; at a free end, **phase is unchanged**
- [ ] Changing $\Delta t$, when $c\Delta t/\Delta x > 1$ the simulation blows up numerically (verifying the CFL condition)

## Hints

<details>
<summary>Expand for hints</summary>

- You need two time layers $u^{n-1}$ and $u^n$ to advance to $u^{n+1}$
- Boundary handling: fixed end $u=0$, free end $\partial u/\partial x = 0$
- Use matshow / imshow with `vmin=-1, vmax=1` to fix the color range, making it easier to observe
- Energy = $\sum (\partial u/\partial t)^2 + c^2(\partial u/\partial x)^2$ should be roughly conserved
</details>

## Next Steps

The wave equation is your first encounter with a "field." Challenge 06 turns to thermodynamics — but you'll find that the heat diffusion equation and the wave equation look like close siblings.

→ [Go to Challenge 06: Heat Engine](../06-heat-engine/README.en.md)
