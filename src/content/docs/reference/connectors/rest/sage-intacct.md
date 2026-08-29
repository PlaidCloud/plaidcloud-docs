---
title: Sage Intacct REST Connector
description: Set up a Sage Intacct REST API connection in PlaidCloud to integrate financial and accounting data into your workflows.
sidebar:
  order: 1
---

## API Documentation

The Sage Intacct REST API documentation is available at the [Sage Developer site](https://developer.sage.com/intacct/docs/1/sage-intacct-rest-api/get-started/quick-start).


## Security Requirements

PlaidCloud provides a dedicated **Intacct** connection in the REST connection family (listed as **REST - Intacct**). It authenticates with OAuth2 client credentials against the Intacct REST API: the Sage Intacct **Web Services** Sender ID/Sender password pair are entered as the connection's **Client ID** and **Client Secret**, plus a Web Service User Username and a Company ID. The sender credentials must be enabled for your company by Sage support; the Web Services user must have permissions for every Intacct object the connector will read.

Treat the Client ID and Client Secret as secrets — store them only via the **Credentials** area in PlaidCloud and reference them from the connection.


## Obtain Credentials

1. Open the Sage Intacct **Company Setup** area
2. Enable Web Services for the Sender ID provided by Sage
3. Create or select a Web Services user for PlaidCloud
4. Grant the user permissions on every object you intend to query
5. Record the Company ID, Web Service User Username, Sender ID, and Sender password


## Create Sage Intacct Connector

1. Go to **Tools > Connections** and click `Add Connection`
2. Under **REST**, select **Intacct** (listed as **REST - Intacct**)
3. Enter:
    * **Connection Name** — friendly name shown in workflow steps
    * **Client ID** — your Intacct Sender ID
    * **Client Secret** — your Intacct Sender password
    * **Web Service User Username** — the Web Services user login
    * **Company ID** — the Intacct company you're connecting to
4. Click `Test` to validate the credentials
5. Click `Save`


## Use in Workflow Steps

The same connection serves both reading from and posting to Intacct. It's selectable from:

* [Import Sage AP](../../../workflow-steps/sage-intacct/import-sage-ap/) — AP bill headers
* [Import Sage AP Lines](../../../workflow-steps/sage-intacct/import-sage-ap-lines/) — AP bill line detail
* [Import Sage Intacct Query](../../../workflow-steps/sage-intacct/import-intacct-query/) — generic query against any Intacct object
* [Import Intacct Entity](../../../workflow-steps/sage-intacct/import-intacct-entity/) — GL detail, balances, entries, and dimension masters, with automatic pagination
* [Intacct: Post Journal Entry](../../../workflow-steps/sage-intacct/export-to-sage/) — post journal entries
