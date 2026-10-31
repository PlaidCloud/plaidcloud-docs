---
title: データとサインイン中のユーザーの読み取り
description: サーバー側のPanelアプリを、閲覧しているユーザーとしてPlaidCloudに接続します。プロジェクトのデータを読み取り、閲覧者のIDをユーザーごとの動作や行レベルセキュリティに利用します。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/accessing-data.md
---

サーバーPanelアプリはPlaidCloudのデータを読み取れます。その際、**アプリを閲覧しているユーザーとして**読み取ります。誰かがアプリを開くと、PlaidCloudはプラットフォームの他の部分と同じシングルサインオンでそのユーザーをサインインさせ、アプリが行うすべての呼び出しは**その閲覧者自身の権限**で実行されます。共有のサービスアカウントはなく、閲覧者自身が見られないデータをアプリが見ることはありません。

これは**サーバー**アプリにのみ適用されます。WASMアプリはブラウザー内だけで動作し、サーバー側の接続を持ちません。

## PlaidCloudに接続する

読み取りたいデータを持つプロジェクトを指定して、`PlaidConnection`を使います。

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection(project_id="<your-project-id>")
```

必要な設定はこれだけです。トークン、ユーザー名、パスワードを指定する必要は**ありません**。接続は、サインイン中の閲覧者として自動的に認証されます。プロジェクトのIDは、プロジェクトのURLまたは設定ページで確認できます。

> **プロジェクトを指定してください。** **プロジェクト**ピッカーでプロジェクトを指定して公開したアプリは、デフォルトでそのプロジェクトを読み取り、[Data API](/ja/guides/panel-apps/data-api/)は`table("name")`にそのプロジェクトを使います。プロジェクトのないアプリでは、上記のように`PlaidConnection`に`project_id`を渡します。引数なしの`PlaidConnection()`には、読み取るプロジェクトがありません。

### テーブルを読み取る

接続を使って、名前でテーブルをpandas DataFrameに読み込みます。

```python
df = conn.get_dataframe("Sales Ledger")
```

接続は閲覧者として動作するため、閲覧者が見ることを許可されている行だけが返されます。閲覧者がプロジェクトにまったくアクセスできない場合は、権限エラーが発生します。

> **テーブルはSQLを書かず、名前で読み取ってください。** 管理者が[行アクセス](/ja/administration/access/managing-security-groups-and-assignments/#行アクセスと自分で作成するクエリ)を有効にしているプロジェクトでは、名前で読み取ると各閲覧者の行の許可が適用されます。一方、アプリ自身が組み立てたクエリは、プロジェクトのアーキテクトでないユーザーには拒否されます。許可によるフィルタリングの対象となる単一のテーブルがないためです。名前で読み取れば、どちらの場合でもアプリは動作し続けます。

## 閲覧者を識別する

**誰が見ているか**に合わせてアプリの表示を調整する場合（パーソナライズされたあいさつ、タブの非表示、行レベルセキュリティなど）は、Panelからサインイン中のユーザーを取得します。

```python
import panel as pn

viewer = pn.state.user          # the viewer's email address
token  = pn.state.access_token  # their JWT, if you need claims or group membership
```

`pn.state.user`は、検証済みのサインインから取得した閲覧者のメールアドレスで、そのユーザーのIDとして信頼できます。`pn.state.access_token`は閲覧者の生のアクセストークンで、より細かいルールのためにグループやロールのクレームをデコードする必要がある場合に役立ちます。

### 行レベルセキュリティ

この2つを組み合わせます。閲覧者を取得し、すべてのクエリをその閲覧者で絞り込みます。たとえば、各地域のマネージャーに自分の地域だけを表示するには次のようにします。

```python
import panel as pn
from plaidcloud.utilities.connect import PlaidConnection

pn.extension()

viewer = pn.state.user
conn = PlaidConnection(project_id="<your-project-id>")

sales = conn.get_dataframe("Regional Sales")
mine = sales[sales["manager_email"] == viewer]

pn.Column(
    f"# Sales for {viewer}",
    pn.pane.DataFrame(mine, index=False),
).servable()
```

接続はすでに閲覧者のプロジェクト権限を適用しているため、このフィルタリングは、閲覧が許可されている範囲に対する*追加の*絞り込みです。PlaidCloud自身のアクセス制御の代わりにはなりません。

> **データの呼び出しはアプリのメインフローから行ってください。** サインイン中の閲覧者は、そのセッションに対してアプリのコードが実行されている間（`.servable()`の処理が行われる場所）に利用できます。ブロッキング呼び出しをバックグラウンドスレッドに移す場合は、`asyncio.to_thread`を使ってください。素のスレッドプールではセッションのIDが引き継がれず、接続は誤ったデータを読み取るのではなく、明確にエラーとなります。

## 公開アプリ

**パブリックアクセスを許可**を有効にして公開した場合、アプリはサインインなしで配信されるため、代理となる閲覧者がいません。`pn.state.user`は空で、`PlaidConnection()`には認証する対象がありません。公開アプリは誰にとっても安全なデータだけに限定するか、パブリックアクセスをオフにして閲覧者がサインインするようにし、上記のユーザーごとのモデルを適用してください。
