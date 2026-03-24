---
name: special-ui-ux-pro-max
description: 既存UIの改善・レビュー・最適化を行うデザインインテリジェンス。「UIを改善して」「デザインを直して」「見た目がダサい」「UIレビューして」「コンポーネントを洗練させて」「レスポンシブ対応して」「ダークモード追加」「アクセシビリティ改善」「shadcn/uiで作り直して」など既存画面の品質向上に使用する。13スタック対応（React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui等）。ゼロからの新規UI構築はspecial-frontend-designを参照。
---
# UI/UX Pro Max - デザインインテリジェンス

Web およびモバイルアプリケーションのための包括的なデザインガイド。13 テクノロジースタック全体で 67 スタイル、96 カラーパレット、57 フォントペアリング、99 UX ガイドライン、25 チャートタイプを収録。優先度ベースの推奨事項を持つ検索可能なデータベース。

## 適用するタイミング

以下の場合にこれらのガイドラインを参照してください：
- 新しい UI コンポーネントやページを設計する場合
- カラーパレットとタイポグラフィを選択する場合
- UX の問題についてコードをレビューする場合
- ランディングページやダッシュボードを構築する場合
- アクセシビリティ要件を実装する場合

## 優先度別ルールカテゴリ

| 優先度 | カテゴリ | 影響 | ドメイン |
|----------|----------|--------|--------|
| 1 | アクセシビリティ | 重要 | `ux` |
| 2 | タッチ & インタラクション | 重要 | `ux` |
| 3 | パフォーマンス | 高 | `ux` |
| 4 | レイアウト & レスポンシブ | 高 | `ux` |
| 5 | タイポグラフィ & カラー | 中 | `typography`, `color` |
| 6 | アニメーション | 中 | `ux` |
| 7 | スタイル選択 | 中 | `style`, `product` |
| 8 | チャート & データ | 低 | `chart` |

## クイックリファレンス

### 1. アクセシビリティ（重要）

- `color-contrast` - 通常テキストの最低 4.5:1 比率
- `focus-states` - インタラクティブ要素の視認可能なフォーカスリング
- `alt-text` - 意味のある画像の説明的な alt テキスト
- `aria-labels` - アイコンのみのボタンへの aria-label
- `keyboard-nav` - タブ順序が視覚的な順序に一致する
- `form-labels` - for 属性を持つ label を使用する

### 2. タッチ & インタラクション（重要）

- `touch-target-size` - 最低 44x44px のタッチターゲット
- `hover-vs-tap` - 主要なインタラクションには click/tap を使用
- `loading-buttons` - 非同期操作中はボタンを無効化
- `error-feedback` - 問題の近くに明確なエラーメッセージ
- `cursor-pointer` - クリック可能な要素に cursor-pointer を追加

### 3. パフォーマンス（高）

- `image-optimization` - WebP、srcset、遅延読み込みを使用
- `reduced-motion` - prefers-reduced-motion を確認
- `content-jumping` - 非同期コンテンツのスペースを確保

### 4. レイアウト & レスポンシブ（高）

- `viewport-meta` - width=device-width initial-scale=1
- `readable-font-size` - モバイルで本文テキスト最低 16px
- `horizontal-scroll` - コンテンツがビューポート幅に収まることを確認
- `z-index-management` - z-index スケールを定義（10、20、30、50）

### 5. タイポグラフィ & カラー（中）

- `line-height` - 本文テキストに 1.5〜1.75 を使用
- `line-length` - 1 行 65〜75 文字に制限
- `font-pairing` - 見出し/本文フォントのパーソナリティを合わせる

### 6. アニメーション（中）

- `duration-timing` - マイクロインタラクションに 150〜300ms を使用
- `transform-performance` - width/height ではなく transform/opacity を使用
- `loading-states` - スケルトンスクリーンまたはスピナー

### 7. スタイル選択（中）

- `style-match` - スタイルをプロダクトタイプに合わせる
- `consistency` - すべてのページで同じスタイルを使用
- `no-emoji-icons` - 絵文字ではなく SVG アイコンを使用

### 8. チャート & データ（低）

- `chart-type` - チャートタイプをデータタイプに合わせる
- `color-guidance` - アクセシブルなカラーパレットを使用
- `data-table` - アクセシビリティのためにテーブルの代替を提供

## 使い方

以下の CLI ツールを使用して特定のドメインを検索してください。

---


## 前提条件

Python がインストールされているか確認してください：

```bash
python3 --version || python --version
```

Python がインストールされていない場合、ユーザーの OS に応じてインストールしてください：

**macOS:**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install python3
```

**Windows:**
```powershell
winget install Python.Python.3.12
```

---

## このスキルの使い方

ユーザーが UI/UX の作業（design、build、create、implement、review、fix、improve）を要求した場合、このワークフローに従ってください：

### ステップ 1: ユーザー要件の分析

ユーザーのリクエストから主要な情報を抽出します：
- **プロダクトタイプ**: SaaS、e-commerce、portfolio、dashboard、landing page 等
- **スタイルキーワード**: minimal、playful、professional、elegant、dark mode 等
- **業界**: healthcare、fintech、gaming、education 等
- **スタック**: React、Vue、Next.js、またはデフォルトの `html-tailwind`

### ステップ 2: デザインシステムの生成（必須）

推論付きの包括的な推奨事項を得るために **常に `--design-system` から始めてください**：

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
```

このコマンドの処理内容：
1. 5 つのドメインを並列検索（product、style、color、landing、typography）
2. `ui-reasoning.csv` の推論ルールを適用して最適なマッチを選択
3. 完全なデザインシステムを返す：パターン、スタイル、カラー、タイポグラフィ、エフェクト
4. 避けるべきアンチパターンを含む

**例:**
```bash
python3 skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service" --design-system -p "Serenity Spa"
```

### ステップ 2b: デザインシステムの永続化（マスター + オーバーライドパターン）

セッション全体で階層的に取得できるようにデザインシステムを保存するには、`--persist` を追加します：

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system --persist -p "Project Name"
```

これにより以下が作成されます：
- `design-system/MASTER.md` — すべてのデザインルールを含むグローバルな信頼の源
- `design-system/pages/` — ページ固有のオーバーライド用フォルダ

**ページ固有のオーバーライドを含む場合:**
```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system --persist -p "Project Name" --page "dashboard"
```

これにより以下も作成されます：
- `design-system/pages/dashboard.md` — マスターからのページ固有の差異

**階層的取得の仕組み:**
1. 特定のページ（例：「Checkout」）を構築する際、まず `design-system/pages/checkout.md` を確認
2. ページファイルが存在する場合、そのルールがマスターファイルを**オーバーライド**する
3. 存在しない場合は `design-system/MASTER.md` のみを使用

### ステップ 3: 詳細検索で補完する（必要に応じて）

デザインシステムを取得した後、ドメイン検索を使用して追加の詳細を得ます：

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

**詳細検索を使用するタイミング:**

| ニーズ | ドメイン | 例 |
|------|--------|---------|
| より多くのスタイルオプション | `style` | `--domain style "glassmorphism dark"` |
| チャートの推奨事項 | `chart` | `--domain chart "real-time dashboard"` |
| UX ベストプラクティス | `ux` | `--domain ux "animation accessibility"` |
| 代替フォント | `typography` | `--domain typography "elegant luxury"` |
| ランディング構造 | `landing` | `--domain landing "hero social-proof"` |

### ステップ 4: スタックガイドライン（デフォルト: html-tailwind）

実装固有のベストプラクティスを取得します。ユーザーがスタックを指定しない場合は **`html-tailwind` をデフォルトとします**。

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --stack html-tailwind
```

利用可能なスタック: `html-tailwind`、`react`、`nextjs`、`vue`、`svelte`、`swiftui`、`react-native`、`flutter`、`shadcn`、`jetpack-compose`

---

## 検索リファレンス

### 利用可能なドメイン

| ドメイン | 用途 | キーワード例 |
|--------|---------|------------------|
| `product` | プロダクトタイプの推奨事項 | SaaS, e-commerce, portfolio, healthcare, beauty, service |
| `style` | UI スタイル、カラー、エフェクト | glassmorphism, minimalism, dark mode, brutalism |
| `typography` | フォントペアリング、Google Fonts | elegant, playful, professional, modern |
| `color` | プロダクトタイプ別カラーパレット | saas, ecommerce, healthcare, beauty, fintech, service |
| `landing` | ページ構造、CTA 戦略 | hero, hero-centric, testimonial, pricing, social-proof |
| `chart` | チャートタイプ、ライブラリの推奨事項 | trend, comparison, timeline, funnel, pie |
| `ux` | ベストプラクティス、アンチパターン | animation, accessibility, z-index, loading |
| `react` | React/Next.js パフォーマンス | waterfall, bundle, suspense, memo, rerender, cache |
| `web` | Web インターフェースガイドライン | aria, focus, keyboard, semantic, virtualize |
| `prompt` | AI プロンプト、CSS キーワード | (スタイル名) |

### 利用可能なスタック

| スタック | フォーカス |
|-------|-------|
| `html-tailwind` | Tailwind ユーティリティ、レスポンシブ、a11y（デフォルト） |
| `react` | State、hooks、パフォーマンス、パターン |
| `nextjs` | SSR、ルーティング、画像、API ルート |
| `vue` | Composition API、Pinia、Vue Router |
| `svelte` | Runes、stores、SvelteKit |
| `swiftui` | Views、State、Navigation、Animation |
| `react-native` | Components、Navigation、Lists |
| `flutter` | Widgets、State、Layout、Theming |
| `shadcn` | shadcn/ui コンポーネント、テーマ設定、フォーム、パターン |
| `jetpack-compose` | Composables、Modifiers、State Hoisting、Recomposition |

---

## ワークフロー例

**ユーザーリクエスト:** 「プロフェッショナルなスキンケアサービスのランディングページを作って」

### ステップ 1: 要件の分析
- プロダクトタイプ: Beauty/Spa サービス
- スタイルキーワード: elegant、professional、soft
- 業界: Beauty/Wellness
- スタック: html-tailwind（デフォルト）

### ステップ 2: デザインシステムの生成（必須）

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service elegant" --design-system -p "Serenity Spa"
```

**出力:** パターン、スタイル、カラー、タイポグラフィ、エフェクト、アンチパターンを含む完全なデザインシステム。

### ステップ 3: 詳細検索で補完する（必要に応じて）

```bash
# アニメーションとアクセシビリティの UX ガイドラインを取得
python3 skills/ui-ux-pro-max/scripts/search.py "animation accessibility" --domain ux

# 必要に応じて代替タイポグラフィオプションを取得
python3 skills/ui-ux-pro-max/scripts/search.py "elegant luxury serif" --domain typography
```

### ステップ 4: スタックガイドライン

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "layout responsive form" --stack html-tailwind
```

**その後:** デザインシステム + 詳細検索を統合してデザインを実装します。

---

## 出力フォーマット

`--design-system` フラグは 2 つの出力フォーマットをサポートします：

```bash
# ASCII ボックス（デフォルト）- ターミナル表示に最適
python3 skills/ui-ux-pro-max/scripts/search.py "fintech crypto" --design-system

# Markdown - ドキュメントに最適
python3 skills/ui-ux-pro-max/scripts/search.py "fintech crypto" --design-system -f markdown
```

---

## より良い結果のためのヒント

1. **キーワードを具体的に** - 「healthcare SaaS dashboard」>「app」
2. **複数回検索する** - 異なるキーワードが異なるインサイトを明らかにする
3. **ドメインを組み合わせる** - Style + Typography + Color = 完全なデザインシステム
4. **常に UX を確認する** - よくある問題には「animation」「z-index」「accessibility」で検索
5. **stack フラグを使用する** - 実装固有のベストプラクティスを取得
6. **反復する** - 最初の検索がマッチしない場合、異なるキーワードを試す

---

## プロフェッショナル UI のための共通ルール

以下は UI を非プロフェッショナルに見せる、よく見落とされる問題です：

### アイコン & ビジュアル要素

| ルール | すること | しないこと |
|------|----|----- |
| **絵文字アイコン禁止** | SVG アイコンを使用（Heroicons、Lucide、Simple Icons） | UI アイコンとして絵文字（🎨 🚀 ⚙️）を使用 |
| **安定したホバー状態** | ホバー時にカラー/透明度トランジションを使用 | レイアウトをずらすスケールトランスフォームを使用 |
| **正確なブランドロゴ** | Simple Icons から公式 SVG を調査する | 誤ったロゴパスを推測または使用 |
| **一貫したアイコンサイズ** | 固定の viewBox（24x24）に w-6 h-6 を使用 | 異なるアイコンサイズをランダムに混在させる |

### インタラクション & カーソル

| ルール | すること | しないこと |
|------|----|----- |
| **カーソルポインター** | クリック/ホバー可能なすべてのカードに `cursor-pointer` を追加 | インタラクティブな要素にデフォルトカーソルを残す |
| **ホバーフィードバック** | ビジュアルフィードバックを提供（カラー、シャドウ、ボーダー） | 要素がインタラクティブであることの表示なし |
| **スムーズなトランジション** | `transition-colors duration-200` を使用 | 瞬時の状態変化または遅すぎる（500ms 超） |

### ライト/ダークモードのコントラスト

| ルール | すること | しないこと |
|------|----|----- |
| **グラスカードのライトモード** | `bg-white/80` 以上の不透明度を使用 | `bg-white/10` を使用（透明すぎる） |
| **テキストコントラスト（ライト）** | テキストに `#0F172A`（slate-900）を使用 | 本文テキストに `#94A3B8`（slate-400）を使用 |
| **ミュートテキスト（ライト）** | 最低 `#475569`（slate-600）を使用 | gray-400 以下を使用 |
| **ボーダーの視認性** | ライトモードで `border-gray-200` を使用 | `border-white/10` を使用（見えない） |

### レイアウト & スペーシング

| ルール | すること | しないこと |
|------|----|----- |
| **フローティングナビバー** | `top-4 left-4 right-4` スペーシングを追加 | ナビバーを `top-0 left-0 right-0` に固定 |
| **コンテンツパディング** | 固定ナビバーの高さを考慮する | コンテンツが固定要素の後ろに隠れるのを許容 |
| **一貫した最大幅** | 同じ `max-w-6xl` または `max-w-7xl` を使用 | 異なるコンテナ幅を混在させる |

---

## 納品前チェックリスト

UI コードを納品する前に以下の項目を確認してください：

### ビジュアル品質
- [ ] アイコンとして絵文字を使用していない（代わりに SVG を使用）
- [ ] すべてのアイコンが一貫したアイコンセットから（Heroicons/Lucide）
- [ ] ブランドロゴが正確（Simple Icons から検証済み）
- [ ] ホバー状態がレイアウトシフトを引き起こさない
- [ ] テーマカラーを直接使用（bg-primary）し var() ラッパーを使用しない

### インタラクション
- [ ] すべてのクリック可能な要素に `cursor-pointer` がある
- [ ] ホバー状態が明確なビジュアルフィードバックを提供する
- [ ] トランジションがスムーズ（150〜300ms）
- [ ] キーボードナビゲーションでフォーカス状態が視認可能

### ライト/ダークモード
- [ ] ライトモードのテキストに十分なコントラストがある（最低 4.5:1）
- [ ] グラス/透明な要素がライトモードで視認可能
- [ ] 両モードでボーダーが視認可能
- [ ] 納品前に両モードをテスト済み

### レイアウト
- [ ] フローティング要素がエッジから適切なスペーシングを持つ
- [ ] 固定ナビバーの後ろにコンテンツが隠れていない
- [ ] 375px、768px、1024px、1440px でレスポンシブ
- [ ] モバイルで横スクロールなし

### アクセシビリティ
- [ ] すべての画像に alt テキストがある
- [ ] フォーム入力にラベルがある
- [ ] カラーだけが唯一の指示子でない
- [ ] `prefers-reduced-motion` が尊重されている
