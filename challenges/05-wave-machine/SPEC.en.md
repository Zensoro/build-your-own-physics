**English** | [**简体中文**](SPEC.md)

# Challenge 05 · Wave Machine — Acceptance Criteria (SPEC)

> This file defines the automated acceptance criteria for Challenge 05. verify.py grades against it.

## Interface

| Function | Signature | Returns |
|------|------|------|
| `simulate` | `(u0, c=1.0, dx=0.01, dt=0.005, n_steps=2000, bc="fixed")` | `(u_hist, x)`: `u_hist` shape `(n_steps+1, nx)`, `x` shape `(nx,)` |

- Physics: 1-D wave equation `∂²u/∂t² = c²∂²u/∂x²`, leapfrog (FTCS) time scheme.
- Initial velocity is zero (`u¹ = u⁰ + 0.5·C²·∇²u⁰`, `C = c·dt/dx`).
- Boundary: `bc="fixed"` fixed end (`u=0`), `bc="free"` free end (`∂u/∂x=0`).
- Stability condition: `C = c·dt/dx ≤ 1` (CFL).

## Acceptance Items

### S5.1 Interface
- Returns `(u_hist, x)`, frames = `n_steps + 1`, `len(x) = nx`.

### S5.2 Gaussian wave packet splits and propagates
- Initial: a centered Gaussian wave packet (`x0=2.0`, width `0.15`, interval `[0,4]`, 400 points).
- Simulate `dt=0.005, n_steps=150`.
- **Acceptance**: central displacement decays to `< 0.4×` the initial peak (energy split to both sides); both left and right halves show peaks `> 0.3×` the initial peak (split into two wave packets).

### S5.3 Wave speed = c
- Same simulation. The right-going peak should be at `x0 + c·t = 2.75`.
- **Acceptance**: measured right-going peak vs. theoretical value error `< 15%`.

### S5.4 Boundary reflection phase
- Wave packet near the right boundary (`x0=3.4`) travels right for 200 steps, enough to reach the boundary and reflect.
- Fixed end: boundary stays `u=0` throughout; after reflection, the point inside the boundary shows a **negative peak** (phase reversal, `min < -0.1`).
- Free end: boundary satisfies `u[-1]=u[-2]`; after reflection, the point inside the boundary shows **no significant negative value** (in phase, `min > -0.05`).

### S5.5 CFL condition
- `c=1, dx=0.01, dt=0.03` → `C=3 > 1`, simulate 200 steps.
- **Acceptance**: `max|u| > 5` (numerical divergence = the scheme blows up when the stability condition is violated).

## Design Notes

- **Why use the leapfrog scheme**: the wave equation is hyperbolic and needs two time layers; the leapfrog scheme is stable and dispersion-free under the CFL condition.
- **u¹ with zero initial velocity**: use the Taylor expansion `u¹ ≈ u⁰ + 0.5·C²·∇²u⁰` to avoid introducing a separate initial velocity — one fewer pitfall.
- **Phase reversal is physical in essence**: reflection at a fixed end reverses phase (peak becomes trough), a free end is in phase — this is the root of why string instruments and wind instruments sound different, and is the core physical phenomenon of the acceptance test.
