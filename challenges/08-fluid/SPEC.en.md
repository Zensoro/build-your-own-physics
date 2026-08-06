**English** | [**简体中文**](SPEC.md)

# Challenge 08 · Fluid — Acceptance Criteria (SPEC)

> This file defines the automated acceptance criteria for Challenge 08. verify.py grades against it.

## Interface

| Function | Signature | Returns |
|------|------|------|
| `equilibrium` | `(i, rho, ux, uy)` | equilibrium distribution scalar/array for direction i |
| `simulate_lid_driven` | `(nx=32, ny=32, tau=0.6, U_wall=0.1, n_steps=5000, rho0=1.0)` | `(rho, ux, uy)`, each of shape `(ny, nx)` |

- Physics: D2Q9 Lattice Boltzmann. Collision relaxation time `τ` (viscosity `ν = (τ-1/2)/3`), lid velocity `U_wall`.
- Macroscopic quantities: `ρ = Σf_i`, `ρu = Σf_i·c_i`.

## Acceptance Items

### S8.1 Interface
- Returns `(rho, ux, uy)`, each of shape `(32, 32)`.

### S8.2 Mass Conservation
- `Σρ` deviates from the initial `nx·ny = 1024` by `< 2%`.

### S8.3 Central Primary Vortex
- The lid drags to the right → the fluid recirculates at the center. **Acceptance**: `ux(center) < 0`.

### S8.4 Lid Velocity
- **Acceptance**: the average `ux` along the lid row `> 0.8·U_wall = 0.08`.

### S8.5 Continuous Velocity Field (no checkerboard oscillation)
- The checkerboard mode is a classic symptom of a broken LBM implementation (an unphysical 2-cell oscillation).
- Detection avoids the boundary layer (where physical gradients are large near the lid): take the interior region `ux[4:-4, 4:-4]`.
- **Acceptance**: the maximum neighbor difference of `ux` in the interior region `< 0.02`.

### S8.6 Two Corner Vortices
- The signature structure of lid-driven cavity flow: a counter-clockwise vortex at the lower-left corner and a clockwise vortex at the lower-right corner.
- **Acceptance**: `uy(lower-left corner) < 0` and `uy(lower-right corner) > 0`.

## Design Notes

- **Why lid-driven cavity flow**: it is the standard benchmark in the LBM literature (Ghia et al.), physically rich (primary vortex + two corner vortices), and implementation errors surface immediately (no vortex, checkerboard oscillation).
- **bounce-back boundaries are provided**: boundary handling is the most error-prone part of LBM; the focus of this challenge is the two core steps of **collision + streaming**. The boundary code is given directly, so learners can focus on understanding LBM's "relax + shift" idea.
- **S8.5 is the debugging gold standard**: if the collision/streaming implementation is wrong, the most common result is checkerboard oscillation — this criterion lets learners instantly know where their implementation broke.
