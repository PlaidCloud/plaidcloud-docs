---
title: Convert Document Encoding to UTF-16
description: Convert document file encoding to UTF-16 in a PlaidCloud workflow step to support multi-byte character sets and Unicode text.
sidebar:
  order: 6
---

## Description

Rewrites a text file in UTF-16. Useful when a downstream system requires UTF-16, or when a source mixes encodings that other tools reject.

## Inputs

- **Input File or Directory** — the text file or compressed file, or a folder of them, to convert.
- **Destination** — where the converted file is written.
- **Compression** — No Compression, Zip, GZip or BZip2 for the output.
- **Keep Subfolders** — for a folder, tick to write each file from a subfolder into the matching subfolder of the destination.
- **Endianness (Byte Order)** — Little Endian or Big Endian.
- **Include BOM** — tick to start the file with a byte-order mark (`FF FE` for little-endian, `FE FF` for big-endian). Leave it clear for no mark.

## How It Works

- The source's encoding is detected. A UTF-8 file is read as UTF-8, and Windows characters pasted into one — curly quotes from Word or Excel, say — come through intact, however many. A file in another encoding is read in the encoding detected from its first part that isn't valid UTF-8.
- The text is written unchanged — accented letters, symbols and other characters come through exactly as they were.
- A file whose encoding cannot be detected fails the step, naming the file.
- If the input path does not exist or has no files in it, the step finishes with a warning that names the path and processes nothing, and the workflow continues.
- A compressed file — a zip, gzip or bzip2 file, say — is expanded first, and each file in it is converted.
- For a folder, each file is converted and written into the destination under its own name. Tick **Keep Subfolders** to write a file from a subfolder into the matching subfolder of the destination instead; the contents of a compressed file then go into the subfolder the compressed file was in.
- If two files would be written to the same place in the destination, the step fails before writing the second, rather than letting it replace the first. The message names both files, or the compressed file they both came from, and the place; if ticking **Keep Subfolders** would write them to separate places, it says so.

## Examples

Select the input file and browse for the file within that location. Select the desired output location, choose the byte order, and tick **Include BOM** if the receiving system expects one. Save and run.
