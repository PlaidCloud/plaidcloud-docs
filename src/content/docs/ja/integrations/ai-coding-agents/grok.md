---
title: Grok
description: xAI の Grok を、カスタムコネクター経由で PlaidCloud のMCPサーバーに接続します。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/grok.md
---

[Grok](https://grok.com) は、grok.com で設定するカスタムコネクターを通じてMCPサーバーに対応しています。

## セットアップ

1. [grok.com/connectors](https://grok.com/connectors) にアクセスし、**New Connector → Custom** をクリックします。
2. MCPサーバーのURLを貼り付けます: `https://<your-workspace>.plaid.cloud/mcp`。
3. Grok から PlaidCloud にリダイレクトされたら、サインインを完了します。リクエスト元のアプリケーションと、認証情報の送信先となるリダイレクトURIを示す **アプリケーションアクセスのリクエスト** ページが表示されます。承認する前に、どちらも Grok と一致していることを確認してください。

## 会社向けプラン

BusinessプランとEnterpriseプランのワークスペースでは、コネクターの設定はチーム管理者を通じて行います。ワークスペース管理者が grok.com/connectors でコネクターをプロビジョニングすると、メンバーは自分のアカウントをそのコネクターに接続できます。

## アクセスを更新する

Grok から接続の再認可が必要と表示された場合は、サインインの手順をもう一度行ってください。コネクターはURLを保持しているため、最初から追加し直す必要はありません。
