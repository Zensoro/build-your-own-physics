**English** | [**简体中文**](SPEC.md)

# SPEC 02 · Pendulum

> The acceptance criteria in this document can be checked automatically. Your implementation must pass every one of them.

## Test Environment

- Language: Python 3.8+
- Dependencies: standard library only (`math`); Matplotlib is optional for visualization
- Default parameters: $L = 1.0$ m, $\theta_0 = 30°$, $\omega_0 = 0$, $\Delta t = 0.01$ s, $t_{max} = 20$ s

## Acceptance Criteria

### S2.1 Interface

- [ ] Provide `simulate_euler(L, theta0, omega0, dt, t_max)`, returning `(times, thetas, omegas)`
- [ ] Provide `simulate_euler_cromer(L, theta0, omega0, dt, t_max)`, returning `(times, thetas, omegas)`
- [ ] The three returned lists have equal length, with `times[0] = 0`, `thetas[0] = theta0`, `omegas[0] = omega0`

### S2.2 Range of motion (small angles)

- [ ] With the default parameters ($\theta_0 = 30°$), `max(thetas) <= theta0 + 0.01` (the swing angle never exceeds the initial amplitude — no divergence)
- [ ] The angle varies periodically in time: there exists $T_{osc} < 5$ s such that $\theta(t + T_{osc}) \approx \theta(t)$ (error < 0.1 rad)

### S2.3 Period approximation (small-angle theory)

- [ ] At small angles ($\theta_0 = 5°$), the measured period $T_{sim}$ is within 2% relative error of the theoretical value $T = 2\pi\sqrt{L/g} \approx 2.007$ s

> Note: this is the core check on **the correctness of your numerical integration** — if your integrator is right, the small-angle period must land close to the theoretical value.

### S2.4 Energy behavior (the essential difference between the two methods)

Let the energy be $E(t) = \frac{1}{2}L^2\omega(t)^2 + gL(1 - \cos\theta(t))$ (unit mass, $m=1$), with $E_0 = E(0)$:

- [ ] **Euler method**: at $t = 20$ s, $\frac{E(20) - E_0}{E_0} > 5\%$ (significant energy drift, usually growth)
- [ ] **Euler–Cromer method**: at $t = 20$ s, $\frac{|E(20) - E_0|}{E_0} < 1\%$ (energy approximately conserved)
- [ ] The Euler method's energy drift points **upward** ($E(20) > E_0$), while the Euler–Cromer method shows no noticeable drift

> Note: these two are the **most important** criteria here — they let you see with your own eyes that "a numerical method can lie about the physics."

### S2.5 Convergence (optional, advanced)

- [ ] Euler method: halving $\Delta t$ roughly halves the angle error at $t = 10$ s (first-order accuracy)
- [ ] Euler–Cromer method: the energy drift shrinks as $\Delta t$ shrinks

## Test Data

| Parameter | Default value |
|------|--------|
| $L$ | 1.0 m |
| $\theta_0$ | 30° (≈ 0.5236 rad) |
| $\omega_0$ | 0 |
| $\Delta t$ | 0.01 s |
| $t_{max}$ | 20 s |

## Reference Solution

The reference implementation lives on the `solutions` branch: `challenges/02-pendulum/solutions/pendulum_solution.py`

---

*These acceptance criteria are based on the frictionless pendulum model. The energy-conservation check is the key to understanding the stability of numerical methods.*
