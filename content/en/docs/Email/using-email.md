---
title: Using the Email Area
slug: using-email
weight: 1.0
description: Browse sent transactional email and bounces, filter by stream, recipient, or tag, and page through delivery history.
date: 2026-04-28T00:00:00
---


## Description

Open the area from **Tools > Email**. The page is split into two panels: **Sent Email** and **Bounces**. The stream selector at the top of each panel chooses which Postmark stream to view; it defaults to the first transactional stream configured for your tenant.


## Sent Email

The **Sent Email** panel shows messages PlaidCloud has sent on your tenant's behalf.

**To filter sent email:**

1. Open **Tools > Email > Sent Email**
2. Use the **Status** filter to narrow by Postmark delivery status
3. Use the **Recipient** filter to search by To address
4. Use the **Tag** filter to narrow to a specific message tag
5. Use the stream selector to switch to a different stream

The status filter offers Postmark's valid status values (delivered, bounced, opened, etc.). Multiple filters combine.


## Bounces

The **Bounces** panel shows delivery failures returned by Postmark.

**To filter bounces:**

1. Open **Tools > Email > Bounces**
2. Use the **Recipient** filter to search by To address
3. Use the **Tag** filter to narrow to a specific message tag

Each row shows the bounce type and the delivery message returned by Postmark. Long delivery messages are truncated to 200 characters in the table — click the row to see the full message.


## Paging

Both panels page through history rather than loading every message at once. Use the pager at the bottom of the table to move forward and back.

{{< note >}}
The Email area is read-only. Replies, retries, and template management still happen in the Postmark dashboard.
{{< /note >}}
