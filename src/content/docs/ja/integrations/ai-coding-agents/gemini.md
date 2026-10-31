---
title: Google Gemini CLI
description: Googleのgemini-cliを設定して、PlaidCloudのMCPツールを呼び出します。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/gemini.md
---

Googleの[`gemini-cli`](https://github.com/google-gemini/gemini-cli)は、`~/.gemini/settings.json`（ユーザー単位）またはプロジェクトのルートにある`.gemini/settings.json`（プロジェクト単位）を通じて、MCPサーバーをサポートしています。

## セットアップ

1. PlaidCloudにサインインしているブラウザーで`https://<your-workspace>.plaid.cloud/mcp/setup/token`にアクセスして、ベアラートークンを取得します。

2. `~/.gemini/settings.json`を編集します（存在しない場合は作成します）。

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "httpUrl": "https://<your-workspace>.plaid.cloud/mcp",
          "headers": {
            "Authorization": "Bearer eyJhbGc…"
          }
        }
      }
    }
    ```

3. `gemini`を再起動します。セッション内で`/mcp`を実行して、サーバーが接続されていることを確認し、そのツールを一覧表示します。

## 使用方法

GeminiにPlaidCloudのツールを直接使うよう依頼します。

- 「plaidcloudを使って、`Sales Forecasting`プロジェクトのワークフローを一覧表示してください。」
- 「`customers`テーブルの列と、直近のスナップショットを説明してください。」

特定のツールを呼び出す前に入力スキーマを確認したい場合は、`/tools`コマンドで明示的にツールを呼び出すこともできます。

## トークンの更新

トークンの有効期限が切れたら、`https://<your-workspace>.plaid.cloud/mcp/setup/token`を再読み込みして、`settings.json`の`Authorization`の値を更新します。変更を取り込むには、`gemini`を再起動してください。

## Gemini Code Assist（IDE）

VSCodeやJetBrainsのGemini Code Assistは、エージェント設定の下で同じ`mcpServers`設定を受け付けます。スキーマはCLIの形式と同じなので、IDEのMCPサーバー設定パネルに同じスニペットを貼り付けてください。
