---
title: Managing Step Errors
slug: managing-step-errors
weight: 9.0
description: Control the behavior of a step when errors occur
date: 2022-01-25T07:40:20
---


If a workflow experiences an error during processing, an error indicator is displayed on both the workflow and the step that had the error. PlaidCloud can retry a failed step multiple times. This is often useful if the step is accessing remote systems or data that may not be highly available or intermittently fail for unknown reasons. The retry capability can be set to retry many times as well as add a delay between retries from seconds to hours.



If no retry is selected or the maximum number of retries is exceeded, then the step will be marked as an error. PlaidCloud provides three levels of error handling in that case:


* Stop the workflow when an error occurs
* Mark the step as an error but keep processing the workflow
* Mark the step as an error and trigger a remediation workflow process instead of continuing the current workflow

## Stop the Workflow


Stopping the workflow when a step errors is the most common approach since workflows generally should run without errors. This will stop the workflow and present the error indicator on both the step and the workflow. The error will also be displayed in the activity monitor but no further action is taken.



## Keep Processing


Each step can be set to continue on error in the step form. If this checkbox is enabled, then any step will be marked with an error if it occurs, but the workflow will treat the error as a completion of the step and continue on. This is often useful if there are steps that perform tasks that can error when there is missing data but are harmless to the overall processes.



Since the workflow is continuing on error under this scenario the workflow will not display an error indicator and continue to show a running indicator.



## Trigger Remediation Workflow


With the ability to set a remediation workflow as part of the workflow setup, a workflow error will immediately stop the processing of the current workflow and start processing the remediation workflow. Note that if a step is marked to continue on error that a failure will not trigger the remediation workflow. Only steps that fail that would also cause the entire workflow to stop will trigger the remediation process.



A remediation workflow may be useful for simply notifying people that a failure has occurred or it can perform other complex processing to attempt an automatic correction of any underlying reasons the original workflow failed.

