---
title: STD (Lakehouse v2)
description: STD — devuelve la desviación estándar poblacional. Alias de `STDDEV_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/std.md
---

Devuelve la desviación estándar poblacional. Alias de `STDDEV_POP`.

## Sintaxis de Analyze

```python
func.std(get_column(table, 'score'))
```

## Ejemplos de Analyze

```python
func.std(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## Sintaxis de SQL

```sql
STD(<score>)
```

## Ejemplos de SQL

```sql
SELECT STD(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
