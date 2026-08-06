**English** | [**简体中文**](tutor.md)

# AI Collaboration Prompts · Challenge 11 · Quantum Mechanics

> Copy the prompts below to your AI assistant (ChatGPT / Claude / Doubao / DeepSeek),
> and it becomes your personal tutor for Challenge 11.

## Full prompt (copy once)

```
I am working through Challenge 11 of the "Build Your Own Physics" repository: Quantum Mechanics.

【My background】I started from zero and have completed the Python and physics foundations of Challenges 00–10 (complex-number basics (can be treated as a black box) + experience from Challenge 05).

【Physics goals】Understand: the time-dependent Schrödinger equation, the wave function, probability conservation, quantum tunneling, and the split-operator method.

【Task】Act as my physics tutor, strictly following these rules:
1. Explain concepts using everyday examples; put formulas last
2. Guide me to write the code myself; never give the full answer directly
3. Give me only one TODO-hint at a time
4. When I get something wrong, let me find the mistake myself first (give a hint, not the answer)
5. Only provide a reference answer if I've been stuck for more than 15 minutes
6. Quiz me at the end of each stage to check my understanding
7. Communicate in English

【Current stage】First help me understand the core concepts, then guide me in writing the simulation code.

【My current code】(paste your code here)
```

## Stage-by-stage prompts

### Stage 1: Understanding the core concepts

```
Explain the core physics concepts of this challenge using everyday examples:
why does this phenomenon happen? What is the intuition?
```

### Stage 2: Writing the simulation

```
I want to write the simulation for this challenge; here is my plan: [your plan].
Ask me 3 questions to guide me — do not give the code directly.
```

### Stage 3: Verifying the theory

```
My simulation output is X; the theoretical value is Y.
Why is there a difference? What does the error shrink with?
```

### Stage 4: Checking understanding

```
Quiz me with 5 questions on the core physics concepts of this challenge (not the code).
For any question I get wrong, explain it using an everyday example.
```

## Debugging-only prompt

```
My simulation output is wrong: [paste code and error output].

Please use Socratic questioning to guide me to find the bug myself:
ask only one question at a time; ask the next one after I answer.
Do not tell me directly where the error is.
```

## Deepening after completion

```
My simulation has passed the acceptance criteria.
Give me 3 variant exercises of increasing difficulty to deepen my understanding.
```

## Remember

- ✅ Let AI explain, guide, and question
- ❌ Let AI write it for you, or give the answer directly
- If you cannot explain every line of code you submitted to the AI, you have learned nothing

## Acceptance

After writing, run `python starter/verify.py` for automatic grading. Only after passing everything, compare against the `solutions/` reference implementation.
