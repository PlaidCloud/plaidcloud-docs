---
title: Fix File Extension
description: Correct file extensions in a PlaidCloud workflow step by detecting the actual file type and renaming with the proper extension.
sidebar:
  order: 16
---

Reads what a file actually contains and, where that contradicts its extension, renames it with the extension its type normally carries — a PDF saved as `.dat` becomes `.pdf`. Useful when a source system hands off files with wrong or missing extensions.

## Inputs

- **Input File or Directory** — a file, or a folder whose files are each checked, in a document account. Files are renamed where they are, so there is no output location.

## How It Works

The step identifies each file's type from its contents, and renames the file only when its current name is missing an extension, has a placeholder one (`.dat`, `.tmp` or `.bin`), or names a different type the step recognises.

The types it recognises are PDF; JPEG, PNG, GIF, TIFF, BMP, WebP and HEIC images; Excel (`.xlsx`, `.xls`), Word (`.docx`, `.doc`) and PowerPoint (`.pptx`) documents; ZIP and GZip archives; and CSV, JSON, HTML, XML and plain text.

A file keeps its name when:

- its extension already fits its contents — `.jpg` and `.jpeg` both fit a JPEG, `.tif` and `.tiff` a TIFF;
- its extension is one the step doesn't recognise, such as `.sql`, `.log` or `.ai`, because contents alone cannot tell a SQL script from any other text, or an Illustrator file from a PDF;
- it holds plain text under a text extension such as `.csv`, `.tsv` or `.json`;
- it holds one text format under another's extension — XML in a `.html` file, CSV in a `.json` file — because contents can't reliably tell those apart. Only a `.txt` file, or one with no or a placeholder extension, is renamed to a text format;
- it is a ZIP file named as an Office document, since `.xlsx`, `.docx` and `.pptx` files are ZIP files inside;
- its type cannot be determined, as for an empty file.

An archive is judged by its own contents: its members are not opened or renamed. Files whose names start with `.` are skipped.

## Examples

| File | Contents | Result |
|---|---|---|
| `invoice.dat` | PDF | renamed `invoice.pdf` |
| `photo.png` | JPEG | renamed `photo.jpg` |
| `export.txt` | CSV | renamed `export.csv` |
| `readme` | plain text | renamed `readme.txt` |
| `query.sql` | plain text | unchanged |
| `budget.xlsx` | ZIP | unchanged |

## Notes

- If the input path is neither a file nor a folder with files in it, the step fails and names the path.

## Related

- [Concatenate files](/reference/workflow-steps/document/concatenate-files/)
- [Documents guide](/guides/documents/)
