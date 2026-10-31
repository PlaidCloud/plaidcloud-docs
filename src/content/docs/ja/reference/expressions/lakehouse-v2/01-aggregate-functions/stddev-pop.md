---
title: STDDEV_POP (Lakehouse v2)
description: STDDEV_POP — 母標準偏差を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-pop.md
---

母標準偏差を返します。

## Analyzeの構文

```python
func.stddev_pop(get_column(table, 'score'))
```

## Analyzeの例

```python
func.stddev_pop(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQLの構文

```sql
STDDEV_POP(<score>)
```

## SQLの例

```sql
SELECT STDDEV_POP(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
