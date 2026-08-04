---
title: Delete Old Files
description: Delete files in a document account older or newer than a chosen age, with a dry-run listing before anything is removed.
sidebar:
  order: 23
---

import { Aside } from '@astrojs/starlight/components';

## Description

Deletes files in a document account based on age. Use it to keep an export or landing folder from growing without bound — drop yesterday's extracts, or clear archives older than a year.

## Configuration

### Files to Delete

- **File path** — the document account and folder to work in.
- **Age** — a number plus a unit: minutes, hours, days, months, or years.
- **Before or after** — delete files last modified **before** the cutoff (the usual clean-up direction) or **after** it.
- **Recursive** — off by default. Turn it on to include subfolders.
- **Test results table** — the table the step editor's **Test** button writes its
  preview of matching files into.

<Aside type="caution" title="Preview With Test, Not by Running the Step">
  The preview comes from the **Test** button while you are editing the step.
  Running the step in a workflow always deletes — there is no dry-run mode, and
  the test results table does not divert it. Deletion is not reversible, and a
  wrong path with **Recursive** on reaches further than you expect, so check the
  preview before you schedule it.
</Aside>

## Related

- [Document steps](/reference/workflow-steps/document/)
- [Delete Document File](/reference/workflow-steps/document/delete-document-file/)
- [Directory Listing](/reference/workflow-steps/document/directory-listing/)
