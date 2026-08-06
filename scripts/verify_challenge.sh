#!/usr/bin/env bash
# 验证指定挑战：在临时目录用 solutions 覆盖跑 verify.py（不碰仓库 starter）
# 用法: bash verify_challenge.sh <challenge_id> [python_bin]
set -e
CH="$1"
PY="${2:-/Users/zen/.workbuddy/binaries/python/envs/default/bin/python}"
ROOT="/Users/zen/WorkBuddy/2026-08-05-21-36-54/outputs/build-your-own-physics"
SRC="$ROOT/challenges/$CH"

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

cp "$SRC"/starter/*.py "$TMP/"
# solutions 覆盖同名模块（模拟学习者完成）
for f in "$SRC"/solutions/*.py; do
  cp "$f" "$TMP/$(basename "$f")"
done

cd "$TMP"
"$PY" verify.py
