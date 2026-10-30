---
title: Calculate and Export PCM Modelステップ
description: PCM モデルの計算を実行し、その結果を PlaidLink エージェント経由でデータベースまたは区切り文字形式のファイルにエクスポートします。
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/export-pcm-model.md
---

## 説明

PCM のインストール環境にアクセスできる [PlaidLink エージェント](/ja/reference/workflow-steps/agent/)を通じて、SAP PCM モデルの計算と結果のエクスポートを 1 つのステップで行います。[Calculate PCM Modelステップ](/ja/reference/workflow-steps/sap-pcm/calculate-pcm-model/)が計算の実行のみを行うのに対し、このステップは出力の移動も行います。

## 設定

### 使用するエージェント

PCM のインストール環境にアクセスする PlaidLink エージェントです。

### モデル情報

- **モデル名** — 計算する PCM モデルです。
- **Export specification path** — エクスポート対象を記述した PCM のエクスポート仕様です。

### エクスポート出力先

データベースターゲット、ファイルターゲット、またはその両方を選択します。

**データベースへ** — デフォルトでオンです。エクスポートは、仕様で設定されたデータベースターゲットに書き込まれます。

**ファイルへ** — デフォルトでオフです。オンにすると、次の項目が使用できます。

- **ファイルパス** — エージェントがファイルを書き込む場所です。
- **エイリアス** — エクスポートに記録されるエイリアスです。デフォルトは `DEFAULT ALIAS` です。
- **Precision** — エクスポートされる値の小数桁数です。デフォルトは 0 です。
- **区切り文字** — カンマ、タブ、パイプ、セミコロン、スペース、`@`、`~`、`:` のいずれかです。デフォルトはタブです。
- **追加** — デフォルトでオフです。そのため、実行のたびにファイルが置き換えられます。オンにすると、実行結果が蓄積されます。
- **Include rules** — デフォルトでオフです。オンにすると、値とともにモデルのルールもエクスポートされます。
- **Unicode** — デフォルトでオフです。エクスポートするデータに、デフォルトのエンコーディング外の文字が含まれる場合にオンにします。

## 関連項目

- [SAP-PCMステップ](/ja/reference/workflow-steps/sap-pcm/)
- [Calculate PCM Modelステップ](/ja/reference/workflow-steps/sap-pcm/calculate-pcm-model/)
- [Run SAP PCM Hyper Loaderステップ](/ja/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader/)
