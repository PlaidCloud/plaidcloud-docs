---
title: PlaidCloud Gitコネクター
description: Panelアプリ、Dashアプリ、またはワークフローを、マネージドの組み込みGitサービスであるPlaidCloud Git上のリポジトリに接続します。サーバーURLや資格情報の設定は不要です。
sidebar:
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/git/plaidcloud-git.md
---

**PlaidCloud Git**は、ワークスペースに組み込まれたマネージドGitサービスです。PlaidCloud Git接続は、PanelデプロイメントやDashデプロイメント、またはワークフローを、いずれかのリポジトリに向けます。サービスがマネージドであるため、**サーバーURL、ユーザー名、トークンは不要**です。PlaidCloudがホストを提供し、ユーザーに代わって認証します。

これらの接続からアプリを提供する手順全体については、[PlaidCloud GitからPanelアプリをデプロイする](/ja/guides/panel-apps/deploy-from-git/)または[PlaidCloud GitからDashアプリをデプロイする](/ja/guides/dash-apps/deploy-from-git/)を参照してください。リポジトリの作成とコードのプッシュについては、[PlaidCloud Gitガイド](/ja/guides/git/)を参照してください。

## 設定

**Tools > Connections**で**新規接続**をクリックし、**PlaidCloud Git**を選択します。フォームでは、外部Gitプロバイダーで表示される認証、SSL、SSHの各セクションは表示されません（資格情報はプラットフォームから取得されるためです）。接続の識別情報、使用方法、対象リポジトリのみが表示されます。

### 識別情報

| フィールド | タイプ | 説明 |
|---|---|---|
| アカウント名 | テキスト | この接続の表示名。 |
| メモ | テキスト | 接続の用途に関する任意のメモ。 |

### リポジトリ

| フィールド | タイプ | 説明 |
|---|---|---|
| リポジトリ | ピッカー | 使用するリポジトリ。**更新**をクリックしてワークスペースのリポジトリ（たとえば`apps`や`udfs`）を一覧表示し、1つ選択します。 |
| デフォルトブランチ | ピッカー | 読み取り元のブランチ。選択したリポジトリのブランチから選びます。 |
| 開始パス | ピッカー | 任意。選択したリポジトリを参照してフォルダーを選択すると、すべてのファイル検索がそのサブディレクトリに限定されます。 |

**使用方法**（`Active` / `Read Only`）と**セキュリティモデル**（ワークスペース内で接続を使用できるユーザー）は標準の接続設定です。[接続ガイド](/ja/guides/connections/plaidcloud-git/)と[接続の作成と管理](/ja/guides/connections/create-connection/)を参照してください。

## 主な用途

- ワークスペースの`apps`リポジトリから[HoloViz Panelアプリ](/ja/guides/panel-apps/deploy-from-git/)または[Plotly Dashアプリ](/ja/guides/dash-apps/deploy-from-git/)を提供する。
- PlaidCloud Gitにあるユーザー定義関数、設定、テンプレートファイルを取得する。

## 関連項目

- [PlaidCloud Git接続](/ja/guides/connections/plaidcloud-git/) — 使用方法とセキュリティモデルを含む、接続を作成するためのタスクガイド
- [PlaidCloud GitからPanelアプリをデプロイする](/ja/guides/panel-apps/deploy-from-git/) — リポジトリから提供されるアプリまでの全手順
- [PlaidCloud GitからDashアプリをデプロイする](/ja/guides/dash-apps/deploy-from-git/) — Plotly Dashアプリ向けの同じ手順
- [PlaidCloud Gitガイド](/ja/guides/git/) — リポジトリ、イシュー、プルリクエストなど
- [Gitリポジトリ接続](/ja/reference/connectors/git/) — 外部Gitプロバイダー（GitHub、GitLabなど）
