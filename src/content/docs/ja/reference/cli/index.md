---
title: CLIツール
description: PlaidCloudのコマンドラインツールのリファレンス。PlaidLinkエージェント、PlaidXL Excelアドイン、ノートブック連携用のJupyter CLIを扱います。
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

PlaidCloudは、Web UIの外部でワークスペースを操作するための、コマンドラインおよびオンマシンのツールを3つ提供しています。

## PlaidLink

[PlaidLink](/ja/reference/cli/plaidlink/)は、ネットワーク内部で動作するエージェントです。PlaidCloudのワークフローを、データベースやファイル共有など、PlaidCloudから直接到達できないファイアウォール内のリソースに橋渡しします。Windowsサービス、Unix/Linux/Macデーモン、コンテナー、またはKubernetesポッドとしてインストールできます。

- [インストール](/ja/reference/cli/plaidlink/install/)
- [設定](/ja/reference/cli/plaidlink/configure/)
- [エージェント](/ja/reference/cli/plaidlink/agents/)
- [アップグレード](/ja/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/ja/reference/cli/plaidxl/)は、Microsoft Excel用のPlaidCloudアドインです。プロジェクトのテーブルとディメンションをワークシートに取得し、必要に応じて更新します。また、PlaidCloudのデータから集計済みの値や管理されたメトリックを計算する `PLAIDXL` 数式を追加し、計画した値を書き戻します。

- [インストール](/ja/reference/cli/plaidxl/install/)
- [サインイン](/ja/reference/cli/plaidxl/connect/)
- [テーブルとディメンションを操作する](/ja/reference/cli/plaidxl/retrieve/)
- [カスタム関数](/ja/reference/cli/plaidxl/functions/)
- [レポートを作成する](/ja/reference/cli/plaidxl/build-a-report/)
- [ドリル、メンバーの選択、数値の説明](/ja/reference/cli/plaidxl/drill/)
- [PlaidCloudに値を入力する](/ja/reference/cli/plaidxl/write-values/)
- [ExcelでWeaveに質問](/ja/reference/cli/plaidxl/weave/)
- [PlaidCloudリボン](/ja/reference/cli/plaidxl/ribbon/)
- [トラブルシューティング](/ja/reference/cli/plaidxl/troubleshooting/)

## Jupyter CLI

[Jupyter CLI](/ja/reference/cli/jupyter/)を使うと、データサイエンティストは、PlaidCloud対応のCLIとPythonヘルパーを使って、Jupyter ノートブックからPlaidCloudのプロジェクトデータを操作できます。

- [コマンドライン](/ja/reference/cli/jupyter/command-line/)
- [Jupyter ノートブック](/ja/reference/cli/jupyter/jupyter-notebook/)
- [OAuthの設定](/ja/reference/cli/jupyter/oauth-setup/)
