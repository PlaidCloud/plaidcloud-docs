---
title: Export Project Table
slug: export-project-table
description: Export data from a project table
date: 2022-05-10T14:00:00
---

## Description

Export data from a project table to different project's table.

## Data Sharing Management

![Data Sharing Management](/images/import_external_project_table_1.png)

In order to export a table to another project you must first go to both projects **Home Tab** and allow the projects to share data with each other. To do this select **New Data Share** and select the project and give them **Read** access.

## Export External Project Table

![Export External Project Table](/images/export_external_project_table.png)

### Read From
Select the **Source Table** from the drop down menu.

### Write To

#### Target Project
Select the **Target Project** from the drop down menu.

#### Target Table Static

To establish the target table select either an existing table as the target table using the **Target Table** dropdown or click on the green **"+"** sign to create a new table as the target. 

##### Table Creation
When creating a new table you will have the option to either create it as a **View** or as a **Table**. 
###### Views:
Views are useful in that the time required for a step to execute is significantly less than when a table is used. The downside of views is they are not a useful for data exploration in the table Details mode.

###### Tables:
When using a table as the target a step will take longer to execute but data exploration in the Details mode is much quicker than with a view.

{{< note >}}
Use tables for key steps in your workflows where data validation or the ability to perform ad-hoc analytics will be necessary. For all other steps use views to decrease the overall workflow calculation time. It's possible to change a table to a view and vice versa so you can always update the table target type at a later date.
{{< /note >}}

#### Target Table Dynamic

The Dynamic option allows specification of a table using text, including variables.  This is useful when employing
variable driven workflows where table and view references are relative to the variables specified.

An example that uses the `current_month` variable to dynamically point to target table:

```
legal_entity/inputs/{current_month}/ledger_values
```

{{< note >}}
If the table does not exist it will be created dynamically when the import process runs
{{< /note >}}

#### Append to Existing Data

To append the data from the source table to the target table select the ***Append to Existing Data*** check box.
