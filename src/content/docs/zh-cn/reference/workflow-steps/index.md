---
title: 工作流步骤
description: PlaidCloud 中的所有工作流步骤类型——导入、导出、转换、分摊、维度、文档、通知等。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/index.md
---

工作流步骤是 PlaidCloud 自动化的构建块。每个步骤执行一项操作（导入 CSV、联接两个表、发送通知），多个步骤组合成工作流，可按顺序、并行、有条件或循环运行。

## 类别

### 数据移动

- [导入](/zh-cn/reference/workflow-steps/import/)——从 CSV、Excel、Parquet、JSON、ORC、Delta Lake、SQL、BigQuery、MongoDB、Kafka、SPSS、Singer 源等拉取数据
- [导出](/zh-cn/reference/workflow-steps/export/)——将数据推送到 CSV、XML、SQL、Excel、Google 表格、Parquet、ORC、MongoDB、Kafka、表归档等

### 表转换

- [表](/zh-cn/reference/workflow-steps/tables/)——联接、合并、筛选、查找、透视、融合、定向更新、基于源表的行访问授权、还原到某个时间点
- [通用操作](/zh-cn/reference/workflow-steps/common/)——共用的数据映射和筛选模式

### 地理空间

- [地理空间](/zh-cn/reference/workflow-steps/spatial/)——导入和导出空间文件、缓冲、匹配、测量、重新投影以及构建几何图形；完整覆盖 Alteryx 空间工具

### 建模

- [分摊](/zh-cn/reference/workflow-steps/allocation/)——基于动因的分配、拆分分摊、基于规则的标记
- [维度](/zh-cn/reference/workflow-steps/dimensions/)——加载、排序、清除、导出以及管理层次结构
- [优化](/zh-cn/reference/workflow-steps/optimization/)——线性和混合整数求解器步骤
- [机器学习](/zh-cn/reference/workflow-steps/machine-learning/)——训练模型（包括 XGBoost 和 KNIME 学习器），并用模型对表进行评分

### 文档和文件

- [文档](/zh-cn/reference/workflow-steps/document/)——文件操作、目录列表、加密、PDF 处理、图像处理、编码转换、Excel 单元格更新
- [文本和文档](/zh-cn/reference/workflow-steps/text-documents/)——PDF 文本提取、图像 OCR、Blob 读写、情感分析、主题建模、词云

### 通信

- [通知](/zh-cn/reference/workflow-steps/notifications/)——电子邮件、Slack、Teams、短信、Webhook、Twitter、日志
- [报表](/zh-cn/reference/workflow-steps/reports/)——根据 RML 模板渲染单个或批量 PDF 报表

### 工作流控制

- [工作流控制](/zh-cn/reference/workflow-steps/workflow-control/)——变量、循环、子工作流、宏、错误处理、行数断言
- [通用](/zh-cn/reference/workflow-steps/general/)——LLM 步骤、Pass、Wait、用户定义转换、运行远程 Python、Alteryx 执行器
- [打包宏](/zh-cn/reference/workflow-steps/macros/)——与 Alteryx 打包宏对应的步骤：Create Samples、DateTime Now、Heat Map 和 Pie Wedge Trade Area 步骤

### 企业集成

- [代理](/zh-cn/reference/workflow-steps/agent/)——用于本地资源的 PlaidLink 代理操作
- [NetSuite](/zh-cn/reference/workflow-steps/netsuite/)——导入余额、总账明细、主数据或您自己的 [SuiteQL 查询](/zh-cn/reference/workflow-steps/netsuite/import-suiteql-query/)；向 NetSuite 过账日记账分录
- [Acumatica](/zh-cn/reference/workflow-steps/acumatica/)——导入主数据和交易实体；过账日记账交易、发票、账单和付款
- [Business Central](/zh-cn/reference/workflow-steps/business-central/)——导入 OData 实体；过账总账日记账行
- [Xero](/zh-cn/reference/workflow-steps/xero/)——导入 Accounting API 实体；过账手工日记账、发票、账单、付款和贷项通知单
- [Dynamics 365 F&O](/zh-cn/reference/workflow-steps/dynamics-365-fo/)——导入 OData/DMF 实体；过账日记账分录
- [Oracle Fusion](/zh-cn/reference/workflow-steps/oracle-fusion/)——导入总账余额和日记账批次；通过 FBDI 过账日记账分录
- [Oracle EPM (HFM / FCCS)](/zh-cn/reference/workflow-steps/oracle-epm/)——通过视点选择器从 Oracle FCCS 自助获取临时数据切片；可选按计划定期加载
- [Oracle Essbase](/zh-cn/reference/workflow-steps/essbase/)——针对多维数据集运行实时 MDX 查询，或将维度大纲加载为 PlaidCloud 维度；云端直连
- [IBM TM1 / Planning Analytics](/zh-cn/reference/workflow-steps/ibm-planning-analytics/)——按已保存视图或 MDX 读取多维数据集，或读取维度层次结构；云端直连或通过本地代理
- [Anaplan](/zh-cn/reference/workflow-steps/anaplan/)——读取已保存视图、运行已有的导出操作，或将一个或多个列表加载到 PlaidCloud 维度；云端直连、只读
- [Workday Financials](/zh-cn/reference/workflow-steps/workday-financials/)——导入 RaaS 报表；过账会计日记账
- [Salesforce](/zh-cn/reference/workflow-steps/salesforce/)——通过 Bulk API 2.0 将任意标准或自定义 CRM 对象提取到项目表中，对象和字段列表读取自组织
- [Sage Intacct](/zh-cn/reference/workflow-steps/sage-intacct/)——导入余额、应付账单、临时查询以及总账/维度对象；过账日记账分录
- [SAP S/4HANA Cloud](/zh-cn/reference/workflow-steps/s4hana-cloud/)——通过 OData 导入试算平衡表和日记账分录行项目；通过 SOAP 过账日记账分录
- [SAP](/zh-cn/reference/workflow-steps/sap/)——SAP ECC / S/4HANA RFC 调用
- [SAP-PCM](/zh-cn/reference/workflow-steps/sap-pcm/)——SAP Profitability and Cost Management 模型控制
