---
title: Panel Studio
description: 无需离开 PlaidCloud 即可创建、编辑、预览和发布 Panel 应用，还可还原早期版本、查看应用的使用情况和速度、设置提醒与摘要、将其列入应用库并固定到主页。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio 是 PlaidCloud 中 Panel 应用的编辑器。它在编辑器旁显示应用的文件，构建可供打开的私有预览，并在准备就绪时发布应用。开始使用时无需 Git 存储库。

## 打开 Panel Studio

- 在项目的 **主页** 看板上，对某个 Panel 应用选择 **在 Studio 中打开**。
- 在 **我的 Panel 应用** 中，在应用所在行选择 **Studio**。

要开始新建应用，请选择 **新建 Studio 应用**。它是 **我的 Panel 应用** 工具栏中的第一个按钮，也位于项目 **主页** 选项卡的 **Panel 应用** 框中。若要基于某个表构建应用，请在项目的 **表** 选项卡上选择该表，然后选择 **创建 Panel 应用**。

## 创建应用

**新建 Studio 应用** 对话框提供五种起始来源：

| 起始来源 | 您将获得 |
|---|---|
| **空白应用** | 包含 `app.py` 和 `requirements.txt` 的最简应用。 |
| **来自表** | 基于所选表构建的应用。 |
| **来自视图** | 同上，基于项目视图构建。 |
| **来自另一个 Studio 应用** | 您的某个 Studio 应用的副本。 |
| **来自应用库** | 工作区已列入[应用库](/zh-cn/guides/panel-apps/gallery/)的某个应用的副本。 |

为应用命名，选择其 **项目**，然后选择 **创建**。Studio 会打开新应用，文件列在左侧。对于表或视图，Weave 用于构建应用首页的提示已准备好发送。请参阅[创建 Panel 应用](/zh-cn/guides/panel-apps/creating/)。

## 应用的存放位置

Studio 应用是工作区 `apps` 存储库（位于 [PlaidCloud Git](/zh-cn/guides/git/) 中，您的其他 Panel 应用也存放在同一存储库）内以应用命名的文件夹（`<app-slug>/`）。Studio 不会为应用单独创建存储库，因此您可以在 `apps` 中与其他应用一起查找和编辑其源代码。

- **草稿分支。** 尚未上线的工作保存在名为 `studio-<app-slug>` 的分支上。**发布** 会将该分支上应用的文件夹复制到主分支。
- **重新构建。** 仅当某个应用的文件夹或存储库根目录的 `requirements.txt` 发生更改时，推送到 `apps` 才会重新构建该应用。
- **现有应用。** 原本位于独立存储库中的 Studio 应用会自动移入其文件夹。旧存储库会被归档：它会保留为只读，永远不会被删除。

## 编辑

在列表中选择一个文件即可在编辑器中编辑。请在 `requirements.txt` 中列出 Python 依赖项，每行一个包。应用构建时会安装这些依赖项。

选择 **询问 Weave**，让 Weave 为您编写或修改应用。请参阅[使用 Weave 构建 Panel 应用](/zh-cn/guides/panel-apps/build-with-weave/)。

## 保存、预览和发布

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="保存会保留仅您自己可见的草稿。预览会为编辑器构建草稿的私有副本。确认后，发布会替换线上应用。" style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">保存</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">仅草稿</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">预览</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">仅编辑器</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">发布</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">线上应用</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">只有发布后，您的编辑才会到达查看者。</figcaption>
</figure>

### 保存

**保存** 会将您的更改存为草稿。线上应用不会改变，其他人也看不到该草稿。

### 预览

**预览** 会将已保存的草稿构建为私有副本并打开。只有应用的编辑者才能打开预览。

- 预览在 24 小时内没有保存操作后会被移除。
- 一个工作区同时最多可以有 10 个预览。
- 再次保存并选择 **预览**，即可查看最新的编辑内容。

### 发布

**发布** 会用已保存的草稿替换线上应用。这需要对应用所属项目具有编辑权限，Studio 会先请您确认。

如果在您打开应用之后有其他人发布了更改，Studio 会报告冲突，而不是覆盖对方的工作。请重新加载应用，将您的编辑合并过来，然后再次发布。

## 构建状态和错误

**构建** 选项卡显示最新构建的状态，并在构建过程中实时更新。构建失败时，该选项卡会列出每个错误及其文件和行号，方便您直接跳转到对应行。`requirements.txt` 中的依赖项问题会附带修复提示。

错误和警告也会标记在编辑器中对应的行上，让您在问题所在之处就能看到它。

应用发布后各状态的含义，请参阅[使用 Panel 应用](/zh-cn/guides/panel-apps/using/#构建状态服务器应用)。

## 历史记录和还原

**历史记录** 选项卡按从新到旧的顺序列出应用的每个已发布版本及其构建状态。选择 **加载更多** 可查看更早的版本。

要回到较早的版本，请在该版本上选择 **还原** 并确认。还原后的版本成为线上应用并重新构建。您未保存的草稿不会丢失：它保留在草稿中，并在您下次发布时叠加在还原后的版本之上上线。如果应用已与该版本一致，Studio 会提示这一点，不做任何更改。如果在您还原期间有其他人进行了发布，Studio 不会还原任何内容，并请您重试。

## 洞察

**洞察** 选项卡显示用户如何使用应用以及应用的响应速度。可选择最近 7 天、14 天或 30 天。

| 部分 | 显示内容 |
|---|---|
| **每日浏览量** | 应用每天被打开的次数。 |
| **页面加载** | 该期间页面加载的中位加载时间，以及 95% 的加载所快于的时间。 |
| **最慢的查询** | 耗时最长的查询，以及它们的运行频率及其中位、慢端和最慢耗时。 |
| **错误** | 该期间出现的问题，按错误类型和发生在应用中的位置划分。 |

如果某个期间的活动量超出洞察所能读取的范围，会提示数据不完整。当页面加载超出应用的[性能预算](/zh-cn/guides/panel-apps/app-kit/#性能预算)时，洞察会警告您有多少次超出以及哪些查询较慢。洞察绝不会显示查询返回的数据，也不会显示打开应用的人员姓名。

**历史记录** 和 **洞察** 选项卡要求应用已分配给某个项目；未分配的应用会显示分配提示。

## 提醒与摘要

选择 **提醒与摘要**，可设置通知：监视应用数据中的某个数字，在其越过限值时通知您，或按计划发送摘要。请参阅[提醒与摘要](/zh-cn/guides/panel-apps/alerts-and-digests/)。

## 将应用列入应用库

在 Studio 中选择 **应用库…**。选择 **在应用库中列出**，可将应用列为模板，任何能查看其项目的人都可以据此创建自己的应用；选择 **从应用库中移除** 可将其移除。该按钮适用于属于某个项目的应用。您需要对该项目具有编辑权限。请参阅[应用库](/zh-cn/guides/panel-apps/gallery/)。

## 固定到主页

选择 **固定到主页** 可将应用添加到项目的 **主页** 看板，选择 **从主页取消固定** 可将其移除。

## 删除应用

删除 Panel 应用前会先请您确认。在 **我的 Panel 应用** 中，使用应用所在行的**减号**图标。取消发布同样需要确认。

## 后续步骤

- [使用 Weave 构建 Panel 应用](/zh-cn/guides/panel-apps/build-with-weave/) — 描述应用并批准具体更改。
- [Panel 应用套件](/zh-cn/guides/panel-apps/app-kit/) — Studio 的表和视图起始模板所使用的组件。
- [提醒与摘要](/zh-cn/guides/panel-apps/alerts-and-digests/) — 在数字越过限值时或按计划通知相关人员。
- [应用库](/zh-cn/guides/panel-apps/gallery/) — 将应用共享为他人的起点。
- [使用 Panel 应用](/zh-cn/guides/panel-apps/using/) — 发布后的日志、使用情况和重新构建。
