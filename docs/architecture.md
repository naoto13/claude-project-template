# アーキテクチャマップ

このドキュメントはコードベースの地図です。新規実装や調査の起点として使います。

## Quick Reference

### レイヤー構成

実プロジェクトに合わせて更新してください。

```text
UI / App
Shared / Domain
API / Services
Data / Storage
Infrastructure
```

### 依存方向

- 上位レイヤーは下位レイヤーに依存してよい
- 下位レイヤーは上位レイヤーへ依存しない
- 例外がある場合はここに明記する

### 主要ディレクトリ

| パス | 役割 |
|---|---|
| `src/` | アプリケーション本体 |
| `docs/` | ドキュメント |
| `tests/` or `e2e/` | テスト |
| `scripts/` | 補助スクリプト |

## 主要フロー

### 例: 1リクエストの流れ
1. エントリポイントで入力を受ける
2. アプリケーション層でユースケースを実行する
3. データ層で読み書きする
4. 整形してレスポンスを返す

## CHANGELOG.md 連携パターン

CHANGELOG.md は `/changelog` スキルにより機械可読フォーマットで管理される。
フロントエンドから消費する場合は以下のいずれかのパターンを採用する。

| 方式 | 説明 | 適用場面 |
|---|---|---|
| ビルド時 MD→JSON | `scripts/parse-changelog.ts` 等でビルド時に JSON 変換 | SSG/SSR |
| API 経由 | `/api/changelog` で raw MD を返し、クライアントでパース | SPA |
| SSG ページ生成 | `getStaticProps` 等で MD パースし `/changelog` ページ生成 | Next.js / Astro |

フォーマット仕様の詳細は `.claude/skills/changelog/SKILL.md` の「機械可読フォーマット仕様」セクションを参照。

## アーキテクチャ判断メモ

- なぜその分割なのか
- どこに責務境界があるか
- どの部分が将来変わりやすいか
