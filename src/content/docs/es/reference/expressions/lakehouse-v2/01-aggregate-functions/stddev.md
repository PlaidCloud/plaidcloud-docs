---
title: STDDEV (Lakehouse v2)
description: STDDEV — devuelve la desviación estándar poblacional. Alias de `STDDEV_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev.md
---

Devuelve la desviación estándar poblacional. Alias de `STDDEV_POP`.

## Sintaxis de Analyze

```python
func.stddev(get_column(table, 'score'))
```

## Ejemplos de Analyze

```python
func.stddev(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## Sintaxis de SQL

```sql
STDDEV(<score>)
```

## Ejemplos de SQL

```sql
SELECT STDDEV(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
