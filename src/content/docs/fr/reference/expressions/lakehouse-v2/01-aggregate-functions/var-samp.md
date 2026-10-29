---
title: VAR_SAMP (Lakehouse v2)
description: VAR_SAMP — renvoie la variance de l'échantillon. Alias de `VARIANCE_SAMP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-samp.md
---

Renvoie la variance de l'échantillon. Alias de `VARIANCE_SAMP`.

## Syntaxe Analyze

```python
func.var_samp(get_column(table, 'score'))
```

## Exemples Analyze

```python
func.var_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## Syntaxe SQL

```sql
VAR_SAMP(<score>)
```

## Exemples SQL

```sql
SELECT VAR_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
