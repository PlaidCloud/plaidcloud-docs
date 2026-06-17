---
title: Creating a Panel App
description: Publish a server-side HoloViz Panel app from a git repository (with a hello-world example), or a static WASM app from a file, in PlaidCloud.
sidebar:
  order: 2
---

Open **My Panel Apps**. The toolbar offers two ways to publish, one per [runtime](/guides/panel-apps/):

- **New Server App** — build and run an app from a git repository.
- **Add WASM App** — publish a static, in-browser app from a file.

## Creating a Server App

A server app is built from a git repository and served at `https://<your-tenant-host>/serve/<slug>/`. You point PlaidCloud at a branch of a repository; it builds the code into a container, runs `panel serve` on it, and rebuilds automatically whenever you push to that branch.

### Prepare Your App Repository

Your repository needs two things: an **entry point** — a Python file that builds a Panel app and marks it `.servable()` — and, optionally, a **`requirements.txt`** at the repository root listing any extra packages.

```
my-panel-app/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies, at the repo root
```

#### Hello World

Create `app.py`:

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello, PlaidCloud 👋\n\nYour first server-side Panel app is running.").servable()
```

That's a complete app. The `.servable()` call is what PlaidCloud serves — anything you want rendered must be marked servable (directly, or by being inside a servable layout).

#### A Slightly Richer Example

Panel apps are interactive. This one adds a slider that updates a table live:

```python
import pandas as pd
import panel as pn

pn.extension()

multiplier = pn.widgets.IntSlider(name="Multiplier", start=1, end=10, value=3)

@pn.depends(multiplier)
def times_table(m):
    df = pd.DataFrame({"n": range(1, 6)})
    df["result"] = df["n"] * m
    return pn.pane.DataFrame(df, index=False)

pn.Column(
    "# Times Table",
    multiplier,
    times_table,
).servable()
```

#### Add Dependencies

This second example imports `pandas`, which isn't part of the base image, so add a `requirements.txt` at the repository root:

```text
pandas
```

PlaidCloud installs these with `pip` when it builds the image.

> **What the platform provides — and expects.** Keep these assumptions in mind when you write your app:
>
> - **`panel` and `bokeh` are pre-installed** by the platform base image. Don't list them in `requirements.txt`, and avoid pinning an older Panel version — the live-update reconnect relies on a recent one.
> - **`requirements.txt` must be at the repository root.** A file in a subdirectory is ignored, even if your entry point lives in one.
> - **The app runs as a non-root user on a read-only filesystem.** Only `/tmp` is writable, so write any temporary files there (most libraries already honor `$TMPDIR`).
> - **Don't hardcode the port, URL prefix, or host.** PlaidCloud assigns them and injects them at deploy time — just call `.servable()`.

Your repository must be reachable through a **git connection** in PlaidCloud. If you don't have one yet, create it under **Tools > Connections** before publishing.

### Publish the App

1. Click **New Server App** to open the **Publish Server Panel App** dialog. Its settings are grouped into sections.
2. Under **Directory Settings**:
   - **App Name** — the display name shown in the list.
   - **URL Slug** — both the app's URL and its internal name, so it must be a valid DNS label: lowercase letters, digits, and hyphens, starting with a letter, 40 characters or fewer (for example, `sales-dashboard`). The dialog checks this before you publish.
   - **Memo** — an optional description.
3. Under **Git Connection and Publish Watcher**:
   - **Git Connection** — the connection that holds your app's repository.
   - **Branch** — the branch to build from. Pushes to this branch rebuild and redeploy the app automatically.
   - **Entry Point** — the `.py` file Panel should serve (your `app.py`).
4. Under **Runtime**:
   - **CPU** and **Memory** the app's container should request.

     > Fewer resources (lower CPU / memory) let the app schedule and cold-start faster.

   - **Idle (minutes)** — how long the app stays warm with no traffic before it scales back to zero. The default is 5 minutes.
   - **Allow Public Access** — tick to allow unauthenticated access; otherwise viewers must sign in to your tenant.
5. Under **Advanced (Embedded Serving)** — optional. By default the app serves only from your PlaidCloud tenant. To embed it in another site, click **Add Domain** and enter each domain allowed to load it, one per row — a host only, no scheme or path (for example, `example.com` or `app.example.com:8443`). Leave the list empty unless you're embedding the app elsewhere.
6. Click **Publish**.

After you publish, the app **builds** — its **Status** shows in the list and updates automatically. See [Using a Panel App](/guides/panel-apps/using/) for what the statuses mean and how to open the app once it is ready.

> The app's URL works only once its build status is **Ready**, and the first request after it has been idle spins it up (~15 seconds).

## Creating a WASM App

A WASM app runs in the browser from a pre-built HTML file.

1. Click **Add WASM App** to open the **Publish Serverless Panel App** dialog.
2. Enter an **App Name** and **Version**.
3. Choose the **App HTML Location** — the HTML file in a document account.
4. Enter an **App URL Slug** and an optional **Memo**.
5. Click **Publish**. A WASM app has no build step and is served immediately.
