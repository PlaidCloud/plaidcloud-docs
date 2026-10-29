---
title: CLI 工具
description: PlaidCloud 命令行工具参考，包括 PlaidLink 代理、PlaidXL Excel 加载项，以及用于笔记本集成的 Jupyter CLI。
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

PlaidCloud 提供三种命令行和本机工具，用于在 Web 界面之外使用工作区：

## PlaidLink

[PlaidLink](/zh-cn/reference/cli/plaidlink/) 是运行在您网络内部的代理，用于将 PlaidCloud 工作流连接到受防火墙保护的资源，例如数据库、文件共享以及 PlaidCloud 无法直接访问的其他系统。它可安装为 Windows 服务、Unix/Linux/Mac 守护进程、容器或 Kubernetes Pod。

- [安装](/zh-cn/reference/cli/plaidlink/install/)
- [配置](/zh-cn/reference/cli/plaidlink/configure/)
- [代理](/zh-cn/reference/cli/plaidlink/agents/)
- [升级](/zh-cn/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/zh-cn/reference/cli/plaidxl/) 是 PlaidCloud 的 Microsoft Excel 加载项。它将项目表和维度提取到工作表中，按需刷新，并添加 `PLAIDXL` 公式，用于根据 PlaidCloud 数据计算汇总值。

- [安装](/zh-cn/reference/cli/plaidxl/install/)
- [登录](/zh-cn/reference/cli/plaidxl/connect/)
- [使用表和维度](/zh-cn/reference/cli/plaidxl/retrieve/)
- [自定义函数](/zh-cn/reference/cli/plaidxl/functions/)
- [使用自定义函数构建报表](/zh-cn/reference/cli/plaidxl/build-a-report/)
- [PlaidCloud 功能区](/zh-cn/reference/cli/plaidxl/ribbon/)
- [故障排除](/zh-cn/reference/cli/plaidxl/troubleshooting/)

## Jupyter CLI

[Jupyter CLI](/zh-cn/reference/cli/jupyter/) 让数据科学家借助支持 PlaidCloud 的 CLI 和 Python 辅助工具，在 Jupyter 笔记本中使用 PlaidCloud 项目数据。

- [命令行](/zh-cn/reference/cli/jupyter/command-line/)
- [Jupyter 笔记本](/zh-cn/reference/cli/jupyter/jupyter-notebook/)
- [OAuth 设置](/zh-cn/reference/cli/jupyter/oauth-setup/)
