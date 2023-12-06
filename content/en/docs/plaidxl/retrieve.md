---
title: Working with Data
slug: retrieve
description: Retrieve and save data using the PlaidCloud Excel Add-in after connecting to a PlaidCloud project
date: 2022-01-25T07:39:47
weight: 3.0
tags:
- plaidcloud
- expression
categories:
- PlaidCloud
- Expressions
---

## Retrieve Data

To retrieve data from PlaidCloud, select your desired project from the dropdown menu. Once a project is selected, a list of tables in that project will appear. 
Click on a table to select it, and click the `Retrieve Table` button to import the selected table into Excel. 
The table will be placed in a new worksheet, named after the table. For your convenience, the following will also happen when a table is retrieved:


* Column headers will be frozen
* Auto-filters will be enabled
* An offset-based named range will be generated to encompass the data


	+ This range’s name will be the same as the table’s name, prefixed with an underscore and with all spaces replaced by underscores
	+ For example, the range for a table named “Sample data” would be “\_Sample\_data”

## Save Data

If you make changes data in the spreadsheet and want to push these changes to the PlaidCloud table, simply press the `Save Table (OVERWRITE!)` button.

{{< warning >}}
Be careful – as the warning suggests, this will overwrite the data in PlaidCloud with the data in your spreadsheet.
{{< /warning >}}


Since you can open multiple PlaidCloud tables in PlaidXL, bulk operations are in place for your convenience. 
The pull/push all active tables buttons will retrieve the latest versions of all tables active in excel, or upload all active tables back to PlaidCloud, 
respectively.

In addition, pulling all tables will also refresh any pivot tables that use data from a refreshed table.  
  


