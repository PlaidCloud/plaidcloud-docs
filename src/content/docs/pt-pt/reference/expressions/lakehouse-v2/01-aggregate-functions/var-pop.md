---
title: VAR_POP (Lakehouse v2)
description: VAR_POP — devolve a variância populacional. Alias de `VARIANCE_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-pop.md
---

Devolve a variância populacional. Alias de `VARIANCE_POP`.

## Sintaxe do Analyze

```python
func.var_pop(get_column(table, 'score'))
```

## Exemplos do Analyze

```python
func.var_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## Sintaxe SQL

```sql
VAR_POP(<score>)
```

## Exemplos SQL

```sql
SELECT VAR_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
