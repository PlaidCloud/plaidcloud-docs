---
title: Dash Apps
description: Build and deploy server-side Plotly Dash data applications in PlaidCloud — published from a Git repository and served with per-user authentication and scale-to-zero, at parity with server Panel apps.
sidebar:
  label: Dash Apps
---

Dash Apps let you publish interactive [Plotly Dash](https://dash.plotly.com/) applications — callbacks, charts, and data grids (`dash-ag-grid`, `dash-mantine-components`) — directly from PlaidCloud. You manage them from the **My Panel Apps** screen, alongside your Panel apps, where each row shows its runtime, build status, and URL.

## Where Dash Fits

A Dash app is hosted exactly like a **server Panel app**: you point PlaidCloud at a branch of a Git repository, it builds your code into a container, and the container idles at zero replicas, wakes on the first request, serves, and scales back to zero when idle. There is no separate "WASM" runtime for Dash — every Dash app is a server app.

Reach for a Dash app when your app is written with Plotly Dash rather than HoloViz Panel — for example, an existing Dash codebase, or a team that prefers Dash's callback model and `dash-ag-grid` / `dash-mantine-components` ecosystem. If you're starting fresh and don't already have a preference, see [Panel Apps](/guides/panel-apps/) for the alternative.

Everything a server Panel app gets, a Dash app gets too:

- **Per-user identity.** Each viewer signs in with the platform's single sign-on, and every call the app makes to read data runs as *that viewer* — the same [Reading Data and the Signed-In User](/guides/panel-apps/accessing-data/) model, using Dash's own helper API. See [Reading Data and the Signed-In User in a Dash App](/guides/dash-apps/accessing-data/).
- **Scale-to-zero.** The app idles to zero replicas after its configured idle window and wakes on the next request, with a brief PlaidCloud loading screen during a cold start — see [Using a Dash App](/guides/dash-apps/using/#opening-a-dash-app).
- **Automatic rebuilds.** Every push to the connected branch rebuilds and redeploys the app.
- **Runtime and build logs**, each tagged with the viewer whose session produced a line.

Two things a Dash app does **not** have, both by design and both matching what a Panel app also lacks:

- **No design/theming setting.** The **Design** option in the Panel publish dialog (FAST vs. Default) is a Panel-specific concern — Dash apps style themselves entirely through the components you choose (`dash-mantine-components`, custom CSS, etc.), so the publish form has no equivalent field.
- **No per-app access list.** Access is the workspace's SSO gate — anyone signed in to your tenant can open the app (or, if you enable **Allow Public Access**, anyone at all). There's no separate per-app ACL layer for either app type.

## App Contract

A Dash app's entry point (`app.py`, unless you name a different **Entry Point**) must:

```python
import os

import plaidcloud_dash as pcd
from dash import Dash

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # gunicorn's entry point targets app:server

pcd.init_auth(server, url_base_pathname=os.environ["DASH_URL_BASE_PATHNAME"])
```

- **Expose `server = app.server`.** Dash apps run under gunicorn, and PlaidCloud's launcher serves `app:server` — Dash's underlying Flask/WSGI application.
- **Don't set `requests_pathname_prefix` or `url_base_pathname` on `Dash(__name__)`.** Every Dash app is served under a mandatory URL prefix (`/serve/<slug>/`), and the platform sets it for you through the `DASH_URL_BASE_PATHNAME` environment variable — which is Dash's own native config variable, read before any constructor argument. Passing the prefix explicitly as well conflicts with Dash's own configuration and the app fails to start.
- **Keep `app.py` at the entry root your publish form points to.** An entry point in a subdirectory isn't supported yet — put your app file at the path you name in **Entry Point**.
- **Call `plaidcloud_dash.init_auth(server, url_base_pathname=...)`** before your layout and callbacks matter, so every request is gated behind per-user sign-in.

PlaidCloud runs your app under **threaded gunicorn**, so it serves concurrent viewers from one process — you don't need to do anything extra to support more than one person using the app at once.

## Choosing Between Panel and Dash

| | Panel Apps | Dash Apps |
|---|---|---|
| Framework | HoloViz Panel | Plotly Dash |
| Runtimes | WASM (in-browser) or Server | Server only |
| Identity model | Per-user SSO (server apps) | Per-user SSO |
| Scale-to-zero | Server apps only | Yes |
| Design/theming setting | Yes (FAST / Default) | No — style through your own components |
| Per-app access list | No — workspace SSO gate | No — workspace SSO gate |

## Next Steps

- [Deploy a Dash App From PlaidCloud Git](/guides/dash-apps/deploy-from-git/) — the complete path from repository to a served app, using a managed no-credentials connection.
- [Reading Data and the Signed-In User in a Dash App](/guides/dash-apps/accessing-data/) — query PlaidCloud data as the person viewing the app.
- [Using a Dash App](/guides/dash-apps/using/) — build status, opening the app, logs, and removing it.
