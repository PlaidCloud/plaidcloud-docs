---
title: Alerts and Digests
description: Notify people when a number in a Panel app crosses a limit, or send a scheduled summary of key numbers by push notification, email, Slack or Microsoft Teams.
sidebar:
  order: 6
---

An **alert** watches one number from a Panel app's data and tells you the moment it crosses a limit. A **digest** sends a short summary of up to 10 numbers every day or every week. Both are set up from the app in [Panel Studio](/guides/panel-apps/studio/), and both are yours: you see and change only your own.

## Open Alerts and Digests

1. In **My Panel Apps** or a project's **Home** board, choose **Open in Studio** on the app.
2. Choose **Alerts & Digests**.

The window has an **Alerts** tab and a **Digests** tab. The app must be assigned to a project, and its tables are the ones in that project.

## Define a Number to Watch

Alerts and digests measure a **KPI** that you build from a table in the app's project:

| Field | What it sets |
|---|---|
| **Table** | The table to read. It must be built. |
| **Measure column** | The column to total or count. |
| **Function** | `sum`, `avg`, `min`, `max`, `count` or `count_distinct`. |
| **Add filter** | Optional conditions that narrow the rows, each a column, a comparison and a value. For *is in*, separate values with commas. **Remove filter** takes one out. |

The number is always calculated with your own access to the table, including [row-level security](/guides/panel-apps/accessing-data/). You never see, or send, a figure for rows you can't read.

## Create an Alert

1. On the **Alerts** tab, choose **New**.
2. Enter a **Name**.
3. Build the KPI.
4. Under **Alert when the KPI is**, pick `>`, `>=`, `<` or `<=` and enter a **Threshold**.
5. Choose how to be told in **Send by** (see [Channels](#channels)).
6. Leave **Enabled** ticked and choose **Save**.

PlaidCloud checks every enabled alert once an hour. An alert fires once each time the number crosses the threshold, then stays quiet until the number is back on the safe side and crosses again. The list shows when each alert last fired, and **(off)** after the name of one that is turned off.

You can have up to 20 of your own alerts on one app.

## Create a Digest

1. On the **Digests** tab, choose **New**.
2. Enter a **Name**.
3. Choose **Add KPI**, give it a **KPI label**, and build the number. Repeat for up to 10 KPIs. **Remove KPI** takes one out.
4. Next to **Send**, pick **Every day** or **Every week**.
5. Choose how to send it in **Send by** and choose **Save**.

A digest goes out once per day or per week, in the first hourly check after the period starts, with the period in UTC. The list shows when each digest last sent. A KPI your access to the table leaves with no rows shows as no data, never as an unfiltered figure.

You can have up to 10 of your own digests on one app and 20 in total across apps.

## Channels

| Send by | Where it goes |
|---|---|
| **Push notification** | The PlaidCloud mobile app on your devices. Alerts only. |
| **Email** | The email address on your account. |
| **Slack** | A Slack channel, through a Slack connection. |
| **Microsoft Teams** | A Teams channel, through a Microsoft Teams connection. |

For **Slack** and **Microsoft Teams**, pick the **Connection** to post through. A workspace administrator creates the connection, and you must have been given access to it. The connection's address must start with `https`.

### What a Slack or Teams Card Shows

A card shows the figures only when your own access to the table is unrestricted, meaning no row-level security limits the rows you can read. If your access is limited to some rows, the card says new values are ready and links to the app, where each reader sees only the rows their own access allows. Every card carries a link to the app. A channel's members are managed outside PlaidCloud, which is why a restricted owner's numbers don't go to one.

## When Delivery Fails

An alert or digest that can't be delivered 24 hours in a row, for example because its Slack connection was removed, is turned off. The list shows it as **(off)** and the form says how many deliveries failed. Fix the channel, tick **Enabled** and choose **Save** to turn it back on.

## Edit or Delete

Choose an item in the list to change it and **Save**. Choose **Delete** to remove it. If you switch items with unsaved changes, PlaidCloud asks before discarding them.

## Next Steps

- [Panel Studio](/guides/panel-apps/studio/) — where you reach **Alerts & Digests**.
- [The Panel App Kit](/guides/panel-apps/app-kit/) — build the app the alerts watch.
