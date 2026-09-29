---
title: Document Text Substitution
description: Perform text find-and-replace substitutions in documents within a PlaidCloud workflow step for automated content transformation.
sidebar:
  order: 15
---

## Description

Find-and-replace inside a text file. Replace specific strings or placeholders with new values — useful for templating (replacing a placeholder such as `CUSTOMER_NAME` with an actual name) or for sanitizing text (removing or redacting specific strings).

Works on UTF-8 text files (TXT, CSV, JSON, XML, HTML, RML) of any size. A file that isn't UTF-8 text, such as a PDF or an Office document, fails the step.

## Inputs

- **Input File or Directory** — the file, or a folder of files, to change.
- **Destination File or Directory** — where the result is written. The result is always written to the input's document account; the destination sets the path.
- **Compression** — No Compression, Zip, GZip or BZip2 for the output.
- **Text Replacement Operation Order** — one row per replacement, each giving the original text and its replacement. Variables can be used in the replacement.

## How It Works

- Replacements run top to bottom, and each one works on the result of those above it — so a replacement can change text that an earlier row put there.
- Matching is exact and case-sensitive, and every occurrence is replaced.
- A row whose original text is empty is ignored.
- For a folder, each file is written into a folder named after the destination, without its extension, under the file's own name.
- If the input path is neither a file nor a folder with files in it, the step fails and names the path.

## Examples

| Original | Replacement | `Dear CUSTOMER_NAME,` becomes |
|---|---|---|
| `CUSTOMER_NAME` | `Acme Ltd` | `Dear Acme Ltd,` |
