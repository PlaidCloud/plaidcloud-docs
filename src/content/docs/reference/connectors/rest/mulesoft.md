---
title: MuleSoft REST Connector
description: Connect PlaidCloud to a MuleSoft Anypoint gateway and attach the API definition so workflow steps can list its endpoints.
sidebar:
  order: 1
---

MuleSoft Anypoint is an API gateway: it fronts whatever services your organization has published behind it, at an address specific to your deployment. So unlike a connector built for one service, a MuleSoft connection doesn't know its own endpoints — you tell it where the API and its definition live.

## API Documentation

The API documentation for this connection is whatever documents the services your gateway fronts.

## Configuration

MuleSoft uses the same form as the [Generic REST Connection](/reference/connectors/rest/generic-rest/) — the same four tabs, the same fields, the same behavior throughout. Two matter most here:

- **Host or IP Address** — your Anypoint gateway's address. There is no default, because a MuleSoft address is specific to your deployment.
- **Authentication Type** — whichever of `None`, `Basic`, `API Key`, `Bearer Token`, or `OAuth 2.0` your gateway expects. Nothing is assumed on your behalf.

## Listing Endpoints in a Workflow

Because the gateway has no built-in endpoint list, attach your API's OpenAPI 3.x or Swagger 2.0 definition to the connection under **API Definition** — either the address it's published at, or a `.json` or `.yaml` file stored in Document. See [API Definition](/reference/connectors/rest/generic-rest/#api-definition) for the fields.

A [REST Request step](/guides/workflows/rest-request-step/) using this connection can then set **Endpoint Source** to **From the connection's API definition** and choose **Load Catalog** to pick from the API's endpoints, instead of typing each path by hand.

## Related

- [Generic REST Connection](/reference/connectors/rest/generic-rest/) — the full field reference for this form.
- [Create and Manage a Connection](/guides/connections/create-connection/)
- [REST Request Workflow Step](/guides/workflows/rest-request-step/)
