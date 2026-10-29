---
title: VARIANCE_POP (Lakehouse v2)
description: VARIANCE_POP – gibt die Varianz der Grundgesamtheit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-pop.md
---

Gibt die Varianz der Grundgesamtheit zurück.

## Analyze-Syntax

```python
func.variance_pop(get_column(table, 'score'))
```

## Analyze-Beispiele

```python
func.variance_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQL-Syntax

```sql
VARIANCE_POP(<score>)
```

## SQL-Beispiele

```sql
SELECT VARIANCE_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
