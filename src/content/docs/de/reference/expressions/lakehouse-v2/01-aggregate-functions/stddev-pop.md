---
title: STDDEV_POP (Lakehouse v2)
description: STDDEV_POP – gibt die Standardabweichung der Grundgesamtheit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-pop.md
---

Gibt die Standardabweichung der Grundgesamtheit zurück.

## Analyze-Syntax

```python
func.stddev_pop(get_column(table, 'score'))
```

## Analyze-Beispiele

```python
func.stddev_pop(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQL-Syntax

```sql
STDDEV_POP(<score>)
```

## SQL-Beispiele

```sql
SELECT STDDEV_POP(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
