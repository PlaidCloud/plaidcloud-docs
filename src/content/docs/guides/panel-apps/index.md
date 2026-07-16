---
title: Panel Apps
description: Build and deploy interactive HoloViz Panel data applications in PlaidCloud — either as static in-browser apps or as server-side apps built from a git repository.
sidebar:
  label: Panel Apps
---

Panel Apps let you publish interactive [HoloViz Panel](https://panel.holoviz.org/) applications — parameterized inputs, live charts, and embedded data tables — directly from PlaidCloud. You manage them from the **My Panel Apps** screen, which lists every app alongside its runtime, build status, and URL.

There are two runtimes, shown in the **Runtime** column:

- **WASM** — a static app that runs entirely in the browser (Pyodide). You publish a pre-built HTML file from a document account. There is no server process and nothing to scale; it is served immediately.
- **Server** — an app built from a git repository and run server-side. On publish, PlaidCloud builds your repository into a container that idles at zero replicas, wakes on the first request to its URL, serves (including live updates), and scales back to zero when idle. This is the right choice for apps that need a Python runtime, server-side compute, or libraries that can't run in the browser.

## Choosing a Runtime

| | WASM | Server |
|---|---|---|
| Source | A published HTML file | A git repository (connection, branch, entry point) |
| Runs | In the browser | Server-side, scale-to-zero |
| Best for | Lightweight, self-contained dashboards | Apps needing server compute or full Python libraries |
| Cold start | None | First request spins the app up (~15 seconds) |

## Next Steps

- [Deploy a Panel App From PlaidCloud Git](/guides/panel-apps/deploy-from-git/) — the complete path from repository to a served app, using a managed no-credentials connection.
- [Creating a Panel App](/guides/panel-apps/creating/) — publish a server app from git, or a WASM app from a file.
- [Using a Panel App](/guides/panel-apps/using/) — build status, opening the app, editing, and removing it.
