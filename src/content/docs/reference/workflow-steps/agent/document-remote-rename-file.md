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
