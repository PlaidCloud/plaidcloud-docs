---
title: PlaidXL 故障排除
description: 常见 PlaidXL 问题的解决方法：功能区中缺少加载项、登录弹出窗口无法打开、缺少工作区或项目、表显示为红色、检索缓慢，以及 PlaidXL 公式出错。
sidebar:
  label: 故障排除
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## 功能区上没有 PlaidCloud 选项卡

- 关闭所有 Excel 窗口并重新打开 Excel。新安装的加载项通常要在重启后才会出现。
- 打开 **Insert → My Add-ins** 并选择 **PlaidCloud**。
- 确认您使用的是适用于 Microsoft 365 的桌面版 Excel，或 Excel 2021 及更高版本。请参阅[安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/)。
- 如果您的组织管理加载项，请询问 Microsoft 365 管理员是否已向您部署 **PlaidCloud** 加载项。

## 登录弹出窗口无法打开

单击 **Sign In** 时，Excel 会询问是否显示弹出窗口，请选择允许。如果您关闭了该提示，请再次单击 **Sign In**。

如果弹出窗口已打开，但无法完成登录，请尝试在浏览器中使用同一电子邮件登录 PlaidCloud。那里的问题（例如密码已过期，或您不再拥有双重验证设备）需要先在 PlaidCloud 中解决。请参阅[成员身份验证](/zh-cn/administration/access/member-authentication/)。

## 未列出某个工作区

**Select a tenant** 列出您的电子邮件地址所属的工作区。如果缺少某个工作区，请检查输入的电子邮件是否与该工作区所用的相同，然后请工作区管理员确认您是成员。请参阅[管理工作区成员](/zh-cn/administration/access/overview/managing-workspace-members/)。

若要切换到您所属的另一个工作区，请单击 **Logout** 并重新登录。

## 缺少项目、表或维度

PlaidXL 显示的是您的账户在 PlaidCloud 中可以看到的内容。如果缺少某个项目，请让其所有者授予您访问权限。如果缺少某个表，请检查它是否存在于所选项目中并且已加载数据；从未写入过的表在您选中时会显示 **Unable to get table metadata**。

项目、表和维度列表中的文件夹默认折叠。请在列表顶部的筛选框中输入名称的一部分，以查找文件夹内的项目。

## 表显示为红色

该表的行数或列数超出了 Excel 工作表的容量。请选择 **高级** 筛选行，并清除不需要的列，直到其能够容纳。请参阅[以红色显示的表](/zh-cn/reference/cli/plaidxl/retrieve/#以红色显示的表)。

## 检索缓慢

Excel 处理宽表最慢。请清除不需要的列的复选框，并使用 **高级** 筛选行。只检索您实际使用的数据速度更快，工作簿也更小。

## 公式显示错误

| 您看到的现象 | 检查什么 |
|---|---|
| `#SPILL!` | 结果所需的单元格中有内容。请清除公式下方或旁边的单元格。 |
| `#NAME?` | Excel 无法识别该函数。请检查是否已安装 PlaidXL（功能区上有 **PlaidCloud** 选项卡），并对照[函数列表](/zh-cn/reference/cli/plaidxl/functions/)检查拼写。 |
| `PLAIDXL` 函数返回的错误 | 检查是否已登录并选择了正确的项目，然后对照 PlaidCloud 检查每个表、列、维度和节点的名称，名称必须完全一致。 |
| `CELL` 报告找不到筛选列 | `DIMENSION_REPR` 的第一个参数是表的列，而不是维度。请准确使用表的列名。请参阅[值](/zh-cn/reference/cli/plaidxl/functions/#值)。 |
| `CELL` 返回 0 或意外的总计 | 对照维度检查节点名称：不存在的节点不会汇总任何内容，因而返回 0。节点只会在链接到其维度的列上汇总；在其他任何列上，它必须与某个值完全匹配。 |
| 数据或项目更改后值没有变化 | 强制完全重新计算：在 Windows 上，按 **Ctrl+Alt+F9**。 |
| `MEASURE_TYPE` 返回错误 | 请使用 `sum`、`mean`、`median`、`min`、`max`、`std` 或 `var` 之一，并使用小写。 |

## 公式返回了另一个项目的数据

PlaidXL 函数读取任务窗格中选定的项目，并且该选择由您打开的所有工作簿共用。请选择报表所针对的项目，然后强制完全重新计算。**设为默认** 会将项目保存在工作簿中，这样在该工作簿中打开任务窗格时就会选中它。请参阅[设置默认项目](/zh-cn/reference/cli/plaidxl/retrieve/#设置默认项目)。

## 相关内容

- [安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/)
- [登录 PlaidXL](/zh-cn/reference/cli/plaidxl/connect/)
- [获取帮助](/zh-cn/guides/support/getting-help/) — 提交支持工单
