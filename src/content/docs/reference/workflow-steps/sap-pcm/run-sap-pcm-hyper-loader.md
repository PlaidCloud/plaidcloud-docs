---
title: Run SAP PCM Hyper Loader
description: Run the SAP PCM Hyper Loader from a PlaidCloud workflow step to perform high-speed bulk data loading into PCM models.
---

## Description


Loads an SAP Profitability and Cost Management (PCM) model using direct table loads. This process is significantly faster than Databridge. The Hyper Loader supports virtually all of the current PCM data, assignment, and structure tables.


This is the current list of available loading targets:


* Activity Aliases
* Activity Dimensional Hierarchy
* Activity Driver Aliases
* Activity Driver Dimensional Hierarchy
* Activity Driver Value
* BOM Default Makeup
* BOM External Unit Rate
* BOM Makeup
* BOM Production Volume
* BOM Units Sold
* Cost Object 1 Aliases
* Cost Object 1 Dimensional Hierarchy
* Cost Object 2 Aliases
* Cost Object 2 Dimensional Hierarchy
* Cost Object 3 Aliases
* Cost Object 3 Dimensional Hierarchy
* Cost Object 4 Aliases
* Cost Object 4 Dimensional Hierarchy
* Cost Object 5 Aliases
* Cost Object 5 Dimensional Hierarchy
* Cost Object Assignment
* Cost Object Driver
* Line Item Aliases
* Line Item Detail Aliases
* Line Item Detail Dimensional Hierarchy
* Line Item Detail Value
* Line Item Dimensional Hierarchy
* Line Item Direct Activity Assignment
* Line Item Resource Driver Assignment
* Line Item Value
* Period Aliases
* Period Dimensional Hierarchy
* Resource Driver Aliases
* Resource Driver Dimensional Hierarchy
* Resource Driver Split
* Resource Driver Value
* Responsibility Center Aliases
* Responsibility Center Dimensional Hierarchy
* Revenue
* Revenue Aliases
* Revenue Dimensional Hierarchy
* Service Aliases
* Service Dimensional Hierarchy
* Spread Aliases
* Spread Dimensional Hierarchy
* Spread Value
* Version Aliases
* Version Dimensional Hierarchy
* Worksheet 1 Aliases
* Worksheet 1 Dimensional Hierarchy
* Worksheet 2 Aliases
* Worksheet 2 Dimensional Hierarchy
* Worksheet Value

## Our Credentials


PlaidCloud is an official SAP Partner and a preferred vendor of services related to SAP PCM model design and implementation.


## What's Checked When You Save

Each source on the **Load Steps** tab stages into the loader table chosen as its **Target Load Table**, matched by column name. Saving is refused, naming the source, when:

- A source has no Target Load Table, or one that isn't a PCM loader table — *Source 'activity_aliases' loads into 'ACTIVITY', which isn't a PCM loader table.*
- A source's columns don't match its loader table: a loader table column is missing, has a different type from the loader table's, or has no source, expression or constant — *Source 'activity_aliases' doesn't match loader table PPLOAD_ACTIVITY_AL: missing DEFAULTALIAS; no source, expression or constant for ALIAS.* **Reset Target Columns to Schema** refills a source's target columns from its loader table.
- Two sources share a name. Each source is exported to a file named after it, so one would overwrite the other — *Source name 'activity_aliases' is used more than once; each source needs its own, or one overwrites the other.*


## Examples


Select Agent to Use from the dropdown. Enter model name and select the load package storage path location, then select the child folder desired from within. Use the Table Data Selection below to select the source table model and the target load table. Inspect source>>propagate both sides of the table will reveal the data. Click “Save and Run Step” when the data is entered and you have added any expressions.
