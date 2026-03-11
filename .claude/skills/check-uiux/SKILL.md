---
name: check-uiux
description: |
  Lightweight UIUX sanity check that runs on every UI edit.
  Trigger whenever the user modifies components, pages, or styles, or mentions UI修正, デザイン直して, デザイン修正, 見た目修正, スタイル修正, UI変更, コンポーネント修正, CSS修正.
  Quick pass/fail — no heavy analysis.
---

# check-uiux — UIUX 軽量サニティチェック

UI を修正するたびに自動発火する軽量チェック。数秒で完了し、✅/❌ を返す。

## 実行手順

1. 直前に変更されたファイルを特定（git diff --name-only 等、または会話コンテキストから判断）
2. 変更ファイルに対して以下の項目を **Grep のみ** で高速チェック
3. 結果を1テーブルで出力

## チェック項目

### 1. カラーハードコード
変更ファイル内に `#[0-9a-fA-F]{3,8}` や `rgb(` がないか Grep。
CSS変数やTailwindクラスでなくインライン hex/rgb があれば ⚠️。
（SVG内の外部ブランドカラーや意図的なものは許容）

### 2. 角丸チェック
変更ファイル内の `rounded-` クラスを Grep。
`rounded-sm` や `rounded-md` があれば ⚠️（`rounded-lg` 以上を推奨）。
`rounded-xl`, `rounded-2xl`, `rounded-full` は ✅。

### 3. スペーシング
変更ファイル内の `max-w-` を Grep。`max-w-7xl` 以外のコンテナ幅があれば ⚠️。
セクション要素の `py-` が `py-20` 未満なら ⚠️。

### 4. レスポンシブプレフィックス
変更ファイルに `className=` があるのに `sm:` `md:` `lg:` が一切なければ ⚠️。
（ユーティリティコンポーネント等、不要なケースは許容）

### 5. a11y 基本
変更ファイル内の `<button` に `aria-label` や表示テキストがあるか。
`<img` に `alt` があるか。
アイコンのみのボタンに `aria-label` がなければ ❌。

### 6. フォーカスリング
変更ファイル内の `<button` `<a` `<input` に `focus-visible:` や `focus:ring` があるか。
インタラクティブ要素にフォーカススタイルが一切なければ ⚠️。

## 出力フォーマット

```
## check-uiux 結果（対象: path/to/file.tsx）

| # | チェック | 結果 |
|---|---------|------|
| 1 | カラーハードコード | ✅ なし or ⚠️ N件 |
| 2 | 角丸 | ✅ or ⚠️ rounded-md あり |
| 3 | スペーシング | ✅ or ⚠️ ... |
| 4 | レスポンシブ | ✅ or ⚠️ プレフィックスなし |
| 5 | a11y | ✅ or ❌ aria-label 欠落 |
| 6 | フォーカスリング | ✅ or ⚠️ なし |
```

❌/⚠️ がある場合のみ、該当行と修正提案を1〜2行で添える。
詳細なレビューが必要な場合は `/review-lp-uiux` を案内する。
