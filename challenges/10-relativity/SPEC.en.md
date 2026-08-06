**English** | [**简体中文**](SPEC.md)

# Challenge 10 · Relativity — Acceptance Criteria (SPEC)

> This file defines the automated acceptance criteria for Challenge 10. It is graded by `verify.py`.

## Interface

| Function | Signature | Returns |
|----------|-----------|---------|
| `gamma` | `(v)` | `1/√(1-v²)` |
| `lorentz` | `(event, v)` | transformed 4-tuple |
| `inverse_lorentz` | `(event, v)` | inverse-transformed 4-tuple |
| `spacetime_interval` | `(event_a, event_b)` | `s² = (cΔt)² - Δx² - Δy² - Δz²` |
| `time_dilation` | `(Δτ, v)` | `γ·Δτ` |
| `length_contraction` | `(L0, v)` | `L0/γ` |

- Events are represented as 4-tuples `(ct, x, y, z)`, with $c = 1$ (natural units).
- Velocity `v` is in units of the speed of light (`0 ≤ v < 1`).
- This challenge **does not need numpy** — pure standard library.

## Acceptance Items

### S10.1 γ Factor
- `γ(0.6) = 1.25` (exact); `γ(0) = 1`.

### S10.2 Invariance of the Spacetime Interval
- 1000 random events (with a fixed random seed for reproducibility), random `v ∈ [0, 0.9]`.
- **Acceptance**: `s²` is consistent before and after the Lorentz transformation (error `< 1e-9`).
- This is the deepest insight of special relativity: **the interval is a geometric quantity that does not change with the observer**.

### S10.3 Invariance of the Speed of Light
- Light-signal event `(ct,x) = (3,3)` (i.e. `x = ct`).
- **Acceptance**: for `v ∈ {0.1, 0.5, 0.9}`, after transformation `x'/ct' = 1` (error `< 1e-9`).

### S10.4 Inverse Transformation
- A round trip $S \to S' \to S$ restores the original event (error `< 1e-9`).

### S10.5 Length Contraction and Time Dilation
- `time_dilation(1.0, 0.6) = 1.25` (time dilation — the moving clock runs slower).
- `length_contraction(1.0, 0.6) = 0.8` (length contraction — the moving rod is shorter).

## Design Notes

- **Why (ct, x, y, z) instead of (t, x, y, z)**: with c=1, ct and x share the same units, so the Lorentz transformation becomes a "rotation in spacetime" (the rapidity viewpoint). The geometric meaning is immediately clear, and you avoid the pitfalls of unit conversion.
- **Why pure standard library**: relativity needs no numerical integration — it is a purely algebraic problem. This gives learners a demonstration that "you can do physics without numpy."
- **Interval invariance is the ultimate acceptance test**: other criteria (γ, length contraction, time dilation) can be faked by "memorizing formulas," but "interval invariance for arbitrary random events" can only be passed by truly understanding the structure of the transformation.
