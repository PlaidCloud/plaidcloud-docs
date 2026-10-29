---
title: PlaidCloud マネージドバケットアカウントの追加
description: 完全マネージドのファイルストレージを、1回の操作でPlaidCloud ドキュメントに追加します。名前を選ぶだけで、設定はすべて PlaidCloud が行います。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-managed-bucket-account.md
---

**PlaidCloudマネージドバケット**は、ドキュメントにファイルストレージを追加する最も手軽な方法です。ストレージの作成と運用は PlaidCloud が行うため、事前の設定や認証情報の管理は不要です。名前を付けるだけです。

ドキュメントのファイルを保管する、新しい自己完結型の場所が必要なときは、PlaidCloudマネージドバケットを使用してください。すでに所有し自分で管理しているストレージに接続する場合は、代わりに[新しいドキュメントアカウントの追加](/ja/guides/documents/adding-accounts/)ページにある他のプロバイダーのいずれかを選択してください。

## セットアップ

1. PlaidCloud にサインインします
2. 新しいドキュメントアカウントを置くワークスペースを選択します
3. `Document > Manage Accounts` に移動します
4. `+ New Account` ボタンを選択します
5. **サービスタイプ**として `PlaidCloud Managed Bucket` を選択します
6. 名前と、任意で説明を入力します
7. **バケット名**を入力します。名前は3～63文字で、小文字、数字、ドット、ハイフンのみを使用でき、先頭と末尾は文字または数字にする必要があります。名前は**グローバルに一意**である必要があります。すでに使用されている場合は、別の名前を選ぶよう求められます
8. ユースケースに適した**セキュリティモデル**を選択します。不明な場合は `Private` のままにします
9. 保存ボタンを選択します

PlaidCloud がストレージをセットアップし、あなたを所有者にします。アカウントはすぐに参照とアップロードに使用できます。ほかに構成するものはありません。

:::note
PlaidCloudマネージドバケットは、**Business** プランと **Enterprise** プランで利用できます。お使いのプランに含まれていない場合や、プランの上限に達している場合は、作成しようとしたときにフォームでお知らせします。
:::

## 作成後

- バケット名は作成後に固定され、既存のアカウントでは変更できません。
- アカウントを削除しても、**保存されているファイルはそのまま残る**ため、削除によってデータが破棄されることはありません。ストレージ自体の削除が必要な場合は、サポートにお問い合わせください。
- PlaidCloudマネージドバケットは、[アクセス制御](/ja/guides/documents/account-management/control-document-account-access/)、[所有権](/ja/guides/documents/account-management/managing-document-account-owners/)、参照について、他のドキュメントアカウントと同じように動作します。
