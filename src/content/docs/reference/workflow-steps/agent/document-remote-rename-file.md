---
title: Document - Remote Rename File
description: Rename files on remote systems through a PlaidLink agent in PlaidCloud workflows for secure file management behind firewalls.
sidebar:
  order: 7
---

## Description



Renames or moves a file on a remote file system through a PlaidLink Agent. Operates entirely on the on-premises side; no data is transferred to or from PlaidCloud.

Common pattern: rename a source file to mark it as 'processed' after a remote-import step succeeds, so the same workflow doesn't re-import it on the next run.


## Examples


First, make a selection from the “Agent to Use” dropdown. 



Next, enter “Source Path” and “Destination Path”. 



Finally, select “Save and Run Step”.

## Missing Source

With an updated PlaidLink agent, a source that doesn't exist on the remote system finishes the step with a warning, `No file or folder found at <path>; nothing renamed`, instead of an error, and the workflow continues. Agents that haven't been updated still fail the step.

An empty source path finishes the step with the warning `No path to rename from; nothing renamed.`, including when a folder in the path is a variable that resolved to nothing in this run.

A source that is a filesystem root or a parent folder of the PlaidLink agent's working directory (`/`, `C:\`, a share root such as `\\server\share`, or `..`) fails the step with `Refusing to rename from the filesystem root <path>.` or `Refusing to rename from <path>, which contains the agent's working directory.` An empty destination path fails the step with `No destination path for the rename; it would write into the agent's working directory.` Renaming into a drive or share root, such as `E:\` or `\\nas\drop`, works. Roots and `..` are refused with the PlaidLink agents you already have deployed; an updated agent also refuses any other folder that contains its working directory, judged against its own file system.
