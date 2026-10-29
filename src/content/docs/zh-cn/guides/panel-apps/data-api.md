---
title: Panel 应用的数据 API
description: 使用 panel_data 从 Panel 应用读取 PlaidCloud 表：以已登录查看者的身份在服务器上筛选、分页、计数和聚合，并应用行级安全。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/data-api.md
---

`plaidcloud.utilities.panel_data` 是服务器 Panel 应用读取表而无需将整个表加载到应用中的方式。您只需描述想要什么：符合某些筛选条件的行、其中一页、计数或分组合计，PlaidCloud 的数据库会完成这些工作，只有结果会返回给应用。

每个请求都以查看应用的人的身份运行，因此其项目权限和[行级安全](/zh-cn/guides/panel-apps/accessing-data/)适用于返回的所有内容。

```python
from plaidcloud.utilities.panel_data import table

sales = table("sales")
```

`table(name)` 打开应用所在项目中的表，该项目即应用发布时[分配到的项目](/zh-cn/guides/panel-apps/branding/#将应用分配到项目)。若要读取其他项目中的表，请传入该项目：`table("sales", project="Finance")`。项目可以是 id、名称或路径。

表句柄永远不会改变。`filter` 会返回新的句柄，因此您可以保留未筛选的句柄，并从中派生多个视图。

## 筛选

```python
emea = sales.filter(region="EMEA", year=[2025, 2026])
```

每个关键字都是一个列名。单个值匹配与其相等的行。列表、元组或集合匹配等于其中任一成员的行。多个关键字以 AND 组合，对结果再次调用 `filter` 会添加更多条件。

值为 `None`、空字符串或空列表时，该列不会被筛选。这使空白的筛选控件不会影响数据：`sales.filter(**widget_values)` 无需先检查空白即可使用。

指定不存在的列会引发错误，错误信息会指明表和列。

## 分页

```python
rows = emea.page(1, 200, sort=["-amount"], key="id")
```

`page(n, size, sort, key)` 以 pandas 数据框形式返回第 `n` 页（从 1 开始计数），每页 `size` 行。

- `sort` 是列名列表。在名称前加 `-` 表示降序：`["region", "-amount"]`。
- `key` 是表的唯一列，或唯一列的列表。请始终传入。

### 稳定分页

分页是从有序的行列表中截取一个切片。每个请求都是一次独立的查询。如果两行在排序列上相同，数据库在下一次请求时可能以不同的顺序返回它们，因此某一行可能出现在两个切片中，也可能不出现在任何切片中。`key` 弥补了这一缺口：PlaidCloud 会将其添加到排序列之后，因此顺序始终是完整的，每一行恰好落在一个切片中。

没有 `key` 时，分页会退而按所有列排序。这在宽表上很慢，而且如果两行完全相同，仍然不稳定。分页时请始终传入唯一键，出于同样的原因，也请将其传给 [`DataGrid`](/zh-cn/guides/panel-apps/app-kit/#datagrid)。

## 计数

```python
total_rows = emea.count()
```

以整数形式返回符合筛选条件的行数。

## 聚合

```python
by_region = sales.aggregate(by=["region"], total=("amount", "sum"), orders=("id", "count"))
grand_total = emea.aggregate(total=("amount", "sum"))
```

`aggregate(by=(), limit=1000, **measures)` 返回一个数据框，每组一行，并按 `by` 列排序。每个度量的形式为 `name=(column, function)`，其中函数为 `sum`、`count`、`avg`、`min` 或 `max`。至少需要一个度量。

不带 `by` 时，您会得到针对筛选后行的单行合计。`limit` 限制返回的分组数量。

Decimal 列可能以字符串形式到达。在绘制图表或设置格式之前，请使用 `float(...)` 或 `astype(float)` 进行转换。

## 综合运用

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

`FilterBar`、`KpiCard` 和 `DataGrid` 都接受这些表句柄，因此大多数应用从不直接调用 `page`、`count` 或 `aggregate`。在构建自己的视图时才使用它们。请参阅 [Panel 应用套件](/zh-cn/guides/panel-apps/app-kit/)。

## 相关内容

- [读取数据和已登录用户](/zh-cn/guides/panel-apps/accessing-data/)：以查看者身份连接，以及何时直接使用 `PlaidConnection`。
