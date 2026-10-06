---
title: Sign In to PlaidXL
description: Connect PlaidXL to your PlaidCloud workspace with your email and your usual sign-in, including single sign-on and two-factor authentication, then sign out or switch workspaces.
sidebar:
  label: Sign In
  order: 2
---

PlaidXL signs you in as yourself, using the same sign-in you use for PlaidCloud in a browser. There's no server address to type and no password stored in the workbook.

## Sign In

1. Open the task pane: **PlaidCloud → Show Taskpane**.
2. Under **Enter your email**, type the email address you use for PlaidCloud and click **Sign In**.
3. If your email belongs to more than one workspace, choose one from **Select a tenant** and click **Sign In**. (A *tenant* in PlaidXL is your PlaidCloud workspace.) If you belong to one workspace, PlaidXL picks it for you.
4. Excel asks whether to allow a pop-up window. Allow it.
5. In the pop-up, sign in the way you normally do:
   - **PlaidCloud sign-in** — your email, password, and any two-factor code you've set up.
   - **Single sign-on** — if you're already signed in to your organization, this step passes straight through. Otherwise your organization's sign-in page opens first.
6. When the pop-up says **Authenticated successfully**, close it if it hasn't closed itself.

The task pane now shows **Connected to** your workspace ID **as** your username, with your projects listed below. Continue with [Work With Tables and Dimensions](/reference/cli/plaidxl/retrieve/).

To set up two-factor authentication or single sign-on for your account, see [Member Authentication](/administration/access/member-authentication/).

## Staying Signed In

PlaidXL keeps you signed in on this computer and renews your sign-in in the background while you work. When you open the task pane in a later session, it goes straight to your projects. If your sign-in has expired completely, PlaidXL asks for your email again.

## What You Can See

PlaidXL reads with your permissions. You see the projects you can open in PlaidCloud, and the tables and dimensions in them, and nothing more. If a project or table is missing, ask a project owner for access. See [Organizations and Workspaces Explained](/administration/access/overview/organizations-and-workspaces-explained/) for how workspace membership works.

## Sign Out or Switch Workspaces

Click **Logout** at the top of the task pane. PlaidXL clears your sign-in and returns to the email screen.

To work in a different workspace, sign out, then sign in again and choose the other workspace under **Select a tenant**. PlaidXL works with one workspace at a time, for every workbook you have open.

## Light and Dark Theme

The task pane follows your Office theme. To pin it to light or dark, click the sun or moon button at the top left of the task pane.

## Related

- [Install PlaidXL](/reference/cli/plaidxl/install/) — add the add-in and open the task pane
- [Troubleshooting](/reference/cli/plaidxl/troubleshooting/) — when the sign-in pop-up doesn't open or a workspace is missing
- [Viewing and Managing Workspaces](/administration/access/overview/viewing-and-managing-workspaces/) — the workspaces you belong to
