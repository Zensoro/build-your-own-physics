# Visualization Guide — 让物理"看得见"

> 物理模拟的一半价值在可视化。这里给出每个挑战的推荐画法。

## 快速参考

| 挑战 | 数据 | 推荐可视化 | 工具 |
|------|------|-----------|------|
| 01 抛体 | 轨迹 (x, y) | 散点/折线图 | Matplotlib |
| 02 单摆 | 相空间 (θ, ω) | 相图 + 能量-时间 | Matplotlib |
| 03 轨道 | 轨迹 (x, y) | 折线 + 太阳标记 | Matplotlib |
| 04 N体 | 粒子位置 | 动画散点图 | Matplotlib.animation |
| 05 波 | 位移 u(x,t) | imshow 时空图 | Matplotlib |
| 06 热 | 温度 T(x,t) | imshow 时空图 | Matplotlib |
| 07 双摆 | 摆臂轨迹 | 折线动画 | Matplotlib.animation |
| 08 流体 | 速度场 (u,v) | quiver + 涡度云图 | Matplotlib |
| 09 电磁 | 场 E,H(z,t) | 双线图（E 和 H 叠画） | Matplotlib |
| 10 相对论 | 时空图 | 世界线 + 光锥 | Matplotlib |
| 11 量子 | |ψ|² | imshow 动画 | Matplotlib |
| 12 太阳系 | 行星轨道 | 动画散点 + 轨迹尾迹 | Matplotlib |

## 三大原则

### 1. 固定颜色范围
用 `vmin=-1, vmax=1` 固定 imshow 的颜色范围，否则每个时间步颜色都会重映射，波形看起来在"呼吸"。

### 2. 比例要真实
轨道图用 `plt.axis("equal")`，否则椭圆会被拉变形。抛体图同理。

### 3. 动起来
静态图只能看到"结果"，动画才能看到"过程"。用 `matplotlib.animation.FuncAnimation`：

```python
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

def update(frame):
    line.set_data(xs[:frame], ys[:frame])
    return line,

anim = FuncAnimation(fig, update, frames=len(xs), interval=20)
plt.show()
```

## 工具选择

| 工具 | 优势 | 劣势 | 适合 |
|------|------|------|------|
| Matplotlib | 万能、教学清晰 | 交互弱 | 默认选择 |
| Plotly | 交互缩放、3D | 依赖浏览器 | 3D 轨道、复杂交互 |
| Manim (3Blue1Brown) | 数学之美、可做视频 | 学习曲线陡 | 做教学视频 |
| p5.js / Three.js | 浏览器实时交互 | 需前端知识 | 网页版模拟 |
| napari / itk | 科研图像 | 领域专用 | 生物图像（跨学科） |

## 进阶：让可视化"讲道理"

- **叠加理论线**：把解析解画成虚线，和你的数值解对比——差异就是数值误差
- **动画+仪表盘**：同屏显示"能量仪表"和"轨迹"，观察能量漂移
- **交互参数**：用滑块实时调初始条件（`matplotlib.widgets.Slider`），物理直觉翻倍

## 延伸阅读

- Matplotlib 官方画廊（gallery）— 找灵感的第一站
- 3Blue1Brown 的动画引擎 Manim — 理解"如何用可视化讲物理"
