---
title: Managing Document Account Backups
slug: managing-document-account-backups
weight: 3.0
description: Control how, where, and when Document account backups occur
date: 2022-01-25T07:39:47
---


Document enables the backup of any account on a nightly basis. This feature permits backup across different cloud storage providers and on local systems. Essentially, any account is a valid target for the backup of another account.

{{< note >}}
You cannot backup to the same account.
{{< /note >}}

The backup process is not limited to a single backup destination. It is possible to have multiple redundant backup locations specified if this is a desired approach. 
For example, the backup of an internal server to another server may be one location with a second backup sent to Amazon S3 for off-site storage.


By using the prefix feature, it’s possible to have a single backup account contain the backups from multiple other accounts. 
Each account backup set begins its top level folder(s) with a different prefix, making it easy to distinguish the originating location and the restoration process. 
For example, if you have three different Document accounts but want to set their backup destination to the same location, using a 
prefix would allow all three accounts to properly backup without the fear of a name collision.


## Reviewing Current Backup Settings

1. Go to Document > Manage Accounts
2. Select the backup icon for the account you wish to review

## Creating a Backup Set

1. Go to Document > Manage Accounts
2. Select the backup icon for the account for which to create a backup
3. Select the `New Backup Set` button
4. Complete the required fields
5. Select the `Create` button

The backup process is now scheduled to run nightly (US Time).

## Updating a Backup Set

1. Go to Document > Manage Accounts
2. Select the backup icon for the account for which to edit a backup
3. Select the edit icon of the desired backup set
4. Adjust the desired information
5. Select the `Update` button

## Deleting a Backup Set

1. Go to Document > Manage Accounts
2. Select the backup icon for the account for which to edit a backup
3. Select the delete icon of the desired backup set
4. Select the `Delete` button

{{< note >}}
The backup sets already present will not be deleted but the backup process will no longer run. You can remove the existing backups using Document file and directory management processes.
{{< /note >}}
