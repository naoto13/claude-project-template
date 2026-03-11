# 開発環境セットアップ

認証・DB接続の環境別切り替えの詳細は [docs/auth-and-db.md](auth-and-db.md) を参照。

## 環境別の概要

| 環境 | DB | セットアップ | 手動操作 |
|---|---|---|---|
| ローカル (macOS/Linux) | Docker MySQL | 手動（本ドキュメントの手順） | あり |
| クラウド (Claude Code Remote) | ネイティブ MySQL | **自動**（SessionStartフック） | なし |

---

## ローカル開発

### 前提
- 使用するランタイムがインストール済み
- 必要なパッケージマネージャが使える
- ローカル用の環境変数ファイルを用意する

### 手順

1. 依存関係をインストールする
2. 必要ならローカル DB や外部サービスを起動する
3. マイグレーションや seed を実行する
4. 開発サーバーを起動する

### 標準例

```bash
pnpm install
pnpm dev
```

### チェックポイント
- 開発サーバーが起動する
- ログインや主要画面に到達できる
- テストコマンドがローカルで実行できる

---

## クラウド環境 (Claude Code Remote)

クラウド環境では Docker が使えないため、SessionStart フックが MySQL をネイティブバイナリで自動セットアップする。**手動操作は不要**。

### 自動実行される処理

セッション開始時に `.claude/hooks/session-start-mysql.sh` が以下を順次実行:

1. Docker 利用可否チェック（利用可能なら何もせず終了）
2. MySQL 8.0 tarball のダウンロード・展開（`/tmp/` に配置）
3. `mysqld` の初期化・起動（パスワードなし、ポート 3306）
4. `.claude/cloud-env.json` の `dbName` で DB 作成
5. `.env.local` を `cloud-env.json` の `envVars` から動的生成
6. `cloud-env.json` の `migrateCommand` でマイグレーション実行
7. Playwright ブラウザの自動配置（E2Eテスト用）

### 設定ファイル: `.claude/cloud-env.json`

プロジェクト固有の設定を記載。フック本体の修正は不要。

```json
{
  "db": "mysql",
  "dbName": "my_app",
  "migrateCommand": "pnpm db:push",
  "envVars": {
    "DATABASE_URL": "mysql://root:@127.0.0.1:3306/${dbName}"
  }
}
```

- `${dbName}` プレースホルダーは `dbName` の値に自動展開される
- `envVars` の各キーがそのまま `.env.local` の環境変数になる
- 必要な環境変数（JWT_SECRET, API キーなど）はプロジェクトに合わせて追加する

### 他プロジェクトへの移植

1. `.claude/hooks/session-start-mysql.sh` をコピー
2. `.claude/settings.json` に SessionStart フック登録を追加
3. `.claude/cloud-env.json` をプロジェクトに合わせて作成

フック本体の修正は不要。

### トラブルシューティング

| 症状 | 確認・対処 |
|---|---|
| MySQL 起動タイムアウト | `/tmp/mysqld.log` を確認 |
| libaio エラー | Ubuntu 24.04 では `libaio.so.1t64` → `libaio.so.1` の symlink が必要（フックが自動対応） |
| Playwright ブラウザ不一致 | `npx playwright install chromium` を手動実行 |
| マイグレーション失敗 | `DATABASE_URL=... pnpm db:push` を手動実行 |
