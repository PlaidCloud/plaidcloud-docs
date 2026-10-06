---
title: Install PlaidXL
description: Add the PlaidXL add-in to Excel on Windows or Mac, find the PlaidCloud ribbon tab, and open the PlaidXL task pane.
sidebar:
  order: 1
---

You install PlaidXL once per computer, not once per workbook. After that, the **PlaidCloud** tab is on the Excel ribbon in every workbook you open.

## Before You Start

- Use Excel for Microsoft 365, or Excel 2021 or later, on Windows or Mac.
- If your organization manages Office add-ins centrally, your Microsoft 365 administrator may need to deploy PlaidXL for you. If you can't install add-ins yourself, ask them to add the **PlaidCloud** add-in.

## Install on Windows

1. In Excel, open **Insert → Add-ins** (in some versions, **Home → Add-ins**).
2. Type `PlaidCloud` in the add-in search box.
3. Select the **PlaidCloud** add-in and click **Add**.

## Install on Mac

1. In Excel for Mac, open **Insert → Add-ins**. In older versions the menu is **Insert → Store**.
2. Type `PlaidCloud` in the add-in search box.
3. Select the **PlaidCloud** add-in and click **Add**.

## Open the Task Pane

1. Click the **PlaidCloud** tab on the ribbon.
2. In the **PlaidXL Controls** group, click **Show Taskpane**.

The PlaidXL task pane opens on the right side of the window and asks you to sign in. Continue with [Sign In](/reference/cli/plaidxl/connect/).

The task pane stays signed in between sessions, so you'll usually sign in once and then just open the task pane when you need it.

## If PlaidXL Doesn't Appear

- Close every Excel window and reopen Excel. An add-in often doesn't show on the ribbon until Excel restarts.
- Look under **Insert → My Add-ins** (Windows) or **Insert → Add-ins → My Add-ins** (Mac) and select **PlaidCloud** from there.
- If your organization blocks add-ins from the store, ask your Microsoft 365 administrator to deploy it.

More fixes are on the [Troubleshooting](/reference/cli/plaidxl/troubleshooting/) page.

## Related

- [Sign In](/reference/cli/plaidxl/connect/) — connect the add-in to your workspace
- [The PlaidCloud Ribbon](/reference/cli/plaidxl/ribbon/) — every command on the **PlaidCloud** tab
