---
title: Convert PDF or Image to JPEG
description: Convert PDF pages or images to JPEG format in a PlaidCloud workflow step for web-compatible output and image processing tasks.
sidebar:
  order: 8
---

Converts a PDF or an image to a JPEG. A PDF's first page becomes the JPEG; an image is re-encoded, and one with several pages or frames, such as a scanned TIFF, converts from its first.

## Inputs

- **Input File or Directory** — a PDF or image (PNG, GIF, TIFF, JPEG or HEIC), or a folder of them, in a document account.
- **Output File or Directory** — where the JPEG is written.

## Output

One JPEG per input file. For a folder, each file's JPEG is written into a folder named after the output path, without its extension, under the source file's own name.

## Notes

- A file of any other type fails the step, naming the types it accepts.
- If the input path is neither a file nor a folder with files in it, the step fails and names the path.
- The output path cannot be the input path.

## Common Uses

- Generating preview images for web display
- Producing image-only versions of PDFs for systems that can't handle PDF

## Related

- [Convert image to PDF](/reference/workflow-steps/document/convert-image-to-pdf/)
- [Compress PDF](/reference/workflow-steps/document/compress-pdf/)
- [Crop image to headshot](/reference/workflow-steps/document/crop-image-to-headshot/)
