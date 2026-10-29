---
title: Report Single 步骤
description: 使用模板、数据源和可配置的布局选项，通过 PlaidCloud 工作流步骤生成单个 PDF 报表。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/report-single.md
---

## 说明



根据 RML（Report Markup Language）模板渲染 PDF 报表，并用一个或多个 PlaidCloud 表中的数据填充。适用于正式、格式化的报表，例如发票、财务报表、监管申报文件和品牌化摘要。

RML 模板定义布局（页面大小、字体、固定文本、表的位置），输入表提供可变数据。如果一个模板需要生成多份报表（例如每个客户一份），请参阅 [Reports Batch 步骤](/zh-cn/reference/workflow-steps/reports/reports-batch/)。


## 模板读取的名称

模板通过名称读取**报表数据**选项卡上的每个源，以及**报表常量（固定值）** 下的每个常量。新源会命名为 `new_source`、`new_source_2` 等，模板可以直接读取这些名称；请将其重命名为能说明其内容的名称。


## 保存时的检查

每个源名称和常量名称必须满足：

- **已填写**：空白名称会被拒绝。
- **唯一**：两个源、两个常量，或一个源与一个常量不能同名，因为模板只能看到其中一个：*Source name 'sales' is also a constant name; rename one of them.*
- **模板可读取**：由字母、数字和下划线组成，并以字母或下划线开头：*Constant name 'fiscal year' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*
- **不是模板保留字**：`True`、`False`、`None`、`true`、`false`、`none`、`not` 和 `self` 会被解读为数据以外的含义：*Source name 'self' is a word the template reserves, so it can't be read as a name.*


## 示例

暂无示例……
