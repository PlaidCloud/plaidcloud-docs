---
title: Document - Remote Rename File 步骤
description: 在 PlaidCloud 工作流中通过 PlaidLink 代理重命名远程系统上的文件，在防火墙之后安全地管理文件。
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-rename-file.md
---

## 说明



通过 PlaidLink 代理重命名或移动远程文件系统上的文件。完全在本地端运行；不会向 PlaidCloud 传输数据，也不会从 PlaidCloud 传出数据。

常见模式：在远程导入步骤成功后，将源文件重命名以标记为“已处理”，这样同一工作流在下次运行时就不会重复导入它。


## 示例


首先，从“要使用的代理”下拉列表中进行选择。 



接着，输入“源路径”和“目标路径”。 



最后，选择“保存并运行步骤”。

## 源缺失

使用已更新的 PlaidLink 代理时，如果远程系统上不存在该源，步骤会带着警告 `No file or folder found at <path>; nothing renamed` 而不是错误结束，工作流继续运行。尚未更新的代理仍会使步骤失败。

源路径为空时，步骤会带着警告 `No path to rename from; nothing renamed.` 结束，路径中的某个文件夹是在本次运行中解析为空的变量时也是如此。

如果源是文件系统根目录，或是 PlaidLink 代理工作目录的上级文件夹（`/`、`C:\`、诸如 `\\server\share` 的共享根目录，或 `..`），步骤会失败，并显示 `Refusing to rename from the filesystem root <path>.` 或 `Refusing to rename from <path>, which contains the agent's working directory.`。目标路径为空时，步骤会失败，并显示 `No destination path for the rename; it would write into the agent's working directory.`。重命名到驱动器或共享根目录（例如 `E:\` 或 `\\nas\drop`）是可行的。您已部署的 PlaidLink 代理就会拒绝根目录和 `..`；已更新的代理还会根据其自身的文件系统判断，拒绝任何其他包含其工作目录的文件夹。
