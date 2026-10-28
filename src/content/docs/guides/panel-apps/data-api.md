---
title: The Data API for Panel Apps
description: Read PlaidCloud tables from a Panel app with panel_data — filter, page, count and aggregate on the server, as the signed-in viewer, with row-level security applied.
sidebar:
  order: 6
---

`plaidcloud.utilities.panel_data` is the way a server Panel app reads a table without loading the whole table into the app. You describe what you want — rows matching some filters, one page of them, a count, a grouped total — and PlaidCloud's database does the work. Only the result comes back to the app.

Every request runs as the person viewing the app, so their project permissions and [row-level security](/guides/panel-apps/accessing-data/) apply to everything it returns.

```python
from plaidcloud.utilities.panel_data import table

sales = table("sales")
```

`table(name)` opens a table in the app's project, which is the project the app was [assigned to](/guides/panel-apps/branding/#assign-an-app-to-a-project) when it was published. To read a table from a different project, pass it: `table("sales", project="Finance")`. The project can be an id, a name or a path.

A table handle never changes. `filter` returns a new handle, so you can keep the unfiltered one and derive several views from it.

## Filter

```python
emea = sales.filter(region="EMEA", year=[2025, 2026])
```

Each keyword is a column name. A single value matches rows equal to it. A list, tuple or set matches rows equal to any member. Several keywords combine with AND, and calling `filter` again on the result adds more conditions.

A value of `None`, an empty string or an empty list leaves that column unfiltered. That is what lets a blank filter widget leave the data alone: `sales.filter(**widget_values)` works without checking for blanks first.

Naming a column that does not exist raises an error that names the table and the column.

## Page

```python
rows = emea.page(1, 200, sort=["-amount"], key="id")
```

`page(n, size, sort, key)` returns page `n` (counting from 1) of `size` rows as a pandas dataframe.

- `sort` is a list of column names. Prefix a name with `-` for descending order: `["region", "-amount"]`.
- `key` is the unique column, or list of unique columns, for the table. Always pass it.

### Stable Paging

Paging takes a slice of an ordered list of rows. Each request is a separate query. If two rows tie on the sort columns, the database can return them in a different order on the next request, so a row can appear in two slices or in none. `key` closes that gap: PlaidCloud adds it after your sort columns, so the order is always complete and every row lands in exactly one slice.

Without a `key`, paging falls back to ordering by every column. That is slow on a wide table, and still unstable if two rows are identical. Pass a unique key whenever you page, and for the same reason pass it to [`DataGrid`](/guides/panel-apps/app-kit/#datagrid).

## Count

```python
total_rows = emea.count()
```

Returns the number of rows that match the filters, as a whole number.

## Aggregate

```python
by_region = sales.aggregate(by=["region"], total=("amount", "sum"), orders=("id", "count"))
grand_total = emea.aggregate(total=("amount", "sum"))
```

`aggregate(by=(), limit=1000, **measures)` returns a dataframe with one row per group, ordered by the `by` columns. Each measure is `name=(column, function)`, where the function is `sum`, `count`, `avg`, `min` or `max`. At least one measure is required.

With no `by`, you get a single row of totals over the filtered rows. `limit` caps the number of groups returned.

Decimal columns can arrive as strings. Convert them with `float(...)` or `astype(float)` before you chart or format them.

## Putting It Together

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

`FilterBar`, `KpiCard` and `DataGrid` all take these table handles, so most apps never call `page`, `count` or `aggregate` directly. Use them when you build your own views. See [The Panel App Kit](/guides/panel-apps/app-kit/).

## Related

- [Reading Data and the Signed-In User](/guides/panel-apps/accessing-data/) — connecting as the viewer, and when to use `PlaidConnection` directly.
