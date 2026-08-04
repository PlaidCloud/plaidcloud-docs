---
title: Calculate and Export PCM Model
description: Run a PCM model calculation and export the result to a database or a delimited file, through a PlaidLink agent.
sidebar:
  order: 11
---

## Description

Calculates a SAP PCM model and exports the result in one step, through a [PlaidLink agent](/reference/workflow-steps/agent/) with access to the PCM installation. Where [Calculate PCM Model](/reference/workflow-steps/sap-pcm/calculate-pcm-model/) only runs the calculation, this step also moves the output.

## Configuration

### Agent to Use

The PlaidLink agent that reaches the PCM installation.

### Model Information

- **Model name** — the PCM model to calculate.
- **Export specification path** — the PCM export specification describing what to export.

### Export Output Destination

Choose a database target, a file target, or both.

**To a database** — on by default; the export writes through the specification's configured database target.

**To a file** — off by default. When on:

- **File path** — where the agent writes the file.
- **Alias** — the alias recorded in the export. Defaults to `DEFAULT ALIAS`.
- **Precision** — decimal places for exported values. Defaults to 0.
- **Delimiter** — comma, tab, pipe, semicolon, space, `@`, `~`, or `:`. Defaults to tab.
- **Append** — off by default, so each run replaces the file. Turn it on to accumulate runs.
- **Include rules** — off by default. Turn it on to export the model's rules alongside the values.
- **Unicode** — off by default. Turn it on when the exported data contains characters outside the default encoding.

## Related

- [SAP-PCM steps](/reference/workflow-steps/sap-pcm/)
- [Calculate PCM Model](/reference/workflow-steps/sap-pcm/calculate-pcm-model/)
- [Run SAP PCM Hyper Loader](/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader/)
