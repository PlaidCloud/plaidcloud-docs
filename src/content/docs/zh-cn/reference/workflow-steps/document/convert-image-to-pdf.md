---
title: Convert Image to PDF 步骤
description: 在 PlaidCloud 工作流步骤中将图像文件转换为 PDF 文档，以获得标准化的文档输出和适合归档的格式。
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-image-to-pdf.md
---

将图像（PNG、GIF、TIFF、JPEG 或 HEIC）转换为单页 PDF，或将现有 PDF 重新适配为标准页面大小。

## 输入

- **输入文件或目录**：文档账户中的图像或 PDF，或包含它们的文件夹。
- **目标位置**：写入 PDF 的位置。
- **页面大小**：US Letter、US Legal、A3、A4 或 A5。
- **压缩**：**Lossy** 会将图像缩减为屏幕分辨率，可大幅缩小文件；默认的 **Lossless** 则完全保留图像数据。

## 工作原理

- 图像会被放置在所选大小的页面上，按比例缩放以适合页面，不改变其长宽比。具有多个页面或帧的图像（例如扫描的 TIFF）从其第一页或第一帧转换。
- 使用 **Lossy** 时，结果随后会被压缩，PDF 输入在压缩时会被适配为所选的页面大小。
- 使用 **Lossless** 时，PDF 输入会原样传递，保留其自身的页面大小。

## 输出

每个输入文件生成一个 PDF。对于文件夹，每个文件的 PDF 会写入一个以目标位置命名（不含扩展名）的文件夹中，并使用源文件自身的名称。若要将多个合并为一个文档，请在此步骤之后使用 [Merge Multiple PDFs 步骤](/zh-cn/reference/workflow-steps/document/merge-multiple-pdfs/)。

## 备注

- 如果输入路径不存在或其中没有文件，步骤会以警告结束，警告中指明该路径，不处理任何内容，工作流继续运行。
- 目标位置不能与输入路径相同。

## 常见用途

- 将收据或发票图像标准化为归档格式
- 为只接受 PDF 输入的系统准备图像证据

## 相关内容

- [Convert PDF or Image to JPEG 步骤](/zh-cn/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Compress PDF 步骤](/zh-cn/reference/workflow-steps/document/compress-pdf/)
- [Merge Multiple PDFs 步骤](/zh-cn/reference/workflow-steps/document/merge-multiple-pdfs/)
