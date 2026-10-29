---
title: 文档步骤
description: 通过用于文件转换、复制、重命名、删除和 PDF 操作的步骤，在 PlaidCloud 工作流中管理文档。
sidebar:
  label: 文档步骤
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/index.md
---

用于操作文档账户中所存储文件的工作流步骤。可在数据工作流中使用它们移动、转换和变换文档。

## 文件操作

- [Copy Document File 步骤](/zh-cn/reference/workflow-steps/document/copy-document-file/) · [Copy Document Directory 步骤](/zh-cn/reference/workflow-steps/document/copy-document-directory/)
- [Create Document Directory 步骤](/zh-cn/reference/workflow-steps/document/create-document-directory/)
- [Delete Document File 步骤](/zh-cn/reference/workflow-steps/document/delete-document-file/) · [Delete Document Directory 步骤](/zh-cn/reference/workflow-steps/document/delete-document-directory/)
- [目录列表](/zh-cn/reference/workflow-steps/document/directory-listing/) — 写入一张文件夹中文件的表
- [Update Excel Cells 步骤](/zh-cn/reference/workflow-steps/document/document-excel-update/) — 将值写入工作簿的指定单元格，或设置其格式
- [Fix File Extension 步骤](/zh-cn/reference/workflow-steps/document/fix-file-extension/)
- [Rename Document File 步骤](/zh-cn/reference/workflow-steps/document/rename-document-file/) · [Rename Document Directory 步骤](/zh-cn/reference/workflow-steps/document/rename-document-directory/)

复制和重命名步骤将源缺失视为正常情况。当文件，或要复制或重命名的文件夹缺失，或文件夹为空时，步骤不执行任何操作，以指明路径的警告结束，工作流继续运行。当天文件夹中没有文件的计划运行不再失败。

## 加密

- [Encrypt File and Decrypt File 步骤](/zh-cn/reference/workflow-steps/document/encrypt-decrypt-file/) — AES、Blowfish 或 Excel 工作簿密码

## PDF 操作

- [Compress PDF 步骤](/zh-cn/reference/workflow-steps/document/compress-pdf/)
- [Convert Image to PDF 步骤](/zh-cn/reference/workflow-steps/document/convert-image-to-pdf/)
- [Convert PDF or Image to JPEG 步骤](/zh-cn/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge Multiple PDFs 步骤](/zh-cn/reference/workflow-steps/document/merge-multiple-pdfs/)

## 图像操作

- [Crop Image to Headshot 步骤](/zh-cn/reference/workflow-steps/document/crop-image-to-headshot/)

## 文本操作

- [Concatenate Files 步骤](/zh-cn/reference/workflow-steps/document/concatenate-files/) — 将多个文件合并为一个
- [Document Text Substitution 步骤](/zh-cn/reference/workflow-steps/document/document-text-substitution/) — 在文档内查找/替换

## 编码转换

- [Convert Document Encoding 步骤](/zh-cn/reference/workflow-steps/document/convert-document-encoding/) — 选择目标编码
- [Convert Document Encoding to ASCII 步骤](/zh-cn/reference/workflow-steps/document/convert-document-encoding-to-ascii/)
- [Convert Document Encoding to UTF-16 步骤](/zh-cn/reference/workflow-steps/document/convert-document-encoding-to-utf-16/)
- [Convert Document Encoding to UTF-8 步骤](/zh-cn/reference/workflow-steps/document/convert-document-encoding-to-utf-8/)

## 另请参阅

- [Convert Dashboard to PDF 步骤](/zh-cn/reference/workflow-steps/document/dashboard-to-pdf/)
- [Delete Old Files 步骤](/zh-cn/reference/workflow-steps/document/document-delete-old-files/)
- [文档账户](/zh-cn/guides/documents/adding-accounts/) — 使用这些步骤之前先连接文档账户
- [文档指南](/zh-cn/guides/documents/) — 针对相同操作的任务式演练
