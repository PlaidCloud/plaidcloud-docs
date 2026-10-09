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
- Every Savant agent type converts. A configuration the converter can't reproduce, such as a spatial match by distance, arrives as a named placeholder step.

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
| API Agent (`apiService`, and legacy `service` with an API service) | A [REST Request](/reference/workflow-steps/general/rest-request/) step that sends one request per input row, then a join back that keeps every input row. The response body lands in a text column. | The export carries no credentials, so requests go out unauthenticated; bind a REST connection whose base URL owns the host, or add headers. A method other than GET runs against the live system once per input row every time the workflow runs, so confirm the target before the first run. Non-GET requests aren't retried automatically. A secret in the URL is stored as a plain-text variable. A failed request leaves its row with an empty response. Only an `http://` or `https://` URL converts, and row data can't choose the host. |
| Recursion Agent (`hierarchy`) | A bounded walk up the parent chain: repeated inner joins, a union, an aggregate over each row's ancestors and itself, and a row-count check. A row with a blank parent, or naming itself as its parent, is a root. | A chain deeper than 17 levels, or a loop in the parent ids, fails the run at the depth check, and nothing downstream is written. |
| Search and Replace (`search_replace`) | A [Table Extract](/reference/workflow-steps/tables/table-extract/) that applies each find and replace rule in order to the chosen text columns, case-sensitive or not, whole word or not. | Rules are literal text, not patterns. |
| Spatial Match Agent (`spatial_match`) | A [Spatial Match (executor)](/reference/workflow-steps/spatial/spatial-match-executor/) step for intersects, within, contains, touches, crosses, overlaps, equals, and disjoint, with several rules combined; Cross Join for a cross match; [Find Nearest](/reference/workflow-steps/spatial/spatial-find-nearest/) for a nearest match. | A within-distance match isn't supported and arrives as a placeholder. |
| Spatial Summarize Agent (`spatial_summarize`) | [Spatial Combine](/reference/workflow-steps/spatial/spatial-combine/) for union, intersect, and bounding box, plus centroid and point-to-line steps for geometric center and line or polygon builds. | None beyond the matrix status. |

`GEO_POINT`, `GEO_TYPE`, and `GEO_SPATIAL_DISTANCE` convert to expressions. An edit whose whole expression is another `GEO_*` function, such as `GEO_AREA` or `GEO_UNION`, converts to the matching spatial step. Geometry travels as WKT text.

A source that reads binary files, such as the documents a Vision agent reads, converts to a document extract of the bound document, or of the file expected at the unbound sources path.

## Read the Conversion Report

The response carries the conversion report: a summary of how many steps converted with high, medium, or low confidence and how many did not convert, plus warnings and the nodes the converter absorbed into others. Read it before you run the workflow. It names every placeholder, every unbound source and unmatched binding, and the table prefix used.

## Placeholders for Unconverted Configurations

A configuration the converter doesn't reproduce, such as a spatial match by distance, is created as a placeholder step that carries the agent's name. By default a placeholder fails when the workflow reaches it, so a run can't report success on work that never happened.

Set `allow_unconverted_placeholders` to `true` to import each placeholder as a pass-through step instead. The run then continues past it and the placeholder's output is its input. Rebuild the capability with a native step when its result matters. 

## Run the Converted Workflow

1. Open the new workflow in the project.
2. Set any project variables that came from Savant parameters.
3. Upload files for unbound sources to the paths in the report.
4. Run the workflow and review each step's output table.

## Known Limitations

- Date and timestamp conversions of text that isn't in a recognizable date format can fail the run on that row.
- A JSON agent over text that isn't valid JSON can fail the run.
- Infer and Vision agents depend on a language model, so their answers differ from Savant's and between runs.
- A hierarchy deeper than 17 levels fails the run.
- An Adapter agent that passes through a source with no declared columns keeps only the columns later steps reference.

## Related Guides

- [Savant Conversion Matrix](/reference/savant-conversion-matrix/)
- [Add Document Accounts](/guides/documents/adding-accounts/)
- [Manage Workflow Variables](/guides/workflows/manage-workflow-variables/)
- [AI/NLP Step](/reference/workflow-steps/text-documents/nlp-ai/)
- [REST Request Step](/guides/workflows/rest-request-step/)
- [Run a Workflow](/guides/workflows/run-a-workflow/)
