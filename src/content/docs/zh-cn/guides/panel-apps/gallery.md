---
title: 应用库
description: 将 Panel 应用列为工作区可用于起步的模板，并基于已列出的应用创建新应用。
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

应用库是工作区保存现成 Panel 应用的货架。任何可以查看已列出应用所属项目的人，都可以创建自己的副本并进行修改，因此一个好的应用会成为起点，而不必让大家重复构建。

## 从应用库创建应用

1. 在 **我的 Panel 应用** 中，选择 **Create app**。
2. 在 **起始来源** 下，选择 **From the gallery**。
3. 选取一个应用。其说明显示在选择器下方。
4. 为您的应用命名，选择其 **项目**，然后选择 **创建**。

您也可以单独打开应用库，其中每张卡片显示应用的名称、说明和项目，并带有 **Create app from this…**。应用库只列出您可以查看的项目中的应用。

新应用是已列出应用文件的副本。您的副本与原应用相互独立：更改其中一个绝不会更改另一个。

## 列出您的应用

您需要拥有应用所属项目的编辑权限，并且该应用必须是在 [Panel Studio](/zh-cn/guides/panel-apps/studio/) 中创建并已分配到项目的。

1. 在 Studio 中打开应用并选择 **Gallery…**。
2. 输入要显示在应用库卡片上的 **说明**。
3. 选择 **List in gallery** 并确认。

若要更改说明，请选择 **Update listing**。若要移除应用，请选择 **Take out of gallery**。将应用移到另一个项目也会将其从应用库中移出。

## 谁能看到什么

所有可以查看该项目的人都可以读取已列出应用的源代码，包括您之后发布的更改。请勿在已列出应用的文件中放入密码或私人备注。选择列出应用时，系统会先要求您确认这一点，列出操作也会记录在审计日志中。

从应用库创建应用的人只会获得应用自身文件夹中文件的副本。他们永远看不到应用的仓库详情、连接或 webhook 设置。

## 后续步骤

- [Panel Studio](/zh-cn/guides/panel-apps/studio/)：编辑并发布您创建的副本。
- [Panel 应用套件](/zh-cn/guides/panel-apps/app-kit/)：大多数应用库应用所用的组件。
