**English** | [**简体中文**](SPEC.md)

# Challenge 04 · N-Body — Acceptance Criteria (SPEC)

> This file defines the automated acceptance criteria for Challenge 04. verify.py grades against it.

## Interface

| Function | Signature | Returns |
|------|------|------|
| `accelerations` | `(positions, masses, G=1.0, soft=1e-3)` | `(N,2)` accelerations |
| `simulate` | `(positions, velocities, masses, dt, n_steps, G=1.0, soft=1e-3)` | `(pos_hist, vel_hist)`, shape `(n_steps+1, N, 2)` |
| `total_energy` | `(pos_hist, vel_hist, masses, G=1.0, soft=1e-3)` | `(n_steps+1,)` energy sequence |
| `center_of_mass` | `(pos_hist, masses)` | `(n_steps+1, 2)` COM sequence |

- Physical units: `G = 1` natural units, distance is dimensionless.
- Integrator: leapfrog method (Velocity Verlet, symplectic integrator).
- Softening parameter `soft` prevents the force from diverging when two particles get very close; the pure two-body circular-orbit test uses `soft=0.0`.

## Acceptance Items

### S4.1 Interface
- `simulate` returns frames = `n_steps + 1`.

### S4.2 Symmetric two-body · energy conservation
- Initial conditions: two masses `m=1` at `(-0.5,0)` and `(0.5,0)`, velocities `(0,√0.5)` and `(0,-√0.5)` (circular orbit).
- Simulate 4000 steps, `dt=0.001`.
- **Acceptance**: total energy relative drift `< 0.5%`. (The leapfrog method should produce bounded oscillation, not linear drift.)

### S4.3 Center-of-mass conservation (momentum conservation)
- Same symmetric two-body system.
- **Acceptance**: COM position drift throughout `|ΔCOM| < 1e-6`. (No external force → COM moves uniformly; with symmetric initial conditions the COM is at rest.)

### S4.4 Orbit stable (no divergence)
- Same system.
- **Acceptance**: each particle's radius from the COM stays between `0.45 ~ 0.55` (circular orbit neither diverges nor collapses).

### S4.5 Three-body · no divergence
- Random initial conditions (seed=7), `dt=0.01`, 800 steps, `soft=0.05`.
- **Acceptance**: after simulation, the maximum radius of all particles `< 20`. (A chaotic system may produce chaotic orbits, but it should not go numerically unstable.)

## Design Notes

- **Why measure energy conservation with a symmetric two-body system**: symmetric initial conditions keep the COM fixed at the origin, avoiding the COM drift introduced by the "planet orbiting a heavy mass" approximation, making the energy criterion cleaner.
- **Use relative drift rather than absolute energy**: the leapfrog method's energy error is a **bounded oscillation**; directly comparing the first and last frames can mix in phase. A relative drift `< 0.5%` is enough to prove the symplectic integrator is correct.
- **Softening parameter**: `soft > 0` slightly modifies the potential formula (systematic error). A pure two-body circular orbit never approaches `r→0`, so the test uses `soft=0.0` to ensure exactness.
