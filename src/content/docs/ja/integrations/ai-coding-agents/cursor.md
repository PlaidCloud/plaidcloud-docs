---
title: Cursor
description: Cursor IDE を、組み込みの MCP サポートを通じて PlaidCloud の MCP ツールを呼び出すように構成します。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/cursor.md
---

[Cursor](https://cursor.com) は、`mcp.json` 構成ファイルを通じて MCP サーバーをサポートしています。形式は Claude Code の `.mcp.json` と同じなので、同じベアラートークンのスニペットがどちらでも動作します。

PlaidCloud のアバター（ユーザー）メニューから開く **AIを接続**ウィンドウには、OAuth サインインでサーバーを追加するワンクリックリンク **Cursorにインストール**があり、構成ファイルは必要ありません。まずこちらをお試しください。以下のベアラートークンによる構成は、このページで詳しく説明しているセットアップ方法であり、ワンクリックリンクでサーバーが追加されない場合や、Cursor がインストールされていない場合の代替手段です。

## セットアップ

1. PlaidCloud にサインインしているブラウザーで `https://<your-workspace>.plaid.cloud/mcp/setup/token` にアクセスし、ベアラートークンを取得します。

2. Cursor の MCP 構成を開きます。
   - **プロジェクトスコープ**: プロジェクトのルートに `.cursor/mcp.json` を作成します。
   - **ユーザースコープ（すべてのプロジェクト）**: ホームディレクトリに `~/.cursor/mcp.json` を作成します。

3. PlaidCloud サーバーを追加します。

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "url": "https://<your-workspace>.plaid.cloud/mcp",
          "headers": {
            "Authorization": "Bearer eyJhbGc…"
          }
        }
      }
    }
    ```

4. Cursor の **設定 → MCP** を開き、サーバーが接続されていることを確認します。エラーが表示された場合は、[トラブルシューティング](../troubleshooting/)を参照してください。

## ツールの使用

Cursor の Composer またはチャットパネルでは、エージェントに平易な日本語で指示できます（「プロジェクト `Q4 Forecast` の構造を説明して」など）。エージェントは適切な `plaidcloud_*` ツールを選びます。ツールの呼び出しと応答はインラインで表示されます。変更を伴う操作は、承認する前に確認してください。

## トークンの更新

トークンの有効期限が切れたら、`https://<your-workspace>.plaid.cloud/mcp/setup/token` を再読み込みして、新しい値を `mcp.json` に貼り付けます。Cursor は、完全に再起動しなくても変更を反映します。必要に応じて、**設定 → MCP** でサーバーをオフ、オンに切り替えてください。

## 複数のテナント

別の名前でエントリを繰り返します。

```json
{
  "mcpServers": {
    "plaidcloud-prod": { "url": "https://prod.plaid.cloud/mcp", "headers": { "Authorization": "Bearer …" } },
    "plaidcloud-dev":  { "url": "https://dev.plaid.cloud/mcp",  "headers": { "Authorization": "Bearer …" } }
  }
}
```
