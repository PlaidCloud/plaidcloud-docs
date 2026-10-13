---
title: Migrate Prophecy Projects
description: Convert a Prophecy project export into PlaidCloud workflows from the Analyze app, the REST API, or an MCP-connected AI agent, bind its datasets and connections, and read the conversion report.
sidebar:
  order: 31.5
---

PlaidCloud converts a Prophecy project into runnable workflows. The converter creates one workflow for each Spark pipeline and one for the SQL project, maps each Prophecy gem to a workflow step, a project variable, or a canvas object, keeps the original graph, and returns a conversion report that names anything it could not convert.

Conversion reads only the export you point it at. It never contacts the system a Prophecy dataset reads from or writes to, and it never runs project code.

Conversion is a one-time step. Converting the same project again creates new workflows and tables, and edits you made in PlaidCloud are never merged with a later export.

## What PlaidCloud Creates

- Each Prophecy gem becomes the matching workflow step, with upstream and downstream relationships preserved.
- Prophecy parameters become project variables, and references to them inside gem settings are rewritten to the PlaidCloud variable syntax. You can override parameter values at conversion.
- Each dataset a gem reads becomes an import step, or reads an existing table or document, depending on how you bind it.
- Scripts, SQL statements, macros, and other project code arrive inside steps that carry the code. See [Project Code in Steps](#project-code-in-steps).
- A gem with no PlaidCloud equivalent arrives as a named placeholder step. See [Placeholders for Unconverted Gems](#placeholders-for-unconverted-gems).
- Expressions are converted assuming Spark SQL behavior for null handling, integer division, and implicit casts. Check results where those differ on your PlaidCloud engine.

## Before You Start

1. Export the project from Prophecy as a `.zip` file, or export a single pipeline, model, or subgraph as a `.json` file.
2. Upload the file to a [Document account](/guides/documents/adding-accounts/) you can read.
3. Choose the PlaidCloud project that should receive the workflows. You need write access to it.
4. Decide where files for unbound datasets are read from. Choose a Document account and a base folder.

## Convert the Project

Convert from the Analyze app, the REST API, or the MCP tool catalog. All three take the same fields.

### Analyze App

1. Open **Analyze** and choose **Tools → Import Prophecy Project**.
2. Choose the **Target Project**, the **Prophecy Project (.zip or .json)** you uploaded to a Document account, and the **Source Files Location**, the Document account and base folder where files for unbound datasets are read from.
3. Under **Object Names and Options**, optionally set workflow, step, and table prefixes, choose the **Workflow Type**, and choose whether to import unconverted components as pass-through placeholders.
4. Under **Source Bindings and Parameters**, optionally bind a dataset to an existing table by entering the dataset name and the table ID, and override Prophecy parameters by name. To bind connections, use the REST API or the MCP tool. See [Bind Connections](#bind-connections).
5. Select **Import**.

The window shows progress as it reads the project, parses the pipelines, maps them to PlaidCloud operations, and creates the workflows, tables, and steps. When it finishes, the window shows the conversion report: step counts by confidence, warnings, partial conversions, unconverted placeholders, dropped components, and the source files to upload.

### Fields

The REST API and MCP tool take these fields.

| Field | Required | What it does |
| --- | --- | --- |
| `source_account_id` | Yes | Document account that holds the Prophecy export. |
| `source_file_path` | Yes | Path of the project `.zip`, or of one pipeline, model, or subgraph `.json` file, within that account. |
| `project_id` | Yes | Project where the workflows are created. |
| `document_account_id` | Yes | Document account that unbound datasets read from. |
| `document_account_path` | Yes | Base folder in that account for unbound datasets. An empty value or `/` is the account root, and a leading `/` is ignored. Paths with `..` or dot-led segments, braces, a drive letter or URL scheme, or control characters are refused. |
| `workflow_prefix` | No | Prefix added to workflow names. |
| `step_prefix` | No | Prefix added to step names. |
| `table_prefix` | No | Prefix added to table names. Defaults to the workflow's own name. A prefix that would reuse an existing table name is refused before anything is created. The prefix used is returned in the conversion report. |
| `workflow_type` | No | `advanced` (default) lays the graph onto the DAG canvas. `standard` produces a serial step list. |
| `source_bindings` | No | Binds datasets and operations to existing data. See [Bind Sources](#bind-sources). |
| `connection_bindings` | No | Binds the databases, file stores, REST APIs and email a project reaches to PlaidCloud connections and Document accounts. See [Bind Connections](#bind-connections). |
| `parameters` | No | Overrides Prophecy parameters. See [Parameters](#parameters). |
| `allow_unconverted_placeholders` | No | Controls what a placeholder does at run time. See [Placeholders for Unconverted Gems](#placeholders-for-unconverted-gems). |

### REST

Send the fields as a JSON body to:

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

You need the `analyze.workflow.write` role.

### MCP

An MCP-connected AI agent calls the `prophecy_convert` tool with the same fields. See [AI Agents (MCP)](/integrations/ai-coding-agents/) to connect an agent. The tool changes your project, so review the call before you approve it.

## Bind Sources

A Prophecy export describes where its data comes from but carries no data and no credentials. Use `source_bindings` to connect each dataset to data you already have in PlaidCloud. A key is the dataset name as the conversion report lists it. A value is either:

- An `analyzetable_` id for a table in the target project. The converted workflow reads that table directly.
- An object with `account`, `path`, and optionally `sheet`, to read a file from a Document account.

```json
"source_bindings": {
  "customers": "analyzetable_1234",
  "budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

A binding you can't read is refused. A key that matches no dataset is reported as a warning. The Analyze window binds datasets to tables; use the REST API or MCP tool to bind a dataset to a Document file.

### Unbound Datasets

A dataset with no binding becomes an import step with no data yet, and the conversion report carries a warning for it. The step reads from:

```text
<document_account_path>/prophecy/<workflow id>/<dataset name>.csv
```

Upload the file to that path and run the workflow. Until the file is there, the import step finishes with a warning and creates an empty table, and the workflow continues. The report lists each path under **Source files to upload**.

### Bind Table and File Operations

Gems that change tables or files, such as Table Operations (update, delete, drop) and File Operation (copy), act only on data the conversion created. To let one work on data that already exists, bind it with a key of the form `operation:<pipeline>/<id>`, where `<pipeline>` is the pipeline's name and `<id>` is the gem's id. The conversion report names the key for each such gem.

```json
"source_bindings": {
  "operation:daily_load/Operation_1": "analyzetable_5678"
}
```

A destructive table or file operation runs only when you bind it. Without a binding, a Table Operations gem works on a table written by another gem of the same project, and otherwise becomes a placeholder that names its key. A File Operation copies from its own staging folder. Nothing outside the conversion's own tables and folders is changed unless you bind it.

## Bind Connections

A Prophecy project reaches databases, file stores, REST APIs and mail servers through connections. The export carries the connection names but no credentials, so use `connection_bindings` to point each one at a PlaidCloud connection or Document account you already have. The conversion report lists every key under its bindings.

```json
"connection_bindings": {
  "connection:warehouse_pg": "<connection id>",
  "connection:landing_s3": "<document account id>",
  "operation:daily_load/Email_1": "<connection id>"
}
```

A key is one of:

| Key | Binds | Value |
| --- | --- | --- |
| `connection:<name>` | The Prophecy connection a gem or database dataset names. One binding serves every gem on that connection. A gem that names no connection uses `connection:<pipeline>/<gem id>`, and a database dataset uses `connection:<dataset name>`. | A PlaidCloud connection id for a database or Singer-backed store. A Document account id for a File Storage or Directory gem. |
| `operation:<pipeline>/<gem id>` | A REST gem that sends anything but GET, HEAD, or OPTIONS, and every Email gem. | A connection id. For REST, a REST connection that holds the credential. |

The binding is your consent for gems that change things outside the conversion:

- A REST request that can change what the API holds, and an email that reaches real people, convert to working steps only when you bind their `operation:` key. Unbound, the gem is a placeholder that names the key.
- A Document account bound to a File Storage or Directory gem lets that gem's steps write, delete, or move files in that account.
- A GET, HEAD, or OPTIONS request goes out as the gem sends it. Unbound, it has no credential until you select a REST connection on the converted step.

A database dataset or External Table gem with no binding converts to a step that names its key and waits for you to select a connection, and the report carries a warning. Re-convert with the key bound, or select the connection on the step. A binding whose id is the wrong kind of store for its gems, or that you can't use, is refused. A key that matches nothing is reported as a warning.

## Parameters

`parameters` overrides Prophecy parameters at conversion:

```json
"parameters": {
  "instance": "prod",
  "values": { "run_date": "2026-10-01", "region": "EMEA" },
  "pipelines": {
    "daily_load": { "instance": "prod", "values": { "region": "APAC" } }
  }
}
```

`instance` names a configuration instance. `values` are text, numbers, or booleans. A pipeline entry overrides the project-wide values for that pipeline. The report lists the parameters used and any that were renamed to fit PlaidCloud variable names.

## Read the Conversion Report

The response carries the conversion report. Read it before you run the workflows.

| Section | What it tells you |
| --- | --- |
| Summary | How many steps converted with high, medium, or low confidence, and how many did not convert. |
| Warnings | Everything the converter assumed, approximated, or skipped, including unbound datasets and binding keys that matched nothing. |
| Partial conversions | Steps that convert but differ from the gem in some mode or option. Each carries a note on what to check. |
| Unconverted placeholders | Gems with no PlaidCloud equivalent, with the reason. |
| Dropped components | Gems that carry no work of their own, such as control-flow boundary markers, and the step that absorbed each. |
| Source files to upload | The Document path each unbound dataset reads from. |
| Workflows | The workflow created for each pipeline, in run order. A pipeline the converter refused is marked. |

The report also names the table prefix used and the parameters applied. A step the converter is not sure about is converted to the most likely reading and carries a note in the report. Check those steps against your Prophecy output.

## Project Code in Steps

Prophecy projects carry code: Script gems, SQL statements, macros, dynamic inputs, stored procedure calls, and custom gems. The converter doesn't run that code. It places it inside a step:

- SQL is translated to your tenant's SQL dialect and placed in a SQL step, with the gem's inputs available under the names the query reads them by.
- Python scripts are placed in a Python step, with table access rewritten. A script that calls Spark data frame methods keeps those calls, and the report notes that you must port them to pandas.
- A macro from a known dbt package becomes the standard steps that do what the macro does.

Every step that carries project code reports `W_PROJECT_CODE_EMBEDDED`, and translated SQL reports `W_DIALECT_TRANSLATED`. Review the code in each such step before you run the workflow. The converter withholds anything credential-like it finds in code strings and comments, so add credentials to a connection and not to the code.

## Placeholders for Unconverted Gems

A gem the converter can't reproduce is created as a placeholder step that carries the gem's name. Examples are a Custom Gem, whose Gem Builder code is not part of the export, Heat Map, whose H3 cells no PlaidCloud step computes, and a gem that changes data outside the conversion, such as a REST request that can change data, an Email, or a table or file operation, when you haven't bound its `operation:` key. A database dataset or External Table with no connection bound is not a placeholder: it converts to a step that waits for you to select a connection. By default a placeholder fails when the workflow reaches it, so a run can't report success on work that never happened.

Set `allow_unconverted_placeholders` to `true` (in the window, **Import unconverted components as pass-through placeholders**) to import each placeholder as a pass-through step instead. The run then continues past it and the placeholder's output is its input. The report counts the pass-through placeholders and lists their steps. Rebuild the capability with a native step when its result matters.

## Run the Converted Workflows

1. Open the new workflows in the project. The report lists them in run order.
2. Set any project variables that came from Prophecy parameters.
3. Upload files for unbound datasets to the paths in the report.
4. Review the steps that carry project code.
5. Run the workflows and review each step's output table.

## What Converts

Prophecy gems convert to native steps, project variables, or canvas objects. A few have no PlaidCloud equivalent and arrive as placeholders. The converter measures itself against each gem's configuration options, not against whole projects, and reports what it can't reproduce in the conversion report.

Each gem has a mapping tier:

- **Full**: every option of the gem has a valid mapping to a PlaidCloud step.
- **Partial**: the gem converts, and the option named below has no mapping. The conversion report names it.

### Data Movement

| Capability | How it converts |
| --- | --- |
| Write modes | Target write modes convert to platform steps: SCD2 with the check and timestamp strategies (the timestamp strategy dates each version from the column the gem's `scd2.updatedAtColumn` names), merge, `replaceWhere`, and `insertInto`. A first run onto an empty target writes every row, as dbt and Delta do. The first run needs no table made ahead, including for a pipeline that reads a dataset it also writes. Later runs apply the incremental filter or merge condition. The `error` and `ignore` modes check with the [table exists condition](/guides/workflows/step-conditions/#table-exists-conditions). |
| Streaming | Streaming sources and targets run as scheduled batch. The streaming sink replaces its table rather than appending, so a re-run never duplicates rows. Schedule the workflow to pick up newly arrived data. |
| Databases | JDBC, Snowflake, Redshift, Hive, and External Table gems read and write through the PlaidCloud connection you bind. |
| Singer-backed stores | MongoDB, Slack, Smartsheet, and Iceberg read through [Import Singer Source](/reference/workflow-steps/import/import-singer/) with their bound connection. |
| File formats | CSV, JSON, Parquet, Avro, Excel, XML, fixed-width (column widths come from the schema), and ORC through [Import ORC](/reference/workflow-steps/import/import-orc/). Format options are mapped, or marked neutral when they change no row. |

### Services and Control

| Gem | How it converts |
| --- | --- |
| REST API, REST API Enrich | [REST Request](/reference/workflow-steps/general/rest-request/) steps, one request for each input row, keeping an error response as Prophecy does. Enrich also reads the status, reason, and final URL. |
| Email, Email Data | [Notify Via Email](/reference/workflow-steps/notifications/notify-via-email/) with Cc, Bcc, Reply-To, and one message for each row when a field reads from a column. |
| OpenAI, Bedrock, SageMaker Endpoint | [Text: NLP (AI)](/reference/workflow-steps/text-documents/nlp-ai/) on your workspace's LLM connection. OpenAI and Bedrock embeddings use the Embed task, which needs an OpenAI-compatible or Azure OpenAI connection; an Anthropic connection is refused. |
| Pinecone Lookup | A REST request for each row. |
| Data Quality Check, Deequ, Soda | The checks run in the warehouse and write the results table. A Data Quality Check stops the run only when the gem sets `minFailedChecks` or a `fail_pipeline` post action; otherwise the results table lists the failures. Deequ and Soda never stop the run. A minimum or maximum length check on a numeric column measures the number as text. |
| ToDo | Raises an error that names the original tool and message when the run reaches it. |

### Partial Conversions

| Gem or option | What has no mapping |
| --- | --- |
| BigQuery datasets | PlaidCloud has no BigQuery SQL driver, so a BigQuery Source or Target can't read or write through a connection. |
| Cosmos DB and Kafka Sources | The Source reads a staged JSON extract of the data, one batch for a Kafka topic. It doesn't connect to the live store. |
| Tableau, Tableau Write, Power BI Write | PlaidCloud publishes to neither. Each input stays a PlaidCloud table and is written as Parquet to the gem's staging folder, and the report says nothing was published. |
| File Storage encryption | The whole-file encryption setting isn't applied. |
| Spark hash functions | `hash()` and `xxhash64()` use Murmur3 and XXH64 with seed 42, which no warehouse has. The converted values differ, as do Data Masking hashes. |
| `regexp_extract_all` | PlaidCloud has no array type, so it returns the first match. |
| Data Encoder/Decoder AES | AES runs on StarRocks lakehouses with the key in the `aes_key` workflow variable. Other engines have no AES function. |
| Buffer and Simplify | Distances are measured in degrees, where Prophecy uses meters. |

The converter also reports these known divergences on the step they affect:

- A Join with two output columns of the same name keeps one, because a table can't hold both.
- A `struct` value reads as a tuple without field names.
- `encode` to ISO-8859-1 returns the text, not its bytes.
- A CSV written in a character set with no codec is written in UTF-8.
- A Bulk Column Expressions gem with no selected column applies to no column.

## Known Limitations

- Conversion is one-time. Re-importing a project creates new workflows and tables.
- Project code is carried over, not run or ported. Spark-specific code needs porting before it runs.

## Related Guides

- [Migrate Savant Analyses](/guides/workflows/migrate-savant-analyses/)
- [Migrate Alteryx Workflows](/guides/workflows/migrate-alteryx-workflows/)
- [Add Document Accounts](/guides/documents/adding-accounts/)
- [Manage Workflow Variables](/guides/workflows/manage-workflow-variables/)
- [Run a Workflow](/guides/workflows/run-a-workflow/)
