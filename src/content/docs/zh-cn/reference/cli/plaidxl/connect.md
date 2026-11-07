---
title: 登录 PlaidXL
description: 使用电子邮件和您常用的登录方式（包括单点登录和双重身份验证）将 PlaidXL 连接到 PlaidCloud 工作区，并了解如何退出登录或切换工作区。
sidebar:
  label: 登录
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL 以您本人的身份登录，使用的登录方式与在浏览器中登录 PlaidCloud 相同。无需输入服务器地址，工作簿中也不会存储密码。

## 登录

1. 打开任务窗格：**PlaidCloud → Open PlaidXL**，或在 **连接** 组中点击 **账户**。
2. 在 **Enter your email** 下输入您用于 PlaidCloud 的电子邮件地址，然后点击 **Sign In**。PlaidXL 会记住该地址，供下次使用。
3. 如果您的电子邮件属于多个工作区，请从 **Select a workspace** 中选择一个，然后点击 **Sign In**。PlaidXL 会记住您的选择。如果您只属于一个工作区，PlaidXL 会自动选择该工作区。如果没有工作区与该电子邮件关联，窗格会给出提示；请检查地址后重试。
4. Excel 会询问是否允许弹出窗口。请允许。
5. 在弹出窗口中，按您平时的方式登录：
   - **PlaidCloud 登录**：您的电子邮件、密码以及已设置的双重验证码。
   - **单点登录**：如果您已登录所在组织，此步骤会直接通过。否则会先打开您所在组织的登录页面。
6. 当弹出窗口显示 **Authenticated successfully** 时，如果窗口没有自动关闭，请手动关闭。

任务窗格标题栏现在会显示您的工作区和与工作簿关联的项目，旁边是您的账户菜单。继续阅读[处理表和维度](/zh-cn/reference/cli/plaidxl/retrieve/)。

要为您的账户设置双重身份验证或单点登录，请参阅[成员身份验证](/zh-cn/administration/access/member-authentication/)。

### 使用 Office 账户登录

如果您使用 Microsoft Entra ID 的工作账户登录了 Office，且 PlaidXL 没有已保存的登录信息，它会通过该账户查找您的工作区，因此无需输入电子邮件：

- **一个工作区**：PlaidXL 开始登录该工作区。如果 Excel 提示，请允许弹出窗口；使用单点登录时会直接通过。在网页版 Excel 中，请先点击 **Continue as** 您的账户。
- **多个工作区**：如果工作簿上次使用过其中一个工作区，PlaidXL 会登录该工作区。否则，请从 **Select a workspace** 中选择一个。
- **没有工作区**：打开电子邮件界面，并已填入您的地址。

如果您使用的电子邮件与 Office 账户不同，PlaidXL 会告知是哪一个。执行 **退出登录** 后，PlaidXL 会等待您自行登录。

### 登录前的命令

登录之前，您可以点击功能区上的任何 PlaidXL 命令。PlaidXL 会打开任务窗格让您登录或选择项目，然后在您开始操作时所在的单元格上运行该命令。

## 保持登录状态

PlaidXL 会在这台计算机上保持您的登录状态，并在您工作时于后台续期登录。在之后的会话中打开任务窗格时，会直接进入您的项目。如果登录已完全过期，PlaidXL 会再次询问您的电子邮件。续期登录时出现短暂的网络问题不会使您退出登录；PlaidXL 会重试。

## 您能看到的内容

PlaidXL 以您的权限读取数据。您只能看到在 PlaidCloud 中可以打开的项目，以及其中的表和维度，不会更多。如果缺少某个项目或表，请向项目所有者申请访问权限。有关工作区成员资格的工作方式，请参阅[组织和工作区说明](/zh-cn/administration/access/overview/organizations-and-workspaces-explained/)。

## 退出登录或切换工作区

点击任务窗格右上角的账户菜单（三个点）。它显示您的姓名和工作区，并提供三个命令：

- **Keyboard shortcuts** 列出 PlaidXL 的快捷键，方便您更改。请参阅[键盘快捷键](/zh-cn/reference/cli/plaidxl/ribbon/#键盘快捷键)。
- **Switch workspace** 会使您退出登录并返回电子邮件界面，以便在 **Select a workspace** 下选择其他工作区。出现提示时，请登录新的工作区。切换回已登录过的工作区无需重新登录，取消登录则会保留您当前所在的工作区。
- **Log out** 会清除您的登录信息并返回电子邮件界面。

每次登录仅对其所在的工作区有效。此更改后，所有人都需要登录一次。退出登录后，**保存** 会显示 **Sign in to PlaidCloud to save.**，检索维度时会显示 **Sign in to PlaidCloud to retrieve a dimension.**

您的登录由已打开的所有工作簿共享，但每个工作簿都有各自的项目。工作簿的项目属于某个工作区，因此切换后，关联到旧工作区中项目的工作簿将没有项目，直到您重新选择。请参阅[项目属于工作簿](/zh-cn/reference/cli/plaidxl/retrieve/#项目属于工作簿)。

## 浅色和深色主题

任务窗格会跟随 Office 主题，并在您更改主题时随之变化。

## 键盘和屏幕阅读器

项目、表和维度列表中的行可获得键盘焦点，并响应 **Enter** 和 **空格**。屏幕阅读器会播报所选行，已选择和警告状态除了颜色外还带有图标。

## 相关内容

- [安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/)：添加加载项并打开任务窗格
- [故障排除](/zh-cn/reference/cli/plaidxl/troubleshooting/)：登录弹出窗口未打开或缺少工作区时
- [查看和管理工作区](/zh-cn/administration/access/overview/viewing-and-managing-workspaces/)：您所属的工作区
