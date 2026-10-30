---
title: Compress PDF
description: PlaidCloudワークフローステップでPDFファイルを圧縮し、ドキュメントの品質を保ちながらファイルサイズを小さくして、ストレージを効率化します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/compress-pdf.md
---

ドキュメントアカウントに保存されているPDFのファイルサイズを小さくします。大きなスキャン文書をアーカイブする前、通知に添付する前、またはドキュメントアカウント間で移動する前に容量を減らすのに便利です。

## 入力

- **入力ファイルまたはディレクトリ** — ドキュメントアカウント内のPDF、またはPDFのフォルダーです。
- **出力ファイルまたはディレクトリ** — 圧縮されたPDFの書き込み先です。

## 仕組み

PDFは、画像が画面解像度（72 dpi）に縮小され、フォントがサブセットとして埋め込まれた状態で書き直されます。これによりスキャン文書を大幅に小さくでき、テキストは鮮明なままです。ページはUS レターサイズに合わせられます。

## 出力

出力パスに圧縮されたPDFが作成されます。フォルダーの場合、各PDFは、入力フォルダーからの相対的な位置を保ったまま、出力パスの下に書き込まれます。

## 注記

- 出力パスを入力パスと同じにすることはできないため、ソースが上書きされることはありません。
- 入力パスが存在しない場合、またはファイルがない場合、ステップはそのパスを示す警告を出して何も処理せずに終了し、ワークフローは続行されます。
- 圧縮できないPDFがあると、ステップはそのファイルと理由を示して失敗します。

## 主な用途

- 長期保管の前に、スキャンした請求書、領収書、契約書を小さくする
- メール送信や通知への添付の前にPDFのサイズを減らす
- サイズ制限のある下流システムへのアップロードに向けてドキュメントを準備する

## 関連項目

- [Convert PDF or Image to JPEG](/ja/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)ステップ
- [Merge Multiple PDFs](/ja/reference/workflow-steps/document/merge-multiple-pdfs/)ステップ
- [ドキュメントガイド](/ja/guides/documents/)
