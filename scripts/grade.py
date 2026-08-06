#!/usr/bin/env python3
"""统一的挑战自动评分脚本。

用法：
    python scripts/grade.py 01-projectile
    python scripts/grade.py 01-projectile 02-pendulum 03-orbit

逻辑：
    1. 对每个挑战，检查 starter/ 下是否有学习者填写的代码（非 TODO 版本）
    2. 有 → 用学习者的实现跑 verify.py（GitHub PR 场景）
    3. 没有 → 用 solutions/ 参考实现临时覆盖 starter，跑 verify.py
             （回归测试：确保 verify.py 本身是正确的，main 分支演示用）

退出码：全部通过返回 0，任一失败返回 1（供 CI 判断）。
"""

import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHALLENGES_DIR = os.path.join(ROOT, "challenges")


def grade_one(challenge_id):
    """评分单个挑战，返回 (挑战名, 通过与否, 输出摘要)。"""
    ch_dir = os.path.join(CHALLENGES_DIR, challenge_id)
    starter_dir = os.path.join(ch_dir, "starter")
    solutions_dir = os.path.join(ch_dir, "solutions")

    if not os.path.isdir(starter_dir):
        return challenge_id, False, "starter/ 目录不存在"

    # 找到 verify.py 会 import 的模块（starter 里的 .py 文件，去掉 verify.py 自身）
    modules = [f for f in os.listdir(starter_dir)
               if f.endswith(".py") and f not in ("verify.py", "__init__.py")]

    use_solution = False
    for mod in modules:
        mod_path = os.path.join(starter_dir, mod)
        content = open(mod_path, encoding="utf-8").read()
        if "TODO" in content:
            use_solution = True
            break

    if use_solution:
        # 学习者还没填：用参考实现做回归测试
        # 把 solutions 的模块复制到临时目录，连同 verify.py 一起跑
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copy(os.path.join(starter_dir, "verify.py"), tmp)
            for mod in modules:
                sol_mod = os.path.join(solutions_dir, mod)
                if os.path.isfile(sol_mod):
                    shutil.copy(sol_mod, tmp)
                else:
                    # 缺参考实现：复制 starter 原样（可能因 TODO 失败，但至少可跑）
                    shutil.copy(os.path.join(starter_dir, mod), tmp)
            proc = subprocess.run(
                [sys.executable, "verify.py"], cwd=tmp,
                capture_output=True, text=True)
        mode = "回归测试（solutions）"
    else:
        # 学习者已填写：直接测 starter
        proc = subprocess.run(
            [sys.executable, "verify.py"], cwd=starter_dir,
            capture_output=True, text=True)
        mode = "学习者代码（starter）"

    passed = proc.returncode == 0
    lines = [l for l in proc.stdout.strip().splitlines() if l.strip()]
    tail = lines[-6:] if lines else ["(无输出)"]
    summary = "\n".join(tail)
    if not passed and proc.stderr.strip():
        summary += "\n[stderr] " + proc.stderr.strip().splitlines()[-1]
    return challenge_id, passed, f"[{mode}]\n{summary}"


def main():
    challenges = sys.argv[1:] or [
        "01-projectile", "02-pendulum", "03-orbit", "04-nbody",
        "05-wave-machine", "06-heat-engine", "07-double-pendulum",
        "08-fluid", "09-electromagnetism", "10-relativity",
        "11-quantum", "12-solar-system",
    ]
    all_pass = True
    print("=" * 60)
    print("Build Your Own Physics · 挑战自动评分")
    print("=" * 60)
    for ch in challenges:
        print(f"\n>>> 评分 {ch}")
        cid, passed, summary = grade_one(ch)
        print(summary)
        if not passed:
            all_pass = False
            if proc_has_error(summary):
                print(f"    [ERROR] {ch} 未通过")
    print("\n" + "=" * 60)
    print(f"结果: {'✅ 全部通过' if all_pass else '❌ 存在失败'}")
    print("=" * 60)
    sys.exit(0 if all_pass else 1)


def proc_has_error(summary):
    return "Error" in summary or "Traceback" in summary


if __name__ == "__main__":
    main()
