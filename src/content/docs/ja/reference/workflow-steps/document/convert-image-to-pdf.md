---
title: Convert Image to PDF
description: PlaidCloudワークフローステップで画像ファイルをPDFドキュメントに変換し、標準化されたドキュメント出力とアーカイブに適した形式を実現します。
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-image-to-pdf.md
---

画像（PNG、GIF、TIFF、JPEG、HEIC）を1ページのPDFにするか、既存のPDFを標準のページサイズに合わせ直します。

## 入力

- **入力ファイルまたはディレクトリ** — ドキュメントアカウント内の画像またはPDF、またはそれらのフォルダーです。
- **宛先** — PDFの書き込み先です。
- **ページサイズ** — US レター、US リーガル、A3、A4、A5から選択します。
- **圧縮** — **Lossy**は画像を画面解像度に縮小し、ファイルを大幅に小さくできます。デフォルトの**Lossless**は、画像データをそのまま保持します。

## 仕組み

- 画像は、選択したサイズのページに、縦横比を変えずに収まるように拡大縮小して配置されます。スキャンしたTIFFなど、複数のページやフレームを持つ画像は、最初のものから変換されます。
- **Lossy**の場合は、その後に結果が圧縮され、PDFが入力のときは、圧縮の際に選択したページサイズに合わせられます。
- **Lossless**の場合は、PDFが入力のときは変更されずにそのまま渡され、元のページサイズが保たれます。

## 出力

入力ファイルごとに1つのPDFが作成されます。フォルダーの場合、各ファイルのPDFは、宛先から拡張子を除いた名前のフォルダーの中に、ソースファイル自身の名前で書き込まれます。複数のPDFを1つのドキュメントにまとめるには、このステップの後に[Merge Multiple PDFs](/ja/reference/workflow-steps/document/merge-multiple-pdfs/)ステップを続けてください。

## 注記

- 入力パスが存在しない場合、またはファイルがない場合、ステップはそのパスを示す警告を出して何も処理せずに終了し、ワークフローは続行されます。
- 宛先を入力パスと同じにすることはできません。

## 主な用途

- 領収書や請求書の画像を、アーカイブ用の形式に標準化する
- PDFの入力のみを受け付けるシステム向けに、証跡となる画像を準備する

## 関連項目

- [Convert PDF or Image to JPEG](/ja/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)ステップ
- [Compress PDF](/ja/reference/workflow-steps/document/compress-pdf/)ステップ
- [Merge Multiple PDFs](/ja/reference/workflow-steps/document/merge-multiple-pdfs/)ステップ
