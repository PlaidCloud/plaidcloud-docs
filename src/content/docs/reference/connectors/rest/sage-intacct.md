---
title: Sage Intacct REST Connector
description: Set up a Sage Intacct REST API connection in PlaidCloud to integrate financial and accounting data into your workflows.
sidebar:
  order: 1
---

## API Documentation

The Sage Intacct REST API documentation is available at the [Sage Developer site](https://developer.sage.com/intacct/docs/1/sage-intacct-rest-api/get-started/quick-start).


## Security Requirements

The connector authenticates with a Sage Intacct **Web Services** sender ID plus a user-level login. The sender credentials must be enabled for your company by Sage support; the user credentials must have permissions for every Intacct object the connector will read.

Treat sender and user credentials as secrets — store them only via the **Credentials** area in PlaidCloud and reference them from the connection.


## Obtain Credentials

1. Open the Sage Intacct **Company Setup** area
2. Enable Web Services for the sender ID provided by Sage
3. Create or select a Web Services user for PlaidCloud
4. Grant the user permissions on every object you intend to query
5. Record the company ID, user ID, user password, sender ID, and sender password


## Create REST Connector

1. Go to **Tools > Connections** and click `Add Connection`
2. Select **Sage Intacct** as the connection type
3. Enter:
    * **Connection Name** — friendly name shown in workflow steps
    * **Company ID** — the Intacct company you're connecting to
    * **User ID** and **User Password**
    * **Sender ID** and **Sender Password**
    * **Entity** — optional, for multi-entity tenants
4. Click `Test` to validate the credentials
5. Click `Save`


## Use in Workflow Steps

The connection is selectable from these workflow import steps:

* [Import Sage AP](../../../workflow-steps/import/import-sage-ap/) — AP bill headers
* [Import Sage AP Lines](../../../workflow-steps/import/import-sage-ap-lines/) — AP bill line detail
* [Import Sage Intacct Query](../../../workflow-steps/import/import-intacct-query/) — generic query against any Intacct object
