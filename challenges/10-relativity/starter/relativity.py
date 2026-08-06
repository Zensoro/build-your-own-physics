"""狭义相对论：洛伦兹变换与时空间隔。

任务：补全 TODO 部分，让所有函数正确实现并通过 verify.py 验收。
用四元组 (ct, x, y, z) 表示事件（c=1 自然单位，ct 与 x 同单位）。
本挑战不需要 numpy，只用标准库 math。
运行：python verify.py（验收）或 python relativity.py（看演示）
"""

import math


def gamma(v):
    """洛伦兹因子 γ = 1/√(1-v²)，v 以光速为单位（0 ≤ v < 1）。"""
    # TODO: 返回 1 / sqrt(1 - v*v)
    # 提示：v=0 → γ=1；v→1 → γ→∞
    pass  # ← 替换这一行


def lorentz(event, v):
    """沿 x 轴以速度 v（单位 c）运动的 S' 系中看到的同一事件。

    Args:
        event: (ct, x, y, z) 四元组
        v:     相对速度（以 c 为单位，0 ≤ v < 1）
    Returns:
        (ct', x', y', z') 四元组
    """
    ct, x, y, z = event
    g = gamma(v)
    # TODO: 洛伦兹变换
    # ct' = g * (ct - v*x)
    # x'  = g * (x - v*ct)
    # y'  = y, z' = z
    pass  # ← 替换这一行


def inverse_lorentz(event, v):
    """逆变换（S' → S），等价于以 -v 变换。"""
    return lorentz(event, -v)


def spacetime_interval(event_a, event_b):
    """时空间隔 s² = (cΔt)² - Δx² - Δy² - Δz²（事件对）。"""
    # TODO: 返回两事件之间的时空间隔平方
    pass  # ← 替换这一行


def time_dilation(delta_tau, v):
    """固有时 Δτ 在 S 系中测得为 Δt = γ·Δτ（钟慢）。"""
    return gamma(v) * delta_tau


def length_contraction(L0, v):
    """固有长度 L0 在 S 系中测得为 L = L0/γ（尺缩）。"""
    return L0 / gamma(v)


if __name__ == "__main__":
    v = 0.6
    print(f"γ(0.6c) = {gamma(v):.6f}")
    print(f"钟慢：Δτ=1s → {time_dilation(1.0, v):.4f} s")
    print(f"尺缩：L0=1m → {length_contraction(1.0, v):.4f} m")
    ct, x = 5.0, 5.0
    ct_p, x_p, _, _ = lorentz((ct, x, 0.0, 0.0), v)
    print(f"光信号变换后 v' = {x_p/ct_p:.6f}（应为 1 = c）")
