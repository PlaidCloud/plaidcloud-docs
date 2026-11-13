---
title: PlaidCloud Git
description: Host, version, and collaborate on Git repositories inside PlaidCloud — with issues, pull requests, project boards, releases, and wikis, and single sign-on built in.
sidebar:
  label: Overview
  order: 0
---

PlaidCloud Git is a private Git service built into your workspace. Each workspace gets its own Git server for storing code, configuration, notebooks, and any other versioned files — together with the issues, pull requests, and project boards your team uses to collaborate on them.

You sign in with your PlaidCloud account, so there's no separate username or password to set up. New repositories are private by default, visible only to members you grant access.

## Open Git

Select **Git** in your workspace's app list. The **Git** tab opens with the workspace's host, your role, and a **Repositories** list. Use **View all in Git** to go to the Git web interface, **Manage who can push** (if you can manage groups) to open group management, and the refresh button to reload. Use **← Back to** your workspace in Git to return to PlaidCloud.

A role indicator shows your level: **Administrator**, **Contributor** or **Viewer**, with a line saying what that lets you do. Each repository row shows its name, description (when it has one), **Updated** with the date, a read-only clone field with a copy button, and **Open**, which opens the repository in Git. Repositories you create privately are in Git directly, not in this list.

If Git is not set up for your workspace, or can't be reached, the **Git** tab shows **Git is not available** with the reason, and **Try again** checks again.

## Clone a Repository

Copy the repository's clone address from its row. The first time you copy, a **Set up Git on your computer** card appears with the steps below. Select **Dismiss** to hide it, and **How to clone** in the header to bring it back.

1. Git must be installed on your computer.
2. Create a token at **Settings → Applications** with the **write:repository** permission. The card links to that page.
3. Tell Git who you are, using the two `git config --global user.name` and `user.email` commands shown, which already hold your name and email.
4. Clone the repository with the `git clone` command shown. When Git asks for a password, paste that token, not your PlaidCloud password.

Each command has its own copy button. See [Repositories](/guides/git/repositories/) for the full walkthrough. Copying needs push access and an activated Git account: if the copy button is disabled, open any repository once to activate your account, or, as a **Viewer**, ask for push access as described below.

## Access Levels

Everyone with Git access can read the workspace's shared repositories. Two further levels let you push.

| Role | What you can do | Granted by |
|---|---|---|
| **Viewer** | View and clone the shared repositories. | Default for every member. |
| **Contributor** | Everything in Read, and push to the `apps` repository, where [Panel](/guides/panel-apps/deploy-from-git/) and [Dash](/guides/dash-apps/deploy-from-git/) app code lives. | The **Git Contributors** security group. |
| **Administrator** | Everything in Contributor, and push to all repositories, including `udfs`, and create organizations. | The **Git Administration** security group. |

The `udfs` repository is limited to Admins because user-defined functions run under the identity of the workflow that calls them.

If you are a **Viewer**, the **Git** tab names up to three workspace administrators you can ask to add you to **Git Contributors**.

## Git From Apps and UDFs

A Panel or Dash app's window has a **Repository** section showing its repository, branch and build status, with **Edit in browser** and **Copy clone URL** for members who can push. Panel Studio apps, and App Runner apps on the managed PlaidCloud Git connection, are folders in the `apps` repository, so that is the repository their window shows. See [Where Your App Lives](/guides/panel-apps/studio/#where-your-app-lives). A Git-backed UDF's toolbar has **Open**, which opens the repository at its branch in Git, and **Edit in browser** for Admins.

## Granting Git Access

Workspace administrators grant access in **Identity** by adding members to a security group, or by adding the permission to a group of your own.

1. Add the member to **Git Contributors** to let them push app code, or to **Git Administration** to make them a Git administrator.
2. To give every new member push access to app code, add **Git Contributors** to your default groups. **Git Administration** can't be a default group.
3. To check what a member can do, open the member and select the **Git** tab. It shows the member's Git username, their level and which group grants it.

A change applies the next time the member signs in to Git or opens the **Git** tab. A member's Git account follows their PlaidCloud membership. Deactivating or removing a member blocks their Git account, including their tokens and SSH keys, within about an hour, and reactivating them unblocks it. Nothing is deleted: their repositories and history stay. Signing in to Git with single sign-on opens the member's own account. PlaidCloud support staff have Admin access automatically.

## What's in This Section

- [Repositories](/guides/git/repositories/) — create a repository, then clone, commit, and push your work
- [Issues](/guides/git/issues/) — track tasks, bugs, and ideas with labels, milestones, and assignees
- [Pull Requests](/guides/git/pull-requests/) — propose changes on a branch and review them before they merge
- [Project Boards](/guides/git/projects/) — organize issues and pull requests on a Kanban board
- [Releases and Tags](/guides/git/releases-and-tags/) — mark and publish versioned snapshots of a repository
- [Wikis](/guides/git/wikis/) — keep long-form documentation next to your code
- [Packages](/guides/git/packages/) — publish and install build artifacts from the repository registry
- [Searching Code](/guides/git/searching-code/) — find code, issues, and pull requests across your repositories

## Related

- [Deploy a Panel App From PlaidCloud Git](/guides/panel-apps/deploy-from-git/) — serve a HoloViz Panel app straight from a repository, with a managed no-credentials connection
- [Deploy a Dash App From PlaidCloud Git](/guides/dash-apps/deploy-from-git/) — serve a Plotly Dash app the same way
- [Access Management](/administration/access/) — how workspace membership and security groups govern who can see and edit repositories
