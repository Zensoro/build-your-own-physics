**English** | [**简体中文**](README.md)

# Challenge 11 · Quantum

> **The wave function is real: solve the Schrödinger equation.**

> Requires: complex-number basics (you can treat them as a black box) + experience from Challenge 05.
> 🎓 AI tutor available: [ai/tutor.en.md](ai/tutor.en.md)

## Why This Challenge

Quantum mechanics is counterintuitive, but its core equation — the **time-dependent Schrödinger equation** — is a partial differential equation you can solve numerically with high precision. You'll watch the wave function interfere, tunnel, and "collapse" upon measurement (if you build a measurement simulation).

## Physics Background

### Time-Dependent Schrödinger Equation (1D)

$$ i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2} + V(x)\psi $$

where $\psi(x,t)$ is a complex-valued wave function, and $|\psi|^2$ is the probability density.

### Split-Operator Method

Because $\hat{T}$ (kinetic energy) and $\hat{V}$ (potential energy) are diagonal operators in momentum space and position space respectively:

1. Half a time step: apply $e^{-iV\Delta t/2\hbar}$ in position space
2. A full time step: apply $e^{-i\hat{T}\Delta t/\hbar}$ in momentum space (switching back and forth with FFT)
3. Half a time step: apply $e^{-iV\Delta t/2\hbar}$ again

$$ \psi(t + \Delta t) \approx e^{-iV\Delta t/2\hbar} e^{-i\hat{T}\Delta t/\hbar} e^{-iV\Delta t/2\hbar}\psi(t) $$

This method has accuracy $O(\Delta t^3)$ and **automatically preserves** $\int|\psi|^2 dx = 1$ (probability conservation).

### Quantum Tunneling

When a particle's energy $E < V_0$ (the barrier height), classical physics says it can't get through — but quantum mechanics says it **might**. The tunneling probability decays exponentially with barrier width.

## Your Task

1. Implement the split-operator method to solve the 1D time-dependent Schrödinger equation
2. Simulate a Gaussian wave packet propagating in free space — observe it **spreading** (positional uncertainty grows)
3. Simulate a wave packet hitting a **square barrier**: observe the transmitted wave + reflected wave (tunneling!)
4. Verify probability conservation: $\int|\psi|^2 dx = 1$ always holds
5. (Advanced) Bound states in a finite square well: start from a guessed wave function and watch it evolve into an energy eigenstate

### Checklist after completion

- [ ] Free wave-packet width grows with time ($\Delta x \propto t$ asymptotically)
- [ ] After crossing the barrier, transmission probability decays exponentially with barrier width/height
- [ ] $\int|\psi|^2 dx$ stays within 1 ± 0.001 after 10,000 steps
- [ ] Energy expectation $\langle E \rangle$ is conserved
- [ ] The wave function is continuous at the barrier (boundary condition satisfied automatically)

## Hints (collapsible)

<details>
<summary>Click to reveal hints</summary>

- Use FFT (`numpy.fft.fft` / `ifft`) to switch between position and momentum space
- Kinetic-energy operator in momentum space: $\hat{T} \to \hbar^2 k^2 / 2m$
- Wave-packet initial condition: $\psi(x,0) = (2\pi\sigma^2)^{-1/4} e^{ik_0 x} e^{-(x-x_0)^2/4\sigma^2}$
- Barrier: $V(x) = V_0$ for $x \in [a,b]$, else 0
- Plot the evolution of $|\psi|^2$ (matplotlib animation or imshow)
- Units: use natural units $\hbar = 1, m = 1$ for friendlier numbers
</details>

## Next Steps

You've now completed all the core simulations, from classical to quantum. Challenge 12 combines every tool into one: **build a solar system from scratch**.

→ [Go to Challenge 12: Solar System](../12-solar-system/README.en.md)
