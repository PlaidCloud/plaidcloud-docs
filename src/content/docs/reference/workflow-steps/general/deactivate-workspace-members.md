---
title: Deactivate Workspace Members
description: Deactivate workspace members listed in a project table, matched by email address or user name.
sidebar:
  order: 12
---

import { Aside } from '@astrojs/starlight/components';

## Description

Deactivates the workspace members named in a source table. Use it to automate offboarding from an authoritative list — an HR extract or an access review — rather than deactivating people by hand.

Pair it with [Get Workspace Members](/reference/workflow-steps/general/get-workspace-members/) to build the list of who should no longer have access.

<Aside type="caution" title="This Revokes Access">
  Every matched member loses access when the step runs. Check the source table
  contains only who you intend before scheduling this step.
</Aside>

## Workspace Admins in the List

[Only a workspace admin can deactivate a workspace admin](/administration/access/member-management/#changing-a-workspace-admin). When the step runs without workspace-admin rights and its list includes admins, it leaves those admins active, deactivates everyone else, and then ends in error with a message that gives how many members it deactivated and names each admin it left active. The members it deactivated stay deactivated. To deactivate an admin, have a workspace admin do it in Identity.

## Configuration

### Member Search Parameter

How rows in the source table are matched to members. Choose one:

- **Email** (default)
- **User name**

## Related

- [General steps](/reference/workflow-steps/general/)
- [Get Workspace Members](/reference/workflow-steps/general/get-workspace-members/)
- [Member management](/administration/access/)
