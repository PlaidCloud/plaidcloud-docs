---
title: PlaidCloud Git
description: 在 PlaidCloud 内托管、版本管理 Git 存储库并协作，内置议题、拉取请求、项目看板、发布和 Wiki，并集成单点登录。
sidebar:
  label: 概述
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git 是内置于工作区的私有 Git 服务。每个工作区都有自己的 Git 服务器，用于存储代码、配置、笔记本以及任何其他受版本控制的文件，同时提供团队协作所用的议题、拉取请求和项目看板。

使用 PlaidCloud 账户登录，无需另行设置用户名或密码。从工作区打开 **Git**，即已登录。新存储库默认为私有，仅对您授予访问权限的成员可见。

## 管理 Git

任何成员都可以创建存储库，但**创建组织**（将存储库和团队归并在一起的共享空间）需要 **Git Administration** 权限。在**身份**中授予该权限，方法是将权限添加到安全组，或将成员添加到内置的 **Git Administration** 组。属于拥有该权限的组的任何人，在下次登录 Git 时都会成为 Git 管理员。PlaidCloud 支持人员自动拥有该权限。

如果新获授权的管理员以前从未打开过 Git，可能需要登录 Git **两次**才能使管理员访问权限生效：第一次登录会创建其 Git 账户，权限在下一次登录时应用。

## 本节内容

- [存储库](/zh-cn/guides/git/repositories/)：创建存储库，然后克隆、提交和推送您的工作
- [议题](/zh-cn/guides/git/issues/)：使用标签、里程碑和负责人跟踪任务、缺陷和想法
- [拉取请求](/zh-cn/guides/git/pull-requests/)：在分支上提出更改，并在合并之前进行审查
- [项目看板](/zh-cn/guides/git/projects/)：在看板上组织议题和拉取请求
- [发布和标签](/zh-cn/guides/git/releases-and-tags/)：标记并发布存储库的版本化快照
- [Wiki](/zh-cn/guides/git/wikis/)：将长篇文档与代码放在一起
- [包](/zh-cn/guides/git/packages/)：从存储库注册表发布和安装构建工件
- [搜索代码](/zh-cn/guides/git/searching-code/)：在所有存储库中查找代码、议题和拉取请求

## 相关内容

- [从 PlaidCloud Git 部署 Panel 应用](/zh-cn/guides/panel-apps/deploy-from-git/)：通过受管的免凭据连接，直接从存储库提供 HoloViz Panel 应用
- [从 PlaidCloud Git 部署 Dash 应用](/zh-cn/guides/dash-apps/deploy-from-git/)：以同样的方式提供 Plotly Dash 应用
- [访问管理](/zh-cn/administration/access/)：工作区成员资格和安全组如何控制谁可以查看和编辑存储库
