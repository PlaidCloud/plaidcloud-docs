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
| Buffer | Converts To Executor | Spatial executor | Creates buffered geometries with validation against spatial fixtures. |
| CheckBoxGroup | Fully Converts | Controlled workflow variable | Converts app check box choices to controlled user input. |
| Classification | Converts With Validation | ML Train step | Fuses with the upstream Assisted Modeling chain into a single ML Train step carrying the algorithm, target, features, and hyperparameters. |
| Condition | Fully Converts | Step condition with warning or error action | Uses workflow step conditions to trigger warnings, errors, or branches. |
| ControlParam | Fully Converts | Macro control parameter | Maps to PlaidCloud macro parameter handling. |
| CreatePoints | Fully Converts | Geometry point creation transform | Creates point geometry from coordinate fields. |
| CrossTab | Fully Converts | Pivot or cross-tab transform | Converts rows to columns. |
| DataCleansePro | Converts With Validation | Data cleanse transform | Cleans whitespace, nulls, punctuation, and casing according to configured options. |
| Date | Fully Converts | Workflow variable date value | Emits ISO date values for downstream steps and conditions. |
| DateTime | Converts With Validation | Date and time transform | Converts date and time parsing or formatting logic. |
| DbFileInput | Fully Converts | Document-backed file input or data materializer | Loads source files from Document into workflow data. |
| DbFileOutput | Fully Converts | Document-backed file output or table write | Writes output data to Document or PlaidCloud tables. |
| Detour | Fully Converts | Conditional branch routing | Converts route selection to DAG conditions. |
| DetourEnd | Fully Converts | Conditional branch merge | Rejoins conditionally selected branches. |
| Directory | Fully Converts | Document directory listing | Lists files from a Document path. |
| Distance | Converts To Executor | Spatial distance executor | Computes distance using managed spatial processing. |
| Download | Converts To Executor | HTTP download executor | Downloads external data or artifacts. |
| DropDown | Fully Converts | Controlled workflow variable | Converts app drop-down choices to controlled user input. |
| DynamicInput | Converts With Validation | Dynamic Document input | Resolves file patterns or variable-driven inputs at runtime. |
| DynamicRename | Fully Converts | Dynamic rename transform | Renames fields using metadata or configured rules. |
| DynamicReplace | Converts With Validation | Dynamic replace transform | Applies replacement rules from a second data stream. |
| DynamicSelect | Fully Converts | Dynamic field selection transform | Selects fields by type, name, or rule. |
| Error | Fully Converts | Step condition with error action | Converts configured error behavior to PlaidCloud step conditions. |
| FileBrowse | Fully Converts | Controlled Document file variable | Lets users choose a file for a converted app run. |
| Filter | Fully Converts | Filter transform | Splits records by expression into true and false paths. |
| FindNearest | Converts To Executor | Spatial nearest-neighbor executor | Finds nearest spatial records with managed spatial processing. |
| Fit | Converts With Validation | ML Train step | Collapses into the fused ML Train step; the trained model is written as a one-row model table. |
| FolderBrowse | Fully Converts | Controlled Document folder variable | Lets users choose a folder for a converted app run. |
| Formula | Fully Converts | Formula transform | Converts field expressions to PlaidCloud expressions or SQL-backed logic. |
| FuzzyMatch | Converts To Executor | Fuzzy matching executor | Uses managed fuzzy matching for match keys, thresholds, and candidate review. |
| Generalize | Converts To Executor | Spatial generalization executor | Simplifies geometry while preserving the requested spatial intent. |
| HtmlBox | Cloud-Native Equivalent | Report text or HTML artifact | Preserves content in PlaidCloud report or artifact output. |
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
| Map | Cloud-Native Equivalent | Map artifact or spatial visualization | Creates a PlaidCloud map artifact for cloud review and sharing. |
| MapInput | Converts With Validation | Spatial input materializer | Loads spatial input data into the converted workflow. |
| Message | Fully Converts | Step condition with warning or message action | Emits workflow warning, message, or error based on configured condition. |
| Modeling | Converts With Validation | ML Train step or placeholder | Fuses into the ML Train step when the pipeline's model choice is saved in the workflow; a lone Assisted Modeling wizard is kept as a placeholder noting the recovered target variable. |
| MultiFieldFormula | Converts With Validation | Multi-field formula transform | Applies a formula across selected fields. |
| MultiRowFormula | Converts With Validation | Window or row-aware formula transform | Converts row-relative logic to PlaidCloud window behavior where possible. |
| NumericUpDown | Fully Converts | Controlled numeric workflow variable | Converts app numeric input to a typed variable. |
| Overlay | Converts To Executor | Spatial overlay executor | Performs spatial overlay operations through managed spatial processing. |
| PDFInput | Converts To Executor | PDF extraction executor | Extracts text or tables from PDFs. |
| PlotlyCharting | Cloud-Native Equivalent | Chart artifact | Creates a PlaidCloud chart artifact from converted data. |
| PolyBuild | Converts To Executor | Spatial polygon build executor | Builds polygon geometry from spatial inputs. |
| PortfolioComposerImage | Cloud-Native Equivalent | Report image artifact | Places images into generated PlaidCloud report artifacts. |
| PortfolioComposerLayout | Cloud-Native Equivalent | Report layout artifact | Converts layout intent to PlaidCloud report generation. |
| PortfolioComposerRender | Cloud-Native Equivalent | Report render artifact | Renders report output as a PlaidCloud artifact. |
| PortfolioComposerTable | Cloud-Native Equivalent | Report table artifact | Converts report table content to PlaidCloud report output. |
| PortfolioComposerText | Cloud-Native Equivalent | Report text artifact | Converts report text content to PlaidCloud report output. |
| Predict | Converts With Validation | ML Score step | Scores the data input with the trained model table and appends a predicted column. |
| RadioButtonGroup | Fully Converts | Controlled workflow variable | Converts app radio choices to controlled user input. |
| RecordID | Fully Converts | Row identifier transform | Adds a deterministic record identifier. |
| RegEx | Fully Converts | Regular expression transform | Parses, matches, or replaces text using configured expressions. |
| Regression | Converts With Validation | ML Train step | Fuses with the upstream Assisted Modeling chain into a single ML Train step carrying the algorithm, target, features, and hyperparameters. |
| ReportMap | Cloud-Native Equivalent | Map report artifact | Produces a cloud-native map/report artifact. |
| Sample | Fully Converts | Sample transform | Keeps configured records by count, percentage, or grouping rule. |
| Smooth | Converts To Executor | Spatial smoothing executor | Smooths geometry through managed spatial processing. |
| Sort | Fully Converts | Sort transform | Sorts records by configured fields and directions. |
| SpatialInfo | Converts With Validation | Spatial metadata transform | Extracts spatial metadata such as area, length, centroid, or bounds. |
| SpatialMatch | Converts To Executor | Spatial match executor | Matches records by spatial relationship. |
| SpatialProcess | Converts To Executor | Spatial processing executor | Runs spatial operations that require executor-backed geometry handling. |
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
| TradeArea | Converts To Executor | Spatial trade area executor | Creates trade area geometry through managed spatial processing. |
| Transformation | Converts With Validation | Transform step | Converts configured transformation logic to PlaidCloud expressions or SQL. |
| Transpose | Fully Converts | Unpivot transform | Converts columns to rows. |
| Tree | Fully Converts | Controlled workflow variable | Converts app tree selection to controlled user input. |
| Union | Fully Converts | Union transform | Combines streams by name, position, or configured field rules. |
| Unique | Fully Converts | Unique and duplicate split transform | Separates first unique records from duplicates. |
| VisualLayout | Annotation Only | Canvas layout metadata | Preserved as design context. |
| WordCloud | Cloud-Native Equivalent | Text visualization artifact | Creates a PlaidCloud visualization artifact from text analysis output. |
| XMLParse | Converts With Validation | XML parse transform | Extracts XML fields into workflow data. |
| Missing plugin reference | Fully Converts | Macro invocation or generated placeholder when resolved | Imports known macro sources and maps macro calls to PlaidCloud macro steps. |

## Validation Notes

For production workflows, validate converted outputs against trusted Alteryx outputs. PlaidCloud validation focuses on schema, row count, and row values, and ignores row order unless the workflow explicitly depends on ordered data.

Specialized operations such as spatial processing, fuzzy matching, OCR, NLP, and reporting may run through managed job executors. These routes keep the converted workflow cloud-native while covering capabilities that are not best expressed as a single SQL transform. Machine-learning pipelines convert to the native [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) and [ML: Score](/reference/workflow-steps/machine-learning/ml-score/) steps.
