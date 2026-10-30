---
title: Panel Studio
description: Create, edit, preview and publish Panel apps without leaving PlaidCloud — then restore an earlier version, read the app's usage and speed, set up alerts and digests, list it in the gallery and pin it to Home.
sidebar:
  order: 3
---

Panel Studio is the editor for Panel apps inside PlaidCloud. It shows the app's files next to an editor, builds a private preview you can open, and publishes the app when you are ready. You don't need a git repository to start.

## Open Panel Studio

- On a project's **Home** board, choose **Open in Studio** on a Panel app.
- In **My Panel Apps**, choose **Studio** on an app's row.

To start a new app, choose **New Studio App**. It is the first button in the **My Panel Apps** toolbar, and it is in the **Panel Apps** box on a project's **Home** tab. To build on a table, select it on the project's **Tables** tab and choose **Create Panel App**.

## Create an App

The **New Studio App** dialog starts you from one of five places:

| Start from | You get |
|---|---|
| **Blank app** | A minimal app with an `app.py` and a `requirements.txt`. |
| **From a table** | An app built on the table you pick. |
| **From a view** | The same, built on a project view. |
| **From another Studio app** | A copy of one of your Studio apps. |
| **From the gallery** | A copy of an app your workspace has listed in the [app gallery](/guides/panel-apps/gallery/). |

Name the app, pick its **Project**, and choose **Create**. Studio opens the new app with its files listed on the left. For a table or a view, Weave's prompt to build the app's first page is ready to send. See [Creating a Panel App](/guides/panel-apps/creating/).

## Edit

Pick a file in the list to edit it in the editor. List your Python dependencies in `requirements.txt`, one package per line. They are installed when the app builds.

Choose **Ask Weave** to have Weave write or change the app for you. See [Build Panel Apps With Weave](/guides/panel-apps/build-with-weave/).

## Save, Preview and Publish

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Saving keeps a draft only you can see. Preview builds a private copy of the draft for the editor. Publish replaces the live app after you confirm." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Save</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">draft only</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Preview</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">editor only</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Publish</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">the live app</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Your edits reach viewers only when you publish.</figcaption>
</figure>

### Save

**Save** stores your changes as a draft. The live app does not change, and nobody else sees the draft.

### Preview

**Preview** builds your saved draft as a private copy and opens it. Only editors of the app can open a preview.

- A preview is removed after 24 hours without a save.
- A workspace can have up to 10 previews at a time.
- Save again and choose **Preview** to see your latest edits.

### Publish

**Publish** replaces the live app with your saved draft. It requires edit permission on the app's project, and Studio asks you to confirm first.

If someone else published a change after you opened the app, Studio reports a conflict instead of overwriting their work. Reload the app, bring your edits across, and publish again.

## Build Status and Errors

The **Build** tab shows the status of the latest build, and updates as it runs. When a build fails, the tab lists each error with its file and line number, so you can go straight to the line. Dependency problems in `requirements.txt` come with a hint about the fix.

Errors and warnings are also marked on their lines in the editor, so you see a problem where it is.

For what each status means once the app is published, see [Using a Panel App](/guides/panel-apps/using/#build-status-server-apps).

## History and Restore

The **History** tab lists every published version of the app, newest first, with its build status. Choose **Load more** to see older ones.

To go back to an earlier version, choose **Restore** on it and confirm. The restored version becomes the live app and rebuilds. Your unsaved draft is not lost: it stays in the draft and goes live on top of the restored version the next time you publish. If the app already matches that version, Studio says so and changes nothing. If someone published while you were restoring, Studio restores nothing and asks you to try again.

## Insights

The **Insights** tab shows how people use the app and how quickly it responds. Choose the last 7, 14 or 30 days.

| Section | Shows |
|---|---|
| **Views per day** | How many times the app was opened each day. |
| **Page load** | The median load time, and the time that 95 percent of loads beat, from the page loads in the period. |
| **Slowest queries** | The queries that took longest, with how often they ran and their median, slow-end and slowest times. |
| **Errors** | What went wrong in the period, by the kind of error and where in the app it happened. |

When a period holds more activity than Insights can read, it says the figures are partial. When page loads go over the app's [performance budget](/guides/panel-apps/app-kit/#performance-budgets), Insights warns you how many did and which queries were slow. Insights never shows the data a query returned or the names of the people who opened the app.

The **History** and **Insights** tabs need the app to be assigned to a project; an unassigned app shows a prompt to assign it.

## Alerts and Digests

Choose **Alerts & Digests** to set up notifications that watch a number in the app's data and tell you when it crosses a limit, or send a summary on a schedule. See [Alerts and Digests](/guides/panel-apps/alerts-and-digests/).

## List an App in the Gallery

Choose **Gallery…** in Studio. Choose **List in gallery** to list the app as a template anyone who can view its project can create their own app from, or **Take out of gallery** to remove it. The button is available for apps that belong to a project. You need edit access to the project. See [The App Gallery](/guides/panel-apps/gallery/).

## Pin to Home

Choose **Pin to Home** to add the app to the project's **Home** board, and **Unpin from Home** to remove it.

## Delete an App

Deleting a Panel app asks you to confirm first. In **My Panel Apps**, use the **minus** icon on the app's row. Unpublishing also asks you to confirm.

## Next Steps

- [Build Panel Apps With Weave](/guides/panel-apps/build-with-weave/) — describe the app and approve the exact change.
- [The Panel App Kit](/guides/panel-apps/app-kit/) — the components Studio's table and view starts use.
- [Alerts and Digests](/guides/panel-apps/alerts-and-digests/) — notify people when a number crosses a limit, or on a schedule.
- [The App Gallery](/guides/panel-apps/gallery/) — share an app as a starting point for others.
- [Using a Panel App](/guides/panel-apps/using/) — logs, usage and rebuilds after you publish.
