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
> - **The PlaidCloud client libraries (`plaidcloud-rpc`, `plaidcloud-utilities`) are pre-installed.** Import `plaidcloud.rpc` or `plaidcloud.utilities` directly — don't list them in `requirements.txt`.
> - **`requirements.txt` must be at the repository root.** A file in a subdirectory is ignored, even if your entry point lives in one.
> - **The app runs as a non-root user on a read-only filesystem.** Only `/tmp` is writable, so write any temporary files there (most libraries already honor `$TMPDIR`).
> - **Don't hardcode the port, URL prefix, or host.** PlaidCloud assigns them and injects them at deploy time — just call `.servable()`.

### Set the Theme: Light, Dark, or a Toggle

Server apps render in PlaidCloud's modern **Fast** design by default — a clean, Fluent-style look applied platform-wide. In the publish dialog, **Design** controls that platform layer:

- **FAST** — the PlaidCloud default. Use it for new apps and apps built with Fast templates.
- **Default** — Panel's default styling. Use it when an existing app's CSS or visuals break under FAST.

What you control in your app code is the **theme**: light, dark, or a switch the viewer can flip.

The theme is a property of the **template** you serve. The Fast templates — `FastListTemplate` (a single column) and `FastGridTemplate` (a responsive grid) — take two settings for it:

- **`theme`** — `"default"` for light or `"dark"`. Setting it pins the app to that theme, even if a viewer adds `?theme=dark` to the URL.
- **`theme_toggle`** — `True` shows a light/dark switch in the header; `False` hides it. It defaults to `True`. Hiding the switch doesn't fix the theme on its own — pin it with `theme` (above); set `theme_toggle=False` once you have, so viewers don't see a switch that can't change anything.

Pick the pattern that fits your app.

**Light only** — best for dense reports and financial tables, which are usually hand-styled for a light background:

```python
import panel as pn

pn.extension("tabulator")

pn.template.FastListTemplate(
    title="Sales Dashboard",
    theme="default",      # light
    theme_toggle=False,   # hide the switch
    main=[...],
).servable()
```

**Dark only:**

```python
pn.template.FastListTemplate(
    title="Ops Monitor",
    theme="dark",
    theme_toggle=False,
    main=[...],
).servable()
```

**Let the viewer choose** — defaults to light, with a switch in the header. Omit `theme` so it follows the toggle:

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **If you allow dark, make your tables dark-aware.** A `Tabulator` pinned to a light table theme (`theme="bootstrap"`), or custom CSS with hardcoded light colors like `background: #fff`, renders as an unreadable white block on a dark page. Use a table theme that follows the app — `pn.widgets.Tabulator(..., theme="fast")` — and avoid hardcoded light colors. If a report is heavily hand-styled for light, pin it to light instead (the first pattern above).

A plain app with no template — `pn.Column(...).servable()` — follows Panel's default and isn't affected by these settings; reach for a template when you want explicit control.

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

   - **Design** — choose **FAST** for PlaidCloud's modern design, or **Default** if the app's CSS expects Panel's default styling.
   - **Idle (minutes)** — how long the app stays warm with no traffic before it scales back to zero. The default is 5 minutes.
   - **Allow Public Access** — tick to allow unauthenticated access; otherwise viewers must sign in to your tenant.
5. Under **Advanced (Embedded Serving)** — optional. By default the app serves only from your PlaidCloud tenant. To embed it in another site, click **Add Domain** and enter each domain allowed to load it, one per row — a host only, no scheme or path (for example, `example.com` or `app.example.com:8443`). Leave the list empty unless you're embedding the app elsewhere.
6. Click **Publish**.

After you publish, the app **builds** — its **Status** shows in the list and updates automatically. See [Using a Panel App](/guides/panel-apps/using/) for what the statuses mean, how to open the app once it is ready, and how to trigger a rebuild without unpublishing.

> The app's URL works only once its build status is **Ready**, and the first request after it has been idle spins it up (~15 seconds).

### Advanced: Match PlaidCloud Locally

Technical users can build and test the app with the same inputs PlaidCloud uses. This is the closest local check before publishing or clicking **Rebuild**.

PlaidCloud builds from the selected git branch with this generated Dockerfile. Use the same content locally as `Dockerfile.plaidcloud-panel`:

```dockerfile
FROM us-docker.pkg.dev/plaidcloud-build/panel-base/platform-panel-base:0.5.1
USER root
COPY . /app
RUN if [ -f /app/requirements.txt ]; then pip install --no-cache-dir -r /app/requirements.txt; fi
USER 10001
```

To match the server build:

1. Check out the same branch you select in **Branch**.
2. Run the build from the repository root, so `COPY . /app` matches PlaidCloud.
3. Put optional dependencies in `requirements.txt` at the repository root.
4. Use the same entry-point path you select in **Entry Point**.

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

The deployed image does not override the base image entry point. It runs `panel serve` from environment variables injected by PlaidCloud. Test the built image with the same runtime contract:

```sh
docker run --rm \
  --cpus 0.5 \
  --memory 512m \
  -p 5006:5006 \
  -e APP_PATH=/app/app.py \
  -e PANEL_PREFIX=/serve/local \
  -e PANEL_PORT=5006 \
  -e PANEL_ORIGIN=localhost:5006 \
  -e PANEL_KEEP_ALIVE_MS=25000 \
  -e PLAID_PANEL_DESIGN=fast \
  local-panel-app:plaidcloud
```

Open `http://localhost:5006/serve/local/`.

Match the publish dialog settings when you test:

- **Entry Point** maps to `APP_PATH=/app/<entry-point>`.
- **CPU** and **Memory** map to Docker's `--cpus` and `--memory` limits.
- **Design: FAST** maps to `PLAID_PANEL_DESIGN=fast`.
- **Design: Default** means omit `PLAID_PANEL_DESIGN`.
- **Idle (minutes)** maps to the deployed scale-down window. It is not enforced by local Docker, but the app still uses the same Panel websocket keepalive and session cleanup settings.
- **Embedded Serving** domains map to `PANEL_ORIGIN`; use a space-separated list if you need to test more than one host.

If you do not need a container, you can still test the serve layer from a local Python environment. Install the same `requirements.txt`, set the platform environment variables, then run `panel serve` with the same flags the deployed image uses.

```sh
export APP_PATH=app.py
export PANEL_PREFIX=/serve/local
export PANEL_PORT=5006
export PANEL_ORIGIN=localhost:5006
export PANEL_KEEP_ALIVE_MS=25000
export PLAID_PANEL_DESIGN=fast

panel serve "$APP_PATH" \
  --address 0.0.0.0 \
  --port "$PANEL_PORT" \
  --prefix "$PANEL_PREFIX" \
  --allow-websocket-origin "$PANEL_ORIGIN" \
  --num-procs 1 \
  --keep-alive "$PANEL_KEEP_ALIVE_MS" \
  --unused-session-lifetime 15000 \
  --index "$(basename "$APP_PATH" .py)"
```

Open `http://localhost:5006/serve/local/`.

Use `PLAID_PANEL_DESIGN=fast` to match the default deployed look. To test the publish dialog's **Default** design option, leave `PLAID_PANEL_DESIGN` unset and run the same command. Keep `PANEL_PREFIX`, `PANEL_ORIGIN`, `--keep-alive`, and `--unused-session-lifetime` in place; those are part of the deployed runtime contract.

## Creating a WASM App

A WASM app runs in the browser from a pre-built HTML file.

1. Click **Add WASM App** to open the **Publish Serverless Panel App** dialog.
2. Enter an **App Name** and **Version**.
3. Choose the **App HTML Location** — the HTML file in a document account.
4. Enter an **App URL Slug** and an optional **Memo**.
5. Click **Publish**. A WASM app has no build step and is served immediately.
