---
title: Conditional Step Execution
slug: step-conditions
description: Control if a step is executed in a workflow based on a set of conditions
date: 2023-06-21T07:40:20
---


## Overview

Workflow steps normally execute in the defined order for the workflow.  However, it is often useful to have certain steps only execute if predefined conditions are met.  By using the step conditions capability you can control execution based on the following options:
 - Variable values
 - Table has rows or is empty
 - A document or folder exists in Document
 - A document or folder is missing in Document
 - Table query result
 - Date and time conditions are met

For variables or table query result comparisons you can use the following comparisons:
 - Equal
 - Does not equal
 - Contains
 - Does not contain
 - Starts with
 - Ends with
 - Greater than
 - Less than
 - Greater than or equal
 - Less than or equal

What is also important to note is that you can have multiple conditions that must be met in order for the step to execute.  This provides a powerful tool for controlling exactly when a step should execute.

## Adding and Controlling Conditions

To activate and add conditions, edit the step and select the **Conditions** tab.

Check the **Check Conditions Before Running** checkbox when you are ready to activate the conditions

Add conditions in the **Condition Checks** section.


## Managing Conditions

You can add as many conditions as necessary in the **Conditions Check** section.  As you add them, it is a good idea to give them a useful name so you can find the conditions easily in the future.

Once you add a condition, select it on the left and the condition evaluation criteria will be editable on the right.


## Variable Conditions

When checking variable conditions, the **Value Check Parameters** section must be completed so a comparison can be made.

In the **Variable or Table Field** fill in the variable name.  Select a comparison type and enter a comparison value.


## Basic Table Conditions

If the condition is checking whether a table has rows or is empty, you will also need to define the table in the **Table Data Selection** tab.


## Advanced Table Conditions

When using Advanced Table conditions, the **Value Check Parameters** section must be completed so a comparison can be made.

In the **Variable or Table Field** fill in the field name from the table selection.  Select a comparison type and enter a comparison value.

In the **Table Data Selection** tab, select the table and complete the data mapping section with at least the field referenced for the condition comparison.

## Document Path Conditions

If the condition is checking whether a document or folder exists, this requires picking the Document account and specifying the document path to check in the **Document Path** tab.

## Date and Time Conditions

For Date or Time selections you can add multiple conditions if a combination of conditions is necessary.  For example, if you only wanted a step to run on Mondays at 2:05am, you would create three conditions:
 - Day of the week condition set to Monday (1)
 - Hour of the day set to 2
 - Minute of the hour set to 5
