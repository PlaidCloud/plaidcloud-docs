---
title: Migrate Savant Analyses
description: Convert a Savant Labs analysis export into a PlaidCloud Advanced workflow from the Analyze app, the REST API, or an MCP-connected AI agent, bind its sources, and read the conversion report.
sidebar:
  order: 31
---

PlaidCloud converts a Savant Labs analysis export into a runnable Advanced workflow. The converter maps each Savant agent to a workflow step, a project variable, or a canvas object, keeps the original graph, and returns a conversion report that names anything it could not convert.

Conversion reads only the export file you point it at. It never contacts the system a Savant source or destination connects to.

## What PlaidCloud Creates

- Each Savant agent becomes the matching workflow step, with upstream and downstream relationships preserved. The [Savant Conversion Matrix](/reference/savant-conversion-matrix/) lists every agent and its measured status.
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
| Infer Agent (`gen_ai`, and legacy `service` with an LLM service) | An [AI/NLP](/reference/workflow-steps/text-documents/nlp-ai/) step with the **Prompt** task. The prompt runs once per row over the input fields, and the answer lands in an **AI Answer** column beside every input column. | An LLM answers, so output is never byte-identical to Savant's and can vary between runs. Every row is answered on every run, and each call has a cost. The step uses the Anthropic LLM connection of your workspace whichever provider Savant used. A batch that fails keeps its rows with an empty answer and warns. |
| Vision Agent (`vision`) | A document extract step, image OCR, then the AI/NLP **Prompt** task. Each document is read from its PDF text layer, or by OCR when it has none, and the prompt runs over that text. | Same LLM caveats as the Infer Agent. A document that isn't found is skipped and the step warns with its path. |
| API Agent (`apiService`, and legacy `service` with an API service) | A [REST Request](/reference/workflow-steps/general/rest-request/) step that sends one request per input row, then a join back that keeps every input row. The response body lands in a text column. | A method other than GET runs against the live system once per input row every time the workflow runs, so confirm the target before the first run. Non-GET requests aren't retried automatically. Settings the converter doesn't recognize map to headers, the body, and parameters. A failed request leaves its row with an empty response. Only an `http://` or `https://` URL converts, and row data can't choose the host. Credentials are handled as described in [API Steps with Credentials](#api-steps-with-credentials). |
| Recursion Agent (`hierarchy`) | A bounded walk up the parent chain: repeated inner joins, a union, an aggregate over each row's ancestors and itself, and a row-count check. A row with a blank parent, or naming itself as its parent, is a root. | A chain deeper than 17 levels, or a loop in the parent ids, fails the run at the depth check, and nothing downstream is written. Duplicate rows and rows with several parents each keep their own values, and a loop stops at the repeated node. |
| Search and Replace (`search_replace`) | A [Table Extract](/reference/workflow-steps/tables/table-extract/) that applies each rule in order to the chosen text columns, case-sensitive or not, whole word or not. Each rule runs in its mode: replace the matched text, replace the whole cell when it contains the text, replace the whole cell when it matches exactly, or append to the cell. | Rules are literal text, not patterns. |
| Spatial Match Agent (`spatial_match`) | A [Spatial Match (executor)](/reference/workflow-steps/spatial/spatial-match-executor/) step for intersects, within, contains, touches, crosses, overlaps, equals, and disjoint, with several rules combined; Cross Join for a cross match; [Find Nearest](/reference/workflow-steps/spatial/spatial-find-nearest/) for a nearest match. | A within-distance match converts too. The distance is in kilometers when the rule gives no unit. |
| Spatial Summarize Agent (`spatial_summarize`) | [Spatial Combine](/reference/workflow-steps/spatial/spatial-combine/) for union, intersect, and bounding box, plus centroid and point-to-line steps for geometric center and line or polygon builds. | None beyond the matrix status. |

`GEO_POINT`, `GEO_TYPE`, and `GEO_SPATIAL_DISTANCE` convert to expressions. An edit whose whole expression is another `GEO_*` function, such as `GEO_AREA` or `GEO_UNION`, converts to the matching spatial step. Geometry travels as WKT text.

A source that reads binary files, such as the documents a Vision agent reads, converts to a document extract of the bound document, or of the file expected at the unbound sources path.

## API Steps with Credentials

A credential in an API agent's headers, URL path, query, or body moves into a PlaidCloud REST connection that the import creates. The REST Request step references that connection, so the credential never sits in the step.

- The response lists the connections the import created or reused under `connections`, and the import report names them. Importing the same analysis again reuses the same connection rather than creating another.
- Credentials in the URL user info and in headers go into the connection's own authentication fields or default headers. Path, query, and body secrets are stored encrypted on the connection and filled in at run time, only for requests to that connection's own `https` host.
- An unencrypted `http://` endpoint is not converted with credentials. The credential is left out and the conversion report warns that it was not copied.
- Importing through an AI assistant (MCP) does not create connections. Credentials are left out and a warning says so. Import from the Analyze app or the REST API instead, or add the credential to a REST connection by hand and select it on the step.
- A user without connection-write permission gets the same outcome: credentials left out and a warning.
- A response that echoes a credential back is stored as received. Treat the output table of such a request as sensitive.

## JWT_ENCODE

`JWT_ENCODE` converts. A literal signing key goes into a dedicated connection bound to the step, and the token is signed at run time, so the key never appears in the step configuration. Through an AI assistant, or without connection-write permission, the key is left out, the token is NULL, and a warning tells you to import again with permission to create connections.

## Promote a Data Row to Column Headers

A Format agent set to **replace names with row** converts. At run time the chosen row, counted from 1, becomes the column names and is removed. A source that carries no record order gets a note, because which row names the columns can change from run to run. A column that row names but no later step mentions is not carried past a step that lists the columns it reads.

## Files with No Declared Columns

A source with no declared columns keeps these columns:

- A CSV, TSV, or TXT source bound at import keeps every column in the file's header.
- Any other file type, and any unbound source, keeps only the columns later steps name, and the conversion report warns.

When such a CSV feeds only a promoted header, the import reads every column by position.

## Behaviors Worth Knowing

These conversions behave as follows.

| Agent | Behavior |
| --- | --- |
| Blend (`blend`) | Joins on OR-combined predicates, contains, and is-part-of. Outer-excluding-inner blends and the unmatched outputs convert to the matching join streams. For any operator, the duplicate right-hand key is dropped from the output. |
| Dedupe (`deduplicate`) | Keeps the first record per key within each Group By group. The duplicates flag marks every member of a duplicate group, and duplicates can also route to a second stream. With a single outlet connected, it behaves as Savant does. |
| Summarize (`summarize`) | Window aggregates add the aggregate to every row instead of collapsing groups. |
| Sample (`sample`) | First N rows, per group or overall, a random percent or number of rows, or one row in every Nth. |
| Time Series (`rollup`) | Month periods are labeled `YYYY-MM`, and periods with no records appear with zeros. Records with a NULL date are excluded. |
| Pivot (`pivot`) | COUNT counts rows. |
| XML (`xml`) | SELECT extracts elements, paths can carry namespaces, and TO_JSON converts XML to JSON. With `processNs` off, names are matched literally, prefix included. |
| JSON (`json`) | Flattens into wide columns. Text that isn't valid JSON gives NULL, and arrays come out as text. |
| Split (`split`) | Splits into columns. When nothing downstream names the columns, the number of columns comes from the data. |

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
| `TO_TEXT` and number-to-text output | Writes plain numbers such as `12`, not `12.0000000000`. |

Expression functions also convert for `sha1`, `NOT_TRUE`, `LEVENSHTEIN`, the daylight saving time functions (`DST`), and regular expression functions that take an nth match. `DAY_OF_WEEK` numbers Sunday as 7, and `DAY_NAME` returns the day's name.

## Read the Conversion Report

The response carries the conversion report: a summary of how many steps converted with high, medium, or low confidence and how many did not convert, plus warnings and the nodes the converter absorbed into others. Read it before you run the workflow. It names every placeholder, every unbound source and unmatched binding, and the table prefix used.

## Placeholders for Unconverted Configurations

A configuration the converter can't reproduce is created as a placeholder step that carries the agent's name, and the conversion report names it. Today every configuration in the measured matrix converts, so a placeholder appears only for a construct the export doesn't describe fully, such as a missing API configuration. By default a placeholder fails when the workflow reaches it, so a run can't report success on work that never happened.

Set `allow_unconverted_placeholders` to `true` to import each placeholder as a pass-through step instead. The run then continues past it and the placeholder's output is its input. Rebuild the capability with a native step when its result matters.

## Run the Converted Workflow

1. Open the new workflow in the project.
2. Set any project variables that came from Savant parameters.
3. Upload files for unbound sources to the paths in the report.
4. Run the workflow and review each step's output table.

## Known Limitations

- Date and timestamp conversions of text that isn't in a recognizable date format can fail the run on that row.
- Infer and Vision agents depend on a language model, so their answers differ from Savant's and between runs.
- A hierarchy deeper than 17 levels fails the run.
- A source with no declared columns that isn't a bound CSV, TSV, or TXT file keeps only the columns later steps reference. See [Files with No Declared Columns](#files-with-no-declared-columns).

## Related Guides

- [Savant Conversion Matrix](/reference/savant-conversion-matrix/)
- [REST Connection](/reference/connectors/rest/generic-rest/)
- [Add Document Accounts](/guides/documents/adding-accounts/)
- [Manage Workflow Variables](/guides/workflows/manage-workflow-variables/)
- [AI/NLP Step](/reference/workflow-steps/text-documents/nlp-ai/)
- [REST Request Step](/guides/workflows/rest-request-step/)
- [Run a Workflow](/guides/workflows/run-a-workflow/)
