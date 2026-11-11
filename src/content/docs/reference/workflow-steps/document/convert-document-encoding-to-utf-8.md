---
title: Convert Document Encoding to UTF-8
description: Convert document file encoding to UTF-8 in a PlaidCloud workflow step for broad compatibility with modern systems and applications.
sidebar:
  order: 5
---

## Description

Rewrites a text file in UTF-8. This is particularly useful if the information source has mixed encodings or other tools don’t support certain encodings.

## How It Works

- The source's encoding is detected. A UTF-8 file is read as UTF-8, and Windows characters pasted into one — curly quotes from Word or Excel, say — come through intact, however many. A file in another encoding is read in the encoding detected from its first part that isn't valid UTF-8.
- The text is written unchanged — accented letters, symbols and other characters come through exactly as they were.
- A file whose encoding cannot be detected fails the step, naming the file.
- If the input path does not exist or has no files in it, the step finishes with a warning that names the path and processes nothing, and the workflow continues.
- For a folder, each file is converted and written into the destination under its own name. Tick **Keep Subfolders** to write a file from a subfolder into the matching subfolder of the destination instead; the contents of a compressed file then go into the subfolder the compressed file was in.
- If two files would be written to the same place in the destination, the step fails before writing the second, rather than letting it replace the first. The message names both files, or the compressed file they both came from, and the place; if ticking **Keep Subfolders** would write them to separate places, it says so.

## Examples

Select the input file and browse for the file within that location. Select the desired output location, and browse then select the desired location for the file. Save and run.
