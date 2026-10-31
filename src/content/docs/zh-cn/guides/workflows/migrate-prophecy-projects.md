---
title: 迁移 Prophecy 项目
description: 在 Analyze 应用、REST API 或连接 MCP 的 AI 代理中，将 Prophecy 项目导出文件转换为 PlaidCloud 工作流，绑定其数据集和连接，并阅读转换报告。
sidebar:
  order: 31.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-prophecy-projects.md
---

PlaidCloud 可直接替代 Prophecy。每个 Prophecy gem 都会转换为执行该 gem 工作的原生 PlaidCloud 工作流步骤：转换器为每个 Spark 管道和 SQL 项目各创建一个工作流，把每个 gem 映射为工作流步骤、项目变量或画布对象，保留原始图，并返回转换报告。已转换的工作流自身不会重现的少数行为列在[边界情况](#边界情况)中。

转换只读取您指定的导出文件。它不会连接 Prophecy 数据集读取或写入的系统，也不会运行项目代码。

转换是一次性操作。再次转换同一项目会创建新的工作流和表，您在 PlaidCloud 中所做的编辑不会与之后的导出合并。

## PlaidCloud 会创建什么

- 每个 Prophecy gem 都会变成对应的工作流步骤，并保留上下游关系。
- Prophecy 参数会变成项目变量，gem 设置中对参数的引用会被改写为 PlaidCloud 变量语法。转换时可以覆盖参数值。
- gem 读取的每个数据集会变成一个导入步骤，或读取现有的表或文档，具体取决于您如何绑定。
- 每个 Prophecy 作业或 SQL 管道计划都会成为已转换工作流上的[计划事件](/zh-cn/administration/scheduled-events/)，在 Prophecy 中启用时同样启用。请参阅[计划](#服务和控制)。
- 脚本、SQL 语句、宏和其他项目代码会放入承载这些代码的步骤中。请参阅[步骤中的项目代码](#步骤中的项目代码)。
- 自定义 gem（包括 Gem Builder gem）会在 Python 步骤中运行导出文件为其携带的代码。请参阅[步骤中的项目代码](#步骤中的项目代码)。
- 带 HAVING 条件或全部值列的 Pivot gem 可以转换，Prophecy 提供的排序和 Deduplicate 类型也同样可以转换。
- 表达式按 Spark SQL 对空值处理、整数除法和隐式类型转换的行为进行转换。在这些行为与您的 PlaidCloud 引擎不同之处，请检查结果。

## 开始之前

1. 将项目从 Prophecy 导出为 `.zip` 文件，或将单个管道、模型或子图导出为 `.json` 文件。
2. 将文件上传到您可以读取的[文档账户](/zh-cn/guides/documents/adding-accounts/)。
3. 选择接收工作流的 PlaidCloud 项目。您需要对其具有写入权限。
4. 确定未绑定数据集的文件从何处读取。选择一个文档账户和一个基础文件夹。

## 转换项目

可以从 Analyze 应用、REST API 或 MCP 工具目录进行转换。三种方式使用相同的字段。

### Analyze 应用

1. 打开 **Analyze**，然后选择 **Tools → 导入 Prophecy 项目**。
2. 选择**目标项目**、已上传到文档账户的 **Prophecy 项目 (.zip 或 .json)**，以及**源文件位置**，即未绑定数据集的文件读取所在的文档账户和基础文件夹。
3. 在**对象名称和选项**下，可以选择设置工作流、步骤和表的前缀，选择**工作流类型**，并选择是否将未转换的组件导入为直通占位符。
4. 在 **Source Bindings and Parameters** 下，可以通过输入数据集名称和表 ID 将数据集绑定到现有表，并按名称覆盖 Prophecy 参数。如需绑定连接，请使用 REST API 或 MCP 工具。请参阅[绑定连接](#绑定连接)。
5. 选择**导入**。

窗口会显示读取项目、解析管道、映射到 PlaidCloud 操作以及创建工作流、表和步骤的进度。完成后，窗口会显示转换报告：按置信度统计的步骤数、警告、部分转换、未转换的占位符、已丢弃的组件，以及需要上传的源文件。

### 字段

REST API 和 MCP 工具使用以下字段。

| 字段 | 是否必填 | 作用 |
| --- | --- | --- |
| `source_account_id` | 是 | 存放 Prophecy 导出文件的文档账户。 |
| `source_file_path` | 是 | 该账户内项目 `.zip` 文件，或单个管道、模型或子图 `.json` 文件的路径。 |
| `project_id` | 是 | 创建工作流的项目。 |
| `document_account_id` | 是 | 未绑定数据集读取所用的文档账户。 |
| `document_account_path` | 是 | 该账户中未绑定数据集所用的基础文件夹。空值或 `/` 表示账户根目录，开头的 `/` 会被忽略。包含 `..` 或以点开头的路径段、花括号、盘符或 URL 方案、控制字符的路径会被拒绝。 |
| `workflow_prefix` | 否 | 添加到工作流名称前的前缀。 |
| `step_prefix` | 否 | 添加到步骤名称前的前缀。 |
| `table_prefix` | 否 | 添加到表名称前的前缀。默认为工作流自身的名称。会重用现有表名的前缀在创建任何内容之前就会被拒绝。所用前缀会在转换报告中返回。 |
| `workflow_type` | 否 | `advanced`（默认）将图布置到 DAG 画布上。`standard` 生成串行步骤列表。 |
| `source_bindings` | 否 | 将数据集和操作绑定到现有数据。请参阅[绑定源](#绑定源)。 |
| `connection_bindings` | 否 | 将项目访问的数据库、文件存储、REST API 和电子邮件绑定到 PlaidCloud 连接和文档账户。请参阅[绑定连接](#绑定连接)。 |
| `parameters` | 否 | 覆盖 Prophecy 参数。请参阅[参数](#参数)。 |
| `allow_unconverted_placeholders` | 否 | 控制占位符在运行时的行为。请参阅[未转换 gem 的占位符](#未转换-gem-的占位符)。 |

### REST

将这些字段作为 JSON 请求体发送到：

```text
POST /rest/v1/analyze/prophecy/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/prophecy/customer-360.zip",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/prophecy-inputs"
}
```

您需要 `analyze.workflow.write` 角色。

### MCP

连接 MCP 的 AI 代理使用相同的字段调用 `prophecy_convert` 工具。要连接代理，请参阅 [AI 代理 (MCP)](/zh-cn/integrations/ai-coding-agents/)。该工具会更改您的项目，因此请在批准调用之前先进行检查。

## 绑定源

Prophecy 导出文件描述了数据的来源，但不携带数据和凭据。使用 `source_bindings` 将每个数据集连接到您在 PlaidCloud 中已有的数据。键是转换报告中列出的数据集名称。值可以是以下之一：

- 目标项目中某个表的 `analyzetable_` ID。转换后的工作流会直接读取该表。
- 包含 `account`、`path` 以及可选 `sheet` 的对象，用于从文档账户读取文件。

```json
"source_bindings": {
  "customers": "analyzetable_1234",
  "budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

无法读取的绑定会被拒绝。与任何数据集都不匹配的键会作为警告报告。Analyze 窗口将数据集绑定到表；如需将数据集绑定到文档文件，请使用 REST API 或 MCP 工具。

### 未绑定的数据集

没有绑定的数据集会变成暂无数据的导入步骤，转换报告会为其附上警告。该步骤从以下位置读取：

```text
<document_account_path>/prophecy/<workflow id>/<dataset name>.csv
```

将文件上传到该路径并运行工作流。在文件就位之前，导入步骤会带着警告完成并创建一个空表，工作流继续执行。报告会在**需要上传的源文件**下列出每个路径。

### 绑定表和文件操作

更改表或文件的 gem，例如 Table Operations（更新、删除、丢弃）和 File Operation（复制），只作用于转换所创建的数据。要让其作用于已有数据，请使用形如 `operation:<pipeline>/<id>` 的键进行绑定，其中 `<pipeline>` 是管道名称，`<id>` 是 gem 的 ID。转换报告会给出每个此类 gem 的键。

```json
"source_bindings": {
  "operation:daily_load/Operation_1": "analyzetable_5678"
}
```

具有破坏性的表或文件操作只有在您绑定后才会运行。未绑定时，Table Operations gem 作用于同一项目中另一个 gem 写入的表，否则会变成一个写明其键的占位符。File Operation 从自己的暂存文件夹复制。除非您绑定，否则不会更改转换自身的表和文件夹之外的任何内容。

## 绑定连接

Prophecy 项目通过连接访问数据库、文件存储、REST API 和邮件服务器。导出文件携带连接名称但不含凭据，因此请使用 `connection_bindings` 将每个连接指向您已有的 PlaidCloud 连接或文档账户。转换报告会在其绑定下列出每个键。

```json
"connection_bindings": {
  "connection:warehouse_pg": "<connection id>",
  "connection:landing_s3": "<document account id>",
  "operation:daily_load/Email_1": "<connection id>"
}
```

键是以下之一：

| 键 | 绑定对象 | 值 |
| --- | --- | --- |
| `connection:<name>` | gem 或数据库数据集所指定的 Prophecy 连接。一个绑定适用于该连接上的每个 gem。未指定连接的 gem 使用 `connection:<pipeline>/<gem id>`，数据库数据集使用 `connection:<dataset name>`。 | PlaidCloud 连接 ID：数据库连接（包括 BigQuery 和 SAP HANA）、MongoDB 或 Apache Kafka 连接、用于 Salesforce 读写的 Salesforce 连接、用于 Tableau gem 的 Tableau 连接、用于 Azure Cosmos DB、Pinecone、Power BI 以及 Smartsheet 和 Slack 写入的 REST 连接，或用于 Smartsheet、Slack 和 Iceberg 读取的基于 Singer 的连接。File Storage 或 Directory gem 使用文档账户 ID。 |
| `operation:<pipeline>/<gem id>` | 发送 GET、HEAD 或 OPTIONS 以外请求的 REST gem，以及每个 Email gem。 | 连接 ID。对于 REST，是保存凭据的 REST 连接。 |

对于会更改转换范围之外内容的 gem，该绑定即表示您的同意：

- 可能更改 API 所保存内容的 REST 请求，以及会发送给真实收件人的电子邮件，只有在您绑定其 `operation:` 键后才会转换为可用的步骤。未绑定时，该 gem 是一个写明该键的占位符。
- 绑定到 File Storage 或 Directory gem 的文档账户，允许该 gem 的步骤在该账户中写入、删除或移动文件。
- GET、HEAD 或 OPTIONS 请求按 gem 发送的方式发出。未绑定时，在您于已转换步骤上选择 REST 连接之前，它没有凭据。

没有绑定的数据库数据集或 External Table gem 会转换为一个写明其键并等待您选择连接的步骤，报告会附上警告。请在绑定该键后重新转换，或在步骤上选择连接。如果绑定的 ID 对其 gem 而言是错误类型的存储，或您无权使用，则该绑定会被拒绝。与任何内容都不匹配的键会作为警告报告。

## 参数

`parameters` 在转换时覆盖 Prophecy 参数：

```json
"parameters": {
  "instance": "prod",
  "values": { "run_date": "2026-10-01", "region": "EMEA" },
  "pipelines": {
    "daily_load": { "instance": "prod", "values": { "region": "APAC" } }
  }
}
```

`instance` 指定配置实例。`values` 是文本、数字或布尔值。管道条目会覆盖该管道的项目级值。报告会列出所用的参数，以及为符合 PlaidCloud 变量名而被重命名的参数。

## 阅读转换报告

响应中包含转换报告。请在运行工作流之前阅读。

| 部分 | 说明的内容 |
| --- | --- |
| 摘要 | 以高、中、低置信度转换的步骤数，以及未转换的步骤数。 |
| 警告 | 转换器所做的全部假设、近似和跳过，包括未绑定的数据集和未匹配任何内容的绑定键。 |
| 部分转换 | 已转换但在某种模式或选项上与 gem 不同的步骤。每项都附有需要检查内容的说明。 |
| 未转换的占位符 | 没有 PlaidCloud 对应项的 gem，并附有原因。 |
| 已丢弃的组件 | 自身不承担任何工作的 gem（例如控制流边界标记），以及吸收它们的步骤。 |
| 需要上传的源文件 | 每个未绑定数据集读取所用的文档路径。 |
| 工作流 | 为每个管道创建的工作流，按运行顺序排列。转换器拒绝的管道会被标出。 |

报告还会写明所用的表前缀和已应用的参数。转换器没有把握的步骤会按最可能的理解进行转换，并在报告中附上说明。请对照您的 Prophecy 输出检查这些步骤。

## 步骤中的项目代码

Prophecy 项目携带代码：Script gem、SQL 语句、宏、动态输入、存储过程调用和自定义 gem。转换器不会运行这些代码，而是把它们放入步骤中：

- SQL 会被翻译为租户的 SQL 方言并放入 SQL 步骤，gem 的输入可以使用查询读取它们时的名称。
- Python 脚本放入 Python 步骤，并改写表访问方式。调用 Spark 数据框方法的脚本会保留这些调用，并在步骤中运行。
- 自定义 gem（包括 Gem Builder gem）会在 Python 步骤中运行其管道导出文件为其携带的 PySpark 代码。
- 来自已知 dbt 包的宏会变成执行该宏所做工作的标准步骤。您自己项目中的宏，或导出文件所含包中的宏，同样会被读取并转换，包括 if 和 for 块、set、过滤器、嵌套宏和适配器分派。
- Aggregate gem 中的 Python 用户定义聚合函数会针对每个分组在 Python 步骤中运行。

每个携带项目代码的步骤都会获得警告，翻译后的 SQL 也一样。运行工作流之前，请检查每个此类步骤中的代码。转换器会隐去在代码字符串和注释中发现的任何类似凭据的内容，因此请将凭据添加到连接中，而不要放在代码里。

## 未转换 gem 的占位符

转换器无法重现的 gem 会创建为携带该 gem 名称的占位符步骤。例如代码不在导出文件中的自定义 gem，以及会在转换范围之外更改数据的 gem，如可能更改数据的 REST 请求、Email，或在您尚未绑定其 `operation:` 键时的表或文件操作。没有绑定连接的数据库数据集或 External Table 不属于占位符：它会转换为等待您选择连接的步骤。默认情况下，占位符在工作流运行到它时会失败，因此运行不会对未实际发生的工作报告成功。

将 `allow_unconverted_placeholders` 设置为 `true`（在窗口中为**将未转换的组件导入为直通占位符**），即可把每个占位符导入为直通步骤。此后运行会越过它继续执行，占位符的输出就是其输入。报告会统计直通占位符的数量并列出其步骤。当其结果很重要时，请使用原生步骤重建该功能。

## 运行已转换的工作流

1. 在项目中打开新工作流。报告按运行顺序列出它们。
2. 设置来自 Prophecy 参数的所有项目变量。
3. 将未绑定数据集的文件上传到报告中的路径。
4. 检查携带项目代码的步骤。
5. 运行工作流，并检查每个步骤的输出表。

由 Prophecy 计划创建的计划事件，在 Prophecy 中启用时同样启用，因此它们会按计划开始运行已转换的工作流。如需先检查工作流，请在[计划事件](/zh-cn/administration/scheduled-events/)中禁用这些事件，准备就绪后再启用。

## 转换内容

每个 Prophecy gem 都会连同其提供的选项一起完整转换为原生步骤、项目变量、计划事件或画布对象。[Prophecy 转换矩阵](/zh-cn/reference/prophecy-conversion-matrix/)列出了每个 gem 及其对应的 PlaidCloud 步骤，[边界情况](#边界情况)列出了少数需要检查的行为；转换报告会在出现之处标明每一项。

### 数据移动

| 功能 | 转换方式 |
| --- | --- |
| 写入模式 | 目标写入模式转换为平台步骤：采用检查和时间戳策略的 SCD2（时间戳策略根据 gem 的 `scd2.updatedAtColumn` 所指定的列为每个版本标注日期）、merge、`replaceWhere` 和 `insertInto`。merge 会应用其匹配更新和未匹配插入子句中的逐列 SET 表达式；不设置任何列的子句会从传入行中获取所有列。首次运行写入空目标时会写入每一行，与 dbt 和 Delta 一致。首次运行无需提前建表，包括读取同时也写入的数据集的管道，除非导出文件没有说明该数据集有哪些列：此时请在首次运行前创建表。之后的运行会应用增量筛选器或合并条件。`error` 和 `ignore` 模式通过[表存在条件](/zh-cn/guides/workflows/step-conditions/#表存在条件)进行检查。 |
| 时间旅行 | 通过 `versionAsOf` 或 `timestampAsOf` 读取表较早版本的 Delta 或目录表源，会通过您绑定的连接从 Databricks 读取该版本。 |
| 流式传输 | 流式源和目标按计划批处理运行。流式接收端会替换其表而不是追加，因此重新运行不会产生重复行。请为工作流设置计划以获取新到达的数据。 |
| 数据库 | JDBC、Snowflake、Redshift、Hive、BigQuery、SAP HANA 和 External Table gem 通过您绑定的 PlaidCloud 连接进行读写。BigQuery 数据集使用 [导入 SQL](/zh-cn/reference/workflow-steps/import/import-sql/) 读取，并在 [BigQuery 连接](/zh-cn/reference/connectors/google/big-query/)上使用 [Export External Database Tables](/zh-cn/reference/workflow-steps/export/export-external-tables/) 写入。以 HANA gem 的任一 merge 模式（包括 SCD2 和删除模式）写入的 SAP HANA 表，会在目标旁暂存，并按目标的主键或 gem 的 merge 列合并到目标中；缺失的目标会先创建。 |
| MongoDB 和 Kafka | MongoDB 数据集使用 [导入 MongoDB](/zh-cn/reference/workflow-steps/import/import-mongodb/) 读取，包括其筛选器或聚合管道；未声明列的读取会像 Spark 连接器一样从前几个文档中获取列。写入使用匹配写入模式下的 [导出 MongoDB](/zh-cn/reference/workflow-steps/export/export-mongodb/)：`update` 更新匹配文档的字段或插入一个文档，`ignore` 仅在集合中没有文档时写入，`error` 在集合中已有文档时停止运行。Kafka 源使用 [导入 Kafka](/zh-cn/reference/workflow-steps/import/import-kafka/) 读取起始偏移量与结束偏移量之间的主题，Kafka 目标使用 [导出 Kafka](/zh-cn/reference/workflow-steps/export/export-kafka/) 发送每一行。使用 `OAUTHBEARER` 登录的 Kafka 数据集会使用您所绑定 Kafka 连接的 [OAuth 登录](/zh-cn/reference/connectors/databases/apache-kafka/#oauthoauthbearer)，因为导出文件不携带凭据。 |
| Azure Cosmos DB | 读取时，在使用 Cosmos DB 身份验证的 REST 连接上通过 [REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/)发送数据集的查询，或读取每个文档，并逐页跟随延续标头。写入时按 gem 的写入策略（overwrite、append、delete 或 patch）为每一行发送一个请求。携带其文档 ETag 的行，仅当文档自那时起未发生更改时才会被替换或删除；容器因此原因、或因文档缺失或已存在而拒绝的行会被跳过，与 Spark 连接器一致。`ignore` 模式仅在容器中没有文档时写入。 |
| Salesforce | 读取使用 [Salesforce：查询对象](/zh-cn/reference/workflow-steps/salesforce/query-salesforce-object/)，在 gem 要求时包含已删除和已归档的记录。写入可插入、更新、upsert 或删除，每一行一个请求；upsert 按 gem 的外部 ID 字段匹配，未指定时使用 `Id`。 |
| Smartsheet、Slack 和 Pinecone | 读取已声明列的指定 Smartsheet 工作表时，会通过您的 REST 连接获取该工作表，并为每个工作表行生成一行，为每个已声明列生成一列。其他 Smartsheet 读取，以及 Slack 和 Iceberg 读取，使用[导入 Singer 源](/zh-cn/reference/workflow-steps/import/import-singer/)。Smartsheet 写入会把行添加到指定工作表，overwrite 会先删除该工作表的行。Slack 写入为每一行发布一条消息，Slack 拒绝的消息会使步骤失败。Pinecone 索引读取为其向量及元数据，写入则将各行作为向量 upsert。 |
| Tableau 和 Power BI | Tableau 和 Tableau Write 通过 [Publish to Tableau](/zh-cn/reference/workflow-steps/export/export-to-tableau/)，在您绑定的 Tableau 连接上将输入发布为 Hyper 提取。Power BI Write 通过使用 OAuth 2.0 的 REST 连接将输入推送到 Power BI 推送数据集，按名称查找工作区，并在数据集是新建时创建它。 |
| 文件格式 | CSV、JSON、Parquet、Avro、Excel、XML、固定宽度，以及通过 [导入 ORC](/zh-cn/reference/workflow-steps/import/import-orc/) 的 ORC。格式选项会被映射，或在不改变任何行时标记为中性：Avro 读取的修改时间窗口、固定宽度文件的 EBCDIC 编码、页眉和页脚记录以及无换行记录、Excel 读取的工作表映射和密码、CSV 写入的引号选项，以及每个值一个工作表的 Excel 写入。压缩文本文件可使用 gzip、Deflate (zlib)、Zstandard、LZ4、Snappy 和 LZO 读写；文件名以其编解码器扩展名结尾时才会按压缩文件读取。加密文件就地解密和加密。请参阅[加密文件](#加密文件)。 |
| File Operation | Copy 和 Move 转换为在您绑定的文件夹上执行的 [文档：复制文件](/zh-cn/reference/workflow-steps/document/copy-document-file/) 或 Copy Directory，仅保留名称与 gem 的 `filenameRegex` 匹配的文件，并在 gem 递归时保留每个文件在源文件夹下的路径。 |
| Directory | 使用 [目录列表](/zh-cn/reference/workflow-steps/document/directory-listing/) 按 gem 的列列出所绑定文档文件夹中的文件。启用工作表名称选项时，每个 Excel 工作簿的每个工作表生成一行及其 `sheet_name`；其他文件生成一行，`sheet_name` 为空。 |

### 列和行

| gem 或函数 | 转换方式 |
| --- | --- |
| Surrogate Key | 键从保存最后发出的键的表继续，与 gem 的键文件一致。指定同一键文件的每个 gem 共享该表，因此它们的键绝不会重叠。没有行的运行会保持该表不变，在任何运行发出键之前，键从初始值开始。 |
| Column Parser、XML Parse、JSON 解析 | XML 和 JSON 文本使用 [XML 解析](/zh-cn/reference/workflow-steps/tables/table-xml-parse/)和 [JSON 解析](/zh-cn/reference/workflow-steps/tables/table-json-parse/)步骤进行解析，从元素的文本、属性或子元素中读取每个字段。在没有模式的情况下解析 XML 时，每个字段的类型取自数据，与 Spark 的 `schema_of_xml` 一致。 |
| 业务规则 | 在表达式中调用的项目业务规则会转换为相同的条件，每个被设置的列对应一个 `CASE`。 |
| 类型转换 | 文本转十进制数或长整型严格遵循 Spark：数字前后的空格和控制字符会被去除，十进制数按其小数位数四舍五入，不是数字的文本或超出范围的值为 null。 |
| 日期和时间 | 日期和时间格式针对您工作区的引擎编写（包括 Databend），`window()` 会将每个时间戳放入其滚动窗口，对齐方式与 Spark 相同。 |
| 迭代器输出 | 输出列仅在运行时才能确定的 Table Iterator 或 While Iterator，会使用[表：全部合并](/zh-cn/reference/workflow-steps/tables/table-union-all/#列匹配)按位置收集每次迭代的行，每一列都会扩宽到所有迭代都适用的类型，与 Prophecy 堆叠各次迭代的方式一致。 |
| Data Encoder/Decoder AES | 可在每个引擎上运行。密钥，以及 gem 指定时的初始化向量和附加数据，来自您设置的工作流变量 `aes_key`、`aes_iv` 和 `aes_aad`。 |
| Data Masking 哈希 | 计算出与 Spark 的 `hash()` 相同的值。 |
| Buffer、Simplify、Heat Map | Buffer 绘制圆角时使用与 Prophecy 相同数量的线段，Simplify 丢弃相同的顶点，Heat Map 按 gem 的分辨率将热度汇总到 H3 六边形中，十进制热度仍为十进制。 |

### 服务和控制

| gem | 转换方式 |
| --- | --- |
| Pipeline | 使用[工作流循环](/zh-cn/reference/workflow-steps/workflow-control/workflow-loop/)为每个输入行运行其指定的管道一次（没有输入时运行一次，没有行时从不运行），每个参数由常量、该行的某一列或基于它的表达式设置。即使前一次运行失败，每次运行仍会继续，gem 的输出为每次运行一行，包含其状态、消息和时间，与 Prophecy 记录的一致。 |
| 计划 | Prophecy 作业或 SQL 管道计划会成为已转换工作流上名为 `Prophecy <name>` 的[计划事件](/zh-cn/administration/scheduled-events/)，除非在 Prophecy 中被禁用，否则处于启用状态。运行一个已转换管道且没有配置覆盖或运行条件的 Spark 作业会以这种方式转换。 |
| Script | Python 脚本放入 Python 步骤。脚本在 `Config` 上设置的值会成为后续步骤读取的工作流变量，并在每次运行开始时重置为管道的值，与 Prophecy 的 `Config` 一致。 |
| REST API、REST API Enrich | [REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/)步骤，每个输入行一个请求，并像 Prophecy 一样保留错误响应。Enrich 还会读取状态、原因和最终 URL。等待异步结果的请求会持续轮询，直到响应表明已完成。 |
| Stored Procedure | 传递参数的 gem 会使用[远程执行：SQL](/zh-cn/reference/workflow-steps/agent/agent-remote-execution-of-sql/#对每行运行一次语句)为每个输入行调用其存储过程一次，每个参数从其列绑定为一个参数。不带参数的 gem 通过代理调用一次。请在已转换的步骤上选择连接或代理。 |
| Email、Email Data | [Notify Via Email](/zh-cn/reference/workflow-steps/notifications/notify-via-email/)，支持抄送、密送、回复地址，且字段读取自某一列时每行一封邮件。 |
| OpenAI、Bedrock、SageMaker Endpoint | 在您工作区的 LLM 连接上使用 [Text: NLP (AI)](/zh-cn/reference/workflow-steps/text-documents/nlp-ai/)。OpenAI 和 Bedrock 嵌入使用 Embed 任务，需要兼容 OpenAI 的连接或 Azure OpenAI 连接；Anthropic 连接会被拒绝。 |
| Pinecone Lookup | 每行一个 REST 请求。 |
| Data Quality Check、Deequ、Soda | 检查在仓库中运行并写入结果表。Data Quality Check 仅在 gem 设置了 `minFailedChecks` 或 `fail_pipeline` 后续操作时才会停止运行；否则结果表会列出失败项。Deequ 和 Soda 从不停止运行。对数值列的最小或最大长度检查，会将该数字作为文本来度量。Soda 检查从项目的 YAML 转换，包括缺失值、无效值和有效值、统计信息、长度、百分位数、跨列重复、新鲜度、失败行以及您自己的指标查询。 |
| ToDo | 运行到它时引发错误，错误中写明原工具和消息。 |

### 加密文件

读取加密文件的 File Storage gem 会转换为[文档：解密文件](/zh-cn/reference/workflow-steps/document/encrypt-decrypt-file/)，它会在导入读取之前把文件解密到其自有文件夹中；解密后的副本随后会被删除。写入加密文件的 gem 会导出到该文件夹，然后使用文档：加密文件将文件加密到位。涵盖 AES 和 Blowfish 文件以及受密码保护的 Excel 工作簿。

导出文件从不携带密钥，因此已转换的步骤从工作流变量中读取：AES 或 Blowfish 密钥使用 `aes_key`，工作簿密码使用 `xlsx_password`。请在运行工作流之前设置该变量，并为这些文件使用专用密钥。密钥和密码字段只接受变量引用，因此密钥绝不会被键入步骤中。

## 边界情况

以下是已转换的工作流自身不会重现的行为。转换报告会在出现之处标明每一项。

- **导出文件未包含的代码或数据**：代码不在导出文件中的 Gem Builder 或其他自定义 gem，以及对导出文件所缺 dbt 包中宏的调用，会变成写明所缺内容的步骤；请连同管道代码和 dbt 包一起导出项目，或在 Python 或 SQL 步骤中重建逻辑。Ab Initio Error Detection 和 MTime gem 会直接传递其输入，因为它们所应用的规则不在导出文件中。从项目之外的文件读取的 Soda 检查，以及与更早扫描或其他数据集比较、或测试 Soda 指定格式的 Soda 检查，在结果表中没有对应行；请在后续步骤中计算。
- **仅在管道运行时才能得知的结果**：在没有任何内容声明字段名时，展平其响应的 REST API gem 会把整个响应放入一列，这只有运行后才能看出；请在后续步骤中提取所需字段。在 dbt 编译时查询仓库的 dbt 宏会变成写明它的步骤；请将查询替换为其返回的值。Spark StoredProcedure gem 可以运行，但不会返回其 OUT 值；输出是直通的列。`input_file_name()` 在表或 Delta 源上返回空字符串，因为这些源没有可命名的文件；在聚合、窗口或有多个输入的 gem 内的 `hash()` / `xxhash64()` 由仓库计算，因此可能与 Spark 的结果不同。
- **项目转换时写入步骤的值**：包含引号、反斜杠或花括号的参数值、SQL 步骤读取的管道值，以及 Delta 表操作通过配置指定的数据库，会作为固定值写入步骤，因此更改工作流变量不会改变它们；配置变化时请编辑步骤。
- **Scala 代码**：Scala 脚本、Scala 表达式，或 Scala 用户定义函数或聚合函数会变成写明它的步骤；请用 SQL 或 Python 重写。
- **Kafka Kerberos 登录**：使用 Kerberos (GSSAPI) 登录的 Kafka 源或目标，转换时不含 Kerberos 服务名称和登录机制；请在 PlaidCloud 连接上设置它们。
- **流式传输**：流式源、目标和管道作为批处理工作流，在运行时针对现有数据运行；请按所需频率为工作流设置计划。
- **作业组件**：Spark 作业只转换其一个管道和计划；其他组件、运行条件和配置覆盖不会转换。
- **不常见的调用**：从 rollup 或窗口中调用的用户定义聚合函数，以及使用 if、for、set 和常见过滤器之外 Jinja 功能的 dbt 宏，会变成写明该 gem 的步骤；请从 Aggregate gem 调用该函数，或将宏内联。

## 相关指南

- [迁移 Savant 分析](/zh-cn/guides/workflows/migrate-savant-analyses/)
- [迁移 Alteryx 工作流](/zh-cn/guides/workflows/migrate-alteryx-workflows/)
- [添加文档账户](/zh-cn/guides/documents/adding-accounts/)
- [管理工作流变量](/zh-cn/guides/workflows/manage-workflow-variables/)
- [运行工作流](/zh-cn/guides/workflows/run-a-workflow/)
