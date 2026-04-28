---
title: Searching Documents
slug: searching-documents
weight: 4.0
description: Find files across one or more PlaidCloud Document accounts using inline search with live progress, advanced filters, and reveal-in-folder.
date: 2026-04-28T00:00:00
---


## Description

The Document browser includes a live search bar that streams results as they are found. Searches run against the connected backend (S3, Azure Blob, Google Drive, OneDrive, etc.) so results reflect the current state of each account, not a stale index.

Results stream in via NDJSON with a progress counter so you can see how much of the search has completed and stop early if you've already found what you need.


## Run a Search

1. Open a Document account
2. Click in the search bar at the top of the file list
3. Type a name pattern and press Enter
4. Watch results stream into the file list with a live progress counter

While the search runs, the status line shows the number of folders scanned and matches found so far. You can keep typing or refine filters at any time.


## Advanced Filters

Click the filter icon next to the search bar to open the advanced filter form. Combine any of the following predicates:

* **Glob pattern** — e.g. `reports/2026/*.csv`
* **File kinds** — file, folder, or both
* **Extensions** — comma-separated list, e.g. `csv, xlsx, parquet`
* **Size** — minimum and/or maximum
* **Modified time** — on/after and/or on/before

Filters apply on top of the name pattern. Clear the form with the `Clear` button to start over.


## Sort, Highlight, and Reveal

* When the search finishes, results are sorted by relevance and the matched substring is highlighted in each row.
* The most recently selected match stays highlighted across re-searches so you can keep your place.
* Right-click any result and select `Reveal in Folder` to jump to the file in its containing directory.


## Native Adapters

Search uses native adapters for the backend where available, including:

* **Google Drive** — uses the Drive API directly so results match what you'd see in the Drive web UI.
* **OneDrive** — uses Microsoft Graph (app-only auth) so results respect the configured SharePoint/OneDrive scope.

For S3-compatible and other object stores, search runs as a parallel live-crawl with per-user concurrency caps so a heavy search won't starve other users.


{{< note >}}
Each user is rate-limited to a small number of concurrent searches across all accounts to keep the system responsive. If you hit the limit, the search bar reports an HTTP 429 — wait for one of your other searches to finish and try again.
{{< /note >}}
