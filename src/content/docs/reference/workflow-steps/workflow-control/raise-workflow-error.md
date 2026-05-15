---
title: Raise Workflow Error
description: Raise a custom error in a PlaidCloud workflow step to trigger error handling and halt execution when conditions are not met.
sidebar:
  order: 10
---

## Description

Forces the workflow into an error state with a custom message. Use this when a step needs to fail the workflow based on a data condition that earlier steps detected — for example, "fail if the row count is zero," "fail if a key validation table has unmapped values," or "fail if a balance check doesn't reconcile."

Pair this with [step conditions](/guides/workflows/step-conditions/) so the error only triggers when something is actually wrong. When the step runs, it stops the workflow immediately and writes the error to the workflow log, which can in turn trigger the remediation workflow if one is configured.


## Raise Workflow Error


Mainly for use with step conditions, the step can be set to execute if conditions are met and raise an error within the workflow
