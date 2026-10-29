---
title: WINDOW_FUNNEL (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 WINDOW_FUNNEL 聚合函数。在按时间排序的序列中搜索事件链，并返回最大链长度。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/window-funnel.md
---

在按时间排序的序列中搜索事件链，并返回最大链长度。

## Analyze 语法

```python
func.window_funnel(86400, get_column(table, 'ts'), cond1, cond2)
```

## Analyze 示例

```python
func.window_funnel(86400, get_column(table, 'event_time'), get_column(table, 'step1'), get_column(table, 'step2'))
```

## SQL 语法

```sql
WINDOW_FUNNEL(86400, <ts>, cond1, cond2)
```

## SQL 示例

```sql
SELECT user_id,
  WINDOW_FUNNEL(86400, event_time,
    event = 'view', event = 'cart', event = 'purchase')
FROM user_events GROUP BY user_id;

┌─────────┬─────────────────┐
│ user_id │ window_funnel    │
├─────────┼─────────────────┤
│       1 │               3 │
│       2 │               2 │
│       3 │               1 │
└─────────┴─────────────────┘
```
