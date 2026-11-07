---
title: PlaidCloud Git
description: 在 PlaidCloud 内托管、版本管理 Git 存储库并进行协作，内置问题、拉取请求、项目看板、发布和 Wiki，并集成单点登录。
sidebar:
  label: 概览
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git 是内置于工作区的私有 Git 服务。每个工作区都有自己的 Git 服务器，用于存储代码、配置、笔记本和任何其他受版本控制的文件，以及团队用来围绕这些文件协作的问题、拉取请求和项目看板。

使用 PlaidCloud 账户登录，因此无需另行设置用户名或密码。新存储库默认为私有，仅对获得访问权限的成员可见。

## 打开 Git

在工作区的应用列表中选择 **Git**。**Git** 选项卡会显示工作区的主机、您的角色和**存储库**列表。使用 **View all in Git** 进入 Git 网页界面；如果您可以管理分组，使用 **Manage who can push** 打开分组管理；使用刷新按钮重新加载。使用 Git 中的 **← Back to** 加工作区名称返回 PlaidCloud。

角色标识显示您的级别：**Administrator**、**Contributor** 或**查看者**，并附有一行说明该级别允许您执行的操作。每个存储库行显示其名称、说明（如有）、带日期的**已更新**、带复制按钮的只读克隆字段，以及在 Git 中打开该存储库的**打开**。您私下创建的存储库直接在 Git 中查看，不会出现在此列表中。

## 克隆存储库

从存储库所在行复制其克隆地址。首次复制时，会出现 **Set up Git on your computer** 卡片，其中包含以下步骤。选择**关闭**可将其隐藏，选择页眉中的 **How to clone** 可重新显示。

1. 计算机上必须已安装 Git。
2. 在 **设置 → 应用程序** 中创建令牌，并授予 **write:repository** 权限。卡片中提供了指向该页面的链接。
3. 使用所示的 `git config --global user.name` 和 `user.email` 两条命令告知 Git 您的身份，这两条命令中已填入您的姓名和电子邮件。
4. 使用所示的 `git clone` 命令克隆存储库。Git 要求输入密码时，请粘贴该令牌，而不是 PlaidCloud 密码。

每条命令都有各自的复制按钮。有关完整说明，请参阅[存储库](/zh-cn/guides/git/repositories/)。复制需要推送权限和已激活的 Git 账户：如果复制按钮被禁用，请先打开任意存储库一次以激活账户；如果您是**查看者**，请按下文所述申请推送权限。

## 访问级别

拥有 Git 访问权限的所有人都可以读取工作区的共享存储库。另有两个级别允许推送。

| 角色 | 可执行的操作 | 授予方式 |
|---|---|---|
| **查看者** | 查看和克隆共享存储库。 | 每个成员默认拥有。 |
| **Contributor** | 拥有读取的全部权限，并可推送到 `apps` 存储库，[Panel](/zh-cn/guides/panel-apps/deploy-from-git/) 和 [Dash](/zh-cn/guides/dash-apps/deploy-from-git/) 应用代码存放在该存储库中。 | **Git Contributors** 安全组。 |
| **Administrator** | 拥有 Contributor 的全部权限，并可推送到所有存储库（包括 `udfs`），还可创建组织。 | **Git Administration** 安全组。 |

`udfs` 存储库仅限管理员使用，因为用户定义函数会以调用它的工作流的身份运行。

如果您是**查看者**，**Git** 选项卡会列出最多三位工作区管理员，您可以请他们将您添加到 **Git Contributors**。

## 从应用和 UDF 使用 Git

Panel 或 Dash 应用的窗口中有一个**存储库**部分，显示其存储库、分支和构建状态，能够推送的成员可使用 **Edit in browser** 和 **Copy clone URL**。基于 Git 的 UDF 的工具栏上有**打开**（在 Git 中打开该分支对应的存储库）以及供管理员使用的 **Edit in browser**。

## 授予 Git 访问权限

工作区管理员在**身份**中授予访问权限：将成员添加到安全组，或将权限添加到您自己的分组。

1. 将成员添加到 **Git Contributors** 以允许其推送应用代码，或添加到 **Git Administration** 使其成为 Git 管理员。
2. 若要让每位新成员都拥有应用代码的推送权限，请将 **Git Contributors** 添加到默认分组。**Git Administration** 不能作为默认分组。
3. 若要查看成员可执行的操作，请打开该成员并选择 **Git** 选项卡。其中会显示该成员的 Git 用户名、级别以及授予该级别的分组。

更改会在成员下次登录 Git 或打开 **Git** 选项卡时生效。停用或移除成员会封禁其 Git 账户，包括其令牌和 SSH 密钥；重新启用该成员会解除封禁。PlaidCloud 支持人员自动拥有管理员访问权限。

## 本节内容

- [存储库](/zh-cn/guides/git/repositories/)：创建存储库，然后克隆、提交和推送您的工作
- [问题](/zh-cn/guides/git/issues/)：使用标签、里程碑和负责人跟踪任务、缺陷和想法
- [拉取请求](/zh-cn/guides/git/pull-requests/)：在分支上提出更改，并在合并前进行审阅
- [项目看板](/zh-cn/guides/git/projects/)：在看板上组织问题和拉取请求
- [发布和标签](/zh-cn/guides/git/releases-and-tags/)：标记并发布存储库的版本化快照
- [Wiki](/zh-cn/guides/git/wikis/)：将长篇文档与代码放在一起
- [包](/zh-cn/guides/git/packages/)：从存储库注册表发布和安装构建产物
- [搜索代码](/zh-cn/guides/git/searching-code/)：在您的存储库中查找代码、问题和拉取请求

## 相关内容

- [从 PlaidCloud Git 部署 Panel 应用](/zh-cn/guides/panel-apps/deploy-from-git/)：直接从存储库提供 HoloViz Panel 应用服务，使用无需凭据的托管连接
- [从 PlaidCloud Git 部署 Dash 应用](/zh-cn/guides/dash-apps/deploy-from-git/)：以同样方式提供 Plotly Dash 应用服务
- [访问管理](/zh-cn/administration/access/)：工作区成员身份和安全组如何管控谁可以查看和编辑存储库
