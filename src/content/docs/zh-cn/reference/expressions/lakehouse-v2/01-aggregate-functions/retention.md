---
title: RETENTION (Lakehouse v2)
description: RETENTION：计算一组事件的留存情况，返回由 0 和 1 组成的数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/retention.md
---

计算一组事件的留存情况，返回由 0 和 1 组成的数组。

## Analyze 语法

```python
func.retention(cond1, cond2)
```

## Analyze 示例

```python
func.retention(get_column(table, 'day1'), get_column(table, 'day2'))
```

## SQL 语法

```sql
RETENTION(cond1, cond2)
```

## SQL 示例

```sql
SELECT uid, RETENTION(dt='2024-01-01', dt='2024-01-02', dt='2024-01-03')
FROM events GROUP BY uid;

┌─────┬────────────┐
│ uid │ retention  │
├─────┼────────────┤
│   1 │ [1,1,0]    │
│   2 │ [1,0,0]    │
│   3 │ [1,1,1]    │
└─────┴────────────┘
```
