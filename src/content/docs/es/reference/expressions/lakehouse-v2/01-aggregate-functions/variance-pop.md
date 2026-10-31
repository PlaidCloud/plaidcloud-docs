---
title: VARIANCE_POP (Lakehouse v2)
description: VARIANCE_POP — devuelve la varianza poblacional.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-pop.md
---

Devuelve la varianza poblacional.

## Sintaxis de Analyze

```python
func.variance_pop(get_column(table, 'score'))
```

## Ejemplos de Analyze

```python
func.variance_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## Sintaxis de SQL

```sql
VARIANCE_POP(<score>)
```

## Ejemplos de SQL

```sql
SELECT VARIANCE_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
