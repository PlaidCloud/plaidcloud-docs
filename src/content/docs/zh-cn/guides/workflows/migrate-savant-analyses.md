---
title: 迁移 Savant 分析
description: 在 Analyze 应用、REST API 或连接 MCP 的 AI 代理中，将 Savant Labs 分析导出文件转换为 PlaidCloud 高级工作流，绑定其源，并阅读转换报告。
sidebar:
  order: 31
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-savant-analyses.md
---

PlaidCloud 可直接替代 Savant。每个 Savant 代理、表达式和设置都会转换为 PlaidCloud 并可运行。转换器会把 Savant Labs 分析导出文件转换为可运行的高级工作流：它把每个 Savant 代理映射为工作流步骤、项目变量或画布对象，保留原始图，并返回一份转换报告，列出所有未能转换的内容。

转换会读取您指定的导出文件，以及您绑定到其源的文件的标题行。它不会连接 Savant 源或目标所连接的系统。

## PlaidCloud 会创建什么

- 每个 Savant 代理都会变成对应的工作流步骤，并保留上下游关系。[Savant 转换矩阵](/zh-cn/reference/savant-conversion-matrix/)列出了每个代理及其映射层级。
- Savant 分析参数会变成项目变量，代理设置中对参数的引用会被改写为 PlaidCloud 变量语法。
- 注释和分组会作为注释和分组出现在画布上。
- 每个源会变成一个导入步骤，或读取现有的表，具体取决于您如何绑定。
- 每种 Savant 代理类型都会完整转换：每个选项都有对应的映射。Savant 自身会失败或未记录的配置，会作为具名占位符步骤出现。请参阅[未转换配置的占位符](#未转换配置的占位符)。

## 开始之前

1. 使用 **Export JSON** 从 Savant 导出分析。
2. 将 `.json` 文件上传到您可以读取的[文档账户](/zh-cn/guides/documents/adding-accounts/)。
3. 选择接收工作流的 PlaidCloud 项目。您需要对其具有写入权限。
4. 选择一个文档账户和基础文件夹，分析的源文件将从中读取。

## 转换分析

可以从 Analyze 应用、REST API 或 MCP 工具目录进行转换。三种方式使用相同的字段。

### Analyze 应用

1. 打开 **Analyze**，然后选择 **Tools → 导入 Savant 分析**。
2. 选择**目标项目**，以及已上传到文档账户的 **Savant 导出文件 (.json)**。
3. 选择**加载源**。窗口会列出导出文件中的每个源节点。
4. 要将源连接到您已有的数据，请选中它并选择**绑定…**。选择**项目表**以读取目标项目中的表，或选择**文档**以从文档账户读取文件（Excel 可选填工作表名称）。选择**取消绑定**可移除绑定。
5. 在**未绑定源目录**下，选择未绑定源的文件读取所在的文档账户和基础文件夹。
6. 在**转换选项**下，选择**工作流类型**，以及是否**允许未转换的占位符**。在**对象前缀**下，可选择设置工作流、步骤和表的前缀。
7. 选择**转换**。

转换完成后，窗口会显示转换报告：工作流名称和表前缀、警告、未绑定源应将文件上传到的文档路径表，以及需要检查的步骤。如果无法加载源列表，请为每个源添加一行，填写其节点 ID 和要绑定的表的 `analyzetable_` ID。

### 字段

REST API 和 MCP 工具使用以下字段。

| 字段 | 是否必填 | 作用 |
| --- | --- | --- |
| `source_account_id` | 是 | 存放 Savant 导出文件的文档账户。 |
| `source_file_path` | 是 | 导出文件在该账户内的路径。 |
| `project_id` | 是 | 创建工作流的项目。 |
| `document_account_id` | 是 | 未绑定源读取所用的文档账户。 |
| `document_account_path` | 是 | 该账户中未绑定源所用的基础文件夹。空值或 `/` 表示账户根目录，开头的 `/` 会被忽略。包含 `..` 或以点开头的路径段、花括号、盘符或 URL 方案、控制字符的路径会被拒绝。 |
| `workflow_prefix` | 否 | 添加到工作流名称前的前缀。 |
| `step_prefix` | 否 | 添加到步骤名称前的前缀。 |
| `table_prefix` | 否 | 添加到表名称前的前缀。默认为工作流自身的名称。会重用现有表名的前缀在创建任何内容之前就会被拒绝。所用前缀会在转换报告中返回。 |
| `workflow_type` | 否 | `advanced`（默认）将图布置到 DAG 画布上。`standard` 生成串行步骤列表。 |
| `source_bindings` | 否 | 将源绑定到现有数据。请参阅[绑定源](#绑定源)。 |
| `destination_bindings` | 否 | 将目标路由到文档账户、连接表、Google 表格、Tableau 数据源、Slack 频道或电子邮件收件人。仅限 REST 和 MCP。请参阅[目标](#目标)。 |
| `api_bindings` | 否 | 指定 API 代理的相对 URL 的去向：基础 URL 或 REST 连接。仅限 REST 和 MCP。请参阅[绑定 API 请求](#绑定-api-请求)。 |
| `allow_unconverted_placeholders` | 否 | 控制占位符在运行时的行为。请参阅[未转换配置的占位符](#未转换配置的占位符)。 |

### REST

将这些字段作为 JSON 请求体发送到：

```text
POST /rest/v1/analyze/savant/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/savant/quarterly-margin.json",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/savant-inputs"
}
```

要在构建 `source_bindings` 之前列出导出文件的源节点，请将 `source_account_id` 和 `source_file_path` 发送到：

```text
POST /rest/v1/analyze/savant/sources
```

响应中的每个条目都包含该源的 `node_id`、`name` 和 `connector`。

### MCP

连接 MCP 的 AI 代理使用相同的字段调用 `savant_convert` 工具。要连接代理，请参阅 [AI 代理 (MCP)](/zh-cn/integrations/ai-coding-agents/)。该工具会更改您的项目，因此请在批准调用之前先进行检查。

## 转换时绑定

Savant 导出文件不含数据、凭据和连接，因此有三个转换时参数用来把它连接到您的环境。每个参数都是从 Savant 节点 ID 或名称到目标的映射，无法使用的绑定会使整个转换在创建任何内容之前就被拒绝。

| 参数 | 绑定对象 | 章节 |
| --- | --- | --- |
| `source_bindings` | 源代理到表或文件 | [绑定源](#绑定源) |
| `destination_bindings` | 目标代理到文件、表、工作表、Tableau 数据源、Slack 频道或电子邮件 | [目标](#目标) |
| `api_bindings` | 带相对 URL 的 API 代理到基础 URL 或 REST 连接 | [绑定 API 请求](#绑定-api-请求) |

## 绑定源

Savant 导出文件描述了数据的来源，但不携带数据和凭据。使用 `source_bindings` 将每个源连接到您在 PlaidCloud 中已有的数据。键是源的节点 ID、数据集 ID 或名称。值可以是以下之一：

- 目标项目中某个表的 `analyzetable_` ID。转换后的工作流会直接读取该表。
- 包含 `account`、`path` 以及可选 `sheet` 的对象，用于从文档账户读取文件。

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "Budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

无法读取的绑定会被拒绝。与任何源都不匹配的键会作为警告报告。

导出文件中的源文件路径可以以 `/` 开头，或经过 `.archive` 这类点开头的文件夹，仍可转换。读取 XML 的源会转换 XML 文本，XML 文档源还会带有 Savant 的文件上下文列。

### 未绑定的源

没有绑定的源会变成暂无数据的导入步骤，转换报告会为其附上警告。该步骤从以下位置读取：

```text
<document_account_path>/savant/<workflow id>/<source name>.csv
```

将文件上传到该路径并运行工作流。在文件就位之前，导入步骤会带着警告完成并创建一个空表，工作流继续执行。

## 代理如何转换

大多数代理会转换为您手动构建的步骤；[Savant 转换矩阵](/zh-cn/reference/savant-conversion-matrix/)列出了每个代理。以下代理需要额外注意。

| Savant 代理 | 转换为 | 注意事项 |
| --- | --- | --- |
| Infer 代理（`gen_ai`，以及使用 LLM 服务的旧版 `service`） | 采用**提示词**任务的 [AI/NLP](/zh-cn/reference/workflow-steps/text-documents/nlp-ai/) 步骤。提示词针对输入字段逐行运行一次，答案落在每个输入列旁边的 **AI Answer** 列中。行数限制变成**最大行数**，空源会发出警告并写入空表。**Max New Rows** 只回答新增的行，并保留早先运行的答案。 | 由 LLM 作答，因此输出绝不会与 Savant 逐字节相同，且每次运行可能不同。每次调用都有成本。请参阅 [AI 提供商](#ai-提供商)。失败的批次会保留其行，答案为空，并发出警告。 |
| Vision 代理（`vision`） | [Document Read Blob](/zh-cn/reference/workflow-steps/text-documents/document-blob-extract/) 步骤、[Image OCR](/zh-cn/reference/workflow-steps/text-documents/image-ocr/)，然后是 AI/NLP **提示词**任务。当提供商接受该类型和大小时，每个文档会作为图像或 PDF 发送给提供商。否则该步骤发送其 PDF 文本层或 OCR 文本。 | 与 Infer 代理相同的 LLM 注意事项。完整文档会离开 PlaidCloud 发送给提供商，转换时会发出警告。TIFF 和 BMP 文件作为 OCR 文本发送，且没有最大文档大小设置。找不到的文档会被跳过，步骤会带着其路径发出警告。 |
| API 代理（`apiService`，以及使用 API 服务的旧版 `service`） | [REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/)步骤，每个输入行发送一个请求，然后联接回去以保留每个输入行。原始响应正文落在文本列中，旁边是状态列。每个周期的配额变成小数形式的**最大请求数/秒**。相对 URL 会与您通过 `api_bindings` 绑定的基础 URL 或 REST 连接拼接。来自行字段的主机、端口或路径会逐行填入。支持跟随 next-URL、Link 标头、偏移量和页码分页，分页值（起始位置、页面大小或参数名称）可以来自输入字段或参数。 | 非 GET 方法每次运行工作流时都会针对实时系统为每个输入行运行一次，因此首次运行前请确认目标。非 GET 请求不会自动重试。失败的请求会保留为带状态的一行。携带凭据的请求不能从行字段获取主机。凭据的处理方式见 [带凭据的 API 步骤](#带凭据的-api-步骤)。 |
| Recursion 代理（`hierarchy`） | [Hierarchy Closure](/zh-cn/reference/workflow-steps/tables/table-hierarchy-closure/) 步骤，沿父链向上遍历每一行（深度不限），然后对每个节点在其到根的路径（含自身）上的 ID 进行聚合。它会写入 Depth 和 Path。父级为空，或父级就是自身的行为根。 | 父级 ID 中的循环会在重复节点处停止，并保留它之前的每个祖先。具有多个父级的行各自保留自己的值。 |
| Search and Replace（`search_replace`） | [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/)，将每条规则按顺序应用于所选文本列，区分或不区分大小写、全字匹配或不匹配。每条规则按其模式运行：替换匹配的文本、当单元格包含该文本时替换整个单元格、当单元格完全匹配时替换整个单元格，或追加到单元格。 | 规则是字面文本，不是模式。 |
| Split（`split`） | [Split Text](/zh-cn/reference/workflow-steps/tables/table-split-text/) 步骤。它按任意长度的字面分隔符拆分为列或行，并在工作流运行时根据数据确定列数。 | 无。 |
| Time Series（`rollup`） | 按周期表达式分组的 Table Extract，配合 [Period Spine](/zh-cn/reference/workflow-steps/tables/table-period-spine/)、反联接以及用零填充无记录期间的合并。 | 日期为 NULL 的记录会被排除。时间轴最多 100,000 个期间。 |
| Format（`format`） | 带有重命名、重设类型、隐藏和填充的 Table Extract，或用于以行替换名称的 [Promote Header](/zh-cn/reference/workflow-steps/tables/table-promote-header/) 步骤。 | 对非文本列的填充会将默认值转换为该列的类型。对未声明列的源提升标题行时，会读取 CSV、Excel、XLS、JSON、Parquet 和 Avro 文件中的每一列。请参阅[未声明列的文件](#未声明列的文件)。 |
| Spatial Match 代理（`spatial_match`） | [空间匹配（执行器）](/zh-cn/reference/workflow-steps/spatial/spatial-match-executor/)步骤，适用于 intersects、within、contains、touches、crosses、overlaps、equals 和 disjoint，可组合多条规则；交叉匹配使用交叉联接；最近匹配使用[查找最近点](/zh-cn/reference/workflow-steps/spatial/spatial-find-nearest/)。 | 最近匹配与 Savant 一样，按大圆距离排序和筛选。与其他规则组合的最近规则会先找出最近的记录，再应用其他规则：使用 AND 时结果保留满足每条规则的记录，使用 OR 时则将最近的记录与其他规则匹配的记录取并集。既无数量也无最大距离的最近规则只保留最近的一条记录。距离内匹配同样可转换，规则未给出单位时以公里计，并测量任意几何图形（不仅是点）之间的测地线距离。无法解析的几何图形给出 NULL 或无匹配，并发出警告。 |
| Spatial Summarize 代理（`spatial_summarize`） | 用于并集、交集和边界框的[空间合并](/zh-cn/reference/workflow-steps/spatial/spatial-combine/)，以及用于几何中心和线或多边形构建的 [Spatial Centroid](/zh-cn/reference/workflow-steps/spatial/spatial-centroid/)、[Spatial Point to Line](/zh-cn/reference/workflow-steps/spatial/spatial-point-to-line/) 和 [Spatial Line to Polygon](/zh-cn/reference/workflow-steps/spatial/spatial-line-to-polygon/)。 | 由少于 3 个点构建的多边形是空多边形。 |
| Destination 代理（`destination`） | 导出到您所绑定目标的导出步骤；未绑定时为项目表或文件。请参阅[目标](#目标)。 | 请参阅[仍然受限的内容](#what-stays-limited)。 |

`GEO_POINT`、`GEO_TYPE` 和 `GEO_SPATIAL_DISTANCE` 转换为表达式。整个表达式就是另一个 `GEO_*` 函数（如 `GEO_AREA` 或 `GEO_UNION`）的编辑，会转换为对应的空间步骤，包括 [Spatial Info](/zh-cn/reference/workflow-steps/spatial/spatial-info/)。几何图形以 WKT 文本传输。以英里为单位的 `GEO_AREA`、`GEO_PERIMETER` 和 `GEO_SPATIAL_DISTANCE` 使用法定英里。

读取二进制文件的源（例如 Vision 代理读取的文档）会转换为对所绑定文档的文档提取，或对预期位于未绑定源路径下的文件的文档提取。

## AI 提供商

Infer 或 Vision 代理会转换为使用 LLM 连接的 AI/NLP 步骤。转换器支持 Anthropic、OpenAI、Gemini、Azure OpenAI、Grok 和 GitHub Models。

- 转换器根据代理指定的提供商和模型，从导入用户可见的 LLM 连接中选择连接。它绝不会指定用户看不到的连接。通过 AI 助手 (MCP) 时，指的是助手用户可见的连接。
- 当提供商没有可见连接，或 Savant 的提供商在 PlaidCloud 中没有对应项（Savant 工作区的云托管模型 API 或自带密钥提供商）时，若用户可见工作区默认连接，步骤就使用该连接。否则它会将连接留空，步骤在运行时使用工作区默认连接。两种情况下转换报告都会发出警告，因此如果应由其他连接作答，请在步骤上选择连接。

## 目标

Savant 目标会把它收到的表写入您绑定的目标。请在 REST 请求体或 MCP 调用中使用 `destination_bindings` 绑定目标。键是目标的节点 ID 或名称。Analyze 窗口不绑定目标，因此在其中转换的目标会写入[未绑定的目标](#未绑定的目标)中所述的未绑定结果。

| 目标 | 绑定 | 结果 |
| --- | --- | --- |
| 文档账户 | `{account, path[, file_name]}` | 按目标的类型生成 CSV、TSV、TXT、Excel、Parquet、JSON、Avro、XML、PDF 或 Tableau Hyper 文件。您需要对该账户具有文档存储写入权限。 |
| 连接上的表 | `{connection, table[, schema, replace]}` | [Export: External Database Tables](/zh-cn/reference/workflow-steps/export/export-external-tables/) 步骤。您需要连接写入权限。替换表需要 `replace: true`。 |
| Google 表格 | `{connection, spreadsheet_name[, sheet_name, replace]}`，或 `{connection, spreadsheet_id[, sheet_name, replace]}` | Google 表格连接上的 [Export to Google Spreadsheet](/zh-cn/reference/workflow-steps/export/export-to-google-spreadsheet/) 步骤。选项卡默认为目标指定的那个，否则为 `Sheet1`。替换工作表行的目标会清空该选项卡，因此需要 `replace: true`。 |
| Tableau | `{account, connection[, path, file_name, replace, datasource_name, tableau_project]}` | 写入账户文件夹的 Tableau Hyper 提取，然后是 [Tableau 连接](/zh-cn/reference/connectors/collaboration/tableau/)上的 [Publish to Tableau](/zh-cn/reference/workflow-steps/export/export-to-tableau/) 步骤。替换数据源，或按匹配键更改其行，需要 `replace: true`。 |
| Slack | `{connection[, channel]}` | CSV 先写入文档账户，然后 [Notify via Slack](/zh-cn/reference/workflow-steps/notifications/notify-via-slack/) 步骤将其上传到频道。连接需要机器人令牌，频道必须是频道 ID，取自绑定，否则取自导出文件。 |
| 电子邮件 | `{email_to: [...]}`，以及 `email_export_recipients: true`（同时使用导出文件列出的收件人） | CSV 作为附件邮寄。您需要电子邮件写入权限。 |

Google 表格、Tableau 或 Slack 连接的检查方式与表连接相同：您必须能看到它并拥有连接写入权限，否则转换会被拒绝。

### 写入模式

- 追加的文件或表目标会读回早先的文件，并连同新行一起重写。它绝不会覆盖。
- upsert、update 或 groupReplace 目标按目标的匹配键合并。文件或表会被读回并重写，Tableau 数据源则就地更改其匹配的行。
- 追加和合并也适用于按值拆分的现有文件、无标题行的文件（按位置匹配行）、锚定在左上角单元格的 Excel 文件，以及使用非 UTF-8 字符集的文件。拆分会读回每个值所写入的文件并在其中合并，其他文件保持不变。
- Tableau 目标将 Savant 的模式映射到 [Publish to Tableau](/zh-cn/reference/workflow-steps/export/export-to-tableau/#模式) 的六种模式：append 和 insert 添加行，replace 覆盖，upsert、update 和 groupReplace 按键匹配。更改现有数据的模式只有在绑定写明 `replace: true` 时才会发布；否则目标会发布一个新的数据源，并在报告中说明。
- 带输出编码的目标以该 Java 字符集写入文件。字符集中缺少的字符会像 Savant 一样写成 `?`。接受 Java 别名、CESU-8 和字节顺序标记形式。少数罕见字符集（例如 `x-ISCII91` 或 `JIS_X0212`）无法写入；文件会以 UTF-8 写入，并在报告中发出警告。使用非 UTF-8 字符集的拆分会转换该文件夹。
- 导出文件名必须保持在所绑定的文件夹内。

### AI 调用方可以绑定的内容

通过 AI 助手 (MCP) 的转换会绑定相同的形式，但会保留其中某些部分，并为每个部分发出写明该部分的警告：

| 被保留的部分 | 改为发生的情况 |
| --- | --- |
| 表、工作表或 Tableau 数据源上的 `replace` | 追加的目标仍追加到其绑定的表或工作表。替换的目标写入 CSV。Tableau 目标发布新的数据源。 |
| 电子邮件收件人 | 写入 CSV 以代替电子邮件。 |
| Slack | 写入 CSV 以代替 Slack 帖子。 |

如需绑定这些内容，请从 Analyze 应用或 REST API 转换，或由您本人登录而不是通过助手。

### 未绑定的目标

没有绑定的目标会写入其 PlaidCloud 对应项，并发出写明原始目标的警告 **Destination target unbound**。转换绝不会连接目标系统。

| 目标 | 结果 |
| --- | --- |
| 数据库、仓库或 SaaS 目标（Oracle、通用数据库、Looker Studio、NetSuite、SAP，以及未绑定连接的 Google 表格、Tableau 或 Slack） | 项目中的一个表，以目标节点命名。 |
| 文件存储（S3、GCS、Box、SFTP、SharePoint、Google Drive、OneDrive） | 目标文件类型的文件，位于您为未绑定源提供的账户下的文档文件夹中。该文件夹与目标文件夹一致。凭据和共享令牌会从路径中去除。 |
| 电子邮件 | CSV，位于您为未绑定源提供的文档账户中。 |

警告会告诉您要绑定什么才能到达真实目标。绑定无法使用的目标会写入 CSV，并发出警告 **Fallback, target not written**，消息中带有原始目标；依赖该 CSV 之前请先检查它。普通 CSV 目标写入自己的文件。

### 拆分目标

按字段的每个值写入一个文件、子文件夹或选项卡的目标，可拆分 CSV、Excel、Parquet 和 PDF 文件以及 Google 表格选项卡。

- **Parquet 和 PDF。** 每个值一个文件。
- **Google 表格。** 每个值一个选项卡。
- **模板。** 模板工作簿作为每个值的工作簿的基础。缺少模板时会发出警告，并在没有模板的情况下写入工作簿。
- **NULL 值。** NULL 拆分值会写入其自己的文件或选项卡，而不是被丢弃。
- **输入中缺少的字段。** 对输入中不存在的字段进行拆分或排序，会按名称被拒绝，因为 Savant 对此会失败。
- **值中的 `/` 或 `\`。** 包含斜杠或反斜杠的拆分值不能作为文件或选项卡名称，因此会被清理。更改过的值会获得固定的六字符后缀：`-` 加上该值 MD5 哈希的前六个字符，放在文件扩展名之前。无需更改的值保留其名称。

### 导出值和行顺序

- **纯数字和布尔值。** CSV、TSV 和 TXT 导出将数字写为纯数字，将布尔值写为 `true` 和 `false`，时间戳不带 `+00:00`。
- **稳定的行顺序。** 排序的目标每次运行都写出相同的行顺序：相同排序值的行每次按同样的方式打破平局，拆分和分段路由同样会排序。Parquet、Google 表格、Tableau 和表目标不保留行顺序。

### Excel 选项

Excel 目标映射以下选项：

- **每个字段值一个选项卡。** 字段的每个值成为一个工作表。空白值进入 `Sheet1`，名称冲突的工作表会获得数字后缀。
- **来自模板的格式。** 每次运行会先将同一文件夹中的 `<name>_template.xlsx` 复制覆盖到工作簿上，然后写入其中，因此工作簿总是被替换。如果模板不存在，复制时会发出警告，并在没有模板的情况下写入工作簿。
- **左上角单元格。** 行从该单元格开始写入工作簿。
- **模式 `create`。** 每次运行都按目标的写入模式写入文件。

## 绑定 API 请求

URL 为相对路径（例如 `/v2/customers`）的 API 代理没有可发送的主机。请使用 `api_bindings` 绑定一个。键是 API 节点的 ID 或名称，或用 `*` 表示每个没有自己绑定的 API 节点。值是以下之一：

- 基础 URL，可为字符串或 `{"base_url": "https://host/path"}`。相对 URL 会与它拼接。该 URL 必须是带公共主机的 `http` 或 `https`，且不含用户、查询或片段。
- `{"connection": "<REST connection id>"}`。请求会发送到该 [REST 连接](/zh-cn/reference/connectors/rest/generic-rest/)的主机并携带其凭据。您需要连接写入权限，且该连接必须是您能看到的 REST 连接。

```json
"api_bindings": {
  "*": "https://api.example.com/v1",
  "Customers": { "connection": "<REST connection id>" }
}
```

未匹配的键是警告，无法使用的绑定会被拒绝。没有绑定的相对 URL 仍是具名占位符。

没有连接写入权限的 AI 助手 (MCP) 的连接绑定会被忽略并发出警告，原本会拼接的相对 URL 仍是占位符。请绑定基础 URL，或从 Analyze 应用或 REST API 转换。

来自输入字段的主机、端口或路径无需绑定。它会逐行填入，每个值在使用时都会被检查，报告会列出行可能指定的主机。携带凭据的请求不能从行字段获取主机：向由数据选择的主机发送凭据会被拒绝。

分页同样可转换。响应中的下一页 URL、`Link` 标头、偏移量和页码，各自成为 [REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/)步骤上的一种分页模式，该步骤会读取每一页。分页值可以来自输入字段（`{{Field}}`）或参数（`{{Param}}`），写成 `10.0` 这样的数字文本的值会被读作数字。

## 带凭据的 API 步骤

API 代理的标头、URL 路径、查询或正文中的凭据，会移入导入所创建的 PlaidCloud REST 连接。REST 请求步骤引用该连接，因此凭据绝不会留在步骤中。

- 响应在 `connections` 下列出导入创建或重用的连接，导入报告也会写明它们。再次导入同一分析会重用同一连接，而不是再创建一个。
- URL 用户信息和标头中的凭据会进入连接自己的身份验证字段或默认标头。路径、查询和正文中的机密会加密存储在连接上，并在运行时填入，仅用于发往该连接自己的 `https` 主机的请求。
- 未加密的 `http://` 端点不会连同凭据一起转换。凭据会被省略，转换报告会警告其未被复制。
- 通过 AI 助手 (MCP) 导入不会创建连接。凭据会被省略并发出警告说明。请改从 Analyze 应用或 REST API 导入，或手动将凭据添加到 REST 连接并在步骤上选择它。
- 没有连接写入权限的用户会得到同样的结果：凭据被省略并发出警告。
- 只有 API 凭据位置会把参数移入连接。在 API 凭据所在位置的标头、查询、路径或正文中使用的管道参数，会移入连接的加密 `secret_values`，步骤通过连接引用它。无论参数叫什么名字，它都不会被创建为工作流变量。
- 名称中含有机密词（如 `password`、`token`、`secret` 或 `key`，其中 `key` 在 `sort` 或 `partition` 等数据词之后除外）的任何其他参数，会变成值为空的工作流变量并发出警告。`api_key_2` 这样的名称同样会被置空。导入后请在项目变量上设置值。
- 以计数或限制命名的参数（如 `max_tokens`）保留其值。
- 在公式、筛选器或替换值中键入的机密会从步骤中省略，转换报告会发出警告。路径、URL 以及 40 或 64 个字符的十六进制摘要会被保留，除非其一部分或某个机密名称另有表明。文件夹共享链接和收件人电子邮件地址绝不会出现在警告或备注中。
- 将凭据回显的响应会按收到的内容存储。请将此类请求的输出表视为敏感数据。

## JWT_ENCODE

`JWT_ENCODE` 转换为 [JWT Encode](/zh-cn/reference/workflow-steps/tables/table-jwt-encode/) 步骤。字面签名密钥会进入绑定到该步骤的专用连接，令牌在运行时签名，因此密钥绝不会出现在步骤配置中。通过 AI 助手，或没有连接写入权限时，密钥会被省略，令牌为 NULL，并有警告提示您以具备创建连接的权限重新导入。

## 将数据行提升为列标题

设置为**以行替换名称**的 Format 代理会转换为 [Promote Header](/zh-cn/reference/workflow-steps/tables/table-promote-header/) 步骤。运行时，所选的行（从 1 开始计数）成为列名并被移除。没有记录顺序的源会获得一条备注，因为由哪一行命名列可能在每次运行之间发生变化。该行命名了、但之后没有步骤提及的列，不会被带过列出了其读取列的步骤。

## 未声明列的文件

没有声明列的源会保留这些列：

- 在导入时绑定的 CSV、TSV 或 TXT 源会保留文件标题行中的每一列。
- 任何其他文件类型以及任何未绑定的源，只保留后续步骤指定的列，并且转换报告会发出警告。
- 对此类源提升的标题行会读取 CSV、Excel、XLS、JSON、Parquet 和 Avro 文件中的每一列。

当此类源只供给提升的标题行时，导入是按位置读取每一列的 [Import Delimited](/zh-cn/reference/workflow-steps/import/import-delimited/) 步骤。在提升的标题行之后导出或联接的步骤，会带上运行时表中的每一列（请参阅 [Table Extract](/zh-cn/reference/workflow-steps/tables/table-extract/) 中的**同时带入运行时指定名称的列**）。

## 值得了解的行为

这些转换的行为如下。

| 代理 | 行为 |
| --- | --- |
| Blend（`blend`） | 在 OR 组合的谓词、contains 和 is-part-of 上联接。排除内部的外部联接 Blend 和未匹配的输出会转换为对应的联接流。对任何运算符，右侧重复的键都会从输出中删除。 |
| Dedupe（`deduplicate`） | 在每个**分组依据**分组内，每个键保留第一条记录。重复标记会标出重复组中的每个成员，重复项也可以路由到第二个流。只连接一个出口时，其行为与 Savant 相同。 |
| Summarize（`summarize`） | 窗口聚合会将聚合值添加到每一行，而不是折叠分组。 |
| Sample（`sample`） | 每个分组或整体的前 N 行、随机百分比或随机行数，或每 N 行取一行。 |
| Time Series（`rollup`） | 在可选的开始和结束日期之间，按分组生成日、周、月、季度、年和十年期间。月份期间标记为 `YYYY-MM`，没有记录的期间以零显示。日期为 NULL 的记录会被排除。 |
| Pivot（`pivot`） | COUNT 统计行数。 |
| XML（`xml`） | SELECT 提取元素，路径可以带命名空间，TO_JSON 将 XML 转换为 JSON。任何 **XPath 1.0** 路径都可转换，包括谓词、属性测试、通配符以及 `count()`、`name()` 和 `contains()` 等函数，[XML 解析](/zh-cn/reference/workflow-steps/tables/table-xml-parse/)步骤将其作为 XPath 读取。`processNs` 关闭时，名称按字面匹配，包括前缀。转换时缺失的 XML 文件，会在工作流运行时解析其根元素。 |
| JSON（`json`） | 展平为宽列。不是有效 JSON 的文本给出 NULL，数组以文本形式输出。 |
| Split（`split`） | 拆分为列或行，列数在每次运行工作流时从数据中读取。 |

以下表达式函数遵循 Savant 的结果：

| 函数 | 行为 |
| --- | --- |
| `DATE_DIFF` | 周和季度的计数方式与 Savant 相同。 |
| `PAD` | 不会截断长于目标宽度的值。 |
| 文本上的 `+` | 连接文本。来自未声明类型的源的列会被读作数字，因此 `+` 执行相加，并有备注说明。 |
| 拆分为行 | 将空片段保留为行。 |
| 不带排序的 `LAST` | 按行到达的顺序返回最后一行，并有备注说明仓库不保证该顺序。 |
| `JOIN_STR` | 按 Savant 的写法连接小数，不补尾部零。 |
| `JSON_FORMAT` | 美化输出 JSON；在 Snowflake 上将 JSON 紧凑地写在一行。 |
| `JSON_SET` | 保留 Savant 的键顺序。 |
| `GREATEST` 和 `LEAST` | 跳过 NULL 参数。仅当每个参数都是 NULL 时结果才为 NULL。 |
| `ROUNDUP` | 向上舍入到下一个整步，因此负数向零舍入：-1.5 变成 -1。`ROUNDDOWN` 不变。 |
| `DURING_DAYLIGHT_SAVING` 和 `DURING_STANDARD` | 输入 NULL 则输出 NULL。 |
| 带**日期格式**的 `TO_TEXT` | 按 Savant 的方式读取格式标记。`YYYY`、`w` 和 `u` 分别是 ISO 周年、周和星期几，时区或纪元字母按 UTC 时间写出。 |
| `TO_TEXT` 和数字转文本输出 | 写出 `12` 这样的纯数字，而不是 `12.0000000000`。 |
| 带数字模式的 `TO_TEXT` | 按 Java `DecimalFormat` 的方式格式化，向最接近的偶数舍入，包括 `##0.##E0` 这样的科学计数模式。 |
| 带逐行格式的 `TO_TEXT` 和日期解析 | 从每一行读取格式。 |
| 小数秒、窄月份和基于周的日期标记 | 可转换。周标记按 ISO 周读取。 |
| 两位数年份（`yy`、`y`） | 通过从当前年份起向前 80 年、向后 20 年的窗口读取。 |
| `REGEX_MATCH` | 部分匹配：模式匹配文本中的任意位置，而不是整个文本。 |

`TO_TEXT` 和日期格式在 [Text Function](/zh-cn/reference/workflow-steps/tables/table-text-function/) 步骤中转换。只带已编译步骤、没有表达式的编辑，会转换为按顺序应用的这些步骤，每个步骤为下一个提供输入，转换报告会注明其假定的顺序。转换器会按名称拒绝 Savant 自身会失败或没有可转换内容的情形，该步骤会变成占位符：Transform 或 Filter 表达式内的普通聚合或窗口函数（在计算或 Summarize 内可以转换）、带有 `md5` 或 `sha1` 之外的字面算法的 `HASH`、PlaidCloud 无法读取的正则构造（类中的类、类交集或未知的 `\p{}` 属性）、既无表达式也无已编译步骤的 Transform 编辑（例如只有提示词的 Copilot 编辑）、不是 XPath 1.0 的 XML 路径，以及携带凭据并从行字段获取主机的 API 请求。[Savant 转换矩阵](/zh-cn/reference/savant-conversion-matrix/#具名拒绝项)列出了每一项及其原因。

表达式函数也适用于 `sha1`、`NOT_TRUE`、`LEVENSHTEIN`、夏令时函数 (`DST`)，以及带第 n 次匹配的正则表达式函数。`DAY_OF_WEEK` 将星期日编号为 7，`DAY_NAME` 返回该日的名称。

## 阅读转换报告

响应中包含转换报告：已转换的步骤中高、中、低置信度各有多少、未转换的有多少的摘要，以及警告和被转换器合并到其他节点中的节点。请在运行工作流之前阅读。它会列出每个占位符、每个未绑定的源和未匹配的绑定，以及所用的表前缀。

## 未转换配置的占位符

转换器无法重现的配置会创建为携带代理名称的占位符步骤，转换报告会写明它。对于转换器按名称拒绝的构造（请参阅 [Savant 转换矩阵](/zh-cn/reference/savant-conversion-matrix/#具名拒绝项)），或导出文件没有完整描述的构造（例如缺失的 API 配置），都会出现占位符。默认情况下，占位符在工作流运行到它时会失败，因此运行不会对未实际发生的工作报告成功。

将 `allow_unconverted_placeholders` 设置为 `true`，即可把每个占位符导入为直通步骤。此后运行会越过它继续执行，占位符的输出就是其输入。当其结果很重要时，请使用原生步骤重建该功能。

## 运行已转换的工作流

1. 在项目中打开新工作流。
2. 设置来自 Savant 参数的所有项目变量。
3. 将未绑定源的文件上传到报告中的路径。
4. 运行工作流，并检查每个步骤的输出表。

## 边界情况

以下是与 Savant 仅有的已知差异。转换报告会写明适用的每一项。

- **日期格式。** 格式中含有 `[`、`]`、`'`、`\` 或 `^` 字面量的 `TO_DATE` 或 `TO_DATETIME`，对读入 9999-12-30 或 9999-12-31 的文本，会超出仓库所能保存的最后一个时间戳，报告会发出警告。
- **机密参数。** 名称中含有机密词、或值看起来像凭据的参数，按设计会变成值为空的项目变量。请在变量中设置值。
- **未声明的参数。** 节点使用但导出文件未声明的参数，会作为值为空的项目变量出现。
- **Snowflake 上的 `JSON_FORMAT`。** 它将紧凑的 JSON 写在一行。
- **行顺序。** 已排序的 Parquet、Google 表格、Tableau 和表目标不保留行顺序。
- **Google 表格和 Tableau。** 发布到任一目标都需要通过 `destination_bindings` 绑定其账户。

## 相关指南

- [Savant 转换矩阵](/zh-cn/reference/savant-conversion-matrix/)
- [REST 连接](/zh-cn/reference/connectors/rest/generic-rest/)
- [添加文档账户](/zh-cn/guides/documents/adding-accounts/)
- [管理工作流变量](/zh-cn/guides/workflows/manage-workflow-variables/)
- [AI/NLP 步骤](/zh-cn/reference/workflow-steps/text-documents/nlp-ai/)
- [REST 请求步骤](/zh-cn/guides/workflows/rest-request-step/)
- [运行工作流](/zh-cn/guides/workflows/run-a-workflow/)
