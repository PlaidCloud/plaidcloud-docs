---
title: Merge Multiple PDFsステップ
description: PlaidCloudのワークフローステップで複数のPDFファイルを1つの結合ドキュメントにまとめ、レポートの組み立てや統合に使用します。
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/merge-multiple-pdfs.md
---

フォルダー内のPDFを1つのPDFに結合します。[Concatenate Filesステップ](/ja/reference/workflow-steps/document/concatenate-files/)とは異なり、このステップはPDF形式を理解しており、有効な結合済みドキュメントを生成します。

## 入力

- **入力ディレクトリ** — 結合するPDFが入った、ドキュメントアカウント内のフォルダーです。PDFをまとめたZIPなど、単一のアーカイブを指定することもでき、その場合はアーカイブ内のPDFが結合されます。
- **結合後の出力ファイル** — 結合したPDFの書き込み先です。

## 動作

- PDFはパスの順に結合され、数字は値として扱われます。そのため `page2.pdf` は `page10.pdf` より前に来ます。順序を制御するには、番号を付けてください。各PDFのページは、元の順序のまま保持されます。
- 名前が `.pdf` のファイルのみが結合されます。フォルダー内のそれ以外のファイルは対象外で、フォルダー内のアーカイブは開かれません。
- サブフォルダー内のファイルは、ドキュメントアカウントが一覧に含める場合に対象となります。S3、Wasabi、Google Cloud Storageのアカウントはフォルダーツリー全体を一覧にしますが、OneDrive、SFTP、Azureのアカウントは最上位のみを一覧にします。
- 結合できるPDFは最大100個です。それを超えるとステップは失敗します。

## 出力

出力パスに、結合したすべてのPDFの全ページを含む単一のPDFが作成されます。

## 注記

- PDFが1つもないフォルダー、または存在しないフォルダーを指定した場合、ステップはそのフォルダーを示す警告とともに終了して何も結合せず、ワークフローは続行されます。
- 出力パスを入力パスと同じにすることはできません。

## 主な用途

- 個別のレポートPDFから月次レポートを組み立てる
- 表紙、本文、付録を1つの成果物にまとめる
- 生成した請求書を、顧客ごと、または期間ごとのアーカイブにまとめる

## 関連項目

- [Compress PDFステップ](/ja/reference/workflow-steps/document/compress-pdf/) — 結合結果を圧縮します
- [Convert Image to PDFステップ](/ja/reference/workflow-steps/document/convert-image-to-pdf/) — 結合前に画像をPDFに変換します
