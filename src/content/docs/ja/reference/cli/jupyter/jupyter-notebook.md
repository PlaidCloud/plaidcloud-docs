---
title: Jupyterノートブック
description: PlaidCloudでJupyterノートブックを実行し、対話的なデータ分析、可視化、Pythonによるデータ探索ワークフローを行います。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/jupyter-notebook.md
---

JupyterノートブックとJupyter Labは、データの分析、探索、説明、レポート作成のための優れた対話機能を提供します。PlaidCloudでは、ノートブックで情報を直接利用できます。

PlaidCloudは、有効化されている場合、各テナントのワークスペース内でJupyterHubを提供します。以下のドキュメントは、デスクトップまたは別のサーバーにJupyterを個別にセットアップする際の手順です。

## Jupyterノートブックのインストール
ここでは、Jupyterノートブックのインストールが正常に動作していることを前提とします。

### スタンドアロンのJupyterノートブックのインストール
Jupyterノートブックをローカルにインストールする方法の詳細は、[Jupyterのインストールに関するドキュメント](https://jupyter.org/install)をご覧ください。

### VS Codeに追加する
VS Codeには、ノートブックをVS Code内で直接実行できる拡張機能もあります。[Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)から拡張機能をインストールします。


## PlaidCloudユーティリティのインストール
PlaidCloudには、標準的なOAuthとJSON-RPCリクエストでもアクセスできますが、アクセスを簡単にするために、事前構築済みのライブラリの使用をおすすめします。さらに、PlaidCloudユーティリティライブラリには、Pandasデータフレームで使える便利なデータヘルパーが含まれています。

PlaidCloudユーティリティをインストールするには、次のpipインストールを実行します。

```bash
pip install plaidcloud-rpc@git+https://github.com/PlaidCloud/plaid-rpc.git@v1.4.0#egg=plaidcloud-rpc
```

```bash
pip install plaidcloud-utilities@git+https://github.com/PlaidCloud/plaid-utilities.git@v1.5.2#egg=plaidcloud-utilities
```

## OAuthトークンの取得

OAuthトークンの取得方法と、自動認証のためのシステム設定については、[OAuthの設定](/ja/reference/cli/jupyter/oauth-setup/)をご覧ください。


## Jupyterノートブックのユーザーインターフェイスを開く

ノートブックサーバーを起動して始めます。



Jupyterノートブックサーバーにサインインしたら、UIから新しいノートブックを作成します。

空のノートブックが開きます。



APIエンドポイント経由でPlaidCloudと通信するための接続を作成します。

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection()
```


ローカルのテーブルオブジェクトを作成してクエリを実行すると、結果が自動的に[Pandas](https://pandas.pydata.org/)のデータフレームに格納されます。

```python
tbl_sf_cust_master = conn.get_table('Salesforce_Customer_Master') # This gets a table object
df_sf_cust_master = conn.get_data(tbl_sf_cust_master) # This retrieves all the data into a dataframe
```


同じテーブルオブジェクトを使って、標準的なSQLAlchemy構文でより高度なクエリを記述することもできます。

```python
df_sf_cust_master_w_sales = conn.get_data(
    tbl_sf_cust_master.select().with_only_columns(
        [tbl_sf_cust_master.c.Id, tbl_sf_cust_master.c.CurrencyIsoCode, tbl_sf_cust_master.c.SyDSalesRegion]
    ).where(
        tbl_sf_cust_master.c.TotalSalesPast3Years > 0
    )
)
```
