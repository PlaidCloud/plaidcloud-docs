---
title: Migrate KNIME Workflows
description: Convert a KNIME workflow (.knwf) or workflow group (.knar) into PlaidCloud Advanced workflows from the Analyze app, the REST API or an MCP-connected AI agent, bind its inputs and connections, and read the conversion report.
sidebar:
  order: 31.7
---

PlaidCloud is a drop-in replacement for KNIME. 98.5% of KNIME node configurations convert fully, and 205 of the 207 core node types are Full: each becomes standard PlaidCloud workflow steps that do the node's work. The converter turns a KNIME workflow archive into runnable Advanced workflows, keeps the original graph, and returns a conversion report that names anything you need to set. The [KNIME Conversion Matrix](/reference/knime-conversion-matrix/) lists every node.

Conversion reads only the archive you point it at. It never contacts the system a KNIME node reads from or writes to.

Conversion is a one-time step. Converting the same archive again creates new workflows, and edits you made in PlaidCloud are never merged with a later export.

## What PlaidCloud Creates

- One Advanced workflow for each KNIME workflow. A `.knwf` gives one workflow, and a `.knar` gives one for every workflow in the group.
- Each KNIME node becomes the matching workflow step, project variable, or canvas object, with upstream and downstream relationships preserved. Metanodes and components are flattened into the workflow, so their nodes run as ordinary steps.
- Flow variables, and Configuration and Widget nodes, become project variables holding their defaults. Switches and loops whose values are known when you convert are pruned and expanded into the steps they run.
- The KNIME expression languages — Expression, String Manipulation, Math Formula, Column Expressions, and Rule Engine — convert to PlaidCloud expressions.
- Data files that ship inside the archive are uploaded to a `knime/` folder in the project's default Document account, one folder per workflow, and the converted readers import them from there.
- Views, charts, and color managers have no data effect. They are dropped and listed in the conversion report.

## Before You Start

1. Export the workflow from KNIME Analytics Platform as a `.knwf` file. To convert several workflows at once, export their workflow group as a `.knar` file. Keep the files your readers use in the workflow's `data` folder so they ship inside the archive.
2. Upload the archive to a [Document account](/guides/documents/adding-accounts/) you can read. In the Analyze app, **Browse** on the import window uploads it from your computer.
3. Choose the PlaidCloud project that should receive the workflows. You must be an Architect or Manager of the project, and the project must have a default Document account.
4. Note the PlaidCloud tables, files, and connections you want the workflow's readers and connector nodes to use. See [Bind Sources](#bind-sources).

## Convert a Workflow

Convert from the Analyze app, the REST API or an MCP-connected AI agent. The REST API and the MCP tool take the same fields; the window takes the ones it shows.

### Analyze App

1. Open **Analyze** and choose **Tools → Import KNIME Workflow**.
2. Under **Import Source and Target**, choose the **Target Project** and the **KNIME Archive (.knwf or .knar)** in a Document account. Select **Browse** to upload the archive from your computer.
3. Under **Object Prefixes**, optionally set the **Workflow Prefix**, **Step Prefix** and **Table Prefix**. The table prefix defaults to the workflow's name.
4. Under **Source Bindings (optional)**, optionally bind a reader to an existing table in the target project: select **Add**, then enter the **KNIME Reader** (its node id, such as `12:3`, its node name or its file name) and the **Table ID**. To bind connections, documents or tables in other projects, use the REST API or the MCP tool. See [Bind Sources](#bind-sources).
5. Select **Import**.

The window shows progress while it converts the archive, then the conversion report: step counts (**Steps**, **High confidence**, **Medium**, **Low** and **Not converted**), the nodes that could not be converted and the steps downstream of them, partial conversions, warnings, the source files to upload, and the nodes with no step. A conversion with nothing to review says so and the window closes on its own.

### Fields

| Field | Required | What it does |
| --- | --- | --- |
| `source_account_id` | Yes | Document account that holds the KNIME archive. |
| `source_file_path` | Yes | Path of the `.knwf` or `.knar` file within that account. |
| `project_id` | Yes | Project where the workflows are created. |
| `workflow_prefix` | No | Prefix added to workflow names. |
| `step_prefix` | No | Prefix added to step names. |
| `table_prefix` | No | Prefix added to table names. Defaults to the workflow's own name. A prefix that would reuse an existing table name is refused before anything is created. For a `.knar`, each workflow's prefix is followed by that workflow's name. |
| `source_bindings` | No | Binds readers and connector nodes to data and connections you already have, up to 500 entries. See [Bind Sources](#bind-sources). |

### REST

Send the fields as a JSON body to:

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

An MCP-connected AI agent calls the `knime_convert` tool with the same fields. See [AI Agents (MCP)](/integrations/ai-coding-agents/) to connect an agent. The tool changes your project, so review the call before you approve it.

## Bind Sources

Use `source_bindings` to point a KNIME reader at data that already exists in PlaidCloud instead of the copy in the archive. A key is a node id (such as `12:3`), a node name, a bundled file path (such as `data/sales.csv`), or a file name; the first match in that order wins. A value is one of:

- An `analyzetable_` id for a table in the target project. The table replaces the reader.
- `{"project": "<project id>", "table": "<table id>"}` for a table in another project you can read. The reader becomes an [Import Project Table](/reference/workflow-steps/import/import-project-table/) step that copies it. The source project must share Read with the target project, or the step warns. A table governed by row access is refused.
- `{"account": "<document account id>", "path": "/finance/budget.xlsx"}` for a document you can read. The reader imports it.
- `{"connection": "<connection id>"}` for a database or REST connector node. The converted steps run on that connection.

The Analyze app window binds readers to tables in the target project by table id. Bind connections, documents and tables in other projects through the REST API or the MCP tool.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "data/budget.xlsx": { "account": "<document account id>", "path": "/finance/budget.xlsx" }
}
```

A bound table that does not exist, or a key that matches no reader, is a warning. The bindings applied, with their project and table names, are listed in the conversion report under `bindings`.

### Unbound Inputs

A reader whose file is not in the archive reads from `inputs/<file name>` in the workflow's folder of the default Document account, and the conversion report lists the path under `missing_inputs` with a warning. Upload the file there and run the workflow. Until the file is there, the import finishes with a warning and creates an empty table, and the workflow continues.

## Credentials and Connections

KNIME credentials are never migrated. Each step that signs in to another system reads its credentials from a PlaidCloud connection or a project variable you set, and the step's warning in the conversion report says which.

| KNIME | What You Set |
| --- | --- |
| Database connectors | A database connection: bind it with `{"connection": "<id>"}` or pick it on the step. |
| REST and web service nodes that sign in | A [REST connection](/reference/connectors/rest/generic-rest/): bind it with `{"connection": "<id>"}` or pick it on the step. |
| Speech Recognizer (IBM Watson) | A REST connection whose base URL is the Watson service URL the warning names, with the user `apikey` and your API key as its Basic login. Bind it to the node. |
| Email Connector, with Email Reader or Email Mover | A project variable holding the mail server password, with the name the warning gives. The host and user come from the Email Connector. |
| Excel Reader or Excel Writer with a workbook password | A project variable holding the password, with the name the warning gives. |
| LLM connectors and authenticators | An LLM connection on the AI step. |

See [Manage Workflow Variables](/guides/workflows/manage-workflow-variables/) to set project variables.

## Read the Conversion Report

The Analyze app window shows the conversion report when the import finishes, and the REST and MCP responses carry it. Read it before you run the workflows.

- `summary` counts the steps created and how many mapped with high, medium, or low confidence.
- `warnings` lists each warning with its node, step, and the action to take, including every credential or connection to set.
- `missing_inputs` lists the Document paths to upload files to for unbound inputs.
- `bindings` lists the bindings applied.
- `table_prefix` is the prefix used. For a `.knar`, `workflows` lists each workflow with its own prefix.
- `uploaded_files`, beside the report, lists the bundled files uploaded to the default Document account.
- `dropped_tools` lists the views and charts that were dropped.

## Placeholders

A node without a conversion path stays on the canvas as a named placeholder. The placeholder passes its data through and warns with the KNIME node's name, and every step downstream of it is flagged in the report, so a missing result is never silent. Rebuild the capability with a standard step when its result matters.

## Run the Converted Workflow

1. Open the new workflow in the project.
2. Set the project variables and connections the warnings name.
3. Upload files for unbound inputs to the paths under **Source files to upload** in the window, or in `missing_inputs`.
4. [Run the workflow](/guides/workflows/run-a-workflow/) and review each step's output table.

## Edge Cases

These are the only known differences from KNIME.

- **Crosstab.** Converts to [Table: Pivot](/reference/workflow-steps/tables/table-pivot/). A few settings combinations give results that differ from KNIME.
- **Loop End (Column Append).** Converts to [Table: Inner Join](/reference/workflow-steps/tables/table-inner-join/). A few settings combinations give results that differ from KNIME.
- **Random draws.** Row Sampler, Table Partitioner, and Equal Size Sampling make KNIME's own random draw with [Table: KNIME Random Sample](/reference/workflow-steps/tables/table-knime-random-sample/), so a node with a seed selects the same rows as in KNIME. The draw takes a table of at most 10,000,000 rows; a larger table fails the step.

## Related Guides

- [KNIME Conversion Matrix](/reference/knime-conversion-matrix/)
- [REST Connection](/reference/connectors/rest/generic-rest/)
- [Add Document Accounts](/guides/documents/adding-accounts/)
- [Manage Workflow Variables](/guides/workflows/manage-workflow-variables/)
- [Run a Workflow](/guides/workflows/run-a-workflow/)
