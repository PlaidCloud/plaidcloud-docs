---
title: Migrate Savant Analyses
description: Convert a Savant Labs analysis export into a PlaidCloud Advanced workflow from the Analyze app, the REST API, or an MCP-connected AI agent, bind its sources, and read the conversion report.
sidebar:
  order: 31
---

PlaidCloud converts a Savant Labs analysis export into a runnable Advanced workflow. The converter maps each Savant agent to a workflow step, a project variable, or a canvas object, keeps the original graph, and returns a conversion report that names anything it could not convert.

Conversion reads only the export file you point it at. It never contacts the system a Savant source or destination connects to.

## What PlaidCloud Creates

- Each Savant agent becomes the matching workflow step, with upstream and downstream relationships preserved. The [Savant Conversion Matrix](/reference/savant-conversion-matrix/) lists every agent, its mapping tier, and any option without a mapping.
- Savant analysis parameters become project variables, and references to them inside agent settings are rewritten to the PlaidCloud variable syntax.
- Notes and groups arrive on the canvas as notes and groups.
- Each source becomes an import step, or reads an existing table, depending on how you bind it.
- Every Savant agent type converts. A configuration the converter can't reproduce arrives as a named placeholder step. See [Placeholders for Unconverted Configurations](#placeholders-for-unconverted-configurations).
- A step whose Savant behavior the help documentation doesn't spell out is converted to the most likely reading and carries a **semantics assumed** note in the conversion report. Check those steps against your Savant output.

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
| `destination_bindings` | No | Routes destinations to a document account, a connection table, or email recipients. REST and MCP only. See [Destinations](#destinations). |
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
| Infer Agent (`gen_ai`, and legacy `service` with an LLM service) | An [AI/NLP](/reference/workflow-steps/text-documents/nlp-ai/) step with the **Prompt** task. The prompt runs once per row over the input fields, and the answer lands in an **AI Answer** column beside every input column. A row limit becomes **Max rows**, and an empty source warns and writes an empty table. | An LLM answers, so output is never byte-identical to Savant's and can vary between runs. Each call has a cost. See [AI Providers](#ai-providers). A batch that fails keeps its rows with an empty answer and warns. |
| Vision Agent (`vision`) | A [Document Read Blob](/reference/workflow-steps/text-documents/document-blob-extract/) step, [Image OCR](/reference/workflow-steps/text-documents/image-ocr/), then the AI/NLP **Prompt** task. Each document goes to the provider as an image or PDF when the provider accepts that type and size. Otherwise the step sends its PDF text layer, or the OCR text. | Same LLM caveats as the Infer Agent. Whole documents leave PlaidCloud for the provider, and the conversion warns. TIFF and BMP files are sent as OCR text, and there is no maximum document size setting. A document that isn't found is skipped and the step warns with its path. |
| API Agent (`apiService`, and legacy `service` with an API service) | A [REST Request](/reference/workflow-steps/general/rest-request/) step that sends one request per input row, then a join back that keeps every input row. The raw response body lands in a text column, with a status column beside it. A quota per period becomes a fractional **Max req/sec**. | A method other than GET runs against the live system once per input row every time the workflow runs, so confirm the target before the first run. Non-GET requests aren't retried automatically. A failed request stays as a row with its status. Pagination isn't followed: only the first page is read, with a warning. Only an absolute `http://` or `https://` URL converts, and row data can't choose the host. Credentials are handled as described in [API Steps with Credentials](#api-steps-with-credentials). |
| Recursion Agent (`hierarchy`) | A [Hierarchy Closure](/reference/workflow-steps/tables/table-hierarchy-closure/) step that walks each row up its parent chain to any depth, then aggregates each node over the ids on its path to the root, itself included. It writes Depth and Path. A row with a blank parent, or naming itself as its parent, is a root. | A loop in the parent ids stops at the repeated node and keeps every ancestor before it. Rows with several parents each keep their own values. |
| Search and Replace (`search_replace`) | A [Table Extract](/reference/workflow-steps/tables/table-extract/) that applies each rule in order to the chosen text columns, case-sensitive or not, whole word or not. Each rule runs in its mode: replace the matched text, replace the whole cell when it contains the text, replace the whole cell when it matches exactly, or append to the cell. | Rules are literal text, not patterns. |
| Split (`split`) | A [Split Text](/reference/workflow-steps/tables/table-split-text/) step. It splits into columns or rows on a literal separator of any length, and decides the number of columns from the data when the workflow runs. | None beyond the matrix status. |
| Time Series (`rollup`) | A Table Extract that groups by a period expression, with a [Period Spine](/reference/workflow-steps/tables/table-period-spine/), an anti join, and a union that zero-fill the periods with no records. | Records with a NULL date are excluded. The spine stops at 100,000 periods. |
| Format (`format`) | A Table Extract with the renames, retypes, hides, and fills, or a [Promote Header](/reference/workflow-steps/tables/table-promote-header/) step for replace-names-with-row. | A few Format settings aren't converted. See [What Stays Limited](#what-stays-limited). |
| Spatial Match Agent (`spatial_match`) | A [Spatial Match (executor)](/reference/workflow-steps/spatial/spatial-match-executor/) step for intersects, within, contains, touches, crosses, overlaps, equals, and disjoint, with several rules combined; Cross Join for a cross match; [Find Nearest](/reference/workflow-steps/spatial/spatial-find-nearest/) for a nearest match. | A nearest match ranks and filters by great-circle distance, as Savant does. A within-distance match converts too, in kilometers when the rule gives no unit, and tests WKT points only. |
| Spatial Summarize Agent (`spatial_summarize`) | [Spatial Combine](/reference/workflow-steps/spatial/spatial-combine/) for union, intersect, and bounding box, plus [Spatial Centroid](/reference/workflow-steps/spatial/spatial-centroid/), [Spatial Point to Line](/reference/workflow-steps/spatial/spatial-point-to-line/), and [Spatial Line to Polygon](/reference/workflow-steps/spatial/spatial-line-to-polygon/) for geometric center and line or polygon builds. | A polygon built from fewer than 3 points is an empty polygon. |
| Destination Agent (`destination`) | An export step to the target you bind, or a CSV when you don't. See [Destinations](#destinations). | See [What Stays Limited](#what-stays-limited). |

`GEO_POINT`, `GEO_TYPE`, and `GEO_SPATIAL_DISTANCE` convert to expressions. An edit whose whole expression is another `GEO_*` function, such as `GEO_AREA` or `GEO_UNION`, converts to the matching spatial step, including [Spatial Info](/reference/workflow-steps/spatial/spatial-info/). Geometry travels as WKT text. `GEO_AREA`, `GEO_PERIMETER`, and `GEO_SPATIAL_DISTANCE` in miles use the statute mile.

A source that reads binary files, such as the documents a Vision agent reads, converts to a document extract of the bound document, or of the file expected at the unbound sources path.

## AI Providers

An Infer or Vision agent converts to an AI/NLP step that uses an LLM connection. The converter supports Anthropic, OpenAI, Gemini, Azure OpenAI, Grok, and GitHub Models.

- The converter picks the connection for the provider and model the agent names, from the LLM connections the importing user can see. It never names one the user can't see. Through an AI assistant (MCP), that means the connections the assistant's user can see.
- When the provider has no visible connection, or Savant's provider has no PlaidCloud match (a cloud-hosted model API or a bring-your-own-key provider of the Savant workspace), the step uses the workspace default connection if the user can see it. Otherwise it leaves the connection blank, and the step uses the workspace default when it runs. The conversion report warns either way, so choose a connection on the step if a different one should answer.

## Destinations

A Savant destination writes the table it receives to the target you bind. Bind destinations with `destination_bindings` in the REST body or MCP call. A key is the destination's node id or name. The Analyze window doesn't bind destinations, so a destination converted there writes a CSV.

| Target | Binding | Result |
| --- | --- | --- |
| Document account | `{account, path[, file_name]}` | A CSV, Excel, or Tableau Hyper export, by the kind of destination. You need the document storage write permission on the account. |
| Table on a connection | `{connection, table[, schema, replace]}` | An [Export: External Database Tables](/reference/workflow-steps/export/export-external-tables/) step. You need connection write permission. Replacing the table needs `replace: true`. |
| Email | `{email_to: [...]}`, and `email_export_recipients: true` to also use the recipients the export lists | The CSV is mailed as an attachment. You need email write permission. |

- An append destination reads the earlier file back and rewrites it with the new rows. It never overwrites.
- Export file names must stay inside the bound folder.
- An AI assistant (MCP) can't bind a replace or email recipients. An appending destination still appends to its bound table. A destination that replaces falls back to a CSV, and the warning says which part wasn't allowed.
- A destination with no usable binding writes a CSV to the Document account you gave for unbound sources and warns **Fallback, target not written**, with the original target in the message. Nothing is dropped. The CSV is not the destination's own output, so check it before you rely on it. A plain CSV destination writes its own file.

## API Steps with Credentials

A credential in an API agent's headers, URL path, query, or body moves into a PlaidCloud REST connection that the import creates. The REST Request step references that connection, so the credential never sits in the step.

- The response lists the connections the import created or reused under `connections`, and the import report names them. Importing the same analysis again reuses the same connection rather than creating another.
- Credentials in the URL user info and in headers go into the connection's own authentication fields or default headers. Path, query, and body secrets are stored encrypted on the connection and filled in at run time, only for requests to that connection's own `https` host.
- An unencrypted `http://` endpoint is not converted with credentials. The credential is left out and the conversion report warns that it was not copied.
- Importing through an AI assistant (MCP) does not create connections. Credentials are left out and a warning says so. Import from the Analyze app or the REST API instead, or add the credential to a REST connection by hand and select it on the step.
- A user without connection-write permission gets the same outcome: credentials left out and a warning.
- A pipeline parameter used where an API credential goes, in a header, query, path, or body, moves into the connection's encrypted `secret_values`, and the step refers to it through the connection. It is never created as a workflow variable, whatever the parameter is named.
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

When such a CSV feeds only a promoted header, the import is an [Import Delimited](/reference/workflow-steps/import/import-delimited/) step that reads every column by position. A step that exports or joins after a promoted header carries every column the table has at run time (see **Also carry columns named at run time** in [Table Extract](/reference/workflow-steps/tables/table-extract/)).

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
| XML (`xml`) | SELECT extracts elements, paths can carry namespaces, and TO_JSON converts XML to JSON. With `processNs` off, names are matched literally, prefix included. |
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
| `JSON_FORMAT` | Pretty-prints the JSON. |
| `JSON_SET` | Keeps Savant's key order. |
| `GREATEST` and `LEAST` | Skip NULL arguments. The result is NULL only when every argument is NULL. |
| `ROUNDUP` | Rounds up to the next whole step, so a negative number rounds toward zero: -1.5 becomes -1. `ROUNDDOWN` is unchanged. |
| `DURING_DAYLIGHT_SAVING` and `DURING_STANDARD` | NULL in gives NULL out. |
| `TO_TEXT` with a date format | Reads the format tokens as Savant does. `YYYY`, `w`, and `u` are the ISO week-year, week, and weekday, and a zone or era letter is written as for a UTC time. |
| `TO_TEXT` and number-to-text output | Writes plain numbers such as `12`, not `12.0000000000`. |

`TO_TEXT` with a numeric pattern, a format that is only known per row, or fractional-second (`S`) tokens isn't converted. It is flagged by name. Plain aggregate and window functions inside an ordinary expression aren't converted either.

Expression functions also convert for `sha1`, `NOT_TRUE`, `LEVENSHTEIN`, the daylight saving time functions (`DST`), and regular expression functions that take an nth match. `DAY_OF_WEEK` numbers Sunday as 7, and `DAY_NAME` returns the day's name.

## Read the Conversion Report

The response carries the conversion report: a summary of how many steps converted with high, medium, or low confidence and how many did not convert, plus warnings and the nodes the converter absorbed into others. Read it before you run the workflow. It names every placeholder, every unbound source and unmatched binding, and the table prefix used.

## Placeholders for Unconverted Configurations

A configuration the converter can't reproduce is created as a placeholder step that carries the agent's name, and the conversion report names it. A placeholder appears for a construct listed in [What Stays Limited](#what-stays-limited) or one the export doesn't describe fully, such as a missing API configuration. By default a placeholder fails when the workflow reaches it, so a run can't report success on work that never happened.

Set `allow_unconverted_placeholders` to `true` to import each placeholder as a pass-through step instead. The run then continues past it and the placeholder's output is its input. Rebuild the capability with a native step when its result matters.

## Run the Converted Workflow

1. Open the new workflow in the project.
2. Set any project variables that came from Savant parameters.
3. Upload files for unbound sources to the paths in the report.
4. Run the workflow and review each step's output table.

## What Stays Limited

A converted workflow can differ from Savant in these ways. The conversion report names each one that applies.

**Reading differences.** Savant's help doesn't settle these, so the converter takes one reading, and the converted step can differ from the Savant answer:

- **Ties between equal values.** In a nearest match, two candidates can sit at the same distance. Savant picks the one that arrived first. A warehouse join has no arrival order, so the converted step can pick the other.
- **The distance column.** The converted nearest match writes a `Distance` column beside each match. Savant writes none.

**Language models.** Infer and Vision agents depend on a language model, so their answers differ from Savant's and between runs. A Fuse agent matches with the deterministic [Fuzzy Match](/reference/workflow-steps/tables/table-fuzzy-match/) step at a threshold of 80, where Savant uses a language model.

**Destinations that fall back to a CSV.** These options aren't converted and write a CSV with a warning: matching keys for an upsert, Google Sheets, an output encoding, a sheet taken from a field, and Slack. A destination with no binding, or one the export can't write, also falls back. See [Destinations](#destinations).

**Other limits.**

- Date and timestamp conversions of text that isn't in a recognizable date format can fail the run on that row.
- A source with no declared columns that isn't a bound CSV, TSV, or TXT file keeps only the columns later steps reference. See [Files with No Declared Columns](#files-with-no-declared-columns).
- An API agent follows only the first page, and a relative URL or a host taken from a row field isn't converted. Credentials in an `http://` URL are left out, and MCP imports don't create connections.
- A Vision agent sends TIFF and BMP files as OCR text.
- Format settings for sort, field reordering, extra, and replace aren't converted, and fill writes only text columns.
- XML paths with predicates, attributes, wildcards, or functions become placeholders, and a path with several steps matches its last element.
- A spatial within-distance test reads WKT points only.
- On StarRocks and Snowflake, `JSON_FORMAT` and `JSON_SET` fail at run time, and the conversion report notes it.

## Related Guides

- [Savant Conversion Matrix](/reference/savant-conversion-matrix/)
- [REST Connection](/reference/connectors/rest/generic-rest/)
- [Add Document Accounts](/guides/documents/adding-accounts/)
- [Manage Workflow Variables](/guides/workflows/manage-workflow-variables/)
- [AI/NLP Step](/reference/workflow-steps/text-documents/nlp-ai/)
- [REST Request Step](/guides/workflows/rest-request-step/)
- [Run a Workflow](/guides/workflows/run-a-workflow/)
