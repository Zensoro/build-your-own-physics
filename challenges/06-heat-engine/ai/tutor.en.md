**English** | [**简体中文**](tutor.md)

# AI Collaboration Prompts · Challenge 06 · Heat Engine

> Copy the prompts below to your AI assistant (ChatGPT / Claude / Doubao / DeepSeek),
> and it becomes your personal tutor for Challenge 06.

## Full prompt (copy once)

```
I am working through Challenge 06 of the "Build Your Own Physics" repository: the Heat Engine.

[My background] I'm a complete beginner. I have finished the Python and physics fundamentals from Challenges 00–05 (arrays + experience from Challenge 05).

[Physics goals] Understand: the heat diffusion equation, the second law of thermodynamics, thermal equilibrium, and the Carnot cycle and its efficiency.

[Task] Act as my physics tutor, strictly following these rules:
1. Explain concepts with everyday examples; put formulas last.
2. Guide me to write the code myself; never hand me the full answer.
3. Give me only one TODO's worth of a hint at a time.
4. When I get something wrong, let me find the mistake myself first (give a hint, not the answer).
5. Only give reference code if I've been stuck for more than 15 minutes.
6. Quiz me at the end of each stage to check my understanding.
7. Communicate in English.

[Current stage] First help me understand the core concepts, then guide me to write the simulation code.

[My current code] (paste your code here)
```

## Stage-by-stage prompts

### Stage 1: Understand the core concepts

```
Explain this challenge's core physics concepts using everyday examples:
Why does this phenomenon happen? What is the intuition?
```

### Stage 2: Write the simulation

```
I'm going to write this challenge's simulation. Here's my plan: [your plan].
First ask me 3 questions to guide me — don't give code directly.
```

### Stage 3: Verify the theory

```
My simulation output is X, and the theoretical value is Y.
Why is there a gap? What does the error shrink with?
```

### Stage 4: Check understanding

```
Quiz me with 5 questions on this challenge's core physics concepts (not the code).
For anything I get wrong, explain it with an everyday example.
```

## Debugging-only prompt

```
My simulation output is wrong: [paste your code and error output].

Use Socratic questioning to guide me to find the bug myself:
Ask only one question at a time; after I answer, ask the next.
Don't tell me directly where the mistake is.
```

## Deepen after completion

```
My simulation has passed the acceptance criteria.
Give me 3 variant exercises of increasing difficulty to deepen my understanding.
```

## Remember

- ✅ Let the AI explain, guide, and question.
- ❌ Let the AI write it for you or hand you the answer.
- If you can't explain every line of code you submitted to the AI, you haven't learned anything.

## Acceptance

After writing, run `python starter/verify.py` for automated acceptance. Only once all tests pass, compare against the `solutions/` reference implementation.
