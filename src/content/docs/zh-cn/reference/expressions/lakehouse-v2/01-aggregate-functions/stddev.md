---
title: STDDEV (Lakehouse v2)
description: STDDEV：返回总体标准差，是 `STDDEV_POP` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev.md
---

返回总体标准差，是 `STDDEV_POP` 的别名。

## Analyze 语法

```python
func.stddev(get_column(table, 'score'))
```

## Analyze 示例

```python
func.stddev(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQL 语法

```sql
STDDEV(<score>)
```

## SQL 示例

```sql
SELECT STDDEV(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
