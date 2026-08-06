**English** | [**简体中文**](SPEC.md)

# Challenge 07 · Double Pendulum — Acceptance Criteria (SPEC)

> This file defines the automated acceptance criteria for Challenge 07. verify.py grades against it.

## Interface

| Function | Signature | Returns |
|------|------|------|
| `derivs` | `(state, m1=1.0, m2=1.0, L1=1.0, L2=1.0, g=9.81)` | `[ω1, ω2, α1, α2]` |
| `rk4_step` | `(f, y, t, dt)` | y after a single RK4 update |
| `simulate` | `(θ1₀, θ2₀, ω1₀=0, ω2₀=0, dt=0.005, t_max=20, ...)` | `(times, states)`, states shape `(n,4)` |
| `simulate_euler` | same as above | same as above (Euler method, for comparison) |
| `energy` | `(states, ...)` | energy sequence |

- State vector: `[θ1, θ2, ω1, ω2]` (radian units). Defaults `m1=m2=L1=L2=1, g=9.81`.
- The equations of motion are derived via Lagrangian mechanics (see `derivs`); **the core of this challenge is implementing the RK4 integrator**.

## Acceptance Items

### S7.1 Interface
- `simulate` returns `(times, states)`, with `states` of shape `(4001, 4)` (dt=0.005, t_max=20).

### S7.2 Small angles · bounded oscillation
- Initial `θ1=0.1, θ2=0.05` (close to the normal modes).
- **Acceptance**: `max|θ1| < 0.2` (bounded, non-diverging motion), and the number of times θ1 crosses zero is `> 10` (it is indeed oscillating).

### S7.3 RK4 energy conservation
- Same simulation, 20 seconds.
- **Acceptance**: relative total-energy drift `< 0.5%`. (RK4 global error is `O(dt⁴)`, so it should be nearly conserved over the short term.)

### S7.4 Chaos · sensitivity to initial conditions
- Large angles `θ1=θ2=2.0`, two simulations differing in initial θ1 by `1e-8`, run for 6 seconds.
- **Acceptance**: estimated Lyapunov exponent `λ ≈ ln(d(4s)/d(1s)) / 3s > 0.3` — the trajectory separation diverges exponentially (quantitative evidence of chaos).

### S7.5 Euler vs RK4 energy drift
- Same small-angle initial condition, same `dt=0.005`, 20 seconds.
- **Acceptance**: Euler method's energy drift `> 10×` RK4's energy drift. (The cost difference between a first-order vs. a fourth-order method.)

## Design Notes

- **Why give the equations of motion directly**: Lagrangian derivation is the core of a physics course, but the focus of this challenge is "first serious use of RK4." Handing over `derivs` in full lets the learner focus on the integrator — also the top-tier-tutorial practice of "introducing only one new difficulty at a time."
- **The chaos criterion uses doubling rather than fitting λ**: `d(4s)/d(1s) > 30` is more robust and easier to understand than a full linear fit, while still sufficient to prove exponential divergence.
- **The Euler comparison is the reward for "building the wheel"**: the learner sees with their own eyes that, with the same equations and the same time step, RK4 beats Euler by two orders of magnitude.
