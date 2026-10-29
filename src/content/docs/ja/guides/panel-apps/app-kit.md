---
title: Panelアプリキット
description: plaidcloud_panelキットを使用して、PlaidCloudらしい外観のPanelアプリを構築します。Appシェル、コマンドパレット、FilterBar、KpiCard、DataGrid、Chart、Form、実行ボタン、保存済み設定、印刷、翻訳を、ライトモードとダークモードで利用できます。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

すべてのサーバーPanelアプリには、`plaidcloud_panel` キットがインストールされています。このキットは、アプリにPlaidCloudの外観（プラットフォームのほかの部分と同じ色、書体、余白を、ライトモードとダークモードの両方で）を与えるとともに、多くのアプリで必要になる画面（フィルター、主要な数値、大規模なデータグリッド、チャート、フォーム）向けに、すぐに使えるコンポーネントを提供します。アプリは、[プロジェクトのブランディング](/ja/guides/panel-apps/branding/)を自動的に取り込みます。

```python
import plaidcloud_panel as pcp
```

キットをインポートすると、PlotlyとMatplotlibのチャートにもPlaidCloudの外観が適用されます。

## テンプレートから始める

キットには、動作するスターターアプリを書き出すコマンドが含まれています。任意のフォルダーから実行し、テーブル名と列名を編集してください。

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| オプション | 内容 |
|---|---|
| `--layout dashboard` | サイドバーにフィルター、2つの主要な数値、チャートを配置します。 |
| `--layout explorer` | サイドバーにフィルター、行数、行のテーブルを配置します。 |
| `--table` | アプリが読み取るPlaidCloudのテーブル。 |
| `--filters` | フィルターに使用する列のカンマ区切りリスト。最初の列がチャートを制御します。 |
| `--measure` | 合計する数値列。 |
| `--dir` | `app.py` と `requirements.txt` を書き出す場所。デフォルトは現在のフォルダーです。 |

`app.py` がすでに存在する場合、コマンドは何も書き込まずに停止します。2つのファイルをリポジトリにコミットし、[アプリを公開](/ja/guides/panel-apps/creating/)してください。

## アプリの例

このアプリは、売上テーブルを地域と年でフィルターし、2つの主要な数値、チャート、一致する行のページング付きグリッドを表示します。グリッドでは、金額が千の位の区切り付きで、利益率がパーセンテージで表示されます。すべての要素がフィルターに追従します。

```python
import panel as pn
import plaidcloud_panel as pcp
from bokeh.plotting import figure
from plaidcloud.utilities.panel_data import table

pn.extension("tabulator")

sales = table("sales")
bar = pcp.FilterBar(sales, "region", "year")


def by_region(t):
    df = t.aggregate(by=["region"], total=("amount", "sum"))
    regions = df["region"].astype(str).tolist()
    fig = figure(x_range=regions, height=320, toolbar_location=None)
    fig.vbar(x=regions, top=df["total"].astype(float).tolist(), width=0.8, color=pcp.series()[0])
    return fig


def grid(t):
    return pcp.DataGrid(t, key="id", totals={"amount": "sum"}, formats={"amount": "0,0", "margin": "0.0%"})


pcp.App(
    "Sales",
    sidebar=[bar],
    main=[
        pn.Row(
            pcp.KpiCard("Total amount", bar.table, "amount"),
            pcp.KpiCard("Orders", bar.table),
        ),
        pcp.Chart(pn.bind(by_region, bar.table), title="Amount by region"),
        pcp.Section("Orders", pn.bind(grid, bar.table)),
    ],
).servable()
```

パターンはどのキットアプリでも同じです。テーブルに対して `FilterBar` を構築し、各ビューを `bar.table` にバインドします。`bar.table`（またはウィジェット）にバインドされていないビューは、フィルターが変わっても更新されません。

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)` は、アプリシェルを構築します。シェルは、タイトル、プロジェクトのロゴ、サインイン中のユーザーを表示するヘッダー、サイドバー、メインエリアで構成されます。結果に対して `.servable()` を呼び出してください。

- **ナビゲーション** — `nav=[("Overview", overview_page), ("Detail", detail_page)]` を渡すと、サイドバーの上部にページメニューが表示されます。各ページは、Panelオブジェクト、またはそれを返す関数です。関数は、ページが選択されたときに実行されます。
- **テーマ** — アプリはライトテーマで開きます。ダークテーマで開くには `theme="dark"` を渡すか、URLに `?theme=dark` を追加します。`theme_toggle=True`（デフォルト）の場合、ヘッダーにライト/ダークの切り替えが表示されます。
- **ブランディング** — アプリは、セッションの開始時にプロジェクトのブランドカラーとロゴを読み取ります。ブランディングのないプロジェクトには、PlaidCloudのデフォルトが適用されます。
- **コマンドパレット** — Ctrl-K（MacではCmd-K）を押すと、コマンドを検索して実行できます。`nav` のすべてのページが「**移動**（ページ名）」の形で一覧に表示され、`commands={"Refresh data": refresh}` で独自のエントリを追加できます。各エントリは、ラベルと、引数を取らない関数です。エントリを選択すると、アプリがそれを実行します。
- **初回起動ツアー** — `tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]` は、短いステップバイステップの紹介を表示します。各ステップは見出しと1行のテキストで構成されます。ツアーは、完了またはスキップするまでページの上部に表示され、その後は再び表示されません。
- **その他** — ほかのキーワード引数は、Panelの `FastListTemplate` にそのまま渡されます。

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))` は、指定した列ごとに、検索可能な複数選択ボックスを1つ作成し、その列の個別の値を一覧表示します（最大1,000件で、一覧が切り詰められた場合は通知が表示されます）。何も選択されていないとき、ボックスには **すべて** と表示されます。そのほかの用途には、列名を指定して独自のウィジェットを渡します。

- `bar.table` は、現在の選択内容で絞り込まれたテーブルです。空のウィジェットは、データを絞り込みません。
- 選択内容はページのURL（`?region=EU`）に保存されるため、フィルター済みのビューをリンクとして共有できます。

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)` は、主要な数値を1つ表示します。`fn` は `sum`、`count`、`avg`、`min`、`max` のいずれかで、サーバーがテーブル全体に対して計算します。`column` を指定しない場合は、行数が表示されます。数値がフィルターに追従するように、ソースとして `bar.table` を渡してください。

`DataGrid` である `drill_to=grid` を渡すと、数値の下に **View rows** ボタンが追加されます。これを選択すると、グリッドがカード自身のテーブルを指すようになり、グリッドにはその数値の元になった行が一覧表示されます。

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})` は、あらゆるサイズのデータに対応するテーブルビューです。ブラウザーに送信されるのは現在のページだけで、ページング、並べ替え、合計、エクスポートはすべてサーバー上で実行されます。

- **ページング** — 1ページあたり200行、500行、1,000行から選択でき、前へ/次へのボタンと行カウンターがあります。
- **並べ替え** — 列ヘッダーをクリックします。並べ替えは、表示中のページだけでなく、テーブル全体に適用されます。
- **合計** — `totals` は、列を `sum`、`count`、`avg`、`min`、`max` のいずれかに対応付けます。サーバーが一致するすべての行に対してそれぞれを計算し、結果をグリッドの最終行に固定します。
- **エクスポート** — **CSV** ボタンと **XLSX** ボタンは、現在の並べ替え順で一致するすべての行を、`export_cap` 行（デフォルトは100,000）までダウンロードします。テーブルがそれより大きい場合は、フィルターを絞り込むよう通知が表示されます。`=`、`+`、`-`、`@` で始まるテキストセルには、スプレッドシートがテキストとして読み取るように、先頭にアポストロフィが付きます。
- **数値の書式** — `formats={"margin": "0.0%", "amount": "0,0"}` は、[numbro](https://numbrojs.com/format.html)の書式文字列を使用して、列ごとの表示形式を設定します。`%` 形式は100倍されます。合計行にも同じ書式が使用されます。書式のない浮動小数点列は、千の位の区切り付きで小数点以下2桁まで表示されます。**コピー**、**CSV**、**XLSX** は生の値を保持します。
- **キー** — `key` は、行を一意に識別する列、または列のリストです。必ず指定してください。[安定したページング](/ja/guides/panel-apps/data-api/#安定したページング)を参照してください。

- **グループ化** — `group_by=["region"]` は、グループごとに1行を表示します。各行には `totals` のメジャーと `rows` の件数があり、すべてサーバーで計算されます。さらに、一致するすべての行に対する **合計** 行があります。`groupable=["region", "year"]` を渡すと **グループ化** セレクターが追加され、閲覧者が列を選択できます。グリッドには最大1,000グループが表示され、一覧を切り詰めた場合は通知されます。グループ行には **開く** リンクがありません。
- **条件付き書式** — `rules` は、値に応じてセルに色を付けます。各ルールは、`column`、`op`（`>`、`>=`、`<`、`<=`、`==`、`!=`、`between` のいずれか）、`value`（`between` の場合は `[low, high]`）、`token`（`success`、`warning`、`error`、`info` のいずれか）を指定します。たとえば `{"column": "margin", "op": "<", "value": 0, "token": "error"}` のようになります。合計行には色が付きません。
- **コピー** — **コピー** ボタンは、表示中の列と合計行を含む現在のページを、Excelに貼り付けられるタブ区切りのテキストとしてクリップボードに入れます。
- **Open in PlaidCloud** — ソースがPlaidCloudのテーブルの場合、**Open in PlaidCloud** リンクでそのテーブルが開きます。
- **保存済みの列レイアウト** — `layout_key="orders"` を指定すると、列の選択と並べ替え、および一部の列の固定のために、**列** セレクターと **Pinned** セレクターが追加されます。各閲覧者の選択はその名前で保存され、次回アプリを開いたときに復元されます。
- **行リンク** — `row_link` は、行を辞書として受け取り、Webアドレスを返す関数です。リンクがない場合は `None` を返します。グリッドには **開く** 列が追加され、リンクのある各行にリンクが表示されます。リンクされるのは、`http` と `https` のアドレス、および同じサイト内のパスだけです。
- **更新** — `grid.refresh()` は、同じソースに再度クエリを実行し、ページ、並べ替え、グループ化を維持します。[実行](#実行ボタンと鮮度)がテーブルへの書き込みを終えた後に呼び出してください。

`source` は、テーブル名、または[データAPI](/ja/guides/panel-apps/data-api/)のテーブルです。グリッドを再度フィルターするには、`grid.source` にフィルター済みのテーブルを設定するか、例のように `bar.table` から新しいグリッドを構築します。

グリッドは、閲覧者の行レベルセキュリティの対象です。閲覧者自身の接続を通じて読み取ります。

## Chart

`pcp.Chart(obj, title=None, height=320)` は、タイトル付きのカードにチャートを配置します。`obj` には、Bokehのフィギュア、hvPlotまたはHoloViewsのプロット、Plotlyのフィギュア、Matplotlibのフィギュア、あるいはそれらのいずれかを返す `pn.bind(...)` を指定できます。Bokehのフィギュアの数値軸には千の位の区切りが表示されるため、800000は800,000と表示されます。

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")` は、入力ウィジェットを送信ボタン付きの1つのフォームとして配置します。`form.values()` は、名前のあるすべてのウィジェットについて `{widget.name: widget.value}` を返し、`on_submit` は、ボタンがクリックされたときにその辞書を受け取ります。

## Section、Card、Tabs、Loading

| コンポーネント | 用途 |
|---|---|
| `pcp.Section(title, *objects)` | ページの背景上に直接配置する、タイトル付きのグループ。 |
| `pcp.Card(title, *objects)` | 浮き上がった面に配置する、タイトル付きのグループ。 |
| `pcp.Tabs(Overview=obj, Detail=obj)` | タブが選択されたときにそのタブの内容を読み込むタブ。アクティブなタブにはブランドカラーが使われます。 |
| `pcp.Loading(height=200)` | データの読み込み中に表示する、きらめくプレースホルダー。 |

## StatusBanner

`pcp.StatusBanner(message, kind="info")` は、インラインの通知を表示します。`kind` は `error`、`warning`、`success`、`info` のいずれかです。

## 実行ボタンと鮮度

`pcp.run_workflow_button(workflow_id, label=None)` は、アプリを開いた本人としてPlaidCloudのワークフローを実行するボタンを追加し、**実行中…**、続いて **完了** または **失敗** と表示します。失敗した場合は、失敗したステップが最大5つまで表示されます。`project_id` を渡さない限り、ワークフローはアプリのプロジェクトに属します。

`pcp.RunButton(label, start, status)` は、任意のジョブに対して同じことを行います。`start` はジョブを起動して実行IDを返し、`status(run_id)` は `"running"`、`"succeeded"`、`"failed"` のいずれか、または理由を表示する `("failed", reason)` を返します。どちらもREST APIの呼び出しなどの通常の関数です。ボタンの `runs` の値は、実行が成功するたびに1ずつ増えるため、その後に更新が必要なビューは、それにバインドします。

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)` は、テーブルが最後に書き込まれた時刻を **Updated 5 min ago** のように表示します。経過時間は、ページを開いたままでも更新されます。`stale_after=datetime.timedelta(hours=24)` を渡すと、それより古いデータが警告付きで示されます。実行後には `.refresh()` を呼び出してください。日時を特定できないテーブルには **Last update unknown** と表示されます。これはエラーではありません。`pcp.Freshness(fetch)` は任意のソースに対して同じことを行い、`fetch` はデータが最後に変更された時刻を返します。

## 保存済み設定

`pcp.user_state` は、訪問のたびに各ユーザーの選択内容を記憶するため、アプリは前回終了したときの状態で開きます。

- `pcp.user_state.persist(widget, "region")` は、保存された値をウィジェットに復元し、変更のたびに保存します。ウィジェットが提供しなくなった保存済みの値は無視されます。
- `nav` で選択したページは自動的に保存されます。
- `pcp.user_state.persist(widget, "filters.region")` のように、`filters.` で始まるキーはフィルターの選択内容を保持します。PlaidCloudは、読み取るたびにそれをそのユーザーの現在の行アクセスに合わせて絞り込むため、保存済みのフィルターが、ユーザーにもう見えない値を復活させることはありません。
- `pcp.user_state.get(key, default)` と `pcp.user_state.set(key, value)` は、そのほかの小さな値を保存します。

保存済みの設定は、1つのアプリ内の1人のユーザーに属し、最大8 KBです。設定が人の間で共有されることはありません。設定の保存時にPlaidCloudに接続できない場合、アプリはセッションが終了するまでそれを保持します。

## 印刷とPDFとして保存

`pcp.PrintButton()` はブラウザーの印刷ダイアログを開き、出力先として **PDFとして保存** を選択できます。ページは、サイドバーとコントロールを非表示にし、プロジェクトのブランドを適用した状態で印刷されます。各 `DataGrid` は、現在のページ全体を最大1,000行まで印刷し、最後に合計行を表示します。ダークモードのアプリは、ライトのパレットで印刷されます。

## 言語

ボタン、通知、コマンドパレット、ツアー、実行と鮮度のメッセージ、グリッドのフッターなど、キット自体のテキストは、英語、ドイツ語、フランス語で表示されます。言語は、ページのアドレスの `?lang=de` または `?lang=fr` で指定し、指定がない場合はブラウザーの言語になります。数値には、その言語の区切り文字が使用されます。データ、列名、および独自に記述したラベルが翻訳されることはありません。

## パフォーマンスバジェット

最初の描画に3,000 msを超える時間がかかるページの読み込み、または2,000 msより遅いクエリを実行するページの読み込みでは、超過した内容を示す警告がアプリのログに書き込まれます。同じ数値は、[Panel Studio](/ja/guides/panel-apps/studio/#インサイト)の **インサイト** タブにも表示されます。アプリに別の上限を設定するには、次の環境変数を設定します。

| 変数 | デフォルト | 設定内容 |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | 最初の描画までのミリ秒。 |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | 1回のクエリのミリ秒。 |

整数でない値は無視され、デフォルトが適用されます。

## 独自のチャート用の色

`pcp.series()` は、PlaidCloudのチャートパレットを、順序付きの色のリストとして返します。例の棒グラフのように、独自に描画するチャートをキット自体のコンポーネントと揃えるために使用してください。

## 次のステップ

- [データAPI](/ja/guides/panel-apps/data-api/) — アプリからPlaidCloudのテーブルをフィルター、ページング、件数取得、集計します。
- [アラートとダイジェスト](/ja/guides/panel-apps/alerts-and-digests/) — アプリからKPIアラートと定期的なサマリーを送信します。
- [プロジェクトのブランディング](/ja/guides/panel-apps/branding/) — プロジェクト内のすべてのアプリに対して、色とロゴを一度だけ設定します。
