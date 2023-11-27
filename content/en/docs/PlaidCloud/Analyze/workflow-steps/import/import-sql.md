---
title: Import SQL
slug: import-sql
weight: 15.0
description: Import data from a remote SQL database.
date: 2022-01-25T07:39:57
---

## Description

Import data from a remote SQL database.

---

## Import Parameters

![Import SQL Table](/images/import_remote_sql_table.png)

---

### Source And Target
#### Database Connection

To establish a **Database Connection** please refer to 
[PlaidCloud Data Connections](https://docs.plaidcloud.com/docs/tools/data-connections/)


{{< include "common-import-target-selection.md" >}}

### SQL Query
In this section write the SQL query to return the required data. 

### Column Type Guessing
SQL Imports have the option of attempting to guess the data type during load, or to set all columns to type Text. Setting the data types dynamically can be quicker if the data is clean, but can cause issues in some circumstances.

For example, if most of the data appears to be numeric but there is some text as well, it may try to set it as numeric causing load issues with mismatched data types. Or there could be issues if there is a numeric product code that is 16 digits, for example. It would crop the leading zeroes resulting in a number instead of a 16 digit code.

Setting the data to all text, however, requires a subsequent Extract step to convert any data types that shouldn't be text to the appropriate type, like dates or numerical values.

---


