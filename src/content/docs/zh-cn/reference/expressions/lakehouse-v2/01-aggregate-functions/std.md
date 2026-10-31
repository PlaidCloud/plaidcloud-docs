---
title: STD (Lakehouse v2)
description: STD：返回总体标准差，是 `STDDEV_POP` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/std.md
---

返回总体标准差，是 `STDDEV_POP` 的别名。

## Analyze 语法

```python
func.std(get_column(table, 'score'))
```

## Analyze 示例

```python
func.std(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQL 语法

```sql
STD(<score>)
```

## SQL 示例

```sql
SELECT STD(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
