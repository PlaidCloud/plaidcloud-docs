---
title: 安装 PlaidXL
description: 在 Windows 或 Mac 上将 PlaidXL 加载项添加到 Excel，找到 PlaidCloud 功能区选项卡，并打开 PlaidXL 任务窗格。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

PlaidXL 每台计算机只需安装一次，无需为每个工作簿分别安装。此后，在您打开的每个工作簿中，Excel 功能区上都会有 **PlaidCloud** 选项卡。

## 开始之前

- 在 Windows 或 Mac 上使用适用于 Microsoft 365 的 Excel，或 Excel 2021 及更高版本。
- 如果您的组织集中管理 Office 加载项，可能需要由 Microsoft 365 管理员为您部署 PlaidXL。如果您无法自行安装加载项，请请他们添加 **PlaidCloud** 加载项。

## 在 Windows 上安装

1. 在 Excel 中，打开**插入 → 加载项**（在某些版本中为**开始 → 加载项**）。
2. 在加载项搜索框中输入 `PlaidCloud`。
3. 选择 **PlaidCloud** 加载项，然后单击**添加**。

## 在 Mac 上安装

1. 在 Excel for Mac 中，打开**插入 → 加载项**。在较早的版本中，该菜单为**插入 → 应用商店**。
2. 在加载项搜索框中输入 `PlaidCloud`。
3. 选择 **PlaidCloud** 加载项，然后单击**添加**。

## 打开任务窗格

1. 单击功能区上的 **PlaidCloud** 选项卡。
2. 在**数据**组中，单击**打开 PlaidXL**。

PlaidXL 任务窗格会在窗口右侧打开，并要求您登录。请继续阅读[登录](/zh-cn/reference/cli/plaidxl/connect/)。

任务窗格在会话之间会保持登录状态，因此您通常只需登录一次，之后需要时打开任务窗格即可。

## 如果 PlaidXL 没有出现

- 关闭所有 Excel 窗口并重新打开 Excel。加载项通常要到 Excel 重新启动后才会显示在功能区上。
- 在**插入 → 我的加载项**（Windows）或**插入 → 加载项 → 我的加载项**（Mac）下查找，并从中选择 **PlaidCloud**。
- 如果您的组织阻止从应用商店获取加载项，请请 Microsoft 365 管理员为您部署。

更多解决办法请参阅[故障排除](/zh-cn/reference/cli/plaidxl/troubleshooting/)页面。

## 相关内容

- [登录](/zh-cn/reference/cli/plaidxl/connect/)——将加载项连接到您的工作区
- [PlaidCloud 功能区](/zh-cn/reference/cli/plaidxl/ribbon/)——**PlaidCloud** 选项卡上的所有命令
