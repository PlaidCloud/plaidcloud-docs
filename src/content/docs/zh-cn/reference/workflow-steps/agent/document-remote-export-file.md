---
title: Document - Remote Export File 步骤
description: 在 PlaidCloud 工作流中通过 PlaidLink 代理将文件导出到远程系统，在防火墙之后安全地传输文件。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-export-file.md
---

## 说明



通过 PlaidLink 代理，将 PlaidCloud 文档账户中的文件写入远程文件系统。适用于将报表、提取结果或已处理文件交付给 PlaidCloud 无法直接访问的系统，例如内部共享驱动器、本地 SFTP 服务器或专用应用程序目录。

代理从 PlaidCloud 接收文件，并将其写入配置的本地目标。


## 示例


首先，从“要使用的代理”下拉列表中进行选择。接着，在“要导出的文件或文件夹”下浏览选择文件或文件夹路径。然后在“导出路径目标”下输入位置。最后，选择“保存并运行步骤”。

## 路径安全

导出路径为空时，步骤会失败，并显示 `No destination path for the export; it would write into the agent's working directory.`。这也包括因其中的变量为空而解析为空的路径。导出到驱动器或共享根目录（例如 `E:\` 或 `\\nas\drop`）是可行的。

选中**到达后解压缩归档**时，步骤会解压目标文件夹中的每个归档并将其删除。因此，它会拒绝作为文件系统根目录的目标，或直接位于根目录中的文件（`Refusing to unpack an export into the filesystem root <path>.`），以及 PlaidLink 代理自己的文件夹（`Refusing to unpack an export into <path>, which contains the agent's working directory.`）。请改为选择专用的子文件夹。

空路径检查和根目录检查适用于您已部署的 PlaidLink 代理。拒绝代理自己的文件夹需要更新的 PlaidLink 代理。
