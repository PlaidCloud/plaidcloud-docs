---
title: Reports Batch
description: Generate batch PDF reports from a PlaidCloud workflow step to produce multiple reports from templates with varying data inputs.
sidebar:
  order: 2
---

## Description



Renders many PDF reports from a single RML template, driven by a control table. One report is produced per row of the control table, with each row's column values used as parameters in that report's rendering.

Common use: customer statements (one PDF per customer), per-unit financials (one PDF per business unit), invoices (one PDF per order). Compare with [Report Single](/reference/workflow-steps/reports/report-single/) for one-off report generation.


## Names the Template Reads

The template reads each source on the **Report Data** tab, and each target column of the **Batch Record Values Data Source** mapping, by its name. There is no constants section: each batch row supplies the template's values for its report. New sources are named `new_source`, `new_source_2` and so on, which the template can read as they are.


## What's Checked When You Save

Every source and batch column name must be given, its own, and readable by the template — the same rules as [Report Single](/reference/workflow-steps/reports/report-single/), with batch columns in place of constants: *Batch column name 'unit id' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*

Saving with a batch source table chosen but an empty batch mapping fills the mapping from that table, as Populate would.


## Empty Batch Table

When the batch source table has no rows, the step finishes successfully with a warning that names the batch table, and no reports are produced.


## Examples

No examples yet...
