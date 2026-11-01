---
title: PlaidXL 故障排除
description: 常见 PlaidXL 问题的解决办法——功能区中缺少加载项、登录弹出窗口无法打开、缺少工作区或项目、表显示为红色、检索缓慢，以及 PlaidXL 公式中的错误。
sidebar:
  label: 故障排除
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## 功能区中没有 PlaidCloud 选项卡

- 关闭所有 Excel 窗口并重新打开 Excel。新安装的加载项通常要重启后才会出现。
- 打开**插入 → 我的加载项**并选择 **PlaidCloud**。
- 确认您使用的是适用于 Microsoft 365 的桌面版 Excel，或 Excel 2021 及更高版本。请参阅[安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/)。
- 如果您的组织管理加载项，请询问 Microsoft 365 管理员是否已向您部署 **PlaidCloud** 加载项。

## 登录弹出窗口无法打开

单击**登录**时，Excel 会询问是否显示弹出窗口。请允许。如果您已关闭该提示，请再次单击**登录**。

如果弹出窗口已打开但您无法完成登录，请尝试使用同一电子邮件在浏览器中登录 PlaidCloud。那里出现的问题——例如密码已过期或您不再拥有双重验证设备——需要先在 PlaidCloud 中解决。请参阅[成员身份验证](/zh-cn/administration/access/member-authentication/)。

## 未列出某个工作区

**选择工作区**会列出您的电子邮件地址所属的工作区。如果缺少某个工作区，请确认您输入的电子邮件与您用于该工作区的电子邮件相同，然后请工作区管理员确认您是成员。请参阅[管理工作区成员](/zh-cn/administration/access/overview/managing-workspace-members/)。

若要转到您所属的另一个工作区，请打开账户菜单并选择**切换工作区**。

## 缺少项目、表或维度

PlaidXL 显示的是您的账户在 PlaidCloud 中可以看到的内容。如果缺少项目，请请其所有者授予您访问权限。如果缺少表，请检查它是否存在于所选项目中并已加载数据——从未写入过数据的表在您选中它时会显示**无法获取表元数据**。

项目、表和维度列表中的文件夹默认折叠。请在列表顶部的筛选框中输入名称的一部分，以查找文件夹内的项目。

## 表显示为红色

该表的行数或列数超过了 Excel 工作表的容量。请选择**高级**来筛选行，并清除不需要的列，直到其可以容纳为止。请参阅[显示为红色的表](/zh-cn/reference/cli/plaidxl/retrieve/#显示为红色的表)。

## 检索缓慢

Excel 处理宽表时最慢。请清除不需要的列的复选框，并使用**高级**筛选行。只检索您要使用的数据，速度更快，生成的工作簿也更小。

## 公式显示错误

| 您看到的现象 | 需要检查的内容 |
|---|---|
| `#SPILL!` | 结果所需的单元格中有内容。请清除公式下方或旁边的单元格。 |
| `#NAME?` | Excel 无法识别该函数。请检查是否已安装 PlaidXL——功能区上有 **PlaidCloud** 选项卡——并对照[函数列表](/zh-cn/reference/cli/plaidxl/functions/)检查拼写。 |
| `PLAIDXL` 函数返回错误 | 请检查您是否已登录并选择了正确的项目，然后对照 PlaidCloud 检查每个表、列、维度和节点名称——名称必须完全一致。 |
| `CELL` 报告找不到筛选列 | `DIMENSION_REPR` 的第一个参数是表的列，而不是维度。请准确使用表的列名。请参阅[值](/zh-cn/reference/cli/plaidxl/functions/#值)。 |
| `CELL` 或 `CELLS` 返回 `#VALUE!` | 将鼠标悬停在单元格上，查看 PlaidCloud 给出的原因，例如未知列、不存在或没有成员的节点，或计算值时出现问题。请对照 PlaidCloud 检查名称。 |
| `CELL` 返回意外的总计 | 节点只会在与其维度链接的列上汇总；在任何其他列上，它必须与某个值完全匹配。请检查每个筛选器的列和节点。 |
| 数据或项目更改后值没有变化 | 强制完全重新计算——在 Windows 上，按 **Ctrl+Alt+F9**。 |
| `MEASURE_TYPE` 返回错误 | 请使用 `sum`、`mean`、`median`、`min`、`max`、`std` 或 `var` 之一，且为小写。 |

## 公式返回了另一个项目的数据

PlaidXL 函数从与工作簿关联的项目中读取数据。请在该工作簿中打开任务窗格，选择报表所针对的项目，然后强制完全重新计算。每个工作簿都有自己的项目，因此在另一个工作簿中选择项目不会改变此工作簿。请参阅[项目属于工作簿](/zh-cn/reference/cli/plaidxl/retrieve/#项目属于工作簿)。

## 来自另一个工作区的表被跳过

切换工作区后，任务窗格会说明有多少个已跟踪的表属于另一个工作区，并会被**刷新所有表**跳过。请在当前工作区中重新检索每个表以建立关联。

## 保存被拒绝或中止

| 您看到的现象 | 操作 |
|---|---|
| 表内有空行 | 连续两个或更多空行且其下方有数据时，保存会被中止。请删除这些空行或将其填充，然后再次保存。 |
| 自检索以来表已更改 | 其他人已在 PlaidCloud 中保存了该表。请重新检索并重新应用您的编辑。 |
| 值无法转换 | 不会写入任何内容，并会列出相关行。请更正这些值，使其与列的数据类型一致。 |
| 工作表未链接到表 | 请先将表检索到工作表中。**保存到 PlaidCloud…** 只会出现在已检索到活动工作表中的表上。 |

若要撤消保存，请单击确认消息中的**还原上一版本**，或在 PlaidCloud 中打开该表，并在**截至**菜单中选择保存之前的版本。还原点会保留 7 天。请参阅[将表保存到 PlaidCloud](/zh-cn/reference/cli/plaidxl/retrieve/#将表保存到-plaidcloud)。

## 相关内容

- [安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/)
- [登录 PlaidXL](/zh-cn/reference/cli/plaidxl/connect/)
- [获取帮助](/zh-cn/guides/support/getting-help/)——提交支持工单
