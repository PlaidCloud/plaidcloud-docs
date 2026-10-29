---
title: 迁移 KNIME 工作流
description: 从 Analyze 应用、REST API 或连接 MCP 的 AI 代理，将 KNIME 工作流（.knwf）或工作流组（.knar）转换为 PlaidCloud 高级工作流，绑定其输入和连接，并阅读转换报告。
sidebar:
  order: 31.7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-knime-workflows.md
---

PlaidCloud 是 KNIME 的直接替代方案。98.5% 的 KNIME 节点配置可完整转换，207 种核心节点类型中有 205 种为完整支持：每个节点都会变为执行该节点工作的标准 PlaidCloud 工作流步骤。转换器会将 KNIME 工作流存档转换为可运行的高级工作流，保留原有的图结构，并返回一份转换报告，指明您需要设置的内容。[KNIME 转换矩阵](/zh-cn/reference/knime-conversion-matrix/)列出了每个节点。

转换只读取您指定的存档，绝不会连接 KNIME 节点读取或写入的系统。

转换是一次性操作。再次转换同一个存档会创建新的工作流，您在 PlaidCloud 中所做的编辑绝不会与之后的导出合并。

## PlaidCloud 创建的内容

- 每个 KNIME 工作流对应一个高级工作流。`.knwf` 生成一个工作流，`.knar` 则为组中的每个工作流各生成一个。
- 每个 KNIME 节点变为对应的工作流步骤、项目变量或画布对象，并保留上下游关系。元节点和组件会被展平到工作流中，因此其节点作为普通步骤运行。
- 流变量以及 Configuration 和 Widget 节点会变为保存其默认值的项目变量。转换时值已知的开关和循环会被裁剪，并展开为它们所运行的步骤。
- KNIME 表达式语言（Expression、String Manipulation、Math Formula、Column Expressions 和 Rule Engine）会转换为 PlaidCloud 表达式。
- 存档内附带的数据文件会上传到项目默认文档账户中的 `knime/` 文件夹，每个工作流一个文件夹，转换后的读取器从该处导入它们。
- 视图、图表和颜色管理器不影响数据。它们会被丢弃，并列在转换报告中。

## 开始之前

1. 从 KNIME Analytics Platform 将工作流导出为 `.knwf` 文件。若要一次转换多个工作流，请将其工作流组导出为 `.knar` 文件。请将读取器使用的文件放在工作流的 `data` 文件夹中，使其随存档一起打包。
2. 将存档上传到您可以读取的[文档账户](/zh-cn/guides/documents/adding-accounts/)。在 Analyze 应用中，导入窗口上的**浏览**可从您的计算机上传存档。
3. 选择要接收这些工作流的 PlaidCloud 项目。您必须是该项目的架构师或管理者，并且该项目必须有默认文档账户。
4. 记下希望工作流的读取器和连接器节点使用的 PlaidCloud 表、文件和连接。参见[绑定源](#绑定源)。

## 转换工作流

从 Analyze 应用、REST API 或连接 MCP 的 AI 代理进行转换。REST API 和 MCP 工具使用相同的字段；窗口只接受它所显示的字段。

### Analyze 应用

1. 打开 **Analyze**，选择 **工具 → 导入 KNIME 工作流**。
2. 在**导入源和目标**下，选择**目标项目**以及文档账户中的 **KNIME 存档（.knwf 或 .knar）**。选择**浏览**可从您的计算机上传存档。
3. 在**对象前缀**下，可选择设置**工作流前缀**、**步骤前缀**和**表前缀**。表前缀默认为工作流的名称。
4. 在**源绑定（可选）** 下，可选择将读取器绑定到目标项目中的现有表：选择**添加**，然后输入 **KNIME 读取器**（其节点 ID，例如 `12:3`、其节点名称或其文件名）和**表ID**。若要绑定连接、文档或其他项目中的表，请使用 REST API 或 MCP 工具。参见[绑定源](#绑定源)。
5. 选择**导入**。

窗口会在转换存档时显示进度，然后显示转换报告：步骤数量（**步骤**、**高置信度**、**中**、**低**和**未转换**）、无法转换的节点及其下游步骤、部分转换、警告、需要上传的源文件，以及没有对应步骤的节点。没有需要审核内容的转换会如实说明，窗口会自动关闭。

### 字段

| 字段 | 必填 | 作用 |
| --- | --- | --- |
| `source_account_id` | 是 | 保存 KNIME 存档的文档账户。 |
| `source_file_path` | 是 | `.knwf` 或 `.knar` 文件在该账户中的路径。 |
| `project_id` | 是 | 创建工作流的项目。 |
| `workflow_prefix` | 否 | 添加到工作流名称的前缀。 |
| `step_prefix` | 否 | 添加到步骤名称的前缀。 |
| `table_prefix` | 否 | 添加到表名称的前缀。默认为工作流自身的名称。会重用现有表名称的前缀在创建任何内容之前就会被拒绝。对于 `.knar`，每个工作流的前缀后面会跟着该工作流的名称。 |
| `source_bindings` | 否 | 将读取器和连接器节点绑定到您已有的数据和连接，最多 500 项。参见[绑定源](#绑定源)。 |

### REST

将这些字段作为 JSON 请求体发送到：

```text
POST /rest/v1/analyze/knime/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/knime/monthly-close.knwf",
  "project_id": "<project id>"
}
```

### MCP

连接 MCP 的 AI 代理使用相同的字段调用 `knime_convert` 工具。连接代理的方法请参见 [AI 代理（MCP）](/zh-cn/integrations/ai-coding-agents/)。该工具会更改您的项目，因此请在批准之前审核调用。

## 绑定源

使用 `source_bindings` 将 KNIME 读取器指向 PlaidCloud 中已有的数据，而不是存档中的副本。键可以是节点 ID（例如 `12:3`）、节点名称、打包的文件路径（例如 `data/sales.csv`）或文件名，按此顺序匹配，第一个匹配的生效。值为下列之一：

- 目标项目中某个表的 `analyzetable_` ID。该表会替代读取器。
- `{"project": "<project id>", "table": "<table id>"}`，用于您可以读取的其他项目中的表。读取器会变为复制该表的 [Import Project Table](/zh-cn/reference/workflow-steps/import/import-project-table/) 步骤。源项目必须向目标项目共享读取权限，否则该步骤会发出警告。受行访问权限管控的表会被拒绝。
- `{"account": "<document account id>", "path": "/finance/budget.xlsx"}`，用于您可以读取的文档。读取器会导入它。
- `{"connection": "<connection id>"}`，用于数据库或 REST 连接器节点。转换后的步骤在该连接上运行。

Analyze 应用窗口通过表 ID 将读取器绑定到目标项目中的表。若要绑定连接、文档和其他项目中的表，请通过 REST API 或 MCP 工具进行。

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "data/budget.xlsx": { "account": "<document account id>", "path": "/finance/budget.xlsx" }
}
```

不存在的绑定表，或与任何读取器都不匹配的键，会产生警告。已应用的绑定及其项目和表名称会列在转换报告的 `bindings` 下。

### 未绑定的输入

文件不在存档中的读取器，会从默认文档账户中该工作流文件夹内的 `inputs/<file name>` 读取，转换报告会在 `missing_inputs` 下列出该路径并附带警告。请将文件上传到该处，然后运行工作流。在文件就位之前，导入会以警告结束并创建一个空表，工作流会继续运行。

## 凭据和连接

KNIME 凭据绝不会被迁移。每个登录到其他系统的步骤，都会从您设置的 PlaidCloud 连接或项目变量中读取其凭据，转换报告中该步骤的警告会指明是哪一个。

| KNIME | 需要设置的内容 |
| --- | --- |
| 数据库连接器 | 数据库连接：使用 `{"connection": "<id>"}` 绑定，或在步骤上选择。 |
| 需要登录的 REST 和 Web 服务节点 | [REST 连接](/zh-cn/reference/connectors/rest/generic-rest/)：使用 `{"connection": "<id>"}` 绑定，或在步骤上选择。 |
| Speech Recognizer (IBM Watson) | 基础 URL 为警告中所指明的 Watson 服务 URL 的 REST 连接，以用户 `apikey` 和您的 API 密钥作为其基本登录信息。将其绑定到该节点。 |
| Email Connector，以及 Email Reader 或 Email Mover | 保存邮件服务器密码的项目变量，名称由警告给出。主机和用户来自 Email Connector。 |
| 带工作簿密码的 Excel Reader 或 Excel Writer | 保存密码的项目变量，名称由警告给出。 |
| LLM 连接器和认证器 | AI 步骤上的 LLM 连接。 |

设置项目变量的方法，请参见[管理工作流变量](/zh-cn/guides/workflows/manage-workflow-variables/)。

## 阅读转换报告

导入完成后，Analyze 应用窗口会显示转换报告，REST 和 MCP 响应中也包含它。请在运行工作流之前阅读它。

- `summary` 统计已创建的步骤数，以及有多少步骤以高、中、低置信度完成映射。
- `warnings` 列出每个警告及其节点、步骤和应采取的操作，包括每个需要设置的凭据或连接。
- `missing_inputs` 列出未绑定输入应上传文件的文档路径。
- `bindings` 列出已应用的绑定。
- `table_prefix` 是所使用的前缀。对于 `.knar`，`workflows` 会列出每个工作流及其各自的前缀。
- `uploaded_files` 位于报告旁边，列出上传到默认文档账户的打包文件。
- `dropped_tools` 列出被丢弃的视图和图表。

## 占位符

没有转换路径的节点会作为命名的占位符保留在画布上。占位符会原样传递其数据，并以 KNIME 节点的名称发出警告，其下游的每个步骤都会在报告中被标记，因此缺失的结果绝不会悄无声息。当其结果重要时，请使用标准步骤重建该功能。

## 运行转换后的工作流

1. 在项目中打开新的工作流。
2. 设置警告中指明的项目变量和连接。
3. 将未绑定输入的文件上传到窗口中**需要上传的源文件**下的路径，或 `missing_inputs` 中的路径。
4. [运行工作流](/zh-cn/guides/workflows/run-a-workflow/)，并审核每个步骤的输出表。

## 边界情况

这些是与 KNIME 之间仅有的已知差异。

- **Crosstab。** 转换为 [Table: Pivot](/zh-cn/reference/workflow-steps/tables/table-pivot/) 步骤。少数设置组合给出的结果与 KNIME 不同。
- **Loop End (Column Append)。** 转换为[表：内联接](/zh-cn/reference/workflow-steps/tables/table-inner-join/)步骤。少数设置组合给出的结果与 KNIME 不同。
- **随机抽取。** Row Sampler、Table Partitioner 和 Equal Size Sampling 使用 [Table: KNIME Random Sample](/zh-cn/reference/workflow-steps/tables/table-knime-random-sample/) 步骤执行 KNIME 自身的随机抽取，因此带种子的节点选出的行与 KNIME 中相同。该抽取处理的表最多 10,000,000 行；更大的表会使该步骤失败。

## 相关指南

- [KNIME 转换矩阵](/zh-cn/reference/knime-conversion-matrix/)
- [REST 连接](/zh-cn/reference/connectors/rest/generic-rest/)
- [添加文档账户](/zh-cn/guides/documents/adding-accounts/)
- [管理工作流变量](/zh-cn/guides/workflows/manage-workflow-variables/)
- [运行工作流](/zh-cn/guides/workflows/run-a-workflow/)
