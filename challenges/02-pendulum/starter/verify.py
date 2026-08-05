"""挑战 02 自动验收。运行：python verify.py"""

import math
import sys

sys.path.insert(0, ".")
from pendulum import simulate_euler, simulate_euler_cromer, energy

G = 9.81
L, theta0, omega0, dt, t_max = 1.0, math.radians(30.0), 0.0, 0.01, 20.0

passed = []
failed = []


def check(name, cond):
    if cond:
        passed.append(name)
        print(f"  ✓ {name}")
    else:
        failed.append(name)
        print(f"  ✗ {name}")


print("=== S2.1 接口 ===")
t_e, th_e, om_e = simulate_euler(L, theta0, omega0, dt, t_max)
t_c, th_c, om_c = simulate_euler_cromer(L, theta0, omega0, dt, t_max)
check("返回长度相等 (欧拉)", len(t_e) == len(th_e) == len(om_e) > 0)
check("返回长度相等 (欧拉-克罗默)", len(t_c) == len(th_c) == len(om_c) > 0)
check("初始条件正确", abs(th_e[0] - theta0) < 1e-12 and abs(om_e[0]) < 1e-12)

print("=== S2.2 运动范围（小角度不发散） ===")
check("欧拉法摆角未爆掉", max(abs(a) for a in th_e) < 10.0)
check("欧拉-克罗默摆角未爆掉", max(abs(a) for a in th_c) < 10.0)

print("=== S2.3 小角度周期 ===")
t5, th5, _ = simulate_euler_cromer(L, math.radians(5.0), 0.0, 0.001, 10.0)
zero_crossings = sum(1 for i in range(1, len(th5)) if th5[i - 1] * th5[i] < 0)
T_sim = 10.0 / max(zero_crossings / 2, 1) if zero_crossings >= 2 else 0.0
T_theory = 2 * math.pi * math.sqrt(L / G)
check(f"小角度周期 {T_sim:.3f}s ≈ 理论 {T_theory:.3f}s (误差<2%)",
      abs(T_sim - T_theory) / T_theory < 0.02)

print("=== S2.4 能量行为 ===")
E0 = energy(L, [theta0], [0.0])[0]
Ee = energy(L, th_e, om_e)
Ec = energy(L, th_c, om_c)
drift_e = (Ee[-1] - E0) / E0
drift_c = (Ec[-1] - E0) / E0
check(f"欧拉法能量漂移 {drift_e:+.2%} > +5% (确实在撒谎)",
      drift_e > 0.05)
check(f"欧拉-克罗默能量漂移 {drift_c:+.2%} < 1% (守恒)",
      abs(drift_c) < 0.01)
check("欧拉法漂移方向是增长 (E 增加)", drift_e > 0)

print(f"\n通过 {len(passed)} / {len(passed) + len(failed)}")
if failed:
    print("未通过:", ", ".join(failed))
    sys.exit(1)
print("🎉 全部通过！去挑战 03 吧！")
