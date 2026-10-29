---
title: VAR_POP (Lakehouse v2)
description: VAR_POP – gibt die Varianz der Grundgesamtheit zurück. Alias für `VARIANCE_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-pop.md
---

Gibt die Varianz der Grundgesamtheit zurück. Alias für `VARIANCE_POP`.

## Analyze-Syntax

```python
func.var_pop(get_column(table, 'score'))
```

## Analyze-Beispiele

```python
func.var_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQL-Syntax

```sql
VAR_POP(<score>)
```

## SQL-Beispiele

```sql
SELECT VAR_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
