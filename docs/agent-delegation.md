# エージェント委任ガイド

このプロジェクトでコード作業を AI に委任するときの設計ノート。
**必ず従うルール** は `.claude/rules/prefer-codex-subagent.md`、本ドキュメントは **背景・選択肢・実装の整理** を扱う。

## なぜ Codex に寄せるか

Claude Code 親エージェント単独でコード作業をすべてこなすと、すべての推論が Anthropic 課金になる。
このプロジェクトでは Codex CLI を併用し、**コード作業の実処理を OpenAI 側に寄せる** ことで Anthropic Token を節約する。

親 Claude は「タスク分解 → 委任 → 結果統合 → 最終検証」に専念し、重い推論は Codex に投げる構造。

## エージェントの 4 系統

| 系統 | 実体 | 主体モデル | 課金 |
|---|---|---|---|
| **親 Claude** | このセッションを駆動する Claude Code | Opus 等 | Anthropic |
| **Claude サブエージェント** | `.claude/agents/<role>.md`（4 ロール） | Sonnet | Anthropic |
| **Codex プラグインサブエージェント** | `openai-codex` プラグイン提供の `codex:codex-rescue` 等 | Claude（forward のみ）→ Codex CLI | OpenAI（実処理） |
| **Codex CLI 直叩き** | `codex exec`、`codex review` 等 | Codex CLI | OpenAI |

### Claude サブエージェント（`.claude/agents/`）

`.claude/agents/<role>.md` に Markdown + YAML frontmatter で定義。

| ロール | 用途 |
|---|---|
| `orchestrator` | 要求整理・タスク分解・担当割り振り |
| `product-owner` | 仕様化・`spec/` 整備・Phase 管理 |
| `senior-engineer` | 実装・統合・リファクタ・デバッグ |
| `api-reviewer` | 読み取り専用レビュー |

呼び出し: `Agent({ subagent_type: "senior-engineer", ... })`

前提として `.claude/settings.json` で `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` が設定済み（ロール間 `SendMessage` 通信が有効化される Agent Teams 機能）。

### Codex プラグインサブエージェント（`codex:codex-rescue`）

`openai-codex` プラグイン提供。本体は `/Users/ny/.claude/plugins/cache/openai-codex/codex/1.0.1/agents/codex-rescue.md`。

中身は **thin forwarding wrapper**:
- `tools: Bash` のみ
- 自分では推論せず、`node $CLAUDE_PLUGIN_ROOT/scripts/codex-companion.mjs task ...` を呼ぶ
- リポジトリ調査・ファイル読み・進捗監視・結果サマリは禁止

Claude モデル分の Token は forward 部分のみ、実処理は OpenAI 課金。

### Codex CLI 直叩き

`codex exec --cd <repo> "<prompt>"` を Bash 経由で呼ぶ。
ジョブ管理機能なし、Bash プロセスは親 Claude の制御下。

### `.codex/agents/*.toml` の位置づけ

`.codex/agents/` に同名 4 ロールの TOML 定義あり（`.claude/agents/*.md` と並列）。
**Codex CLI からの参照方法は公式ドキュメントで未確認**（`codex exec --help` に `--agent` フラグなし）。

並列定義になっているが、**運用上は `.claude/agents/*.md` を Single Source of Truth として扱い、`.codex/agents/*.toml` は基本的に放置する**。ロール変更が必要なときは `.claude/agents/*.md` だけ更新し、ペルソナ埋め込みパターンで Codex に内容を渡せば最新定義が反映される。`.codex/agents/*.toml` を手動同期する運用は同期忘れで分岐するリスクがあるため非推奨。

## 委任パスの選択基準（3 系統）

優先順は **A → B → C**。`.claude/rules/prefer-codex-subagent.md` の定義に従う。

| パス | コスト | ジョブ管理 | 使う場面 |
|---|---|---|---|
| **A `codex:codex-rescue`** | OpenAI（forward Token は最小） | ✅（`/codex:status` / `/codex:result` / `/codex:cancel`） | 標準。長時間・多段階・親コンテキスト保護したい |
| **B `codex exec` 直叩き** | OpenAI | ❌（Bash プロセスのみ） | ワンショット・軽量 |
| **C `.claude/agents/<role>.md`** | **Anthropic** | Claude Code 標準 | Codex 不可、または Claude モデルの判断特性が必要 |

### A と B の本質的な違い

| 観点 | A | B |
|---|---|---|
| 再開機能 | `--resume-last` で前回継続を統合制御 | `codex exec resume` 別サブコマンド、ID 管理が手動 |
| prompt 整形支援 | `gpt-5-4-prompting` skill を内部で使用可 | 親 Claude が直接書く |
| コンテキスト分離 | subagent として独立コンテキスト、親窓を圧迫しない | Bash 出力が親窓に直接戻る |
| 呼び出し簡潔さ | `Agent({...})` 1 回 | `codex exec ... "$(cat <<EOF ... EOF)"` |

→ 長時間タスク / 複数 Codex ジョブ並走 / 親コンテキスト保護のいずれかが必要なら **A**、本当にワンショットの軽い呼び出しなら **B**。

## `codex:codex-rescue` の routing flags

prompt 先頭に置く。wrapper が抜き取って Codex に渡す。

| フラグ | 動作 | デフォルト |
|---|---|---|
| `--write` | 書き込み可能で実行 | wrapper が自動付与。read-only にしたいときは prompt 内で「read-only」「review only」「diagnose without edits」を明示すると wrapper が付与しない |
| `--background` / `--wait` | background / foreground 実行 | 小タスク foreground、複雑/長時間 background |
| `--resume-last` / `--fresh` | 前回 Codex ジョブ継続 / 新規 | 新規 |
| `--model <name>` | モデル指定（例: `gpt-5.3-codex-spark`） | 未指定（プラグインデフォルト） |
| `--effort <low\|medium\|high>` | reasoning effort | 未指定（プラグインデフォルト） |

## ペルソナ埋め込みパターン

`.claude/agents/<role>.md` を SSoT として、その内容を prompt 先頭に Persona ブロックとして埋め込む。Claude 側で更新するだけで Codex に最新ロール定義が反映される。

**組み立て順**: `routing flags` → `Persona` → `Goal block` → `Task`

```
--write --background

# Persona

<.claude/agents/senior-engineer.md の Role / Execution Protocol を抜粋>

## Goal

Complete <タスクの目的> without stopping until <検証可能な終了状態>.

## Success Criteria

- [ ] 要件1 → 証拠: <ファイル / コマンド出力>
- [ ] 要件2 → 証拠: <...>

## Task

<具体的なタスク内容・背景・制約>
```

これを `Agent({ subagent_type: "codex:codex-rescue", prompt: <上記本文> })` で渡す。

## 設計判断の経緯（履歴）

1. **初期案**: `~/.codex/config.toml` のプロファイル定義（`review/debug/refactor/quick/arch`）を前提に `codex exec --profile` で振り分ける設計を試みた
2. **問題発覚**: このプロジェクトの `.codex/config.toml` にはプロファイル未定義（shell_environment_policy のみ）。`codex exec --help` にも `--agent` フラグは無い
3. **`codex:codex-rescue` 発見**: OMC プラグインと思い込んだが、実際は **`openai-codex` プラグイン** が提供する thin forwarding wrapper
4. **`.codex/agents/*.toml` 調査**: Claude Code は `.claude/agents/*.md`（Markdown）のみ参照。`.codex/agents/*.toml` を Codex CLI が読むかは公式未確認
5. **結論**: A (`codex:codex-rescue`) を標準パスに、`.claude/agents/*.md` を SSoT に、ペルソナ埋め込みで Codex に渡す運用
6. **疎通実証**: 軽量プロンプト（"hello from codex-rescue" + cwd 報告）で `subagent_type: "codex:codex-rescue"`（プラグイン名空間付き）が正しく呼べることを確認。21,827 tokens / 27 秒で完了し、wrapper → Codex CLI → 結果返却の流れが期待通り動作（実処理は OpenAI 課金）

## 関連ファイル

| ファイル | 役割 |
|---|---|
| `.claude/rules/prefer-codex-subagent.md` | 必ず従うルール本体 |
| `.claude/rules/proactive-subagent-and-skill.md` | サブエージェント全般の活用ルール |
| `.claude/agents/<role>.md` | Claude サブエージェントのロール定義（SSoT） |
| `.codex/agents/<role>.toml` | Codex CLI 用並列定義（参照方法未確認・運用上は同期しない） |
| `.claude/settings.json` | Claude Code 設定（`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`、tmux モード等） |
| `.codex/hooks.json` / `.claude/hooks/` | Claude / Codex 両方に効くセキュリティ・lint・CI フック |
| `AGENTS.md` | プロジェクト最上位ガイド。Codex 委任方針への参照あり |
