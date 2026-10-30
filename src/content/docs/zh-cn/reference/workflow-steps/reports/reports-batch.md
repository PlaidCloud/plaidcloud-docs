---
title: Reports Batch 步骤
description: 通过 PlaidCloud 工作流步骤生成批量 PDF 报表，使用不同的数据输入，由模板生成多份报表。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/reports-batch.md
---

## 说明



根据单个 RML 模板，由控制表驱动，渲染多份 PDF 报表。控制表的每一行生成一份报表，该行的列值用作该报表渲染时的参数。

常见用途：客户对账单（每个客户一份 PDF）、各业务单元财务报表（每个业务单元一份 PDF）、发票（每个订单一份 PDF）。如需一次性生成单份报表，请参阅 [Report Single 步骤](/zh-cn/reference/workflow-steps/reports/report-single/)。


## 模板读取的名称

模板通过名称读取**报表数据**选项卡上的每个源，以及**批处理记录值数据源**映射中的每个目标列。没有常量部分：每个批处理行为其报表提供模板所需的值。新源会命名为 `new_source`、`new_source_2` 等，模板可以直接读取这些名称。


## 保存时的检查

每个源名称和批处理列名称必须已填写、唯一，并且模板可读取，规则与 [Report Single 步骤](/zh-cn/reference/workflow-steps/reports/report-single/)相同，只是用批处理列代替常量：*Batch column name 'unit id' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*

如果已选择批处理源表但批处理映射为空，保存时会根据该表填充映射，效果与“填充”相同。


## 空批处理表

当批处理源表没有任何行时，步骤会成功完成，并给出指明该批处理表的警告，不会生成任何报表。


## 示例

暂无示例……
