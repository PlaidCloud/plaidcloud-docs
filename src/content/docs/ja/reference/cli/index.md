---
title: CLIツール
description: PlaidCloudのコマンドラインツールのリファレンスです。PlaidLinkエージェント、PlaidXL Excelアドイン、ノートブック連携用のJupyter CLIを扱います。
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

PlaidCloudは、Web UIの外でワークスペースを操作するための、コマンドラインツールとマシン上で動作するツールを3つ提供しています。

## PlaidLink

[PlaidLink](/ja/reference/cli/plaidlink/)は、ネットワーク内で動作するエージェントです。PlaidCloudから直接アクセスできない、ファイアウォールで保護されたリソース（データベース、ファイル共有、その他のシステム）とPlaidCloudワークフローを橋渡しします。Windowsサービス、Unix/Linux/Macデーモン、コンテナー、またはKubernetesポッドとしてインストールできます。

- [インストール](/ja/reference/cli/plaidlink/install/)
- [設定](/ja/reference/cli/plaidlink/configure/)
- [エージェント](/ja/reference/cli/plaidlink/agents/)
- [アップグレード](/ja/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/ja/reference/cli/plaidxl/)は、Microsoft Excel用のPlaidCloudアドインです。プロジェクトテーブルとディメンションをワークシートに取得し、必要に応じて更新できます。また、PlaidCloudのデータから集計値を計算する `PLAIDXL` 数式を追加します。

- [インストール](/ja/reference/cli/plaidxl/install/)
- [サインイン](/ja/reference/cli/plaidxl/connect/)
- [テーブルとディメンションを扱う](/ja/reference/cli/plaidxl/retrieve/)
- [カスタム関数](/ja/reference/cli/plaidxl/functions/)
- [カスタム関数を使ってレポートを作成する](/ja/reference/cli/plaidxl/build-a-report/)
- [PlaidCloudリボン](/ja/reference/cli/plaidxl/ribbon/)
- [トラブルシューティング](/ja/reference/cli/plaidxl/troubleshooting/)

## Jupyter CLI

[Jupyter CLI](/ja/reference/cli/jupyter/)を使うと、データサイエンティストは、PlaidCloud対応のCLIとPythonヘルパーを使って、Jupyter ノートブックからPlaidCloudのプロジェクトデータを扱えます。

- [コマンドライン](/ja/reference/cli/jupyter/command-line/)
- [Jupyterノートブック](/ja/reference/cli/jupyter/jupyter-notebook/)
- [OAuthの設定](/ja/reference/cli/jupyter/oauth-setup/)
