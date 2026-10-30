---
title: Call SAP Master Data Table RFC 步骤
description: 调用 SAP ECC / S/4HANA 远程函数调用 (RFC)，用于访问主数据表并以表格形式检索数据。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-master-data-table-rfc.md
---

## 说明


调用 SAP ECC / S/4HANA 远程函数调用 (RFC)，用于访问主数据表并以表格形式检索数据。这些数据随后可用于 PlaidCloud 中的转换流程。它还支持将主数据表结构导出到单独的文件，其中包含列名、数据类型和列顺序信息。


## 示例


### RFC 参数


选择“要使用的代理”。从下拉栏中选择“目标目录”，并在下方浏览到文件的正确子文件夹目标位置。接着，为“Target File Name”设置合适的名称。在“Function Call Information”下，输入 Function、“返回值参数”，并选择参数。



您可以在“Parameters”部分选择“插入行”或“追加行”，并为参数命名和赋值。选择“最大并发请求数”，然后选择 Wait for RFC to Complete。保存并运行步骤。
