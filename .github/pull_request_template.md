# Pull Request

## Description

Brief description of the changes in this PR.

## Type of Change

Please delete options that are not relevant.

- [ ] 🐛 Bug fix (typo, wrong value, broken link)
- [ ] ✨ New page or section
- [ ] 💥 Breaking change (section restructure, file rename/move)
- [ ] 📚 Documentation update (new official blog post / docs change reflected)
- [ ] 🔧 Maintenance (scripts, CI, templates)

## Sections Updated

- [ ] `README.md` (入口・姉妹サイト)
- [ ] `kiro-all-docs/00_start/` (はじめての人向け)
- [ ] `kiro-all-docs/01_story/` (開発経緯・ハーネス統一・Kiro CLI の道)
- [ ] `kiro-all-docs/02_why-kiro-cli/` (筆者の推し)
- [ ] `kiro-all-docs/03_reference/` (公式ブログ索引・情報源)
- [ ] `scripts/` / `Makefile` / CI
- [ ] Other: _______________

## Primary sources

List the official pages (kiro.dev blog / docs / changelog, `kirodotdev/KiroCrew`,
`aws/amazon-q-developer-cli`) that support every factual statement added or changed.

## Checklist

- [ ] I have read the [documentation workflow](WORKFLOW.md) and [commit checklist](COMMIT_CHECKLIST.md)
- [ ] Every factual statement cites a primary source; summaries are in my own words, English quotes are 30 words or fewer
- [ ] Statements that cannot be verified officially are explicitly marked 未確認
- [ ] Opinions appear only in `02_why-kiro-cli/` or in the single 🐾 block in `README.md`
- [ ] Kiro IDE / CLI / Web / Mobile / Crew are not conflated
- [ ] Dates use ISO format (`YYYY-MM-DD`); no fetch dates in the public text
- [ ] No official images, logos, or screenshots (diagrams are Mermaid)
- [ ] No author affiliation (employer) is stated or implied
- [ ] kiro.dev URLs end with a trailing slash (no trailing slash returns 301)

## Testing

- [ ] `make check-kiro-all-all` passes locally (exit 0)
- [ ] `make check-kiro-all-ignore` passes locally (exit 0)
- [ ] If I created or modified a validation script, I ran a negative test per rule
- [ ] Mermaid diagrams render on GitHub (if applicable)

## Related Issues

Closes #(issue number)

---

**Important**: This is an unofficial documentation project. By submitting this PR, you acknowledge that this project is not affiliated with Kiro or Amazon Web Services, Inc.
