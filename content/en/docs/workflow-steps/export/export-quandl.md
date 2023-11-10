---
title: Export to Quandl
slug: export-quandl
weight: 8.0
description: Export an Analyze data table to Quandl’s database
date: 2022-01-25T07:39:58
---


## Description


Export an Analyze data table to Quandl’s database.



## Source and Target


Specify the following parameters:


* **Source Table**: Analyze data table to export
* **Quandl Connection**: Accessing Quandl data sets requires a user account or a guest account with limited access. This requires set up in Tools. For details on setting up a Quandl account connection, see here: [PlaidCloud Tools – Connection](/docs/tools/data-connections)
* **Quandl Code**: Use the **Search** button to search for data sets. Alternatively, data sets can be entered manually. This requires the user to enter the portion of the URL after “[http://www.quandl.com](http://www.quandl.com/)”. For example, to import the data set for Microsoft stock, which can be found here (<http://www.quandl.com/GOOG/NASDAQ_MSFT>), enter *GOOG/NASDAQ_MSFT* in the Quandl Code field
* **Dataset Name**: Name of the dataset to be exported to Quandl
* **Dataset Description**: Description of dataset to be exported to Quandl


## Table Data Selection

{{< include "common-data-mapper" >}}




For more aggregation details, see the Analyze overview page [here](/docs/workflow-steps/common/aggregation).


## Data Filters

{{< include "common-data-filter" >}}

## Examples

No examples yet...

