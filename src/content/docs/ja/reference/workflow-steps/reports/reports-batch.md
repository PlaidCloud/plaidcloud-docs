---
title: Reports Batchステップ
description: PlaidCloud のワークフローステップからバッチ PDF レポートを生成し、データ入力の異なる複数のレポートをテンプレートから作成します。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/reports-batch.md
---

## 説明



1 つの RML テンプレートから、コントロールテーブルに基づいて多数の PDF レポートを生成します。コントロールテーブルの 1 行につき 1 つのレポートが生成され、各行の列の値がそのレポートの描画時のパラメーターとして使用されます。

主な用途は、顧客ごとの明細書（顧客ごとに 1 つの PDF）、事業部門ごとの財務諸表（事業部門ごとに 1 つの PDF）、請求書（注文ごとに 1 つの PDF）です。単発のレポートを生成する場合は、[Report Singleステップ](/ja/reference/workflow-steps/reports/report-single/)と比較してください。


## テンプレートが読み取る名前

テンプレートは、**レポートデータ**タブの各ソースと、**バッチレコード値データソース**マッピングの各ターゲット列を、それぞれの名前で読み取ります。定数のセクションはありません。各バッチ行が、そのレポートに対するテンプレートの値を提供します。新しいソースには `new_source`、`new_source_2` のような名前が付き、テンプレートはそのまま読み取れます。


## 保存時にチェックされる内容

すべてのソース名とバッチ列名は、指定されていて、重複しておらず、テンプレートが読み取れる必要があります。ルールは [Report Singleステップ](/ja/reference/workflow-steps/reports/report-single/)と同じで、定数の代わりにバッチ列が対象になります。*Batch column name 'unit id' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*

バッチのソーステーブルを選択しているのにバッチマッピングが空のまま保存すると、Populate と同様に、そのテーブルからマッピングが自動入力されます。


## 空のバッチテーブル

バッチのソーステーブルに行がない場合、ステップはバッチテーブルの名前を示す警告とともに正常終了し、レポートは生成されません。


## 例

例はまだありません...
