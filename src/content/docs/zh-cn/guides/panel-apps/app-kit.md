---
title: Panel 应用工具包
description: 使用 plaidcloud_panel 工具包构建外观与 PlaidCloud 一致的 Panel 应用，涵盖 App 外壳、命令面板、FilterBar、KpiCard、DataGrid、Chart、Form、运行按钮、已保存设置、打印和翻译，并支持浅色和深色主题。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

每个服务器 Panel 应用都已安装 `plaidcloud_panel` 工具包。它为应用提供 PlaidCloud 的外观，包括与平台其余部分一致的颜色、字体和间距，支持浅色和深色主题，并提供一组现成组件，可满足大多数应用所需的界面：筛选器、关键数字、大型数据网格、图表和表单。应用会自动采用其[项目的品牌](/zh-cn/guides/panel-apps/branding/)。

```python
import plaidcloud_panel as pcp
```

导入该工具包还会将 PlaidCloud 的外观应用到 Plotly 和 Matplotlib 图表。

## 从模板开始

在 [Panel Studio](/zh-cn/guides/panel-apps/studio/) 中，**新建 Studio 应用** 可以从空白应用、表或视图、另一个 Studio 应用，或[图库](/zh-cn/guides/panel-apps/gallery/)中的应用开始，无需运行任何命令。

对于保存在 git 存储库中的应用，该工具包包含一个可生成可运行起始应用的命令。可在任意文件夹中运行它，然后修改表名和列名：

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| 选项 | 作用 |
|---|---|
| `--layout dashboard` | 侧边栏中放置筛选器，并包含两个关键数字和一个图表。 |
| `--layout explorer` | 侧边栏中放置筛选器，并包含行数和一个行表。 |
| `--table` | 应用读取的 PlaidCloud 表。 |
| `--filters` | 以逗号分隔的筛选列。第一列驱动图表。 |
| `--measure` | 要汇总的数值列。 |
| `--dir` | 写入 `app.py` 和 `requirements.txt` 的位置。默认为当前文件夹。 |

如果 `app.py` 已存在，该命令会停止且不写入任何内容。将这两个文件提交到存储库，然后[将其发布为服务器应用](/zh-cn/guides/panel-apps/creating/#创建服务器应用)。

## 示例应用

此应用按地区和年份筛选销售表，显示两个关键数字、一个图表，以及一个分页显示匹配行的网格。网格中的金额带有千位分隔符，利润率以百分比显示。每一部分都会随筛选器变化。

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

每个工具包应用的模式都相同：在表上构建 `FilterBar`，然后将每个视图绑定到 `bar.table`。未绑定到 `bar.table`（或某个控件）的视图不会在筛选器变化时刷新。

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)` 构建应用外壳：包含标题、项目徽标和已登录用户的页眉，以及侧边栏和主区域。对结果调用 `.servable()`。

- **导航**：传入 `nav=[("Overview", overview_page), ("Detail", detail_page)]`，即可在侧边栏顶部得到页面菜单。每个页面可以是 Panel 对象，也可以是返回 Panel 对象的函数。函数在选择该页面时运行。
- **主题**：应用默认以浅色主题打开。传入 `theme="dark"` 可以深色主题打开，也可以在 URL 中添加 `?theme=dark`。当 `theme_toggle=True`（默认）时，页眉带有浅色/深色切换开关。
- **品牌**：应用在会话开始时读取其项目的品牌颜色和徽标。没有品牌设置的项目使用 PlaidCloud 默认值。
- **命令面板**：按 Ctrl-K（Mac 上为 Cmd-K）可搜索并运行命令。`nav` 中的每个页面都列为**转到**页面名称，`commands={"Refresh data": refresh}` 可添加您自己的条目，每个条目由一个标签和一个不带参数的函数组成。选择某个条目后，应用就会运行它。
- **首次运行导览**：`tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]` 会显示简短的分步介绍，每一步包含一个标题和一行文字。它显示在页面顶部，直到您完成或跳过，之后不会再次显示。
- **其他选项**：其他关键字参数会传递给 Panel 的 `FastListTemplate`。

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))` 会为您指定的每一列生成一个可搜索的多选框，列出该列的不同值（最多 1,000 个，列表被截断时会显示提示）。未选择任何内容时，选择框显示**全部**。对于其他需求，可按列名传入您自己的控件。

- `bar.table` 是按当前所选内容缩小范围后的表。空白控件不会缩小数据范围。
- 所选内容保存在页面 URL 中（`?region=EU`），因此筛选后的视图可以通过链接分享。

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)` 显示一个关键数字。`fn` 为 `sum`、`count`、`avg`、`min` 或 `max`，由服务器针对整个表计算。未指定 `column` 时，显示行数。将 `bar.table` 作为源传入，数字就会随筛选器变化。

传入 `drill_to=grid`（一个 `DataGrid`），可在数字下方添加 **View rows** 按钮。选择它会使网格指向该卡片自己的表，因此网格会列出该数字背后的行。

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})` 是适用于任意数据量的表视图。只有当前页会发送到浏览器；分页、排序、合计和导出都在服务器上运行。

- **分页**：每页 200、500 或 1,000 行，带有“上一页”和“下一页”按钮以及行计数器。
- **排序**：单击列标题。排序应用于整个表，而不仅是可见的页面。
- **合计**：`totals` 将某一列映射为 `sum`、`count`、`avg`、`min` 或 `max`。服务器针对每个匹配行计算各项结果，并将结果固定为网格的最后一行。
- **导出**：**CSV** 和 **XLSX** 按钮按当前排序下载所有匹配行，最多 `export_cap` 行（默认为 100,000）。当表更大时，会有提示告知您缩小筛选范围。以 `=`、`+`、`-` 或 `@` 开头的文本单元格会加上撇号前缀，以便电子表格将其作为文本读取。
- **数字格式**：`formats={"margin": "0.0%", "amount": "0,0"}` 按列设置显示格式，使用 [numbro](https://numbrojs.com/format.html) 格式字符串。`%` 格式会乘以 100。总计行使用相同的格式。没有指定格式的浮点列最多显示两位小数并带千位分隔符。**复制**、**CSV** 和 **XLSX** 保留原始值。
- **键**：`key` 是唯一标识一行的列或列的列表。请始终传入它。请参阅[稳定分页](/zh-cn/guides/panel-apps/data-api/#稳定分页)。

- **分组依据**：`group_by=["region"]` 每个分组显示一行，包含 `totals` 指标和 `rows` 计数（均由服务器计算），以及覆盖所有匹配行的**总计**行。传入 `groupable=["region", "year"]` 可添加**分组依据**选择器，让查看者自行选择列。网格最多显示 1,000 个分组，并在截断列表时告知您。分组行没有**打开**链接。
- **条件格式**：`rules` 按值为单元格着色。每条规则指定一个 `column`、一个 `op`（`>`、`>=`、`<`、`<=`、`==`、`!=` 或 `between`）、一个 `value`（`between` 为 `[low, high]`）和一个 `token`（`success`、`warning`、`error` 或 `info`），例如 `{"column": "margin", "op": "<", "value": 0, "token": "error"}`。总计行从不着色。
- **复制**：**复制**按钮会将当前页（含可见列和总计行）以制表符分隔的文本形式放入剪贴板，可粘贴到 Excel 中。
- **Open in PlaidCloud**：当源是 PlaidCloud 表时，**Open in PlaidCloud** 链接会打开该表。
- **已保存的列布局**：`layout_key="orders"` 会添加**列**和 **Pinned** 选择器，用于选择列、为列排序并固定部分列。每位查看者的选择以该名称保存，并在下次打开应用时恢复。
- **行链接**：`row_link` 是一个函数，它接收以字典表示的一行，并返回网址，返回 `None` 则表示没有链接。网格会添加**打开**列，在每个有链接的行上显示一个链接。只有 `http` 和 `https` 地址以及同一站点上的路径才会生成链接。
- **刷新**：`grid.refresh()` 会再次查询同一数据源，并保留页码、排序和分组。在[运行](#运行按钮和数据新鲜度)完成表的写入后调用它。

`source` 是表名，或来自[数据 API](/zh-cn/guides/panel-apps/data-api/) 的表。若要重新筛选网格，可将 `grid.source` 设置为筛选后的表，也可以像示例那样基于 `bar.table` 构建新的网格。

网格受查看者行级安全的约束：它通过查看者自己的连接读取数据。

## Chart

`pcp.Chart(obj, title=None, height=320)` 将图表放入带标题的卡片中。`obj` 可以是 Bokeh 图形、hvPlot 或 HoloViews 绘图、Plotly 图形、Matplotlib 图形，或返回其中任意一种的 `pn.bind(...)`。Bokeh 图形上的数值轴会显示千位分隔符，因此 800000 显示为 800,000。

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")` 将输入控件排布为带提交按钮的一个表单。`form.values()` 为每个命名控件返回 `{widget.name: widget.value}`，单击按钮时 `on_submit` 会收到该字典。

## Section、Card、Tabs 和 Loading

| 组件 | 用途 |
|---|---|
| `pcp.Section(title, *objects)` | 直接放在页面背景上的带标题分组。 |
| `pcp.Card(title, *objects)` | 放在凸起表面上的带标题分组。 |
| `pcp.Tabs(Overview=obj, Detail=obj)` | 选择选项卡时才加载其内容的选项卡。活动选项卡采用品牌颜色。 |
| `pcp.Loading(height=200)` | 数据加载时显示的闪烁占位符。 |

## StatusBanner

`pcp.StatusBanner(message, kind="info")` 显示内嵌通知。`kind` 为 `error`、`warning`、`success` 或 `info`。

## 运行按钮和数据新鲜度

`pcp.run_workflow_button(workflow_id, label=None)` 会添加一个按钮，以打开该应用的用户身份运行 PlaidCloud 工作流，并显示**正在运行…**，然后显示**完成**或**失败**。失败时会指出失败的步骤，最多五个。除非传入 `project_id`，否则工作流属于应用所在的项目。

`pcp.RunButton(label, start, status)` 对任何作业的作用相同。`start` 启动作业并返回运行 ID；`status(run_id)` 返回 `"running"`、`"succeeded"` 或 `"failed"`，或返回 `("failed", reason)` 以显示原因。两者都是普通函数，例如对 REST API 的调用。每次运行成功时，按钮的 `runs` 值会加一，因此需要在之后刷新的视图可以绑定到它：

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)` 显示表最后一次写入的时间，如 **Updated 5 min ago**。页面保持打开时，时间会持续更新。传入 `stale_after=datetime.timedelta(hours=24)` 可用警告标记更旧的数据，运行之后请调用 `.refresh()`。无法确定时间的表会显示 **Last update unknown**；这从来不是错误。`pcp.Freshness(fetch)` 对任何数据源的作用相同，其中 `fetch` 返回数据最后一次更改的时间。

## 已保存设置

`pcp.user_state` 会在两次访问之间记住每个人的选择，使应用以他们离开时的状态打开。

- `pcp.user_state.persist(widget, "region")` 会将已保存的值恢复到控件中，并在每次更改时保存。控件不再提供的已保存值会被忽略。
- 在 `nav` 中选择的页面会自动保存。
- 以 `filters.` 开头的键（例如 `pcp.user_state.persist(widget, "filters.region")`）保存筛选器选择。PlaidCloud 每次读取时都会将其裁剪到该用户当前的行访问权限范围内，因此已保存的筛选器不会带回他们已无法查看的值。
- `pcp.user_state.get(key, default)` 和 `pcp.user_state.set(key, value)` 用于保存任何其他小型值。

已保存设置属于某个应用中的某个人，最大 8 KB。设置绝不会在人与人之间共享。如果保存设置时无法连接到 PlaidCloud，应用会保留该设置直到会话结束。

## 打印和另存为 PDF

`pcp.PrintButton()` 会打开浏览器的打印对话框，目标可选择**另存为 PDF**。打印页面时会隐藏侧边栏和控件，并应用您项目的品牌。每个 `DataGrid` 会打印其整个当前页（最多 1,000 行），总计行在最后。深色应用使用浅色调色板打印。

## 语言

工具包自身的文字（例如按钮、通知、命令面板、导览、运行和新鲜度消息以及网格页脚）以英语、德语或法语显示。语言由页面地址中的 `?lang=de` 或 `?lang=fr` 决定，否则使用浏览器的语言。数字使用该语言的分隔符。您的数据、列名和您编写的任何标签绝不会被翻译。

## 性能预算

如果页面加载的首次绘制耗时超过 3,000 毫秒，或运行的查询慢于 2,000 毫秒，会向应用日志写入一条警告，指明超出的项目。相同的数据也显示在 [Panel Studio](/zh-cn/guides/panel-apps/studio/#洞察) 的**洞察**选项卡中。若要为应用设置不同的限制，请设置以下环境变量：

| 变量 | 默认 | 设置 |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | 首次绘制的毫秒数。 |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | 一次查询的毫秒数。 |

不是整数的值会被忽略，转而使用默认值。

## 自定义图表的颜色

`pcp.series()` 按顺序以颜色列表的形式返回 PlaidCloud 图表调色板。使用它可让您自己绘制的图表与工具包自带的组件保持一致，示例中的条形图就是这样做的。

## 后续步骤

- [数据 API](/zh-cn/guides/panel-apps/data-api/)：从您的应用中筛选、分页、计数和聚合 PlaidCloud 表。
- [告警和摘要](/zh-cn/guides/panel-apps/alerts-and-digests/)：从应用发送 KPI 告警和定期摘要。
- [项目品牌](/zh-cn/guides/panel-apps/branding/)：一次性为项目中的每个应用设置颜色和徽标。
