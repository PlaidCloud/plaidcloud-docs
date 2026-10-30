---
title: STDDEV_SAMP (Lakehouse v2)
description: STDDEV_SAMP — devolve o desvio-padrão amostral.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-samp.md
---

Devolve o desvio-padrão amostral.

## Sintaxe do Analyze

```python
func.stddev_samp(get_column(table, 'score'))
```

## Exemplos do Analyze

```python
func.stddev_samp(get_column(table, 'score'))

┌───────┐
│ 15.89 │
└───────┘
```

## Sintaxe SQL

```sql
STDDEV_SAMP(<score>)
```

## Exemplos SQL

```sql
SELECT STDDEV_SAMP(score) FROM test_results;

┌───────┐
│ 15.89 │
└───────┘
```
