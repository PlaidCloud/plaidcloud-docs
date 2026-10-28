---
title: The Panel App Kit
description: Build Panel apps that look like PlaidCloud with the plaidcloud_panel kit — the App shell, FilterBar, KpiCard, DataGrid, Chart, Form and layout components, in light and dark.
sidebar:
  order: 5
---

Every server Panel app has the `plaidcloud_panel` kit installed. It gives your app the PlaidCloud look — the same colors, type and spacing as the rest of the platform, in light and dark — and a set of ready-made components for the screens most apps need: filters, headline numbers, a large data grid, charts and forms. Your app picks up its [project's branding](/guides/panel-apps/branding/) automatically.

```python
import plaidcloud_panel as pcp
```

Importing the kit also applies the PlaidCloud look to Plotly and Matplotlib charts.

## Start From a Template

The kit includes a command that writes a working starter app. Run it from any folder, then edit the table and column names:

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

The command stops without writing anything if `app.py` already exists. Commit the two files to your repository and [publish the app](/guides/panel-apps/creating/).

## An Example App

This app filters a sales table by region and year, shows two headline numbers, a chart, and a grid with paging of the matching rows. Every piece follows the filters.

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
    return pcp.DataGrid(t, key="id", totals={"amount": "sum"})


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

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None)` builds the app shell: a header with the title, the project's logo and the signed-in user, a sidebar and a main area. Call `.servable()` on the result.

- **Navigation** — pass `nav=[("Overview", overview_page), ("Detail", detail_page)]` to get a page menu at the top of the sidebar. Each page is a Panel object or a function that returns one. Functions run when the page is selected.
- **Theme** — the app opens in the light theme. Pass `theme="dark"` to open in the dark theme, or add `?theme=dark` to the URL. With `theme_toggle=True` (the default) the header carries a light/dark switch.
- **Branding** — the app reads its project's brand colors and logo when a session starts. A project without branding gets the PlaidCloud defaults.
- **Anything else** — other keyword arguments pass through to Panel's `FastListTemplate`.

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))` makes one multi-select per column you name, listing that column's distinct values (up to 1,000, with a notice when the list is cut). Pass your own widgets by column name for anything else.

- `bar.table` is the table narrowed by the current selections. A blank widget does not narrow the data.
- Selections are saved in the page URL (`?region=EU`), so a filtered view can be shared as a link.

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}")` shows one headline number. `fn` is `sum`, `count`, `avg`, `min` or `max`, computed over the whole table by the server. With no `column` it shows the row count. Pass `bar.table` as the source so the number follows the filters.

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})` is a table view for data of any size. Only the current page is sent to the browser; paging, sorting, totals and export all run on the server.

- **Paging** — 200, 500 or 1,000 rows per page, with Previous and Next buttons and a row counter.
- **Sorting** — click a column header. The sort applies to the whole table, not only the visible page.
- **Totals** — `totals` maps a column to `sum`, `count`, `avg`, `min` or `max`. The server calculates each one over every matching row and pins the result as the last row of the grid.
- **Export** — **CSV** and **XLSX** buttons download every matching row in the current sort, up to `export_cap` rows (100,000 by default). When the table is larger, a notice tells you to narrow the filters. Text cells that start with `=`, `+`, `-` or `@` are prefixed with an apostrophe so a spreadsheet reads them as text.
- **Key** — `key` is the column, or list of columns, that uniquely identifies a row. Always pass it. See [Stable Paging](/guides/panel-apps/data-api/#stable-paging).

`source` is a table name or a table from the [Data API](/guides/panel-apps/data-api/). To refilter a grid, set `grid.source` to a filtered table, or build a new grid from `bar.table` as the example does.

The grid is subject to the viewer's row-level security: it reads through the viewer's own connection.

## Chart

`pcp.Chart(obj, title=None, height=320)` puts a chart in a titled card. `obj` can be a Bokeh figure, an hvPlot or HoloViews plot, a Plotly figure, a Matplotlib figure, or a `pn.bind(...)` that returns any of them.

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

## Colors for Your Own Charts

`pcp.series()` returns the PlaidCloud chart palette as a list of colors, in order. Use it so charts you draw yourself match the kit's own components, as the example does for the bar chart.

## Next Steps

- [The Data API](/guides/panel-apps/data-api/) — filter, page, count and aggregate PlaidCloud tables from your app.
- [Project Branding](/guides/panel-apps/branding/) — set your colors and logo once for every app in a project.
