---
title: VARIANCE_POP (Lakehouse v2)
description: VARIANCE_POP — renvoie la variance de la population.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-pop.md
---

Renvoie la variance de la population.

## Syntaxe Analyze

```python
func.variance_pop(get_column(table, 'score'))
```

## Exemples Analyze

```python
func.variance_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## Syntaxe SQL

```sql
VARIANCE_POP(<score>)
```

## Exemples SQL

```sql
SELECT VARIANCE_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
