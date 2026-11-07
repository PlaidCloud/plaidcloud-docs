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
| **Full¹** | Read directly when the system holds it. A system without the data, or a connection without access to it, doesn't stop the load. |
| **File** | The system doesn't supply this dataset. Add it as a file. |

## SAP, Oracle, and Dynamics 365

| Dataset | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Entities | Full | Full | Full | Full | Full | Full |
| Fiscal calendar | Full | Full | Full | Full | Full | Full |
| Chart of accounts | Full | Full | Full | Full | Full | Full |
| Departments | Full | Full | Full | Full | Full | Full |
| Profit centers | Full¹ | Full¹ | File | File | File | File |
| Products | Full | Full | Full | Full¹ | Full¹ | Full |
| Customers | Full | Full | Full | Full¹ | Full¹ | Full |
| General ledger | Full | Full | Full | Full | Full | Full |
| Trial balance | Full | Full | Full | Full | Full | Full |
| Sales lines | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ |
| Pipeline | File | File | File | File | File | File |
| Inventory balances | Full¹ | Full¹ | Full¹ | File | File | Full¹ |
| Budget | Full¹ | Full¹ | Full¹ | File | File | Full¹ |
| Allocation drivers | Full¹ | Full¹ | File | File | File | File |
| Currency rates | Full | Full | Full | Full | Full | Full |
| Segment values | File | File | File | File | File | File |
| CO-PA by valuation | File | File | File | File | File | File |

## Mid-Market and Cloud Finance Systems

| Dataset | Business Central | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- |
| Entities | Full | Full | Full | Full | Full | Full |
| Fiscal calendar | Full | Full | Full | Full | Full | Full |
| Chart of accounts | Full | Full | Full | Full | Full | Full |
| Departments | Full | Full | Full¹ | Full | Full | Full |
| Profit centers | File | File | File | File | File | File |
| Products | Full | Full | Full¹ | Full | Full¹ | Full |
| Customers | Full | Full | Full¹ | Full | Full¹ | Full |
| General ledger | Full | Full | Full | Full | Full | Full |
| Trial balance | Full | Full | Full | Full | Full | Full |
| Sales lines | Full¹ | Full¹ | Full¹ | Full¹ | Full¹ | Full |
| Pipeline | File | File | File | File | File | File |
| Inventory balances | File | File | Full¹ | File | File | Full¹ |
| Budget | Full¹ | Full¹ | Full¹ | Full¹ | File | Full¹ |
| Allocation drivers | Full¹ | Full¹ | File | File | Full¹ | Full |
| Currency rates | Full | Full | Full¹ | File | Full | Full¹ |
| Segment values | File | File | File | File | Full¹ | Full |
| CO-PA by valuation | File | File | File | File | File | File |

## CRM, Consolidation, and Planning Sources

| Dataset | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Entities | File | File | File |
| Fiscal calendar | File | File | File |
| Chart of accounts | File | File | File |
| Departments | File | File | File |
| Profit centers | File | File | File |
| Products | Full¹ | File | File |
| Customers | Full¹ | File | File |
| General ledger | File | File | File |
| Trial balance | File | File | File |
| Sales lines | File | File | File |
| Pipeline | Full¹ | File | File |
| Inventory balances | File | File | File |
| Budget | File | Full | Full |
| Allocation drivers | File | File | File |
| Currency rates | File | File | File |
| Segment values | File | File | File |
| CO-PA by valuation | File | File | File |

## Notes by System

- **Salesforce** is a CRM source. It supplies customers, products, and the sales pipeline, never the ledger.
- **OneStream** is a results source. It supplies the budget dataset only, landing your consolidated results so Data Foundation can reconcile the group P&L to them.
- **Anaplan** is a plan source. It supplies the budget dataset only, from a Budget, Forecast, or Consolidated plan.
- **SAP S/4HANA and SAP ECC** read the same master data. ECC reads its ledger from financial accounting and controlling line items, and its totals from the general ledger totals tables. Profit centers are read when the system holds them. Sales lines are billing documents, not CO-PA.
- **CO-PA by valuation** isn't read directly from any system. Add it as a file.
- **Workday** has no direct journal or balance service. Data Foundation gives you the reports to build and reads them. Segment values (worktags), customers, products, sales lines, and headcount drivers come from optional reports. Budgets stay files.
- **Xero** doesn't supply currency rates. Add them as a file if your entities use more than one currency.
- **QuickBooks Online** reads departments, customers, products, currency rates, budgets, inventory, and sales lines when the company file holds them.
- **NetSuite** reads custom segments as segment values. Currency rates and inventory are read when the account offers them, and budgets when the account uses NetSuite Budgets and the role can read them.

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
  - [Sage Intacct](/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/guides/connections/anaplan/#anaplan-as-a-data-foundation-source)
