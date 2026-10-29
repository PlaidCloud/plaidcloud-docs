---
title: Concatenate Files 步骤
description: 在 PlaidCloud 工作流步骤中将多个文件拼接为单个文件，用于合并文本、CSV 或其他文档输出。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/concatenate-files.md
---

将文档账户中的两个或多个文件合并为单个输出文件。按字节逐个操作，适用于简单拼接即可生成有效输出的纯文本格式（CSV、日志文件、JSON Lines）。

## 输入

- **源文件**：要拼接的文件列表，按顺序排列
- **输出路径**：合并后文件的目标位置
- **分隔符**：可选，插入到各源文件之间的字节序列（通常为换行符）

## 输出

单个文件，包含所有源文件按所列顺序排列的内容，并以配置的分隔符连接。

不存在的源文件不会包含在合并后的文件中，步骤会以警告结束，警告中指明该文件，因此工作流继续运行。

## 常见用途

- 将每日日志文件合并为月度归档
- 合并具有相同架构的 CSV 文件（除第一个文件外，其余文件去掉标题行）
- 在处理之前，连接来自多个源的 JSON Lines 导出

## 不适用于

- PDF：请改用 [Merge Multiple PDFs 步骤](/zh-cn/reference/workflow-steps/document/merge-multiple-pdfs/)
- 带标头的二进制格式（XLSX、ZIP、图像文件）：拼接字节无法生成有效文件

## 相关内容

- [Merge Multiple PDFs 步骤](/zh-cn/reference/workflow-steps/document/merge-multiple-pdfs/)
- [文档指南](/zh-cn/guides/documents/)
