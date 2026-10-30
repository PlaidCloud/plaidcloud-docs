---
title: STD (Lakehouse v2)
description: STD – gibt die Standardabweichung der Grundgesamtheit zurück. Alias für `STDDEV_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/std.md
---

Gibt die Standardabweichung der Grundgesamtheit zurück. Alias für `STDDEV_POP`.

## Analyze-Syntax

```python
func.std(get_column(table, 'score'))
```

## Analyze-Beispiele

```python
func.std(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQL-Syntax

```sql
STD(<score>)
```

## SQL-Beispiele

```sql
SELECT STD(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
