---
title: Merge Multiple PDFs 步骤
description: 在 PlaidCloud 工作流步骤中将多个 PDF 文件合并为一个文档，用于报表组装和汇总。
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/merge-multiple-pdfs.md
---

将文件夹中的 PDF 合并为单个 PDF。与 [Concatenate Files 步骤](/zh-cn/reference/workflow-steps/document/concatenate-files/)不同，此步骤理解 PDF 格式，并生成有效的合并文档。

## 输入

- **输入目录** — 文档账户中要合并其 PDF 的文件夹。也可以改为提供单个归档（例如包含 PDF 的 ZIP），此时会合并其中的 PDF。
- **输出合并文件** — 合并后的 PDF 的写入位置。

## 工作方式

- PDF 按路径顺序合并，其中的数字按数值比较 — `page2.pdf` 排在 `page10.pdf` 之前 — 因此请为文件编号以控制顺序。每个 PDF 保持其自身页面的顺序。
- 只合并名称为 `.pdf` 的文件。文件夹中的其他内容会被排除，文件夹中的归档不会被打开。
- 子文件夹中的文件按文档账户的列出方式包含：S3、Wasabi 和 Google Cloud Storage 账户会列出整个文件夹树，而 OneDrive、SFTP 和 Azure 账户只列出顶层。
- 最多合并 100 个 PDF；超过则步骤失败。

## 输出

输出路径处的单个 PDF，包含所有被合并 PDF 的每一页。

## 备注

- 文件夹中没有 PDF 或文件夹不存在时，步骤会以指明该文件夹的警告结束，不合并任何内容，工作流继续运行。
- 输出路径不能与输入路径相同。

## 常见用途

- 用各份报表 PDF 组装月度报表
- 将封面、正文和附录合并为一份交付物
- 将生成的发票打包为按客户或按期间划分的归档

## 相关内容

- [Compress PDF 步骤](/zh-cn/reference/workflow-steps/document/compress-pdf/) — 缩小合并后的结果
- [Convert Image to PDF 步骤](/zh-cn/reference/workflow-steps/document/convert-image-to-pdf/) — 合并前将图像转换为 PDF
