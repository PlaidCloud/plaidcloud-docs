---
title: Document - Remote Import File
description: Import files from remote systems through a PlaidLink agent in PlaidCloud workflows for secure file retrieval behind firewalls.
sidebar:
  order: 6
---

## Description



Pulls a file from a remote file system through a PlaidLink Agent and stores it in a PlaidCloud document account. Used when source files originate on internal file shares, on-prem servers, or behind a firewall.

The Agent reads the file locally and streams it to PlaidCloud, where downstream workflow steps can process it.


## Examples


First, make a selection from the “Agent to Use” dropdown. Next, enter the file or folder path under “File or Folder Path for Import”. Then enter the folder destination under “Folder Destination”. Select the file type from the dropdown. Finally, select “Save and Run Step”.
