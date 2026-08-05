# Contributing to Build Your Own Physics

> 这是社区项目。**你的贡献就是它活着的证明。**

感谢你愿意贡献！无论你是提交挑战、改进教程、修 bug 还是提建议，都欢迎。

## 目录

- [贡献类型](#贡献类型)
- [提交新挑战](#提交新挑战)
- [改进已有挑战](#改进已有挑战)
- [Git 工作流](#git-工作流)
- [代码规范](#代码规范)
- [审核流程](#审核流程)

## 贡献类型

| 类型 | 说明 | 门槛 |
|------|------|------|
| 🐛 修 bug | 修正错别字、公式错误、链接失效 | 极低 |
| 📝 改进教程 | 补充提示、改进措辞、优化 starter 代码 | 低 |
| ➕ 提交解决方案 | 用你喜欢的语言提交挑战的解法 | 低 |
| 🆕 新挑战 | 提交全新的挑战 | 中 |
| 🌐 翻译 | 翻译到其他语言 | 低 |

## 提交新挑战

新挑战必须满足以下标准：

1. **可独立完成** — 不依赖私有数据/付费软件
2. **物理真实** — 模拟的是真实物理定律，不是魔改规则
3. **有验收标准** — 必须配 `SPEC.md`，可自动化验证
4. **有梯度** — 从"能跑"到"做得好"之间至少 3 个台阶
5. **有学习价值** — 完成者应能说"我终于理解了这个概念"

### 新挑战模板

```
challenges/NN-name/
├── README.md    # 物理背景 + 定律 + 提示
├── SPEC.md      # 验收标准
├── starter/     # 起步代码模板（可选但推荐）
└── solutions/   # 参考实现（可选）
```

NN 是两位数的序号（如 13、14...），name 用 kebab-case。

## 改进已有挑战

- 直接在 issue 中提出建议，或提交 PR
- 改公式/数据时**必须**说明依据（教材页码/链接）
- 修改 starter 代码时保持接口不变（`simulate(...)` 等）

## Git 工作流

```bash
# 1. Fork 并克隆
git clone https://github.com/YOUR_NAME/build-your-own-physics.git
cd build-your-own-physics

# 2. 建分支
git checkout -b feat/add-challenge-13

# 3. 提交
git add .
git commit -m "feat: add challenge 13 - Brownian motion"

# 4. 推送并开 PR
git push origin feat/add-challenge-13
```

## 代码规范

- 语言不限（Python / JS / Rust / C++ / Julia 均可）
- starter 代码必须**可运行**（不含语法错误）
- 代码中标注 `# TODO` 的位置就是挑战要你填的地方
- 注释要"讲物理"：`# 欧拉法：先更新速度再更新位置`
- 使用 ASCII 引号，不用中文引号（避免编码问题）

## 审核流程

1. PR 提交后由维护者或社区成员 review
2. 检查：物理正确性 → 可运行性 → 文档质量
3. 合并到 `main` 分支；参考实现合并到 `solutions` 分支

## 行为准则

见 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。核心一条：**尊重每个人**，无论水平高低。我们都在学习的路上。
