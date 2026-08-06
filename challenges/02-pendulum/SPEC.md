**简体中文** | [**English**](SPEC.en.md)

# SPEC 02 · Pendulum

> 本文件的验收标准可被自动化测试。实现需通过以下全部标准。

## 测试环境

- 语言：Python 3.8+
- 依赖：仅标准库（`math`），可视化可用 Matplotlib（非必需）
- 参数默认值：$L = 1.0$ m，$\theta_0 = 30°$，$\omega_0 = 0$，$\Delta t = 0.01$ s，$t_{max} = 20$ s

## 验收标准

### S2.1 接口

- [ ] 提供 `simulate_euler(L, theta0, omega0, dt, t_max)`，返回 `(times, thetas, omegas)`
- [ ] 提供 `simulate_euler_cromer(L, theta0, omega0, dt, t_max)`，返回 `(times, thetas, omegas)`
- [ ] 返回的三个列表长度相等，`times[0] = 0`，`thetas[0] = theta0`，`omegas[0] = omega0`

### S2.2 运动范围（小角度）

- [ ] 默认参数（$\theta_0 = 30°$）下，`max(thetas) <= theta0 + 0.01`（摆角不超出初始幅值，无发散）
- [ ] 摆角随时间做周期变化：存在 $T_{osc} < 5$ s 使 $\theta(t + T_{osc}) \approx \theta(t)$（误差 < 0.1 rad）

### S2.3 周期近似（小角度理论）

- [ ] 小角度（$\theta_0 = 5°$）下，测得周期 $T_{sim}$ 与理论值 $T = 2\pi\sqrt{L/g} \approx 2.007$ s 的相对误差 < 2%

> 说明：这是**数值积分正确性**的核心检验——如果你的积分器对，小角度周期必然接近理论值。

### S2.4 能量行为（两种方法的本质区别）

设能量 $E(t) = \frac{1}{2}L^2\omega(t)^2 + gL(1 - \cos\theta(t))$（单位质量，$m=1$），$E_0 = E(0)$：

- [ ] **欧拉法**：$t = 20$ s 时，$\frac{E(20) - E_0}{E_0} > 5\%$（能量显著漂移，通常为增长）
- [ ] **欧拉-克罗默法**：$t = 20$ s 时，$\frac{|E(20) - E_0|}{E_0} < 1\%$（能量近似守恒）
- [ ] 欧拉法能量漂移方向为**增长**（$E(20) > E_0$），欧拉-克罗默法无明显漂移

> 说明：这两条是**最关键**的验收——它们让学习者亲眼看到「数值方法会在物理上撒谎」。

### S2.5 收敛性（可选，进阶）

- [ ] 欧拉法：$\Delta t$ 减半后，$t = 10$ s 时角度误差约减半（一阶精度）
- [ ] 欧拉-克罗默法：能量漂移随 $\Delta t$ 减小而减小

## 测试数据

| 参数 | 默认值 |
|------|--------|
| $L$ | 1.0 m |
| $\theta_0$ | 30°（≈ 0.5236 rad） |
| $\omega_0$ | 0 |
| $\Delta t$ | 0.01 s |
| $t_{max}$ | 20 s |

## 参考解

参考实现见 `solutions` 分支：`challenges/02-pendulum/solutions/pendulum_solution.py`

---

*验收标准基于无摩擦单摆模型。能量守恒检验是理解数值方法稳定性的关键。*
