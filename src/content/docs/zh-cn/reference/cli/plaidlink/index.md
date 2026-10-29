---
title: PlaidLink
description: 安装并配置 PlaidLink 代理，以安全访问防火墙后的系统，实现远程查询和文件传输。
sidebar:
  label: PlaidLink
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/index.md
---

PlaidLink 可间接访问受防火墙保护或存在其他限制、导致 PlaidCloud 难以直接连接的客户系统和流程。通过在隔离区域内安装 PlaidCloud 代理，PlaidCloud 可以请求代理执行各种操作，例如运行查询、下载或上传文件、检查传感器状态、与 SAP 交互等。

由于代理主动联系 PlaidCloud，并通过标准 HTTPS 网络协议通信，通常只需极少的设置即可运行。此外，代理可以以非特权用户身份运行，从而在受限环境中控制访问权限。

## 主题

- [安装](/zh-cn/reference/cli/plaidlink/install/) — 在 Windows、Linux、macOS 或容器中运行 PlaidLink
- [配置](/zh-cn/reference/cli/plaidlink/configure/) — 连接设置、凭据和运行时选项
- [代理](/zh-cn/reference/cli/plaidlink/agents/) — 管理多个代理及其功能
- [升级](/zh-cn/reference/cli/plaidlink/upgrade/) — 升级到较新的 PlaidLink 版本
