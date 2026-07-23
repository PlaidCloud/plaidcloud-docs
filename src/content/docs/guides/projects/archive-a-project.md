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

The **Archive Table Data** tree in that dialog chooses which tables have their *data* written into the archive — the difference between a full and a partial backup. It does not change what else the archive holds: an archive always captures the project's whole structure, including every workflow, step, function, table, data editor, and dimension. Choose what you want to bring back when you restore it.

## Restoring an Archive


Once you have an archive, you may want to restore it. You can restore an archive into a new project or into an existing project.



To restore an archive:


1. Open Analyze
2. Select the “Projects” tab
3. Choose **Import Project Archive** from the **Actions** menu (or the toolbar) and select the archive to restore

### Choosing What to Restore

Once you pick an archive, its contents are listed grouped by kind — workflows, steps, functions, tables, data editors, and dimensions. Everything is ticked to start with, so leaving the tree alone restores the whole archive.

To bring back only part of it, untick whatever you don't want. You can untick a whole kind, or expand one and tick individual items.

Whatever you pick, anything it needs comes with it, so a partial restore still works:

- A workflow brings its steps, and each step brings the tables it reads and writes and the function it runs.
- A dimension brings the tables its members are built from, and any dimension it refers to.
- A data editor brings its source and target tables.

This means a restore can include a few items you didn't tick — they are what your selection depends on. If you start the import with nothing ticked, PlaidCloud asks you to pick something rather than create an empty project.

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
