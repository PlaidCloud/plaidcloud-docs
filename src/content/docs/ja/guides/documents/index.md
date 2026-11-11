---
title: ファイル管理
description: CSV、Excel、Parquetなどのファイル形式でデータをインポートおよびエクスポートするために、PlaidCloudでファイルストレージアカウントを管理します。
sidebar:
  label: 概要
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/index.md
---

PlaidCloud Documents では、データやワークフローと並べて、ファイルの保存、整理、検索、共有を行えます。ドキュメントは、接続済みの任意のストレージアカウントから取得でき、ワークフローから参照できます。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="S3、Google Cloud Storage、OneDriveなどの接続済みストレージアカウントがPlaidCloud Documentsにデータを供給し、そこでファイルの保存、整理、検索、共有が行われます。その後、ワークフローのステップがこれらのファイルを参照して、データをインポートおよびエクスポートします。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="dc-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">ストレージアカウント</text>
  <rect x="16" y="40" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="60" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">S3</text>
  <rect x="16" y="82" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Cloud Storage</text>
  <rect x="16" y="124" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">OneDrive</text>
  <path d="M136 55 C186 55 206 92 246 96" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 97 L246 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 139 C186 139 206 108 246 104" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="248" y="70" width="180" height="64" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="338" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">ドキュメント</text>
  <text x="338" y="115" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">保存 · 整理 · 検索 · 共有</text>
  <path d="M428 102 L510 102" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="512" y="76" width="152" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="588" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">ワークフローのステップ</text>
  <text x="588" y="118" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">ファイルのインポート · エクスポート</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">ファイルは、接続済みの任意のストレージアカウントからドキュメントに取り込まれ、そこで保存、整理、検索、共有を行います。その後、ワークフローのステップから参照して、データをインポートおよびエクスポートします。</figcaption>
</figure>

## ドキュメントワークスペース

**ドキュメント**を開くと、左側にレールが、その横に選択したページが表示されます。レールはページを**ドキュメント**（**概要**と**参照**）と**アカウント**（**あなたのアカウント**と**管理**）にまとめています。ページを開けないメンバーには、その項目は表示されません。ページにはタイトルがあり、多くの場合サブタイトルが付き、アクションはその横のヘッダーに表示されます。

| レールの項目 | 表示内容 |
|---|---|
| **概要** | アカウントのタイル（**アカウント**は**あなたのアカウント**を開き、**マネージドバケット**、**外部サービス**、**無効**が続きます。**無効**は、所有するアカウントが無効になっていると**要対応**のタグが付き、**管理**を開きます）、**ピン留め**したファイル、**サービス別のアカウント**、**利用できるユーザー**。ピン留めしたファイルを選択すると、そのフォルダーで**参照**が開き、ファイルが選択された状態になります。 |
| **参照** | ファイルエクスプローラー。お気に入りのアカウント（最上位フォルダーをピン留めしたアカウント）、またはワークスペースのデフォルトのアカウントが開き、ページヘッダーの一覧から別のアカウントを選択できます。[ドキュメントアカウントの使用](/ja/guides/documents/using-document/)を参照してください。 |
| **あなたのアカウント** | 使用できるすべてのアカウントを1つにまとめた一覧。各行の**共有**または**プライベート**のピルで、あなたと共有されているアカウントか、あなただけのアカウントかがわかります。行をダブルクリックすると参照できます。 |
| **管理** | あなたが所有するアカウント。**名前**、**サービス**、**セキュリティの種類**、**ステータス**、**説明**が表示されます。ワークスペース管理者には、ここにすべてのドキュメントアカウントが表示され、ほかの方法でも管理できるアカウントであれば管理できます。システム管理のアカウントは拒否され、マネージドバケットのアカウントは複製できません。 |

レールの**あなたのアカウント**の横には件数が表示されます。概要には、すぐに始められるように**ファイルを参照**ボタンと**新しいアカウント**ボタンがあります。

### 管理での行アクション

行の **⋯** メニューを開くか、行を右クリックするか、ツールバーの**アクション**メニューを使用すると、次の操作を行えます。

- **開く**と**編集**。アカウントページが開きます。
- **複製…**、**バージョン履歴**、**使用箇所…**。[使用箇所と付け替え](/ja/guides/documents/account-management/document-account-used-by/)を参照してください。
- **使用できるユーザー**（**メンバー**、**グループ**、**エージェント**、**所有者**）。[ドキュメントアカウントへのアクセスを制御する](/ja/guides/documents/account-management/control-document-account-access/)を参照してください。
- **有効にする**または**無効にする**、および**削除**。

### アカウントページ

**新しいアカウント**、**開く**、**編集**を選択すると、アカウントがページとして表示され、上部の**アカウントの管理**から前の画面に戻れます。ページには次のカードがあります。

- **一般**：アカウントの名前、サービス、バケット、開始パス。
- **アクセス**：セキュリティモデルと、アカウントを使用できるユーザー。**メンバー**、**グループ**、**エージェント**、**所有者**にはそれぞれ**編集**リンクがあり、行メニューと同じ選択画面が開きます。
- **認証情報**：選択したサービス用の書き込み専用フィールド。認証情報が設定済みであることは **Credentials saved** という注記で示され、保存された値が表示されることはありません。保存済みの値をそのまま使うには、フィールドを空白のままにします。SFTP アカウントには**接続をテスト**もあります。
- **SSH**：SFTP アカウント専用のキー設定。

ヘッダーには、**参照**、**使用箇所**、および**複製**、**バージョン履歴**、**有効にする**または**無効にする**、**削除**を含む**アクション**メニューがあります。未保存の変更があるままページを離れようとすると、PlaidCloud は変更を破棄するかどうかを確認します。

ドキュメント画面への古いリンクやブックマークからも、対応するページが開きます。
