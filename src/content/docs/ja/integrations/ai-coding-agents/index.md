---
title: AIエージェント（MCP）
description: Claude、Cursor、GitHub Copilot、Gemini などのAIエージェントを、Model Context Protocol（MCP）サーバー経由で PlaidCloud テナントに接続します。
sidebar:
  label: AIエージェント（MCP）
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

PlaidCloud は、すべてのワークスペースの `/mcp` で、厳選された [Model Context Protocol](https://modelcontextprotocol.io)（MCP）サーバーを公開しています。AIエージェントは、ほかのMCPサーバーと同じ方法でこのサーバーに接続し、ツールを呼び出してプロジェクトの読み取り、ワークフローの実行、テーブルのクエリ、ディメンションの管理などを行います。

このセクションのページでは、サーバーが公開する機能、認証方法、よく使われるAIクライアントの手順別セットアップを説明します。これらの背後にあるアーキテクチャ（すべてのAIリクエストが通るガバナンス経路、検索の仕組み、独自のモデルを実行する方法）については、[AIとLLMのアーキテクチャ](/ja/integrations/ai-architecture/)を参照してください。

## PlaidCloud のAI分析が優れている点

- **[信頼できる回答](./honest-answers/)** — すべての回答に信頼度のシグナルと平易な言葉での注意事項が付き、PlaidCloud が数値を捏造することはありません。この誠実さがあるからこそ、AIの回答を手作業で再確認せずに、そのまま判断に使えます。
- **[配賦のトレース](./tracing-allocations/)** — 配賦結果がなぜ変わったのか、何が影響しているのか、仮にこう変えたらどうなるのかを、平易な言葉で質問できます。
- **[分析パス](./analysis-paths/)** — 主要なテーブルにわかりやすい名前とデフォルトを付けておけば、「先四半期になぜ増えたのか」とそのまま質問できます。
- **[メトリック定義](./metric-definitions/)** — ビジネス上の数値の計算方法を一度合意しておけば、それを使うすべての回答が同じ方法で計算されます。

## アシスタントを接続する

最も簡単なのは、PlaidCloud 自体のヘッダーツールバーにある **AIを接続** ボタンを使う方法です。クライアントを選んで表示される手順に従うだけで、MCPサーバーのURLも含まれています。

- [はじめに](./getting-started/) — MCPサーバーが公開する機能と認証方法。
- [Microsoft 365 Copilot](/ja/integrations/microsoft-365-copilot/) — Teams と Outlook で、チーム全体に PlaidCloud を提供します。
- クライアント別のセットアップ: [Claude Code](./claude-code/)、[Claude Desktop](./claude-desktop/)、[Cursor](./cursor/)、[GitHub Copilot](./copilot/)、[Gemini](./gemini/)、[ChatGPT](./chatgpt/)、[Grok](./grok/)。
