# Claude Project Template

Claude Code を前提にしたプロジェクトテンプレート。
`CLAUDE.md`、`.claude/`、`docs/` の骨格をまとめて持ち込み、別プロジェクトでそのまま初期セットアップできるようにしている。

## 何が入っているか

| パス | 役割 |
|---|---|
| `CLAUDE.md` | Claude が最初に読む最上位ガイド |
| `.claude/agents/` | 役割別エージェント定義 |
| `.claude/commands/` | `/dev-spec` などのコマンド定義 |
| `.claude/rules/` | 自動適用ルール |
| `.claude/hooks/` | セキュリティ、CI 補助、クラウド環境セットアップフック |
| `.claude/cloud-env.json` | クラウド環境（Claude Code Remote）の設定 |
| `.claude/skills/` | 再利用可能な Skill |
| `docs/` | アーキテクチャ、仕様、TODO、ドメイン知識のテンプレート |
| `TEMPLATE_SETUP.md` | 移植時に最初に埋めるチェックリスト |

## 最初にやること

1. `TEMPLATE_SETUP.md` を読む
2. `CLAUDE.md` のプロジェクト名、構成、標準コマンドを更新する
3. `docs/architecture.md` を実プロジェクトの構成に合わせる
4. `docs/domain/` と `todo.md` を実情に合わせて埋める
5. `package.json` scripts と `CLAUDE.md` のコマンド説明を一致させる

## AI エージェント設定（`.claude/`）

このテンプレートは Claude Code による AI 支援開発を前提としている。`.claude/` に設定をまとめている。

### エージェントコマンド（`/` で呼び出す）

| コマンド | 説明 | いつ使う |
|---|---|---|
| `/dev-spec` | ユーザー要望から仕様書を生成 | 新機能の設計開始時 |
| `/dev-impl` | 確定仕様に基づいて実装 | 仕様が固まった後 |
| `/dev-setup` | ローカル開発環境セットアップ | 初回セットアップ時 |
| `/form-impl` | DB→Zod→FE 三層整合性を検証してフォーム実装 | フォーム実装時 |
| `/commit-merge` | コミット → テスト → Push → PR → Merge を一括実行 | 作業完了時 |
| `/test-e2e` | E2E テスト実行と失敗時の切り分け | UI テスト時 |
| `/doc-garden` | ドキュメント健全性チェック | ドキュメント乖離が気になった時 |
| `/skill-creator` | 新しいスキルの作成・改善 | Skill 開発時 |

### エージェントルール（`.claude/rules/`）

自動適用されるルール。特に意識しておくとよいものだけを抜粋する。

| ルール | 概要 |
|---|---|
| `architecture-compliance.md` | レイヤー依存方向の遵守 |
| `doc-self-healing.md` | 実装変更時に関連ドキュメントも更新 |
| `ci-verification.md` | 作業完了前に test/check/build を実行 |
| `test-quality.md` | Happy Path テスト必須 |
| `implementation-quality.md` | 空実装禁止・動作確認必須 |
| `security-awareness.md` | API キーや秘密情報のハードコード禁止 |

## docs/ の考え方

| ファイル | 役割 |
|---|---|
| `docs/architecture.md` | コードベースの地図。レイヤー、依存方向、主要フロー |
| `todo.md` | 唯一のタスク管理ソース |
| `spec/` | 機能仕様書 |
| `docs/domain/` | ビジネスルール、データモデル、Phase 計画 |
| `docs/local-dev.md` | ローカル開発手順 |

## クラウド環境対応 (Claude Code Remote)

クラウド環境では Docker が使えないため、SessionStart フックでネイティブ MySQL を自動セットアップする仕組みを内蔵している。

- **フック**: `.claude/hooks/session-start-mysql.sh` — セッション開始時に自動実行
- **設定**: `.claude/cloud-env.json` — DB名・マイグレーションコマンド・環境変数を定義
- **ドキュメント**: `docs/local-dev.md` に詳細手順・トラブルシューティングを記載

移植時は `.claude/cloud-env.json` をプロジェクトに合わせて編集するだけでよい。フック本体の修正は不要。

## 注意点

- `.claude/hooks/` は `jq`、`curl`、`pnpm` を前提にしている
- `.claude/start-dev.sh` は初期状態では `pnpm dev` 前提
- `project-template` は汎用版なので、ASP 固有の前提は落としてある
- 固有のロール、ディレクトリ、コマンド、レビュー観点は移植先で埋める必要がある

## 次に読むファイル

- `TEMPLATE_SETUP.md`
- `CLAUDE.md`
- `docs/architecture.md`
- `.claude/commands/dev-spec.md`
