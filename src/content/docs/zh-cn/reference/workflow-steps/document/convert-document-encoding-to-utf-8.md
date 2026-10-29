---
title: Convert Document Encoding to UTF-8 步骤
description: 在 PlaidCloud 工作流步骤中将文档文件编码转换为 UTF-8，以便与现代系统和应用程序广泛兼容。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-8.md
---

## 说明

将文本文件重写为 UTF-8。当信息源的编码混杂，或其他工具不支持某些编码时，此步骤尤其有用。

## 工作原理

- 会检测源的编码。UTF-8 文件按 UTF-8 读取，其中混入的 Windows 字符（例如来自 Word 或 Excel 的弯引号）无论数量多少都能完整保留。其他编码的文件，则按从其第一个无效 UTF-8 的部分检测到的编码读取。
- 文本会原样写入，带重音的字母、符号和其他字符都与原来完全一致。
- 无法检测编码的文件会使步骤失败，并指明该文件。
- 如果输入路径不存在或其中没有文件，步骤会以警告结束，警告中指明该路径，不处理任何内容，工作流继续运行。

## 示例

选择输入文件，并在该位置中浏览找到文件。选择所需的输出位置，并浏览选择文件的所需位置。保存并运行。
