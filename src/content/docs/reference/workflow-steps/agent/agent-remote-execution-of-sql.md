---
title: Agent Remote Execution of SQL
description: Execute SQL queries remotely through a PlaidLink agent in PlaidCloud workflows for secure database operations behind firewalls.
sidebar:
  order: 1
---

## Description

Executes SQL on a database that PlaidCloud can reach only through a PlaidLink Agent — typically because the database sits behind a firewall, on a private network, or in an on-premises data center. The Agent runs the SQL locally and reports success or failure back to PlaidCloud.

Use this for triggering remote stored procedures, refresh routines, or maintenance jobs as part of a PlaidCloud workflow without exposing the source database to the public internet.

## Run a Statement Once per Row

The **Remote Execute: SQL** step, which connects to the database directly rather than through an Agent, can run its statement once for each row of a table, such as to call a stored procedure for each input row. Set **Run the SQL** to **Once Per Row**, choose a **Driver Table**, and fill in **Parameters**. Write each value in the statement as a `:name` placeholder, such as `CALL load_region(:region, :period)`, and map each placeholder in **Parameter** to the **Driver Column** that supplies it. Each value is sent to the database as a bound parameter, never pasted into the statement text.

Every parameter needs both a name and a driver column, and a parameter can't be listed twice. The form warns when a `:name` in the statement has no mapping or a mapping isn't in the statement. The driver table must be a table, not a view. A driver table with no rows finishes with a warning and runs nothing, and one with more than 100,000 rows fails the step without running any of them, so filter it first.
