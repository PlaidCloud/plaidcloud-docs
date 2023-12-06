---
title: Publishing Tables
slug: tables-views-publish
description: Publishing Tables and Views to allow usage in Dashboard, PlaidXL, and other external reporting
date: 2022-01-25T07:39:48
weight: 4.0
---


Since data pipelines can generate many intermediate tables and views useful for validation and process checks but not suitable for final results reporting, 
PlaidCloud provides a `Publish` process to help reduce the noise when building Dashboards or pulling data in PlaidXL.  The `Publish` process helps clarify 
which tables and views are final and reliable for reporting purposes.


## Publish

From the `Tables` tab in a PlaidCloud project configuration, find the table you wish to publish for use in dashboards and PlaidXL.  Right-click on the 
table record and select `Set Published Table Reporting Name` from the menu.

This will open a dialog where you can specify a unique published name.  This name does not need to be the same as the table or view name.  Enabling a different name 
is often useful when referencing data sources in dashboards and PlaidXL because it can provide a friendlier name to users.

Once the table or view is published, its published name will appear in the `Published As` column in the `Tables` view.

{{< note >}}
There are some restrictions on published names.  They can be a maximum of 63 characters and do have some restrictions on special characters.  This is
needed to ensure maximum compatibility with systems, tools, and processes outside of PlaidCloud.
{{< /note >}}


## Unpublish

Unpublishing a table or view is similar to the publish process.  From the `Tables` tab in a PlaidCloud project configuration, find the table you wish 
to publish for use in dashboards and PlaidXL.  Right-click on the table record and select `Set Published Table Reporting Name` from the menu.

When the dialog appears to set the published name, select the `Unpublish` button.  This will remove the table from Dashboard and PlaidXL usage.

The published name will no longer appear in the `Published As` column.


## Renaming 

Renaming a table or view is similar to the publish process.  From the `Tables` tab in a PlaidCloud project configuration, find the table you wish 
to publish for use in dashboards and PlaidXL.  Right-click on the table record and select `Set Published Table Reporting Name` from the menu.

When the dialog appears change the publish name to the new desired name. Press the `Publish` button to update the name.

The updated name will now appear in the `Published As` column as well as in Dashboard and PlaidXL.
