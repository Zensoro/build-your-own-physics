**简体中文** | [**English**](README.en.md)

# Challenge 05 · Wave Machine

> **让波在格点上奔跑：从波动方程到驻波与干涉。**

> 需要：数组操作（NumPy）+ 挑战 04 的经验。
> 🎓 有 AI 导师：[ai/tutor.md](ai/tutor.md)

## Why This Challenge

波无处不在——声、光、水、地震。你将从**波动方程**出发，在一个格点上模拟波的真实传播，亲眼看到驻波、干涉和边界反射。

## Physics Background

### 一维波动方程

$$ \frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2} $$

其中 $u(x,t)$ 是位移，$c$ 是波速。

### 离散化（FTCS 格式）

把空间离散成格点 $x_i = i \Delta x$，时间离散成 $t_n = n \Delta t$：

$$ u_i^{n+1} = 2u_i^n - u_i^{n-1} + \left(\frac{c\Delta t}{\Delta x}\right)^2 (u_{i+1}^n - 2u_i^n + u_{i-1}^n) $$

这个格式叫**蛙跳格式（leapfrog in time）**。稳定条件是 $c\Delta t / \Delta x \le 1$（CFL 条件）。

## Your Task

1. 实现一维波动方程模拟（FTCS 格式）
2. 初始条件给一个高斯波包，观察它向两侧传播
3. 观察**边界反射**（固定端 vs 自由端）
4. （进阶）双缝干涉：两个波源产生的干涉图案

### 完成后的检查

- [ ] 高斯波包分裂成两个波包，向左右传播
- [ ] 波速 = $c$（测量波峰移动距离/时间）
- [ ] 固定端反射时**相位反转**，自由端反射时**相位不变**
- [ ] 改变 $\Delta t$，当 $c\Delta t/\Delta x > 1$ 时数值爆炸（验证 CFL 条件）

## Hints

<details>
<summary>展开查看提示</summary>

- 需要两个时间层 $u^{n-1}$ 和 $u^n$ 来推进到 $u^{n+1}$
- 边界处理：固定端 $u=0$，自由端 $\partial u/\partial x = 0$
- 用 matshow / imshow 的 `vmin=-1, vmax=1` 固定颜色范围，方便观察
- 能量 = $\sum (\partial u/\partial t)^2 + c^2(\partial u/\partial x)^2$ 应大致守恒
</details>

## Next Steps

波动方程是"场"的第一次接触。挑战 06 转向热力学——但你会发现，热扩散方程和波动方程长得像亲兄弟。

→ [前往挑战 06：Heat Engine](../06-heat-engine/README.md)
