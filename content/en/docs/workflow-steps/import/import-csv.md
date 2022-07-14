---
title: Import CSV
slug: import-csv
description: Import delimited text files from PlaidCloud Document
date: 2022-01-25T07:39:55
---

## Description

Import delimited text files from PlaidCloud Document. This includes, but is not limited to, the following delimiter types:
* comma (, )
* pipe (|)
* semicolon (; )
* tab
* space ( )
* at symbol (@)
* tilda (~)
* colon (:)

## Examples

{{< include "no-examples" >}}

---

## Unique Configuration Items

### Inspect Selected Source File

By pressing the *Guess Settings from Source File* button, PlaidCloud will open the file and inspect it to attempt to determine the data format.  Always check
the guessed settings to make sure they seem correct.

{{< note >}}
If a directory of files is selected for import or search is used, the first file found will be used for guessing
{{< /note >}}

### Data Format

#### Delimiter
As mentioned above, **Inspect Source File** will attempt to determine the delimiter in the source file. If another delimiter is desired, use this 
section to specify the delimiter. Users can choose from a list of standard delimiters.
* comma (, )
* pipe (|)
* semicolon (; )
* tab
* space ( )
* at symbol (@)
* tilda (~)
* colon (:)

#### Header Type

Since CSVs may or may not contain headers, PlaidCloud provides a way to either use the headers, ignore headers, or use column order to determine the column alignment.
* **No Header**: The CSV file contains no header.  Use the source list in the *Data Mapper* to determine the column alignment
* **Has Header - Use Header and Override Field List**: The CSV file has a header.  Use the header names specified and ignore the source list in the *Data Mapper*.
* **Has Header - Skip Header and Use Field List Instead**: The CSV file has a header but it should be ignored.  Use the header names specified by the source list in the *Data Mapper*.

#### Date Format

This setting is useful if the dates contained in the CSV file are not readily recognizable as dates and times.  The import process attempts to convert dates but having a little extra information
can help in the import process.

### Special Characters

The special character inputs control how PlaidCloud handles the presence of certain characters and what they mean in the context of processing the CSV
 * **Quote Character**: This is the character used to indicate an enclosed set of text that should be processed as a single field
 * **Escape Character**: This is the character used to indicate the following character should be processed as it is and not interpreted as a special character.  Useful when field may contain the delimiter.
 * **Null Character**: Since CSVs don't have data types, this character provides a way to indicate that the value should be NULL rather than an empty string or 0.
 * **Trailing Negatives**: Some source systems generate negative numbers with trailing negative symbols instead of prefixing the negative.  This setting will process those as negative numbers.

### Row Selection

For input files with extraneous records, you can specify a number of rows to skip before processing the data.  This is useful if files contain header blocks that must be skipped before arriving at the tabular data.



---

## Common Configuration Items

{{< include "common-remove-non-ascii" >}}

{{< include "common-delete-files-after-import" >}}

{{< include "common-import-file-selection" >}}

{{< include "common-import-target-selection" >}}

{{< include "common-data-mapper" >}}

{{< include "common-data-filter" >}}
