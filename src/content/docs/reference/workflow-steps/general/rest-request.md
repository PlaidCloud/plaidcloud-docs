---
title: REST Request
description: Call a REST API in a workflow step — import endpoints from Postman, OpenAPI, or HAR, and route the response to a table or to workflow variables.
sidebar:
  order: 6
---

## Description

The **REST Request** step calls a REST API and routes the response to a target table or to workflow variables. It supersedes the older REST-flavored steps with one unified, Postman-style step: pick an endpoint (manual, Postman, OpenAPI/Swagger, or HAR), edit headers/query/body, send a test request, and save.

For a full walkthrough, see the [REST Request step guide](/guides/workflows/rest-request-step/).

While you edit, the browser keeps a local draft for the step. If you close or reload before saving, reopening the step offers to restore that unsaved draft.

## Configuration

### Request

* **Endpoint Source** — `Manual`, `From the connection's API definition`, `Postman collection (file/URL)`, `OpenAPI / Swagger (URL/file)`, or `HAR archive (file)`. Use **Load Catalog** to list the endpoints of an imported source; picking one fills in its method, URL, headers, query parameters, and body, asking first if you have edited the request. The three file sources also offer **Paste…**, letting you supply the collection or spec directly instead of picking a file.
* **Connection** *(optional)* — a REST connection for auth and base URL; omit to call a full URL directly. The edit shortcut beside the picker opens the selected connection editor for viewing or editing.
* **Method** — `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`.
* **Endpoint** — path (with a connection) or full URL.
* **Headers** / **Query Parameters** — name/value rows with an on/off toggle.
* **Body** — request payload (JSON, form, or raw).
* **Send Test Request** / **Copy as curl** / **Import from curl** — fire the request and inspect the response inline; copy an equivalent curl command (secrets masked); or paste a curl command to fill the method, URL, headers, and body.
* **Send** — `One request` (default), or `One request per table row` to fan the request out over a driver table.

Saving outbound request changes before a successful **Send Test Request** asks for confirmation. In fan-out mode, **Test Row 1** is the successful test that clears the warning.

When **Send** is `One request per table row`, pick a **Driver Table** (choose it with the table picker or type a name) and use `{{row.column}}` tokens in the endpoint, query, headers, or body to substitute each row's values. The endpoint and body variable insert menus include the selected driver table's columns. Optional: **Driver Filter** (a SQL `WHERE` clause), **Key Columns** (carried onto each output row), **Row Limit**, **Concurrency**, **Max req/sec** (cap on how fast requests start across all workers, independent of concurrency; accepts fractions, so 0.5 sends one request every two seconds; 0 = no limit; a value over 1000 is capped at 1000 with a warning), **Add Idempotency-Key header** (send a stable per-row `Idempotency-Key` on a single No-Paging POST/PUT/PATCH so re-runs don't double-create; skipped with a warning otherwise), and **Continue on error** (record a failed row and warn instead of aborting), and **Response** (`Parsed records` by default; `Text (one row per request)` writes each response as a row with `DownloadData` and `DownloadHeaders` columns; `Raw text, errors as rows` does the same with the body exactly as the server sent it, adds a `DownloadStatus` column, and keeps an HTTP or transport error as a row, with credentials masked in the body, headers, and error text). **Test Row 1** fires the request for the first driver row so you can preview the fan-out before running it. Fan-out writes to the target table; it can't capture to variables.

Two more fan-out options for the text responses are set with an AI assistant or the REST API:

* **Poll while** (`poll_while`) — for an API that answers "still working" until a job finishes. Give a JSON path in the response, an operator (`==`, `!=`, `<`, `<=`, `>`, or `>=`; `==` by default), and a value. Each row's request is sent again while its response matches, every **poll interval** (`poll_interval_seconds`, 5 seconds by default, 1 to 600) for at most **poll max attempts** requests (`poll_max_attempts`, 60 by default, 1 to 1000); a row still matching after the last attempt fails.
* **Body text** (`body_text`) — `html` writes the visible text of an HTML page in `DownloadData` instead of its markup; `base64` writes the body's bytes exactly as the server sent them, base64-encoded, for a file or other binary response.

`{{name}}` references to workflow variables (also `{{var.name}}` / `{{project_var.name}}`) are substituted in the endpoint, headers, query values, and body at run time. Only double braces are substituted, so single braces in a JSON body are left literal. Sensor/webhook runs also expose `{{trigger_sensor_id}}`, `{{trigger_sensor_type}}`, `{{trigger_fired_at}}`, and `{{trigger_payload_json}}` (empty on non-triggered runs).

The editor highlights detected `{{...}}` tokens in the endpoint, header and query tables, and body editor.

**Retries** apply only to idempotent methods (GET/HEAD/OPTIONS/DELETE); a POST/PUT/PATCH is always sent once so a non-idempotent body is never re-sent. **Retries** accepts 0 to 100. **Timeout (s)** is the per-request limit, 1 to 600 s; test requests wait at most 300 s. See [REST Request Step](/guides/workflows/rest-request-step/) for the catalog filter, paste and drop, JSON tools, request warnings, and test results.

### Response Destination

* **Table** *(default)* — parse the response into the **Target Table** (required; tables only, not views). Controls: Row format (`Object` or `Array`; one request per table row needs `Object`), Items path, Pagination mode (`No Paging`, `Offset Paging`, `Page Number Paging`, `Next Page URL Paging`, `Cursor Paging`, or `Link Header Paging (RFC 5988)`), Mode params, Mode paths, "Dump raw JSON instead of parsing rows", Retries, Timeout. The **Table Data Selection** tab maps response fields to columns; **Inspect Source → Populate** fills it from a live response, which needs a connection and asks first before sending a method other than GET, HEAD, or OPTIONS. Summarize and Distinct aren't offered.
* **Workflow variables** — fire one request and set `{prefix}_status`, `{prefix}_body`, `{prefix}_headers`, and `{prefix}_elapsed_ms`. The **Variable prefix** must be a plain identifier and can't be one of `cloud`, `project`, `model`, `date`.

## Behavior

* In variable mode the step makes a single request; pagination and row parsing don't apply.
* Captured variables are referenced downstream by name, e.g. `{my_call_status}`.
