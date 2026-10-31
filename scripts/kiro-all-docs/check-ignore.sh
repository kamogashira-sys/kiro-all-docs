#!/usr/bin/env bash
# 公開範囲の機械検証（作業計画書 0-3 / 2-3 / 2-5）
#
# ローカル管理対象が .gitignore で除外されていること、および
# 公開対象が誤って除外されていないことを機械確認する。
#
# 使い方: make check-kiro-web-ignore  または  scripts/kiro-all-docs/check-ignore.sh
set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT" || exit 1

fail=0

# ローカル管理対象（GitHub 非公開）: ignore されていなければ NG
LOCAL_ONLY=(
  "work_plans/x_plan.md"
  "work_plans/202611010705_作業計画書_Kiroまとめサイト.md"
  "06_embedded-docs/x.html"
  "06_embedded-docs/blog/one-agent.html"
  "work_records/20260801/x_worklog.md"
  "x_update_plan.md"
  "kiro-all-docs/01_story/x_plan.md"
  ".claude/settings.local.json"
  ".kiro/settings/mcp.json"
)

# 公開対象: ignore されていたら NG
PUBLIC=(
  "README.md"
  "LICENSE"
  "CODE_OF_CONDUCT.md"
  ".github/ISSUE_TEMPLATE/bug_report.yml"
  ".github/ISSUE_TEMPLATE/config.yml"
  ".github/pull_request_template.md"
  ".github/workflows/validate-kiro-all-docs.yml"
  "kiro-all-docs/README.md"
  "kiro-all-docs/00_start/03_get-started.md"
  "kiro-all-docs/01_story/02_one-agent.md"
  "kiro-all-docs/01_story/03_cli-journey.md"
  "kiro-all-docs/02_why-kiro-cli/01_why-i-love-kiro-cli.md"
  "scripts/kiro-all-docs/check-ignore.sh"
  "Makefile"
)

echo "=== ローカル管理対象が除外されていることを確認 ==="
for p in "${LOCAL_ONLY[@]}"; do
  if git check-ignore -q "$p"; then
    echo "  OK   ignored: $p"
  else
    echo "  FAIL not ignored: $p"
    fail=1
  fi
done

echo "=== 公開対象が除外されていないことを確認 ==="
for p in "${PUBLIC[@]}"; do
  if git check-ignore -q "$p"; then
    echo "  FAIL wrongly ignored: $p"
    fail=1
  else
    echo "  OK   publishable: $p"
  fi
done

echo "=== コミット済みツリーにローカル管理対象が含まれていないことを確認 ==="
tracked=$(git ls-files | grep -E "work_plans/|06_embedded-docs/|work_records/|_plan\.md$|_作業計画書_" || true)
if [ -n "$tracked" ]; then
  echo "  FAIL 以下がトラックされています:"
  echo "$tracked" | sed 's/^/    /'
  fail=1
else
  echo "  OK   local-only files are not tracked"
fi

echo "=== 公開ファイルにローカル絶対パス・ユーザー名が含まれていないことを確認 ==="
# 対象は git が追跡する（＝公開される）ファイルのみ。バイナリは除外。
leak=$(git ls-files -z | xargs -0 -r grep -n -I -E '/home/[a-z_][a-z0-9_-]*|/Users/[A-Za-z0-9_-]+' 2>/dev/null || true)
if [ -n "$leak" ]; then
  echo "  FAIL ローカル絶対パスらしい記述があります:"
  echo "$leak" | sed 's/^/    /'
  fail=1
else
  echo "  OK   no local absolute paths in tracked files"
fi

if [ "$fail" -eq 0 ]; then
  echo "=== 結果: すべて OK ==="
else
  echo "=== 結果: 失敗あり（公開してはいけない状態） ==="
fi
exit "$fail"
