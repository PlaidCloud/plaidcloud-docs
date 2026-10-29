---
title: Convert PDF or Image to JPEG 步骤
description: 在 PlaidCloud 工作流步骤中将 PDF 页面或图像转换为 JPEG 格式，用于兼容网页的输出和图像处理任务。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg.md
---

将 PDF 或图像转换为 JPEG。PDF 的第一页会成为 JPEG；图像会被重新编码，具有多个页面或帧的图像（例如扫描的 TIFF）从其第一页或第一帧转换。

## 输入

- **输入文件或目录**：文档账户中的 PDF 或图像（PNG、GIF、TIFF、JPEG 或 HEIC），或包含它们的文件夹。
- **输出文件或目录**：写入 JPEG 的位置。

## 输出

每个输入文件生成一个 JPEG。对于文件夹，每个文件的 JPEG 会写入一个以输出路径命名（不含扩展名）的文件夹中，并使用源文件自身的名称。

## 备注

- 任何其他类型的文件都会使步骤失败，并指明其接受的类型。
- 如果输入路径不存在或其中没有文件，步骤会以警告结束，警告中指明该路径，不处理任何内容，工作流继续运行。
- 输出路径不能与输入路径相同。

## 常见用途

- 生成用于网页显示的预览图像
- 为无法处理 PDF 的系统生成 PDF 的纯图像版本

## 相关内容

- [Convert Image to PDF 步骤](/zh-cn/reference/workflow-steps/document/convert-image-to-pdf/)
- [Compress PDF 步骤](/zh-cn/reference/workflow-steps/document/compress-pdf/)
- [Crop Image to Headshot 步骤](/zh-cn/reference/workflow-steps/document/crop-image-to-headshot/)
