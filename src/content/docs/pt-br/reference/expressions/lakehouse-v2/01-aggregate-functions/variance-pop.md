---
title: VARIANCE_POP (Lakehouse v2)
description: VARIANCE_POP — retorna a variância populacional.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-pop.md
---

Retorna a variância populacional.

## Sintaxe do Analyze

```python
func.variance_pop(get_column(table, 'score'))
```

## Exemplos do Analyze

```python
func.variance_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## Sintaxe SQL

```sql
VARIANCE_POP(<score>)
```

## Exemplos SQL

```sql
SELECT VARIANCE_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
