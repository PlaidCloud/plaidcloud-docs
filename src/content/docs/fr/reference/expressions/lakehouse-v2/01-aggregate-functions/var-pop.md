---
title: VAR_POP (Lakehouse v2)
description: VAR_POP — renvoie la variance de la population. Alias de `VARIANCE_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-pop.md
---

Renvoie la variance de la population. Alias de `VARIANCE_POP`.

## Syntaxe Analyze

```python
func.var_pop(get_column(table, 'score'))
```

## Exemples Analyze

```python
func.var_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## Syntaxe SQL

```sql
VAR_POP(<score>)
```

## Exemples SQL

```sql
SELECT VAR_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
