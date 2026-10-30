---
title: エディターでのコードの整形（Prettify）
description: 整形ボタンまたは Shift+Alt+F を使って、PlaidCloudのワークフローステップエディターでSQL、JSON、式のコードを自動整形します。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/prettify-code-in-editors.md
---

## エディターでコードを整形する

複数のワークフローステップエディターがコードエディターを使用しています。SQLステップ（Frame Extract SQL、SQLのリモート実行、Remote Direct SQL、Remote Export SQL、SQLのインポート）、LLMステップの**Result schema**（JSON）、およびフローの各領域で使用される式エディターです。

これらのエディターにはそれぞれ**整形**ボタンがあり、コードをその場で再整形します。インデントを付け、レイアウトを統一して、読みやすくレビューしやすくします。エディター内にカーソルがあるときに **Shift+Alt+F**（macOSでは **Shift+Option+F**）を押すこともできます。

## 整形される内容

- **SQL** — 読みやすい複数行のレイアウトに整形されます。1行に1つの句、位置をそろえた `CASE` / `WHEN`、ネストした関数の展開が行われます。プロジェクト変数や、`{variable}`、`{{ ... }}`、`{% ... %}` などのテンプレートトークンは、そのまま保持されます。
- **JSON** — 2スペースのインデントで再インデントされます（たとえば、LLMステップのResult schema）。
- **式** — PlaidCloudの式は、標準のPython形式で整形されます。演算子とカンマの前後のスペースが統一され、長い式は改行されます。

## 知っておくべきこと

- 整形によって、コードの動作が変わることはありません。変わるのはレイアウトだけです。SQLのキーワードと識別子は、元の大文字・小文字がそのまま保持されます。
- コードを解析できない場合（構文エラー）、整形はコードに手を加えず、短いメッセージを表示します。そのため、作業内容が失われることはありません。
- 整形は1回の操作として適用されます。**Ctrl+Z**（macOSでは **Cmd+Z**）を押すと元に戻せます。
