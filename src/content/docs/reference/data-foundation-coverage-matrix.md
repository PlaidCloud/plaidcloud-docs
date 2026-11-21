---
title: Data Foundation Coverage Matrix
description: Which Common Finance Model dataset each system Data Foundation connects to supplies directly, and which you add as a file.
sidebar:
  label: Data Foundation Coverage
---

Data Foundation reads every ERP system and instance you connect, directly, into one Common Finance Model. Files fill anything a system doesn't hold, so every dataset below can also be supplied as a file.

## Legend

| Mark | Meaning |
| --- | --- |
| **Full** | Data Foundation reads the dataset directly from the system. |
| **Full¹** | Read directly when the system holds it. A system without the data doesn't stop the load. A connection without access to it leaves that dataset empty or fails only that dataset, and the rest loads. |
| **File** | The system doesn't supply this dataset. Add it as a file. |

## SAP, Oracle, and Dynamics 365

| Dataset | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Entities | Full | Full | Full | Full | Full | Full |
| Fiscal calendar | Full | Full | Full | Full | Full | Full |
| Chart of accounts | Full | Full | Full | Full | Full | Full |
| Departments | Full | Full | Full | Full | Full | Full |
| Profit centers | Full¹ | Full¹ | Full¹ | Full¹ | File | Full¹ |
| Sites | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| Projects | File | File | File | File | File | File |
| Sales reps | File | File | File | File | File | File |
| Products | Full | Full | Full | Full¹ | Full¹ | Full |
| Customers | Full | Full | Full | Full¹ | Full¹ | Full |
| Suppliers | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| General ledger | Full | Full | Full | Full | Full | Full |
| Trial balance | Full | Full | Full | Full | Full | Full |
| Month-end balance | File | Full¹ | File | Full¹ | Full¹ | File |
| Bank balances | File | Full¹ | File | Full¹ | Full¹ | Full¹ |
| Sales lines | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| Pipeline | File | File | File | File | File | File |
| Supplier invoice lines | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| Purchase orders | Full¹ | Full¹ | File | Full¹ | Full¹ | File |
| Open items | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| Payments | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| Inventory balances | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| Standard costs | Full¹ | Full¹ | File | Full¹ | Full¹ | File |
| Fixed assets | Full¹ | Full¹ | File | Full¹ | Full¹ | File |
| Asset movements | Full¹ | Full¹ | File | Full¹ | Full¹ | File |
| Budget | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| Allocation drivers | Full¹ | Full¹ | File | File | File | File |
| Currency rates | Full | Full | Full | Full | Full | Full |
| Segment values | File | File | File | File | File | File |
| CO-PA by valuation | Full¹ | Full¹ | File | File | File | File |

## Mid-Market and Cloud Finance Systems

| Dataset | Business Central | Sage 100 | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Entities | Full | Full | Full | Full | Full | Full | Full |
| Fiscal calendar | Full | Full | Full | Full | Full | Full | Full |
| Chart of accounts | Full | Full | Full | Full | Full | Full | Full |
| Departments | Full | Full¹ | Full | File | Full¹ | Full | Full |
| Profit centers | Full¹ | File | Full¹ | Full¹ | Full¹ | File | Full¹ |
| Sites | Full¹ | File | Full¹ | Full¹ | Full¹ | File | Full¹ |
| Projects | File | File | Full¹ | File | File | File | File |
| Sales reps | File | File | File | File | File | File | Full¹ |
| Products | Full | File | Full | Full¹ | Full¹ | Full¹ | Full |
| Customers | Full | File | Full | Full¹ | Full¹ | Full¹ | Full |
| Suppliers | Full¹ | File | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| General ledger | Full | Full | Full | Full | Full | Full | Full |
| Trial balance | Full | Full | Full | Full | Full | Full | Full |
| Month-end balance | Full¹ | File | Full¹ | Full¹ | Full¹ | Full¹ | File |
| Bank balances | Full¹ | File | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| Sales lines | Full¹ | File | Full¹ | Full¹ | Full¹ | Full¹ | Full |
| Pipeline | File | File | File | File | File | File | File |
| Supplier invoice lines | Full¹ | File | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| Open items | Full¹ | File | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| Payments | Full¹ | File | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| Purchase orders | File | File | File | File | File | File | File |
| Inventory balances | Full¹ | File | File | Full¹ | File | File | Full¹ |
| Standard costs | File | File | File | File | File | File | File |
| Fixed assets | File | File | File | File | File | File | File |
| Asset movements | File | File | File | File | File | File | File |
| Budget | Full¹ | File | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| Allocation drivers | Full¹ | File | Full¹ | File | File | Full¹ | Full |
| Currency rates | Full | File | Full | Full¹ | File | Full | Full¹ |
| Segment values | File | File | File | File | File | Full¹ | Full¹ |
| CO-PA by valuation | File | File | File | File | File | File | File |

## CRM, Consolidation, and Planning Sources

| Dataset | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Entities | File | File | File |
| Fiscal calendar | Full¹ | File | File |
| Chart of accounts | File | File | File |
| Departments | File | File | File |
| Profit centers | File | File | File |
| Projects | Full¹ | File | File |
| Sales reps | Full¹ | File | File |
| Products | Full¹ | File | File |
| Customers | Full¹ | File | File |
| General ledger | File | File | File |
| Trial balance | File | File | File |
| Sales lines | File | File | File |
| Pipeline | Full¹ | File | File |
| Sales orders | Full¹ | File | File |
| Inventory balances | File | File | File |
| Budget | File | Full | Full |
| Allocation drivers | File | Full¹ | Full¹ |
| Currency rates | File | File | File |
| Segment values | File | File | File |
| CO-PA by valuation | File | File | File |

## Notes by System

- **Sales orders, contracts, deferred revenue and inventory movements** aren't read from any system except Salesforce orders. Add them as files.
- **Salesforce** is a CRM source. It supplies customers, products, the sales pipeline, sales reps (users), campaigns as projects, its fiscal months and orders, never the ledger. Orders need Orders enabled in Salesforce. When Salesforce refuses the order read, only the order months fail, and they keep what they last loaded.
- **OneStream** is a results source. It supplies the budget dataset, landing your consolidated results so Data Foundation can reconcile the group P&L to them, and a Budget or Forecast scenario as a plan. An optional second adapter supplies planned headcount and units as allocation drivers.
- **Anaplan** is a plan source. It supplies the budget dataset, from a Budget, Forecast or Consolidated plan, and allocation drivers from an optional second export.
- **SAP S/4HANA and SAP ECC** read the same master data, suppliers, supplier invoices, purchase orders, open items, payments, the fixed asset register and standard costs. ECC reads its ledger from financial accounting and controlling line items, and its totals and month-end balance from the general ledger totals table. Profit centers and plants (sites) are read when the system holds them. Sales lines are billing documents. CO-PA by valuation is read from the operating concern's line item table you name; with none named, add it as a file.
- **Oracle E-Business Suite** reads sites and profit centers from the chart of accounts segment you name for each.
- **Oracle Fusion** reads each optional dataset from its own BI Publisher report. A customers, products, sites or suppliers report you don't deploy leaves that dataset empty with a warning; any other report's dataset fails and keeps what it last loaded; everything else loads.
- **Workday** has no direct journal or balance service. Data Foundation gives you the reports to build and reads them. Segment values (worktags), customers, products, suppliers, sales lines, sub-ledgers, bank balances, budgets and drivers come from optional reports, and the month-end balance from the beginning balances report's ending balance.
- **Sage 100** is read through a PlaidLink agent, one company per connection. It keeps its books in one currency, so it supplies no currency rates, and Data Foundation doesn't read its products, customers or sales lines. Departments are read from the account's department segment when the account mask has one.
- **Xero** doesn't supply currency rates. Add them as a file if your entities use more than one currency. Departments, sites and profit centers are the options of the tracking categories named exactly Department, Site and Profit centre. Xero allows two tracking categories, so an organisation has at most two of the three.
- **QuickBooks Online** has no departments: its locations are read as sites and its classes as profit centers. Customers, products, suppliers, currency rates, budgets, inventory, sales and purchases are read when the company holds them, and inventory only when the company tracks quantity on hand.
- **NetSuite** reads custom segments as segment values, classes as profit centers and locations as sites. Currency rates and inventory are read when the account offers them, and budgets when the account uses NetSuite Budgets and the role can read them.

## Month-End Balance

Data Foundation reads the closing balance each system itself reports at each month end (see [Can the Numbers Be Trusted?](/guides/projects/data-foundation-proof/)) from:

| System | Month-end balance read from |
| --- | --- |
| SAP ECC | The general ledger totals table (`FAGLFLEXT`, or `GLT0` on the classic general ledger) |
| Oracle E-Business Suite | `GL_BALANCES`, which must hold every period |
| Oracle Fusion | The PlaidCloudBalances report, covering every period |
| Business Central | The trial balance at each month end |
| Sage Intacct | Account balances (the ending balance of each month) |
| QuickBooks Online | The Trial Balance report at each month end |
| Xero | The Trial Balance report at each month end |
| Workday | The ending balance of the Beginning Balances report |

SAP S/4HANA, SAP S/4HANA Cloud, Dynamics 365 Finance and Operations, NetSuite and Sage 100 report no separate balance that Data Foundation reads. They load and work as usual. When Business Central refuses its trial balance at a month end, that month's balance fails and keeps what it last loaded.

## Journal Detail

Besides the amounts, each general ledger line carries the journal's type, its document date, who entered it and when, who approved it, the journal it reverses and its tax, where the system holds them. The fiscal calendar carries each period's status.

| System | Journal type | Document date | Entered by and when | Approver | Reversal | Tax | Period status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SAP S/4HANA | Yes | Yes | Yes | No | No | Code | Yes |
| SAP ECC | Yes | Yes | Yes | No | Yes | Code and amount | Yes |
| SAP S/4HANA Cloud | Yes | Yes | Yes | No | Yes | No | No |
| Oracle E-Business Suite | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Oracle Fusion | Yes | Yes | Yes | Yes | Yes | No | Yes |
| Dynamics 365 Finance and Operations | Yes | Yes | Yes | No | No | No | Yes |
| Business Central | Yes | Yes | Yes | No | Yes | No | Yes |
| Sage 100 | No | No | No | No | No | No | Closed once the period ends |
| Sage Intacct | Yes | Yes | Yes | Yes | Yes | No | Yes |
| QuickBooks Online | Yes | Yes | Yes | No | No | No | The close-the-books date |
| Xero | Yes | Yes | When only | No | No | No | The lock date |
| Workday | Yes | Yes | Yes | Yes | Yes | Code and amount | Yes |
| NetSuite | Yes | Yes | Yes | No | No | No | Yes |

SAP S/4HANA Cloud reads who entered a journal and what it reverses from the Journal Entry service, Sage Intacct from journal batches, and Oracle E-Business Suite the approver from `GL_JE_BATCHES`. A connection that can't read them leaves those columns empty.

## Related

- [Data Foundation](/guides/projects/data-foundation/)
- [Get Started with Data Foundation](/guides/projects/data-foundation-getting-started/)
- [Add files for data outside your ERP](/guides/projects/data-foundation/#add-files-for-data-outside-your-erp)
- Connection access guides:
  - [NetSuite](/guides/connections/netsuite-access-for-data-foundation/)
  - [Salesforce](/guides/connections/salesforce-access-for-data-foundation/)
  - [SAP S/4HANA](/guides/connections/sap-s4hana-access-for-data-foundation/)
  - [SAP ECC](/guides/connections/sap-ecc-access-for-data-foundation/)
  - [SAP S/4HANA Cloud](/guides/connections/s4hana-cloud-access-for-data-foundation/)
  - [Oracle E-Business Suite](/guides/connections/oracle-ebs-access-for-data-foundation/)
  - [Oracle Fusion](/guides/connections/oracle-fusion-access-for-data-foundation/)
  - [Dynamics 365 Finance and Operations](/guides/connections/dynamics-365-fo-access-for-data-foundation/)
  - [Business Central](/guides/connections/business-central-access-for-data-foundation/)
  - [Sage 100](/guides/connections/sage-100/)
  - [Sage Intacct](/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/guides/connections/anaplan/#anaplan-as-a-data-foundation-source)
