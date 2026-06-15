---
title: Managing Data Editors
description: Manage data editor assignments in PlaidCloud projects to control who can modify table data directly through the data interface.
sidebar:
  order: 5
---

PlaidCloud offers the ability to organize and manage data editors, including labels. Data Editors allow editing table data or creating data by user interaction.



PlaidCloud uses a path-based system to organize data editors, like you would use to navigate a series of folders, allowing for a more flexible and logical organization (control hierarchy) of the data editors. Using this system, data editors can move within a control hierarchy. Multiple references to one data editor from different locations in the control hierarchy (alternate hierarchies) can be created. The ability to manage data editors using this method allows the structure to reflect operational needs, reporting, and control.




## Create a Data Editor from a Table


You can build a ready-to-use data editor directly from an existing table. PlaidCloud examines the table's columns and pre-configures the editor — choosing an input control for each column and turning columns that hold a small set of repeating values into drop-down pick lists.


To create a data editor from a table:


1. Open the project's **Tables** view and select a single table
2. Open **Create Data Editor from Table** — from the **New** menu on the toolbar, or by right-clicking the table
3. PlaidCloud profiles the table and opens the **Data Editor Configuration** window with everything pre-filled: it sets both the source and target to the selected table, so your edits save straight back to it, and it gives each column on the **Form Columns** tab a control that matches its data type and values
4. Review the columns and adjust any controls as needed
5. Click **Save** or **Save & Close**

Saving creates the editor — clicking **Cancel** adds nothing.

When a column maps to a dimension, choose a hierarchy for it on the Form Columns tab before you save. PlaidCloud blocks saving while a dimension column has no hierarchy.


## How PlaidCloud Configures Columns


When you create an editor from a table — or use **Populate From Source** — PlaidCloud sets up each column automatically:


- **Boolean** columns become a checkbox, or a True/False list when the column allows empty values
- **Date** columns become a date chooser
- **Numeric** columns become a number field
- Columns that map to a **dimension** become a dimension picker, where you choose the hierarchy
- Columns whose values repeat over a small set — for example a status or region code — become a **drop-down** that lists the values found in the column
- Other **text** columns become a text field, or a text area for long values
- PlaidCloud includes key-like columns, such as auto-generated IDs, but marks them read-only

For very large tables, PlaidCloud estimates the list of values from a sample of rows. You can change any column's control afterward.

On the **Form Columns** tab, select a column to see a short explanation of why PlaidCloud chose its control.


## Adjust the Pick-List Cutoff


PlaidCloud turns a column into a drop-down only when its values repeat over a small set. You can change that cutoff and re-derive the columns:


1. On the **Form Columns** tab, set **Max pick-list values** to the largest number of distinct values a column may have and still become a drop-down
2. Click **Re-profile**

PlaidCloud re-examines the source table with the new setting and rebuilds the columns. If the editor already has columns, re-profiling replaces them, so PlaidCloud asks you to confirm.


## Populate an Existing Editor from a Table


You can apply the same automatic configuration to an editor you are already editing:


1. Open the data editor's configuration and go to the **Source and Target** tab
2. Set the source to a table
3. On the **Form Columns** tab, click **Populate From Source**

PlaidCloud adds a configured column for each column in the source table. It keeps the columns you have already customized, and prompts you to remove any columns that are no longer in the source.


## Searching


To search for data editors:


1. Use the filter box in the lower left of the control hierarchy

The search filter will search data editors’ names and labels for matches and show the results in the control hierarchy above.




## Move


To move a data editor within the control hierarchy:


1. Drag it into the folder where you wish to place it

## Rename


To rename a data editor:


1. Right click on the data editor
2. Select the rename option
3. Type in the new name and save it

The data editor will now be renamed but retain its original unique identifier.




## Delete


You can delete a single data editor or multiple data editors.


To delete a data editor:


1. Select the data editors in the control hierarchy
2. Click the delete button on the top toolbar


## Create New Directory Structure


To add a new folder to the control hierarchy:


1. Click the New Folder button on the toolbar

To add a folder to an existing folder:


1. Right-click on the folder
2. Select New Folder


## Mark Hierarchy for Viewing Roles


The viewing of data editors by various roles:


1. Click in the Explorer or Manager checkboxes

To update multiple data editors:


1. Select the data editors in the control hierarchy
2. Select the desired viewing role from the Actions menu on the top toolbar


## Memos to Describe Table Contents


To add a memo to a data editor:


1. Select the data editor
2. Update the memo in the right context form


## View Additional Hierarchy Attributes


To view and edit additional data editor attributes:


1. Select the data editor and view the data editor context form on the right


## Duplicate a Data Editor


To duplicate a data editor:


1. Select the data editor
2. Click on the Duplicate button on the top toolbar
