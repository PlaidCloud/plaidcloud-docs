---
title: MANN_WHITNEY_U_TEST
description: "Learn how to use the MANN_WHITNEY_U_TEST aggregate function in PlaidCloud Lakehouse. Performs a Mann-Whitney U test on two independent samples."
---

Performs a Mann-Whitney U test on two independent samples.

## Analyze Syntax

```python
func.mann_whitney_u_test(get_column(table, 'sample'), get_column(table, 'treatment'))
```

## Analyze Examples

```python
func.mann_whitney_u_test(get_column(table, 'score'), get_column(table, 'group_id'))

┌─────────────────────────────┐
│ {"U":245.0,"p-value":0.032} │
└─────────────────────────────┘
```

## SQL Syntax

```sql
MANN_WHITNEY_U_TEST(<sample>, <treatment>)
```

## SQL Examples

```sql
SELECT MANN_WHITNEY_U_TEST(score, group_id) FROM experiment;

┌─────────────────────────────┐
│ {"U":245.0,"p-value":0.032} │
└─────────────────────────────┘
```
