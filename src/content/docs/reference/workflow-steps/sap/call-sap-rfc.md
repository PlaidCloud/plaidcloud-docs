---
title: Call SAP RFC
description: Call SAP RFC function modules from a PlaidCloud workflow step for direct integration with SAP ECC and S/4HANA systems.
---

## Description


Calls an SAP ECC / S/4HANA Remote Function Call (RFC) and retrieves the data in tabular form. This data is then available for transformation processes in PlaidCloud.


## Data Destination

Land the RFC result as a file or in a table.

**File** writes the result as **JSON**, **Comma Delimited**, **Tab Delimited**, **Pipe Delimited**, or **Parquet**. A Parquet file carries the same column types as a table.

**Table** lands the result in a **Target Table**, typed from the RFC function's own field definitions:

| SAP field type | Lands as |
|---|---|
| Date | Date. A blank or initial date lands empty. An invalid date lands empty, and the step finishes with a warning naming the column. |
| Packed decimal | Exact decimal. More than 10 decimal places or 28 integer digits lands as text instead, and the step finishes with a warning naming the column. |
| Integer | Integer. |
| `FLOAT` | Double. |
| Decimal float | Exact text. |
| `NUMC`, `CHAR` | Text, leading zeros kept. |
| Time | Text, as `HH:MM:SS`. |
| Raw bytes | Hex text. |
| `UTCLONG` | Text. |

If SAP can't describe the function's fields, decimals land as exact text instead.

When SAP describes the function, each parameter converts to the type it expects: dates to `YYYYMMDD`, times to `HHMMSS`, integers and decimals to numbers, text fields to text, and structure and table parameters field by field. A value that can't convert to an integer or decimal parameter fails the step.

## Examples


### RFC Parameters


Select Agent to Use. Select Target Directory from the drop down bar, and browse below for the correct child folder destination for the file. Next, appropriately 
name the “Target File Name”. Under “Function Call Information”, enter the Function, the Return Value Parameter, and select the parameters.

You can choose to Insert Row or Append Row under the Parameters section, as well as name the parameters and give them values. Choose the Max Concurrent Requests 
number, and select Wait for RFC to Complete. Save and Run Step.



### Advanced Value Iteration


You can select “No Iterators” at the top of this tab and then select Save and Run Step if desired, or you can specify.


Here, you can select “Specify Argument Values” to Iterate Over and create arguments to then go to the Iteration Value.


Next to Select Iterator Argument to Edit Values, there is the option to Insert Tow, Append Row, Delete Row, Move Down Row, or Move to Bottom Row. 
Below you can choose Range Iterators using the same drop down menu. The last section is titled “Exclusions for Selected Range Iteration” 
with the same options per row to add, delete, etc. The excluded values can be entered below. Save and Run Step.
