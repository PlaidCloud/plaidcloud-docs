---
title: Using Start Paths in Document Accounts
slug: using-start-paths-in-document-accounts
weight: 5.0
description: Control where users start navigation in document storage
date: 2022-01-25T07:39:47
---


The account management form allows the configuration of the storage connection information and a start path. A start path allows those who use the account to begin browsing the directory structure further down the directory tree. This particular option is useful when you have multiple teams that need segregated file storage, but you only want one underlying storage service account.



The Start Path option in Document accounts is useful for the following reasons:


* When controlling access to sub-directories for specific teams and groups
* Granting access to only one bucket

For example, setting a start path of *teams/team_1/* for the `Team 1` Document account *and teams/team_2* for the `Team 2` Document account provides different start points on a shared account. When a member opens the Team 1 Document account they will begin file navigation inside *team/team_1*. They will not be able to move up the tree and see anything above *teams/team_1*.



Team 2 would have a similar restriction of not being able to navigate into Team 1's area.



This provides the ability to restrict specific teams to lower levels of the tree while allowing other teams higher level access to the tree while not needing any additional cloud storage complexity like additional buckets or special permissions.



## Adding and Updating the Start Path


1. Go to Document > Manage Accounts
2. Select the account you wish to edit and enter the edit mode
3. Add a Start Path in the Start Path text field
4. Select the save button

## Start Path Format


The path always begins with the bucket name followed by the sub-directories.



```
<my-bucket>/folder1/folder2/
```

