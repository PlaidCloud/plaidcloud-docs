---
title: CLI Tools
description: Reference for PlaidCloud command-line tools — PlaidLink agent, PlaidXL Excel add-in, and the Jupyter CLI for notebook integration.
---

PlaidCloud provides three command-line and on-machine tools for working with workspaces outside the web UI:

## PlaidLink

[PlaidLink](/reference/cli/plaidlink/) is an agent that runs inside your network to bridge PlaidCloud workflows to firewall-protected resources — databases, file shares, and other systems that PlaidCloud can't reach directly. It installs as a Windows service, Unix/Linux/Mac daemon, container, or Kubernetes pod.

- [Install](/reference/cli/plaidlink/install/)
- [Configure](/reference/cli/plaidlink/configure/)
- [Agents](/reference/cli/plaidlink/agents/)
- [Upgrade](/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/reference/cli/plaidxl/) is the PlaidCloud add-in for Microsoft Excel. It retrieves project tables and dimensions into worksheets, refreshes them on demand, and adds `PLAIDXL` formulas that calculate rolled-up values from PlaidCloud data.

- [Install](/reference/cli/plaidxl/install/)
- [Sign In](/reference/cli/plaidxl/connect/)
- [Work With Tables and Dimensions](/reference/cli/plaidxl/retrieve/)
- [Custom Functions](/reference/cli/plaidxl/functions/)
- [Build a Report With Custom Functions](/reference/cli/plaidxl/build-a-report/)
- [The PlaidCloud Ribbon](/reference/cli/plaidxl/ribbon/)
- [Troubleshooting](/reference/cli/plaidxl/troubleshooting/)

## Jupyter CLI

[Jupyter CLI](/reference/cli/jupyter/) lets data scientists work with PlaidCloud project data from Jupyter notebooks using a PlaidCloud-aware CLI and Python helpers.

- [Command line](/reference/cli/jupyter/command-line/)
- [Jupyter notebook](/reference/cli/jupyter/jupyter-notebook/)
- [OAuth setup](/reference/cli/jupyter/oauth-setup/)
