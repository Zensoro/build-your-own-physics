**English** | [**简体中文**](SPEC.md)

# Challenge 12 · Solar System — Acceptance Criteria (SPEC)

> This file defines the automated acceptance criteria for Challenge 12 (capstone project). It is graded by `verify.py`.

## Interface

| Function | Signature | Returns |
|----------|-----------|---------|
| `initial_state` | `()` | `(positions, velocities, masses)`, each containing 9 bodies (Sun + 8 planets) |
| `simulate_solar` | `(dt=0.001, years=10.0, soft=1e-6)` | `(pos_hist, vel_hist, masses)` |
| `total_energy` | `(pos_hist, vel_hist, masses, soft=1e-6)` | energy sequence |
| `orbital_period` | `(xs, ys, dt)` | orbital period (interpolated time at which the angle accumulates 2π) |

- Units: AU-year system, `GM_☉ = 4π²` (Earth's period comes out to exactly 1 year).
- Planet data are in the `PLANETS` table (real semi-major axes / masses, with circular-orbit initial angles staggered).
- Integrator: leapfrog method (Velocity Verlet) — the tool from Challenge 03; N-body direct summation — the tool from Challenge 04.

## Acceptance Items

### S12.1 Interface
- `simulate_solar(dt=0.001, years=1)` returns `(pos_hist, vel_hist)` of shape `(1001, 9, 2)`, with `masses[0] = 1` (the Sun).

### S12.2 Stable Orbits (10 years)
- **Acceptance**: the distance from each of the 8 planets to the Sun always stays within `(0.1, 40)` AU — no escape, no crashing into the Sun. (Mercury's perihelion ~0.35 AU, Neptune ~30 AU.)

### S12.3 Energy Conservation
- **Acceptance**: relative total-energy drift over 10 years `< 1%` (leapfrog symplectic integrator).

### S12.4 Kepler's Third Law
- Measure the orbital period T for the **inner planets** (Mercury, Venus, Earth, Mars — all with periods < 10 years, so they complete a full orbit within the simulation window).
- **Acceptance**: `T²/a³ ≈ 1` (error `< 2%`) — Kepler's third law is automatically satisfied by your simulation.
- Note: the outer planets (Jupiter 11.9 yr, Neptune 165 yr) have periods far exceeding the 10-year window and don't complete a full orbit, so they're outside this acceptance scope (you can extend the simulation to verify them yourself).

### S12.5 Convergence
- Earth over 1 year, `dt=0.001` vs `dt=0.0005`.
- **Acceptance**: endpoint position difference `< 0.05 AU` (halving dt gives consistent results).

## Design Notes

- **Why a capstone project**: it strings together Challenges 03 (leapfrog integrator), 04 (N-body summation), 06 (energy monitoring), and 10 (unit systems and geometric intuition), and each acceptance item corresponds to a skill learned in a previous challenge.
- **Circular-orbit initial values + Kepler verification**: using the real semi-major axis to compute the circular-orbit speed, the simulation automatically runs near-circular orbits; Kepler's third law `T²/a³=1` becomes a "self-check" for the whole system — any integrator error breaks it immediately.
- **Energy drift on the order of 0.2%**: 10 years, 10,000 leapfrog steps, energy drift ~0.2% — this is the gap between a symplectic integrator and the Euler method (Euler would drift by tens of percent over the same number of steps).
- **Advanced easter egg (outside the SPEC)**: adding the general-relativity correction term yields Mercury's perihelion precession (43″/century) — see the README.
