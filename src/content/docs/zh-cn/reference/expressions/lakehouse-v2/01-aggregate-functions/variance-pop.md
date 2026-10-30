---
title: VARIANCE_POP (Lakehouse v2)
description: VARIANCE_POP：返回总体方差。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-pop.md
---

返回总体方差。

## Analyze 语法

```python
func.variance_pop(get_column(table, 'score'))
```

## Analyze 示例

```python
func.variance_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQL 语法

```sql
VARIANCE_POP(<score>)
```

## SQL 示例

```sql
SELECT VARIANCE_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
