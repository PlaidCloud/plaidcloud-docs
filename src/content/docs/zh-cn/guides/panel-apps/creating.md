---
title: 创建 Panel 应用
description: 在 PlaidCloud 中，从 git 仓库发布服务器端 HoloViz Panel 应用（含 hello-world 示例），或从文件发布静态 WASM 应用。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

打开 **我的 Panel 应用**。工具栏提供两种发布方式，分别对应一种[运行时](/zh-cn/guides/panel-apps/)：

- **新建服务器应用**：从 git 仓库构建并运行应用。
- **添加 WASM 应用**：从文件发布静态的浏览器内应用。

若要直接在 PlaidCloud 中编写应用而无需设置仓库，请使用 [Panel Studio](/zh-cn/guides/panel-apps/studio/)。

## 创建服务器应用

服务器应用从 git 仓库构建，并在 `https://<your-tenant-host>/serve/<slug>/` 提供服务。您将 PlaidCloud 指向仓库的某个分支；它会将代码构建为容器，在其上运行 `panel serve`，并在您每次推送到该分支时自动重新构建。

### 准备应用仓库

仓库需要两样东西：一个 **入口点**（构建 Panel 应用并将其标记为 `.servable()` 的 Python 文件），以及可选的 **`requirements.txt`**（列出任何额外的包，位于仓库根目录或入口点旁边）。

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

这就是一个完整的应用。PlaidCloud 提供服务的正是 `.servable()` 调用：任何想要渲染的内容都必须标记为 servable（直接标记，或位于 servable 的布局中）。

#### 稍丰富的示例

Panel 应用是交互式的。此示例添加了一个滑块，可实时更新表格：

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

第二个示例导入了 `pandas`，它不属于基础镜像，因此请添加 `requirements.txt`（位于仓库根目录或入口点旁边）：

```text
pandas
```

PlaidCloud 在构建镜像时使用 `pip` 安装这些包。常见的可视化库（`plotly`、`holoviews`、`hvplot`）同样不在基础镜像中，因此请在此列出应用导入的所有库。

> **平台提供什么，以及期望什么。** 编写应用时请牢记以下假设：
>
> - **`panel` 和 `bokeh` 已由平台基础镜像预装。** 不要在 `requirements.txt` 中列出它们，并避免固定较旧的 Panel 版本，实时更新的重新连接依赖较新的版本。
> - **PlaidCloud 客户端库（`plaidcloud-rpc`、`plaidcloud-utilities`）已预装。** 直接导入 `plaidcloud.rpc` 或 `plaidcloud.utilities`，不要在 `requirements.txt` 中列出它们。
> - **`requirements.txt` 可以位于仓库根目录或入口点旁边。** 在共享（monorepo）仓库中，请将每个应用的依赖项放在各自的文件夹中。如果存在根目录的文件，也会一并安装：将共享依赖项放在那里，将应用专用的依赖项放在应用旁边。
> - **应用以非 root 用户在只读文件系统上运行。** 只有 `/tmp` 可写，因此请将任何临时文件写入那里（大多数库已遵循 `$TMPDIR`）。
> - **不要硬编码端口、URL 前缀或主机。** PlaidCloud 会在部署时分配并注入它们，只需调用 `.servable()`。

若要获得 PlaidCloud 的外观以及现成的筛选器、网格和图表，请使用 [Panel 应用套件](/zh-cn/guides/panel-apps/app-kit/)构建应用。

### 设置主题：浅色、深色或切换开关

服务器应用默认以 PlaidCloud 现代的 **Fast** 设计渲染，这是在整个平台应用的简洁 Fluent 风格外观。在发布对话框中，**设计** 控制该平台层：

- **FAST**：PlaidCloud 默认。用于新应用以及使用 Fast 模板构建的应用。
- **默认**：Panel 的默认样式。当现有应用的 CSS 或视觉效果在 FAST 下出现问题时使用。

您在应用代码中控制的是 **主题**：浅色、深色，或查看者可切换的开关。

主题是您所提供的 **模板** 的属性。Fast 模板（`FastListTemplate`（单列）和 `FastGridTemplate`（响应式网格））为此提供两项设置：

- **`theme`**：`"default"` 表示浅色，`"dark"` 表示深色。设置后会将应用固定为该主题，即使查看者在 URL 中添加 `?theme=dark` 也是如此。
- **`theme_toggle`**：`True` 在页眉中显示浅色/深色开关；`False` 将其隐藏。默认为 `True`。隐藏开关本身并不能固定主题，请使用上面的 `theme` 固定；固定之后再设置 `theme_toggle=False`，这样查看者就不会看到一个无法改变任何内容的开关。

请选择适合您应用的模式。

**仅浅色**：最适合密集的报表和财务表格，它们通常是针对浅色背景手工设计样式的：

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

> **如果允许深色，请让表格适配深色。** 固定为浅色表格主题的 `Tabulator`（`theme="bootstrap"`），或带有硬编码浅色（如 `background: #fff`）的自定义 CSS，在深色页面上会渲染成难以辨认的白色块。请使用跟随应用的表格主题，即 `pn.widgets.Tabulator(..., theme="fast")`，并避免硬编码浅色。如果报表主要针对浅色手工设计样式，请改为将其固定为浅色（上面的第一种模式）。

没有模板的普通应用（`pn.Column(...).servable()`）遵循 Panel 的默认设置，不受这些设置影响；需要明确控制时，请使用模板。

您的仓库必须可通过 PlaidCloud 中的 **git 连接**访问。如果您的代码位于 [PlaidCloud Git](/zh-cn/guides/git/) 中，请在 **Tools > 连接** 下创建托管的 **PlaidCloud Git** 连接，它无需服务器 URL 或凭据。有关从空仓库到已提供服务的应用的完整流程，请参阅[从 PlaidCloud Git 部署 Panel 应用](/zh-cn/guides/panel-apps/deploy-from-git/)。

### 发布应用

1. 单击 **新建服务器应用** 以打开 **发布服务器 Panel 应用** 对话框。其设置分为若干部分。
2. 在 **目录设置** 下：
   - **应用名称**：列表中显示的显示名称。
   - **URL 标识**：既是应用的 URL，也是其内部名称，因此必须是有效的 DNS 标签：小写字母、数字和连字符，以字母开头，不超过 40 个字符（例如 `sales-dashboard`）。对话框会在发布前检查这一点。
   - **备注**：可选的说明。
   - **项目**：拥有该应用的项目。它提供应用的[品牌](/zh-cn/guides/panel-apps/branding/)，并且是其表的默认项目。发布后无法在此更改；请使用[分配](/zh-cn/guides/panel-apps/branding/#对于现有应用)。
3. 在 **Git 连接和发布监视器** 下：
   - **Git 连接**：保存应用仓库的连接。
   - **分支**：要从中构建的分支。推送到该分支会自动重新构建并重新部署应用。
   - **入口点**：Panel 应提供服务的 `.py` 文件（您的 `app.py`）。
4. 在 **运行时** 下：
   - 应用容器应请求的 **CPU** 和 **内存**。

     > 资源越少（CPU / 内存越低），应用的调度和冷启动越快。

   - **设计**：选择 **FAST** 使用 PlaidCloud 的现代设计，或者在应用的 CSS 需要 Panel 默认样式时选择 **默认**。
   - **空闲（分钟）**：应用在没有流量的情况下保持预热的时长，之后缩减到零。默认为 5 分钟。
   - **允许公共访问**：勾选后允许未经身份验证的访问；否则查看者必须登录您的租户。
5. 在 **高级（嵌入式服务）** 下（可选）。默认情况下，应用仅从您的 PlaidCloud 租户提供服务。若要将其嵌入其他站点，请单击 **添加域**，并在每行输入一个允许加载它的域，仅填写主机，不含协议或路径（例如 `example.com` 或 `app.example.com:8443`）。除非要在其他地方嵌入应用，否则请保持列表为空。
6. 单击 **发布**。

发布后，应用开始 **构建**，其 **状态** 显示在列表中并自动更新。有关各状态的含义、应用就绪后如何打开，以及如何在不取消发布的情况下触发重新构建，请参阅[使用 Panel 应用](/zh-cn/guides/panel-apps/using/)。

> 只有当应用的构建状态为 **就绪** 时，其 URL 才可用，并且应用空闲后的第一个请求会将其唤醒（约 15 秒）。

### 高级：在本地匹配 PlaidCloud

技术用户可以使用 PlaidCloud 所用的相同输入来构建和测试应用。这是发布或单击 **重新构建** 之前最接近的本地检查。

PlaidCloud 使用以下生成的 Dockerfile 从所选的 git 分支构建。在本地使用相同的内容，命名为 `Dockerfile.plaidcloud-panel`：

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

要匹配服务器构建：

1. 检出您在 **分支** 中选择的同一分支。
2. 从仓库根目录运行构建，使 `COPY . /app` 与 PlaidCloud 一致。
3. 将可选依赖项放在 `requirements.txt` 中，位于仓库根目录或入口点旁边。两者都会安装，应用文件夹中的最后安装（这样应用专用的固定版本优先）。
4. 使用与您在 **入口点** 中选择的相同入口点路径。

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

部署的镜像不会覆盖基础镜像的入口点。它根据 PlaidCloud 注入的环境变量运行 `panel serve`。使用相同的运行时约定测试构建好的镜像：

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

测试时请匹配发布对话框中的设置：

- **入口点** 对应 `APP_PATH=/app/<entry-point>`。
- **CPU** 和 **内存** 对应 Docker 的 `--cpus` 和 `--memory` 限制。
- **设计：FAST** 对应 `PLAID_PANEL_DESIGN=fast`。
- **设计：默认** 表示省略 `PLAID_PANEL_DESIGN`。
- **空闲（分钟）** 对应已部署的缩容窗口。本地 Docker 不强制执行它，但应用仍使用相同的 Panel websocket 保活和会话清理设置。
- **嵌入式服务** 的域对应 `PANEL_ORIGIN`；如果需要测试多个主机，请使用以空格分隔的列表。

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

使用 `PLAID_PANEL_DESIGN=fast` 可匹配默认的已部署外观。若要测试发布对话框中的 **默认** 设计选项，请保持 `PLAID_PANEL_DESIGN` 未设置并运行相同的命令。请保留 `PANEL_PREFIX`、`PANEL_ORIGIN`、`--keep-alive` 和 `--unused-session-lifetime`；它们是已部署运行时约定的一部分。

## 创建 WASM 应用

WASM 应用在浏览器中从预先构建的 HTML 文件运行。

1. 单击 **添加 WASM 应用** 以打开 **发布无服务器 Panel 应用** 对话框。
2. 输入 **应用名称** 和 **版本**。
3. 选择 **应用 HTML 位置**，即文档账户中的 HTML 文件。
4. 输入 **应用 URL 标识** 和可选的 **备注**。
5. 单击 **发布**。WASM 应用没有构建步骤，会立即提供服务。
