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
* **Send Test Request** / **Copy as curl** / **Import from curl** — fire the request and inspect the response inline; copy an equivalent curl command (secrets masked); or paste a curl command to fill the method, URL, headers, and body.
* **Send** — `One request` (default), or `One request per table row` to fan the request out over a driver table.

When **Send** is `One request per table row`, pick a **Driver Table** (choose it with the table picker or type a name) and use `{{row.column}}` tokens in the endpoint, query, headers, or body to substitute each row's values. Optional: **Driver Filter** (a SQL `WHERE` clause), **Key Columns** (carried onto each output row), **Row Limit**, **Concurrency**, **Max req/sec** (cap on how fast requests start across all workers, independent of concurrency; 0 = no limit), and **Continue on error** (record a failed row and warn instead of aborting). **Test Row 1** fires the request for the first driver row so you can preview the fan-out before running it. Fan-out writes to the target table; it can't capture to variables.

`{{name}}` references to workflow variables (also `{{var.name}}` / `{{project_var.name}}`) are substituted in the endpoint, headers, query values, and body at run time. Only double braces are substituted, so single braces in a JSON body are left literal. Sensor/webhook runs also expose `{{trigger_sensor_id}}`, `{{trigger_sensor_type}}`, `{{trigger_fired_at}}`, and `{{trigger_payload_json}}` (empty on non-triggered runs).

**Retries** apply only to idempotent methods (GET/HEAD/OPTIONS/DELETE); a POST/PUT/PATCH is always sent once so a non-idempotent body is never re-sent. **Timeout (s)** is the per-request limit, capped at 600.

### Response Destination

* **Table** *(default)* — parse the response into the target table. Controls: Row format, Items path, Pagination mode, Mode params, Mode paths, "Dump raw JSON instead of parsing rows", Retries, Timeout.
* **Workflow variables** — fire one request and set `{prefix}_status`, `{prefix}_body`, `{prefix}_headers`, and `{prefix}_elapsed_ms`. The **Variable prefix** must be a plain identifier and can't be one of `cloud`, `project`, `model`, `date`.

## Behavior

* In variable mode the step makes a single request; pagination and row parsing don't apply.
* Captured variables are referenced downstream by name, e.g. `{my_call_status}`.
