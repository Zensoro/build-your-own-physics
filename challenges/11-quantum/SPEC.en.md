**English** | [**简体中文**](SPEC.md)

# Challenge 11 · Quantum — Acceptance Criteria (SPEC)

> This file defines the automated acceptance criteria for Challenge 11. It is graded by `verify.py`.

## Interface

| Function | Signature | Returns |
|----------|-----------|---------|
| `gaussian_wavepacket` | `(x, x0=0, k0=0, sigma=1)` | normalized complex wave function `(nx,)` |
| `evolve` | `(psi, V, dx, dt, n_steps)` | evolved complex wave function |
| `expectation_energy` | `(psi, V, dx)` | `⟨E⟩` scalar |
| `transmission_probability` | `(psi, x, barrier_right)` | total probability to the right of the barrier |

- Natural units: `ħ = 1, m = 1`. The 1D time-dependent Schrödinger equation is `i∂ψ/∂t = -(1/2)∂²ψ/∂x² + Vψ`.
- Method: split-operator method (second-order symmetric split, accuracy `O(Δt³)`, automatically preserves probability conservation).

## Acceptance Items

### S11.1 Interface
- `evolve` returns a complex array with the same shape as the input.

### S11.2 Probability Conservation
- Evolve a free wave packet for 1000 steps (`dt=0.1`).
- **Acceptance**: the relative deviation of `∫|ψ|²dx` from the initial value is `< 1e-9`. (The hallmark property of the split-operator method.)

### S11.3 Energy Conservation
- Same evolution. **Acceptance**: the relative change in `⟨E⟩` is `< 1e-3`.

### S11.4 Free Wave-Packet Spreading
- Gaussian wave packet (`σ=3, k0=0.5`) evolved freely for 2000 steps.
- **Acceptance**: σ (centered standard deviation) grows by `> 1.2×` (measured at roughly 17×) — the growth of positional uncertainty.

### S11.5 Barrier Tunneling
- Square barrier `V0=1, x∈[10,20]`; wave-packet energy `E ≈ k0²/2 = 0.125 < V0`, evolved for 2000 steps (the packet reaches the barrier region without being disturbed by wraparound from periodic boundaries).
- **Acceptance 1**: transmission probability `> 0.01` (classical physics would give 0 — tunneling happens).
- **Acceptance 2**: transmission with the barrier `<` transmission in the no-barrier control (the barrier does indeed block).

## Design Notes

- **Why the split-operator method**: T and V act in their respective diagonal spaces, so one FFT round trip completes a single time step — this is the ultimate demonstration of "algorithm matching physical structure," and one of the highest accuracy/cost-ratio schemes in numerical methods.
- **Probability conservation is a free lunch**: unitary evolution automatically preserves normalization; the `1e-9` criterion directly tests that "unitarity has not been broken by the numerical method."
- **The dual design of the tunneling criterion**: it must both prove "something classically impossible happened" (transmission > 0) and prove "the barrier really does block" (transmission < no-barrier) — together the two conditions form the complete physical picture.
