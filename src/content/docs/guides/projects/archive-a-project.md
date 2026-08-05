---
title: Archive a Project
description: Archive PlaidCloud projects to preserve completed work, free up workspace resources, and maintain a clean project environment.
sidebar:
  order: 6
---

## Creating an Archive


Projects normally contain critical processes and logic, which are important to archive. If you ever need to restore the project to a specific state, having archives is essential. 



PlaidCloud allows you to archive projects at any point in time. Creation of archives complements the built-in point-in-time tracking of PlaidCloud by allowing for specific points in time to be captured. This might be particularly useful before a major change or to capture the exact state of a production environment for posterity.



**Full backup**: This includes all the data tables included in a project. The archive may be quite large, depending on the volume of data in the project.


**Partial backup:** This can be used if all of the project data can be derived from other sources. If this is the case, it is not necessary to archive the data in the project and have it remain elsewhere. Partial archives save time and storage space when creating the archive.



To archive a project:


1. Open Analyze
2. Select the “Projects” tab
3. Select the project, then choose **Export Project Archive** from the **Actions** menu (or right-click the project and choose **Export Project Archive**)

The window names the project it will archive in its title bar, so you can confirm you have the right one before you start.

### Tables Whose Data Cannot Be Included

Occasionally a table listed in a project no longer has any data behind it — for example, a table that was never built, or whose data was removed outside the project. The archive is still written: those tables are left out of the table data, and the export finishes with a message naming them. Everything else — the project configuration, workflows, table definitions, and the data for every other table — is archived as normal.

The archive records which tables went in without their data, and restoring it names them again at the end of the restore rather than presenting them as complete. A table whose definition was still readable comes back with its columns and no rows; one whose definition had gone too comes back as an entry with no table behind it. Re-run the workflow that builds a table to fill it in.

:::note
A scheduled archive records skipped tables in the system log rather than showing you a message, since nothing is on screen to show it to. Check the export message when it matters which tables were included.
:::

### If You Cannot Read the Project's Tables

Reading a project's tables is a separate permission from reading the project itself, and an archive depends on both. If you can open a project but do not have table read access, the archive is still written — it simply carries no table data, and no table definitions either, since both sit behind that same permission. The export finishes with a message naming the tables that were left out, identified by their internal ids rather than their names, because the names come from the definitions the archive did not include.

An archive taken this way is a copy of the project's configuration — its workflows, variables, dimensions, views and layouts, as far as you are entitled to read each of them — and not of its data. **Restoring it recreates no tables at all**, so it is not a backup you can rebuild the project's data from. Check the export message before relying on one.

Unlike the tables described above, this is not something re-running a workflow corrects — the data was never read in the first place. Ask a workspace administrator to grant you read access to the project's tables, then take the archive again.

:::caution
This applies to scheduled archives too, which run as a particular member. Where that member does not have table read access, every archive the schedule produces is configuration-only, and the shortfall is recorded in the system log rather than shown to anyone. If you keep scheduled archives as backups, confirm the member they run as can read the project's tables.
:::

### If the Export Fails

An export that fails now reports the failure. Previously an archive could report as finished when it had not been written, leaving you to discover the missing file later — most often when you came to restore it. A failed export now says so, so treat a reported success as a genuine one and check the message on anything that reports an error. The same applies to the other export types, not just project archives.

## Restoring an Archive


Once you have an archive, you may want to restore it. You can restore an archive into a new project or into an existing project.



To restore an archive:


1. Open Analyze
2. Select the “Projects” tab
3. Choose **Import Project Archive** from the **Actions** menu (or the toolbar) and select the archive to restore

## Archiving Schedule


Archives can also serve as a periodic backup of your project. PlaidCloud allows you to manage the backup schedule and set the retention period of the backup archives to whatever is most convenient or desired.


Since all changes to a project are automatically tracked, archiving is not necessary for rollback purposes. However, it does provide specific snapshots of the project state, which is often useful for control purposes and/or having the ability to recover to a known point.



To set an archiving schedule:


1. Open Analyze
2. Select the “Projects” tab
3. Click the backup icon
4. Choose a directory destination in a **Document** account
5. Choose the backup frequency and retention
6. Choose which items to backup
7. Click “Update”
