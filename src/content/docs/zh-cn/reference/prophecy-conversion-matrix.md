---
title: Prophecy 转换矩阵
description: PlaidCloud 如何将 Prophecy 管道和 SQL 项目转换为原生高级工作流步骤，包含每个 gem 的支持状态。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/prophecy-conversion-matrix.md
---

PlaidCloud 可将 Prophecy Spark 管道和 SQL 项目转换为原生高级工作流。导入器会把每个 Prophecy gem 映射为一个工作流步骤、项目变量或画布对象，因此转换后的工作流以云原生方式运行，而不是通过仿真运行。

每个 gem、连接器和项目结构都可以转换：**完整**表示该 gem 成为原生 PlaidCloud 步骤、变量或画布对象，并完成该 gem 的工作。转换后的工作流自身不会复现的少数行为列在[已知边缘情况](#已知边缘情况)中，并附有应对方法。

要运行转换，请参阅[迁移 Prophecy 项目](/zh-cn/guides/workflows/migrate-prophecy-projects/)。

## Spark 管道 gem

### Source/Target

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Lookup | 完整 | [查找](/zh-cn/reference/workflow-steps/tables/table-lookup/) | 每次 lookup 调用都会在使用它的步骤中成为一个查找步骤；没有匹配的键读取为 NULL，重复的键返回其中一行。 |
| Source | 完整 | 按数据集格式选择的导入步骤（请参阅[连接器](#连接器)） | 每个 Source 都会成为导入到以数据集命名的表中的导入步骤；转换器无法识别的格式会被读取为上传到工作流文档文件夹的 CSV 文件，并给出警告。 |
| Streaming Source | 完整 | 与批处理 Source 相同的导入 | 流式源会转换为一次性批量导入，并给出警告。 |
| Streaming Target | 完整 | 批量追加加载 | 流式目标会转换为批量追加，并给出警告。 |
| Target | 完整 | 按数据集格式和 writeMode 选择的表导出/加载步骤 | 每个 Target 都会按该 gem 的写入模式成为表加载或导出步骤：append、overwrite、带 SET 表达式的 merge、upsert、SCD2、replaceWhere 和 insertInto。 |

### Prepare

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Data Cleansing | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤中的列表达式 | 将空值填充、去除首尾空格和大小写选项转换为列表达式；清理后的列移到最后。 |
| Sequence | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带行号表达式 | 根据起始值和增量添加序列列。 |
| Surrogate Key Generator | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带行号表达式 | 从初始值开始添加顺序键；键会跨运行延续，依据是保存最后一个已发放键的表。 |

### Transform

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Aggregate | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带聚合；当该 gem 进行透视时使用[Pivot](/zh-cn/reference/workflow-steps/tables/table-pivot/) | 分组并聚合，应用 HAVING 条件，并为每个透视值透视出一列；propagate-all 会携带所有其他输入列。 |
| Bulk Column Expressions | 完整 | 在 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤中展开为每列一个表达式 | 在 Table Extract 步骤中为每个列出的列生成一个表达式；转换会警告该 gem 的布局是推断得出的。 |
| Bulk Column Rename | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤中的列重命名 | 在 Table Extract 步骤中为每个列出的列生成一个重命名；转换会警告该 gem 的布局是推断得出的。 |
| Deduplicate | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带 distinct 或行号筛选器 | 每个键保留一行：distinct、按您的排序顺序取第一行或最后一行、任意一行，或仅保留只出现一次的键。 |
| Dynamic Replace | 完整 | 动态替换转换，需手动配置 | 转换为动态替换转换上的替换规则；转换会警告该 gem 的布局是推断得出的。 |
| Dynamic Select | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤中按类型解析的列选择 | 在转换时按类型解析列，生成明确的选择。 |
| Filter | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带筛选表达式 | 转换为带筛选表达式的 Table Extract 步骤；条件为 NULL 的行会被丢弃。 |
| Flatten Schema | 完整 | [JSON 解析](/zh-cn/reference/workflow-steps/tables/table-json-parse/)和 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤 | 将嵌套字段展平为以该 gem 的分隔符命名的列，并将数组展开为每个元素一行。 |
| Fuzzy Match | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤和 [User Defined Transform](/zh-cn/reference/workflow-steps/general/user-defined-transform/) 步骤 | 对记录配对，按该 gem 的方法为每个匹配字段评分，对分数求平均，并保留达到或超过您所设阈值的配对。 |
| Group By Rollup | 完整 | 每个汇总层级一个 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 聚合步骤，再做合并 | 将汇总展开为每个分组层级一个聚合，并合并在一起，小计为 NULL。 |
| Limit | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带行数限制 | 转换为行数限制；配置引用会成为项目变量。 |
| Normalize | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带展开表达式 | 按长度表达式重复每条记录，按索引计算输出列，并在完成条件首次成立的索引处停止。 |
| Order By | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤上的排序 | 转换为具有相同键、方向和空值位置的排序。 |
| Reformat | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带列表达式 | 转换为每个输出列一个表达式的 Table Extract 步骤；未列出的列会被丢弃。 |
| Sample Rows | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带行数限制或随机抽样 | 保留随机比例或数量的行；由于抽样是随机的，所选行与 Spark 运行的结果不同。 |
| Schema Transform | 完整 | 按顺序应用的 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤链 | 按顺序应用每个操作：添加或替换列、删除、重命名、缺失时按默认值添加，以及添加项目业务规则。 |
| Set Operation | 完整 | [全部合并](/zh-cn/reference/workflow-steps/tables/table-union-all/)；except 使用[反联接](/zh-cn/reference/workflow-steps/tables/table-anti-join/)；intersect 使用[内联接](/zh-cn/reference/workflow-steps/tables/table-inner-join/) | Union all 堆叠各输入；except all 和 intersect all 会保留正确数量的重复行。 |
| TransposeAgg | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带聚合 | 将该 gem 的分组、聚合和透视转换为 Aggregate，并给出需要检查的警告。 |
| Unpivot | 完整 | [Melt](/zh-cn/reference/workflow-steps/tables/table-melt/) | 将所选列堆叠为名称列和值列。 |
| Watermark | 完整 | 无需步骤 | 已丢弃：批量运行会读取现有的所有数据，因此不存在需要应用的迟到数据截止点。 |
| Window Function | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤中的窗口表达式 | 按该 gem 的分区、排序和框架（行或范围）添加窗口列，边界可为无界、当前行或偏移。 |

### Join/Split

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Compare Columns | 完整 | 全外联接加每列聚合 | 通过对逆透视数据做全外联接来比较各列，并给出匹配与不匹配的计数。 |
| Join | 完整 | [内联接](/zh-cn/reference/workflow-steps/tables/table-inner-join/)、[多表联接](/zh-cn/reference/workflow-steps/tables/table-multi-table-join/)、[反联接](/zh-cn/reference/workflow-steps/tables/table-anti-join/)或[交叉联接](/zh-cn/reference/workflow-steps/tables/table-cross-join/) | 针对任意联接条件构建每种类型的联接（inner、left、right、full、semi、anti、cross 和 natural），应用 where 子句，并写出 select 列表。 |
| Repartition | 完整 | 无需步骤 | 已丢弃：PlaidCloud 管理分区，因此下一步会直接读取上游表。 |
| Row Distributor | 完整 | 每个输出一个 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 筛选器 | 转换为每个输出一个筛选器；行可以进入多个输出。 |

### Parse

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Column Parser | 完整 | [JSON 解析](/zh-cn/reference/workflow-steps/tables/table-json-parse/) / [XML 解析](/zh-cn/reference/workflow-steps/tables/table-xml-parse/) | 转换为对指定列的 JSON 或 XML 解析；转换会警告该 gem 的布局是推断得出的。 |

### Custom

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Custom Gem (Gem Builder) | 完整 | 运行该 gem 所生成代码的 [User Defined Transform](/zh-cn/reference/workflow-steps/general/user-defined-transform/) 步骤 | 管道导出中该 gem 生成的 PySpark 代码会在 Python 步骤中运行，并给出需要检查的警告。 |
| CustomReformatBitbucket | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤 | 按该 gem 所携带表达式的 Reformat 进行转换，并给出需要检查的警告。 |
| Data Quality Check | 完整 | 每项检查一个结果行的[全部合并](/zh-cn/reference/workflow-steps/tables/table-union-all/)；失败时使用[引发工作流错误](/zh-cn/reference/workflow-steps/workflow-control/raise-workflow-error/)停止 | 对输入评估每项检查，并为每项检查写出一个带状态和消息的结果行。数据会原样传递，并在达到该 gem 的失败阈值时停止运行。 |
| Deequ | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤检查 | 传递数据，并为 isComplete、isUnique、isNonNegative 和 isContainedIn 规则构建约束结果表。 |
| Delta Table Operations | 完整 | [Table In-Place Delete](/zh-cn/reference/workflow-steps/tables/table-in-place-delete/)、[Table Update](/zh-cn/reference/workflow-steps/tables/table-update/)、[Table Drop](/zh-cn/reference/workflow-steps/tables/table-drop/)、[Table Restore to Timestamp](/zh-cn/reference/workflow-steps/tables/table-restore-timestamp/) 步骤 | 删除、更新、丢弃和还原到时间戳会映射为表步骤；optimize、vacuum 和按版本还原会传递数据并给出警告。 |
| Directory | 完整 | [目录列表](/zh-cn/reference/workflow-steps/document/directory-listing/) | 以该 gem 的列列出所绑定文档文件夹中的文件；使用工作表名称选项时，每个工作簿的每个工作表生成一行。文件夹缺失时生成零行。 |
| Email | 完整 | [Notify Via Email](/zh-cn/reference/workflow-steps/notifications/notify-via-email/) 步骤 | 通过所绑定的电子邮件连接发送电子邮件，可选附带数据附件。 |
| Email Data | 完整 | [Notify Via Email](/zh-cn/reference/workflow-steps/notifications/notify-via-email/) 步骤 | 将输入行以表的形式通过电子邮件发送，并原样传递输入。 |
| File Operation | 完整 | [Copy Document File](/zh-cn/reference/workflow-steps/document/copy-document-file/) 步骤或 [Copy Document Directory](/zh-cn/reference/workflow-steps/document/copy-document-directory/) 步骤 | 将所绑定文档文件夹中的文件复制、移动或同步到已转换工作流的文档文件夹；移动会删除源文件。 |
| Log | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤 | 将该 gem 的事件行（时间、gem 名称、事件类型和文本）写入其输出表。 |
| REST API Enrich | 完整 | [REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/) | 对每行调用一次 API 并添加响应列。 |
| Script | 完整 | 带数据框访问重写的 Python 步骤 | 将脚本主体嵌入 Python 步骤，并重写数据框访问；Scala 主体会连同说明一并保留。 |
| Soda Data Quality Check | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤检查 | 根据 Soda 检查构建检查结果表。 |
| SQL Statement | 完整 | 每个输出选项卡一个 SQL 步骤，文本翻译为租户方言 | 将每个选项卡嵌入为一个 SQL 步骤，输入绑定为临时表；翻译为租户方言。 |
| Todo | 完整 | [引发工作流错误](/zh-cn/reference/workflow-steps/workflow-control/raise-workflow-error/)或 [Notify via Log](/zh-cn/reference/workflow-steps/notifications/notify-via-log/) 步骤 | 标记尚待编写的逻辑：没有任何内容读取它时为一条日志消息，后续步骤依赖它时则为一个以该 gem 的消息停止运行的步骤。 |

### Report

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Tableau | 完整 | [Publish to Tableau](/zh-cn/reference/workflow-steps/export/export-to-tableau/) 步骤 | 写出 Hyper 提取并发布到所绑定的 Tableau 连接。 |

### ML/AI

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Bedrock | 完整 | [Text NLP AI](/zh-cn/reference/workflow-steps/text-documents/nlp-ai/) 步骤 | 通过工作区 AI 连接对文本列做嵌入。 |
| OpenAI | 完整 | [Text NLP AI](/zh-cn/reference/workflow-steps/text-documents/nlp-ai/) 步骤 | 通过工作区 AI 连接回答问题或对文本做嵌入。 |
| Pinecone Lookup | 完整 | [REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/) | 为每一行查询 Pinecone 索引，并添加 pinecone_matches 和 pinecone_error 列。 |
| SageMaker Endpoint | 完整 | [Text NLP AI](/zh-cn/reference/workflow-steps/text-documents/nlp-ai/) 步骤 | 通过工作区 AI 连接回答问题。 |
| Text Processing | 完整 | 分块拆分使用 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤；网页抓取使用 [REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/) | 分块拆分成为按字符分块的表达式；网页抓取会获取每行的 URL，并将页面内容联接回该行。 |

### Subgraph/Control

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Control Flow Input | 完整 | 已丢弃（仅为边界标记） | 已丢弃；它只标记迭代器子工作流的输入边界。 |
| Control Flow Output | 完整 | 已丢弃（仅为边界标记） | 已丢弃；它只标记迭代器子工作流的输出边界。 |
| Subgraph (Basic) | 完整 | 画布容器 / 由内联流程生成的嵌套工作流 | 将内联的内部图转换为带输入/输出表参数的嵌套工作流（或内联步骤）。 |
| Table Iterator | 完整 | [Workflow Loop](/zh-cn/reference/workflow-steps/workflow-control/workflow-loop/) 步骤 | 对每个输入行运行一次循环体，并用该行对应的列设置每个配置值，最多运行 maxIteration 次。 |
| While Iterator | 完整 | [Workflow Loop](/zh-cn/reference/workflow-steps/workflow-control/workflow-loop/) 步骤 | 每次遍历运行一次循环体并传入迭代序号，直到循环体不返回任何行或达到该 gem 的最大值。 |

## SQL / Analyst gem

### Source/Target

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| External table Source/Target (BigQuery, Databricks, SAP HANA, MongoDB, MSSQL, Oracle, Postgres, Redshift, Salesforce, Snowflake, Synapse) | 完整 | 带匹配数据库连接的外部数据导入/导出步骤 | 通过 PlaidCloud 连接读取或写入外部数据库中的表。 |
| File storage Source/Target (ADLS, Databricks Volumes, GCS, OneDrive, S3, SFTP, SharePoint, Smartsheet) | 完整 | 针对文档账户（ADLS/GCS/S3/SFTP/SharePoint/OneDrive）的导入/导出文件步骤 | 读取或写入云存储/SFTP 存储中的文件，支持通配符合并、触发器、删除/移动和加密选项。 |
| Model | 完整 | 上游步骤的输出表 | 将另一个 model 读取为所引用上游步骤产生的表。 |
| Seed | 完整 | [导入：CSV](/zh-cn/reference/workflow-steps/import/import-csv/) | Seed CSV 会被导入 PlaidCloud 表。 |
| Source | 完整 | 按数据集格式选择的导入步骤（请参阅[连接器](#连接器)） | 每个 Source 都会成为导入到以数据集命名的表中的导入步骤；转换器无法识别的格式会被读取为上传到工作流文档文件夹的 CSV 文件，并给出警告。 |
| Target Model / Table (Target) | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤、[upsert](/zh-cn/reference/workflow-steps/tables/table-upsert/)、[复制表](/zh-cn/reference/workflow-steps/tables/table-copy/)和[全部合并](/zh-cn/reference/workflow-steps/tables/table-union-all/) | 将 model 最终的 select 以 replace、append、upsert、delete-and-insert、SCD2 或按谓词替换的方式写入 PlaidCloud 表。 |
| Upload Files | 完整 | [导入：CSV](/zh-cn/reference/workflow-steps/import/import-csv/) | 上传的本地文件通过导入步骤成为表。 |

### Prepare

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Data Cleansing | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤中的列表达式 | 将空值填充、去除首尾空格和大小写选项转换为列表达式；清理后的列移到最后。 |
| Data Masking | 完整 | 用于字符掩码或哈希的列表达式 | 对所选字符串列就地掩码或哈希，或生成为新列。 |
| Find Duplicates | 完整 | 行号窗口表达式加筛选器 | 按键返回唯一行、重复行，或按计数/位置选出的行。 |
| Generate Rows | 完整 | 对每个输入行联接并筛选的序列表 | 根据 init、condition 和 loop 表达式，为每个输入行生成行。 |
| Imputation | 完整 | 聚合加联接回填和列表达式 | 用平均值、中位数、众数或固定值替换空值或哨兵值。 |
| Multi-Column Edit | 完整 | 按模板展开的逐列表达式 | 将一个表达式模板应用于每个所选列。 |
| Multi-Column Rename | 完整 | select 步骤上的列重命名映射 | 按前缀、后缀或名称表达式重命名所选列。 |
| Record ID | 完整 | 行号或 uuid 列表达式 | 添加 UUID 或顺序记录 ID 列。 |
| Sample | 完整 | 提取上的行数限制或抽样选项 | 对整体或每个分组取前/后/随机/第 N/百分比行。 |
| Tile | 完整 | 用于分块编号和序列的窗口表达式 | 按等和、等计数、标准差区间、不同值或手动切点分配分块编号。 |

### Transform

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Aggregate | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带聚合；当该 gem 进行透视时使用[Pivot](/zh-cn/reference/workflow-steps/tables/table-pivot/) | 分组并聚合，应用 HAVING 条件，并为每个透视值透视出一列；propagate-all 会携带所有其他输入列。 |
| Count Records | 完整 | 带计数函数的聚合步骤 | 以一行返回总计数、非空计数或去重计数。 |
| Data Encoder/Decoder | 完整 | 用于 base64/hex 编码和解码的列表达式 | 对所选列编码或解码；AES 仅适用于 Databricks。 |
| Deduplicate | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带 distinct 或行号筛选器 | 每个键保留一行：distinct、按您的排序顺序取第一行或最后一行、任意一行，或仅保留只出现一次的键。 |
| Dynamic Select | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤中按类型解析的列选择 | 在转换时按类型解析列，生成明确的选择。 |
| Filter | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带筛选表达式 | 转换为带筛选表达式的 Table Extract 步骤；条件为 NULL 的行会被丢弃。 |
| Finance | 完整 | 实现财务函数的列表达式 | 将财务函数结果（FV、PV、NPV、IRR 等）作为新列追加。 |
| Flatten Schema | 完整 | [JSON 解析](/zh-cn/reference/workflow-steps/tables/table-json-parse/)和 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤 | 将嵌套字段展平为以该 gem 的分隔符命名的列，并将数组展开为每个元素一行。 |
| Fuzzy Match | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤和 [User Defined Transform](/zh-cn/reference/workflow-steps/general/user-defined-transform/) 步骤 | 对记录配对，按该 gem 的方法为每个匹配字段评分，对分数求平均，并保留达到或超过您所设阈值的配对。 |
| Limit | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带行数限制 | 转换为行数限制；配置引用会成为项目变量。 |
| Order By | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤上的排序 | 转换为具有相同键、方向和空值位置的排序。 |
| Pivot | 完整 | [Pivot](/zh-cn/reference/workflow-steps/tables/table-pivot/) | 将所选透视值转换为聚合列；在设计时获取的 Simple 模式值列表会按所列值转换。 |
| Reformat | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带列表达式 | 转换为每个输出列一个表达式的 Table Extract 步骤；未列出的列会被丢弃。 |
| Running Total | 完整 | 累计求和窗口表达式列 | 为每个所选列追加累计和。 |
| Snowflake Unpivot (third-party) | 完整 | [Melt](/zh-cn/reference/workflow-steps/tables/table-melt/) | 通过 Snowflake UNPIVOT 对列做逆透视。 |
| Transpose | 完整 | [Melt](/zh-cn/reference/workflow-steps/tables/table-melt/) | 将数据列堆叠为名称列和字符串值列。 |
| TransposeAgg | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带聚合 | 将该 gem 的分组、聚合和透视转换为 Aggregate，并给出需要检查的警告。 |
| Unpivot | 完整 | [Melt](/zh-cn/reference/workflow-steps/tables/table-melt/) | 将数据列堆叠为名称列和值列。 |
| Weighted Average | 完整 | 带加权平均表达式的聚合步骤 | 计算整体或每个分组的加权平均值。 |
| Window Function | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤中的窗口表达式 | 按该 gem 的分区、排序和框架（行或范围）添加窗口列，边界可为无界、当前行或偏移。 |

### Join/Split

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Except | 完整 | 基于所有列的[反联接](/zh-cn/reference/workflow-steps/tables/table-anti-join/)，加上去重的 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤 | 保留第一个输入中未出现在任何其他输入里的行。 |
| Intersect | 完整 | 基于所有列的[内联接](/zh-cn/reference/workflow-steps/tables/table-inner-join/)，加上 Distinct | 保留每个输入中都存在的行。 |
| Join | 完整 | [内联接](/zh-cn/reference/workflow-steps/tables/table-inner-join/)、[多表联接](/zh-cn/reference/workflow-steps/tables/table-multi-table-join/)、[反联接](/zh-cn/reference/workflow-steps/tables/table-anti-join/)或[交叉联接](/zh-cn/reference/workflow-steps/tables/table-cross-join/) | 针对任意联接条件构建每种类型的联接（inner、left、right、full、semi、anti、cross 和 natural），应用 where 子句，并写出 select 列表。 |
| Union | 完整 | [全部合并](/zh-cn/reference/workflow-steps/tables/table-union-all/) | 按位置堆叠各输入，在该 gem 不保留重复行时删除重复行。 |
| Union By Name | 完整 | [全部合并](/zh-cn/reference/workflow-steps/tables/table-union-all/) | 成为按名称对齐列并对缺失列填充 NULL 的全部合并。 |

### Parse

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| JSON Parse | 完整 | [JSON 解析](/zh-cn/reference/workflow-steps/tables/table-json-parse/) | 将 JSON 文本列解析为结构化字段。 |
| Regex | 完整 | Table Extract / Transform 步骤中的正则表达式 | 使用正则表达式对文本列进行替换、解析、匹配或分词。 |
| Text To Columns | 完整 | 带正则分隔符的拆分列/展开步骤 | 使用正则分隔符将带分隔符的列拆分为多列或多行。 |
| XML Parse | 完整 | [XML 解析](/zh-cn/reference/workflow-steps/tables/table-xml-parse/) | 将 XML 文本列解析为结构化字段。 |

### Custom

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Directory | 完整 | [目录列表](/zh-cn/reference/workflow-steps/document/directory-listing/) | 以该 gem 的列列出所绑定文档文件夹中的文件；使用工作表名称选项时，每个工作簿的每个工作表生成一行。文件夹缺失时生成零行。 |
| DynamicInput | 完整 | 查询模板使用 SQL 步骤；多文件模式使用工作流循环 | 查询模板模式将模板嵌入为 SQL 步骤；多文件模式按假设进行映射。 |
| Email | 完整 | [Notify Via Email](/zh-cn/reference/workflow-steps/notifications/notify-via-email/) 步骤 | 通过所绑定的电子邮件连接发送电子邮件，可选附带数据附件。 |
| RestAPI | 完整 | [REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/) | 按您设置的 URL、标头、查询、正文和重试，为每个输入行发送一个请求，保留响应，并轮询异步请求直到完成。凭据来自您绑定的连接。 |
| Script | 完整 | 带数据框访问重写的 Python 步骤 | 将脚本主体嵌入 Python 步骤，并重写数据框访问；Scala 主体会连同说明一并保留。 |
| SQL Statement | 完整 | 每个输出选项卡一个 SQL 步骤，文本翻译为租户方言 | 将每个选项卡嵌入为一个 SQL 步骤，输入绑定为临时表；翻译为租户方言。 |
| StoredProcedure | 完整 | [Agent Remote Execution of SQL](/zh-cn/reference/workflow-steps/agent/agent-remote-execution-of-sql/) 步骤 | 通过您选择的连接在其仓库上调用存储过程：每个输入行调用一次，每个参数由对应的列绑定；若无参数则只调用一次。输入列会原样传递。 |
| Table Operations | 完整 | [Table In-Place Delete](/zh-cn/reference/workflow-steps/tables/table-in-place-delete/)、[Table Update](/zh-cn/reference/workflow-steps/tables/table-update/)、[Table Drop](/zh-cn/reference/workflow-steps/tables/table-drop/) 步骤 | 更新、删除和丢弃会映射为表步骤；vacuum 和 optimize 会成为表优化，或成为带警告的空操作。 |
| ToDo | 完整 | [引发工作流错误](/zh-cn/reference/workflow-steps/workflow-control/raise-workflow-error/)或 [Notify via Log](/zh-cn/reference/workflow-steps/notifications/notify-via-log/) 步骤 | 标记尚待编写的逻辑：没有任何内容读取它时为一条日志消息，后续步骤依赖它时则为一个以该 gem 的消息停止运行的步骤。 |

### Spatial

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Buffer | 完整 | [Spatial Buffer](/zh-cn/reference/workflow-steps/spatial/spatial-buffer/) 步骤 | 按配置的英里或公里距离扩展每个几何图形。 |
| CreatePoint | 完整 | 使用 `geom_point` 的 [Table Extract](/zh-cn/reference/workflow-steps/spatial/spatial-sql-recipes/) 步骤 | 根据经度和纬度列构建点几何图形。 |
| Distance | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤 | 计算两个 WKT 点之间的距离、基本方位和方位角。 |
| FindNearest | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤，带交叉联接 | 为每个源点在最大距离内查找 N 个最近的目标点。 |
| HeatMap | 完整 | [Heat Map (macro)](/zh-cn/reference/workflow-steps/macros/macro-heat-map/) 步骤 | 按该 gem 的分辨率将点分箱到 H3 六边形，按网格距离及其衰减扩散热度，并给出每个六边形的密度和轮廓。 |
| PolyBuild | 完整 | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤和 Python 步骤 | 根据每个分组中有序的点构建多边形或折线 WKT。 |
| Simplify | 完整 | [Spatial Generalize](/zh-cn/reference/workflow-steps/spatial/spatial-generalize/) 步骤 | 按以英里/公里为单位的容差简化 WKT 几何图形。 |
| SpatialMatch | 完整 | [空间匹配](/zh-cn/reference/workflow-steps/spatial/spatial-match/) | 按 intersects/contains/within/touches/envelope 匹配源几何图形和目标几何图形。 |

### Report

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| PowerBIWrite | 完整 | [REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/) | 创建 Power BI 数据集，并通过 Power BI REST API 推送行。 |
| TableauWrite | 完整 | [Publish to Tableau](/zh-cn/reference/workflow-steps/export/export-to-tableau/) 步骤 | 写出 Hyper 提取并发布到所绑定的 Tableau 连接。 |
| Visualize | 完整 | [复制表](/zh-cn/reference/workflow-steps/tables/table-copy/) | 原样传递各行；请在同一个表上将图表构建为 PlaidCloud 仪表板。 |

### Subgraph/Control

| Gem | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Condition | 完整 | [交叉联接](/zh-cn/reference/workflow-steps/tables/table-cross-join/)和 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 步骤 | 对整个输入评估各条件，并将每一行发送到第一个条件成立的输出，否则发送到最后一个输出。 |
| Macro | 完整 | 展开宏主体的 SQL 步骤 | 将宏主体嵌入为翻译为租户方言的 SQL 步骤，输入绑定为临时表。 |
| Pipeline (trigger) | 完整 | [Workflow Loop](/zh-cn/reference/workflow-steps/workflow-control/workflow-loop/) 步骤 | 按您的参数和触发条件，对每个输入行运行一次指定的管道，在运行失败后继续，并为每次运行返回一行。 |
| Subgraph (Basic) | 完整 | 画布容器 / 由内联流程生成的嵌套工作流 | 将内联的内部图转换为带输入/输出表参数的嵌套工作流（或内联步骤）。 |

## 连接器

数据集格式和连接器是 gem 的源和目标设置，而不是 gem。每种格式都会转换为所示的导入或导出步骤，且转换从不连接源系统或目标系统。

| 格式 | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Avro | 完整 | 导入：[Avro](/zh-cn/reference/workflow-steps/import/import-avro/)；导出：[Avro](/zh-cn/reference/workflow-steps/export/export-to-avro/) | 读取和写入 Avro 文件。 |
| BigQuery | 完整 | 带表导入的外部数据库连接 | 通过连接读取和写入。 |
| Binary files | 完整 | 读取文件内容的[目录列表](/zh-cn/reference/workflow-steps/document/directory-listing/)；写入使用 [Alteryx 执行器](/zh-cn/reference/workflow-steps/general/alteryx-executor/) | 读取文件夹中每个文件的路径、修改时间、长度和内容；将每行的内容写入其路径所指向的文件。 |
| Catalog table | 完整 | 现有 PlaidCloud 表绑定 | 按名称绑定到表；读取和每种写入模式都可转换。 |
| Cosmos DB | 完整 | 导入和导出：[REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/) | 通过您的 Cosmos DB 连接读取和写入容器中的文档。 |
| CSV | 完整 | [导入：CSV](/zh-cn/reference/workflow-steps/import/import-csv/)；导出：CSV | 读取和写入带分隔符的文件，支持标题行、分隔符、引号、转义和编码选项。 |
| Data Generator | 完整 | [Table Faker](/zh-cn/reference/workflow-steps/tables/table-faker/) 步骤 | 生成该数据集的各列，使用相同类型的模拟数据。 |
| DataHub table | 完整 | [导入 SQL](/zh-cn/reference/workflow-steps/import/import-sql/) | 通过您的连接读取数据集所指定的表；写入会落到 PlaidCloud 表中。 |
| Delta | 完整 | 现有 PlaidCloud 表绑定 | 以每种写入模式读取和写入表；读取早期版本时，通过您绑定的 Databricks 连接读取。 |
| Excel (XLSX) | 完整 | 导入：Excel；导出：Excel | 读取和写入工作簿的工作表和区域。 |
| Fixed format | 完整 | 导入：[固定宽度](/zh-cn/reference/workflow-steps/import/import-fixed-width/)；导出：[CSV](/zh-cn/reference/workflow-steps/export/export-to-csv/) | 按数据集的列宽布局读取固定宽度文件；写出带分隔符的文件。 |
| Hive | 完整 | 导入：[导入 SQL](/zh-cn/reference/workflow-steps/import/import-sql/)；导出：[外部表](/zh-cn/reference/workflow-steps/export/export-external-tables/) | 通过您的 Hive 连接读取和写入表。 |
| Iceberg | 完整 | 现有 PlaidCloud 表绑定 | 读取和写入表。 |
| JDBC | 完整 | 带表导入的外部数据库连接 | 通过您的连接读取表或查询，并以 replace 或 append 模式写入；写入后会运行 post-write 语句。 |
| JSON | 完整 | [JSON 解析](/zh-cn/reference/workflow-steps/tables/table-json-parse/) | 加载记录并展平嵌套字段。 |
| Kafka | 完整 | 导入：[导入 Kafka](/zh-cn/reference/workflow-steps/import/import-kafka/)；导出：[导出 Kafka](/zh-cn/reference/workflow-steps/export/export-kafka/) | 将一个主题作为一批消息读取，并将行作为消息写入。 |
| MongoDB | 完整 | 导入：[MongoDB](/zh-cn/reference/workflow-steps/import/import-mongodb/)；导出：[MongoDB](/zh-cn/reference/workflow-steps/export/export-mongodb/) | 通过您的 MongoDB 连接读取和写入集合。 |
| ORC | 完整 | 导入：[ORC](/zh-cn/reference/workflow-steps/import/import-orc/)；导出：ORC | 读取和写入 ORC 文件。 |
| Parquet | 完整 | 导入：Parquet；导出：Parquet | 读取和写入 Parquet 文件。 |
| Pinecone | 完整 | 导入和导出：[REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/) | 通过 Pinecone REST API 读取索引的记录，并将行作为向量 upsert。 |
| Redshift | 完整 | 带表导入的外部数据库连接 | 通过连接读取和写入。 |
| Salesforce | 完整 | 导入：[Query Salesforce Object](/zh-cn/reference/workflow-steps/salesforce/query-salesforce-object/)；导出：[REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/) | 通过您的 Salesforce 连接读取对象或 SOQL 查询，并写入记录。 |
| Seed (inline) | 完整 | [导入：CSV](/zh-cn/reference/workflow-steps/import/import-csv/) | 将内联行加载为表。 |
| Slack | 完整 | 导入：[Singer](/zh-cn/reference/workflow-steps/import/import-singer/)；导出：[REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/) | 通过您的 Slack 连接读取频道消息，并将每行作为一条消息发布。 |
| Smartsheet | 完整 | 导入和导出：[REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/) | 通过您的 Smartsheet 连接读取和写入工作表的行。 |
| Snowflake | 完整 | 带表导入的外部数据库连接 | 通过连接读取和写入。 |
| SQL file types (CSV, Excel, JSON, Parquet, Text, XML, fixed-width) | 完整 | 针对文档账户的导入和导出文件步骤 | 读取和写入该文件类型；没有 PlaidCloud 对应项的选项会被标记。 |
| Text | 完整 | 作为单列的[导入：CSV](/zh-cn/reference/workflow-steps/import/import-csv/) | 将每一行读取为一列。 |
| Web page | 完整 | [REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/) | 将数据集 URL 处的页面读入表。 |
| XML | 完整 | [XML 解析](/zh-cn/reference/workflow-steps/tables/table-xml-parse/) | 按行标签加载记录。 |

## 表达式与项目结构

| 范围 | 状态 | PlaidCloud 对应项 | 转换结果 |
| --- | --- | --- | --- |
| Expressions | 完整 | 逐函数翻译的 Spark 和仓库 SQL 表达式 | 函数和运算符会转换为 PlaidCloud 表达式；没有对应项的函数会按名称标记。 |
| Project and graph structure | 完整 | 项目加载器 | 每种 Prophecy 导出形态都会加载并规范化为同一个模型。 |

## 已知边缘情况

| 情形 | 会发生什么 |
| --- | --- |
| 导出中不包含的代码或数据 | 代码不在导出中的 Gem Builder 或其他自定义 gem，以及对导出中缺失的 dbt 包的宏调用，会成为一个指出缺失内容的步骤；请连同管道代码和 dbt 包一起导出项目，或在 Python 或 SQL 步骤中重建逻辑。Ab Initio Error Detection 和 MTime gem 会传递其输入，因为它们所应用的规则不在导出中。读取项目之外文件的 Soda 检查，以及与早期扫描或另一个数据集比较的 Soda 检查，或测试 Soda 所指明格式的检查，在结果表中没有对应行；请在后续步骤中计算它们。 |
| 仅在管道运行时才可知的结果 | 展平其响应的 REST API gem，在没有任何内容声明字段名称时会把整个响应放入一列，而这只有运行时才会揭示；请在后续步骤中提取您需要的字段。在 dbt 编译时查询仓库的 dbt 宏会成为一个指出它的步骤；请将查询替换为其返回的值。Spark StoredProcedure gem 可以运行，但不会返回其 OUT 值；输出是传递的列。`input_file_name()` 对表或 Delta 源返回空字符串，因为它们没有可命名的文件；聚合、窗口或多输入 gem 内的 `hash()` / `xxhash64()` 由仓库计算，因此可能与 Spark 的结果不同。 |
| 项目转换时写入步骤的值 | 包含引号、反斜杠或花括号的参数值、SQL 步骤读取的管道值，以及 Delta 表操作通过配置指定的数据库，都会作为固定值写入步骤，因此更改工作流变量不会改变它们；配置变化时请编辑该步骤。 |
| Scala 代码 | Scala 脚本、Scala 表达式，或 Scala 用户定义函数或聚合函数，会成为一个指出它的步骤；请用 SQL 或 Python 重写。 |
| Kafka Kerberos 登录 | 使用 Kerberos（GSSAPI）登录的 Kafka 源或目标，转换后不带 Kerberos 服务名称和登录机制；请在 PlaidCloud 连接上设置它们。 |
| 流式处理 | 流式源、目标和管道会作为批处理工作流，对运行时存在的数据运行；请按需要的频率为工作流设置运行计划。 |
| 作业组件 | Spark 作业会转换其唯一的管道和计划；其他组件、运行条件和配置覆盖不会被转换。 |
| 不常见的调用 | 在汇总或窗口中调用的用户定义聚合函数，以及使用了 if、for、set 和常用筛选器之外 Jinja 功能的 dbt 宏，会成为一个指出该 gem 的步骤；请从 Aggregate gem 中调用该函数，或将宏内联。 |

## 验证已转换的工作流

请将已转换工作流的输出与您自己的 Prophecy 管道的输出进行比较：结构、行数和行值。除非工作流依赖行顺序，否则可忽略行顺序。
