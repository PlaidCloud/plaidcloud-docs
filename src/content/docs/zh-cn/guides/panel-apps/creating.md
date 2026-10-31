---
title: 创建 Panel 应用
description: 在 Panel Studio 中从空白应用、表、视图或图库创建 Panel 应用，或者针对定制需求从 git 发布服务器应用，或发布静态 WASM 应用。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

从 Panel Studio 开始。它无需存储库，也无需任何设置：您在 PlaidCloud 中构建应用、预览，并在准备好时发布。只有在 Studio 不适用时，才选择定制运行时。

## 创建 Studio 应用

打开**我的 Panel 应用**。**新建 Studio 应用** 是工具栏中的第一个按钮。您也可以在项目**主页**选项卡的 **Panel 应用**框中选择 **新建 Studio 应用**，或[从表开始](#从表开始)。

1. 选择 **新建 Studio 应用**。
2. 输入**名称**。**URL 标识**会根据它自动填写。
3. 选择拥有该应用的**项目**。您需要拥有该项目的编辑权限。
4. 在**起始来源**下，选择应用的起点：

   | 起始来源 | 您将获得 |
   |---|---|
   | **空白应用** | 包含 `app.py` 和 `requirements.txt` 的最小应用。 |
   | **来自表** | 基于所选表构建的应用。 |
   | **来自视图** | 同上，基于项目视图构建。 |
   | **来自另一个 Studio 应用** | 您的某个 Studio 应用的副本。 |
   | **来自应用库** | 您的工作区[在图库中列出](#从图库开始)的某个应用的副本。 |

5. 选择**创建**。Studio 会打开新应用。对于表或视图，Weave 构建第一个页面的提示已准备好发送。

要编辑、预览和发布应用，请参阅 [Panel Studio](/zh-cn/guides/panel-apps/studio/)。

### 从表开始

您也可以从项目的**表**选项卡开始。选择一个表或视图，然后从**新建**菜单或右键菜单中选择 **创建 Panel 应用**。**新建 Studio 应用** 对话框随即打开，并已选好项目和表。当您拥有该项目的编辑权限且项目不是只读时，此命令才可用。

### 从图库开始

在**我的 Panel 应用**工具栏中选择 **应用库**，浏览您的工作区已列出的应用，然后选择 **从此创建应用…** 创建您自己的副本。也可以在 **新建 Studio 应用** 对话框中选择 **来自应用库**。请参阅[应用图库](/zh-cn/guides/panel-apps/gallery/)，其中包括如何列出您自己的应用。

## 其他运行时

Studio 应用可满足大多数仪表板和工具的需求。对于定制需求，可从**我的 Panel 应用**工具栏使用其他[运行时](/zh-cn/guides/panel-apps/)之一进行发布：

- **添加 WASM 应用**：从文件发布静态的浏览器内应用。
- **新建服务器应用**：从您管理的 git 存储库构建并运行应用，例如要复用现有代码或使用您自己的构建流程时。
- **新建 Dash 应用**：发布 Plotly Dash 应用。请参阅 [Dash 应用](/zh-cn/guides/dash-apps/)。

## 创建服务器应用

服务器应用从 git 存储库构建，并通过 `https://<your-tenant-host>/serve/<slug>/` 提供服务。您将 PlaidCloud 指向某个存储库的分支；它会将代码构建为容器，在其上运行 `panel serve`，并在您每次推送到该分支时自动重新构建。

### 准备应用存储库

您的存储库需要两样东西：**入口点**（构建 Panel 应用并将其标记为 `.servable()` 的 Python 文件），以及可选的 **`requirements.txt`**（列出任何额外的包，位于存储库根目录或入口点旁边）。

```
my-panel-app/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

#### Hello World

创建 `app.py`：

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello, PlaidCloud 👋\n\nYour first server-side Panel app is running.").servable()
```

这就是一个完整的应用。PlaidCloud 提供服务的是 `.servable()` 调用，任何想要渲染的内容都必须标记为 servable（直接标记，或位于 servable 布局之中）。

#### 稍复杂的示例

Panel 应用是交互式的。这个示例添加了一个滑块，可实时更新表：

```python
import pandas as pd
import panel as pn

pn.extension()

multiplier = pn.widgets.IntSlider(name="Multiplier", start=1, end=10, value=3)

@pn.depends(multiplier)
def times_table(m):
    df = pd.DataFrame({"n": range(1, 6)})
    df["result"] = df["n"] * m
    return pn.pane.DataFrame(df, index=False)

pn.Column(
    "# Times Table",
    multiplier,
    times_table,
).servable()
```

#### 添加依赖项

第二个示例导入了 `pandas`，它不属于基础镜像，因此请添加 `requirements.txt`（位于存储库根目录，或入口点旁边）：

```text
pandas
```

PlaidCloud 在构建镜像时使用 `pip` 安装这些依赖项。常见的可视化库（`plotly`、`holoviews`、`hvplot`）同样不在基础镜像中，因此请在此列出应用导入的所有此类库。

> **平台提供什么，以及期望什么。** 编写应用时请牢记以下假设：
>
> - **`panel` 和 `bokeh` 由平台基础镜像预装。** 不要在 `requirements.txt` 中列出它们，也要避免固定较旧的 Panel 版本，因为实时更新的重新连接依赖较新的版本。
> - **PlaidCloud 客户端库（`plaidcloud-rpc`、`plaidcloud-utilities`）已预装。** 直接导入 `plaidcloud.rpc` 或 `plaidcloud.utilities`，不要在 `requirements.txt` 中列出它们。
> - **`requirements.txt` 可以位于存储库根目录或入口点旁边。** 在共享（monorepo）存储库中，请将每个应用的依赖项放在各自的文件夹中。如果存在根目录级文件，也会安装它：将共享依赖项放在那里，将应用专用的依赖项放在应用旁边。
> - **应用以非 root 用户身份在只读文件系统上运行。** 只有 `/tmp` 可写，因此请将任何临时文件写入该位置（大多数库已遵循 `$TMPDIR`）。
> - **不要硬编码端口、URL 前缀或主机。** PlaidCloud 会分配它们并在部署时注入，只需调用 `.servable()`。

要获得 PlaidCloud 的外观以及现成的筛选器、网格和图表，请使用 [Panel 应用工具包](/zh-cn/guides/panel-apps/app-kit/)构建应用。

### 设置主题：浅色、深色或切换

服务器应用默认以 PlaidCloud 的现代 **FAST** 设计渲染，这是应用于整个平台的简洁 Fluent 风格外观。在发布对话框中，**设计**控制该平台层：

- **FAST**：PlaidCloud 默认。用于新应用和使用 Fast 模板构建的应用。
- **默认**：Panel 的默认样式。当现有应用的 CSS 或视觉效果在 FAST 下出现问题时使用。

您在应用代码中控制的是**主题**：浅色、深色，或查看者可以切换的开关。

主题是您所提供的**模板**的属性。Fast 模板（`FastListTemplate`，单列；`FastGridTemplate`，响应式网格）为此提供两项设置：

- **`theme`**：`"default"` 表示浅色，或 `"dark"`。设置它会将应用固定在该主题上，即使查看者在 URL 中添加 `?theme=dark` 也是如此。
- **`theme_toggle`**：`True` 在页眉中显示浅色/深色开关；`False` 将其隐藏。默认为 `True`。仅隐藏开关并不能固定主题，请使用上面的 `theme` 固定；固定之后再设置 `theme_toggle=False`，这样查看者就不会看到无法改变任何内容的开关。

请选择适合您应用的模式。

**仅浅色**：最适合密集的报表和财务表，它们通常是针对浅色背景手工设计样式的：

```python
import panel as pn

pn.extension("tabulator")

pn.template.FastListTemplate(
    title="Sales Dashboard",
    theme="default",      # light
    theme_toggle=False,   # hide the switch
    main=[...],
).servable()
```

**仅深色：**

```python
pn.template.FastListTemplate(
    title="Ops Monitor",
    theme="dark",
    theme_toggle=False,
    main=[...],
).servable()
```

**由查看者选择**：默认为浅色，页眉中带有开关。省略 `theme`，使其跟随开关：

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **如果允许深色，请让您的表适配深色。** 固定为浅色表主题（`theme="bootstrap"`）的 `Tabulator`，或带有 `background: #fff` 这类硬编码浅色的自定义 CSS，会在深色页面上渲染为无法阅读的白色块。请使用跟随应用的表主题，即 `pn.widgets.Tabulator(..., theme="fast")`，并避免硬编码浅色。如果某份报表是针对浅色手工设计样式的，请改为将其固定为浅色（即上面的第一种模式）。

没有模板的普通应用（`pn.Column(...).servable()`）遵循 Panel 的默认值，不受这些设置影响；需要明确控制时，请使用模板。

您的存储库必须能通过 PlaidCloud 中的 **Git 连接**访问。如果您的代码位于 [PlaidCloud Git](/zh-cn/guides/git/) 中，请在 **Tools > Connections** 下创建一个托管的 **PlaidCloud Git** 连接，它无需服务器 URL 或凭据。关于从空存储库到已提供服务的应用的完整流程，请参阅[从 PlaidCloud Git 部署 Panel 应用](/zh-cn/guides/panel-apps/deploy-from-git/)。

### 发布应用

1. 单击**新建服务器应用**以打开**发布服务器 Panel 应用**对话框。其设置分为多个部分。
2. 在**目录设置**下：
   - **应用名称**：列表中显示的名称。
   - **URL 标识**：既是应用的 URL，也是其内部名称，因此必须是有效的 DNS 标签：小写字母、数字和连字符，以字母开头，不超过 40 个字符（例如 `sales-dashboard`）。对话框会在发布前检查这一点。
   - **备注**：可选的描述。
   - **项目**：拥有该应用的项目。它提供应用的[品牌](/zh-cn/guides/panel-apps/branding/)，并且是应用所用表的默认项目。发布后无法在此更改；请使用 [Assign](/zh-cn/guides/panel-apps/branding/#对于现有应用)。
3. 在 **Git 连接和发布监视器**下：
   - **Git 连接**：保存应用存储库的连接。
   - **分支**：要从中构建的分支。推送到该分支会自动重新构建并重新部署应用。
   - **入口点**：Panel 应提供服务的 `.py` 文件（即您的 `app.py`）。
4. 在**运行时**下：
   - 应用容器应请求的 **CPU** 和**内存**。

     > 资源越少（CPU/内存越低），应用的调度和冷启动越快。

   - **设计**：选择 **FAST** 使用 PlaidCloud 的现代设计，如果应用的 CSS 需要 Panel 的默认样式，则选择**默认**。
   - **空闲（分钟）**：在没有流量的情况下，应用保持预热状态多长时间后缩减为零。默认为 5 分钟。
   - **允许公共访问**：勾选后允许未经身份验证的访问；否则查看者必须登录您的租户。
5. 在**高级（嵌入式服务）** 下，此项可选。默认情况下，应用仅从您的 PlaidCloud 租户提供服务。若要将其嵌入另一个站点，请单击**添加域**，并输入每个允许加载它的域，每行一个，只需主机，不含协议或路径（例如 `example.com` 或 `app.example.com:8443`）。除非要将应用嵌入到其他位置，否则请将列表留空。
6. 单击**发布**。

发布后，应用开始**构建**，其**状态**显示在列表中并自动更新。有关各状态的含义、应用就绪后如何打开，以及如何在不取消发布的情况下触发重新构建，请参阅[使用 Panel 应用](/zh-cn/guides/panel-apps/using/)。

> 只有构建状态为**就绪**时，应用的 URL 才能使用；空闲之后的第一次请求会将其启动（约 15 秒）。

### 高级：在本地匹配 PlaidCloud

技术用户可以使用 PlaidCloud 所用的相同输入来构建和测试应用。这是发布或单击**重新构建**之前最接近的本地检查。

PlaidCloud 使用以下生成的 Dockerfile，从所选的 git 分支构建。在本地使用相同的内容，命名为 `Dockerfile.plaidcloud-panel`：

```dockerfile
FROM us-docker.pkg.dev/plaidcloud-build/panel-base/platform-panel-base:0.5.1
USER root
COPY . /app
RUN if [ -f /app/requirements.txt ]; then pip install --no-cache-dir -r /app/requirements.txt; fi
# If your entry point is in a subfolder, PlaidCloud also installs that folder's requirements.txt,
# after the root one (so a per-app pin wins). Replace <app-folder> with your entry point's folder,
# or drop this line if your app is at the repository root.
RUN if [ -f "/app/<app-folder>/requirements.txt" ]; then pip install --no-cache-dir -r "/app/<app-folder>/requirements.txt"; fi
USER 10001
```

要与服务器构建保持一致：

1. 检出您在**分支**中选择的同一分支。
2. 从存储库根目录运行构建，使 `COPY . /app` 与 PlaidCloud 一致。
3. 将可选依赖项放入 `requirements.txt`，位于存储库根目录或入口点旁边。两者都会安装，应用文件夹中的最后安装（因此应用专用的固定版本优先）。
4. 使用您在**入口点**中选择的同一入口点路径。

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

部署的镜像不会覆盖基础镜像的入口点。它根据 PlaidCloud 注入的环境变量运行 `panel serve`。请使用相同的运行时约定测试构建的镜像：

```sh
docker run --rm \
  --cpus 0.5 \
  --memory 512m \
  -p 5006:5006 \
  -e APP_PATH=/app/app.py \
  -e PANEL_PREFIX=/serve/local \
  -e PANEL_PORT=5006 \
  -e PANEL_ORIGIN=localhost:5006 \
  -e PANEL_KEEP_ALIVE_MS=25000 \
  -e PLAID_PANEL_DESIGN=fast \
  local-panel-app:plaidcloud
```

打开 `http://localhost:5006/serve/local/`。

测试时请与发布对话框的设置保持一致：

- **入口点**对应 `APP_PATH=/app/<entry-point>`。
- **CPU** 和**内存**对应 Docker 的 `--cpus` 和 `--memory` 限制。
- **设计：FAST** 对应 `PLAID_PANEL_DESIGN=fast`。
- **设计：默认**表示省略 `PLAID_PANEL_DESIGN`。
- **空闲（分钟）** 对应已部署的缩减窗口。本地 Docker 不会强制执行它，但应用仍使用相同的 Panel websocket 保活和会话清理设置。
- **嵌入式服务**的域对应 `PANEL_ORIGIN`；如需测试多个主机，请使用以空格分隔的列表。

如果不需要容器，您仍然可以在本地 Python 环境中测试服务层。安装相同的 `requirements.txt`，设置平台环境变量，然后使用已部署镜像所用的相同标志运行 `panel serve`。

```sh
export APP_PATH=app.py
export PANEL_PREFIX=/serve/local
export PANEL_PORT=5006
export PANEL_ORIGIN=localhost:5006
export PANEL_KEEP_ALIVE_MS=25000
export PLAID_PANEL_DESIGN=fast

panel serve "$APP_PATH" \
  --address 0.0.0.0 \
  --port "$PANEL_PORT" \
  --prefix "$PANEL_PREFIX" \
  --allow-websocket-origin "$PANEL_ORIGIN" \
  --num-procs 1 \
  --keep-alive "$PANEL_KEEP_ALIVE_MS" \
  --unused-session-lifetime 15000 \
  --index "$(basename "$APP_PATH" .py)"
```

打开 `http://localhost:5006/serve/local/`。

使用 `PLAID_PANEL_DESIGN=fast` 以匹配默认的已部署外观。要测试发布对话框的**默认**设计选项，请不设置 `PLAID_PANEL_DESIGN` 并运行同一命令。请保留 `PANEL_PREFIX`、`PANEL_ORIGIN`、`--keep-alive` 和 `--unused-session-lifetime`；它们是已部署运行时约定的一部分。

## 创建 WASM 应用

WASM 应用从预先构建的 HTML 文件在浏览器中运行。

1. 单击**添加 WASM 应用**以打开**发布无服务器 Panel 应用**对话框。
2. 输入**应用名称**和**版本**。
3. 选择**应用 HTML 位置**，即文档账户中的 HTML 文件。
4. 输入**应用 URL 标识**和可选的**备注**。
5. 单击**发布**。WASM 应用没有构建步骤，会立即提供服务。
