---
title: Convert Document Encoding to ASCII
description: Convert document file encoding to ASCII in a PlaidCloud workflow step to ensure compatibility with systems requiring ASCII text.
sidebar:
  order: 4
---

## Description

Rewrites a text file as plain ASCII. This is particularly useful if the source of information has mixed encodings or other tools don’t support certain encodings.

## How It Works

- The source's encoding is detected. A UTF-8 file is read as UTF-8, and Windows characters pasted into one — curly quotes from Word or Excel, say — come through intact, however many. A file in another encoding is read in the encoding detected from its first part that isn't valid UTF-8.
- Accented letters keep their base letter (`café` becomes `cafe`), and characters with no ASCII form are dropped.
- A line holding only a double quote is joined to the end of the line before it.
- A file whose encoding cannot be detected fails the step, naming the file.
- If the input path is neither a file nor a folder with files in it, the step fails and names the path.

## Examples

Select the input file and browse for the file within that location. Select the desired output location, and browse to select the desired location for the file. Save and run.
