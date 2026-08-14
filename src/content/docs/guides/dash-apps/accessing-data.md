---
title: Reading Data and the Signed-In User in a Dash App
description: Connect a Dash app to PlaidCloud as the person viewing it — read project data, and use the viewer's identity for per-user behavior and row-level security.
sidebar:
  order: 4
---

A Dash app can read your PlaidCloud data — and it does so **as the person viewing it**, exactly like a server Panel app. When someone opens the app, PlaidCloud signs them in with the same single sign-on the rest of the platform uses, and every call your app makes runs with **that viewer's own permissions**. There is no shared service account, and the app can never see data the viewer couldn't see themselves.

The helpers live in `plaidcloud_dash`, part of the Dash base image:

```python
from plaidcloud_dash import current_user, get_connection
```

## Connect to PlaidCloud

Call `get_connection()` from inside a Dash callback, naming the project whose data you want to read:

```python
from plaidcloud_dash import get_connection

conn = get_connection(project_id="<your-project-id>")
```

That's all the setup you need. You do **not** supply a token, username, or password — `get_connection()` authenticates as the signed-in viewer automatically, using the access token from their current session. Find your project's id in the project's URL or its settings page.

> **Call it from inside a callback.** `get_connection()` reads the viewer's token from the current request's Flask session, which is only available while a callback is handling that viewer's request. If you push a blocking call onto a background thread, a raw thread pool won't carry the session — read the token inside the callback and pass it in explicitly instead. Calling `get_connection()` outside a request (or with authentication disabled) raises a `RuntimeError` rather than silently returning a connection with no identity behind it.

> **Name your project in code.** There is no project setting in the publish dialog — a Dash app reads whichever project you name in `get_connection(project_id=...)`. (To read from more than one project, open a connection per project.)

### Read a Table

With a connection, pull a table into a pandas DataFrame by name:

```python
df = conn.get_dataframe("Sales Ledger")
```

Because the connection is the viewer, this returns only the rows the viewer is allowed to see, and raises a permission error if they have no access to the project at all.

> **Read tables by name, not by writing SQL.** On a project where an administrator has turned on [Row Access](/administration/access/managing-security-groups-and-assignments/#row-access-and-queries-you-write-yourself), reading by name applies each viewer's row grants, while a query your app composes itself is declined for anyone who is not a project Architect — there is no single table for the grants to filter. Reading by name keeps your app working either way.

## Identify the Viewer

To tailor what the app shows to **who is looking at it** — a personalized greeting, hiding a tab, or row-level security — call `current_user()`:

```python
from plaidcloud_dash import current_user

viewer = current_user()  # the viewer's identifier
```

`current_user()` returns the signed-in viewer's identifier — their username, falling back to their email and then their account ID if no username claim is present — taken from their verified sign-in, so you can trust it as their identity. It never raises; called with authentication disabled or outside a request, it returns an empty string.

### Row-Level Security

Combine the two: read the viewer, then filter every query by them. For example, to show each regional manager only their own region:

```python
from dash import Input, Output
from plaidcloud_dash import current_user, get_connection


@app.callback(Output("sales-table", "children"), Input("load-btn", "n_clicks"))
def _load_my_region(n_clicks):
    viewer = current_user()
    conn = get_connection(project_id="<your-project-id>")

    sales = conn.get_dataframe("Regional Sales")
    mine = sales[sales["manager_email"] == viewer]

    return mine.to_dict("records")
```

Because the connection already enforces the viewer's project permissions, this filtering is *additional* shaping on top of what they're allowed to see — not a substitute for PlaidCloud's own access control.

## Public Apps

If you published with **Allow Public Access**, the app serves without a sign-in, so there is no viewer to act as — `current_user()` returns an empty string and `get_connection()` has no session token to authenticate with, so it raises. Keep public apps to data that's safe for anyone, or leave public access off so viewers sign in and the per-user model above applies.
