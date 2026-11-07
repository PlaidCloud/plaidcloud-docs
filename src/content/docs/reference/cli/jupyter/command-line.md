---
title: Command Line
description: Use the PlaidCloud command line interface to automate tasks, run scripts, and interact with PlaidCloud resources via terminal.
sidebar:
  order: 2
---

PlaidCloud has a REST API that any application able to send HTTP requests can use. To make things easier, the `plaidcloud-rpc` Python package handles the connection and request details for you.

:::caution[JSON-RPC is deprecated]
JSON-RPC is deprecated and will be removed in a later release. Use `plaidcloud-rpc` 1.25.0 or later, which sends your calls to the REST API, and write new integrations against the REST API. See [JSON-RPC Is Deprecated](#json-rpc-is-deprecated).
:::


## Required Installation

From a terminal run the following command:

```bash
pip install "plaidcloud-rpc>=1.25.0"
```


## Using the SimpleRPC Object to Make a Request

To make a request using the `plaidcloud-rpc` package use the `SimpleRPC` object.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC

auth_token = "Your PlaidCloud OAuth token"  # See Obtaining an OAuth Token below
endpoint_uri = "https://<your-workspace>.plaid.cloud/json-rpc/"
rpc = SimpleRPC(auth_token, endpoint_uri)
```

Once you have the `SimpleRPC` object instantiated you can then issue requests to PlaidCloud. This example requests the metadata for a table.

```python
table = rpc.analyze.table.table(
            project_id=project_id,
            table_id=table_id
        )
```

`SimpleRPC` sends each call to the REST API at `/rest/v1/` on your workspace's host, with the same token. A call the REST API doesn't cover yet, or a call to a workspace still on an older release, uses JSON-RPC instead, so the same code works either way. A failed call raises `RPCError` in both cases.


## Calling the REST API Directly

`call_rest` sends a request to any REST API endpoint with the same token, TLS settings, and retries as `SimpleRPC`. Give it the HTTP method, the path under `/rest/v1/`, and optionally `params` for the query string and `body` for a JSON request body.

```python
dimensions = rpc.call_rest(
    'GET',
    'analyze/dimension/dimensions',
    params={'project_id': project_id},
)
```

It returns the decoded JSON response, or `None` when the response has no body. Any response other than a success raises `RPCError`, with the HTTP status as its `code`.


## JSON-RPC Is Deprecated

JSON-RPC is deprecated and will be removed in a later release. Versions of `plaidcloud-rpc` before 1.25.0 send every call over JSON-RPC, so they stop working when it's removed. Upgrade to 1.25.0 or later; your `SimpleRPC` code doesn't need to change. Write new integrations against the REST API.


## What APIs Are Available?

There are many APIs available for use that control nearly every aspect of PlaidCloud. The interactive API reference is served per-tenant inside each PlaidCloud workspace — open your workspace and navigate to the API documentation menu to see the live endpoint catalog.


## Obtaining an OAuth Token

See [OAuth setup](/reference/cli/jupyter/oauth-setup/) for more information on obtaining an OAuth token and how to configure the system for automated auth.
