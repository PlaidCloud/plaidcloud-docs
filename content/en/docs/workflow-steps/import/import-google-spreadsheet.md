---
title: Import Google Spreadsheet
slug: import-google-spreadsheet
weight: 7.0
description: Import specific worksheets from Google Spreadsheet files
date: 2022-01-25T07:39:58
---


## Description

Import specific worksheets from Google Spreadsheet files.


## Examples

No examples yet...

---

## Import Parameters


![Import Google Spreadsheet](/images/import_file_google_target.png)
### Source And Target
#### Google Account

Accessing Google Spreadsheet data requires a valid Google user account. This requires set up in Tools. For details on setting up a Google account connection, see here: [PlaidCloud Tools – Connection](/docs/tools/data-connections).

Once all necessary accounts have been set up, select the appropriate **Google Account** from the drop down list.
#### Spreadsheet

Next, specify the **Spreadsheet** to import from the dropdown menu containing all available files associated with the specified **Google Account**.

{{< note >}}
Make sure the provided user account has access to the specified file, especially if the file is owned by another user.
{{< /note >}}



{{< include "common-import-target-selection" >}}
### Header Type

Since Google Spreadsheets may or may not contain headers, PlaidCloud provides a way to either use the headers, ignore headers, or use column order to determine the column alignment.
* **No Header**: The file contains no header.  Use the source list in the *Data Mapper* to determine the column alignment
* **Has Header - Use Header and Override Field List**: The file has a header.  Use the header names specified and ignore the source list in the *Data Mapper*.
* **Has Header - Skip Header and Use Field List Instead**: The file has a header but it should be ignored.  Use the header names specified by the source list in the *Data Mapper*.

### Worksheets to Import

Because workbooks may contain many worksheets with different data, it is possible to select which worksheets should be imported in the current import process.  The options are:

* All Worksheets
* Worksheets Matching Search
* Selected Worksheets

#### Using Worksheet Search

The search functionality for worksheets allows inclusion of worksheets matching the search criteria.  The search criteria allows for:
* **Starts With**: The worksheet name starts with the search text
* **Contains**: The worksheet name contains the search text
* **Ends With**: The worksheet name ends with the search text

#### Find Sheets in Selected File

The find sheets button will open the Excel file and list the worksheets available in the table.  Mark the checkboxes in the table for the worksheets to be included in the import.

{{< note >}}
When populating the *Data Mapper*, the first worksheet found in the list will be used.  Ensure all worksheets have a similar format that are included in the import step.
{{< /note >}}
### Column Headers

{{< note >}}
Due to technical limitations, all columns from Google Spreadsheets are imported as String data type. Boolean, Numerical and/or Date/Time data types must be explicitly specified in the mapper.
{{< /note >}}

## Table Data Selection

{{< include "common-data-mapper" >}}

## Data Filters

{{< include "common-data-filter" >}}


---
