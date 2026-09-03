---
title: Connections
description: Set up and manage PlaidCloud connections — saved configurations that let workflows reach external databases, cloud storage, ERPs, and REST APIs.
---

A **connection** is a saved configuration that lets PlaidCloud reach an external system — a database, cloud storage account, ERP, or REST API. Workflow steps that need to read from or write to that system reference the connection, so credentials and endpoint details live in one place.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="Many workflow steps reference one saved connection, which holds the credentials and endpoint in a single place and reaches the external system — a database, cloud storage, ERP, or REST API." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">workflow steps</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Import step</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Export step</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Lookup step</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Connection</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">credentials + endpoint, once</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">external system</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">DB · storage · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Configure the connection once; every step that reads or writes the external system points at it, so credentials and endpoint details aren't duplicated across steps.</figcaption>
</figure>

## Guides

- [Create and Manage a Connection](/guides/connections/create-connection/) — create, edit, test, and control access to a connection, and configure it per environment.
- [Use an External Lakehouse](/guides/connections/external-lakehouse/) — store a project's data in your own Snowflake or Databricks lakehouse, so workflows read and write directly in your warehouse.
- [PlaidCloud Git Connection](/guides/connections/plaidcloud-git/) — connect to your workspace's own managed Git server with no server URL or credentials, and automate Panel app builds from it.
- [Clone a Connection](/guides/connections/clone-connection/) — duplicate an existing connection for a new environment or tenant.
- [Singer Sources](/guides/connections/singer-sources/) — connect to sources such as Stripe, GitHub, Slack, and BigQuery with Singer taps, then import their data into project tables.
- [Connect to NetSuite](/guides/connections/netsuite/) — set up a NetSuite connection and pull financial and operational data with SuiteQL.
- [Import NetSuite Financials](/guides/connections/import-netsuite-financials/) — pull balances, GL detail, and master data with the canned NetSuite import steps, no SuiteQL to write.
- [Post a NetSuite Journal Entry](/guides/connections/post-netsuite-journal-entries/) — map header and line tables, preview, and post journal entries to NetSuite.
- [Connect to Acumatica](/guides/connections/acumatica/) — set up an Acumatica connection, import entities, and post journal transactions, invoices, bills, and payments.
- [Connect to Business Central](/guides/connections/business-central/) — set up a Business Central connection with Azure AD, import OData entities, and post general journal lines.
- [Connect to Dynamics 365 Finance & Operations](/guides/connections/dynamics-365-fo/) — set up a D365 F&O connection with Azure AD, import OData/DMF entities, and post journal entries.
- [Connect to Oracle Fusion](/guides/connections/oracle-fusion/) — set up an Oracle Fusion connection, import GL balances and journal batches, and post journals through FBDI.
- [Connect to Workday Financials](/guides/connections/workday-financials/) — set up a Workday Financials connection with an Integration System User, import a RaaS report, and post journal entries.
- [Connect to SAP S/4HANA Cloud](/guides/connections/s4hana-cloud/) — set up a direct S/4HANA Cloud connection with OAuth2, import trial balance and journal entry items, and post journal entries over SOAP.
- [Connect to Sage Intacct](/guides/connections/sage-intacct/) — set up a Sage Intacct connection and pull financial and accounting data.
- [Connect to Xero](/guides/connections/xero/) — authorize a Xero organisation in one click, import Accounting API entities, and post manual journals, invoices, bills, payments, and credit notes.
- [Extract from HFM / FCCS (Ad-hoc)](/guides/connections/hfm-fccs/) — connect to Oracle FCCS and self-serve a data slice with a point-of-view picker, no ticket to the HFM team.
- [Connect to QuickBooks](/guides/connections/quickbooks/) — prerequisites and current limitations for QuickBooks Online.
- [Review the Posting Register](/guides/connections/posting-register/) — a tenant-level console for finance and accounting to review ERP postings across every project and connection they can see.

## Related

- [Connectors reference](/reference/connectors/) — the full catalog of supported systems and the fields each one needs.
