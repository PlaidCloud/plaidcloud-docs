---
title: Compress PDF
description: Compress PDF files in a PlaidCloud workflow step to reduce file size while maintaining document quality for storage efficiency.
sidebar:
  order: 1
---

Reduces the file size of a PDF stored in a document account. Useful for trimming large scanned documents before archiving, attaching to notifications, or moving across document accounts.

## Inputs

- **Input File or Directory** — a PDF, or a folder of PDFs, in a document account.
- **Output File or Directory** — where the compressed PDF is written.

## How It Works

The PDF is rewritten with its images reduced to screen resolution (72 dpi) and its fonts embedded as subsets, which can shrink scanned documents dramatically; text stays sharp. Pages are fitted to US Letter size.

## Output

A compressed PDF at the output path. For a folder, each PDF is written below the output path, keeping its place relative to the input folder.

## Notes

- The output path cannot be the input path, so the source is never overwritten.
- If the input path does not exist or has no files in it, the step finishes with a warning that names the path and processes nothing, and the workflow continues.
- A PDF that cannot be compressed fails the step, naming the file and the reason.

## Common Uses

- Shrinking scanned invoices, receipts, or contracts before long-term storage
- Reducing PDF size before emailing or attaching to notifications
- Preparing documents for upload to size-constrained downstream systems

## Related

- [Convert PDF or image to JPEG](/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge multiple PDFs](/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Documents guide](/guides/documents/)
