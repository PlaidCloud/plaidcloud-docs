---
title: AI エージェント（MCP）
description: Model Context Protocol（MCP）サーバーを通じて、Claude、Cursor、GitHub Copilot、Gemini などの AI エージェントを PlaidCloud テナントに接続します。
sidebar:
  label: AI エージェント（MCP）
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

PlaidCloud は、すべてのワークスペースの `/mcp` で、厳選された [Model Context Protocol](https://modelcontextprotocol.io)（MCP）サーバーを公開しています。AI エージェントは、他の MCP サーバーと同じ方法でこのサーバーに接続し、ツールを呼び出して、プロジェクトの読み取り、ワークフローの実行、テーブルのクエリ、ディメンションの管理などを行えます。

このセクションのページでは、サーバーが公開する内容、認証方法、最も一般的な AI クライアントの手順ごとのセットアップについて説明します。これらの背景にあるアーキテクチャ（すべての AI リクエストが通るガバナンスされた経路、検索のしくみ、独自のモデルの実行方法）については、[AI と LLM のアーキテクチャ](/ja/integrations/ai-architecture/)を参照してください。

## PlaidCloud の AI 分析が他と違う点

- **[信頼できる回答](./honest-answers/)** — すべての回答に信頼度のシグナルと平易な言葉の注意事項が付き、PlaidCloud が数値をでっち上げることはありません。この誠実さにより、AI の回答を手作業で再確認せずに、その回答に基づいて行動できます。
- **[配賦の追跡](./tracing-allocations/)** — 配賦された結果が*なぜ*変わったのか、何がそれに影響しているのか、仮に変更したらどうなるのかを、平易な言葉で質問できます。
- **[分析パス](./analysis-paths/)** — 主要なテーブルに分かりやすい名前とデフォルトを付けておくと、「先四半期になぜ増えたのか」とそのまま質問できます。
- **[ダッシュボードの作成](./build-dashboards/)** — 同じ PlaidCloud の接続を通じて、公開済みのテーブルとビューに対するチャートやダッシュボードを依頼できます。
- **[メトリック定義](./metric-definitions/)** — ビジネス上の数値の計算方法を一度合意しておけば、それを使うすべての回答が同じ方法で計算されます。

## アシスタントを接続する

最も手早い方法は、PlaidCloud 独自のアバター（ユーザー）メニューにある **AIを接続**を使うことです。クライアントを選び、表示される手順（MCP サーバーの URL を含む）に従ってください。

- [はじめに](./getting-started/) — MCP サーバーが公開する内容と、認証方法。
- [Microsoft 365 Copilot](/ja/integrations/microsoft-365-copilot/) — Teams と Outlook で、チーム全体に PlaidCloud を提供します。
- クライアント別のセットアップ: [Claude Code](./claude-code/)、[Claude Desktop](./claude-desktop/)、[Cursor](./cursor/)、[GitHub Copilot](./copilot/)、[Gemini](./gemini/)、[ChatGPT](./chatgpt/)、[Grok](./grok/)。
