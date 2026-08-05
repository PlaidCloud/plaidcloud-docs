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

## Configuration

### Member Search Parameter

How rows in the source table are matched to members. Choose one:

- **Email** (default)
- **User name**

## Related

- [General steps](/reference/workflow-steps/general/)
- [Get Workspace Members](/reference/workflow-steps/general/get-workspace-members/)
- [Member management](/administration/access/)
