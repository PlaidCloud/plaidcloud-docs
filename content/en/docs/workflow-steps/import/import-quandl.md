---
title: Import Quandl
slug: import-quandl
weight: 12.0
description: Imports data sets from Quandl’s repository of millions of data sets
date: 2022-01-25T07:39:57
---

## Description

Imports data sets from Quandl’s repository of millions of data sets.

For more details on Quandl data sets, see the Quandl official website here: <http://www.quandl.com/>.


## Examples

No examples yet...

---

## Unique Configuration Items

### Source Data Specification

Accessing Quandl data sets requires a user account or a guest account with limited access. This requires set up in Tools. For details on setting up a Quandl account connection, see here: [PlaidCloud Tools – Connection](/docs/tools/data-connections).

Once all necessary accounts have been set up, select the appropriate account from the drop down list.

Next, enter criteria for the desired Quandl code. Users can use the **Search** functionality to search for data sets. Alternatively, data sets can be entered manually. This requires the user to enter the portion of the URL after “[http://www.quandl.com](http://www.quandl.com/)”. 

For example, to import the data set for Microsoft stock, which can be found here (<http://www.quandl.com/GOOG/NASDAQ_MSFT>), enter *GOOG/NASDAQ_MSFT* in the Quandl Code field.


### Data Selection


It is possible to slice Quandl data sets upon import. Available options include the following:


* Start Date: Use the date picker to select the desired date.
* End Date: Use the date picker to select the desired date.
* Collapse: Aggregate results on a daily, weekly, monthly, quarterly, or annual basis. There is no aggregation by default.
* Transformation: Summary calculations.
* Limit Rows: The default value of 0 returns all rows. Any other positive integer value will specify the limit of rows to return from the data set.

---

## Common Configuration Items

{{< include "common-remove-non-ascii" >}}

{{< include "common-delete-files-after-import" >}}

{{< include "common-import-target-selection" >}}

{{< include "common-data-mapper" >}}

{{< include "common-data-filter" >}}
