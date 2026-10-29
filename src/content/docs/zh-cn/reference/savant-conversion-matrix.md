---
title: Savant 转换矩阵
description: PlaidCloud 如何将 Savant Labs 分析转换为原生高级工作流，包括每个代理的映射层级和少数具名边缘情况。
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/savant-conversion-matrix.md
---

PlaidCloud 将 Savant Labs 分析转换为原生高级工作流。导入器会把每个 Savant 代理映射为工作流步骤、项目变量或画布对象，因此转换后的工作流可在云端原生运行。

要运行转换，请参阅[迁移 Savant 分析](/zh-cn/guides/workflows/migrate-savant-analyses/)。

每个代理都有一个映射层级。**完整**表示该代理的每个选项都有到 PlaidCloud 步骤的有效映射。按名称拒绝的构造列在“具名拒绝项”下。

外部系统连接器是**连接而非转换**，请参阅[连接外部系统](#连接外部系统)。

## 代理支持

全部 33 个代理均以完整层级转换。

| 代理 | 层级 | PlaidCloud 对应项 | 转换内容 |
| --- | --- | --- | --- |
| 适配器代理 (`adapter`) | 完整 | 选择和架构投影步骤 | 重命名字段、更改字段类型并为字段排序。 |
| API / Infer 代理（旧版服务）(`service`) | 完整 | 按 serviceType 与 API 代理或 Infer 代理相同 | LLMService 按 Infer 代理转换，APIService 按 API 代理转换；缺失或拼写错误的 serviceType 会从节点的键中读取，并给出警告。 |
| API 代理 (`apiService`) | 完整 | Table Extract、[REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/)，以及一个左联接回原表 | 每个输入行发出一次 GET、POST、PUT、PATCH 或 DELETE 请求；原始响应正文存入文本列，HTTP 错误保留为行，每个输入行都会保留，每个周期的配额会变为小数形式的每秒请求数。相对 URL 会与其 api_bindings 基础 URL 或 REST 连接主机拼接；来自行字段的主机、端口或路径会逐行替换；支持跟随 next-URL、Link 标头、偏移量和页码分页，包括由行字段模板化的起始位置、页大小或参数名称。 |
| Blend 代理 (`blend`) | 完整 | [内联接](/zh-cn/reference/workflow-steps/tables/table-inner-join/)、[外联接](/zh-cn/reference/workflow-steps/tables/table-outer-join/)、[反联接](/zh-cn/reference/workflow-steps/tables/table-anti-join/) | 内部、左侧、右侧、完全、反向以及排除内部的外部混合，支持 OR 联接、包含和属于条件，并提供匹配与未匹配流；仅在运行时由透视或解析命名的列会被一并带过。 |
| 去重代理 (`deduplicate`) | 完整 | 带有去重行的 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) | 在“分组依据”组内为每个键保留第一条记录，并将重复项路由到第二个流或为其添加标记。 |
| 目标代理 (`destination`) | 完整 | [导出：CSV](/zh-cn/reference/workflow-steps/export/export-to-csv/)、[导出：Excel](/zh-cn/reference/workflow-steps/export/export-to-excel/)、导出：Parquet、JSON、Avro 或 XML、[Export to PDF](/zh-cn/reference/workflow-steps/export/export-to-pdf/)、[导出：Tableau Hyper](/zh-cn/reference/workflow-steps/export/export-hyper/) 加 [Publish to Tableau](/zh-cn/reference/workflow-steps/export/export-to-tableau/)、[Export: External Database Tables](/zh-cn/reference/workflow-steps/export/export-external-tables/)、[Export to Google Spreadsheet](/zh-cn/reference/workflow-steps/export/export-to-google-spreadsheet/)、[Notify via Slack](/zh-cn/reference/workflow-steps/notifications/notify-via-slack/)，或电子邮件 | 通过 destination_bindings 写入文档账户（CSV、TSV、TXT、Excel、Parquet、JSON、Avro、XML、PDF 或 Tableau .hyper，支持任何 Java 字符集，包括别名、CESU-8 和字节顺序标记形式；字符集中没有的字符会写成 ?）、连接表、Google 表格、Tableau 数据源、Slack 频道或电子邮件收件人。未绑定的目标会改为写入项目表或文档文件（见下文“去向”）。按字段值拆分文件、子文件夹或选项卡时，会拆分 CSV、Excel、Parquet 和 PDF 文件以及 Google 表格选项卡；模板会作为拆分后每个工作簿的初始内容。Excel 选项映射如下：空白值写入 `Sheet1`，冲突的工作表名称添加后缀，`formatFromTemplate`、`topLeftCell` 以及 `create` 模式。追加、upsert、更新和 groupReplace 会基于匹配键合并（文件或表会被读回并重写；拆分时会读回本次运行中每个值所写入的文件并在其中合并，其他文件保持不变；Tableau 就地更新其行）。仅由数据命名的列（提升的标题行的列、透视的值、解析后的 JSON 或 XML 的键）会与已知列一起由每次导出和表写入写出、用于排序和拆分，并追加或合并到表中，或合并到读回了其全部列的文件中。 |
| 展开代理 (`explode`) | 完整 | [交叉联接](/zh-cn/reference/workflow-steps/tables/table-cross-join/) | 将较小的一侧与主流进行交叉联接。 |
| 筛选代理 (`filter`) | 完整 | 带筛选表达式的 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) | 按向导或表达式将记录拆分为真路径和假路径。 |
| 筛选下推 (`pdfilter`) | 完整 | 带筛选表达式的 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) | 数据库端筛选，转换方式与筛选代理相同。 |
| 格式代理 (`format`) | 完整 | 带列重命名的 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/)，或 Promote Header | 隐藏、更改类型、重命名并填充按名称（包含、开头为、结尾为）或按为空而匹配的字段；填充会把默认值写入其类型可转换为该默认值的任意列（文本、数字、日期）。标题行提升和为空匹配在 Promote Header 步骤中于运行时执行，提升的标题行会读取其文件的每一列。 |
| Fuse 代理 (`fuzzy_match`) | 完整 | [Fuzzy Match](/zh-cn/reference/workflow-steps/tables/table-fuzzy-match/)，位于一个 Union All 和两个联接之间 | 将两个输入堆叠，在相似度阈值 80 下按关键字段匹配记录，并连同置信度分数将两侧联接回来。 |
| 分组 (`group`) | 完整 | 画布容器 | 作为工作流组织结构保留。 |
| Infer 代理 (`gen_ai`) | 完整 | [AI/NLP](/zh-cn/reference/workflow-steps/text-documents/nlp-ai/) 提示任务 | 提示会在与 Savant 的提供商和模型匹配的可见 LLM 连接上，针对输入字段逐行运行；答案存入每个输入列旁边的 AI Answer 列。rowLimit 限制每次运行回答的行数并保留较早的答案：此前已回答过的行（相同的提示、模型和输入值）保留其答案，只有尚未回答的行计入限制。 |
| JSON 代理 (`json`) | 完整 | [JSON 解析](/zh-cn/reference/workflow-steps/tables/table-json-parse/) | 将 JSON 字段展平为点号键列，或将数组展开为每个元素一行；键在运行时从数据中读取。 |
| 备注代理 (`notes`) | 完整 | 画布注释 | 作为工作流上下文保留。 |
| 透视代理 (`pivot`) | 完整 | [Pivot](/zh-cn/reference/workflow-steps/tables/table-pivot/) | 将行透视为列并进行聚合。 |
| 递归代理 (`hierarchy`) | 完整 | Hierarchy Closure、[Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 和 [多表联接](/zh-cn/reference/workflow-steps/tables/table-multi-table-join/) | 遍历任意深度的父子树，对每个节点按其到根节点路径上（含自身）的 ID 进行聚合，并写出 Depth 和 Path；循环在重复节点处停止。 |
| 抽样代理 (`sample`) | 完整 | 带行数限制的 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) | 保留前 N 行，可按组、随机百分比或 N 行，或每 N 行取一行。 |
| 查找和替换 (`search_replace`) | 完整 | 带嵌套替换表达式、分阶段拆分的 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) | 查找/替换规则（包含或匹配；替换或追加），区分或不区分大小写，整词或非整词，按顺序应用于所选文本字段；未指定时应用于所有文本字段。 |
| 源代理 (`source`) | 完整 | 通过 `source_bindings` 绑定的导入步骤（[导入：CSV](/zh-cn/reference/workflow-steps/import/import-csv/)、[导入：Excel](/zh-cn/reference/workflow-steps/import/import-excel/)、[导入：SQL](/zh-cn/reference/workflow-steps/import/import-sql/)）或现有表 | 读取已绑定的表或文档；未绑定的源会创建空导入并给出警告。XML 文本通过“导入 XML”读取其文档（未绑定的则读取 savant/<workflow>/<name>.xml）。绑定到 XML 文档的源还会写出导出中的其他列：来自文档的文件名或路径列，其余列留空。位于提升标题行的“格式”之下的源，会按位置读取其 CSV、Excel（包括 Excel 97 .xls）、JSON、Parquet 或 Avro 文件的每一列。 |
| 空间匹配代理 (`spatial_match`) | 完整 | [Spatial Match (executor)](/zh-cn/reference/workflow-steps/spatial/spatial-match-executor/)、[交叉联接](/zh-cn/reference/workflow-steps/tables/table-cross-join/) 或 [查找最近点](/zh-cn/reference/workflow-steps/spatial/spatial-find-nearest/) | 相交、位于内部、包含、接触、交叉、重叠、相等、不相交以及 and/or 多规则匹配，任意几何图形（点、线、多边形）之间的测地线距离内匹配（半径 6371 km 球体上的最短距离），按同一距离并带最大距离的最近 N 个（单独的最近规则不写距离列，与 Savant 一致；与其他规则组合为先最近后筛选、AND 联接和 OR 并集时，每条最近规则会各自添加一个距离列），以及交叉，并提供匹配与未匹配流。 |
| 空间汇总代理 (`spatial_summarize`) | 完整 | [空间合并](/zh-cn/reference/workflow-steps/spatial/spatial-combine/)、Spatial Centroid 以及点到线步骤 | 并集、交集、边界框、一个或多个几何中心，以及折线或多边形构建，按组执行，可选排序。 |
| 拆分代理 (`split`) | 完整 | Split Text，或带 split_part 列的 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) | 按任意长度的字面分隔符将文本字段拆分为行或列，支持修剪和保留原值；列数在运行时从数据中读取。 |
| 拆分输出 (`outlet`) | 完整 | 工作流连线 | 将已命名的输出路由给其使用者。 |
| 堆叠代理 (`multi_stack`) | 完整 | [Union All](/zh-cn/reference/workflow-steps/tables/table-union-all/) | 按名称或位置堆叠任意数量的输入。 |
| 汇总代理 (`summarize`) | 完整 | 带聚合的 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) | 分组并聚合，包括按确定性排序取首个/末个，以及逐行窗口聚合（useWindow）。 |
| 汇总下推 (`pdsummarize`) | 完整 | 带聚合的 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) | 数据库端聚合，转换方式与汇总代理相同。 |
| 文本 (`text`) | 完整 | 画布注释 | 作为工作流上下文保留。 |
| 时间序列代理 (`rollup`) | 完整 | 基于期间分桶表达式的 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 聚合、Period Spine、[反联接](/zh-cn/reference/workflow-steps/tables/table-anti-join/) 和 [Union All](/zh-cn/reference/workflow-steps/tables/table-union-all/) | 在可选的起止日期之间，按组将记录汇总到日、周、月、季度、年或十年期间，排除 NULL 日期并以零填充空期间。 |
| 变换代理 (`edit`) | 完整 | 带列表达式的 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) | 计算列、类型更改和窗口计算（lag、lead、累计求和、行号、前向和后向填充），按顺序求值。仅带有已编译步骤的编辑，会转换为按顺序应用这些步骤，每一步的输出作为下一步的输入。 |
| 逆透视代理 (`unpivot`) | 完整 | [Melt](/zh-cn/reference/workflow-steps/tables/table-melt/) | 将列转换为名称/值对形式的行。 |
| 视觉代理 (`vision`) | 完整 | [Image OCR](/zh-cn/reference/workflow-steps/text-documents/image-ocr/)，然后是 [AI/NLP](/zh-cn/reference/workflow-steps/text-documents/nlp-ai/) 提示任务 | 当提供商接受相应类型和大小时，每个文档会作为图像或 PDF 发送给提供商，否则发送其 PDF 文本层或 OCR 文本；提示的答案存入 AI Answer 列。 |
| XML 代理 (`xml`) | 完整 | [XML 解析](/zh-cn/reference/workflow-steps/tables/table-xml-parse/) | 选择元素，将子值和属性提取到列中，或将 XML 转换为 JSON；简单的 //a/b 路径照常转换，其他任何 XPath 1.0 路径（谓词、属性测试、通配符，以及 count()、name() 和 contains() 等函数）都按 XPath 求值，可识别命名空间，也可按原样处理。 |

接线、画布和下推变体（拆分输出、分组、文本、筛选下推、汇总下推）是 Savant 的节点类型，没有独立的帮助中心代理文章；每一种都按其所对应的代理转换。

API 代理请求中的凭据绝不会被复制到工作流步骤中。通过 https 时，它会移入 REST 连接；通过 http、没有写入连接的权限，或通过 MCP 进行转换时，它会被扣留并给出警告。这是有意为之，不会降低层级。

有两项目标限制不会降低层级。少数罕见字符集（例如 `x-ISCII91` 或 `JIS_X0212`）无法写入；文件会以 UTF-8 写入，并且转换会给出警告。按键合并的 Tableau 发布需要在其目标绑定中设置 `replace: true`；没有它时，转换会给出警告并发布新的数据源，而在已存在数据源的运行中这会失败。

## 具名拒绝项

有八种构造按名称被拒绝而不是被转换。这些都不会降低代理的层级。

| 构造 | 拒绝原因 |
| --- | --- |
| 携带凭据并从输入字段获取主机的 API 代理请求 | 每一行都可能把凭据发送到数据所选择的主机。该请求会变为具名占位符。不带凭据的请求，以及固定主机上的凭据，可以正常转换。 |
| 既没有表达式也没有已编译步骤的变换编辑，例如只有提示的 Copilot 编辑 | 没有可转换的内容：提示不是公式。带有已编译步骤的编辑可以转换。 |
| 变换或筛选表达式中 PlaidCloud 无法读取的正则表达式构造：类中套类、类交集（`&&`）或未知的 `\p{}` 属性 | 该步骤会变为具名占位符，并在运行时拒绝。 |
| 变换或筛选表达式中的聚合函数或窗口函数 | Savant 本身在运行时就会因此失败。作为变换计算或在汇总中使用时可以转换。 |
| 变换或筛选表达式中使用除 `md5` 或 `sha1` 之外的字面算法的 `HASH` | Savant 本身会因此失败（算法必须是 `md5` 或 `sha1`）。从列中读取的算法可以转换，对任何其他值返回 NULL。 |
| 对其输入中不存在的列进行目标排序 | Savant 本身在运行时就会因此失败。 |
| 按其输入中不存在的列的每个值生成一个目标文件、子文件夹、选项卡或工作表 | Savant 本身在运行时就会因此失败。 |
| 不是 XPath 1.0 的 XML 代理路径 | Savant 同样无法运行它。 |

当您使用 `api_bindings` 绑定基础 URL 或 REST 连接时，相对 API URL 可以转换；请参阅[转换时绑定](/zh-cn/guides/workflows/migrate-savant-analyses/#转换时绑定)。

## 表达式语言

Savant 表达式函数和运算符会转换为 PlaidCloud 表达式。层级：**完整**。所有函数和格式均可转换，包括带数字模式的 `TO_TEXT`、仅在逐行时才知晓的格式、小数秒、基于周、季度和时区的日期标记、两位数年份，以及 Java 正则表达式构造。表达式中任意位置的 GEO_* 函数在配套的空间步骤中运行。例外情况见[具名拒绝项](#具名拒绝项)。

已知边缘情况：`TO_DATE` 或 `TO_DATETIME` 的格式包含 `[`、`]`、引号、反斜杠或 `^` 字面量，且文本读出的日期为 9999-12-30 或 9999-12-31，这超出了仓库能保存的最后一个时间戳；转换会给出警告。

## 导出格式

加载器接受每一种 Savant 导出形态：扁平、模型包装、服务器记录、配方信封、数组包装、带 BOM 前缀以及旧版类型别名，并将它们规范化为同一个模型。层级：**完整**。

## 分析参数

Savant 分析参数会转换为工作流变量，节点配置中对它们的引用会改写为 PlaidCloud 变量语法。列表、字典和带别名的参数形态均可加载。层级：**完整**。

已知边缘情况：名称包含机密字样或值看起来像凭据的参数，会变为值为空白的变量，并给出警告。节点使用但导出中未声明的参数，会变为值为空的变量，并给出警告。

## 连接外部系统

Savant 连接器是源和目标，而不是步骤，并且导出不包含数据集或凭据。PlaidCloud 通过连接而不是画布上的节点来访问这些系统。

| Savant | 在 PlaidCloud 中的去向 |
| --- | --- |
| 源连接器 | `source_bindings` 将 Savant 节点或数据集映射到 PlaidCloud 表或文档文件，并通过相应的导入步骤读取；未绑定的源会给出警告且不处理任何内容 |
| 目标：CSV、Excel 和其他文件格式 | 导出步骤（[导出：CSV](/zh-cn/reference/workflow-steps/export/export-to-csv/)、[导出：Excel](/zh-cn/reference/workflow-steps/export/export-to-excel/)、[Export to PDF](/zh-cn/reference/workflow-steps/export/export-to-pdf/)） |
| 目标：Google 表格、Tableau、Slack | 通过您用 `destination_bindings` 绑定的连接，使用 [Export to Google Spreadsheet](/zh-cn/reference/workflow-steps/export/export-to-google-spreadsheet/)、[Publish to Tableau](/zh-cn/reference/workflow-steps/export/export-to-tableau/) 或 [Notify via Slack](/zh-cn/reference/workflow-steps/notifications/notify-via-slack/) |
| 目标：未绑定的数据库、仓库或 SaaS 目标（Oracle、通用数据库、Looker Studio、NetSuite、SAP，以及未绑定连接的 Google 表格、Tableau 或 Slack） | 以目标节点命名的项目表，并给出指明原始目标的警告 |
| 目标：未绑定的文件系统目标（S3、GCS、Box、SFTP、SharePoint、Google Drive、OneDrive） | 以目标的文件类型生成的文件，位于与目标文件夹对应的文档文件夹中，并给出警告。凭据和共享令牌会从文件夹路径中去除 |
| 目标：未绑定的电子邮件 | 一个 CSV，并给出警告 |
| 目标：无法使用的绑定 | 一个 CSV，并给出指明原始目标的警告 |

转换绝不会联系源系统或目标系统。
