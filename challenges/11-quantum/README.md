# Challenge 11 · Quantum

> **波函数是真实的：求解薛定谔方程。**

> 需要：复数基础（可以当作黑盒）+ 挑战 05 的经验。
> 🎓 有 AI 导师：[ai/tutor.md](ai/tutor.md)

## Why This Challenge

量子力学反直觉，但它的核心方程——**含时薛定谔方程**——是一个可以精确数值求解的偏微分方程。你会看到波函数干涉、隧穿、以及测量时的"坍缩"（如果做测量模拟）。

## Physics Background

### 含时薛定谔方程（一维）

$$ i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2} + V(x)\psi $$

其中 $\psi(x,t)$ 是复值波函数，$|\psi|^2$ 是概率密度。

### 分裂算符法（Split-Operator Method）

利用 $\hat{T}$（动能）和 $\hat{V}$（势能）在动量空间和坐标空间分别是对角算子：

1. 半个时间步：在坐标空间作用 $e^{-iV\Delta t/2\hbar}$
2. 整个时间步：在动量空间作用 $e^{-i\hat{T}\Delta t/\hbar}$（FFT 来回切换）
3. 半个时间步：再作用 $e^{-iV\Delta t/2\hbar}$

$$ \psi(t + \Delta t) \approx e^{-iV\Delta t/2\hbar} e^{-i\hat{T}\Delta t/\hbar} e^{-iV\Delta t/2\hbar}\psi(t) $$

这个方法的精度是 $O(\Delta t^3)$，且**自动保持** $\int|\psi|^2 dx = 1$（概率守恒）。

### 量子隧穿

当粒子能量 $E < V_0$（势垒高度）时，经典物理说它过不去——但量子力学说它**有可能**过去。隧穿概率随势垒宽度指数衰减。

## Your Task

1. 实现分裂算符法求解一维含时薛定谔方程
2. 模拟一个高斯波包在自由空间的传播——观察它**展宽**（位置不确定性增大）
3. 模拟波包遇到**方势垒**：观察透射波 + 反射波（隧穿！）
4. 验证概率守恒：$\int|\psi|^2 dx = 1$ 始终成立
5. （进阶）有限方势阱的束缚态：初始猜测波函数，观察它演化成能量本征态

### 完成后的检查

- [ ] 自由波包宽度随时间增大（$\Delta x \propto t$ 渐近）
- [ ] 穿过势垒后，透射概率随势垒宽度/高度指数衰减
- [ ] $\int|\psi|^2 dx$ 在 1 万步后仍在 1 ± 0.001
- [ ] 能量期望值 $\langle E \rangle$ 守恒
- [ ] 波函数在势垒处连续（边界条件自动满足）

## Hints

<details>
<summary>展开查看提示</summary>

- 用 FFT（`numpy.fft.fft` / `ifft`）在坐标与动量空间切换
- 动量空间的动能算子：$\hat{T} \to \hbar^2 k^2 / 2m$
- 波包初始条件：$\psi(x,0) = (2\pi\sigma^2)^{-1/4} e^{ik_0 x} e^{-(x-x_0)^2/4\sigma^2}$
- 势垒：$V(x) = V_0$（$x \in [a,b]$），否则 0
- 画 $|\psi|^2$ 的演化（matplotlib animation 或 imshow）
- 单位：用 $\hbar = 1, m = 1$ 的自然单位，数字更友好
</details>

## Next Steps

你已经完成了从经典到量子的全部核心模拟。挑战 12 把所有工具合而为一：**从零构建一个太阳系**。

→ [前往挑战 12：Solar System](../12-solar-system/README.md)
