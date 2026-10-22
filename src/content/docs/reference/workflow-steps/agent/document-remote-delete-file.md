---
title: Document - Remote Delete File
description: Delete files on remote systems through a PlaidLink agent in PlaidCloud workflows for secure file management behind firewalls.
sidebar:
  order: 4
---

## Description



Deletes a file on a file system that sits behind a firewall, reached through a PlaidLink Agent. The Agent performs the delete locally on the on-premises file system.

Use this for cleanup after on-prem export operations, or as part of file-based integrations that need to remove processed source files.


## Examples


First, make a selection from the “Agent to Use” dropdown. Next, enter the file or folder path under “File or Folder Path for Delete”. Finally, select “Save and Run Step”.

## Missing Path

With an updated PlaidLink agent, a path that doesn't exist on the remote system finishes the step with a warning, `Nothing to delete at <path>`, instead of an error, and the workflow continues. Agents that haven't been updated still fail the step.

An empty path finishes the step with the warning `No path to delete; nothing deleted.` and deletes nothing. This includes a path whose folder is a variable that resolved to nothing in this run, such as `{folder}/archive`.

A path that is a filesystem root or a parent folder of the PlaidLink agent's working directory (`/`, `C:\`, a share root such as `\\server\share`, or `..`) fails the step before anything is deleted, with `Refusing to delete the filesystem root <path>.` or `Refusing to delete <path>, which contains the agent's working directory.` Roots and `..` are refused with the PlaidLink agents you already have deployed; an updated agent also refuses any other folder that contains its working directory, judged against its own file system.
