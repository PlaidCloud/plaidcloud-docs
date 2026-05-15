---
title: Crop Image to Headshot
description: Automatically crop images to headshot dimensions in a PlaidCloud workflow step using face detection for standardized portraits.
sidebar:
  order: 12
---

Detects the face in a source image and crops the output to a standardized headshot frame around it. Useful for normalizing employee or member directories where source photos vary in aspect ratio and framing.

## Inputs

- **Source image** — JPEG or PNG path in a document account
- **Output path** — destination for the cropped result
- **Target aspect ratio** — e.g., 1:1 (square), 4:5 (portrait)
- **Headroom** — how much space to leave above the head (proportion of frame)

## Output

A cropped image at the target dimensions centered on the detected face. If no face is detected, the step either falls back to center-crop or errors depending on configuration.

## Common uses

- Standardizing employee directory photos
- Generating consistent avatar imagery for an internal portal
- Trimming photos for ID badges and credentials

## Caveats

- Face detection works best on well-lit, front-facing portraits. Heavily-cropped, side-angle, or low-resolution sources may not detect cleanly.
- The step doesn't enhance image quality — output resolution can be at most the input resolution.

## Related

- [Convert PDF or image to JPEG](/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Fix file extension](/reference/workflow-steps/document/fix-file-extension/)
