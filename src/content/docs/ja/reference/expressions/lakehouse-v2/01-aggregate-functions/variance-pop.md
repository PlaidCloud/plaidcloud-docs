---
title: VARIANCE_POP (Lakehouse v2)
description: VARIANCE_POP — 母分散を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-pop.md
---

母分散を返します。

## Analyzeの構文

```python
func.variance_pop(get_column(table, 'score'))
```

## Analyzeの例

```python
func.variance_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQLの構文

```sql
VARIANCE_POP(<score>)
```

## SQLの例

```sql
SELECT VARIANCE_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
