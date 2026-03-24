---
name: cmux-browser
description: cmux 環境でブラウザサーフェスを操作し、Webページの情報取得・DOM操作・フォーム入力・スクリーンショット等を自律的に行う。cmux上で動作している時、隣のサーフェスのブラウザからフィードバックを得てデバッグや検証を進める。「ブラウザで確認」「画面を見て」「ページを開いて」「DOMを操作」「スクリーンショット撮って」「ブラウザでデバッグ」「cmux browser」などに対応。
metadata:
  version: 1.0.0
---

# cmux ブラウザ自律操作

cmux のブラウザサーフェスを使い、Webページの閲覧・操作・検証を自律的に行う。

## 前提条件

- cmux 環境で実行されていること
- ブラウザサーフェスが利用可能であること（通常 `surface:2` 等の隣接サーフェス）

## 基本ワークフロー

### 1. ブラウザを開く

```bash
# 新規ブラウザサーフェスを開く
cmux browser open <URL>

# 分割で開く
cmux browser open-split <URL>
```

### 2. ページ情報を取得する

```bash
# アクセシビリティツリー（DOM構造の把握に最適）
cmux browser surface:2 snapshot --interactive --compact

# 特定要素のみ
cmux browser surface:2 snapshot --selector "main" --max-depth 5

# スクリーンショット（視覚的確認）
cmux browser surface:2 screenshot --out /tmp/cmux-page.png

# 現在のURL
cmux browser surface:2 url

# ページタイトル
cmux browser surface:2 get title

# テキスト取得
cmux browser surface:2 get text "h1"
cmux browser surface:2 get html "main"
```

### 3. ナビゲーション

```bash
cmux browser surface:2 navigate <URL> --snapshot-after
cmux browser surface:2 back
cmux browser surface:2 forward
cmux browser surface:2 reload --snapshot-after
```

`--snapshot-after` を付けるとアクション後に自動でスナップショットが返る。**積極的に使用すること。**

### 4. DOM操作

```bash
# クリック
cmux browser surface:2 click "button[type='submit']" --snapshot-after

# テキスト入力
cmux browser surface:2 type "#search" "検索テキスト"
cmux browser surface:2 fill "#email" --text "user@example.com"

# フォームクリア
cmux browser surface:2 fill "#email" --text ""

# キー入力
cmux browser surface:2 press Enter

# チェックボックス
cmux browser surface:2 check "#terms"
cmux browser surface:2 uncheck "#newsletter"

# セレクトボックス
cmux browser surface:2 select "#region" "us-east"

# スクロール
cmux browser surface:2 scroll --dy 800 --snapshot-after
cmux browser surface:2 scroll-into-view "#pricing"
```

### 5. 要素検索・状態確認

```bash
# 要素を探す（複数の方法）
cmux browser surface:2 find role button --name "送信"
cmux browser surface:2 find text "注文完了"
cmux browser surface:2 find label "メールアドレス"
cmux browser surface:2 find testid "save-btn"

# 要素の状態確認
cmux browser surface:2 is visible "#checkout"
cmux browser surface:2 is enabled "button[type='submit']"

# 要素数カウント
cmux browser surface:2 get count ".row"

# 属性取得
cmux browser surface:2 get attr "a.primary" --attr href
cmux browser surface:2 get value "#email"
```

### 6. 待機条件

ページ遷移やAPI応答を待つ場合:

```bash
cmux browser surface:2 wait --load-state complete --timeout-ms 15000
cmux browser surface:2 wait --selector "#checkout" --timeout-ms 10000
cmux browser surface:2 wait --text "読み込み完了"
cmux browser surface:2 wait --url-contains "/dashboard"
cmux browser surface:2 wait --function "window.__appReady === true"
```

### 7. JavaScript 実行

```bash
cmux browser surface:2 eval "document.title"
cmux browser surface:2 eval "document.querySelectorAll('.item').length"
cmux browser surface:2 addscript "document.querySelector('#debug')?.remove()"
cmux browser surface:2 addstyle "#banner { display: none !important; }"
```

### 8. コンソール・エラー確認

```bash
cmux browser surface:2 console list
cmux browser surface:2 errors list
```

## 自律操作の原則

1. **snapshot を多用する** — 操作前後で snapshot を取り、状態変化を確認する
2. **`--snapshot-after` を常に付ける** — navigate, click, scroll 等のアクションに付与し、結果を即座に把握する
3. **wait で確実に待つ** — ページ遷移やAjax後は wait で完了を確認してから次の操作へ
4. **エラー時はコンソールを確認** — `errors list` と `console list` で問題を特定する
5. **スクリーンショットは視覚確認用** — レイアウト崩れ等の確認には screenshot を使う

## 典型的なユースケース

### ローカル開発サーバーの動作確認
```bash
cmux browser open http://localhost:5173
cmux browser surface:2 snapshot --interactive --compact
```

### フォーム送信テスト
```bash
cmux browser surface:2 fill "#name" --text "テストユーザー"
cmux browser surface:2 fill "#email" --text "test@example.com"
cmux browser surface:2 click "button[type='submit']" --snapshot-after
cmux browser surface:2 wait --text "送信完了" --timeout-ms 5000
```

### デバッグ（コンソールログ確認）
```bash
cmux browser surface:2 eval "console.log(JSON.stringify(window.__APP_STATE__))"
cmux browser surface:2 console list
```

## 詳細リファレンス

- **全コマンド一覧と詳細オプション**: [references/commands.md](references/commands.md)
