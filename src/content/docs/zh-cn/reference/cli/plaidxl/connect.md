---
title: 登录 PlaidXL
description: 使用电子邮件和常用登录方式（包括单点登录和双重身份验证）将 PlaidXL 连接到 PlaidCloud 工作区，然后退出登录或切换工作区。
sidebar:
  label: 登录
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL 以您本人的身份登录，使用的登录方式与在浏览器中登录 PlaidCloud 时相同。无需输入服务器地址，工作簿中也不会存储密码。

## 登录

1. 打开任务窗格：**PlaidCloud → Show Taskpane**。
2. 在 **Enter your email** 下，输入用于 PlaidCloud 的电子邮件地址，然后单击 **Sign In**。
3. 如果您的电子邮件属于多个工作区，请从 **Select a tenant** 中选择一个，然后单击 **Sign In**。（PlaidXL 中的 *tenant* 即您的 PlaidCloud 工作区。）如果只属于一个工作区，PlaidXL 会自动选择。
4. Excel 会询问是否允许弹出窗口，请选择允许。
5. 在弹出窗口中，按平时的方式登录：
   - **PlaidCloud 登录** — 电子邮件、密码以及您设置的任何双重验证码。
   - **单点登录** — 如果您已登录所在组织，此步骤会直接通过；否则会先打开所在组织的登录页面。
6. 弹出窗口显示 **Authenticated successfully** 后，如果它没有自动关闭，请手动关闭。

任务窗格现在会显示 **Connected to** 您的工作区 ID **as** 您的用户名，下方列出您的项目。继续阅读[处理表和维度](/zh-cn/reference/cli/plaidxl/retrieve/)。

若要为账户设置双重身份验证或单点登录，请参阅[成员身份验证](/zh-cn/administration/access/member-authentication/)。

## 保持登录状态

PlaidXL 会在这台计算机上保持您的登录状态，并在您工作时于后台续期。在之后的会话中打开任务窗格时，会直接进入您的项目。如果登录已完全过期，PlaidXL 会再次要求输入电子邮件。

## 可见内容

PlaidXL 以您的权限读取数据。您只能看到在 PlaidCloud 中可以打开的项目，以及其中的表和维度。如果缺少某个项目或表，请向项目所有者申请访问权限。有关工作区成员资格的工作方式，请参阅[组织和工作区详解](/zh-cn/administration/access/overview/organizations-and-workspaces-explained/)。

## 退出登录或切换工作区

单击任务窗格顶部的 **Logout**。PlaidXL 会清除您的登录信息并返回电子邮件界面。

若要在其他工作区中工作，请先退出登录，然后重新登录，并在 **Select a tenant** 下选择另一个工作区。PlaidXL 一次只使用一个工作区，适用于您打开的所有工作簿。

## 浅色和深色主题

任务窗格跟随 Office 主题。若要固定为浅色或深色，请单击任务窗格左上角的太阳或月亮按钮。

## 相关内容

- [安装 PlaidXL](/zh-cn/reference/cli/plaidxl/install/) — 添加加载项并打开任务窗格
- [故障排除](/zh-cn/reference/cli/plaidxl/troubleshooting/) — 登录弹出窗口无法打开或工作区缺失时
- [查看和管理工作区](/zh-cn/administration/access/overview/viewing-and-managing-workspaces/) — 您所属的工作区
