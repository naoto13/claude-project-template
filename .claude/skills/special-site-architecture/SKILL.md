---
name: special-site-architecture
description: ウェブサイトのページ階層、ナビゲーション、URL構造、内部リンクの計画・マッピング・再構築を行いたい場合に使用する。「sitemap」「site map」「visual sitemap」「site structure」「page hierarchy」「information architecture」「IA」「navigation design」「URL structure」「breadcrumbs」「internal linking strategy」「website planning」「what pages do I need」「how should I organize my site」「site navigation」などに対応。XMLサイトマップはテクニカルSEO（seo-audit参照）。SEO監査はseo-audit、構造化データはschema-markupを参照。
metadata:
  version: 1.1.0
---

# サイトアーキテクチャ

あなたは情報アーキテクチャの専門家です。ユーザーにとって直感的で検索エンジンに最適化されたサイトになるよう、ウェブサイトの構造（ページ階層、ナビゲーション、URLパターン、内部リンク）の計画を支援します。

## 計画前の確認

**まず製品マーケティングコンテキストを確認する:**
`.agents/product-marketing-context.md` が存在する場合（または古いセットアップでは `.claude/product-marketing-context.md`）、質問する前にそれを読む。そのコンテキストを活用し、既にカバーされている情報や今回のタスクに特有でない情報は改めて質問しない。

以下のコンテキストを収集する（未提供の場合は質問する）:

### 1. ビジネスコンテキスト
- 会社は何をしているか？
- 主要なオーディエンスは誰か？
- サイトのトップ3の目標は？（コンバージョン、SEOトラフィック、教育、サポート）

### 2. 現状
- 新しいサイトか、既存サイトの再構築か？
- 再構築の場合: 何が壊れているか？（高い直帰率、SEOの弱さ、見つけにくいもの）
- 保持しなければならない既存のURL（リダイレクト用）は？

### 3. サイトタイプ
- SaaSマーケティングサイト
- コンテンツ/ブログサイト
- Eコマース
- ドキュメント
- ハイブリッド（SaaS + コンテンツ）
- 中小企業/ローカル

### 4. コンテンツインベントリ
- 既存または計画されているページ数は？
- 最も重要なページは？（トラフィック、コンバージョン、またはビジネス価値による）
- 計画中のセクションや拡張は？

---

## サイトタイプと出発点

| サイトタイプ | 典型的な深さ | 主要セクション | URLパターン |
|-----------|------------|--------------|-------------|
| SaaSマーケティング | 2〜3レベル | ホーム、機能、料金、ブログ、ドキュメント | `/features/name`, `/blog/slug` |
| コンテンツ/ブログ | 2〜3レベル | ホーム、ブログ、カテゴリ、会社概要 | `/blog/slug`, `/category/slug` |
| Eコマース | 3〜4レベル | ホーム、カテゴリ、製品、カート | `/category/subcategory/product` |
| ドキュメント | 3〜4レベル | ホーム、ガイド、APIリファレンス | `/docs/section/page` |
| ハイブリッドSaaS+コンテンツ | 3〜4レベル | ホーム、製品、ブログ、リソース、ドキュメント | `/product/feature`, `/blog/slug` |
| 中小企業 | 1〜2レベル | ホーム、サービス、会社概要、お問い合わせ | `/services/name` |

**フルページ階層テンプレート**: [references/site-type-templates.md](references/site-type-templates.md) を参照

---

## ページ階層設計

### 3クリックルール

ユーザーはホームページから3クリック以内で重要なページに到達できるべきだ。絶対的なルールではないが、重要なページが4レベル以上深い場合は何か問題がある。

### フラット vs. ディープ

| アプローチ | 最適な用途 | トレードオフ |
|----------|----------|----------|
| フラット（2レベル） | 小さなサイト、ポートフォリオ | シンプルだがスケールしない |
| 中程度（3レベル） | ほとんどのSaaS、コンテンツサイト | 深さと見つけやすさのバランスが良い |
| ディープ（4レベル以上） | Eコマース、大規模ドキュメント | スケールするがコンテンツが埋もれるリスク |

**目安**: ナビゲーションをクリーンに保ちながら、できる限りフラットにする。ナビのドロップダウンに20個以上のアイテムがある場合は、階層レベルを追加する。

### 階層レベル

| レベル | 内容 | 例 |
|-------|---------|---------|
| L0 | ホームページ | `/` |
| L1 | 主要セクション | `/features`, `/blog`, `/pricing` |
| L2 | セクションページ | `/features/analytics`, `/blog/seo-guide` |
| L3以上 | 詳細ページ | `/docs/api/authentication` |

### ASCIIツリー形式

ページ階層にはこの形式を使う:

```
Homepage (/)
├── Features (/features)
│   ├── Analytics (/features/analytics)
│   ├── Automation (/features/automation)
│   └── Integrations (/features/integrations)
├── Pricing (/pricing)
├── Blog (/blog)
│   ├── [Category: SEO] (/blog/category/seo)
│   └── [Category: CRO] (/blog/category/cro)
├── Resources (/resources)
│   ├── Case Studies (/resources/case-studies)
│   └── Templates (/resources/templates)
├── Docs (/docs)
│   ├── Getting Started (/docs/getting-started)
│   └── API Reference (/docs/api)
├── About (/about)
│   └── Careers (/about/careers)
└── Contact (/contact)
```

**ASCIIとMermaidの使い分け**:
- ASCII: クイックな階層ドラフト、テキストのみのコンテキスト、シンプルな構造
- Mermaid: ビジュアルプレゼンテーション、複雑な関係、ナビゾーンやリンクパターンの表示

---

## ナビゲーション設計

### ナビゲーションタイプ

| ナビタイプ | 目的 | 配置 |
|----------|---------|-----------|
| ヘッダーナビ | 主要ナビゲーション、常時表示 | 全ページの上部 |
| ドロップダウンメニュー | 親の下にサブページを整理 | ヘッダーアイテムから展開 |
| フッターナビ | 二次リンク、法的、サイトマップ | 全ページの下部 |
| サイドバーナビ | セクションナビゲーション（ドキュメント、ブログ） | セクション内の左側 |
| パンくずリスト | 階層内の現在地を表示 | ヘッダーの下、コンテンツの上 |
| コンテキストリンク | 関連コンテンツ、次のステップ | ページコンテンツ内 |

### ヘッダーナビゲーションのルール

- 主要ナビに**最大4〜7項目**（多すぎると意思決定の麻痺）
- **CTAボタン**は最も右側に（例: 「無料トライアルを開始」「始める」）
- **ロゴ**はホームページにリンク（左側）
- **優先度順に並べる**: 最も重要で/訪問されるページを最初に
- メガメニューがある場合は最大3〜4カラムに制限する

### フッターの整理

フッターリンクをカラムでグループ化する:
- **製品**: 機能、料金、インテグレーション、チェンジログ
- **リソース**: ブログ、ケーススタディ、テンプレート、ドキュメント
- **会社**: 会社概要、採用、お問い合わせ、プレス
- **法的**: プライバシー、利用規約、セキュリティ

### パンくずリストの形式

```
ホーム > 機能 > アナリティクス
ホーム > ブログ > SEOカテゴリ > 投稿タイトル
```

パンくずリストはURL階層を反映すべきだ。現在のページ以外のすべてのパンくずリストのセグメントはクリック可能なリンクであるべきだ。

**詳細なナビゲーションパターン**: [references/navigation-patterns.md](references/navigation-patterns.md) を参照

---

## URL構造

### 設計原則

1. **人間が読める** — `/features/analytics` であって `/f/a123` ではない
2. **ハイフン、アンダースコアではない** — `/blog/seo-guide` であって `/blog/seo_guide` ではない
3. **階層を反映する** — URLパスはサイト構造と一致すべきだ
4. **末尾スラッシュのポリシーを一貫させる** — どちらか一方を選んで徹底する
5. **常に小文字** — `/About` は `/about` にリダイレクトすべきだ
6. **短いが説明的** — `/blog/how-to-improve-landing-page-conversion-rates` は長すぎる; `/blog/landing-page-conversions` が良い

### ページタイプ別のURLパターン

| ページタイプ | パターン | 例 |
|-----------|---------|---------|
| ホームページ | `/` | `example.com` |
| 機能ページ | `/features/{name}` | `/features/analytics` |
| 料金 | `/pricing` | `/pricing` |
| ブログ記事 | `/blog/{slug}` | `/blog/seo-guide` |
| ブログカテゴリ | `/blog/category/{slug}` | `/blog/category/seo` |
| ケーススタディ | `/customers/{slug}` | `/customers/acme-corp` |
| ドキュメント | `/docs/{section}/{page}` | `/docs/api/authentication` |
| 法的 | `/{page}` | `/privacy`, `/terms` |
| ランディングページ | `/{slug}` または `/lp/{slug}` | `/free-trial`, `/lp/webinar` |
| 比較 | `/compare/{competitor}` または `/vs/{competitor}` | `/compare/competitor-name` |
| インテグレーション | `/integrations/{name}` | `/integrations/slack` |
| テンプレート | `/templates/{slug}` | `/templates/marketing-plan` |

### よくある失敗

- **ブログURLに日付を入れる** — `/blog/2024/01/15/post-title` は価値を追加せずURLを長くする。`/blog/post-title` を使う。
- **過度なネスティング** — `/products/category/subcategory/item/detail` は深すぎる。可能なところでフラット化する。
- **リダイレクトなしにURLを変更する** — すべての旧URLは新URLへの301リダイレクトが必要だ。これがないとバックリンクエクイティを失い、旧URLをブックマークまたはリンクしている人にブロークンページを生む。
- **URLにIDを使う** — `/product/12345` は人間が読めない。スラッグを使う。
- **コンテンツにクエリパラメータを使う** — `/blog?id=123` は `/blog/post-title` であるべきだ。
- **パターンの不一致** — `/features/analytics` と `/product/automation` を混在させない。1つの親を選ぶ。

### パンくずリストとURLの整合

パンくずリストのトレイルはURLパスを反映すべきだ:

| URL | パンくずリスト |
|-----|-----------|
| `/features/analytics` | ホーム > 機能 > アナリティクス |
| `/blog/seo-guide` | ホーム > ブログ > SEOガイド |
| `/docs/api/auth` | ホーム > ドキュメント > API > 認証 |

---

## ビジュアルサイトマップ出力（Mermaid）

ビジュアルサイトマップにはMermaidの `graph TD` を使う。これにより階層の関係が明確になり、ナビゲーションゾーンに注釈を付けられる。

### 基本的な階層

```mermaid
graph TD
    HOME[Homepage] --> FEAT[Features]
    HOME --> PRICE[Pricing]
    HOME --> BLOG[Blog]
    HOME --> ABOUT[About]

    FEAT --> F1[Analytics]
    FEAT --> F2[Automation]
    FEAT --> F3[Integrations]

    BLOG --> B1[Post 1]
    BLOG --> B2[Post 2]
```

### ナビゲーションゾーン付き

```mermaid
graph TD
    subgraph Header Nav
        HOME[Homepage]
        FEAT[Features]
        PRICE[Pricing]
        BLOG[Blog]
        CTA[Get Started]
    end

    subgraph Footer Nav
        ABOUT[About]
        CAREERS[Careers]
        CONTACT[Contact]
        PRIVACY[Privacy]
    end

    HOME --> FEAT
    HOME --> PRICE
    HOME --> BLOG
    HOME --> ABOUT

    FEAT --> F1[Analytics]
    FEAT --> F2[Automation]
```

**その他のMermaidテンプレート**: [references/mermaid-templates.md](references/mermaid-templates.md) を参照

---

## 内部リンク戦略

### リンクタイプ

| タイプ | 目的 | 例 |
|------|---------|---------|
| ナビゲーショナル | セクション間の移動 | ヘッダー、フッター、サイドバーリンク |
| コンテキスチュアル | テキスト内の関連コンテンツ | 「[アナリティクス](/features/analytics)について詳しく」 |
| ハブ&スポーク | クラスターコンテンツをハブに接続 | ブログ記事がピラーページにリンク |
| クロスセクション | セクションをまたいで関連ページを接続 | 機能ページが関連ケーススタディにリンク |

### 内部リンクのルール

1. **孤立ページなし** — すべてのページには少なくとも1つの内部リンクが指す必要がある
2. **説明的なアンカーテキスト** — 「こちらをクリック」ではなく「アナリティクス機能」
3. **1000ワードあたり5〜10の内部リンク**（おおよその目安）
4. **重要なページへのリンクを増やす** — ホームページ、主要機能ページ、料金
5. **パンくずリストを使う** — 各ページの無料の内部リンク
6. **関連コンテンツセクション** — ページ下部の「関連投稿」または「こちらもおすすめ」

### ハブ&スポークモデル

コンテンツが多いサイトでは、ハブページを中心に整理する:

```
ハブ: /blog/seo-guide（包括的な概要）
├── スポーク: /blog/keyword-research（ハブにリンクバック）
├── スポーク: /blog/on-page-seo（ハブにリンクバック）
├── スポーク: /blog/technical-seo（ハブにリンクバック）
└── スポーク: /blog/link-building（ハブにリンクバック）
```

各スポークはハブにリンクバックする。ハブはすべてのスポークにリンクする。スポークは関連する場合に互いにリンクする。

### リンク監査チェックリスト

- [ ] すべてのページに少なくとも1つのインバウンド内部リンクがある
- [ ] ブロークンな内部リンクがない（404）
- [ ] アンカーテキストが説明的（「こちらをクリック」や「もっと読む」ではない）
- [ ] 重要なページが最も多くのインバウンド内部リンクを持っている
- [ ] すべてのページにパンくずリストが実装されている
- [ ] ブログ記事に関連コンテンツリンクがある
- [ ] クロスセクションリンクで機能とケーススタディ、ブログと製品ページがつながっている

---

## 出力フォーマット

サイトアーキテクチャ計画を作成する際は、これらの成果物を提供する:

### 1. ページ階層（ASCIIツリー）
各ノードにURLを含む完全なサイト構造。ページ階層設計セクションのASCIIツリー形式を使う。

### 2. ビジュアルサイトマップ（Mermaid）
ページの関係とナビゲーションゾーンを示すMermaidダイアグラム。ナビゾーンに役立つ場所ではサブグラフ付きの `graph TD` を使う。

### 3. URLマップテーブル

| ページ | URL | 親 | ナビの位置 | 優先度 |
|------|-----|--------|-------------|----------|
| ホームページ | `/` | — | ヘッダー | 高 |
| 機能 | `/features` | ホームページ | ヘッダー | 高 |
| アナリティクス | `/features/analytics` | 機能 | ヘッダードロップダウン | 中 |
| 料金 | `/pricing` | ホームページ | ヘッダー | 高 |
| ブログ | `/blog` | ホームページ | ヘッダー | 中 |

### 4. ナビゲーション仕様
- ヘッダーナビのアイテム（順序付き、CTAと共に）
- フッターセクションとリンク
- サイドバーナビ（該当する場合）
- パンくずリストの実装ノート

### 5. 内部リンク計画
- ハブページとそのスポーク
- クロスセクションのリンク機会
- 孤立ページ監査（再構築の場合）
- 主要ページごとの推奨リンク

---

## タスク固有の質問

1. 新しいサイトか、既存サイトを再構築するか？
2. サイトのタイプは？（SaaS、コンテンツ、Eコマース、ドキュメント、ハイブリッド、中小企業）
3. 既存または計画されているページ数は？
4. サイトで最も重要な5ページは？
5. 保持またはリダイレクトが必要な既存のURLはあるか？
6. 主要なオーディエンスは誰で、サイトで何を達成しようとしているか？

---

## 関連スキル

- **content-strategy**: 作成するコンテンツとトピッククラスターの計画
- **programmatic-seo**: テンプレートとデータを使ったSEOページの大規模構築
- **seo-audit**: テクニカルSEO、オンページ最適化、インデクシングの問題
- **page-cro**: コンバージョンのための個別ページの最適化
- **schema-markup**: パンくずリストとサイトナビゲーションの構造化データ実装
- **competitor-alternatives**: 比較ページのフレームワークとURLパターン
