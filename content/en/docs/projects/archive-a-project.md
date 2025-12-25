---
title: Archive a Project
slug: archive-a-project
weight: 6.0
description: Create and Restore your project archives
date: 2022-01-25T07:39:48
---


## Creating an Archive


Projects normally contain critical processes and logic, which are important to archive. If you ever need to restore the project to a specific state, having archives is essential. 



PlaidCloud allows you to archive projects at any point in time. Creation of archives complements the built-in point-in-time tracking of PlaidCloud by allowing for specific points in time to be captured. This might be particularly useful before a major change or to capture the exact state of a production environment for posterity.



**Full backup**: This includes all the data tables included in a project. The archive may be quite large, depending on the volume of data in the project.


**Partial backup:** This can be used if all of the project data can be derived from other sources. If this is the case, it is not necessary to archive the data in the project and have it remain elsewhere. Partial archives save time and storage space when creating the archive.



To archive a project:


1. Open Analyze
2. Select the “Projects” tab

## Restoring an Archive


Once you have an archive, you may want to restore it. You can restore an archive into a new project or into an existing project.



To restore an archive:


1. Open Analyze
2. Select the “Projects” tab

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
