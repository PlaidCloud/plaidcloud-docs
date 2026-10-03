---
title: Merge Multiple PDFs
description: Merge multiple PDF files into a single combined document in a PlaidCloud workflow step for report assembly and consolidation.
sidebar:
  order: 17
---

Joins the PDFs in a folder into a single PDF. Unlike [Concatenate files](/reference/workflow-steps/document/concatenate-files/), this step understands the PDF format and produces a valid merged document.

## Inputs

- **Input Directory** — the folder whose PDFs are merged, in a document account. A single archive, such as a ZIP of PDFs, can be given instead, and the PDFs inside it are merged.
- **Output Merged File** — where the merged PDF is written.

## How It Works

- The PDFs are merged in order of their path, with numbers taken by value — `page2.pdf` comes before `page10.pdf` — so number them to control the order. Each keeps its own pages in order.
- Only files named `.pdf` are merged. Anything else in the folder is left out, and an archive in the folder is not opened.
- Files in subfolders are included where the document account lists them: S3, Wasabi and Google Cloud Storage accounts list the whole folder tree, while OneDrive, SFTP and Azure accounts list the top level only.
- At most 100 PDFs are merged; more fails the step.

## Output

A single PDF at the output path, holding every page of every merged PDF.

## Notes

- A folder with no PDFs in it, or one that does not exist, finishes the step with a warning that names the folder and merges nothing, and the workflow continues.
- The output path cannot be the input path.

## Common Uses

- Assembling monthly reports from individual report PDFs
- Combining a cover sheet, body, and appendices into a single deliverable
- Bundling generated invoices into a per-customer or per-period archive

## Related

- [Compress PDF](/reference/workflow-steps/document/compress-pdf/) — shrink the merged result
- [Convert image to PDF](/reference/workflow-steps/document/convert-image-to-pdf/) — turn images into PDFs before merging
