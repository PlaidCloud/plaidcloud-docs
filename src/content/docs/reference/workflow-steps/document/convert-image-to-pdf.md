---
title: Convert Image to PDF
description: Convert image files to PDF documents in a PlaidCloud workflow step for standardized document output and archive-ready formats.
sidebar:
  order: 7
---

Wraps one or more image files (JPEG, PNG, TIFF) into a PDF. Each image becomes one page.

## Inputs

- **Source images** — one or more image paths in a document account
- **Output path** — destination for the generated PDF
- **Page order** — order in which input images are placed in the PDF

## Output

A PDF containing one page per input image, in the order specified.

## Common Uses

- Bundling scanned pages from a multi-page document originally captured as separate images
- Standardizing receipt or invoice attachments into a single archival format
- Preparing image evidence for systems that only accept PDF input

## Related

- [Convert PDF or image to JPEG](/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Compress PDF](/reference/workflow-steps/document/compress-pdf/)
- [Merge multiple PDFs](/reference/workflow-steps/document/merge-multiple-pdfs/)
