---
title: PlaidXL 故障排除
description: 常见 PlaidXL 问题的解决方法：功能区中缺少加载项、登录弹出窗口无法打开、缺少工作区或项目、以红色显示的表、检索缓慢、PlaidXL 公式和指标出错、键入的值未写入以及保存中断。
sidebar:
  label: 故障排除
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## 功能区中没有 PlaidCloud 选项卡

- 关闭所有 Excel 窗口，然后重新打开 Excel。新安装的加载项通常要在重启后才会出现。
- 打开 **插入 → 我的加载项**，然后选择 **PlaidCloud**。
- 确认您使用的是 Microsoft 365 版桌面 Excel，或 Excel 2021 及更高版本。请参阅[安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/)。
- 如果贵组织管理加载项，请询问 Microsoft 365 管理员是否已向您部署 **PlaidCloud** 加载项。

## 登录弹出窗口无法打开

单击 **Sign In** 时，Excel 会询问是否显示弹出窗口。请允许。如果您关闭了该提示，请再次单击 **Sign In**。

如果弹出窗口已打开但无法完成登录，请尝试使用相同的电子邮件在浏览器中登录 PlaidCloud。如果那里存在问题（例如密码已过期，或您不再拥有的双重验证设备），需要先在 PlaidCloud 中解决。请参阅[成员身份验证](/zh-cn/administration/access/member-authentication/)。

## 工作区未列出

**Select a workspace** 会列出您的电子邮件地址所属的工作区。如果缺少某个工作区，请确认您输入的电子邮件与该工作区所用的相同，然后请工作区管理员确认您是成员。请参阅[管理工作区成员](/zh-cn/administration/access/overview/managing-workspace-members/)。

若要切换到您所属的另一个工作区，请打开账户菜单并选择 **Switch workspace**。

## 缺少项目、表或维度

PlaidXL 显示的是您的账户在 PlaidCloud 中能看到的内容。如果缺少项目，请让其所有者授予您访问权限。如果缺少表，请确认它存在于所选项目中并已加载数据：从未写入过数据的表在您选中时会显示 **Unable to get table metadata**。

项目、表和维度列表中的文件夹默认折叠。在列表顶部的筛选框中输入名称的一部分，即可找到文件夹内的项目。

## 表显示为红色

该表的行数或列数超过了 Excel 工作表的容量，或者 PlaidCloud 无法报告其大小。您仍可检索它，放不下的行会延续到后续工作表，但拆分到多个工作表的表无法保存。请选择 **高级** 筛选行，并清除不需要的列，直到能放入一个工作表。请参阅[以红色显示的表](/zh-cn/reference/cli/plaidxl/retrieve/#以红色显示的表)。

## 检索缓慢

Excel 处理宽表最慢。请清除不需要的列的复选框，并使用 **高级** 筛选行。只检索您要使用的数据速度更快，工作簿也更小。

在网页版 Excel 和当前的桌面版 Excel 中，大型表的检索和刷新速度要快得多。较旧版本的 Excel 仍可使用，只是没有这种提速。

如果窗格提示 **PlaidXL was updated — reload the pane**，请关闭任务窗格，重新打开，然后再次检索。PlaidXL 更新后，窗格会在下次加载时采用新版本。

如果拉取时提示 **This PlaidCloud workspace needs an update for PlaidXL**，请让管理员将工作区更新到当前的 PlaidCloud 版本。

## 公式显示错误

| 您看到的内容 | 需要检查的内容 |
|---|---|
| `#SPILL!` | 结果所需的单元格中已有内容。请清除公式下方或旁边的单元格。 |
| `#NAME?` | Excel 无法识别该函数。请确认已安装 PlaidXL（功能区上有 **PlaidCloud** 选项卡），并对照[函数列表](/zh-cn/reference/cli/plaidxl/functions/)检查拼写。 |
| `PLAIDXL` 函数返回的错误 | 请确认您已登录并选择了正确的项目，然后对照 PlaidCloud 检查每个表、列、维度和节点的名称，名称必须完全匹配。 |
| `CELL` 报告找不到筛选列 | `DIMENSION_REPR` 的第一个参数是表的列，而不是维度。请准确使用表的列名。请参阅[值](/zh-cn/reference/cli/plaidxl/functions/#值)。 |
| `METRIC` 或 `METRIC_BREAKDOWN` 返回 `#VALUE!` | 将鼠标悬停在单元格上可查看原因。请参阅[指标错误](/zh-cn/reference/cli/plaidxl/functions/#指标错误)。 |
| 指标返回 `#VALUE!`：**This PlaidCloud workspace can't combine an alternate hierarchy with other members yet. Ask your administrator to update the workspace.** | 工作区需要更新，指标才能将备用层次结构成员与其他成员混合使用。请联系管理员。同一次重新计算中的其他单元格仍会得到结果。 |
| `CELL` 或 `CELLS` 返回 `#VALUE!` | 将鼠标悬停在单元格上可查看 PlaidCloud 给出的原因，例如未知的列、不存在或没有成员的节点，或计算值时出现的问题。请对照 PlaidCloud 检查名称。 |
| `CELL` 返回意外的合计 | 节点只会在与其维度链接的列上汇总；在任何其他列上，它必须与某个值完全匹配。请检查每个筛选器的列和节点。 |
| 数据或项目更改后值没有变化 | 单击功能区 **刷新** 菜单中的 **Recalculate PlaidXL formulas**。 |
| `MEASURE_TYPE` 返回错误 | 请使用小写的 `sum`、`mean`、`median`、`min`、`max`、`std` 或 `var` 之一。 |

## 公式返回了另一个项目的数据

PlaidXL 函数从链接到工作簿的项目读取数据。请在该工作簿中打开任务窗格，选择该报表所针对的项目，然后单击功能区 **刷新** 菜单中的 **Recalculate PlaidXL formulas**。每个工作簿都有各自的项目，因此在另一个工作簿中选择项目不会改变此工作簿。请参阅[项目属于工作簿](/zh-cn/reference/cli/plaidxl/retrieve/#项目属于工作簿)。

## 来自另一个工作区的表被跳过

切换工作区后，**Refresh All Tables** 会提示此工作簿中来自另一个工作区的表或维度未被刷新，并且它们不会列在 **On this sheet** 下。请在当前工作区中重新检索每个表以建立链接。

## 键入的值未写入

在 `CELL` 上键入内容时，任务窗格会说明写入了什么，并列出未写入的内容及原因。请参阅[向 PlaidCloud 输入值](/zh-cn/reference/cli/plaidxl/write-values/)。

| 您看到的内容 | 处理方法 |
|---|---|
| 只有仅包含一个 `PLAIDXL.CELL` 的单元格才接受键入的值 | 请在公式为单个 `CELL`（可选地乘、除或取负）的单元格上键入。 |
| 此处无法读取某个参数 | `CELL` 的参数必须是单元格或文本，而不能是其他计算。 |
| 分摊方法、形状或保持仅适用于求和 | `E1200`、`1200 like FY2025` 和 `H` 等代码仅对 **求和** 单元格有效。对其他单元格请键入普通数字。 |
| 所有成员均已保持 | 请用 `H` 解除保持，然后重新键入值。 |
| 工作区尚不接受在 Excel 中键入的值 | 请联系管理员更新工作区。 |

## 保存被拒绝或中止

保存会立即写入，很少会中断。出现以下情况时会中断：

| 您看到的内容 | 处理方法 |
|---|---|
| 标题行不再与检索的列匹配 | 将标题恢复为检索时的样子，或重新检索该表。 |
| 某个值无法转换 | 不会写入任何内容，并会列出相关行。请更正这些值，使其与列的数据类型一致。 |
| 表延续到其他工作表 | 拆分到多个工作表的表无法保存。请使用筛选器检索，使其能放入一个工作表。 |
| 表是用保存无法遵循的筛选器检索的 | 请使用由 **等于** 和 **in** 规则以 **AND** 连接而成的筛选器重新检索，或不使用筛选器。 |
| 行超出了您的行访问权限 | 不会保存任何内容。请删除这些行，然后再次保存。 |
| 列中的文本长于 Excel 单元格的 32,767 个字符 | Excel 会截断显示这些文本，而保存也会在 PlaidCloud 中截断它们，因此该表的保存功能被关闭。请不包含这些列重新检索该表，以便保存。 |
| 表只被部分写入 | Excel 拒绝了上次刷新的一部分。请刷新该表，然后保存。 |
| 工作表未链接到表 | 请先将表检索到该工作表。只有检索到活动工作表的表才会列在 **On this sheet** 下。 |

若要撤消保存，请单击消息中的 **撤消** 或功能区上的 **Undo last write**。每次保存都会将各自的还原点保留 7 天，因此您可以在保存后的 7 天内撤消任何一次保存。请参阅[将表保存到 PlaidCloud](/zh-cn/reference/cli/plaidxl/retrieve/#将表保存到-plaidcloud)。

## 相关内容

- [安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/)
- [登录 PlaidXL](/zh-cn/reference/cli/plaidxl/connect/)
- [获取帮助](/zh-cn/guides/support/getting-help/)：提交支持工单
