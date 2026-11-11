---
title: ファイル管理
description: CSV、Excel、Parquet などのファイル形式でデータをインポートおよびエクスポートするための、PlaidCloud のファイルストレージアカウントを管理します。
sidebar:
  label: 概要
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/index.md
---

PlaidCloud ドキュメント：データやワークフローと並べて、ファイルを保存、整理、検索、共有できます。ドキュメントは、接続された任意のストレージアカウントから取得でき、ワークフローから参照できます。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="S3、Google Cloud Storage、OneDrive などの接続されたストレージアカウントが PlaidCloud ドキュメントにファイルを供給し、ドキュメントではファイルの保存、整理、検索、共有を行います。その後、ワークフローのステップがそれらのファイルを参照して、データのインポートとエクスポートを行います。" style="width:100%;max-width:680px;height:auto;">
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
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">ファイルは、接続された任意のストレージアカウントからドキュメントに取り込まれ、そこで保存、整理、検索、共有を行います。その後、ワークフローのステップから参照して、データをインポートおよびエクスポートします。</figcaption>
</figure>

## ドキュメントワークスペース

**ドキュメント**を開くと、左側にレールが表示され、その横に選択したページが表示されます。レールでは、ページが**ドキュメント**（**概要**と**参照**）と**勘定科目**（**Your accounts** と**管理**）にグループ化されています。ページを開く権限のないメンバーには、その項目は表示されません。各ページの上部にはタイトルと短いサブタイトルがあり、そのアクションは横のヘッダーに表示されます。

| レールの項目 | 表示内容 |
|---|---|
| **概要** | アカウントのタイル（**勘定科目**、**Shared**、**Private to you**、**Managed buckets**、**External services**、アカウントの対応が必要な場合は**無効**）、**Pinned** ファイル、**Accounts by service**、**Who can use them**。ピン留めされたファイルを選択すると、そのフォルダーでファイルが選択された状態の**参照**が開きます。 |
| **参照** | ファイルエクスプローラー。お気に入りのアカウント（トップフォルダーをピン留めしたアカウント）またはワークスペースのデフォルトのアカウントが開き、ページヘッダーのリストから別のアカウントを選択できます。[ドキュメントアカウントの使い方](/ja/guides/documents/using-document/)を参照してください。 |
| **Your accounts** | 使用できるすべてのアカウントを1つの一覧に表示します。各行の **Shared** または**プライベート**のピルは、そのアカウントが自分と共有されているものか、自分専用のものかを示します。行をダブルクリックすると、そのアカウントを参照します。 |
| **管理** | 所有しているアカウント。**名前**、**サービス**、**Security type**、**ステータス**、**説明**が表示されます。ワークスペース管理者はここですべてのドキュメントアカウントを確認でき、他の方法で管理できる任意のアカウントを管理できます。システム管理のアカウントは拒否され、管理対象バケットのアカウントは複製できません。 |

レールには、**Your accounts** と**管理**の横にカウントが表示されます。所有していないアカウントを保持しているワークスペース管理者には、**管理**にカウントの代わりに **admin** が表示されます。概要には、すぐに始められるよう**ファイルを参照**と**新しいアカウント**のボタンがあります。

### 管理の行アクション

行の **⋯** メニューを開くか、行を右クリックするか、ツールバーの**アクション**メニューを使用して、次の操作を行います。

- **開く**と**編集**。アカウントページが開きます。
- **Clone…**、**Version history**、**使用箇所…**。[使用箇所と再指定](/ja/guides/documents/account-management/document-account-used-by/)を参照してください。
- **Who can use it**（**メンバー**、**グループ**、**エージェント**、**所有者**付き）。[ドキュメントアカウントのアクセス制御](/ja/guides/documents/account-management/control-document-account-access/)を参照してください。
- **有効にする**または**無効**、および**削除**。

### アカウントページ

**新しいアカウント**、**開く**、**編集**を選択すると、アカウントがページとして表示され、上部の**アカウントの管理**で戻ることができます。ページには次のカードがあります。

- **一般**：アカウントの名前、サービス、バケット、開始パス。
- **アクセス**：セキュリティモデルと、アカウントを使用できるユーザー。**メンバー**、**グループ**、**エージェント**、**所有者**にはそれぞれ**編集**リンクがあり、行メニューと同じピッカーが開きます。
- **Credentials**：選択したサービス用の書き込み専用フィールド。**Credentials saved** の注記は、認証情報が設定済みであることを示します。保存された値は表示されません。保存されている内容を維持するには、フィールドを空白のままにします。SFTP アカウントには**接続をテスト**もあります。
- **SSH**：SFTP アカウントのみのキー設定。

ヘッダーには、**参照**、**使用箇所**、そして**複製**、**Version history**、**有効にする**または**無効**、**削除**を含む**アクション**メニューがあります。保存されていない変更がある状態でページを離れようとすると、PlaidCloud は変更を破棄するかどうかを確認します。

ドキュメント画面への古いリンクやブックマークも、対応するページが引き続き開きます。
