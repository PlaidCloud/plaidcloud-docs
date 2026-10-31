---
title: 从 PlaidCloud Git 部署 Dash 应用
description: 在 PlaidCloud 中提供 Plotly Dash 应用服务的完整路径：将代码放入 PlaidCloud Git 仓库，通过免凭据的托管连接进行连接，并发布上线。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/deploy-from-git.md
---

这是从本机上的 Dash 应用代码到线上 URL 的完整路径，以 **[PlaidCloud Git](/zh-cn/guides/git/)**（内置于您工作区的托管 Git 服务）作为源。由于 PlaidCloud Git 是托管的，应用用于部署的连接**无需服务器 URL、用户名或令牌**，PlaidCloud 会代您进行身份验证。

共有五个步骤：

1. 编写一个最小的 Dash 应用。
2. 将其放入 PlaidCloud Git 仓库。
3. 创建托管的 PlaidCloud Git 连接。
4. 发布指向该仓库的 Dash 应用。
5. 打开已上线的应用，如果无法启动则查看构建日志。

本演练与[从 PlaidCloud Git 部署 Panel 应用](/zh-cn/guides/panel-apps/deploy-from-git/)几乎相同，两者都是基于 Git 构建、并以相同方式提供服务的服务器端 Python 应用。区别在于应用代码本身，以及发布对话框中的一个字段。

## 开始之前

- 在工作区中打开 **Git**，确认可以访问 PlaidCloud Git。默认情况下，工作区的组织包含一个 **`apps`** 仓库，它同样适合存放 Dash 应用。
- 如果想从本机推送代码，请在本地安装 `git`（也可以在 Git 网页界面中添加文件）。

## 1. 编写最小的 Dash 应用

应用需要一个**入口点**，即构建 Dash 应用并公开其 Flask 服务器的 Python 文件；另可选择提供 **`requirements.txt`** 来安装额外的包，它可以放在仓库根目录，也可以放在入口点旁边。

```
apps/
├── app.py            # entry point — exposes `server`
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

创建 `app.py`：

```python
import plaidcloud_dash as pcd
from dash import Dash, Input, Output, html

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you

app.layout = html.Div(
    [
        html.H1("Hello from PlaidCloud Git"),
        html.P(id="whoami"),
        html.Button("Who am I?", id="whoami-btn", n_clicks=0),
    ]
)


@app.callback(Output("whoami", "children"), Input("whoami-btn", "n_clicks"))
def _whoami(n_clicks):
    if not n_clicks:
        return ""
    return f"Signed in as {pcd.current_user()!r}"


if __name__ == "__main__":
    app.run(debug=True)
```

这就是一个完整的应用。`dash`、`plotly`、`dash-mantine-components`、`dash-ag-grid` 以及 PlaidCloud 客户端库（`plaidcloud-rpc`、`plaidcloud-utilities`）均已预装，因此在 `requirements.txt` 中只需列出*额外*的包。不要向 `Dash(__name__)` 传入 `requests_pathname_prefix` 或 `url_base_pathname`，平台会通过 `DASH_URL_BASE_PATHNAME` 自动设置 URL 前缀，同时设置两者会在启动时抛出配置错误。有关完整的应用约定和数据访问辅助函数，请参见[应用约定](/zh-cn/guides/dash-apps/#应用约定)以及[在 Dash 应用中读取数据和已登录用户](/zh-cn/guides/dash-apps/accessing-data/)。

## 2. 将应用放入 PlaidCloud Git 仓库

使用工作区现有的 **`apps`** 仓库，或者[新建一个](/zh-cn/guides/git/repositories/#创建存储库)，然后把代码放进去。

由于您是通过 PlaidCloud 登录的，您的 Git 账户没有单独的密码，请[生成个人访问令牌](/zh-cn/guides/git/repositories/#生成个人访问令牌)（**your avatar → Settings → Applications**），授予仓库**读取**和**写入**权限，并在 Git 提示输入密码时使用它。从仓库的**代码**按钮复制其 **HTTPS** 克隆 URL，然后执行：

```bash
git clone https://<your-git-host>/<org>/apps.git
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

记下仓库路径 `<org>/apps`，其中 `<org>` 是工作区的组织名称。下一步需要输入该路径。完整的克隆、提交和推送说明请参见[仓库](/zh-cn/guides/git/repositories/)。

> **这里的令牌仅用于*您自己*推送代码。** 接下来创建的连接是托管的，不需要令牌，请不要混淆两者。

## 3. 创建托管的 PlaidCloud Git 连接

**连接**用于告知 Dash 部署其代码所在的位置。对于 PlaidCloud Git，连接是*托管*的：PlaidCloud 提供主机和凭据，因此只需输入仓库目标。这与服务器 Panel 应用使用的连接类型相同。

1. 打开 **Tools > Connections**，点击**新建连接**，然后选择 **PlaidCloud Git**。
2. 为连接指定**账户名称**（例如 `Apps Repo`）。
3. 将 **Repository Path** 设置为 `<org>/apps`（即您在第 2 步中记下的路径），将**默认分支**设置为 `main`。除非应用位于子目录中，否则请将**起始路径**留空。
4. 点击**创建**。

没有服务器 URL、用户、密码或 SSL/SSH 字段，PlaidCloud Git 是托管的，由平台处理主机和身份验证。有关完整表单，包括连接的**用法**和**安全模型**（工作区中谁可以使用它），请参见 [PlaidCloud Git 连接](/zh-cn/guides/connections/plaidcloud-git/)。

## 4. 发布 Dash 应用

现在让 Dash 部署指向该连接。

1. 打开**我的 Panel 应用**，点击**新建 Dash 应用**。
2. 在**目录设置**下，设置**应用名称**和 **URL 标识**。URL 标识既是应用的 URL，也是其内部名称，因此请使用小写字母、数字和连字符，以字母开头，长度不超过 40 个字符（例如 `hello-dash`）。可选的**备注**用于描述应用。
3. 在 **Git 连接和发布监视器**下：
   - **Git 连接**：您在第 3 步中创建的 PlaidCloud Git 连接。
   - **分支**：`main`。推送到该分支会自动重新构建并重新部署应用。
   - **入口点**：`app.py`。
4. 在**运行时**下，选择 **CPU**、**内存**和**空闲（分钟）** 窗口。仅当应用应当无需登录即可访问时，才勾选**允许公共访问**。没有**设计**设置，那是 Panel 专有的选项。
5. 在**高级（嵌入式服务）** 下，此项为可选。除非要将应用嵌入其他站点，否则请留空。
6. 点击**发布**。

## 5. 打开应用，如果无法启动则查看日志

发布后，应用会进行**构建**：PlaidCloud 克隆该分支，安装您的 `requirements.txt`，并基于 `platform-dash-base` 镜像构建容器镜像。其**状态**显示在**我的 Panel 应用**列表中，并会自动更新。

- 当状态为**就绪**时，通过 `https://<your-tenant-host>/serve/<slug>/` 打开应用。空闲后的首次请求会将其启动，期间会短暂显示 PlaidCloud 加载屏幕。
- 如果构建失败，请打开应用并查看其**构建**日志，缺失的依赖项或导入错误会显示在那里。有关各状态的含义、如何阅读日志以及如何触发重新构建，请参见[使用 Dash 应用](/zh-cn/guides/dash-apps/using/)。

此后，**每次推送到连接的分支都会自动重新构建并重新部署应用**：编辑 `app.py`，执行 `git push`，更改即可上线。（除非应用已**锁定**，此时推送会被跳过，直到解锁，参见[使用 Dash 应用](/zh-cn/guides/dash-apps/using/#锁定应用)。）

## 后续步骤

- [在 Dash 应用中读取数据和已登录用户](/zh-cn/guides/dash-apps/accessing-data/)：以查看应用的人的身份查询 PlaidCloud 数据。
- [使用 Dash 应用](/zh-cn/guides/dash-apps/using/)：构建状态、日志、锁定和移除应用。
- [PlaidCloud Git 连接](/zh-cn/guides/connections/plaidcloud-git/)：完整的连接表单、用法和安全模型。
- [仓库](/zh-cn/guides/git/repositories/)：PlaidCloud Git 中的分支、令牌和协作。
