---
title: PlaidXL 故障排除
description: 常见 PlaidXL 问题的解决方法：功能区中缺少加载项、登录弹出窗口无法打开、缺少工作区或项目、表显示为红色、检索缓慢，以及 PlaidXL 公式中的错误。
sidebar:
  label: 故障排除
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## 功能区上没有 PlaidCloud 选项卡

- 关闭所有 Excel 窗口并重新打开 Excel。新安装的加载项通常需要重启后才会出现。
- 打开**插入 → 我的加载项**并选择 **PlaidCloud**。
- 检查您使用的是 Microsoft 365 版桌面 Excel，或 Excel 2021 及更高版本。参见[安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/)。
- 如果您的组织管理加载项，请询问您的 Microsoft 365 管理员是否已将 **PlaidCloud** 加载项部署给您。

## 登录弹出窗口无法打开

单击 **Sign In** 时，Excel 会询问是否显示弹出窗口。请允许。如果您已关闭该提示，请再次单击 **Sign In**。

如果弹出窗口已打开但无法完成登录，请尝试在浏览器中使用同一电子邮件登录 PlaidCloud。那里的问题（例如密码过期或您不再拥有的双重验证设备）需要先在 PlaidCloud 中解决。参见[成员身份验证](/zh-cn/administration/access/member-authentication/)。

## 未列出某个工作区

**Select a workspace** 列出您的电子邮件地址所属的工作区。如果缺少某个工作区，请检查您输入的电子邮件是否与您在该工作区使用的相同，然后请工作区管理员确认您是成员。参见[管理工作区成员](/zh-cn/administration/access/overview/managing-workspace-members/)。

若要切换到您所属的另一个工作区，请打开账户菜单并选择 **Switch workspace**。

## 缺少项目、表或维度

PlaidXL 显示您的账户在 PlaidCloud 中可见的内容。如果缺少某个项目，请请其所有者授予您访问权限。如果缺少某个表，请检查它是否存在于所选项目中且已加载数据；从未写入过数据的表在您选中它时会显示 **Unable to get table metadata**。

项目、表和维度列表中的文件夹默认折叠。在列表顶部的筛选框中输入名称的一部分，即可找到文件夹内的项目。

## 表显示为红色

该表的行数或列数超出了 Excel 工作表的容量。请选择 **Advanced** 筛选行，并清除不需要的列，直到它能放得下为止。参见[以红色显示的表](/zh-cn/reference/cli/plaidxl/retrieve/#以红色显示的表)。

## 检索缓慢

Excel 处理宽表时最慢。请清除不需要的列的复选框，并使用 **Advanced** 筛选行。只检索您使用的数据速度更快，工作簿也更小。

## 公式显示错误

| 您看到的现象 | 检查内容 |
|---|---|
| `#SPILL!` | 结果所需的单元格中有内容。请清除公式下方或旁边的单元格。 |
| `#NAME?` | Excel 无法识别该函数。请检查 PlaidXL 是否已安装（功能区上有 **PlaidCloud** 选项卡），并对照[函数列表](/zh-cn/reference/cli/plaidxl/functions/)检查拼写。 |
| 来自 `PLAIDXL` 函数的错误 | 检查您是否已登录并选择了正确的项目，然后对照 PlaidCloud 检查每个表、列、维度和节点的名称，名称必须完全一致。 |
| `CELL` 报告找不到筛选列 | `DIMENSION_REPR` 的第一个参数是表的列，而不是维度。请准确使用表的列名。参见[值](/zh-cn/reference/cli/plaidxl/functions/#值)。 |
| `CELL` 或 `CELLS` 返回 `#VALUE!` | 将鼠标悬停在单元格上，阅读 PlaidCloud 给出的原因，例如未知的列、不存在或没有成员的节点，或计算该值时出现问题。请对照 PlaidCloud 检查名称。 |
| `CELL` 返回意外的总计 | 节点只在链接到其维度的列上汇总；在任何其他列上，它必须精确匹配某个值。请检查每个筛选器的列和节点。 |
| 数据或项目更改后值没有变化 | 强制完全重新计算：在 Windows 上，按 **Ctrl+Alt+F9**。 |
| `MEASURE_TYPE` 返回错误 | 请使用 `sum`、`mean`、`median`、`min`、`max`、`std` 或 `var` 之一，并使用小写。 |

## 公式返回了其他项目的数据

PlaidXL 函数从与工作簿关联的项目读取数据。请在该工作簿中打开任务窗格，选择该报表所针对的项目，然后强制完全重新计算。每个工作簿都有自己的项目，因此在另一个工作簿中选择项目不会改变此工作簿。参见[项目属于工作簿](/zh-cn/reference/cli/plaidxl/retrieve/#项目属于工作簿)。

## 来自其他工作区的表被跳过

切换工作区后，任务窗格会说明有多少个已跟踪的表属于另一个工作区，并被 **Refresh All Tables** 跳过。请在当前工作区中重新检索每个表以建立关联。

## 保存被拒绝或停止

| 您看到的现象 | 处理方法 |
|---|---|
| 表内有空行 | 单个空行会被跳过。连续两个或更多空行且其下方有数据时，会停止保存。请删除这些空行或填写内容，然后重新保存。 |
| 自您检索以来表已更改 | 其他人在 PlaidCloud 中保存了该表。请重新检索并重新应用您的编辑。（PlaidCloud 仅能对某些表类型进行此项检查；无法检查时，确认信息会警告其他人的更改将被覆盖。） |
| 某个值无法转换 | 不会写入任何内容，并会列出相关行。请更正值以匹配该列的数据类型。 |
| 工作表未链接到表 | 请先将表检索到该工作表。**Save to PlaidCloud…** 仅对检索到活动工作表中的表显示。 |

若要撤消保存，请单击确认消息中的 **Restore previous version**，或在 PlaidCloud 中打开该表，并在 **As of** 菜单中选择保存之前的版本。还原点保留 7 天。参见[将表保存到 PlaidCloud](/zh-cn/reference/cli/plaidxl/retrieve/#将表保存到-plaidcloud)。

## 相关内容

- [安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/)
- [登录 PlaidXL](/zh-cn/reference/cli/plaidxl/connect/)
- [获取帮助](/zh-cn/guides/support/getting-help/) — 提交支持工单
