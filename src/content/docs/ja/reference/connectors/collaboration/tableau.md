---
title: Tableau接続
description: 個人用アクセストークンを使ってPlaidCloudをTableau ServerまたはTableau Cloudに接続し、ワークフローからデータソースを公開できるようにします。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/collaboration/tableau.md
---

Tableau接続には、Tableau ServerまたはTableau Cloudサイトのアドレスと、個人用アクセストークンが保持されます。[Publish to Tableau](/ja/reference/workflow-steps/export/export-to-tableau/)ステップは、この接続を使用して`.hyper`抽出をデータソースとして公開します。

## 開始する前に

Tableauで、公開を行うアカウントの個人用アクセストークンを作成します。**My Account Settings**を選択し、次に**Personal Access Tokens**を選択します。トークンのシークレットはTableauに表示されたときにコピーしてください。Tableauでは再表示されません。このアカウントには、公開先のプロジェクトにデータソースを公開する権限が必要です。

## 接続を作成する

1. **分析**を開き、**Tools → 外部データ接続**を選択して、**+ 新規接続 → Tableau**を選択します。
2. 接続の名前と説明を入力します。
3. 接続の設定を入力します。

| 項目 | 入力する内容 |
| --- | --- |
| **サーバーURL** | サーバーまたはTableau Cloudポッドのアドレス。たとえば`https://prod-useast-a.online.tableau.com`です。ホスト名のみの場合は`https`として扱われ、`http`アドレスは拒否されます。 |
| **サイト** | サイトのコンテンツURL。ブラウザーのアドレスのうち`#/site/`の後ろの部分です。Defaultサイトの場合は空白のままにします。 |
| **個人用アクセストークン名** | Tableauでトークンに付けた名前。 |
| **個人用アクセストークンのシークレット** | トークンのシークレット。暗号化して保存され、接続を開き直すと空白で表示されます。保存済みのシークレットを維持するには、空白のままにします。 |

4. **作成**を選択します。

サーバーはインターネットから到達可能である必要があります。PlaidCloudは、プライベートネットワーク上のTableauサーバーには接続しません。

## 関連項目

- [Publish to Tableau](/ja/reference/workflow-steps/export/export-to-tableau/)ステップ
- [Tableau Hyper Export](/ja/reference/workflow-steps/export/export-hyper/)ステップ
