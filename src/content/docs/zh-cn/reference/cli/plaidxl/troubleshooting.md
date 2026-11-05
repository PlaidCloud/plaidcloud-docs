---
title: PlaidXL 故障排除
description: 常见 PlaidXL 问题的解决办法——功能区中缺少加载项、登录弹出窗口未打开、缺少工作区或项目、表显示为红色、检索缓慢、PlaidXL 公式和指标出错、键入的值未写入，以及保存中止。
sidebar:
  label: 故障排除
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## 功能区中没有 PlaidCloud 选项卡

- 关闭所有 Excel 窗口并重新打开 Excel。新安装的加载项通常要重启后才会出现。
- 打开 **插入 → My Add-ins** 并选择 **PlaidCloud**。
- 检查您使用的是 Microsoft 365 版桌面 Excel，或 Excel 2021 及更高版本。请参阅[安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/)。
- 如果您的组织管理加载项，请询问 Microsoft 365 管理员是否已向您部署 **PlaidCloud** 加载项。

## 登录弹出窗口未打开

单击 **Sign In** 时，Excel 会询问是否显示弹出窗口。请允许。如果您关闭了提示，请再次单击 **Sign In**。

如果弹出窗口已打开但您无法完成登录，请尝试在浏览器中使用相同的电子邮件登录 PlaidCloud。如果那里有问题——密码已过期，或您不再拥有双重验证设备——需要先在 PlaidCloud 中解决。请参阅[成员身份验证](/zh-cn/administration/access/member-authentication/)。

## 未列出某个工作区

**Select a workspace** 会列出您的电子邮件地址所属的工作区。如果缺少某一个，请检查您输入的是否是用于该工作区的同一个电子邮件，然后请工作区管理员确认您是成员。请参阅[管理工作区成员](/zh-cn/administration/access/overview/managing-workspace-members/)。

若要切换到您所属的另一个工作区，请打开账户菜单并选择 **Switch workspace**。

## 缺少项目、表或维度

PlaidXL 显示的是您的账户在 PlaidCloud 中能看到的内容。如果缺少某个项目，请让其所有者授予您访问权限。如果缺少某个表，请检查它是否存在于所选项目中，并且已加载数据——从未写入过数据的表在您选中时会显示 **Unable to get table metadata**。

项目、表和维度列表中的文件夹默认折叠。在列表顶部的筛选框中键入名称的一部分，即可查找文件夹中的项。

## 表显示为红色

该表的行数或列数超过了 Excel 工作表的容量，或者 PlaidCloud 无法报告其大小。您可以检索它，放不下的行会继续放在后续工作表上，但拆分到多个工作表的表无法保存。请选择 **高级** 筛选行，并清除不需要的列，直到能放得下。请参阅[以红色显示的表](/zh-cn/reference/cli/plaidxl/retrieve/#以红色显示的表)。

## 检索缓慢

Excel 处理较宽的表最慢。清除不需要的列的复选框，并使用 **高级** 筛选行。只检索您要处理的数据更快，工作簿也更小。

## 公式显示错误

| 您看到的内容 | 检查什么 |
|---|---|
| `#SPILL!` | 结果所需的单元格中有内容。请清除公式下方或旁边的单元格。 |
| `#NAME?` | Excel 无法识别该函数。请检查是否已安装 PlaidXL——功能区上有 **PlaidCloud** 选项卡——并对照[函数列表](/zh-cn/reference/cli/plaidxl/functions/)检查拼写。 |
| 来自 `PLAIDXL` 函数的错误 | 检查您是否已登录并选择了正确的项目，然后对照 PlaidCloud 检查每个表、列、维度和节点的名称——名称必须完全一致。 |
| `CELL` 报告找不到筛选列 | `DIMENSION_REPR` 的第一个参数是表的列，而不是维度。请精确使用表的列名。请参阅[值](/zh-cn/reference/cli/plaidxl/functions/#值)。 |
| `METRIC` 或 `METRIC_BREAKDOWN` 返回 `#VALUE!` | 将鼠标悬停在单元格上查看原因。请参阅[指标错误](/zh-cn/reference/cli/plaidxl/functions/#指标错误)。 |
| `CELL` 或 `CELLS` 返回 `#VALUE!` | 将鼠标悬停在单元格上查看 PlaidCloud 给出的原因，例如未知的列、不存在或没有成员的节点，或计算该值时出现问题。请对照 PlaidCloud 检查名称。 |
| `CELL` 返回意外的总计 | 节点只在关联到其维度的列上汇总；在任何其他列上，它必须与某个值精确匹配。请检查每个筛选器的列和节点。 |
| 数据或项目变化后值没有改变 | 在功能区的 **刷新** 菜单中单击 **Recalculate PlaidXL formulas**。 |
| `MEASURE_TYPE` 返回错误 | 使用 `sum`、`mean`、`median`、`min`、`max`、`std` 或 `var` 之一，使用小写。 |

## 公式返回了另一个项目的数据

PlaidXL 函数读取与工作簿关联的项目。请在该工作簿中打开任务窗格，选择报表所针对的项目，然后在功能区的 **刷新** 菜单中单击 **Recalculate PlaidXL formulas**。每个工作簿都有自己的项目，因此在另一个工作簿中选择项目不会改变这个工作簿的项目。请参阅[项目属于工作簿](/zh-cn/reference/cli/plaidxl/retrieve/#项目属于工作簿)。

## 来自其他工作区的表被跳过

切换工作区后，**Refresh All Tables** 会提示此工作簿中来自其他工作区的表或维度未被刷新，并且它们不会列在 **On this sheet** 下。请在当前工作区中重新检索每个表以建立关联。

## 键入的值未写入

在 `CELL` 上键入内容时，任务窗格会说明写入了什么，并列出未写入的内容及原因。请参阅[向 PlaidCloud 输入值](/zh-cn/reference/cli/plaidxl/write-values/)。

| 您看到的内容 | 处理方法 |
|---|---|
| 只有仅包含一个 `PLAIDXL.CELL` 的单元格才接受键入的值 | 在公式为单个 `CELL`（可选地乘以、除以或取负）的单元格上键入。 |
| 此处无法读取某个参数 | `CELL` 的参数必须是单元格或文本，而不能是其他计算。 |
| 分摊方法、形状或保持仅适用于求和 | 诸如 `E1200`、`1200 like FY2025` 和 `H` 之类的代码仅适用于 **求和** 单元格。其他单元格请键入普通数字。 |
| 所有成员均被保持 | 用 `H` 解除保持，然后再次键入该值。 |
| 工作区尚不接受在 Excel 中键入的值 | 请管理员更新该工作区。 |

## 保存被拒绝或中止

保存会立即写入，很少会中止。在以下情况下会中止：

| 您看到的内容 | 处理方法 |
|---|---|
| 标题行与检索的列不再匹配 | 将标题恢复为检索时的样子，或重新检索该表。 |
| 某个值无法转换 | 不会写入任何内容，并列出相关行。请更正这些值以匹配列的数据类型。 |
| 表延续到其他工作表 | 拆分到多个工作表的表无法保存。请使用筛选器检索，使其能放在一个工作表上。 |
| 表是使用保存无法兼容的筛选器检索的 | 使用由 **等于** 和 **in** 规则通过 **AND** 连接的筛选器，或不使用筛选器，重新检索。 |
| 行超出您的行访问范围 | 不会保存任何内容。请移除这些行，或请项目架构师来保存它们。 |
| 工作表未关联到表 | 请先将表检索到该工作表。只有检索到活动工作表中的表才会列在 **On this sheet** 下。 |

若要撤消保存，请单击消息中的 **撤消**，或功能区上的 **Undo last write**。还原点保留 7 天。请参阅[将表保存到 PlaidCloud](/zh-cn/reference/cli/plaidxl/retrieve/#将表保存到-plaidcloud)。

## 相关内容

- [安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/)
- [登录 PlaidXL](/zh-cn/reference/cli/plaidxl/connect/)
- [获取帮助](/zh-cn/guides/support/getting-help/)——提交支持工单
