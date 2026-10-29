---
title: Panel 应用套件
description: 使用 plaidcloud_panel 套件构建外观与 PlaidCloud 一致的 Panel 应用：App 外壳、命令面板、FilterBar、KpiCard、DataGrid、Chart、Form、运行按钮、已保存设置、打印和翻译，支持浅色和深色主题。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

每个服务器 Panel 应用都安装了 `plaidcloud_panel` 套件。它为您的应用提供 PlaidCloud 的外观（与平台其他部分相同的颜色、字体和间距，支持浅色和深色），以及一组现成的组件，用于大多数应用所需的界面：筛选器、关键数值、大型数据网格、图表和表单。您的应用会自动采用[项目品牌](/zh-cn/guides/panel-apps/branding/)。

```python
import plaidcloud_panel as pcp
```

导入该套件还会将 PlaidCloud 的外观应用到 Plotly 和 Matplotlib 图表。

## 从模板开始

该套件包含一个可生成可运行入门应用的命令。在任意文件夹中运行它，然后编辑表名和列名：

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| 选项 | 作用 |
|---|---|
| `--layout dashboard` | 侧边栏中放置筛选器，并包含两个关键数值和一张图表。 |
| `--layout explorer` | 侧边栏中放置筛选器，并包含行数和行表格。 |
| `--table` | 应用读取的 PlaidCloud 表。 |
| `--filters` | 用逗号分隔的筛选列。第一个列驱动图表。 |
| `--measure` | 要求和的数值列。 |
| `--dir` | 写入 `app.py` 和 `requirements.txt` 的位置。默认为当前文件夹。 |

如果 `app.py` 已存在，该命令会停止且不写入任何内容。将这两个文件提交到您的仓库，然后[发布应用](/zh-cn/guides/panel-apps/creating/)。

## 示例应用

此应用按区域和年份筛选销售表，显示两个关键数值、一张图表，以及一个对匹配行分页的网格。网格中的金额带有千位分隔符，利润率以百分比显示。每个部分都会随筛选器联动。

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

每个套件应用的模式都相同：基于一个表构建 `FilterBar`，然后将每个视图绑定到 `bar.table`。未绑定到 `bar.table`（或某个控件）的视图在筛选器变化时永远不会刷新。

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)` 构建应用外壳：包含标题、项目徽标和已登录用户的页眉，以及侧边栏和主区域。对结果调用 `.servable()`。

- **导航**：传入 `nav=[("Overview", overview_page), ("Detail", detail_page)]`，即可在侧边栏顶部获得页面菜单。每个页面是一个 Panel 对象，或返回 Panel 对象的函数。函数在选中页面时运行。
- **主题**：应用默认以浅色主题打开。传入 `theme="dark"` 可以深色主题打开，也可以在 URL 中添加 `?theme=dark`。当 `theme_toggle=True`（默认值）时，页眉带有浅色/深色切换开关。
- **品牌**：会话开始时，应用会读取其项目的品牌颜色和徽标。没有品牌设置的项目使用 PlaidCloud 默认值。
- **命令面板**：按 Ctrl-K（Mac 上为 Cmd-K）可搜索并运行命令。`nav` 中的每个页面都会列为 **转到** 页面名称，`commands={"Refresh data": refresh}` 可添加您自己的条目，每个条目由一个标签和一个不带参数的函数组成。选择某个条目，应用就会运行它。
- **首次运行导览**：`tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]` 会显示一个简短的分步介绍，每一步包含一个标题和一行文字。它出现在页面顶部，直到您完成或跳过，之后不会再次显示。
- **其他选项**：其他关键字参数会传递给 Panel 的 `FastListTemplate`。

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))` 为您指定的每个列创建一个可搜索的多选框，列出该列的不同值（最多 1,000 个，列表被截断时会显示提示）。未选择任何项时，选择框显示 **全部**。其他情况可按列名传入您自己的控件。

- `bar.table` 是按当前选择缩小范围后的表。空白控件不会缩小数据范围。
- 选择会保存在页面 URL 中（`?region=EU`），因此筛选后的视图可以通过链接分享。

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)` 显示一个关键数值。`fn` 为 `sum`、`count`、`avg`、`min` 或 `max`，由服务器针对整个表计算。未指定 `column` 时，显示行数。将 `bar.table` 作为数据源传入，数值就会随筛选器变化。

传入 `drill_to=grid`（一个 `DataGrid`），可在数值下方添加 **View rows** 按钮。选择它会让网格指向该卡片自己的表，因此网格会列出该数值背后的行。

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})` 是适用于任意规模数据的表视图。只有当前页会发送到浏览器；分页、排序、合计和导出都在服务器上运行。

- **分页**：每页 200、500 或 1,000 行，带有 Previous 和 Next 按钮以及行计数器。
- **排序**：点击列标题。排序作用于整个表，而不仅仅是可见的页面。
- **合计**：`totals` 将列映射到 `sum`、`count`、`avg`、`min` 或 `max`。服务器针对所有匹配的行计算每一项，并将结果固定为网格的最后一行。
- **导出**：**CSV** 和 **XLSX** 按钮会按当前排序下载所有匹配的行，最多 `export_cap` 行（默认 100,000）。当表更大时，提示会告诉您缩小筛选范围。以 `=`、`+`、`-` 或 `@` 开头的文本单元格会加上撇号前缀，使电子表格将其读取为文本。
- **数字格式**：`formats={"margin": "0.0%", "amount": "0,0"}` 为每个列设置显示格式，使用 [numbro](https://numbrojs.com/format.html) 格式字符串。`%` 格式会乘以 100。合计行使用相同的格式。未设置格式的浮点列最多显示两位小数，并带千位分隔符。**复制**、**CSV** 和 **XLSX** 保留原始值。
- **键**：`key` 是唯一标识一行的列或列列表。请始终传入。请参阅[稳定分页](/zh-cn/guides/panel-apps/data-api/#稳定分页)。

- **分组依据**：`group_by=["region"]` 每组显示一行，包含 `totals` 度量和 `rows` 计数（均由服务器计算），以及覆盖所有匹配行的 **总计** 行。传入 `groupable=["region", "year"]` 可添加 **分组依据** 选择器，让查看者自行选择列。网格最多显示 1,000 个分组，并在截断列表时给出提示。分组行没有 **打开** 链接。
- **条件格式**：`rules` 按值为单元格着色。每条规则指定一个 `column`、一个 `op`（`>`、`>=`、`<`、`<=`、`==`、`!=` 或 `between`）、一个 `value`（`between` 为 `[low, high]`）和一个 `token`（`success`、`warning`、`error` 或 `info`），例如 `{"column": "margin", "op": "<", "value": 0, "token": "error"}`。合计行永远不会着色。
- **复制**：**复制** 按钮会将当前页（含可见列和合计行）以制表符分隔的文本放入剪贴板，可直接粘贴到 Excel。
- **Open in PlaidCloud**：当数据源是 PlaidCloud 表时，**Open in PlaidCloud** 链接会打开该表。
- **已保存的列布局**：`layout_key="orders"` 会添加 **列** 和 **Pinned** 选择器，用于选择列、为列排序以及固定部分列。每位查看者的选择都以该名称保存，并在下次打开应用时恢复。
- **行链接**：`row_link` 是一个函数，接收一行（字典形式）并返回网址，或返回 `None` 表示无链接。网格会添加一个 **打开** 列，在每个有链接的行上显示链接。仅会链接 `http` 和 `https` 地址以及同一站点上的路径。
- **刷新**：`grid.refresh()` 会再次查询同一数据源，并保持页码、排序和分组。请在[运行](#运行按钮和数据新鲜度)完成表写入后调用。

`source` 是表名，或来自[数据 API](/zh-cn/guides/panel-apps/data-api/)的表。若要重新筛选网格，请将 `grid.source` 设置为筛选后的表，或如示例那样基于 `bar.table` 构建新的网格。

网格受查看者的行级安全约束：它通过查看者自己的连接读取数据。

## Chart

`pcp.Chart(obj, title=None, height=320)` 将图表放入带标题的卡片中。`obj` 可以是 Bokeh 图形、hvPlot 或 HoloViews 绘图、Plotly 图形、Matplotlib 图形，或返回其中任意一种的 `pn.bind(...)`。Bokeh 图形上的数值轴显示千位分隔符，因此 800000 显示为 800,000。

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")` 将输入控件排列为带提交按钮的单个表单。`form.values()` 为每个具名控件返回 `{widget.name: widget.value}`，点击按钮时，`on_submit` 会收到该字典。

## Section、Card、Tabs 和 Loading

| 组件 | 用途 |
|---|---|
| `pcp.Section(title, *objects)` | 直接位于页面背景上的带标题分组。 |
| `pcp.Card(title, *objects)` | 位于凸起表面上的带标题分组。 |
| `pcp.Tabs(Overview=obj, Detail=obj)` | 选中选项卡时才加载其内容的选项卡。活动选项卡采用品牌颜色。 |
| `pcp.Loading(height=200)` | 数据加载时显示的闪烁占位符。 |

## StatusBanner

`pcp.StatusBanner(message, kind="info")` 显示内联通知。`kind` 为 `error`、`warning`、`success` 或 `info`。

## 运行按钮和数据新鲜度

`pcp.run_workflow_button(workflow_id, label=None)` 添加一个按钮，以打开应用的人的身份运行 PlaidCloud 工作流，并依次显示 **正在运行…**，然后是 **完成** 或 **失败**。失败时会列出失败的步骤，最多五个。除非传入 `project_id`，否则该工作流属于应用所在的项目。

`pcp.RunButton(label, start, status)` 对任意作业执行相同的操作。`start` 启动作业并返回运行 id；`status(run_id)` 返回 `"running"`、`"succeeded"` 或 `"failed"`，或返回 `("failed", reason)` 以显示原因。两者都是普通函数，例如对 REST API 的调用。每次运行成功，按钮的 `runs` 值就加一，因此之后必须刷新的视图可以绑定到它：

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)` 显示表上次写入的时间，例如 **Updated 5 min ago**。页面保持打开时，时长会持续更新。传入 `stale_after=datetime.timedelta(hours=24)` 可用警告标记更旧的数据，并在运行后调用 `.refresh()`。无法确定时间的表显示 **Last update unknown**，这绝不是错误。`pcp.Freshness(fetch)` 对任意数据源执行相同的操作，其中 `fetch` 返回数据上次更改的时间。

## 已保存的设置

`pcp.user_state` 会在两次访问之间记住每个人的选择，使应用以其离开时的状态打开。

- `pcp.user_state.persist(widget, "region")` 将已保存的值恢复到控件中，并在每次更改时保存。控件不再提供的已保存值会被忽略。
- 在 `nav` 中选择的页面会自动保存。
- 以 `filters.` 开头的键（例如 `pcp.user_state.persist(widget, "filters.region")`）保存筛选选择。每次读取时，PlaidCloud 都会将其裁剪到此人当前的行访问权限，因此已保存的筛选器不会带回其已无权查看的值。
- `pcp.user_state.get(key, default)` 和 `pcp.user_state.set(key, value)` 用于保存其他小型值。

已保存的设置属于某个人在某个应用中的数据，最大 8 KB。设置绝不会在人与人之间共享。如果保存设置时无法连接 PlaidCloud，应用会保留该设置直到会话结束。

## 打印和另存为 PDF

`pcp.PrintButton()` 会打开浏览器的打印对话框，目标可选择 **另存为 PDF**。打印时会隐藏侧边栏和控件，并应用项目的品牌。每个 `DataGrid` 会打印其整个当前页（最多 1,000 行），合计行位于最后。深色应用使用浅色配色打印。

## 语言

套件自身的文本，例如按钮、通知、命令面板、导览、运行和新鲜度消息以及网格页脚，会以英语、德语或法语显示。语言取自页面地址中的 `?lang=de` 或 `?lang=fr`，否则使用浏览器的语言。数字使用该语言的分隔符。您的数据、列名和您编写的任何标签都不会被翻译。

## 性能预算

如果页面加载的首次绘制耗时超过 3,000 毫秒，或运行的查询慢于 2,000 毫秒，则会向应用的日志写入一条警告，指明超出的部分。相同的数据也显示在 [Panel Studio](/zh-cn/guides/panel-apps/studio/#洞察) 的 **洞察** 选项卡上。若要为应用设置不同的限值，请设置以下环境变量：

| 变量 | 默认 | 设置 |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | 首次绘制的毫秒数。 |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | 单次查询的毫秒数。 |

不是整数的值会被忽略，并使用默认值。

## 自定义图表的颜色

`pcp.series()` 按顺序返回 PlaidCloud 图表调色板的颜色列表。使用它可让您自己绘制的图表与套件自带组件保持一致，示例中的条形图就是这样做的。

## 后续步骤

- [数据 API](/zh-cn/guides/panel-apps/data-api/)：在应用中筛选、分页、计数和聚合 PlaidCloud 表。
- [警报和摘要](/zh-cn/guides/panel-apps/alerts-and-digests/)：从应用发送 KPI 警报和定期摘要。
- [项目品牌](/zh-cn/guides/panel-apps/branding/)：为项目中的每个应用一次性设置颜色和徽标。
