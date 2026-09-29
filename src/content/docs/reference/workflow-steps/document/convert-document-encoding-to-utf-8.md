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
- If the input path is neither a file nor a folder with files in it, the step fails and names the path.

## Examples

Select the input file and browse for the file within that location. Select the desired output location, and browse then select the desired location for the file. Save and run.
