---
title: Call SAP RFC
slug: call-sap-rfc
description: Calls an SAP ECC Remote Function Call (RFC) and retrieves the data in tabular form
date: 2022-01-25T07:39:56
---

## Description


Calls an SAP ECC Remote Function Call (RFC) and retrieves the data in tabular form. This data is then available for transformation processes in PlaidCloud.


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
