---
title: PlaidLink
description: PlaidLinkエージェントをインストールして設定し、ファイアウォールの内側にあるシステムへ安全にアクセスして、リモートクエリやファイル転送を行えるようにします。
sidebar:
  label: PlaidLink
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/index.md
---

PlaidLinkは、ファイアウォールで保護されている、またはその他の制限によりPlaidCloudからの直接接続が難しいクライアントのシステムやプロセスに、間接的にアクセスするための仕組みです。隔離された領域内にインストールしたPlaidCloudエージェントを介して、PlaidCloudはエージェントにクエリの実行、ファイルのダウンロードやアップロード、センサー条件の確認、SAPとの連携など、さまざまな処理を依頼できます。

エージェントの側からPlaidCloudに接続し、標準のHTTPSネットワークプロトコルで通信するため、通常は最小限のセットアップで動作します。また、エージェントは権限のないユーザーとして実行できるため、制限された環境内でのアクセス権を管理できます。

## トピック

- [インストール](/ja/reference/cli/plaidlink/install/) — Windows、Linux、macOS、またはコンテナーでPlaidLinkを動作させる
- [設定](/ja/reference/cli/plaidlink/configure/) — 接続設定、認証情報、ランタイムオプション
- [エージェント](/ja/reference/cli/plaidlink/agents/) — 複数のエージェントとその機能の管理
- [アップグレード](/ja/reference/cli/plaidlink/upgrade/) — 新しいPlaidLinkビルドへの移行
