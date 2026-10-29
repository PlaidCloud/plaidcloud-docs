---
title: Convert Document Encoding to ASCII
description: PlaidCloudワークフローステップでドキュメントファイルのエンコードをASCIIに変換し、ASCIIテキストを必要とするシステムとの互換性を確保します。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-ascii.md
---

## 説明

テキストファイルをプレーンなASCIIで書き直します。情報源に複数のエンコードが混在している場合や、他のツールが特定のエンコードをサポートしていない場合に特に便利です。

## 仕組み

- ソースのエンコードが検出されます。UTF-8のファイルはUTF-8として読み取られ、そこに貼り付けられたWindowsの文字（たとえばWordやExcelの引用符）は、いくつあってもそのまま通ります。それ以外のエンコードのファイルは、UTF-8として無効な最初の部分から検出されたエンコードで読み取られます。
- アクセント付きの文字は基底文字が残り（`café`は`cafe`になります）、ASCIIの形がない文字は削除されます。
- 二重引用符だけを含む行は、その前の行の末尾に結合されます。
- エンコードを検出できないファイルがあると、ステップはそのファイルを示して失敗します。
- 入力パスが存在しない場合、またはファイルがない場合、ステップはそのパスを示す警告を出して何も処理せずに終了し、ワークフローは続行されます。

## 例

入力ファイルを選択し、その場所にあるファイルを参照します。出力先を選択し、ファイルの保存先を参照して選択します。保存して実行します。
