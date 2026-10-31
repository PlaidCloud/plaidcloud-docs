---
title: Document Text Substitution 步骤
description: 在 PlaidCloud 工作流步骤中对文档执行文本查找和替换，实现内容的自动转换。
sidebar:
  order: 15
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-text-substitution.md
---

## 说明

在文本文件内查找并替换。将特定字符串或占位符替换为新值，适用于模板化（将 `CUSTOMER_NAME` 之类的占位符替换为实际名称）或文本脱敏（删除或遮盖特定字符串）。

适用于任意大小的 UTF-8 文本文件（TXT、CSV、JSON、XML、HTML、RML）。不是 UTF-8 文本的文件（如 PDF 或 Office 文档）会使步骤失败。

## 输入

- **输入文件或目录** — 要修改的文件，或包含多个文件的文件夹。
- **目标文件或目录** — 结果的写入位置。结果始终写入输入所在的文档账户；目标仅设置路径。
- **压缩** — 输出可选择不压缩、Zip、GZip、BZip2、Zstandard、LZ4、Snappy、LZO 或 Deflate (zlib)。Snappy 和 LZ4 以 Spark 和 Hadoop 可读取的块格式写入，LZO 则写为 `lzop` 文件。
- **文本替换操作顺序** — 每个替换占一行，每行给出原始文本及其替换内容。替换内容中可以使用变量。

## 工作方式

- 替换自上而下依次执行，每一行都作用于其上各行处理后的结果，因此某个替换可以修改前面某行写入的文本。
- 匹配是精确的且区分大小写，所有出现的位置都会被替换。
- 原始文本为空的行会被忽略。
- 对于文件夹，每个文件会写入一个以目标命名（不含扩展名）的文件夹中，文件名保持不变。
- 如果输入路径不存在或其中没有文件，步骤会以指明该路径的警告结束，不处理任何内容，工作流继续运行。

## 示例

| 原始文本 | 替换内容 | `Dear CUSTOMER_NAME,` 变为 |
|---|---|---|
| `CUSTOMER_NAME` | `Acme Ltd` | `Dear Acme Ltd,` |
