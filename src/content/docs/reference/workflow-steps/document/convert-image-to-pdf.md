---
title: Convert Image to PDF
description: Convert image files to PDF documents in a PlaidCloud workflow step for standardized document output and archive-ready formats.
sidebar:
  order: 7
---

Turns an image (PNG, GIF, TIFF, JPEG or HEIC) into a one-page PDF, or re-fits an existing PDF to a standard page size.

## Inputs

- **Input File or Directory** — an image or PDF, or a folder of them, in a document account.
- **Destination** — where the PDF is written.
- **Page Size** — US Letter, US Legal, A3, A4 or A5.
- **Compression** — **Lossy** reduces images to screen resolution and can shrink the file dramatically; **Lossless**, the default, keeps the image data exactly.

## How It Works

- An image is placed on a page of the chosen size, scaled to fit inside it without changing its proportions. An image with several pages or frames, such as a scanned TIFF, converts from its first.
- With **Lossy**, the result is then compressed, and a PDF input is fitted to the chosen page size as it is compressed.
- With **Lossless**, a PDF input is passed through unchanged, keeping its own page size.

## Output

One PDF per input file. For a folder, each file's PDF is written into a folder named after the destination, without its extension, under the source file's own name. To combine several into one document, follow this step with [Merge multiple PDFs](/reference/workflow-steps/document/merge-multiple-pdfs/).

## Notes

- If the input path does not exist or has no files in it, the step finishes with a warning that names the path and processes nothing, and the workflow continues.
- The destination cannot be the input path.

## Common Uses

- Standardizing receipt or invoice images into an archival format
- Preparing image evidence for systems that only accept PDF input

## Related

- [Convert PDF or image to JPEG](/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Compress PDF](/reference/workflow-steps/document/compress-pdf/)
- [Merge multiple PDFs](/reference/workflow-steps/document/merge-multiple-pdfs/)
