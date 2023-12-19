---
title: Dashboard Expression Examples
slug: dashboard-expressions
weight: 6.0
description: Using common dashboard expressions
date: 2022-06-07T07:39:48
---

## Description

An expression is a basic function that does a conversion, calculation, cast to another data type, or other action on data in a column. Examples are `startswith`, `max`, or `current_date`. For a full list of core expressions, see: [Standard Expressions](/docs/plaidcloud/analyze/expressions/)

There are two primary types of expressions - metrics and calculated columns.  Both can be written and modified with PostgreSQL-flavored SQL. Learn more about PostgreSQL [here](https://www.postgresql.org/docs/current/).

## Navigating to a dataset
In order to view and edit metrics and calculated expressions:
1.  Sign into plaidcloud.com and navigate to Dasboards. Select the dashboard you want to work in.
2.  Select Data > Datasets from the menu.
3.  Search for a dataset to view or modify
4.  Hover over the dataset with the cursor and you will see icons in the actions column.
5.  Click the `edit` icon beneath `Actions`

Each dataset will contain a tab for Metrics and one for Calulated Columns.


## Metrics
Metrics are expressions that are typically used to describe a field, including how it will be consolidated. Examples are below.

### cast
```
cast("MyColumnName" AS datatype)    'Converts a value (of any type) into a specified datatype
```

Parameter Values

|Parameter   |   Description                       |
|------------|-------------------------------------|
|MyColumnName|The value to convert                 |
|datatype    |The datatype to convert expression to|

Example: 
```
cast("MyColumnName" AS NUMERIC)
```


coalesce (useful for converting nulls to 0.0, for instance)
```
coalesce("BaselineCost",0.0)
```

divide, with a hack for avoiding DIV/0 errors
``` 
sum("so_infull")/(count(*)+0.00001)

```

{{<note>}}
A better way to do this would be to check for a null or zero denominator and then coalese to zero rather than attempting the division.
{{</note>}}

### count
```
count(*)
```

### distinct
```
distinct("MyColumnName")
```

### first
```
first("MyColumnName")
```

### min
```
min("MyColumnName")
```

### max
```
max("MyColumnName")
```

### nullif
```
nullif("MyColumnName","MyColumnName2")  'returns NULL if two expressions are equal, otherwise it returns the first expression.
```

Parameter Values

|Parameter    |      Description         |
|-------------|--------------------------|
|MyColumnName |Expression to be compared |
|MyColumnName2|Expression to be compared |


### over
```
over(
    [ <PARTITION BY MyColumnName> ]  
    [ <ORDER BY MyColumnName> ]   
    [ <ROW or RANGE MyColumnName> ]  
    )     
```
|Arguments    |                                 Description                                                  |
|-------------|----------------------------------------------------------------------------------------------|
|PARTITION BY |Divides the query result set into partitions                                                  |
|ORDER BY     |Defines the logical order of the rows within each partition of the result set                 |
|ROW/RANGE    |Limits the rows within the partition by specifying start and end points within the partition  |

Example:
```
sum("MyColumnName") over (partition by "MyColumnName2")
```

### round
```
round("MyColumnName",2) 
```
Parameter Values
|Parameter  |            Description                     |
|-----------|--------------------------------------------|
|Number     |Number to be rounded                        |
|Decimals   |Number of decimal places to round number to |



### to_char
```
to_char("MyColumnName", 'DateFormat')
```
Parameter Values
|Parameter    |                Description                           |
|-------------|------------------------------------------------------|
|MyColumnName |A number or date that will be converted to a string   |
|DateFormat   |Format that will be used to convert value to a string |


### sum
```
sum("MyColumnName")
```



Conditional statement
```
CASE WHEN "Field_A"= 'Foo' THEN max(coalesce("Value_A",0.0)) - max(coalesce("Value_B",0.0)) END

## Calculated Columns
Calculated columns are typically additional columns made by combining logic and existing columns.

Convert a date to text
```
to_char("week_ending_sol_del_req", 'YYYY-mm-dd')
```


