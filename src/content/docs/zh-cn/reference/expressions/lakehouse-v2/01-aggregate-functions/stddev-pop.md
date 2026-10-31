---
title: STDDEV_POP (Lakehouse v2)
description: STDDEV_POP：返回总体标准差。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-pop.md
---

返回总体标准差。

## Analyze 语法

```python
func.stddev_pop(get_column(table, 'score'))
```

## Analyze 示例

```python
func.stddev_pop(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQL 语法

```sql
STDDEV_POP(<score>)
```

## SQL 示例

```sql
SELECT STDDEV_POP(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
