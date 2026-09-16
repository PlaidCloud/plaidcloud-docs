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

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 250" role="img" aria-label="The two Panel App runtimes. A WASM app is a prebuilt HTML file served straight to the browser with no server. A Server app is built from a git repository into a container that idles at zero replicas, wakes on the first request in about fifteen seconds, serves, and scales back to zero when idle." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pa-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="14" y="40" font-size="12" font-weight="700" fill="var(--sl-color-accent)">WASM</text>
  <rect x="70" y="24" width="150" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="49" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">prebuilt HTML file</text>
  <path d="M220 45 L286 45" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="288" y="24" width="164" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="370" y="43" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">browser · Pyodide</text>
  <text x="370" y="58" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">served immediately</text>
  <line x1="14" y1="96" x2="666" y2="96" stroke="var(--sl-color-gray-5)" stroke-dasharray="3 3" />
  <text x="14" y="146" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Server</text>
  <rect x="70" y="128" width="96" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="118" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">git repo</text>
  <path d="M166 149 L186 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="188" y="128" width="110" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="243" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">build container</text>
  <path d="M298 149 L318 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="320" y="128" width="120" height="42" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="380" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">idle · 0 replicas</text>
  <text x="380" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">nothing running</text>
  <path d="M440 149 L474 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <text x="457" y="140" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">1st req</text>
  <rect x="476" y="128" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="536" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">serving</text>
  <text x="536" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">wakes ~15s</text>
  <path d="M536 170 C536 212 380 212 380 174" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#pa-arrow)" />
  <text x="458" y="206" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">scales back to 0 when idle</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Two runtimes: a <strong>WASM</strong> app is a prebuilt HTML file served straight to the browser; a <strong>Server</strong> app is built from git, idles at zero, wakes on the first request (~15s), serves, and scales back to zero.</figcaption>
</figure>

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
- [Build an AI Agent Inside a Panel App](/get-started/tutorials/panel-ai-agent/) — a tutorial: give an AI agent the REST API as its tools, scoped to the viewer's own permissions.
