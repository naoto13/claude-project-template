# Template Setup

このテンプレートを他プロジェクトへ入れたら、最初に以下を更新してください。

## 必須
- `CLAUDE.md` のプロジェクト名、構成、標準コマンド
- `docs/architecture.md` の実ディレクトリ、依存方向、主要フロー
- `docs/domain/business-model.md` のロール、業務フロー、重要ルール
- `docs/domain/data-model.md` の実エンティティ
- `docs/domain/phase-roadmap.md` と `docs/todo.md`
- `.claude/rules/project-scope-restriction.md` の表現が移植先に合うか確認
- `.claude/settings.json` の hooks と permissions

## 任意
- 不要な agent を削除
- 不要な skill を削除
- `launch.json` と `start-dev.sh` を起動方法に合わせて変更
- `package.scripts.template.json` を見ながら scripts 名を揃える

## 削除候補
- E2E を使わないなら `.claude/commands/test-e2e.md`
- レビュー専用 agent が不要なら `.claude/agents/api-reviewer.md`
- Task ベース運用をしないなら `orchestrator` / `product-owner`
