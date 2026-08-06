# Build Your Own Physics

> **Master physics by recreating it from scratch.**

**简体中文** | [**English**](README.en.md)

---

## Why This Exists

> *"What I cannot create, I do not understand."* — Richard Feynman

Most physics learning stops at "understanding the formula." But *reading* a formula is not *understanding* it. When you build a gravitational orbit, a traveling wave, or a heat-engine cycle from scratch in code, those formulas stop being answers to memorize — they become intuition you walked through step by step.

**This repository guides you through Reconstructive Learning: calculate → derive → simulate → create.**

## 🎯 Zero Prerequisites

**No prior knowledge needed.** Everything is redesigned from the ground up:

| You don't need to know | We'll walk you through |
|-----------------------|------------------------|
| ❌ Programming | ✅ Start from your first `print`, with AI as your co-pilot |
| ❌ Calculus | ✅ Every math concept is explained from *intuition* first; formulas come second |
| ❌ College physics | ✅ Start from "why does an apple fall?" |
| ❌ Environment setup | ✅ Running in your browser within three minutes |

**AI is your personal tutor.** Every challenge ships with ready-to-paste "AI collaboration prompts." Copy them into ChatGPT / Claude / 豆包 (Doubao), and the AI will:
- Explain every line of code you don't understand
- Help you debug
- Give you hints when you're stuck — not the answer
- Quiz you to check your understanding

## How It Works

Every challenge follows the same loop:

```
Read the law (intuition first) → write the code → run it → see the phenomenon → tweak parameters → deeper understanding
```

- Each challenge gives you **the physics law and minimal hints** — never the full answer
- Your job is to write a **run-and-verify simulation from scratch**
- Every challenge ships with **automated acceptance criteria** (numerical errors, physical phenomena that must appear)
- When done, check against the **reference implementation** (`solutions/` directory, or switch to the `solutions` branch to browse them all)

## The Roadmap

From your "first line of physics code" to "a solar system" — 12 challenge levels:

| # | Challenge | Physics topic | Math needed | Difficulty |
|---|-----------|---------------|-------------|------------|
| 00 | [Python Crash Course](challenges/00-python-basics/README.md) | Variables, loops, functions | Basic arithmetic | ★☆☆ |
| 01 | [Projectile Motion](challenges/01-projectile/README.md) | Projectiles, air resistance | Pythagorean theorem | ★☆☆ |
| 02 | [Pendulum](challenges/02-pendulum/README.md) | Simple harmonic motion, phase space | Trigonometry | ★☆☆ |
| 03 | [Orbit](challenges/03-orbit/README.md) | Gravity, Kepler's laws | Squares / square roots | ★★☆ |
| 04 | [N-Body](challenges/04-nbody/README.md) | Many-body problem, energy conservation | Vector addition | ★★☆ |
| 05 | [Wave Machine](challenges/05-wave-machine/README.md) | Wave equation, standing waves | Arrays | ★★☆ |
| 06 | [Heat Engine](challenges/06-heat-engine/README.md) | Thermodynamics, Carnot cycle | +−×÷ | ★★★ |
| 07 | [Double Pendulum](challenges/07-double-pendulum/README.md) | Chaos, Lyapunov exponent | ODEs (AI helps) | ★★★ |
| 08 | [Fluid](challenges/08-fluid/README.md) | Fluid dynamics | Array ops | ★★★★ |
| 09 | [Electromagnetism](challenges/09-electromagnetism/README.md) | EM fields, Maxwell's equations | Array ops | ★★★★ |
| 10 | [Relativity](challenges/10-relativity/README.md) | Special relativity, spacetime | Matrices | ★★★★ |
| 11 | [Quantum](challenges/11-quantum/README.md) | Quantum mechanics, wave functions | Complex numbers (AI helps) | ★★★★★ |
| 12 | [Solar System](challenges/12-solar-system/README.md) | Capstone project | Everything (AI helps) | ★★★★★ |

> **About the math**: every concept is explained *inside* the challenge when you need it (an "intuition-first" primer). You don't learn math before using it — you **learn by using it**. AI handles the parts you find confusing.

## Getting Started

### Start in three steps (no preparation needed)

```bash
# 1. Fork this repository
# 2. Open challenge 00: Python Crash Course (browser edition — nothing to install)
# 3. Copy the AI collaboration prompt and write your first line of code
```

### Run in your browser (recommended)

| Platform | URL | Notes |
|----------|-----|-------|
| Google Colab | [colab.research.google.com](https://colab.research.google.com) | Free, no install, Python built in |
| Deepnote | [deepnote.com](https://deepnote.com) | Free, collaboration-friendly |
| Local Jupyter | `pip install jupyter` | Install once, use forever |

### The AI collaboration workflow

This is the most important part of the repository. **You're not learning alone — AI is your tutor.**

```
1. Open a challenge → copy the "AI collaboration prompt" into an AI chat
2. AI guides you: explain → write code → run → observe
3. Stuck? Ask AI to explain the code, not to give you the answer
4. Done? Ask AI to quiz you (checks your understanding)
```

**The golden rule**: let AI *explain*, never let AI *write it for you*. If you can't explain the code you submitted, you haven't learned anything.

## Challenge Template

Every challenge contains:

```
challenges/NN-name/
├── README.md          # Physics background (intuition-first) + laws + hints + AI prompts
├── SPEC.md            # Acceptance criteria (automated, machine-checkable)
├── starter/           # Starting code template with TODOs
│   └── projectile.py
├── ai/                # AI collaboration prompts
│   └── tutor.md
└── solutions/         # Reference implementation (or browse via the `solutions` branch)
```

## Auto-Grading

On every push / PR, GitHub Actions runs `.github/workflows/challenge-grading.yml`, grading challenges 01-12 in parallel:

- **main branch** (TODOs unfilled): automatically runs **regression tests** against the `solutions/` reference implementations — proving the acceptance criteria themselves are correct
- **PR / learner branch** (starter completed): runs `verify.py` directly against the learner's code — **passing is how you pass**
- Challenges 04-09, 11-12 need NumPy (installed automatically in CI); challenge 10 is pure standard library

Simulate CI locally: `python scripts/grade.py` (all 12 by default, or pass specific challenge names)

## Resources

- [Numerical Methods Primer](resources/numerical-methods.md) — Euler, RK4, leapfrog in one picture
- [Visualization Guide](resources/visualization.md) — making physics visible
- [Classic Physics Education](resources/physics-education.md) — Feynman Lectures, Landau, Susskind and more
- [AI-Assisted Learning Guide](resources/ai-learning-guide.md) — how to make AI your personal physics tutor
- [Zero-Math Refresher](resources/math-primer.md) — intuition-first calculus, just enough to get going

## Community

- [Contributing](community/CONTRIBUTING.md) — submit challenges, improve tutorials, report issues
- [Challenge Ideas](community/ideas.md) — what challenge should we build next?
- [Code of Conduct](community/CODE_OF_CONDUCT.md) — how we collaborate
- [Study Groups](community/study-groups.md) — team up, review each other, finish together

## FAQ

**Q: I've never programmed. Can I still learn?**
A: Yes. Challenge 00 is designed for absolute beginners — running in your browser in three minutes, with AI by your side.

**Q: How much math do I need?**
A: Basic arithmetic is enough to start. All math is explained inside each challenge, and AI handles the hard parts.

**Q: Why Python? Is it required?**
A: It's not required. But Python is the **closest to natural language**, the fastest to pick up, and has the richest scientific ecosystem (NumPy/Matplotlib). It's simply the most convenient tool.

**Q: Why not use an existing physics engine?**
A: An existing engine is someone else's wheel. The whole point here is **building the wheel yourself** — you only truly understand gravity once you've written it yourself and watched a planet orbit.

**Q: Are there reference solutions?**
A: Yes — in each challenge's `solutions/` directory (or switch to the `solutions` branch to see them all). But write your own first; peek only when you're stuck.

**Q: How do I know if my simulation is correct?**
A: Each challenge's `SPEC.md` defines automated acceptance criteria (e.g., "energy drift < 1% after 10,000 steps"). Run `python starter/verify.py` to check yourself.

## Project Roadmap

- [x] 12 core challenges + challenge 00 crash course
- [x] AI collaboration prompts for every challenge
- [x] Automated grading (GitHub Actions verifies the SPECs)
- [ ] Bilingual site (中文/English)
- [ ] Video walkthroughs per challenge
- [ ] More language templates (Rust, Julia, JS)

---

## License

MIT License — free to use, modify, and distribute.

## Acknowledgments

- [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) — inspiration
- [The Feynman Lectures on Physics](https://www.feynmanlectures.caltech.edu/) — the soul of physics
- All contributors 🙏

---

*Master physics by recreating it from scratch.*
