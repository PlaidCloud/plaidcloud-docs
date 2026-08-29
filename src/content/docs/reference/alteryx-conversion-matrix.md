---
title: Alteryx Conversion Matrix
description: How PlaidCloud converts Alteryx tools into native Advanced workflow steps, macros, variables, and managed executors — with per-tool support status.
sidebar:
  order: 6
---

<!-- STATUS SCHEME: this page uses EXACTLY three statuses — Full / Partial / Not supported. Do NOT reintroduce "coverage levels" (Fully Converts / Converts With Validation / etc.). See plaidcloud-docs/CLAUDE.md. Only a structural capability-mode gap is Partial; only a no-conversion-path tool is Not supported. -->

PlaidCloud converts Alteryx workflows, apps, and macros into native Advanced
workflows. The importer maps each Alteryx tool to a workflow step, macro
construct, controlled variable, Document-backed file operation, or managed job
executor — so a converted workflow runs cloud-native, not as an emulation.

**Nearly every standard Alteryx tool converts fully.** The support status below
is per tool:

- **Full** — converts to a native PlaidCloud step, macro, variable, artifact, or
  managed executor and runs the tool's function. Most tools are here.
- **Partial** — converts and runs for its common use, while one distinct
  *capability mode* of the tool is not yet reproduced. Rare.
- **Not supported** — no conversion; the capability is rebuilt natively instead.

External-system connectors (Salesforce, HTTP, Google Analytics, Cassandra,
email, Hadoop, Spark, and the like) are **connected, not converted** — see
[Connecting to External Systems](#connecting-to-external-systems).

## Tool Support

| Alteryx Tool | Status | PlaidCloud Equivalent | Converts |
| --- | --- | --- | --- |
| Action | Full | Variable binding and conditional step configuration | Updates downstream step settings from converted app inputs. |
| Append Fields | Full | Append fields transform | Appends fields from one stream to another. |
| Auto Field | Full | Auto field sizing transform | Preserves inferred field sizing. |
| AutoML | Full | [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) | Fuses the model-method, target, and candidate-algorithm selections into an ML Train step, the same as Classification and Regression. AutoML never records which candidate algorithm actually won at Alteryx run time, so conversion picks the first checked algorithm ML Train supports and notes the choice. Validated against a reconstructed fixture rather than a real Alteryx export — AutoML left Alteryx's palette after 2023.1, so no export sample exists to convert from; confirm against a real workflow if one surfaces. |
| Barcode | Full | Barcode executor | Reads or writes barcodes in the configured symbology. |
| Browse | Full | Browse / passthrough | Preserved for inspection with no runtime cost. |
| Buffer | Full | [Spatial Buffer](/reference/workflow-steps/spatial/spatial-buffer/) | Grows each geometry by a fixed distance. |
| Build Features | Partial | [Build Features](/reference/workflow-steps/tables/table-build-features/) | Converts arithmetic and interaction primitives, date-part extraction, explicit-threshold binning, z-score and min-max scaling, and one-hot encoding. Cross-table aggregation (Deep Feature Synthesis across the Manage Relationships tab), PCA, target encoding, and data-driven auto-binning have no equivalent — each is flagged by name in the conversion report rather than silently dropped. |
| Calgary Cross Count | Full | [Calgary database](/guides/workflows/migrate-alteryx-workflows/#calgary-databases) aggregate | Groups indexed fields and counts each custom field's named values. |
| Calgary Cross Count Append | Full | [Calgary Cross Count Append](/guides/workflows/migrate-alteryx-workflows/#calgary-join-and-cross-count-append) | Matches each input record against a value index, then counts how many database records it matched. |
| Calgary Input | Full | [Calgary database](/guides/workflows/migrate-alteryx-workflows/#calgary-databases) input | Reads the database with its saved query applied as a filter. |
| Calgary Join | Full | [Calgary Join](/guides/workflows/migrate-alteryx-workflows/#calgary-join-and-cross-count-append) | Matches each record against a value index on the database, keeping the records that matched. |
| Calgary Loader | Full | [Calgary database](/guides/workflows/migrate-alteryx-workflows/#calgary-databases) writer | Writes the stand-in table every Calgary reader binds to. |
| Centroid | Full | Centroid executor op | Reduces each geometry to its centre point, appended as a `Centroid` column. |
| Check Box | Full | Controlled workflow variable | Converts app check-box choices to controlled input. |
| Classification | Full | [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) | Fuses the Assisted Modeling chain into one ML Train step with its algorithm, target, features, and hyperparameters. |
| Comment / Annotation / Link | Full | Canvas annotation | Preserved as workflow context. |
| Condition | Full | Step condition | Triggers warnings, errors, or branches from an expression. |
| Control Parameter | Full | Macro control parameter | Maps to PlaidCloud macro parameters. |
| Convex Hull | Full | Convex Hull executor op | Builds the smallest convex polygon enclosing each geometry, appended as a `ConvexHull` column. |
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
| Download | Full | [REST Request](/reference/workflow-steps/general/rest-request/) step against a REST connection | Downloads external data or artifacts; assign a REST connection to the converted step before it runs. |
| Drop Down | Full | Controlled workflow variable | Converts app drop-down choices to controlled input. |
| Dynamic Input | Full | Dynamic Document input | Resolves file patterns and variable-driven inputs at runtime. |
| Dynamic Rename | Full | Dynamic rename transform | Renames fields from metadata or rules. |
| Dynamic Replace | Full | Dynamic replace transform | Applies replacement rules from a second stream. |
| Dynamic Select | Full | Dynamic field selection transform | Selects fields by type, name, or rule. |
| Error | Full | Step condition (error) | Converts configured error behavior to step conditions. |
| Feature Types | Full | [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) feature configuration | Carries each field's assigned model role into the fused ML Train step. |
| File Browse | Full | Controlled Document file variable | Lets users choose a file for a converted app run. |
| Filter | Full | Filter transform | Splits records by expression into true and false paths. |
| Fit | Full | [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) | Collapses into the fused ML Train step. |
| Folder Browse | Full | Controlled Document folder variable | Lets users choose a folder for a converted app run. |
| Formula | Full | Formula transform | Converts field expressions to PlaidCloud expressions or SQL. |
| Fuzzy Match | Full | Fuzzy matching executor | Matches on keys, thresholds, and candidate review. |
| Generalize | Full | [Spatial Generalize](/reference/workflow-steps/spatial/spatial-generalize/) | Simplifies geometry to a tolerance, preserving topology. |
| HTML | Full | Report text / HTML artifact | Preserves content as report or artifact output. |
| Image Processing | Full | Image transform executor | Applies grayscale, scale, crop, and rotation in canvas order. |
| Image Profile | Full | Image profile executor | Reports dimensions, mode, format, channels, and luminance statistics. |
| Image to Text | Full | OCR executor | Extracts text from images through managed OCR. |
| Input Data | Full | Document-backed file input | Loads `.yxdb`, `.dbf`, Excel, and fixed-width `.flat` source files into workflow data. |
| Insights | Full | Dashboard / artifact output | Creates a cloud-native review artifact. |
| Interactive Chart | Full | Chart artifact | Creates a chart artifact from converted data. |
| Join | Full | Join transform | Produces joined, left-only, and right-only streams on a single- or multi-field key or by position. |
| Join Multiple | Full | Multi-join transform | Joins multiple input streams. |
| Key/Value Pairs | Full | [Text: NLP AI](/reference/workflow-steps/text-documents/nlp-ai/) (keyvalue task) | Extracts key/value pairs from a text column through the LLM-backed NLP AI step, with optional candidate keys and fuzzy or exact matching. |
| Line To Polygon | Full | Line To Polygon executor op | Closes each line into a polygon ring, appended as a `Polygon` column. |
| List Box | Full | Controlled workflow variable | Converts app list selections to controlled input. |
| Location Optimizer | Partial | [Location Optimizer](/reference/workflow-steps/optimization/location-optimizer/) | Converts the linear distance-minimization case — choosing K sites to minimize total or weighted distance to demand — to the native p-median MIP step. A gravity-kernel score, a bespoke scoring macro, or any other candidate-search objective still refuses; see [Migrate Alteryx Workflows](/guides/workflows/migrate-alteryx-workflows/#macros-in-a-converted-workflow). |
| Macro calls | Full | Macro invocation | Imports known macro sources and maps macro calls to PlaidCloud macro steps. |
| Macro Input / Macro Output | Full | Macro input / output port | Map directly to PlaidCloud macro ports. |
| Make Grid | Full | [Spatial Make Grid](/reference/workflow-steps/spatial/spatial-make-grid/) | Tiles an extent into square cells, one row per cell. |
| Map | Full | Map artifact | Creates a PlaidCloud map artifact. |
| Map Input | Full | [Spatial File Import](/reference/workflow-steps/spatial/spatial-file-import/) | Reads MapInfo, ESRI, KML, and GeoJSON files with their sidecars. |
| Master Selector | Partial | Controlled workflow variable and conditional step visibility | Converts the tool's show/hide visibility conditions on interface elements to conditional step visibility. Converts which sub-workflow the selection runs on a best-effort basis — validation against real on-tenant apps is still pending, so review the selected run-target before relying on it in production. |
| Message | Full | Step condition (message) | Emits workflow warning, message, or error from a condition. |
| Modeling | Full | [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) | Fuses into the ML Train step with the pipeline's model choice. |
| Multi-Field Formula | Full | Multi-field formula transform | Applies a formula across selected fields. |
| Multi-Row Formula | Full | Window / row-aware formula transform | Converts row-relative logic to window behavior, partitioned by Group By. |
| Named Entity Recognition (NER) | Full | [Text: NLP AI](/reference/workflow-steps/text-documents/nlp-ai/) (ner task) | Extracts entities (people, organizations, locations, dates, quantities, or a custom type list) from a text column through the LLM-backed NLP AI step. |
| Numeric Up Down | Full | Controlled numeric variable | Converts app numeric input to a typed variable. |
| Output Data | Full | Document / table output | Writes output to Document or PlaidCloud tables. |
| Overlay | Full | [Spatial Process](/reference/workflow-steps/spatial/spatial-process/) | Intersect, union, or cut two geometry columns. |
| PDF Input | Full | PDF extraction executor | Extracts text or tables from PDFs. |
| Point To Line | Full | Point To Line executor op | Threads each group's points into one `SequenceLine` per group, ordered by the sequence field. |
| Poly-Build | Full | [Spatial Poly-Build](/reference/workflow-steps/spatial/spatial-poly-build/) | Builds a polygon or convex hull per group of points. |
| Poly-Split | Full | [Spatial Poly-Split](/reference/workflow-steps/spatial/spatial-poly-split/) | One row per vertex, component polygon, or hole. |
| Portfolio Composer (Text / Table / Image / Layout / Render) | Partial | Report artifacts | Converts report content, layout, and rendering to PlaidCloud report output. A reusable multi-tab Excel writer with template-tab cloning is available on-platform — it preserves values, formats, styles, merged cells, and column widths — but automatic conversion of the Render tool's Alteryx report-packaging layer into that writer is not yet wired, and the template clone does not preserve charts, images, or pivot tables. |
| POS Tagger | Full | [Text: NLP AI](/reference/workflow-steps/text-documents/nlp-ai/) (pos task) | Tags each token's part of speech from a text column through the LLM-backed NLP AI step. |
| Predict | Full | [ML: Score](/reference/workflow-steps/machine-learning/ml-score/) | Scores data with the trained model table and appends a prediction column. |
| Radio Button | Full | Controlled workflow variable | Converts app radio choices to controlled input. |
| Random % Sample | Full | Table Extract (random) | Returns the exact count or percentage of records requested. |
| Record ID | Full | Row identifier transform | Adds a deterministic record identifier in the configured type and start value, restarting per group. |
| Redistribute | Full | Redistribute executor op | Reallocates a measure from one set of geographies onto another by area of overlap, appended as a `Redistributed` column. |
| RegEx | Full | Regular expression transform | Parses, matches, or replaces text. |
| Regression | Full | [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) | Fuses the Assisted Modeling chain into one ML Train step. |
| Report Map | Full | Map report artifact | Produces a cloud-native map/report artifact. |
| Run Command | Partial | [REST Request](/reference/workflow-steps/general/rest-request/) step against a REST connection (`curl`/`wget` only) | Converts a `curl` or `wget` command line to a REST Request step. Interpreter and script commands (`cscript`, PowerShell, Python, and similar), Excel-COM automation, filesystem operations, and opaque or workflow-launching commands are flagged by name for manual review rather than auto-converted. |
| Sample | Full | Sample transform | Keeps records by count, percentage, or grouping. |
| Select | Full | Select and schema projection step | Selects, renames, reorders, and retypes fields. |
| Smooth | Full | [Spatial Smooth](/reference/workflow-steps/spatial/spatial-smooth/) | Smooths each geometry over a number of passes. |
| Sort | Full | Sort transform | Sorts records by configured fields and directions. |
| Spatial Info | Full | [Spatial Info](/reference/workflow-steps/spatial/spatial-info/) | Area, length, centroid, and bounding rectangle as geodesic measures. |
| Spatial Match | Full | [Spatial Match](/reference/workflow-steps/spatial/spatial-match/) / [Spatial Match (Intersect / Unmatched)](/reference/workflow-steps/spatial/spatial-match-executor/) | Converts every relationship — Within, Contains, Intersects, Touches, Crosses, Overlaps, and Centroid-In — matched in the database or the workflow engine. |
| Spatial Process | Full | [Spatial Process](/reference/workflow-steps/spatial/spatial-process/) | Intersect, union, or cut geometry columns. |
| Summarize | Full | Aggregate transform | Groups and aggregates — sum, count, average, min, max, median, mode, standard deviation, variance, and count distinct. |
| Tab | Full | App tab grouping | Preserved as converted app structure. |
| Test | Full | Step condition | Converts test assertions to step conditions. |
| Text Box | Full | Controlled text variable | Converts app text input to a typed variable. |
| Text Input | Full | Inline table input | Creates inline data for the workflow. |
| Text Pre-processing | Full | NLP preprocessing executor | Normalizes and preprocesses text. |
| Text Summary | Full | [Text: NLP AI](/reference/workflow-steps/text-documents/nlp-ai/) (summary task) | Summarizes a text column to a configured maximum sentence count through the LLM-backed NLP AI step. |
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
| Zero-shot Text Classification | Full | [Text: NLP AI](/reference/workflow-steps/text-documents/nlp-ai/) (zeroshot task) | Classifies a text column against a per-row list of candidate labels, single- or multi-label, through the LLM-backed NLP AI step. |
| Find Nearest | Full | [Spatial Find Nearest](/reference/workflow-steps/spatial/spatial-find-nearest/) | Distance-ranked nearest-neighbor join — straight-line, and drive-time nearest (ranked by minutes on a road network) via PlaidCloud's self-hosted routing engine. Drive-time enabled per workspace. |
| Trade Area | Full | [Spatial Trade Area](/reference/workflow-steps/spatial/spatial-trade-area/) | Concentric buffers sized in real-world units — fixed-radius, and drive-time trade areas (minutes on a road network) via the self-hosted routing engine. Drive-time enabled per workspace. |
| Image Template | Full | Image Template executor op | Manual mode crops the image to each region you draw on the template. Automatic mode detects the page regions for you with an open-standard layout model and emits one row per region, each carrying its detected bounds and confidence for review; a page the model cannot read confidently is flagged by name rather than cropped. Open-standard detection can differ from Alteryx's own — review the detected regions, or use Manual mode for exact control. |
| Image Recognition | Full | Image recognition executor | Trains an image classifier in the workflow and scores new images against it, in place — no external account and no data leaves PlaidCloud. The classifier is retrained rather than copied from Alteryx, so results are a faithful approximation rather than a bit-for-bit match, and training runs on CPU. Enabled per workspace. |
| Geocoder | Full | Self-hosted geocoder | Geocodes addresses to coordinates and reverse-geocodes coordinates to addresses against PlaidCloud's own geocoder — no external account, no data leaves PlaidCloud. Enabled per workspace. |

Interface widgets (drop-downs, list boxes, check boxes, text/numeric/date
inputs, file and folder pickers), canvas objects (comments, links,
containers), and macro ports all convert as native controlled variables or
canvas objects. An Alteryx App's full interface layout — the `.yxwz` file's
`<Questions>` definition — converts to an interface manifest and renders
through a generic Panel "App Runner" at run time, so a converted app keeps
its original input form rather than only its individual controlled
variables.

## Spatial Tool Coverage

Every tool in the Alteryx **Spatial** palette has a PlaidCloud route, and every
one of those routes is a step you can also build by hand — conversion is a
convenience, not the only way in. See [Geospatial steps](/reference/workflow-steps/spatial/)
for the full reference and [Geospatial Analytics](/guides/workflows/geospatial-analytics/)
for how they fit together.

| Alteryx Spatial Tool | PlaidCloud Route | Runs In |
| --- | --- | --- |
| Buffer | [Spatial Buffer](/reference/workflow-steps/spatial/spatial-buffer/) | Workflow engine |
| Centroid | Centroid executor op | Workflow engine |
| Convex Hull | Convex Hull executor op | Workflow engine |
| Create Points | [Table Extract expression](/reference/workflow-steps/spatial/spatial-sql-recipes/) | Database |
| Distance | [Table Extract expression](/reference/workflow-steps/spatial/spatial-sql-recipes/) | Database |
| Find Nearest | [Spatial Find Nearest](/reference/workflow-steps/spatial/spatial-find-nearest/) | Database; routing service for drive-time |
| Generalize | [Spatial Generalize](/reference/workflow-steps/spatial/spatial-generalize/) | Workflow engine |
| Heat Map | [Heat Map (macro)](/reference/workflow-steps/macros/macro-heat-map/) | Workflow engine |
| Line To Polygon | Line To Polygon executor op | Workflow engine |
| Make Grid | [Spatial Make Grid](/reference/workflow-steps/spatial/spatial-make-grid/) | Workflow engine |
| Point To Line | Point To Line executor op | Workflow engine |
| Poly-Build | [Spatial Poly-Build](/reference/workflow-steps/spatial/spatial-poly-build/) | Workflow engine |
| Poly-Split | [Spatial Poly-Split](/reference/workflow-steps/spatial/spatial-poly-split/) | Workflow engine |
| Redistribute | Redistribute executor op | Workflow engine |
| Smooth | [Spatial Smooth](/reference/workflow-steps/spatial/spatial-smooth/) | Workflow engine |
| Spatial Info | [Spatial Info](/reference/workflow-steps/spatial/spatial-info/) | Workflow engine |
| Spatial Match | [Spatial Match](/reference/workflow-steps/spatial/spatial-match/) | Database |
| Spatial Match — intersection object, Unmatched | [Spatial Match (Intersect / Unmatched)](/reference/workflow-steps/spatial/spatial-match-executor/) | Workflow engine |
| Spatial Process | [Spatial Process](/reference/workflow-steps/spatial/spatial-process/) | Workflow engine |
| Trade Area (fixed-radius + drive-time) | [Spatial Trade Area](/reference/workflow-steps/spatial/spatial-trade-area/) | Workflow engine; routing service for drive-time |
| Pie Wedge Trade Area | [Pie Wedge Trade Area (macro)](/reference/workflow-steps/macros/macro-pie-wedge-trade-area/) | Workflow engine |
| Spatial file input | [Spatial File Import](/reference/workflow-steps/spatial/spatial-file-import/) | Workflow engine |
| Summarize — SpatialObjCombine, SpatialObjConvexHull | [Spatial Combine](/reference/workflow-steps/spatial/spatial-combine/) | Workflow engine |
| Report Map | [Report Map](/reference/workflow-steps/reports/report-map/) | Workflow engine |

**Drive-time trade areas and nearest** — Trade Area drive-time rings and Find
Nearest drive-time ranking run on PlaidCloud's self-hosted routing engine
(road-network isochrones and travel-time matrices), not a hosted third-party
API, so origin coordinates never leave the platform. Drive-time is enabled per
workspace. Routing and drive-time areas use OpenStreetMap data —
© OpenStreetMap contributors, available under the [Open Database License
(ODbL)](https://www.openstreetmap.org/copyright).

### Known Spatial Prerequisites

The spatial tools themselves convert; these are prerequisites on the input.

- **The `.geo` GeoFile format.** Alteryx's proprietary binary GeoFile has no
  open reader, so an import of one fails closed rather than crashing at run
  time. In Alteryx, re-export the layer to a standard spatial format —
  shapefile or GeoJSON — and import that instead; other spatial formats are
  unaffected. See
  [Migrate Spatial Alteryx Workflows](/guides/workflows/migrate-spatial-alteryx-workflows/#package-spatial-inputs).
- **The Peano key Spatial Info measure.** Peano key is a proprietary Alteryx
  spatial index with no public specification, so a Spatial Info that asks for it
  skips that one column and names it in a note. Every other Spatial Info measure
  — area, length, centroid, bounding rectangle, object type, part and point
  counts, and end points — converts.
- **Projected Create Points coordinates.** Create Points converts
  floating-point and integer (×1,000,000) lon/lat coordinates directly.
  Coordinates already in a projected system need reprojecting to WGS84 lon/lat
  upstream first, because the workflow does not record which projection they use.

## Calgary Tool Coverage

An Alteryx Calgary database (`.cydb`) is a proprietary indexed store PlaidCloud cannot open. Conversion treats each one as standing for one ordinary PlaidCloud table, named `calgary_<database name>`, so the tools built around it convert as ordinary table operations rather than refusing outright. See [Calgary Databases](/guides/workflows/migrate-alteryx-workflows/#calgary-databases) for how the stand-in table works, and [Calgary Join and Cross Count Append](/guides/workflows/migrate-alteryx-workflows/#calgary-join-and-cross-count-append) for the index-matching tools.

| Alteryx Calgary Tool | PlaidCloud Route | Converts |
| --- | --- | --- |
| Calgary Loader | Table Extract writing `calgary_<database>` | Yes, once the database is named and it stores at least one data field. |
| Calgary Input | Dynamic Document input reading `calgary_<database>`, with the saved query as filter | Yes, including a query built from an Or or wrapped in a Not, and a contains or starts-with filter (rebuilt as a SQL LIKE). Refuses on a spatial-lookup query and on Skip Records/Max Records limits. |
| Calgary Input (Count Only) / Calgary Cross Count | Aggregate transform over `calgary_<database>` | Yes, including a bucket built from an Or or wrapped in a Not. Refuses on a cross over more than one custom field, and on a count-only read naming no column to count over. |
| Calgary Join | Dynamic Document input matching each record of its input against `calgary_<database>` | When the incoming field is a plain value matched against a value index — including Count Only mode, which counts the database records each input record matched, a record matching nothing counting zero. Refuses when the field is spatial (rebuild as Spatial Match) or its type is unresolved, and on range-index or unmatched-output-wired Joins, on a Join naming no match field, and on a Join with nothing wired to its input. |
| Calgary Cross Count Append | Dynamic Document input matching each record, then a counted join over `calgary_<database>` | When the incoming field is a plain value matched against a value index: it counts, per input record, the database records matched, and a record that matched nothing counts zero. Refuses on a spatial or unresolved index (rebuild as Spatial Match), a custom-value cross-count grid, a range index, and a match naming no field. |

### Known Calgary Prerequisites

Most of these are prerequisites on the input rather than conversion limits.

- **A spatial-index match needs rebuilding as a Spatial Match.** A Calgary Join or Cross Count Append matched against a spatial index refuses, naming the stand-in table — the workflow records the index's name but not whether it holds ordinary values or spatial geometry, and a value match (an equality join) and a spatial match (point-in-polygon) are different operations. Export the database to a table and rebuild the match as a Join (value index) or a Spatial Match (spatial index).
- **A read limited by Skip Records or Max Records needs an explicit order.** The exported stand-in table carries no record order, so add an order column when you export if you need to take the first or last N records by position.
- **A demographic or reference database must be loaded first.** A Calgary read before its database has been loaded stops, naming the table to build. The `.cydb` file itself has no open reader, so re-export it in Alteryx (a Calgary Input into an Output Data tool writing CSV or Parquet) and import that as the named table — see [Unreadable .cydb (Calgary) Databases](/guides/workflows/troubleshoot-alteryx-imports/#unreadable-cydb-calgary-databases). This is the common case for the licensed demographic and reference `.cydb` files Alteryx ships (Experian, Census, and similar): no converter can reproduce that third-party data, so bring your own licensed reference data and load it into the named table — the same as the Geocoder reference data.
- **A Calgary Loader that stores no data field doesn't convert**, since the table it wrote would have no columns.
- **A custom-value cross-count grid doesn't convert yet.** A single plain cross-count field converts — it counts, per input record, the matching database records — but a grid of *named* custom values would append one count column per value, and Alteryx documents neither how many columns that is nor what it names them. Tracked for a future release, pending a reference export to reverse-engineer the column contract.

Value, range, contains and starts-with queries all convert to a filter; only a spatial-lookup query, an index operation with no column-level equivalent, does not.

## Connecting to External Systems

Alteryx's connector endpoints — Salesforce, HTTP, Google Analytics, Cassandra,
email, Hadoop, and Spark, in both directions — do not convert, because
PlaidCloud reaches these systems through a connection rather than through a
tool on the canvas. Each one refuses by name and states where the work
belongs:

| Alteryx Tool | Where It Goes in PlaidCloud |
| --- | --- |
| Salesforce Input / Output | A **Salesforce** connection |
| HTTP Input | A **REST Request** step against a **REST** connection |
| Google Analytics Input | **Import: Singer Source** with the Google Analytics tap |
| Cassandra Input | **Import: Singer Source** with the Cassandra tap |
| Email Input | **Import: Singer Source** with the GMail tap |
| Hadoop Input / Output | **Import: SQL** / **Export: SQL** through a Hive, Impala or Presto connection |
| Spark Input / Output | **Import: SQL** / **Export: SQL** through a Databricks connection |

Three of these have no write path at all. PlaidCloud reads Google Analytics
and Cassandra but never writes to them, so a Google Analytics Output or
Cassandra Output tool becomes an **Export: SQL** to a supported destination
instead. Email is not a data destination either: **Notify: Email** sends a
notification to people, so an Email Output tool becomes an Export step plus a
separate notification.

## Validating a Converted Workflow

For production workflows, validate converted outputs against trusted Alteryx
outputs — PlaidCloud validation focuses on schema, row count, and row values,
and ignores row order unless the workflow depends on it. Specialized
operations (spatial, fuzzy matching, OCR, NLP, reporting) run through managed
job executors that keep the workflow cloud-native; machine-learning pipelines
convert to the native [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/)
and [ML: Score](/reference/workflow-steps/machine-learning/ml-score/) steps.
See [Migrate Alteryx Workflows](/guides/workflows/migrate-alteryx-workflows/)
for the end-to-end import and validation guide.
