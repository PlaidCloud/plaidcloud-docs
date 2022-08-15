---
title: Allocation Split
slug: allocation-split
description: Allocate values based on driver data
date: 2022-05-10T14:00:00
---


## Description


Allocate values based on driver data.

![Allocation Split](/images/allocation_split.png)
## Data Table Settings  

The **Values To Allocate Table**, **Driver Data Table** and **Allocation Result Table** can be selected dynamically or statically.

#### Dynamic Table Selection
The dynamic table option allows specification of a table using text and variables.  This is useful when employing
variable driven workflows where the table or view references are relative to the variables specified.

An example that uses the `current_month` variable to dynamically point to a table:

```
legal_entity/inputs/{current_month}/ledger_values
```

#### Static Table Selection
When a specific table is desired as the source, leave the *Dynamic* box unchecked and select the source table using the dropdown menu.


Table Explorer is always avaible with any table selection.  Click on the Table Explorer button to the right of the table selection and a Table Explorer window will open.

{{< note >}}
The **Allocation Result Table** must be a table and not a view.
{{< /note >}}

### Values To Allocate Table

This is the table that contains the values that are to be allocated. These are typically cost or revenue values.  


### Driver Data Table

The driver data table contains the values that the allocation step will use to allocate costs. 


Examples:

- For a supply chain to assign costs to customers you might use delivery data with the number of deliveries or the weight of the deliveries as the driver.
- For an IT help desk to assign its costs to the departments it supports the driver data be the number of tickets by cost center. 

#### Driver Data Sign Rule
Driver data can contain both positive and negative values. The **Driver Data Sign Rule** lets you decide how conflicting signs will be handled.
- **Error on conficting signs** - Allocation step will produce an error and stop if conflicting signs are encountered.
- **Proceed with warning on conflicting signs** - Allocation step will use both negative and positive driver values but will display a warning.
- **Use only positive driver values** - Allocation step will only use positive driver values, will ignore negative values.
- **Use only negative driver values** - Allocation step will only use negative driver values, will ignore positive values.
- **Use absolute values of driver data** - Allocation step will use the absolute values of the driver data.


### Allocation Result Table



#### Append Results to Target Table
If this box is checked the allocation results will be appended to the allocation result table. 
If this box is not checked the allocation results table will be overwritten each time the allocation step runs.

#### Separate Columns for Allocated Results

If this box is checked then the results table will show the amount of each allocated record as well as the amount actually allocated to each driver record.

## Allocation Source Map

{{< include "common-allocation-source-map" >}}

## Allocation Source Filters

{{< include "common-data-filter" >}}

## Driver Data Map

{{< include "common-allocation-driver-map" >}}

## Driver Data Filters

{{< include "common-data-filter" >}}

