---
title: Cursor
description: Cursor IDEを設定して、組み込みのMCPサポートを通じてPlaidCloudのMCPツールを呼び出します。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/cursor.md
---

[Cursor](https://cursor.com)は、`mcp.json`設定ファイルを通じてMCPサーバーをサポートしています。形式はClaude Codeの`.mcp.json`と同じなので、同じベアラートークンのスニペットがどちらでも機能します。

PlaidCloudのヘッダーツールバーにある**AIを接続**ウィンドウには、OAuthサインインを通じてサーバーを追加するワンクリックのリンク**Cursorにインストール**があり、設定ファイルは不要です。まずはこちらを試してください。以下のベアラートークンの設定は、このページで詳しく説明するセットアップであり、ワンクリックのリンクでサーバーが追加されない場合やCursorがインストールされていない場合のフォールバックです。

## セットアップ

1. PlaidCloudにサインインしているブラウザーで`https://<your-workspace>.plaid.cloud/mcp/setup/token`にアクセスして、ベアラートークンを取得します。

2. CursorのMCP設定を開きます。
   - **プロジェクト単位**：プロジェクトのルートに`.cursor/mcp.json`を作成します。
   - **ユーザー単位（すべてのプロジェクト）**：ホームディレクトリに`~/.cursor/mcp.json`を作成します。

3. PlaidCloudサーバーを追加します。

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

4. Cursorの**Settings → MCP**を開いて、サーバーが接続されていることを確認します。エラーが表示された場合は、[トラブルシューティング](../troubleshooting/)を参照してください。

## ツールの使用

CursorのComposerまたはチャットパネルで、エージェントに普通の言葉で依頼できます（「プロジェクト`Q4 Forecast`の構造を説明してください」など）。適切な`plaidcloud_*`ツールが選択されます。ツールの呼び出しと応答はインラインで表示されます。変更を伴う操作は、承認する前に確認してください。

## トークンの更新

トークンの有効期限が切れたら、`https://<your-workspace>.plaid.cloud/mcp/setup/token`を再読み込みして、新しい値を`mcp.json`に貼り付けます。Cursorは完全に再起動しなくても変更を取り込みます。必要に応じて、**Settings → MCP**でサーバーのオンとオフを切り替えてください。

## 複数のテナント

別の名前で同じエントリを繰り返します。

```json
{
  "mcpServers": {
    "plaidcloud-prod": { "url": "https://prod.plaid.cloud/mcp", "headers": { "Authorization": "Bearer …" } },
    "plaidcloud-dev":  { "url": "https://dev.plaid.cloud/mcp",  "headers": { "Authorization": "Bearer …" } }
  }
}
```
