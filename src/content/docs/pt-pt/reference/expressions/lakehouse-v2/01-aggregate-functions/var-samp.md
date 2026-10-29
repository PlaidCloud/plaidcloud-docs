---
title: VAR_SAMP (Lakehouse v2)
description: VAR_SAMP — devolve a variância amostral. Alias de `VARIANCE_SAMP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-samp.md
---

Devolve a variância amostral. Alias de `VARIANCE_SAMP`.

## Sintaxe do Analyze

```python
func.var_samp(get_column(table, 'score'))
```

## Exemplos do Analyze

```python
func.var_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## Sintaxe SQL

```sql
VAR_SAMP(<score>)
```

## Exemplos SQL

```sql
SELECT VAR_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
