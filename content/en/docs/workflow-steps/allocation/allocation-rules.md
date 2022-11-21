---
title: Allocation By Assignment Dimension
slug: allocation-rules
description: Allocate values based on driver data and assignment dimension
date: 2022-05-10T14:00:00
---


## Description

Allocate values based on an assignment dimesion and driver data table.

![Allocation By Dimension](/images/allocation_by_dimension.png)

## Data Table Settings  
### Assignment Dimesion Hierarchy

![Assignment Hierarchy](/images/assignment-hierarchy.png)

The **Assignment Dimension Hierarchy** gives the user the ability to point, click and filter either or both the ***Values To Allocate Table*** and ***Driver Data Table*** to create targeted allocations. 
The **Assignment Dimension Hierarchy** is created by combining dimensions that reference the ***Values To Allocate Table*** and the ***Driver Data Table***.

#### Creating An Assignment Dimension Hierarchy

To create the **Assignment Dimension Hierarchy** you must first create the dimensions you wish to use to as filters for the ***Values To Allocate Table*** and the ***Driver Data Table***. The links below will guide you through creating these dimensions.

{{< note >}}
In the above **Assignment Dimension Hierarchy** the ***Values To Allocate Table*** has columns for Version, Period, Account and Original Cost Center. The ***Driver Data Table*** has columns for Resource Driver, Period, Version, Original Cost Center and Original Activity. Both of these tables have additional columns, but these are the columns we wish to use to create our allocation rules.
{{< /note >}}

[Creating Dimensions](https://docs.plaidcloud.com/docs/workflow-steps/dimensions/dimension-create/) 

[Loading Dimensions](https://docs.plaidcloud.com/docs/workflow-steps/dimensions/dimension-load/) 

##### Creating The Main Hierarchy

Once the dimensions for the ***Values To Allocate Table*** and the ***Driver Data Table*** have been created the next step is to decide which of the dimensions for the ***Values To Allocate Table*** will serve as the ***Main Hierarchy*** for the **Assignment Dimension Hierarchy**. 
{{< note >}}
When allocating ledger values _Account_ or _Cost Center_ dimensions are normally used. 
{{< /note >}}

Copy this dimension by navigating to the Dimensions tab in PlaidCloud, clicking on the dimension and then selecting ***Actions*** and ***Copy Dimension***.
When you copy the dimension a pop-up will apprear asking you to enter a name for the copied dimension. 

{{< note >}}
The name of the **Assignment Dimension Hierarchy** should convey what allocation is being performed such as "Ledger to Activity". 
{{< /note >}}


##### Adding Dimensions To The Assignment Hierarchy


Open the newley created **Assignment Dimension**, click on the down arrow next to ***Properties*** and select ***New Property***.

![Assignment Hierarchy Property](/images/allocation_by_dimension_add_property.png)

This will open the ***Property Configuration*** dialog box:
###### Property Configuration

![Assignment Hierarchy Configure Property](/images/allocation_by_dimension_configure_property.png)

- **Property Name** - This is normally the name of the dimension that is being added to the Assignment Hierarchy.
- **Property Display** - This should be set to "Tag".
- **Property Type** - This property informs the allocation step which table ***Values To Allocate Table*** or the ***Driver Data Table*** this dimension is related too. 
  - **Source** - Is used in conjunction with the ***Values To Allocate Table***.
  - **Target** - Is used in conjunction with the ***Driver Data Table***.
  - **Driver** - Is used to filter ***Driver Data Table*** for the specific driver selected.
  - **Context** - When the ***Values To Allocate Table*** and the ***Driver Data Table*** contain the same dimension then context can be used to specify how the dimensions should relate to one another. Context is often used when both the ***Values To Allocate Table*** and the ***Driver Data Table*** contain _Profit / Cost Centers_ or _Geography_.
    - **Current** - Acts as a passthrough and will filter the ***Driver Data Table*** based on the settings of the target dimension. An example would be if the ***Cotext*** is based on the _Profit Center_ dimension and the _Profit Center_ target dimension is set to ***ALL*** then the driver data would filter on all _Profit Centers_. 
    - **Parent** - When selected then the parent of the _Profit Center_ in the ***Values To Allocate Table*** will be used to filter the driver values in the ***Driver Data Table***. This is useful when driver values are, at times, not available for a specific _Profit Center_ but often are at the parent level. 
    - **All** - When selected then the _Profit Center_ in the ***Values To Allocate Table*** will not filter the driver values in the ***Driver Data Table***, driver values for all _Profit Centers_ will be used.
    {{< note >}}
When ***Context*** is set to ***ALL*** or ***Parent*** it will override the setting on the target dimension. 
{{< /note >}}
- **Editor Type** - This drop down should be set to ***Select Dimension***.

Once the appropriate properties have been selected for the dimension being added to the Assignment Hierarchy select "Edit Configuration".
###### Dimension Configuration

![Assignment Hierarchy Configure](/images/allocation_by_dimension_configure.png)

- **Dimension** - Use the drop down to select the dimension.
- **Hierarchy** - If the dimension selected has alternate hierarchies, then they will appear and be selectable here as well as the main hierarchy.
- **Start Node** - If you don't wish the dimension to be displayed from the top node you can select any node within the hierarchy as the node from which the dimension will be displayed.
- **Allow Multiple Selections** - If checked the user will be able to select multiple nodes in the hierarchy.
- **Special Cases** - When selected the special cases will be available for selection in the dimension drop down menu. They are typically used in ***Target*** dimensions.
  - **Source** - When a dimension is set to _Source_ the allocation will ignore this dimension when it filters the ***Driver Data Table*** but the allocated results will include values from the dimension.
  - **Current** - Can be used when a dimension is shared between _Source_ and _Target_. When the _Target_ dimension is set to ***Current*** then the ***Driver Data Table*** will be filtered by the current value of the _Source_ dimension as the allocation runs. An example would be if there are multiple periods in the ***Values To Allocate Table*** and the ***Driver Data Table*** but you want the allocation to allocate within the periods and not acrocss them. It is also common to use ***Current*** on _Business Units_, _Cost Centers_ and _Geographies_.
  - **Unassigned** - When a dimension is set to _Unassigned_ the allocation will ignore this dimension when it filters the ***Driver Data Table*** and the allocation result for this dimension will be a _Null_ value.
  - **All** - When a dimension is set to _ALL_ then the allocation will use all the values in the dimension.


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

### Intermediate Tables
The _Intermediate Tables_ are created each time an allocation step runs and provides a summary of the allocation processing. The _Intermediate Tables_ provide insight into how the alloation process is running an are used to trouble shoot unexpected results.

- **Paths** - Shows the number of unique allocation paths summarized from the assignment hierarchy.
- **Mapping** - Shows how each line of the ***Values To Allocate Table*** are mapped to the allocation targets.
- **Summary** - Shows each rule, as a result of the assignment hierachy, and how many of the records from the ***Values To Allocate Table*** match it.
### Allocation Result Table



#### Append Results to Target Table
If this box is checked the allocation results will be appended to the allocation result table. 
If this box is not checked the allocation results table will be overwritten each time the allocation step runs.

#### Separate Columns for Allocated Results

If this box is checked then the results table will show the amount of each allocated record as well as the amount actually allocated to each driver record.

#### Rename Dimension Nodes
If this box is checked when the allocation step runs it will rename the dimension node in the Assignment dimension.  

### Advanced Options

#### Thread Count
Sets the number of concurrent operations the allocation step will use.

#### Chunk Size
Set the number of allocation paths within a thread.

{{< warning >}}
Setting either or both of the ***Thread Count*** or ***Chunk Size*** to high will slow the allocation processing. Slowly incrementing these values up and observing performance is the ideal way of tuning the allocation step.
{{< /warning >}}


## Allocation Source Map

{{< include "common-allocation-source-map" >}}

## Allocation Source Filters

{{< include "common-data-filter" >}}

## Driver Data Map

{{< include "common-allocation-driver-map" >}}

## Driver Data Filters

{{< include "common-data-filter" >}}

## Examples

### Example 1

**Values To Allocate Table**

![Allocation By Dimension](/images/allocation_by_dimension_example_1_source.png)


**Driver Data Table**

![Allocation By Dimension](/images/allocation_by_dimension_example_1_driver.png)


**Assignment Dimension Hierarchy**


![Allocation By Dimension](/images/allocation_by_dimension_example_1_assignment.png)

Since the ***Target RC*** dimension is set to ***Current*** the driver data will be filtered by the ***Source RC*** values in the ***Values To Allocation Table***. 
Since the only value in the ***Source RC*** is **"A"**, only the driver value records where **RC = A** will be used in the allocation step.


**Allocation Results Table**

![Allocation By Dimension](/images/allocation_by_dimension_example_1_result.png)

### Example 2

**Values To Allocate Table**

![Allocation By Dimension](/images/allocation_by_dimension_example_1_source.png)


**Driver Data Table**

![Allocation By Dimension](/images/allocation_by_dimension_example_1_driver.png)


**Assignment Dimension Hierarchy**

![Allocation By Dimension](/images/allocation_by_dimension_example_2_assignment.png)

Since the ***Target RC*** dimension is set to ***ALL*** the driver data will include all **RC** values as you can see in the **RC** column in the ***Allocation Results Table***. 

**Allocation Results Table**

![Allocation By Dimension](/images/allocation_by_dimension_example_2_result.png)

### Example 3

**Values To Allocate Table**

![Allocation By Dimension](/images/allocation_by_dimension_example_3_source.png)


**Driver Data Table**

![Allocation By Dimension](/images/allocation_by_dimension_example_3_driver.png)


**Assignment Dimension Hierarchy**

![Allocation By Dimension](/images/allocation_by_dimension_example_3_assignment.png)

With the ***Context RC*** set to ***ALL*** and the ***Target RC*** set to ***Source*** the driver data will include all the ***RC*** in the driver data. The ***Contect RC*** will override the setting on the ***Target RC***.

**Allocation Results Table**

![Allocation By Dimension](/images/allocation_by_dimension_example_3_result.png)


### Example 4

**Values To Allocate Table**

![Allocation By Dimension](/images/allocation_by_dimension_example_3_source.png)


**Driver Data Table**

![Allocation By Dimension](/images/allocation_by_dimension_example_3_driver.png)


**Assignment Dimension Hierarchy**

![Allocation By Dimension](/images/allocation_by_dimension_example_4_assignment.png)

With the ***Context RC*** set to ***ALL*** the driver data will include all the ***RC*** in the driver data. 

**Allocation Results Table**

![Allocation By Dimension](/images/allocation_by_dimension_example_4_result.png)
