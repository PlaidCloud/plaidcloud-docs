---
title: Example Metrics
slug: dashboard-metrics
description: Examples of common metrics
date: 2022-06-07T07:39:48
weight: 5.0
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

### various SUM examples
```
SUM(Value)

SUM(-1*"value_usd_mkp") / (0.0001+SUM(-1*"value_usd_base"))

(SUM("Value_USD_VAT")/SUM("Value_USD_HEADER"))*100

sum(delivery_cases) where Material_Type = Gloves

sum("total_cost") / sum("delivery_count")
```


### various case examples
```
CASE WHEN
SUM("distance_dc_xd") = 0 THEN 0
ELSE
sum("XD")/sum("distance_dc_xd")
END

sum(CASE
WHEN "FUNCTION" = 'OM' THEN "VALUE__FC"
ELSE 0.0
END)
```


### count
```
count(*)
```


### First and Cast
```
public.first(cast("PRETAX_SEQ" AS NUMERIC))
```


### Round
```
round(Sum("GROSS PROFIT"),0)
```


### Concat
```
concat("GCOA","CC Code")
```
