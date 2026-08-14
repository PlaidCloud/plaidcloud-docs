---
title: Alteryx Conversion Matrix
description: How PlaidCloud converts Alteryx tools into native Advanced workflow steps, macros, variables, and managed executors — with per-tool support status.
sidebar:
  order: 6
---

PlaidCloud converts Alteryx workflows, apps, and macros into native Advanced
workflows. The importer maps each Alteryx tool to a workflow step, macro
construct, controlled variable, Document-backed file operation, or managed job
executor — so a converted workflow runs cloud-native, not as an emulation.

**Nearly every standard Alteryx tool converts fully.** The support status below is
per tool:

- **Full** — converts to a native PlaidCloud step, macro, variable, artifact, or
  managed executor and runs the tool's function. Most tools are here.
- **Partial** — converts and runs for its common use, while one distinct
  *capability mode* of the tool is not yet reproduced. Rare.
- **Not supported** — no conversion; the capability is rebuilt natively instead.
  A short list, called out below.

External-system connectors (Salesforce, Amazon S3, Anaplan, cloud ML services,
and the like) are **connected, not converted** — see
[Connecting to External Systems](#connecting-to-external-systems).

## Tool Support

| Alteryx Tool | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Action | Full | Variable binding and conditional step configuration | Updates downstream step settings from converted app inputs. |
| Append Fields | Full | Append fields transform | Appends fields from one stream to another. |
| Auto Field | Full | Auto field sizing transform | Preserves inferred field sizing. |
| Barcode | Full | Barcode executor | Reads or writes barcodes in the configured symbology. |
| Browse | Full | Browse / passthrough | Preserved for inspection with no runtime cost. |
| Buffer | Full | [Spatial Buffer](/reference/workflow-steps/spatial/spatial-buffer/) | Grows each geometry by a fixed distance. |
| Calgary Cross Count | Full | [Calgary database](/guides/workflows/migrate-alteryx-workflows/#calgary-databases) aggregate | Groups indexed fields and counts each custom field's named values. |
| Calgary Input | Full | [Calgary database](/guides/workflows/migrate-alteryx-workflows/#calgary-databases) input | Reads the database with its saved query applied as a filter. |
| Calgary Join | Full | [Calgary Join](/guides/workflows/migrate-alteryx-workflows/#calgary-join-and-cross-count-append) | Matches each record against a value index on the database. |
| Calgary Loader | Full | [Calgary database](/guides/workflows/migrate-alteryx-workflows/#calgary-databases) writer | Writes the stand-in table every Calgary reader binds to. |
| Check Box | Full | Controlled workflow variable | Converts app check-box choices to controlled input. |
| Classification | Full | [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) | Fuses the Assisted Modeling chain into one ML Train step with its algorithm, target, features, and hyperparameters. |
| Comment / Annotation / Link | Full | Canvas annotation | Preserved as workflow context. |
| Condition | Full | Step condition | Triggers warnings, errors, or branches from an expression. |
| Control Parameter | Full | Macro control parameter | Maps to PlaidCloud macro parameters. |
| Create Points | Full | [Table Extract](/reference/workflow-steps/spatial/spatial-sql-recipes/) with `geom_point` | Builds point geometry from longitude/latitude columns, in SQL. |
| Create Samples | Full | Table Extract, one per output | Splits input into Estimation, Validation, and Holdout at the configured percentages. |
| Cross Tab | Full | Pivot / cross-tab transform | Pivots rows to columns across every aggregation method and the derived totals. |
| Data Cleansing | Full | Data cleanse transform | Cleans whitespace, nulls, punctuation, and casing. |
| Date | Full | Workflow variable (date) | Emits ISO date values for steps and conditions. |
| DateTime | Full | Date/time transform | Converts date and time parsing and formatting. |
| Detour | Full | Conditional branch routing | Converts route selection to DAG conditions. |
| Detour End | Full | Conditional branch merge | Rejoins conditionally selected branches. |
| Directory | Full | Document directory listing | Lists files from a Document path. |
| Distance | Full | [Table Extract](/reference/workflow-steps/spatial/spatial-sql-recipes/) with `ST_DISTANCE_SPHERE` | Geodesic point-to-point distance and bearing, in SQL. |
| Download | Full | HTTP download executor | Downloads external data or artifacts. |
| Drop Down | Full | Controlled workflow variable | Converts app drop-down choices to controlled input. |
| Dynamic Input | Full | Dynamic Document input | Resolves file patterns and variable-driven inputs at runtime. |
| Dynamic Rename | Full | Dynamic rename transform | Renames fields from metadata or rules. |
| Dynamic Replace | Full | Dynamic replace transform | Applies replacement rules from a second stream. |
| Dynamic Select | Full | Dynamic field selection transform | Selects fields by type, name, or rule. |
| Error | Full | Step condition (error) | Converts configured error behavior to step conditions. |
| File Browse | Full | Controlled Document file variable | Lets users choose a file for a converted app run. |
| Filter | Full | Filter transform | Splits records by expression into true and false paths. |
| Find Nearest | Full | [Spatial Find Nearest](/reference/workflow-steps/spatial/spatial-find-nearest/) | Distance-ranked nearest-neighbor join in the database. |
| Fit | Full | [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) | Collapses into the fused ML Train step. |
| Folder Browse | Full | Controlled Document folder variable | Lets users choose a folder for a converted app run. |
| Formula | Full | Formula transform | Converts field expressions to PlaidCloud expressions or SQL. |
| Fuzzy Match | Full | Fuzzy matching executor | Matches on keys, thresholds, and candidate review. |
| Generalize | Full | [Spatial Generalize](/reference/workflow-steps/spatial/spatial-generalize/) | Simplifies geometry to a tolerance, preserving topology. |
| HTML | Full | Report text / HTML artifact | Preserves content as report or artifact output. |
| Image Processing | Full | Image transform executor | Applies grayscale, scale, crop, and rotation in canvas order. |
| Image Profile | Full | Image profile executor | Reports dimensions, mode, format, channels, and luminance statistics. |
| Image to Text | Full | OCR executor | Extracts text from images through managed OCR. |
| Input Data | Full | Document-backed file input | Loads `.yxdb`, `.dbf`, Excel, fixed-width, and other source files into workflow data. |
| Insights | Full | Dashboard / artifact output | Creates a cloud-native review artifact. |
| Interactive Chart | Full | Chart artifact | Creates a chart artifact from converted data. |
| Join | Full | Join transform | Produces joined, left-only, and right-only streams on a single- or multi-field key or by position. |
| Join Multiple | Full | Multi-join transform | Joins multiple input streams. |
| List Box | Full | Controlled workflow variable | Converts app list selections to controlled input. |
| Macro calls | Full | Macro invocation | Standard macros inline into the canvas; Batch and Iterative macros convert to native per-record and looping constructs. |
| Macro Input / Macro Output | Full | Macro input / output port | Map directly to PlaidCloud macro ports. |
| Make Grid | Full | [Spatial Make Grid](/reference/workflow-steps/spatial/spatial-make-grid/) | Tiles an extent into square cells, one row per cell. |
| Map | Full | Map artifact | Creates a PlaidCloud map artifact. |
| Map Input | Full | [Spatial File Import](/reference/workflow-steps/spatial/spatial-file-import/) | Reads MapInfo, ESRI, KML, and GeoJSON files with their sidecars. |
| Message | Full | Step condition (message) | Emits workflow warning, message, or error from a condition. |
| Modeling | Full | [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) | Fuses into the ML Train step with the pipeline's model choice. |
| Multi-Field Formula | Full | Multi-field formula transform | Applies a formula across selected fields. |
| Multi-Row Formula | Full | Window / row-aware formula transform | Converts row-relative logic to window behavior, partitioned by Group By. |
| Numeric Up Down | Full | Controlled numeric variable | Converts app numeric input to a typed variable. |
| Output Data | Full | Document / table output | Writes output to Document or PlaidCloud tables. |
| Overlay | Full | [Spatial Process](/reference/workflow-steps/spatial/spatial-process/) | Intersect, union, or cut two geometry columns. |
| PDF Input | Full | PDF extraction executor | Extracts text or tables from PDFs. |
| PDF to Text | Full | PDF text executor | Extracts text from PDF documents. |
| Poly-Build | Full | [Spatial Poly-Build](/reference/workflow-steps/spatial/spatial-poly-build/) | Builds a polygon or convex hull per group of points. |
| Poly-Split | Full | [Spatial Poly-Split](/reference/workflow-steps/spatial/spatial-poly-split/) | One row per vertex, component polygon, or hole. |
| Portfolio Composer (Text / Table / Image / Layout / Render) | Full | Report artifacts | Convert report content, layout, and rendering to PlaidCloud report output. |
| Predict | Full | [ML: Score](/reference/workflow-steps/machine-learning/ml-score/) | Scores data with the trained model table and appends a prediction column. |
| Python | Full | Jupyter / inline code step | Converts recognized notebook logic to a native step. |
| Radio Button | Full | Controlled workflow variable | Converts app radio choices to controlled input. |
| Random % Sample | Full | Table Extract (random) | Returns the exact count or percentage of records requested. |
| Record ID | Full | Row identifier transform | Adds a deterministic record identifier in the configured type and start value, restarting per group. |
| RegEx | Full | Regular expression transform | Parses, matches, or replaces text. |
| Regression | Full | [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) | Fuses the Assisted Modeling chain into one ML Train step. |
| Report Map | Full | Map report artifact | Produces a cloud-native map/report artifact. |
| Sample | Full | Sample transform | Keeps records by count, percentage, or grouping. |
| Select | Full | Select and schema projection step | Selects, renames, reorders, and retypes fields. |
| Smooth | Full | [Spatial Smooth](/reference/workflow-steps/spatial/spatial-smooth/) | Smooths each geometry over a number of passes. |
| Sort | Full | Sort transform | Sorts records by configured fields and directions. |
| Spatial Info | Full | [Spatial Info](/reference/workflow-steps/spatial/spatial-info/) | Area, length, centroid, and bounding rectangle as geodesic measures. |
| Spatial Process | Full | [Spatial Process](/reference/workflow-steps/spatial/spatial-process/) | Intersect, union, or cut geometry columns. |
| Summarize | Full | Aggregate transform | Groups and aggregates — sum, count, average, min, max, median, mode, standard deviation, variance, and count distinct. |
| Tab | Full | App tab grouping | Preserved as converted app structure. |
| Test | Full | Step condition | Converts test assertions to step conditions. |
| Text Box | Full | Controlled text variable | Converts app text input to a typed variable. |
| Text Input | Full | Inline table input | Creates inline data for the workflow. |
| Text Pre-processing | Full | NLP preprocessing executor | Normalizes and preprocesses text. |
| Text To Columns | Full | Split columns transform | Splits text into fields or rows. |
| Tile | Full | Tile / grouping transform | Assigns tile groups by configured rule. |
| Tool Container | Full | Canvas container / execution group | Preserved as workflow organization. |
| Topic Modeling | Full | Topic modeling executor | Runs topic modeling through managed NLP. |
| Transformation | Full | Transform step | Converts transformation logic to PlaidCloud expressions or SQL. |
| Transpose | Full | Unpivot transform | Converts columns to rows into a Name/Value pair. |
| Tree | Full | Controlled workflow variable | Converts app tree selection to controlled input. |
| Union | Full | Union transform | Combines streams by name, position, or configured rules. |
| Unique | Full | Unique / duplicate split transform | Separates first-unique records from duplicates. |
| Visual Layout | Full | Canvas layout metadata | Preserved as design context. |
| Word Cloud | Full | Text visualization artifact | Creates a visualization artifact from text analysis. |
| XML Parse | Full | XML parse transform | Extracts XML fields into workflow data. |
| Trade Area | Partial | [Spatial Trade Area](/reference/workflow-steps/spatial/spatial-trade-area/) | Fixed-radius trade areas convert. Drive-time trade areas — minutes on a road network — are not yet reproduced. |
| Image Recognition | Partial | [ML: Score](/reference/workflow-steps/machine-learning/ml-score/) | Scores against a trained model table. The tool's own VGG16 transfer-learning is not reproduced. |
| Image Template | Partial | Manual region extraction | Page-region detection is not reproduced; extract regions with a Formula or Text step. |
| Spatial Match | Partial | [Spatial Match](/reference/workflow-steps/spatial/spatial-match/) | Intersects, within, and contains convert. Touches, Crosses, Overlaps, and Centroid-In are not reproduced. |

Interface widgets (drop-downs, list boxes, check boxes, text/numeric/date inputs,
file and folder pickers), canvas objects (labels, links, containers), and macro
ports all convert as native controlled variables or canvas objects.

## Not Yet Supported

A small set of tools has no conversion route and is rebuilt natively instead. The
importer stops with a message naming the tool, so you know at conversion time:

| Alteryx Tool | Rebuild As |
| --- | --- |
| Centroid, Convex Hull, Line To Polygon, Point To Line | A [spatial SQL recipe](/reference/workflow-steps/spatial/spatial-sql-recipes/) or geometry step |
| Geocoder, Redistribute | A native geospatial step or connection to a geocoding service |
| Calgary Cross Count Append | A [Calgary Cross Count](/guides/workflows/migrate-alteryx-workflows/#calgary-databases), joined back to your input |

## Spatial Tool Coverage

Every tool in the Alteryx **Spatial** palette has a PlaidCloud route, and each is
a step you can also build by hand — conversion is a convenience, not the only way
in. See [Geospatial steps](/reference/workflow-steps/spatial/) for the reference
and [Geospatial Analytics](/guides/workflows/geospatial-analytics/) for how they
fit together.

| Alteryx Spatial Tool | PlaidCloud Route | Runs In |
| --- | --- | --- |
| Buffer | [Spatial Buffer](/reference/workflow-steps/spatial/spatial-buffer/) | Workflow engine |
| Create Points | [Table Extract expression](/reference/workflow-steps/spatial/spatial-sql-recipes/) | Database |
| Distance | [Table Extract expression](/reference/workflow-steps/spatial/spatial-sql-recipes/) | Database |
| Find Nearest | [Spatial Find Nearest](/reference/workflow-steps/spatial/spatial-find-nearest/) | Database |
| Generalize | [Spatial Generalize](/reference/workflow-steps/spatial/spatial-generalize/) | Workflow engine |
| Heat Map | [Heat Map (macro)](/reference/workflow-steps/macros/macro-heat-map/) | Workflow engine |
| Make Grid | [Spatial Make Grid](/reference/workflow-steps/spatial/spatial-make-grid/) | Workflow engine |
| Poly-Build | [Spatial Poly-Build](/reference/workflow-steps/spatial/spatial-poly-build/) | Workflow engine |
| Poly-Split | [Spatial Poly-Split](/reference/workflow-steps/spatial/spatial-poly-split/) | Workflow engine |
| Smooth | [Spatial Smooth](/reference/workflow-steps/spatial/spatial-smooth/) | Workflow engine |
| Spatial Info | [Spatial Info](/reference/workflow-steps/spatial/spatial-info/) | Workflow engine |
| Spatial Match | [Spatial Match](/reference/workflow-steps/spatial/spatial-match/) | Database |
| Spatial Process | [Spatial Process](/reference/workflow-steps/spatial/spatial-process/) | Workflow engine |
| Trade Area (fixed radius) | [Spatial Trade Area](/reference/workflow-steps/spatial/spatial-trade-area/) | Workflow engine |
| Pie Wedge Trade Area | [Pie Wedge Trade Area (macro)](/reference/workflow-steps/macros/macro-pie-wedge-trade-area/) | Workflow engine |
| Spatial file input | [Spatial File Import](/reference/workflow-steps/spatial/spatial-file-import/) | Workflow engine |
| Report Map | [Report Map](/reference/workflow-steps/reports/report-map/) | Workflow engine |

### Known Spatial Gaps

A few spatial capabilities are not yet reproduced; conversion names each in a note
rather than emitting a wrong result:

- **Drive-time trade areas** — fixed-radius trade areas convert; minutes on a road
  network do not.
- **The proprietary `.geo` GeoFile format** — other spatial formats read normally.
- **A handful of tools with no equivalent** — Centroid, Convex Hull, Line To
  Polygon, Point To Line, Geocoder, and Redistribute (see
  [Not Yet Supported](#not-yet-supported)).
- **Spatial Match relationships beyond Within, Contains, and Intersects** —
  Touches, Crosses, Overlaps, and Centroid-In select a different record set and
  are named rather than approximated.

## Connecting to External Systems

Alteryx ships a family of **connector** tools that read from or write to an
external service — Salesforce, Amazon S3, Anaplan, Box, Cassandra, Adobe
Analytics, Microsoft Dataverse / Dynamics, Marketo, Google Sheets, Google
BigQuery, Azure Data Lake, and cloud machine-learning services such as DataRobot,
Azure Cognitive Services, and AutoML, among others. Alteryx distributes these as
separately installed marketplace add-ons rather than core workflow tools.

In PlaidCloud you connect to those systems through the native
[connection catalog](/reference/connectors/) and read or write them with the
standard import/export steps — so the integration is a first-class, managed
PlaidCloud connection rather than a converted tool. When an imported workflow
uses one of these connectors, the importer names it and points you at the
equivalent PlaidCloud connection.

## Validating a Converted Workflow

For production workflows, validate converted outputs against trusted Alteryx
outputs — PlaidCloud validation focuses on schema, row count, and row values, and
ignores row order unless the workflow depends on it. Specialized operations
(spatial, fuzzy matching, OCR, NLP, reporting) run through managed job executors
that keep the workflow cloud-native; machine-learning pipelines convert to the
native [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) and
[ML: Score](/reference/workflow-steps/machine-learning/ml-score/) steps. See
[Migrate Alteryx Workflows](/guides/workflows/migrate-alteryx-workflows/) for the
end-to-end import and validation guide.
