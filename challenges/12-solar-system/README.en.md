**English** | [**简体中文**](README.md)

# Challenge 12 · Solar System

> **Capstone project: assemble every tool from the previous 11 challenges into one solar system.**

> Capstone challenge: every tool from Challenges 01–11. AI is your co-pilot.
> 🎓 AI tutor available: [ai/tutor.en.md](ai/tutor.en.md)

## Why This Challenge

This is the **capstone design** of the entire repository. You won't use off-the-shelf astronomy software — instead, you'll build a working solar system from scratch, using the integrators, forces, and fields you wrote yourself in Challenges 01–11.

## Physics Background

### Every tool you'll use

| Source challenge | Tool | Used here for |
|------------------|------|---------------|
| 03 | Leapfrog method / symplectic integrator | planetary orbit integration |
| 04 | N-body direct summation | planet–planet interaction (not just sun–planet two-body) |
| 08 | Numerical-stability experience | long-term stable simulation of high mass-ratio systems |
| 06 | Energy monitoring | system energy-conservation check |
| 10 | Relativistic correction (advanced) | Mercury's perihelion precession (general-relativistic effect) |

### Mercury's Perihelion Precession (advanced easter egg)

Classical Newtonian mechanics cannot explain the precession of Mercury's perihelion (about 574 arcseconds per century, of which 43 arcseconds cannot be accounted for by Newtonian mechanics). Einstein's general-relativity correction term:

$$ \vec{a}_{GR} = \frac{GM}{c^2 r^3}\left(4\frac{GM}{r} - v^2\right)\vec{r} $$

Adding this term makes Mercury's perihelion precession match the observed value — one of the most famous verifications in the history of physics.

## Your Task

1. Simulate the Sun + the eight planets (with real initial conditions: orbital radius, velocity, mass)
2. Integrate with the leapfrog method for at least 10 Earth years
3. Verify: stable orbits, energy conservation, periods consistent with Kepler's third law
4. Visualize: a dynamic solar system (advancing in time)
5. (Advanced) Add the general-relativity correction for Mercury's perihelion precession; compare the precession angle with and without the correction

### Checklist after completion

- [ ] The eight planets keep stable orbits over 10 Earth years (no planet escapes / crashes into the Sun)
- [ ] Total system energy drift $< 1\%$
- [ ] Each planet's orbital period matches Kepler's third law (error $< 2\%$)
- [ ] (Advanced) Mercury's perihelion precession ≈ 43 arcseconds/century (after the general-relativity correction)
- [ ] Comparing $\Delta t = 0.1$ days and $\Delta t = 0.01$ days gives consistent results (convergence)

## Hints (collapsible)

<details>
<summary>Click to reveal hints</summary>

- Real data: NASA JPL HORIZONS system lets you download planetary initial states
- Unit system: use AU (distance), year (time), solar mass (mass) so that the numbers stay in a reasonable range
- Planet masses are 5–6 orders of magnitude smaller than the Sun — double precision is fine, but avoid single precision
- Long simulations (100 years+) need a smaller time step or a higher-order integrator
- Advanced: add the Moon's orbit around Earth and observe the center-of-mass motion of the Earth–Moon system
</details>

## 🎉 Done!

Congratulations — through 12 challenges you've rebuilt the edifice of physics, from classical mechanics to quantum mechanics, with your own hands. You now possess:

- **A numerical-physics toolbox of your own** (Euler method → RK4 → leapfrog → FDTD → LBM → split-operator)
- **Cross-domain intuition** (from particles to fields, from determinism to chaos, from classical to quantum)
- **The foundational confidence of "I can do it, so I understand it"**

### What can you do next?

- Submit your solution as a PR to help those who come after you
- Use the tools you've learned to solve a real problem (research, engineering, astronomy hobby)
- Try a new challenge: see [community/ideas.md](../community/ideas.md)
- Share your work with the community at [study-groups.md](../community/study-groups.md)

**Master physics by recreating it from scratch.**
