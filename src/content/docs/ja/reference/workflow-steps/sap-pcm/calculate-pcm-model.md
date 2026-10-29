---
title: Calculate PCM Modelステップ
description: PlaidCloud のワークフローステップから SAP PCM モデルの計算をトリガーし、収益性とコスト配賦の処理ジョブを実行します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/calculate-pcm-model.md
---

## 説明



SAP Profitability and Cost Management（PCM）モデルの計算エンジンをトリガーします。上流のデータロードによってモデルの入力（アサインメント、ドライバー、ソースデータ）が投入された後に、ワークフローでコスト計算を実行するために使用します。

計算は PCM サーバー側で非同期に実行されます。長時間かかる計算を中止する必要がある場合は、[Stop PCM Model Calculationステップ](/ja/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation/)と組み合わせてください。


## 当社の認定実績


PlaidCloud は SAP の公式パートナーであり、SAP PCM のモデル設計と導入に関連するサービスの推奨ベンダーです。







## 例


ドロップダウンから使用するエージェントを選択し、「Model Name」フィールドにモデル名を入力します。必要に応じて「Wait for Calculation to Complete」チェックボックスをオンにし、「Save and Run Step」をクリックします。
