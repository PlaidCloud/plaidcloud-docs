---
title: PlaidXL
description: 使用 PlaidXL Excel 加载项登录 PlaidCloud 工作区，将项目表和维度层次结构拉取到工作表中，按需刷新，并使用 PlaidXL 自定义函数构建实时报表。
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

PlaidXL 是适用于 Microsoft Excel 的 PlaidCloud 加载项。它将工作簿连接到您的 PlaidCloud 工作区，使模型和报表读取权威的项目表和维度，而不是在下次工作流运行后就会过时的副本。

使用 PlaidXL 有两种方式，大多数工作簿会同时用到：

- **任务窗格** — 浏览项目，选择表或维度，选择列和筛选器，并将数据检索到工作表中。**Refresh All Tables** 会为您检索过的每个表拉取当前数据。
- **自定义函数** — 例如 `=PLAIDXL.TABLE.GET_TABLE("Sales")` 和 `=PLAIDXL.CELL(...)` 这样的公式，可将 PlaidCloud 数据直接读入单元格。可用它们列出表和维度、排布层次结构，并为报表计算汇总值。

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
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">任务窗格和自定义函数都使用您自己的 PlaidCloud 权限，从您选择的项目读取数据。</figcaption>
</figure>

PlaidXL 只读取数据，不会向 PlaidCloud 写回任何内容，因此编辑已检索的工作表绝不会更改项目表。

## 要求

- 适用于 Windows 或 Mac 的 Excel for Microsoft 365，或 Excel 2021 及更高版本。PlaidCloud 功能区选项卡和任务窗格在桌面版 Excel 中运行。
- 至少属于一个工作区的 PlaidCloud 账户，以及对要读取的项目的访问权限。PlaidXL 仅显示您的账户在 PlaidCloud 中已经可以看到的项目、表和维度。

## 主题

- [安装](/zh-cn/reference/cli/plaidxl/install/) — 将 PlaidXL 添加到 Excel 并打开任务窗格
- [登录](/zh-cn/reference/cli/plaidxl/connect/) — 连接到工作区、退出登录以及切换工作区
- [处理表和维度](/zh-cn/reference/cli/plaidxl/retrieve/) — 选择项目、筛选表、将其检索到工作表中并刷新
- [自定义函数](/zh-cn/reference/cli/plaidxl/functions/) — 每个 `PLAIDXL` 函数、其参数及返回内容
- [使用自定义函数构建报表](/zh-cn/reference/cli/plaidxl/build-a-report/) — 排布层次结构并用汇总值填充
- [PlaidCloud 功能区](/zh-cn/reference/cli/plaidxl/ribbon/) — 刷新、钻取和清理命令
- [故障排除](/zh-cn/reference/cli/plaidxl/troubleshooting/) — 最常见问题的解决方法

初次使用 PlaidXL？[在 Excel 中使用 PlaidXL](/zh-cn/get-started/tutorials/excel-with-plaidxl/) 教程将带您在约 20 分钟内完成从安装加载项到首份报表的全过程。

## 相关内容

- [项目](/zh-cn/guides/projects/) — 项目包含的内容以及如何找到项目
- [表和视图](/zh-cn/guides/data/tables-views/) — PlaidXL 检索的表
- [使用维度](/zh-cn/guides/dimensions/dimensions/) — PlaidXL 排布并汇总的层次结构
