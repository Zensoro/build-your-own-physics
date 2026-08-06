**English** | [**简体中文**](README.md)

# Challenge 08 · Fluid

> **Let flow emerge on its own: an introduction to the Lattice Boltzmann Method.**

> Prerequisites: array operations + experience from Challenges 05–06. The algorithm is intricate, but AI can guide you through the whole way.
> 🎓 AI tutor available: [ai/tutor.en.md](ai/tutor.en.md)

## Why This Challenge

Fluids are among the hardest classical systems to simulate — the nonlinear terms in the Navier–Stokes equations make analytic solutions almost nonexistent. Yet the **Lattice Boltzmann Method (LBM)** sidesteps this in a nearly counterintuitive way: instead of tracking fluid particles, it tracks the collision and streaming of the **particle distribution function** on a lattice.

## Physics Background

### The Lattice Boltzmann Equation

$$ f_i(\vec{x} + \vec{c}_i\Delta t, t + \Delta t) = f_i(\vec{x}, t) - \frac{\Delta t}{\tau}(f_i - f_i^{eq}) $$

- $f_i$: the particle distribution function in direction $i$
- $\vec{c}_i$: the lattice velocity (the D2Q9 model has 9 directions)
- $f_i^{eq}$: the equilibrium distribution (depends on the local density and velocity)
- $\tau$: the relaxation time (related to viscosity)

### Recovering the Macroscopic Quantities

Density and velocity are recovered from the first and second moments of the distribution function:

$$ \rho = \sum_i f_i, \quad \rho\vec{u} = \sum_i f_i \vec{c}_i $$

The correctness of LBM lies in this: a Chapman–Enskog expansion of $f_i$ recovers the **incompressible Navier–Stokes equations** at the macroscopic scale.

## Your Task

1. Implement the D2Q9 Lattice Boltzmann Method (LBM)
2. Simulate the **lid-driven cavity flow** — the most classic LBM benchmark
3. Plot the velocity field and watch the central vortex form
4. (Advanced) Simulate flow past a cylinder and watch the Kármán vortex street (vortex shedding)

### Checklist after completion

- [ ] The lid-driven cavity shows a central primary vortex + two corner vortices ($Re \approx 100$)
- [ ] The velocity field is continuous, with no oscillation (no unphysical checkerboard mode)
- [ ] The vortex structure changes with $Re$ in line with the literature
- [ ] (Advanced) For flow past a cylinder, the periodic vortex-street frequency matches the Strouhal number

## Hints

<details>
<summary>Expand for hints</summary>

- The 9 directions of D2Q9: rest (1) + orthogonal (4) + diagonal (4)
- Equilibrium distribution $f_i^{eq} = w_i \rho (1 + 3\vec{c}_i\cdot\vec{u} + \frac{9}{2}(\vec{c}_i\cdot\vec{u})^2 - \frac{3}{2}\vec{u}\cdot\vec{u})$, where $w_i$ is the weight
- The streaming step is a "shifting": move $f_i$ from neighboring lattice sites using index operations
- Reynolds number $Re = U L / \nu$, with viscosity controlled via $\tau$
- Visualization: use quiver for the velocity field and color for the vorticity $\omega = \nabla \times \vec{u}$
</details>

## Next Steps

After fluids comes fields. Challenge 09 solves Maxwell's equations directly with the **FDTD** method, and you'll watch electromagnetic waves radiate from your own code.

→ [Go to Challenge 09: Electromagnetism](../09-electromagnetism/README.en.md)
