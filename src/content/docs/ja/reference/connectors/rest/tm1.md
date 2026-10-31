---
title: TM1コネクタ
description: RESTのAPIを介して、PlaidCloudをIBM TM1 / Planning Analyticsサーバーに接続します。ネイティブのBasic認証またはCAM名前空間認証を使用でき、クラウドから直接接続することも、クラウドから直接到達できないサーバーにはオンプレミスのPlaidLinkエージェント経由で接続することもできます。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/tm1.md
---

公開されているOData v4 REST APIを介して、PlaidCloudをIBM **TM1 / Planning Analytics**サーバーに接続します。JVMブリッジやPAOlapドライバーは不要です。キューブのデータは[TM1: キューブのクエリ](/ja/reference/workflow-steps/ibm-planning-analytics/tm1-query/)ステップで、TM1のディメンション階層は[TM1: ディメンションの読み取り](/ja/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/)ステップで読み取ります。どちらもクラウドから直接接続します。自社ネットワーク内からしか到達できないTM1サーバーには、[TM1: キューブのクエリ（エージェント）](/ja/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/)ステップを使用します。このステップは、インストール済みのPlaidLinkエージェント経由で同じ読み取りを実行します。

この接続の種類は、接続ピッカーに**IBM Planning Analytics (TM1)** と表示されます。

## 認証の仕組み

TM1自身のREST認証方式に対応した、2つの認証モードがあります。

- **Native**：TM1のユーザー名とパスワードによるHTTP Basic認証です。
- **CAM**：名前空間を指定する、IBM Cognos Access Managerのシングルサインオンです。リクエストには、ユーザー名、パスワード、名前空間を組み合わせて作成した`Authorization: CAMNamespace`ヘッダーが付きます。通常のBasic認証とは異なります。

PlanningAnalytics-as-a-Service（PAaaS）のベアラートークンによるログインにはまだ対応しておらず、上記の2つのREST認証方式のみに対応しています。

## 設定

| フィールド | 必須 | 説明 |
|---|---|---|
| 名前 | はい | この接続の表示名です。 |
| ホスト | はい | TM1のREST APIのホストです。例：`https://tm1-prod.example.com:8010`、またはPAaaSのURL。 |
| デフォルトのデータベース | いいえ | TM1: キューブのクエリステップのデータベースフィールドに、あらかじめ入力される値です。ステップごとに上書きできます。 |
| 認証モード | はい | `Native`（TM1のユーザー／パスワード）または`CAM`（Cognos Access ManagerのSSO）です。デフォルトはNativeです。 |
| ユーザー名 | はい | 認証に使用するTM1アカウントです。 |
| パスワード | はい | 暗号化して保存されます。 |
| CAM名前空間 | CAMの場合のみ | 認証先のCognos Access Manager名前空間です。Nativeモードでは使用されません。 |
| SSL証明書を検証 | いいえ | デフォルトでオンです。テストサーバーで、自己署名証明書であることが分かっている場合にのみオフにしてください。 |
| タイムアウト（秒） | いいえ | デフォルトは30です。 |

## 接続のテスト

**接続をテスト**は、サーバーの`Configuration`シングルトン（`GET {host}/api/v1/Configuration`）にアクセスして確認します。これはTM1が公開する認証付き呼び出しのうち最も負荷が軽く、データベースやキューブのコンテキストを必要としません。テストに成功すると、サーバーの **`ProductVersion`** が表示され、ホストに到達できること、および認証情報で認証できることの両方を確認できます。

## 読み取り専用

このコネクタは読み取り専用です。TM1からキューブのデータとディメンション階層を読み取りますが、TM1への書き込み、転記、TIプロセスの実行は行いません。

## 接続でできること

- **保存済みビューまたはMDXでキューブのデータを読み取る。** [TM1: キューブのクエリ](/ja/reference/workflow-steps/ibm-planning-analytics/tm1-query/)ステップは、名前付きのキューブビューまたはMDXクエリを直接実行し、必要に応じてポイントオブビューによるスライスを適用して、結果をテーブルに格納します。
- **TM1の階層をPlaidCloudのディメンションとして読み込む。** [TM1: ディメンションの読み取り](/ja/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/)ステップは、ディメンションの要素、親子の関係、属性を読み取り、それらからPlaidCloudのディメンションを作成します。
- **期間で絞り込んで増分抽出する。** TM1には変更追跡の機能がないため、新しいデータだけが必要なワークフローでは、期間またはバージョンでクエリを絞り込みます。パターンについては、ステップのリファレンスを参照してください。
- **キューブ、ビュー、ディメンションをクラウドから直接ライブで検出する。** ステップのフォームにあるキューブ、ビュー、ディメンションのピッカーは、接続先のサーバーに直接問い合わせます。そのため、名前を手入力せずに、実在する名前を選択できます。
- **クラウドから到達できないTM1サーバーを、オンプレミスのエージェント経由で読み取る。** 以下の[ファイアウォール内のTM1を読み取る](#ファイアウォール内のtm1を読み取る)を参照してください。

## ファイアウォール内のTM1を読み取る

自社ネットワーク内からしか到達できないTM1サーバー（公開エンドポイントも、許可リストに登録されたIPも、PlaidCloudへのVPNもないサーバー）には、クラウドから直接接続する代わりに、インストール済みの**PlaidLinkエージェント**経由で接続します。[TM1: キューブのクエリ（エージェント）](/ja/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/)ワークフローステップは、TM1: キューブのクエリと同じビュー／MDX／ポイントオブビューのクエリを、エージェントに送って実行します。エージェントはお使いのネットワーク上でTM1に接続し、結果を返します。

この方法には、次のものが必要です。

- **インストール済みのPlaidLinkエージェント**：TM1サーバーにネットワークでアクセスできるマシンにインストールします。[PlaidLinkのインストール](/ja/reference/cli/plaidlink/install/)を参照してください。
- **TM1ハンドラーを含むビルドのエージェント**：PlaidCloudは、エージェントにクエリを送る前に、そのエージェントが通知する機能を確認します。そのため、古いビルドのエージェントは、再ビルドして再インストールするまでTM1のリクエストを処理できません。PlaidLinkは自動更新されません。[PlaidLinkのアップグレード](/ja/reference/cli/plaidlink/upgrade/)を参照してください。
- **そのエージェントと共有されたこのTM1接続**：接続にすでに設定されているメンバー／グループのアクセスに加えて、接続の`Actions > Agents`リストから共有します。[セキュリティモデル](/ja/guides/connections/create-connection/#セキュリティモデル)を参照してください。

TM1: キューブのクエリ（エージェント）にはライブ検出がありません。エージェントに到達できるのは実行中のみで、ステップのフォームを開いている間は到達できないためです。そのため、キューブ、ビュー、MDXは手入力し、ステップの実行時に検証されます。TM1: ディメンションの読み取りはクラウドからの直接接続のみに対応しており、オンプレミス経由の方法はまだありません。

## 既知の制限事項

| 制限事項 | 内容 |
|---|---|
| 読み取り専用 | 書き戻しとTIプロセスの実行はできません。 |
| オンプレミス経由はクエリのみ | オンプレミスのPlaidLinkエージェント経由の方法で対応しているのは、キューブの読み取り（TM1: キューブのクエリ（エージェント））のみです。TM1: ディメンションの読み取りには、オンプレミス経由の方法がまだありません。PlaidCloudが直接到達できるネットワーク経路が必要です。 |
| ディメンションの読み取りは単一階層・単一親のみ | 複数の親を持つ要素を含むTM1の階層は、PlaidCloudのディメンションとして読み込めません。また、集計の重みは符号のみが表現可能で、その大きさ（0.5、2.0）は表現できません。[TM1: ディメンションの読み取り](/ja/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/#このステップで表現できないこと)を参照してください。 |
| PAaaSのベアラー認証には非対応 | 対応している認証は、Native（Basic）とCAMのみです。 |

## 関連情報

- [TM1に接続する（ガイド）](/ja/guides/connections/tm1/)：接続を作成し、クエリを構築します。
- [TM1: キューブのクエリ](/ja/reference/workflow-steps/ibm-planning-analytics/tm1-query/)：クラウドから直接接続してキューブを読み取ります。
- [TM1: キューブのクエリ（エージェント）](/ja/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/)：オンプレミスのエージェント経由でキューブを読み取ります。
- [TM1: ディメンションの読み取り](/ja/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/)：TM1の階層をPlaidCloudのディメンションとして読み込みます。
- [接続の作成と管理](/ja/guides/connections/create-connection/)
