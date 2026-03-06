---
description: コミット、検証、Push、PR作成、Merge を一括実行する標準手順
---

# Commit & Merge ワークフロー

変更をコミットし、検証を通してから PR 作成・Merge まで進める。失敗したら停止し、修正してから再実行する。

## ステップ 1: 最新取得と変更確認

1. 必要なら `git fetch origin` で最新を取得
2. `git status` と `git diff --stat` で変更内容を把握
3. 変更内容を簡潔にサマリー化

## ステップ 2: 検証実行

コミット前に、そのプロジェクトで定義されている検証コマンドを実行する。

```bash
pnpm check
pnpm test
pnpm test:e2e
```

- 存在しないコマンドは等価コマンドで代替する
- 3回連続で失敗したら停止して報告する

## ステップ 3: コミット

- 変更ファイルを個別に `git add` する
- `.env`、credentials、生成物、依存ディレクトリは含めない
- コミットメッセージは短く具体的にする

## ステップ 4: Push

- 必要なら feature ブランチを作成する
- `git push -u origin HEAD` で push する

## ステップ 5: PR 作成

- `gh pr create` で PR を作る
- Summary と Test plan を簡潔に書く

## ステップ 6: Merge

- 承認条件を満たしたら `gh pr merge` を実行する
- 必要ならローカルブランチを同期する

## 中断条件

- 検証が連続で失敗
- `git push` が失敗
- `gh pr create` が失敗
- `gh pr merge` が失敗
- コミット対象がない
