# DB接続と認証 — 環境別ガイド

本番コードを一切変更せず、環境変数と `NODE_ENV` だけで DB・認証・レート制限を切り替える。

## 環境別の比較

| | ローカル | クラウド (Claude Code Remote) | 本番 |
|---|---|---|---|
| **DB** | Docker MySQL (`docker compose up`) | ネイティブ MySQL (SessionStartフック自動) | クラウド MySQL |
| **接続先** | `localhost:3306` via `.env.local` | `127.0.0.1:3306` via `.env.local`(自動生成) | `DATABASE_URL` 環境変数 |
| **マイグレーション** | 手動 | 自動実行 | 事前実行済み |
| **認証方式** | DevAuth（OAuth スキップ） | DevAuth（OAuth スキップ） | OAuth |
| **NODE_ENV** | development | development | production |
| **レート制限** | 無効 (development) | 無効 | 有効 |

## DB接続

全環境共通で `DATABASE_URL` 環境変数ベース。

```
ローカル:  docker compose up → .env.local に接続先を記載
クラウド:  session-start-mysql.sh → .env.local を cloud-env.json から自動生成
本番:      環境変数に設定済み
```

## 認証フロー

### 開発環境 (ローカル・クラウド共通)

`NODE_ENV=development` のとき DevAuth が有効になる。

```
ブラウザ → /dev-login 画面
  → /api/dev/login?role=admin (または一般ユーザー)
  → DB に upsert → JWT 署名 → Cookie 発行 → / にリダイレクト
```

- DevAuth エンドポイントは開発時のみ登録される
- DevLogin 画面は `import.meta.env.DEV` 時のみ表示
- 本番ビルドからは tree-shaking で完全削除

### 本番環境

```
ブラウザ → OAuth プロバイダ
  → /api/oauth/callback?code=...
  → access token 交換 → user info 取得 → DB upsert → JWT → Cookie → /
```

### リクエスト認証（全環境共通）

```
リクエスト → Cookie から JWT 取得 → 署名検証 → DB から user 検索 → context.user に設定
```

呼び出し側は環境を意識する必要がない。

## E2E テストでの認証

Playwright は DevAuth を使って認証状態を保存・再利用する。

```
auth.setup.ts
  → /api/dev/login?role=admin     → storageState → e2e/.auth/admin.json
  → /api/dev/login?role=user      → storageState → e2e/.auth/user.json

各テスト
  → browser.newContext({ storageState: "e2e/.auth/admin.json" })
  → 認証済みセッションで実行
```

- `playwright.config.ts` の `projects` で `auth-setup` を最初に実行、他テストが依存
- `webServer` 設定で `NODE_ENV=development` を指定
- `e2e/.auth/` は `.gitignore` 対象

## レート制限

開発環境（`NODE_ENV=development` / `test`）ではレート制限を無効化する。
本番のみ有効にする設計を推奨。

## 環境変数一覧

| 変数 | ローカル | クラウド | 本番 | 用途 |
|---|---|---|---|---|
| `DATABASE_URL` | Docker MySQL | ネイティブ MySQL | クラウド DB | DB接続 |
| `JWT_SECRET` | ローカル固定値 | ローカル固定値 | 本番秘密鍵 | セッション署名 |
| `NODE_ENV` | development | development | production | 認証方式・レート制限の切り替え |

プロジェクトに応じて OAuth 関連の変数（`APP_ID`, `OAUTH_PORTAL_URL` 等）を追加する。
