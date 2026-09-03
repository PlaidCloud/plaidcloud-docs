---
title: Set Project Variable
description: Set project-level variables from a PlaidCloud workflow step to store values accessible across all workflows within the project.
sidebar:
  order: 7
---

## Description


“Set Project Variable” sets project variables for use during the workflow. A variable name and value may contain any combination of valid characters, including spaces. Variables are referenced within the workflow by placing them inside curly braces. For example, *a_variable* is referenced within a transform as *\{a_variable}* so it could be used in something like a formula or field value (e.g., \{a_variable} * 2).



## Variable List


The table lists every variable registered in the project, each with its **Current Value** and **Memo** read fresh every time you open the step — so you can see what a variable holds now before deciding what to set it to.

To set one, tick **Set** on its row and enter the new value under **Set Value**. Only ticked rows are written when the step runs, so a value entered without ticking **Set** is ignored. It’s also possible to set a variable that has not been registered yet: add a row and set it the same way — running the step creates it.







## Examples


No examples yet...
