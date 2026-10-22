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
- Each Prophecy job or SQL pipeline schedule becomes a [scheduled event](/administration/scheduled-events/) on the converted workflow, enabled when it is enabled in Prophecy. See [Schedules](#services-and-control).
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
| `connection:<name>` | The Prophecy connection a gem or database dataset names. One binding serves every gem on that connection. A gem that names no connection uses `connection:<pipeline>/<gem id>`, and a database dataset uses `connection:<dataset name>`. | A PlaidCloud connection id: a database connection (BigQuery and SAP HANA included), a MongoDB or Apache Kafka connection, a Salesforce connection for Salesforce reads and writes, a Tableau connection for a Tableau gem, a REST connection for Azure Cosmos DB, Pinecone, Power BI, and Smartsheet and Slack writes, or a Singer-backed connection for Smartsheet, Slack, and Iceberg reads. A Document account id for a File Storage or Directory gem. |
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

Every step that carries project code gets a warning, and so does translated SQL. Review the code in each such step before you run the workflow. The converter withholds anything credential-like it finds in code strings and comments, so add credentials to a connection and not to the code.

## Placeholders for Unconverted Gems

A gem the converter can't reproduce is created as a placeholder step that carries the gem's name. Examples are a Custom Gem, whose Gem Builder code is not part of the export, and a gem that changes data outside the conversion, such as a REST request that can change data, an Email, or a table or file operation, when you haven't bound its `operation:` key. A database dataset or External Table with no connection bound is not a placeholder: it converts to a step that waits for you to select a connection. By default a placeholder fails when the workflow reaches it, so a run can't report success on work that never happened.

Set `allow_unconverted_placeholders` to `true` (in the window, **Import unconverted components as pass-through placeholders**) to import each placeholder as a pass-through step instead. The run then continues past it and the placeholder's output is its input. The report counts the pass-through placeholders and lists their steps. Rebuild the capability with a native step when its result matters.

## Run the Converted Workflows

1. Open the new workflows in the project. The report lists them in run order.
2. Set any project variables that came from Prophecy parameters.
3. Upload files for unbound datasets to the paths in the report.
4. Review the steps that carry project code.
5. Run the workflows and review each step's output table.

Scheduled events created from Prophecy schedules are enabled when they were enabled in Prophecy, so they start running the converted workflows on their schedule. To review the workflows first, disable the events in [Scheduled Events](/administration/scheduled-events/) and enable them when you are ready.

## What Converts

Prophecy gems convert to native steps, project variables, scheduled events, or canvas objects. Nearly every gem converts fully, with every option it offers. The few exceptions are listed under [Partial Conversions](#partial-conversions) and [Placeholders](#settings-that-become-placeholders), and the conversion report names each one where it occurs. The [Prophecy Conversion Matrix](/reference/prophecy-conversion-matrix/) lists every gem with the PlaidCloud step it becomes.

Each gem has a status:

- **Full**: the gem converts to a valid mapping that is expected to run its function. Nearly every gem is Full.
- **Partial**: the gem converts and runs for its common use, and one mode, named below, isn't reproduced. Partial gems are Bedrock, SageMaker Endpoint, and Directory.
- **Not supported**: no conversion path. Only a Custom Gem, whose Gem Builder code isn't part of the export, is Not supported.

### Data Movement

| Capability | How it converts |
| --- | --- |
| Write modes | Target write modes convert to platform steps: SCD2 with the check and timestamp strategies (the timestamp strategy dates each version from the column the gem's `scd2.updatedAtColumn` names), merge, `replaceWhere`, and `insertInto`. A merge applies the per-column SET expressions of its matched-update and not-matched-insert clauses; a clause that sets no column takes every column from the incoming row. A first run onto an empty target writes every row, as dbt and Delta do. The first run needs no table made ahead, including for a pipeline that reads a dataset it also writes, unless the export doesn't say what columns that dataset has: then create the table before the first run. Later runs apply the incremental filter or merge condition. The `error` and `ignore` modes check with the [table exists condition](/guides/workflows/step-conditions/#table-exists-conditions). |
| Time travel | A Delta or catalog table source that reads an earlier version of its table, by `versionAsOf` or `timestampAsOf`, reads that version from Databricks through the connection you bind. |
| Streaming | Streaming sources and targets run as scheduled batch. The streaming sink replaces its table rather than appending, so a re-run never duplicates rows. Schedule the workflow to pick up newly arrived data. |
| Databases | JDBC, Snowflake, Redshift, Hive, BigQuery, SAP HANA, and External Table gems read and write through the PlaidCloud connection you bind. A BigQuery dataset reads with [Import SQL](/reference/workflow-steps/import/import-sql/) and writes with [Export External Database Tables](/reference/workflow-steps/export/export-external-tables/) on a [BigQuery connection](/reference/connectors/google/big-query/). A SAP HANA table written in any of the HANA gem's merge modes, SCD2 and the delete modes included, is staged beside the target and merged into it on the target's primary key or the gem's merge columns; a missing target is created first. |
| MongoDB and Kafka | A MongoDB dataset reads with [Import MongoDB](/reference/workflow-steps/import/import-mongodb/), its filter or aggregation pipeline included, and a read that declares no columns takes them from the first documents, as the Spark connector does. A write uses [Export MongoDB](/reference/workflow-steps/export/export-mongodb/) in the matching write mode: `update` updates the fields of the matching document or inserts one, `ignore` writes only while the collection holds no document, and `error` stops the run when it holds one. A Kafka source reads its topics between the starting and ending offsets with [Import Kafka](/reference/workflow-steps/import/import-kafka/), and a Kafka target sends each row with [Export Kafka](/reference/workflow-steps/export/export-kafka/). A Kafka dataset that signs in with `OAUTHBEARER` uses the [OAuth sign-in](/reference/connectors/databases/apache-kafka/#oauth-oauthbearer) of the Kafka connection you bind, because the export carries no credentials. |
| Azure Cosmos DB | A read sends the dataset's query, or reads every document, with [REST Request](/reference/workflow-steps/general/rest-request/) on a REST connection with Cosmos DB authentication, and follows the continuation header from page to page. A write sends one request for each row by the gem's write strategy: overwrite, append, delete, or patch. A row that carries its document's ETag is replaced or deleted only if the document hasn't changed since, and a row the container refuses for that reason, or for a missing or existing document, is skipped, as the Spark connector does. The `ignore` mode writes only while the container holds no document. |
| Salesforce | A read uses [Salesforce: Query Object](/reference/workflow-steps/salesforce/query-salesforce-object/), deleted and archived records included when the gem asks for them. A write inserts, updates, upserts, or deletes, with one request for each row; an upsert matches on the gem's external id field, `Id` when it names none. |
| Smartsheet, Slack, and Pinecone | A Smartsheet read of a named sheet with declared columns fetches the sheet through your REST connection and lands a row for each sheet row, a column for each declared column. Other Smartsheet reads, and Slack and Iceberg reads, use [Import Singer Source](/reference/workflow-steps/import/import-singer/). A Smartsheet write adds the rows to the named sheet, and an overwrite deletes the sheet's rows first. A Slack write posts one message for each row, and a message Slack refuses fails the step. A Pinecone index reads as its vectors and their metadata, and a write upserts the rows as vectors. |
| Tableau and Power BI | Tableau and Tableau Write publish the input as a Hyper extract through [Publish to Tableau](/reference/workflow-steps/export/export-to-tableau/) on the Tableau connection you bind. Power BI Write pushes the inputs to a Power BI push dataset through a REST connection with OAuth 2.0, finding the workspace by name and creating the dataset when it is new. |
| File formats | CSV, JSON, Parquet, Avro, Excel, XML, fixed-width, and ORC through [Import ORC](/reference/workflow-steps/import/import-orc/). Format options are mapped, or marked neutral when they change no row: an Avro read's modified-time window, a fixed-width file's EBCDIC encoding, header and footer records and records with no line breaks, an Excel read's sheet map and password, the quote options of a CSV write, and an Excel write with one sheet for each value. Compressed text files read and write with gzip, Deflate (zlib), Zstandard, LZ4, Snappy, and LZO; a compressed file is read when its name ends in its codec's extension. Encrypted files are decrypted and encrypted in place. See [Encrypted Files](#encrypted-files). |
| File Operation | Copy and Move convert to [Document: Copy File](/reference/workflow-steps/document/copy-document-file/) or Copy Directory on the folder you bind, keeping only the files whose name matches the gem's `filenameRegex`, and keeping each file's path below the source folder when the gem recurses. |

### Columns and Rows

| Gem or function | How it converts |
| --- | --- |
| Surrogate Key | Keys continue from a table that keeps the last key issued, as the gem's key file does. Every gem that names the same key file shares that table, so their keys never overlap. A run with no rows leaves it as it was, and keys start from the initial value before any run has issued one. |
| Column Parser, XML Parse, JSON parsing | XML and JSON text parses with the [XML Parse](/reference/workflow-steps/tables/table-xml-parse/) and [JSON Parse](/reference/workflow-steps/tables/table-json-parse/) steps, reading each field from the element's text, an attribute, or a child element. XML parsed without a schema takes each field's type from the data, as Spark's `schema_of_xml` does. |
| Business rules | A project business rule called in an expression converts to the same conditions, one `CASE` for each column it sets. |
| Casts | A cast of text to a decimal or a long follows Spark exactly: spaces and control characters around the number are trimmed, a decimal rounds half up to its scale, and text that isn't a number, or a value out of range, is null. |
| Dates and times | Date and time formats are written for your workspace's engine, Databend included, and `window()` places each timestamp in its tumbling window, aligned as Spark aligns it. |
| Iterator outputs | A Table Iterator or While Iterator whose output columns are known only at run time gathers each pass's rows by position with [Table: Union All](/reference/workflow-steps/tables/table-union-all/#column-matching), each column widened to a type every pass fits, as Prophecy stacks the passes. |
| Data Encoder/Decoder AES | Runs on every engine. The key, and the initialization vector and additional data when the gem names them, come from the workflow variables `aes_key`, `aes_iv`, and `aes_aad`, which you set. |
| Data Masking hash | Computes the same values as Spark's `hash()`. |
| Buffer, Simplify, Heat Map | Buffer draws a rounded corner with the same number of segments Prophecy does, Simplify drops the same vertices, and Heat Map sums heat into H3 hexagons at the gem's resolution. |

### Services and Control

| Gem | How it converts |
| --- | --- |
| Pipeline | Runs the pipeline it names with a [Workflow Loop](/reference/workflow-steps/workflow-control/workflow-loop/), once for each input row (once when it has no input, never for no rows), with each parameter set from a constant, a column of the row, or an expression over it. Every run goes ahead even when an earlier one fails, and the gem's output has one row for each run with its status, message, and times, as Prophecy records them. |
| Schedules | A Prophecy job or SQL pipeline schedule becomes a [scheduled event](/administration/scheduled-events/) named `Prophecy <name>` on the converted workflow, enabled unless it is disabled in Prophecy. A Spark job converts this way when it runs one converted pipeline with no configuration overrides or run conditions. |
| Script | A Python script is placed in a Python step. A value the script sets on `Config` becomes a workflow variable that later steps read, reset to the pipeline's value at the start of each run, as Prophecy's `Config` is. |
| REST API, REST API Enrich | [REST Request](/reference/workflow-steps/general/rest-request/) steps, one request for each input row, keeping an error response as Prophecy does. Enrich also reads the status, reason, and final URL. A request that waits for an asynchronous result polls until the response says it is done. |
| Stored Procedure | A gem that passes arguments calls its procedure with [Remote Execute: SQL](/reference/workflow-steps/agent/agent-remote-execution-of-sql/#run-a-statement-once-per-row) once for each input row, each argument bound from its column as a parameter. A gem with no arguments calls it once through an Agent. Choose the connection or agent on the converted step. |
| Email, Email Data | [Notify Via Email](/reference/workflow-steps/notifications/notify-via-email/) with Cc, Bcc, Reply-To, and one message for each row when a field reads from a column. |
| OpenAI, Bedrock, SageMaker Endpoint | [Text: NLP (AI)](/reference/workflow-steps/text-documents/nlp-ai/) on your workspace's LLM connection. OpenAI and Bedrock embeddings use the Embed task, which needs an OpenAI-compatible or Azure OpenAI connection; an Anthropic connection is refused. |
| Pinecone Lookup | A REST request for each row. |
| Data Quality Check, Deequ, Soda | The checks run in the warehouse and write the results table. A Data Quality Check stops the run only when the gem sets `minFailedChecks` or a `fail_pipeline` post action; otherwise the results table lists the failures. Deequ and Soda never stop the run. A minimum or maximum length check on a numeric column measures the number as text. |
| ToDo | Raises an error that names the original tool and message when the run reaches it. |

### Encrypted Files

A File Storage gem that reads an encrypted file converts to [Document: Decrypt File](/reference/workflow-steps/document/encrypt-decrypt-file/), which decrypts the file into a folder of its own before the import reads it; the decrypted copy is removed afterwards. A gem that writes an encrypted file exports into that folder and then encrypts the file into place with Document: Encrypt File. AES and Blowfish files and password-protected Excel workbooks are covered.

The export never carries a key, so the converted steps read it from a workflow variable: `aes_key` for an AES or Blowfish key, and `xlsx_password` for a workbook password. Set the variable before you run the workflow, and give it a key meant for these files only. Key and password fields take only a variable reference, so a key is never typed into a step.

### Partial Conversions

| Gem or option | What isn't reproduced |
| --- | --- |
| Bedrock, SageMaker Endpoint | Answers and embeddings come from your workspace's LLM connection, not the Bedrock or SageMaker model, so they differ from Prophecy's. A SageMaker endpoint's name, token limit, and `top_p` aren't applied, and a gem that names no text, question, or context column stops the run. |
| Directory | A listing of Smartsheet or another store with no Document account lists the same path in the conversion's Document account instead, and `include_sheet_name` isn't applied. |
| File Operation Sync | Copies the files, but doesn't remove destination files the source no longer has. |
| Table restore by version | Restoring a Delta table to a version number does nothing, because PlaidCloud restores a table to a point in time. A restore to a timestamp converts. |
| Schedules | A cron with a seconds or year field, or with `L`, `W`, or `#`, isn't applied, nor is a time zone that isn't a whole-hour offset. A zone whose daylight saving differs from the scheduled event's region runs at its standard offset. More than one concurrent run becomes unlimited concurrency, and email alerts aren't applied. |
| Job components | In a Spark job, components other than its one pipeline, and run conditions and configuration overrides, aren't converted. A SQL orchestration pipeline's Dataset, Model, Orchestration Target, Run Stored Procedure, and Script components in a job aren't converted. |
| `input_file_name()` | The converted step reads a table, so the file each row came from isn't known, and the function returns an empty string. |
| Spark hash functions | `hash()` and `xxhash64()` in an expression use Murmur3 and XXH64 with seed 42, which no warehouse has, so the converted values differ. |
| Ab Initio components | Assign Keys, Compare Records, Error Detection, and MTime work by a rule the export doesn't carry: the first output passes the input through unchanged and any other output is empty. |
| Unsafe parameter values | A parameter value holding a quote, backslash, or brace isn't put into an expression; the step that reads it becomes a placeholder. |
| Rare source options | A few options whose exported form isn't documented convert in part, and the report names each: a Kafka source's Kerberos (`GSSAPI`) sign-in, a Salesforce SAQL query or Wave dataset read through a dataset, a DataHub table's `replaceWhere`, Data Generator providers with no PlaidCloud equivalent, Upload Files' multi-table extraction, a REST response that Prophecy flattens into columns, and the schema REST Enrich infers for parsed content. |
| XML export of timestamps and doubles | A timestamp or double column is written as the warehouse formats it as text, not in Spark's form (ISO-8601 with `T` and the offset for a timestamp, Java's notation for a double). |
| XML string field with child elements | A string field whose element holds child elements reads as their JSON, where Spark reads their XML. |
| Sliding windows | `window()` with a slide shorter than its duration puts a row in several windows, which no single value can hold, so the step that uses it doesn't convert. |

The converter also reports these known divergences on the step they affect:

- A Join with two output columns of the same name renames the later one, because a table can't hold both.
- A `struct` value reads as a tuple without field names.
- `encode` to ISO-8859-1 returns the text, not its bytes.
- A CSV written in a character set with no codec is written in UTF-8.
- A Bulk Column Expressions gem with no selected column applies to no column.
- A Salesforce insert doesn't send the table's `Id` column, because Salesforce assigns the Id of each record it creates.
- A Heat Map sums a decimal heat column as a double.

### Settings That Become Placeholders

A gem setting that Prophecy itself can't run converts to a placeholder step that names the reason: a Custom Gem, a Script in Scala or with no code, a SQL Statement with no query, a File Operation with no source or destination, a spatial gem or Fuzzy Match with no column to work on, a window frame that runs backwards, a method-style call such as `x.f()` in a SQL expression, and the Ab Initio Create Data component, whose record format isn't in the export.

## Known Limitations

- Conversion is one-time. Re-importing a project creates new workflows and tables.
- Project code is carried over, not run or ported. Spark-specific code needs porting before it runs.

## Related Guides

- [Migrate Savant Analyses](/guides/workflows/migrate-savant-analyses/)
- [Migrate Alteryx Workflows](/guides/workflows/migrate-alteryx-workflows/)
- [Add Document Accounts](/guides/documents/adding-accounts/)
- [Manage Workflow Variables](/guides/workflows/manage-workflow-variables/)
- [Run a Workflow](/guides/workflows/run-a-workflow/)
