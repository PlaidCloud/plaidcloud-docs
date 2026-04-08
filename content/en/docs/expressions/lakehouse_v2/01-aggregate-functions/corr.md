---
title: CORR
description: "Learn how to use the CORR aggregate function in PlaidCloud Lakehouse. Returns the Pearson correlation coefficient between two expressions."
---

Returns the Pearson correlation coefficient between two expressions.

## Analyze Syntax

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))
```

## Analyze Examples

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))

┌───────┐
│ 0.872 │
└───────┘
```

## SQL Syntax

```sql
CORR(<revenue>, <ad_spend>)
```

## SQL Examples

```sql
SELECT CORR(revenue, ad_spend) FROM marketing;

┌───────┐
│ 0.872 │
└───────┘
```
