---
title: Panel Studio
description: 无需离开 PlaidCloud 即可创建、编辑、预览和发布 Panel 应用，然后还原到较早的版本、查看应用的使用情况和速度、设置警报和摘要、将其列入应用库，并固定到主页。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio 是 PlaidCloud 内用于 Panel 应用的编辑器。它在编辑器旁边显示应用的文件，构建您可以打开的私有预览，并在您准备好时发布应用。无需 git 仓库即可开始。

## 打开 Panel Studio

- 在项目的 **主页** 看板上，选择 Panel 应用上的 **Open in Studio**。
- 在 **我的 Panel 应用** 中，选择应用所在行上的 **Open in Studio**。

若要开始新应用，请在任一位置选择 **Create app**。

## 创建应用

**Create app** 对话框提供五种起点：

| 起始来源 | 您将获得 |
|---|---|
| **Blank** | 一个包含 `app.py` 和 `requirements.txt` 的最简应用。 |
| **表** | 基于您所选表构建的应用。 |
| **视图** | 同样，但基于项目视图构建。 |
| **模板** | 来自 [Panel 应用套件](/zh-cn/guides/panel-apps/app-kit/#从模板开始)的现成应用。 |
| **From the gallery** | 工作区已列入[应用库](/zh-cn/guides/panel-apps/gallery/)的应用的副本。 |

为应用命名，选择其 **项目**，然后选择 **创建**。Studio 会打开新应用，文件列在左侧。

## 编辑

在列表中选取一个文件，即可在编辑器中编辑。在 `requirements.txt` 中列出 Python 依赖项，每行一个包。它们会在应用构建时安装。

选择 **Ask Weave**，让 Weave 为您编写或更改应用。请参阅[使用 Weave 构建 Panel 应用](/zh-cn/guides/panel-apps/build-with-weave/)。

## 保存、预览和发布

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="保存会保留一份只有您能看到的草稿。预览会为编辑者构建草稿的私有副本。确认后，发布会替换线上应用。" style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">保存</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">仅草稿</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">预览</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">仅编辑者</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">发布</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">线上应用</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">只有在发布后，您的编辑才会到达查看者。</figcaption>
</figure>

### 保存

**保存** 会将更改存为草稿。线上应用不会改变，其他人也看不到草稿。

### 预览

**预览** 会将已保存的草稿构建为私有副本并打开。只有应用的编辑者可以打开预览。

- 预览在 24 小时内没有保存则会被移除。
- 一个工作区同时最多可以有 10 个预览。
- 再次保存并选择 **预览**，即可看到最新的编辑。

### 发布

**发布** 会用已保存的草稿替换线上应用。它需要应用所属项目的编辑权限，Studio 会先要求您确认。

如果在您打开应用之后有其他人发布了更改，Studio 会报告冲突，而不是覆盖他们的工作。请重新加载应用，将您的编辑合并进来，然后再次发布。

## 构建状态和错误

**构建** 选项卡显示最新构建的状态，并在运行时更新。构建失败时，该选项卡会列出每个错误及其文件和行号，方便您直接跳转到相应行。`requirements.txt` 中的依赖项问题会附带修复提示。

错误和警告也会标记在编辑器中的对应行上，让您在问题所在位置看到它。

有关应用发布后各状态的含义，请参阅[使用 Panel 应用](/zh-cn/guides/panel-apps/using/#构建状态服务器应用)。

## 历史记录和还原

**历史记录** 选项卡按从新到旧的顺序列出应用的每个已发布版本及其构建状态。选择 **加载更多** 可查看更早的版本。

若要回到较早的版本，请在其上选择 **还原** 并确认。还原后的版本会成为线上应用并重新构建。您未保存的草稿不会丢失：它保留在草稿中，并在您下次发布时叠加在还原后的版本之上上线。如果应用已与该版本一致，Studio 会提示并且不做任何更改。如果在您还原期间有人发布了内容，Studio 不会还原任何内容，并请您重试。

## 洞察

**洞察** 选项卡显示人们如何使用应用以及应用的响应速度。可选择最近 7、14 或 30 天。

| 部分 | 显示内容 |
|---|---|
| **Views per day** | 应用每天被打开的次数。 |
| **Page load** | 加载时间的中位数，以及 95% 的加载所快于的时间，取自该期间的页面加载。 |
| **Slowest queries** | 耗时最长的查询，以及其运行频率及中位数、慢端和最慢耗时。 |
| **错误** | 该期间出了什么问题，按错误类型及其在应用中发生的位置划分。 |

当某个期间的活动量超出洞察所能读取的范围时，它会说明数据不完整。当页面加载超出应用的[性能预算](/zh-cn/guides/panel-apps/app-kit/#性能预算)时，洞察会警告您有多少次超出以及哪些查询较慢。洞察从不显示查询返回的数据，也不显示打开应用的人的姓名。

两个选项卡都要求应用已分配到项目；未分配的应用会显示分配提示。

## 警报和摘要

选择 **Alerts & Digests** 可设置通知，用于监视应用数据中的某个数值并在其越过限值时通知您，或按计划发送摘要。请参阅[警报和摘要](/zh-cn/guides/panel-apps/alerts-and-digests/)。

## 将应用列入应用库

选择 **Gallery…** 可将应用列为模板，让任何可以查看其项目的人都能据此创建自己的应用，也可以将其从应用库中移出。请参阅[应用库](/zh-cn/guides/panel-apps/gallery/)。

## 固定到主页

选择 **Pin to Home** 可将应用添加到项目的 **主页** 看板，选择 **Unpin from Home** 则将其移除。

## 删除应用

删除 Panel 应用时会先要求您确认。在 **我的 Panel 应用** 中，使用应用所在行上的 **减号** 图标。取消发布也会要求您确认。

## 后续步骤

- [使用 Weave 构建 Panel 应用](/zh-cn/guides/panel-apps/build-with-weave/)：描述应用并批准具体的更改。
- [Panel 应用套件](/zh-cn/guides/panel-apps/app-kit/)：Studio 的表、视图和模板起点所使用的组件。
- [警报和摘要](/zh-cn/guides/panel-apps/alerts-and-digests/)：在数值越过限值时或按计划通知相关人员。
- [应用库](/zh-cn/guides/panel-apps/gallery/)：将应用作为他人的起点进行共享。
- [使用 Panel 应用](/zh-cn/guides/panel-apps/using/)：发布后的日志、使用情况和重新构建。
