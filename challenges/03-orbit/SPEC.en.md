**English** | [**简体中文**](SPEC.md)

# SPEC 03 · Orbit

> The acceptance criteria in this document can be checked automatically. Your implementation must pass every one of them.

## Test Environment

- Language: Python 3.8+ (NumPy is recommended but not required)
- Dependencies: standard library (`math`); Matplotlib optional for visualization
- Parameters: $\mu = GM = 1.327 \times 10^{20}$ m³/s² (the Sun); you may work in the AU-year system

## Conventions

This SPEC offers two unit systems — pick whichever you prefer:

**SI units** (intuitive, but the numbers are huge):
- $\mu = 1.327 \times 10^{20}$ m³/s²
- Earth's orbital radius $a = 1.496 \times 10^{11}$ m
- Time step $\Delta t = 3600$ s (1 hour)

**AU-year system** (friendlier numbers, recommended):
- $\mu = 4\pi^2$ AU³/yr² (the convenient form of Kepler's third law)
- Earth's orbital radius $a = 1.0$ AU
- Time step $\Delta t = 0.001$ yr (≈ 8.76 hours)

> Tip: in the AU-year system, Earth's circular orbital speed is exactly $v = 2\pi$ AU/yr.

## Acceptance Criteria

### S3.1 Interface

- [ ] Provide `simulate(mu, x0, y0, vx0, vy0, dt, n_steps)`, returning `(xs, ys)`
- [ ] `xs[0] = x0`, `ys[0] = y0`
- [ ] The returned lists have length `n_steps + 1`

### S3.2 Stable circular orbit (the Earth baseline)

Integrate for one year using Earth's initial conditions ($x_0 = 1.0$ AU, $y_0 = 0$, $v_{x0} = 0$, $v_{y0} = 2\pi$ AU/yr) with $n = 1000$ steps and $\Delta t = 0.001$ yr:

- [ ] The orbital radius stays between $0.95$ and $1.05$ AU (no escape, no crash into the Sun)
- [ ] After one year the planet returns near its starting point: $\sqrt{(x_n - x_0)^2 + (y_n - y_0)^2} < 0.05$ AU (the orbit closes)
- [ ] Constant areal velocity: the areas swept during any two equal-length time intervals differ by < 2% (Kepler's second law)

### S3.3 Elliptical orbit (speed $0.8 v_{circle}$)

Integrate with $v_{y0} = 0.8 \times 2\pi$ AU/yr:

- [ ] The orbit is an ellipse: $\min(r) > 0.3$ AU, $\max(r) < 1.6$ AU, and $\min(r) < \max(r)$
- [ ] The perihelion-to-aphelion ratio matches what energy conservation predicts (error < 10%)

### S3.4 Energy conservation (the leapfrog method's core advantage)

Total energy $E = \frac{1}{2}v^2 - \mu/r$ (unit mass; recover the velocity from positions with the forward difference $v = (x_{n+1} - x_n)/\Delta t$):

- [ ] After $10^4$ steps of the circular orbit, $\frac{|E_n - E_0|}{|E_0|} < 0.1\%$ (a circular orbit stays phase-synchronized, so comparing the first and last values directly is fine)
- [ ] Elliptical orbit ($0.8 v_c$): the energy **oscillates within a bounded amplitude** — run it for 1 year and for 5 years and $\frac{\max(E) - \min(E)}{|E_0|}$ should be essentially the same (growth < 0.5×)

> Note: this is the dividing line between the leapfrog method (a symplectic integrator) and the Euler method.
> A **symplectic integrator**'s energy error is a **bounded oscillation** (it doesn't grow with time); the Euler method's error **drifts linearly** (the longer you run, the further off you get).
> An elliptical orbit's period doesn't line up with the simulation length, so comparing the first and last values mixes in phase oscillation — which is why the correct criterion is "the oscillation is bounded."
> How to check: simulate 1 year and 5 years and compare the oscillation amplitude — a symplectic integrator keeps it unchanged, while the Euler method doubles it.

### S3.5 Kepler's third law (advanced)

- [ ] Simulate 3 different orbital radii (e.g. $a = 0.7, 1.0, 1.5$ AU), measure the period $T$, and verify that $T^2 / a^3$ is constant (deviation < 2%)
- [ ] (Optional) Plot $\log T$ vs $\log a$; the slope should be $3/2$

### S3.6 Escape velocity (an intuition check)

- [ ] With $v_{y0} = \sqrt{2} \times v_{circle}$, the orbit **does not close**: after one year $r > 2$ AU and still growing
- [ ] With $v_{y0} = 1.5 \times v_{circle}$, the planet clearly escapes ($r$ increases monotonically)

## Test Data Summary

| Scenario | $x_0$ (AU) | $y_0$ (AU) | $v_{x0}$ (AU/yr) | $v_{y0}$ (AU/yr) | Expected |
|------|-----------|-----------|-----------------|-----------------|------|
| Circular orbit | 1.0 | 0 | 0 | $2\pi$ | closed circle |
| Ellipse | 1.0 | 0 | 0 | $0.8 \times 2\pi$ | ellipse |
| Parabola | 1.0 | 0 | 0 | $\sqrt{2} \times 2\pi$ | escape |
| Hyperbola | 1.0 | 0 | 0 | $1.5 \times 2\pi$ | faster escape |

## Reference Solution

The reference implementation lives on the `solutions` branch: `challenges/03-orbit/solutions/orbit_solution.py`

---

*These acceptance criteria are based on the two-body problem with a fixed Sun. The energy-conserving property of the leapfrog method is the foundation for the later challenges in this repository (04 N-Body, 12 Solar System).*
