#!/usr/bin/env bash
# check-blog-sync.sh - 公式 sitemap のブログ記事と blog-index.tsv の差分を表示する（手動のみ。CI では実行しない）
#
# 使用方法:
#   ./scripts/kiro-all-docs/check-blog-sync.sh
#
# 規則（作業計画 §9-1 `blog-sync`・F7）:
#   https://kiro.dev/sitemap.xml の /blog/ 配下（page/N・feed を除く）を正とし、
#   scripts/kiro-all-docs/blog-index.tsv の slug 集合と比較する。
#   差分があれば一覧表示して exit 1。無ければ exit 0。
#   ネットワークに出るため CI には組み込まない。
set -u
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TSV="$ROOT/scripts/kiro-all-docs/blog-index.tsv"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

if ! curl -sSL -A "Mozilla/5.0" --max-time 30 https://kiro.dev/sitemap.xml -o "$TMP/sitemap.xml"; then
  echo "NG: sitemap.xml を取得できない"; exit 1
fi
grep -oE 'https://kiro\.dev/blog/[a-z0-9./-]+' "$TMP/sitemap.xml" \
  | sed 's|https://kiro.dev/blog/||; s|/$||' \
  | grep -vE '^(page/[0-9]+|feed.*)?$' | sort -u > "$TMP/remote.txt"
tail -n +2 "$TSV" | cut -f2 | sort -u > "$TMP/local.txt"

R=$(wc -l < "$TMP/remote.txt"); L=$(wc -l < "$TMP/local.txt")
echo "sitemap: $R 本 / blog-index.tsv: $L 本"
ADD=$(comm -23 "$TMP/remote.txt" "$TMP/local.txt")
DEL=$(comm -13 "$TMP/remote.txt" "$TMP/local.txt")
rc=0
if [ -n "$ADD" ]; then
  echo "--- sitemap にあり TSV に無い（追記候補）:"; echo "$ADD" | sed 's|^|  https://kiro.dev/blog/|; s|$|/|'; rc=1
fi
if [ -n "$DEL" ]; then
  echo "--- TSV にあり sitemap に無い（削除・移転の確認が必要）:"; echo "$DEL" | sed 's|^|  |'; rc=1
fi
[ $rc -eq 0 ] && echo "OK: 差分なし"
exit $rc
