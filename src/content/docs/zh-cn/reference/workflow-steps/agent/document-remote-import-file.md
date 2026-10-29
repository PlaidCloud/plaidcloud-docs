---
title: Document - Remote Import File 步骤
description: 在 PlaidCloud 工作流中通过 PlaidLink 代理从远程系统导入文件，在防火墙之后安全地获取文件。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-import-file.md
---

## 说明



通过 PlaidLink 代理从远程文件系统拉取文件，并将其存入 PlaidCloud 文档账户。适用于源文件来自内部文件共享、本地服务器或防火墙之后的情况。

代理在本地读取文件并将其流式传输到 PlaidCloud，后续工作流步骤即可在那里处理它。


## 示例


首先，从“要使用的代理”下拉列表中进行选择。接着，在“导入的文件或文件夹路径”下输入文件或文件夹路径。然后在“文件夹目标”下输入目标文件夹。还可以选择一种**压缩**方式，在文件到达时对其压缩：Zip、GZip、BZip2、Zstandard、LZ4、Snappy、LZO 或 Deflate (zlib)。最后，选择“保存并运行步骤”。

## 源文件或文件夹缺失

当远程共享上的该路径下不存在任何内容时，步骤会带着警告 `No file or folder found at <path>; nothing imported.` 而不是错误结束。工作流会继续执行下一步，并且步骤的重试和出错时设置（转到某个步骤，或继续）不会因源缺失而运行。这适用于您已部署的 PlaidLink 代理。

路径为空时，步骤会以同样的方式结束，并显示警告 `No path to import from; nothing imported.`。这也包括其文件夹是一个在本次运行中解析为空的变量的路径，例如 `{folder}/archive`。

如果路径是文件系统根目录，或是 PlaidLink 代理工作目录的上级文件夹（`/`、`C:\`、诸如 `\\server\share` 的共享根目录，或 `..`），步骤会在上传任何内容之前失败，并显示 `Refusing to import from the filesystem root <path>.` 或 `Refusing to import from <path>, which contains the agent's working directory.`。您已部署的 PlaidLink 代理就会拒绝根目录和 `..`；已更新的代理还会根据其自身的文件系统判断，拒绝任何其他包含其工作目录的文件夹。

其他故障仍会使步骤失败：权限被拒绝、上传到 PlaidCloud 失败，或者在已更新的 PlaidLink 代理上，无法访问服务器或共享。

由于没有导入任何内容，上一次运行留下的文档会保留在原处。若要仅在本期文件到达时才运行下游步骤，可以任选其一：

- 为下游步骤添加 **file exists in Document** [步骤条件](/zh-cn/guides/workflows/step-conditions/#文档路径条件)，并将 Document 路径设置为按期间划分的路径，例如在文件名中包含期间的路径。
- 在工作流使用完导入的文档后将其删除，这样缺失的源就不会留下旧文件。
