---
title: Panelアプリキット
description: plaidcloud_panelキットで、PlaidCloudのような見た目のPanelアプリを構築します。Appシェル、コマンドパレット、FilterBar、KpiCard、DataGrid、Chart、Form、実行ボタン、保存された設定、印刷、翻訳を、ライトとダークの両方で扱います。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

すべてのサーバーPanelアプリには、`plaidcloud_panel`キットがインストールされています。このキットは、ライトとダークの両方で、プラットフォームの他の部分と同じ色、書体、余白というPlaidCloudの外観をアプリに与え、フィルター、主要な数値、大規模なデータグリッド、チャート、フォームなど、ほとんどのアプリで必要な画面向けのコンポーネントを提供します。アプリは、[プロジェクトのブランディング](/ja/guides/panel-apps/branding/)を自動的に取得します。

```python
import plaidcloud_panel as pcp
```

キットをインポートすると、PlotlyとMatplotlibのチャートにもPlaidCloudの外観が適用されます。

## テンプレートから始める

[Panel Studio](/ja/guides/panel-apps/studio/)では、**新規アプリ** > **Studio**から、空のアプリ、テーブルまたはビュー、別のStudioアプリ、[ギャラリー](/ja/guides/panel-apps/gallery/)のアプリのいずれかから、コマンドを実行することなく開始できます。

gitリポジトリで管理するアプリ向けに、キットには、動作するスターターアプリを書き出すコマンドが含まれています。任意のフォルダーから実行し、テーブル名と列名を編集してください。

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| オプション | 内容 |
|---|---|
| `--layout dashboard` | サイドバーにフィルター、2つの主要な数値、チャート。 |
| `--layout explorer` | サイドバーにフィルター、行数、行のテーブル。 |
| `--table` | アプリが読み取るPlaidCloudのテーブル。 |
| `--filters` | フィルターに使用する列のカンマ区切りリスト。最初の列がチャートを制御します。 |
| `--measure` | 合計する数値の列。 |
| `--dir` | `app.py`と`requirements.txt`の書き込み先。デフォルトは現在のフォルダーです。 |

`app.py`がすでに存在する場合、コマンドは何も書き込まずに停止します。2つのファイルをリポジトリにコミットし、[サーバーアプリとして公開](/ja/guides/panel-apps/creating/#サーバーアプリの作成)します。

## アプリの例

このアプリは、販売テーブルを地域と年でフィルターし、2つの主要な数値、チャート、一致する行のページ分割されたグリッドを表示します。グリッドでは、金額が桁区切り付きで、利益率がパーセントで表示されます。すべての要素がフィルターに追従します。

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

パターンは、キットのどのアプリでも同じです。テーブルに対して`FilterBar`を作成し、各ビューを`bar.table`にバインドします。`bar.table`（またはウィジェット）にバインドされていないビューは、フィルターが変わっても更新されません。

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)`は、アプリのシェルを構築します。タイトル、プロジェクトのロゴ、サインイン中のユーザーを表示するヘッダー、サイドバー、メインエリアで構成されます。結果に対して`.servable()`を呼び出します。

- **ナビゲーション** — `nav=[("Overview", overview_page), ("Detail", detail_page)]`を渡すと、サイドバーの上部にページメニューが表示されます。各ページは、Panelオブジェクト、またはそれを返す関数です。関数は、ページが選択されたときに実行されます。
- **テーマ** — アプリはライトテーマで開きます。ダークテーマで開くには`theme="dark"`を渡すか、URLに`?theme=dark`を追加します。`theme_toggle=True`（デフォルト）の場合、ヘッダーにライト/ダークの切り替えスイッチが表示されます。
- **ブランディング** — アプリは、セッションの開始時に、プロジェクトのブランドカラーとロゴを読み取ります。ブランディングのないプロジェクトには、PlaidCloudのデフォルトが適用されます。
- **コマンドパレット** — Ctrl-K（MacではCmd-K）を押すと、コマンドを検索して実行できます。`nav`のすべてのページが、ページ名の**移動**として一覧表示され、`commands={"Refresh data": refresh}`で独自のエントリを追加できます。各エントリは、ラベルと、引数を取らない関数で構成されます。エントリを選択すると、アプリがそれを実行します。
- **初回起動のツアー** — `tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]`は、見出しとテキスト1行で構成される各ステップによる、短いステップごとの紹介を表示します。完了またはスキップするまでページの上部に表示され、その後は再表示されません。
- **その他** — その他のキーワード引数は、Panelの`FastListTemplate`にそのまま渡されます。

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))`は、指定した列ごとに、検索可能な複数選択ボックスを1つ作成し、その列の個別の値（最大1,000件。リストが切り捨てられた場合は通知されます）を一覧表示します。何も選択されていない場合、ボックスには**すべて**と表示されます。その他のものには、列名で独自のウィジェットを渡します。

- `bar.table`は、現在の選択によって絞り込まれたテーブルです。空のウィジェットは、データを絞り込みません。
- 選択内容はページのURL（`?region=EU`）に保存されるため、フィルターされたビューをリンクとして共有できます。

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)`は、主要な数値を1つ表示します。`fn`は`sum`、`count`、`avg`、`min`、`max`のいずれかで、サーバーがテーブル全体に対して計算します。`column`がない場合は、行数が表示されます。数値がフィルターに追従するように、ソースとして`bar.table`を渡します。

`drill_to=grid`（`DataGrid`）を渡すと、数値の下に**View rows**ボタンが追加されます。これを選択すると、グリッドがカード自身のテーブルを参照するようになり、その数値の元になっている行が一覧表示されます。

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})`は、あらゆるサイズのデータに対応するテーブルビューです。現在のページのみがブラウザーに送信され、ページ送り、並べ替え、合計、エクスポートはすべてサーバーで実行されます。

- **ページ送り** — 1ページあたり200、500、または1,000行で、PreviousとNextのボタンと行カウンターがあります。
- **並べ替え** — 列ヘッダーをクリックします。並べ替えは、表示されているページだけでなく、テーブル全体に適用されます。
- **合計** — `totals`は、列を`sum`、`count`、`avg`、`min`、`max`に対応付けます。サーバーが、一致するすべての行に対してそれぞれを計算し、結果をグリッドの最後の行として固定します。
- **エクスポート** — **CSV**と**XLSX**ボタンは、一致するすべての行を、現在の並べ替え順で、`export_cap`行（デフォルトは100,000行）までダウンロードします。テーブルがそれより大きい場合は、フィルターを絞り込むよう通知されます。`=`、`+`、`-`、`@`で始まるテキストセルには、スプレッドシートがテキストとして読み取るように、アポストロフィが前に付けられます。
- **数値の書式** — `formats={"margin": "0.0%", "amount": "0,0"}`は、[numbro](https://numbrojs.com/format.html)の書式文字列を使用して、列ごとの表示形式を設定します。`%`の書式は100倍されます。合計行にも同じ書式が使用されます。書式のない浮動小数点の列は、桁区切り付きで小数点以下2桁まで表示されます。**コピー**、**CSV**、**XLSX**は、元の値を保持します。
- **キー** — `key`は、行を一意に識別する列（または列のリスト）です。必ず指定してください。[安定したページ送り](/ja/guides/panel-apps/data-api/#安定したページング)を参照してください。

- **グループ化** — `group_by=["region"]`は、グループごとに1行を、`totals`のメジャーと`rows`の件数（いずれもサーバーが計算）とともに表示し、一致するすべての行に対する**合計**行も表示します。`groupable=["region", "year"]`を渡すと、閲覧者が列を選択できる**グループ化**セレクターが追加されます。グリッドには最大1,000のグループが表示され、リストが切り捨てられた場合は通知されます。グループ行には**開く**リンクはありません。
- **条件付き書式** — `rules`は、値に応じてセルに色を付けます。各ルールは、`column`、`op`（`>`、`>=`、`<`、`<=`、`==`、`!=`、`between`）、`value`（`between`の場合は`[low, high]`）、`token`（`success`、`warning`、`error`、`info`）を指定します。たとえば、`{"column": "margin", "op": "<", "value": 0, "token": "error"}`です。合計行には色が付きません。
- **コピー** — **コピー**ボタンは、現在のページを、表示されている列と合計行とともに、Excelに貼り付けられるタブ区切りテキストとして、クリップボードにコピーします。
- **Open in PlaidCloud** — ソースがPlaidCloudのテーブルの場合、**Open in PlaidCloud**リンクで、そのテーブルが開きます。
- **保存された列のレイアウト** — `layout_key="orders"`は、列の選択と並べ替え、一部の列の固定を行うための**列**と**Pinned**のセレクターを追加します。各閲覧者の選択は、その名前で保存され、次回アプリを開いたときに復元されます。
- **行リンク** — `row_link`は、行を辞書として受け取り、Webアドレスを返す関数で、リンクがない場合は`None`を返します。グリッドには**開く**列が追加され、リンクのある各行にリンクが表示されます。`http`と`https`のアドレスと、同じサイト内のパスのみがリンクされます。
- **更新** — `grid.refresh()`は、同じソースを再度クエリし、ページ、並べ替え、グループ化を保持します。[実行](#実行ボタンと鮮度)がテーブルへの書き込みを完了した後に呼び出してください。

`source`は、テーブル名、または[Data API](/ja/guides/panel-apps/data-api/)のテーブルです。グリッドを再フィルターするには、`grid.source`をフィルター済みのテーブルに設定するか、例のように`bar.table`から新しいグリッドを作成します。

グリッドは、閲覧者の行レベルセキュリティの対象です。閲覧者自身の接続を通じて読み取ります。

## Chart

`pcp.Chart(obj, title=None, height=320)`は、チャートをタイトル付きのカードに配置します。`obj`には、Bokehの図、hvPlotまたはHoloViewsのプロット、Plotlyの図、Matplotlibの図、またはそれらのいずれかを返す`pn.bind(...)`を指定できます。Bokehの図の数値軸には桁区切りが表示されるため、800000は800,000と表示されます。

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")`は、入力ウィジェットを送信ボタン付きの1つのフォームとして配置します。`form.values()`は、名前の付いたすべてのウィジェットについて`{widget.name: widget.value}`を返し、`on_submit`は、ボタンがクリックされたときにその辞書を受け取ります。

## Section、Card、Tabs、Loading

| コンポーネント | 用途 |
|---|---|
| `pcp.Section(title, *objects)` | ページの背景に直接配置される、タイトル付きのグループ。 |
| `pcp.Card(title, *objects)` | 浮き上がった面に配置される、タイトル付きのグループ。 |
| `pcp.Tabs(Overview=obj, Detail=obj)` | タブの内容を、そのタブが選択されたときに読み込むタブ。アクティブなタブには、ブランドカラーが使用されます。 |
| `pcp.Loading(height=200)` | データの読み込み中に表示する、きらめくプレースホルダー。 |

## StatusBanner

`pcp.StatusBanner(message, kind="info")`は、インライン通知を表示します。`kind`は`error`、`warning`、`success`、`info`のいずれかです。

## 実行ボタンと鮮度

`pcp.run_workflow_button(workflow_id, label=None)`は、アプリを開いたユーザーとしてPlaidCloudのワークフローを実行するボタンを追加し、**実行中…**、続いて**完了**または**失敗**を表示します。失敗した場合は、失敗したステップが最大5つまで示されます。`project_id`を渡さない限り、ワークフローはアプリのプロジェクトに属します。

`pcp.RunButton(label, start, status)`は、任意のジョブに対して同じことを行います。`start`はジョブを起動して実行IDを返し、`status(run_id)`は`"running"`、`"succeeded"`、`"failed"`、または理由を表示するための`("failed", reason)`を返します。どちらも、REST APIの呼び出しなど、通常の関数です。ボタンの`runs`の値は、実行が成功するたびに1ずつ増えるため、その後に更新が必要なビューは、これにバインドします。

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)`は、テーブルが最後に書き込まれた時刻を**Updated 5 min ago**のように表示します。経過時間は、ページを開いている間も更新されます。`stale_after=datetime.timedelta(hours=24)`を渡すと、それより古いデータが警告で示され、実行後に`.refresh()`を呼び出します。日付を特定できないテーブルには**Last update unknown**と表示されますが、これはエラーではありません。`pcp.Freshness(fetch)`は、任意のソースに対して同じことを行い、`fetch`はデータが最後に変更された時刻を返します。

## 保存された設定

`pcp.user_state`は、訪問の合間にそれぞれのユーザーの選択を記憶するため、アプリは前回終了したときの状態で開きます。

- `pcp.user_state.persist(widget, "region")`は、保存された値をウィジェットに復元し、変更のたびに保存します。ウィジェットがもう提供していない保存済みの値は、無視されます。
- `nav`で選択したページは、自動的に保存されます。
- `filters.`で始まるキー（たとえば`pcp.user_state.persist(widget, "filters.region")`）は、フィルターの選択を保持します。PlaidCloudは、読み取るたびに、これをそのユーザーの現在の行アクセスに合わせて絞り込むため、保存されたフィルターが、そのユーザーにもう見えない値を復活させることはありません。
- `pcp.user_state.get(key, default)`と`pcp.user_state.set(key, value)`は、その他の小さな値を保存します。

保存された設定は、1つのアプリの1人のユーザーに属し、最大8 KBです。設定がユーザー間で共有されることはありません。設定の保存時にPlaidCloudに接続できない場合、アプリはセッションが終了するまで、それを保持します。

## 印刷とPDFとして保存

`pcp.PrintButton()`は、ブラウザーの印刷ダイアログを開き、保存先として**PDFとして保存**を選択できます。ページは、サイドバーとコントロールが非表示で、プロジェクトのブランドが適用された状態で印刷されます。各`DataGrid`は、現在のページ全体を最大1,000行まで、最後に合計行を付けて印刷します。ダークアプリは、ライトのパレットで印刷されます。

## 言語

ボタン、通知、コマンドパレット、ツアー、実行と鮮度のメッセージ、グリッドのフッターなど、キット自体のテキストは、英語、ドイツ語、フランス語で表示されます。言語は、ページのアドレスの`?lang=de`または`?lang=fr`で指定し、指定がない場合はブラウザーの言語になります。数値には、その言語の区切り文字が使用されます。データ、列名、ユーザーが記述したラベルが翻訳されることはありません。

## パフォーマンスバジェット

最初の描画に3,000 msより長くかかるページの読み込み、または2,000 msより遅いクエリを実行するページの読み込みでは、アプリのログに、超過した項目を示す警告が書き込まれます。同じ数値は、[Panel Studio](/ja/guides/panel-apps/studio/#インサイト)の**インサイト**タブにも表示されます。アプリに別の上限を設定するには、次の環境変数を設定します。

| 変数 | デフォルト | 設定内容 |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | 最初の描画までのミリ秒。 |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | 1つのクエリのミリ秒。 |

整数でない値は無視され、デフォルトが適用されます。

## 独自のチャートの色

`pcp.series()`は、PlaidCloudのチャートのパレットを、色のリストとして順番に返します。例の棒グラフのように、独自に描画するチャートをキット自体のコンポーネントと一致させるために使用します。

## 次のステップ

- [Data API](/ja/guides/panel-apps/data-api/) — アプリからPlaidCloudのテーブルをフィルター、ページ送り、カウント、集計します。
- [アラートとダイジェスト](/ja/guides/panel-apps/alerts-and-digests/) — アプリからKPIアラートと定期サマリーを送信します。
- [プロジェクトのブランディング](/ja/guides/panel-apps/branding/) — プロジェクト内のすべてのアプリに対して、色とロゴを一度に設定します。
