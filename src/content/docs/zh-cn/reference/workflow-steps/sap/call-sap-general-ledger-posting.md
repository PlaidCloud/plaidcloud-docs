---
title: Call SAP General Ledger Posting 步骤
description: 调用 SAP ECC / S/4HANA 远程函数调用 (RFC)，用于过账日记账分录，包括适用的增值税和预扣税。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-general-ledger-posting.md
---

## 说明


调用 SAP ECC / S/4HANA 远程函数调用 (RFC)，用于过账日记账分录，包括适用的增值税和预扣税。也可以在测试模式下运行，此时会执行过账流程但不会完成过账，从而收集可检测到的错误，例如科目已关闭，或指定的公司代码中不存在某个客户。错误检查非常全面，单次测试即可返回多个检测到的错误。


## 示例


### RFC 参数


选择“要使用的代理”。从下拉栏中选择“目标目录”，并在下方浏览到文件的正确子文件夹目标位置。接着，为“Target File Name”设置合适的名称。在“Function Call Information”下，输入 Function、“返回值参数”，并选择参数。



您可以在“Parameters”部分选择“插入行”或“追加行”，并为参数命名和赋值。选择“最大并发请求数”，然后选择 Wait for RFC to Complete。保存并运行步骤。
