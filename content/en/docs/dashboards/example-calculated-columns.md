---
title: Example Calculated Columns
slug: dashboard-calculated-columns
description: Examples of calculated column expressions
date: 2022-06-07T07:39:48
weight: 4.0
---

## Description

Data in dashboards can be augmented with calculated columns.  Each dataset will contain a section for calculated columns.  Calculated columns can be written and modified with PostgreSQL-flavored SQL.

{{< include "dashboards/common-navigate-to-dataset.md" >}}

## Metrics
Metrics are expressions that are typically used to describe a field, including how it will be consolidated.

## Examples
### count
```
COUNT(*)
```

### min
```
min("MyColumnName")
```

### max
```
max("MyColumnName")
```

### coalesce (useful for converting nulls to 0.0, for instance)
```
coalesce("BaselineCost",0.0)
```

### divide
divide, with a hack for avoiding DIV/0 errors
```
sum("so_infull")/(count(*)+0.00001)
```
{{<note>}}
A better way to do this would be to check for a null or zero denominator and then coalese to zero rather than attempting the division.
{{</note>}}


### conditional statement
```
CASE WHEN "Field_A"= 'Foo' THEN max(coalesce("Value_A",0.0)) - max(coalesce("Value_B",0.0)) END
```

