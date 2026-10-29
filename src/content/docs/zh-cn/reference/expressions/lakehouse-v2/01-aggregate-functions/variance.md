---
title: VARIANCE (Lakehouse v2)
description: VARIANCE：返回总体方差，是 `VARIANCE_POP` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance.md
---

返回总体方差，是 `VARIANCE_POP` 的别名。

## Analyze 语法

```python
func.variance(get_column(table, 'score'))
```

## Analyze 示例

```python
func.variance(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQL 语法

```sql
VARIANCE(<score>)
```

## SQL 示例

```sql
SELECT VARIANCE(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
