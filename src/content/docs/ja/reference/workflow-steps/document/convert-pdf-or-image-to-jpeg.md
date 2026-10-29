---
title: Convert PDF or Image to JPEG
description: PlaidCloudワークフローステップでPDFのページや画像をJPEG形式に変換し、Web互換の出力や画像処理タスクに利用します。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg.md
---

PDFまたは画像をJPEGに変換します。PDFの場合は最初のページがJPEGになります。画像は再エンコードされ、スキャンしたTIFFなど、複数のページやフレームを持つ画像は、最初のものから変換されます。

## 入力

- **入力ファイルまたはディレクトリ** — ドキュメントアカウント内のPDFまたは画像（PNG、GIF、TIFF、JPEG、HEIC）、またはそれらのフォルダーです。
- **出力ファイルまたはディレクトリ** — JPEGの書き込み先です。

## 出力

入力ファイルごとに1つのJPEGが作成されます。フォルダーの場合、各ファイルのJPEGは、出力パスから拡張子を除いた名前のフォルダーの中に、ソースファイル自身の名前で書き込まれます。

## 注記

- その他の種類のファイルがあると、ステップは受け付けられる種類を示して失敗します。
- 入力パスが存在しない場合、またはファイルがない場合、ステップはそのパスを示す警告を出して何も処理せずに終了し、ワークフローは続行されます。
- 出力パスを入力パスと同じにすることはできません。

## 主な用途

- Web表示用のプレビュー画像を生成する
- PDFを扱えないシステム向けに、PDFの画像のみのバージョンを作成する

## 関連項目

- [Convert Image to PDF](/ja/reference/workflow-steps/document/convert-image-to-pdf/)ステップ
- [Compress PDF](/ja/reference/workflow-steps/document/compress-pdf/)ステップ
- [Crop Image to Headshot](/ja/reference/workflow-steps/document/crop-image-to-headshot/)ステップ
