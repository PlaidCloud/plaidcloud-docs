---
title: 从 PlaidCloud Git 部署 Panel 应用
description: 在 PlaidCloud 中提供 HoloViz Panel 应用的完整路径：将代码放入 PlaidCloud Git 存储库，通过无需凭据的托管连接进行连接，然后发布上线。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

这是从本机上的 Panel 应用代码到在线 URL 的完整路径，以 **[PlaidCloud Git](/zh-cn/guides/git/)**（工作区内置的托管 Git 服务）作为源。由于 PlaidCloud Git 是托管的，应用用于部署的连接**无需服务器 URL、用户名或令牌**：PlaidCloud 会代您完成身份验证。

共有五个步骤：

1. 编写一个最简 Panel 应用。
2. 将其放入 PlaidCloud Git 存储库。
3. 创建托管的 PlaidCloud Git 连接。
4. 发布指向该存储库的服务器应用。
5. 打开已提供服务的应用；如果无法启动，请查看构建日志。

每个步骤都链接到相应部分的深入指南；本页将它们串联成一条完整路径。

## 开始之前

- 在工作区中打开 **Git**，确认可以访问 PlaidCloud Git。默认情况下，工作区的组织包含一个 **`apps`** 存储库（以及一个 **`udfs`** 存储库），apps 是存放 Panel 应用的自然之选。
- 如果要从本机推送代码，请在本地安装 `git`（也可以在 Git 网页界面中添加文件）。

## 1. 编写最简 Panel 应用

应用需要一个**入口点**，即构建 Panel 应用并将其标记为 `.servable()` 的 Python 文件；还可以选择在存储库根目录或入口点旁边放置 **`requirements.txt`**，用于列出额外的包。

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

这就是一个完整的应用，PlaidCloud 提供服务的正是 `.servable()` 调用。`panel`、`bokeh` 以及 PlaidCloud 客户端库（`plaidcloud-rpc`、`plaidcloud-utilities`）均已预装，因此 `requirements.txt` 中只需列出*额外*的包。有关更丰富的示例、依赖项以及浅色/深色主题，请参阅[创建 Panel 应用](/zh-cn/guides/panel-apps/creating/)。

## 2. 将应用放入 PlaidCloud Git 存储库

使用工作区现有的 **`apps`** 存储库，或[创建新存储库](/zh-cn/guides/git/repositories/#创建存储库)，然后将代码放入其中。

由于通过 PlaidCloud 登录，您的 Git 账户没有单独的密码：请[生成个人访问令牌](/zh-cn/guides/git/repositories/#生成个人访问令牌)（**您的头像 → 设置 → 应用程序**），授予 **write:repository** 权限，并在 Git 提示时将其用作密码。向 `apps` 推送需要 **Contributor** 权限；如果 **Git** 选项卡显示您只有读取权限，请让工作区管理员将您添加到 **Git Contributors**。在 **Git** 选项卡中选择该存储库的 **Copy clone URL**，然后执行：

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

记下存储库路径 `<org>/apps`，其中 `<org>` 是工作区的组织名称。下一步将输入该路径。完整的克隆、提交和推送说明请参阅[存储库](/zh-cn/guides/git/repositories/)。

> **此处的令牌仅用于*您*推送代码。** 接下来创建的连接是托管的，无需令牌，请不要将两者混淆。

## 3. 创建托管的 PlaidCloud Git 连接

**连接**用于告诉 Panel 部署其代码所在的位置。对于 PlaidCloud Git，连接是*托管*的：PlaidCloud 提供主机和凭据，因此只需输入存储库目标。

1. 打开 **Tools > Connections**，单击**新建连接**，然后选择 **PlaidCloud Git**。
2. 为连接指定**账户名称**（例如 `Apps Repo`）。
3. 将 **Repository Path** 设置为 `<org>/apps`（即第 2 步中记下的路径），将**默认分支**设置为 `main`。除非应用位于子目录中，否则请将**起始路径**留空。
4. 单击**创建**。

没有服务器 URL、用户、密码或 SSL/SSH 字段：PlaidCloud Git 是托管的，主机和身份验证由平台处理。有关完整表单，包括连接的**用法**和**安全模型**（工作区中谁可以使用它），请参阅 [PlaidCloud Git 连接](/zh-cn/guides/connections/plaidcloud-git/)。

> **使用的是较旧的工作区版本？** 如果表单中仍显示服务器 URL 或凭据字段，请将其留空，无论哪种情况，平台都会代您完成身份验证。

## 4. 发布服务器应用

现在让服务器部署指向该连接。

1. 打开**我的 Panel 应用**，单击**新建服务器应用**。
2. 在**目录设置**下，设置**应用名称**和 **URL 标识**。URL 标识既是应用的 URL，也是内部名称，因此请使用小写字母、数字和连字符，以字母开头，不超过 40 个字符（例如 `hello-panel`）。
3. 在 **Git 连接和发布监视器**下：
   - **Git 连接**：在第 3 步中创建的 PlaidCloud Git 连接。
   - **分支**：`main`。向该分支推送会自动重新构建并重新部署应用。
   - **入口点**：`app.py`。
4. 在**运行时**下，选择 **CPU**、**内存**、**设计**（**FAST** 为 PlaidCloud 的现代外观）以及**空闲**时间窗口。仅当应用应允许未登录访问时，才勾选**允许公共访问**。
5. 单击**发布**。

此对话框中的每个字段都在[创建 Panel 应用](/zh-cn/guides/panel-apps/creating/#发布应用)中有说明。

## 5. 打开应用；如果无法启动，请查看日志

发布后，应用会进行**构建**：PlaidCloud 克隆该分支，安装 `requirements.txt` 中的依赖（存储库根目录和应用文件夹中的，如果存在），并构建容器镜像。其**状态**显示在**我的 Panel 应用**列表中，并自动更新。

- 当状态为**就绪**时，在 `https://<your-tenant-host>/serve/<slug>/` 打开应用。空闲后的第一次请求会将其启动（约 15 秒）。
- 如果构建失败，请打开应用并查看其**构建**日志，缺少依赖或导入错误会在其中显示。有关各状态的含义、如何查看日志以及如何触发重新构建，请参阅[使用 Panel 应用](/zh-cn/guides/panel-apps/using/)。

此后，**每次向连接的分支推送都会自动重新构建并重新部署应用**：编辑 `app.py`，执行 `git push`，更改即可上线。（除非应用已被**锁定**（请参阅[锁定应用](/zh-cn/guides/panel-apps/using/#锁定应用)），此时会跳过推送，直到解锁。）

## 后续步骤

- [创建 Panel 应用](/zh-cn/guides/panel-apps/creating/)：更丰富的示例、依赖项以及浅色/深色主题
- [PlaidCloud Git 连接](/zh-cn/guides/connections/plaidcloud-git/)：完整的连接表单、用法和安全模型
- [读取数据和已登录用户](/zh-cn/guides/panel-apps/accessing-data/)：以查看应用者的身份查询 PlaidCloud 数据
- [存储库](/zh-cn/guides/git/repositories/)：在 PlaidCloud Git 中使用分支、令牌和协作
