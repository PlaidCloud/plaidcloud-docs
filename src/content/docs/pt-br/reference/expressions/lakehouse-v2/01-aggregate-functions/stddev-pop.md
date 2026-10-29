---
title: STDDEV_POP (Lakehouse v2)
description: STDDEV_POP — retorna o desvio padrão populacional.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-pop.md
---

Retorna o desvio padrão populacional.

## Sintaxe do Analyze

```python
func.stddev_pop(get_column(table, 'score'))
```

## Exemplos do Analyze

```python
func.stddev_pop(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## Sintaxe SQL

```sql
STDDEV_POP(<score>)
```

## Exemplos SQL

```sql
SELECT STDDEV_POP(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
