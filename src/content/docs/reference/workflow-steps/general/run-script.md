---
title: Run App Operation
description: Invoke a registered application operation from a workflow, optionally passing a document path and parameters.
sidebar:
  order: 10
---

## Description

Invokes a registered application operation from within a workflow. Use it to trigger platform work that is not a data transform — the operations an app exposes for automation.

## Configuration

### Application Operation to Execute

The operation to invoke.

### File Path

For operations that take a file:

- **Document directory** — the document account and path to pass.
- **File parameter name** — the parameter the operation expects the path under. Defaults to `document_path`; change it only if the operation names it differently.

### Optional Parameters

Name/value pairs passed to the operation alongside the file path.

## Related

- [General steps](/reference/workflow-steps/general/)
- [User Defined Transform](/reference/workflow-steps/general/user-defined-transform/)
- [Run Remote Python](/reference/workflow-steps/general/run-remote-python/)
