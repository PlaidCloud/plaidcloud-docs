---
title: Fix File Extension
description: Correct file extensions in a PlaidCloud workflow step by detecting the actual file type and renaming with the proper extension.
sidebar:
  order: 16
---

Inspects the byte signature of a file and renames it with the correct extension. Useful when source systems hand off files with wrong or missing extensions (e.g., `.dat` for what's really a PDF, `.tmp` for a JPEG).

## Inputs

- **Source path** — file to inspect, in a document account
- **Rename in place** — if true, the source file is renamed; if false, the corrected name is written to a target path

## How It Works

The step reads the first few bytes of the file (the magic number) and matches against known signatures: PDF, JPEG, PNG, ZIP/Office formats, CSV (best-effort by sniffing), and others. If a match is found, the file gets the canonical extension for that format.

## Output

A file with the corrected extension. If detection fails (unknown format or empty file), the step either keeps the original name or errors based on configuration.

## Common Uses

- Cleaning up uploads from systems that strip or mangle extensions
- Normalizing files arriving over FTP/SFTP where extensions aren't enforced
- Pre-processing before format-specific steps that match on extension

## Related

- [Concatenate files](/reference/workflow-steps/document/concatenate-files/)
- [Documents guide](/guides/documents/)
