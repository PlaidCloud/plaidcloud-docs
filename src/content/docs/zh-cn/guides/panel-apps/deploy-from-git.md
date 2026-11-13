---
title: 从 PlaidCloud Git 部署 Panel 应用
description: 在 PlaidCloud 中提供 HoloViz Panel 应用的完整路径：将代码放入 PlaidCloud Git 存储库，通过无需凭据的托管连接进行连接，然后发布上线。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

本文介绍从本机上的 Panel 应用代码到线上 URL 的完整路径，以 **[PlaidCloud Git](/zh-cn/guides/git/)**（内置于工作区的托管 Git 服务）作为源。由于 PlaidCloud Git 是托管的，应用部署所用的连接**无需服务器 URL、用户名或令牌**：PlaidCloud 会代您完成身份验证。

共分五个步骤：

1. 编写一个最简 Panel 应用。
2. 将其放入 PlaidCloud Git 存储库。
3. 创建托管的 PlaidCloud Git 连接。
4. 发布指向该存储库的服务器应用。
5. 打开已提供服务的应用，如果无法启动，请查看构建日志。

每个步骤都链接到相应部分的详细指南；本文将它们串联成一条完整的路径。

## 开始之前

- 在工作区中打开 **Git**，确认可以访问 PlaidCloud Git。默认情况下，工作区的组织包含一个 **`apps`** 存储库（以及一个 **`udfs`** 存储库），这是存放 Panel 应用的理想位置。
- 如果想从本机推送代码，请在本地安装 `git`（也可以在 Git 网页界面中添加文件）。

## 1. 编写最简 Panel 应用

应用需要一个**入口点**，即构建 Panel 应用并将其标记为 `.servable()` 的 Python 文件；另外可以选择提供 **`requirements.txt`** 以安装额外的包，它可以位于存储库根目录，也可以与入口点放在一起。

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

这就是一个完整的应用，PlaidCloud 提供服务的正是 `.servable()` 调用。`panel`、`bokeh` 以及 PlaidCloud 客户端库（`plaidcloud-rpc`、`plaidcloud-utilities`）均已预装，因此在 `requirements.txt` 中只需列出*额外*的包。更丰富的示例、依赖项以及浅色/深色主题，请参阅[创建 Panel 应用](/zh-cn/guides/panel-apps/creating/)。

## 2. 将应用放入 PlaidCloud Git 存储库

使用工作区现有的 **`apps`** 存储库，或[新建一个](/zh-cn/guides/git/repositories/#创建存储库)，然后将代码放入其中。在 [Panel Studio](/zh-cn/guides/panel-apps/studio/#应用的存放位置) 中构建的应用已经是 `apps` 中的文件夹，因此您会在那里看到它们与您的应用并列。

由于您通过 PlaidCloud 登录，您的 Git 账户没有单独的密码，请[生成个人访问令牌](/zh-cn/guides/git/repositories/#生成个人访问令牌)（**头像 → Settings → Applications**），授予 **write:repository** 权限，并在 Git 提示输入密码时使用该令牌。推送到 `apps` 需要 **Contributor** 访问权限；如果 **Git** 选项卡显示您是 **查看者**，请让工作区管理员将您添加到 **Git Contributors**。使用 **Git** 选项卡中存储库克隆地址旁的复制按钮，然后执行：

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

记下存储库路径 `<org>/apps`，其中 `<org>` 是工作区的组织名称。下一步将输入该路径。完整的克隆、提交和推送说明请参阅[存储库](/zh-cn/guides/git/repositories/)。

> **此处的令牌仅用于*您自己*推送代码。** 接下来创建的连接是托管的，不需要令牌，请勿混淆两者。

## 3. 创建托管的 PlaidCloud Git 连接

**连接**告诉 Panel 部署其代码所在的位置。对于 PlaidCloud Git，该连接是*托管*的：PlaidCloud 提供主机和凭据，因此只需输入存储库目标。

1. 打开 **Tools > Connections**，单击 **新建连接**，然后选择 **PlaidCloud Git**。
2. 为连接指定 **账户名称**（例如 `Apps Repo`）。
3. 将 **Repository Path** 设置为 `<org>/apps`（即您在步骤 2 中记下的路径），将 **默认分支** 设置为 `main`。除非应用位于子目录中，否则请将 **起始路径** 留空。
4. 单击 **创建**。

没有服务器 URL、用户、密码或 SSL/SSH 字段：PlaidCloud Git 是托管的，由平台处理主机和身份验证。完整的表单说明（包括连接的 **用法** 和 **安全模型**，即工作区中谁可以使用它）请参阅 [PlaidCloud Git 连接](/zh-cn/guides/connections/plaidcloud-git/)。

> **使用的是较旧的工作区版本？** 如果表单仍显示服务器 URL 或凭据字段，请将其留空，无论如何平台都会代您完成身份验证。

## 4. 发布服务器应用

现在让服务器部署指向该连接。

1. 打开 **我的 Panel 应用** 并单击 **新建服务器应用**。
2. 在 **目录设置** 下，设置 **应用名称** 和 **URL 标识**。标识即应用的 URL 和内部名称，因此请使用小写字母、数字和连字符，以字母开头，长度不超过 40 个字符（例如 `hello-panel`）。
3. 在 **Git 连接和发布监视器** 下：
   - **Git 连接**：您在步骤 3 中创建的 PlaidCloud Git 连接。
   - **分支**：`main`。推送到该分支会自动重新构建并重新部署应用。
   - **入口点**：`app.py`。
4. 在 **运行时** 下，选择 **CPU**、**内存**、**设计**（选择 **FAST** 可获得 PlaidCloud 的现代外观）和 **Idle** 窗口。仅当应用应无需登录即可访问时，才勾选 **允许公共访问**。
5. 单击 **发布**。

此对话框中的每个字段都在[创建 Panel 应用](/zh-cn/guides/panel-apps/creating/#发布应用)中有说明。

## 5. 打开应用，如果无法启动则查看日志

发布后，应用开始**构建**：PlaidCloud 克隆该分支，安装 `requirements.txt`（如果存在，包括存储库根目录和应用文件夹中的），并构建容器映像。其 **状态** 显示在 **我的 Panel 应用** 列表中，并自动更新。

- 当状态为 **就绪** 时，可通过 `https://<your-tenant-host>/serve/<slug>/` 打开应用。空闲一段时间后的首次请求会启动应用（约 15 秒）。
- 如果构建失败，请打开应用并查看其 **构建** 日志，缺少依赖项或导入错误会显示在其中。各状态的含义、如何读取日志以及如何触发重新构建，请参阅[使用 Panel 应用](/zh-cn/guides/panel-apps/using/)。

此后，**每次推送到连接的分支都会自动重新构建并重新部署应用**：编辑 `app.py`，执行 `git push`，更改即可上线。（除非应用已被**锁定**，请参阅[锁定应用](/zh-cn/guides/panel-apps/using/#锁定应用)，此时在解锁之前会跳过推送。）

## 后续步骤

- [创建 Panel 应用](/zh-cn/guides/panel-apps/creating/) — 更丰富的示例、依赖项以及浅色/深色主题
- [PlaidCloud Git 连接](/zh-cn/guides/connections/plaidcloud-git/) — 完整的连接表单、用法和安全模型
- [读取数据和已登录用户](/zh-cn/guides/panel-apps/accessing-data/) — 以查看应用者的身份查询 PlaidCloud 数据
- [存储库](/zh-cn/guides/git/repositories/) — 在 PlaidCloud Git 中管理分支、令牌并开展协作
