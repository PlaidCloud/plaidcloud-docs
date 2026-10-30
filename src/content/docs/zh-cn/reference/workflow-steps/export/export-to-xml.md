---
title: Export to XML 步骤
description: 通过 PlaidCloud 工作流步骤将数据导出为 XML 文件，用于结构化数据交换和系统集成。
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-xml.md
---

## 说明

将 PlaidCloud 项目表作为 XML 文件写入文档账户。当下游系统需要 XML 输入时使用——常见于较旧的企业集成、政府申报或特定行业的数据交换格式。

XML 结构与表一致：每行一个元素，每列一个子元素。如需更多地控制结构，可对模板文件使用 [Document Text Substitution](/zh-cn/reference/workflow-steps/document/document-text-substitution/)，采用模板化方式。

## 文件已存在时

在**文件已存在时**下，**已存在的文件**（`if_exists`）决定文件已存在时的处理方式。**覆盖它**（`overwrite`，默认）会替换已存在的文件；**使步骤失败且不写入任何内容**（`fail`）会在要写入的文件已存在时使步骤停止，且不写入任何内容。
