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

Every gem, connector and project structure converts: **Full** means the gem
becomes a native PlaidCloud step, variable, or canvas object that does the
gem's work. The few behaviours a converted workflow does not reproduce on its
own are listed under [Known Edge Cases](#known-edge-cases), each with what to
do.

To run a conversion, see [Migrate Prophecy Projects](/guides/workflows/migrate-prophecy-projects/).

## Spark pipeline gems

### Source/Target

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Lookup | Full | [Lookup](/reference/workflow-steps/tables/table-lookup/) | Each lookup call becomes a Lookup step in the step that uses it; a key with no match reads NULL, and a duplicated key returns one of its rows. |
| Source | Full | Import step chosen by the dataset format (see [Connectors](#connectors)) | Each Source becomes an import step into a table named after the dataset; a format the converter does not recognise is read as a CSV file uploaded to the workflow's document folder, with a warning. |
| Streaming Source | Full | Same import as batch Source | Streaming sources convert to a one-shot batch import with a warning. |
| Streaming Target | Full | Batch append load | Streaming targets convert to a batch append with a warning. |
| Target | Full | Table export / load step chosen by dataset format and writeMode | Each Target becomes a table load or export step in the gem's write mode: append, overwrite, merge with its SET expressions, upsert, SCD2, replaceWhere and insertInto. |

### Prepare

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Data Cleansing | Full | Column expressions in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | Converts null fill, trim and case options into column expressions; cleaned columns move last. |
| Sequence | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a row number expression | Adds a sequence column from the start value and increment. |
| Surrogate Key Generator | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a row number expression | Adds a sequential key from the initial value; keys continue across runs from a table that holds the last key issued. |

### Transform

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Aggregate | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with aggregation; [Pivot](/reference/workflow-steps/tables/table-pivot/) when the gem pivots | Groups and aggregates, applies the HAVING condition, and pivots into one column per pivot value; propagate-all carries every other input column. |
| Bulk Column Expressions | Full | Expand to one expression per column in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | One expression per listed column in a Table Extract step; the conversion warns that the gem's layout is assumed. |
| Bulk Column Rename | Full | Column rename in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | One rename per listed column in a Table Extract step; the conversion warns that the gem's layout is assumed. |
| Deduplicate | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with distinct or a row-number filter | Keeps one row per key: distinct, first or last by your sort order, any, or only the keys that occur once. |
| Dynamic Replace | Full | Dynamic replace transform, configured by hand | Converts to replacement rules on the dynamic replace transform; the conversion warns that the gem's layout is assumed. |
| Dynamic Select | Full | Column select in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step resolved by type | Resolves columns by type at conversion time into an explicit select. |
| Filter | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a filter expression | Converts to a Table Extract step with a filter expression; NULL conditions drop the row. |
| Flatten Schema | Full | [JSON Parse](/reference/workflow-steps/tables/table-json-parse/) and [Table Extract](/reference/workflow-steps/tables/table-extract/) | Flattens nested fields into columns named with the gem's delimiter and explodes arrays into one row per element. |
| Fuzzy Match | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) and [User Defined Transform](/reference/workflow-steps/general/user-defined-transform/) | Pairs the records, scores each match field by the gem's method, averages the scores, and keeps the pairs at or above your threshold. |
| Group By Rollup | Full | Union of [Table Extract](/reference/workflow-steps/tables/table-extract/) aggregation steps per rollup level | Expands the rollup into one aggregate per grouping level unioned together with NULL subtotals. |
| Limit | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a row limit | Converts to a row limit; config references become project variables. |
| Normalize | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with an explode expression | Repeats each record by the length expression, computes the output columns per index, and stops at the first index where the finished condition holds. |
| Order By | Full | Sort on a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | Converts to a sort with the same keys, direction and null placement. |
| Reformat | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with column expressions | Converts to a Table Extract step with one expression per output column; unlisted columns are dropped. |
| Sample Rows | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a row limit or random sample | Keeps a random fraction or count of rows; the rows chosen differ from the Spark run because sampling is random. |
| Schema Transform | Full | Chain of [Table Extract](/reference/workflow-steps/tables/table-extract/) steps applied in order | Applies each operation in order: add or replace a column, drop, rename, add if missing with its default, and add a project business rule. |
| Set Operation | Full | [Union All](/reference/workflow-steps/tables/table-union-all/); [Anti Join](/reference/workflow-steps/tables/table-anti-join/) for except; [Inner Join](/reference/workflow-steps/tables/table-inner-join/) for intersect | Union all stacks the inputs; except all and intersect all keep the right number of duplicate rows. |
| TransposeAgg | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with aggregation | Converts the gem's grouping, aggregates and pivot as an Aggregate, with a warning to review it. |
| Unpivot | Full | [Melt](/reference/workflow-steps/tables/table-melt/) | Stacks the selected columns into name and value columns. |
| Watermark | Full | No step needed | Dropped: a batch run reads all the data present, so there is no late-data cutoff to apply. |
| Window Function | Full | Window expressions in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | Adds window columns with the gem's partition, order and frame, rows or range, with unbounded, current-row or offset bounds. |

### Join/Split

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Compare Columns | Full | Full outer join plus per-column aggregates | Compares the columns through a full outer join of the unpivoted data, with match and mismatch counts. |
| Join | Full | [Inner Join](/reference/workflow-steps/tables/table-inner-join/), [Multi-Table Join](/reference/workflow-steps/tables/table-multi-table-join/), [Anti Join](/reference/workflow-steps/tables/table-anti-join/) or [Cross Join](/reference/workflow-steps/tables/table-cross-join/) | Builds the join of each type, inner, left, right, full, semi, anti, cross and natural, on any join condition, applies the where clause, and writes the select list. |
| Repartition | Full | No step needed | Dropped: PlaidCloud manages partitioning, so the next step reads the upstream table directly. |
| Row Distributor | Full | One [Table Extract](/reference/workflow-steps/tables/table-extract/) filter per output | Converts to one filter per output; rows can land in multiple outputs. |

### Parse

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Column Parser | Full | [JSON Parse](/reference/workflow-steps/tables/table-json-parse/) / [XML Parse](/reference/workflow-steps/tables/table-xml-parse/) | Converts to a JSON or XML parse of the named column; the conversion warns that the gem's layout is assumed. |

### Custom

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Custom Gem (Gem Builder) | Full | [User Defined Transform](/reference/workflow-steps/general/user-defined-transform/) running the gem's generated code | The gem's generated PySpark code from the pipeline export runs in a Python step, with a warning to review it. |
| CustomReformatBitbucket | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) | Converts as the Reformat whose expressions the gem carries, with a warning to review it. |
| Data Quality Check | Full | [Union All](/reference/workflow-steps/tables/table-union-all/) of one result row per check; [Raise Workflow Error](/reference/workflow-steps/workflow-control/raise-workflow-error/) to stop on failures | Evaluates each check over the input and writes one result row per check with its status and message. The data passes through, and the run stops when the gem's failure threshold is reached. |
| Deequ | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) checks | Passes data through and builds the constraint results table for the isComplete, isUnique, isNonNegative and isContainedIn rules. |
| Delta Table Operations | Full | [Table In-Place Delete](/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/reference/workflow-steps/tables/table-update/), [Table Drop](/reference/workflow-steps/tables/table-drop/), [Table Restore to Timestamp](/reference/workflow-steps/tables/table-restore-timestamp/) | Delete, update, drop and restore to a timestamp map to table steps; optimize, vacuum and restore by version pass data through with a warning. |
| Directory | Full | [Directory Listing](/reference/workflow-steps/document/directory-listing/) | Lists the files of the bound document folder in the gem's columns; with the sheet-name option, each workbook gives one row per sheet. A missing folder gives zero rows. |
| Email | Full | [Notify Via Email](/reference/workflow-steps/notifications/notify-via-email/) | Sends the email, with an optional data attachment, through a bound email connection. |
| Email Data | Full | [Notify Via Email](/reference/workflow-steps/notifications/notify-via-email/) | Emails the input rows as a table and passes the input through unchanged. |
| File Operation | Full | [Copy Document File](/reference/workflow-steps/document/copy-document-file/) or [Copy Document Directory](/reference/workflow-steps/document/copy-document-directory/) | Copies, moves or syncs files from the bound document folder into the converted workflow's document folder; a move removes the source files. |
| Log | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) | Writes the gem's event row (time, gem name, event type and text) to its output table. |
| REST API Enrich | Full | [REST Request](/reference/workflow-steps/general/rest-request/) | Calls the API once per row and adds the response columns. |
| Script | Full | Python step with frame-access rewrite | Embeds the script body in a python step, with data-frame access rewritten; Scala bodies carried with a note. |
| Soda Data Quality Check | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) checks | Builds the check results table from the Soda checks. |
| SQL Statement | Full | SQL step per output tab, text translated to the tenant dialect | Embeds each tab as a SQL step with inputs bound as temp tables; translated to the tenant dialect. |
| Todo | Full | [Raise Workflow Error](/reference/workflow-steps/workflow-control/raise-workflow-error/) or [Notify via Log](/reference/workflow-steps/notifications/notify-via-log/) | Marks logic still to be written: a log message when nothing reads it, or a step that stops the run with the gem's message when a later step depends on it. |

### Report

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Tableau | Full | [Publish to Tableau](/reference/workflow-steps/export/export-to-tableau/) | Writes a Hyper extract and publishes it to the bound Tableau connection. |

### ML/AI

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Bedrock | Full | [Text NLP AI](/reference/workflow-steps/text-documents/nlp-ai/) | Embeds the text column through the workspace AI connection. |
| OpenAI | Full | [Text NLP AI](/reference/workflow-steps/text-documents/nlp-ai/) | Answers questions or embeds text through the workspace AI connection. |
| Pinecone Lookup | Full | [REST Request](/reference/workflow-steps/general/rest-request/) | Queries the Pinecone index for each row and adds pinecone_matches and pinecone_error columns. |
| SageMaker Endpoint | Full | [Text NLP AI](/reference/workflow-steps/text-documents/nlp-ai/) | Answers questions through the workspace AI connection. |
| Text Processing | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) for chunk splitting; [REST Request](/reference/workflow-steps/general/rest-request/) for web scraping | Chunk splitting becomes a character-chunk expression; web scraping fetches each row's URL and joins the page content back onto the row. |

### Subgraph/Control

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Control Flow Input | Full | Dropped (boundary marker only) | Dropped; it only marks the iterator sub-workflow input boundary. |
| Control Flow Output | Full | Dropped (boundary marker only) | Dropped; it only marks the iterator sub-workflow output boundary. |
| Subgraph (Basic) | Full | Canvas container / nested workflow from inline processes | Converts the inline inner graph into a nested workflow (or inlined steps) with in/out table parameters. |
| Table Iterator | Full | [Workflow Loop](/reference/workflow-steps/workflow-control/workflow-loop/) | Runs the loop body once per input row, setting each configuration value from its column, up to maxIteration. |
| While Iterator | Full | [Workflow Loop](/reference/workflow-steps/workflow-control/workflow-loop/) | Runs the loop body once per pass, passing the iteration number, until the body returns no rows or the gem's maximum is reached. |

## SQL / Analyst gems

### Source/Target

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| External table Source/Target (BigQuery, Databricks, SAP HANA, MongoDB, MSSQL, Oracle, Postgres, Redshift, Salesforce, Snowflake, Synapse) | Full | External Data import/export step with the matching database connection | Reads or writes a table in an external database through a PlaidCloud connection. |
| File storage Source/Target (ADLS, Databricks Volumes, GCS, OneDrive, S3, SFTP, SharePoint, Smartsheet) | Full | Import/Export file steps against a document account (ADLS/GCS/S3/SFTP/SharePoint/OneDrive) | Reads or writes files in cloud/SFTP storage with wildcard union, trigger, delete/move and encryption options. |
| Model | Full | Upstream step output table | Reads another model as the table produced by the referenced upstream step. |
| Seed | Full | [Import: CSV](/reference/workflow-steps/import/import-csv/) | Seed CSV is imported into a PlaidCloud table. |
| Source | Full | Import step chosen by the dataset format (see [Connectors](#connectors)) | Each Source becomes an import step into a table named after the dataset; a format the converter does not recognise is read as a CSV file uploaded to the workflow's document folder, with a warning. |
| Target Model / Table (Target) | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/), [Upsert](/reference/workflow-steps/tables/table-upsert/), [Copy Table](/reference/workflow-steps/tables/table-copy/) and [Union All](/reference/workflow-steps/tables/table-union-all/) | Writes the model's final select to a PlaidCloud table as replace, append, upsert, delete-and-insert, SCD2 or replace by predicate. |
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
| Aggregate | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with aggregation; [Pivot](/reference/workflow-steps/tables/table-pivot/) when the gem pivots | Groups and aggregates, applies the HAVING condition, and pivots into one column per pivot value; propagate-all carries every other input column. |
| Count Records | Full | Aggregate step with count functions | Returns total, non-null or distinct counts as one row. |
| Data Encoder/Decoder | Full | Column expressions for base64/hex encode and decode | Encodes or decodes selected columns; AES only on Databricks. |
| Deduplicate | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with distinct or a row-number filter | Keeps one row per key: distinct, first or last by your sort order, any, or only the keys that occur once. |
| Dynamic Select | Full | Column select in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step resolved by type | Resolves columns by type at conversion time into an explicit select. |
| Filter | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a filter expression | Converts to a Table Extract step with a filter expression; NULL conditions drop the row. |
| Finance | Full | Column expression implementing the financial function | Appends a financial function result (FV, PV, NPV, IRR, ...) as a new column. |
| Flatten Schema | Full | [JSON Parse](/reference/workflow-steps/tables/table-json-parse/) and [Table Extract](/reference/workflow-steps/tables/table-extract/) | Flattens nested fields into columns named with the gem's delimiter and explodes arrays into one row per element. |
| Fuzzy Match | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) and [User Defined Transform](/reference/workflow-steps/general/user-defined-transform/) | Pairs the records, scores each match field by the gem's method, averages the scores, and keeps the pairs at or above your threshold. |
| Limit | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a row limit | Converts to a row limit; config references become project variables. |
| Order By | Full | Sort on a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | Converts to a sort with the same keys, direction and null placement. |
| Pivot | Full | [Pivot](/reference/workflow-steps/tables/table-pivot/) | Turns the selected pivot values into columns of aggregates; a Simple-mode value list fetched at design time is converted as the listed values. |
| Reformat | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with column expressions | Converts to a Table Extract step with one expression per output column; unlisted columns are dropped. |
| Running Total | Full | Cumulative-sum window expression column | Appends cumulative sums per selected column. |
| Snowflake Unpivot (third-party) | Full | [Melt](/reference/workflow-steps/tables/table-melt/) | Unpivots columns via Snowflake UNPIVOT. |
| Transpose | Full | [Melt](/reference/workflow-steps/tables/table-melt/) | Stacks data columns into name and string value columns. |
| TransposeAgg | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with aggregation | Converts the gem's grouping, aggregates and pivot as an Aggregate, with a warning to review it. |
| Unpivot | Full | [Melt](/reference/workflow-steps/tables/table-melt/) | Stacks data columns into name and value columns. |
| Weighted Average | Full | Aggregate step with weighted-average expression | Computes a weighted mean overall or per group. |
| Window Function | Full | Window expressions in a [Table Extract](/reference/workflow-steps/tables/table-extract/) step | Adds window columns with the gem's partition, order and frame, rows or range, with unbounded, current-row or offset bounds. |

### Join/Split

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Except | Full | [Anti Join](/reference/workflow-steps/tables/table-anti-join/) on all columns plus a distinct [Table Extract](/reference/workflow-steps/tables/table-extract/) | Keeps rows of the first input that appear in none of the other inputs. |
| Intersect | Full | [Inner Join](/reference/workflow-steps/tables/table-inner-join/) on all columns plus Distinct | Keeps rows present in every input. |
| Join | Full | [Inner Join](/reference/workflow-steps/tables/table-inner-join/), [Multi-Table Join](/reference/workflow-steps/tables/table-multi-table-join/), [Anti Join](/reference/workflow-steps/tables/table-anti-join/) or [Cross Join](/reference/workflow-steps/tables/table-cross-join/) | Builds the join of each type, inner, left, right, full, semi, anti, cross and natural, on any join condition, applies the where clause, and writes the select list. |
| Union | Full | [Union All](/reference/workflow-steps/tables/table-union-all/) | Stacks the inputs by position, removing duplicates when the gem does not keep them. |
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
| Directory | Full | [Directory Listing](/reference/workflow-steps/document/directory-listing/) | Lists the files of the bound document folder in the gem's columns; with the sheet-name option, each workbook gives one row per sheet. A missing folder gives zero rows. |
| DynamicInput | Full | SQL step for query templates; workflow loop for multi-file mode | Query-template mode embeds the template as a SQL step; multi-file mode maps with assumptions. |
| Email | Full | [Notify Via Email](/reference/workflow-steps/notifications/notify-via-email/) | Sends the email, with an optional data attachment, through a bound email connection. |
| RestAPI | Full | [REST Request](/reference/workflow-steps/general/rest-request/) | Sends one request per input row with your URL, headers, query, body and retries, keeps the response, and polls an asynchronous request until it is done. Credentials come from the connection you bind. |
| Script | Full | Python step with frame-access rewrite | Embeds the script body in a python step, with data-frame access rewritten; Scala bodies carried with a note. |
| SQL Statement | Full | SQL step per output tab, text translated to the tenant dialect | Embeds each tab as a SQL step with inputs bound as temp tables; translated to the tenant dialect. |
| StoredProcedure | Full | [Agent Remote Execution of SQL](/reference/workflow-steps/agent/agent-remote-execution-of-sql/) | Calls the procedure on its warehouse through the connection you choose: once per input row with each argument bound from its column, or once when it takes no arguments. The input columns pass through. |
| Table Operations | Full | [Table In-Place Delete](/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/reference/workflow-steps/tables/table-update/), [Table Drop](/reference/workflow-steps/tables/table-drop/) | Update, delete and drop map to table steps; vacuum and optimize become table optimize or a no-op with a warning. |
| ToDo | Full | [Raise Workflow Error](/reference/workflow-steps/workflow-control/raise-workflow-error/) or [Notify via Log](/reference/workflow-steps/notifications/notify-via-log/) | Marks logic still to be written: a log message when nothing reads it, or a step that stops the run with the gem's message when a later step depends on it. |

### Spatial

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Buffer | Full | [Spatial Buffer](/reference/workflow-steps/spatial/spatial-buffer/) | Grows each geometry by the configured distance in miles or kilometers. |
| CreatePoint | Full | [Table Extract](/reference/workflow-steps/spatial/spatial-sql-recipes/) with `geom_point` | Builds point geometry from longitude and latitude columns. |
| Distance | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) | Computes distance, cardinal direction and bearing between two WKT points. |
| FindNearest | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) with a cross join | Finds N nearest target points for each source point within a max distance. |
| HeatMap | Full | [Heat Map (macro)](/reference/workflow-steps/macros/macro-heat-map/) | Bins points into H3 hexagons at the gem's resolution, spreads the heat over the grid distance with its decay, and gives each hexagon's density and outline. |
| PolyBuild | Full | [Table Extract](/reference/workflow-steps/tables/table-extract/) and a Python step | Builds polygon or polyline WKT from ordered points per group. |
| Simplify | Full | [Spatial Generalize](/reference/workflow-steps/spatial/spatial-generalize/) | Simplifies WKT geometries by a tolerance in miles/kms. |
| SpatialMatch | Full | [Spatial Match](/reference/workflow-steps/spatial/spatial-match/) | Matches source and target geometries by intersects/contains/within/touches/envelope. |

### Report

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| PowerBIWrite | Full | [REST Request](/reference/workflow-steps/general/rest-request/) | Creates the Power BI dataset and pushes the rows through the Power BI REST API. |
| TableauWrite | Full | [Publish to Tableau](/reference/workflow-steps/export/export-to-tableau/) | Writes a Hyper extract and publishes it to the bound Tableau connection. |
| Visualize | Full | [Copy Table](/reference/workflow-steps/tables/table-copy/) | Passes the rows on unchanged; build the chart as a PlaidCloud dashboard on the same table. |

### Subgraph/Control

| Gem | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Condition | Full | [Cross Join](/reference/workflow-steps/tables/table-cross-join/) and [Table Extract](/reference/workflow-steps/tables/table-extract/) | Evaluates the conditions over the whole input and sends every row to the first output whose condition holds, else to the last output. |
| Macro | Full | SQL step with the macro body expanded | Embeds the macro body as a SQL step translated to the tenant dialect, inputs bound as temp tables. |
| Pipeline (trigger) | Full | [Workflow Loop](/reference/workflow-steps/workflow-control/workflow-loop/) | Runs the named pipeline once per input row with your parameters and trigger condition, continues past a failed run, and returns one row per run. |
| Subgraph (Basic) | Full | Canvas container / nested workflow from inline processes | Converts the inline inner graph into a nested workflow (or inlined steps) with in/out table parameters. |

## Connectors

Dataset formats and connectors are source and target settings of a gem, not gems. Each format converts to the import or export step shown, and conversion never contacts the source or target system.

| Format | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Avro | Full | Import: [Avro](/reference/workflow-steps/import/import-avro/); Export: [Avro](/reference/workflow-steps/export/export-to-avro/) | Reads and writes Avro files. |
| BigQuery | Full | External database connection with a table import | Reads and writes through a connection. |
| Binary files | Full | [Directory Listing](/reference/workflow-steps/document/directory-listing/) with file contents; [Alteryx Executor](/reference/workflow-steps/general/alteryx-executor/) to write | Reads each file of the folder with its path, modification time, length and content; writes each row's content to the file its path names. |
| Catalog table | Full | Existing PlaidCloud table binding | Binds to a table by name; reads and every write mode convert. |
| Cosmos DB | Full | Import and export: [REST Request](/reference/workflow-steps/general/rest-request/) | Reads and writes the container's documents through your Cosmos DB connection. |
| CSV | Full | [Import: CSV](/reference/workflow-steps/import/import-csv/); Export: CSV | Reads and writes delimited files with header, separator, quote, escape, and encoding options. |
| Data Generator | Full | [Table Faker](/reference/workflow-steps/tables/table-faker/) | Generates the dataset's columns with the same kinds of fake data. |
| DataHub table | Full | [Import SQL](/reference/workflow-steps/import/import-sql/) | Reads the table the dataset names through your connection; a write lands in a PlaidCloud table. |
| Delta | Full | Existing PlaidCloud table binding | Reads and writes the table in every write mode; a read of an earlier version reads it through the Databricks connection you bind. |
| Excel (XLSX) | Full | Import: Excel; Export: Excel | Reads and writes workbook sheets and ranges. |
| Fixed format | Full | Import: [Fixed Width](/reference/workflow-steps/import/import-fixed-width/); Export: [CSV](/reference/workflow-steps/export/export-to-csv/) | Reads fixed-width files laid out from the dataset's column widths; writes a delimited file. |
| Hive | Full | Import: [Import SQL](/reference/workflow-steps/import/import-sql/); Export: [External Tables](/reference/workflow-steps/export/export-external-tables/) | Reads and writes the table through your Hive connection. |
| Iceberg | Full | Existing PlaidCloud table binding | Reads and writes the table. |
| JDBC | Full | External database connection with a table import | Reads a table or query and writes in replace or append mode through your connection; a post-write statement runs after the write. |
| JSON | Full | [JSON Parse](/reference/workflow-steps/tables/table-json-parse/) | Loads records and flattens nested fields. |
| Kafka | Full | Import: [Import Kafka](/reference/workflow-steps/import/import-kafka/); Export: [Export Kafka](/reference/workflow-steps/export/export-kafka/) | Reads a topic as one batch of messages and writes rows as messages. |
| MongoDB | Full | Import: [MongoDB](/reference/workflow-steps/import/import-mongodb/); Export: [MongoDB](/reference/workflow-steps/export/export-mongodb/) | Reads and writes the collection through your MongoDB connection. |
| ORC | Full | Import: [ORC](/reference/workflow-steps/import/import-orc/); Export: ORC | Reads and writes ORC files. |
| Parquet | Full | Import: Parquet; Export: Parquet | Reads and writes Parquet files. |
| Pinecone | Full | Import and export: [REST Request](/reference/workflow-steps/general/rest-request/) | Reads an index's records and upserts rows as vectors through the Pinecone REST API. |
| Redshift | Full | External database connection with a table import | Reads and writes through a connection. |
| Salesforce | Full | Import: [Query Salesforce Object](/reference/workflow-steps/salesforce/query-salesforce-object/); Export: [REST Request](/reference/workflow-steps/general/rest-request/) | Reads an object or SOQL query and writes records through your Salesforce connection. |
| Seed (inline) | Full | [Import: CSV](/reference/workflow-steps/import/import-csv/) | Loads the inline rows as a table. |
| Slack | Full | Import: [Singer](/reference/workflow-steps/import/import-singer/); Export: [REST Request](/reference/workflow-steps/general/rest-request/) | Reads channel messages and posts each row as a message through your Slack connection. |
| Smartsheet | Full | Import and export: [REST Request](/reference/workflow-steps/general/rest-request/) | Reads and writes the sheet's rows through your Smartsheet connection. |
| Snowflake | Full | External database connection with a table import | Reads and writes through a connection. |
| SQL file types (CSV, Excel, JSON, Parquet, Text, XML, fixed-width) | Full | Import and export file steps against a document account | Reads and writes the file type; options without a PlaidCloud equivalent are flagged. |
| Text | Full | [Import: CSV](/reference/workflow-steps/import/import-csv/) as a single column | Reads each line as one column. |
| Web page | Full | [REST Request](/reference/workflow-steps/general/rest-request/) | Reads the page at the dataset's URL into a table. |
| XML | Full | [XML Parse](/reference/workflow-steps/tables/table-xml-parse/) | Loads records by row tag. |

## Expressions and Project Structure

| Area | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Expressions | Full | Spark and warehouse SQL expressions translated function by function | Functions and operators convert to PlaidCloud expressions; a function without an equivalent is flagged by name. |
| Project and graph structure | Full | Project loader | Every Prophecy export shape loads and normalizes into one model. |

## Known Edge Cases

| Case | What happens |
| --- | --- |
| Custom gem without its code in the export | A Gem Builder or other custom gem runs the code the project export carries for it with each pipeline. When the export holds no code for the gem, it becomes a step that names the gem; export the project with its pipeline code, or rebuild the logic in a Python step. |
| Scala code | Script and custom gems in a Scala project become a step that names the gem; rewrite the logic in Python or with standard steps. |
| Smartsheet as a file store | A Directory or File Storage gem on a Smartsheet connection lists or reads the converted workflow's document folder; read the sheets with a Smartsheet source instead. |
| Spark-only functions | `hash()` and `xxhash64()` return different values, because no warehouse uses Spark's seed, and `input_file_name()` returns an empty string, because the step reads a table. |
| Stored procedure results | The procedure runs on its warehouse, and the values it returns are not brought back; the step's output is its input columns. |
| Delta restore by version | Restoring a Delta table to a version number does nothing; restore it to a timestamp. |
| File Operation sync | Copies the files, but does not remove destination files the source no longer has. |
| Job components | A Spark job converts its one pipeline and schedule; its other components, run conditions and configuration overrides, and the Dataset, Model, Orchestration Target, Run Stored Procedure and Script components of a SQL orchestration job, are not converted. |
| Ab Initio record rules | Assign Keys, Compare Records, Error Detection and MTime pass their input through, because the rule they apply is not in the export. |
| Rare options | A Kafka Kerberos sign-in, a Salesforce SAQL query or Wave dataset, a DataHub `replaceWhere`, Data Generator providers with no PlaidCloud equivalent, Upload Files multi-table extraction, REST response flattening and the schema REST Enrich infers for parsed content convert in part, and the conversion report names each. |
| Unsafe parameter values | A parameter value holding a quote, backslash or brace is not put into an expression; the step that reads it becomes a step that names it. |
| Streaming | Streaming sources, targets and pipelines run as batch workflows over the data present when they run; schedule the workflow to run as often as you need. |

## Validating a Converted Workflow

Compare the converted workflow's output against the output of your own Prophecy pipeline: schema, row count, and row values. Ignore row order unless the workflow depends on it.
