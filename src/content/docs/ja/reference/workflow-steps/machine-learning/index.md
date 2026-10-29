---
title: 機械学習
description: scikit-learnモデルを学習し、それらでテーブルをスコアリングするワークフローステップです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/machine-learning/index.md
---

任意のテーブルでモデルを学習し、モデルテーブルとしてワークフロー内で引き継いで、データテーブルをスコアリングします。

## ステップ

- [ML: モデルの学習](/ja/reference/workflow-steps/machine-learning/ml-train/) — ソーステーブルでscikit-learnモデル（分類または回帰）を適合させ、適合済みモデル、パラメーター、特徴量リスト、学習メトリックを含む、クエリ可能なモデルテーブルを書き出します。
- [ML: スコアリング](/ja/reference/workflow-steps/machine-learning/ml-score/) — 学習済みのモデルテーブルでデータテーブルをスコアリングし、予測列を追加します。

AlteryxのAssisted Modelingパイプラインがこれらのステップにどのように変換されるかについては、[Alteryxワークフローの移行](/ja/guides/workflows/migrate-alteryx-workflows/#機械学習アシストモデリングの変換)を参照してください。
