---
title: Document - Remote Import File
description: PlaidCloudのワークフローで、PlaidLinkエージェントを通じてリモートシステムからファイルをインポートし、ファイアウォールの内側のファイルを安全に取得します。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-import-file.md
---

## 説明



PlaidLinkエージェントを通じてリモートのファイルシステムからファイルを取得し、PlaidCloudのドキュメントアカウントに保存します。ソースファイルが社内のファイル共有、オンプレミスのサーバー、またはファイアウォールの内側にある場合に使用します。

エージェントがファイルをローカルで読み取ってPlaidCloudにストリーミングし、後続のワークフローステップで処理できるようにします。


## 例


まず、“Agent to Use”ドロップダウンから選択します。次に、“File or Folder Path for Import”にファイルまたはフォルダーのパスを入力します。続いて、“Folder Destination”にフォルダーの出力先を入力します。必要に応じて、ファイルの到着時に圧縮するための**圧縮**として、Zip、GZip、BZip2、Zstandard、LZ4、Snappy、LZO、Deflate（zlib）のいずれかを選択します。最後に、“Save and Run Step”を選択します。

## ソースのファイルまたはフォルダーが存在しない場合

リモート共有のパスに何も存在しない場合、ステップはエラーにならず、警告`No file or folder found at <path>; nothing imported.`とともに終了します。ワークフローは次のステップに進み、存在しないソースに対しては、ステップの再試行設定とエラー時の設定（ステップへ移動、または続行）は実行されません。これは、すでにデプロイ済みのPlaidLinkエージェントでも動作します。

パスが空の場合も同様に、警告`No path to import from; nothing imported.`とともに終了します。これには、`{folder}/archive`のように、フォルダー部分が変数で、今回の実行で何にも解決されなかったパスも含まれます。

ファイルシステムのルート、またはPlaidLinkエージェントの作業ディレクトリの親フォルダーであるパス（`/`、`C:\`、`\\server\share`のような共有のルート、または`..`）は、何かがアップロードされる前にステップが失敗し、`Refusing to import from the filesystem root <path>.`または`Refusing to import from <path>, which contains the agent's working directory.`が出力されます。ルートと`..`は、すでにデプロイ済みのPlaidLinkエージェントでも拒否されます。更新済みのエージェントは、作業ディレクトリを含むその他のフォルダーも、自身のファイルシステムに照らして判断して拒否します。

その他の失敗は、引き続きステップを失敗させます。アクセス拒否、PlaidCloudへのアップロードの失敗、または更新済みのPlaidLinkエージェントでは、到達できないサーバーや共有などです。

何もインポートされないため、前回の実行のドキュメントはそのまま残ります。今回の期間のファイルが到着した場合にのみ後続のステップを実行するには、次のいずれかを行います。

- 後続のステップに、**ドキュメント内にファイルが存在する**[ステップ条件](/ja/guides/workflows/step-conditions/#ドキュメントパスの条件)を追加し、ドキュメントパスを、ファイル名に期間を含めるなど、期間ごとのパスに設定します。
- ワークフローでの使用後にインポートしたドキュメントを削除し、ソースが存在しない場合に古いファイルが残らないようにします。
