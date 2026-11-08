---
title: PlaidXL 故障排除
description: 常见 PlaidXL 问题的解决方法：功能区中缺少加载项、登录弹出窗口无法打开、缺少工作区或项目、表显示为红色、检索缓慢、PlaidXL 公式和指标出错、键入的值未写入，以及保存中止。
sidebar:
  label: 故障排除
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## 功能区中没有 PlaidCloud 选项卡

- 关闭所有 Excel 窗口并重新打开 Excel。新安装的加载项通常要重启后才会出现。
- 打开 **Insert → My Add-ins** 并选择 **PlaidCloud**。
- 确认您使用的是 Microsoft 365 桌面版 Excel，或 Excel 2021 及更高版本。请参阅[安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/)。
- 如果您的组织管理加载项，请询问 Microsoft 365 管理员是否已向您部署 **PlaidCloud** 加载项。

## 登录弹出窗口无法打开

点击 **Sign In** 时，Excel 会询问是否显示弹出窗口，请允许。如果您关闭了提示，请再次点击 **Sign In**。

如果弹出窗口已打开但无法完成登录，请尝试在浏览器中使用相同的电子邮件登录 PlaidCloud。那里的问题（例如密码已过期或您不再拥有双重验证设备）需要先在 PlaidCloud 中解决。请参阅[成员身份验证](/zh-cn/administration/access/member-authentication/)。

## 工作区未列出

**Select a workspace** 会列出您的电子邮件地址所属的工作区。如果缺少某个工作区，请确认您输入的电子邮件与该工作区所用的相同，然后请工作区管理员确认您是成员。请参阅[管理工作区成员](/zh-cn/administration/access/overview/managing-workspace-members/)。

要转到您所属的另一个工作区，请打开账户菜单并选择 **Switch workspace**。

## 缺少项目、表或维度

PlaidXL 显示的是您的账户在 PlaidCloud 中可见的内容。如果缺少某个项目，请让其所有者授予您访问权限。如果缺少某个表，请确认它存在于所选项目中并且已加载数据：从未写入过数据的表在您选中时会显示 **Unable to get table metadata**。

项目、表和维度列表中的文件夹默认折叠。在列表顶部的筛选框中输入名称的一部分，即可找到文件夹内的项目。

## 表显示为红色

该表的行数或列数超过 Excel 工作表的容量，或 PlaidCloud 无法报告其大小。您仍可检索它，放不下的行会继续放到后续工作表上，但跨工作表拆分的表无法保存。请选择**高级**来筛选行，并取消勾选不需要的列，直到能够放下。请参阅[显示为红色的表](/zh-cn/reference/cli/plaidxl/retrieve/#显示为红色的表)。

## 检索缓慢

Excel 处理宽表时最慢。请取消勾选不需要的列，并使用**高级**筛选行。只检索您使用的数据会更快，工作簿也更小。

## 公式显示错误

| 您看到的内容 | 需要检查的内容 |
|---|---|
| `#SPILL!` | 结果所需的单元格中有内容。请清除公式下方或旁边的单元格。 |
| `#NAME?` | Excel 无法识别该函数。请确认已安装 PlaidXL（功能区中有 **PlaidCloud** 选项卡），并对照[函数列表](/zh-cn/reference/cli/plaidxl/functions/)检查拼写。 |
| `PLAIDXL` 函数返回的错误 | 确认您已登录并选择了正确的项目，然后对照 PlaidCloud 检查每个表、列、维度和节点名称，名称必须完全一致。 |
| `CELL` 报告找不到筛选列 | `DIMENSION_REPR` 的第一个参数是表的列，而不是维度。请使用表的列名，且必须完全一致。请参阅[值](/zh-cn/reference/cli/plaidxl/functions/#值)。 |
| `METRIC` 或 `METRIC_BREAKDOWN` 返回 `#VALUE!` | 将鼠标悬停在单元格上以查看原因。请参阅[指标错误](/zh-cn/reference/cli/plaidxl/functions/#指标错误)。 |
| 指标返回 `#VALUE!`：**此 PlaidCloud 工作区暂时无法将备用层次结构与其他成员组合使用。请联系管理员更新工作区。** | 工作区需要更新后，指标才能将备用层次结构的成员与其他成员组合使用。请联系管理员。同一次重新计算中的其他单元格仍会返回结果。 |
| `CELL` 或 `CELLS` 返回 `#VALUE!` | 将鼠标悬停在单元格上以查看 PlaidCloud 给出的原因，例如未知的列、不存在或没有成员的节点，或计算该值时出现问题。请对照 PlaidCloud 检查名称。 |
| `CELL` 返回意外的总计 | 节点只会在与其维度关联的列上汇总；在任何其他列上，它必须与某个值完全匹配。请检查每个筛选器的列和节点。 |
| 数据或项目更改后值没有变化 | 在功能区的**刷新**菜单中点击 **Recalculate PlaidXL formulas**。 |
| `MEASURE_TYPE` 返回错误 | 请使用 `sum`、`mean`、`median`、`min`、`max`、`std` 或 `var` 之一，且为小写。 |

## 公式返回了另一个项目的数据

PlaidXL 函数从与工作簿关联的项目读取数据。请在该工作簿中打开任务窗格，选择报表所针对的项目，然后在功能区的**刷新**菜单中点击 **Recalculate PlaidXL formulas**。每个工作簿都有自己的项目，因此在另一个工作簿中选择项目不会改变这个工作簿。请参阅[项目属于工作簿](/zh-cn/reference/cli/plaidxl/retrieve/#项目属于工作簿)。

## 来自另一个工作区的表被跳过

切换工作区后，**Refresh All Tables** 会提示此工作簿中来自另一个工作区的表或维度未被刷新，并且它们不会列在 **On this sheet** 下。请在当前工作区中重新检索每个表以建立关联。

## 键入的值未写入

在 `CELL` 上键入值时，任务窗格会说明写入了什么，并列出未写入的内容及原因。请参阅[向 PlaidCloud 键入值](/zh-cn/reference/cli/plaidxl/write-values/)。

| 您看到的内容 | 操作 |
|---|---|
| 只有恰好包含一个 `PLAIDXL.CELL` 的单元格才接受键入的值 | 请在公式仅为单个 `CELL`（可以乘以、除以或取负）的单元格上键入。 |
| 此处无法读取某个参数 | `CELL` 的参数必须是单元格或文本，而不能是其他计算。 |
| 分摊方法、形态或锁定仅适用于求和 | `E1200`、`1200 like FY2025` 和 `H` 等代码仅适用于**求和**单元格。在其他单元格上请键入普通数字。 |
| 所有成员均被锁定 | 请用 `H` 解除锁定，然后重新键入该值。 |
| 工作区尚不支持在 Excel 中键入值 | 请让管理员更新该工作区。 |

## 保存被拒绝或中止

保存会立即写入，很少中止。在以下情况下会中止：

| 您看到的内容 | 操作 |
|---|---|
| 标题行与检索到的列不再一致 | 请将标题恢复为检索时的样子，或重新检索该表。 |
| 值无法转换 | 不会写入任何内容，并会列出相关行。请更正这些值，使其与列的数据类型一致。 |
| 表延续到其他工作表 | 跨工作表拆分的表无法保存。请使用筛选器重新检索，使其放入一个工作表。 |
| 表检索时使用了保存无法保留的筛选器 | 请重新检索，筛选器只能使用以 **AND** 连接的 **equal** 和 **in** 规则，或不使用筛选器。 |
| 行超出了您的行访问权限 | 不会保存任何内容。请移除这些行，然后再次保存。 |
| 工作表未关联到表 | 请先将表检索到该工作表。只有检索到活动工作表中的表才会列在 **On this sheet** 下。 |

要撤消保存，请点击消息中的**撤消**，或功能区上的 **Undo last write**。每次保存都会各自保留还原点 7 天，因此您可以在保存后的 7 天内撤消任意一次保存。请参阅[将表保存到 PlaidCloud](/zh-cn/reference/cli/plaidxl/retrieve/#将表保存到-plaidcloud)。

## 相关内容

- [安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/)
- [登录 PlaidXL](/zh-cn/reference/cli/plaidxl/connect/)
- [获取帮助](/zh-cn/guides/support/getting-help/) — 提交支持工单
