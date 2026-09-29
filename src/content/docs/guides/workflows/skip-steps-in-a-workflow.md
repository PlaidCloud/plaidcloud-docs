---
title: Skip steps in a workflow
description: Skip specific steps in a PlaidCloud workflow to bypass operations during testing, debugging, or selective processing runs.
sidebar:
  order: 11
---

Steps in the workflow can be set to skip during the workflow run. This may be useful if there are debugging steps or old steps that you are not prepared to completely remove from the workflow yet.

To set this option, uncheck the step's **Enabled** checkbox in the workflow table. The change is saved as soon as you click it, with no separate Save. The step will no longer run as part of the workflow but can still be run using the single step run process.



Steps that have been set to disabled will have a disabled indicator in the workflow steps hierarchy table.
