---
title: Convert PDF or Image to JPEG
description: Convert PDF pages or images to JPEG format in a PlaidCloud workflow step for web-compatible output and image processing tasks.
sidebar:
  order: 8
---

Rasters a PDF or converts an image to JPEG. Each PDF page becomes one JPEG; non-PDF inputs are simply re-encoded.

## Inputs

- **Source document** — PDF or image path in a document account
- **Output path or prefix** — destination JPEG path; for multi-page PDFs, a numeric page suffix is appended
- **Resolution (DPI)** — pixels per inch when rasterizing PDF pages (higher = larger file, sharper output)
- **JPEG quality** — compression level (typical 70–90)

## Output

One JPEG per source page, written to the output path with a page index in the filename for multi-page sources.

## Common Uses

- Generating preview thumbnails for web display
- Producing image-only versions of PDFs for systems that can't handle PDF
- Pulling specific pages out of a PDF as standalone images

## Related

- [Convert image to PDF](/reference/workflow-steps/document/convert-image-to-pdf/)
- [Compress PDF](/reference/workflow-steps/document/compress-pdf/)
- [Crop image to headshot](/reference/workflow-steps/document/crop-image-to-headshot/)
