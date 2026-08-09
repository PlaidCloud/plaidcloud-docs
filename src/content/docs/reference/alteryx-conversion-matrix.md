---
title: Alteryx Conversion Matrix
description: Coverage reference for how PlaidCloud converts Alteryx tools into Advanced workflow steps, macros, typed variables, Document assets, and managed job executors.
sidebar:
  order: 6
---

PlaidCloud converts Alteryx workflows, apps, and macros into Advanced workflows. The importer maps each Alteryx object to a native workflow step, macro construct, controlled variable, Document-backed file operation, or managed job executor.

Coverage levels:

- **Fully Converts** - converted directly to native PlaidCloud DAG behavior.
- **Converts With Validation** - converted to PlaidCloud behavior and should be validated against expected outputs for option-level parity.
- **Converts To Executor** - converted to a managed PlaidCloud job executor for specialized processing.
- **Cloud-Native Equivalent** - converted to a useful PlaidCloud artifact or operation that preserves the business purpose in a cloud-native form.
- **Annotation Only** - retained as workflow context, layout, or pass-through behavior with no separate runtime operation.

| Alteryx Object | Coverage Level | PlaidCloud Operation | Notes |
| --- | --- | --- | --- |
| Action | Fully Converts | Variable binding and conditional step configuration | Updates downstream settings from converted app inputs. |
| AlteryxSelect | Fully Converts | Select and schema projection step | Keeps selected, renamed, and reordered fields. |
| AppendFields | Fully Converts | Append fields transform | Appends fields from one stream to another. |
| AutoField | Converts With Validation | Auto field sizing transform | Preserves inferred field sizing intent; validate schema where precision matters. |
| BrowseV2 | Annotation Only | Browse or passthrough marker | Preserved for inspection without adding runtime work. |
| Buffer | Converts To Executor | [Spatial Buffer](/reference/workflow-steps/spatial/spatial-buffer/) | Grows each geometry by a fixed distance. |
| CalgaryCrossCount | Converts With Validation | [Calgary databases](/guides/workflows/migrate-alteryx-workflows/#calgary-databases) aggregate over the stand-in table | Groups indexed fields and counts each custom field's named values; a bucket built from an Or, or wrapped in a Not, now converts too. Refuses a cross over more than one custom field — see [Calgary Tool Coverage](#calgary-tool-coverage). |
| CalgaryInput | Converts With Validation | [Calgary databases](/guides/workflows/migrate-alteryx-workflows/#calgary-databases) input reading the stand-in table | Applies the saved query as a filter, now including one built from an Or or wrapped in a Not. Refuses contains/starts-with/spatial queries, and a read limited by Skip Records or Max Records. |
| CalgaryJoin | Converts With Validation | [Calgary Join](/guides/workflows/migrate-alteryx-workflows/#calgary-join-and-cross-count-append) matching each record against the stand-in table | Converts when the incoming field is a plain value matched to a value index, keeping the records that matched and carrying the input's columns through; refuses, naming Spatial Match, when the field is spatial — the workflow records the index's name but not its kind. See [Calgary Tool Coverage](#calgary-tool-coverage). |
| CalgaryLoader | Converts With Validation | [Calgary databases](/guides/workflows/migrate-alteryx-workflows/#calgary-databases) writing the stand-in table | Writes `calgary_<database>` from its input for every Calgary reader of that file to bind to. Refuses when two `.cydb` files of the same name would claim one table. |
| CheckBoxGroup | Fully Converts | Controlled workflow variable | Converts app check box choices to controlled user input. |
| Classification | Converts With Validation | ML Train step | Fuses with the upstream Assisted Modeling chain into a single ML Train step carrying the algorithm, target, features, and hyperparameters. |
| Condition | Fully Converts | Step condition with warning or error action | Uses workflow step conditions to trigger warnings, errors, or branches. |
| ControlParam | Fully Converts | Macro control parameter | Maps to PlaidCloud macro parameter handling. |
| CreatePoints | Fully Converts | [Table Extract](/reference/workflow-steps/spatial/spatial-sql-recipes/) with `geom_point` | Builds point geometry from longitude/latitude columns, in SQL. Non-floating-point coordinate modes are flagged rather than mis-scaled. |
| Create Samples | Converts With Validation | Three Table Extract steps, one per output | Splits the input into Estimation, Validation, and Holdout at the configured percentages. Each sample holds its configured share, drawn at random — not the same records Alteryx's seed picks, and a different set on each run. See [Random Sampling](/guides/workflows/migrate-alteryx-workflows/#random-sampling). |
| CrossTab | Fully Converts | Pivot or cross-tab transform | Converts rows to columns. |
| DataCleansePro | Converts With Validation | Data cleanse transform | Cleans whitespace, nulls, punctuation, and casing according to configured options. |
| Date | Fully Converts | Workflow variable date value | Emits ISO date values for downstream steps and conditions. |
| DateTime | Converts With Validation | Date and time transform | Converts date and time parsing or formatting logic. |
| DbFileInput | Converts With Validation | Document-backed file input or data materializer | Loads source files from Document into workflow data, including `.yxdb`, `.dbf`, Excel, and fixed-width `.flat`. A `.flat` needs its layout file packaged alongside the workflow; without it the step stops and names the file to supply. Alteryx `.geo` files are not read — the step stops rather than risk a wrong shape. |
| DbFileOutput | Fully Converts | Document-backed file output or table write | Writes output data to Document or PlaidCloud tables. |
| Detour | Fully Converts | Conditional branch routing | Converts route selection to DAG conditions. |
| DetourEnd | Fully Converts | Conditional branch merge | Rejoins conditionally selected branches. |
| Directory | Fully Converts | Document directory listing | Lists files from a Document path. |
| Distance | Fully Converts | [Table Extract](/reference/workflow-steps/spatial/spatial-sql-recipes/) with `ST_DISTANCE_SPHERE` | Geodesic point-to-point distance and bearing, in SQL, in the requested unit. |
| Download | Converts To Executor | HTTP download executor | Downloads external data or artifacts. |
| DropDown | Fully Converts | Controlled workflow variable | Converts app drop-down choices to controlled user input. |
| DynamicInput | Converts With Validation | Dynamic Document input | Resolves file patterns or variable-driven inputs at runtime. |
| DynamicRename | Fully Converts | Dynamic rename transform | Renames fields using metadata or configured rules. |
| DynamicReplace | Converts With Validation | Dynamic replace transform | Applies replacement rules from a second data stream. |
| DynamicSelect | Fully Converts | Dynamic field selection transform | Selects fields by type, name, or rule. |
| Error | Fully Converts | Step condition with error action | Converts configured error behavior to PlaidCloud step conditions. |
| FileBrowse | Fully Converts | Controlled Document file variable | Lets users choose a file for a converted app run. |
| Filter | Fully Converts | Filter transform | Splits records by expression into true and false paths. |
| FindNearest | Fully Converts | [Spatial Find Nearest](/reference/workflow-steps/spatial/spatial-find-nearest/) | Runs as a distance-ranked join in the database; adds the computed distance column. |
| Fit | Converts With Validation | ML Train step | Collapses into the fused ML Train step; the trained model is written as a one-row model table. |
| FolderBrowse | Fully Converts | Controlled Document folder variable | Lets users choose a folder for a converted app run. |
| Formula | Fully Converts | Formula transform | Converts field expressions to PlaidCloud expressions or SQL-backed logic. |
| FuzzyMatch | Converts To Executor | Fuzzy matching executor | Uses managed fuzzy matching for match keys, thresholds, and candidate review. |
| Generalize | Converts To Executor | [Spatial Generalize](/reference/workflow-steps/spatial/spatial-generalize/) | Simplifies geometry to a tolerance, preserving topology. |
| HtmlBox | Cloud-Native Equivalent | Report text or HTML artifact | Preserves content in PlaidCloud report or artifact output. |
| Barcode | Converts To Executor | Barcode executor | Reads or writes barcodes in the configured symbology. A row with no readable barcode returns empty; several return a joined list. |
| ImageProcessing | Converts To Executor | Image transform executor | Applies the tool's pipeline in canvas order — grayscale, scale, crop, and custom-angle rotation — writing `<field>_processed`. Thresholding, brightness balance, OCR optimization, and automatic alignment stop with a message naming the setting, because Alteryx records the choice but not the values needed to reproduce it. |
| ImageProfile | Converts To Executor | Image profile executor | Reports image dimensions, mode, format, and channel count, or luminance statistics. Column names are PlaidCloud's — Alteryx records none. |
| ImageRecognition | Converts With Validation | ML Score step | Stops with a message pointing at ML Score, which reads the same trained model table. The tool's own VGG16 transfer learning is not reproduced. |
| ImageTemplate | Converts With Validation | Manual region extraction | Stops with a message naming the missing page-region detection. Extract the regions with a Formula or Text step instead. |
| ImageToText | Converts To Executor | OCR executor | Extracts text from images through managed OCR. |
| Insights | Cloud-Native Equivalent | PlaidCloud dashboard or artifact output | Creates a cloud-native review artifact for repeatable sharing and review. |
| Join | Fully Converts | Join transform | Produces joined, left-only, and right-only streams. |
| JoinMultiple | Fully Converts | Multi-join transform | Joins multiple input streams. |
| Label | Annotation Only | Canvas label | Preserved as workflow context. |
| LabelGroup | Annotation Only | Canvas label group | Preserved as workflow context. |
| Link | Annotation Only | Canvas link or annotation | Preserved as workflow context. |
| ListBox | Fully Converts | Controlled workflow variable | Converts app list selections to controlled user input. |
| MacroInput | Fully Converts | PlaidCloud macro input port | Maps directly to a PlaidCloud macro input step. |
| MacroOutput | Fully Converts | PlaidCloud macro output port | Maps directly to a PlaidCloud macro output step. |
| MakeGrid | Converts To Executor | [Spatial Make Grid](/reference/workflow-steps/spatial/spatial-make-grid/) | Tiles an extent into square cells of a fixed ground size, one row per cell. |
| Map | Cloud-Native Equivalent | Map artifact or spatial visualization | Creates a PlaidCloud map artifact for cloud review and sharing. |
| MapInput | Converts With Validation | [Spatial File Import](/reference/workflow-steps/spatial/spatial-file-import/) | Reads MapInfo, ESRI, KML, and GeoJSON files with their sidecars. The proprietary `.geo` GeoFile format is rejected at conversion. |
| Message | Fully Converts | Step condition with warning or message action | Emits workflow warning, message, or error based on configured condition. |
| Modeling | Converts With Validation | ML Train step or placeholder | Fuses into the ML Train step when the pipeline's model choice is saved in the workflow; a lone Assisted Modeling wizard is kept as a placeholder noting the recovered target variable. |
| MultiFieldFormula | Converts With Validation | Multi-field formula transform | Applies a formula across selected fields. |
| MultiRowFormula | Converts With Validation | Window or row-aware formula transform | Converts row-relative logic to PlaidCloud window behavior where possible. |
| NumericUpDown | Fully Converts | Controlled numeric workflow variable | Converts app numeric input to a typed variable. |
| Overlay | Converts To Executor | [Spatial Process](/reference/workflow-steps/spatial/spatial-process/) | Intersect, union, or cut two geometry columns. |
| PDFInput | Converts To Executor | PDF extraction executor | Extracts text or tables from PDFs. |
| PlotlyCharting | Cloud-Native Equivalent | Chart artifact | Creates a PlaidCloud chart artifact from converted data. |
| PolyBuild | Converts To Executor | [Spatial Poly-Build](/reference/workflow-steps/spatial/spatial-poly-build/) | Builds a polygon or convex hull per group of points. |
| PolySplit | Converts To Executor | [Spatial Poly-Split](/reference/workflow-steps/spatial/spatial-poly-split/) | One row per vertex, component polygon, or hole. |
| PortfolioComposerImage | Cloud-Native Equivalent | Report image artifact | Places images into generated PlaidCloud report artifacts. |
| PortfolioComposerLayout | Cloud-Native Equivalent | Report layout artifact | Converts layout intent to PlaidCloud report generation. |
| PortfolioComposerRender | Cloud-Native Equivalent | Report render artifact | Renders report output as a PlaidCloud artifact. |
| PortfolioComposerTable | Cloud-Native Equivalent | Report table artifact | Converts report table content to PlaidCloud report output. |
| PortfolioComposerText | Cloud-Native Equivalent | Report text artifact | Converts report text content to PlaidCloud report output. |
| Predict | Converts With Validation | ML Score step | Scores the data input with the trained model table and appends a predicted column. |
| RadioButtonGroup | Fully Converts | Controlled workflow variable | Converts app radio choices to controlled user input. |
| Random % Sample | Converts With Validation | Table Extract with a random record position | Returns exactly the number or the percentage of records asked for. With a fixed seed set, the count is exact but the records are not the ones Alteryx's seed picks. See [Random Sampling](/guides/workflows/migrate-alteryx-workflows/#random-sampling). |
| RecordID | Fully Converts | Row identifier transform | Adds a deterministic record identifier. |
| RegEx | Fully Converts | Regular expression transform | Parses, matches, or replaces text using configured expressions. |
| Regression | Converts With Validation | ML Train step | Fuses with the upstream Assisted Modeling chain into a single ML Train step carrying the algorithm, target, features, and hyperparameters. |
| ReportMap | Cloud-Native Equivalent | Map report artifact | Produces a cloud-native map/report artifact. |
| Sample | Fully Converts | Sample transform | Keeps configured records by count, percentage, or grouping rule. |
| Smooth | Converts To Executor | [Spatial Smooth](/reference/workflow-steps/spatial/spatial-smooth/) | Smooths each geometry over a number of passes. |
| Sort | Fully Converts | Sort transform | Sorts records by configured fields and directions. |
| SpatialInfo | Converts To Executor | [Spatial Info](/reference/workflow-steps/spatial/spatial-info/) | Area, length, centroid, and bounding rectangle as WGS84 geodesic measures. Object type, part/point counts, Peano key, and end-point coordinates are skipped with a note. |
| SpatialMatch | Converts With Validation | [Spatial Match](/reference/workflow-steps/spatial/spatial-match/) or [Spatial Match (Intersect / Unmatched)](/reference/workflow-steps/spatial/spatial-match-executor/) | Plain matched pairs run in the database; the intersection-geometry and Unmatched outputs run in the workflow engine. |
| SpatialProcess | Converts To Executor | [Spatial Process](/reference/workflow-steps/spatial/spatial-process/) | Intersect, union, or cut, with optional dropping of empty results. |
| Summarize | Fully Converts | Aggregate transform | Groups and aggregates records. |
| Tab | Annotation Only | App tab grouping | Preserved as converted app structure where relevant. |
| Test | Fully Converts | Step condition with warning or error action | Converts test assertions to PlaidCloud conditions. |
| TextBox | Fully Converts | Controlled text workflow variable | Converts app text input to a typed variable. |
| TextInput | Fully Converts | Inline table input | Creates inline data for the workflow. |
| TextPreProcessing | Converts To Executor | NLP preprocessing executor | Performs text normalization and preprocessing. |
| TextToColumns | Fully Converts | Split columns transform | Splits text into fields or rows. |
| Tile | Converts With Validation | Tile or grouping transform | Assigns tile groups according to configured rules. |
| ToolContainer | Annotation Only | Canvas container | Preserved as visual workflow organization. |
| TopicModel | Converts To Executor | Topic modeling executor | Runs topic modeling through managed NLP execution. |
| TradeArea | Converts To Executor | [Spatial Trade Area](/reference/workflow-steps/spatial/spatial-trade-area/) | Concentric buffers sized in real-world units. Fixed-radius mode; drive-time trade areas are not covered. |
| Transformation | Converts With Validation | Transform step | Converts configured transformation logic to PlaidCloud expressions or SQL. |
| Transpose | Fully Converts | Unpivot transform | Converts columns to rows. |
| Tree | Fully Converts | Controlled workflow variable | Converts app tree selection to controlled user input. |
| Union | Fully Converts | Union transform | Combines streams by name, position, or configured field rules. |
| Unique | Fully Converts | Unique and duplicate split transform | Separates first unique records from duplicates. |
| VisualLayout | Annotation Only | Canvas layout metadata | Preserved as design context. |
| WordCloud | Cloud-Native Equivalent | Text visualization artifact | Creates a PlaidCloud visualization artifact from text analysis output. |
| XMLParse | Converts With Validation | XML parse transform | Extracts XML fields into workflow data. |
| Missing plugin reference | Fully Converts | Macro invocation or generated placeholder when resolved | Imports known macro sources and maps macro calls to PlaidCloud macro steps. |

## Spatial Tool Coverage

Every tool in the Alteryx **Spatial** palette has a PlaidCloud route, and every
one of those routes is a step you can also build by hand — conversion is a
convenience, not the only way in. See [Geospatial steps](/reference/workflow-steps/spatial/)
for the full reference and [Geospatial Analytics](/guides/workflows/geospatial-analytics/)
for how they fit together.

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
| Spatial Match — intersection object, Unmatched | [Spatial Match (Intersect / Unmatched)](/reference/workflow-steps/spatial/spatial-match-executor/) | Workflow engine |
| Spatial Process | [Spatial Process](/reference/workflow-steps/spatial/spatial-process/) | Workflow engine |
| Trade Area (fixed radius) | [Spatial Trade Area](/reference/workflow-steps/spatial/spatial-trade-area/) | Workflow engine |
| Pie Wedge Trade Area | [Pie Wedge Trade Area (macro)](/reference/workflow-steps/macros/macro-pie-wedge-trade-area/) | Workflow engine |
| Spatial file input | [Spatial File Import](/reference/workflow-steps/spatial/spatial-file-import/) | Workflow engine |
| Summarize — SpatialObjCombine, SpatialObjConvexHull | [Spatial Combine](/reference/workflow-steps/spatial/spatial-combine/) | Workflow engine |
| Report Map | [Report Map](/reference/workflow-steps/reports/report-map/) | Workflow engine |

### Known Spatial Gaps

- **Drive-time trade areas.** Trade Area converts in fixed-radius mode. There is
  no factor that turns minutes on a road network into a distance, so drive-time
  sizing does not convert.
- **The `.geo` GeoFile format.** Alteryx's proprietary binary GeoFile cannot be
  read. Conversion fails closed rather than emitting an import that crashes at
  run time; other spatial formats are unaffected.
- **Some Spatial Info measures.** Object type, part count, point count, Peano
  key, and end-point coordinates have no verified parity definition and are
  skipped. Conversion names the dropped measures in a note.
- **Non-floating-point Create Points modes.** Coordinates stored as integers
  scaled by 1,000,000, or already projected, are flagged for upstream rescaling
  rather than converted into mis-scaled points.
- **Make Grid and Poly-Split configuration forms.** Both step types run
  correctly, but neither has a configuration form in the workflow designer yet;
  converted steps carry their settings, and hand-authoring goes through the API
  or MCP.

## Calgary Tool Coverage

An Alteryx Calgary database (`.cydb`) is a proprietary indexed store PlaidCloud cannot open. Conversion treats each one as standing for one ordinary PlaidCloud table, named `calgary_<database name>`, so the tools built around it convert as ordinary table operations rather than refusing outright. See [Calgary Databases](/guides/workflows/migrate-alteryx-workflows/#calgary-databases) for how the stand-in table works, and [Calgary Join and Cross Count Append](/guides/workflows/migrate-alteryx-workflows/#calgary-join-and-cross-count-append) for the index-matching tools.

| Alteryx Calgary Tool | PlaidCloud Route | Converts |
| --- | --- | --- |
| Calgary Loader | Table Extract writing `calgary_<database>` | Yes, once the database is named and it stores at least one data field. |
| Calgary Input | Dynamic Document input reading `calgary_<database>`, with the saved query as filter | Yes, including a query built from an Or or wrapped in a Not. Refuses on contains/starts-with/spatial queries and on Skip Records/Max Records limits. |
| Calgary Input (Count Only) / Calgary Cross Count | Aggregate transform over `calgary_<database>` | Yes, including a bucket built from an Or or wrapped in a Not. Refuses on a cross over more than one custom field, and on a count-only read naming no column to count over. |
| Calgary Join | Dynamic Document input matching each record of its input against `calgary_<database>` | When the incoming field is a plain value matched against a value index. Refuses when the field is spatial (rebuild as Spatial Match) or its type is unresolved, and on count-only, range-index, or unmatched-output-wired Joins, on a Join naming no match field, and on a Join with nothing wired to its input. |
| Calgary Cross Count Append | — | Never. Rebuild as a Cross Count over `calgary_<database>`, joined back to this input. |

### Known Calgary Gaps

- **Calgary Cross Count Append never converts.** It appends the *counts* of matching database records, and Alteryx doesn't document what columns that produces beyond a single field — there is no shape to build with confidence, spatial index or not.
- **A Calgary Join or Cross Count Append matched against a spatial index refuses**, naming the stand-in table and pointing at Spatial Match — the workflow file records the index's name but not whether it holds ordinary values or spatial geometry.
- **Contains, starts-with, and spatial-lookup queries don't convert.** Only indexed value and range comparisons do.
- **A read limited by Skip Records or Max Records doesn't convert** — the stand-in table carries no record order.
- **A Calgary Loader that stores no data field doesn't convert**, since the table it wrote would have no columns.
- **A database read before it has been loaded stops, naming the table to build.** This is the common case for the demographic and reference `.cydb` files Alteryx ships, which nothing in your workflow wrote.

## How Coverage Is Measured

The coverage level in the table above is a statement about a **tool**. It says
the importer has a real route for that tool — not that every one of its
configuration options has been exercised.

Parity is tracked at a finer grain: one **tool × permutation**, where a
permutation is a distinct configuration path through the tool. A Join's join
type, a Sample's mode, a Summarize's aggregation action and a file input's
format are each their own permutation. Every permutation carries three gates,
and all three are required:

| Gate | Question |
| --- | --- |
| Converts | Does it produce a real step, rather than a refusal? |
| Runs | Does that step execute without erroring? |
| Correct | Is the output what Alteryx would produce? |

A permutation that ends in a **specific refusal naming what is missing** is an
acceptable outcome. It is reported separately and never counted as a pass — you
find out at conversion time, in a message that tells you what to build by hand.
A conversion that runs and returns a **quietly wrong answer** is treated as
worse than a refusal, which is why several options in the Known Gaps lists are
refused rather than approximated.

Because there is no Alteryx licence in the loop, the "Correct" gate is never
recorded on judgement. Each verdict names its oracle: Alteryx's own published
documentation, the output schema Alteryx wrote into the workflow file, the
tool's own internal contract (row counts, column sets, types), or agreement
between two independent conversion paths. A verdict with no named oracle is
recorded as unverified, however good the underlying test is.

The scoreboard is regenerated from the test suite on every pull request, and a
permutation that used to pass a gate cannot quietly stop passing it.

**What this means for you:** treat *Fully Converts* as "this tool has a route",
and validate the specific options your workflows use — which is what the
validation guidance below is for. The Known Gaps sections on this page name the
options that are deliberately refused.

## Validation Notes

For production workflows, validate converted outputs against trusted Alteryx outputs. PlaidCloud validation focuses on schema, row count, and row values, and ignores row order unless the workflow explicitly depends on ordered data.

Specialized operations such as spatial processing, fuzzy matching, OCR, NLP, and reporting may run through managed job executors. These routes keep the converted workflow cloud-native while covering capabilities that are not best expressed as a single SQL transform. Machine-learning pipelines convert to the native [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) and [ML: Score](/reference/workflow-steps/machine-learning/ml-score/) steps.
