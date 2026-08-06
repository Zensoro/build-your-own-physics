**English** | [**简体中文**](tutor.md)

# AI Collaboration Prompts · Challenge 04 · Many-Body Problem (N-Body)

> Copy the prompt below to your AI assistant (ChatGPT / Claude / Doubao / DeepSeek),
> and it becomes your personal tutor for Challenge 04.

## Full prompt (copy once)

```
I'm working through Challenge 04 of the "Build Your Own Physics" repository: the many-body problem (N-Body).

[My background] I'm starting from scratch and have completed the Python and physics foundations of Challenges 00–03 (experience from Challenge 03).

[Physics goals] Understand: why the many-body problem has no analytical solution, the complexity of direct summation, and the numerical test for energy conservation.

[Task] Please act as my physics tutor, strictly following:
1. Explain concepts with everyday examples; put formulas last
2. Guide me to write the code myself — never hand me a complete answer
3. Give me only one TODO hint at a time
4. When I make a mistake, let me find it myself first (hints, not answers)
5. Only give a reference answer if I've been stuck for 15 minutes or more
6. Quiz me with questions at the end of each stage to check my understanding
7. Communicate in English

[Current stage] First help me understand the core concepts, then guide me to write the simulation code.

[My current code] (paste your code here)
```

## Stage-by-stage prompts

### Stage 1: Understand the core concepts

```
Explain the core physics concepts of this challenge using everyday examples:
Why does this phenomenon happen? What's the intuition?
```

### Stage 2: Write the simulation

```
I'm going to write the simulation for this challenge. Here's my plan: [your plan].
Ask me 3 questions to guide me first — don't give me code directly.
```

### Stage 3: Verify the theory

```
My simulation outputs X, and the theoretical value is Y.
Why is there a difference? What does the error shrink with?
```

### Stage 4: Check understanding

```
Quiz me with 5 questions on the core physics concepts of this challenge (not the code).
For anything I get wrong, explain it using an everyday example.
```

## Debugging prompts

```
My simulation output is wrong: [paste your code and error output].

Use Socratic questioning to guide me to find the bug myself:
Ask only one question at a time; after I answer, ask the next one.
Don't tell me directly where the error is.
```

## Deepen after completion

```
My simulation has passed acceptance.
Give me 3 variation exercises of increasing difficulty to deepen my understanding.
```

## Remember

- ✅ Let AI explain, guide, and question
- ❌ Let AI write it for you or hand you answers
- If you can't explain every line of code you submitted to the AI, you haven't learned anything

## Acceptance

After writing, run `python starter/verify.py` for automated acceptance. Only after all tests pass, compare against the `solutions/` reference implementation.
