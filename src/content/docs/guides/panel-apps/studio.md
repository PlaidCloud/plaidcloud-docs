---
title: Panel Studio
description: Create, edit, preview and publish Panel apps without leaving PlaidCloud — start from a blank app, a table, a view or a template, then Save, Preview and Publish.
sidebar:
  order: 3
---

Panel Studio is the editor for Panel apps inside PlaidCloud. It shows the app's files next to an editor, builds a private preview you can open, and publishes the app when you are ready. You don't need a git repository to start.

## Open Panel Studio

- On a project's **Home** board, choose **Open in Studio** on a Panel app.
- In **My Panel Apps**, choose **Open in Studio** on an app's row.

To start a new app, choose **Create app** in either place.

## Create an App

The **Create app** dialog starts you from one of four places:

| Start from | You get |
|---|---|
| **Blank** | A minimal app with an `app.py` and a `requirements.txt`. |
| **Table** | An app built on the table you pick. |
| **View** | The same, built on a project view. |
| **Template** | A ready-made app from the [Panel App Kit](/guides/panel-apps/app-kit/#start-from-a-template). |

Name the app, pick its **Project**, and choose **Create**. Studio opens the new app with its files listed on the left.

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

For what each status means once the app is published, see [Using a Panel App](/guides/panel-apps/using/#build-status-server-apps).

## Delete an App

Deleting a Panel app asks you to confirm first. In **My Panel Apps**, use the **minus** icon on the app's row. Unpublishing also asks you to confirm.

## Next Steps

- [Build Panel Apps With Weave](/guides/panel-apps/build-with-weave/) — describe the app and approve the exact change.
- [The Panel App Kit](/guides/panel-apps/app-kit/) — the components Studio's table, view and template starts use.
- [Using a Panel App](/guides/panel-apps/using/) — logs, usage and rebuilds after you publish.
