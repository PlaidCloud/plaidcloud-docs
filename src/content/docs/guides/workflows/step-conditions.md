---
title: Conditional Step Execution
description: Configure conditional execution for PlaidCloud workflow steps to control which steps run based on variable values and logic.
sidebar:
  order: 12
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

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 640 190" role="img" aria-label="A step condition gates whether a step runs. When the prior step finishes, the condition is checked; if it is met the step runs, otherwise the step is skipped and the workflow continues to the next step." style="width:100%;max-width:640px;height:auto;">
  <defs><marker id="sc3-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="74" width="104" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="66" y="100" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">prior step</text>
  <path d="M118 96 L150 96" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <rect x="152" y="66" width="150" height="60" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="227" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">condition met?</text>
  <text x="227" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">variable · rows · doc exists</text>
  <path d="M302 82 C340 82 350 54 384 54" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="345" y="48" text-anchor="middle" font-size="10" fill="var(--sl-color-accent)">true</text>
  <path d="M302 110 C340 110 350 138 384 138" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="5 4" marker-end="url(#sc3-arrow)" />
  <text x="345" y="132" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">false</text>
  <rect x="386" y="34" width="128" height="40" rx="8" fill="var(--sl-color-accent)" fill-opacity="0.12" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="450" y="59" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-text)">step runs</text>
  <rect x="386" y="118" width="128" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="450" y="143" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">step skipped</text>
  <path d="M514 54 C548 54 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <path d="M514 138 C548 138 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="606" y="100" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">next</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">A condition gates the step: met → the step runs; not met → it's skipped. Either way the workflow moves on to the next step. Conditions test variables, whether a table has rows, or whether a document exists.</figcaption>
</figure>

## Adding and Controlling Conditions

To activate and add conditions on a step:
1) Find the step you want to add a condition on
2) Click the **Edit Step Details** (pencil) icon
3) Select the **Conditions** tab.
4) Check the **Check Conditions Before Running** checkbox to enable the dialog and add conditions.
5) In the **Condition Checks** section on the left, select the "+" to add a New Condition
6) Add a condition from the tabbed section on the right
7) Repeat steps 5,6 as needed to add all your conditions


## Managing Conditions

You can add as many conditions as necessary in the **Condition Checks** section.  As you add them, it is a good idea to give them a useful name so you can find the conditions easily in the future.

Once you add a condition, select it on the left and the condition evaluation criteria will be editable on the right.

To rename a condition, select it and edit the **Name** field at the top of the Configuration panel on the right — or double-click the condition in the list. You can also right-click a condition for **Rename** and **Delete**; **Delete** is also available from the "−" button above the list.


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

For "Use Financial Close Workday", set that to the xth day of the month that your close happens on. For example, if your close happens on the 5th day of the month, have "5".

## Setting Conditions With an AI Assistant

An AI assistant connected to your workspace can add and change a step's conditions for you, whether it is creating the step or editing one you already have. Every condition type described earlier is available to it except **Check Financial Close Workday**: an assistant can write that one, but it never matches, so the assistant warns you instead of letting it pass unnoticed. Set that one on the **Conditions** tab yourself.

Three things work differently from editing conditions by hand:

- **The whole list is replaced each time.** Ask for one condition to be added or changed and the assistant sends the full list, so any condition it leaves out is removed. If you are not certain it has them all, ask it to list the step's current conditions before it writes.
- **A condition that cannot be evaluated is refused.** A condition that does not say what it checks is rejected instead of saved, and the step keeps the conditions it already had. Fix the request and ask again.
- **An incomplete condition is saved, with a warning.** A condition missing the value to compare against, or conditions added without **Check Conditions Before Running** ticked, are stored and reported back as a warning. Open the **Conditions** tab and finish them, or the step does not behave as you asked.

An assistant can also set the step's lock, its visibility in the Manager and Explorer views, its retry settings, and the step to go to on error.
