---
title: Using a Panel App
description: Track build status, open, rebuild, lock, view logs and usage metrics for, edit, and remove published HoloViz Panel apps from the My Panel Apps screen in PlaidCloud.
sidebar:
  order: 3
---

Every published app appears on the **My Panel Apps** screen with its **Runtime**, **Status**, **Slug**, and timestamps. The leftmost column opens the app; the remaining row icons let you lock it against accidental changes, edit it, remove it, and — for server apps — rebuild it, view its logs, and view usage metrics. The open icon reflects the app's runtime, so WASM and server apps are easy to tell apart at a glance.

## Build Status (Server Apps)

A server app's **Status** column tracks its build, and the list refreshes on its own while a build is in progress:

- **Building…** — PlaidCloud is building your repository into a container. The app has no URL yet.
- **Ready** — the build succeeded. The app's URL is live and the **Open** icon appears on its row.
- **Failed** — the build did not complete. Check the entry point and branch, then edit the app to republish.

WASM apps have no build step and are available as soon as they are published.

## Rebuilding a Server App

Click the **Rebuild** icon on a server app's row to rebuild and redeploy it without changing its settings. The app's status returns to **Building…** while PlaidCloud builds the same branch and entry point again, then switches back to **Ready** when the new build is live.

Use **Rebuild** after dependency changes, base-image updates, or a transient failed build. Editing and saving a server app also rebuilds it, but a rebuild does not require opening the edit form.

## Locking an App

Click the **lock** icon on an app's row to protect it from accidental changes. While an app is locked:

- **Edit**, **Remove**, and **Rebuild** refuse to run and tell you the app is locked.
- A **push to a server app's branch does not rebuild it** — the automatic rebuild is skipped until you unlock the app. No build runs for a skipped push, so nothing new appears in the app's Build logs; push again (or use **Rebuild**) after unlocking to pick the change up.
- Opening the app, viewing its logs, and viewing its usage metrics all keep working — the lock only stops changes, never viewers.

Click the icon again to unlock. The icon shows the app's current state: closed when locked, open when not.

The lock is a guard against accidents — a mistaken edit, an unintended delete, or a git push landing on an app you're demoing — just like the lock on workflows and workflow steps. It is **not** a security control: anyone who can edit panel apps can also unlock them.

> Two things the lock does not cover: a **build already in progress** when you lock still finishes and goes live, and a **WASM** app's files live in its document account, so replacing those files changes the running app without touching the locked record.

## Opening an App

Click the **Open** icon at the start of a ready app's row to launch it in a new tab.

- A server app is served at `https://<your-tenant-host>/serve/<slug>/`.
- The **Open** icon appears only once a server app is **Ready**.

A server app scales to zero when idle to save resources, so the first open after an idle period has to spin it up. While that happens you see a **PlaidCloud loading screen** — your app's name, a progress indicator, and your workspace details — instead of a blank tab. The app appears on its own as soon as it is ready (usually a few seconds, up to about a minute on a cold start), and then responds normally until it next goes idle.

> If an app can't start, the loading screen turns into a **"This app didn't start"** message with a **Try Again** button rather than spinning forever. If that keeps happening, edit the app to check its entry point and branch and republish, or contact your PlaidCloud administrator.

### Appearance

Server Panel apps use PlaidCloud's modern **Fast** design by default, but the app's **Design** setting can switch it back to Panel's **Default** styling when existing CSS depends on it. The theme — light, dark, or a light/dark switch viewers can flip — is something you set in your app's template. See [Set the Theme](/guides/panel-apps/creating/#set-the-theme-light-dark-or-a-toggle) in the Creating guide for the patterns. If your app's tables or custom styling are built for a light background, keep it pinned to light.

## Viewing Logs (Server Apps)

Click the **View Logs** icon on a server app's row to open its log viewer. (WASM apps run entirely in the browser and have no server logs, so the icon appears only on server-app rows.)

The viewer has two tabs:

- **Runtime** (shown first) — the running app's own output: anything it logs, anything it prints, and any uncaught errors. These are kept even after the app scales to zero, so you can review what an earlier session did.
- **Build** — the output from building the app's container. Use it to see *why* a build shows **Failed** — for example, a dependency that wouldn't install.

Each tab gives you **Info / Warn / Error** filters, a **Logs since** time range (from the last hour up to 30 days, or all), a **Refresh** button, and **Auto-refresh** to poll for new entries — handy while you watch a live app or a build in progress. The newest entries are listed first.

> If the build output couldn't be captured, the Build tab shows a short note explaining why rather than appearing empty.

### Reading a Full Log Message

The log table trims long lines to keep the list readable. Select a log row to open a **detail pane** alongside the table that shows the entry's full message. This is the easiest way to read something that's too long for the table — a long error message or a complete stack trace — without it being cut off.

### Copying Log Lines

You can select several log rows at once and click **Copy** to put them on your clipboard. This is handy for pasting logs into a chat with an AI assistant when you're debugging your app, or into a message to your team or PlaidCloud support.

### Who Triggered a Log Line

When your app signs viewers in, each log line is tagged with the **user** whose session produced it, so you can tell which viewer hit a particular error or warning. Tagging is best-effort — some framework and startup lines run before any viewer is involved and may not show a user.

## Usage Metrics (Server Apps)

Click the **Usage Metrics** icon on a server app's row — next to **View Logs** — to see how the app is being used. The view summarizes:

- **Unique users** — how many distinct people have opened the app.
- **Sessions** — how many times it has been opened.
- **Average and median session duration** — roughly how long a visit lasts.
- **Last used** — when the app was most recently opened.

Below the summary you get a breakdown **per user** and **per day**, so you can see who is using the app and how usage trends over time.

> Durations are approximate. Server apps idle and scale down when no one is using them, so a session's exact end isn't always observed — read the duration figures as a guide, not an exact measurement.

## Editing an App

Click the **pencil** icon on an app's row to edit it. The edit form matches the app's runtime.

For a **server** app you can change the name, slug, branch, entry point, CPU, memory, design, idle window, public flag, embedded-serving domains, and memo. The **Git Connection** is fixed once the app is created and is shown read-only. Saving rebuilds the app — its status returns to **Building…** until the new build is ready.

## Removing an App

Click the **minus** icon on an app's row and confirm. Removing a server app tears down its build and deployment; removing a WASM app unpublishes the static file. The app's URL stops working immediately.
