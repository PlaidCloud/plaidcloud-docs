---
title: Crop Image to Headshot
description: Crop images to a square headshot in a PlaidCloud workflow step for standardized portraits in directories and badges.
sidebar:
  order: 12
---

Crops an image to a centred square and scales it to a 500 × 500 pixel JPEG. Useful for normalizing employee or member directories where source photos vary in aspect ratio.

## Inputs

- **Input File or Directory** — an image, or a folder of images, in a document account.
- **Output File or Directory** — where the headshot is written.

## Output

A 500 × 500 JPEG cropped from the centre of the source. For a folder, each file's headshot is written into a folder named after the output path, without its extension.

## Notes

- The crop is taken from the centre of the image; it does not look for a face, so frame source photos with the subject centred.
- A file that cannot be read as an image is copied to the output unchanged rather than failing the step.
- If the input path is neither a file nor a folder with files in it, the step fails and names the path.
- The output path cannot be the input path.

## Common Uses

- Standardizing employee directory photos
- Generating consistent avatar imagery for an internal portal
- Trimming photos for ID badges and credentials

## Related

- [Convert PDF or image to JPEG](/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Fix file extension](/reference/workflow-steps/document/fix-file-extension/)
