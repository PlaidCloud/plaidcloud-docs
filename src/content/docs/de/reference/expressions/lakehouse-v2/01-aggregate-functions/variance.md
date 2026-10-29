---
title: VARIANCE (Lakehouse v2)
description: VARIANCE – gibt die Varianz der Grundgesamtheit zurück. Alias für `VARIANCE_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance.md
---

Gibt die Varianz der Grundgesamtheit zurück. Alias für `VARIANCE_POP`.

## Analyze-Syntax

```python
func.variance(get_column(table, 'score'))
```

## Analyze-Beispiele

```python
func.variance(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQL-Syntax

```sql
VARIANCE(<score>)
```

## SQL-Beispiele

```sql
SELECT VARIANCE(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
