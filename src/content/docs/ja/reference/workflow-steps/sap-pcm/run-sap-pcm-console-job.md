---
title: Run SAP PCM Console Jobステップ
description: PlaidCloud のワークフローステップから SAP PCM コンソールジョブを実行し、バッチ処理や管理操作をリモートで行います。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/run-sap-pcm-console-job.md
---

## 説明



リモートの PCM サーバー上の SAP PCM コンソールでジョブを起動します。通常は、モデル計算 API ではなく PCM がコンソールインターフェース経由で公開している、管理タスクやバッチタスクに使用します。

アーカイブ操作、ハイパーローダーの実行、ベンダー固有のメンテナンス処理などに使用できます。具体的なジョブとパラメーターは、PCM の導入環境によって異なります。


## 当社の認定実績


PlaidCloud は SAP の公式パートナーであり、SAP PCM のモデル設計と導入に関連するサービスの推奨ベンダーです。








## 例


ドロップダウンから**使用するエージェント**を選択し、「Console File Path」フィールドにコンソールファイルのパスを入力します。必要に応じて「Wait for Console Job to Complete」チェックボックスをオンにし、「Save and Run Step」をクリックします。
