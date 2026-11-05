---
title: PlaidCloud Git
description: 在 PlaidCloud 中托管、版本化并协作处理 Git 存储库，内置议题、拉取请求、项目看板、发行版和 Wiki，并支持单点登录。
sidebar:
  label: 概览
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git 是内置于工作区的私有 Git 服务。每个工作区都有自己的 Git 服务器，用于存储代码、配置、笔记本和任何其他受版本控制的文件，以及团队围绕这些文件协作所用的议题、拉取请求和项目看板。

使用 PlaidCloud 账户登录即可，无需另行设置用户名或密码。新存储库默认为私有，仅对您授予访问权限的成员可见。

## 打开 Git

在工作区的应用列表中选择 **Git**。**Git** 选项卡显示工作区的存储库，包括每个存储库的名称、描述、默认分支和上次更新时间，顶部有一行文字说明您可以执行的操作。选择某个存储库即可打开它，或选择 **View all in Git** 前往 Git 网页界面。在 Git 中使用 **← Back to** 工作区返回 PlaidCloud。

要克隆存储库，请选择其所在行的 **Copy clone URL**。首次使用时，会有提示说明所需条件：

1. 计算机上必须已安装 Git。
2. 在 Git 的**设置 → 应用程序**下创建访问令牌，并授予 **write:repository** 权限。提示中带有指向该页面的链接。
3. Git 要求输入密码时，粘贴令牌，而不是 PlaidCloud 密码。
4. 运行所示的两条 `git config --global user.name` 和 `user.email` 命令，其中已包含您的姓名和电子邮件。

完整演练请参阅[存储库](/zh-cn/guides/git/repositories/)。如果无法复制克隆 URL，说明您只有读取权限，请参阅下文。

## 访问级别

所有具有 Git 访问权限的用户都可以读取工作区的共享存储库。另有两个级别允许推送。

| 级别 | 您可以执行的操作 | 授予方式 |
|---|---|---|
| **读取** | 查看并克隆共享存储库。 | 每个成员默认拥有。 |
| **Contributor** | 拥有读取级别的全部权限，并可向 `apps` 存储库推送，[Panel](/zh-cn/guides/panel-apps/deploy-from-git/) 和 [Dash](/zh-cn/guides/dash-apps/deploy-from-git/) 应用代码存放在该存储库中。 | **Git Contributors** 安全组。 |
| **管理员** | 拥有 Contributor 级别的全部权限，并可向所有存储库（包括 `udfs`）推送，还可创建组织。 | **Git Administration** 安全组。 |

`udfs` 存储库仅限管理员访问，因为用户定义函数以调用它们的工作流的身份运行。

如果您只有读取权限，**Git** 选项卡会列出最多三位工作区管理员，您可以请他们将您添加到 **Git Contributors**。

## 来自应用和 UDF 的 Git

Panel 或 Dash 应用的窗口中有一个**存储库**部分，显示其存储库、分支和构建状态，可推送的成员还会看到 **Edit in browser** 和 **Copy clone URL**。基于 Git 的 UDF 的工具栏中有 **Open**（在 Git 中打开其分支上的存储库），管理员还有 **Edit in browser**。

## 授予 Git 访问权限

工作区管理员在**身份**中授予访问权限：将成员添加到安全组，或将权限添加到您自己的分组。

1. 将成员添加到 **Git Contributors** 以允许其推送应用代码，或添加到 **Git Administration** 使其成为 Git 管理员。
2. 要让每位新成员都拥有应用代码的推送权限，请将 **Git Contributors** 添加到默认分组。**Git Administration** 不能作为默认分组。
3. 要查看成员可以执行的操作，请打开该成员并选择 **Git** 选项卡。其中显示该成员的 Git 用户名、级别以及授予该级别的分组。

更改会在成员下次登录 Git 或打开 **Git** 选项卡时生效。PlaidCloud 支持人员自动拥有管理员权限。

## 本节内容

- [存储库](/zh-cn/guides/git/repositories/)：创建存储库，然后克隆、提交并推送您的工作
- [议题](/zh-cn/guides/git/issues/)：使用标签、里程碑和负责人跟踪任务、缺陷和想法
- [拉取请求](/zh-cn/guides/git/pull-requests/)：在分支上提出更改，并在合并前进行审阅
- [项目看板](/zh-cn/guides/git/projects/)：在看板上组织议题和拉取请求
- [发行版和标签](/zh-cn/guides/git/releases-and-tags/)：标记并发布存储库的版本化快照
- [Wiki](/zh-cn/guides/git/wikis/)：将长篇文档与代码放在一起
- [包](/zh-cn/guides/git/packages/)：从存储库注册表发布和安装构建产物
- [搜索代码](/zh-cn/guides/git/searching-code/)：在所有存储库中查找代码、议题和拉取请求

## 相关内容

- [从 PlaidCloud Git 部署 Panel 应用](/zh-cn/guides/panel-apps/deploy-from-git/)：通过托管的无凭据连接，直接从存储库提供 HoloViz Panel 应用
- [从 PlaidCloud Git 部署 Dash 应用](/zh-cn/guides/dash-apps/deploy-from-git/)：以相同方式提供 Plotly Dash 应用
- [访问管理](/zh-cn/administration/access/)：工作区成员身份和安全组如何管控谁可以查看和编辑存储库
