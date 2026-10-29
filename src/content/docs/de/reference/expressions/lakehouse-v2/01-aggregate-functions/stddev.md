---
title: STDDEV (Lakehouse v2)
description: STDDEV – gibt die Standardabweichung der Grundgesamtheit zurück. Alias für `STDDEV_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev.md
---

Gibt die Standardabweichung der Grundgesamtheit zurück. Alias für `STDDEV_POP`.

## Analyze-Syntax

```python
func.stddev(get_column(table, 'score'))
```

## Analyze-Beispiele

```python
func.stddev(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQL-Syntax

```sql
STDDEV(<score>)
```

## SQL-Beispiele

```sql
SELECT STDDEV(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
