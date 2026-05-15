---
title: Concatenate Files
description: Concatenate multiple files into a single file in a PlaidCloud workflow step for combining text, CSV, or other document outputs.
sidebar:
  order: 2
---

Combines two or more files in a document account into a single output file. Operates byte-by-byte — useful for plain-text formats (CSV, log files, JSON Lines) where simple concatenation produces valid output.

## Inputs

- **Source files** — list of files to concatenate, in order
- **Output path** — destination for the combined file
- **Separator** — optional byte sequence inserted between source files (commonly a newline)

## Output

A single file containing the contents of all source files in the order listed, joined by the configured separator.

## Common Uses

- Combining daily log files into a monthly archive
- Merging CSV files that share a schema (drop headers from all but the first)
- Joining JSON Lines exports from multiple sources before processing

## Not For

- PDFs — use [Merge multiple PDFs](/reference/workflow-steps/document/merge-multiple-pdfs/) instead
- Binary formats with headers (XLSX, ZIP, image files) — concatenating bytes won't produce a valid file

## Related

- [Merge multiple PDFs](/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Documents guide](/guides/documents/)
