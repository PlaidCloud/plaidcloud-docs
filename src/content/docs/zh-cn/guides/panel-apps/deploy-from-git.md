---
title: 从 PlaidCloud Git 部署 Panel 应用
description: 在 PlaidCloud 中提供 HoloViz Panel 应用服务的端到端流程：将代码放入 PlaidCloud Git 仓库，通过无需凭据的受管理连接进行连接，并发布上线。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

这是从您机器上的 Panel 应用代码到上线 URL 的完整流程，以 **[PlaidCloud Git](/zh-cn/guides/git/)**（内置于您工作区的受管理 Git 服务）作为来源。由于 PlaidCloud Git 是受管理的，您的应用用于部署的连接**无需服务器 URL、用户名或令牌**：PlaidCloud 会代您完成身份验证。

共有五个步骤：

1. 编写最小的 Panel 应用。
2. 将其放入 PlaidCloud Git 仓库。
3. 创建受管理的 PlaidCloud Git 连接。
4. 发布指向该仓库的服务器应用。
5. 打开已提供服务的应用，如果它没有启动，请阅读构建日志。

每个步骤都链接到相应部分的深入指南；本页将它们串联成一条完整的路径。

## 开始之前

- 从工作区打开 **Git**，确认您可以访问 PlaidCloud Git。默认情况下，工作区的组织包含一个 **`apps`** 仓库（以及一个 **`udfs`** 仓库），这是存放 Panel 应用的天然场所。
- 如果要从本机推送代码，请在本地安装 `git`（您也可以在 Git 网页界面中添加文件）。

## 1. 编写最小的 Panel 应用

您的应用需要一个**入口点**（构建 Panel 应用并将其标记为 `.servable()` 的 Python 文件），以及可选的 **`requirements.txt`**（用于额外的软件包，位于仓库根目录或入口点旁边）。

```
apps/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

创建 `app.py`：

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello from PlaidCloud Git 👋\n\nServed straight from your workspace repository.").servable()
```

这就是一个完整的应用，PlaidCloud 提供服务的是 `.servable()` 调用。`panel`、`bokeh` 和 PlaidCloud 客户端库（`plaidcloud-rpc`、`plaidcloud-utilities`）已预装，因此只需在 `requirements.txt` 中列出*额外的*软件包。有关更丰富的示例、依赖项以及浅色/深色主题，请参阅[创建 Panel 应用](/zh-cn/guides/panel-apps/creating/)。

## 2. 将应用放入 PlaidCloud Git 仓库

使用工作区现有的 **`apps`** 仓库，或者[创建一个新仓库](/zh-cn/guides/git/repositories/#创建存储库)。然后将代码放入其中。您在 [Panel Studio](/zh-cn/guides/panel-apps/studio/#应用存放位置) 中构建的应用已经是 `apps` 中的文件夹，因此您会在那里看到它们与您的应用并列。

由于您通过 PlaidCloud 登录，您的 Git 账户没有单独的密码，请[生成个人访问令牌](/zh-cn/guides/git/repositories/#生成个人访问令牌)（**your avatar → Settings → Applications**），并授予 **write:repository** 权限，在 Git 提示时将其用作密码。推送到 `apps` 需要**贡献者**访问权限；如果 **Git** 选项卡显示您是**查看者**，请让工作区管理员将您添加到 **Git Contributors**。使用 **Git** 选项卡中仓库克隆地址旁边的复制按钮，然后：

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

请记下仓库路径 `<org>/apps`，其中 `<org>` 是您工作区的组织名称。您将在下一步输入该路径。完整的克隆、提交和推送详情请参阅[仓库](/zh-cn/guides/git/repositories/)。

> **这里的令牌仅用于*您*推送代码**。接下来创建的连接是受管理的，不需要令牌，请不要混淆两者。

## 3. 创建受管理的 PlaidCloud Git 连接

**连接**会告诉 Panel 部署其代码所在的位置。对于 PlaidCloud Git，连接是*受管理的*：PlaidCloud 提供主机和凭据，因此您只需输入仓库目标。

1. 打开 **Tools > Connections**，点击**新建连接**，然后选择 **PlaidCloud Git**。
2. 为连接指定**账户名称**（例如 `Apps Repo`）。
3. 将**仓库路径**设置为 `<org>/apps`（即您在第 2 步中记下的路径），将**默认分支**设置为 `main`。除非您的应用位于子目录中，否则请将**起始路径**留空。
4. 点击**创建**。

没有服务器 URL、用户、密码或 SSL/SSH 字段，PlaidCloud Git 是受管理的，因此平台会处理主机和身份验证。有关完整的表单，包括连接的**用法**和**安全模型**（工作区中谁可以使用它），请参阅 [PlaidCloud Git 连接](/zh-cn/guides/connections/plaidcloud-git/)。

> **使用较旧的工作区构建？** 如果表单仍显示服务器 URL 或凭据字段，请将它们留空，无论哪种情况，平台都会代您进行身份验证。

## 4. 发布服务器应用

现在将服务器部署指向该连接。

1. 打开**应用**，选择**新建应用** > **基于服务器**。
2. 在**目录设置**下，设置**应用名称**和 **URL 标识**，标识既是应用的 URL，也是其内部名称，因此请使用小写字母、数字和连字符，以字母开头，不超过 40 个字符（例如 `hello-panel`）。
3. 在 **Git 连接和发布监视器**下：
   - **Git 连接**：您在第 3 步中创建的 PlaidCloud Git 连接。
   - **分支**：`main`。推送到该分支会自动重新构建并重新部署应用。
   - **入口点**：`app.py`。
4. 在**运行时**下，选择 **CPU**、**内存**、**设计**（**FAST** 为 PlaidCloud 的现代外观）和**空闲**窗口。只有在应用无需登录即可访问时，才勾选**允许公共访问**。
5. 点击**发布**。

此对话框中的每个字段都在[创建 Panel 应用](/zh-cn/guides/panel-apps/creating/#发布应用)中有说明。

## 5. 打开应用，如果无法启动则阅读日志

发布后，应用开始**构建**：PlaidCloud 会克隆分支，安装您的 `requirements.txt`（仓库根目录的以及您的应用文件夹中的，如果存在），并构建容器镜像。其**状态**显示在**应用**列表中并自动更新。

- 当状态为**就绪**时，请在 `https://<your-tenant-host>/serve/<slug>/` 打开应用。空闲后的首个请求会将其启动（约 15 秒）。
- 如果构建失败，请打开应用并查看其**构建**日志，缺少依赖项或导入错误会在那里显示。请参阅[使用 Panel 应用](/zh-cn/guides/panel-apps/using/)，了解每个状态的含义、如何读取日志以及如何触发重新构建。

从现在起，**每次推送到连接的分支都会自动重新构建并重新部署应用**：编辑 `app.py`，执行 `git push`，您的更改就会上线。（除非应用已**锁定**，请参阅[锁定应用](/zh-cn/guides/panel-apps/using/#锁定应用)，此时在您解锁之前会跳过推送。）

## 后续步骤

- [创建 Panel 应用](/zh-cn/guides/panel-apps/creating/)：更丰富的示例、依赖项以及浅色/深色主题
- [PlaidCloud Git 连接](/zh-cn/guides/connections/plaidcloud-git/)：完整的连接表单、用法和安全模型
- [读取数据和已登录用户](/zh-cn/guides/panel-apps/accessing-data/)：以查看应用的人的身份查询 PlaidCloud 数据
- [仓库](/zh-cn/guides/git/repositories/)：在 PlaidCloud Git 中进行分支、令牌和协作
