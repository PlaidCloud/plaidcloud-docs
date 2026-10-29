---
title: IBM TM1 / Planning Analytics ステップ
description: TM1 接続を介して IBM TM1 / Planning Analytics サーバーから読み取るワークフローステップです。保存済みビューまたは MDX によるキューブデータと、ディメンション階層を、クラウド直接またはオンプレミスの PlaidLink エージェント経由で読み取ります。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/index.md
---

[TM1 接続](/ja/guides/connections/tm1/)を介して IBM **TM1 / Planning Analytics** から読み取るワークフローステップです。保存済みビューまたは MDX によるキューブデータ（POV スライスの指定も可能）と、PlaidCloud ディメンションに読み込まれるディメンション階層を読み取ります。TM1 にはクラウドから直接アクセスするか、自社ネットワーク内からしかアクセスできないサーバーの場合は、オンプレミスの PlaidLink エージェント経由でアクセスします。

## ステップ

- [TM1: キューブのクエリ](/ja/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — 保存済みビューまたは MDX でキューブを読み取ります。POV スライスと、保存前のプレビューを利用できます。クラウド直接です。
- [TM1: キューブのクエリ（エージェント）](/ja/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — TM1: キューブのクエリのオンプレミス版で、インストール済みの PlaidLink エージェント経由でディスパッチされます。
- [TM1: ディメンションの読み取り](/ja/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — TM1 の階層を PlaidCloud ディメンションに読み込みます。クラウド直接です。

## 関連項目

- [TM1 への接続（ガイド）](/ja/guides/connections/tm1/)
- [TM1 コネクター](/ja/reference/connectors/rest/tm1/)
