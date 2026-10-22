---
title: Savant Conversion Matrix
description: How PlaidCloud converts Savant Labs analyses into native Advanced workflows, with the mapping tier of each agent and the few named edge cases.
sidebar:
  order: 7
---

PlaidCloud converts Savant Labs analyses into native Advanced workflows. The
importer maps each Savant agent to a workflow step, project variable, or
canvas object, so a converted workflow runs cloud-native.

To run a conversion, see [Migrate Savant Analyses](/guides/workflows/migrate-savant-analyses/).

Each agent has a mapping tier. **Full** means every option of the agent has a
valid mapping to a PlaidCloud step. Constructs refused by name are listed
under Named Refusals.

External-system connectors are **connected, not converted** — see
[Connecting to External Systems](#connecting-to-external-systems).

## Agent Support

All 33 agents convert at Full.

| Agent | Tier | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Adapter Agent (`adapter`) | Full | Select and schema projection step | Renames, retypes, and orders fields. |
| API / Infer Agent (legacy service) (`service`) | Full | Same as the API or Infer Agent, by serviceType | An LLMService converts as the Infer Agent and an APIService as the API Agent; a missing or misspelled serviceType is read from the node's keys with a warning. |
| API Agent (`apiService`) | Full | Table Extract, [REST Request](/reference/workflow-steps/general/rest-request/), and a left join back | One GET, POST, PUT, PATCH or DELETE request per input row; the raw response body lands in a text column, HTTP errors stay as rows, every input row is kept, and a quota per period becomes a fractional requests-per-second. A relative URL joins its api_bindings base URL or REST connection host; a host, port or path from a row field is substituted per row; next-URL, Link-header, offset and page paging are followed, including a start, page size or parameter name templated from a row field. |
| Blend Agent (`blend`) | Full | [Inner Join](/reference/workflow-steps/tables/table-inner-join/), [Outer Join](/reference/workflow-steps/tables/table-outer-join/), [Anti Join](/reference/workflow-steps/tables/table-anti-join/) | Inner, left, right, full, anti and outer-excluding-inner blends, OR-joined, contains and is-part-of conditions, with matched and unmatched streams; columns a pivot or parse names only at run time are carried through. |
| Dedupe Agent (`deduplicate`) | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with distinct rows | Keeps the first record per key, within Group By groups, and routes duplicates to a second stream or flags them. |
| Destination Agent (`destination`) | Full | [Export: CSV](/reference/workflow-steps/export/export-to-csv/), [Export: Excel](/reference/workflow-steps/export/export-to-excel/), Export: Parquet, JSON, Avro or XML, [Export to PDF](/reference/workflow-steps/export/export-to-pdf/), [Export: Tableau Hyper](/reference/workflow-steps/export/export-hyper/) with [Publish to Tableau](/reference/workflow-steps/export/export-to-tableau/), [Export: External Database Tables](/reference/workflow-steps/export/export-external-tables/), [Export to Google Spreadsheet](/reference/workflow-steps/export/export-to-google-spreadsheet/), [Notify via Slack](/reference/workflow-steps/notifications/notify-via-slack/), or email | Writes through destination_bindings to a document account (CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF or a Tableau .hyper, in any Java charset, including aliases, CESU-8 and byte-order-mark forms; a character the charset lacks is written as ?), a connection table, a Google Sheet, a Tableau data source or a Slack channel, or email recipients. An unbound destination writes a project table or a Document file instead (see Where It Goes below). A file, sub-folder or tab per field value splits CSV, Excel, Parquet and PDF files and Google Sheets tabs; a template seeds every workbook of a split. Excel options map: blank values go to `Sheet1`, colliding sheet names get a suffix, `formatFromTemplate`, `topLeftCell` and mode `create`. Append, upsert, update and groupReplace merge on the match keys (a file or table is read back and rewritten; a split reads back the file each value of the run is written to and merges within it, leaving the other files as they are; Tableau updates its rows in place). Columns only the data names (a promoted header's, a pivot's values, a parsed JSON's or XML's keys) are written beside the known ones by every export and table write, sorted and split on, and appended or merged into a table, or into a file read back with every column it has. |
| Explode Agent (`explode`) | Full | [Cross Join](/reference/workflow-steps/tables/table-cross-join/) | Cross-joins a small side against the main stream. |
| Filter Agent (`filter`) | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a filter expression | Splits records by wizard or expression into true and false paths. |
| Filter Pushdown (`pdfilter`) | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a filter expression | Database-side filter, converted the same as Filter. |
| Format Agent (`format`) | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with column renames, or Promote Header | Hides, retypes, renames and fills fields matched by name (contains, starts with, ends with) or by being empty; a fill writes its default into any column whose type the default casts to (text, number, date). Header-row promotion and is-empty matching run at run time in the Promote Header step, and a promoted header reads every column of its file. |
| Fuse Agent (`fuzzy_match`) | Full | [Fuzzy Match](/reference/workflow-steps/tables/table-fuzzy-match/), between a Union All and two joins | Stacks both inputs, matches records on the key fields at a similarity threshold of 80, and joins both sides back with a Confidence Score. |
| Group (`group`) | Full | Canvas container | Preserved as workflow organization. |
| Infer Agent (`gen_ai`) | Full | [AI/NLP](/reference/workflow-steps/text-documents/nlp-ai/) prompt task | The prompt runs per row over the input fields on the visible LLM connection matching Savant's provider and model; the answer lands in an AI Answer column beside every input column. rowLimit caps the rows answered per run and keeps earlier answers: a row answered before (same prompt, model and input values) keeps its answer, and only unanswered rows count toward the limit. |
| JSON Agent (`json`) | Full | [JSON Parse](/reference/workflow-steps/tables/table-json-parse/) | Flattens a JSON field into dotted-key columns, or explodes an array into one row per element; the keys are read from the data at run time. |
| Notes Agent (`notes`) | Full | Canvas annotation | Preserved as workflow context. |
| Pivot Agent (`pivot`) | Full | [Pivot](/reference/workflow-steps/tables/table-pivot/) | Pivots rows to columns with aggregation. |
| Recursion Agent (`hierarchy`) | Full | Hierarchy Closure, [Table Extract](/reference/workflow-steps/tables/table-extract/), and [Multi-Table Join](/reference/workflow-steps/tables/table-multi-table-join/) | Walks a parent/child tree to any depth, aggregating each node over the ids on its path to the root, itself included, and writing Depth and Path; a loop stops at the repeated node. |
| Sample Agent (`sample`) | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a row limit | Keeps the first N rows, optionally per group, a random percent or N rows, or one row in every N. |
| Search and Replace (`search_replace`) | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with nested replace expressions, split across stages | Find/replace rules (contains or matches; replace or append), case-sensitive or not, whole word or not, applied in order over the chosen text fields, or every text field when none is named. |
| Source Agent (`source`) | Full | Import steps bound through `source_bindings` ([Import: CSV](/reference/workflow-steps/import/import-csv/), [Import: Excel](/reference/workflow-steps/import/import-excel/), [Import: SQL](/reference/workflow-steps/import/import-sql/)) or an existing table | Reads the bound table or document; an unbound source creates an empty import and a warning. XML text reads its document through Import XML (an unbound one reads savant/<workflow>/<name>.xml). A source bound to an XML document also writes the export's other columns: a file name or path column from the document, the rest blank. A source below a Format that promotes a header row reads every column of its CSV, Excel (including Excel 97 .xls), JSON, Parquet or Avro file by position. |
| Spatial Match Agent (`spatial_match`) | Full | [Spatial Match (executor)](/reference/workflow-steps/spatial/spatial-match-executor/), [Cross Join](/reference/workflow-steps/tables/table-cross-join/), or [Find Nearest](/reference/workflow-steps/spatial/spatial-find-nearest/) | Intersects, within, contains, touches, crosses, overlaps, equals, disjoint and and/or multi-rule matches, geodesic within distance between any geometries (points, lines, polygons: the least distance on a 6371 km sphere), nearest N by that same distance with a maximum distance (a lone nearest rule writes no Distance column, as Savant's writes none; combined with other rules as nearest-then-filter, AND joins and OR unions, each nearest rule adds a Distance column of its own), and Cross, with matched and unmatched streams. |
| Spatial Summarize Agent (`spatial_summarize`) | Full | [Spatial Combine](/reference/workflow-steps/spatial/spatial-combine/), Spatial Centroid, and point-to-line steps | Union, intersect, bounding box, one or several geometric centers, and polyline or polygon builds, per group with an optional sort. |
| Split Agent (`split`) | Full | Split Text, or [Table Extract](/reference/workflow-steps/tables/table-extract/) with split_part columns | Splits a text field on a literal separator of any length into rows or columns, with trim and keep-original; the number of columns is read from the data at run time. |
| Split Output (`outlet`) | Full | Workflow edge | Routes a named output to its consumers. |
| Stack Agent (`multi_stack`) | Full | [Union All](/reference/workflow-steps/tables/table-union-all/) | Stacks any number of inputs by name or position. |
| Summarize Agent (`summarize`) | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with aggregation | Groups and aggregates, including first/last by a deterministic sort and per-row window aggregates (useWindow). |
| Summarize Pushdown (`pdsummarize`) | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with aggregation | Database-side aggregation, converted the same as Summarize. |
| Text (`text`) | Full | Canvas annotation | Preserved as workflow context. |
| Time Series Agent (`rollup`) | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) aggregation over a period-bucket expression, Period Spine, [Anti Join](/reference/workflow-steps/tables/table-anti-join/) and [Union All](/reference/workflow-steps/tables/table-union-all/) | Rolls records up to day, week, month, quarter, year or decade periods between optional start and end dates, per group, excluding NULL dates and zero-filling empty periods. |
| Transform Agent (`edit`) | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with column expressions | Calculated columns, type changes, and window calculations (lag, lead, cumulative sum, row number, forward and backward fill), evaluated in order. |
| Unpivot Agent (`unpivot`) | Full | [Melt](/reference/workflow-steps/tables/table-melt/) | Converts columns to rows as a name/value pair. |
| Vision Agent (`vision`) | Full | [Image OCR](/reference/workflow-steps/text-documents/image-ocr/), then the [AI/NLP](/reference/workflow-steps/text-documents/nlp-ai/) prompt task | Each document goes to the provider as an image or PDF when it accepts that type and size, else its PDF text layer or OCR text is sent; the prompt's answer lands in an AI Answer column. |
| XML Agent (`xml`) | Full | [XML Parse](/reference/workflow-steps/tables/table-xml-parse/) | Selects elements, extracts child values and attributes into columns, or converts XML to JSON; a simple //a/b path converts as before and any other XPath 1.0 path (predicates, attribute tests, wildcards, functions such as count(), name() and contains()) is evaluated as XPath, namespace-aware or as written. |

Wiring, canvas, and pushdown variants (Split Output, Group, Text, Filter Pushdown, Summarize Pushdown) are Savant node types without a help-center agent article of their own; each converts as the agent it mirrors.

A credential in an API Agent request is never copied into a workflow step. Over https it moves into a REST connection; over http, without permission to write connections, or in a conversion made through MCP it is withheld with a warning. This is by design and does not lower the tier.

Two destination limits do not lower the tier. A few rare charsets (for example `x-ISCII91` or `JIS_X0212`) cannot be written; the file is written as UTF-8 and the conversion warns. A Tableau publish that merges on keys needs `replace: true` in its destination binding; without it the conversion warns and publishes a new data source, which fails on a run where one exists.

## Named Refusals

Nine constructs are refused by name rather than converted. None lowers an agent's tier.

| Construct | Why It Is Refused |
| --- | --- |
| An API Agent request that carries a credential and takes its host from an input field | Each row could send the credential to a host the data chooses. The request becomes a named placeholder. A request without a credential, and a credential on a fixed host, convert. |
| A Copilot edit that has only its prompt | The prompt is not a formula, and Savant does not document how the pipeline it compiles from the prompt combines its steps. |
| A Transform edit with no expression whose compiled pipeline chains several steps | Savant does not document how the chained steps combine. A one-step pipeline converts. |
| A regex construct in a Transform or Filter expression that PlaidCloud cannot read: a class inside a class, a class intersection (`&&`), or an unknown `\p{}` property | The step becomes a named placeholder that refuses at run time. |
| An aggregate or window function in a Transform or Filter expression | Savant itself fails on it at run time. As a Transform calculation or in a Summarize it converts. |
| `HASH` in a Transform or Filter expression with a literal algorithm other than `md5` or `sha1` | Savant itself fails on it (the algorithm is `md5` or `sha1`). An algorithm read from a column converts, giving NULL for any other value. |
| A destination sort on a column its input does not carry | Savant itself fails on it at run time. |
| A destination file, sub-folder, tab or worksheet per value of a column its input does not carry | Savant itself fails on it at run time. |
| An XML Agent path that is not XPath 1.0 | Savant cannot run it either. |

A relative API URL converts when you bind a base URL or REST connection with `api_bindings`; see [Convert-Time Bindings](/guides/workflows/migrate-savant-analyses/#convert-time-bindings).

## Expression Language

Savant expression functions and operators convert to PlaidCloud expressions. Tier: **Full**. Every function and format converts, including `TO_TEXT` with a numeric pattern, a format known only per row, fractional-second, week-based, quarter and zone date tokens, two-digit years, and Java regex constructs. GEO_* functions anywhere in an expression run in companion Spatial steps. The exceptions are the [named refusals](#named-refusals).

Known edge cases: `TO_DATE` or `TO_DATETIME` with a format holding a `[`, `]`, quote, backslash or `^` literal, on text that reads into 9999-12-30 or 9999-12-31, which is past the last timestamp the warehouse holds; the conversion warns.

## Export Formats

The loader accepts every Savant export shape — flat, model-wrapped, server-record, recipe envelope, array-wrapped, BOM-prefixed, and legacy type aliases — and normalizes them into one model. Tier: **Full**.

## Analysis Parameters

Savant analysis parameters convert to workflow variables, and references to them inside node configs are rewritten to the PlaidCloud variable syntax. List, dictionary, and aliased parameter shapes all load. Tier: **Full**.

Known edge cases: A parameter whose name holds a secret word or whose value looks like a credential becomes a variable with a blank value, with a warning. A parameter a node uses that the export does not declare becomes a variable with an empty value, with a warning.

## Connecting to External Systems

Savant connectors are source and destination targets, not steps, and an export carries no datasets or credentials. PlaidCloud reaches these systems through a connection rather than through a node on the canvas.

| Savant | Where It Goes in PlaidCloud |
| --- | --- |
| Source connector | `source_bindings` maps the Savant node or dataset to a PlaidCloud table or a Document file, read through the matching import step; an unbound source warns and processes nothing |
| Destination: CSV, Excel and other file formats | An export step ([Export: CSV](/reference/workflow-steps/export/export-to-csv/), [Export: Excel](/reference/workflow-steps/export/export-to-excel/), [Export to PDF](/reference/workflow-steps/export/export-to-pdf/)) |
| Destination: Google Sheets, Tableau, Slack | [Export to Google Spreadsheet](/reference/workflow-steps/export/export-to-google-spreadsheet/), [Publish to Tableau](/reference/workflow-steps/export/export-to-tableau/), or [Notify via Slack](/reference/workflow-steps/notifications/notify-via-slack/), through a connection you bind with `destination_bindings` |
| Destination: unbound database, warehouse or SaaS target (Oracle, generic database, Looker Studio, NetSuite, SAP, and Google Sheets, Tableau or Slack with no connection bound) | A project table named after the destination node, with a warning naming the original target |
| Destination: unbound file-system target (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | The file, in the destination's file type, in a Document folder that mirrors the target folder, with a warning. Credentials and share tokens are dropped from the folder path |
| Destination: unbound email | A CSV with a warning |
| Destination: binding that can't be used | A CSV with a warning naming the original target |

Conversion never contacts the source or destination system.

