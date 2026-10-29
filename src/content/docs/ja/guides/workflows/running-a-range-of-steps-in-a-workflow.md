---
title: ワークフローのステップ範囲の実行
description: PlaidCloudのワークフロー内の特定のステップ範囲を実行して、データ処理パイプラインの一部を選択的に実行します。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/running-a-range-of-steps-in-a-workflow.md
---

個々のステップを実行するだけでなく、開発、テスト、トラブルシューティングのために、ワークフロー全体の一部を実行したい場合もあります。ステップのサブセットを実行するには、実行したいステップをすべて選択し、ワークフローステップ階層の上部にある**アクション**メニューから**選択したステップを実行**を選択します。通常のワークフロー処理が開始されますが、選択したステップの先頭から開始し、最後に選択したステップが完了した時点で停止します。

最後に選択したステップが[**Execute in Parallel**](/ja/guides/workflows/controlling-parallel-execution/)に設定されたグループ内にある場合、実行は、そのグループ内で選択されている他のすべてのステップが終了するまで待ってから停止します。
