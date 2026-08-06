**English** | [**简体中文**](SPEC.md)

# Challenge 06 · Heat Engine — Acceptance Criteria (SPEC)

> This file defines the automated acceptance criteria for Challenge 06. verify.py grades against it.

## Interface

| Function | Signature | Returns |
|------|------|------|
| `simulate_diffusion` | `(T0, alpha=1.0, dx=0.01, dt=5e-5, n_steps=20000)` | `(T_hist, x)`: `T_hist` has shape `(n_steps+1, nx)` |
| `carnot_efficiency` | `(T_hot, T_cold)` | Carnot efficiency `1 - Tc/Th` |
| `engine_efficiency` | `(T_hot, T_cold, r=1.5, gamma=1.4)` | actual efficiency of the rectangular cycle (`< Carnot`) |

- Physics: 1D heat diffusion `∂T/∂t = α∂²T/∂x²`, explicit FTCS scheme, Dirichlet fixed endpoints.
- Stability condition: `r = α·dt/dx² ≤ 1/2`.

## Acceptance Items

### S6.1 Interface
- Returns `(T_hist, x)`, with number of frames = `n_steps + 1`.

### S6.2 Thermal equilibrium: step → linear
- Initial: `x∈[0,1]`, 100 points, `T0 = 1 (x<0.5)`, `0 (x≥0.5)` (left hot, right cold step).
- `α=1, dx=0.01, dt=5e-5, n_steps=20000` (`r=0.5`).
- **Acceptance**: the final temperature profile's maximum deviation from the linear steady state `1 - x/L` is `< 0.05`. (The 1D steady-state solution is linear.)

### S6.3 Direction of heat flow (second law)
- Same simulation.
- **Acceptance**: at all times the temperature is monotonically non-increasing along x (maximum overshoot `≤ 1e-6`) — heat always flows from hot to cold.

### S6.4 Explicit scheme stability
- `dt=1e-4` → `r = 1 > 1/2`, run 500 steps.
- **Acceptance**: `max|T| > 2` (violating the stability condition → numerical divergence).

### S6.5 Engine efficiency ≤ Carnot efficiency
- `carnot_efficiency(600, 300)` must equal exactly `0.5` (`1 - 300/600`).
- `engine_efficiency(600, 300)` (rectangular cycle, non-Carnot) must satisfy `0 < η_engine < η_carnot`.

## Design Notes

- **Step → linear is visible evidence of the second law**: rather than an animation of "heat flowing backward," the monotonicity criterion directly proves the direction of heat flow.
- **Exact Carnot-efficiency criterion**: the upper bound on engine efficiency is a quantitative expression of the second law of thermodynamics; `1 - Tc/Th` must be exact, with no approximation allowed.
- **Rectangular cycle vs. Carnot cycle**: comparing two genuinely computable cycles turns "real engines fall below the theoretical limit" into a measurable number rather than a slogan.
