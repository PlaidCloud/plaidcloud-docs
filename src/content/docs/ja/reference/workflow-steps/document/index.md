---
title: ドキュメントステップ
description: ファイルの変換、コピー、名前の変更、削除、PDF操作のステップで、PlaidCloudのワークフロー内のドキュメントを管理します。
sidebar:
  label: ドキュメントステップ
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/index.md
---

ドキュメントアカウントに保存されたファイルを操作するワークフローステップです。データのワークフローと合わせて、ドキュメントの移動、変換、形式変換に使用します。

## ファイル操作

- [Copy Document Fileステップ](/ja/reference/workflow-steps/document/copy-document-file/) · [Copy Document Directoryステップ](/ja/reference/workflow-steps/document/copy-document-directory/)
- [Create Document Directoryステップ](/ja/reference/workflow-steps/document/create-document-directory/)
- [Delete Document Fileステップ](/ja/reference/workflow-steps/document/delete-document-file/) · [Delete Document Directoryステップ](/ja/reference/workflow-steps/document/delete-document-directory/)
- [ディレクトリ一覧](/ja/reference/workflow-steps/document/directory-listing/) — フォルダー内のファイルのテーブルを書き込みます
- [Update Excel Cellsステップ](/ja/reference/workflow-steps/document/document-excel-update/) — ブックの指定したセルに値を書き込む、またはセルの書式を設定します
- [Fix File Extensionステップ](/ja/reference/workflow-steps/document/fix-file-extension/)
- [Rename Document Fileステップ](/ja/reference/workflow-steps/document/rename-document-file/) · [Rename Document Directoryステップ](/ja/reference/workflow-steps/document/rename-document-directory/)

コピーと名前の変更のステップでは、ソースが存在しないことは通常の状態として扱われます。ファイル、またはコピーや名前の変更の対象となるフォルダーが存在しない場合、またはフォルダーが空の場合、ステップは何もせず、そのパスを示す警告とともに終了し、ワークフローは続行されます。その日はファイルがないフォルダーに対するスケジュール実行も、失敗しなくなりました。

## 暗号化

- [ファイルの暗号化と復号](/ja/reference/workflow-steps/document/encrypt-decrypt-file/) — AES、Blowfish、またはExcelブックのパスワード

## PDF操作

- [Compress PDFステップ](/ja/reference/workflow-steps/document/compress-pdf/)
- [Convert Image to PDFステップ](/ja/reference/workflow-steps/document/convert-image-to-pdf/)
- [Convert PDF or Image to JPEGステップ](/ja/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge Multiple PDFsステップ](/ja/reference/workflow-steps/document/merge-multiple-pdfs/)

## 画像操作

- [Crop Image to Headshotステップ](/ja/reference/workflow-steps/document/crop-image-to-headshot/)

## テキスト操作

- [Concatenate Filesステップ](/ja/reference/workflow-steps/document/concatenate-files/) — 複数のファイルを1つに結合します
- [Document Text Substitutionステップ](/ja/reference/workflow-steps/document/document-text-substitution/) — ドキュメント内を検索して置換します

## エンコード変換

- [Convert Document Encodingステップ](/ja/reference/workflow-steps/document/convert-document-encoding/) — 変換先のエンコードを選択します
- [Convert Document Encoding to ASCIIステップ](/ja/reference/workflow-steps/document/convert-document-encoding-to-ascii/)
- [Convert Document Encoding to UTF-16ステップ](/ja/reference/workflow-steps/document/convert-document-encoding-to-utf-16/)
- [Convert Document Encoding to UTF-8ステップ](/ja/reference/workflow-steps/document/convert-document-encoding-to-utf-8/)

## 関連項目

- [Convert Dashboard to PDFステップ](/ja/reference/workflow-steps/document/dashboard-to-pdf/)
- [Delete Old Filesステップ](/ja/reference/workflow-steps/document/document-delete-old-files/)
- [ドキュメントアカウント](/ja/guides/documents/adding-accounts/) — これらのステップを使用する前に、ドキュメントアカウントを接続します
- [ドキュメントガイド](/ja/guides/documents/) — 同じ操作をタスクごとに説明するチュートリアルです
