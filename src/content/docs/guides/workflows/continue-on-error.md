---
title: Continue on Error
description: Configure PlaidCloud workflow steps to continue execution on error, allowing subsequent steps to run despite earlier failures.
sidebar:
  order: 10
---

Workflow steps can be set to continue processing even when there is an error. This might be useful in workflow start-up conditions or where data may be available intermittently. If the step errors, it will be recorded as an error but the workflow will continue to process.



To set this option, open the step's form from the workflow table — click its gear icon, or right-click it and choose **Edit Step Details** — and go to the **General** tab. Set **Action to perform on Error** to **Continue**. After saving the updated step, any errors with the step will not cause the workflow to stop.



Steps that have been set to continue on error will have a special indicator in the workflow steps hierarchy table.
