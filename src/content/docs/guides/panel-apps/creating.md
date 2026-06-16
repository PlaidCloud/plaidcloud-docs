---
title: Creating a Panel App
description: Publish a server-side HoloViz Panel app from a git repository, or a static WASM app from a file, on the My Panel Apps screen in PlaidCloud.
sidebar:
  order: 2
---

Open **My Panel Apps**. The toolbar offers two ways to publish, one per [runtime](/guides/panel-apps/):

- **New Server App** — build and run an app from a git repository.
- **Add WASM App** — publish a static, in-browser app from a file.

## Creating a Server App

A server app is built from a git repository and served at `https://<your-tenant-host>/serve/<slug>/`.

1. Click **New Server App** to open the **Publish Server Panel App** dialog.
2. Enter an **App Name** — the display name shown in the list.
3. Enter a **URL Slug**. The slug is both the app's URL and its internal name, so it must be a valid DNS label: lowercase letters, digits, and hyphens, starting with a letter, 40 characters or fewer (for example, `sales-dashboard`). The dialog checks this before you publish.
4. Pick the **Git Connection** that holds your app's repository, then the **Branch**, then the **Entry Point** — the `.py` file Panel should serve.
5. Set the **CPU** and **Memory** the app's container should request.

   > Fewer resources (lower CPU / memory) let the app schedule and cold-start faster.

6. Set **Idle (minutes)** — how long the app stays warm with no traffic before it scales back to zero. The default is 30 minutes.
7. Optionally tick **Public** to allow unauthenticated access, add **Allowed Origins** (comma-separated; defaults to this tenant), and a **Memo**.
8. Click **Publish**.

After you publish, the app **builds** — its **Status** shows in the list and updates automatically. See [Using a Panel App](/guides/panel-apps/using/) for what the statuses mean and how to open the app once it is ready.

> The app's URL works only once its build status is **Ready**, and the first request after it has been idle spins it up (~15 seconds).

## Creating a WASM App

A WASM app runs in the browser from a pre-built HTML file.

1. Click **Add WASM App** to open the **Publish Serverless Panel App** dialog.
2. Enter an **App Name** and **Version**.
3. Choose the **App HTML Location** — the HTML file in a document account.
4. Enter an **App URL Slug** and an optional **Memo**.
5. Click **Publish**. A WASM app has no build step and is served immediately.
