---
title: STDDEV_POP (Lakehouse v2)
description: STDDEV_POP — devuelve la desviación estándar poblacional.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-pop.md
---

Devuelve la desviación estándar poblacional.

## Sintaxis de Analyze

```python
func.stddev_pop(get_column(table, 'score'))
```

## Ejemplos de Analyze

```python
func.stddev_pop(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## Sintaxis de SQL

```sql
STDDEV_POP(<score>)
```

## Ejemplos de SQL

```sql
SELECT STDDEV_POP(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
