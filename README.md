# Build Your Own Physics

> **Master physics by recreating it from scratch.**
> 亲手重建物理定律，而不仅仅是背诵它们。

---

## Why This Exists

> *"What I cannot create, I do not understand."* — Richard Feynman

大多数物理学习止步于「看懂公式」。但看懂 ≠ 理解。当你亲手用代码从零搭出一个引力轨道、一段波的传播、一个热机的循环时，那些公式不再是需要背诵的答案，而是你亲手走过每一步的直觉积累。

**这个仓库帮你完成一次「重构式学习」（Reconstructive Learning）：会算 → 会推 → 会模拟 → 会创造。**

## 🎯 完全零基础友好

**不需要任何前置知识。** 我们重新设计了一切：

| 你不必先会 | 我们会带你 |
|-----------|-----------|
| ❌ 编程 | ✅ 从第一行 `print` 开始，AI 全程辅助 |
| ❌ 微积分 | ✅ 所有数学都从"直觉"讲起，公式是副产品 |
| ❌ 大学物理 | ✅ 从"苹果为什么会落地"开始 |
| ❌ 装环境 | ✅ 三分钟在浏览器里跑起来 |

**AI 是你的私人导师。** 每个挑战都配有「AI 协作提示词」，你把它们复制给 ChatGPT / Claude / 豆包，AI 会：
- 解释你看不懂的每一行代码
- 帮你 debug
- 在你卡住时给提示，而不是给答案
- 检查你的理解

## How It Works

每个挑战都遵循同一个循环：

```
读定律（直觉版）→ 抄写代码 → 跑起来 → 看到现象 → 改参数 → 深入理解
```

- 每个挑战**只给你物理定律和最小提示**，不给完整答案
- 你的任务是从零写出**可运行、可验证**的模拟
- 每个挑战都配有**验收标准**（数值误差、物理现象必须出现）
- 完成后对照**参考实现**（`solutions/` 目录；也可直接切到 `solutions` 分支整体查看）

## The Roadmap

从「第一行物理代码」到「一个太阳系」，共 12 级挑战：

| 等级 | 挑战 | 物理主题 | 需要数学 | 难度 |
|------|------|---------|---------|------|
| 00 | [Python 零基础速成](challenges/00-python-basics/README.md) | 变量、循环、函数 | 四则运算 | ★☆☆ |
| 01 | [Projectile Motion](challenges/01-projectile/README.md) | 抛体运动、空气阻力 | 勾股定理 | ★☆☆ |
| 02 | [Pendulum](challenges/02-pendulum/README.md) | 简谐运动、相空间 | 三角函数 | ★☆☆ |
| 03 | [Orbit](challenges/03-orbit/README.md) | 万有引力、开普勒定律 | 平方/开方 | ★★☆ |
| 04 | [N-Body](challenges/04-nbody/README.md) | 多体问题、能量守恒 | 向量加减 | ★★☆ |
| 05 | [Wave Machine](challenges/05-wave-machine/README.md) | 波动方程、驻波 | 数组 | ★★☆ |
| 06 | [Heat Engine](challenges/06-heat-engine/README.md) | 热力学、卡诺循环 | 加减乘除 | ★★★ |
| 07 | [Double Pendulum](challenges/07-double-pendulum/README.md) | 混沌、李雅普诺夫指数 | 微分方程（AI 帮忙） | ★★★ |
| 08 | [Fluid](challenges/08-fluid/README.md) | 流体动力学 | 数组操作 | ★★★★ |
| 09 | [Electromagnetism](challenges/09-electromagnetism/README.md) | 电磁场、麦克斯韦方程 | 数组操作 | ★★★★ |
| 10 | [Relativity](challenges/10-relativity/README.md) | 狭义相对论、时空 | 矩阵 | ★★★★ |
| 11 | [Quantum](challenges/11-quantum/README.md) | 量子力学、波函数 | 复数（AI 帮忙） | ★★★★★ |
| 12 | [Solar System](challenges/12-solar-system/README.md) | 综合项目 | 全部（AI 帮你） | ★★★★★ |

> **数学说明**：所有数学概念都在挑战内即时讲解（"微积分直觉版"）。你不需要先学会再用，而是**用着学着**。AI 会帮你处理看不懂的部分。

## Getting Started

### 三步开始（不需要任何准备）

```bash
# 1. Fork 这个仓库
# 2. 打开挑战 00：Python 零基础速成（有浏览器在线版，不用装任何东西）
# 3. 复制 AI 协作提示词，开始第一段代码
```

### 浏览器在线版（推荐）

| 平台 | 地址 | 说明 |
|------|------|------|
| Google Colab | [colab.research.google.com](https://colab.research.google.com) | 免费、无需安装、内置 Python |
| Deepnote | [deepnote.com](https://deepnote.com) | 免费、协作友好 |
| 本地 Jupyter | `pip install jupyter` | 安装一次，永久使用 |

### AI 协作工作流

这是本仓库最重要的部分。**你不是一个人学——AI 是你的导师。**

```
1. 打开挑战 → 复制「AI 协作提示词」到 AI 对话
2. AI 引导你：解释 → 写代码 → 跑 → 看现象
3. 卡住时：让 AI 解释代码，而不是直接给答案
4. 完成后：让 AI 考考你（检查理解）
```

**黄金法则**：让 AI 解释，不让 AI 代写。如果你看不懂自己提交的代码，你就没有学到东西。

## Challenge Template

每个挑战包含：

```
challenges/NN-name/
├── README.md          # 物理背景（直觉版）+ 定律 + 提示 + AI 协作提示词
├── SPEC.md            # 验收标准（可自动化测试）
├── starter/           # 起步代码模板
│   └── projectile.py
├── ai/                # AI 协作提示词
│   └── tutor.md
└── solutions/         # 参考实现（也可切 `solutions` 分支整体查看）
```

## Auto-Grading（自动评分）

每次 push / PR 时，GitHub Actions 会自动运行 `.github/workflows/challenge-grading.yml`，用矩阵并行评分挑战 01-12：

- **main 分支**（TODO 模板未填）：自动用 `solutions/` 参考实现做**回归测试**，确保验收标准本身正确
- **PR / 学习者分支**（starter 已填完）：直接对学习者的代码跑 `verify.py`，**通过才算过关**
- 挑战 04-09、11-12 依赖 NumPy（CI 自动安装）；挑战 10 纯标准库

本地想模拟 CI：`python scripts/grade.py`（默认全部 12 个挑战，或指定挑战名）

## Resources

- [数值方法入门](resources/numerical-methods.md) — 欧拉法、RK4、蛙跳法一图流
- [可视化指南](resources/visualization.md) — 让物理"看得见"
- [物理教育经典](resources/physics-education.md) — Feynman Lectures、Landau、Susskind 等
- [AI 辅助学习指南](resources/ai-learning-guide.md) — 如何让 AI 当你的私人物理导师
- [零基础数学补给站](resources/math-primer.md) — 微积分直觉版，够用就好

## Community

- [如何贡献](community/CONTRIBUTING.md) — 提交挑战、改进教程、报告问题
- [挑战建议](community/ideas.md) — 你希望看到的下一个挑战
- [代码规范](community/CODE_OF_CONDUCT.md) — 我们如何协作
- [学习小组](community/study-groups.md) — 组队通关，互相 review

## FAQ

**Q: 我完全不会编程，能学吗？**
A: 能。挑战 00 专为零基础设计，浏览器三分钟跑起来，AI 全程辅助。

**Q: 数学基础要多少？**
A: 会四则运算就能开始。所有数学都在挑战内即时讲解，AI 帮你处理难题。

**Q: 为什么用 Python？它是必须的吗？**
A: 不是必须的。但 Python 是**最接近自然语言**的编程语言，学起来最快，科学计算生态最全（NumPy/Matplotlib），AI 辅助效果最好。它只是**最顺手的工具**。

**Q: 为什么不用现成的物理引擎？**
A: 用现成引擎 = 用别人造的轮子。这里的目的是**亲手造轮子**——只有当你自己写出万有引力并看到行星绕起来，你才真正理解它。

**Q: 有参考实现吗？**
A: 有，每个挑战的 `solutions/` 目录里。想一次性看全部答案可切到 `solutions` 分支。但强烈建议先自己写，卡住再看。

**Q: 我写完了，怎么验证对错？**
A: 每个挑战的 `SPEC.md` 都定义了可自动化的验收标准（如"1 万步后能量误差 < 1%"）。

## Roadmap

- [x] 12 级核心挑战 + 00 零基础速成
- [x] 每挑战 AI 协作提示词
- [x] 挑战自动评分器（GitHub Actions 验证 SPEC）
- [ ] 中文/英文双语站
- [ ] 每挑战配套视频讲解
- [ ] 更多语言模板（Rust、Julia、JS）

---

## License

MIT License — 自由使用、修改、分发。

## Acknowledgments

- [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) — 灵感来源
- [The Feynman Lectures on Physics](https://www.feynmanlectures.caltech.edu/) — 物理之魂
- 所有贡献者 🙏

---

*Master physics by recreating it from scratch.*
