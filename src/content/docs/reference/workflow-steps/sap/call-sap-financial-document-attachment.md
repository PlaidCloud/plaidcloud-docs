---
title: Call SAP Financial Document Attachment
description: Retrieve SAP financial document attachments from a PlaidCloud workflow step for automated document extraction and processing.
---

## Description



Attaches a file to a specific FI (Financial Accounting) document in SAP ECC via an RFC (Remote Function Call). Useful for posting supporting documentation — scanned invoices, approval workflows, contract copies — alongside the financial entries they back.

Requires the SAP RFC credentials configured on the SAP connector and the target FI document number (company code, document number, fiscal year).


## Examples


### RFC Parameters


Select Agent to Use. Select Target Directory from the drop down bar, and browse below for the correct child folder destination for the file. Next, appropriately name the “Target File Name”. Under “Function Call Information”, enter the Function, the Return Value Parameter, and select the parameters.



You can choose to Insert Row or Append Row under the Parameters section, as well as name the parameters and give them values. Choose the Max Concurrent Requests number, and select Wait for RFC to Complete. Save and Run Step.
