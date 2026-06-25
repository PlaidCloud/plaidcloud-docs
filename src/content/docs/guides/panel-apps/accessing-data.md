---
title: Reading Data and the Signed-In User
description: Connect a server-side Panel app to PlaidCloud as the person viewing it — read project data, and use the viewer's identity for per-user behavior and row-level security.
sidebar:
  order: 4
---

A server Panel app can read your PlaidCloud data — and it does so **as the person viewing it**. When someone opens the app, PlaidCloud signs them in with the same single sign-on the rest of the platform uses, and every call your app makes runs with **that viewer's own permissions**. There is no shared service account, and the app can never see data the viewer couldn't see themselves.

This applies to **Server** apps only. WASM apps run entirely in the browser and have no server-side connection.

## Connect to PlaidCloud

Use `PlaidConnection`, naming the project whose data you want to read:

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection(project_id="<your-project-id>")
```

That's all the setup you need. You do **not** supply a token, username, or password — the connection authenticates as the signed-in viewer automatically. Find your project's id in the project's URL or its settings page.

> **Name your project in code.** There is no project setting in the publish dialog — a panel app reads whichever project you name in `PlaidConnection(project_id=...)`. A bare `PlaidConnection()` with no project will fail when it tries to read data; always pass `project_id`. (To read from more than one project, open a connection per project.)

### Read a Table

With a connection, pull a table into a pandas DataFrame by name:

```python
df = conn.get_dataframe("Sales Ledger")
```

Because the connection is the viewer, this returns only the rows the viewer is allowed to see, and raises a permission error if they have no access to the project at all.

## Identify the Viewer

To tailor what the app shows to **who is looking at it** — a personalized greeting, hiding a tab, or row-level security — read the signed-in user from Panel:

```python
import panel as pn

viewer = pn.state.user          # the viewer's email address
token  = pn.state.access_token  # their JWT, if you need claims or group membership
```

`pn.state.user` is the viewer's email, taken from their verified sign-in — you can trust it as their identity. `pn.state.access_token` is their raw access token, useful if you need to decode group or role claims for finer-grained rules.

### Row-Level Security

Combine the two: read the viewer, then filter every query by them. For example, to show each regional manager only their own region:

```python
import panel as pn
from plaidcloud.utilities.connect import PlaidConnection

pn.extension()

viewer = pn.state.user
conn = PlaidConnection(project_id="<your-project-id>")

sales = conn.get_dataframe("Regional Sales")
mine = sales[sales["manager_email"] == viewer]

pn.Column(
    f"# Sales for {viewer}",
    pn.pane.DataFrame(mine, index=False),
).servable()
```

Because the connection already enforces the viewer's project permissions, this filtering is *additional* shaping on top of what they're allowed to see — not a substitute for PlaidCloud's own access control.

> **Make data calls from the app's main flow.** The signed-in viewer is available while your app's code runs for their session (which is where `.servable()` work happens). If you push a blocking call onto a background thread, use `asyncio.to_thread` — a raw thread pool won't carry the session's identity, and the connection will fail loudly rather than read the wrong data.

## Public Apps

If you published with **Allow Public Access**, the app serves without a sign-in, so there is no viewer to act as — `pn.state.user` is empty and a `PlaidConnection()` has no one to authenticate. Keep public apps to data that's safe for anyone, or leave public access off so viewers sign in and the per-user model above applies.
