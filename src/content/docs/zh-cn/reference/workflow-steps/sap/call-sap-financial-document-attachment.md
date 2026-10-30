---
title: Call SAP Financial Document Attachment 步骤
description: 通过 PlaidCloud 工作流步骤检索 SAP 财务凭证附件，实现自动化的文档提取与处理。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## 说明



通过 RFC（远程函数调用）将文件附加到 SAP ECC / S/4HANA 中指定的 FI（财务会计）凭证。适用于将扫描发票、审批流程、合同副本等证明文件与其所支持的财务分录一并过账。

需要在 SAP 连接器上配置 SAP RFC 凭据，以及目标 FI 凭证编号（公司代码、凭证编号、会计年度）。


## 保存时的检查内容

该步骤从其**表数据选择**选项卡上输出列中名为 `relative_file_path` 的列读取每个文件的路径，且该列必须为文本类型。没有该列时保存会被拒绝——*The output columns must include relative_file_path, the path of each file to attach.*——类型不符时同样会被拒绝——*The relative_file_path column must be text, not integer.*

选择了源表但没有源列或目标列时，保存会根据源表填充空的一侧，效果与**填充两个映射表**相同。


## 示例


### RFC 参数


选择“要使用的代理”。从下拉栏中选择“目标目录”，并在下方浏览到文件的正确子文件夹目标位置。接着，为“Target File Name”设置合适的名称。在“Function Call Information”下，输入 Function、“返回值参数”，并选择参数。



您可以在“Parameters”部分选择“插入行”或“追加行”，并为参数命名和赋值。选择“最大并发请求数”，然后选择 Wait for RFC to Complete。保存并运行步骤。
