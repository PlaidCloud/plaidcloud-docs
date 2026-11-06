---
title: PlaidXL
description: 使用 PlaidXL Excel 加载项登录 PlaidCloud 工作区，将项目表和维度层次结构拉取到工作表中，构建实时报表，钻取并说明数字，读取受管控的指标，通过将值键入回 PlaidCloud 进行规划，并询问 Weave。
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

PlaidXL 是适用于 Microsoft Excel 的 PlaidCloud 加载项。它将工作簿连接到您的 PlaidCloud 工作区，使您的模型和报表读取权威的项目表和维度，而不是在下次工作流运行后就会过时的副本。

您可以通过三种方式使用 PlaidXL，大多数工作簿会三者兼用：

- **任务窗格**——浏览项目，选择表或维度，选择列和筛选器，并将数据检索到工作表中。刷新可使其保持最新，**Save to PlaidCloud** 可将编辑后的表写回。其他选项卡可为您构建公式或整份报表，说明数字的来源，并让您用自然语言询问 Weave。
- **自定义函数**——诸如 `=PLAIDXL.TABLE.GET_TABLE("Sales")`、`=PLAIDXL.CELL(...)` 和 `=PLAIDXL.METRIC("Net Revenue")` 之类的公式，可将 PlaidCloud 数据直接读入单元格。使用它们列出表和维度、排布层次结构、为报表计算汇总值，以及读取受管控的指标。
- **功能区和右键菜单**——从任意单元格钻取维度、选取成员、刷新、说明数字或显示其背后的行，每项操作都有对应的键盘快捷键。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="Excel 包含 PlaidXL 任务窗格和 PlaidXL 自定义函数。两者都以您的身份登录，向 PlaidCloud 工作区中的项目发送请求，项目将表行、维度层次结构和汇总值返回到工作表单元格中。" style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="px-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="20" y="20" width="250" height="190" rx="10" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Excel 工作簿</text>
  <rect x="40" y="62" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="84" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">PlaidXL 任务窗格</text>
  <text x="145" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">浏览、筛选、检索、刷新</text>
  <rect x="40" y="130" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="152" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">PLAIDXL.* 函数</text>
  <text x="145" y="170" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">单元格中的表、层次结构和值</text>
  <rect x="410" y="40" width="230" height="150" rx="10" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">PlaidCloud 工作区</text>
  <rect x="430" y="80" width="190" height="94" rx="8" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="102" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">项目</text>
  <text x="525" y="124" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">表</text>
  <text x="525" y="142" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">维度和层次结构</text>
  <path d="M252 98 L405 98" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">以您的身份登录</text>
  <path d="M405 150 L254 150" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="168" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">行、节点、值</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">任务窗格和自定义函数都使用您自己的 PlaidCloud 权限，从您所选的项目读取数据。</figcaption>
</figure>

PlaidXL 从 PlaidCloud 读取数据，只有在您自己写入时才会更改项目表：在 `CELL` 值上键入数字，或使用 **Save to PlaidCloud** 保存已检索的工作表。两者都会立即写入，**Undo last write** 可将其撤销。请参阅[向 PlaidCloud 输入值](/zh-cn/reference/cli/plaidxl/write-values/)。

## 要求

- 在 Windows 或 Mac 上使用 Microsoft 365 版 Excel，或 Excel 2021 及更高版本。PlaidCloud 功能区选项卡、右键菜单和任务窗格在桌面版 Excel 中运行。
- 在至少一个工作区中拥有 PlaidCloud 账户，并有权访问您要读取的项目。PlaidXL 只显示您的账户在 PlaidCloud 中已经能看到的项目、表和维度。

## 主题

- [安装](/zh-cn/reference/cli/plaidxl/install/)——将 PlaidXL 添加到 Excel 并打开任务窗格
- [登录](/zh-cn/reference/cli/plaidxl/connect/)——连接到您的工作区、退出登录以及切换工作区
- [使用表和维度](/zh-cn/reference/cli/plaidxl/retrieve/)——选择项目、筛选表、将其检索到工作表中、刷新并保存回去
- [自定义函数](/zh-cn/reference/cli/plaidxl/functions/)——所有 `PLAIDXL` 函数、其参数及返回内容
- [构建报表](/zh-cn/reference/cli/plaidxl/build-a-report/)——通过任务窗格或公式排布实时报表
- [钻取、选取成员和说明数字](/zh-cn/reference/cli/plaidxl/drill/)——从单元格钻取、选取成员、说明数字并显示其明细行
- [向 PlaidCloud 输入值](/zh-cn/reference/cli/plaidxl/write-values/)——通过覆盖报表值进行规划，并撤销任何写入
- [在 Excel 中询问 Weave](/zh-cn/reference/cli/plaidxl/weave/)——通过自然语言请求来构建、钻取和修复
- [PlaidCloud 功能区](/zh-cn/reference/cli/plaidxl/ribbon/)——每个命令、右键菜单和键盘快捷键
- [故障排除](/zh-cn/reference/cli/plaidxl/troubleshooting/)——最常见问题的解决办法

初次接触 PlaidXL？[使用 PlaidXL 在 Excel 中工作](/zh-cn/get-started/tutorials/excel-with-plaidxl/)教程将在约 20 分钟内带您从安装加载项到完成第一份报表。

## 相关内容

- [项目](/zh-cn/guides/projects/)——项目包含什么以及如何查找项目
- [表和视图](/zh-cn/guides/data/tables-views/)——PlaidXL 检索的表
- [使用维度](/zh-cn/guides/dimensions/dimensions/)——PlaidXL 排布和汇总的层次结构
