---
title: Control Document Account Access
slug: control-document-account-access
weight: 1.0
description: Set access controls for Document accounts
date: 2022-01-25T07:39:47
---


Four types of access restrictions are available for an account: Private, Workspace, Member Only, and Security Group. The type of restriction set for a user is editable at any time from the account form.

{{< note >}}
None of the account access levels reveal the account credentials used to access the documents. Only account owners can view the credentials.
{{< /note >}}

## Updating Account Access


1. Select `Document > Manage Accounts` within PlaidCloud
2. Enter the edit mode on the account you wish to change
3. Select the desired access level restriction located under `Security Model`
4. Select the Save button

{{< note >}}
Depending on the selected Security Model, there will be different options for assigning which members or security groups are allowed access from the account list under Manage Accounts.
{{< /note >}}


## Restriction Options


### All Workspace Members


This access is the simplest since it provides access to all members of the workspace and does not require any additional assignment of members.



### Specific Members Only


This access setting requires assignment of each member to an account. This option is particularly useful when combined with the single sign-on option of assigning members based on a list of groups sent with the authentication. However, for workspaces with large numbers of members, this approach can often require more effort than desired, which is where security groups become useful. To choose specific members only:


1. Select the members icon from the Manage Accounts list
2. Drag the desired members from the `Unassigned Members` column on the left, to the `Assigned Members` column on the right
3. To remove members, do the opposite
4. Select the Save button

### Specific Security Groups Only


With this option, permission to access an account is granted to specific security groups rather than just individuals. With access restrictions relying on association with a security group or groups, the administration of accounts with much larger user counts becomes much simpler. To edit assigned groups:


1. Select the groups icon from the Manage Accounts list
2. Drag the desired groups from the `Unassigned Groups` column on the left, to the `Assigned Groups` column on the right
3. To remove groups, do the opposite
4. Select the Save button

### Remote agents


PlaidLink agents will often use Document accounts to store files or move files among systems. To allow remote agents access to Document accounts, agents MUST have permission granted. This is a security feature to limit unwanted access to potentially sensitive information. To add agents:


1. Select the agent icon from the Manage Accounts list
2. Drag desired agents from the `Unassigned Agents` column on the left, to the `Assigned Agents` column on the right
3. To remove agents, do the opposite
4. Select the Save button
