---
title: MANN_WHITNEY_U_TEST (Lakehouse v2)
description: MANN_WHITNEY_U_TEST – führt einen Mann-Whitney-U-Test an zwei unabhängigen Stichproben durch.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/mann-whitney-u-test.md
---

Führt einen Mann-Whitney-U-Test an zwei unabhängigen Stichproben durch.

## Analyze-Syntax

```python
func.mann_whitney_u_test(get_column(table, 'sample'), get_column(table, 'treatment'))
```

## Analyze-Beispiele

```python
func.mann_whitney_u_test(get_column(table, 'score'), get_column(table, 'group_id'))

┌─────────────────────────────┐
│ {"U":245.0,"p-value":0.032} │
└─────────────────────────────┘
```

## SQL-Syntax

```sql
MANN_WHITNEY_U_TEST(<sample>, <treatment>)
```

## SQL-Beispiele

```sql
SELECT MANN_WHITNEY_U_TEST(score, group_id) FROM experiment;

┌─────────────────────────────┐
│ {"U":245.0,"p-value":0.032} │
└─────────────────────────────┘
```
