---
title: CLI 工具
description: PlaidCloud 命令行工具参考——PlaidLink 代理、PlaidXL Excel 加载项，以及用于笔记本集成的 Jupyter CLI。
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

PlaidCloud 提供三种命令行和本机工具，用于在 Web 界面之外使用工作区：

## PlaidLink

[PlaidLink](/zh-cn/reference/cli/plaidlink/) 是一个在您的网络内部运行的代理，用于将 PlaidCloud 工作流桥接到受防火墙保护的资源——数据库、文件共享以及 PlaidCloud 无法直接访问的其他系统。它可以作为 Windows 服务、Unix/Linux/Mac 守护进程、容器或 Kubernetes Pod 安装。

- [安装](/zh-cn/reference/cli/plaidlink/install/)
- [配置](/zh-cn/reference/cli/plaidlink/configure/)
- [代理](/zh-cn/reference/cli/plaidlink/agents/)
- [升级](/zh-cn/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/zh-cn/reference/cli/plaidxl/) 是适用于 Microsoft Excel 的 PlaidCloud 加载项。它将项目表和维度检索到工作表中，按需刷新，提供 `PLAIDXL` 公式以基于 PlaidCloud 数据计算汇总值和受管控的指标，并可写回规划值。

- [安装](/zh-cn/reference/cli/plaidxl/install/)
- [登录](/zh-cn/reference/cli/plaidxl/connect/)
- [使用表和维度](/zh-cn/reference/cli/plaidxl/retrieve/)
- [自定义函数](/zh-cn/reference/cli/plaidxl/functions/)
- [构建报表](/zh-cn/reference/cli/plaidxl/build-a-report/)
- [钻取、选取成员和说明数字](/zh-cn/reference/cli/plaidxl/drill/)
- [向 PlaidCloud 输入值](/zh-cn/reference/cli/plaidxl/write-values/)
- [在 Excel 中询问 Weave](/zh-cn/reference/cli/plaidxl/weave/)
- [PlaidCloud 功能区](/zh-cn/reference/cli/plaidxl/ribbon/)
- [故障排除](/zh-cn/reference/cli/plaidxl/troubleshooting/)

## Jupyter CLI

[Jupyter CLI](/zh-cn/reference/cli/jupyter/) 让数据科学家可以使用支持 PlaidCloud 的 CLI 和 Python 辅助工具，在 Jupyter 笔记本中处理 PlaidCloud 项目数据。

- [命令行](/zh-cn/reference/cli/jupyter/command-line/)
- [Jupyter 笔记本](/zh-cn/reference/cli/jupyter/jupyter-notebook/)
- [OAuth 设置](/zh-cn/reference/cli/jupyter/oauth-setup/)
