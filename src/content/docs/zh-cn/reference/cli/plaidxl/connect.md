---
title: 登录 PlaidXL
description: 使用电子邮件和您常用的登录方式（包括单点登录和双重身份验证）将 PlaidXL 连接到 PlaidCloud 工作区，然后退出登录或切换工作区。
sidebar:
  label: 登录
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL 以您本人的身份登录，使用的登录方式与在浏览器中登录 PlaidCloud 时相同。无需输入服务器地址，工作簿中也不会保存密码。

## 登录

1. 打开任务窗格：**PlaidCloud → Open PlaidXL**，或单击**连接**组中的**账户**。
2. 在**Enter your email**下，输入用于 PlaidCloud 的电子邮件地址，然后单击 **Sign In**。PlaidXL 会记住该地址，供下次使用。
3. 如果您的电子邮件属于多个工作区，请从**Select a workspace**中选择一个，然后单击 **Sign In**。PlaidXL 会记住您的选择。如果您只属于一个工作区，PlaidXL 会自动选择。如果该电子邮件未关联任何工作区，窗格会给出提示；请检查地址后重试。
4. Excel 会询问是否允许弹出窗口。请允许。
5. 在弹出窗口中，按平时的方式登录：
   - **PlaidCloud 登录** — 您的电子邮件、密码，以及已设置的双重验证码。
   - **单点登录** — 如果您已登录所在组织，此步骤会直接通过。否则会先打开您所在组织的登录页面。
6. 当弹出窗口显示**Authenticated successfully**时，如果窗口没有自动关闭，请将其关闭。

任务窗格标题现在会显示您的工作区和与工作簿关联的项目，旁边是您的账户菜单。请继续阅读[使用表和维度](/zh-cn/reference/cli/plaidxl/retrieve/)。

要为您的账户设置双重身份验证或单点登录，请参阅[成员身份验证](/zh-cn/administration/access/member-authentication/)。

### 使用 Office 账户登录

如果您使用 Microsoft Entra ID 的工作账户登录了 Office，并且 PlaidXL 没有已保存的登录信息，PlaidXL 会通过该账户查找您的工作区，因此无需输入电子邮件：

- **一个工作区** — PlaidXL 开始让您登录该工作区。如果 Excel 询问，请允许弹出窗口；使用单点登录时会直接通过。在 Excel 网页版中，请先单击**Continue as** 您的账户。
- **多个工作区** — 如果工作簿上次使用的是其中某个工作区，PlaidXL 会让您登录该工作区。否则请从**Select a workspace**中选择一个。
- **没有工作区** — 打开电子邮件屏幕，并已填入您的地址。

如果您登录时使用的电子邮件与 Office 账户不同，PlaidXL 会说明是哪一个。**Log out**后，PlaidXL 会等待您自行登录。

### 登录前使用命令

登录之前，您可以单击功能区上的任何 PlaidXL 命令。PlaidXL 会打开任务窗格，让您登录或选择项目，然后在您开始操作的单元格上运行该命令。

## 保持登录状态

PlaidXL 会在此计算机上保持您的登录状态，并在您工作期间在后台续期登录。在之后的会话中打开任务窗格时，会直接进入您的项目。如果登录已完全过期，PlaidXL 会再次询问您的电子邮件。续期登录时出现短暂的网络问题不会使您退出登录；PlaidXL 会重试。

## 您可以看到的内容

PlaidXL 按您的权限读取数据。您只能看到在 PlaidCloud 中有权打开的项目，以及其中的表和维度，其他内容均不可见。如果缺少某个项目或表，请向项目所有者申请访问权限。有关工作区成员资格的工作方式，请参阅[组织和工作区说明](/zh-cn/administration/access/overview/organizations-and-workspaces-explained/)。

## 退出登录或切换工作区

单击任务窗格右上角的账户菜单（三个点）。它会显示您的姓名和工作区，并提供三个命令：

- **Keyboard shortcuts**列出 PlaidXL 的快捷键，您可以更改它们。请参阅[键盘快捷键](/zh-cn/reference/cli/plaidxl/ribbon/#键盘快捷键)。
- **Switch workspace**会使您退出登录并返回电子邮件屏幕，以便在**Select a workspace**下选择其他工作区。出现提示时，请登录新的工作区。切换回已登录过的工作区无需重新登录，取消登录则会保留您当前所在的工作区。
- **Log out**会清除您的登录信息并返回电子邮件屏幕。

每次登录仅对其所属的工作区有效。此次更改之后，所有人都需要登录一次。退出登录状态下，**保存**会显示**Sign in to PlaidCloud to save.**，检索维度时会显示**Sign in to PlaidCloud to retrieve a dimension.**

您的登录由所有已打开的工作簿共享，但每个工作簿保留各自的项目。工作簿的项目属于某个工作区，因此切换之后，关联到旧工作区项目的工作簿在您重新选择之前没有项目。请参阅[项目属于工作簿](/zh-cn/reference/cli/plaidxl/retrieve/#项目属于工作簿)。

## 浅色和深色主题

任务窗格与 PlaidCloud Web 应用保持一致，采用品牌蓝色、导轨式选项卡和列表，并将表、维度、项目和列放在有边界的滚动卡片中。它会跟随您的 Office 主题，并在您更改主题时随之变化。在较窄的窗格中，选项卡排成三列两行；宽度达到 560 像素后排成一行。

## 键盘和屏幕阅读器

项目、表和维度列表中的行可获得键盘焦点，并响应 **Enter** 和**Space** 键。屏幕阅读器会播报所选行；所选状态和警告状态除颜色外还带有图标，具有键盘焦点的控件有清晰的焦点环。

## 数字

任务窗格显示的所有数字，例如行数和列数，以及刷新、重新计算、Explain、Formulas、Report 和规划消息，都遵循 Excel 的显示语言。例如，德语版 Excel 显示 4.812.233。写入单元格的值不会改变。

## 相关内容

- [安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/) — 添加加载项并打开任务窗格
- [故障排除](/zh-cn/reference/cli/plaidxl/troubleshooting/) — 登录弹出窗口无法打开或缺少工作区时
- [查看和管理工作区](/zh-cn/administration/access/overview/viewing-and-managing-workspaces/) — 您所属的工作区
