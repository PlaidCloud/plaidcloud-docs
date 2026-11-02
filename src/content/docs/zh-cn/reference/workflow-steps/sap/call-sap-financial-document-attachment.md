---
title: Call SAP Financial Document Attachment 步骤
description: 通过 PlaidCloud 工作流步骤检索 SAP 财务凭证附件，以便自动提取和处理文档。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## 描述



通过 RFC（远程函数调用）将文件附加到 SAP ECC / S/4HANA 中指定的 FI（财务会计）凭证。可用于将扫描的发票、审批流程、合同副本等证明文档与其所支持的财务分录一并过账。

需要在 SAP 连接器上配置的 SAP RFC 凭据，以及目标 FI 凭证编号（公司代码、凭证编号、会计年度）。


## 保存时会检查什么

步骤从**列**选项卡上输出列中的 `relative_file_path` 列读取每个文件的路径，且该列必须为文本类型。没有该列时，保存会被拒绝，提示为*输出列必须包含 relative_file_path，即要附加的每个文件的路径。*；如果它是其他类型，也会被拒绝，提示为*relative_file_path 列必须是文本类型，而不是整数。*

如果已选择源表但没有源列或目标列，保存时会像**填充两个映射表**一样，用源表填充空的一侧。


## 示例


### RFC 参数


选择“要使用的代理”。从下拉栏中选择**目标目录**，并在下方浏览选择文件的正确子文件夹目标位置。接着，为“Target File Name”适当命名。在“Function Call Information”下，输入函数、**返回值参数**，并选择参数。



您可以在参数部分选择**插入行**或**追加行**，也可以为参数命名并赋值。选择**最大并发请求数**，并选中“Wait for RFC to Complete”。保存并运行步骤。
