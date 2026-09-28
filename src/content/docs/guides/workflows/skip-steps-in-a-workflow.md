---
title: Skip steps in a workflow
description: Skip specific steps in a PlaidCloud workflow to bypass operations during testing, debugging, or selective processing runs.
sidebar:
  order: 11
---

Steps in the workflow can be set to skip during the workflow run. This may be useful if there are debugging steps or old steps that you are not prepared to completely remove from the workflow yet. To set this option, you have two options:


* Edit the step form
* Uncheck the enabled checkbox in the workflow hierarchy

To edit the step form, open the step's form from the workflow table — click its gear icon, or right-click it and choose **Edit Step Details** — and go to the **General** tab. Uncheck the enabled checkbox. After saving the updated step it will no longer run as part of the workflow but can still be run using the single step run process.



Steps that have been set to disabled will have a disabled indicator in the workflow steps hierarchy table.
