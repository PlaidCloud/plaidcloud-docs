---
title: Stop PCM Model Calculationステップ
description: ワークフローステップからSAP PCMモデルの実行中の計算を停止し、エラーや問題が検出された場合に処理を中断します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation.md
---

## 説明



実行中のSAP PCMモデルの計算を中止します。計算に時間がかかりすぎている場合、誤った入力データで開始してしまった場合、または優先度の高いジョブのためにサーバーリソースを解放する必要がある場合に便利です。

実行中の計算がない場合、このステップはワークフローログに警告を書き込み、処理を続行します。


## 当社の資格


PlaidCloudはSAP公式パートナーであり、SAP PCMモデルの設計および実装に関するサービスの優先ベンダーです。




## 例


ドロップダウンから**使用するエージェント**を選択し、「Model Name」を入力して、「Wait for Copy to Complete」チェックボックスをオンにしてから、「Save and Run Step」をクリックします。
