---
title: Call SAP Master Data Table RFC
slug: call-sap-master-data-table-rfc
description: Calls an SAP ECC Remote Function Call (RFC) designed to access master data tables and retrieves the data in tabular form
date: 2022-01-25T07:39:56
---


## Description


Calls an SAP ECC Remote Function Call (RFC) designed to access master data tables and retrieves the data in tabular form. This data is then available for transformation processes in PlaidCloud. It also provides the ability to export the master data table structure to a separate file which includes column names, data types, and column order information.


## Examples


### RFC Parameters


Select Agent to Use. Select Target Directory from the drop down bar, and browse below for the correct child folder destination for the file. Next, appropriately name the “Target File Name”. Under “Function Call Information”, enter the Function, the Return Value Parameter, and select the parameters.



You can choose to Insert Row or Append Row under the Parameters section, as well as name the parameters and give them values. Choose the Max Concurrent Requests number, and select Wait for RFC to Complete. Save and Run Step.

