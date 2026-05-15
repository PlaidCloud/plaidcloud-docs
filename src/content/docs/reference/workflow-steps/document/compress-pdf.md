---
title: Compress PDF
description: Compress PDF files in a PlaidCloud workflow step to reduce file size while maintaining document quality for storage efficiency.
sidebar:
  order: 1
---

Reduces the file size of a PDF stored in a document account. Useful for trimming large scanned documents before archiving, attaching to notifications, or moving across document accounts.

## Inputs

- **Source document** — path to the input PDF inside a document account
- **Output path** — destination for the compressed result (can overwrite the source or write to a different location)
- **Compression level** — trade-off between size reduction and image fidelity

## Output

A compressed PDF at the configured output path. The step does not alter the source unless source and output paths match.

## Common Uses

- Shrinking scanned invoices, receipts, or contracts before long-term storage
- Reducing PDF size before emailing or attaching to notifications
- Preparing documents for upload to size-constrained downstream systems

## Related

- [Convert PDF or image to JPEG](/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge multiple PDFs](/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Documents guide](/guides/documents/)
