---
title: Migrate Savant Analyses
description: Convert a Savant Labs analysis export into a PlaidCloud Advanced workflow from the Analyze app, the REST API, or an MCP-connected AI agent, bind its sources, and read the conversion report.
sidebar:
  order: 31
---

PlaidCloud is a drop-in replacement for Savant. Every Savant agent, expression and setting converts to PlaidCloud and runs. The converter converts a Savant Labs analysis export into a runnable Advanced workflow: it maps each Savant agent to a workflow step, a project variable, or a canvas object, keeps the original graph, and returns a conversion report that names anything it could not convert.

Conversion reads the export file you point it at and the headers of the files you bind to its sources. It never contacts the system a Savant source or destination connects to.

## What PlaidCloud Creates

- Each Savant agent becomes the matching workflow step, with upstream and downstream relationships preserved. The [Savant Conversion Matrix](/reference/savant-conversion-matrix/) lists every agent and its mapping tier.
- Savant analysis parameters become project variables, and references to them inside agent settings are rewritten to the PlaidCloud variable syntax.
- Notes and groups arrive on the canvas as notes and groups.
- Each source becomes an import step, or reads an existing table, depending on how you bind it.
- Every Savant agent type converts in full: each option has a mapping. A configuration Savant itself fails on or doesn't document arrives as a named placeholder step. See [Placeholders for Unconverted Configurations](#placeholders-for-unconverted-configurations).

## Before You Start

1. Export the analysis from Savant with **Export JSON**.
2. Upload the `.json` file to a [Document account](/guides/documents/adding-accounts/) you can read.
3. Choose the PlaidCloud project that should receive the workflow. You need write access to it.
4. Choose a Document account and base folder where the analysis's source files will be read from.

## Convert an Analysis

Convert from the Analyze app, the REST API, or the MCP tool catalog. All three take the same fields.

### Analyze App

1. Open **Analyze** and choose **Tools → Import Savant Analysis**.
2. Choose the **Target Project** and the **Savant Export File (.json)** you uploaded to a Document account.
3. Select **Load Sources**. The window lists each source node in the export.
4. To connect a source to data you already have, select it and choose **Bind…**. Choose **Project table** to read a table in the target project, or **Document** to read a file from a Document account (with an optional worksheet name for Excel). Choose **Unbind** to remove a binding.
5. Under **Unbound Sources Directory**, choose the Document account and base folder where files for unbound sources are read from.
6. Under **Conversion Options**, choose the **Workflow Type** and whether to **Allow unconverted placeholders**. Under **Object Prefixes**, optionally set workflow, step, and table prefixes.
7. Select **Convert**.

When conversion finishes, the window shows the conversion report: the workflow name and table prefix, the warnings, a table of the Document paths to upload files to for unbound sources, and the steps that need review. If the list of sources can't be loaded, add a row for each source with its node id and the `analyzetable_` id of the table to bind.

### Fields

The REST API and MCP tool take these fields.

| Field | Required | What it does |
| --- | --- | --- |
| `source_account_id` | Yes | Document account that holds the Savant export. |
| `source_file_path` | Yes | Path of the export within that account. |
| `project_id` | Yes | Project where the workflow is created. |
| `document_account_id` | Yes | Document account that unbound sources read from. |
| `document_account_path` | Yes | Base folder in that account for unbound sources. An empty value or `/` is the account root, and a leading `/` is ignored. Paths with `..` or dot-led segments, braces, a drive letter or URL scheme, or control characters are refused. |
| `workflow_prefix` | No | Prefix added to workflow names. |
| `step_prefix` | No | Prefix added to step names. |
| `table_prefix` | No | Prefix added to table names. Defaults to the workflow's own name. A prefix that would reuse an existing table name is refused before anything is created. The prefix used is returned in the conversion report. |
| `workflow_type` | No | `advanced` (default) lays the graph onto the DAG canvas. `standard` produces a serial step list. |
| `source_bindings` | No | Binds sources to existing data. See [Bind Sources](#bind-sources). |
| `destination_bindings` | No | Routes destinations to a document account, a connection table, a Google Sheet, a Tableau data source, a Slack channel, or email recipients. REST and MCP only. See [Destinations](#destinations). |
| `api_bindings` | No | Says where an API agent's relative URL goes: a base URL or a REST connection. REST and MCP only. See [Bind API Requests](#bind-api-requests). |
| `allow_unconverted_placeholders` | No | Controls what a placeholder does at run time. See [Placeholders for Unconverted Configurations](#placeholders-for-unconverted-configurations). |

### REST

Send the fields as a JSON body to:

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

To list an export's source nodes before you build `source_bindings`, send `source_account_id` and `source_file_path` to:

```text
POST /rest/v1/analyze/savant/sources
```

Each entry in the response has the source's `node_id`, `name`, and `connector`.

### MCP

An MCP-connected AI agent calls the `savant_convert` tool with the same fields. See [AI Agents (MCP)](/integrations/ai-coding-agents/) to connect an agent. The tool changes your project, so review the call before you approve it.

## Convert-Time Bindings

A Savant export carries no data, no credentials and no connections, so three convert-time parameters connect it to yours. Each is a map from a Savant node id or name to a target, and a binding you can't use refuses the whole conversion before anything is created.

| Parameter | Binds | Section |
| --- | --- | --- |
| `source_bindings` | Source agents to tables or files | [Bind Sources](#bind-sources) |
| `destination_bindings` | Destination agents to a file, table, sheet, Tableau data source, Slack channel, or email | [Destinations](#destinations) |
| `api_bindings` | API agents with a relative URL to a base URL or REST connection | [Bind API Requests](#bind-api-requests) |

## Bind Sources

A Savant export describes where its data comes from but carries no data and no credentials. Use `source_bindings` to connect each source to data you already have in PlaidCloud. A key is the source's node id, dataset id, or name. A value is either:

- An `analyzetable_` id for a table in the target project. The converted workflow reads that table directly.
- An object with `account`, `path`, and optionally `sheet`, to read a file from a Document account.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "Budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

A binding you can't read is refused. A key that matches no source is reported as a warning.

A source file path in the export can start with `/` or run through dot-folders such as `.archive`, and it converts. A source that reads XML converts the XML text, and an XML document source also carries Savant's file-context columns.

### Unbound Sources

A source with no binding becomes an import step with no data yet, and the conversion report carries a warning for it. The step reads from:

```text
<document_account_path>/savant/<workflow id>/<source name>.csv
```

Upload the file to that path and run the workflow. Until the file is there, the import step finishes with a warning and creates an empty table, and the workflow continues.

## How Agents Convert

Most agents convert to the step you would build by hand; the [Savant Conversion Matrix](/reference/savant-conversion-matrix/) lists every agent. These agents need extra care.

| Savant Agent | What It Becomes | Caveats |
| --- | --- | --- |
| Infer Agent (`gen_ai`, and legacy `service` with an LLM service) | An [AI/NLP](/reference/workflow-steps/text-documents/nlp-ai/) step with the **Prompt** task. The prompt runs once per row over the input fields, and the answer lands in an **AI Answer** column beside every input column. A row limit becomes **Max rows**, and an empty source warns and writes an empty table. **Max New Rows** answers only the rows that are new and keeps the answers from earlier runs. | An LLM answers, so output is never byte-identical to Savant's and can vary between runs. Each call has a cost. See [AI Providers](#ai-providers). A batch that fails keeps its rows with an empty answer and warns. |
| Vision Agent (`vision`) | A [Document Read Blob](/reference/workflow-steps/text-documents/document-blob-extract/) step, [Image OCR](/reference/workflow-steps/text-documents/image-ocr/), then the AI/NLP **Prompt** task. Each document goes to the provider as an image or PDF when the provider accepts that type and size. Otherwise the step sends its PDF text layer, or the OCR text. | Same LLM caveats as the Infer Agent. Whole documents leave PlaidCloud for the provider, and the conversion warns. TIFF and BMP files are sent as OCR text, and there is no maximum document size setting. A document that isn't found is skipped and the step warns with its path. |
| API Agent (`apiService`, and legacy `service` with an API service) | A [REST Request](/reference/workflow-steps/general/rest-request/) step that sends one request per input row, then a join back that keeps every input row. The raw response body lands in a text column, with a status column beside it. A quota per period becomes a fractional **Max req/sec**. A relative URL joins the base URL or REST connection you bind with `api_bindings`. A host, port, or path that comes from a row field is filled in per row. Next-URL, Link header, offset, and page paging are followed, and a paging value (start, page size, or parameter name) can come from an input field or a parameter. | A method other than GET runs against the live system once per input row every time the workflow runs, so confirm the target before the first run. Non-GET requests aren't retried automatically. A failed request stays as a row with its status. A request that carries a credential can't take its host from a row field. Credentials are handled as described in [API Steps with Credentials](#api-steps-with-credentials). |
| Recursion Agent (`hierarchy`) | A [Hierarchy Closure](/reference/workflow-steps/tables/table-hierarchy-closure/) step that walks each row up its parent chain to any depth, then aggregates each node over the ids on its path to the root, itself included. It writes Depth and Path. A row with a blank parent, or naming itself as its parent, is a root. | A loop in the parent ids stops at the repeated node and keeps every ancestor before it. Rows with several parents each keep their own values. |
| Search and Replace (`search_replace`) | A [Table Extract](/reference/workflow-steps/tables/table-extract/) that applies each rule in order to the chosen text columns, case-sensitive or not, whole word or not. Each rule runs in its mode: replace the matched text, replace the whole cell when it contains the text, replace the whole cell when it matches exactly, or append to the cell. | Rules are literal text, not patterns. |
| Split (`split`) | A [Split Text](/reference/workflow-steps/tables/table-split-text/) step. It splits into columns or rows on a literal separator of any length, and decides the number of columns from the data when the workflow runs. | None. |
| Time Series (`rollup`) | A Table Extract that groups by a period expression, with a [Period Spine](/reference/workflow-steps/tables/table-period-spine/), an anti join, and a union that zero-fill the periods with no records. | Records with a NULL date are excluded. The spine stops at 100,000 periods. |
| Format (`format`) | A Table Extract with the renames, retypes, hides, and fills, or a [Promote Header](/reference/workflow-steps/tables/table-promote-header/) step for replace-names-with-row. | A fill on a column that isn't text casts the default to the column's type. Promoting a header over a source that declares no columns reads every column, from CSV, Excel, XLS, JSON, Parquet, and Avro files. See [Files with No Declared Columns](#files-with-no-declared-columns). |
| Spatial Match Agent (`spatial_match`) | A [Spatial Match (executor)](/reference/workflow-steps/spatial/spatial-match-executor/) step for intersects, within, contains, touches, crosses, overlaps, equals, and disjoint, with several rules combined; Cross Join for a cross match; [Find Nearest](/reference/workflow-steps/spatial/spatial-find-nearest/) for a nearest match. | A nearest match ranks and filters by great-circle distance, as Savant does. A nearest rule combined with other rules finds the nearest records first, then applies the other rules: with AND the result keeps records that satisfy every rule, and with OR it unions the nearest records with the records the other rules match. A nearest rule with neither a count nor a maximum distance keeps the single nearest record. A within-distance match converts too, in kilometers when the rule gives no unit, and measures geodesic distance between any geometries, not only points. A geometry that can't be parsed gives NULL or no match, with a warning. |
| Spatial Summarize Agent (`spatial_summarize`) | [Spatial Combine](/reference/workflow-steps/spatial/spatial-combine/) for union, intersect, and bounding box, plus [Spatial Centroid](/reference/workflow-steps/spatial/spatial-centroid/), [Spatial Point to Line](/reference/workflow-steps/spatial/spatial-point-to-line/), and [Spatial Line to Polygon](/reference/workflow-steps/spatial/spatial-line-to-polygon/) for geometric center and line or polygon builds. | A polygon built from fewer than 3 points is an empty polygon. |
| Destination Agent (`destination`) | An export step to the target you bind, or a project table or file when you don't. See [Destinations](#destinations). | See [Edge Cases](#edge-cases). |

`GEO_POINT`, `GEO_TYPE`, and `GEO_SPATIAL_DISTANCE` convert to expressions. An edit whose whole expression is another `GEO_*` function, such as `GEO_AREA` or `GEO_UNION`, converts to the matching spatial step, including [Spatial Info](/reference/workflow-steps/spatial/spatial-info/). Geometry travels as WKT text. `GEO_AREA`, `GEO_PERIMETER`, and `GEO_SPATIAL_DISTANCE` in miles use the statute mile.

A source that reads binary files, such as the documents a Vision agent reads, converts to a document extract of the bound document, or of the file expected at the unbound sources path.

## AI Providers

An Infer or Vision agent converts to an AI/NLP step that uses an LLM connection. The converter supports Anthropic, OpenAI, Gemini, Azure OpenAI, Grok, and GitHub Models.

- The converter picks the connection for the provider and model the agent names, from the LLM connections the importing user can see. It never names one the user can't see. Through an AI assistant (MCP), that means the connections the assistant's user can see.
- When the provider has no visible connection, or Savant's provider has no PlaidCloud match (a cloud-hosted model API or a bring-your-own-key provider of the Savant workspace), the step uses the workspace default connection if the user can see it. Otherwise it leaves the connection blank, and the step uses the workspace default when it runs. The conversion report warns either way, so choose a connection on the step if a different one should answer.

## Destinations

A Savant destination writes the table it receives to the target you bind. Bind destinations with `destination_bindings` in the REST body or MCP call. A key is the destination's node id or name. The Analyze window doesn't bind destinations, so a destination converted there writes the unbound result described under [Unbound Destinations](#unbound-destinations).

| Target | Binding | Result |
| --- | --- | --- |
| Document account | `{account, path[, file_name]}` | A CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF, or Tableau Hyper file, by the kind of destination. You need the document storage write permission on the account. |
| Table on a connection | `{connection, table[, schema, replace]}` | An [Export: External Database Tables](/reference/workflow-steps/export/export-external-tables/) step. You need connection write permission. Replacing the table needs `replace: true`. |
| Google Sheets | `{connection, spreadsheet_name[, sheet_name, replace]}`, or `{connection, spreadsheet_id[, sheet_name, replace]}` | An [Export to Google Spreadsheet](/reference/workflow-steps/export/export-to-google-spreadsheet/) step on a Google Sheets connection. The tab defaults to the one the destination names, else `Sheet1`. A destination that replaces the sheet's rows clears the tab, so it needs `replace: true`. |
| Tableau | `{account, connection[, path, file_name, replace, datasource_name, tableau_project]}` | A Tableau Hyper extract written to the account's folder, then a [Publish to Tableau](/reference/workflow-steps/export/export-to-tableau/) step on a [Tableau connection](/reference/connectors/collaboration/tableau/). Replacing the data source, or changing its rows on match keys, needs `replace: true`. |
| Slack | `{connection[, channel]}` | The CSV is written to a document account, then a [Notify via Slack](/reference/workflow-steps/notifications/notify-via-slack/) step uploads it to the channel. The connection needs a bot token, and the channel must be a channel ID, taken from the binding or else from the export. |
| Email | `{email_to: [...]}`, and `email_export_recipients: true` to also use the recipients the export lists | The CSV is mailed as an attachment. You need email write permission. |

A Sheets, Tableau, or Slack connection is checked the way a table connection is: you must be able to see it and hold connection write permission, or the conversion is refused.

### Write Modes

- A file or table destination that appends reads the earlier file back and rewrites it with the new rows. It never overwrites.
- An upsert, update, or groupReplace destination merges on the destination's match keys. A file or table is read back and rewritten, and a Tableau data source has its matching rows changed in place.
- Append and merge also work on existing files that are split per value, headerless (rows match by position), Excel files anchored at a top-left cell, and files in a non-UTF-8 charset. A split reads back the file each value is written to and merges within it, leaving the other files as they are.
- A Tableau destination maps Savant's modes to the six [Publish to Tableau](/reference/workflow-steps/export/export-to-tableau/#modes) modes: append and insert add rows, replace overwrites, and upsert, update, and groupReplace match on keys. A mode that changes existing data publishes only when the binding says `replace: true`; otherwise the destination publishes a new data source and the report says so.
- A destination with an output encoding writes the file in that Java character set. A character the set lacks is written as `?`, as Savant does. Java aliases, CESU-8, and byte-order-mark forms are accepted. A few rare charsets (for example `x-ISCII91` or `JIS_X0212`) can't be written; the file is written as UTF-8 and the report warns. A split in a non-UTF-8 charset converts the folder.
- Export file names must stay inside the bound folder.

### What AI Callers Can Bind

A conversion through an AI assistant (MCP) binds the same shapes with these parts withheld, each with a warning that names the part:

| Withheld | What Happens Instead |
| --- | --- |
| `replace` on a table, sheet, or Tableau data source | A destination that appends still appends to its bound table or sheet. A destination that replaces writes a CSV. A Tableau destination publishes a new data source. |
| Email recipients | A CSV is written in place of the email. |
| Slack | A CSV is written in place of the Slack post. |

Convert from the Analyze app or the REST API, or sign in yourself rather than through an assistant, to bind these.

### Unbound Destinations

A destination with no binding writes its PlaidCloud counterpart and warns **Destination target unbound**, naming the original target. The conversion never contacts the target system.

| Destination | Result |
| --- | --- |
| Database, warehouse, or SaaS target (Oracle, generic database, Looker Studio, NetSuite, SAP, and Google Sheets, Tableau, or Slack with no connection bound) | A table in the project, named after the destination node. |
| File storage (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | The file, in the destination's file type, in a Document folder under the account you gave for unbound sources. The folder mirrors the target folder. Credentials and share tokens are dropped from the path. |
| Email | A CSV, in the Document account you gave for unbound sources. |

The warning tells you what to bind to reach the real target. A destination whose binding can't be used writes a CSV and warns **Fallback, target not written**, with the original target in the message; check that CSV before you rely on it. A plain CSV destination writes its own file.

### Split Destinations

A destination that writes a file, sub-folder, or tab per value of a field splits CSV, Excel, Parquet, and PDF files and Google Sheets tabs.

- **Parquet and PDF.** One file per value.
- **Google Sheets.** One tab per value.
- **Template.** A template workbook seeds the workbook for every value. A missing template warns and the workbook is written without it.
- **NULL values.** A NULL split value is written to its own file or tab, not dropped.
- **A field the input lacks.** A split, or a sort, on a field the input doesn't carry is refused by name, because Savant fails on it.
- **A `/` or `\` in a value.** A split value that holds a slash or backslash can't be a file or tab name, so it is sanitised. A changed value gets a fixed six-character suffix, `-` followed by the first six characters of the value's MD5 hash, placed before the file extension. Values that need no change keep their name.

### Exported Values and Row Order

- **Plain numbers and booleans.** CSV, TSV, and TXT exports write numbers as plain numbers and booleans as `true` and `false`, with no `+00:00` on timestamps.
- **Stable row order.** A destination that sorts writes one row order on every run: ties are broken the same way each time, and split and part routes sort too. Parquet, Google Sheets, Tableau, and table targets keep no row order.

### Excel Options

An Excel destination maps these options:

- **Tab per field value.** Each value of the field becomes a sheet. Blank values go to `Sheet1`, and sheets whose names collide get a numeric suffix.
- **Format from template.** Each run first copies `<name>_template.xlsx` from the same folder over the workbook, then writes into it, so the workbook is always replaced. If the template isn't there, the copy warns and the workbook is written without it.
- **Top-left cell.** The rows are written into the workbook starting at that cell.
- **Mode `create`.** Every run writes the file as the destination's write mode says.

## Bind API Requests

An API agent whose URL is relative, such as `/v2/customers`, has no host to send to. Bind one with `api_bindings`. A key is the API node's id or name, or `*` for every API node without a binding of its own. A value is one of:

- A base URL, as a string or `{"base_url": "https://host/path"}`. The relative URL is joined to it. The URL must be `http` or `https` with a public host, and carry no user, query, or fragment.
- `{"connection": "<REST connection id>"}`. The request goes to that [REST connection](/reference/connectors/rest/generic-rest/)'s host and carries its credentials. You need connection write permission, and the connection must be a REST connection you can see.

```json
"api_bindings": {
  "*": "https://api.example.com/v1",
  "Customers": { "connection": "<REST connection id>" }
}
```

An unmatched key is a warning, and a binding you can't use is refused. A relative URL with no binding stays a named placeholder.

An AI assistant (MCP) without connection write permission has a connection binding ignored with a warning, and the relative URL it would have joined stays a placeholder. Bind a base URL, or convert from the Analyze app or the REST API.

A host, port, or path that comes from an input field needs no binding. It is filled in per row, each value checked as it is used, and the report lists the hosts a row may name. A request that carries a credential can't take its host from a row field: sending a credential to a host the data chooses is refused.

Paging converts too. A next-page URL in the response, a `Link` header, an offset, and a page number each become a paging mode on the [REST Request](/reference/workflow-steps/general/rest-request/) step, which reads every page. A paging value can come from an input field (`{{Field}}`) or a parameter (`{{Param}}`), and a value written as numeric text such as `10.0` is read as a number.

## API Steps with Credentials

A credential in an API agent's headers, URL path, query, or body moves into a PlaidCloud REST connection that the import creates. The REST Request step references that connection, so the credential never sits in the step.

- The response lists the connections the import created or reused under `connections`, and the import report names them. Importing the same analysis again reuses the same connection rather than creating another.
- Credentials in the URL user info and in headers go into the connection's own authentication fields or default headers. Path, query, and body secrets are stored encrypted on the connection and filled in at run time, only for requests to that connection's own `https` host.
- An unencrypted `http://` endpoint is not converted with credentials. The credential is left out and the conversion report warns that it was not copied.
- Importing through an AI assistant (MCP) does not create connections. Credentials are left out and a warning says so. Import from the Analyze app or the REST API instead, or add the credential to a REST connection by hand and select it on the step.
- A user without connection-write permission gets the same outcome: credentials left out and a warning.
- Only an API credential slot moves a parameter into a connection. A pipeline parameter used in a header, query, path, or body where an API credential goes moves into the connection's encrypted `secret_values`, and the step refers to it through the connection. It is never created as a workflow variable, whatever the parameter is named.
- Any other parameter whose name holds a secret word (such as `password`, `token`, `secret`, or `key`, with `key` excepted after a data word such as `sort` or `partition`) becomes a workflow variable with a blank value and a warning. A name such as `api_key_2` is blanked too. Set the value on the project variable after the import.
- A parameter named for a count or limit, such as `max_tokens`, keeps its value.
- A secret typed into a formula, filter, or replace value is left out of the step and the conversion report warns. A path, a URL, and a 40 or 64 character hex digest are kept, unless part of them or a secret name says otherwise. Folder sharing links and recipient email addresses never appear in warnings or notes.
- A response that echoes a credential back is stored as received. Treat the output table of such a request as sensitive.

## JWT_ENCODE

`JWT_ENCODE` converts to a [JWT Encode](/reference/workflow-steps/tables/table-jwt-encode/) step. A literal signing key goes into a dedicated connection bound to the step, and the token is signed at run time, so the key never appears in the step configuration. Through an AI assistant, or without connection-write permission, the key is left out, the token is NULL, and a warning tells you to import again with permission to create connections.

## Promote a Data Row to Column Headers

A Format agent set to **replace names with row** converts to a [Promote Header](/reference/workflow-steps/tables/table-promote-header/) step. At run time the chosen row, counted from 1, becomes the column names and is removed. A source that carries no record order gets a note, because which row names the columns can change from run to run. A column that row names but no later step mentions is not carried past a step that lists the columns it reads.

## Files with No Declared Columns

A source with no declared columns keeps these columns:

- A CSV, TSV, or TXT source bound at import keeps every column in the file's header.
- Any other file type, and any unbound source, keeps only the columns later steps name, and the conversion report warns.
- A promoted header over such a source reads every column, from CSV, Excel, XLS, JSON, Parquet, and Avro files.

When such a source feeds only a promoted header, the import is an [Import Delimited](/reference/workflow-steps/import/import-delimited/) step that reads every column by position. A step that exports or joins after a promoted header carries every column the table has at run time (see **Also carry columns named at run time** in [Table Extract](/reference/workflow-steps/tables/table-extract/)).

## Behaviors Worth Knowing

These conversions behave as follows.

| Agent | Behavior |
| --- | --- |
| Blend (`blend`) | Joins on OR-combined predicates, contains, and is-part-of. Outer-excluding-inner blends and the unmatched outputs convert to the matching join streams. For any operator, the duplicate right-hand key is dropped from the output. |
| Dedupe (`deduplicate`) | Keeps the first record per key within each Group By group. The duplicates flag marks every member of a duplicate group, and duplicates can also route to a second stream. With a single outlet connected, it behaves as Savant does. |
| Summarize (`summarize`) | Window aggregates add the aggregate to every row instead of collapsing groups. |
| Sample (`sample`) | First N rows, per group or overall, a random percent or number of rows, or one row in every Nth. |
| Time Series (`rollup`) | Day, week, month, quarter, year, and decade periods between the optional start and end dates, per group. Month periods are labeled `YYYY-MM`, and periods with no records appear with zeros. Records with a NULL date are excluded. |
| Pivot (`pivot`) | COUNT counts rows. |
| XML (`xml`) | SELECT extracts elements, paths can carry namespaces, and TO_JSON converts XML to JSON. Any XPath 1.0 path converts, including predicates, attribute tests, wildcards, and functions such as `count()`, `name()`, and `contains()`, and the [XML Parse](/reference/workflow-steps/tables/table-xml-parse/) step reads it as XPath. With `processNs` off, names are matched literally, prefix included. An XML file missing when you convert resolves its root element when the workflow runs. |
| JSON (`json`) | Flattens into wide columns. Text that isn't valid JSON gives NULL, and arrays come out as text. |
| Split (`split`) | Splits into columns or rows, with the number of columns read from the data each time the workflow runs. |

These expression functions follow Savant's results:

| Function | Behavior |
| --- | --- |
| `DATE_DIFF` | Weeks and quarters count the way Savant does. |
| `PAD` | Doesn't truncate a value longer than the target width. |
| `+` on text | Concatenates text. A column from a source with no declared types reads as a number, so `+` adds, and a note says so. |
| Split to rows | Keeps empty pieces as rows. |
| `LAST` with no sort | Returns the last row in the order rows arrive, with a note that the warehouse doesn't guarantee that order. |
| `JOIN_STR` | Joins a fractional number as Savant writes it, without trailing zero padding. |
| `JSON_FORMAT` | Pretty-prints the JSON; on Snowflake it writes the JSON compact on one line. |
| `JSON_SET` | Keeps Savant's key order. |
| `GREATEST` and `LEAST` | Skip NULL arguments. The result is NULL only when every argument is NULL. |
| `ROUNDUP` | Rounds up to the next whole step, so a negative number rounds toward zero: -1.5 becomes -1. `ROUNDDOWN` is unchanged. |
| `DURING_DAYLIGHT_SAVING` and `DURING_STANDARD` | NULL in gives NULL out. |
| `TO_TEXT` with a date format | Reads the format tokens as Savant does. `YYYY`, `w`, and `u` are the ISO week-year, week, and weekday, and a zone or era letter is written as for a UTC time. |
| `TO_TEXT` and number-to-text output | Writes plain numbers such as `12`, not `12.0000000000`. |
| `TO_TEXT` with a numeric pattern | Formats as a Java `DecimalFormat` does, rounding half to even, including scientific patterns such as `##0.##E0`. |
| `TO_TEXT` and date parsing with a per-row format | Reads the format from each row. |
| Fractional-second, narrow month, and week-based date tokens | Convert. The week tokens read as ISO weeks. |
| Two-digit years (`yy`, `y`) | Read through a window of 80 years back and 20 years forward from the current year. |
| `REGEX_MATCH` | A partial match: the pattern matches anywhere in the text, not the whole text. |

`TO_TEXT` and date formats convert in a [Text Function](/reference/workflow-steps/tables/table-text-function/) step. An edit that carries only its compiled steps, with no expression, converts as those steps applied in order, each feeding the next, and the conversion report notes the order it assumed. The converter refuses by name what Savant itself fails on or what has nothing to convert, and the step becomes a placeholder: a plain aggregate or window function inside a Transform or Filter expression (inside a calculation or a Summarize it converts), `HASH` with a literal algorithm other than `md5` or `sha1`, a regex construct PlaidCloud can't read (a class inside a class, a class intersection, or an unknown `\p{}` property), a Transform edit with no expression and no compiled steps (such as a Copilot edit that has only its prompt), an XML path that is not XPath 1.0, and an API request that carries a credential and takes its host from a row field. The [Savant Conversion Matrix](/reference/savant-conversion-matrix/#named-refusals) lists each with its reason.

Expression functions also convert for `sha1`, `NOT_TRUE`, `LEVENSHTEIN`, the daylight saving time functions (`DST`), and regular expression functions that take an nth match. `DAY_OF_WEEK` numbers Sunday as 7, and `DAY_NAME` returns the day's name.

## Read the Conversion Report

The response carries the conversion report: a summary of how many steps converted with high, medium, or low confidence and how many did not convert, plus warnings and the nodes the converter absorbed into others. Read it before you run the workflow. It names every placeholder, every unbound source and unmatched binding, and the table prefix used.

## Placeholders for Unconverted Configurations

A configuration the converter can't reproduce is created as a placeholder step that carries the agent's name, and the conversion report names it. A placeholder appears for a construct the converter refuses by name (see the [Savant Conversion Matrix](/reference/savant-conversion-matrix/#named-refusals)) or one the export doesn't describe fully, such as a missing API configuration. By default a placeholder fails when the workflow reaches it, so a run can't report success on work that never happened.

Set `allow_unconverted_placeholders` to `true` to import each placeholder as a pass-through step instead. The run then continues past it and the placeholder's output is its input. Rebuild the capability with a native step when its result matters.

## Run the Converted Workflow

1. Open the new workflow in the project.
2. Set any project variables that came from Savant parameters.
3. Upload files for unbound sources to the paths in the report.
4. Run the workflow and review each step's output table.

## Edge Cases

These are the only known differences from Savant. The conversion report names each one that applies.

- **Date formats.** `TO_DATE` or `TO_DATETIME` with a format holding a `[`, `]`, `'`, `\`, or `^` literal, on text it reads into 9999-12-30 or 9999-12-31, falls past the last timestamp the warehouse holds, and the report warns.
- **Secret parameters.** A parameter whose name holds a secret word, or whose value looks like a credential, becomes a project variable with a blank value, by design. Set the value in the variable.
- **Undeclared parameters.** A parameter a node uses that the export doesn't declare comes through as a project variable with an empty value.
- **`JSON_FORMAT` on Snowflake.** It writes compact JSON on one line.
- **Row order.** Sorted Parquet, Google Sheets, Tableau, and table targets keep no row order.
- **Google Sheets and Tableau.** Publishing to either needs its account bound through `destination_bindings`.

## Related Guides

- [Savant Conversion Matrix](/reference/savant-conversion-matrix/)
- [REST Connection](/reference/connectors/rest/generic-rest/)
- [Add Document Accounts](/guides/documents/adding-accounts/)
- [Manage Workflow Variables](/guides/workflows/manage-workflow-variables/)
- [AI/NLP Step](/reference/workflow-steps/text-documents/nlp-ai/)
- [REST Request Step](/guides/workflows/rest-request-step/)
- [Run a Workflow](/guides/workflows/run-a-workflow/)
