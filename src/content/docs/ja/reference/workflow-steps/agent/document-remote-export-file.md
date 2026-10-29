---
title: Document - Remote Export File
description: PlaidCloudのワークフローで、PlaidLinkエージェントを通じてリモートシステムにファイルをエクスポートし、ファイアウォールの内側へファイルを安全に転送します。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-export-file.md
---

## 説明



PlaidLinkエージェントを通じて、PlaidCloudのドキュメントアカウントにあるファイルをリモートのファイルシステムに書き込みます。PlaidCloudから直接到達できないシステム（社内の共有ドライブ、オンプレミスのSFTPサーバー、専用のアプリケーションディレクトリなど）にレポート、抽出結果、処理済みファイルを届けるのに便利です。

エージェントがPlaidCloudからファイルを受け取り、構成されたローカルの出力先に書き込みます。


## 例


まず、“Agent to Use”ドロップダウンから選択します。次に、“File or Folder to Export”でファイルまたはフォルダーのパスを参照します。続いて、“Export Path Destination”に場所を入力します。最後に、“Save and Run Step”を選択します。

## パスの安全性

エクスポートパスが空の場合、ステップは`No destination path for the export; it would write into the agent's working directory.`で失敗します。これには、パス内の変数が空だったために何にも解決されなかったパスも含まれます。`E:\`や`\\nas\drop`のように、ドライブや共有のルートへのエクスポートは動作します。

**到着時にアーカイブを展開**を選択すると、ステップは出力先フォルダー内のすべてのアーカイブを展開して削除します。そのため、ファイルシステムのルートまたはその直下のファイルである出力先（`Refusing to unpack an export into the filesystem root <path>.`）や、PlaidLinkエージェント自身のフォルダー（`Refusing to unpack an export into <path>, which contains the agent's working directory.`）は拒否されます。代わりに、専用のサブフォルダーを選択してください。

空のパスとルートのチェックは、すでにデプロイ済みのPlaidLinkエージェントでも動作します。エージェント自身のフォルダーの拒否には、更新済みのPlaidLinkエージェントが必要です。
