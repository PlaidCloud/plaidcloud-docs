---
title: Crop Image to Headshot
description: ディレクトリやバッジ用に標準化されたポートレートを作成するため、PlaidCloudワークフローステップで画像を正方形のヘッドショットに切り抜きます。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/crop-image-to-headshot.md
---

画像を中央の正方形に切り抜き、500 × 500ピクセルのJPEGにスケーリングします。ソース写真の縦横比がまちまちな、従業員やメンバーのディレクトリを正規化するのに便利です。

## 入力

- **入力ファイルまたはディレクトリ** — ドキュメントアカウント内の画像、または画像のフォルダーです。
- **出力ファイルまたはディレクトリ** — ヘッドショットの書き込み先です。

## 出力

ソースの中央から切り抜かれた、500 × 500のJPEGです。フォルダーの場合、各ファイルのヘッドショットは、出力パスから拡張子を除いた名前のフォルダーの中に書き込まれます。

## 注記

- 切り抜きは画像の中央から行われます。顔を検出することはないため、被写体が中央に来るようにソース写真を構図してください。
- 画像として読み取れないファイルは、ステップを失敗させずに、そのまま出力にコピーされます。
- 入力パスが存在しない場合、またはファイルがない場合、ステップはそのパスを示す警告を出して何も処理せずに終了し、ワークフローは続行されます。
- 出力パスを入力パスと同じにすることはできません。

## 主な用途

- 従業員ディレクトリの写真を標準化する
- 社内ポータル向けに、統一されたアバター画像を生成する
- IDバッジや資格情報用に写真をトリミングする

## 関連項目

- [Convert PDF or Image to JPEG](/ja/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)ステップ
- [Fix File Extension](/ja/reference/workflow-steps/document/fix-file-extension/)ステップ
