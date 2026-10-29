---
title: VARIANCE_SAMP (Lakehouse v2)
description: VARIANCE_SAMP — retorna a variância amostral.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-samp.md
---

Retorna a variância amostral.

## Sintaxe do Analyze

```python
func.variance_samp(get_column(table, 'score'))
```

## Exemplos do Analyze

```python
func.variance_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## Sintaxe SQL

```sql
VARIANCE_SAMP(<score>)
```

## Exemplos SQL

```sql
SELECT VARIANCE_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
