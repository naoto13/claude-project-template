---
description: コミット、検証、Push、PR 作成、Merge の標準手順
---

# Commit & Merge ワークフロー

## ステップ 1: 変更確認
- `git status`
- `git diff --stat`
- 必要なら `git fetch origin`

## ステップ 2: 検証

```bash
pnpm check
pnpm test
pnpm test:e2e
```

存在しないコマンドは、そのプロジェクトの等価コマンドで代替する。

## ステップ 3: コミット
- 変更ファイルを個別に `git add`
- 秘密情報や生成物を含めない
- コミットメッセージは短く具体的に

## ステップ 4: Push / PR / Merge
- feature ブランチで push
- `gh pr create`
- 承認条件を満たしたら `gh pr merge`

## 停止条件
- 検証が連続で失敗
- push / PR / merge に失敗
- コミット対象がない
