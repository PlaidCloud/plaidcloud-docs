---
title: VARIANCE (Lakehouse v2)
description: VARIANCE — devolve a variância populacional. Alias de `VARIANCE_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance.md
---

Devolve a variância populacional. Alias de `VARIANCE_POP`.

## Sintaxe do Analyze

```python
func.variance(get_column(table, 'score'))
```

## Exemplos do Analyze

```python
func.variance(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## Sintaxe SQL

```sql
VARIANCE(<score>)
```

## Exemplos SQL

```sql
SELECT VARIANCE(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
