---
title: PlaidCloud Git
description: Host, version, and collaborate on Git repositories inside PlaidCloud — with issues, pull requests, project boards, releases, and wikis, and single sign-on built in.
sidebar:
  label: Overview
  order: 0
---

PlaidCloud Git is a private Git service built into your workspace. Each workspace gets its own Git server for storing code, configuration, notebooks, and any other versioned files — together with the issues, pull requests, and project boards your team uses to collaborate on them.

You sign in with your PlaidCloud account, so there's no separate username or password to set up. Open **Git** from your workspace and you're already signed in. New repositories are private by default, visible only to members you grant access.

## Administering Git

Any member can create repositories, but **creating organizations** — shared spaces that group repositories and teams — requires the **Git Administration** permission. Grant it in **Identity** by adding the permission to a security group, or by adding members to the built-in **Git Administration** group. Anyone in a group that has the permission becomes a Git administrator when they next sign in to Git. PlaidCloud support staff have it automatically.

If a newly-granted administrator has never opened Git before, they may need to sign in to Git **twice** for administrator access to take effect — the first sign-in creates their Git account, and the permission is applied on the next.

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
- [Access Management](/administration/access/) — how workspace membership and security groups govern who can see and edit repositories
