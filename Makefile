# Makefile - kiro-all-docs 検証ツール一括実行
#
# 使用方法:
#   make                          # ヘルプを表示
#   make check-kiro-all-quick     # 執筆中の常用（links / notation）
#   make check-kiro-all-all       # コミット前・公開前（ネットワーク不要のもの全部）
#   make check-kiro-all-ignore    # 公開範囲チェック（コミット前に必須・exit 0 必須）
#
# ⚠ 「exit 0」は「検証して合格した」を必ずしも意味しません:
#   - 外部依存のターゲット（-urls / -urls-important / -blog-sync）は all に含まれません
#   - first-person は**警告のみ**で終了コードを変えません（人が目視で判断する）
#   検証スクリプトを新規作成・改修したときは、意図的に文書を壊して検出されることを
#   確認してください（ネガティブテスト）。
#
# 📌 存在しないターゲットは書きません（実装済みのものだけを並べます）。
#    未実装分はヘルプの「未実装」に列挙しています。

.DEFAULT_GOAL := help

.PHONY: help \
        check-kiro-all-all check-kiro-all-quick check-kiro-all-ignore \
        check-kiro-all-links check-kiro-all-notation \
        check-kiro-all-sources check-kiro-all-quotes check-kiro-all-first-person \
        check-kiro-all-urls check-kiro-all-urls-important \
        check-kiro-all-blog-index-count check-kiro-all-blog-sync gen-kiro-all-blog-index

SCRIPTS := ./scripts/kiro-all-docs

help:
	@echo "=== kiro-all-docs 検証ツール ==="
	@echo ""
	@echo "まとめて実行:"
	@echo "  make check-kiro-all-all            # 全チェック（ネットワーク不要のもの全部）"
	@echo "  make check-kiro-all-quick          # 高速チェック（links / notation。執筆中の確認用）"
	@echo "  make check-kiro-all-ignore         # 公開範囲チェック（コミット前に必須）"
	@echo ""
	@echo "個別に実行（ネットワーク不要）:"
	@echo "  make check-kiro-all-links          # 内部リンク実在＋アンカー（日本語含む）＋kiro.dev URL 書式"
	@echo "  make check-kiro-all-notation       # 表記規約（製品名の揺れ・非 ISO 日付・取得日・禁止表現・所属語句）"
	@echo "  make check-kiro-all-sources        # H2 節ごとの出典リンクの有無（00_start / 01_story / 03_reference）"
	@echo "  make check-kiro-all-quotes         # 英文引用が 1 箇所 30 語以内"
	@echo "  make check-kiro-all-first-person   # 🐾 ブロック外の一人称・推し表現（警告のみ・exit 0）"
	@echo ""
	@echo "外部サイトに依存（all には含めない）:"
	@echo "  make check-kiro-all-urls           # 公開文書の外部 URL の到達性（全件）"
	@echo "  make check-kiro-all-urls-important # 重要 URL のみ（公式・姉妹サイト・Qiita）"
	@echo ""
	@echo "  make check-kiro-all-blog-index-count # ブログ索引の件数 = README 収録範囲行の N、索引 = TSV から再生成した内容"
	@echo "  make check-kiro-all-blog-sync      # 公式 sitemap と blog-index.tsv の差分（手動のみ・ネットワーク）"
	@echo "  make gen-kiro-all-blog-index       # blog-index.tsv から 03_reference/01_blog-index.md を再生成"

# ------------------------------------------------------------
# まとめて実行
# ------------------------------------------------------------
check-kiro-all-all: check-kiro-all-links check-kiro-all-notation check-kiro-all-sources check-kiro-all-quotes check-kiro-all-first-person check-kiro-all-blog-index-count
	@echo ""
	@echo "=== check-kiro-all-all: すべて完了 ==="

check-kiro-all-quick: check-kiro-all-links check-kiro-all-notation

check-kiro-all-ignore:
	@$(SCRIPTS)/check-ignore.sh

# ------------------------------------------------------------
# 個別（ネットワーク不要）
# ------------------------------------------------------------
check-kiro-all-links:
	@$(SCRIPTS)/check-links.py --check-anchors

check-kiro-all-notation:
	@$(SCRIPTS)/check-notation.py

check-kiro-all-sources:
	@$(SCRIPTS)/check-sources.py

check-kiro-all-quotes:
	@$(SCRIPTS)/check-quotes.py

check-kiro-all-first-person:
	@$(SCRIPTS)/check-first-person.py

check-kiro-all-blog-index-count:
	@$(SCRIPTS)/check-blog-index-count.py

gen-kiro-all-blog-index:
	@$(SCRIPTS)/gen-blog-index.py

# ------------------------------------------------------------
# 外部依存
# ------------------------------------------------------------
check-kiro-all-blog-sync:
	@$(SCRIPTS)/check-blog-sync.sh

check-kiro-all-urls:
	@$(SCRIPTS)/check-urls.sh

check-kiro-all-urls-important:
	@$(SCRIPTS)/check-urls.sh --important
