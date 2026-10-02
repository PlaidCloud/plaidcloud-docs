---
title: Report Single
description: Generate a single PDF report from a PlaidCloud workflow step using templates, data sources, and configurable layout options.
sidebar:
  order: 1
---

## Description



Renders a PDF report from an RML (Report Markup Language) template, populated with data from one or more PlaidCloud tables. Use this for formal, formatted reports — invoices, financial statements, regulatory filings, branded summaries.

The RML template defines the layout (page size, fonts, fixed text, table placement); the input tables supply the variable data. Compare with [Reports Batch](/reference/workflow-steps/reports/reports-batch/) when one template needs to produce many reports (e.g., one per customer).


## Names the Template Reads

The template reads each source on the **Report Data** tab, and each constant under **Report Constants (Fixed Values)**, by its name. New sources are named `new_source`, `new_source_2` and so on, which the template can read as they are; rename them to say what they hold.


## What's Checked When You Save

Every source and constant name must be:

- **Given** — a blank name is refused.
- **Its own** — two sources, two constants, or a source and a constant can't share a name, because the template would see only one of them: *Source name 'sales' is also a constant name; rename one of them.*
- **Readable by the template** — letters, digits and underscores, starting with a letter or underscore: *Constant name 'fiscal year' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*
- **Not a word the template reserves** — `True`, `False`, `None`, `true`, `false`, `none`, `not` and `self` read as something other than your data: *Source name 'self' is a word the template reserves, so it can't be read as a name.*


## Examples

No examples yet...
