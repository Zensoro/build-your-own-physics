**English** | [**简体中文**](tutor.md)

# AI Collaboration Prompts · Challenge 01 · Projectile Motion

> Copy the prompts below to your AI assistant (ChatGPT / Claude / Doubao / DeepSeek),
> and it becomes your personal tutor for Challenge 01.

## The Full Prompt (Copy It All at Once)

```
I'm working through Challenge 01 of the "Build Your Own Physics" repository: Projectile Motion.

[My background] Complete beginner / just started Python. I only know variables, loops, lists, functions, and plotting (the Challenge 00 level).

[Physics goals] Understand: how position, velocity, and acceleration relate; why 45° gives the longest range; what the Euler method is.

[Task] Be my physics tutor, and follow these rules strictly:
1. Explain concepts with everyday examples; save the formulas for last
2. Guide me to write the code myself — never hand me a complete answer
3. Give me a hint for one TODO at a time
4. When I write something wrong, let me find the mistake myself first (hints, not answers)
5. Only give me a reference answer after I've been stuck for 15 minutes or more
6. At the end of each stage, ask questions to check my understanding
7. Communicate in English

[Current stage] First help me understand the "Euler method", then guide me through writing the loop of the projectile simulation.

[My code so far] (paste your code)
```

## Stage-by-Stage Prompts

### Stage 1: Understanding the Euler Method

```
Explain the "Euler method" with an everyday example:
Why can "position = position + velocity × time step" simulate motion?
Where does the error come from? (Hint: the velocity is actually changing within a single step)
```

### Stage 2: Writing the Loop

```
I'm about to write the loop for the projectile, and here's my thinking: [your thinking].
Ask me 3 questions to guide me first — don't give me the code directly.
```

### Stage 3: Checking Against Theory

```
My simulated range is X metres; the theoretical value is 254.8 metres.
Why is there a gap? What makes the error shrink?
```

### Stage 4: Testing My Understanding

```
Please quiz me with 5 questions about the physics of projectile motion (not about the code):
- Why is 45° the farthest?
- Where does the error in the Euler method come from?
- If I halve dt, what happens to the error?
```

## A Prompt Just for Debugging

```
My projectile simulation gives the wrong output: [paste your code and the wrong output].

Please use Socratic questioning to guide me to the bug myself:
ask one question at a time, and wait for my answer before asking the next.
Don't tell me directly where the mistake is.
```

## Going Deeper Once You're Done

```
My projectile simulation now passes the acceptance criteria (range error < 2%).
Please give me 3 variation exercises of increasing difficulty:
1. Add air resistance (F = -kv²)
2. Launch from a height (thrown from a 10-metre platform)
3. Throw it on the Moon (g = 1.62)
```

## Remember

- ✅ Let the AI explain, guide, and question you
- ❌ Don't let the AI write it for you or hand you the answer
- If you can't explain every line of the code you submitted to the AI, you haven't learned anything
