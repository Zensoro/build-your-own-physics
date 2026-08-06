**English** | [**简体中文**](README.md)

# Challenge 00 · Python Crash Course

> **From zero to your first line of physics code in 30 minutes.**
> This is the only prerequisite in the whole repository — no programming experience required.

## Why This Challenge

You don't have to finish learning Python before you start learning physics. You only need **just enough**: once you can express "position, velocity, acceleration" in code, you're ready for Challenge 01.

This challenge teaches five things and nothing more: **variables, loops, functions, lists, and plotting**. Learn those five and you'll have every tool you need to write a physics simulation.

## Start in Three Minutes (Nothing to Install)

Open [Google Colab](https://colab.research.google.com) (free, runs right in your browser):

```
1. Click "New Notebook"
2. Type the first snippet below into the code cell
3. Press Shift + Enter to run it
```

If Colab is hard to reach from mainland China, use [Deepnote](https://deepnote.com) or install locally:
```bash
# Local install (Mac / Windows / Linux all work)
python3 -m pip install jupyter matplotlib numpy
python3 -m jupyter notebook
```

## The Five Concepts You Need

### 1. Variables — Giving Numbers a Name

```python
# 物理的"量"就是变量：位置、速度、时间
x = 0.0        # 位置，单位米
v = 10.0       # 速度，单位米/秒
t = 0.0        # 时间，单位秒
```

**Practice**: store your name and your age in variables, then print them.

```python
name = "小明"
age = 20
print(name, age)
```

### 2. Loops — Making Physics *Move*

Physics is, at its core, "change over time." A loop lets time walk forward one step at a time:

```python
t = 0.0
while t < 5.0:          # 只要 t 小于 5 秒
    print("时间:", t, "秒")
    t = t + 0.5         # 每步加 0.5 秒
```

**Practice**: write a loop that counts from 0 to 10, adding 1 each time.

### 3. Lists — Remembering Every Step

Physics needs a record of "where things were at each moment," and a list is exactly the container for those records:

```python
positions = []          # 空列表
t = 0.0
while t < 5.0:
    positions.append(t * 10)   # 位置 = 时间 × 速度
    t = t + 0.5

print(positions)         # 打印全部位置
```

**Practice**: record the position every 0.1 s from 0 to 1 s (assume a speed of 5 m/s).

### 4. Functions — Wrapping Up a "Physics Formula"

A function is just a black box that goes "input → formula → output":

```python
def 距离(速度, 时间):
    return 速度 * 时间   # 公式：距离 = 速度 × 时间

d = 距离(5.0, 3.0)       # 用函数
print(d)                 # 15.0
```

**Practice**: write a function that takes a radius and returns the area of a circle ($A = \pi r^2$).

### 5. Plotting — Making Physics *Visible*

The climax of any physics simulation: turning numbers into a picture.

```python
import matplotlib.pyplot as plt   # 引入画图工具

positions = []
times = []
t = 0.0
while t < 5.0:
    positions.append(10 * t)      # 匀速直线运动
    times.append(t)
    t = t + 0.1

plt.plot(times, positions)         # 画图
plt.xlabel("时间 (秒)")
plt.ylabel("位置 (米)")
plt.show()                         # 显示
```

**Practice**: turn the constant-velocity motion above into constant *acceleration* (position = ½ × acceleration × time²) and see how the curve changes.

## What the Five Concepts Mean in Physics

| Python concept | Physics meaning | Example |
|------------|---------|-----|
| Variable | A physical quantity (position, velocity, time) | `x = 0.0` |
| Loop | Time evolution (the simulation's "heartbeat") | `while t < 10:` |
| List | A trajectory record (the state at every moment) | `positions.append(x)` |
| Function | A physical law (input a state → output the change) | `def force(m, a): return m * a` |
| Plot | Visualization (the eyes that let you see a phenomenon) | `plt.plot(t, x)` |

## Going Further (Optional — Learn It When You Meet It)

You don't need any of this right now, but later challenges will use it, so just get a feel for the names:

- **NumPy** (`import numpy as np`) — array math, used heavily from here on
- **The math library** (`import math`) — `math.sin`, `math.cos`, `math.sqrt`
- **Random numbers** (`import random`) — used later for simulating Brownian motion

## Self-Check After Completion

- [ ] You can store numbers and text in variables
- [ ] You can use a `while` loop to push time forward
- [ ] You can use a list to record the position at every step
- [ ] You can write a function that wraps up a formula
- [ ] You can plot an x-t curve
- [ ] You can explain why "a loop = time moving forward"

## AI Collaboration Prompts

Copy this to your AI assistant (ChatGPT / Claude / Doubao):

```
I'm working through a Python crash course from scratch, and my goal is to learn physics simulation.
Please teach me in the plainest language possible. Requirements:
1. Cover one concept at a time, using examples from everyday life
2. After each explanation, let me write the code myself; then check it and explain
3. When I get something wrong, guide me to find the mistake myself — don't hand me the answer
4. After each concept, reinforce it with a physics example (velocity, acceleration, and so on)
5. Communicate in English
Let's start with "variables".
```

## Next Steps

Congratulations! You now have every tool you need to write physics code. Next, use them to make a **projectile fly** — your very first physics simulation.

→ [Go to Challenge 01: Projectile Motion](../01-projectile/README.en.md)
