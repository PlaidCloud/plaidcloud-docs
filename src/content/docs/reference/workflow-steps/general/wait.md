---
title: Wait
description: Add a timed delay in a PlaidCloud workflow step to pause execution for a specified duration before proceeding to the next step.
sidebar:
  order: 4
---

## Description


The Wait transform is used to pause processing for a specified duration. This can be especially helpful when waiting for I/O operations from other systems or for debugging workflows during development.



## Duration Parameters


Specify a non-negative integer value using the **Duration** spinner.



Next, specify the unit of time from the dropdown menu. The following units are available for selection:


* Seconds
* Minutes
* Hours

## Wait for a Time or a File

An AI assistant or the REST API can also set these keys. The step waits for them in this order, after the duration:

* `milliseconds` — milliseconds waited on top of the duration.
* `until_time` — then sleep until the clock next reads this time of day, in UTC, as `HH:MM:SS`.
* `file` — then wait for this Document file, `{account, path}`, to change. `file_event` is the change to wait for: `modified` (default), `created` or `deleted`. The step looks every `poll_seconds` (default 5) for at most `max_wait_seconds` (default 3600, at most a day), then finishes with a warning and the workflow continues. A file that is already there when waiting for `created` ends the wait at once, and a missing file when waiting for `modified` or `deleted` finishes with a warning naming the path, without waiting.
