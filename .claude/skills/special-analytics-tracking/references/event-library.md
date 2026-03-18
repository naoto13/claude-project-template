# イベントライブラリリファレンス

ビジネスタイプとコンテキスト別の包括的なトラッキングイベントリスト。

## 目次
- マーケティングサイトイベント（ナビゲーション・エンゲージメント、CTA・フォームインタラクション、コンバージョンイベント）
- プロダクト/アプリイベント（オンボーディング、コア利用、エラー・サポート）
- マネタイゼーションイベント（料金・チェックアウト、サブスクリプション管理）
- Eコマースイベント（ブラウジング、カート、チェックアウト、購入後）
- B2B / SaaS固有イベント（チーム・コラボレーション、インテグレーションイベント、アカウントイベント）
- イベントプロパティ（パラメータ）
- ファネルイベントシーケンス

## マーケティングサイトイベント

### ナビゲーション・エンゲージメント

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| page_view | ページ読み込み（拡張） | page_title, page_location, content_group |
| scroll_depth | ユーザーが閾値までスクロール | depth (25, 50, 75, 100) |
| outbound_link_clicked | 外部サイトへのクリック | link_url, link_text |
| internal_link_clicked | サイト内のクリック | link_url, link_text, location |
| video_played | 動画再生開始 | video_id, video_title, duration |
| video_completed | 動画再生終了 | video_id, video_title, duration |

### CTA・フォームインタラクション

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| cta_clicked | CTAボタンのクリック | button_text, cta_location, page |
| form_started | フォーム入力開始 | form_name, form_location |
| form_field_completed | フィールド入力 | form_name, field_name |
| form_submitted | フォーム送信成功 | form_name, form_location |
| form_error | フォームバリデーション失敗 | form_name, error_type |
| resource_downloaded | 資料ダウンロード | resource_name, resource_type |

### コンバージョンイベント

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| signup_started | サインアップ開始 | source, page |
| signup_completed | サインアップ完了 | method, plan, source |
| demo_requested | デモフォーム送信 | company_size, industry |
| contact_submitted | お問い合わせフォーム送信 | inquiry_type |
| newsletter_subscribed | メールリスト登録 | source, list_name |
| trial_started | 無料トライアル開始 | plan, source |

---

## プロダクト/アプリイベント

### オンボーディング

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| signup_completed | アカウント作成 | method, referral_source |
| onboarding_started | オンボーディング開始 | - |
| onboarding_step_completed | ステップ完了 | step_number, step_name |
| onboarding_completed | すべてのステップ完了 | steps_completed, time_to_complete |
| onboarding_skipped | オンボーディングをスキップ | step_skipped_at |
| first_key_action_completed | Ahaモーメント到達 | action_type |

### コア利用

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| session_started | アプリセッション開始 | session_number |
| feature_used | 機能とのインタラクション | feature_name, feature_category |
| action_completed | コアアクション実行 | action_type, count |
| content_created | ユーザーがコンテンツ作成 | content_type |
| content_edited | ユーザーがコンテンツ編集 | content_type |
| content_deleted | ユーザーがコンテンツ削除 | content_type |
| search_performed | アプリ内検索 | query, results_count |
| settings_changed | 設定変更 | setting_name, new_value |
| invite_sent | ユーザーが他のユーザーを招待 | invite_type, count |

### エラー・サポート

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| error_occurred | エラー発生 | error_type, error_message, page |
| help_opened | ヘルプにアクセス | help_type, page |
| support_contacted | サポートリクエスト送信 | contact_method, issue_type |
| feedback_submitted | ユーザーフィードバック送信 | feedback_type, rating |

---

## マネタイゼーションイベント

### 料金・チェックアウト

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| pricing_viewed | 料金ページ表示 | source |
| plan_selected | プラン選択 | plan_name, billing_cycle |
| checkout_started | チェックアウト開始 | plan, value |
| payment_info_entered | 支払い情報送信 | payment_method |
| purchase_completed | 購入成功 | plan, value, currency, transaction_id |
| purchase_failed | 購入失敗 | error_reason, plan |

### サブスクリプション管理

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| trial_started | トライアル開始 | plan, trial_length |
| trial_ended | トライアル終了 | plan, converted (bool) |
| subscription_upgraded | プランアップグレード | from_plan, to_plan, value |
| subscription_downgraded | プランダウングレード | from_plan, to_plan |
| subscription_cancelled | キャンセル | plan, reason, tenure |
| subscription_renewed | 更新 | plan, value |
| billing_updated | 支払い方法変更 | - |

---

## Eコマースイベント

### ブラウジング

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| product_viewed | 商品ページ閲覧 | product_id, product_name, category, price |
| product_list_viewed | カテゴリ/リスト閲覧 | list_name, products[] |
| product_searched | 商品検索 | query, results_count |
| product_filtered | フィルター適用 | filter_type, filter_value |
| product_sorted | 並び替え適用 | sort_by, sort_order |

### カート

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| product_added_to_cart | 商品をカートに追加 | product_id, product_name, price, quantity |
| product_removed_from_cart | 商品をカートから削除 | product_id, product_name, price, quantity |
| cart_viewed | カートページ閲覧 | cart_value, items_count |

### チェックアウト

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| checkout_started | チェックアウト開始 | cart_value, items_count |
| checkout_step_completed | ステップ完了 | step_number, step_name |
| shipping_info_entered | 住所入力 | shipping_method |
| payment_info_entered | 支払い情報入力 | payment_method |
| coupon_applied | クーポン使用 | coupon_code, discount_value |
| purchase_completed | 注文確定 | transaction_id, value, currency, items[] |

### 購入後

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| order_confirmed | 注文確認表示 | transaction_id |
| refund_requested | 返金申請 | transaction_id, reason |
| refund_completed | 返金処理完了 | transaction_id, value |
| review_submitted | 商品レビュー投稿 | product_id, rating |

---

## B2B / SaaS固有イベント

### チーム・コラボレーション

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| team_created | 新しいチーム/組織作成 | team_size, plan |
| team_member_invited | 招待送信 | role, invite_method |
| team_member_joined | メンバーが参加を承認 | role |
| team_member_removed | メンバー削除 | role |
| role_changed | 権限更新 | user_id, old_role, new_role |

### インテグレーションイベント

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| integration_viewed | インテグレーションページ閲覧 | integration_name |
| integration_started | セットアップ開始 | integration_name |
| integration_connected | 接続成功 | integration_name |
| integration_disconnected | インテグレーション削除 | integration_name, reason |

### アカウントイベント

| イベント名 | 説明 | プロパティ |
|------------|-------------|------------|
| account_created | 新規アカウント | source, plan |
| account_upgraded | プランアップグレード | from_plan, to_plan |
| account_churned | アカウント解約 | reason, tenure, mrr_lost |
| account_reactivated | 復帰ユーザー | previous_tenure, new_plan |

---

## イベントプロパティ（パラメータ）

### 標準的に含めるプロパティ

**ユーザーコンテキスト:**
```
user_id: "12345"
user_type: "free" | "trial" | "paid"
account_id: "acct_123"
plan_type: "starter" | "pro" | "enterprise"
```

**セッションコンテキスト:**
```
session_id: "sess_abc"
session_number: 5
page: "/pricing"
referrer: "https://google.com"
```

**キャンペーンコンテキスト:**
```
source: "google"
medium: "cpc"
campaign: "spring_sale"
content: "hero_cta"
```

**プロダクトコンテキスト（Eコマース）:**
```
product_id: "SKU123"
product_name: "Product Name"
category: "Category"
price: 99.99
quantity: 1
currency: "USD"
```

**タイミング:**
```
timestamp: "2024-01-15T10:30:00Z"
time_on_page: 45
session_duration: 300
```

---

## ファネルイベントシーケンス

### サインアップファネル
1. signup_started
2. signup_step_completed (email)
3. signup_step_completed (password)
4. signup_completed
5. onboarding_started

### 購入ファネル
1. pricing_viewed
2. plan_selected
3. checkout_started
4. payment_info_entered
5. purchase_completed

### Eコマースファネル
1. product_viewed
2. product_added_to_cart
3. cart_viewed
4. checkout_started
5. shipping_info_entered
6. payment_info_entered
7. purchase_completed
