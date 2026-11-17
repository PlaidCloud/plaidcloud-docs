---
title: PlaidCloud Git
description: 在 PlaidCloud 中托管、版本化 Git 存储库并开展协作，内置议题、拉取请求、项目看板、发布和 Wiki，并支持单点登录。
sidebar:
  label: 概览
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git 是内置于工作区的私有 Git 服务。每个工作区都有自己的 Git 服务器，用于存放代码、配置、笔记本和其他任何受版本控制的文件，同时提供团队协作所需的议题、拉取请求和项目看板。

使用 PlaidCloud 账户登录即可，无需另行设置用户名或密码。新建存储库默认为私有，仅对已授予访问权限的成员可见。

## 打开 Git

在工作区的应用列表中选择 **Git**。**Git** 选项卡会显示工作区的主机、您的角色以及 **Repositories** 列表。使用 **View all in Git** 进入 Git 网页界面；如果您可以管理分组，使用 **Manage who can push** 打开分组管理；使用刷新按钮重新加载。使用 **← Back to** your workspace in Git 返回 PlaidCloud。

角色标识会显示您的级别：**Administrator**、**Contributor** 或 **Viewer**，并附有一行说明该级别允许的操作。每个存储库行显示其名称、说明（如有）、带日期的 **已更新**、带复制按钮的只读克隆字段，以及 **打开**，用于在 Git 中打开该存储库。您以私有方式创建的存储库直接位于 Git 中，不在此列表内。

如果工作区尚未设置 Git 或无法连接到 Git，**Git** 选项卡会显示 **Git is not available** 及原因，选择 **重试** 即可再次检查。

## 克隆存储库

从存储库所在行复制其克隆地址。首次复制时会出现 **Set up Git on your computer** 卡片，其中列出以下步骤。选择 **关闭** 可隐藏该卡片，选择页眉中的 **How to clone** 可重新显示。

1. 计算机上必须已安装 Git。
2. 在 **Settings → Applications** 中创建具有 **write:repository** 权限的令牌。卡片中提供指向该页面的链接。
3. 使用所示的两条命令 `git config --global user.name` 和 `user.email` 告知 Git 您的身份，命令中已填入您的姓名和电子邮件。
4. 使用所示的 `git clone` 命令克隆存储库。当 Git 要求输入密码时，粘贴该令牌，而不是 PlaidCloud 密码。

每条命令都有各自的复制按钮。完整步骤请参阅[存储库](/zh-cn/guides/git/repositories/)。复制需要推送权限和已激活的 Git 账户：如果复制按钮处于禁用状态，请先打开任意一个存储库一次以激活账户；如果您是 **查看者**，请按下文所述申请推送权限。

## 访问级别

所有拥有 Git 访问权限的用户都可以读取工作区的共享存储库。另有两个级别允许推送。

| 角色 | 可执行的操作 | 授予方式 |
|---|---|---|
| **查看者** | 查看和克隆共享存储库。 | 每位成员默认拥有。 |
| **Contributor** | 具备读取的全部权限，并可推送到 `apps` 存储库，[Panel](/zh-cn/guides/panel-apps/deploy-from-git/) 和 [Dash](/zh-cn/guides/dash-apps/deploy-from-git/) 应用代码存放在该存储库中。 | **Git Contributors** 安全组。 |
| **Administrator** | 具备 Contributor 的全部权限，并可推送到所有存储库（包括 `udfs`），以及创建组织。 | **Git Administration** 安全组。 |

`udfs` 存储库仅限管理员访问，因为用户定义函数以调用它们的工作流的身份运行。

如果您是 **查看者**，**Git** 选项卡会列出最多三位工作区管理员，您可以请他们将您添加到 **Git Contributors**。

## 来自应用和 UDF 的 Git

Panel 或 Dash 应用的窗口中有一个 **存储库** 部分，显示其存储库、分支和构建状态；能够推送的成员还可使用 **Edit in browser** 和 **Copy clone URL**。Panel Studio 应用以及使用托管 PlaidCloud Git 连接的 App Runner 应用都是 `apps` 存储库中的文件夹，因此其窗口显示的就是该存储库。请参阅[应用的存放位置](/zh-cn/guides/panel-apps/studio/#应用存放位置)。由 Git 支持的 UDF，其工具栏上有 **打开**（在 Git 中打开该分支下的存储库），管理员还可使用 **Edit in browser**。

## 授予 Git 访问权限

工作区管理员在 **身份** 中授予访问权限：将成员添加到某个安全组，或将该权限添加到您自己创建的分组。

1. 将成员添加到 **Git Contributors** 以允许其推送应用代码，或添加到 **Git Administration** 使其成为 Git 管理员。
2. 若要让每位新成员都拥有应用代码的推送权限，请将 **Git Contributors** 添加到默认分组。**Git Administration** 不能作为默认分组。
3. 若要查看成员可执行的操作，请打开该成员并选择 **Git** 选项卡。其中显示该成员的 Git 用户名、级别以及授予该级别的分组。

更改在成员下次登录 Git 或打开 **Git** 选项卡时生效。成员的 Git 账户跟随其 PlaidCloud 成员身份：停用或移除成员后，其 Git 账户（包括令牌和 SSH 密钥）会在大约一小时内被阻止，重新激活后即解除阻止。不会删除任何内容：其存储库和历史记录均予保留。使用单点登录登录 Git 时，打开的是该成员自己的账户。PlaidCloud 支持人员自动拥有 Admin 访问权限。

## 本节内容

- [存储库](/zh-cn/guides/git/repositories/) — 创建存储库，然后克隆、提交并推送您的工作
- [议题](/zh-cn/guides/git/issues/) — 使用标签、里程碑和负责人跟踪任务、缺陷和想法
- [拉取请求](/zh-cn/guides/git/pull-requests/) — 在分支上提出更改，并在合并前进行审核
- [项目看板](/zh-cn/guides/git/projects/) — 在看板上组织议题和拉取请求
- [发布和标签](/zh-cn/guides/git/releases-and-tags/) — 标记并发布存储库的版本化快照
- [Wiki](/zh-cn/guides/git/wikis/) — 将长篇文档与代码放在一起
- [包](/zh-cn/guides/git/packages/) — 从存储库注册表发布和安装构建产物
- [搜索代码](/zh-cn/guides/git/searching-code/) — 在所有存储库中查找代码、议题和拉取请求

## 相关内容

- [从 PlaidCloud Git 部署 Panel 应用](/zh-cn/guides/panel-apps/deploy-from-git/) — 通过无需凭据的托管连接，直接从存储库提供 HoloViz Panel 应用
- [从 PlaidCloud Git 部署 Dash 应用](/zh-cn/guides/dash-apps/deploy-from-git/) — 以相同方式提供 Plotly Dash 应用
- [访问管理](/zh-cn/administration/access/) — 工作区成员身份和安全组如何决定谁可以查看和编辑存储库
