---
title: モデリング学習パス
description: PlaidCloud モデリングのプラクティショナーとエキスパートのラボの前に読むもの、および各ラボで行う内容を説明します。
sidebar:
  label: モデリング
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/modeling.md
---

モデリングトラックでは、ディメンションと配賦を扱います。階層の構築、ドライバーによるコストの按分、結果が一致することの確認です。まず[ファンデーション](/ja/guides/certification/foundations/)パスから始めてください。ラボの仕組みについては、[PlaidCloud 認定](/ja/guides/certification/)を参照してください。

## プラクティショナー

### 読む順序

1. [ディメンションの使い方](/ja/guides/dimensions/getting-started/)
2. [階層の管理](/ja/guides/projects/managing-hierarchies/)
3. [ディメンション階層を設計する](/ja/get-started/tutorials/design-a-dimension/)
4. [配賦クイックスタート](/ja/guides/allocations/getting-started/allocations-quick-start/)
5. [Allocation Split ステップ](/ja/reference/workflow-steps/allocation/allocation-split/)
6. [配賦モデルを構築する](/ja/get-started/tutorials/build-an-allocation/)
7. [配賦結果](/ja/guides/allocations/results/allocation-results/)
8. [ワークフローログを表示する](/ja/guides/workflows/viewing-workflow-log/)

### ラボの内容

このラボの名前は *モデリング: 共通IT費用の配賦* です。

あるテーブルに、各部門とその親部門が一覧されています。このツリーとまったく同じ主階層を持つディメンションを構築します。続いて、ラボのワークフローで、コストプールを部門の人数に比例して各部門に配賦し、部門ごとに 1 行の結果行を作成します。2 つ目のドライバーテーブルもありますが、このプールのドライバーではありません。

ラボでは、ワークフローが実行されること、階層が正しいこと、配賦後の合計が元データと一致すること、各部門が正しい金額を受け取っていることをチェックします。

## エキスパート

エキスパートのラボには時間制限があります。開始した時点から 4 時間です。

### 読む順序

1. [配賦を設定する](/ja/guides/allocations/setup/configure-an-allocation/)
2. [配賦のトラブルシューティング](/ja/guides/allocations/results/troubleshooting-allocations/)
3. [MCP 接続の AI エージェントで配賦をトレースする](/ja/integrations/ai-coding-agents/tracing-allocations/)
4. [配賦結果](/ja/guides/allocations/results/allocation-results/)
5. [ドライバーのシミュレーションを試す](/ja/guides/allocations/results/driver-what-if/)
6. [階層の管理](/ja/guides/projects/managing-hierarchies/)

### ラボの内容

このラボの名前は *モデリング エキスパート: 配賦モデルの修復* です。

2 段階の配賦モデルが総勘定元帳と一致しなくなっており、一部の部門の金額が明らかに誤っています。原因をたどってモデルを修正します。各段階がプールの金額をちょうど配賦し、部門ごとの合計が正しく、総勘定元帳と合うようにします。部門ディメンションには、実在する部門だけを含めます。一致させるために調整行を使うことはできません。続いて、IT コストを人数ではなくフロア面積で配賦した場合に各部門が負担する金額を示すステップを追加します。

ラボでは、ワークフローが実行されること、階層が正しいこと、各段階と部門ごとの合計が総勘定元帳と一致すること、各部門の合計が正しいこと、フロア面積のシナリオが正しいことをチェックします。
