**English** | [**简体中文**](SPEC.md)

# Challenge 09 · Electromagnetism — Acceptance Criteria (SPEC)

> This file defines the automated acceptance criteria for Challenge 09. verify.py grades against it.

## Interface

| Function | Signature | Returns |
|------|------|------|
| `fdtd_1d` | `(nz=400, dz=1e-3, dt=None, n_steps=1000, source="gauss", eps_r_profile=None, source_idx=None, f_source=2e9)` | `(ez_hist, hy_hist, z)` |

- Physics: 1D source-free Maxwell's equations (Ez/Hy polarization), Yee staggered grid.
- Stability condition (CFL): `c·Δt/Δz ≤ 1`, default `0.95`.
- Constants: `C0 = 3e8`, `MU0 = 4πe-7`, `EPS0 = 1/(μ₀c²)`.
- Boundary: first-order Mur absorbing boundary (code provided, suppresses boundary reflection).

## Acceptance Items

### S9.1 Interface
- Returns `(ez_hist, hy_hist, z)`, with shapes matching `(n_steps, nz)`.

### S9.2 Vacuum wave speed = c
- The Gaussian pulse peak moves over time.
- **Acceptance**: the measured wave speed deviates from `c` by `< 2%`. (`v = Δz_peak / (Δt_steps·dt)`)

### S9.3 Medium Interface · Reflection present + phase reversal
- Interface: `εr = 4` for `z ≥ 1.2 m`, vacuum elsewhere. Source at `z = 0.3 m`.
- Observe at `z = 1.0 m` on the left side of the interface: the incident pulse and the interface-reflected pulse are **separated in time**.
- **Acceptance 1 (reflection present)**: energy in the reflection time window `> 3×` the no-interface baseline (same window, to guarantee a real reflection).
- **Acceptance 2 (phase reversal)**: the reflected main peak `< 0`.
  - Physical basis: `Z = √(μ/ε)`, increasing ε → Z decreases → reflection coefficient `(Z₁-Z₂)/(Z₁+Z₂) < 0` → reflected wave phase reversal. This is the core EM conclusion that "reflection from high to low impedance reverses."

### S9.4 Wave speed in medium = c/√εr
- Arrival time of the transmitted wave at `z = 1.4 m` (200 cells past the interface).
- **Acceptance**: the measured wave speed deviates from `c/2` by `< 12%`. (`√4 = 2`; halving the wave speed is the direct verification of the definition of refractive index.)

### S9.5 CFL Condition
- `dt = 2·dz/c` (CFL=2), simulate 300 steps.
- **Acceptance**: numerical blow-up — `NaN` or `max|Ez| > 10` appears.

## Design Notes

- **Why the Yee grid is "staggered"**: Ez and Hy are each offset by half a cell in space/time, and the difference is center-symmetric → second-order accuracy + naturally satisfies `c = 1/√(εμ)`.
- **Reflectance measured by energy ratio, not amplitude ratio**: FDTD numerical dispersion produces an oscillating tail on the pulse; the energy criterion is more robust than a single-point amplitude.
- **Phase reversal is hard-core physics**: increasing `ε` → impedance drops → reflection reverses — a phenomenon used daily in optics (anti-reflection coatings, reflective coatings). Verifying it in ~20 lines of code is far deeper than memorizing a formula.
- **Pedagogical simplification**: the Mur boundary doesn't absorb completely (residual ~1% reflection), so S9.3 uses a "relative to no-interface baseline" criterion instead of an absolute reflection coefficient — to avoid the acceptance test being disturbed by boundary artifacts.
