**简体中文** | [**English**](README.en.md)

# Challenge 06 · Heat Engine

> **从扩散方程到卡诺循环：热力学第二定律的代码之证。**

> 需要：数组操作 + 挑战 05 的经验。
> 🎓 有 AI 导师：[ai/tutor.md](ai/tutor.md)

## Why This Challenge

热扩散方程是物理模拟的另一个支柱。你会看到"热量从高温流向低温"在格点上自然发生——然后把它升级成一个真正的**热机**，跑出卡诺循环。

## Physics Background

### 热扩散方程

$$ \frac{\partial T}{\partial t} = \alpha \nabla^2 T $$

其中 $\alpha$ 是热扩散系数。这是**抛物型**方程（波动方程是双曲型），数值格式和要求完全不同。

### 显式 FTCS

$$ T_i^{n+1} = T_i^n + \frac{\alpha \Delta t}{\Delta x^2} (T_{i+1}^n - 2T_i^n + T_{i-1}^n) $$

稳定性条件：$\frac{\alpha \Delta t}{\Delta x^2} \le \frac{1}{2}$。

### 热机与卡诺循环

一个热机在高温热源 $T_H$ 和低温热源 $T_C$ 之间工作，最大效率为卡诺效率：

$$ \eta = 1 - \frac{T_C}{T_H} $$

## Your Task

1. 实现一维热扩散模拟（FTCS 格式）
2. 验证：初始为阶梯温度分布，随时间平滑成直线（热平衡）
3. 绘制温度-时间演化，观察热流方向（第二定律的体现）
4. （进阶）二维热扩散，模拟"热源+散热器"，计算稳态温度场
5. （挑战）模拟一个简单的热机循环（等温 + 绝热），测量效率并与卡诺效率对比

### 完成后的检查

- [ ] 初始阶梯分布 → 最终线性分布（热平衡）
- [ ] 热流永远从高温流向低温（第二定律）
- [ ] 显式格式在 $\alpha\Delta t/\Delta x^2 > 0.5$ 时数值不稳定
- [ ] 热机效率 ≤ 卡诺效率

## Hints

<details>
<summary>展开查看提示</summary>

- 注意：扩散方程的稳定条件是 $\alpha\Delta t/\Delta x^2 \le 1/2$，与波的 CFL 条件不同
- 热平衡后温度梯度是线性的（一维）、满足拉普拉斯方程（二维）
- 隐式格式（Crank-Nicolson）无条件稳定，但需要解线性方程组——进阶挑战
- 卡诺循环的等温过程用玻意耳定律，绝热过程用泊松方程
</details>

## Next Steps

热力学之后，回到动力学——但这次是**混沌**。挑战 07 的双摆是"确定性系统不可预测"的经典演示。

→ [前往挑战 07：Double Pendulum](../07-double-pendulum/README.md)
