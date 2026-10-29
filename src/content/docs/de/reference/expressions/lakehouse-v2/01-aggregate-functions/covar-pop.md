---
title: COVAR_POP (Lakehouse v2)
description: COVAR_POP gibt die Kovarianz der Grundgesamtheit für zwei Ausdrücke zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-pop.md
---

Gibt die Kovarianz der Grundgesamtheit für zwei Ausdrücke zurück.

## Analyze-Syntax

```python
func.covar_pop(get_column(table, 'y'), get_column(table, 'x'))
```

## Analyze-Beispiele

```python
func.covar_pop(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 102.46 │
└────────┘
```

## SQL-Syntax

```sql
COVAR_POP(<y>, <x>)
```

## SQL-Beispiele

```sql
SELECT COVAR_POP(height, weight) FROM measurements;

┌────────┐
│ 102.46 │
└────────┘
```
