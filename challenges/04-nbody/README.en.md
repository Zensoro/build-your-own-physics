**English** | [**简体中文**](README.md)

# Challenge 04 · N-Body

> **Gravity belongs to everyone: the art of simulating the many-body problem.**

> Prerequisites: experience from Challenge 03 + vector addition (see the Math Refresher).
> 🎓 AI tutor available: [ai/tutor.en.md](ai/tutor.en.md)

## Why This Challenge

The two-body problem has an analytical solution. The three-body problem and beyond — the **many-body problem** — does not. You'll need numerical methods to simulate any number of mutually attracting particles. This is the shared foundation of galaxy evolution, satellite formation flying, and molecular dynamics.

## Physics Background

### Equation of Motion

Each particle $i$ feels the gravitational pull of every other particle:

$$ \vec{a}_i = \sum_{j \neq i} \frac{G m_j}{r_{ij}^3}(\vec{r}_j - \vec{r}_i) $$

### The Complexity Problem

Direct summation is $O(N^2)$. For $N = 10^4$ particles that's $10^8$ operations per step. The **Barnes-Hut algorithm** uses a spatial octree to treat a distant group of particles as a single "super-particle," bringing the complexity down to $O(N \log N)$.

## Your Task

1. Implement a **direct-summation** N-Body simulation ($N$ from 2 to 1000)
2. Measure per-step cost at different $N$, and verify the $O(N^2)$ scaling
3. (Advanced) Implement the Barnes-Hut algorithm, and compare the speedup at $N = 10^4$
4. Visualization: simulate a rotating disk / globular cluster

### Checklist after completion

- [ ] Two-body system: stable orbit, energy conserved ($< 0.1\%$ drift)
- [ ] Three-body system with random initial conditions: chaotic but not diverging
- [ ] Center of mass position conserved (linear momentum conserved)
- [ ] Direct-summation cost grows roughly quadratically with $N$

## Hints

<details>
<summary>Expand for hints</summary>

- First validate your integrator on the two-body case, then scale up to many bodies
- Use vectorization (NumPy) instead of Python loops — 100× faster
- Barnes-Hut: a tree node's center of mass + total mass represents the whole subtree
- Gravitational softening parameter $\epsilon$ prevents the force from blowing up as $r \to 0$: $r_{eff}^2 = r^2 + \epsilon^2$
</details>

## Next Steps

From particles to continuous media. Challenge 05 uses the **wave equation** to simulate how waves propagate through a medium — your first taste of "field" code.

→ [Go to Challenge 05: Wave Machine](../05-wave-machine/README.en.md)
