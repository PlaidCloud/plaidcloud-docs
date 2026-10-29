---
title: WINDOW_FUNNEL (Lakehouse v2)
description: "PlaidCloud Lakehouse で WINDOW_FUNNEL 集計関数を使用します。時間順のシーケンスからイベントチェーンを検索し、最大のチェーン長を返します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/window-funnel.md
---

時間順のシーケンスからイベントチェーンを検索し、最大のチェーン長を返します。

## Analyzeの構文

```python
func.window_funnel(86400, get_column(table, 'ts'), cond1, cond2)
```

## Analyzeの例

```python
func.window_funnel(86400, get_column(table, 'event_time'), get_column(table, 'step1'), get_column(table, 'step2'))
```

## SQLの構文

```sql
WINDOW_FUNNEL(86400, <ts>, cond1, cond2)
```

## SQLの例

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
