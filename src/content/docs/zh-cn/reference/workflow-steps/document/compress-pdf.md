---
title: Compress PDF 步骤
description: 在 PlaidCloud 工作流步骤中压缩 PDF 文件，在保持文档质量的同时减小文件大小，提高存储效率。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/compress-pdf.md
---

减小存储在文档账户中的 PDF 的文件大小。适用于在归档、附加到通知或在文档账户之间移动之前，精简体积较大的扫描文档。

## 输入

- **输入文件或目录**：文档账户中的一个 PDF，或包含多个 PDF 的文件夹。
- **输出文件或目录**：写入压缩后 PDF 的位置。

## 工作原理

PDF 会被重写：其中的图像被缩减为屏幕分辨率（72 dpi），字体以子集形式嵌入，这可以大幅缩小扫描文档，而文字依然清晰。页面会适配 US Letter 尺寸。

## 输出

在输出路径生成压缩后的 PDF。对于文件夹，每个 PDF 都写入输出路径之下，并保持其相对于输入文件夹的位置。

## 备注

- 输出路径不能与输入路径相同，因此源文件绝不会被覆盖。
- 如果输入路径不存在或其中没有文件，步骤会以警告结束，警告中指明该路径，不处理任何内容，工作流继续运行。
- 无法压缩的 PDF 会使步骤失败，并指明文件及原因。

## 常见用途

- 在长期存储之前缩小扫描的发票、收据或合同
- 在通过电子邮件发送或附加到通知之前减小 PDF 大小
- 为上传到有大小限制的下游系统准备文档

## 相关内容

- [Convert PDF or Image to JPEG 步骤](/zh-cn/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge Multiple PDFs 步骤](/zh-cn/reference/workflow-steps/document/merge-multiple-pdfs/)
- [文档指南](/zh-cn/guides/documents/)
