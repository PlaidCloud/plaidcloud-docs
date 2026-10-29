---
title: Concatenate Files
description: PlaidCloudワークフローステップで複数のファイルを1つのファイルに連結し、テキスト、CSV、その他のドキュメント出力をまとめます。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/concatenate-files.md
---

ドキュメントアカウント内の2つ以上のファイルを、1つの出力ファイルにまとめます。バイト単位で処理するため、単純な連結で有効な出力になるプレーンテキスト形式（CSV、ログファイル、JSON Lines）に便利です。

## 入力

- **ソースファイル** — 連結するファイルのリスト（順序どおり）
- **出力パス** — 連結したファイルの保存先
- **区切り文字** — ソースファイルの間に挿入するオプションのバイト列（一般的には改行）

## 出力

すべてのソースファイルの内容を、指定された順序で、設定した区切り文字でつなげた1つのファイルです。

存在しないソースファイルは連結後のファイルから除外され、ステップはそのファイルを示す警告を出して終了するため、ワークフローは続行されます。

## 主な用途

- 日次のログファイルを月次のアーカイブにまとめる
- 同じスキーマを共有するCSVファイルを結合する（最初のファイル以外はヘッダーを除く）
- 処理の前に、複数のソースからのJSON Lines形式のエクスポートを結合する

## 対象外

- PDF — 代わりに[Merge Multiple PDFs](/ja/reference/workflow-steps/document/merge-multiple-pdfs/)ステップを使用してください
- ヘッダーを持つバイナリ形式（XLSX、ZIP、画像ファイル）— バイトを連結しても有効なファイルにはなりません

## 関連項目

- [Merge Multiple PDFs](/ja/reference/workflow-steps/document/merge-multiple-pdfs/)ステップ
- [ドキュメントガイド](/ja/guides/documents/)
