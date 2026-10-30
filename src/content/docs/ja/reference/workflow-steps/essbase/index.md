---
title: Oracle Essbaseステップ
description: Essbase接続を通じてOracle Essbaseキューブから読み取るワークフローステップです。ライブのMDXクエリと、PlaidCloudディメンションに読み込むディメンションアウトラインに対応し、クラウド直結です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/index.md
---

[Oracle Essbase接続](/ja/guides/connections/essbase/)を通じて、Oracle **Essbase**から読み取るワークフローステップです。ライブのMDXクエリによるキューブデータの取得と、PlaidCloudディメンションへのディメンションアウトラインの読み込みができます。EssbaseにはREST APIを介して**クラウド直結**で接続します。これらのステップには、オンプレミスのエージェント経由のパスはありません。

## ステップ

- [Essbase: キューブのクエリ](/ja/reference/workflow-steps/essbase/essbase-query/) — キューブに対してライブのMDXクエリを実行し、結果のグリッドをテーブルとして格納します。クラウド直結です。
- [Essbase: ディメンションの読み取り](/ja/reference/workflow-steps/essbase/essbase-dimension-read/) — Essbaseのディメンションアウトラインを、PlaidCloudディメンションに読み込みます。クラウド直結です。

## 関連項目

- [Oracle Essbaseに接続する（ガイド）](/ja/guides/connections/essbase/)
- [Oracle Essbaseコネクタ](/ja/reference/connectors/erp/oracle-essbase/)
