---
title: User Defined Transform ステップ
description: PlaidCloud のワークフローステップで Python コードを使用してカスタムのデータ変換を作成し、柔軟で強力なデータ処理ロジックを実現します。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/user-defined-transform.md
---

## 説明

PlaidCloud に付属する **標準ワークフロー変換** で、通常は必要なほぼすべての操作を実行できます。さらに、これらの標準変換はパフォーマンスのために継続的に最適化されており、最も堅牢なデータを提供します。ただし、標準のオプションを単独または組み合わせて使用しても目的を達成できない場合は、**ユーザー定義変換** を作成してニーズを満たすことができます。PlaidCloud では、多くの高度なパッケージを含む標準的な Python コードを使用できます。

ユーザー定義変換の作成には Python によるコーディングが必要で、Python 3.14 上で実行されます。詳細については、[Python の Web サイト](https://www.python.org/)をご覧ください。



## ユーザー定義変換

ユーザー定義関数（UDF）を作成する方法は 2 つあります。
 - ロジックを PlaidCloud 内で直接記述して管理する
 - Git リポジトリに接続し、ファイルを指定する

標準的な Python の使用に加えて、PlaidCloud のすべての API 関数をすぐに利用でき、PlaidCloud とネイティブに連携できます。SciPy、PySpark、Pandas などの高度な分析パッケージもインポートして使用できます。

### PlaidCloud に保存する UDF の記述と管理
新しいユーザー定義関数（UDF）を作成するには、カスタム変換が必要なワークフローを開き、**ユーザー定義** タブを選択して、**Add User Defined Function** ボタンをクリックします。UDF の ID を指定します。作成後、編集機能のロジックアイコン（左端）を選択して、「Edit User Defined Function」ウィンドウを開きます。

また、以前に作成したユーザー定義関数は、**ユーザー定義** タブ内の **インポート** ボタンを使用してインポートすることもできます。このボタンを押して、ドロップダウンメニュー（現在のワークスペース内のすべてのワークフローが含まれます）から該当するワークフローを選択するだけです。次に、インポートする関数を選択し、**Import Selected Functions** ボタンを押します。

関数を作成またはインポートしたら、ワークフローの **Analyze Steps** タブに進み、**標準変換** を追加する場合と同じように、適切な位置に **User Defined Transform** ステップを追加します。設定ウィンドウで、タイプとして UDFの分析 を選択し、ドロップダウンメニューから該当する **ユーザー定義関数** を選択します。

### Git リポジトリ内の UDF を参照する

まず、**外部データ接続** の領域で、Git リポジトリ（GitHub、GitLab など）への接続を作成する必要があります。

Git リポジトリへの接続が利用可能になったら、ワークフローの **Analyze Steps** タブに進み、**標準変換** を追加する場合と同じように、適切な位置に **User Defined Transform** ステップを追加します。設定ウィンドウで、タイプとして 外部ソースコードリポジトリ を選択し、接続、ブランチ、UDF へのファイルパスを選択します。ブランチの選択ではタグも選択できるため、標準的なリリースプロセスに対応できます。

Git 内のファイルへの変更は、次回 UDF が実行されたときに自動的に反映されます。

## ソーステーブルとターゲットテーブルの設定
UDF 変換の設定でテーブルを定義せずに、UDF 内でテーブルに直接アクセスすることは可能ですが、テーブルの依存関係は利用できません。そのため、UDF で使用するすべてのソーステーブルとターゲットテーブルを設定で定義することをお勧めします。設定でテーブルを定義すると、UDF 内でより簡単に利用できるようになります（後述）。

## 追加の変数の指定
プロジェクトレベルとワークフローレベルの両方の変数は、標準の API メソッドを使用して UDF 内で利用できますが、ステップ固有の追加の変数が役立つことも少なくありません。これらは、設定の **その他の変数** セクションで定義できます。

変数の値は、手動で設定することも、プロジェクト変数とワークフロー変数の組み合わせを使って動的に定義することもできます。

## Python UDF の例

### PlaidCloud API 接続の設定を含む一般的なインポート

```python
### COMMON PYTHON IMPORTS
# import os
# import pandas as pd
# import numpy as np

### COMMON PLAIDCLOUD IMPORTS
from plaidcloud.utilities.connect import PlaidConnection
from plaidcloud.utilities import frame_manager as fm
# from plaidcloud.utilities import data_helpers as dh

conn = PlaidConnection()
```

### アプリケーションログへのログメッセージの設定
```python
conn.logger.info('Sample Info Log Message')
conn.logger.warn('Sample Warning Log Message')
conn.logger.error('Sample Error Log Message')
```

### プロジェクト変数とワークフロー変数へのアクセス
```python
workflow_vars = conn.analyze.workflow.variable_values(project_id=conn.project_id, workflow_id=conn.workflow_id)
variable_1 = workflow_vars.get('my_wf_var_1')

project_vars = conn.analyze.project.variable_values(project_id=conn.project_id)
variable_2 = project_vars.get('my_prj_var_2')
```

### テーブルへのデータの保存
この例では、データが Pandas のデータフレームに存在することを前提としています。

```python
fm.save(dfImport, name='/path_to_table/OUTBOUND_TABLE_NAME', append=False)
```

### テーブルからのデータの読み取り

テーブルを使用するには、まずテーブルオブジェクトを取得する必要があります。オブジェクトを取得したら、`get_data()` メソッドを使用してクエリを実行できます。`get_data()` メソッドは SQLAlchemy の構文にも対応しており、高度なクエリを構築できます。クエリの結果は Pandas のデータフレームオブジェクトです。

```python
tbl_object = conn.get_table('INBOUND_TABLE_NAME')
dfImport = conn.get_data(tbl_object)
dfImportQuery = conn.get_data(
    tblImport.select().with_only_columns(
        [tblImport.c.Col1, tblImport.c.Col2]
    ).where(
        tblImport.c.Col1 == 'FilterValue'
    )
)
```

### 定義済みのソーステーブルとターゲットテーブルからのデータへのアクセス
ステップの設定で構成した、定義済みのソーステーブルとターゲットテーブルを使用する場合、最初のオブジェクトの取得（つまり `get_table()`）は自動的に実行されます。事前に構成したテーブルを利用するには、次の手順を使用します。

```python
# Source Tables as a dict
my_source = conn.udf.source_by_name('my_table')

# All sources as a list
my_sources = conn.udf.sources()

# Target Tables as a dict
my_target = conn.udf.target_by_name('my_table')

# All targets as a list
my_targets = conn.udf.targets()
```

### ステップ変数へのアクセス
ステップの設定で定義した変数へのアクセスは、次の手順で行います。

```python
# Access variables by name
my_var = conn.udf.variable_by_name('my_var')

# All variables as a list
my_vars = conn.udf.variables()
```

### Document からのファイルの読み取り
Document 内のファイルへのアクセスも、PlaidCloud 接続を使用すれば簡単です。これは、ファイルの内容を取得して、実行時コンテナー内のローカルパスに保存する関数の例です。

```python
def get_from_document(conn, document_account, remote_path, local_file_path):
    # accounts = conn.document.view.shared_accounts()
    remote_file = base64.b64decode(
        conn.document.view.download(
            account_id=document_account,
            path=remote_path,
        )
    )
    with open(local_file_path, 'wb') as output_file:
        output_file.write(remote_file)

    return local_file_path
```
