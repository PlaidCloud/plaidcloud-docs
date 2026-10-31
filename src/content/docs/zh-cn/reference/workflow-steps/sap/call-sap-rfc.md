---
title: Call SAP RFC 步骤
description: 通过 PlaidCloud 工作流步骤调用 SAP RFC 函数模块，与 SAP ECC 和 S/4HANA 系统直接集成。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-rfc.md
---

## 说明


调用 SAP ECC / S/4HANA 远程函数调用 (RFC)，并以表格形式检索数据。这些数据随后可用于 PlaidCloud 中的转换流程。


## 数据目标

将 RFC 结果保存为文件或表。

**文件**将结果写为 **JSON**、**逗号分隔**、**制表符分隔**、**竖线分隔**或 **Parquet**。Parquet 文件的列类型与表相同。

**表**将结果保存到**目标表**中，类型取自 RFC 函数自身的字段定义：

| SAP 字段类型 | 保存为 |
|---|---|
| 日期 | 日期。空白或初始日期保存为空。无效日期保存为空，且步骤完成时会给出指明该列的警告。 |
| 压缩十进制数 | 精确的十进制数。超过 10 位小数或 28 位整数时改为保存为文本，且步骤完成时会给出指明该列的警告。 |
| 整数 | 整数。 |
| `FLOAT` | 双精度浮点数。 |
| 十进制浮点数 | 精确文本。 |
| `NUMC`、`CHAR` | 文本，保留前导零。 |
| 时间 | 文本，格式为 `HH:MM:SS`。 |
| 原始字节 | 十六进制文本。 |
| `UTCLONG` | 文本。 |

如果 SAP 无法描述该函数的字段，则十进制数改为保存为精确文本。

当 SAP 描述了该函数时，每个参数都会转换为其所需的类型：日期转换为 `YYYYMMDD`，时间转换为 `HHMMSS`，整数和十进制数转换为数字，文本字段转换为文本，结构参数和表参数则逐字段转换。无法转换为整数或十进制数参数的值会导致步骤失败。

## 示例


### RFC 参数


选择“要使用的代理”。从下拉栏中选择“目标目录”，并在下方浏览到文件的正确子文件夹目标位置。接着，为“Target File Name”设置合适的名称。在“Function Call Information”下，输入 Function、“返回值参数”，并选择参数。

您可以在“Parameters”部分选择“插入行”或“追加行”，并为参数命名和赋值。选择“最大并发请求数”，然后选择 Wait for RFC to Complete。保存并运行步骤。



### 高级值迭代


您可以在此选项卡顶部选择“No Iterators”，然后根据需要选择保存并运行步骤，也可以进行具体指定。


在此处，可以选择“Specify Argument Values”作为“迭代对象”，并创建参数，然后转到“迭代值”。


在“选择要编辑值的迭代器参数”旁边，可以选择“插入行”、“追加行”、“删除行”、“下移”或“移到底部”。
下方可以使用同一个下拉菜单选择“范围迭代器”。最后一部分名为“Exclusions for Selected Range Iteration”，每行同样提供添加、删除等选项。被排除的值可在下方输入。保存并运行步骤。
