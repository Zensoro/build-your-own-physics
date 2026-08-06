**简体中文** | [**English**](README.en.md)
# Challenge 08 · Fluid

> **让流动自然发生：格子玻尔兹曼方法入门。**

> 需要：数组操作 + 挑战 05-06 的经验。算法复杂，但 AI 可以全程引导。
> 🎓 有 AI 导师：[ai/tutor.md](ai/tutor.md)


## Why This Challenge

流体是最难模拟的经典系统之一——纳维-斯托克斯方程的非线性项让解析解几乎不存在。但**格子玻尔兹曼方法（LBM）**用一种几乎违反直觉的方式绕过了它：不是追踪流体粒子，而是追踪**粒子分布函数**在格点上的碰撞与迁移。

## Physics Background

### 格子玻尔兹曼方程

$$ f_i(\vec{x} + \vec{c}_i\Delta t, t + \Delta t) = f_i(\vec{x}, t) - \frac{\Delta t}{\tau}(f_i - f_i^{eq}) $$

- $f_i$：方向 $i$ 上的粒子分布函数
- $\vec{c}_i$：格点速度（D2Q9 模型有 9 个方向）
- $f_i^{eq}$：平衡分布（取决于当地密度和速度）
- $\tau$：松弛时间（与黏度相关）

### 宏观量恢复

密度和速度从分布函数的一阶、二阶矩恢复：

$$ \rho = \sum_i f_i, \quad \rho\vec{u} = \sum_i f_i \vec{c}_i $$

LBM 的正确性在于：对 $f_i$ 做 Chapman-Enskog 展开，可以在宏观尺度恢复**不可压缩纳维-斯托克斯方程**。

## Your Task

1. 实现 D2Q9 格子玻尔兹曼方法（LBM）
2. 模拟**顶盖驱动流（lid-driven cavity）**——最经典的 LBM 基准测试
3. 绘制速度场，观察中心涡流的形成
4. （进阶）模拟绕圆柱的流动，观察卡门涡街（涡旋脱落）

### 完成后的检查

- [ ] 顶盖驱动流出现中心主涡 + 两个角涡（$Re \approx 100$）
- [ ] 速度场连续、无振荡（非物理的棋盘模式）
- [ ] 不同 $Re$ 下涡流结构变化符合文献
- [ ] （进阶）绕圆柱时周期性涡街频率符合斯特劳哈尔数

## Hints

<details>
<summary>展开查看提示</summary>

- D2Q9 的 9 个方向：静止(1) + 正交(4) + 对角(4)
- 平衡分布 $f_i^{eq} = w_i \rho (1 + 3\vec{c}_i\cdot\vec{u} + \frac{9}{2}(\vec{c}_i\cdot\vec{u})^2 - \frac{3}{2}\vec{u}\cdot\vec{u})$，$w_i$ 是权重
- 迁移步骤是"搬运"：$f_i$ 从邻居格点搬过来，用索引操作实现
- 雷诺数 $Re = U L / \nu$，通过 $\tau$ 控制黏度
- 可视化：用 quiver 画速度场，用颜色画涡度 $\omega = \nabla \times \vec{u}$
</details>

## Next Steps

流体之后是场。挑战 09 将用 **FDTD** 方法直接求解麦克斯韦方程组，看到电磁波从你的代码里发出来。

→ [前往挑战 09：Electromagnetism](../09-electromagnetism/README.md)
