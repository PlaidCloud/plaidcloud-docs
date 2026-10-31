---
title: Panelアプリキット
description: plaidcloud_panelキットを使って、PlaidCloudと同じ外観のPanelアプリを作成します。Appシェル、コマンドパレット、FilterBar、KpiCard、DataGrid、Chart、Form、実行ボタン、保存済み設定、印刷、翻訳に対応し、ライトテーマとダークテーマの両方で利用できます。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

すべてのサーバーPanelアプリには`plaidcloud_panel`キットがインストールされています。このキットにより、アプリはライトテーマとダークテーマの両方で、プラットフォームの他の部分と同じ色、書体、余白というPlaidCloudの外観になります。また、フィルター、見出しの数値、大規模なデータグリッド、チャート、フォームなど、多くのアプリで必要になる画面向けの既製コンポーネントも利用できます。アプリは[プロジェクトのブランディング](/ja/guides/panel-apps/branding/)を自動的に取り込みます。

```python
import plaidcloud_panel as pcp
```

キットをインポートすると、PlotlyとMatplotlibのチャートにもPlaidCloudの外観が適用されます。

## テンプレートから開始する

[Panel Studio](/ja/guides/panel-apps/studio/)では、**新しい Studio アプリ**から、空のアプリ、テーブルまたはビュー、別のStudioアプリ、[ギャラリー](/ja/guides/panel-apps/gallery/)のアプリのいずれかを元に開始できます。実行するコマンドはありません。

gitリポジトリで管理するアプリ向けに、キットには動作するスターターアプリを書き出すコマンドが含まれています。任意のフォルダーから実行し、テーブル名と列名を編集してください。

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| オプション | 内容 |
|---|---|
| `--layout dashboard` | サイドバーにフィルター、2つの見出し数値、チャートを配置します。 |
| `--layout explorer` | サイドバーにフィルター、行数、行のテーブルを配置します。 |
| `--table` | アプリが読み取るPlaidCloudのテーブルです。 |
| `--filters` | フィルター対象の列をカンマ区切りで指定します。最初の列がチャートの軸になります。 |
| `--measure` | 合計する数値列です。 |
| `--dir` | `app.py`と`requirements.txt`の書き込み先です。デフォルトは現在のフォルダーです。 |

`app.py`がすでに存在する場合、コマンドは何も書き込まずに停止します。2つのファイルをリポジトリにコミットし、[サーバーアプリとして公開](/ja/guides/panel-apps/creating/#サーバーアプリの作成)します。

## アプリの例

このアプリは、売上テーブルを地域と年でフィルターし、2つの見出し数値、チャート、条件に一致する行のページング付きグリッドを表示します。グリッドでは、金額を桁区切り付きで、マージンをパーセントで表示します。すべての要素がフィルターに追従します。

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

パターンはどのキットアプリでも同じです。テーブルに対して`FilterBar`を作成し、各ビューを`bar.table`にバインドします。`bar.table`（またはウィジェット）にバインドされていないビューは、フィルターが変わっても更新されません。

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)`は、アプリシェルを作成します。シェルには、タイトル、プロジェクトのロゴ、サインイン中のユーザーを表示するヘッダー、サイドバー、メインエリアが含まれます。結果に対して`.servable()`を呼び出します。

- **ナビゲーション** — `nav=[("Overview", overview_page), ("Detail", detail_page)]`を渡すと、サイドバーの上部にページメニューが表示されます。各ページは、Panelオブジェクト、またはそれを返す関数です。関数はページが選択されたときに実行されます。
- **テーマ** — アプリはライトテーマで開きます。ダークテーマで開くには`theme="dark"`を渡すか、URLに`?theme=dark`を追加します。`theme_toggle=True`（デフォルト）の場合、ヘッダーにライト/ダークの切り替えが表示されます。
- **ブランディング** — アプリは、セッションの開始時にプロジェクトのブランドカラーとロゴを読み取ります。ブランディングのないプロジェクトには、PlaidCloudのデフォルトが適用されます。
- **コマンドパレット** — Ctrl-K（MacではCmd-K）を押すと、コマンドを検索して実行できます。`nav`のすべてのページが「**移動** ページ名」として一覧に表示されます。`commands={"Refresh data": refresh}`で独自の項目を追加できます。各項目はラベルと、引数を取らない関数です。項目を選ぶと、アプリがそれを実行します。
- **初回ツアー** — `tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]`を指定すると、短いステップ形式の紹介が表示されます。各ステップは見出しと1行のテキストです。完了またはスキップするまでページの上部に表示され、その後は再表示されません。
- **その他** — その他のキーワード引数は、Panelの`FastListTemplate`にそのまま渡されます。

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))`は、指定した列ごとに、検索可能な複数選択ボックスを1つ作成し、その列の個別の値を一覧表示します（最大1,000件で、一覧が切り詰められた場合は通知が表示されます）。何も選択されていない場合、ボックスには**すべて**と表示されます。それ以外のものには、列名を指定して独自のウィジェットを渡します。

- `bar.table`は、現在の選択内容で絞り込まれたテーブルです。空のウィジェットはデータを絞り込みません。
- 選択内容はページのURL（`?region=EU`）に保存されるため、フィルター済みのビューをリンクとして共有できます。

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)`は、見出しとなる数値を1つ表示します。`fn`は`sum`、`count`、`avg`、`min`、`max`のいずれかで、テーブル全体に対してサーバーが計算します。`column`を指定しない場合は、行数が表示されます。数値がフィルターに追従するように、ソースには`bar.table`を渡します。

`drill_to=grid`として`DataGrid`を渡すと、数値の下に**View rows**ボタンが追加されます。これを選ぶと、グリッドがカード自身のテーブルを参照するようになり、数値の元になっている行が一覧表示されます。

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})`は、あらゆる規模のデータに対応するテーブルビューです。ブラウザーに送信されるのは現在のページだけで、ページング、並べ替え、合計、エクスポートはすべてサーバーで実行されます。

- **ページング** — 1ページあたり200行、500行、1,000行から選べます。前へ・次へのボタンと行カウンターがあります。
- **並べ替え** — 列ヘッダーをクリックします。並べ替えは、表示中のページだけでなくテーブル全体に適用されます。
- **合計** — `totals`は、列を`sum`、`count`、`avg`、`min`、`max`のいずれかに対応付けます。サーバーが一致するすべての行に対してそれぞれを計算し、結果をグリッドの最終行に固定します。
- **エクスポート** — **CSV**ボタンと**XLSX**ボタンは、現在の並び順で一致するすべての行を、最大`export_cap`行（デフォルトは100,000行）までダウンロードします。テーブルがそれより大きい場合は、フィルターを絞り込むよう通知が表示されます。`=`、`+`、`-`、`@`で始まるテキストセルには、スプレッドシートがテキストとして読み取るように先頭にアポストロフィが付きます。
- **数値形式** — `formats={"margin": "0.0%", "amount": "0,0"}`は、[numbro](https://numbrojs.com/format.html)の書式文字列を使って、列ごとの表示形式を設定します。`%`形式は100倍されます。合計行にも同じ形式が使われます。形式を指定していない浮動小数点の列は、桁区切り付きで小数点以下2桁まで表示されます。**コピー**、**CSV**、**XLSX**では元の値が保持されます。
- **キー** — `key`は、行を一意に識別する列（または列のリスト）です。必ず指定してください。[安定したページング](/ja/guides/panel-apps/data-api/#安定したページング)を参照してください。

- **グループ化** — `group_by=["region"]`を指定すると、グループごとに1行が表示されます。`totals`の集計値と`rows`の件数はすべてサーバーが計算し、一致するすべての行に対する**合計**行も表示されます。`groupable=["region", "year"]`を渡すと**グループ化**セレクターが追加され、閲覧者が列を選べるようになります。グリッドには最大1,000グループが表示され、一覧が切り詰められた場合は通知されます。グループ行には**開く**リンクがありません。
- **条件付き書式** — `rules`は、値に応じてセルに色を付けます。各ルールは、`column`、`op`（`>`、`>=`、`<`、`<=`、`==`、`!=`、`between`）、`value`（`between`の場合は`[low, high]`）、`token`（`success`、`warning`、`error`、`info`）を指定します。たとえば`{"column": "margin", "op": "<", "value": 0, "token": "error"}`です。合計行に色が付くことはありません。
- **コピー** — **コピー**ボタンは、表示中の列と合計行を含む現在のページを、Excelに貼り付けられるタブ区切りテキストとしてクリップボードに置きます。
- **Open in PlaidCloud** — ソースがPlaidCloudのテーブルの場合、**Open in PlaidCloud**リンクでそのテーブルが開きます。
- **保存済みの列レイアウト** — `layout_key="orders"`を指定すると、列の選択と並べ替え、一部の列の固定を行う**列**セレクターと**Pinned**セレクターが追加されます。各閲覧者の選択はその名前で保存され、次回アプリを開いたときに復元されます。
- **行リンク** — `row_link`は、行を辞書として受け取り、Webアドレスを返す関数です。リンクがない場合は`None`を返します。グリッドには**開く**列が追加され、リンクがある各行にリンクが表示されます。リンクされるのは、`http`と`https`のアドレスと、同じサイト内のパスだけです。
- **更新** — `grid.refresh()`は、同じソースを再度クエリし、ページ、並べ替え、グループ化を維持します。[実行](#実行ボタンと鮮度)がテーブルへの書き込みを終えたら呼び出します。

`source`は、テーブル名、または[Data API](/ja/guides/panel-apps/data-api/)のテーブルです。グリッドを再フィルターするには、`grid.source`にフィルター済みのテーブルを設定するか、例のように`bar.table`から新しいグリッドを作成します。

グリッドは閲覧者の行レベルセキュリティの対象です。閲覧者自身の接続を通じてデータを読み取ります。

## Chart

`pcp.Chart(obj, title=None, height=320)`は、タイトル付きのカードにチャートを配置します。`obj`には、Bokehのfigure、hvPlotまたはHoloViewsのプロット、Plotlyのfigure、Matplotlibのfigure、またはそれらのいずれかを返す`pn.bind(...)`を指定できます。Bokehのfigureの数値軸には桁区切りが表示されるため、800000は800,000と読めます。

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")`は、入力ウィジェットを送信ボタン付きの1つのフォームとして配置します。`form.values()`は、名前の付いたすべてのウィジェットについて`{widget.name: widget.value}`を返し、ボタンがクリックされると`on_submit`がその辞書を受け取ります。

## Section、Card、Tabs、Loading

| コンポーネント | 用途 |
|---|---|
| `pcp.Section(title, *objects)` | ページの背景に直接置く、タイトル付きのグループです。 |
| `pcp.Card(title, *objects)` | 浮き上がった面に置く、タイトル付きのグループです。 |
| `pcp.Tabs(Overview=obj, Detail=obj)` | タブが選択されたときにその内容を読み込むタブです。アクティブなタブにはブランドカラーが使われます。 |
| `pcp.Loading(height=200)` | データの読み込み中に表示する、きらめくプレースホルダーです。 |

## StatusBanner

`pcp.StatusBanner(message, kind="info")`は、インライン通知を表示します。`kind`は`error`、`warning`、`success`、`info`のいずれかです。

## 実行ボタンと鮮度

`pcp.run_workflow_button(workflow_id, label=None)`は、アプリを開いた本人としてPlaidCloudのワークフローを実行するボタンを追加します。ボタンは**実行中…**、続いて**完了**または**失敗**と表示します。失敗した場合は、失敗したステップの名前が最大5件まで示されます。`project_id`を渡さない限り、ワークフローはアプリのプロジェクトに属します。

`pcp.RunButton(label, start, status)`は、任意のジョブに対して同じ動作をします。`start`はジョブを起動して実行IDを返します。`status(run_id)`は`"running"`、`"succeeded"`、`"failed"`のいずれか、または理由を表示するための`("failed", reason)`を返します。どちらもREST APIの呼び出しなどの通常の関数です。ボタンの`runs`値は実行が成功するたびに1ずつ増えるため、その後に更新が必要なビューはこれにバインドします。

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)`は、テーブルが最後に書き込まれた時刻を**Updated 5 min ago**のように表示します。ページを開いている間も経過時間は進みます。`stale_after=datetime.timedelta(hours=24)`を渡すと、それより古いデータが警告付きで示されます。実行後は`.refresh()`を呼び出します。日時を特定できないテーブルには**Last update unknown**と表示されますが、これがエラーになることはありません。`pcp.Freshness(fetch)`は任意のソースに対して同じ動作をし、`fetch`はデータが最後に変更された時刻を返します。

## 保存済み設定

`pcp.user_state`は、各ユーザーの選択を訪問をまたいで記憶するため、アプリは前回終了したときの状態で開きます。

- `pcp.user_state.persist(widget, "region")`は、保存された値をウィジェットに復元し、変更のたびに保存します。ウィジェットがもう提供していない保存済みの値は無視されます。
- `nav`で選択したページは自動的に保存されます。
- `filters.`で始まるキー（たとえば`pcp.user_state.persist(widget, "filters.region")`）は、フィルターの選択を保持します。PlaidCloudは、読み取るたびにこれをユーザーの現在の行アクセスに合わせて絞り込むため、保存済みのフィルターによって、ユーザーが見られなくなった値が再び表示されることはありません。
- `pcp.user_state.get(key, default)`と`pcp.user_state.set(key, value)`は、その他の小さな値を保存します。

保存済み設定は、1人のユーザーの1つのアプリに属し、上限は8 KBです。設定がユーザー間で共有されることはありません。設定の保存時にPlaidCloudに接続できない場合、アプリはセッションが終了するまでそれを保持します。

## 印刷とPDFとして保存

`pcp.PrintButton()`はブラウザーの印刷ダイアログを開き、送信先として**PDFとして保存**を選べます。ページは、サイドバーとコントロールを非表示にし、プロジェクトのブランドを適用して印刷されます。各`DataGrid`は、現在のページ全体を最大1,000行まで、合計行を最後にして印刷します。ダークテーマのアプリは、ライトのカラーパレットで印刷されます。

## 言語

ボタン、通知、コマンドパレット、ツアー、実行や鮮度のメッセージ、グリッドのフッターなど、キット自体のテキストは、英語、ドイツ語、フランス語で表示されます。言語はページアドレスの`?lang=de`または`?lang=fr`で指定し、指定がない場合はブラウザーの言語になります。数値には、その言語の区切り文字が使われます。データ、列名、ユーザーが書いたラベルが翻訳されることはありません。

## パフォーマンス予算

最初の描画に3,000 ミリ秒を超える、または2,000 ミリ秒より遅いクエリを実行するページ読み込みでは、超過した項目を示す警告がアプリのログに書き込まれます。同じ数値は、[Panel Studio](/ja/guides/panel-apps/studio/#インサイト)の**インサイト**タブにも表示されます。アプリに別の上限を設定するには、次の環境変数を設定します。

| 変数 | デフォルト | 設定内容 |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | 最初の描画までのミリ秒数です。 |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | 1回のクエリのミリ秒数です。 |

整数でない値は無視され、デフォルトが適用されます。

## 独自のチャート用の色

`pcp.series()`は、PlaidCloudのチャートパレットを色のリストとして順番に返します。例の棒グラフのように、自分で描画するチャートをキット自体のコンポーネントと揃えたい場合に使います。

## 次のステップ

- [Data API](/ja/guides/panel-apps/data-api/) — アプリからPlaidCloudのテーブルをフィルター、ページング、カウント、集計します。
- [アラートとダイジェスト](/ja/guides/panel-apps/alerts-and-digests/) — アプリからKPIアラートと定期サマリーを送信します。
- [プロジェクトのブランディング](/ja/guides/panel-apps/branding/) — プロジェクト内のすべてのアプリに適用する色とロゴを一度に設定します。
