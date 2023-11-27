---
title: Managing Security Groups and Assignments
slug: managing-security-groups-and-assignments
description: Manage security group settings and view membership
date: 2022-01-25T07:39:48
tags:
- plaidcloud
- expression
categories:
- PlaidCloud
- Expressions
Weight: 2.0
---


PlaidCloud’s security and access management is straightforward. A member is granted or denied access based on the groups in which a member is associated. Adding or changing a member’s security association is easily customizable.

{{< note >}}
Each workspace is allowed an unlimited number of security groups, but we recommend minimizing the number in order to ease security management.
{{< /note >}}



## Managing Security Groups


Security groups can be added, updated, or deleted.



**To manage security groups:**


1. Open Identity
2. Select the “Security” tab
3. Click “Security Groups” in the dropdown menu (this will display a form with existing groups)
4. To add a group, click the “Create Security Group”
5. To edit permissions of a group, click on the left-most icon

**To manage group members:**


1. Open Identity
2. Select the “Security” tab
3. Click “Security Groups” in the dropdown menu
4. Click the Member icon
5. Drag desired members from the “Unassigned Members” column to the “Assigned Members” column or vice versa to remove members

## Setting Default Security Groups


To reduce the time needed for adding new members, identify a set of default security groups. This provides a baseline set of security groups for new members without needing to manually assign each person. The setting is available when adding a new security group if you check the box at the bottom of the Security Group window that reads “Assign to New Users by Default”.



## Performing a Security Audit


The security audit capability provides the ability to see group membership across all members and groups.



**To perform a security audit:**


1. Open Identity
2. Select the “Security” tab
3. Click “Security Group Audit” in the dropdown menu

As all tables in PlaidCloud are exportable as a CSV file format, the group member associations are reviewable outside of PlaidCloud for either historical purposes or just some fun off-line viewing.



**To export from the “Security Group Audit” form:**


1. Open Identity
2. Select the “Security” Tab
3. Click “Security Group Audit” in the dropdown menu
4. Click the small icon to the far right of “Username” in the table
5. Click “Export CSV” or “Export XLXS” depending on your preference

## Viewing Available Permission Settings


Each application being used in the workspace has specific available permissions. The security group permissions are based on these application permissions.


The complete list of available permission for each application is viewable from the Security Bin.



**To access the Security Bin:**


1. Open Identity
2. Select the “Security”
3. Click “Security Bins” in the dropdown menu

To view the detailed security settings for each application, select the tags icon on the far left.



This available security settings information is informational only. For details on managing permissions, refer to the Managing Security Groups section above.

