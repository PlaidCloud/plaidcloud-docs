---
title: Panelアプリ向けデータAPI
description: panel_data を使用して Panel アプリから PlaidCloud のテーブルを読み取ります。フィルター、ページング、件数取得、集計をサーバー側で、ログイン中の閲覧者として実行し、行レベルセキュリティも適用されます。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/data-api.md
---

`plaidcloud.utilities.panel_data` は、サーバー型の Panel アプリがテーブル全体をアプリに読み込まずに読み取るための方法です。必要な内容（一部のフィルターに一致する行、そのうちの1ページ、件数、グループ化した合計）を指定すると、PlaidCloud のデータベースが処理を行います。アプリに返されるのは結果だけです。

すべてのリクエストはアプリを表示しているユーザーとして実行されるため、そのユーザーのプロジェクト権限と[行レベルセキュリティ](/ja/guides/panel-apps/accessing-data/)が、返されるすべてのデータに適用されます。

```python
from plaidcloud.utilities.panel_data import table

sales = table("sales")
```

`table(name)` は、アプリのプロジェクトにあるテーブルを開きます。アプリのプロジェクトとは、アプリを公開したときに[割り当てられた](/ja/guides/panel-apps/branding/#アプリをプロジェクトに割り当てる)プロジェクトです。別のプロジェクトのテーブルを読み取るには、`table("sales", project="Finance")` のようにプロジェクトを渡します。プロジェクトには ID、名前、パスのいずれかを指定できます。

テーブルハンドルは変更されません。`filter` は新しいハンドルを返すため、フィルターなしのハンドルを残したまま、そこから複数のビューを派生させることができます。

## フィルター

```python
emea = sales.filter(region="EMEA", year=[2025, 2026])
```

各キーワードは列名です。単一の値を指定すると、その値と等しい行に一致します。リスト、タプル、セットを指定すると、いずれかの要素と等しい行に一致します。複数のキーワードは AND で結合され、結果に対して `filter` を再度呼び出すと条件が追加されます。

値が `None`、空文字列、空のリストの場合、その列はフィルターされません。これにより、空のフィルターウィジェットがデータに影響しなくなります。空かどうかを確認しなくても、`sales.filter(**widget_values)` がそのまま動作します。

存在しない列を指定すると、テーブル名と列名を示すエラーが発生します。

## ページ

```python
rows = emea.page(1, 200, sort=["-amount"], key="id")
```

`page(n, size, sort, key)` は、`size` 行ずつに区切った `n` ページ目（1から数えます）を pandas データフレームとして返します。

- `sort` は列名のリストです。名前の先頭に `-` を付けると降順になります（`["region", "-amount"]`）。
- `key` は、テーブルの一意の列、または一意の列のリストです。必ず指定してください。

### 安定したページング

ページングでは、順序付けられた行のリストから一部を切り出します。各リクエストは別々のクエリです。2つの行がソート列で同順位の場合、データベースは次のリクエストで異なる順序で返すことがあり、その結果、ある行が2つのスライスに現れたり、どちらにも現れなかったりします。`key` がこの問題を解消します。PlaidCloud はソート列の後ろに key を追加するため、順序が常に完全に決まり、すべての行がちょうど1つのスライスに含まれます。

`key` がない場合、ページングはすべての列による並べ替えにフォールバックします。列数の多いテーブルでは遅くなり、2つの行がまったく同じ場合は依然として不安定です。ページングするときは必ず一意の key を渡してください。同じ理由で、[`DataGrid`](/ja/guides/panel-apps/app-kit/#datagrid) にも渡します。

## 件数

```python
total_rows = emea.count()
```

フィルターに一致する行数を整数で返します。

## 集計

```python
by_region = sales.aggregate(by=["region"], total=("amount", "sum"), orders=("id", "count"))
grand_total = emea.aggregate(total=("amount", "sum"))
```

`aggregate(by=(), limit=1000, **measures)` は、グループごとに1行のデータフレームを `by` の列順で返します。各メジャーは `name=(column, function)` の形式で、function には `sum`、`count`、`avg`、`min`、`max` のいずれかを指定します。メジャーは少なくとも1つ必要です。

`by` を指定しない場合は、フィルター後の行全体の合計が1行で返されます。`limit` は返されるグループ数の上限です。

小数列は文字列として届くことがあります。チャートの作成や書式設定の前に、`float(...)` または `astype(float)` で変換してください。

## まとめ

```python
import panel as pn
import plaidcloud_panel as pcp
from plaidcloud.utilities.panel_data import table

pn.extension("tabulator")

orders = table("orders")
bar = pcp.FilterBar(orders, "status")

pcp.App(
    "Orders",
    sidebar=[bar],
    main=[
        pcp.KpiCard("Open value", bar.table, "amount"),
        pn.bind(lambda t: pcp.DataGrid(t, key="order_id"), bar.table),
    ],
).servable()
```

`FilterBar`、`KpiCard`、`DataGrid` はいずれもこれらのテーブルハンドルを受け取るため、ほとんどのアプリでは `page`、`count`、`aggregate` を直接呼び出す必要はありません。独自のビューを作成する場合に使用してください。[Panelアプリキット](/ja/guides/panel-apps/app-kit/)を参照してください。

## 関連項目

- [データとログイン中ユーザーの読み取り](/ja/guides/panel-apps/accessing-data/) — 閲覧者として接続する方法と、`PlaidConnection` を直接使用する場合。
