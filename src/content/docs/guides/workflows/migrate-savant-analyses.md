---
title: Migrate Savant Analyses
description: Convert a Savant Labs analysis export into a PlaidCloud Advanced workflow through the REST API or an MCP-connected AI agent, bind its sources, and read the conversion report.
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
- An agent with no PlaidCloud equivalent arrives as a named placeholder step.

## Before You Start

1. Export the analysis from Savant with **Export JSON**.
2. Upload the `.json` file to a [Document account](/guides/documents/adding-accounts/) you can read.
3. Choose the PlaidCloud project that should receive the workflow. You need write access to it.
4. Choose a Document account and base folder where the analysis's source files will be read from.

## Convert an Analysis

Conversion is available through the REST API and the MCP tool catalog. Both take the same fields.

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
| `allow_unconverted_placeholders` | No | Controls what a placeholder does at run time. See [Placeholders for Unsupported Agents](#placeholders-for-unsupported-agents). |

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

## Read the Conversion Report

The response carries the conversion report: a summary of how many steps converted with high, medium, or low confidence and how many did not convert, plus warnings and the nodes the converter absorbed into others. Read it before you run the workflow. It names every placeholder, every unbound source and unmatched binding, and the table prefix used.

## Placeholders for Unsupported Agents

An agent with no PlaidCloud equivalent, or a configuration the converter doesn't reproduce, is created as a placeholder step that carries the agent's name. By default a placeholder fails when the workflow reaches it, so a run can't report success on work that never happened.

Set `allow_unconverted_placeholders` to `true` to import each placeholder as a pass-through step instead. The run then continues past it and the placeholder's output is its input. Rebuild the capability with a native step when its result matters. The matrix lists the PlaidCloud step to use for each agent.

## Run the Converted Workflow

1. Open the new workflow in the project.
2. Set any project variables that came from Savant parameters.
3. Upload files for unbound sources to the paths in the report.
4. Run the workflow and review each step's output table.

## Known Limitations

- Date and timestamp conversions of text that isn't in a recognizable date format can fail the run on that row.
- A JSON agent over text that isn't valid JSON can fail the run.
- An Adapter agent that passes through a source with no declared columns keeps only the columns later steps reference.

## Related Guides

- [Savant Conversion Matrix](/reference/savant-conversion-matrix/)
- [Add Document Accounts](/guides/documents/adding-accounts/)
- [Manage Workflow Variables](/guides/workflows/manage-workflow-variables/)
- [Run a Workflow](/guides/workflows/run-a-workflow/)
