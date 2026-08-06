**English** | [**简体中文**](README.md)

# Challenge 09 · Electromagnetism

> **The code dance of Maxwell's equations: launch an electromagnetic wave.**

> Prerequisites: array operations + experience from Challenge 05.
> 🎓 AI tutor available: [ai/tutor.en.md](ai/tutor.en.md)

## Why This Challenge

Maxwell's equations are one of the crown jewels of physics. With the **FDTD (Finite-Difference Time-Domain)** method, you can solve them directly on a lattice and watch the electric and magnetic fields excite each other and propagate at the speed of light — an electromagnetic wave is born from your own code.

## Physics Background

### 1D Maxwell's Equations (source-free)

$$ \frac{\partial E_x}{\partial t} = -\frac{1}{\epsilon_0}\frac{\partial H_y}{\partial z}, \quad \frac{\partial H_y}{\partial t} = -\frac{1}{\mu_0}\frac{\partial E_x}{\partial z} $$

### Staggered Grid (Yee Grid)

The essence of FDTD: $E$ and $H$ are **spatially staggered by half a lattice cell** and **temporally staggered by half a time step**:

```
E field at integer lattice sites, integer time
H field at half cells, half time
```

This staggering makes the difference scheme inherently stable and satisfies $c = 1/\sqrt{\epsilon_0\mu_0}$.

## Your Task

1. Implement 1D FDTD (Yee grid)
2. Inject a Gaussian pulse (or sine wave) at the boundary and watch it propagate at the speed of light
3. Observe **impedance matching**: when the pulse crosses a medium with a different permittivity, part reflects and part transmits
4. (Advanced) 2D FDTD: simulate the circular wavefront spreading from a point source
5. (Challenge) Simulate total reflection at a **metal boundary** and observe the standing wave

### Checklist after completion

- [ ] The Gaussian pulse propagates at speed $c = 3\times10^8$ m/s
- [ ] The reflection coefficient $R$ at the medium interface matches the theoretical value $\left(\frac{Z_1 - Z_2}{Z_1 + Z_2}\right)^2$
- [ ] The waveform does not deform as it propagates (no dissipation, no dispersion)
- [ ] Numerical blow-up when the CFL condition $c\Delta t / \Delta z \le 1$ is violated

## Hints

<details>
<summary>Expand for hints</summary>

- Yee grid update formulas (1D):
  - $E_x^{n+1}(k) = E_x^n(k) - \frac{\Delta t}{\epsilon_0 \Delta z}(H_y^{n+1/2}(k+1/2) - H_y^{n+1/2}(k-1/2))$
  - $H_y^{n+1/2}(k+1/2) = H_y^{n-1/2}(k+1/2) - \frac{\Delta t}{\mu_0 \Delta z}(E_x^n(k+1) - E_x^n(k))$
- Use `numpy.roll` for spatial differences — fast and clean
- Absorbing boundary: a simple ABC (first-order Mur), or PML for the advanced case
- In the wave equation, both $c$ and $Z$ follow from $\epsilon, \mu$: $c = 1/\sqrt{\epsilon\mu}$, $Z = \sqrt{\mu/\epsilon}$
</details>

## Next Steps

After Newtonian mechanics comes Einstein. Challenge 10 directly manipulates spacetime with the **Lorentz transformation**, letting you witness length contraction, time dilation, and the invariance of the speed of light.

→ [Go to Challenge 10: Relativity](../10-relativity/README.en.md)
