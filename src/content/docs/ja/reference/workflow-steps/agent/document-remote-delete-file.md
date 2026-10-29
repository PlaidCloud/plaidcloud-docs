---
title: Document - Remote Delete File
description: PlaidCloudのワークフローで、PlaidLinkエージェントを通じてリモートシステム上のファイルを削除し、ファイアウォールの内側のファイルを安全に管理します。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-delete-file.md
---

## 説明



PlaidLinkエージェント経由で到達する、ファイアウォールの内側にあるファイルシステム上のファイルを削除します。エージェントがオンプレミスのファイルシステム上で、削除をローカルで実行します。

オンプレミスでのエクスポート処理後のクリーンアップや、処理済みのソースファイルを削除する必要があるファイルベースの連携の一部として使用します。


## 例


まず、“Agent to Use”ドロップダウンから選択します。次に、“File or Folder Path for Delete”にファイルまたはフォルダーのパスを入力します。最後に、“Save and Run Step”を選択します。

## パスが存在しない場合

更新済みのPlaidLinkエージェントでは、リモートシステムに存在しないパスを指定すると、エラーにならず、警告`Nothing to delete at <path>`とともにステップが終了し、ワークフローは続行されます。更新されていないエージェントでは、これまでどおりステップが失敗します。

パスが空の場合は、警告`No path to delete; nothing deleted.`とともにステップが終了し、何も削除されません。これには、`{folder}/archive`のように、フォルダー部分が変数で、今回の実行で何にも解決されなかったパスも含まれます。

ファイルシステムのルート、またはPlaidLinkエージェントの作業ディレクトリの親フォルダーであるパス（`/`、`C:\`、`\\server\share`のような共有のルート、または`..`）は、何かを削除する前にステップが失敗し、`Refusing to delete the filesystem root <path>.`または`Refusing to delete <path>, which contains the agent's working directory.`が出力されます。ルートと`..`は、すでにデプロイ済みのPlaidLinkエージェントでも拒否されます。更新済みのエージェントは、作業ディレクトリを含むその他のフォルダーも、自身のファイルシステムに照らして判断して拒否します。
