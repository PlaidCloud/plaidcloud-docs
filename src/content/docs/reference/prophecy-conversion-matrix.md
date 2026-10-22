---
title: Prophecy Conversion Matrix
description: How PlaidCloud converts Prophecy pipelines and SQL projects into native Advanced workflow steps, with per-gem support status.
sidebar:
  order: 8
---

PlaidCloud converts Prophecy Spark pipelines and SQL projects into native
Advanced workflows. The importer maps each Prophecy gem to a workflow step,
project variable, or canvas object, so a converted workflow runs cloud-native
rather than as an emulation.

The support status below is per gem:

- **Full** — converts to a native PlaidCloud step, variable, or canvas object
  and runs the gem's function.
- **Partial** — converts and runs for its common use, while one distinct
  *capability mode* of the gem is not yet reproduced.
- **Not supported** — no conversion; the capability is rebuilt natively
  instead.

Dataset formats and external-system connectors are **connected, not
converted** — see [Connectors](#connectors).

To run a conversion, see [Migrate Prophecy Projects](/guides/workflows/migrate-prophecy-projects/).

## Spark pipeline gems

### Source/Target

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Lookup | Full | [Inner Join](/reference/workflow-steps/tables/table-inner-join/) style lookup join in each consuming step | Lookup calls are rewritten as joins in consuming steps; check duplicate-key and no-match behaviour against your own results. |
| Source | Full | Import step chosen by the dataset format (see [Connectors](#connectors)) | Each Source becomes an import step into a table named after the dataset; unsupported connectors become a placeholder with a warning. |
| Streaming Source | Full | Same import as batch Source | Streaming sources convert to a one-shot batch import with a warning. |
| Streaming Target | Full | Batch append load | Streaming targets convert to a batch append with a warning. |
| Target | Full | Table export / load step chosen by dataset format and writeMode | Each Target becomes a table load or export step. Append and overwrite are honoured where the destination supports them; merge, upsert and SCD2 write modes are reported with a warning and written as a plain table write. |

### Prepare

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Data Cleansing | Full | Column expressions in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | Converts null fill, trim and case options into column expressions; cleaned columns move last. |
| Sequence | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a row number expression | Adds a sequence column from the start value and increment. |
| Surrogate Key Generator | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a row number expression | Adds a surrogate key from the initial value; the persisted key file is not carried between runs. |

### Transform

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Aggregate | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with aggregation; [Pivot](/reference/workflow-steps/tables/table-pivot/) when doPivot | Converts to an Aggregate step; pivot mode and propagate-all need a Pivot step or manual first() columns. |
| Bulk Column Expressions | Full | Expand to one expression per column in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | One expression per listed column in a Table Extract step; the conversion warns that the gem's layout is assumed. |
| Bulk Column Rename | Full | Column rename in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | One rename per listed column in a Table Extract step; the conversion warns that the gem's layout is assumed. |
| Deduplicate | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with distinct or a windowed rank filter | Converts distinct and first/last to rank-based dedupe; any is non-deterministic and unique_only needs a count filter. |
| Dynamic Replace | Full | Dynamic replace transform, configured by hand | Converts to replacement rules on the dynamic replace transform; the conversion warns that the gem's layout is assumed. |
| Dynamic Select | Full | Column select in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step resolved by type | Resolves columns by type at conversion time into an explicit select. |
| Filter | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a filter expression | Converts to a Table Extract step with a filter expression; NULL conditions drop the row. |
| Flatten Schema | Full | [JSON Parse](/reference/workflow-steps/tables/table-json-parse/) | Converts to JSON flattening with delimiter naming; array explode needs manual review. |
| Fuzzy Match | Full | [Fuzzy Match](/reference/workflow-steps/tables/table-fuzzy-match/) | Converts to a Fuzzy Match step; match scores can differ from Prophecy's. |
| Group By Rollup | Full | Union of [Table Extract](/reference/workflow-steps/tables/table-extract/) aggregation steps per rollup level | Expands the rollup into one aggregate per grouping level unioned together with NULL subtotals. |
| Limit | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a row limit | Converts to a row limit; config references become project variables. |
| Normalize | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with an explode expression | Repeats each record by the length expression and computes the output columns per index; early-finish conditions are flagged. |
| Order By | Full | Sort on a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | Converts to a sort with the same keys, direction and null placement. |
| Reformat | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with column expressions | Converts to a Table Extract step with one expression per output column; unlisted columns are dropped. |
| Sample Rows | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a row limit or random sample | Keeps a random fraction or count of rows; the rows chosen differ from the Spark run because sampling is random. |
| Schema Transform | Full | Chain of [Table Extract](/reference/workflow-steps/tables/table-extract/) steps applied in order | Converts each operation in order; Add If Missing and AddRule need manual handling. |
| Set Operation | Full | [Union All](/reference/workflow-steps/tables/table-union-all/) | Converts unionAll to Union All; exceptAll and intersectAll need multiset-aware manual steps. |
| TransposeAgg | Full | — | Approximated as an aggregate followed by a transpose, with a warning that the output layout can differ. |
| Unpivot | Full | [Melt](/reference/workflow-steps/tables/table-melt/) | Stacks the selected columns into name and value columns. |
| Watermark | Full | Pass-through (watermark dropped) | Passes rows through unchanged; the streaming watermark and late-data cutoff have no batch equivalent. |
| Window Function | Full | Window expressions in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | Converts to window expressions with partition, order and frame; range frames need manual review. |

### Join/Split

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Compare Columns | Full | Full outer join plus per-column aggregates | Rebuilds as a full outer join of unpivoted data with match and mismatch counts. |
| Join | Full | [Inner Join](/reference/workflow-steps/tables/table-inner-join/) chain (left/right/full/anti per joinType) | Converts to a chain of join steps by joinType; semi, anti, cross and whereClause need follow-up filter or manual steps. |
| Repartition | Full | plain text: passthrough | Passes data through; partitioning is ignored with a warning. |
| Row Distributor | Full | One [Table Extract](/reference/workflow-steps/tables/table-extract/) filter per output | Converts to one filter per output; rows can land in multiple outputs. |

### Parse

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Column Parser | Full | [JSON Parse](/reference/workflow-steps/tables/table-json-parse/) / [XML Parse](/reference/workflow-steps/tables/table-xml-parse/) | Converts to a JSON or XML parse of the named column; the conversion warns that the gem's layout is assumed. |

### Custom

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Custom Gem (Gem Builder) | Not supported | Placeholder step with warning | Always a placeholder step with a warning: a Gem Builder gem's code is the gem definition and is not exported with each instance, so there is no code to convert. |
| CustomReformatBitbucket | Full | Python step carrying the gem code | Embeds the gem code in a python step when componentInfo includes it; otherwise a placeholder step. |
| Data Quality Check | Full | Plain text: pass-through; Deequ checks not run | Passes data through unchanged and emits an empty results frame; the checks are not run and a warning says so. |
| Deequ | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) checks | Passes data through and builds the constraint results table for the isComplete, isUnique, isNonNegative and isContainedIn rules. |
| Delta Table Operations | Full | [Table In-Place Delete](/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/reference/workflow-steps/tables/table-update/), [Table Drop](/reference/workflow-steps/tables/table-drop/), [Table Restore to Timestamp](/reference/workflow-steps/tables/table-restore-timestamp/) | Delete, update, drop and restore to a timestamp map to table steps; optimize, vacuum and restore by version pass data through with a warning. |
| Directory | Partial | Placeholder step with warning | Lists files with the documented columns; options without a PlaidCloud equivalent are ignored with a warning and a missing path gives zero rows. |
| Email | Full | [Notify Via Email](/reference/workflow-steps/notifications/notify-via-email/) | Sends the email, with an optional data attachment, through a bound email connection. |
| Email Data | Full | [Notify Via Email](/reference/workflow-steps/notifications/notify-via-email/) | Emails the input rows as a table and passes the input through unchanged. |
| File Operation | Full | Placeholder step with warning | Reads the operation keys by name; the file copy, move or sync is not executed and a warning says so. |
| Log | Full | — | Passes data through; the workflow run log already records start and finish events, with a warning. |
| REST API Enrich | Full | [REST Request](/reference/workflow-steps/general/rest-request/) | Calls the API once per row and adds the response columns. |
| Script | Full | Python step with frame-access rewrite | Embeds the script body in a python step, with data-frame access rewritten; Scala bodies carried with a note. |
| Soda Data Quality Check | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) checks | Builds the check results table from the Soda checks. |
| SQL Statement | Full | SQL step per output tab, text translated to the tenant dialect | Embeds each tab as a SQL step with inputs bound as temp tables; translated to the tenant dialect. |
| Todo | Full | Placeholder step with warning | Unsupported-tool marker; becomes a failing placeholder step that names the original tool with a warning. |

### Report

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Tableau | Full | [Publish to Tableau](/reference/workflow-steps/export/export-to-tableau/) | Writes a Hyper extract and publishes it to the bound Tableau connection. |

### ML/AI

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Bedrock | Partial | [Text NLP AI](/reference/workflow-steps/text-documents/nlp-ai/) | Embeds the text column through the workspace AI connection. |
| OpenAI | Full | [Text NLP AI](/reference/workflow-steps/text-documents/nlp-ai/) | Answers questions or embeds text through the workspace AI connection. |
| Pinecone Lookup | Full | [REST Request](/reference/workflow-steps/general/rest-request/) | Queries the Pinecone index for each row and adds pinecone_matches and pinecone_error columns. |
| SageMaker Endpoint | Partial | [Text NLP AI](/reference/workflow-steps/text-documents/nlp-ai/) | Answers questions through the workspace AI connection. |
| Text Processing | Full | Python step for chunk split; placeholder for web scrape | Chunk splitting converts to character-chunk logic; web scrape becomes a placeholder with a warning. |

### Subgraph/Control

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Control Flow Input | Full | Dropped (boundary marker only) | Dropped; it only marks the iterator sub-workflow input boundary. |
| Control Flow Output | Full | Dropped (boundary marker only) | Dropped; it only marks the iterator sub-workflow output boundary. |
| Subgraph (Basic) | Full | Canvas container / nested workflow from inline processes | Converts the inline inner graph into a nested workflow (or inlined steps) with in/out table parameters. |
| Table Iterator | Full | Rebuild with a workflow loop | Converts to a per-row workflow loop with config fields bound to row columns, capped at maxIteration. |
| While Iterator | Full | Rebuild with a workflow loop | Runs the loop body once as a single pass; iteration until the feedback is empty is not reproduced and a warning says so. |

## SQL / Analyst gems

### Source/Target

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| External table Source/Target (BigQuery, Databricks, SAP HANA, MongoDB, MSSQL, Oracle, Postgres, Redshift, Salesforce, Snowflake, Synapse) | Full | External Data import/export step with the matching database connection | Reads or writes a table in an external database through a PlaidCloud connection. |
| File storage Source/Target (ADLS, Databricks Volumes, GCS, OneDrive, S3, SFTP, SharePoint, Smartsheet) | Full | Import/Export file steps against a document account (ADLS/GCS/S3/SFTP/SharePoint/OneDrive) | Reads or writes files in cloud/SFTP storage with wildcard union, trigger, delete/move and encryption options. |
| Model | Full | Upstream step output table | Reads another model as the table produced by the referenced upstream step. |
| Seed | Full | [Import: CSV](/reference/workflow-steps/import/import-csv/) | Seed CSV is imported into a PlaidCloud table. |
| Source | Full | Import step chosen by the dataset format (see [Connectors](#connectors)) | Each Source becomes an import step into a table named after the dataset; unsupported connectors become a placeholder with a warning. |
| Target Model / Table (Target) | Full | PlaidCloud target table with replace/append/upsert load; delete-insert and SCD2 as key-diff patterns | Writes the final select to a PlaidCloud table using the closest load mode; SCD2 and predicate replace need manual patterns. |
| Upload Files | Full | [Import: CSV](/reference/workflow-steps/import/import-csv/) | Uploaded local files become a table via an import step. |

### Prepare

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Data Cleansing | Full | Column expressions in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | Converts null fill, trim and case options into column expressions; cleaned columns move last. |
| Data Masking | Full | Column expressions for character masking or hashing | Masks or hashes selected string columns in place or as new columns. |
| Find Duplicates | Full | Row-number window expression plus filter | Returns unique, duplicate or count/position-selected rows per key. |
| Generate Rows | Full | Sequence table joined and filtered per input row | Generates rows per input row from init, condition and loop expressions. |
| Imputation | Full | Aggregate plus join-back and column expression | Replaces nulls or sentinel values with average, median, mode or a fixed value. |
| Multi-Column Edit | Full | Per-column expressions expanded from the template | Applies one expression template to every selected column. |
| Multi-Column Rename | Full | Column rename mapping on a select step | Renames selected columns by prefix, suffix or name expression. |
| Record ID | Full | Row-number or uuid column expression | Adds a UUID or sequential record id column. |
| Sample | Full | Row limit or sample option on extract | Takes first/last/random/Nth/percent rows overall or per group. |
| Tile | Full | Window expressions for tile number and sequence | Assigns tile numbers by equal sum, count, std-dev bands, distinct values or manual cutoffs. |

### Transform

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Aggregate | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with aggregation; [Pivot](/reference/workflow-steps/tables/table-pivot/) when doPivot | Converts to an Aggregate step; pivot mode and propagate-all need a Pivot step or manual first() columns. |
| Count Records | Full | Aggregate step with count functions | Returns total, non-null or distinct counts as one row. |
| Data Encoder/Decoder | Full | Column expressions for base64/hex encode and decode | Encodes or decodes selected columns; AES only on Databricks. |
| Deduplicate | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with distinct or a windowed rank filter | Converts distinct and first/last to rank-based dedupe; any is non-deterministic and unique_only needs a count filter. |
| Dynamic Select | Full | Column select in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step resolved by type | Resolves columns by type at conversion time into an explicit select. |
| Filter | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a filter expression | Converts to a Table Extract step with a filter expression; NULL conditions drop the row. |
| Finance | Full | Column expression implementing the financial function | Appends a financial function result (FV, PV, NPV, IRR, ...) as a new column. |
| Flatten Schema | Full | [JSON Parse](/reference/workflow-steps/tables/table-json-parse/) | Converts to JSON flattening with delimiter naming; array explode needs manual review. |
| Fuzzy Match | Full | [Fuzzy Match](/reference/workflow-steps/tables/table-fuzzy-match/) | Converts to a Fuzzy Match step; match scores can differ from Prophecy's. |
| Limit | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a row limit | Converts to a row limit; config references become project variables. |
| Order By | Full | Sort on a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | Converts to a sort with the same keys, direction and null placement. |
| Pivot | Full | [Pivot](/reference/workflow-steps/tables/table-pivot/) | Turns the selected pivot values into columns of aggregates; a Simple-mode value list fetched at design time is converted as the listed values. |
| Reformat | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with column expressions | Converts to a Table Extract step with one expression per output column; unlisted columns are dropped. |
| Running Total | Full | Cumulative-sum window expression column | Appends cumulative sums per selected column. |
| Snowflake Unpivot (third-party) | Full | [Melt](/reference/workflow-steps/tables/table-melt/) | Unpivots columns via Snowflake UNPIVOT. |
| Transpose | Full | [Melt](/reference/workflow-steps/tables/table-melt/) | Stacks data columns into name and string value columns. |
| TransposeAgg | Full | — | Approximated as an aggregate followed by a transpose, with a warning that the output layout can differ. |
| Unpivot | Full | [Melt](/reference/workflow-steps/tables/table-melt/) | Stacks data columns into name and value columns. |
| Weighted Average | Full | Aggregate step with weighted-average expression | Computes a weighted mean overall or per group. |
| Window Function | Full | Window expressions in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | Converts to window expressions with partition, order and frame; range frames need manual review. |

### Join/Split

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Except | Full | [Anti Join](/reference/workflow-steps/tables/table-anti-join/) on all columns plus a distinct [Table Extract](/reference/workflow-steps/tables/table-extract/) | Keeps rows of the first input that appear in none of the other inputs. |
| Intersect | Full | [Inner Join](/reference/workflow-steps/tables/table-inner-join/) on all columns plus Distinct | Keeps rows present in every input. |
| Join | Full | [Inner Join](/reference/workflow-steps/tables/table-inner-join/) chain (left/right/full/anti per joinType) | Converts to a chain of join steps by joinType; semi, anti, cross and whereClause need follow-up filter or manual steps. |
| Union | Full | [Union All](/reference/workflow-steps/tables/table-union-all/) | Union becomes a Union All step with Distinct when duplicates are not preserved; Except and Intersect need join-based rebuilds. |
| Union By Name | Full | [Union All](/reference/workflow-steps/tables/table-union-all/) | Becomes a Union All that aligns columns by name and null-fills missing ones. |

### Parse

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| JSON Parse | Full | [JSON Parse](/reference/workflow-steps/tables/table-json-parse/) | Parses a JSON text column into structured fields. |
| Regex | Full | Regex expressions in a Table Extract / Transform step | Replace, parse, match or tokenize a text column with a regex. |
| Text To Columns | Full | Split-column / explode steps with regex delimiter | Splits a delimited column into columns or rows using a regex delimiter. |
| XML Parse | Full | [XML Parse](/reference/workflow-steps/tables/table-xml-parse/) | Parses an XML text column into structured fields. |

### Custom

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Directory | Partial | Placeholder step with warning | Lists files with the documented columns; options without a PlaidCloud equivalent are ignored with a warning and a missing path gives zero rows. |
| DynamicInput | Full | SQL step for query templates; workflow loop for multi-file mode | Query-template mode embeds the template as a SQL step; multi-file mode maps with assumptions. |
| Email | Full | [Notify Via Email](/reference/workflow-steps/notifications/notify-via-email/) | Sends the email, with an optional data attachment, through a bound email connection. |
| RestAPI | Full | Rebuild with a REST Request step | Calls an HTTP API per input row with auth, parsing, async polling and retry. |
| Script | Full | Python step with frame-access rewrite | Embeds the script body in a python step, with data-frame access rewritten; Scala bodies carried with a note. |
| SQL Statement | Full | SQL step per output tab, text translated to the tenant dialect | Embeds each tab as a SQL step with inputs bound as temp tables; translated to the tenant dialect. |
| StoredProcedure | Full | Not supported (warehouse-native procedure call) | Calls the procedure with column-bound arguments one row at a time where the warehouse has a native CALL; elsewhere it passes data through with a warning. |
| Table Operations | Full | [Table In-Place Delete](/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/reference/workflow-steps/tables/table-update/), [Table Drop](/reference/workflow-steps/tables/table-drop/) | Update, delete and drop map to table steps; vacuum and optimize become table optimize or a no-op with a warning. |
| ToDo | Full | Placeholder step with the message as a note | Unconverted logic becomes a failing placeholder step that names the original tool and message in the migration report. |

### Spatial

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Buffer | Full | [Spatial Buffer](/reference/workflow-steps/spatial/spatial-buffer/) | Grows each geometry by the configured distance in miles or kilometers. |
| CreatePoint | Full | [Table Extract](/reference/workflow-steps/spatial/spatial-sql-recipes/) with `geom_point` | Builds point geometry from longitude and latitude columns. |
| Distance | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) | Computes distance, cardinal direction and bearing between two WKT points. |
| FindNearest | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a cross join | Finds N nearest target points for each source point within a max distance. |
| HeatMap | Partial | [Heat Map (macro)](/reference/workflow-steps/macros/macro-heat-map/) | Aggregates points into contoured density bands rather than H3 cells. |
| PolyBuild | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) and a Python step | Builds polygon or polyline WKT from ordered points per group. |
| Simplify | Full | [Spatial Generalize](/reference/workflow-steps/spatial/spatial-generalize/) | Simplifies WKT geometries by a tolerance in miles/kms. |
| SpatialMatch | Full | [Spatial Match](/reference/workflow-steps/spatial/spatial-match/) | Matches source and target geometries by intersects/contains/within/touches/envelope. |

### Report

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| PowerBIWrite | Full | [REST Request](/reference/workflow-steps/general/rest-request/) | Creates the Power BI dataset and pushes the rows through the Power BI REST API. |
| TableauWrite | Full | [Publish to Tableau](/reference/workflow-steps/export/export-to-tableau/) | Writes a Hyper extract and publishes it to the bound Tableau connection. |
| Visualize | Full | Rebuild with a REST Request step | Passes data through unchanged; the dashboard binding is not migrated and a warning says so. |

### Subgraph/Control

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Condition | Full | Rebuild with a workflow loop | Routes the whole input to the first output whose scalar SQL condition is true. |
| Macro | Full | SQL step with the macro body expanded | Embeds the macro body as a SQL step translated to the tenant dialect, inputs bound as temp tables. |
| Pipeline (trigger) | Full | Run another workflow from this workflow (workflow chaining) | Triggers the named pipeline with its parameters; version pinning and the trigger-count limit are not reproduced. |
| Subgraph (Basic) | Full | Canvas container / nested workflow from inline processes | Converts the inline inner graph into a nested workflow (or inlined steps) with in/out table parameters. |

## Connectors

Dataset formats and connectors are source and target settings of a gem, not gems. Each format converts to the import or export step shown, and conversion never contacts the source or target system.

| Format | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| avro | Full | Table or document import binding with a warning | Kept on the canvas as a pass-through that names the original connector. |
| BigQuery | Full | External database connection with a table import | Reads and writes through a connection. |
| binary | Full | Table or document import binding with a warning | Kept on the canvas as a pass-through that names the original connector. |
| Catalog table | Full | Existing PlaidCloud table binding | Binds to a table by name. Reads and plain writes convert; merge, upsert and SCD2 write modes are reported with a warning and written as a plain table write. |
| cosmos | Full | Table or document import binding with a warning | Kept on the canvas as a pass-through that names the original connector. |
| CSV | Full | [Import: CSV](/reference/workflow-steps/import/import-csv/); Export: CSV | Reads and writes delimited files with header, separator, quote, escape, and encoding options. |
| Data_Generator | Full | Table or document import binding with a warning | Kept on the canvas as a pass-through that names the original connector. |
| DatahubTable | Full | Table or document import binding with a warning | Kept on the canvas as a pass-through that names the original connector. |
| Delta | Full | Existing PlaidCloud table binding | Reads and writes the table as a plain table; merge, upsert and SCD2 write modes (reported with a warning), time travel and streaming triggers are not reproduced. |
| Excel (XLSX) | Full | Import: Excel; Export: Excel | Reads and writes workbook sheets and ranges. |
| fixedFormat | Full | Table or document import binding with a warning | Kept on the canvas as a pass-through that names the original connector. |
| hive | Full | Table or document import binding with a warning | Kept on the canvas as a pass-through that names the original connector. |
| Iceberg | Full | Existing PlaidCloud table binding | Reads and writes the table. |
| JDBC | Full | External database connection with a table import | Reads through a connection; pre and post queries are flagged. |
| JSON | Full | [JSON Parse](/reference/workflow-steps/tables/table-json-parse/) | Loads records and flattens nested fields. |
| Kafka | Full | Import: [Import Kafka](/reference/workflow-steps/import/import-kafka/); Export: [Export Kafka](/reference/workflow-steps/export/export-kafka/) | Reads a topic as one batch of messages and writes rows as messages. |
| mongodb | Full | Table or document import binding with a warning | Kept on the canvas as a pass-through that names the original connector. |
| orc | Full | Table or document import binding with a warning | Kept on the canvas as a pass-through that names the original connector. |
| Parquet | Full | Import: Parquet; Export: Parquet | Reads and writes Parquet files; datetime rebase options are ignored. |
| Pinecone | Full | Import and export: [REST Request](/reference/workflow-steps/general/rest-request/) | Reads an index's records and upserts rows as vectors through the Pinecone REST API. |
| Redshift | Full | External database connection with a table import | Reads and writes through a connection. |
| salesforce | Full | Table or document import binding with a warning | Kept on the canvas as a pass-through that names the original connector. |
| Seed (inline) | Full | [Import: CSV](/reference/workflow-steps/import/import-csv/) | Loads the inline rows as a table. |
| slack | Full | Table or document import binding with a warning | Kept on the canvas as a pass-through that names the original connector. |
| smartsheet | Full | Table or document import binding with a warning | Kept on the canvas as a pass-through that names the original connector. |
| Snowflake | Full | External database connection with a table import | Reads and writes through a connection. |
| SQL file types (CSV, Excel, JSON, Parquet, Text, XML, fixed-width) | Full | Import and export file steps against a document account | Reads and writes the file type; options without a PlaidCloud equivalent are flagged. |
| Text | Full | [Import: CSV](/reference/workflow-steps/import/import-csv/) as a single column | Reads each line as one column. |
| webpage | Full | Table or document import binding with a warning | Kept on the canvas as a pass-through that names the original connector. |
| XML | Full | [XML Parse](/reference/workflow-steps/tables/table-xml-parse/) | Loads records by row tag. |

## Expressions and Project Structure

| Area | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Expressions | Full | Spark and warehouse SQL expressions translated function by function | Functions and operators convert to PlaidCloud expressions; a function without an equivalent is flagged by name. |
| Project and graph structure | Full | Project loader | Every Prophecy export shape loads and normalizes into one model. |

## Validating a Converted Workflow

Compare the converted workflow's output against the output of your own Prophecy pipeline: schema, row count, and row values. Ignore row order unless the workflow depends on it.
