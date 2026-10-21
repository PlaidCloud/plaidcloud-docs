---
title: Document - Remote Export File
description: Export files to remote systems through a PlaidLink agent in PlaidCloud workflows for secure file transfers behind firewalls.
sidebar:
  order: 5
---

## Description



Writes a file from a PlaidCloud document account to a remote file system through a PlaidLink Agent. Useful for delivering reports, extracts, or processed files to systems that aren't reachable from PlaidCloud directly — internal shared drives, on-prem SFTP servers, or specialized application directories.

The Agent receives the file from PlaidCloud and writes it to the configured local destination.


## Examples


First, make a selection from the “Agent to Use” dropdown. Next, browse for the file or folder path under “File or Folder to Export”. Then enter the location under “Export Path Destination”. Finally, select “Save and Run Step”.

## Path Safety

An empty export path fails the step with `No destination path for the export; it would write into the agent's working directory.` This includes a path that resolved to nothing because a variable in it was empty. Exporting into a drive or share root, such as `E:\` or `\\nas\drop`, works.

With **Uncompress archive on arrival** selected, the step unpacks every archive in the destination folder and removes it. It therefore refuses a destination that is a filesystem root or a file directly in one (`Refusing to unpack an export into the filesystem root <path>.`), or the PlaidLink agent's own folder (`Refusing to unpack an export into <path>, which contains the agent's working directory.`). Choose a dedicated subfolder instead.

The empty-path and root checks work with the PlaidLink agents you already have deployed. Refusing the agent's own folder needs an updated PlaidLink agent.
