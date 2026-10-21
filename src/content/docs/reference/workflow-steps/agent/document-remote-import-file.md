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


First, make a selection from the “Agent to Use” dropdown. Next, enter the file or folder path under “File or Folder Path for Import”. Then enter the folder destination under “Folder Destination”. Optionally choose a **Compression** to compress the file as it arrives: Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO or Deflate (zlib). Finally, select “Save and Run Step”.

## Missing Source File or Folder

When nothing exists at the path on the remote share, the step finishes with a warning, `No file or folder found at <path>; nothing imported.`, instead of an error. The workflow continues to the next step, and the step's retry and on-error settings (go to a step, or continue) don't run for a missing source. This works with the PlaidLink agents you already have deployed.

Other failures still fail the step: permission denied, a failed upload to PlaidCloud, or, on an updated PlaidLink agent, a server or share that can't be reached.

Because nothing is imported, a document from a previous run stays where it was. To run a downstream step only when this period's file arrived, either:

- Add a **file exists in Document** [step condition](/guides/workflows/step-conditions/#document-path-conditions) to the downstream step, with the Document path set to a per-period path such as one that includes the period in the filename.
- Delete the imported document after the workflow uses it, so a missing source can't leave an old file behind.
