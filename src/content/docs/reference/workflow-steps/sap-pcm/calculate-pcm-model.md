---
title: Calculate PCM Model
description: Trigger SAP PCM model calculations from a PlaidCloud workflow step to run profitability and cost allocation processing jobs.
---

## Description



Triggers the calculation engine in an SAP Profitability and Cost Management (PCM) model. Use this in a workflow to run the costing calculation after upstream data loads have populated the model's inputs (assignments, drivers, source data).

Calculation is asynchronous on the PCM server side; pair with [Stop PCM Model Calculation](/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation/) if you need to abort a long-running calculation.


## Our Credentials


PlaidCloud is an official SAP Partner and a preferred vendor of services related to SAP PCM model design and implementation.







## Examples


Select Agent to Use from the dropdown, enter model name in the “Model Name” field, click the “Wait for Calculation to Complete” check box (if desired), then click “Save and Run Step”.
