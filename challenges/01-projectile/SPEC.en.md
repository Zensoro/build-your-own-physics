**English** | [**简体中文**](SPEC.md)

# SPEC 01 · Projectile Motion

> The acceptance criteria in this file can be checked automatically. Your implementation must pass all of them.

## Acceptance Criteria

### S1.1 Trajectory Shape

- [ ] Simulate a projectile launched from the origin; the trajectory stays within the region `y >= 0`
- [ ] The trajectory is a parabola (fit `y(x)` with a quadratic polynomial, $R^2 > 0.99$)

### S1.2 Range Accuracy

- [ ] Using the Euler method with $\Delta t = 0.001$ s, $v_0 = 50$ m/s, $\theta = 45°$:
  - [ ] The simulated range differs from the theoretical value $R = v_0^2 \sin(2\theta)/g \approx 254.8$ m by a relative error $< 2\%$
- [ ] When $\Delta t$ is halved, the error decreases monotonically (convergence check)

### S1.3 Peak Height Accuracy

- [ ] The simulated peak height differs from the theoretical value $H = v_0^2 \sin^2\theta/(2g) \approx 63.7$ m by a relative error $< 2\%$

### S1.4 Input / Output Interface

- [ ] Provide a `simulate(v0, theta_deg, dt, t_max)` interface that returns `(times, xs, ys)`
- [ ] Stop the simulation automatically once `y < 0` (it stops on landing)

## Test Data

| Parameter | Value |
|------|-----|
| $v_0$ | 50 m/s |
| $\theta$ | 45° |
| $\Delta t$ | 0.001 s |
| $t_{max}$ | 10 s |

## Reference Solution

The reference implementation lives on the `solutions` branch: `challenges/01-projectile/solutions/projectile.py`

---

*These acceptance criteria are based on the idealized projectile model without air resistance.*
