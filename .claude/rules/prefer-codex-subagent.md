# Codex 優先委任ルール

## 原則

実装・デバッグ・調査・リファクタリング・コードレビューなど **コード作業を伴うタスクは、原則として Codex に委任する**。
親 Claude は「タスク分解 → 委任 → 結果統合 → 最終検証」に専念する。

このルールは `proactive-subagent-and-skill.md`（Skill/Subagent 活用ルール）の拡張であり、サブエージェントを使うべきと判断したら、まず Codex への委任が成立しないかを検討する。

## Codex Agent Teams（推奨パス）

このプロジェクトには `.codex/agents/*.toml` で 4 ロールの Codex エージェントが定義済み。
役割が明確なタスクは、まずこの 4 ロールへの委任を検討する。

| ロール | 用途 | sandbox |
|---|---|---|
| `orchestrator` | 要求整理・タスク分解・担当割り振り・進捗管理 | workspace-write |
| `product-owner` | 仕様化・`spec/` の追加更新・Phase 管理 | workspace-write |
| `senior-engineer` | 実装・統合・リファクタ・デバッグ・レビュー | workspace-write |
| `api-reviewer` | バグ・セキュリティ・性能・テスト観点の読み取り専用レビュー | **read-only** |

### ロール選択フロー

1. 要求が曖昧 or 複数領域にまたがる → `orchestrator` に投げて分解させる
2. 仕様が固まっていない → `product-owner` に投げて `spec/` を起こさせる
3. 仕様が固まっている → `senior-engineer` に実装/修正を委任
4. 変更レビュー・差分監査・読み取り調査 → `api-reviewer`

`.codex/hooks/` で secrets/lint/CI が自動実行されるため、委任先で安全装置が効く。

## 委任パス（3 系統）

### A) Claude Code Agent Teams 経由（環境変数 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 前提）

`.codex/agents/*.toml` の定義に基づき、Agent ツールから `subagent_type` でロール名を指定して呼び出す。
セッション開始時のフック（`session-start-mysql.sh` 等）も効く。

### B) `codex exec` 直叩き（1 回完結タスク向け）

```bash
codex exec --cd <repo_abs_path> "<prompt with Goal block>"
```

`.codex/config.toml` にはプロファイル定義が無いため `--profile` フラグは使わない。
モデル指定が必要なら `--model` を明示する。`--cd` には対象リポジトリのルート絶対パスを指定。

### C) `codex:codex-rescue` サブエージェント（長時間 / background 向け）

background ジョブ管理（`/codex:status`, `/codex:result`, `/codex:cancel`）が使える多段階タスク用。

```
Agent({
  subagent_type: "codex:codex-rescue",
  description: "<task summary>",
  prompt: "--model gpt-5.5 --effort medium --write --background <task with Goal block>"
})
```

## 委任の作法

1. **宣言**: 委任前に「Codex に委任します（role=`<name>` / パス=`<A|B|C>`）: `<理由>`」を 1 行で明示
2. **プロンプト**: 下記 **Goal ブロックを必須** とし、背景・制約（ファイルパス、行番号、既知の落とし穴）を self-contained で記述
3. **パス選択**:
   - 役割が明確 → A（Agent Teams）
   - 1 回完結・軽量 → B（`codex exec`）
   - 多段階・長時間 → C（`codex-rescue` + `--background`）
4. **結果統合**: 出力を親で確認し、最終検証・コミット判断は親が行う

### Goal ブロック（必須）

`codex exec` は非対話モードのため `/goal` スラッシュコマンドが使えない。同等の効果を **プロンプト先頭に Goal ブロックとして埋め込む** ことで再現する。

```
## Goal

Complete <タスクの目的> without stopping until <検証可能な終了状態>.

## Success Criteria（要件 → 証拠マッピング）

- [ ] 要件1 → 証拠: <確認するファイル / コマンド出力 / テスト結果>
- [ ] 要件2 → 証拠: <...>

## Verification Rules

- 自己申告で "done" としない。各要件は実ファイル / コマンド出力 / テスト結果で裏取りする。
- 不確実な点は "not-done" として扱い、追加調査かブロッカー報告を行う。

## Task

<具体的なタスク内容・背景・制約>
```

**書き方のコツ:**

- 終了状態は「`pnpm test` が pass」「`grep -r "TODO" src/ で 0 件`」のように **コマンド出力で判定可能** にする
- 要件は最大 5 項目程度。多すぎると焦点がぼやける
- 委任先ロールの `developer_instructions` で前提が既に縛られているので、Task ブロックでは差分情報だけ書けばよい

## 委任対象

| 状況 | 推奨ロール / パス |
|---|---|
| 新機能の実装・既存コードの修正 | `senior-engineer` / A |
| バグ調査・根本原因分析・最小パッチ | `senior-engineer` / A |
| リファクタリング・コード整理 | `senior-engineer` / A |
| 仕様策定・`spec/` 作成更新 | `product-owner` / A |
| 差分レビュー・セキュリティ確認 | `api-reviewer` / A |
| 横断的な調査（複数ファイル/モジュール） | `senior-engineer`（書込不要なら `api-reviewer`） / A |
| 1 ファイル read・タイポ修正・1 行変更 | 親で直接実行（委任不要） |
| 長時間・多段階の作業 | C（`codex-rescue` + `--background`） |

## 委任しない（親で直接実行）

- 1 コマンド / 1 ファイル read で完了する微小タスク
- ユーザーへの単純な回答・状況報告
- 設定ファイル（`.claude/**`, `.codex/**`, `AGENTS.md`, `~/.claude/**`, `~/.codex/**`）の直接編集
- コミット・PR 作成など承認を伴うフロー
- Codex で既に失敗した同一タスクの繰り返し（→ 別アプローチか親で着手）

## 並列実行

独立した複数タスクは並列で Codex を起動してよい。ただし以下を確認する:

- 書き込み対象ファイル / モジュールが競合しないか
- 各タスクが self-contained に Goal ブロックを持っているか
- 親が結果を統合できる粒度に分かれているか

## 禁止事項

- 委任で済む実装作業を親で抱え込まない
- Codex 結果を未検証のまま「完了」と報告しない
- `api-reviewer` ロールで書き込みを期待しない（read-only）
- Goal ブロック / 終了条件のないまま委任しない（無限ループ・暴走防止）
- `.codex/agents/*.toml` を書き換えてロールを暫定追加しない（必要なら別 PR で正式追加）
