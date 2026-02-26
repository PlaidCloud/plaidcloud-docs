---
title: Rule-Based Tagging
slug: rule-based-tagging
weight: 14.0
description: Tag data based on rules
date: 2022-05-10T14:00:00
---


## Description


Rule Based Tagging is used to add attributes contained within a dimesion to a data table.

![Rule Based Tagging](/images/rule_based_tagging.png)



## Data Table Settings

The **Source Table** and **Tagging Result Table** can be selected dynamically or statically.

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
The **Tagging Result Table** must be a table and not a view.
{{< /note >}}

### Source Table

This is the table that contains the data that you wish to add the attributes from the _Assignment Dimension_ to. 

![Rule Based Tagging](/images/rule_based_tagging_source.png)


### Tagging Result Table

The _Tagging Result Table_ will contain the data from the _Source Data Table_ with the attributes contained in the _Assignment Dimension Hierarchy_. 

![Rule Based Tagging](/images/rule_based_tagging_target.png)

### Assignment Dimesion Hierarchy

![Rule Based Tagging](/images/rule_based_tagging_assignment.png)

The **Assignment Dimension Hierarchy** gives the user the ability to point, click and filter the ***Source Table*** to add attributes to the ***Tagging Result Table***. 
The **Assignment Dimension Hierarchy** is created by combining dimensions that reference the ***Source Table***.

#### Creating An Assignment Dimension Hierarchy

To create the **Assignment Dimension Hierarchy** you must first create the dimensions you wish to use to as filters for the ***Source Table***. The links below will guide you through creating these dimensions.


[Creating Dimensions](https://docs.plaidcloud.com/docs/workflow-steps/dimensions/dimension-create/) 

[Loading Dimensions](https://docs.plaidcloud.com/docs/workflow-steps/dimensions/dimension-load/) 

##### Creating The Main Hierarchy

Once the dimensions for the ***Source Table*** have been created the next step is to decide which of the dimensions for the ***Source Table*** will serve as the ***Main Hierarchy*** for the **Assignment Dimension Hierarchy**. 

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
- **Property Type** - For _Rule Based Tagging_ property type should be set to _Source_. 
  - **Source** - Is used in conjunction with the ***Source Table***.

- **Editor Type** - This drop down should be set to ***Select Dimension***.

Once the appropriate properties have been selected for the dimension being added to the Assignment Hierarchy select "Edit Configuration".
###### Dimension Configuration

![Assignment Hierarchy Configure](/images/allocation_by_dimension_configure.png)

- **Dimension** - Use the drop down to select the dimension.
- **Hierarchy** - If the dimension selected has alternate hierarchies, then they will appear and be selectable here as well as the main hierarchy.
- **Start Node** - If you don't wish the dimension to be displayed from the top node you can select any node within the hierarchy as the node from which the dimension will be displayed.
- **Allow Multiple Selections** - If checked the user will be able to select multiple nodes in the hierarchy.
- **Special Cases** - Are not used in _Rule Based Tagging_.

## Source Map

{{< include "common-allocation-source-map" >}}

## Source Filters

{{< include "common-data-filter" >}}

