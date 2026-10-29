---
title: Workflow Loop ステップ
description: PlaidCloudのワークフローステップでループを作成し、一連の値を反復処理して、コレクション内の各項目に対してステップを繰り返します。
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/workflow-loop.md
---

## 説明

データセットの行ごとに1回ずつ対象のワークフローを実行し、各反復の前にその行の列の値をプロジェクト変数として設定します。異なる入力で複数回実行する必要がある、パラメーター化されたプロセスがある場合に使用します。たとえば、「このテーブルにあるすべての事業部門について月次締めを実行する」「一覧にあるすべての四半期についてこのレポートをロードする」といった場合です。

各ループの反復では、変数が手動で設定されたかのように参照できるため、呼び出されたワークフローは、標準の `\{variable_name}` 構文を使って、式、フィルター、ファイルパス、テーブル名の中でそれらを参照できます。ループはデフォルトで順次実行され、反復は並列には実行されません。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 690 170" role="img" aria-label="Q1、Q2、Q3の行を持つデータセットに対するWorkflow Loop。各行の列の値がプロジェクト変数になり、その後、対象のワークフローが実行されます。行ごとに1回ずつ、並列ではなく順番に実行されます。" style="width:100%;max-width:690px;height:auto;">
  <defs><marker id="wl-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="50" width="120" height="74" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="74" y="44" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">データセット</text>
  <text x="74" y="76" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q1</text>
  <text x="74" y="96" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q2</text>
  <text x="74" y="116" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q3</text>
  <path d="M134 87 L178 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="180" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="250" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q1</text>
  <text x="250" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">1回目</text>
  <path d="M320 87 L360 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="362" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="432" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q2</text>
  <text x="432" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">2回目</text>
  <path d="M502 87 L542 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="544" y="63" width="138" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="613" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q3</text>
  <text x="613" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">3回目</text>
  <text x="408" y="142" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">順次実行 — 一度に1回ずつ、並列ではありません</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">各行の列がプロジェクト変数になり、その後、対象のワークフローが実行されます。行ごとに1回ずつ、順番に実行されます。分離された並列のファンアウトが必要な場合は、代わりに<a href="/ja/guides/workflows/create-a-macro/">マクロ</a>を使用してください。</figcaption>
</figure>



## 停止するワークフロー


まず、**プロジェクト**ドロップダウンメニューから、ループのたびに実行されるワークフローを含むプロジェクトを選択します。



次に、**ワークフロー**ドロップダウンメニューから、実行する特定のワークフローを選択します。

## 反復が失敗した場合

デフォルトでは、ワークフローが失敗した最初の反復でループが停止し、ステップも失敗します。**エラー処理**で**失敗した反復の後も続行**を選択すると、1つの反復が失敗しても、すべての反復が実行されます。失敗はそれぞれ、各反復の結果とともに**ループ実行ステータス**に保持され、ステップは、失敗した反復の数を示す警告とともに終了します。この選択を解除すると、ループは最初の失敗で停止します。

## 例

例は近日公開予定です
