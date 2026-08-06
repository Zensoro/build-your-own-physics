**简体中文** | [**English**](README.en.md)
# Challenge 09 · Electromagnetism

> **麦克斯韦方程组的代码之舞：发射一束电磁波。**

> 需要：数组操作 + 挑战 05 的经验。
> 🎓 有 AI 导师：[ai/tutor.md](ai/tutor.md)


## Why This Challenge

麦克斯韦方程组是物理学的皇冠之一。用 **FDTD（时域有限差分）** 方法，你可以在格点上直接求解它，亲眼看到电场和磁场相互激发、以光速传播——一束电磁波从你的代码里诞生。

## Physics Background

### 一维麦克斯韦方程组（无源）

$$ \frac{\partial E_x}{\partial t} = -\frac{1}{\epsilon_0}\frac{\partial H_y}{\partial z}, \quad \frac{\partial H_y}{\partial t} = -\frac{1}{\mu_0}\frac{\partial E_x}{\partial z} $$

### 交错网格（Yee 网格）

FDTD 的精髓：$E$ 和 $H$ 在**空间上交错半个格点**，在**时间上交错半个步长**：

```
E 场在整数格点、整数时间
H 场在半格点、半时间
```

这种交错让差分格式天然稳定，且满足 $c = 1/\sqrt{\epsilon_0\mu_0}$。

## Your Task

1. 实现一维 FDTD（Yee 网格）
2. 在边界注入一个高斯脉冲（或正弦波），观察它以光速传播
3. 观察**阻抗匹配**：脉冲穿过不同介电常数介质时，部分反射、部分透射
4. （进阶）二维 FDTD：模拟点源的圆形波前扩散
5. （挑战）模拟**金属边界**的全反射，观察驻波

### 完成后的检查

- [ ] 高斯脉冲以速度 $c = 3\times10^8$ m/s 传播
- [ ] 介质界面处反射系数 $R$ 与理论值 $\left(\frac{Z_1 - Z_2}{Z_1 + Z_2}\right)^2$ 一致
- [ ] 波形在传播中不变形（无耗散、无色散）
- [ ] CFL 条件 $c\Delta t / \Delta z \le 1$ 被破坏时数值爆炸

## Hints

<details>
<summary>展开查看提示</summary>

- Yee 网格更新公式（一维）：
  - $E_x^{n+1}(k) = E_x^n(k) - \frac{\Delta t}{\epsilon_0 \Delta z}(H_y^{n+1/2}(k+1/2) - H_y^{n+1/2}(k-1/2))$
  - $H_y^{n+1/2}(k+1/2) = H_y^{n-1/2}(k+1/2) - \frac{\Delta t}{\mu_0 \Delta z}(E_x^n(k+1) - E_x^n(k))$
- 用 `numpy.roll` 实现空间差分，快且简洁
- 吸收边界：简单用 ABC（一阶 Mur），进阶用 PML
- 波动方程里 $c$ 和 $Z$ 都从 $\epsilon, \mu$ 得出：$c = 1/\sqrt{\epsilon\mu}$，$Z = \sqrt{\mu/\epsilon}$
</details>

## Next Steps

牛顿力学之后是爱因斯坦。挑战 10 将用**洛伦兹变换**直接操作时空，亲眼看到尺缩、钟慢和光速不变。

→ [前往挑战 10：Relativity](../10-relativity/README.md)
