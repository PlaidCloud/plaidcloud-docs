---
title: Using a Panel App
description: Track build status, open, edit, and remove published HoloViz Panel apps from the My Panel Apps screen in PlaidCloud.
sidebar:
  order: 3
---

Every published app appears on the **My Panel Apps** screen with its **Runtime**, **Status**, **Slug**, and timestamps. The leftmost column opens the app; the pencil and minus icons edit and remove it.

## Build Status (Server Apps)

A server app's **Status** column tracks its build, and the list refreshes on its own while a build is in progress:

- **Building…** — PlaidCloud is building your repository into a container. The app has no URL yet.
- **Ready** — the build succeeded. The app's URL is live and the **Open** icon appears on its row.
- **Failed** — the build did not complete. Check the entry point and branch, then edit the app to republish.

WASM apps have no build step and are available as soon as they are published.

## Opening an App

Click the **Open** icon at the start of a ready app's row to launch it in a new tab.

- A server app is served at `https://<your-tenant-host>/serve/<slug>/`.
- The **Open** icon appears only once a server app is **Ready**.

A server app scales to zero when idle to save resources, so the first open after an idle period has to spin it up. While that happens you see a **PlaidCloud loading screen** — your app's name, a progress indicator, and your workspace details — instead of a blank tab. The app appears on its own as soon as it is ready (usually a few seconds, up to about a minute on a cold start), and then responds normally until it next goes idle.

> If an app can't start, the loading screen turns into a **"This app didn't start"** message with a **Try Again** button rather than spinning forever. If that keeps happening, edit the app to check its entry point and branch and republish, or contact your PlaidCloud administrator.

## Editing an App

Click the **pencil** icon on an app's row to edit it. The edit form matches the app's runtime.

For a **server** app you can change the name, slug, branch, entry point, CPU, memory, idle window, public flag, embedded-serving domains, and memo. The **Git Connection** is fixed once the app is created and is shown read-only. Saving rebuilds the app — its status returns to **Building…** until the new build is ready.

## Removing an App

Click the **minus** icon on an app's row and confirm. Removing a server app tears down its build and deployment; removing a WASM app unpublishes the static file. The app's URL stops working immediately.
