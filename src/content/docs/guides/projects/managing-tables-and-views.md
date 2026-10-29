---
title: Managing Tables and Views
description: Manage tables and views within PlaidCloud projects including creation, configuration, permissions, and data object organization.
sidebar:
  order: 3
---

PlaidCloud offers the ability to organize and manage tables, including labels. Tables are available to all workflows within a project and have many tools and options.


In addition to tables, PlaidCloud also offers Views based on table data. Using Views allows for instant updates when underlying table changes occur, as well as saving data storage space.



Options include:


* The same table can exist on multiple paths in the hierarchy (alternate hierarchies)
* Tables are taggable for easier search and inclusion in PlaidCloud processes
* Tables can be versioned
* Tables can be published so they are available for Dashboard Visualizations

PlaidCloud uses a path-based system to organize tables, like you would use to navigate a series of folders, allowing for a more flexible and logical organization of tables. Using this system, tables can be moved within a hierarchy, or multiple references to one table from different locations in the hierarchy (alternate hierarchies), can be created. The ability to manage tables using this method allows the structure to reflect operational needs, reporting, and control.



## Finding Tables


Use the filter box in the lower left of the hierarchy to search table names and labels. The matches show in the hierarchy above.


### By Workflow

The **By Workflow** folder at the end of the **Tables** tab groups tables under each workflow that reads or writes them. Open a workflow to see its tables. The folder is a view of the same tables, so you can't move or copy anything from it.


### By Column

Type a column name in the column search box on the **Tables** tab and press Enter, or select the magnifier beside it, to show only the tables that have a column with that name. The search reads column names, not the data, so it is fast. Select **Contains** to match part of a column name instead of the whole name. Clear the box to show every table again. A long search can return in pages and the status line says when it is still searching or may be incomplete.

Select **Column Tree** to search from a window of its own. Each table that has the column opens to two lists:

* **Fed by** — the tables that supply the column
* **Feeds** — the tables the column goes on to feed

An AI assistant connected over MCP finds the same tables with `table_find(column=...)`, matching the whole name or part of it.


### Search Values

To find which tables hold a value, choose **Search values in data… (slow)** from the **Actions** menu on the **Tables** tab, or right-click a table and choose it to look in that table only. Enter the value, choose **Contains** to match part of a value, and select **Search**. Each table that holds the value is listed with the columns it appears in and a few of the matching values. Double-click a table, or press Enter on it, to open it in the Table Explorer. A column opens the table filtered to the rows that match. If the column search box holds text, it fills in the value to find.

Before you search, know that:

* The search reads every row of every table searched, so it can be very slow and use a lot of warehouse resources. The window warns you, and the search buttons stay off until a search finishes.
* You see only rows you could already open. Row-level security applies to every search.
* Your warehouse's query history records the values you search for.
* The search covers the text columns of tables. Tables that haven't been built are skipped and named in a warning.
* Results come in pages. When the status line says the search stopped early, choose **Search more** to continue with the tables not yet searched.

An AI assistant connected over MCP uses `table_value_search`. It returns the tables and columns that hold the value, never the values themselves. When you ask the AI assistant in a project to find a value, Weave sends the names of the matching tables and columns to the language model provider.



## Import a CSV File

**To turn a CSV file into a new table in this project:**

1. Drag the file from your computer onto the project's **Tables** list, or choose **New** > **Table from CSV File** on the toolbar and drop the file onto the box or click **Choose a CSV file**.
2. PlaidCloud uploads the file to your **Personal Temp Drive**, or to the workspace's **Temp Drive** if you don't have one, and imports it into a new table at the top level of the list, named after the file: `Sales Data.csv` becomes `sales_data`. If the project already has a table with that name, the new one gets a number, such as `sales_data_2`.
3. The list refreshes with the new table selected, and **Your data at a glance** opens on it. See [Start With Your Own CSV](/get-started/quickstart/#start-with-your-own-csv) for what the panel shows.

Only files ending in `.csv` are accepted. You need permission to create tables and to write to document storage, and a locked project doesn't accept a CSV until it is unlocked. If the import fails, the window says why and your project is left as it was. PlaidCloud deletes the uploaded file from the temp drive once the import has finished, whether or not it succeeded; failing that, the temp drive deletes it after a day.

## Move


**To move a table:**


1. Drag it into the folder where you wish it to be located

## Rename


**To rename a table:**


1. Right click on the table
2. Select the rename option
3. Type in the new name and save it
4. The table is now renamed, but it retains its original unique identifier.

## Clear


**To clear a table:**


1. Select the tables in the hierarchy ‘
2. Click the clear button on the top toolbar.

*Note: You can clear a single table or multiple tables*



## Delete


**To delete a table:**


1. Select the tables in the hierarchy
2. Click the delete button on the top toolbar
3. The deleted operation will check to see if the table is in use by workflow steps or Views. If so, you will be asked to remove those associations before deletion can occur.

*Note: You can also force delete the table(s). Force deletion of the table(s) will leave references broken, so this should be used sparingly.*


### Last Read

The delete window shows when the table was last read, for example **Last read 3 days ago by** a person or step, so you can tell a table nobody uses from one that is still in use. PlaidCloud takes this from your warehouse's own query history and leaves out reads made by its own housekeeping.

| Warehouse | What is needed |
| --- | --- |
| Snowflake | Reads come from Access History, which Snowflake records up to about 3 hours late. The connection's role needs the `SNOWFLAKE.GOVERNANCE_VIEWER` database role (`IMPORTED PRIVILEGES` on the `SNOWFLAKE` database also works). Snowflake Standard edition has no Access History. |
| Databricks | Reads come from the lineage table, which Databricks also records with a delay, so a recent read may not show yet. The connection's identity needs `USE CATALOG` on `system`, `USE SCHEMA` on `system.access`, and `SELECT` on `system.access.table_lineage`. |
| PlaidCloud Lakehouse | Read history is not yet available. The window shows **Read history incomplete**. |

When you connect your warehouse, [the connection check](/guides/connections/external-lakehouse/#3-check-then-use-it) recommends any of these grants that are missing, each with the statement to run. They are recommended, not required: without them the warehouse connects and the window shows **Read history incomplete**.

When PlaidCloud can't read the whole history, the line says **Read history incomplete** and never reports "no reads" in its place. Anyone with direct SQL access to your warehouse can set a session tag that changes how their own reads are labelled.

An AI assistant connected over MCP gets the same answer from `table_describe(include=['last_read'])`.



## See a Table's Columns


Selecting a table opens its details panel. Its **Columns** section lists each column with its **Type** and **Description**, the description coming from **Column Properties**. Point at a row to read a long description in full.

A table that isn't in the warehouse right now, because its data expired or no step has built it, has no columns to list. The section says so and shows how many columns the table has. Run a step that writes the table to list them.


## See Where a Table Is Used


Selecting a table opens its details panel, which lists the workflow steps that touch it:


* **Table Created By** — steps that write to the table
* **Table Contributes To** — steps that read from it
* **May Reference This Table** — steps that reach a table through a variable that cannot be resolved. This section only appears when there are such steps.


A step can name a table outright, or reach it through a path containing a variable, such as `/Periods/{period}/Sales`. Where that variable has a current value, the step appears in the first two lists with an information icon beside it. Hover the row to see the path as the step stores it.


Treat those rows as the weaker answer they are. They describe what a run starting now would touch — not everything that has ever touched the table. Change the variable and a different table is read.


Some variables cannot be resolved. Either nothing has set the variable at all, or the value a run uses does not come from what is stored — a Workflow Loop takes its variables from data as it iterates, a Set Variable step assigns during the run, a macro is handed its variables by whichever step calls it, and a run started by a sensor carries that sensor's own details. In each case whatever is stored between runs is left over from the last one rather than a value to trust. Rather than resolve those to a table that may be the wrong one, PlaidCloud lists the steps by name under **May Reference This Table**, with the variable it could not resolve, so you can open them and check.


A step your role can't see is still listed, so you know the table is in use, but without its name or workflow, and you can't open it. It still counts when you delete the table. A step you can see is listed without any workflow your role hides. Nothing is hidden from an Architect.


*Note: When you delete tables from the **Tables** list, a step that reaches a table through a path, with or without a variable, counts as using it, even when its variable can't be resolved. The delete window lists the step, and the delete goes ahead only if you force it.*



## Create New Directory Structure


**To add a new folder:**


1. Click the New Folder button on the toolbar

**To add a folder to an existing folder:**


1. Right-click on the folder
2. Select New Folder


## View Data (table Explorer)


Table data is viewed using the Data Explorer. The Data Explorer provides a grid view of the data as well as a column by column summary of values and statistics. Point-and-click filtering and exporting to familiar file formats are both available. The filter selections can also be saved as an Extract step usable in a workflow.



## Publish Table for Reporting


Dashboard Visualizations are purposely limited to tables that have been published. When publishing a table, you can provide a unique name that may distinguish the data. This may be useful when the table has a more obscure name on part of the workflow that generated it, but it needs a clearer name for those building dashboards.


Published tables do not have paths associated with them. They will appear as a list of tables for use in the dashboards area.



## Mark Table for Viewing Roles


The viewing of tables by various roles can be controlled by clicking the Explorer or Manager checkboxes. If multiple tables need to be updated, select the tables in the hierarchy and select the desired viewing role from the Actions menu on the top toolbar.



## Memos to Describe Table Contents


Add a memo to a table to help understand the data.



## View Table Shape, Size, and Last Updated Time


The number of rows, columns, and the data size for each table is shown in the table hierarchy. For very large tables (multi-million rows) the row count may be estimated and an indicator for approximate row count will be shown.



## View Additional Table Attributes


**To view and edit other table attributes:**


1. Select a table
2. Click the view the table context form on the right.


## Duplicate a Table


**To duplicate a table:**


1. Selecting the table
2. Click on the duplicate button on the top toolbar.


## Create a Panel App From a Table


Select a table or view and choose **Create Panel App** from the **New** menu or the right-click menu. The **New Studio App** dialog opens with the project and the table already chosen. Name the app and choose **Create**, and Panel Studio opens it with Weave ready to build its first page. The command is available when you select a single table or view, have edit access to the project, and the project isn't read-only. See [Creating a Panel App](/guides/panel-apps/creating/#start-from-a-table).


## See What Tables Store


The **Tables** list shows **Current data**, **History** and **Note** columns beside each table's size, and **Time Travel Days** after them. Above the list, a line gives the project's total: how much it stores, and how much of that is current data and how much is history. A table PlaidCloud hasn't measured yet has no sizes.

Choose **Storage** on the toolbar to open the project's **Storage** window, with suggestions for freeing space and the time travel settings. See [Managing Storage](/guides/projects/managing-storage/#the-storage-window-for-a-project).


## Create a Data Editor from a Table


You can turn a table into a configured data editor in one step — select the table and choose **Create Data Editor from Table** from the **New** menu or the right-click menu. PlaidCloud examines the table's columns and pre-builds the editor's input controls. See [Create a Data Editor from a Table](/guides/projects/managing-data-editors/#create-a-data-editor-from-a-table) for details.
