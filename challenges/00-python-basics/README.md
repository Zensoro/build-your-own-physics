# Challenge 00 · Python 零基础速成

> **从零到会写第一段物理代码，只需 30 分钟。**
> 这是本仓库的唯一前置条件——不需要任何编程经验。

## Why This Challenge

你不需要先学完 Python 再学物理。你只需要**够用就好**：能用代码表达"位置、速度、加速度"这几个概念，就能开始挑战 01。

本挑战只教 5 件事：**变量、循环、函数、列表、画图**。学完这 5 件事，你就有了写物理模拟的全部工具。

## 三分钟开始（不用装任何东西）

打开 [Google Colab](https://colab.research.google.com)（免费，浏览器直接跑）：

```
1. 点 "New Notebook"（新建笔记本）
2. 在代码框里输入下面第一段代码
3. 按 Shift + Enter 运行
```

如果在中国大陆访问 Colab 不便，可以用 [Deepnote](https://deepnote.com) 或本地安装：
```bash
# 本地安装（Mac / Windows / Linux 均可）
python3 -m pip install jupyter matplotlib numpy
python3 -m jupyter notebook
```

## 5 个必学概念

### 1. 变量 —— 给数字起名字

```python
# 物理的"量"就是变量：位置、速度、时间
x = 0.0        # 位置，单位米
v = 10.0       # 速度，单位米/秒
t = 0.0        # 时间，单位秒
```

**练习**：把你的名字和年龄存成变量，打印出来。

```python
name = "小明"
age = 20
print(name, age)
```

### 2. 循环 —— 让物理"动起来"

物理的本质是"随时间变化"。用循环让时间一步步走：

```python
t = 0.0
while t < 5.0:          # 只要 t 小于 5 秒
    print("时间:", t, "秒")
    t = t + 0.5         # 每步加 0.5 秒
```

**练习**：让循环从 0 数到 10，每次加 1。

### 3. 列表 —— 记住每一步

物理需要记录"每个时刻的位置"，列表就是用来装这些记录的：

```python
positions = []          # 空列表
t = 0.0
while t < 5.0:
    positions.append(t * 10)   # 位置 = 时间 × 速度
    t = t + 0.5

print(positions)         # 打印全部位置
```

**练习**：记录 0 到 1 秒内，每 0.1 秒的位置（假设速度 5 m/s）。

### 4. 函数 —— 打包成"物理公式"

函数就是"输入 → 公式 → 输出"的黑盒：

```python
def 距离(速度, 时间):
    return 速度 * 时间   # 公式：距离 = 速度 × 时间

d = 距离(5.0, 3.0)       # 用函数
print(d)                 # 15.0
```

**练习**：写一个函数，输入半径，输出圆的面积（$A = \pi r^2$）。

### 5. 画图 —— 让物理"看得见"

物理模拟的最高潮：把数字变成图像。

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

**练习**：把上面的匀速运动改成匀加速运动（位置 = ½ × 加速度 × 时间²），看看曲线变成什么样。

## 5 个概念的物理意义

| Python 概念 | 物理意义 | 例 |
|------------|---------|-----|
| 变量 | 物理量（位置、速度、时间） | `x = 0.0` |
| 循环 | 时间演化（模拟的"心跳"） | `while t < 10:` |
| 列表 | 轨迹记录（每个时刻的状态） | `positions.append(x)` |
| 函数 | 物理定律（输入状态 → 输出变化） | `def force(m, a): return m * a` |
| 画图 | 可视化（理解现象的眼睛） | `plt.plot(t, x)` |

## 进阶（可选，遇到再学）

以下概念不需要现在就学，但后面挑战会遇到，先有个印象：

- **NumPy**（`import numpy as np`）— 数组计算，后面大量使用
- **数学库**（`import math`）— `math.sin`, `math.cos`, `math.sqrt`
- **随机数**（`import random`）— 后面模拟布朗运动用

## 完成后自测

- [ ] 会用变量存数字和文字
- [ ] 会用 while 循环让时间推进
- [ ] 会用列表记录每一步的位置
- [ ] 会写函数封装公式
- [ ] 会画一条 x-t 曲线
- [ ] 能解释"循环 = 时间的推进"

## AI 协作提示词

把这个复制给你的 AI 助手（ChatGPT / Claude / 豆包）：

```
我正在学 Python 零基础课程，目标是学物理模拟。
请用最通俗的语言教我，要求：
1. 每次只讲一个概念，用生活中的例子
2. 讲完让我自己写代码，你检查并解释
3. 我出错时，先引导我自己找错，不要直接给答案
4. 每讲完一个概念，用物理的例子巩固（比如速度、加速度）
现在开始讲"变量"。
```

## Next Steps

恭喜！你有了写物理代码的全部工具。接下来，用它们让一个**抛体飞起来**——这是你的第一个物理模拟。

→ [前往挑战 01：Projectile Motion](../01-projectile/README.md)
