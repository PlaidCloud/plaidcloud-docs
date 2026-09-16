---
title: Troubleshooting Allocations
description: Troubleshoot PlaidCloud allocation issues including common errors, configuration problems, and techniques for debugging results.
sidebar:
  order: 2
---

## Why an Allocation Step Will Not Save

PlaidCloud checks an allocation step's column mapping when you save it. A mapping that cannot run is refused at that point, with a **Cannot save** notification listing what to fix, and the form switches to the tab holding the problem. Previously such a step saved without complaint and then stopped the workflow part-way through a run — often minutes later, and with a message that named a count rather than a field.

Nothing is checked until you have chosen both the **Values To Allocate Table** and the **Driver Data Table**. The column mapping is built from those two tables, so until both are set the step only asks for the tables themselves.

### Allocation Source Map

**"No columns specified for allocation."**
Set the **Role** of at least one column to **Value to Allocate**. That column holds the values being spread across the targets.

**"Only numeric columns can be allocated, but ... is not numeric."**
A column marked **Value to Allocate** has a non-numeric **Type**. Change the type to a numeric one — Numeric, Currency, Integer, Big Integer, Small Integer, Tiny Integer, Float, Double, Decimal, Serial or Big Serial.

**"Rename the `alloc_status` target column."**
An allocation writes its own `alloc_status` column into the result table, so a target column of that name collides with it. Rename yours.

### Driver Data Map

**"No driver split value column found."**
Set the **Role** of one driver column to **Split Value**. That column holds the weights or percentages the allocation divides by.

**"The driver value column ... must be numeric."**
Change the **Type** of the **Split Value** column to a numeric one.

**"No driver relation columns specified."**
Set the **Role** of at least one driver column to **Source Relation (Denominator)**. This is what relates the driver rows back to the source rows.

**"No allocation target columns are indicated."**
Set the **Role** of at least one driver column to **Allocation Target (Numerator)**. These become the targets of the allocation and appear in the result table.

**"Driver relation columns do not exist in the source data."**
A column marked **Source Relation (Denominator)** has no matching column of the same name in the **Allocation Source Map**. Either rename it to match, or add the column to the source map.

**"Allocation value column ... is also used as a numerator or denominator column."**
The same column name is both a **Value to Allocate** in the source map and a **Source Relation (Denominator)** or **Allocation Target (Numerator)** in the driver map. Rename one of them so the value being allocated is distinct from the columns describing where it goes.

### Split Using Dimension Only

**"Please select a hierarchy to use for the allocation dimension."**
Choose an **Assignment Dimension Hierarchy** on the **Data Table Settings** tab. See [Configure an Allocation](/guides/allocations/setup/configure-an-allocation/).

## Stranded Cost


Stranded cost is....



## Over Allocation of Cost


Over allocation of cost is when you end up with more output cost...



## Incorrect Allocation of Cost


Incorrect allocation of costs happens when...
