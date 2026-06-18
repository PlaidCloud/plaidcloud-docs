---
title: REST Request
description: Call a REST API in a workflow step — import endpoints from Postman, OpenAPI, or HAR, and route the response to a table or to workflow variables.
sidebar:
  order: 6
---

## Description

The **REST Request** step calls a REST API and routes the response to a target table or to workflow variables. It supersedes the older REST-flavored steps with one unified, Postman-style step: pick an endpoint (manual, Postman, OpenAPI/Swagger, or HAR), edit headers/query/body, send a test request, and save.

For a full walkthrough, see the [REST Request step guide](/guides/workflows/rest-request-step/).

## Configuration

### Request

* **Endpoint Source** — `Manual`, `Postman collection (file/URL)`, `OpenAPI / Swagger (URL/file)`, or `HAR archive (file)`. Use **Load Catalog** to list and pick an endpoint from an imported source.
* **Connection** *(optional)* — a REST connection for auth and base URL; omit to call a full URL directly.
* **Method** — `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`.
* **Endpoint** — path (with a connection) or full URL.
* **Headers** / **Query Parameters** — name/value rows with an on/off toggle.
* **Body** — request payload (JSON, form, or raw).
* **Send Test Request** / **Copy as curl** — fire the request and inspect the response inline, or copy an equivalent curl command (secrets masked).

`${...}` references to workflow variables are substituted in the endpoint, headers, query values, and body at run time.

### Response Destination

* **Table** *(default)* — parse the response into the target table. Controls: Row format, Items path, Pagination mode, Mode params, Mode paths, "Dump raw JSON instead of parsing rows", Retries, Timeout.
* **Workflow variables** — fire one request and set `{prefix}_status`, `{prefix}_body`, `{prefix}_headers`, and `{prefix}_elapsed_ms`. The **Variable prefix** must be a plain identifier and can't be one of `cloud`, `project`, `model`, `date`.

## Behavior

* In variable mode the step makes a single request; pagination and row parsing don't apply.
* Captured variables are referenced downstream by name, e.g. `{my_call_status}`.
