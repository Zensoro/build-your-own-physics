**English** | [**简体中文**](README.md)

# Challenge 10 · Relativity

> **Program spacetime as a geometric object.**

> Requires: matrix basics + experience from Challenge 03. AI can handle the matrices for you.
> 🎓 AI tutor available: [ai/tutor.en.md](ai/tutor.en.md)

## Why This Challenge

Special relativity is not "weird physics" — it's a **geometry**: time is the fourth dimension, and different observers are simply taking different "slices" of spacetime. By manipulating the Lorentz transformation directly in code, you'll understand length contraction and time dilation far more deeply than by memorizing formulas.

## Physics Background

### Lorentz Transformation

Two inertial frames $S$ and $S'$ (relative velocity $v$ along the $x$-axis):

$$ t' = \gamma(t - vx/c^2), \quad x' = \gamma(x - vt) $$

where $\gamma = 1/\sqrt{1 - v^2/c^2}$.

### The Invariant: Spacetime Interval

$$ s^2 = c^2 t^2 - x^2 - y^2 - z^2 $$

The spacetime interval is **invariant** in every inertial frame — this is the deepest insight of special relativity, and the yardstick by which you verify your code is correct.

### Minkowski Spacetime Diagram

Treat time as one axis and plot it on a 2D plane ($ct$ vs $x$). The light cone divides spacetime into three regions: "timelike" (causally reachable), "lightlike" (at the speed of light), and "spacelike" (causally unreachable).

## Your Task

1. Implement the Lorentz transformation function (both $S \to S'$ and the inverse)
2. Verify **the invariance of the speed of light**: the speed of a light signal is $c$ in both frames
3. Verify **the invariance of the spacetime interval**: for any pair of events, $s^2$ is unchanged before and after the transformation
4. Visualize the **Minkowski spacetime diagram**: draw the worldlines of two observers, the light cone, and the surfaces of simultaneity
5. (Advanced) Simulate concrete numerical scenarios of "length contraction" and "time dilation"

### Checklist after completion

- [ ] $\gamma$ equals 1.25 at $v=0.6c$
- [ ] The spacetime interval is invariant under any Lorentz transformation (error $< 10^{-10}$)
- [ ] Invariance of the speed of light: the speed of light is $c$ in any inertial frame
- [ ] A worldline inside the light cone → timelike; outside the light cone → spacelike
- [ ] The length-contraction and time-dilation values agree with the formulas

## Hints (collapsible)

<details>
<summary>Click to reveal hints</summary>

- Use the 4-tuple $(ct, x, y, z)$ instead of $(t, x, y, z)$ to make the geometry clearer
- The Lorentz transformation can be written in matrix form — a 4×4 matrix multiplying a vector
- Spacetime diagram: the $ct$ axis and the $x$ axis use different unit lengths (one grid cell on the $x$ axis = 1 m, one grid cell on the $ct$ axis = the light-time corresponding to 1 m)
- To verify invariance: randomly generate 1000 event pairs and compare $s^2$ after the transformation
- Advanced: try the rapidity $\eta = \text{atanh}(v/c)$, which turns the Lorentz transformation into a "rotation in spacetime"
</details>

## Next Steps

Relativity turns spacetime into geometry; quantum mechanics turns certainty into probability. Challenge 11 solves the Schrödinger equation and shows you wave-function collapse and quantum tunneling.

→ [Go to Challenge 11: Quantum](../11-quantum/README.en.md)
