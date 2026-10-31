---
title: The Panel App Kit
description: Build Panel apps that look like PlaidCloud with the plaidcloud_panel kit — the App shell, command palette, FilterBar, KpiCard, DataGrid, Chart, Form, run buttons, saved settings, printing and translations, in light and dark.
sidebar:
  order: 5
---

Every server Panel app has the `plaidcloud_panel` kit installed. It gives your app the PlaidCloud look — the same colors, type and spacing as the rest of the platform, in light and dark — and a set of ready-made components for the screens most apps need: filters, headline numbers, a large data grid, charts and forms. Your app picks up its [project's branding](/guides/panel-apps/branding/) automatically.

```python
import plaidcloud_panel as pcp
```

Importing the kit also applies the PlaidCloud look to Plotly and Matplotlib charts.

## Start From a Template

In [Panel Studio](/guides/panel-apps/studio/), **New Studio App** starts from a blank app, a table or view, another Studio app, or an app in the [gallery](/guides/panel-apps/gallery/), with no command to run.

For an app you keep in a git repository, the kit includes a command that writes a working starter app. Run it from any folder, then edit the table and column names:

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| Option | What it does |
|---|---|
| `--layout dashboard` | Filters in the sidebar, two headline numbers and a chart. |
| `--layout explorer` | Filters in the sidebar, a row count and a table of rows. |
| `--table` | The PlaidCloud table the app reads. |
| `--filters` | Comma-separated columns to filter by. The first one drives the chart. |
| `--measure` | The numeric column to total. |
| `--dir` | Where to write `app.py` and `requirements.txt`. Defaults to the current folder. |

The command stops without writing anything if `app.py` already exists. Commit the two files to your repository and [publish it as a server app](/guides/panel-apps/creating/#creating-a-server-app).

## An Example App

This app filters a sales table by region and year, shows two headline numbers, a chart, and a grid with paging of the matching rows. The grid shows amounts with thousands separators and margins as percentages. Every piece follows the filters.

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

The pattern is the same in every kit app: build a `FilterBar` over a table, then bind each view to `bar.table`. A view that is not bound to `bar.table` (or to a widget) never refreshes when the filters change.

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)` builds the app shell: a header with the title, the project's logo and the signed-in user, a sidebar and a main area. Call `.servable()` on the result.

- **Navigation** — pass `nav=[("Overview", overview_page), ("Detail", detail_page)]` to get a page menu at the top of the sidebar. Each page is a Panel object or a function that returns one. Functions run when the page is selected.
- **Theme** — the app opens in the light theme. Pass `theme="dark"` to open in the dark theme, or add `?theme=dark` to the URL. With `theme_toggle=True` (the default) the header carries a light/dark switch.
- **Branding** — the app reads its project's brand colors and logo when a session starts. A project without branding gets the PlaidCloud defaults.
- **Command palette** — press Ctrl-K (Cmd-K on a Mac) to search and run commands. Every page in `nav` is listed as **Go to** the page name, and `commands={"Refresh data": refresh}` adds your own entries, each a label and a function that takes no arguments. Pick an entry and the app runs it.
- **First-run tour** — `tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]` shows a short step-by-step intro, each step a heading and a line of text. It appears at the top of the page until you finish or skip it, and is not shown to you again.
- **Anything else** — other keyword arguments pass through to Panel's `FastListTemplate`.

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))` makes one searchable multi-choice box per column you name, listing that column's distinct values (up to 1,000, with a notice when the list is cut). A box shows **All** when nothing is picked. Pass your own widgets by column name for anything else.

- `bar.table` is the table narrowed by the current selections. A blank widget does not narrow the data.
- Selections are saved in the page URL (`?region=EU`), so a filtered view can be shared as a link.

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)` shows one headline number. `fn` is `sum`, `count`, `avg`, `min` or `max`, computed over the whole table by the server. With no `column` it shows the row count. Pass `bar.table` as the source so the number follows the filters.

Pass `drill_to=grid`, a `DataGrid`, to add a **View rows** button under the number. Choosing it points the grid at the card's own table, so the grid lists the rows behind the number.

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})` is a table view for data of any size. Only the current page is sent to the browser; paging, sorting, totals and export all run on the server.

- **Paging** — 200, 500 or 1,000 rows per page, with Previous and Next buttons and a row counter.
- **Sorting** — click a column header. The sort applies to the whole table, not only the visible page.
- **Totals** — `totals` maps a column to `sum`, `count`, `avg`, `min` or `max`. The server calculates each one over every matching row and pins the result as the last row of the grid.
- **Export** — **CSV** and **XLSX** buttons download every matching row in the current sort, up to `export_cap` rows (100,000 by default). When the table is larger, a notice tells you to narrow the filters. Text cells that start with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet reads them as text.
- **Number formats** — `formats={"margin": "0.0%", "amount": "0,0"}` sets a display format per column, using [numbro](https://numbrojs.com/format.html) format strings. A `%` format multiplies by 100. The Total row uses the same format. Float columns without a format show up to two decimals with thousands separators. **Copy**, **CSV** and **XLSX** keep the raw values.
- **Key** — `key` is the column, or list of columns, that uniquely identifies a row. Always pass it. See [Stable Paging](/guides/panel-apps/data-api/#stable-paging).

- **Group by** — `group_by=["region"]` shows one row per group, with the `totals` measures and a `rows` count, all calculated by the server, and a **Total** row over every matching row. Pass `groupable=["region", "year"]` to add a **Group by** selector so viewers choose the columns. A grid shows up to 1,000 groups and tells you when it has cut the list. Group rows have no **Open** links.
- **Conditional formatting** — `rules` colors cells by value. Each rule names a `column`, an `op` (`>`, `>=`, `<`, `<=`, `==`, `!=` or `between`), a `value` (`[low, high]` for `between`) and a `token` (`success`, `warning`, `error` or `info`), for example `{"column": "margin", "op": "<", "value": 0, "token": "error"}`. The Total row is never colored.
- **Copy** — the **Copy** button puts the current page, with the visible columns and the Total row, on the clipboard as tab-separated text that pastes into Excel.
- **Open in PlaidCloud** — when the source is a PlaidCloud table, an **Open in PlaidCloud** link opens that table.
- **Saved column layout** — `layout_key="orders"` adds **Columns** and **Pinned** selectors for choosing and ordering columns and pinning some of them. Each viewer's choice is saved under that name and restored the next time they open the app.
- **Row links** — `row_link` is a function that takes a row, as a dictionary, and returns a web address, or `None` for no link. The grid adds an **Open** column with a link on each row that has one. Only `http` and `https` addresses and paths on the same site are linked.
- **Refresh** — `grid.refresh()` queries the same source again and keeps the page, sort and grouping. Call it after a [run](#run-buttons-and-freshness) finishes writing the table.

`source` is a table name or a table from the [Data API](/guides/panel-apps/data-api/). To refilter a grid, set `grid.source` to a filtered table, or build a new grid from `bar.table` as the example does.

The grid is subject to the viewer's row-level security: it reads through the viewer's own connection.

## Chart

`pcp.Chart(obj, title=None, height=320)` puts a chart in a titled card. `obj` can be a Bokeh figure, an hvPlot or HoloViews plot, a Plotly figure, a Matplotlib figure, or a `pn.bind(...)` that returns any of them. Numeric axes on Bokeh figures show thousands separators, so 800000 reads 800,000.

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")` lays input widgets out as one form with a submit button. `form.values()` returns `{widget.name: widget.value}` for every named widget, and `on_submit` receives that dictionary when the button is clicked.

## Section, Card, Tabs and Loading

| Component | Use it for |
|---|---|
| `pcp.Section(title, *objects)` | A titled group directly on the page background. |
| `pcp.Card(title, *objects)` | A titled group on a raised surface. |
| `pcp.Tabs(Overview=obj, Detail=obj)` | Tabs that load a tab's content when it is selected. The active tab takes the brand color. |
| `pcp.Loading(height=200)` | A shimmering placeholder to show while data loads. |

## StatusBanner

`pcp.StatusBanner(message, kind="info")` shows an inline notice. `kind` is `error`, `warning`, `success` or `info`.

## Run Buttons and Freshness

`pcp.run_workflow_button(workflow_id, label=None)` adds a button that runs a PlaidCloud workflow as the person who opened the app, and shows **Running…**, then **Done** or **Failed**. A failure names the steps that failed, up to five. The workflow belongs to the app's project unless you pass `project_id`.

`pcp.RunButton(label, start, status)` does the same for any job. `start` launches it and returns a run id; `status(run_id)` returns `"running"`, `"succeeded"` or `"failed"`, or `("failed", reason)` to show a reason. Both are ordinary functions, such as calls to a REST API. The button's `runs` value goes up by one each time a run succeeds, so a view that must refresh afterward binds to it:

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)` shows when a table was last written, as **Updated 5 min ago**. The age moves on while the page stays open. Pass `stale_after=datetime.timedelta(hours=24)` to flag older data with a warning, and call `.refresh()` after a run. A table that can't be dated shows **Last update unknown**; that is never an error. `pcp.Freshness(fetch)` does the same for any source, where `fetch` returns when the data last changed.

## Saved Settings

`pcp.user_state` remembers each person's choices between visits, so an app opens the way they left it.

- `pcp.user_state.persist(widget, "region")` restores the saved value into the widget and saves it on every change. A saved value that the widget no longer offers is ignored.
- The page chosen in `nav` is saved automatically.
- A key that starts with `filters.`, such as `pcp.user_state.persist(widget, "filters.region")`, holds a filter choice. PlaidCloud trims it to the person's current row access each time it is read, so a saved filter never brings back values they can no longer see.
- `pcp.user_state.get(key, default)` and `pcp.user_state.set(key, value)` save any other small value.

Saved settings belong to one person in one app, up to 8 KB. Settings are never shared between people. If PlaidCloud can't be reached when a setting is saved, the app keeps it until the session ends.

## Print and Save as PDF

`pcp.PrintButton()` opens the browser's print dialog, where the destination can be **Save as PDF**. The page prints with the sidebar and controls hidden and your project's brand applied. Each `DataGrid` prints its whole current page, up to 1,000 rows, with its Total row last. A dark app prints with the light palette.

## Languages

The kit's own text, such as buttons, notices, the command palette, the tour, run and freshness messages and the grid footer, appears in English, German or French. The language is `?lang=de` or `?lang=fr` in the page address, otherwise the browser's language. Numbers use the language's separators. Your data, column names and any labels you write are never translated.

## Performance Budgets

A page load whose first paint takes longer than 3,000 ms, or that runs a query slower than 2,000 ms, writes a warning to the app's log naming what went over. The same figures appear on the **Insights** tab in [Panel Studio](/guides/panel-apps/studio/#insights). To set different limits for an app, set these environment variables:

| Variable | Default | Sets |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | Milliseconds to the first paint. |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | Milliseconds for one query. |

A value that is not a whole number is ignored, and the default applies.

## Colors for Your Own Charts

`pcp.series()` returns the PlaidCloud chart palette as a list of colors, in order. Use it so charts you draw yourself match the kit's own components, as the example does for the bar chart.

## Next Steps

- [The Data API](/guides/panel-apps/data-api/) — filter, page, count and aggregate PlaidCloud tables from your app.
- [Alerts and Digests](/guides/panel-apps/alerts-and-digests/) — send KPI alerts and scheduled summaries from an app.
- [Project Branding](/guides/panel-apps/branding/) — set your colors and logo once for every app in a project.
