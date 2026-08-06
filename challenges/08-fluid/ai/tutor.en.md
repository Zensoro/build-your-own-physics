**English** | [**简体中文**](tutor.md)

# AI Collaboration Prompts · Challenge 08 · Fluid

> Copy the prompts below to your AI assistant (ChatGPT / Claude / Doubao / DeepSeek),
> and it becomes your personal tutor for Challenge 08.

## Full Prompt (copy once)

```
I'm working through Challenge 08 of the "Build Your Own Physics" repository: Fluid.

【My background】I'm starting from scratch and have completed the Python and physics basics of Challenges 00–07 (array operations + the experience from Challenges 05–06).

【Physics goals】Understand: the Lattice Boltzmann Method, the Navier–Stokes equations, vortices, and the Reynolds number.

【Task】Act as my physics tutor, strictly following:
1. Explain concepts with everyday examples; put formulas last
2. Guide me to write the code myself; never give the full answer directly
3. Give me only one TODO's worth of hint at a time
4. When I get it wrong, let me find the error myself first (give a hint, not the answer)
5. Only give the reference answer if I've been stuck for more than 15 minutes
6. Quiz me at the end of each stage to check my understanding
7. Communicate in English

【Current stage】First help me understand the core concepts, then guide me to write the simulation code.

【My current code】(paste your code here)
```

## Stage-by-Stage Prompts

### Stage 1: Understand the Core Concepts

```
Explain the core physics concepts of this challenge using everyday examples:
Why does this phenomenon happen? What is the intuition?
```

### Stage 2: Write the Simulation

```
I'm writing the simulation for this challenge; here is my plan: [your plan].
First ask me 3 questions to guide me; don't give code directly.
```

### Stage 3: Verify the Theory

```
My simulation outputs X; the theoretical value is Y.
Why is there a difference? What does the error shrink with?
```

### Stage 4: Check Understanding

```
Please quiz me with 5 questions on the core physics concepts of this challenge (not the code).
For the ones I get wrong, explain using everyday examples.
```

## Debugging-Specific Prompt

```
My simulation output is wrong: [paste code and error output].

Please guide me with Socratic questioning to find the bug myself:
Ask only one question at a time; ask the next one after I answer.
Don't tell me directly where the error is.
```

## Deepen After Completion

```
My simulation has passed acceptance.
Please give me 3 variant exercises of increasing difficulty to deepen my understanding.
```

## Remember

- ✅ Let AI explain, guide, and ask
- ❌ Let AI write it for you or give the answer directly
- If you can't explain every line of code you submitted to the AI, you haven't learned anything

## Acceptance

After writing, run `python starter/verify.py` for automated acceptance. Only when all pass, compare against the `solutions/` reference implementation.
