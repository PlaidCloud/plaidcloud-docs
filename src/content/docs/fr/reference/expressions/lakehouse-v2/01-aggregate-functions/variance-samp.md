---
title: VARIANCE_SAMP (Lakehouse v2)
description: VARIANCE_SAMP — renvoie la variance de l'échantillon.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-samp.md
---

Renvoie la variance de l'échantillon.

## Syntaxe Analyze

```python
func.variance_samp(get_column(table, 'score'))
```

## Exemples Analyze

```python
func.variance_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## Syntaxe SQL

```sql
VARIANCE_SAMP(<score>)
```

## Exemples SQL

```sql
SELECT VARIANCE_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
