---
title: Merge Multiple PDFs
description: Merge multiple PDF files into a single combined document in a PlaidCloud workflow step for report assembly and consolidation.
sidebar:
  order: 17
---

Joins multiple PDF files into a single PDF, preserving page order and bookmarks where present. Unlike [Concatenate files](/reference/workflow-steps/document/concatenate-files/), this step understands the PDF format and produces a valid merged document.

## Inputs

- **Source PDFs** — list of input PDF paths in order
- **Output path** — destination for the merged PDF

## Output

A single PDF containing all pages from the source PDFs in the order listed.

## Common Uses

- Assembling monthly reports from individual report PDFs
- Combining a cover sheet, body, and appendices into a single deliverable
- Bundling generated invoices into a per-customer or per-period archive

## Notes

- Bookmark and metadata behavior depends on the source PDFs. Some sources strip metadata; the merged output reflects the union of what's present.
- Form fields in source PDFs may be flattened in the merged output to avoid name collisions.

## Related

- [Compress PDF](/reference/workflow-steps/document/compress-pdf/) — shrink the merged result
- [Convert image to PDF](/reference/workflow-steps/document/convert-image-to-pdf/) — turn images into PDF pages before merging
