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
- **Test results table** — write the list of files that *would* be deleted to a table instead of deleting them.

<Aside type="caution" title="Dry Run First">
  Point the step at a test results table and run it once before letting it
  delete anything. Deletion is not reversible, and a wrong path with
  **Recursive** on reaches further than you expect.
</Aside>

## Related

- [Document steps](/reference/workflow-steps/document/)
- [Delete Document File](/reference/workflow-steps/document/delete-document-file/)
- [Directory Listing](/reference/workflow-steps/document/directory-listing/)
