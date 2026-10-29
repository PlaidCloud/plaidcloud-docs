---
title: Dashアプリでのデータとサインイン中ユーザーの読み取り
description: Dashアプリを、閲覧しているユーザーとして PlaidCloud に接続します。プロジェクトデータを読み取り、ユーザーごとの動作や行レベルセキュリティに閲覧者の ID を利用します。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/accessing-data.md
---

Dashアプリは PlaidCloud のデータを読み取ることができます。このとき、サーバー型の Panel アプリと同様に、**アプリを閲覧しているユーザーとして**読み取ります。アプリを開くと、PlaidCloud はプラットフォームの他の部分と同じシングルサインオンでユーザーをサインインさせ、アプリが行うすべての呼び出しは**その閲覧者自身の権限**で実行されます。共有のサービスアカウントはなく、閲覧者本人が見られないデータをアプリが見ることはありません。

ヘルパーは Dash ベースイメージに含まれる `plaidcloud_dash` にあります。

```python
from plaidcloud_dash import current_user, get_connection
```

## PlaidCloud への接続

Dashコールバックの内部から `get_connection()` を呼び出し、読み取りたいデータのあるプロジェクトを指定します。

```python
from plaidcloud_dash import get_connection

conn = get_connection(project_id="<your-project-id>")
```

必要な設定はこれだけです。トークン、ユーザー名、パスワードを指定する必要は**ありません**。`get_connection()` は、現在のセッションのアクセストークンを使って、サインイン中の閲覧者として自動的に認証します。プロジェクトの ID は、プロジェクトの URL または設定ページで確認できます。

> **コールバックの内部から呼び出してください。** `get_connection()` は、現在のリクエストの Flask セッションから閲覧者のトークンを読み取ります。このセッションは、コールバックがその閲覧者のリクエストを処理している間しか利用できません。ブロッキング呼び出しをバックグラウンドスレッドに渡す場合、素のスレッドプールはセッションを引き継ぎません。コールバック内でトークンを読み取り、明示的に渡してください。リクエストの外で（または認証を無効にした状態で）`get_connection()` を呼び出すと、ID のない接続を黙って返すのではなく、`RuntimeError` が発生します。

> **プロジェクトはコードで指定してください。** 公開ダイアログにプロジェクトの設定項目はありません。Dashアプリは、サーバー型 Panel アプリの `PlaidConnection(project_id=...)` と同様に、`get_connection(project_id=...)` で指定したプロジェクトを読み取ります。詳しくは[データとサインイン中ユーザーの読み取り](/ja/guides/panel-apps/accessing-data/)をご覧ください。`project_id` を指定しない `get_connection()` は、プロジェクトデータにアクセスしないアプリ（たとえば `current_user()` だけを呼び出すアプリ）であれば問題ありません。実在してアクセス可能なプロジェクト ID なしで、その接続に対してプロジェクト単位の操作を呼び出すと、`Project Id has not been set` が発生します。（複数のプロジェクトから読み取る場合は、プロジェクトごとに接続を開きます。）

### テーブルの読み取り

接続を使って、テーブルを名前で指定し、pandas の DataFrame として取得します。

```python
df = conn.get_dataframe("Sales Ledger")
```

接続は閲覧者本人なので、閲覧が許可されている行だけが返されます。プロジェクトへのアクセス権がまったくない場合は、権限エラーが発生します。

> **SQL を書かず、テーブルを名前で読み取ってください。** 管理者が[行アクセス](/ja/administration/access/managing-security-groups-and-assignments/#行アクセスと自分で作成するクエリ)を有効にしているプロジェクトでは、名前で読み取ると各閲覧者の行の許可が適用されます。一方、アプリが自分で組み立てたクエリは、プロジェクトのアーキテクト以外には拒否されます。許可を適用する対象となる単一のテーブルがないためです。名前で読み取っておけば、どちらの場合でもアプリは動作します。

## コールバック内で読み取る（インポート時やプロセススコープでは読み取らない）

1つのプロセスがすべての閲覧者に対応します。データの分離を正しく行うには、次の2つのルールを守ります。

- **モジュールスコープ（インポート時）で接続を開いたり、テーブルを読み取ったりしないでください。** `app.py` とそこからインポートされるモジュールは、コンテナーの起動時に**1回だけ**実行されます。この時点ではまだ誰もサインインしていません。そこで `get_connection()` や `PlaidConnection()` を呼び出しても、認証する閲覧者がおらず、アプリは起動時に失敗します（「アプリが起動しない」クラッシュループの最も一般的な原因です）。読み取りはすべて、閲覧者のリクエストとセッショントークンが存在するコールバックの内部で行ってください。

- **閲覧者ごとの結果を、モジュールやプロセスのスコープでキャッシュしないでください。** スレッド化された gunicorn ワーカーは、同時に接続するすべての閲覧者で1つの Python プロセスを共有します。そのため、モジュールレベルの変数、グローバルな辞書、`lru_cache` に保存した DataFrame は、*ほかのすべての*閲覧者から見えてしまい、1人の行が別の人の画面に漏れます。閲覧者ごとのデータはコールバック内で計算し、コールバックが終了したらスコープから外してください。

  ```python
  # WRONG — a module/process-global cache is shared across all viewers
  _CACHE = {}

  @app.callback(...)
  def _load(n):
      viewer = current_user()
      if viewer not in _CACHE:                      # still process-global; leaks under load
          _CACHE[viewer] = get_connection(project_id="…").get_dataframe("Sales")
      return _CACHE[viewer].to_dict("records")

  # RIGHT — read inside the callback, no shared state
  @app.callback(...)
  def _load(n):
      conn = get_connection(project_id="…")          # this viewer, this request
      return conn.get_dataframe("Sales").to_dict("records")
  ```

### 共有の参照データ

複数の閲覧者が本当に*同じ*参照データ（ルックアップテーブルや製品リストなど）を必要とする場合でも、プロセスレベルのキャッシュで共有しようとしないでください。PlaidCloud の通常の[行アクセスとプロジェクト権限](/ja/administration/access/managing-security-groups-and-assignments/)を使ってそれらのテーブルをアプリのユーザーに許可し、各閲覧者が自分の `get_connection()` で読み取るようにします。全員が同じ参照行を取得できるのは、全員に同じアクセスが許可されているからであり、ある閲覧者の読み取り結果を別の閲覧者に使い回しているからではありません。

## 閲覧者の識別

アプリの表示内容を**誰が見ているか**に応じて調整するには（パーソナライズされたあいさつ、タブの非表示、行レベルセキュリティなど）、`current_user()` を呼び出します。

```python
from plaidcloud_dash import current_user

viewer = current_user()  # the viewer's identifier
```

`current_user()` は、サインイン中の閲覧者の識別子を返します。ユーザー名を返し、ユーザー名のクレームがない場合はメールアドレス、さらにない場合はアカウント ID を返します。検証済みのサインイン情報から取得されるため、閲覧者の ID として信頼できます。例外は発生しません。認証が無効な状態やリクエストの外で呼び出すと、空の文字列を返します。

### 行レベルセキュリティ

この2つを組み合わせます。閲覧者を取得し、すべてのクエリをその閲覧者で絞り込みます。たとえば、各地域のマネージャーに自分の地域だけを表示するには、次のようにします。

```python
from dash import Input, Output
from plaidcloud_dash import current_user, get_connection


@app.callback(Output("sales-table", "children"), Input("load-btn", "n_clicks"))
def _load_my_region(n_clicks):
    viewer = current_user()
    conn = get_connection(project_id="<your-project-id>")

    sales = conn.get_dataframe("Regional Sales")
    mine = sales[sales["manager_email"] == viewer]

    return mine.to_dict("records")
```

接続がすでに閲覧者のプロジェクト権限を適用しているため、この絞り込みは、閲覧が許可されている範囲に対する*追加の*整形です。PlaidCloud 自体のアクセス制御の代わりにはなりません。

## 公開アプリ

**パブリックアクセスを許可**して公開した場合、アプリはサインインなしで提供されます。そのため、代理となる閲覧者がいません。`current_user()` は空の文字列を返し、`get_connection()` は認証に使うセッショントークンがないため例外を発生させます。公開アプリでは、誰に見られても問題のないデータだけを扱うか、パブリックアクセスをオフにして閲覧者にサインインしてもらい、上記のユーザー単位のモデルを適用してください。
