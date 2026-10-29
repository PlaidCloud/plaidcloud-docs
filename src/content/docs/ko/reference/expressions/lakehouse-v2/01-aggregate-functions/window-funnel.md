---
title: WINDOW_FUNNEL (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 WINDOW_FUNNEL 집계 함수를 사용합니다. 시간순으로 정렬된 시퀀스에서 이벤트 체인을 검색하고 최대 체인 길이를 반환합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/window-funnel.md
---

시간순으로 정렬된 시퀀스에서 이벤트 체인을 검색하고 최대 체인 길이를 반환합니다.

## Analyze 구문

```python
func.window_funnel(86400, get_column(table, 'ts'), cond1, cond2)
```

## Analyze 예제

```python
func.window_funnel(86400, get_column(table, 'event_time'), get_column(table, 'step1'), get_column(table, 'step2'))
```

## SQL 구문

```sql
WINDOW_FUNNEL(86400, <ts>, cond1, cond2)
```

## SQL 예제

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
