---
title: 使用 Weave 构建 Panel 应用
description: 描述您想要的应用，让 Weave 在 Panel Studio 中编写，并在保存任何内容之前批准具体的更改。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/build-with-weave.md
---

Weave 可以为您编写和更改 Panel 应用。它在 [Panel Studio](/zh-cn/guides/panel-apps/studio/) 中针对您打开的应用工作，在您批准之前，它提出的任何建议都不会更改应用。

## 向 Weave 提问

1. 在 Panel Studio 中打开应用。
2. 选择 **Ask Weave**，并描述您的需求，例如“添加区域筛选器和按月收入图表”。

Weave 已经了解它正在处理的应用：应用的文件、构建状态和任何构建错误，以及应用所基于的表或视图。您无需将代码或错误粘贴到对话中。如果构建失败，请让 Weave 修复。

## 批准更改

当 Weave 想要更改应用的代码时，会显示一张审批卡片，其中包含完整的差异：逐个文件列出它添加和删除的每一行。

1. 阅读差异。
2. 选择 **批准** 将更改保存到应用的草稿，或选择 **拒绝** 放弃更改。

批准只是保存草稿，不会发布。预览结果，满意后再[发布](/zh-cn/guides/panel-apps/studio/#发布)。

### 仅限网页端批准

您只能在网页版 PlaidCloud 中批准代码更改。在 PlaidCloud 移动应用中，您可以拒绝建议的代码更改，但不能批准。Weave 的其他更改仍可在手机上批准。请参阅[移动端的 Weave](/zh-cn/guides/mobile-app/weave-on-mobile/)。

## 后续步骤

- [Panel Studio](/zh-cn/guides/panel-apps/studio/)：保存、预览和发布。
- [Panel 应用套件](/zh-cn/guides/panel-apps/app-kit/)：Weave 用来构建应用的组件。
