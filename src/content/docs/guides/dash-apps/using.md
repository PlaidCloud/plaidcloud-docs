---
title: Using a Dash App
description: Track build status, open, rebuild, lock, view logs, edit, and remove published Plotly Dash apps from the My Panel Apps screen in PlaidCloud.
sidebar:
  order: 3
---

Dash apps appear in the same **My Panel Apps** screen as your WASM and server Panel apps, with **Dash** shown in the **Runtime** column and their own icon so they're easy to tell apart. Everything on this page mirrors [Using a Panel App](/guides/panel-apps/using/) for a server app, with one exception called out below: Dash apps don't yet get **Usage Metrics**.

## Build Status

A Dash app's **Status** column tracks its build, and the list refreshes on its own while a build is in progress:

- **Building…** — PlaidCloud is building your repository into a container. The app has no URL yet.
- **Ready** — the build succeeded. The app's URL is live and the **Open** icon appears on its row.
- **Failed** — the build did not complete. Check the entry point and branch, then edit the app to republish.

## Rebuilding a Dash App

Click the **Rebuild** icon on a Dash app's row to rebuild and redeploy it without changing its settings. The app's status returns to **Building…** while PlaidCloud builds the same branch and entry point again, then switches back to **Ready** when the new build is live.

Use **Rebuild** after dependency changes, base-image updates, or a transient failed build. Editing and saving a Dash app also rebuilds it, but a rebuild does not require opening the edit form.

## Locking an App

Click the **lock** icon on an app's row to protect it from accidental changes. While a Dash app is locked:

- **Edit**, **Remove**, and **Rebuild** refuse to run and tell you the app is locked.
- **A push to the app's branch does not rebuild it** — the automatic rebuild is skipped until you unlock the app. Push again (or use **Rebuild**) after unlocking to pick the change up.
- Opening the app and viewing its logs both keep working — the lock only stops changes, never viewers.

Click the icon again to unlock. The icon shows the app's current state: closed when locked, open when not. The lock is a guard against accidents, not a security control — anyone who can edit Dash apps can also unlock them.

## Opening a Dash App

Click the **Open** icon at the start of a ready app's row to launch it in a new tab, at `https://<your-tenant-host>/serve/<slug>/`. The icon appears only once the app is **Ready**.

A Dash app scales to zero when idle to save resources, so the first open after an idle period has to spin it up. While that happens you see a **PlaidCloud loading screen** instead of a blank tab, and the app appears on its own once it's ready. If an app can't start, the loading screen turns into a **"This app didn't start"** message with a **Try Again** button; if that keeps happening, edit the app to check its entry point and branch and republish.

> **A `dcc.Interval` (or any other always-on polling) defeats scale-to-zero while its tab stays open.** Scale-to-zero relies on the app going quiet — no requests in flight — once nobody is actively using it. A component that keeps making requests on a timer, such as `dcc.Interval`, holds the app awake for as long as that tab is open, even if the person looking at it has stepped away. If you want an app to scale down between visits, avoid always-on polling, or stop the interval once the page has been idle for a while.

## Viewing Logs

Click the **View Logs** icon on a Dash app's row to open its log viewer, with the same **Runtime** and **Build** tabs, filters, time range, and detail pane a server Panel app has — see [Viewing Logs](/guides/panel-apps/using/#viewing-logs-server-apps) for the full mechanics. Each runtime log line is tagged with the **user** whose session produced it, the same way a server Panel app's are.

**Usage Metrics are not available for Dash apps in this release** — the **Usage Metrics** icon that appears on a server Panel app's row doesn't appear for Dash apps, so there's no unique-users/session breakdown to check yet.

## Editing an App

Click the **pencil** icon on a Dash app's row to edit it. You can change the name, slug, branch, entry point, CPU, memory, idle window, public flag, embedded-serving domains, and memo. The **Git Connection** is fixed once the app is created and is shown read-only. There is no **Design** field to edit — that setting is Panel-specific. Saving rebuilds the app — its status returns to **Building…** until the new build is ready.

## Removing an App

Click the **minus** icon on a Dash app's row and confirm. Removing it tears down its build and deployment, and the app's URL stops working immediately.
