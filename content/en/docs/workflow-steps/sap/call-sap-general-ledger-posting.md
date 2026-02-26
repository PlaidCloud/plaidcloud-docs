---
title: Call SAP General Ledger Posting
slug: call-sap-general-ledger-posting
description: Calls an SAP ECC Remote Function Call (RFC) designed to post a journal entry including applicable VAT and Withholding taxes
date: 2022-01-25T07:39:56
---


## Description


Calls an SAP ECC Remote Function Call (RFC) designed to post a journal entry including applicable VAT and Withholding taxes. This may also run in test mode which will perform a posting process but not complete the posting. This allows for the collection of detectable errors such as an account being closed or a customer not existing in the specified company code specified. The error checking is robust with the ability to return multiple detected errors in a single test.


## Examples


### RFC Parameters


Select Agent to Use. Select Target Directory from the drop down bar, and browse below for the correct child folder destination for the file. Next, appropriately name the “Target File Name”. Under “Function Call Information”, enter the Function, the Return Value Parameter, and select the parameters. 



You can choose to Insert Row or Append Row under the Parameters section, as well as name the parameters and give them values. Choose the Max Concurrent Requests number, and select Wait for RFC to Complete. Save and Run Step.

