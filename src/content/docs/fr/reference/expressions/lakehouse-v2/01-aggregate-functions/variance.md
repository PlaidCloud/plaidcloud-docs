---
title: VARIANCE (Lakehouse v2)
description: VARIANCE — renvoie la variance de la population. Alias de `VARIANCE_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance.md
---

Renvoie la variance de la population. Alias de `VARIANCE_POP`.

## Syntaxe Analyze

```python
func.variance(get_column(table, 'score'))
```

## Exemples Analyze

```python
func.variance(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## Syntaxe SQL

```sql
VARIANCE(<score>)
```

## Exemples SQL

```sql
SELECT VARIANCE(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
