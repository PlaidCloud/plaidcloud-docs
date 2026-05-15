---
title: Agent Remote Execution of SQL
description: Execute SQL queries remotely through a PlaidLink agent in PlaidCloud workflows for secure database operations behind firewalls.
sidebar:
  order: 1
---

## Description

Executes SQL on a database that PlaidCloud can reach only through a PlaidLink Agent — typically because the database sits behind a firewall, on a private network, or in an on-premises data center. The Agent runs the SQL locally and reports success or failure back to PlaidCloud.

Use this for triggering remote stored procedures, refresh routines, or maintenance jobs as part of a PlaidCloud workflow without exposing the source database to the public internet.
