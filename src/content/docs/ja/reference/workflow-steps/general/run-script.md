---
title: アプリ操作の実行
description: ワークフローから、登録済みのアプリケーション操作を呼び出します。必要に応じて、ドキュメントのパスとパラメーターを渡せます。
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/run-script.md
---

## 説明

ワークフロー内から、登録済みのアプリケーション操作を呼び出します。データ変換ではないプラットフォームの処理（アプリが自動化のために公開している操作）を起動するために使用します。

## 設定

### 実行するアプリケーション操作

呼び出す操作です。

### ファイルパス

ファイルを受け取る操作の場合:

- **Document directory** — 渡すドキュメントアカウントとパスです。
- **File parameter name** — 操作がパスを受け取るパラメーターの名前です。デフォルトは `document_path` です。操作の名前が異なる場合にのみ変更してください。

### 任意のパラメーター

ファイルパスとあわせて操作に渡される、名前と値のペアです。

## 関連項目

- [一般ステップ](/ja/reference/workflow-steps/general/)
- [User Defined Transform ステップ](/ja/reference/workflow-steps/general/user-defined-transform/)
- [Run Remote Python ステップ](/ja/reference/workflow-steps/general/run-remote-python/)
