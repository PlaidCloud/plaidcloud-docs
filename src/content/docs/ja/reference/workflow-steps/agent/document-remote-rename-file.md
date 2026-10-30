---
title: Document - Remote Rename File
description: PlaidCloudのワークフローで、PlaidLinkエージェントを通じてリモートシステム上のファイルの名前を変更し、ファイアウォールの内側のファイルを安全に管理します。
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-rename-file.md
---

## 説明



PlaidLinkエージェントを通じて、リモートのファイルシステム上のファイルの名前を変更または移動します。処理は完全にオンプレミス側で行われ、PlaidCloudとの間でデータは転送されません。

よくあるパターン: リモートインポートのステップが成功した後で、ソースファイルの名前を変更して「処理済み」の印を付け、同じワークフローが次の実行で再びインポートしないようにします。


## 例


まず、“Agent to Use”ドロップダウンから選択します。



次に、“Source Path”と“Destination Path”を入力します。



最後に、“Save and Run Step”を選択します。

## ソースが存在しない場合

更新済みのPlaidLinkエージェントでは、リモートシステムに存在しないソースを指定すると、エラーにならず、警告`No file or folder found at <path>; nothing renamed`とともにステップが終了し、ワークフローは続行されます。更新されていないエージェントでは、これまでどおりステップが失敗します。

ソースパスが空の場合は、警告`No path to rename from; nothing renamed.`とともにステップが終了します。これは、パス内のフォルダーが変数で、今回の実行で何にも解決されなかった場合も同様です。

ファイルシステムのルート、またはPlaidLinkエージェントの作業ディレクトリの親フォルダーであるソース（`/`、`C:\`、`\\server\share`のような共有のルート、または`..`）は、`Refusing to rename from the filesystem root <path>.`または`Refusing to rename from <path>, which contains the agent's working directory.`でステップが失敗します。出力先パスが空の場合は、`No destination path for the rename; it would write into the agent's working directory.`でステップが失敗します。`E:\`や`\\nas\drop`のように、ドライブや共有のルートへの名前の変更は動作します。ルートと`..`は、すでにデプロイ済みのPlaidLinkエージェントでも拒否されます。更新済みのエージェントは、作業ディレクトリを含むその他のフォルダーも、自身のファイルシステムに照らして判断して拒否します。
