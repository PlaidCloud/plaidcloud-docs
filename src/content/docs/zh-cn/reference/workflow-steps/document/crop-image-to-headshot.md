---
title: Crop Image to Headshot 步骤
description: 在 PlaidCloud 工作流步骤中将图像裁剪为正方形头像，用于目录和工牌中的标准化肖像。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/crop-image-to-headshot.md
---

将图像裁剪为居中的正方形，并缩放为 500 × 500 像素的 JPEG。适用于规范员工或成员目录，其中源照片的长宽比各不相同。

## 输入

- **输入文件或目录**：文档账户中的图像，或包含图像的文件夹。
- **输出文件或目录**：写入头像的位置。

## 输出

从源图像中心裁剪出的 500 × 500 JPEG。对于文件夹，每个文件的头像会写入一个以输出路径命名（不含扩展名）的文件夹中。

## 备注

- 裁剪取自图像中心，不会识别人脸，因此请让源照片中的主体居中取景。
- 无法作为图像读取的文件会原样复制到输出，而不会使步骤失败。
- 如果输入路径不存在或其中没有文件，步骤会以警告结束，警告中指明该路径，不处理任何内容，工作流继续运行。
- 输出路径不能与输入路径相同。

## 常见用途

- 规范员工目录照片
- 为内部门户生成风格一致的头像图像
- 为工牌和证件裁剪照片

## 相关内容

- [Convert PDF or Image to JPEG 步骤](/zh-cn/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Fix File Extension 步骤](/zh-cn/reference/workflow-steps/document/fix-file-extension/)
