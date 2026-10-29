---
title: Export to XML ステップ
description: PlaidCloud のワークフローステップから XML ファイルとしてデータをエクスポートし、構造化データの交換やシステム連携に利用します。
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-xml.md
---

## 説明

PlaidCloud のプロジェクトテーブルを、XML ファイルとしてドキュメントアカウントに書き込みます。下流のシステムが XML 入力を必要とする場合に使用します。従来型のエンタープライズ連携、政府への届出、特定の業界のデータ交換形式でよく使われます。

XML の構造はテーブルを反映します。行ごとに 1 つの要素があり、列ごとに子要素があります。構造をより細かく制御するには、テンプレートファイルに対して [Document Text Substitution](/ja/reference/workflow-steps/document/document-text-substitution/) ステップを使用するテンプレート方式を利用します。

## ファイルが存在する場合

**ファイルが存在する場合** の **すでに存在するファイル**（`if_exists`）で、ファイルがすでに存在する場合の動作を指定します。**上書きする**（`overwrite`、デフォルト）は、すでにあるファイルを置き換えます。**何も書き込まずにステップを失敗させる**（`fail`）は、書き込もうとするファイルがすでに存在する場合に、何も書き込まずにステップを停止します。
