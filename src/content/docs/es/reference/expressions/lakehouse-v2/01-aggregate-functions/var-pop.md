---
title: VAR_POP (Lakehouse v2)
description: VAR_POP — devuelve la varianza poblacional. Alias de `VARIANCE_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-pop.md
---

Devuelve la varianza poblacional. Alias de `VARIANCE_POP`.

## Sintaxis de Analyze

```python
func.var_pop(get_column(table, 'score'))
```

## Ejemplos de Analyze

```python
func.var_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## Sintaxis de SQL

```sql
VAR_POP(<score>)
```

## Ejemplos de SQL

```sql
SELECT VAR_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
