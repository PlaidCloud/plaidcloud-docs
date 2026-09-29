---
title: Convert Document Encoding to UTF-16
description: Convert document file encoding to UTF-16 in a PlaidCloud workflow step to support multi-byte character sets and Unicode text.
sidebar:
  order: 6
---

## Description

Rewrites a text file in UTF-16. Useful when a downstream system requires UTF-16, or when a source mixes encodings that other tools reject.

## Inputs

- **Input File or Directory** — the text file, or a folder of text files, to convert.
- **Destination** — where the converted file is written.
- **Compression** — No Compression, Zip, GZip or BZip2 for the output.
- **Endianness (Byte Order)** — Little Endian or Big Endian.
- **Include BOM** — tick to start the file with a byte-order mark (`FF FE` for little-endian, `FE FF` for big-endian). Leave it clear for no mark.

## How It Works

- The source's encoding is detected. A UTF-8 file is read as UTF-8, and Windows characters pasted into one — curly quotes from Word or Excel, say — come through intact, however many. A file in another encoding is read in the encoding detected from its first part that isn't valid UTF-8.
- The text is written unchanged — accented letters, symbols and other characters come through exactly as they were.
- A file whose encoding cannot be detected fails the step, naming the file.
- If the input path is neither a file nor a folder with files in it, the step fails and names the path.
- For a folder, each file is converted and written into the destination under its own name. Files from subfolders are written into the destination itself, not into matching subfolders.

## Examples

Select the input file and browse for the file within that location. Select the desired output location, choose the byte order, and tick **Include BOM** if the receiving system expects one. Save and run.
