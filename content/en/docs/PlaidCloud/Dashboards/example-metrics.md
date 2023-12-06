---
title: Example Metrics
slug: dashboard-metrics
description: Examples of common metrics
date: 2022-06-07T07:39:48
weight: 4.0
---

## Description

Data in dashboards can be augmented with metrics.  Each dataset will contain a section for Metrics.  Metrics can be written and modified with PostgreSQL-flavored SQL.

{{< include "dashboards/common-navigate-to-dataset.md" >}}

## Examples
Calculated columns are typically additional columns made by combining logic and existing columns.

### convert a date to text
```
to_char("week_ending_sol_del_req", 'YYYY-mm-dd')
```


