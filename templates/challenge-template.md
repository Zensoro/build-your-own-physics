# Template — 挑战文件模板

> 提交新挑战时，复制本模板。**不要修改**模板文件本身。

## 结构

```
challenges/NN-name/
├── README.md    # 物理背景 + 定律 + 提示
├── SPEC.md      # 验收标准
├── starter/     # 起步代码模板（可选但推荐）
└── solutions/   # 参考实现（可选）
```

## README.md 模板

```markdown
# Challenge NN · Challenge Name

> **一句 slogan——学习者完成后的"啊哈"时刻。**

## Why This Challenge
为什么值得做？完成者会获得什么理解？
（写清楚它在前一挑战的基础上新增了什么）

## Physics Background
运动方程 / 定律 / 关键概念。
（数学公式用 LaTeX：$$ ... $$）

## Your Task
1. 明确的任务清单
2. 分步骤

### Starter Code
\`\`\`python
# 可运行的模板，TODO 标出要填的地方
\`\`\`

### 完成后的检查
- [ ] 可验证的清单

## Hints
<details>
<summary>展开查看提示</summary>
- 提示内容
</details>

## Next Steps
→ [前往挑战 NN+1](../NN+1-name/README.md)
```

## SPEC.md 模板

```markdown
# SPEC NN · Challenge Name

> 验收标准，可自动化测试。

## 验收标准
### S.N.1 功能
- [ ] 标准

### S.N.2 数值精度
- [ ] 标准（含误差范围）

## 测试数据
| 参数 | 值 |

## 参考解
参考实现见 `solutions` 分支。
```

## 规范要点

- 挑战名用 kebab-case：`03-orbit`，序号两位：`03`
- 所有文件使用 UTF-8 编码
- 公式用 LaTeX（GitHub 自动渲染）
- starter 代码必须可运行、用 ASCII 引号
- 提示用 `<details>` 折叠，鼓励先自己尝试
- 每关有"→ Next Steps"衔接下一个挑战
