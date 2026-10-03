---
title: Call SAP Financial Document Attachment
description: Retrieve SAP financial document attachments from a PlaidCloud workflow step for automated document extraction and processing.
---

## Description



Attaches a file to a specific FI (Financial Accounting) document in SAP ECC / S/4HANA via an RFC (Remote Function Call). Useful for posting supporting documentation — scanned invoices, approval workflows, contract copies — alongside the financial entries they back.

Requires the SAP RFC credentials configured on the SAP connector and the target FI document number (company code, document number, fiscal year).


## What's Checked When You Save

The step reads each file's path from a `relative_file_path` column among the output columns on its **Table Data Selection** tab, and that column must be text. Saving is refused without one — *The output columns must include relative_file_path, the path of each file to attach.* — or when it has another type — *The relative_file_path column must be text, not integer.*

Saving with a source table chosen but no source or no target columns fills the empty side from the source, as **Populate Both Mapping Tables** would.


## Examples


### RFC Parameters


Select Agent to Use. Select Target Directory from the drop down bar, and browse below for the correct child folder destination for the file. Next, appropriately name the “Target File Name”. Under “Function Call Information”, enter the Function, the Return Value Parameter, and select the parameters.



You can choose to Insert Row or Append Row under the Parameters section, as well as name the parameters and give them values. Choose the Max Concurrent Requests number, and select Wait for RFC to Complete. Save and Run Step.
