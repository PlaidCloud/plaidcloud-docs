---
title: データエンジニアリング学習パス
description: PlaidCloud データエンジニアリングのプラクティショナーとエキスパートのラボの前に読むもの、および各ラボで行う内容を説明します。
sidebar:
  label: データエンジニアリング
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/data-engineering.md
---

データエンジニアリングトラックでは、正確で、変数で駆動され、高速なワークフローの構築を扱います。まず[ファンデーション](/ja/guides/certification/foundations/)パスから始めてください。ラボの仕組みについては、[PlaidCloud 認定](/ja/guides/certification/)を参照してください。

## プラクティショナー

### 読む順序

1. [ワークフローの作成](/ja/guides/workflows/create-workflow/)
2. [ワークフローステップ](/ja/reference/workflow-steps/)、特に[内部結合](/ja/reference/workflow-steps/tables/table-inner-join/)と [Table Extract ステップ](/ja/reference/workflow-steps/tables/table-extract/)
3. [ワークフロー変数を管理する](/ja/guides/workflows/manage-workflow-variables/)
4. [作業を再利用する: 変数、マクロ、UDF](/ja/get-started/tutorials/reuse-variables-macros-udfs/)
5. [ワークフローを実行する](/ja/guides/workflows/run-a-workflow/)
6. [ワークフローログを表示する](/ja/guides/workflows/viewing-workflow-log/)

### ラボの内容

このラボの名前は *データエンジニアリング: 月次売上の構築* です。

3 つの未加工テーブル（売上明細、店舗、製品）がロードされています。ラボのワークフローで、1 か月分の販売済み明細について、地域と製品カテゴリごとに 1 行で、数量と売上を含む月次サマリーを構築します。月はステップに直接入力した値ではなく、プロジェクト変数から取得します。ラボは変数を変更して、ワークフローをもう一度実行します。使用できるのは標準ステップだけで、SQL ステップやコードステップは使いません。

ラボでは、ワークフローが実行されること、標準ステップだけが使われていること、サマリーがその月でも別の月でも正しいことをチェックします。

## エキスパート

エキスパートのラボには時間制限があります。開始した時点から 4 時間です。

### 読む順序

1. [ワークフローをデバッグする](/ja/get-started/tutorials/debug-a-workflow/)
2. [ワークフローログを表示する](/ja/guides/workflows/viewing-workflow-log/)
3. [ステップエラーの管理](/ja/guides/workflows/managing-step-errors/)
4. [ステップデータをプレビューする](/ja/guides/workflows/preview-step-data/)
5. [ワークフローを最適化する](/ja/guides/workflows/optimize-a-workflow/)
6. [ワークフローステップ](/ja/reference/workflow-steps/)、特に[内部結合](/ja/reference/workflow-steps/tables/table-inner-join/)

### ラボの内容

このラボの名前は *データエンジニアリング エキスパート: 夜間ビルドの修復と高速化* です。

夜間のワークフローが実行されなくなっており、その前から非常に遅くなっていました。実行ログを読み、原因をすべて見つけて、ワークフローが成功し、正しいサマリーを生成し、以前よりはるかに短い時間で完了するように修正します。アカウントのない行は除外し、重複して登録されているアカウントによって件数が水増しされないようにします。使用できるのは標準ステップだけで、入力テーブルはそのままにします。

ラボでは、ワークフローが実行されること、標準ステップだけが使われていること、サマリーが正しいこと、入力テーブルが変更されていないこと、ワークフローが十分に高速であることをチェックします。
