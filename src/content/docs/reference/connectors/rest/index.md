---
title: REST Connections
description: Connect PlaidCloud to REST API services including Salesforce, NetSuite, Workday, Dynamics, and other cloud-based platforms.
---

PlaidCloud connects to REST API services using standard authentication patterns (OAuth, API keys, Basic Auth). Each provider has its own quirks in token flow, scope handling, and pagination — the dedicated connectors below encapsulate those specifics so you don't have to.

For any REST service that doesn't have a dedicated connector, PlaidCloud provides a generic REST connector configurable to most authentication and response-parsing patterns.

## CRM and Sales

- [Salesforce](/reference/connectors/rest/salesforce/)
- [Dynamics](/reference/connectors/rest/dynamics/) — Microsoft Dynamics 365

## Financial and Accounting

- [NetSuite](/reference/connectors/rest/netsuite/)
- [QuickBooks](/reference/connectors/rest/quickbooks/)
- [Sage Intacct](/reference/connectors/rest/sage-intacct/)
- [Stripe](/reference/connectors/rest/stripe/)
- [Ramp](/reference/connectors/rest/ramp/)

## HR and Payroll

- [Workday](/reference/connectors/rest/workday/)
- [Paycor](/reference/connectors/rest/paycor/)
- [Gusto](/reference/connectors/rest/gusto/)

## Integration Platforms

- [MuleSoft](/reference/connectors/rest/mulesoft/)
