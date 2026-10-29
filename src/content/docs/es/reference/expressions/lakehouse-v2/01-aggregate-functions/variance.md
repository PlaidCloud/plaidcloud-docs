---
title: VARIANCE (Lakehouse v2)
description: VARIANCE — devuelve la varianza poblacional. Alias de `VARIANCE_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance.md
---

Devuelve la varianza poblacional. Alias de `VARIANCE_POP`.

## Sintaxis de Analyze

```python
func.variance(get_column(table, 'score'))
```

## Ejemplos de Analyze

```python
func.variance(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## Sintaxis de SQL

```sql
VARIANCE(<score>)
```

## Ejemplos de SQL

```sql
SELECT VARIANCE(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
