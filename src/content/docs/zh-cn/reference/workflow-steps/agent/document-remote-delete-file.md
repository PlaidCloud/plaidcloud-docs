---
title: Document - Remote Delete File 步骤
description: 在 PlaidCloud 工作流中通过 PlaidLink 代理删除远程系统上的文件，在防火墙之后安全地管理文件。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-delete-file.md
---

## 说明



通过 PlaidLink 代理删除位于防火墙之后的文件系统上的文件。代理在本地文件系统上执行删除操作。

可用于本地导出操作后的清理，或需要删除已处理源文件的基于文件的集成。


## 示例


首先，从“要使用的代理”下拉列表中进行选择。接着，在“删除的文件或文件夹路径”下输入文件或文件夹路径。最后，选择“保存并运行步骤”。

## 路径缺失

使用已更新的 PlaidLink 代理时，如果远程系统上不存在该路径，步骤会带着警告 `Nothing to delete at <path>` 而不是错误结束，工作流继续运行。尚未更新的代理仍会使步骤失败。

路径为空时，步骤会带着警告 `No path to delete; nothing deleted.` 结束，并且不删除任何内容。这也包括其文件夹是一个在本次运行中解析为空的变量的路径，例如 `{folder}/archive`。

如果路径是文件系统根目录，或是 PlaidLink 代理工作目录的上级文件夹（`/`、`C:\`、诸如 `\\server\share` 的共享根目录，或 `..`），步骤会在删除任何内容之前失败，并显示 `Refusing to delete the filesystem root <path>.` 或 `Refusing to delete <path>, which contains the agent's working directory.`。您已部署的 PlaidLink 代理就会拒绝根目录和 `..`；已更新的代理还会根据其自身的文件系统判断，拒绝任何其他包含其工作目录的文件夹。
