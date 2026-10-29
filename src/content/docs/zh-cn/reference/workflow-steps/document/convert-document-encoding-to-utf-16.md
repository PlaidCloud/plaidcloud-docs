---
title: Convert Document Encoding to UTF-16 步骤
description: 在 PlaidCloud 工作流步骤中将文档文件编码转换为 UTF-16，以支持多字节字符集和 Unicode 文本。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-16.md
---

## 说明

将文本文件重写为 UTF-16。当下游系统要求 UTF-16，或源混杂了其他工具无法接受的编码时很有用。

## 输入

- **输入文件或目录**：要转换的文本文件，或包含文本文件的文件夹。
- **目标位置**：写入转换后文件的位置。
- **压缩**：输出使用不压缩、Zip、GZip 或 BZip2。
- **字节序（字节顺序）**：小端序或大端序。
- **Include BOM**：勾选后，文件以字节顺序标记开头（小端序为 `FF FE`，大端序为 `FE FF`）。不勾选则不带标记。

## 工作原理

- 会检测源的编码。UTF-8 文件按 UTF-8 读取，其中混入的 Windows 字符（例如来自 Word 或 Excel 的弯引号）无论数量多少都能完整保留。其他编码的文件，则按从其第一个无效 UTF-8 的部分检测到的编码读取。
- 文本会原样写入，带重音的字母、符号和其他字符都与原来完全一致。
- 无法检测编码的文件会使步骤失败，并指明该文件。
- 如果输入路径不存在或其中没有文件，步骤会以警告结束，警告中指明该路径，不处理任何内容，工作流继续运行。
- 对于文件夹，每个文件都会被转换，并以其自身的名称写入目标位置。子文件夹中的文件会写入目标位置本身，而不是对应的子文件夹。

## 示例

选择输入文件，并在该位置中浏览找到文件。选择所需的输出位置，选择字节顺序，如果接收系统需要，请勾选 **Include BOM**。保存并运行。
