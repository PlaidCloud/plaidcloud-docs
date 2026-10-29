---
title: Dash 应用
description: 在 PlaidCloud 中构建和部署服务器端 Plotly Dash 数据应用，从 Git 仓库发布，并提供按用户身份验证和缩容到零，与服务器 Panel 应用保持一致。
sidebar:
  label: Dash 应用
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/index.md
---

Dash 应用可让您直接从 PlaidCloud 发布交互式 [Plotly Dash](https://dash.plotly.com/) 应用，包括回调、图表和数据网格（`dash-ag-grid`、`dash-mantine-components`）。您可以在**我的 Panel 应用**屏幕中管理它们，它们与 Panel 应用并列显示，每一行都显示其运行时、构建状态和 URL。

## Dash 的定位

Dash 应用的托管方式与**服务器 Panel 应用**完全相同：您让 PlaidCloud 指向 Git 仓库的某个分支，它将代码构建为容器，容器空闲时保持零副本，在首次请求时唤醒并提供服务，空闲后再缩容到零。Dash 没有单独的“WASM”运行时，每个 Dash 应用都是服务器应用。

当您的应用使用 Plotly Dash 而非 HoloViz Panel 编写时，请选择 Dash 应用，例如已有 Dash 代码库，或者团队更喜欢 Dash 的回调模型以及 `dash-ag-grid` / `dash-mantine-components` 生态。如果您刚开始且没有特定偏好，可参见 [Panel 应用](/zh-cn/guides/panel-apps/)了解另一种选择。

服务器 Panel 应用具备的一切，Dash 应用也同样具备：

- **按用户身份。** 每位查看者都通过平台的单点登录登录，应用为读取数据而发出的每次调用都以*该查看者*的身份运行，采用相同的[读取数据和已登录用户](/zh-cn/guides/panel-apps/accessing-data/)模型，并使用 Dash 自己的辅助 API。参见[在 Dash 应用中读取数据和已登录用户](/zh-cn/guides/dash-apps/accessing-data/)。
- **缩容到零。** 应用在配置的空闲窗口之后空闲到零副本，并在下一次请求时唤醒，冷启动期间会短暂显示 PlaidCloud 加载屏幕，参见[使用 Dash 应用](/zh-cn/guides/dash-apps/using/#打开-dash-应用)。
- **自动重新构建。** 每次推送到所连接的分支都会重新构建并重新部署应用。
- **运行时和构建日志**，每一行都标记了产生该行的会话所属的查看者。

Dash 应用有两点**不具备**，均出于设计考虑，且与 Panel 应用同样缺少的内容一致：

- **没有设计/主题设置。** Panel 发布对话框中的**设计**选项（FAST 与默认）是 Panel 专有的功能，Dash 应用完全通过您选择的组件（`dash-mantine-components`、自定义 CSS 等）来设置样式，因此发布表单中没有对应字段。
- **没有按应用的访问列表。** 访问由工作区的 SSO 关口控制，任何登录到您租户的人都可以打开应用（如果启用**允许公共访问**，则任何人都可以）。两种应用类型都没有单独的按应用 ACL 层。

## 应用约定

Dash 应用的入口文件必须命名为 `app.py`，并且必须公开 `server`，这就是全部约定：

```python
from dash import Dash

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you
```

- **将文件命名为 `app.py`。** PlaidCloud 的启动器会将您的应用作为 `app` 模块导入并读取其 `server` 对象，因此无论在**入口点**中设置什么路径（仓库根目录或子文件夹），该路径上的文件都必须命名为 `app.py`。
- **在模块级别公开 `server = app.server`。** 这是平台导入的对象。
- **无需自行接入登录。** 平台会自动将每个请求置于按用户单点登录的关口之后，您无需为获取身份而调用 `init_auth` 或导入 `plaidcloud_dash`。（仍然调用 `plaidcloud_dash.init_auth(server, url_base_pathname=os.environ["DASH_URL_BASE_PATHNAME"])` 的旧应用照常工作，该调用是幂等的，因此可与平台自己的接入共存。）
- **不要在 `Dash(__name__)` 上设置 `requests_pathname_prefix` 或 `url_base_pathname`。** 每个 Dash 应用都在强制的 URL 前缀（`/serve/<slug>/`）下提供服务，平台通过 `DASH_URL_BASE_PATHNAME` 环境变量为您设置它，这是 Dash 自身的原生配置变量，先于任何构造函数参数被读取。再显式传入前缀会与 Dash 自身的配置冲突，导致应用无法启动。
- **`Entry Point` 可以指向子文件夹。** 启动应用之前，宿主会将容器的工作目录设置为入口文件所在的文件夹，因此同一文件夹中的同级导入（`import data`）和应用中的相对文件路径都以该文件夹为基准解析，与在其中运行 `python app.py` 相同。
- **不要在导入时读取数据。** 请在回调中而不是模块范围内执行 PlaidCloud 读取，参见[在 Dash 应用中读取数据和已登录用户](/zh-cn/guides/dash-apps/accessing-data/)。应用的模块在容器启动时运行一次，此时还没有查看者登录，在那里读取连接或表没有可代表的查看者，会导致应用在启动时失败。

PlaidCloud 在**带线程的 gunicorn** 下运行您的应用，因此它可以在一个进程中为并发查看者提供服务，无需额外操作即可支持多人同时使用应用。

## 在 Panel 和 Dash 之间选择

| | Panel 应用 | Dash 应用 |
|---|---|---|
| 框架 | HoloViz Panel | Plotly Dash |
| 运行时 | WASM（浏览器内）或服务器 | 仅服务器 |
| 身份模型 | 按用户 SSO（服务器应用） | 按用户 SSO |
| 缩容到零 | 仅服务器应用 | 是 |
| 设计/主题设置 | 有（FAST / 默认） | 无，通过您自己的组件设置样式 |
| 按应用的访问列表 | 无，工作区 SSO 关口 | 无，工作区 SSO 关口 |

## 后续步骤

- [从 PlaidCloud Git 部署 Dash 应用](/zh-cn/guides/dash-apps/deploy-from-git/)：使用免凭据的托管连接，从仓库到已上线应用的完整路径。
- [在 Dash 应用中读取数据和已登录用户](/zh-cn/guides/dash-apps/accessing-data/)：以查看应用的人的身份查询 PlaidCloud 数据。
- [使用 Dash 应用](/zh-cn/guides/dash-apps/using/)：构建状态、打开应用、日志和移除应用。
