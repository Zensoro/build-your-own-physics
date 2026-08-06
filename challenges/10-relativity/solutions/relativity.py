"""挑战 10 · Relativity — 参考实现（洛伦兹变换 + 时空间隔）。

用四元组 (ct, x, y, z) 表示事件（c=1 时 ct 与 x 同单位，几何更清晰）。
本挑战不需要 numpy，只用标准库 math。
被 verify.py import 时无任何第三方依赖。
"""

import math

C = 299792458.0  # m/s（仅用于展示；内部用 c=1 自然单位）


def gamma(v):
    """洛伦兹因子 γ = 1/√(1-v²)，v 以光速为单位（0 ≤ v < 1）。"""
    return 1.0 / math.sqrt(1.0 - v * v)


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
    ct_new = g * (ct - v * x)
    x_new = g * (x - v * ct)
    return (ct_new, x_new, y, z)


def inverse_lorentz(event, v):
    """逆变换（S' → S），等价于以 -v 变换。"""
    return lorentz(event, -v)


def spacetime_interval(event_a, event_b):
    """时空间隔 s² = (cΔt)² - Δx² - Δy² - Δz²（事件对）。"""
    dct = event_a[0] - event_b[0]
    dx = event_a[1] - event_b[1]
    dy = event_a[2] - event_b[2]
    dz = event_a[3] - event_b[3]
    return dct * dct - dx * dx - dy * dy - dz * dz


def time_dilation(delta_tau, v):
    """固有时 Δτ 在 S 系中测得为 Δt = γ·Δτ（钟慢）。"""
    return gamma(v) * delta_tau


def length_contraction(L0, v):
    """固有长度 L0 在 S 系中测得为 L = L0/γ（尺缩）。"""
    return L0 / gamma(v)


if __name__ == "__main__":
    # 演示：v=0.6c 的 γ、光速不变、间隔不变
    v = 0.6
    print(f"γ(0.6c) = {gamma(v):.6f}")
    print(f"钟慢：Δτ=1s 的固有时在 S 系 = {time_dilation(1.0, v):.4f} s")
    print(f"尺缩：L0=1m 的杆在 S 系 = {length_contraction(1.0, v):.4f} m")

    # 光速不变：一个沿 x 以 c 传播的光信号 (t, x=c·t) 变换后仍以 c 传播
    ct, x = 5.0, 5.0          # 光信号事件 (c=1)
    ct_p, x_p, _, _ = lorentz((ct, x, 0.0, 0.0), v)
    print(f"光信号 S 系 (ct,x)=({ct},{x}) → S' 系 ({ct_p:.4f},{x_p:.4f})，"
          f"v' = x'/ct' = {x_p/ct_p:.6f}（应为 1 = c）")
