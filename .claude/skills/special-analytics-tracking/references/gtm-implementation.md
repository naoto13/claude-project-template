# Google Tag Manager実装リファレンス

Google Tag Manager経由でトラッキングを実装するための詳細ガイド。

## 目次
- コンテナ構成（タグ、トリガー、変数）
- 命名規則
- データレイヤーパターン
- 一般的なタグ設定（GA4設定タグ、GA4イベントタグ、Facebookピクセル）
- プレビューとデバッグ
- ワークスペースとバージョン管理
- 同意管理
- 高度なパターン（タグシーケンス、例外処理、カスタムJavaScript変数）

## コンテナ構成

### タグ

タグはトリガーされたときに実行されるコードスニペット。

**主なタグの種類:**
- GA4設定（基本セットアップ）
- GA4イベント（カスタムイベント）
- Google Adsコンバージョン
- Facebookピクセル
- LinkedIn Insight Tag
- カスタムHTML（その他のピクセル向け）

### トリガー

トリガーはタグが発火するタイミングを定義する。

**組み込みトリガー:**
- ページビュー: すべてのページ、DOM準備完了、ウィンドウ読み込み完了
- クリック: すべての要素、リンクのみ
- フォーム送信
- スクロール深度
- タイマー
- 要素の表示

**カスタムトリガー:**
- カスタムイベント（dataLayerから）
- トリガーグループ（複数条件）

### 変数

変数は動的な値を取得する。

**組み込み変数（必要に応じて有効化）:**
- クリックテキスト、クリックURL、クリックID、クリッククラス
- ページパス、ページURL、ページホスト名
- リファラー
- フォーム要素、フォームID

**ユーザー定義変数:**
- データレイヤー変数
- JavaScript変数
- ルックアップテーブル
- 正規表現テーブル
- 定数

---

## 命名規則

### 推奨形式

```
[タイプ] - [説明] - [詳細]

タグ:
GA4 - Event - Signup Completed
GA4 - Config - Base Configuration
FB - Pixel - Page View
HTML - LiveChat Widget

トリガー:
Click - CTA Button
Submit - Contact Form
View - Pricing Page
Custom - signup_completed

変数:
DL - user_id
JS - Current Timestamp
LT - Campaign Source Map
```

---

## データレイヤーパターン

### 基本構造

```javascript
// 初期化（GTMより前の<head>内）
window.dataLayer = window.dataLayer || [];

// イベントをプッシュ
dataLayer.push({
  'event': 'event_name',
  'property1': 'value1',
  'property2': 'value2'
});
```

### ページ読み込み時のデータ

```javascript
// ページ読み込み時に設定する（GTMコンテナより前）
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  'pageType': 'product',
  'contentGroup': 'products',
  'user': {
    'loggedIn': true,
    'userId': '12345',
    'userType': 'premium'
  }
});
```

### フォーム送信

```javascript
document.querySelector('#contact-form').addEventListener('submit', function() {
  dataLayer.push({
    'event': 'form_submitted',
    'formName': 'contact',
    'formLocation': 'footer'
  });
});
```

### ボタンクリック

```javascript
document.querySelector('.cta-button').addEventListener('click', function() {
  dataLayer.push({
    'event': 'cta_clicked',
    'ctaText': this.innerText,
    'ctaLocation': 'hero'
  });
});
```

### Eコマースイベント

```javascript
// 商品閲覧
dataLayer.push({ ecommerce: null }); // 前のデータをクリア
dataLayer.push({
  'event': 'view_item',
  'ecommerce': {
    'items': [{
      'item_id': 'SKU123',
      'item_name': 'Product Name',
      'price': 99.99,
      'item_category': 'Category',
      'quantity': 1
    }]
  }
});

// カートに追加
dataLayer.push({ ecommerce: null });
dataLayer.push({
  'event': 'add_to_cart',
  'ecommerce': {
    'items': [{
      'item_id': 'SKU123',
      'item_name': 'Product Name',
      'price': 99.99,
      'quantity': 1
    }]
  }
});

// 購入
dataLayer.push({ ecommerce: null });
dataLayer.push({
  'event': 'purchase',
  'ecommerce': {
    'transaction_id': 'T12345',
    'value': 99.99,
    'currency': 'USD',
    'tax': 5.00,
    'shipping': 10.00,
    'items': [{
      'item_id': 'SKU123',
      'item_name': 'Product Name',
      'price': 99.99,
      'quantity': 1
    }]
  }
});
```

---

## 一般的なタグ設定

### GA4設定タグ

**タグタイプ:** Google Analytics: GA4設定

**設定:**
- 測定ID: G-XXXXXXXX
- ページビューを送信: オン（ページビュー計測に必要）
- ユーザープロパティ: ユーザーレベルのディメンションを追加する

**トリガー:** すべてのページ

### GA4イベントタグ

**タグタイプ:** Google Analytics: GA4イベント

**設定:**
- 設定タグ: 作成した設定タグを選択
- イベント名: {{DL - event_name}} またはハードコード
- イベントパラメータ: dataLayerからパラメータを追加

**トリガー:** イベント名に一致するカスタムイベント

### Facebookピクセル - ベース

**タグタイプ:** カスタムHTML

```html
<script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', 'YOUR_PIXEL_ID');
  fbq('track', 'PageView');
</script>
```

**トリガー:** すべてのページ

### Facebookピクセル - イベント

**タグタイプ:** カスタムHTML

```html
<script>
  fbq('track', 'Lead', {
    content_name: '{{DL - form_name}}'
  });
</script>
```

**トリガー:** カスタムイベント - form_submitted

---

## プレビューとデバッグ

### プレビューモード

1. GTMで「プレビュー」をクリックする
2. サイトURLを入力する
3. GTMデバッグパネルが下部に表示される

**確認すべき内容:**
- このイベントで発火したタグ
- 発火しなかったタグ（理由も確認）
- 変数とその値
- データレイヤーの内容

### デバッグのコツ

**タグが発火しない:**
- トリガー条件を確認する
- データレイヤーへのプッシュを確認する
- タグのシーケンスを確認する

**変数の値が正しくない:**
- データレイヤーの構造を確認する
- 変数のパスを確認する（ネストされたオブジェクト）
- タイミングを確認する（データがまだ存在しない可能性）

**複数回発火している:**
- トリガーの一意性を確認する
- タグの重複を探す
- タグの発火オプションを確認する

---

## ワークスペースとバージョン管理

### ワークスペース

チームコラボレーションのためにワークスペースを使用する:
- 本番用にデフォルトワークスペースを使う
- 大きな変更には別のワークスペースを使う
- 準備ができたらマージする

### バージョン管理

**ベストプラクティス:**
- すべてのバージョンにわかりやすい名前をつける
- 変更内容を説明するメモを追加する
- 公開前に変更内容をレビューする
- 本番バージョンを記録しておく

**バージョンメモの例:**
```
v15: 購入コンバージョントラッキングを追加
- 新しいタグ: GA4 - Event - Purchase
- 新しいトリガー: Custom Event - purchase
- 新しい変数: DL - transaction_id, DL - value
- テスト済み: Chrome、Safari、モバイル
```

---

## 同意管理

### 同意モードの連携

```javascript
// デフォルト状態（同意前）
gtag('consent', 'default', {
  'analytics_storage': 'denied',
  'ad_storage': 'denied'
});

// 同意時に更新
function grantConsent() {
  gtag('consent', 'update', {
    'analytics_storage': 'granted',
    'ad_storage': 'granted'
  });
}
```

### GTM同意の概要

1. 管理画面で同意の概要を有効にする
2. 各タグの同意を設定する
3. タグは同意の状態を自動的に尊重する

---

## 高度なパターン

### タグシーケンス

**タグを順番に発火させる設定:**
タグ設定 > 詳細設定 > タグシーケンス

**ユースケース:**
- イベントタグより前に設定タグを発火させる
- トラッキング前にピクセルを初期化する
- コンバージョン後にクリーンアップを実行する

### 例外処理

**トリガーの例外** — タグの発火を防ぐ:
- 特定のページを除外する
- 内部トラフィックを除外する
- テスト中に除外する

### カスタムJavaScript変数

```javascript
// URLパラメータを取得
function() {
  var params = new URLSearchParams(window.location.search);
  return params.get('campaign') || '(not set)';
}

// Cookieの値を取得
function() {
  var match = document.cookie.match('(^|;) ?user_id=([^;]*)(;|$)');
  return match ? match[2] : null;
}

// ページからデータを取得
function() {
  var el = document.querySelector('.product-price');
  return el ? parseFloat(el.textContent.replace('$', '')) : 0;
}
```
